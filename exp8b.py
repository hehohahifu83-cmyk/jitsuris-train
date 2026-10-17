import numpy as np
from collections import Counter
from sklearn.linear_model import LogisticRegression
import gen
from exp7 import load_real, split, real_train_rows, predict
from train3 import build_train, mat, split_curriculum
gen.HARD_NUMERIC = 0.0
general = load_real(("materials/real_labels.jsonl",)); biz = load_real(("materials/real_labels_biz.jsonl",))
gtr, gte = split(general); btr, bte = split(biz)
train_t, _ = split_curriculum()
rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, train_t) + real_train_rows(gtr, 3, 5, True) + real_train_rows(btr, 3, 6, True)
lr = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), np.array([r[2] for r in rows]))
pred = predict(lr, [(h, v, l, c) for h, v, l, c, _ in bte])
N = {"date", "amount", "quantity", "rate", "id"}
print(Counter((t[2], p) for t, p in zip(bte, pred) if p != t[2] and p != "unknown").most_common(15))
for t, p in zip(bte, pred):
    if p != t[2] and p in N and t[2] in N:
        print(f"  重大 {t[0][:40]!r:44s} 正={t[2]:8s} 予={p:8s} 値={[x[:16] for x in t[1][:3]]}")
