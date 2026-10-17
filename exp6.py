"""v6 の候補を、開発用セット・自分の評価・くせの列名で比べる（OpenAI の指摘を試す）"""
import json, sys, random
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen, features
from train3 import build_train, mat
from curriculum import CURRICULUM
from export4 import save
import dev_eval
from blind_eval3 import main as _  # noqa
cfgs = [("v5相当", 0.0, False), ("共通の数字0.3", 0.3, False), ("組み合わせ", 0.0, True), ("共通0.3＋組み合わせ", 0.3, True)]
for name, shared, cross in cfgs:
    gen.SHARED_NUMERIC = shared; features.USE_CROSS = cross
    rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, sorted(CURRICULUM))
    X = mat(rows); y = np.array([r[2] for r in rows])
    lr = LogisticRegression(C=8, max_iter=3000).fit(X, y)
    fn = f"cand_{name}.json"; save(fn, lr, note=name)
    m = json.load(open(fn)); m["cross"] = cross; json.dump(m, open(fn, "w"))
    drows = dev_eval.rows_of(); truth = [r[2] for r in drows]
    from exp import score
    s = score([p for p, _ in dev_eval.predict(m, drows)], truth)
    print(f"[{name}] 開発用: 正解{s['correct']}/{s['n']}（{s['acc_all']:.1%}） 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}"); sys.stdout.flush()
