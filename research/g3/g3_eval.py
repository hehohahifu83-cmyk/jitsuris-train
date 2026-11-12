"""G3（金額・単位の列が多い海外の陣）の 1 回だけの測り：直し M と銀教材（L24S）（2026-11-13 Claude。予測の前に SHA を事前記録に固定する）。
事前記録：bench/fixm_prereg_20261112.md（M）・bench/silver24_prereg_20261113.md（銀）。

  python research/g3/g3_eval.py --labels <ai-bridge>/labels/g3/final.jsonl [--dry]   → research/g3/g3_eval.md・g3_eval_per_column.json

形（製品の形と採点は F1・G1・G2 と同じ。正解が unknown・S・other・person の列は数えない）：
  L24+G      ＝ L24（run 41735353926 の job1〜3、種子 1〜3）
  L24+G+M    ＝ L24+G の再確認（recheck.cue_types）に直し M（research/guard_dates/fix_m.py の extra_cues）を足した形
  L24S+G     ＝ L24S（run 43266270727 の job1〜3、L24 の設定＋FT_SILVER=train_A、種子 1〜3）
  L24+G+R    ＝ L24+G に rho の金額の守り（research/silver/rho_amount_guard.py）を入れた形（読むだけ）
  L24S+G+R   ＝ L24S+G に同じ守り（読むだけ）
  L+G        ＝ L（読むだけ）
主 1（M）：L24+G 対 L24+G+M を決まり 1〜4（表で引き直す）。満たしても「仮に採る」（事前記録 2026-11-13 00:10 の追記）。
主 2（銀）：L24+G 対 L24S+G を決まり 1〜4（公開元で引き直す）。
採点の環境は Python 3.12・scikit-learn 1.8.0・NumPy 2.3.5・SciPy 1.17.0（違えば止まる）。
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
for p in (ROOT, os.path.join(ROOT, "research"), os.path.join(ROOT, "research", "fixes"), os.path.join(ROOT, "independent_eval"),
          os.path.join(ROOT, "research", "f1"), os.path.join(ROOT, "research", "guard_dates"), os.path.join(ROOT, "research", "silver")):
    sys.path.insert(0, p)
import d1_eval as D  # noqa: E402
import reserve_eval as R  # noqa: E402
import g3 as G  # noqa: E402
import f1_eval as F1E  # noqa: E402
import recheck as RC  # noqa: E402
import fix_m as FM  # noqa: E402
import rho_amount_guard as RG  # noqa: E402
import sklearn  # noqa: E402
import scipy  # noqa: E402

LABELS_SHA = "1162b62032d580e59345f0ca44ed588d1e8d05a707fb0453d54adb380994bbeb"
SET_SHA = "41bb6c1832c0e6659c0b56766253769fd303564499a93e5c98c7c97676d3051a"
FIXM_SHA = "fc4c25eb2e4d70c91854c7ff5a80e93e8e1aa15310eaabf8cf2769853a021e9a"
GUARD_SHA = "68610f8e7fce92e26b3862c421efc93ed2b82eb414c20473090821329d4e956c"
ENV = {"python": "3.12", "sklearn": "1.8.0", "numpy": "2.3.5", "scipy": "1.17.0"}
PRED_DIR = os.path.join(ROOT, "independent_eval", "predictions_g3")
SEEDS = (1, 2, 3)
PRED = {"L": {1: "pred_l_job2.json", 2: "pred_l_job3.json", 3: "pred_l_job4.json"},
        "L24": {1: "pred_l24_job1.json", 2: "pred_l24_job2.json", 3: "pred_l24_job3.json"},
        "L24S": {1: "pred_l24s_job1.json", 2: "pred_l24s_job2.json", 3: "pred_l24s_job3.json"}}
# 形：名前 → (重み, 直し M, rho の守り)
ARMS = {"L+G": ("L", False, False), "L24+G": ("L24", False, False), "L24+G+M": ("L24", True, False),
        "L24S+G": ("L24S", False, False), "L24+G+R": ("L24", False, True), "L24S+G+R": ("L24S", False, True)}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load_g3(labels_path):
    set_path = os.path.join(ROOT, "independent_eval", "results", "g3", "g3.json")
    if sha(set_path) != SET_SHA:
        raise SystemExit("g3.json が凍結のものと違う")
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
        raise SystemExit("corpus の選び直しが g3.json と合わない")
    out = []
    for c, i in zip(cols5, picked):
        r = rows[i]
        if r["header"] != c["header"]:
            raise SystemExit(f"{c['id']}: 列名が corpus と合わない")
        vals = [str(v) for v in (r.get("row_values") or r["values"]) if str(v).strip() not in F1E.JUNK] or [str(v) for v in c["values"]]
        out.append({"batch": "g3", "i": i, "id": c["id"], "table": c["table"], "header": str(c["header"]),
                    "values5": [str(v) for v in c["values"]], "values": vals, "context": [str(x) for x in c.get("siblings") or []],
                    "unit": str(c.get("unit") or ""), "language": c.get("language", ""), "truth": truth[c["id"]], "adjudicated": True,
                    "teacher": truth[c["id"]], "publisher": r["publisher"],
                    "tab": {"rows": r.get("row_values") or r["values"], "row_index": r.get("row_index"), "total": r.get("datastore_total")}})
    return {"g3": out}


class _Nothing:
    def __enter__(self):
        return None

    def __exit__(self, *a):
        return False


def run(base, mv, labels, model, s, with_m, with_guard):
    data = D.with_job(base, os.path.join(PRED_DIR, PRED[model][s]))
    orig = RC.cue_types
    if with_m:
        RC.cue_types = lambda h, u="": orig(h, u) | FM.extra_cues(h, u)
    try:
        with (RG.use() if with_guard else _Nothing()):
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
    got = {"python": "%d.%d" % sys.version_info[:2], "sklearn": sklearn.__version__, "numpy": np.__version__, "scipy": scipy.__version__}
    if got != ENV:
        raise SystemExit(f"採点の環境が事前記録と違う：{got}")
    if sha(os.path.join(ROOT, "research", "guard_dates", "fix_m.py")) != FIXM_SHA:
        raise SystemExit("fix_m.py が事前記録の SHA と違う")
    if sha(os.path.join(ROOT, "research", "silver", "rho_amount_guard.py")) != GUARD_SHA:
        raise SystemExit("rho_amount_guard.py が事前記録の SHA と違う")
    f, dsha = R.DICTS["K"]
    if sha(os.path.join(ROOT, "materials", "dictionary", f)) != dsha:
        raise SystemExit("辞書が凍結したものと違う")
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", f)
    D.EF._DICT.clear()
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = load_g3(a.labels)
    cols = {c["id"]: c for c in base["g3"]}
    res, per, raw = {}, {}, {}
    for arm, (model, m, g) in ARMS.items():
        for s in SEEDS:
            r, p = run(base, mv, labels, model, s, m, g)
            res[f"{arm}{s}"], raw[f"{arm}{s}"] = r, p
            per[f"{arm}{s}"] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}
    if len({r[0] for r in res.values()}) != 1:
        raise SystemExit("採点列の数が形で違う")
    n = res["L24+G1"][0]
    by_tab = {k: cols[k]["table"] for k in per["L24+G1"]}
    by_pub = {k: cols[k]["publisher"] for k in per["L24+G1"]}
    vm = F1E.judge(per, res, "L24+G", "L24+G+M", by_tab)
    vs = F1E.judge(per, res, "L24+G", "L24S+G", by_pub)
    vsr = F1E.judge(per, res, "L24+G+R", "L24S+G+R", by_pub)
    vl = F1E.judge(per, res, "L+G", "L24+G", by_pub)
    mk = lambda b: "○" if b else "×"  # noqa: E731

    def rules(v, yes, no):
        return [f"- 1. 正しい {v['d_ok']:+.2f} {mk(v['checks'][0])}", f"- 2. 重大 {v['d_crit']:+d} {mk(v['checks'][1])}",
                f"- 3. ほかの誤り {v['d_wrong']:+.2f} {mk(v['checks'][2])}", f"- 4. 90% 区間 {v['lo']:+.2f}〜{v['hi']:+.2f} {mk(v['checks'][3])}",
                f"- **判定：{yes if v['adopt'] else no}**"]

    L = ["# G3 の 1 回だけの測り：直し M と銀教材（`research/g3/g3_eval.py`）", "",
         f"- 事前記録 `bench/fixm_prereg_20261112.md`・`bench/silver24_prereg_20261113.md`。採点 {n} 列（正解が unknown・S・other・person の列を除く）。環境 {got}。",
         f"- 正解：先生 2 人の独立のラベル（互いに SHA だけを連絡）の裁定と Codex の見直し。SHA-256 {LABELS_SHA}。G3 は Alberta・Ontario・Berlin の金額・単位の語の表。",
         "", "| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |", "|---|---:|---:|---:|---:|---|"]
    for arm in ARMS:
        m = F1E.mean_of(res, arm)
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | " + "・".join(str(res[f'{arm}{s}'][1]) for s in SEEDS) + " |")
    L += ["", "## 主 1：直し M（L24+G+M 対 L24+G、表で引き直す）", ""] + rules(vm, "決まりを満たした（仮に採る。公開元の重ならない別の陣で確かめてから本物へ）", "確かめられなかった")
    L += ["", "## 主 2：銀教材（L24S+G 対 L24+G、公開元で引き直す）", ""] + rules(vs, "確かめられた（銀で下地を作る学習を採る候補）", "確かめられなかった（銀は使わないまま）")
    L += ["", "## 読むだけ：rho の金額の守りを入れたとき（L24S+G+R 対 L24+G+R、公開元で引き直す）", "",
          f"- 正しいの差 {vsr['d_ok']:+.2f}、90% 区間 {vsr['lo']:+.2f}〜{vsr['hi']:+.2f}、重大の差 {vsr['d_crit']:+d}、ほかの誤りの差 {vsr['d_wrong']:+.2f}", "",
          "## 読むだけ：L24+G 対 L+G（公開元で引き直す）", "",
          f"- 正しいの差 {vl['d_ok']:+.2f}、90% 区間 {vl['lo']:+.2f}〜{vl['hi']:+.2f}、重大の差 {vl['d_crit']:+d}", "",
          "## 読むだけ：正解の種類ごとの正しい・不明（3 本の合計）", "",
          "| 正解 | 列 | " + " | ".join(f"正しい {x}" for x in ARMS) + " | " + " | ".join(f"不明 {x}" for x in ARMS) + " |",
          "|---|---:|" + "---:|" * (2 * len(ARMS))]
    kinds = defaultdict(list)
    for k in per["L24+G1"]:
        kinds[cols[k]["truth"]].append(k)
    for t, ks in sorted(kinds.items(), key=lambda x: -len(x[1])):
        c = lambda arm, o: sum(per[f"{arm}{s}"][k] == o for s in SEEDS for k in ks)  # noqa: E731
        L.append(f"| {t} | {len(ks)} | " + " | ".join(str(c(x, "ok")) for x in ARMS) + " | " + " | ".join(str(c(x, "unk")) for x in ARMS) + " |")
    L += ["", "## 読むだけ：重大の列（銀 × rho の守り、3 本）", "", "| 形 | 本 | id | 列名 | 正解 | 答え | 理由 |", "|---|---|---|---|---|---|---|"]
    for arm in ("L24+G", "L24S+G", "L24+G+R", "L24S+G+R"):
        for s in SEEDS:
            x = raw[f"{arm}{s}"]
            for k in sorted(x):
                if per[f"{arm}{s}"][k] == "crit":
                    L.append(f"| {arm} | {s} | {k} | {str(x[k][2])[:35]} | {x[k][1]} | {x[k][0]} | {str(x[k][3])[:30]} |")
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
    open(os.path.join(HERE, "g3_eval.md"), "w", encoding="utf-8").write(text)
    json.dump(per, open(os.path.join(HERE, "g3_eval_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)


if __name__ == "__main__":
    main()
