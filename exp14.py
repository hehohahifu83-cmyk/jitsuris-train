"""⑤ しきい値（自信がこれ未満なら不明）と、数字の種類どうしで迷うときの差の幅の効き目。③（数字の値特徴あり）で。
しきい値は「検証用」（学習側の表の一部を伏せる）で選び、試験側は確認だけに使う。"""
import hashlib
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen, features, guard as G
from exp7 import load_real, split, real_train_rows
from llm_baseline import score_real
from train3 import build_train, mat, split_curriculum
from dev_eval import rows_of
gen.HARD_NUMERIC = 0.0; features.USE_NUM2 = True
gtr, gte = split(load_real(("materials/real_labels.jsonl",))); btr, bte = split(load_real(("materials/real_labels_biz.jsonl",)))
val = lambda t: int(hashlib.md5(("v" + t).encode()).hexdigest(), 16) % 5 == 0
gtr2, gva = [r for r in gtr if not val(r[4])], [r for r in gtr if val(r[4])]
btr2, bva = [r for r in btr if not val(r[4])], [r for r in btr if val(r[4])]
rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, split_curriculum()[0]) + real_train_rows(gtr2, 3, 5, True) + real_train_rows(btr2, 6, 6, True, per_table=60)
lr = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), np.array([r[2] for r in rows])); C = list(lr.classes_)
N = {"date", "amount", "quantity", "rate", "id"}
def decide2(P, rs, thr, margin):
    out = []
    for r, p in zip(rs, P):
        order = sorted(zip(C, p), key=lambda x: -x[1]); lab = order[0][0] if order[0][1] >= thr else "unknown"
        if lab != "unknown":
            g = G.guard(lab, [(order[0][0], 1.0), (order[1][0], 0.0)], r[1])  # 値との食い違いの見張りだけ使う
            lab = g
            a, pa = order[0]; b, pb = order[1]
            if lab != "unknown" and a in N and b in N and pa - pb < margin: lab = "unknown"
        out.append("unknown" if lab == "other" else lab)
    return out
sets = {"検証（一般）": gva, "検証（業務）": bva, "試験（一般）": gte, "試験（業務）": bte}
P = {k: lr.predict_proba(mat([(h, v, l, c) for h, v, l, c, _ in rs])) for k, rs in sets.items()}
for thr in (0.3, 0.4, 0.5, 0.6):
    for margin in (0.1, 0.25, 0.4):
        out = []
        for k, rs in sets.items():
            s = score_real(decide2(P[k], rs, thr, margin), [r[2] for r in rs]); out.append(f"{k} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}")
        print(f"しきい値{thr} 差{margin}: " + " ／ ".join(out), flush=True)
