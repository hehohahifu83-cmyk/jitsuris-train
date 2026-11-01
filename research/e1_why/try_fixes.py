"""直しの試し（2026-11-01 Claude。探索用、採否には使わない）。陣（E1・決める陣・確かめる陣）で、製品の形＋K2 に直しを足したときの 3 本の合計。
  python research/e1_why/try_fixes.py E1|decide|confirm F3 F6 F7 ...
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "research"))
import reserve_eval as R, d1_eval as D  # noqa: E402

def main():
    side, extra = sys.argv[1], tuple(sys.argv[2:])
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    if side == "E1":
        base, folder, preds = R.load("E1"), "e1", [R.PRED["LV"][s] for s in R.SEEDS]
    else:
        fx = D.label_fixes(os.path.join(ROOT, "research", "labels", "consistency_20261031", "decisions.jsonl"))
        base = D.load_side(side, fx); folder = "d1dec" if side == "decide" else "d1conf"
        preds = ["pred_d2_job2.json", "pred_d2_job3.json", "pred_d2_job4.json"]
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", R.DICTS["K2"][0]); D.EF._DICT.clear()
    for name, fx in (("製品＋K2", ()), ("＋" + "・".join(extra), extra)):
        tot = [0] * 5; per = {}
        for f in preds:
            D.EF._PCACHE.clear(); p = {}
            r = D.EF.run(D.with_job(base, os.path.join(ROOT, "materials", "pool", "work", folder, f)), mv, labels, D.PRODUCT + ("K",) + fx, per=p)
            tot = [a + b for a, b in zip(tot, r)]; per[f] = p
        print(f"{name}: 採点 {tot[0]} 正しい {tot[1]} 不明 {tot[2]} 重大 {tot[3]} ほか {tot[4]}")
        if fx:
            for f in preds:
                for k in per[f]:
                    if per[f][k][0] != base_per[f][k][0]:
                        print(f"   {f[-10:]} {k} [{str(per[f][k][2])[:30]}] 正解 {per[f][k][1]}：{base_per[f][k][0]} → {per[f][k][0]}")
        base_per = per

if __name__ == "__main__":
    main()
