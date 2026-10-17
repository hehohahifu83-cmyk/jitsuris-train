"""v4 の候補を学習して保存する（未見セット3の前に、候補と第一候補を事前に決める）。
v4a：ロジスティック回帰＋文脈＋教材（合成・自治体・業務の表）＋見張り
v4b：v4a ＋ 小さなニューラルネットとの組み合わせ
v4c（第一候補）：v4a ＋ 数字の値を見分けにくくした例で学習 ＋ 見張り2（列名だけの答えと数字の種類が食い違えば不明）
理由：未見セット1・2で不合格の主因は重大な誤り（数字の種類の取り違え）。値に頼らず列名で決め、迷えば不明にする設計を第一にする"""
import base64, json
import numpy as np
from sklearn.linear_model import LogisticRegression
import gen
from train3 import MLP, build_train, mat, split_curriculum
from curriculum import CURRICULUM


def q8(W):
    scale = np.abs(W).max(axis=-1) / 127.0 + 1e-12
    return base64.b64encode(np.clip(np.round(W / scale[..., None]), -127, 127).astype(np.int8).tobytes()).decode(), scale.tolist()


def save(name, lr, mlp=None, agree=False, note=""):
    w, s = q8(lr.coef_)
    m = {"version": 4, "classes": list(lr.classes_), "dim": int(lr.coef_.shape[1]), "lr": {"weights_b64": w, "scale": s, "bias": lr.intercept_.tolist()},
         "threshold": 0.5, "agree_guard": agree, "context": True, "note": note}
    import features
    if features.USE_NUM2:
        m["num2"] = True  # 数字の列の値特徴（v8〜）。ブラウザ版も同じ並びで読む
    if mlp is not None:
        w1, s1 = q8(mlp.W1.T); w2, s2 = q8(mlp.W2.T)
        m["mlp"] = {"hidden": int(mlp.W1.shape[1]), "W1T_b64": w1, "s1": s1, "b1": mlp.b1.tolist(), "W2T_b64": w2, "s2": s2, "b2": mlp.b2.tolist()}
    json.dump(m, open(name, "w"), ensure_ascii=False)
    print(name, len(json.dumps(m)) // 1024, "KB")


def _main():
    all_tables = sorted(CURRICULUM)  # 最終モデルは教材の表をすべて使う
    gen.HARD_NUMERIC = 0.0
    rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, all_tables)
    X = mat(rows); y = np.array([r[2] for r in rows])
    lr = LogisticRegression(C=8, max_iter=3000).fit(X, y)
    save("model_v4a.json", lr, note="v4a LR+文脈+教材")
    mlp = MLP().fit(X, y)
    save("model_v4b.json", lr, mlp, note="v4b LR+NN+文脈+教材")
    gen.HARD_NUMERIC = 0.3
    rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, all_tables)
    X = mat(rows); y = np.array([r[2] for r in rows])
    lr_c = LogisticRegression(C=8, max_iter=3000).fit(X, y)
    save("model_v4c.json", lr_c, agree=True, note="v4c 第一候補：LR+文脈+教材+見分けにくい数字+見張り2")


if __name__ == '__main__':
    _main()
