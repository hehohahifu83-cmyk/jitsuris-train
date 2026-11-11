"""G1（海外の確かめの陣）の 1 回だけの測り（2026-11-11 Claude。research/f1/f1_eval.py を写した。予測の前に SHA を事前記録に固定する）。
事前記録：bench/g1_prereg_20261111.md。

  python research/g1/g1_eval.py --labels <ai-bridge>/labels/g1/final.jsonl [--dry]   → research/g1/g1_eval.md・g1_eval_per_column.json

形（製品の形と採点は F1 と同じ。research/f1/f1_eval.py の run_arm。正解が unknown・S・other・person の列は数えない）：
  L+G    ＝ L（D2 run 41192849082 の job2〜4、種子 1〜3）
  L24+G  ＝ L24（run 41735353926 の job1〜3、種子 1〜3）
  L24+G−検査役 ＝ L24+G から検査役 v2 を外した形（読むだけ。research/f1/l24_errors.md の調べ）
主：L24+G が L+G より悪くないか。正しいの差（種子 3 本の平均）の、公開元で引き直す 90% 区間の下限が −1.0 ポイントより上、かつ重大（3 本の合計）が増えない。
読むだけ：各形の正しい・不明・重大・ほかの誤り、カタログ（Alberta・Ontario・Berlin）ごとの正しい、address・org の取り違え。
"""
import argparse
import hashlib
import json
import os
import sys
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
for p in (ROOT, os.path.join(ROOT, "research"), os.path.join(ROOT, "research", "fixes"), os.path.join(ROOT, "independent_eval"), os.path.join(ROOT, "research", "f1")):
    sys.path.insert(0, p)
import d1_eval as D  # noqa: E402
import d2_eval as D2  # noqa: E402
import reserve_eval as R  # noqa: E402
import g1 as G  # noqa: E402
import f1_eval as F1E  # noqa: E402

LABELS_SHA = "606d4d3150c35d9d6e3d7f4f85b32efa8f18369d8ed82f036cdd6dfa5c9bbefa"
SET_SHA = "d96ab7776b4070afcf0b5f8ee23c123ba076636bfcc58688d42d2c14537c409a"
PRED_DIR = os.path.join(ROOT, "independent_eval", "predictions_g1")
SEEDS = (1, 2, 3)
PRED = F1E.PRED   # 同じ名前（pred_l_job2〜4・pred_l24_job1〜3）
CATALOG = {"alberta_cat": "Alberta", "ontario_cat": "Ontario", "berlin_cat": "Berlin"}
NONINF = -1.0


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load_g1(labels_path):
    """G1 の列（g1.json の順）。値は corpus の行の値ぜんぶ。g1.py の select で corpus（g1 → g1x の順につなぐ）の行に戻す。"""
    set_path = os.path.join(ROOT, "independent_eval", "results", "g1", "g1.json")
    if sha(set_path) != SET_SHA:
        raise SystemExit("g1.json が凍結のものと違う")
    if sha(labels_path) != LABELS_SHA:
        raise SystemExit("確定ラベルの SHA が事前記録と違う")
    truth = {d["id"]: d["label"] for d in map(json.loads, open(labels_path, encoding="utf-8"))}
    cols5 = json.load(open(set_path, encoding="utf-8"))["columns"]
    rows = [json.loads(line) for line in open(G.WORK / "corpus.jsonl", encoding="utf-8") if line.strip()]
    extra = G.EXTRA_ADOPTED.parent / "corpus.jsonl"
    rows += [json.loads(line) for line in open(extra, encoding="utf-8") if line.strip()]
    picked, _ = G.select(rows)
    if len(picked) != len(cols5):
        raise SystemExit("corpus の選び直しが g1.json と合わない")
    out = []
    for c, i in zip(cols5, picked):
        r = rows[i]
        if r["header"] != c["header"]:
            raise SystemExit(f"{c['id']}: 列名が corpus と合わない")
        vals = [str(v) for v in (r.get("row_values") or r["values"]) if str(v).strip() not in F1E.JUNK] or [str(v) for v in c["values"]]
        out.append({"batch": "g1", "i": i, "id": c["id"], "table": c["table"], "header": str(c["header"]),
                    "values5": [str(v) for v in c["values"]], "values": vals, "context": [str(x) for x in c.get("siblings") or []],
                    "unit": str(c.get("unit") or ""), "language": c.get("language", ""), "truth": truth[c["id"]], "adjudicated": True,
                    "teacher": truth[c["id"]], "publisher": r["publisher"], "catalog": CATALOG.get(r["publisher"].split(":")[0], "?"),
                    "tab": {"rows": r.get("row_values") or r["values"], "row_index": r.get("row_index"), "total": r.get("datastore_total")}})
    return {"g1": out}


