"""G2（2 つ目の海外の陣）の 1 回だけの測り：直し M（2026-11-12 Claude。予測の前に SHA を事前記録に固定する）。
事前記録：bench/fixm_prereg_20261112.md。

  python research/g2/g2_eval.py --labels <ai-bridge>/labels/g2/final.jsonl [--dry]   → research/g2/g2_eval.md・g2_eval_per_column.json

形（製品の形と採点は F1・G1 と同じ。正解が unknown・S・other・person の列は数えない）：
  L24+G    ＝ L24（run 41735353926 の job1〜3、種子 1〜3）
  L24+G+M  ＝ L24+G の再確認（recheck.cue_types）に直し M（research/guard_dates/fix_m.py の extra_cues）を足した形
  L+G      ＝ L（読むだけ。L24 が海外でも悪くないかの 2 回目）
主：L24+G 対 L24+G+M を決まり 1〜4（表で引き直す）で。採点の環境は scikit-learn 1.8.0・NumPy 2.3.5・SciPy 1.17.0（違えば止まる）。
"""
import argparse
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
for p in (ROOT, os.path.join(ROOT, "research"), os.path.join(ROOT, "research", "fixes"), os.path.join(ROOT, "independent_eval"),
          os.path.join(ROOT, "research", "f1"), os.path.join(ROOT, "research", "guard_dates")):
    sys.path.insert(0, p)
import d1_eval as D  # noqa: E402
import reserve_eval as R  # noqa: E402
import g2 as G  # noqa: E402
import f1_eval as F1E  # noqa: E402
import recheck as RC  # noqa: E402
import fix_m as FM  # noqa: E402
import sklearn  # noqa: E402
import scipy  # noqa: E402

LABELS_SHA = "b734c0d32b98e0259625419d7692ff77c403acad8ef7be8b203c9dde25690c04"
SET_SHA = "83b708061d2f185917e1b25918070e5a285ca07797bd8b64aa4e55c4e19aa68b"
FIXM_SHA = "fc4c25eb2e4d70c91854c7ff5a80e93e8e1aa15310eaabf8cf2769853a021e9a"
ENV = {"sklearn": "1.8.0", "numpy": "2.3.5", "scipy": "1.17.0"}
PRED_DIR = os.path.join(ROOT, "independent_eval", "predictions_g2")
SEEDS = (1, 2, 3)
PRED = F1E.PRED


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load_g2(labels_path):
    set_path = os.path.join(ROOT, "independent_eval", "results", "g2", "g2.json")
    if sha(set_path) != SET_SHA:
        raise SystemExit("g2.json が凍結のものと違う")
    if sha(labels_path) != LABELS_SHA:
        raise SystemExit("確定ラベルの SHA が事前記録と違う")
    truth = {d["id"]: d["label"] for d in map(json.loads, open(labels_path, encoding="utf-8"))}
    cols5 = json.load(open(set_path, encoding="utf-8"))["columns"]
    rows = [json.loads(line) for line in open(G.WORK / "corpus.jsonl", encoding="utf-8") if line.strip()]
    extra = G.EXTRA_ADOPTED.parent / "corpus.jsonl"
    if extra.exists():
        rows += [json.loads(line) for line in open(extra, encoding="utf-8") if line.strip()]
    picked, _ = G.select(rows)
    if len(picked) != len(cols5):
        raise SystemExit("corpus の選び直しが g2.json と合わない")
    out = []
    for c, i in zip(cols5, picked):
        r = rows[i]
        if r["header"] != c["header"]:
            raise SystemExit(f"{c['id']}: 列名が corpus と合わない")
        vals = [str(v) for v in (r.get("row_values") or r["values"]) if str(v).strip() not in F1E.JUNK] or [str(v) for v in c["values"]]
        out.append({"batch": "g2", "i": i, "id": c["id"], "table": c["table"], "header": str(c["header"]),
                    "values5": [str(v) for v in c["values"]], "values": vals, "context": [str(x) for x in c.get("siblings") or []],
                    "unit": str(c.get("unit") or ""), "language": c.get("language", ""), "truth": truth[c["id"]], "adjudicated": True,
                    "teacher": truth[c["id"]], "publisher": r["publisher"],
                    "tab": {"rows": r.get("row_values") or r["values"], "row_index": r.get("row_index"), "total": r.get("datastore_total")}})
    return {"g2": out}


