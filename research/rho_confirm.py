"""rho の再確認（事前記録 bench/rho_retune_prereg_20261029.md の「次の新しい陣でもう一度確かめる」、2026-10-29 Claude）。
新しい陣（既定 b064・b065）で、本体 C2 の製品の形を ρ=0.7（今）と 0.8（候補）で比べる。重大が増えなければ候補を採る。
使い方：python research/rho_confirm.py [--batches b064 b065] [--out ...]
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

TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--batches", nargs="+", default=["b064", "b065"])
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])
    L = [f"### 再確認：新しい陣（{'・'.join(a.batches)}）・本体 C2（`research/rho_confirm.py`）", "", "| 陣 | 設定 | 結果 | 不明 | 重大 |", "|---|---|---|---:|---:|"]
    tot = {}
    for b in a.batches + ["合計"]:
        bs = a.batches if b == "合計" else [b]
        te = [c for x in bs for c in with_pred(E.load_batch(x), os.path.join(ROOT, "materials", "pool", "work", x, "pred_c2_seed1.json"))[0]]
        P = np.zeros((len(te), len(labels)), dtype="float32")
        p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
        for j, lab in enumerate(mv.classes_):
            P[:, labels.index(lab)] = p[:, j]
        idx = list(range(len(te)))
        fin = E.combine(E.base_decisions(te), P, np.zeros(len(te)), labels, TAU, None, idx)
        for rho in (0.7, 0.8):
            decs = []
            for k in idx:
                d = fin[k]
                c = V.candidate(d[0], d[1], te[k]["pred"], te[k]["top3"], te[k]["header"], P[k], labels, rho)
                decs.append((c, "assert") if c else d)
            s = E.score([d[0] for d in decs], te)
            L.append(f"| {b} | ρ={rho}{'（今）' if rho == 0.7 else '（候補）'} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} |")
            if b == "合計":
                tot[rho] = s
    up = tot[0.8]["critical"] <= tot[0.7]["critical"]
    L += ["", f"- 重大：ρ=0.7 {tot[0.7]['critical']} → ρ=0.8 {tot[0.8]['critical']} → **{'増えない＝ρ=0.8 を採る' if up else '増えた＝今の形のまま'}**"]
    print("\n".join(L))
    if a.out:
        with open(a.out, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    main()
