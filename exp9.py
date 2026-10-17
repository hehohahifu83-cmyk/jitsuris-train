"""v7 の教え方の調整（業務の写しの数・正則化 C・1表あたりの上限）。本物の試験は開発用として使う（最終判定は ChatGPT の未見セット）。"""
import sys, itertools
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen
from exp7 import load_real, split, real_train_rows, predict
from llm_baseline import score_real
from train3 import build_train, mat, split_curriculum
gen.HARD_NUMERIC = 0.0
gtr, gte = split(load_real(("materials/real_labels.jsonl",))); btr, bte = split(load_real(("materials/real_labels_biz.jsonl",)))
train_t, _ = split_curriculum()
base = build_train({"syn": 1200, "muni": 3, "cur": 8}, train_t)
for cp, C, cap in [(3, 8, 30), (6, 8, 30), (6, 8, 60), (6, 16, 60), (10, 8, 60)]:
    rows = base + real_train_rows(gtr, 3, 5, True) + real_train_rows(btr, cp, 6, True, per_table=cap)
    lr = LogisticRegression(C=C, max_iter=3000).fit(mat(rows), np.array([r[2] for r in rows]))
    out = []
    for tn, te in (("一般", gte), ("業務", bte)):
        s = score_real(predict(lr, [(h, v, l, c) for h, v, l, c, _ in te]), [r[2] for r in te])
        out.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}")
    print(f"写し{cp} C={C} 上限{cap}: " + " ／ ".join(out), flush=True)
