"""ラベルの掃除（強化案 B6、confident learning の考え方）の候補を出す（2026-10-25 Claude）。

教材庫 b001〜b014 の列のうち、**値だけを見る検査役 v2 を、その陣を外して学んだ確率**が今のラベルと強く食い違う列を出す。
- 検査役は列名を読まないので、先生（列名も見る）や本体とは別の見方になる
- 候補：今のラベルの確率 < 0.02 かつ 検査役の 1 位の確率 ≥ 0.9。値だけでは決めにくい種類の組（text↔category など）も含めて出し、判定は人の目の代わりに ChatGPT（2 人目）→ Claude（裁定）が LABEL_GUIDE だけで行う
- 出力：candidates.jsonl（id・陣・表・列名・値 5 つ・同じ表の列・単位・今のラベル・検査役の 1 位と確率・裁定済みか）。値は公開データのまま
使い方：python materials/pool/label_review/make_candidates.py
"""
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402

BATCHES = tuple(f"b{n:03d}" for n in range(1, 15))
P_LABEL, P_TOP = 0.02, 0.9


def main():
    labels = list(V.LABELS)
    cols = [c for b in BATCHES for c in E.load_batch(b)]
    X = np.hstack([V.matrix([c["values"] for c in cols]), E.table_matrix(cols)])
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in cols])
    y = np.array([c["truth"] if o else "" for c, o in zip(cols, ok)])
    bt = np.array([c["batch"] for c in cols])
    P = np.zeros((len(cols), len(labels)), dtype="float32")
    for b in BATCHES:
        m, _, _ = E.fit(X[ok & (bt != b)], y[ok & (bt != b)])
        p = m.predict_proba(X[bt == b])
        for j, c in enumerate(m.classes_):
            P[bt == b, labels.index(c)] = p[:, j]
        print("fold", b, flush=True)
    out = []
    for k, c in enumerate(cols):
        if not ok[k]:
            continue
        top = int(P[k].argmax())
        if P[k, labels.index(c["truth"])] < P_LABEL and P[k, top] >= P_TOP:
            out.append({"id": c["id"], "batch": c["batch"], "table": c["table"], "header": c["header"], "values5": c["values5"],
                        "context": c["context"], "unit": c["unit"], "label": c["truth"], "verifier_top": labels[top],
                        "verifier_p": round(float(P[k, top]), 3), "adjudicated": c.get("adjudicated")})
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "candidates.jsonl"), "w", encoding="utf-8") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"候補 {len(out)} / {int(ok.sum())} 列", flush=True)


if __name__ == "__main__":
    main()
