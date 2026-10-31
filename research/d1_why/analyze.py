"""D1 で V・U が伸びなかった原因を数える（2026-10-31 Claude。決める陣だけ。確かめる陣は見ない）。

1. V・U が本体の入力を変えた列の数（予測の入力を A と比べる）と、その列での結果の変化
2. A の誤りがどの段で起きたか（本体の 1 位が正しいのに後ろの段で外れた／本体の 1 位が違うが 3 位以内／3 位にもない）
3. A の誤りの正解の種類・列名の形
  python research/d1_why/analyze.py → research/d1_why/findings_data.md
"""
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "research"))
import numpy as np  # noqa: E402
import evaluate_independent as EI  # noqa: E402
import d1_eval as D  # noqa: E402

FOLDER = os.path.join(ROOT, "materials", "pool", "work", "d1dec")


def main():
    set_data = json.load(open(os.path.join(FOLDER, "set.json"), encoding="utf-8"))
    base_rows = EI.model_rows_of(set_data, {})
    v_rows = EI.model_rows_of(set_data, {"val_select": True})
    u_rows = EI.model_rows_of(set_data, {"unit_ext": True})
    ids = [c["id"] for c in set_data["columns"]]
    v_changed = {i for i, a, b in zip(ids, base_rows, v_rows) if a != b}
    u_changed = {i for i, a, b in zip(ids, base_rows, u_rows) if a != b}

    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = D.load_side("decide")
    per, raw = {}, {}
    for j in D.JOBS:
        D.EF._PCACHE.clear()
        data = D.with_job(base, os.path.join(FOLDER, f"pred_d1_job{j}.json"))
        p = {}
        D.EF.run(data, mv, labels, D.PRODUCT, per=p)
        per[j] = p
        preds = json.load(open(os.path.join(FOLDER, f"pred_d1_job{j}.json"), encoding="utf-8"))["rows"]
        raw[j] = {r["id"]: r for r in preds}
    scored = set(per[1])
    L = ["# D1 が伸びなかった原因の数（決める陣、`research/d1_why/analyze.py`）", ""]

    L += ["## 1. V・U が本体の入力を変えた列", "", "| 形 | 入力が変わった列（set 1,620 列） | うち採点する列 | その列で A→形 の正しい（種子 1・2） |", "|---|---:|---:|---|"]
    for name, ch, js in (("V", v_changed, (3, 4)), ("U", u_changed, (5, 6))):
        sc = ch & scored
        moves = []
        for a, b in zip((1, 2), js):
            ok_a = sum(per[a][k][0] == per[a][k][1] for k in sc)
            ok_b = sum(per[b][k][0] == per[b][k][1] for k in sc)
            moves.append(f"{ok_a}→{ok_b}")
        L.append(f"| {name} | {len(ch)} | {len(sc)} | {'・'.join(moves)} |")
    # 入力が変わっていない列で結果が変わった数（重みが違うことによるゆれ）
    for name, ch, js in (("V", v_changed, (3, 4)), ("U", u_changed, (5, 6))):
        same = scored - ch
        flips = [sum((per[a][k][0] == per[a][k][1]) != (per[b][k][0] == per[b][k][1]) for k in same) for a, b in zip((1, 2), js)]
        L.append(f"- {name}：入力が同じ列 {len(same)} のうち、A と正誤が入れ替わった列 種子 1 {flips[0]}・種子 2 {flips[1]}（学習のゆれ）")
    ab = sum((per[1][k][0] == per[1][k][1]) != (per[2][k][0] == per[2][k][1]) for k in scored)
    L.append(f"- 参考：A の種子 1 と種子 2 で正誤が入れ替わった列 {ab}（同じ設定の学習のゆれ）")

    L += ["", "## 2. A の誤りの段（種子 1・2）", "", "| 段 | 種子 1 | 種子 2 |", "|---|---:|---:|"]
    stages = {}
    for j in (1, 2):
        c = Counter()
        for k in scored:
            final, truth = per[j][k][0], per[j][k][1]
            if final == truth:
                continue
            r = raw[j][k]
            top = [t["label"] for t in r["top3"]]
            if r["raw_prediction"] == truth:
                c["本体の 1 位は正しい → 見張り・後ろの段で外れた（不明）" if final == "unknown" else "本体の 1 位は正しい → 後ろの段で別の種類に"] += 1
            elif truth in top:
                c["本体の 1 位は違う・正解は 3 位以内"] += 1
            else:
                c["正解が本体の 3 位にもない"] += 1
        stages[j] = c
    for s in sorted(set(stages[1]) | set(stages[2])):
        L.append(f"| {s} | {stages[1][s]} | {stages[2][s]} |")
    L += ["", "### 本体の 1 位が正しいのに外れた列の理由（種子 1・2）", "", "| 理由 | 種子 1 | 種子 2 |", "|---|---:|---:|"]
    rs = {}
    for j in (1, 2):
        rs[j] = Counter(str(per[j][k][3]).split(":")[0] for k in scored
                        if per[j][k][0] != per[j][k][1] and raw[j][k]["raw_prediction"] == per[j][k][1])
    for s in sorted(set(rs[1]) | set(rs[2]), key=lambda s: -(rs[1][s] + rs[2][s])):
        L.append(f"| {s} | {rs[1][s]} | {rs[2][s]} |")
    L += ["", "### 正解が 3 位以内の列：本体の 1 位 → 正解（種子 1、多い順）", ""]
    pairs = Counter((raw[1][k]["raw_prediction"], per[1][k][1]) for k in scored
                    if per[1][k][0] != per[1][k][1] and raw[1][k]["raw_prediction"] != per[1][k][1]
                    and per[1][k][1] in [t["label"] for t in raw[1][k]["top3"]])
    L += [f"- {a} → {b}：{n}" for (a, b), n in pairs.most_common(15)]

    L += ["", "## 3. A（種子 1）の誤りの正解の種類と、どう外れたか", "", "| 正解 | 誤り（不明を含む） | 不明 | 別の種類（多い順） |", "|---|---:|---:|---|"]
    by = {}
    for k in scored:
        final, truth = per[1][k][0], per[1][k][1]
        if final != truth:
            by.setdefault(truth, Counter())[final] += 1
    for t, c in sorted(by.items(), key=lambda x: -sum(x[1].values())):
        other = ", ".join(f"{a} {n}" for a, n in c.most_common() if a != "unknown")
        L.append(f"| {t} | {sum(c.values())} | {c['unknown']} | {other} |")
    L += ["", "## 4. A の種子 1・2 の両方で誤った列（一部）", ""]
    both = [k for k in scored if per[1][k][0] != per[1][k][1] and per[2][k][0] != per[2][k][1]]
    L.append(f"両方で誤り {len(both)} 列。")
    L += ["", "| id | 正解 | 答え（1・2） | 本体の 1 位 | 理由 | 列名 | 値 |", "|---|---|---|---|---|---|---|"]
    for k in sorted(both)[:80]:
        p1, p2 = per[1][k], per[2][k]
        L.append(f"| {k} | {p1[1]} | {p1[0]}・{p2[0]} | {raw[1][k]['raw_prediction']} | {p1[3]} | {p1[2][:30]} | {' / '.join(p1[5][:3])[:50]} |")
    open(os.path.join(HERE, "findings_data.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:60]))


if __name__ == "__main__":
    main()
