"""通貨の手がかりの無い「金額」を不明にする試し（事前記録 bench/amount_cue_prereg_20261029.md、2026-10-29 Claude）。
製品の形（recheck v1 → 検査役 v2 → ρ=0.8）の最後が amount の列で、見出し・単位の例・値の先頭 5 件に通貨の手がかりが無ければ不明にする。
本体 C2 種子 1、新しい陣 8 つ。決まりの前と後を同じ列で比べる。
使い方：python research/amount_cue_eval.py [--out ...]
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
def has_cue(c):
    return V.has_amount_cue(c.get("header"), c.get("unit"), c.get("values"))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])
    L = ["### 結果（`research/amount_cue_eval.py`、C2 種子 1・製品の形 ρ=0.8）", "", "| 陣 | 決まり | 結果 | 不明 | 重大 |", "|---|---|---|---|---:|"]
    allte, d0s, d1s = [], [], []
    for b in BATCHES:
        te, _ = with_pred(E.load_batch(b), os.path.join(ROOT, "materials", "pool", "work", b, "pred_c2_seed1.json"))
        P = np.zeros((len(te), len(labels)), dtype="float32")
        p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
        for j, lab in enumerate(mv.classes_):
            P[:, labels.index(lab)] = p[:, j]
        idx = list(range(len(te)))
        fin = E.combine(E.base_decisions(te), P, np.zeros(len(te)), labels, TAU, None, idx)
        d0 = []
        for k in idx:
            d = fin[k]
            cand = V.candidate(d[0], d[1], te[k]["pred"], te[k]["top3"], te[k]["header"], P[k], labels, RHO)
            d0.append(cand if cand else d[0])
        d1 = ["unknown" if lab == "amount" and not has_cue(c) else lab for lab, c in zip(d0, te)]
        for tag, d in (("前", d0), ("後", d1)):
            s = E.score(d, te)
            L.append(f"| {b} | {tag} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} |")
        allte += te; d0s += d0; d1s += d1
    s0, s1 = E.score(d0s, allte), E.score(d1s, allte)
    for tag, s in (("前", s0), ("後", s1)):
        L.append(f"| 合計 | {tag} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} |")
    lost = [c["header"][:30] for c, x, y in zip(allte, d0s, d1s) if x != y and c["truth"] == "amount"]
    saved = [f"{c['header'][:30]}（正 {c['truth']}）" for c, x, y in zip(allte, d0s, d1s) if x != y and c["truth"] not in ("amount", "unknown", "S", "")]
    ok_c = s1["critical"] <= s0["critical"]
    ok_w = s1["wrong"] < s0["wrong"]
    ok_a = s1["correct"] / s1["n"] >= s0["correct"] / s0["n"] - 0.005
    L += ["", f"- 不明にした列：{sum(1 for x, y in zip(d0s, d1s) if x != y)}。取りこぼし（本当は amount）{len(lost)}：{lost[:15]}",
          f"- 救った誤り（本当は amount でない）{len(saved)}：{saved[:20]}",
          f"- 判定：重大が増えない {'○' if ok_c else '×'}（{s0['critical']}→{s1['critical']}）・誤りが減る {'○' if ok_w else '×'}（{s0['wrong']}→{s1['wrong']}）・"
          f"正解率の下がり 0.5 ポイント以内 {'○' if ok_a else '×'}（{s0['correct'] / s0['n']:.1%}→{s1['correct'] / s1['n']:.1%}）→ **{'採る' if ok_c and ok_w and ok_a else '採らない'}**"]
    print("\n".join(L))
    if a.out:
        with open(a.out, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    main()
