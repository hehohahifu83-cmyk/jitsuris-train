"""融合の試し：C1 ＋ λ ×（候補 − e5-base）を作り、C1 が見ていない陣（b013・b014）で C1 そのままと比べる（2026-10-25 Claude。学習なし・CPU）。

オーナー指示「今のジツリスの弱点に特攻を持つモデルで融合できるものを探し出せ」→「やれ」。候補と理由は research/merge/FINDINGS.md。
- 混ぜるのは本体（roberta.*）だけ。分類の頭（classifier.*）は C1 のまま。候補の頭は捨てる
- 測る陣の正解は混ぜ方に使わない。λ は 0.2・0.5 を先に決めて両方出す（ここでは選ばない）
- 判定は C1 そのままと同じ道具（見張り → recheck v1 → 検査役 v2（b001〜b012 で学ぶ）→ rho_assert 0.7）
- 封印セット・固定試験は使わない

使い方：
  python research/merge/merge_eval.py merge --c1 DIR --base DIR --cand DIR [--cand-file kA/model.pt] --lam 0.2 --tag pii02 --out DIR
  python research/merge/merge_eval.py score --tags c1 pii02 ... --out research/merge/RESULTS.md
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
PRED = os.path.join(ROOT, "research", "merge", "preds")
TEST = ("b013", "b014")
RHO = 0.7


def strip(k):
    for p in ("roberta.", "model.", "0.auto_model."):
        if k.startswith(p):
            k = k[len(p):]
    return k


def load_state(d, file=None):
    """重み（safetensors、なければ .bin／.pt を weights_only で）→ {名前（roberta. などを外す）: 値}。"""
    import torch
    from safetensors.torch import load_file
    if file:
        paths = [os.path.join(d, file)]
    else:
        paths = sorted(glob.glob(os.path.join(d, "*.safetensors"))) or sorted(glob.glob(os.path.join(d, "pytorch_model*.bin")))
    if not paths:
        raise SystemExit(f"重みが無い：{d}")
    sd = {}
    for p in paths:
        part = load_file(p) if p.endswith(".safetensors") else torch.load(p, map_location="cpu", weights_only=True)
        if isinstance(part, dict) and "state_dict" in part and isinstance(part["state_dict"], dict):
            part = part["state_dict"]
        sd.update(part)
    return {strip(k): v for k, v in sd.items()}


def merge(a):
    from safetensors.torch import load_file, save_file
    manifest = json.load(open(os.path.join(a.c1, "manifest.json"), encoding="utf-8"))
    wname = next(iter(manifest["saved_model"]["weights"]))
    c1 = load_file(os.path.join(a.c1, wname))
    base, cand = load_state(a.base), load_state(a.cand, a.cand_file)
    out, used, skipped = {}, 0, []
    enc = [k for k in c1 if not k.startswith("classifier.")]
    for k, v in c1.items():
        s = strip(k)
        if k.startswith("classifier.") or not v.is_floating_point():
            out[k] = v
            continue
        if s in base and s in cand and base[s].shape == v.shape == cand[s].shape:
            out[k] = (v.float() + a.lam * (cand[s].float() - base[s].float())).to(v.dtype).contiguous()
            used += 1
        else:
            out[k] = v
            skipped.append(k)
    share = used / max(1, len([k for k in enc if c1[k].is_floating_point()]))
    print(f"{a.tag}: merged {used} tensors ({share:.1%}), kept {len(skipped)}: {skipped[:8]}", flush=True)
    if share < 0.95:
        raise SystemExit(f"{a.tag}: 合う重みが少ない（{share:.1%}）。系列が違う候補は混ぜない")
    if os.path.exists(a.out):
        shutil.rmtree(a.out)
    shutil.copytree(a.c1, a.out)
    save_file(out, os.path.join(a.out, wname), metadata={"format": "pt"})
    digest = hashlib.sha256(open(os.path.join(a.out, wname), "rb").read()).hexdigest()
    manifest["saved_model"]["weights"][wname]["sha256"] = digest
    manifest.setdefault("extra", {})["merge"] = {"c1_weights_sha256": json.load(open(os.path.join(a.c1, "manifest.json")))["saved_model"]["weights"][wname]["sha256"],
                                                "candidate": a.cand_repo, "candidate_revision": a.cand_rev, "candidate_file": a.cand_file,
                                                "lam": a.lam, "merged_tensors": used, "kept_tensors": skipped}
    json.dump(manifest, open(os.path.join(a.out, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{a.tag}: weights {digest}", flush=True)


def soup(a):
    """種子違いの C1（同じ e5-base から同じ設定で微調整）の重みを、分類の頭も含めて平均する（model soup）。"""
    from safetensors.torch import load_file, save_file
    mans = [json.load(open(os.path.join(d, "manifest.json"), encoding="utf-8")) for d in a.dirs]
    names = [next(iter(m["saved_model"]["weights"])) for m in mans]
    sds = [load_file(os.path.join(d, n)) for d, n in zip(a.dirs, names)]
    labels = [json.load(open(os.path.join(d, "labels.json"), encoding="utf-8")) for d in a.dirs]
    if any(l != labels[0] for l in labels) or any(set(sd) != set(sds[0]) for sd in sds):
        raise SystemExit("種子の重みの形・ラベルの並びが違う")
    out = {k: (sum(sd[k].float() for sd in sds) / len(sds)).to(v.dtype).contiguous() if v.is_floating_point() else v for k, v in sds[0].items()}
    if os.path.exists(a.out):
        shutil.rmtree(a.out)
    shutil.copytree(a.dirs[0], a.out)
    save_file(out, os.path.join(a.out, names[0]), metadata={"format": "pt"})
    digest = hashlib.sha256(open(os.path.join(a.out, names[0]), "rb").read()).hexdigest()
    m = mans[0]
    m["saved_model"]["weights"][names[0]]["sha256"] = digest
    m.setdefault("extra", {})["soup"] = {"members": [mm["saved_model"]["weights"][n]["sha256"] for mm, n in zip(mans, names)]}
    json.dump(m, open(os.path.join(a.out, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"soup of {len(sds)}: weights {digest}", flush=True)


def with_pred(cols, path):
    pred = json.load(open(path, encoding="utf-8"))
    by = {r["id"]: r for r in pred["rows"]}
    for c in cols:
        r = by[c["id"]]
        c["pred"], c["top3"] = r["guarded_prediction"], r["top3"]
    return cols, pred.get("checkpoint", {}).get("weights_sha256", "")


def score(a):
    """検査役 v2 を b001〜b012 で 1 回だけ学び、各 tag の予測に同じ判定を重ねる（verifier_c1.py と同じ手順）。"""
    import numpy as np
    import pool_bench as B
    import verifier as V
    import verifier_eval as E
    from verifier_c1 import TAU
    labels = list(V.LABELS)
    train_b = [b for b in E.BATCHES if b not in TEST]
    tr = [c for b in train_b for c in E.load_batch(b)]
    Xtr = np.hstack([V.matrix([c["values"] for c in tr]), E.table_matrix(tr)])
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in tr])
    y = np.array([c["truth"] if o else "" for c, o in zip(tr, ok)])
    mv, _, _ = E.fit(Xtr[ok], y[ok])
    meta = {t: json.load(open(os.path.join(PRED, f"{t}_meta.json"), encoding="utf-8")) for t in a.tags if os.path.exists(os.path.join(PRED, f"{t}_meta.json"))}
    L = [a.title or "# 融合の試し：C1 ＋ λ ×（候補 − e5-base）を b013・b014 で比べる（2026-10-25 Claude。`research/merge/merge_eval.py`）", "",
         "- C1 はこの 2 陣を学習していない。検査役 v2 は b001〜b012 で学んだ（測る陣の正解は見ない）。tau＝0.05、rho_assert＝0.7（先に固定した値）",
         "- 候補と理由：`research/merge/FINDINGS.md`。λ は 0.2・0.5 を先に決めた。**ここの数字は開発用**（封印セットではない）", "",
         "| 本体 | 見張りだけ | ＋ recheck v1 ＋ 検査役 v2 ＋ rho 0.7（製品の形） | 不明 | 重大 |", "|---|---|---|---:|---:|"]
    for t in a.tags:
        te = []
        for b in TEST:
            cs, _ = with_pred(E.load_batch(b), os.path.join(PRED, f"{t}_{b}.json"))
            te += cs
        base_te = E.base_decisions(te)
        Xte = np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)])
        Pte = np.zeros((len(te), len(labels)), dtype="float32")
        p = mv.predict_proba(Xte)
        for j, c in enumerate(mv.classes_):
            Pte[:, labels.index(c)] = p[:, j]
        idx = list(range(len(te)))
        fin = E.combine(base_te, Pte, np.zeros(len(te)), labels, TAU, None, idx)
        f2 = []
        for k in idx:
            d = fin[k]
            c = V.candidate(d[0], d[1], te[k]["pred"], te[k]["top3"], te[k]["header"], Pte[k], labels, RHO)
            f2.append((c, "assert") if c else d)
        s1, s2 = E.score([c["pred"] for c in te], te), E.score([d[0] for d in f2], te)
        m = meta.get(t, {})
        name = "C1 そのまま" if t == "c1" else m.get("name") or f"{m.get('candidate', t)} λ={m.get('lam', '?')}"
        L.append(f"| {name} | {E.fmt(s1)} | {E.fmt(s2)} | {s2['unknown'] / s2['n']:.1%} | {s2['critical'] / s2['n']:.2%} |")
        print(t, E.fmt(s1), "|", E.fmt(s2), flush=True)
    L += ["", "- 「良い」の目安（FINDINGS.md）：重大が増えず、正解率 +1.0 ポイント以上。採否は b015 で確かめてから"]
    open(a.out, "w", encoding="utf-8").write("\n".join(L) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    m = sp.add_parser("merge")
    m.add_argument("--c1", required=True); m.add_argument("--base", required=True); m.add_argument("--cand", required=True)
    m.add_argument("--cand-file", default=None); m.add_argument("--cand-repo", default=""); m.add_argument("--cand-rev", default="")
    m.add_argument("--lam", type=float, required=True); m.add_argument("--tag", required=True); m.add_argument("--out", required=True)
    u = sp.add_parser("soup")
    u.add_argument("--dirs", nargs="+", required=True); u.add_argument("--out", required=True)
    s = sp.add_parser("score")
    s.add_argument("--tags", nargs="+", required=True); s.add_argument("--out", required=True)
    s.add_argument("--title", default=None)
    a = ap.parse_args(argv)
    {"merge": merge, "soup": soup, "score": score}[a.cmd](a)


if __name__ == "__main__":
    main()
