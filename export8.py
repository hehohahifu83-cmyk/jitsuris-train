"""v8：v7 ＋ 数字の列の値特徴（num2）＋ 業務の表2回目（英・アイルランド・日本・カナダ、先生役 Claude）＋ カナダ連邦の契約。
本物の試験側（表ごとの2割）は学習に使わず、比較に残す（exp7.split と同じ分け方）。重みは exp15 で選んだもの（業務・業務2とも ×6、表あたり60）。"""
import json
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen, features
from blind_eval3 import probs_v4
from curriculum import CURRICULUM
from dev_eval import rows_of
from exp7 import load_real, split, real_train_rows
from export4 import save
from train3 import build_train, mat

gen.HARD_NUMERIC = 0.0
features.USE_NUM2 = True
gtr, gte = split(load_real(("materials/real_labels.jsonl",)))
btr, bte = split(load_real(("materials/real_labels_biz.jsonl",)))
b2tr, b2te = split(load_real(("materials/real_labels_biz2.jsonl", "materials/real_labels_direct.jsonl")))
rows = (build_train({"syn": 1200, "muni": 3, "cur": 8}, sorted(CURRICULUM)) + real_train_rows(gtr, 3, 5, True)
        + real_train_rows(btr, 6, 6, True, per_table=60) + real_train_rows(b2tr, 6, 7, True, per_table=60))
X = mat(rows); y = np.array([r[2] for r in rows])
lr = LogisticRegression(C=8, max_iter=3000).fit(X, y)
save("model_v8.json", lr, note="v8 LR C=8+文脈+教材+本物の公開表（一般・業務・業務2の学習側）+その他+数字の値特徴")
m = json.load(open("model_v8.json"))
T = lambda d: [(h, v, l, c) for h, v, l, c, _ in d]
fx_rows = rows_of()[:40] + T(gte[:30]) + T(bte[:30]) + T(b2te[:40])
P = probs_v4(m, mat(fx_rows))
json.dump([{"header": h, "values": v, "context": c, "probs": [float(x) for x in p]} for (h, v, _, c), p in zip(fx_rows, P)],
          open("fixtures_v8.json", "w"), ensure_ascii=False)
print("fixtures_v8", len(fx_rows), "num2", m.get("num2"))
