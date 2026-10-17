"""本物の公開表（先生役 Claude がラベル付け、materials/real_labels.jsonl）を足すと良くなるか。
- 本物の表は「表ごと」に8:2で分け、2割は学習に使わず本物での試験に使う
- 「その他」（15種類に入らない列）を学習に入れる場合は、判定で「その他」→「不明」として出す
- 採点：15種類の列は従来どおり。その他の列は「不明」と答えれば正しく見送り、15種類のどれかを答えれば誤り
未見セット（blind_set*.py）は読まない。"""
import hashlib, json, random, sys, time
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen
from curriculum import CURRICULUM
from train3 import build_train, mat, perturb, dev_sets, split_curriculum, decide, tally
from dev_eval import rows_of

JUNK = {"nan", "None", "", "NaN", "null", "NULL"}


def load_real(files=("materials/real_labels.jsonl", "materials/real_labels_biz.jsonl")):
    import os
    rows = []
    for fn in files:
        if not os.path.exists(fn):
            continue
        rows += [json.loads(l) for l in open(fn, encoding="utf-8")]
    return [(d["header"].lstrip("\ufeff"), [v for v in d["values"] if v.strip() not in JUNK], d["label"], d["context"], d["table"]) for d in rows]


def _old_load_real():
    rows = []
    for l in open("materials/real_labels.jsonl", encoding="utf-8"):
        d = json.loads(l)
        vals = [v for v in d["values"] if v.strip() not in JUNK]
        rows.append((d["header"].lstrip("﻿"), vals, d["label"], d["context"], d["table"]))
    return rows


def split(rows):
    te = lambda t: int(hashlib.md5(t.encode()).hexdigest(), 16) % 5 == 0
    return [r for r in rows if not te(r[4])], [r for r in rows if te(r[4])]


def real_train_rows(rows, copies, seed, keep_other, per_table=30):
    rng = random.Random(seed); out = []
    from collections import defaultdict
    by = defaultdict(list)
    for r in rows:
        by[r[4]].append(r)
    capped = []
    for t, rs in by.items():  # 同じ表の似た列（アンケートの0/1など）が多すぎないように
        capped += rng.sample(rs, per_table) if len(rs) > per_table else rs
    for h, v, lab, ctx, _ in capped:
        if lab == "other" and not keep_other:
            continue
        for _ in range(copies):
            vv = rng.sample(v, max(1, int(len(v) * rng.uniform(0.6, 1.0)))) if v else []
            c = rng.sample(ctx, max(1, int(len(ctx) * rng.uniform(0.4, 1.0)))) if ctx and rng.random() < 0.8 else None
            out.append((perturb(rng, h), vv, lab, c))
    return out


def predict(lr, rows):
    P = lr.predict_proba(mat(rows))
    pred = decide(list(lr.classes_), P, rows)
    return ["unknown" if p == "other" else p for p in pred]


def score_real(pred, truth):
    c = w = u = k = 0; oc = ow = 0
    for p, t in zip(pred, truth):
        if t == "other":
            if p == "unknown": oc += 1
            else: ow += 1
            continue
        if p == "unknown": u += 1
        elif p == t: c += 1
        else:
            w += 1
            if p in {"date", "amount", "quantity", "rate", "id"} and t in {"date", "amount", "quantity", "rate", "id"}: k += 1
    n = c + w + u
    return f"15種類{n}列 正{c / n:.1%} 誤{w} 不明{u} 重大{k} ／ その他{oc + ow}列 見送り{oc} 誤答{ow}"


def run(name, extra, sets, real_test, train_t):
    t0 = time.time()
    gen.HARD_NUMERIC = 0.0
    rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, train_t) + extra
    X = mat(rows); y = np.array([r[2] for r in rows])
    lr = LogisticRegression(C=8, max_iter=3000).fit(X, y)
    out = [f"[{name}] 学習{len(rows)}行 {time.time() - t0:.0f}s"]
    for sn, srows in sets.items():
        c, w, u, k = tally(predict(lr, srows), [r[2] for r in srows]); n = len(srows)
        out.append(f"  {sn}: 正{c / n:.1%} 誤{w} 不明{u} 重大{k}")
    out.append("  本物の試験: " + score_real(predict(lr, [(h, v, l, c) for h, v, l, c, _ in real_test]), [r[2] for r in real_test]))
    print("\n".join(out)); sys.stdout.flush()
    return lr


if __name__ == "__main__":
    real = load_real(); rtr, rte = split(real)
    print("本物：学習", len(rtr), "試験", len(rte))
    train_t, val_t = split_curriculum()
    sets = dev_sets(val_t); sets["開発用220"] = rows_of()
    which = sys.argv[1:] or ["base", "real", "real_other"]
    if "base" in which: run("従来（v5相当・伏せた分野あり）", [], sets, rte, train_t)
    if "real" in which: run("＋本物（その他は除く）", real_train_rows(rtr, 3, 5, False), sets, rte, train_t)
    if "real_other" in which: run("＋本物（その他も学習）", real_train_rows(rtr, 3, 5, True), sets, rte, train_t)
