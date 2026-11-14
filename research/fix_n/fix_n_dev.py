"""直し N の使い済みの陣での確かめ（2026-11-14 Claude。回帰の点検だけ。採否には使わない。新しい予測・学習なし）。
  python research/fix_n/fix_n_dev.py --f1 <labels/f1/final.jsonl> --g1 <...> --g2 <...> → research/fix_n/fix_n_dev.md
陣：古い 23 陣・決める陣・確かめる陣・E1・E2（research/h_why/ablate.py と同じ、予測は当時の L）、F1・G1・G2（L24 の 3 本）。
形：今の製品の形（PRODUCT＋K）と、それに直し N を足した形。変えた列は全部書く（当たりに・外れのまま・悪く・不明の列への言い切り）。
採点の環境は Python 3.12・scikit-learn 1.8.0・NumPy 2.3.5・SciPy 1.17.0（違えば止まる）。
"""
import argparse
import os
import sys

import numpy as np
import scipy
import sklearn

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
for p in (ROOT, os.path.join(ROOT, "research"), os.path.join(ROOT, "research", "fixes"), os.path.join(ROOT, "independent_eval"),
          os.path.join(ROOT, "research", "f1"), os.path.join(ROOT, "research", "g1"), os.path.join(ROOT, "research", "g2"),
          os.path.join(ROOT, "research", "guard_dates"), HERE):
    sys.path.insert(0, p)
import reserve_eval as R  # noqa: E402
import d1_eval as D  # noqa: E402
import f1_eval as F1E  # noqa: E402
import g1_eval as G1E  # noqa: E402
import g2_eval as G2E  # noqa: E402
import fix_n as N  # noqa: E402

ENV = {"python": "3.12", "sklearn": "1.8.0", "numpy": "2.3.5", "scipy": "1.17.0"}
J3 = ["pred_d2_job2.json", "pred_d2_job3.json", "pred_d2_job4.json"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--f1", required=True)
    ap.add_argument("--g1", required=True)
    ap.add_argument("--g2", required=True)
    a = ap.parse_args()
    got = {"python": "%d.%d" % sys.version_info[:2], "sklearn": sklearn.__version__, "numpy": np.__version__, "scipy": scipy.__version__}
    if got != ENV:
        raise SystemExit(f"環境が違う：{got}")
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", R.DICTS["K"][0])
    D.EF._DICT.clear()
    fx = D.label_fixes(os.path.join(ROOT, "research", "labels", "consistency_20261031", "decisions.jsonl"))
    old = lambda base, folder: [D.with_job(base, os.path.join(ROOT, "materials", "pool", "work", folder, f)) for f in J3]  # noqa: E731
    f1 = F1E.load_f1(a.f1)
    g1 = G1E.load_g1(a.g1)
    g2 = G2E.load_g2(a.g2)
    sets = {"古い 23 陣": [D.EF.load(D.EF.DECIDE + D.EF.CONFIRM)],
            "決める陣": old(D.load_side("decide", fx), "d1dec"),
            "確かめる陣": old(D.load_side("confirm", fx), "d1conf"),
            "E1": [D.with_job(R.load("E1"), os.path.join(ROOT, "materials", "pool", "work", "e1", R.PRED["L"][s])) for s in R.SEEDS],
            "E2": [D.with_job(R.load("E2"), os.path.join(ROOT, "materials", "pool", "work", "e2", R.PRED["L"][s])) for s in R.SEEDS],
            "F1（L24）": [D.with_job(f1, os.path.join(F1E.PRED_DIR, F1E.PRED["L24"][s])) for s in F1E.SEEDS],
            "G1（L24）": [D.with_job(g1, os.path.join(G1E.PRED_DIR, G1E.PRED["L24"][s])) for s in G1E.SEEDS],
            "G2（L24）": [D.with_job(g2, os.path.join(G2E.PRED_DIR, G2E.PRED["L24"][s])) for s in G2E.SEEDS]}
    L = ["# 直し N の使い済みの陣での確かめ（`research/fix_n/fix_n_dev.py`。回帰の点検だけ、採否には使わない）", "",
         f"- 環境 {got}。形：今の製品の形（PRODUCT＋K）と ＋直し N（`research/fix_n/fix_n.py`）。", "",
         "| 陣 | 本 | 採点 | 正しい 今→N | 不明 今→N | 重大 今→N | ほか 今→N | 変えた出力 | 当たりに | 悪く | 外れのまま |",
         "|---|---:|---:|---|---|---|---|---:|---:|---:|---:|"]
    detail = []
    rel_total = {}
    for name, jobs in sets.items():
        tot = {"今": [0] * 5, "N": [0] * 5}
        ch = []
        for i, j in enumerate(jobs):
            res = {}
            for arm in ("今", "N"):
                D.EF._PCACHE.clear()
                p = {}
                if arm == "N":
                    released = []
                    inner = N.n_check_assert

                    def counting(pred, top3, values, header, *x, **y):
                        out = inner(pred, top3, values, header, *x, **y)
                        if N._orig(pred, top3, values, header, *x, **y)[1] == "amount_precision" and out[1] != "amount_precision":
                            released.append(str(header))
                        return out
                    N.n_check_assert = counting
                    try:
                        with N.use():
                            r = D.EF.run(j, mv, labels, D.PRODUCT + ("K",), per=p)
                    finally:
                        N.n_check_assert = inner
                    scored_hdr = [str(v[2]) for k, v in p.items()]
                    unscored = [h for h in released if h not in scored_hdr]
                    if unscored:
                        detail.append(f"- {name} 本{i + 1}：採点の範囲外の列で直し N が止めを外した（列名）：{unscored}")
                    rel_total[name] = rel_total.get(name, 0) + len(released)
                else:
                    r = D.EF.run(j, mv, labels, D.PRODUCT + ("K",), per=p)
                tot[arm] = [x + y for x, y in zip(tot[arm], r)]
                res[arm] = p
            for k in res["今"]:
                x, y = res["今"][k], res["N"][k]
                if x[0] != y[0]:
                    ch.append((i + 1, k, x[2], x[1], x[0], y[0], [str(v) for v in (x[5] if len(x) > 5 else [])][:5]))
        good = sum(1 for c in ch if c[5] == c[3])
        bad = sum(1 for c in ch if c[4] == c[3])
        L.append(f"| {name} | {len(jobs)} | {tot['今'][0]} | {tot['今'][1]}→{tot['N'][1]} | {tot['今'][2]}→{tot['N'][2]} | {tot['今'][3]}→{tot['N'][3]} | "
                 f"{tot['今'][4]}→{tot['N'][4]} | {len(ch)} | {good} | {bad} | {len(ch) - good - bad} |")
        detail += [f"- {name} 本{c[0]} {c[1]} [{str(c[2])[:40]}] 正解 {c[3]}：{c[4]} → {c[5]}（値 {' / '.join(v[:18] for v in c[6])}）" for c in ch]
        print(name, tot, len(ch), good, bad, rel_total.get(name, 0), flush=True)
    L += ["", "直し N が再確認の止めを外した数（見張りのあとの言い切りの段、採点の範囲外も含む）：" + "、".join(f"{k} {v}" for k, v in rel_total.items()), "",
          "採点の範囲外（正解が unknown・S・other・person）の列で外したものは、下の「採点の範囲外」の行に列名を書く（無ければ行が無い）。", "",
          "## 変えた出力（全部）", ""] + detail
    open(os.path.join(HERE, "fix_n_dev.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
