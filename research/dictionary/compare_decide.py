"""辞書の 2 つの版を、使い済みの決める陣で並べる（2026-10-31 Claude。探索、害の見つけ出し用。採否には使わない）。
  python research/dictionary/compare_decide.py <辞書A> <辞書B>
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "research"))
import d1_eval as D  # noqa: E402


def run(base, mv, labels, path, dict_path):
    os.environ["JITSURIS_DICT"] = dict_path
    D.EF._DICT.clear()
    D.EF._PCACHE.clear()
    p = {}
    r = D.EF.run(D.with_job(base, path), mv, labels, D.PRODUCT + ("K",), per=p)
    return r, p


def main():
    a, b = sys.argv[1], sys.argv[2]
    labels = list(D.V.LABELS)
    train = [c for bb in D.A.TRAIN for c in D.E.load_batch(bb)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = D.load_side("decide", D.label_fixes(os.path.join(ROOT, "research", "labels", "consistency_20261031", "decisions.jsonl")))
    for s in (2, 3, 4):
        path = os.path.join(ROOT, "materials", "pool", "work", "d1dec", f"pred_d2_job{s}.json")
        ra, pa = run(base, mv, labels, path, a)
        rb, pb = run(base, mv, labels, path, b)
        print(f"L 種子 {s - 1}：A {ra} → B {rb}")
        if s == 2:
            for k in sorted(pa):
                if pa[k][0] != pb[k][0]:
                    print("  ", k, str(pa[k][2])[:30], "正解", pa[k][1], ":", pa[k][0], "→", pb[k][0])


if __name__ == "__main__":
    main()
