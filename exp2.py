"""改良の比較：学習量・正則化・ルールの結果を特徴に足す（ハイブリッド）・評価の値を5通りに変える・列名を崩した評価。"""
import random, sys, time
import numpy as np
from scipy.sparse import csr_matrix, hstack
from sklearn.linear_model import LogisticRegression
from eval_set import EVAL
from eval_values import eval_column
from features import DIM, vectorize, norm_header
from gen import CLASSES, make_train, make_train2
from rules import rule_by_header, rule_by_values
from exp import score

RCLS = CLASSES
def rule_feats(h, v):
    a = rule_by_header(h) if h else None; b = rule_by_values(v) if v else None
    z = np.zeros(2 * len(RCLS) + 2)
    if a: z[RCLS.index(a)] = 1
    else: z[2 * len(RCLS)] = 1
    if b: z[len(RCLS) + RCLS.index(b)] = 1
    else: z[2 * len(RCLS) + 1] = 1
    return z

def mat(rows, hybrid):
    data, ri, ci = [], [], []
    for r, (h, v, _) in enumerate(rows):
        for k, x in vectorize(h, v).items():
            ri.append(r); ci.append(k); data.append(x)
    X = csr_matrix((data, (ri, ci)), shape=(len(rows), DIM))
    if hybrid:
        X = hstack([X, csr_matrix(np.array([rule_feats(h, v) for h, v, _ in rows]))]).tocsr()
    return X

def perturb(rng, h):
    ops = [lambda s: s.lower(), lambda s: s.upper(), lambda s: s.replace(" ", "_"), lambda s: "".join(chr(ord(c)+0xFEE0) if "!" <= c <= "~" else c for c in s),
           lambda s: s + "（必須）", lambda s: "【" + s + "】", lambda s: s + "2", lambda s: s.replace("(円)", "").replace("（円）", ""), lambda s: " " + s + " "]
    return rng.choice(ops)(h)

def eval_rows(seed, mode, pert=False):
    rng = random.Random(seed); out = []
    for _, h, c in EVAL:
        hh = perturb(rng, h) if pert else h
        out.append((hh if mode != "values" else "", eval_column(rng, c) if mode != "header" else [], c))
    return out

def run(n_per, C, hybrid, drop=(0.15, 0.35), verbose=False, return_model=False, v2=False, share=0.4, real=0):
    train = make_train2(n_per_class=n_per, composed_share=share) if v2 else make_train(n_per_class=n_per)
    if real:
        from real_data import real_rows
        train = train + real_rows(copies=real)
    rng = random.Random(7)
    train = [(h if rng.random() > drop[0] else "", v if rng.random() > drop[1] else [], c) for h, v, c in train]
    X = mat(train, hybrid); y = np.array([c for _, _, c in train])
    m = LogisticRegression(C=C, max_iter=4000).fit(X, y)
    out = {}
    for tag, mode, pert in (("both", "both", False), ("header", "header", False), ("values", "values", False), ("崩し", "both", True)):
        accs, wr, cr, un = [], 0, 0, 0
        errs = []
        for seed in range(5):
            ev = eval_rows(100 + seed, mode, pert)
            P = m.predict_proba(mat(ev, hybrid)); pred = [m.classes_[i] for i in P.argmax(1)]
            s = score(pred, [c for *_, c in ev], P.max(1), 0.0)
            accs.append(s["acc_all"]); wr += s["wrong"]; cr += s["critical"]
            errs += [(ev[i][0], t, p) for i, (t, p) in enumerate(zip([c for *_, c in ev], pred)) if t != p]
        out[tag] = (np.mean(accs), wr / 5, cr / 5)
        if verbose and tag == "both":
            from collections import Counter
            print("  誤り（5回分）:", Counter((h, t, p) for h, t, p in errs).most_common(12))
    return (out, m) if return_model else out

if __name__ == "__main__":
    for n_per, C, hyb in [(400, 8, False), (400, 8, True), (800, 8, True), (800, 2, True), (800, 32, True), (1500, 8, True)]:
        t = time.time(); o = run(n_per, C, hyb, verbose=(n_per == 800 and C == 8))
        print(f"n={n_per} C={C} hybrid={hyb}: " + "  ".join(f"{k} {a:.1%}(誤{w:.1f}/重大{c:.1f})" for k, (a, w, c) in o.items()), f"{time.time()-t:.0f}s")
