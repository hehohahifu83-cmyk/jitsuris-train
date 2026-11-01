"""直し H（H1 種類のコード・H2 日付の形）の害と効きの確かめ（2026-11-01 Claude。使い済みの陣だけ。探索用、採否には使わない）。
  python research/h_why/ablate.py → research/h_why/ablate.md
形：P（今の製品＝直し G 込み、辞書 frozen_d3）、P＋H1、P＋H2、P＋H。
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
for p in (os.path.join(ROOT, "research"), os.path.join(ROOT, "research", "fixes")):
    sys.path.insert(0, p)
import reserve_eval as R, d1_eval as D, eval_fixes as EF  # noqa: E402
J3 = ["pred_d2_job2.json", "pred_d2_job3.json", "pred_d2_job4.json"]
CONFIGS = [("P", ()), ("P＋H1", ("H1",)), ("P＋H2", ("H2",)), ("P＋H", ("H1", "H2"))]


def main():
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", R.DICTS["K"][0]); D.EF._DICT.clear()
    fx = D.label_fixes(os.path.join(ROOT, "research", "labels", "consistency_20261031", "decisions.jsonl"))
    sets = {"古い 23 陣": None,
            "決める陣": (D.load_side("decide", fx), "d1dec", J3),
            "確かめる陣": (D.load_side("confirm", fx), "d1conf", J3),
            "E1": (R.load("E1"), "e1", [R.PRED["L"][s] for s in R.SEEDS]),
            "E2": (R.load("E2"), "e2", [R.PRED["L"][s] for s in R.SEEDS])}
    L = ["# 直し H の 1 つずつの確かめ（`research/h_why/ablate.py`。使い済みの陣、探索用。採否には使わない）", ""]
    for sname, spec in sets.items():
        if spec is None:
            jobs = [EF.load(EF.DECIDE + EF.CONFIRM)]
        else:
            base, folder, preds = spec
            jobs = [D.with_job(base, os.path.join(ROOT, "materials", "pool", "work", folder, f)) for f in preds]
        L += [f"## {sname}（{len(jobs)} 本の合計）", "", "| 形 | 採点 | 正しい | 不明 | 重大 | ほか |", "|---|---:|---:|---:|---:|---:|"]
        ref = None; changed = []
        for name, fs in CONFIGS:
            tot = [0] * 5; per = []
            for j in jobs:
                D.EF._PCACHE.clear(); p = {}
                r = D.EF.run(j, mv, labels, D.PRODUCT + ("K",) + fs, per=p)
                tot = [a + b for a, b in zip(tot, r)]; per.append(p)
            L.append(f"| {name} | {tot[0]} | {tot[1]} | {tot[2]} | {tot[3]} | {tot[4]} |")
            print(sname, name, tot, flush=True)
            if ref is None:
                ref = per
            elif name == "P＋H":
                changed = [(i, k, ref[i][k][0], p[k][0], p[k][1], p[k][2]) for i, p in enumerate(per) for k in p if p[k][0] != ref[i][k][0]]
        good = [x for x in changed if x[3] == x[4]]; bad = [x for x in changed if x[3] != x[4]]
        L += ["", f"P＋H が変えた出力：{len(changed)}（当たりに {len(good)}、それ以外に {len(bad)}）", ""]
        L += [f"- 悪く・外れのまま：本{i+1} {k} [{str(h)[:40]}] 正解 {t}：{a} → {b}" for i, k, a, b, t, h in bad]
        L += [f"- 当たり：本{i+1} {k} [{str(h)[:40]}] {a} → {b}" for i, k, a, b, t, h in good[:60]] + [""]
    open(os.path.join(HERE, "ablate.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
