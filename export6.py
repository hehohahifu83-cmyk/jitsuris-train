"""v6：v5 ＋ 本物の公開表（先生役 Claude のラベル、表ごとに分けた学習側だけ）＋「その他」の種類（判定では「不明」として人に回す）。
本物の試験側（表の2割）は学習に使わず、大きなAIとの比較に使う（exp7.split と同じ分け方）。"""
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
rtr, rte = split(load_real())
rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, sorted(CURRICULUM)) + real_train_rows(rtr, 3, 5, True)
X = mat(rows); y = np.array([r[2] for r in rows])
lr = LogisticRegression(C=8, max_iter=3000).fit(X, y)
save("model_v6.json", lr, note="v6 LR C=8+文脈+教材+本物の公開表（学習側）+その他の種類")
m = json.load(open("model_v6.json"))
fx_rows = rows_of()[:40] + [(h, v, l, c) for h, v, l, c, _ in rte[:40]]
P = probs_v4(m, mat(fx_rows))
json.dump([{"header": h, "values": v, "context": c, "probs": [float(x) for x in p]} for (h, v, _, c), p in zip(fx_rows, P)],
          open("fixtures_v6.json", "w"), ensure_ascii=False)
print("fixtures_v6", len(fx_rows))
