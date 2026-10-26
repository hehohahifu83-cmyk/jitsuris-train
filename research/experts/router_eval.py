"""使い分けの手順書 v0（research/router-procedure.md）を測る（2026-10-26 Claude。事前記録 bench/hard_model_router_20261026.md）。

本体＝C2（pred_c2_seed1.json）、苦手克服モデル H（research/experts/preds/hard_job1_<陣>.json）、検査役 v2（b001〜b014 で学ぶ）。
形：(0) 今の製品の形、(0') rho なし、(1) 手順書 v0（rho なし）、(2) 手順書 v0＋rho。T_H を {0.7,0.8,0.9,0.95,0.98} で測る
使い方：python research/experts/router_eval.py --batches b015 b016 [--out 結果.md]
"""
import argparse
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from verifier_c1 import TAU  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402

NUM = set(V.NUMERIC)
TS = (0.7, 0.8, 0.9, 0.95, 0.98)
TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))
HARD_PREFIX = "hard_job1"   # --hard で変える（交差検証の全部の教材の H は hcv_job6）


def hard_preds(batches):
    out = {}
    for b in batches:
        for r in json.load(open(os.path.join(ROOT, "research", "experts", "preds", f"{HARD_PREFIX}_{b}.json"), encoding="utf-8"))["rows"]:
            out[r["id"]] = (r["guarded_prediction"], r["top3"])
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--batches", nargs="+", default=["b015", "b016"])
    ap.add_argument("--out", default=None)
    ap.add_argument("--hard", default="hard_job1")
    a = ap.parse_args(argv)
    global HARD_PREFIX
    HARD_PREFIX = a.hard
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])
    te = []
    for b in a.batches:
        cs, _ = with_pred(E.load_batch(b), os.path.join(ROOT, "materials", "pool", "work", b, "pred_c2_seed1.json"))
        te += cs
    P = np.zeros((len(te), len(labels)), dtype="float32")
    p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
    for j, lab in enumerate(mv.classes_):
        P[:, labels.index(lab)] = p[:, j]
    base = E.base_decisions(te)
    idx = list(range(len(te)))
    fin = E.combine(base, P, np.zeros(len(te)), labels, TAU, None, idx)
    no_rho = [fin[k] for k in idx]

    def with_rho(decs):
        out = []
        for k, d in enumerate(decs):
            c = V.candidate(d[0], d[1], te[k]["pred"], te[k]["top3"], te[k]["header"], P[k], labels, 0.7)
            out.append((c, "assert") if c else d)
        return out

    H = hard_preds(a.batches)

    def router(T):
        out, back, down = [], 0, 0
        for k, d in enumerate(no_rho):
            hl, ht = H[te[k]["id"]]
            hp = (ht or [{}])[0].get("probability", 0)
            top3 = [t["label"] for t in (te[k]["top3"] or [])][:3]
            if d[0] == "unknown" and hl != "unknown" and hp >= T and hl in top3:
                if hl in NUM and P[k][labels.index(hl)] < TAU:
                    out.append(d)
                else:
                    out.append((hl, "hard_model")); back += 1
                continue
            if d[0] in NUM and hl in NUM and hl != d[0] and hp >= T:
                out.append(("unknown", "hard_model_check")); down += 1
                continue
            out.append(d)
        return out, back, down

    def row(name, decs, back=0, down=0):
        s = E.score([d[0] for d in decs], te)
        return f"| {name} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} | {back} | {down} |", s

    L = [f"## 手順書 v0 の結果（{'・'.join(a.batches)}、`research/experts/router_eval.py`）", "", "| 形 | 結果 | 不明 | 重大 | H で言い切り | H で不明に |", "|---|---|---:|---:|---:|---:|"]
    r0, s0 = row("(0) 今の製品の形（rho 0.7）", with_rho(no_rho))
    L.append(r0)
    L.append(row("(0') rho なし", no_rho)[0])
    picks = []
    for T in TS:
        dec, bk, dn = router(T)
        r1, s1 = row(f"(1) 手順書 v0 T_H={T}", dec, bk, dn)
        L.append(r1)
        L.append(row(f"(2) 手順書 v0＋rho T_H={T}", with_rho(dec), bk, dn)[0])
        if s1["critical"] <= 0.002 * s1["n"] and s1["correct"] >= s0["correct"]:
            picks.append(T)
    # H 単独（見張り後）
    sh = E.score([H[c["id"]][0] for c in te], te)
    L += ["", f"- H 単独（見張り後）：{E.fmt(sh)}", f"- 線の決まり（重大 ≤ 0.2% かつ正解率 ≥ (0)）を満たす T_H：{picks or 'なし'} → 選ぶのは一番低い値：{min(picks) if picks else 'なし'}"]
    print("\n".join(L))
    if a.out:
        with open(a.out, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    main()
