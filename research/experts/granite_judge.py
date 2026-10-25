"""granite の事前記録（bench/granite_expert_20261026.md）の判定を計算する（2026-10-26 Claude）。

判定 1：本体の入れ替え（granite 種子 1・2 の平均 vs C1 種子 1・2 の平均。製品の形）
判定 2：2 つのモデルを専門家として使う（C1 種子 1 の製品の形に、granite 種子 1 の答えで救済・再検査）
使い方：python research/experts/granite_judge.py
"""
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from research.experts import numeric_expert_v2 as V2  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402

NUM = set(V.NUMERIC)
C1 = {"1": "research/merge/preds/c1_{b}.json", "2": "research/merge/preds/seed2_{b}.json"}
GR = {"1": "research/experts/preds/granite_job1_{b}.json", "2": "research/experts/preds/granite_job2_{b}.json"}


def cols_with(pattern):
    te = []
    for b in V2.TEST:
        cs, _ = with_pred(E.load_batch(b), pattern.format(b=b))
        te += cs
    return te


def guarded(pattern):
    out = {}
    for b in V2.TEST:
        for r in json.load(open(pattern.format(b=b), encoding="utf-8"))["rows"]:
            out[r["id"]] = r["guarded_prediction"]
    return out


def main():
    labels = list(V.LABELS)
    train = [c for b in V2.TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    Xtr = np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])
    mv, _, _ = E.fit(Xtr[ok], np.array([c["truth"] for c in train])[ok])

    def prod(pattern):
        te = cols_with(pattern)
        X = np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)])
        P = np.zeros((len(te), len(labels)), dtype="float32")
        p = mv.predict_proba(X)
        for j, lab in enumerate(mv.classes_):
            P[:, labels.index(lab)] = p[:, j]
        return te, V2.product(te, P, labels)

    L = ["## 結果（2026-10-26 Claude。`research/experts/granite_judge.py`）", "", "### 判定 1：本体の入れ替え（製品の形、b013・b014）",
         "| 本体 | 種子 | 結果 | 不明 | 重大 |", "|---|---:|---|---:|---:|"]
    avg = {}
    for name, pats in (("C1（e5-base）", C1), ("granite", GR)):
        accs, crits, unks = [], [], []
        for s, pat in pats.items():
            te, pr = prod(pat)
            sc = E.score([d[0] for d in pr], te)
            accs.append(sc["correct"] / sc["n"]); crits.append(sc["critical"]); unks.append(sc["unknown"] / sc["n"])
            L.append(f"| {name} | {s} | {E.fmt(sc)} | {sc['unknown'] / sc['n']:.1%} | {sc['critical']} |")
            if name.startswith("C1") and s == "1":
                c1_te, c1_prod, n = te, pr, sc["n"]
        avg[name] = (np.mean(accs), np.mean(crits), np.mean(unks))
        L.append(f"| **{name} 平均** | | 正 {np.mean(accs):.1%} | {np.mean(unks):.1%} | {np.mean(crits):.1f} |")
    d_acc = (avg["granite"][0] - avg["C1（e5-base）"][0]) * 100
    if d_acc >= 1.5 and avg["granite"][1] <= avg["C1（e5-base）"][1] and avg["granite"][2] <= 0.10:
        v1 = "入れ替えて良い"
    elif d_acc <= -1.5:
        v1 = "悪い"
    else:
        v1 = "差なし"
    L.append(f"\n- 差：正解率 {d_acc:+.1f} ポイント、重大 {avg['granite'][1] - avg['C1（e5-base）'][1]:+.1f} → **{v1}**")

    g = guarded(GR["1"])
    base = c1_prod
    L += ["", "### 判定 2：2 つのモデルを専門家として使う（C1 種子 1 ＋ granite 種子 1）", "| 形 | 結果 | 不明 | 重大 | 戻した | 下げた |", "|---|---|---:|---:|---:|---:|"]
    s0 = E.score([d[0] for d in base], c1_te)
    L.append(f"| C1 の製品の形 | {E.fmt(s0)} | {s0['unknown'] / s0['n']:.1%} | {s0['critical']} | 0 | 0 |")
    good = []
    for mode in ("救済", "再検査", "救済＋再検査"):
        out, back, down = [], 0, 0
        for c, d in zip(c1_te, base):
            gl = g.get(c["id"])
            raw1 = (c["top3"] or [{}])[0].get("label")
            t2 = [t["label"] for t in (c["top3"] or [])][:2]
            if "救済" in mode and d[0] == "unknown" and gl and gl != "unknown" and gl == raw1 and gl in t2:
                out.append((gl, "two_models")); back += 1; continue
            if "再検査" in mode and d[0] in NUM and gl in NUM and gl != d[0]:
                out.append(("unknown", "two_models_check")); down += 1; continue
            out.append(d)
        s = E.score([d[0] for d in out], c1_te)
        L.append(f"| ＋ {mode} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical']} | {back} | {down} |")
        if s["critical"] <= 0.002 * s["n"] and (s["correct"] - s0["correct"]) / s["n"] * 100 >= 1.0:
            good.append(mode)
    L.append(f"\n- 「良い」（重大 ≤ 0.2% かつ正解率 +1.0 以上）：{good or 'なし'}")
    # 誤りの重なり（見張り後の答え）
    c1g = guarded(C1["1"])
    both = only_c1 = only_g = 0
    for c in c1_te:
        if not V2.scored(c):
            continue
        e1 = c1g[c["id"]] not in (c["truth"], "unknown")
        e2 = g[c["id"]] not in (c["truth"], "unknown")
        both += e1 and e2; only_c1 += e1 and not e2; only_g += e2 and not e1
    L.append(f"- 誤りの重なり（見張り後、言い切った誤り）：両方 {both}・C1 だけ {only_c1}・granite だけ {only_g}")
    print("\n".join(L))
    with open("bench/granite_expert_20261026.md", "a", encoding="utf-8") as f:
        f.write("\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    main()
