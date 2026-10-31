"""辞書の材料：過去の試験（古い 23 陣 b015〜b065、C2 種子 1 の予測）で製品の形が外した列（2026-10-31 Claude）。
D1 の決める陣・確かめる陣（b066〜b090）、封印セット、blind_set*、b018 は使わない。
  python research/dictionary/past_errors.py → research/dictionary/past_errors.md
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
for p in (os.path.join(ROOT, "research"), os.path.join(ROOT, "research", "fixes")):
    sys.path.insert(0, p)
import d1_eval as D  # noqa: E402
import eval_fixes as EF  # noqa: E402


def main():
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm],
                       np.array([c["truth"] for c in train])[okm])
    data = EF.load(EF.DECIDE + EF.CONFIRM)
    cols = {c["id"]: c for cs in data.values() for c in cs}
    per = {}
    EF.run(data, mv, labels, D.PRODUCT, per=per)
    L = ["# 過去の試験で外した列（古い 23 陣、C2 種子 1、製品の形）", "", "| id | 列名 | 値 | 兄弟の列 | 正解 | 最終 | 上位 3 |", "|---|---|---|---|---|---|---|"]
    n = 0
    for k, (final, truth, header, why, *_r) in sorted(per.items()):
        if final == truth:
            continue
        c = cols[k]
        n += 1
        esc = lambda s: str(s).replace("|", "/").replace("\n", " ")  # noqa: E731
        L.append(f"| {k} | {esc(header)[:40]} | {' ・ '.join(esc(v)[:18] for v in c['values'][:6])} | {' ・ '.join(esc(x)[:20] for x in (c.get('context') or [])[:6])} | "
                 f"{truth} | {final} | {', '.join(t['label'] + f'{t['probability']:.2f}' for t in c['top3'])} |")
    L.insert(1, f"- {n} 列。辞書の「過去の試験で知識があれば分かった列」を選ぶ材料。")
    open(os.path.join(HERE, "past_errors.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(n)


if __name__ == "__main__":
    main()
