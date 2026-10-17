"""実験：ルール（AIなし）と小さなAIを、評価用の公開資料の列名で比べる。
合格（オーナー承認時に ChatGPT と合意）：正解率90%以上、誤りがルールの半分以下、重大な誤り0、分からないときは「不明」。
重大な誤り：日付・金額・数量・率・番号のあいだの取り違え（会計の取り込みで数字が壊れるもの）。
"""
import json
import random
import sys
import time
from collections import Counter

import numpy as np
from scipy.sparse import csr_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

from eval_set import EVAL
from features import DIM, vectorize
from gen import CLASSES, column, make_train
from eval_values import eval_column
from rules import rule

NUMERIC = {"date", "amount", "quantity", "rate", "id"}


def matrix(rows, **kw):
    data, ri, ci = [], [], []
    for r, (h, vals, _) in enumerate(rows):
        for k, v in vectorize(h, vals, **kw).items():
            ri.append(r); ci.append(k); data.append(v)
    return csr_matrix((data, (ri, ci)), shape=(len(rows), DIM))


def eval_rows(seed, mode="both"):
    rng = random.Random(seed)
    out = []
    for src, h, c in EVAL:
        vals = eval_column(rng, c) if mode != "header" else []
        out.append((h if mode != "values" else "", vals, c))
    return out


def score(pred, truth, conf=None, thr=0.0):
    n = len(truth); ans = wrong = crit = unk = 0
    errs = []
    for i, (p, t) in enumerate(zip(pred, truth)):
        if p == "unknown" or (conf is not None and conf[i] < thr):
            unk += 1; continue
        ans += 1
        if p != t:
            wrong += 1; errs.append((t, p))
            if p in NUMERIC and t in NUMERIC:
                crit += 1
    return {"n": n, "correct": n - wrong - unk, "wrong": wrong, "unknown": unk, "critical": crit,
            "acc_all": round((n - wrong - unk) / n, 3), "acc_answered": round((ans - wrong) / max(1, ans), 3), "errs": errs}


def main():
    t0 = time.time()
    train = make_train(n_per_class=int(sys.argv[1]) if len(sys.argv) > 1 else 500)
    # 列名だけ・値だけでも判断できるよう、学習時に片方を消した例を混ぜる（どちらかに頼りきらないため）
    rng = random.Random(7)
    train = [(h if rng.random() > 0.15 else "", v if rng.random() > 0.35 else [], c) for h, v, c in train]
    X = matrix(train); y = np.array([c for _, _, c in train])
    seen = Counter(h for h, _, _ in train)
    overlap = sum(1 for _, h, _ in EVAL if h in seen)
    print(f"学習 {len(train)} 列、評価 {len(EVAL)} 列（評価の列名のうち学習と完全一致 {overlap}）")
    res = {}
    models = {
        "LR": LogisticRegression(C=8, max_iter=3000),
        "MLP": MLPClassifier(hidden_layer_sizes=(64,), alpha=1e-4, max_iter=60, early_stopping=True, random_state=0),
    }
    for mode in ("both", "header", "values"):
        ev = eval_rows(99, mode)
        truth = [c for _, _, c in ev]
        rp = [rule(h, v) for h, v, _ in ev]
        res[("rules", mode)] = score(rp, truth)
    for name, m in models.items():
        m.fit(X, y)
        for mode in ("both", "header", "values"):
            ev = eval_rows(99, mode)
            truth = [c for _, _, c in ev]
            P = m.predict_proba(matrix(ev))
            pred = [m.classes_[i] for i in P.argmax(1)]
            conf = P.max(1)
            res[(name, mode)] = score(pred, truth)
            for thr in (0.5, 0.7):
                res[(name + f"@{thr}", mode)] = score(pred, truth, conf, thr)
    for (name, mode), s in res.items():
        print(f"{name:8s} {mode:6s} 正解 {s['correct']:3d}/{s['n']}（{s['acc_all']:.1%}） 誤り {s['wrong']:2d} 不明 {s['unknown']:2d} 重大 {s['critical']}  答えた中の正解率 {s['acc_answered']:.1%}")
    print("秒", round(time.time() - t0, 1))
    return res, models


if __name__ == "__main__":
    main()
