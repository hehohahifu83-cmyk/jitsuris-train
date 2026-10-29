"""単位の列の見出しを広げる試しの採点（事前記録 bench/unit_header_prereg_20261029.md、2026-10-29 Claude）。
b017・b063・b064 で、今の C2 の予測（単位なし）と、単位の例を替えた列だけ予測し直したもの（materials/pool/work/unitfix1029/pred_c2_seed1.json）を、
製品の形（recheck v1 → 検査役 v2 → ρ=0.8）で比べる。替えた列だけと 3 陣全体の両方を出す。
使い方：python research/unit_eval.py [--out ...]
"""
import argparse
import copy
import json
import os
import sys
from collections import Counter

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from verifier_c1 import TAU  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402

BATCHES = ("b017", "b063", "b064")
TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))
RHO = 0.8


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])
    fix = {r["id"]: r for r in json.load(open(os.path.join(ROOT, "materials", "pool", "work", "unitfix1029", "pred_c2_seed1.json"), encoding="utf-8"))["rows"]}
    base = [c for b in BATCHES for c in with_pred(E.load_batch(b), os.path.join(ROOT, "materials", "pool", "work", b, "pred_c2_seed1.json"))[0]]
    new = copy.deepcopy(base)
    for c in new:
        if c["id"] in fix:
            c["pred"], c["top3"] = fix[c["id"]]["guarded_prediction"], fix[c["id"]]["top3"]

    def product(te):
        P = np.zeros((len(te), len(labels)), dtype="float32")
        p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
        for j, lab in enumerate(mv.classes_):
            P[:, labels.index(lab)] = p[:, j]
        idx = list(range(len(te)))
        fin = E.combine(E.base_decisions(te), P, np.zeros(len(te)), labels, TAU, None, idx)
        out = []
        for k in idx:
            d = fin[k]
            c = V.candidate(d[0], d[1], te[k]["pred"], te[k]["top3"], te[k]["header"], P[k], labels, RHO)
            out.append(c if c else d[0])
        return out

    d0, d1 = product(base), product(new)
    sub = [k for k, c in enumerate(base) if c["id"] in fix]
    L = ["### 結果（`research/unit_eval.py`、C2 種子 1・製品の形 ρ=0.8）", "", "| 範囲 | 単位 | 結果 | 不明 | 重大 |", "|---|---|---|---|---:|"]
    res = {}
    for name, ks in (("替えた列（183）", sub), ("3 陣全体", list(range(len(base))))):
        for tag, d in (("今（単位なし）", d0), ("広げた決まり（単位あり）", d1)):
            s = E.score([d[k] for k in ks], [base[k] for k in ks])
            res[(name, tag)] = s
            L.append(f"| {name} | {tag} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} |")
    moves = Counter()
    for k in sub:
        t = base[k]["truth"]
        if not t or t in ("unknown", "S"):
            continue
        a0, a1 = d0[k], d1[k]
        if a0 == a1:
            continue
        moves[("正→誤" if a0 == t and a1 not in (t, "unknown") else "誤→正" if a1 == t and a0 != t else
               "不明→言い切り" if a0 == "unknown" else "言い切り→不明" if a1 == "unknown" else "誤→別の誤")] += 1
    s0, s1 = res[("替えた列（183）", "今（単位なし）")], res[("替えた列（183）", "広げた決まり（単位あり）")]
    keep = s1["critical"] <= s0["critical"] and s1["correct"] / s1["n"] >= s0["correct"] / s0["n"] - 0.005
    L += ["", f"- 変わった列の向き：{dict(moves) or 'なし'}",
          f"- 判定（替えた列）：重大 {s0['critical']} → {s1['critical']}、正解率 {s0['correct'] / s0['n']:.1%} → {s1['correct'] / s1['n']:.1%} → **{'採る' if keep else '採らない'}**"]
    print("\n".join(L))
    if a.out:
        with open(a.out, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    main()
