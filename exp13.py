"""④ 同じ表のほかの列の「予測」を使う後段判定（Sato の考え方の軽量版）。数字の値特徴あり（③）を土台に比べる。
段1：今の仕組み。ほかの列の列名だけで段1が出す種類の分布（平均）を、段2の特徴として足す。"""
import numpy as np
from functools import lru_cache
from scipy.sparse import csr_matrix, hstack
from sklearn.linear_model import LogisticRegression
import gen, features
from exp7 import load_real, split, real_train_rows
from llm_baseline import score_real
from train3 import build_train, mat, split_curriculum, decide
from dev_eval import rows_of
gen.HARD_NUMERIC = 0.0; features.USE_NUM2 = True
gtr, gte = split(load_real(("materials/real_labels.jsonl",))); btr, bte = split(load_real(("materials/real_labels_biz.jsonl",)))
rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, split_curriculum()[0]) + real_train_rows(gtr, 3, 5, True) + real_train_rows(btr, 6, 6, True, per_table=60)
y = np.array([r[2] for r in rows])
tests = {"開発用220": rows_of(), "一般": [(h, v, l, c) for h, v, l, c, _ in gte], "業務": [(h, v, l, c) for h, v, l, c, _ in bte]}
lr1 = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), y); C = list(lr1.classes_)
cache = {}
def hprob(hs):
    need = [h for h in set(hs) if h not in cache]
    if need:
        P = lr1.predict_proba(mat([(h, [], "", None) for h in need]))
        for h, p in zip(need, P): cache[h] = p
def ctxfeat(rs, w):
    hprob([h for r in rs for h in (r[3] or [])])
    M = np.zeros((len(rs), len(C)))
    for i, r in enumerate(rs):
        if r[3]: M[i] = np.mean([cache[h] for h in r[3]], axis=0)
    return csr_matrix(M * w)
def report(name, pred_fn):
    out = []
    for tn, te in tests.items():
        pred = ["unknown" if p == "other" else p for p in decide(C, pred_fn(te), te)]
        s = score_real(pred, [r[2] for r in te]); out.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}")
    print(f"[{name}] " + " ／ ".join(out), flush=True)
report("段1だけ（③）", lambda te: lr1.predict_proba(mat(te)))
for w in (1.0, 3.0):
    X2 = hstack([mat(rows), ctxfeat(rows, w)]).tocsr()
    lr2 = LogisticRegression(C=8, max_iter=3000).fit(X2, y)
    report(f"段2（ほかの列の予測・重み{w}）", lambda te, lr2=lr2, w=w: lr2.predict_proba(hstack([mat(te), ctxfeat(te, w)]).tocsr()))
