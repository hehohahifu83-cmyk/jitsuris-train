"""学習能力の引き上げ＋教育（2026-10-16、オーナー指示）。
- 特徴：列名・値・ルールの答え（従来）＋ 同じ表のほかの列名（文脈）
- 教材：合成（gen.py）＋ 自治体標準OD（先生役ラベル）＋ 業務の表の教材（curriculum.py、先生役が書いた）
- モデル：ロジスティック回帰（従来）と、一から作る小さなニューラルネット（numpy）、その組み合わせ
- 検証：教材の表の2割を丸ごと伏せる（分野が違っても当たるか）＋ 既存の評価179件（表ごとに文脈つき）＋ くせのある列名
未見セット（blind_set*.py）は読まない。"""
import json, random, sys, time
from collections import defaultdict
import numpy as np
from scipy.sparse import csr_matrix, hstack
from sklearn.linear_model import LogisticRegression

from curriculum import CURRICULUM
from eval_set import EVAL
from eval_values import eval_column
import features
from features import DIM_CTX, vectorize
from gen import CLASSES, column, make_train2, vary_case, to_fullwidth
from guard import guard_with_reason
from personal_set import PERSONAL
from rules import rule_by_header, rule_by_values

NUMERIC = {"date", "amount", "quantity", "rate", "id"}
R = len(CLASSES)


def rule_feats(h, v):
    z = np.zeros(2 * R + 2)
    a = rule_by_header(h) if h else None
    b = rule_by_values(v) if v else None
    z[CLASSES.index(a) if a else 2 * R] = 1
    z[R + CLASSES.index(b) if b else 2 * R + 1] = 1
    return z


def mat(rows):
    data, ri, ci = [], [], []
    for r, row in enumerate(rows):
        h, v, ctx = row[0], row[1], row[3] if len(row) > 3 else None
        for k, x in vectorize(h, v, context=ctx).items():
            ri.append(r); ci.append(k); data.append(x)
    X = csr_matrix((data, (ri, ci)), shape=(len(rows), features.total_dim()))
    return hstack([X, csr_matrix(np.array([rule_feats(r[0], r[1]) for r in rows]))]).tocsr()


def perturb(rng, h):
    r = rng.random()
    if r < 0.2:
        return vary_case(rng, h)
    if r < 0.28:
        return to_fullwidth(rng, h)
    if r < 0.36:
        return h.replace("_", rng.choice([" ", ""])).replace(" ", rng.choice(["_", "", " "]))
    if r < 0.42:
        return h + rng.choice(["1", "2", "（必須）", "(円)" if "金額" in h or "額" in h else ""])
    return h


def split_curriculum():
    names = sorted(CURRICULUM)
    val = set(names[i] for i in range(len(names)) if i % 5 == 2)
    return [n for n in names if n not in val], sorted(val)


def curriculum_rows(tables, copies, seed):
    rng = random.Random(seed); rows = []
    for t in tables:
        cols = CURRICULUM[t]
        for i, (h, lab) in enumerate(cols):
            others = [c for j, (c, _) in enumerate(cols) if j != i]
            for _ in range(copies):
                ctx = rng.sample(others, max(1, int(len(others) * rng.uniform(0.4, 1.0)))) if rng.random() < 0.8 else None
                rows.append((perturb(rng, h), column(rng, lab), lab, ctx))
    return rows


def municipal_rows(copies, seed):
    from real_data import real_rows
    from materials.teacher_labels import LABELS
    fields = json.load(open("materials/jp_municipal_fields.json", encoding="utf-8"))
    by_ds = defaultdict(list)
    for f in fields:
        by_ds[f["dataset"]].append(f["name"])
    name2ds = {}
    for f in fields:
        name2ds.setdefault(f["name"], f["dataset"])
    rng = random.Random(seed)
    out = []
    for h, v, lab in real_rows(seed=seed, copies=copies):
        ds = name2ds.get(h)
        ctx = rng.sample(by_ds[ds], min(len(by_ds[ds]), 12)) if ds and rng.random() < 0.7 else None
        out.append((h, v, lab, ctx))
    return out


