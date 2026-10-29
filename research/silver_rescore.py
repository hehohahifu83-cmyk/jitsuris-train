"""銀（C3b）を直した決め方で測り直す（事前記録 bench/silver_rescore_prereg_20261029.md、2026-10-29 Claude）。
決め方：recheck v1 → 検査役 v2（τ 0.05）→ rho 0.8 → 通貨の手がかりの無い金額は不明。本体 C2・C3a・C3b 種子 1、新しい陣 8 つ。
使い方：python research/silver_rescore.py [--out ...]
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

BATCHES = ("b015", "b016", "b017", "b060", "b062", "b063", "b064", "b065")
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
    L = ["### 結果（`research/silver_rescore.py`、直した決め方）", "", "| 本体 | 陣 | 結果 | 不明 | 重大 |", "|---|---|---|---|---:|"]
    tot, crit = {}, {}
    for model in ("c2", "c3a", "c3b"):
        allte, alld = [], []
        for b in BATCHES:
            te, _ = with_pred(E.load_batch(b), os.path.join(ROOT, "materials", "pool", "work", b, f"pred_{model}_seed1.json"))
            P = np.zeros((len(te), len(labels)), dtype="float32")
            p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
            for j, lab in enumerate(mv.classes_):
                P[:, labels.index(lab)] = p[:, j]
            idx = list(range(len(te)))
            fin = E.combine(E.base_decisions(te), P, np.zeros(len(te)), labels, TAU, None, idx)
            d = []
            for k in idx:
                cand = V.candidate(fin[k][0], fin[k][1], te[k]["pred"], te[k]["top3"], te[k]["header"], P[k], labels, RHO)
                lab = cand if cand else fin[k][0]
                d.append(V.amount_cue_veto(lab, te[k]["header"], te[k].get("unit"), te[k]["values"]))
            s = E.score(d, te)
            L.append(f"| {model} | {b} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} |")
            allte += te; alld += d
        s = E.score(alld, allte)
        tot[model] = s
        crit[model] = [f"{c['batch']} {c['header'][:28]}（正 {c['truth']} → {x}）" for c, x in zip(allte, alld) if E.score([x], [c])["critical"]]
        L.append(f"| **{model}** | **合計** | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} |")
    a3, b3 = tot["c3a"], tot["c3b"]
    r1 = b3["critical"] <= a3["critical"]
    da = (b3["correct"] / b3["n"] - a3["correct"] / a3["n"]) * 100
    du = (b3["unknown"] / b3["n"] - a3["unknown"] / a3["n"]) * 100
    r2 = da >= 1.5 or du <= -1.5
    L += ["", f"- 重大の列：C3a {crit['c3a'] or 'なし'}／C3b {crit['c3b'] or 'なし'}",
          f"- 判定：規則 1（重大が C3a 以下）{'○' if r1 else '×'}（{a3['critical']}→{b3['critical']}）、規則 2（正 +1.5 以上か不明 −1.5 以上）{'○' if r2 else '×'}"
          f"（正 {da:+.1f}・不明 {du:+.1f} ポイント）→ **{'C3b を次の学習の本命にする' if r1 and r2 else '採らない（金額・件数を外した銀へ）'}**"]
    print("\n".join(L))
    if a.out:
        with open(a.out, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    main()
