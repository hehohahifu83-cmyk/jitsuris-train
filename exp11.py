"""許容量と理解力（組み合わせ）の比較（本物の表で）。業務の写し6・上限60。"""
import sys
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen, features
from exp7 import load_real, split, real_train_rows
from llm_baseline import score_real
from train3 import build_train, mat, split_curriculum, decide
gen.HARD_NUMERIC = 0.0
gtr, gte = split(load_real(("materials/real_labels.jsonl",))); btr, bte = split(load_real(("materials/real_labels_biz.jsonl",)))
rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, split_curriculum()[0]) + real_train_rows(gtr, 3, 5, True) + real_train_rows(btr, 6, 6, True, per_table=60)
y = np.array([r[2] for r in rows])
tests = {"一般": [(h, v, l, c) for h, v, l, c, _ in gte], "業務": [(h, v, l, c) for h, v, l, c, _ in bte]}
CFG = {"今（4k/2k/512）": dict(), "大（16k/8k/2k）": dict(h=16384, v=8192, ctx=2048), "大＋組み合わせ": dict(h=16384, v=8192, ctx=2048, x=4096, cross=True),
       "今＋組み合わせ": dict(x=2048, cross=True)}
for name in sys.argv[1:] or CFG:
    features.set_dims(**CFG[name]); X = mat(rows)
    for C in (8, 16):
        lr = LogisticRegression(C=C, max_iter=4000).fit(X, y)
        out = []
        for tn, te in tests.items():
            P = lr.predict_proba(mat(te)); pred = ["unknown" if p == "other" else p for p in decide(list(lr.classes_), P, te)]
            s = score_real(pred, [r[2] for r in te]); out.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}")
        print(f"[{name} C={C} 次元{X.shape[1]}] " + " ／ ".join(out), flush=True)
