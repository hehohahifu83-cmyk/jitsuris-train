"""開発用セット（dev_set.py、Claude が中身を見て直してよい）での評価と誤りの一覧。blind_eval3 と同じ判定のしかた。"""
import json, random, sys
from collections import defaultdict, Counter
import numpy as np
from blind_eval3 import probs_v4, NUMERIC
from eval_values import eval_column
from exp import score
from guard import guard
from rules import rule
from train3 import mat
import dev_set


def rows_of(seed=20261018):
    by = defaultdict(list)
    for r in dev_set.DEV:
        by[r[0]].append(r[-2])
    rng = random.Random(seed)
    return [(r[-2], eval_column(rng, r[-1]), r[-1], [h for h in by[r[0]] if h != r[-2]]) for r in dev_set.DEV]


def predict(m, rows, models=None):
    import features
    features.USE_NUM2 = bool(m.get("num2"))  # モデルごとに特徴の並びを合わせる
    C = m["classes"]; P = probs_v4(m, mat(rows))
    Ph = probs_v4(m, mat([(h, [], c, ctx) for h, _, c, ctx in rows])) if m.get("agree_guard") else None
    out = []
    for i, ((h, v, _, _), p) in enumerate(zip(rows, P)):
        order = sorted(zip(C, p), key=lambda x: -x[1])
        lab = order[0][0] if order[0][1] >= m["threshold"] else "unknown"
        if lab != "unknown":
            lab = guard(lab, order, v)
        if Ph is not None and lab in NUMERIC and h:
            hl = C[int(np.argmax(Ph[i]))]
            if hl in NUMERIC and hl != lab:
                lab = "unknown"
        out.append((lab, order[0]))
    return out


if __name__ == "__main__":
    rows = rows_of(); truth = [r[2] for r in rows]
    s = score([rule(h, v) for h, v, _, _ in rows], truth)
    print(f"ルール: 正解={s['correct']}/{s['n']}（{s['acc_all']:.1%}） 誤り={s['wrong']} 不明={s['unknown']} 重大={s['critical']}")
    for path in sys.argv[1:]:
        m = json.load(open(path))
        if m.get("version") != 4:
            print(path, "（v4 形式でないので省略）"); continue
        pr = predict(m, rows)
        s = score([p for p, _ in pr], truth)
        print(f"{path}: 正解={s['correct']}/{s['n']}（{s['acc_all']:.1%}） 誤り={s['wrong']} 不明={s['unknown']} 重大={s['critical']}")
        if "-v" in sys.argv[0:1] or path == sys.argv[1]:
            for (h, v, t, _), (p, top) in zip(rows, pr):
                if p != t:
                    print(f"   {'重大' if p in NUMERIC and t in NUMERIC else '    '} {h!r:40s} 正={t:9s} 予={p:9s} ({top[0]} {top[1]:.2f}) 値={v[:2]}")
