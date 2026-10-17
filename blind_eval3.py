"""未見セット3での一度だけの評価（v4 形式のモデル用。ChatGPT が実行し、Claude は集計だけを見る）。
使い方: python3 blind_eval3.py blind_set3 model_v4c.json model_v4a.json model_v4b.json model_v2.json
- 同じ出典URLの列を「同じ表」とみなし、ほかの列名を文脈として使う
- 出力は集計だけ（列名ごとの誤りは出さない）。事前に決めた第一候補：model_v4c.json"""
import base64, importlib, json, random, sys
from collections import defaultdict
import numpy as np
from eval_values import eval_column
from exp import score
from guard import guard
from rules import rule

NUMERIC = {"date", "amount", "quantity", "rate", "id"}


def deq(b64, scale, shape):
    return np.frombuffer(base64.b64decode(b64), dtype=np.int8).astype(np.float64).reshape(shape) * np.asarray(scale)[:, None]


def probs_v4(m, X):
    C = len(m["classes"])
    W = deq(m["lr"]["weights_b64"], m["lr"]["scale"], (C, m["dim"]))
    z = X @ W.T + np.asarray(m["lr"]["bias"]); z -= z.max(1, keepdims=True); P = np.exp(z); P /= P.sum(1, keepdims=True)
    if "mlp" in m:
        H = m["mlp"]["hidden"]
        W1 = deq(m["mlp"]["W1T_b64"], m["mlp"]["s1"], (H, m["dim"])); W2 = deq(m["mlp"]["W2T_b64"], m["mlp"]["s2"], (C, H))
        h = np.maximum(X @ W1.T + np.asarray(m["mlp"]["b1"]), 0)
        z2 = h @ W2.T + np.asarray(m["mlp"]["b2"]); z2 -= z2.max(1, keepdims=True); P2 = np.exp(z2); P2 /= P2.sum(1, keepdims=True)
        P = (P + P2) / 2
    return P


def main():
    mod = importlib.import_module(sys.argv[1])
    SET = next(v for k, v in vars(mod).items() if k.isupper() and isinstance(v, list) and v and isinstance(v[0], (tuple, list)) and len(v[0]) >= 3)
    by = defaultdict(list)
    for r in SET:
        by[r[0]].append(r[1])
    rng = random.Random(20261017)
    # 形式：(出典, 列名, 正解) なら値は eval_values で作る／(出典, 列名, [本物の値…], 正解) なら渡された値を使う（セット5〜）
    rows = [(r[1], list(r[2]) if len(r) >= 4 and isinstance(r[2], (list, tuple)) else eval_column(rng, r[-1]), r[-1], [h for h in by[r[0]] if h != r[1]]) for r in SET]
    has_other = any(r[2] == "other" for r in rows)
    truth = [r[2] for r in rows]
    s = score([rule(h, v) for h, v, _, _ in rows], truth)
    print(f"ルール: n={s['n']} 正解={s['correct']}（{s['acc_all']:.1%}） 誤り={s['wrong']} 不明={s['unknown']} 重大={s['critical']}")
    for path in sys.argv[2:]:
        m = json.load(open(path, encoding="utf-8"))
        if m.get("version") != 4:
            from exp2 import mat as mat2
            C = m["classes"]
            W = np.frombuffer(base64.b64decode(m["weights_b64"]), dtype=np.int8).astype(np.float64).reshape(len(C), m["dim"]) * np.asarray(m["scale"])[:, None]
            X = mat2([(h, v, c) for h, v, c, _ in rows], True)
            z = X @ W.T + np.asarray(m["bias"]); z -= z.max(1, keepdims=True); P = np.exp(z); P /= P.sum(1, keepdims=True); Ph = None
        else:
            from train3 import mat
            import features
            features.USE_NUM2 = bool(m.get("num2"))  # モデルごとに特徴の並びを合わせる
            C = m["classes"]; P = probs_v4(m, mat(rows))
            Ph = probs_v4(m, mat([(h, [], c, ctx) for h, _, c, ctx in rows])) if m.get("agree_guard") else None
        pred = []
        for i, ((h, v, _, _), p) in enumerate(zip(rows, P)):
            order = sorted(zip(C, p), key=lambda x: -x[1])
            lab = order[0][0] if order[0][1] >= m["threshold"] else "unknown"
            if lab != "unknown":
                lab = guard(lab, order, v)
            if Ph is not None and lab in NUMERIC and h:
                hl = C[int(np.argmax(Ph[i]))]
                if hl in NUMERIC and hl != lab:
                    lab = "unknown"
            pred.append(lab)
        if has_other:  # 15種類に入らない列（other）を含むセット：その他は「不明」と答えれば正しい見送り
            from llm_baseline import score_real
            s = score_real(pred, truth)
            print(f"{path}: 15種類{s['n']}列 正解={s['correct']}（{s['acc_all']:.1%}） 誤り={s['wrong']} 不明={s['unknown']} 重大={s['critical']} ／ その他 見送り={s['other_ok']} 誤答={s['other_ng']}")
            continue
        s = score(pred, truth)
        print(f"{path}: 正解={s['correct']}（{s['acc_all']:.1%}） 誤り={s['wrong']} 不明={s['unknown']} 重大={s['critical']}")


if __name__ == "__main__":
    main()
