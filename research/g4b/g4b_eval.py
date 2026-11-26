"""G4b の 1 回だけの測り：方法 T1（同じ行のほかの列の値、rowctx-v1）（2026-11-26 Claude。予測の前に SHA を事前記録に固定する）。
事前記録：bench/g4_prereg_20261118.md（G4、f51d25f で凍結）と bench/g4b_prereg_20261122.md（G4b の差、e98987b で凍結）。

  python research/g4b/g4b_eval.py --labels <ai-bridge>/labels/g4b/final.jsonl [--dry]   → research/g4b/g4b_eval.md・g4b_eval_per_column.json

形（製品の形と採点は G3 と同じ：guard＋recheck＋verifier v2（採点のたびに 14 バッチで学び直し）＋rho＋辞書 K＋末尾の通貨確認）：
  C      ＝ control-256（run 44688386547 の job1〜3、種子 1〜3、FT_ROWCTX なし）
  T      ＝ T1-256（同じ run の job4〜6、種子 1〜3、FT_ROWCTX=1・rowctx-v1）
  L24    ＝ L24（run 41735353926 の job1〜3、長さ 160。読むだけ）
  C+N・T+N ＝ それぞれに直し N（research/fix_n/fix_n.py）を足した形（読むだけ）
主（1 本だけ）：T 対 C を決まり 1〜4（表で引き直す、3 本を同じ表の組で一緒に、2,000 回、種 "d2-boot"）。
採点の環境は Python 3.12・scikit-learn 1.8.0・NumPy 2.3.5・SciPy 1.17.0（違えば止まる）。
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
          os.path.join(ROOT, "research", "f1"), os.path.join(ROOT, "research", "fix_n")):
    sys.path.insert(0, p)
import d1_eval as D  # noqa: E402
import reserve_eval as R  # noqa: E402
import f1_eval as F1E  # noqa: E402
import fix_n as N  # noqa: E402
import g4 as G4  # noqa: E402
import sklearn  # noqa: E402
import scipy  # noqa: E402

G4.use_variant("g4b")   # このプロセスでは G4b だけを使う（g4 には戻さない）

LABELS_SHA = "bd3baa8dfd4fcec64f8aab1cad041a2b7ff057cc2b163eed450ea45496e96bd7"
SET_SHA = "b452695332509f3b13c719c97e6be00caed4df41c16c8d02deb3efeee6195dfc"
TITLES_SHA = "a9719e3556f7d99e7a10e6e53f7e235f6ad3beca0a931323fa2b47b2d7a175ff"
FIXN_SHA = "672dd70566b70f16915a382f80dcc603194d92c178fac253a008d9452f2eda35"
ENV = {"python": "3.12", "sklearn": "1.8.0", "numpy": "2.3.5", "scipy": "1.17.0"}
SET_PATH = os.path.join(ROOT, "independent_eval", "results", "g4b", "g4b.json")
PRED_DIR = os.path.join(ROOT, "independent_eval", "predictions_g4b")
SEEDS = (1, 2, 3)
PRED = {"C": {1: "pred_c_job1.json", 2: "pred_c_job2.json", 3: "pred_c_job3.json"},
        "T": {1: "pred_t_job4.json", 2: "pred_t_job5.json", 3: "pred_t_job6.json"},
        "L24": {1: "pred_l24_job1.json", 2: "pred_l24_job2.json", 3: "pred_l24_job3.json"}}
WEIGHTS = {("C", 1): "0b3765d5262d58dc704751978f2e4c0fe8e644e0055d48667977b37316debc7c",
           ("C", 2): "53b148ac3793707132877a2a995e0530cd85d276e34e81aff3d3ef9681ebce13",
           ("C", 3): "f745789ed9b80f98b754dba93e40315e62ccd206b87314014292653597bfb021",
           ("T", 1): "31fa3544b2c88d1bbbc68bc3189cc63c0705693d35e25c79465f90c76e14ce25",
           ("T", 2): "139601790e3e1d252b900aafedaccb4536666e7d78394f6e72556fc109bc197d",
           ("T", 3): "e7af7ec00066d52903d6aa98f7c1dd4a8b8a17873a690667320494c056ce34f1",
           ("L24", 1): "201d9757040ae4bd27c35cc2a9baaba47c5110dbec404dd4cca1a487a312c180",
           ("L24", 2): "981168cac01307a39e34aa24f36a6741c5484e4e6af2b5d3d4dd1cda2174ca76",
           ("L24", 3): "a6811a32a41641bc5fc90af2d1e42c558e9d870084712c58260d407fe6efe3af"}
# 形：名前 → (重み, 直し N)
ARMS = {"C": ("C", False), "T": ("T", False), "L24": ("L24", False), "C+N": ("C", True), "T+N": ("T", True)}
EXCLUDED = ("unknown", "S", "other", "person")


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load_g4b(labels_path):
    if sha(SET_PATH) != SET_SHA:
        raise SystemExit("g4b.json が凍結のものと違う")
    if sha(labels_path) != LABELS_SHA:
        raise SystemExit("確定ラベルの SHA が事前記録と違う")
    truth = {d["id"]: d["label"] for d in map(json.loads, open(labels_path, encoding="utf-8"))}
    doc = json.load(open(SET_PATH, encoding="utf-8"))
    cols5 = doc["columns"]
    rows = G4.load_rows()
    picked, _ = G4.select(rows)
    if len(picked) != len(cols5):
        raise SystemExit("corpus の選び直しが g4b.json と合わない")
    out = []
    for c, i in zip(cols5, picked):
        r = rows[i]
        if r["header"] != c["header"]:
            raise SystemExit(f"{c['id']}: 列名が corpus と合わない")
        vals = [str(v) for v in (r.get("row_values") or r["values"]) if str(v).strip() not in F1E.JUNK] or [str(v) for v in c["values"]]
        out.append({"batch": "g4b", "i": i, "id": c["id"], "table": c["table"], "header": str(c["header"]),
                    "values5": [str(v) for v in c["values"]], "values": vals, "context": [str(x) for x in c.get("siblings") or []],
                    "unit": str(c.get("unit") or ""), "language": c.get("language", ""), "truth": truth[c["id"]], "adjudicated": True,
                    "teacher": truth[c["id"]], "publisher": r["publisher"],
                    "tab": {"rows": r.get("row_values") or r["values"], "row_index": r.get("row_index"), "total": r.get("datastore_total")}})
    return {"g4b": out}


def check_predictions(ids):
    """9 本の予測ファイルの由来を照合する（セット・題名・重み×種子・列の id の集合、T の row_context の版と付いた列の数）。"""
    want = set(ids)
    if len(want) != len(ids):
        raise SystemExit("G4b の列 id が重複している")
    for (model, s), wsha in WEIGHTS.items():
        path = os.path.join(PRED_DIR, PRED[model][s])
        d = json.load(open(path, encoding="utf-8"))
        ck, ti = d.get("checkpoint") or {}, d.get("titles") or {}
        if d.get("set_sha256") != SET_SHA or d.get("set_id") != G4.SET_ID:
            raise SystemExit(f"{path}: セットの SHA・id が違う")
        if ck.get("weights_sha256") != wsha or str(ck.get("seed")) != str(s):
            raise SystemExit(f"{path}: 重み・種子が {model} の {s} 本目と違う")
        if ti.get("sha256") != TITLES_SHA:
            raise SystemExit(f"{path}: 題名の SHA が違う")
        rc = d.get("row_context")
        if model == "T":
            if not rc or rc.get("version") != "rowctx-v1" or rc.get("columns_with_context") != len(ids) or rc.get("columns") != len(ids):
                raise SystemExit(f"{path}: T1 の予測に同じ行の文が全部の列に付いていない")
        elif rc:
            raise SystemExit(f"{path}: control・L24 の予測に同じ行の文が付いている")
        if int(ck.get("max_length") or 0) != {"C": 256, "T": 256, "L24": 160}[model]:
            raise SystemExit(f"{path}: 入力の長さが形と合わない（C・T は 256、L24 は 160）")
        got = [r["id"] for r in d["rows"]]
        if len(got) != len(set(got)) or set(got) != want:
            raise SystemExit(f"{path}: 列 id の集合が g4b.json と違う（重複・欠け・余り）")


def run(base, mv, labels, model, s, with_n, per_all=None):
    data = D.with_job(base, os.path.join(PRED_DIR, PRED[model][s]))
    D.EF._PCACHE.clear()
    p = {}
    if with_n:
        with N.use():
            res = D.EF.run(data, mv, labels, D.PRODUCT + ("K",), per=p)
    else:
        res = D.EF.run(data, mv, labels, D.PRODUCT + ("K",), per=p)
    if per_all is not None:   # 採点の外の列の最終の答え（正解は eval_fixes.run:77 で絞り込みにしか使われない。写しの正解を印に替える）
        u = {b: [dict(c, truth="__範囲外__") if (not c["truth"] or c["truth"] in EXCLUDED) else c for c in cs] for b, cs in data.items()}
        D.EF._PCACHE.clear()
        q = {}
        if with_n:
            with N.use():
                D.EF.run(u, mv, labels, D.PRODUCT + ("K",), per=q)
        else:
            D.EF.run(u, mv, labels, D.PRODUCT + ("K",), per=q)
        per_all.update({k: v[0] for k, v in q.items() if v[1] == "__範囲外__"})
    return res, p


def rate(per, arm, keys):
    n = len(keys) * len(SEEDS)
    return 100 * sum(per[f"{arm}{s}"][k] == "ok" for s in SEEDS for k in keys) / n if n else float("nan")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", required=True)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args(argv)
    got = {"python": "%d.%d" % sys.version_info[:2], "sklearn": sklearn.__version__, "numpy": np.__version__, "scipy": scipy.__version__}
    if got != ENV:
        raise SystemExit(f"採点の環境が事前記録と違う：{got}")
    if sha(os.path.join(ROOT, "research", "fix_n", "fix_n.py")) != FIXN_SHA:
        raise SystemExit("fix_n.py が事前記録の SHA と違う")
    if sha(os.path.join(ROOT, "independent_eval", "results", "g4b", "titles.json")) != TITLES_SHA:
        raise SystemExit("titles.json が事前記録の SHA と違う")
    f, dsha = R.DICTS["K"]
    if sha(os.path.join(ROOT, "materials", "dictionary", f)) != dsha:
        raise SystemExit("辞書が凍結したものと違う")
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", f)
    D.EF._DICT.clear()
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = load_g4b(a.labels)
    cols = {c["id"]: c for c in base["g4b"]}
    check_predictions([c["id"] for c in base["g4b"]])
    res, per, raw, outside = {}, {}, {}, {}
    for arm, (model, n) in ARMS.items():
        for s in SEEDS:
            pa = {}
            r, p = run(base, mv, labels, model, s, n, pa)
            res[f"{arm}{s}"], raw[f"{arm}{s}"], outside[f"{arm}{s}"] = r, p, pa
            per[f"{arm}{s}"] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}
    if len({r[0] for r in res.values()}) != 1:
        raise SystemExit("採点列の数が形で違う")
    n_cols = res["C1"][0]
    by_tab = {k: cols[k]["table"] for k in per["C1"]}
    by_pub = {k: cols[k]["publisher"] for k in per["C1"]}
    vt = F1E.judge(per, res, "C", "T", by_tab)
    vtp = F1E.judge(per, res, "C", "T", by_pub)
    vl = F1E.judge(per, res, "L24", "C", by_tab)
    vn = F1E.judge(per, res, "T", "T+N", by_tab)
    mk = lambda b: "○" if b else "×"  # noqa: E731
    L = ["# G4b の 1 回だけの測り：方法 T1（`research/g4b/g4b_eval.py`）", "",
         f"- 事前記録 `bench/g4_prereg_20261118.md`・`bench/g4b_prereg_20261122.md`。採点 {n_cols} 列（正解が unknown・S・other・person の列を除く）。環境 {got}。",
         f"- 正解：先生 2 人の独立のラベルの裁定と Codex の見直し。SHA-256 {LABELS_SHA}。G4b は Alberta・GovData.de の、G1〜G3 で評価した公開元を含む新しい表。",
         "", "| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |", "|---|---:|---:|---:|---:|---|"]
    for arm in ARMS:
        m = F1E.mean_of(res, arm)
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | " + "・".join(str(res[f'{arm}{s}'][1]) for s in SEEDS) + " |")
    L += ["", "## 主：T1-256 対 control-256（T 対 C、表で引き直す）", "",
          f"- 1. 正しい {vt['d_ok']:+.2f} {mk(vt['checks'][0])}", f"- 2. 重大 {vt['d_crit']:+d} {mk(vt['checks'][1])}",
          f"- 3. ほかの誤り {vt['d_wrong']:+.2f} {mk(vt['checks'][2])}", f"- 4. 90% 区間 {vt['lo']:+.2f}〜{vt['hi']:+.2f} {mk(vt['checks'][3])}",
          f"- **判定：{'決まりを満たした（T1 を採る候補）' if vt['adopt'] else '確かめられなかった'}**", "",
          "## 読むだけ", "",
          f"- T 対 C（公開元で引き直す）：正しいの差 {vtp['d_ok']:+.2f}、90% 区間 {vtp['lo']:+.2f}〜{vtp['hi']:+.2f}",
          f"- C 対 L24（長さ 256 と 160、表で引き直す）：正しいの差 {vl['d_ok']:+.2f}、90% 区間 {vl['lo']:+.2f}〜{vl['hi']:+.2f}、重大の差 {vl['d_crit']:+d}",
          f"- T+N 対 T（直し N）：正しいの差 {vn['d_ok']:+.2f}、重大の差 {vn['d_crit']:+d}", ""]
    used = G4.used_publishers()   # G1〜G3 で表を採った公開元（正規化した id）
    groups = {"カタログ Alberta": lambda k: by_pub[k].startswith("alberta_cat"), "カタログ GovData": lambda k: by_pub[k].startswith("govdata_cat"),
              "G1〜G3 で評価した公開元": lambda k: G4.norm_pub(by_pub[k]) in used, "未評価の公開元": lambda k: G4.norm_pub(by_pub[k]) not in used}
    L += ["## 読むだけ：まとまりごとの正しい（3 本の平均）", "", "| まとまり | 採点の列 | 表 | " + " | ".join(ARMS) + " |", "|---|---:|---:|" + "---:|" * len(ARMS)]
    for g, fn in groups.items():
        ks = [k for k in per["C1"] if fn(k)]
        L.append(f"| {g} | {len(ks)} | {len({by_tab[k] for k in ks})} | " + " | ".join(f"{rate(per, x, ks):.2f}%" for x in ARMS) + " |")
    kinds = defaultdict(list)
    for k in per["C1"]:
        kinds[cols[k]["truth"]].append(k)
    L += ["", "## 読むだけ：正解の種類ごとの正しい・不明（3 本の合計）", "",
          "| 正解 | 列 | " + " | ".join(f"正しい {x}" for x in ARMS) + " | " + " | ".join(f"不明 {x}" for x in ARMS) + " |", "|---|---:|" + "---:|" * (2 * len(ARMS))]
    for t, ks in sorted(kinds.items(), key=lambda x: -len(x[1])):
        c = lambda arm, o: sum(per[f"{arm}{s}"][k] == o for s in SEEDS for k in ks)  # noqa: E731
        L.append(f"| {t} | {len(ks)} | " + " | ".join(str(c(x, "ok")) for x in ARMS) + " | " + " | ".join(str(c(x, "unk")) for x in ARMS) + " |")
    L += ["", "## T1 が変えた列（C → T、3 本）", "", "| 本 | id | 表 | 列名 | 正解 | C | T |", "|---|---|---|---|---|---|---|"]
    for s in SEEDS:
        x, y = raw[f"C{s}"], raw[f"T{s}"]
        for k in sorted(x):
            if x[k][0] != y[k][0]:
                L.append(f"| {s} | {k} | {by_tab[k]} | {str(x[k][2])[:35]} | {x[k][1]} | {x[k][0]} | {y[k][0]} |")
    L += ["", "## 重大の列（C・T、3 本）", "", "| 形 | 本 | id | 列名 | 正解 | 答え |", "|---|---|---|---|---|---|"]
    for arm in ("C", "T"):
        for s in SEEDS:
            x = raw[f"{arm}{s}"]
            for k in sorted(x):
                if per[f"{arm}{s}"][k] == "crit":
                    L.append(f"| {arm} | {s} | {k} | {str(x[k][2])[:35]} | {x[k][1]} | {x[k][0]} |")
    L += ["", "## 採点の外の列への新しい言い切り（C で unknown、T で言い切り。id×本）", ""]
    news = [(s, k, outside[f"T{s}"][k]) for s in SEEDS for k in sorted(outside[f"C{s}"]) if outside[f"C{s}"][k] == "unknown" and outside[f"T{s}"].get(k, "unknown") != "unknown"]
    truth_all = {d["id"]: d["label"] for d in map(json.loads, open(a.labels, encoding="utf-8"))}
    L += [f"- 本{s} {k} [{str(cols[k]['header'])[:35]}] 正解 {truth_all[k]}：→ {v}" for s, k, v in news] or ["- なし"]
    text = "\n".join(L) + "\n"
    print(text)
    if a.dry:
        return
    open(os.path.join(HERE, "g4b_eval.md"), "w", encoding="utf-8").write(text)
    json.dump({"per": per, "outside": outside}, open(os.path.join(HERE, "g4b_eval_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)


if __name__ == "__main__":
    main()
