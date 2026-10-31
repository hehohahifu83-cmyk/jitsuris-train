"""D2 の判定の感度（2026-10-31 Claude。読むだけ。判定は事前記録どおり research/d2_eval_decide.md のまま）。

予測を見たあとに気づいた正解の誤り 3 列を直したら数字がどう変わるかを見る：
  b072-0182 Angebotsstufe Code：quantity → category（D1 のあとで記録済み）
  b073-0116・b073-0195 POIコード：id → category（LABEL_GUIDE 131 行。b090 の同じ列は category。b073 の全部の見直しでの Claude の誤り）
  python research/d2_why/sensitivity.py
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "research"))
import d1_eval as D  # noqa: E402
import d2_eval as D2  # noqa: E402

FIX = {"b072-0182": "category", "b073-0116": "category", "b073-0195": "category"}


def main():
    folder = os.path.join(ROOT, "materials", "pool", "work", "d1dec")
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm],
                       np.array([c["truth"] for c in train])[okm])
    for fixed in (False, True):
        base = D.load_side("decide")
        if fixed:
            for cs in base.values():
                for c in cs:
                    if c["id"] in FIX:
                        c["truth"] = c["teacher"] = FIX[c["id"]]
        res, per = {}, {}
        for name, (_, _, pred, _, _) in D2.RUNS.items():
            D.EF._PCACHE.clear()
            p = {}
            res[name] = D.EF.run(D.with_job(base, os.path.join(folder, pred)), mv, labels, D.PRODUCT, per=p)
            per[name] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}
        tables = {c["id"]: (c["batch"], c["table"]) for cs in base.values() for c in cs if c["id"] in per["A1"]}
        mean = {arm: {"ok": sum(100 * res[f"{arm}{s}"][1] / res[f"{arm}{s}"][0] for s in D2.SEEDS) / 3,
                      "crit": sum(res[f"{arm}{s}"][3] for s in D2.SEEDS),
                      "wrong": sum(100 * res[f"{arm}{s}"][4] / res[f"{arm}{s}"][0] for s in D2.SEEDS) / 3} for arm in ("A", "L")}
        lo, hi = D2.pooled_boot(per, tables)
        d_ok, d_crit, d_wrong, checks, adopt = D2.verdict(mean, lo)
        print(f"{'直した' if fixed else 'そのまま'}：A 正 {mean['A']['ok']:.2f}% 重大 {mean['A']['crit']}／L 正 {mean['L']['ok']:.2f}% 重大 {mean['L']['crit']}／"
              f"差 {d_ok:+.2f}、ほか {d_wrong:+.2f}、区間 {lo:+.2f}〜{hi:+.2f}、決まり {checks} → {'採る' if adopt else '採らない'}")


if __name__ == "__main__":
    main()