def run(base, mv, labels, model, s, with_m):
    data = D.with_job(base, os.path.join(PRED_DIR, PRED[model][s]))
    orig = RC.cue_types
    if with_m:
        RC.cue_types = lambda h, u="": orig(h, u) | FM.extra_cues(h, u)
    try:
        D.EF._PCACHE.clear()
        p = {}
        res = D.EF.run(data, mv, labels, D.PRODUCT + ("K",), per=p)
    finally:
        RC.cue_types = orig
    return res, p


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", required=True)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args(argv)
    got = {"sklearn": sklearn.__version__, "numpy": np.__version__, "scipy": scipy.__version__}
    if got != ENV:
        raise SystemExit(f"採点の環境が事前記録と違う：{got}")
    if sha(os.path.join(ROOT, "research", "guard_dates", "fix_m.py")) != FIXM_SHA:
        raise SystemExit("fix_m.py が事前記録の SHA と違う")
    f, dsha = R.DICTS["K"]
    if sha(os.path.join(ROOT, "materials", "dictionary", f)) != dsha:
        raise SystemExit("辞書が凍結したものと違う")
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", f)
    D.EF._DICT.clear()
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = load_g2(a.labels)
    cols = {c["id"]: c for c in base["g2"]}
    res, per, raw = {}, {}, {}
    for arm, model, m in (("L24+G", "L24", False), ("L24+G+M", "L24", True), ("L+G", "L", False)):
        for s in SEEDS:
            r, p = run(base, mv, labels, model, s, m)
            res[f"{arm}{s}"], raw[f"{arm}{s}"] = r, p
            per[f"{arm}{s}"] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}
    if len({r[0] for r in res.values()}) != 1:
        raise SystemExit("採点列の数が形で違う")
    n = res["L24+G1"][0]
    by_tab = {k: cols[k]["table"] for k in per["L24+G1"]}
    by_pub = {k: cols[k]["publisher"] for k in per["L24+G1"]}
    vm = F1E.judge(per, res, "L24+G", "L24+G+M", by_tab)
    vl = F1E.judge(per, res, "L+G", "L24+G", by_pub)
    mk = lambda b: "○" if b else "×"  # noqa: E731
    L = ["# G2 の 1 回だけの測り：直し M（`research/g2/g2_eval.py`）", "",
         f"- 事前記録 `bench/fixm_prereg_20261112.md`。採点 {n} 列（正解が unknown・S・other・person の列を除く）。環境 {got}。",
         f"- 正解：先生 2 人の独立のラベル（互いに SHA だけを連絡）の裁定。SHA-256 {LABELS_SHA}。G2 は GovData.de（ドイツ）だけ。",
         "", "| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |", "|---|---:|---:|---:|---:|---|"]
    for arm in ("L+G", "L24+G", "L24+G+M"):
        m = F1E.mean_of(res, arm)
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | " + "・".join(str(res[f'{arm}{s}'][1]) for s in SEEDS) + " |")
    L += ["", "## 主：直し M（L24+G+M 対 L24+G、表で引き直す）", "",
          f"- 1. 正しい {vm['d_ok']:+.2f} {mk(vm['checks'][0])}", f"- 2. 重大 {vm['d_crit']:+d} {mk(vm['checks'][1])}",
          f"- 3. ほかの誤り {vm['d_wrong']:+.2f} {mk(vm['checks'][2])}", f"- 4. 90% 区間 {vm['lo']:+.2f}〜{vm['hi']:+.2f} {mk(vm['checks'][3])}",
          f"- **判定：{'確かめられた（採る）' if vm['adopt'] else '確かめられなかった'}**", "",
          "## 読むだけ：L24+G 対 L+G（公開元で引き直す）", "",
          f"- 正しいの差 {vl['d_ok']:+.2f}、90% 区間 {vl['lo']:+.2f}〜{vl['hi']:+.2f}、重大の差 {vl['d_crit']:+d}", "",
          "## 読むだけ：正解の種類ごとの不明（L24+G → L24+G+M、3 本の合計）", "", "| 正解 | 列 | 不明 L24+G | 不明 +M | 正しい L24+G | 正しい +M |", "|---|---:|---:|---:|---:|---:|"]
    kinds = defaultdict(list)
    for k in per["L24+G1"]:
        kinds[cols[k]["truth"]].append(k)
    for t, ks in sorted(kinds.items(), key=lambda x: -len(x[1])):
        c = lambda arm, o: sum(per[f"{arm}{s}"][k] == o for s in SEEDS for k in ks)  # noqa: E731
        L.append(f"| {t} | {len(ks)} | {c('L24+G', 'unk')} | {c('L24+G+M', 'unk')} | {c('L24+G', 'ok')} | {c('L24+G+M', 'ok')} |")
    L += ["", "## 直し M が変えた列（3 本）", "", "| 本 | id | 列名 | 正解 | L24+G | +M |", "|---|---|---|---|---|---|"]
    for s in SEEDS:
        x, y = raw[f"L24+G{s}"], raw[f"L24+G+M{s}"]
        for k in sorted(x):
            if x[k][0] != y[k][0]:
                L.append(f"| {s} | {k} | {str(x[k][2])[:35]} | {x[k][1]} | {x[k][0]} | {y[k][0]} |")
    text = "\n".join(L) + "\n"
    print(text)
    if a.dry:
        return
    open(os.path.join(HERE, "g2_eval.md"), "w", encoding="utf-8").write(text)
    json.dump(per, open(os.path.join(HERE, "g2_eval_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)


if __name__ == "__main__":
    main()
