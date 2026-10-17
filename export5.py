"""v5：v4a（ロジスティック回帰＋文脈＋教材）に、開発用セットの誤りの分析から足した教材（郵便番号の書式・業務ソフトの英語）。
未見セット3で v4c（見張り2）が v4a より悪かったので、見張り2は使わない。"""
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen
from export4 import save
from train3 import build_train, mat
from curriculum import CURRICULUM
import sys
C = float(sys.argv[1]) if len(sys.argv) > 1 else 8
gen.HARD_NUMERIC = 0.0
rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, sorted(CURRICULUM))
X = mat(rows); y = np.array([r[2] for r in rows])
lr = LogisticRegression(C=C, max_iter=3000).fit(X, y)
save(sys.argv[2] if len(sys.argv) > 2 else "model_v5.json", lr, note=f"v5 LR C={C}+文脈+教材（郵便番号・業務ソフトの英語を追加）")
