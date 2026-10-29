"""決め方の段（rho）の決め直し（事前記録 bench/rho_retune_prereg_20261029.md、2026-10-29 Claude）。

決める陣で 19 通り（ρ × 本体の 1 位の確率の下限 m、と rho なし）を測って 1 つ選び、確かめる陣ではその 1 つと今の形だけを測る。
本体は C2 種子 1（--model で変えられるが、選ぶのは C2 だけ。ほかは記録用）。検査役 v2 は b001〜b014 で学ぶ（c3_eval.py と同じ）。
使い方：python research/rho_tune.py [--out bench/rho_retune_prereg_20261029.md]
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

TUNE = ("b015", "b016", "b017", "b060")
CONFIRM = ("b062", "b063")
TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))
RHOS = (0.7, 0.8, 0.85, 0.9, 0.95, 0.98)
MS = (0.0, 0.5, 0.7)
NOW = (0.7, 0.0)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])

    def prepare(model, batches):
        te = []
        for b in batches:
            cs, _ = with_pred(E.load_batch(b), os.path.join(ROOT, "materials", "pool", "work", b, f"pred_{model}_seed1.json"))
            te += cs
        P = np.zeros((len(te), len(labels)), dtype="float32")
        p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
        for j, lab in enumerate(mv.classes_):
            P[:, labels.index(lab)] = p[:, j]
        idx = list(range(len(te)))
        fin = E.combine(E.base_decisions(te), P, np.zeros(len(te)), labels, TAU, None, idx)
        return te, P, [fin[k] for k in idx]

    def decide(te, P, no_rho, setting):
        if setting is None:
            return no_rho
        rho, m = setting
        out = []
        for k, d in enumerate(no_rho):
            c = V.candidate(d[0], d[1], te[k]["pred"], te[k]["top3"], te[k]["header"], P[k], labels, rho)
            if c and (te[k]["top3"] or [{}])[0].get("probability", 0) < m:
                c = None
            out.append((c, "assert") if c else d)
        return out

    def name(s):
        return "rho なし" if s is None else f"ρ={s[0]}・m={s[1]}"

    def crit_rows(te, decs):
        rows = []
        for c, d in zip(te, decs):
            if E.score([d[0]], [c])["critical"]:
                rows.append(f"{c['header'][:30]}（正 {c['truth']} → {d[0]}）")
        return rows

    L = ["## 結果（`research/rho_tune.py`）", "", "### 決める陣（b015・b016・b017・b060）・本体 C2", "",
         "| 設定 | 結果 | 不明 | 重大 |", "|---|---|---:|---:|"]
    te, P, no_rho = prepare("c2", TUNE)
    settings = [None] + [(r, m) for r in RHOS for m in MS]
    res = {}
    for s in settings:
        sc = E.score([d[0] for d in decide(te, P, no_rho, s)], te)
        res[s] = sc
        L.append(f"| {name(s)} | {E.fmt(sc)} | {sc['unknown'] / sc['n']:.1%} | {sc['critical'] / sc['n']:.2%} |")
    okset = [s for s in settings if s is not None and res[s]["critical"] <= 0.002 * res[s]["n"]]
    if okset:
        pick = sorted(okset, key=lambda s: (-res[s]["correct"], res[s]["critical"], -s[0], -s[1]))[0]
    else:
        pick = None
    L += ["", f"- 重大 ≤ 0.2% を満たす設定：{len(okset)} 通り → 選んだもの：**{name(pick)}**", ""]
    L += ["### 確かめる陣（b062・b063）", "", "| 本体 | 設定 | 結果 | 不明 | 重大 |", "|---|---|---|---:|---:|"]
    verdict = None
    for model in ("c2", "c3a", "c3b"):
        te2, P2, nr2 = prepare(model, CONFIRM)
        for s in ([pick, NOW] if pick != NOW else [NOW]):
            sc = E.score([d[0] for d in decide(te2, P2, nr2, s)], te2)
            L.append(f"| {model} | {name(s)}{'（今）' if s == NOW else '（選んだ）'} | {E.fmt(sc)} | {sc['unknown'] / sc['n']:.1%} | {sc['critical'] / sc['n']:.2%} |")
            if model == "c2":
                if s == pick:
                    picked = sc
                    picked_crit = crit_rows(te2, decide(te2, P2, nr2, s))
                if s == NOW:
                    now = sc
        if model == "c2":
            if pick == NOW:
                picked, picked_crit = now, crit_rows(te2, decide(te2, P2, nr2, NOW))
            ok_c = picked["critical"] <= 0.002 * picked["n"]
            ok_a = picked["correct"] / picked["n"] >= now["correct"] / now["n"] - 0.015
            verdict = (ok_c, ok_a)
    tune_crit = crit_rows(te, decide(te, P, no_rho, pick))
    L += ["", f"- 判定（C2・確かめる陣）：重大 ≤ 0.2% {'○' if verdict[0] else '×'}、正解率が今の形 −1.5 ポイント以内 {'○' if verdict[1] else '×'} → "
          f"**{'採る候補（次の新しい陣でもう一度確かめる）' if all(verdict) else '採らない（今の形のまま）'}**",
          f"- 重大の列（選んだ設定・C2）：決める陣 {tune_crit or 'なし'}／確かめる陣 {picked_crit or 'なし'}"]
    print("\n".join(L))
    if a.out:
        with open(a.out, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    main()
