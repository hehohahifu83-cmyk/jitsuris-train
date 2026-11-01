"""直しの 1 つ外し（2026-11-01 Claude。探索用、採否には使わない）。決める陣・確かめる陣（使い済み）と E1 で、
製品＋K2、全部の直し、各直しを 1 つ外した形の 3 本の合計と、重大・誤りを増やした列を書く。
  python research/e1_why/ablate.py → research/e1_why/ablate.md
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "research"))
import reserve_eval as R, d1_eval as D  # noqa: E402
ALLG = ("F1b", "F3", "F6", "F7", "G1", "G2", "G3", "G4")

def main():
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", R.DICTS["K2"][0]); D.EF._DICT.clear()
    fx = D.label_fixes(os.path.join(ROOT, "research", "labels", "consistency_20261031", "decisions.jsonl"))
    sets = {"decide": (D.load_side("decide", fx), "d1dec", ["pred_d2_job2.json", "pred_d2_job3.json", "pred_d2_job4.json"]),
            "confirm": (D.load_side("confirm", fx), "d1conf", ["pred_d2_job2.json", "pred_d2_job3.json", "pred_d2_job4.json"]),
            "E1": (R.load("E1"), "e1", [R.PRED["LV"][s] for s in R.SEEDS])}
    configs = [("製品＋K2", ()), ("全部", ALLG)] + [(f"全部−{g}", tuple(x for x in ALLG if x != g)) for g in ALLG]
    L = ["# 直しの 1 つ外し（`research/e1_why/ablate.py`。使い済みの陣で探索、採否には使わない）", ""]
    for sname, (base, folder, preds) in sets.items():
        jobs = [D.with_job(base, os.path.join(ROOT, "materials", "pool", "work", folder, f)) for f in preds]
        L += [f"## {sname}", "", "| 形 | 正しい | 不明 | 重大 | ほか |", "|---|---:|---:|---:|---:|"]
        ref = None
        for name, fs in configs:
            tot = [0] * 5; per = []
            for j in jobs:
                D.EF._PCACHE.clear(); p = {}
                r = D.EF.run(j, mv, labels, D.PRODUCT + ("K",) + fs, per=p)
                tot = [a + b for a, b in zip(tot, r)]; per.append(p)
            L.append(f"| {name} | {tot[1]} | {tot[2]} | {tot[3]} | {tot[4]} |")
            if ref is None:
                ref = per
            elif name == "全部":
                bad = [(i, k, ref[i][k][0], p[k][0], p[k][1], p[k][2]) for i, p in enumerate(per) for k in p
                       if p[k][0] != ref[i][k][0] and p[k][0] not in ("unknown", p[k][1])]
                L += ["", "誤りを増やした列（全部）："] + [f"- 本{i+1} {k} [{str(h)[:30]}] 正解 {t}：{a} → {b}" for i, k, a, b, t, h in bad] + [""]
            print(sname, name, tot, flush=True)
        L.append("")
    open(os.path.join(HERE, "ablate.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
