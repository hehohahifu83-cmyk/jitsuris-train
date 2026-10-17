"""v7：v6 ＋ 業務の本物の表（英・加・豪・日本の支出・契約、先生役 Claude のラベル）＋ 8桁コードの見張り。
本物の試験側（表ごとの2割、一般・業務とも）は学習に使わず、比較に残す（exp7.split と同じ分け方）。"""
import json
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen
from blind_eval3 import probs_v4
from curriculum import CURRICULUM
from dev_eval import rows_of
from exp7 import load_real, split, real_train_rows
from export4 import save
from train3 import build_train, mat

gen.HARD_NUMERIC = 0.0
gtr, gte = split(load_real(("materials/real_labels.jsonl",)))
btr, bte = split(load_real(("materials/real_labels_biz.jsonl",)))
rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, sorted(CURRICULUM)) + real_train_rows(gtr, 3, 5, True) + real_train_rows(btr, 3, 6, True)
X = mat(rows); y = np.array([r[2] for r in rows])
lr = LogisticRegression(C=8, max_iter=3000).fit(X, y)
save("model_v7.json", lr, note="v7 LR C=8+文脈+教材+本物の公開表（一般・業務の学習側）+その他の種類")
m = json.load(open("model_v7.json"))
fx_rows = rows_of()[:40] + [(h, v, l, c) for h, v, l, c, _ in gte[:30]] + [(h, v, l, c) for h, v, l, c, _ in bte[:30]]
P = probs_v4(m, mat(fx_rows))
json.dump([{"header": h, "values": v, "context": c, "probs": [float(x) for x in p]} for (h, v, _, c), p in zip(fx_rows, P)],
          open("fixtures_v7.json", "w"), ensure_ascii=False)
print("fixtures_v7", len(fx_rows))