def synthetic_rows(n_per, seed):
    rng = random.Random(seed)
    rows = make_train2(n_per_class=n_per, composed_share=0.4, seed=seed)
    heads = [h for h, _, _ in rows]
    out = []
    for h, v, c in rows:
        ctx = rng.sample(heads, rng.randint(3, 12)) if rng.random() < 0.3 else None
        out.append((h, v, c, ctx))
    return out


def build_train(cfg, train_tables):
    rows = synthetic_rows(cfg["syn"], 1)
    if cfg.get("muni"):
        rows += municipal_rows(cfg["muni"], 11)
    if cfg.get("cur"):
        rows += curriculum_rows(train_tables, cfg["cur"], 21)
    rng = random.Random(7)
    # 列名だけ・値だけでも判断できるように片方を消した例を混ぜる
    return [(h if rng.random() > 0.12 else "", v if rng.random() > 0.3 else [], c, ctx) for h, v, c, ctx in rows]


# ---------- 小さなニューラルネット（numpy、一から） ----------
class MLP:
    def __init__(self, hidden=128, epochs=12, lr=2e-3, l2=1e-5, drop=0.3, seed=0):
        self.h, self.epochs, self.lr, self.l2, self.drop, self.seed = hidden, epochs, lr, l2, drop, seed

    def fit(self, X, y):
        rng = np.random.default_rng(self.seed)
        self.classes_ = np.array(sorted(set(y))); yi = np.searchsorted(self.classes_, y)
        D, H, C = X.shape[1], self.h, len(self.classes_)
        self.W1 = rng.normal(0, np.sqrt(2 / 64), (D, H)).astype(np.float32); self.b1 = np.zeros(H, np.float32)
        self.W2 = rng.normal(0, np.sqrt(2 / H), (H, C)).astype(np.float32); self.b2 = np.zeros(C, np.float32)
        P = [self.W1, self.b1, self.W2, self.b2]; M = [np.zeros_like(p) for p in P]; V = [np.zeros_like(p) for p in P]
        t = 0; X = X.tocsr().astype(np.float32); n = X.shape[0]
        for ep in range(self.epochs):
            idx = rng.permutation(n)
            for s in range(0, n, 256):
                b = idx[s:s + 256]; xb = X[b]; yb = yi[b]
                a1 = xb @ self.W1 + self.b1; h1 = np.maximum(a1, 0)
                mask = (rng.random(h1.shape) > self.drop).astype(np.float32) / (1 - self.drop); h1d = h1 * mask
                z = h1d @ self.W2 + self.b2; z -= z.max(1, keepdims=True); p = np.exp(z); p /= p.sum(1, keepdims=True)
                g = p; g[np.arange(len(b)), yb] -= 1; g /= len(b)
                gW2 = h1d.T @ g + self.l2 * self.W2; gb2 = g.sum(0)
                gh = (g @ self.W2.T) * mask * (a1 > 0)
                gW1 = (xb.T @ gh) + self.l2 * self.W1; gb1 = gh.sum(0)
                t += 1
                for i, gr in enumerate([np.asarray(gW1), gb1, gW2, gb2]):
                    M[i] = 0.9 * M[i] + 0.1 * gr; V[i] = 0.999 * V[i] + 0.001 * gr * gr
                    P[i] -= self.lr * (M[i] / (1 - 0.9 ** t)) / (np.sqrt(V[i] / (1 - 0.999 ** t)) + 1e-8)
        return self

    def predict_proba(self, X):
        h1 = np.maximum(X.astype(np.float32) @ self.W1 + self.b1, 0)
        z = h1 @ self.W2 + self.b2; z -= z.max(1, keepdims=True); p = np.exp(z); return p / p.sum(1, keepdims=True)


# ---------- 評価 ----------
def decide_with_details(classes, P, rows, use_guard=True, thr=0.5, Ph=None):
    """Return labels plus machine-readable reason codes without changing decisions."""
    details = []
    for i, (row, p) in enumerate(zip(rows, P)):
        order = sorted(zip(classes, p), key=lambda x: -x[1])
        raw = order[0][0] if order else None
        reason = None
        if not order or order[0][1] < thr:
            lab = "unknown"
            reason = "probability_below_threshold"
        else:
            lab = order[0][0]
            if use_guard:
                lab, reason = guard_with_reason(lab, order, row[1])
        if Ph is not None and lab in NUMERIC and row[0]:
            hl = classes[int(np.argmax(Ph[i]))]
            if hl in NUMERIC and hl != lab:
                lab = "unknown"
                reason = "header_numeric_disagreement"
        details.append({"raw_prediction": raw, "guarded_prediction": lab,
                        "decision_reason": reason})
    return details


