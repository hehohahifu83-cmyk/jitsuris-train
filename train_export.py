"""最終モデルを学習して、ブラウザ用の JSON（重みは8ビットに縮めた値）と、JavaScript と結果が一致するかの見本を書き出す。"""
import base64, json, random
import numpy as np
from exp2 import run, mat, eval_rows, rule_feats
from features import DIM, STAT_NAMES, H_DIM, V_DIM
from gen import CLASSES, make_train, column

import sys
ARG = sys.argv[1] if len(sys.argv) > 1 else "v1"
V2 = ARG in ("v2", "v3")
out, m = run(1500, 8, True, return_model=True, v2=V2, share=0.4, real=3 if ARG == "v3" else 0)
NAME = {"v1": "model", "v2": "model_v2", "v3": "model_v3"}[ARG]
W = m.coef_.astype(np.float64); b = m.intercept_.astype(np.float64)
scale = np.abs(W).max(1) / 127.0
Q = np.clip(np.round(W / scale[:, None]), -127, 127).astype(np.int8)
Wq = Q.astype(np.float64) * scale[:, None]
model = {"version": 1, "classes": list(m.classes_), "dim": int(W.shape[1]), "h_dim": H_DIM, "v_dim": V_DIM, "stats": STAT_NAMES,
         "rule_classes": CLASSES, "threshold": 0.5, "scale": [float(x) for x in scale], "bias": [float(x) for x in b],
         "weights_b64": base64.b64encode(Q.tobytes()).decode(), "trained": "synthetic only (gen.py), no customer data"}
model["variant"] = {"v1": "v1", "v2": "v2（組み立て式の列名を4割）", "v3": "v3（v2＋先生役ラベルの本物の列名）"}[ARG]
json.dump(model, open(NAME + ".json", "w"), ensure_ascii=False)

def probs(rows):
    X = mat(rows, True).toarray()
    z = X @ Wq.T + b; z -= z.max(1, keepdims=True); e = np.exp(z); return e / e.sum(1, keepdims=True)

# 8ビットに縮めても精度が変わらないか
from exp import score
for tag, mode, pert in (("both", "both", False), ("崩し", "both", True), ("header", "header", False)):
    acc = []
    for s in range(5):
        ev = eval_rows(100 + s, mode, pert); P = probs(ev)
        acc.append(score([model["classes"][i] for i in P.argmax(1)], [c for *_, c in ev])["acc_all"])
    print("8ビット", tag, f"{np.mean(acc):.1%}")
# 見本（JavaScript の一致確認用）
rng = random.Random(5); fx = []
for _ in range(120):
    c = rng.choice(CLASSES); h = rng.choice([x[1] for x in __import__("eval_set").EVAL] + ["", "ﾒﾓ", "Ｔｏｔａｌ（円）", "取引先名 "])
    vals = column(rng, c) if rng.random() < 0.8 else []
    fx.append({"header": h, "values": vals})
P = probs([(f["header"], f["values"], "") for f in fx])
for f, p in zip(fx, P): f["probs"] = [float(x) for x in p]
json.dump(fx, open({"v1": "fixtures", "v2": "fixtures_v2", "v3": "fixtures_v3"}[ARG] + ".json", "w"), ensure_ascii=False)
print(NAME, len(json.dumps(model)) // 1024, "KB")