def run_no_verifier(data, mv, labels, fixes, per):
    """eval_fixes.run と同じで、検査役（E.combine）だけを通さない形（読むだけ）。"""
    EF, E, A, V, FX, FI = D.EF, D.EF.E, D.EF.A, D.EF.V, D.EF.FX, D.EF.FI
    n = ok = unk = crit = wrong = 0
    with FX.use(fixes), FI.use(fixes):
        for b, te0 in data.items():
            te = FX.fix_guard(FX.prepare(te0, fixes), fixes)
            P = EF.probs(b, te, mv, labels, "F2" in fixes)
            base = E.base_decisions(te)
            for k, c in enumerate(te):
                if not c["truth"] or c["truth"] in ("unknown", "S", "other", "person"):
                    continue
                f = base[k]
                cand = V.candidate(f[0], f[1], c["pred"], c["top3"], c["header"], P[k], labels, A.RHO)
                lab = cand if cand else f[0]
                if "K" in fixes:
                    lab, _ = EF._dictionary().apply(lab, c["top3"], c["header"], c["values"])
                final = V.amount_cue_veto(lab, c["header"], c.get("unit"), c["values"])
                per[c["id"]] = (final, c["truth"], c["header"], f[1], c["pred"], [str(v) for v in c["values5"][:5]], c.get("unit", ""))
                n += 1
                if final == "unknown":
                    unk += 1
                elif final == c["truth"]:
                    ok += 1
                elif final in V.NUMERIC and c["truth"] in V.NUMERIC:
                    crit += 1
                else:
                    wrong += 1
    return n, ok, unk, crit, wrong


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", required=True)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args(argv)
    f, dsha = R.DICTS["K"]
    if sha(os.path.join(ROOT, "materials", "dictionary", f)) != dsha:
        raise SystemExit("辞書が凍結したものと違う")
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", f)
    D.EF._DICT.clear()
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = load_g1(a.labels)
    cols = {c["id"]: c for c in base["g1"]}
    res, per, raw = {}, {}, {}
    for model in ("L", "L24"):
        for s in SEEDS:
            data = D.with_job(base, os.path.join(PRED_DIR, PRED[model][s]))
            D.EF._PCACHE.clear()
            p = {}
            res[f"{model}+G{s}"] = D.EF.run(data, mv, labels, D.PRODUCT + ("K",), per=p)
            raw[f"{model}+G{s}"] = p
            per[f"{model}+G{s}"] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}
            if model == "L24":
                D.EF._PCACHE.clear()
                q = {}
                res[f"L24+G-V{s}"] = run_no_verifier(data, mv, labels, D.PRODUCT + ("K",), q)
                raw[f"L24+G-V{s}"] = q
                per[f"L24+G-V{s}"] = {k: D.outcome(v[0], v[1]) for k, v in q.items()}
    if len({r[0] for r in res.values()}) != 1:
        raise SystemExit("採点列の数が形で違う")
    n = res["L+G1"][0]
    by_pub = {k: cols[k]["publisher"] for k in per["L+G1"]}
    v = F1E.judge(per, res, "L+G", "L24+G", by_pub)
    ok_main = v["lo"] > NONINF and v["d_crit"] <= 0
    vv = F1E.judge(per, res, "L24+G", "L24+G-V", by_pub)
    mk = lambda b: "○" if b else "×"  # noqa: E731
    L = ["# G1 の 1 回だけの測り（`research/g1/g1_eval.py`）", "",
         f"- 事前記録 `bench/g1_prereg_20261111.md`。採点 {n} 列（正解が unknown・S・other・person の列を除く）。",
         f"- 正解：先生 2 人（Claude・Codex）の独立のラベル（互いに SHA だけを連絡）の裁定。SHA-256 {LABELS_SHA}。",
         "- G1 は Alberta・Ontario・Berlin の 3 カタログだけ（英語・ドイツ語）。", "",
         "| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |", "|---|---:|---:|---:|---:|---|"]
    for arm in ("L+G", "L24+G", "L24+G-V"):
        m = F1E.mean_of(res, arm)
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | " + "・".join(str(res[f'{arm}{s}'][1]) for s in SEEDS) + " |")
    L += ["", "## 主：L24+G は L+G より悪くないか（公開元で引き直す）", "",
          f"- 正しいの差 {v['d_ok']:+.2f}、90% 区間 {v['lo']:+.2f}〜{v['hi']:+.2f}（下限が {NONINF:+.1f} より上か：{mk(v['lo'] > NONINF)}）",
          f"- 重大の差 {v['d_crit']:+d}（増えないか：{mk(v['d_crit'] <= 0)}）", f"- ほかの誤りの差 {v['d_wrong']:+.2f}（読むだけ）",
          f"- **判定：{'悪くない（L24 を土台のままにする）' if ok_main else '悪くないと言えない（原因を突き止める）'}**", "",
          "## 読むだけ：検査役を外した形（L24+G-V 対 L24+G）", "",
          f"- 正しいの差 {vv['d_ok']:+.2f}、90% 区間 {vv['lo']:+.2f}〜{vv['hi']:+.2f}、重大の差 {vv['d_crit']:+d}、ほかの誤りの差 {vv['d_wrong']:+.2f}",
          "", "## 読むだけ：カタログごと", "", "| 形 | Alberta | Ontario | Berlin | address→org | org→address |", "|---|---:|---:|---:|---:|---:|"]
    for arm in ("L+G", "L24+G", "L24+G-V"):
        cells = []
        for cat in ("Alberta", "Ontario", "Berlin"):
            ks = [k for k in per["L+G1"] if cols[k]["catalog"] == cat]
            cells.append(f"{100 * sum(per[f'{arm}{s}'][k] == 'ok' for s in SEEDS for k in ks) / (3 * len(ks)):.1f}%（{len(ks)}）" if ks else "—")
        ao = sum(raw[f"{arm}{s}"][k][1] == "address" and raw[f"{arm}{s}"][k][0] == "org" for s in SEEDS for k in raw[f"{arm}{s}"]) / 3
        oa = sum(raw[f"{arm}{s}"][k][1] == "org" and raw[f"{arm}{s}"][k][0] == "address" for s in SEEDS for k in raw[f"{arm}{s}"]) / 3
        L.append(f"| {arm} | " + " | ".join(cells) + f" | {ao:.1f} | {oa:.1f} |")
    L += ["", "### 公開元ごとの正しい（3 本の平均）", "", "| 公開元 | 列 | L+G | L24+G |", "|---|---:|---:|---:|"]
    pubs = defaultdict(list)
    for k in per["L+G1"]:
        pubs[cols[k]["publisher"]].append(k)
    for pb, ks in sorted(pubs.items(), key=lambda x: -len(x[1])):
        fr = lambda arm: 100 * sum(per[f"{arm}{s}"][k] == "ok" for s in SEEDS for k in ks) / (3 * len(ks))  # noqa: E731
        L.append(f"| {pb} | {len(ks)} | {fr('L+G'):.1f}% | {fr('L24+G'):.1f}% |")
    text = "\n".join(L) + "\n"
    print(text)
    if a.dry:
        return
    open(os.path.join(HERE, "g1_eval.md"), "w", encoding="utf-8").write(text)
    json.dump(per, open(os.path.join(HERE, "g1_eval_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)


if __name__ == "__main__":
    main()
