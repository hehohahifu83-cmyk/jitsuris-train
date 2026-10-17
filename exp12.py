"""③ 数字の列の値特徴の追加（USE_NUM2）の効き目。同じ学習データ（v7 と同じ作り）・同じ試験。"""
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen, features
from exp7 import load_real, split, real_train_rows
from llm_baseline import score_real
from train3 import build_train, mat, split_curriculum, decide
from dev_eval import rows_of
gen.HARD_NUMERIC = 0.0
gtr, gte = split(load_real(("materials/real_labels.jsonl",))); btr, bte = split(load_real(("materials/real_labels_biz.jsonl",)))
rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, split_curriculum()[0]) + real_train_rows(gtr, 3, 5, True) + real_train_rows(btr, 6, 6, True, per_table=60)
y = np.array([r[2] for r in rows])
tests = {"開発用220": rows_of(), "一般": [(h, v, l, c) for h, v, l, c, _ in gte], "業務": [(h, v, l, c) for h, v, l, c, _ in bte]}
for flag in (False, True):
    features.USE_NUM2 = flag
    lr = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), y); out = []
    for tn, te in tests.items():
        pred = ["unknown" if p == "other" else p for p in decide(list(lr.classes_), lr.predict_proba(mat(te)), te)]
        s = score_real(pred, [r[2] for r in te]); out.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}")
    print(f"[数字の値特徴 {'あり' if flag else 'なし'}] " + " ／ ".join(out), flush=True)
