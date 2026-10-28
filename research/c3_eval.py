"""C3 の判定（事前記録 bench/c3_prereg_20261029.md）：確かめの 6 陣で、本体の予測を製品の形に通して採点する（2026-10-29 Claude）。

本体の予測は各陣の materials/pool/work/<陣>/pred_<model>_seed1.json。検査役 v2 は router_eval.py と同じく b001〜b014 で学ぶ（どの本体でも同じ）。
形：(0) 製品の形（recheck v1 → 検査役 v2 → rho 0.7）、(0') rho なし。陣ごとと合計を出す。
使い方：python research/c3_eval.py --model c2 [--model c3a ...] [--out 結果.md]
"""
import argparse
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from verifier_c1 import TAU  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402

DEV = ("b015", "b016", "b017", "b060", "b062", "b063")
TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", action="append", required=True)
    ap.add_argument("--batches", nargs="+", default=list(DEV))
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])
    L = ["## C3 の判定の採点（`research/c3_eval.py`、確かめの陣・製品の形）", "", "| 本体 | 陣 | 形 | 結果 | 不明 | 重大 |", "|---|---|---|---|---:|---:|"]
    for model in a.model:
        per = {}
        for b in a.batches:
            te, _ = with_pred(E.load_batch(b), os.path.join(ROOT, "materials", "pool", "work", b, f"pred_{model}_seed1.json"))
            P = np.zeros((len(te), len(labels)), dtype="float32")
            p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
            for j, lab in enumerate(mv.classes_):
                P[:, labels.index(lab)] = p[:, j]
            idx = list(range(len(te)))
            fin = E.combine(E.base_decisions(te), P, np.zeros(len(te)), labels, TAU, None, idx)
            no_rho = [fin[k] for k in idx]
            rho = []
            for k, d in enumerate(no_rho):
                c = V.candidate(d[0], d[1], te[k]["pred"], te[k]["top3"], te[k]["header"], P[k], labels, 0.7)
                rho.append((c, "assert") if c else d)
            per[b] = (te, rho, no_rho)
        for b in a.batches + ["合計"]:
            for name, i in (("(0) 製品の形（rho 0.7）", 1), ("(0') rho なし", 2)):
                if b == "合計":
                    te = [c for x in a.batches for c in per[x][0]]
                    decs = [d for x in a.batches for d in per[x][i]]
                else:
                    te, decs = per[b][0], per[b][i]
                s = E.score([d[0] for d in decs], te)
                L.append(f"| {model} | {b} | {name} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} |")
    print("\n".join(L))
    if a.out:
        with open(a.out, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    main()
