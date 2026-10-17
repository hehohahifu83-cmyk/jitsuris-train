"""ラベルの監査（confident learning の考え方）：本物の表を表ごとに5つに分け、ほかの4つで学んだモデルで残りを判定。
モデルが強く反対する列を「見直す順番」として出す（確定は根拠を見て人＝先生役が決める）。"""
import hashlib, json, sys
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen
from curriculum import CURRICULUM
from exp7 import load_real, real_train_rows
from train3 import build_train, mat

gen.HARD_NUMERIC = 0.0
real = load_real()
fold = lambda t: int(hashlib.md5(("a" + t).encode()).hexdigest(), 16) % 5
base = build_train({"syn": 1200, "muni": 3, "cur": 8}, sorted(CURRICULUM))
out = []
for k in range(5):
    tr = [r for r in real if fold(r[4]) != k]; te = [r for r in real if fold(r[4]) == k]
    rows = base + real_train_rows(tr, 3, 5, True)
    lr = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), np.array([r[2] for r in rows]))
    P = lr.predict_proba(mat([(h, v, l, c) for h, v, l, c, _ in te]))
    C = list(lr.classes_)
    for r, p in zip(te, P):
        i = int(np.argmax(p)); given = C.index(r[2]) if r[2] in C else None
        out.append({"header": r[0], "values": r[1][:3], "table": r[4], "label": r[2], "pred": C[i], "p_pred": float(p[i]),
                    "p_label": float(p[given]) if given is not None else 0.0})
    print("fold", k, "done", flush=True)
sus = sorted([o for o in out if o["pred"] != o["label"]], key=lambda o: o["p_label"] - o["p_pred"])
json.dump(sus, open("materials/audit_suspects.json", "w"), ensure_ascii=False, indent=0)
print("食い違い", len(sus), "/", len(out))