def decide(classes, P, rows, use_guard=True, thr=0.5, Ph=None):
    """Backward-compatible label-only decision API."""
    return [item["guarded_prediction"]
            for item in decide_with_details(classes, P, rows, use_guard, thr, Ph)]


def tally(pred, truth):
    c = w = u = k = 0
    for p, t in zip(pred, truth):
        if p == "unknown": u += 1
        elif p == t: c += 1
        else:
            w += 1
            if p in NUMERIC and t in NUMERIC: k += 1
    return c, w, u, k


def dev_sets(val_tables):
    sets = {}
    rows = []
    for s in range(3):
        rows += curriculum_rows(val_tables, 1, 500 + s)
    sets["伏せた分野"] = [(r[0], r[1], r[2], r[3]) for r in rows]
    by_src = defaultdict(list)
    for src, h, c in EVAL:
        by_src[src].append(h)
    ev = []
    for s in range(3):
        rng = random.Random(100 + s)
        for src, h, c in EVAL:
            ev.append((h, eval_column(rng, c), c, [x for x in by_src[src] if x != h]))
    sets["公開資料179"] = ev
    rng = random.Random(9)
    sets["くせ36"] = [(h, eval_column(rng, c), c, None) for h, c in PERSONAL]
    return sets


def evaluate(models, sets, weights=None, agree=False):
    out = {}
    for name, rows in sets.items():
        X = mat(rows); truth = [r[2] for r in rows]
        w = weights or [1 / len(models)] * len(models)
        P = sum(wi * m.predict_proba(X) for wi, m in zip(w, models))
        Ph = None
        if agree:
            hr = [(r[0], [], r[2], r[3] if len(r) > 3 else None) for r in rows]
            Xh = mat(hr); Ph = sum(wi * m.predict_proba(Xh) for wi, m in zip(w, models))
        out[name] = tally(decide(models[0].classes_, P, rows, Ph=Ph), truth) + (len(rows),)
    return out


def fmt(res):
    return "  ".join(f"{k}: 正{c / n:.1%} 誤{w} 不明{u} 重大{k_}" for k, (c, w, u, k_, n) in res.items())


def main2():
    import gen
    train_t, val_t = split_curriculum()
    sets = dev_sets(val_t)
    for hard in (0.0, 0.3):
        gen.HARD_NUMERIC = hard
        rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, train_t)
        X = mat(rows); y = np.array([r[2] for r in rows])
        lr = LogisticRegression(C=8, max_iter=3000).fit(X, y); mlp = MLP().fit(X, y)
        for tag, ms in (("LR", [lr]), ("LR+NN", [lr, mlp])):
            for agree in (False, True):
                print(f"難しい値={hard} {tag:5s} 見張り2={'あり' if agree else 'なし'}", fmt(evaluate(ms, sets, agree=agree)))
        sys.stdout.flush()


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "2":
    main2(); sys.exit()
if __name__ == "__main__":
    train_t, val_t = split_curriculum()
    print("教材の表：学習", len(train_t), "／伏せる", len(val_t), val_t)
    sets = dev_sets(val_t)
    configs = [
        ("合成のみ", {"syn": 1200}),
        ("合成＋自治体", {"syn": 1200, "muni": 3}),
        ("合成＋教材", {"syn": 1200, "cur": 8}),
        ("合成＋自治体＋教材", {"syn": 1200, "muni": 3, "cur": 8}),
    ]
    for name, cfg in configs:
        t0 = time.time()
        rows = build_train(cfg, train_t)
        X = mat(rows); y = np.array([r[2] for r in rows])
        lr = LogisticRegression(C=8, max_iter=3000).fit(X, y)
        mlp = MLP().fit(X, y)
        print(f"[{name}] 学習 {len(rows)} 行 {time.time() - t0:.0f}s")
        print("  LR      ", fmt(evaluate([lr], sets)))
        print("  NN      ", fmt(evaluate([mlp], sets)))
        print("  LR+NN   ", fmt(evaluate([lr, mlp], sets)))
        sys.stdout.flush()
