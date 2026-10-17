"""① 教材を増やす（業務の表2回目 biz2＋カナダ契約 direct）の効き目。数字の値特徴あり（v8 候補の作り）。試験は固定：開発用220・一般・業務（1回目）・業務2回目の試験側。"""
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen, features
from exp7 import load_real, split, real_train_rows
from llm_baseline import score_real
from train3 import build_train, mat, split_curriculum, decide
from dev_eval import rows_of
gen.HARD_NUMERIC = 0.0
features.USE_NUM2 = True
gtr, gte = split(load_real(("materials/real_labels.jsonl",))); btr, bte = split(load_real(("materials/real_labels_biz.jsonl",)))
b2tr, b2te = split(load_real(("materials/real_labels_biz2.jsonl", "materials/real_labels_direct.jsonl")))
base = build_train({"syn": 1200, "muni": 3, "cur": 8}, split_curriculum()[0]) + real_train_rows(gtr, 3, 5, True) + real_train_rows(btr, 6, 6, True, per_table=60)
T = lambda d: [(h, v, l, c) for h, v, l, c, _ in d]
tests = {"開発用220": rows_of(), "一般": T(gte), "業務": T(bte), "業務2": T(b2te)}
print("業務2 学習", len(b2tr), "試験", len(b2te), flush=True)
import sys
GRID = [("土台（v7＋数字特徴）", [], 8), ("＋業務2（×6）", real_train_rows(b2tr, 6, 7, True, per_table=60), 8)]
if "--sweep" in sys.argv:
    GRID = [("＋業務2（×6・表あたり20）", real_train_rows(b2tr, 6, 7, True, per_table=20), 8),
            ("＋業務2（×2・表あたり60）", real_train_rows(b2tr, 2, 7, True, per_table=60), 8),
            ("＋業務2（×6）C=4", real_train_rows(b2tr, 6, 7, True, per_table=60), 4),
            ("＋業務2（×6）C=16", real_train_rows(b2tr, 6, 7, True, per_table=60), 16)]
for name, extra, C in GRID:
    rows = base + extra; y = np.array([r[2] for r in rows])
    lr = LogisticRegression(C=C, max_iter=3000).fit(mat(rows), y); out = []
    for tn, te in tests.items():
        pred = ["unknown" if p == "other" else p for p in decide(list(lr.classes_), lr.predict_proba(mat(te)), te)]
        s = score_real(pred, [r[2] for r in te]); out.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}")
    print(f"[{name}] " + " ／ ".join(out), flush=True)
