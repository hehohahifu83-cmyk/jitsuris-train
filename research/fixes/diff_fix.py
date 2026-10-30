"""直しを入れたとき・入れないときで最終の答えが変わった列を並べる（2026-10-30 Claude。懸念点：F7 で増えた重大、F1 で増えた誤り）。
使い方：python research/fixes/diff_fix.py decide F7 ／ python research/fixes/diff_fix.py confirm F1
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import eval_fixes as EF  # noqa: E402

V, E, A = EF.V, EF.E, EF.A


def main():
    mode, fix = sys.argv[1], sys.argv[2]
    labels = list(V.LABELS)
    train = [c for b in A.TRAIN for c in E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    data = EF.load(EF.DECIDE if mode == "decide" else EF.CONFIRM)
    a, b = {}, {}
    EF.run(data, mv, labels, (), a)
    EF.run(data, mv, labels, (fix,), b)
    L = [f"# {fix} で最終の答えが変わった列（{'決める陣' if mode == 'decide' else '確かめる陣'}）", "", "| id | 列名 | 正解 | 直しなし | 直しあり | 直しなしの理由 | 見張り | 値 |", "|---|---|---|---|---|---|---|---|"]
    for i in sorted(a):
        if a[i][0] != b[i][0]:
            fa, t, h, why, g, v, u = a[i]
            mark = "**重大**" if b[i][0] in V.NUMERIC and t in V.NUMERIC and b[i][0] != t else ("正" if b[i][0] == t else ("誤" if b[i][0] != "unknown" else "不明"))
            L.append(f"| {i} | {str(h)[:30].replace('|', '/')} | {t} | {fa} | {b[i][0]}（{mark}） | {why} | {g} | {' / '.join(x[:12] for x in v).replace('|', '/')} |")
    out = os.path.join(HERE, f"diff_{mode}_{fix}.md")
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
