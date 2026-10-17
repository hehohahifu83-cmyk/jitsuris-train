"""v6（本物の公開表）と v7（＋業務の本物の表）を、表ごとに分けた本物の試験で比べる。出典ごとにも出す。"""
import sys
from collections import defaultdict
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen
from exp7 import load_real, split, real_train_rows, predict
from llm_baseline import score_real
from train3 import build_train, mat, dev_sets, split_curriculum, tally
from dev_eval import rows_of
gen.HARD_NUMERIC = 0.0
general = load_real(("materials/real_labels.jsonl",)); biz = load_real(("materials/real_labels_biz.jsonl",))
gtr, gte = split(general); btr, bte = split(biz)
train_t, val_t = split_curriculum()
base = build_train({"syn": 1200, "muni": 3, "cur": 8}, train_t)
tests = {"本物（一般）": gte, "本物（業務）": bte}
dev = rows_of()
for name, extra in (("v6相当", real_train_rows(gtr, 3, 5, True)), ("v7（＋業務）", real_train_rows(gtr, 3, 5, True) + real_train_rows(btr, 3, 6, True))):
    rows = base + extra
    lr = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), np.array([r[2] for r in rows]))
    print(f"[{name}] 学習{len(rows)}")
    c, w, u, k = tally(predict(lr, dev), [r[2] for r in dev]); print(f"  開発用220: 正{c/len(dev):.1%} 誤{w} 不明{u} 重大{k}")
    for tn, te in tests.items():
        s = score_real(predict(lr, [(h, v, l, cx) for h, v, l, cx, _ in te]), [r[2] for r in te])
        print(f"  {tn}: 15種類{s['n']}列 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']} ／ その他 見送り{s['other_ok']} 誤答{s['other_ng']}")
    sys.stdout.flush()
