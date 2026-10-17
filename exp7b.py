"""exp7 の続き：本物の写しの数と、誤りの中身"""
import sys
from collections import Counter
import exp7
from exp7 import *
real = load_real(); rtr, rte = split(real)
train_t, val_t = split_curriculum()
sets = dev_sets(val_t); sets["開発用220"] = rows_of()
for cp in map(int, sys.argv[1:] or ["6", "10"]):
    lr = run(f"＋本物×{cp}（その他も学習）", real_train_rows(rtr, cp, 5, True), sets, rte, train_t)
    pred = predict(lr, [(h, v, l, c) for h, v, l, c, _ in rte])
    errs = Counter((t[2], p) for t, p in zip(rte, pred) if p != t[2] and not (t[2] == "other" and p == "unknown"))
    print("  誤りの組（正→予）:", errs.most_common(12))
    for t, p in zip(rte, pred):
        if p != t[2] and p != "unknown" and not (t[2] == "other" and p == "unknown"):
            print(f"    {t[0][:30]!r:34s} 正={t[2]:9s} 予={p:9s} 値={t[1][:2]}")
