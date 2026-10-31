"""辞書の動作の確かめ（2026-10-31 Claude）。古い 23 陣（辞書の「過去」の材料にした陣）で K あり・なしを比べる。
材料にした陣なので当てはまりは良く出る。効き目の測りではなく、壊していないか（重大が増えないか）の確かめ。
  python research/dictionary/sanity_old.py
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
for p in (os.path.join(ROOT, "research"), os.path.join(ROOT, "research", "fixes")):
    sys.path.insert(0, p)
import d1_eval as D  # noqa: E402
import eval_fixes as EF  # noqa: E402


def main():
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm],
                       np.array([c["truth"] for c in train])[okm])
    data = EF.load(EF.DECIDE + EF.CONFIRM)
    pa, pb = {}, {}
    a = EF.run(data, mv, labels, D.PRODUCT, per=pa)
    EF._PCACHE.clear()
    b = EF.run(data, mv, labels, D.PRODUCT + ("K",), per=pb)
    for name, (n, ok, unk, crit, wrong) in (("辞書なし", a), ("辞書あり", b)):
        print(f"{name}: 採点 {n} 正しい {ok} 不明 {unk} 重大 {crit} ほか {wrong}")
    for k in pa:
        if pa[k][0] != pb[k][0]:
            print(k, pa[k][2][:35], "正解", pa[k][1], ":", pa[k][0], "→", pb[k][0])


if __name__ == "__main__":
    main()
