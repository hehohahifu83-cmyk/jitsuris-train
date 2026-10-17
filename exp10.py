"""学習曲線：業務の本物の表の学習側を 0・25・50・75・100% 使ったとき、業務の試験がどう伸びるか（表ごとに間引く）"""
import random
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen
from exp7 import load_real, split, real_train_rows, predict
from llm_baseline import score_real
from train3 import build_train, mat, split_curriculum
gen.HARD_NUMERIC = 0.0
gtr, gte = split(load_real(("materials/real_labels.jsonl",))); btr, bte = split(load_real(("materials/real_labels_biz.jsonl",)))
tables = sorted(set(r[4] for r in btr)); random.Random(1).shuffle(tables)
base = build_train({"syn": 1200, "muni": 3, "cur": 8}, split_curriculum()[0]) + real_train_rows(gtr, 3, 5, True)
for frac in (0, 0.25, 0.5, 0.75, 1.0):
    keep = set(tables[:int(len(tables) * frac)]); sub = [r for r in btr if r[4] in keep]
    rows = base + real_train_rows(sub, 6, 6, True, per_table=60)
    lr = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), np.array([r[2] for r in rows]))
    s = score_real(predict(lr, [(h, v, l, c) for h, v, l, c, _ in bte]), [r[2] for r in bte])
    print(f"業務の表 {int(frac*100):3d}%（{len(keep)}表・{len(sub)}列）: 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}", flush=True)
