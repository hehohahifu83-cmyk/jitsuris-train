"""本体が誤った列（root_cause の M11）について、学習の教材（b001〜b014）でいちばん似た列にどの種類が付いていたかを見る（2026-10-30 Claude）。
本体の重みはこの環境にないので、本体の代わりに「列名が近い列」（文字の 2〜4 文字の並びの TF-IDF・余弦）と「値の形が近い列」（verifier の値の特徴を標準化・距離）を
それぞれ 10 列ずつ探し、付いていた種類の多数を、本体の答え・正解と比べる。
出力：research/unknown/analogs.md・analogs.jsonl
使い方：python research/unknown/analogs.py
"""
import json
import os
import re
import sys
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402

TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))
K = 10


def norm_header(h):
    h = re.sub(r"([a-z])([A-Z])", r"\1 \2", str(h or ""))
    return re.sub(r"[_\s]+", " ", h).strip().lower()


def majority(labels):
    c = Counter(labels)
    lab, n = c.most_common(1)[0]
    return lab, n, c


def main():
    from sklearn.feature_extraction.text import TfidfVectorizer
    train = [c for b in TRAIN for c in E.load_batch(b) if c.get("truth") and c["truth"] not in ("unknown", "S")]
    rc = [json.loads(l) for l in open(os.path.join(HERE, "root_cause.jsonl"), encoding="utf-8")]
    cols = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")}
    targets = [r for r in rc if r["mechanism"].startswith("M11")]
    tv = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4), min_df=2)
    Ht = tv.fit_transform([norm_header(c["header"]) for c in train])
    Hq = tv.transform([norm_header(cols[r["id"]]["header"]) for r in targets])
    Xt = V.matrix([c["values"] for c in train]).astype("float64")
    mu, sd = Xt.mean(0), Xt.std(0) + 1e-6
    Xt = (Xt - mu) / sd
    Xq = (V.matrix([cols[r["id"]]["values"] for r in targets]).astype("float64") - mu) / sd
    tl = np.array([c["truth"] for c in train])
    out = []
    for k, r in enumerate(targets):
        sim = (Ht @ Hq[k].T).toarray().ravel()
        hi = np.argsort(-sim)[:K]
        d = np.linalg.norm(Xt - Xq[k], axis=1)
        vi = np.argsort(d)[:K]
        hl, hn, hc = majority(tl[hi])
        vl, vn, vc = majority(tl[vi])
        m = r["model_top1"]
        if vl == m and hl == r["truth"]:
            kind = "A 値の形は教材の別の種類の列と同じで、本体は列名より値の形に従った"
        elif vl == m and hl == m:
            kind = "B 列名も値の形も、教材では本体の答えの種類の列に似ている（教材の付け方か、新しい陣の形が違う）"
        elif hl == m:
            kind = "C 列名が教材の別の種類の列に似ている"
        elif vl == m:
            kind = "A 値の形は教材の別の種類の列と同じで、本体は列名より値の形に従った"
        elif sim[hi[0]] < 0.3:
            kind = "D 列名の似た列が教材にない（いちばん近くても似ていない）"
        else:
            kind = "E 似た列の種類は本体の答えとも正解とも違う（本体の答えは似た列からは説明できない）"
        out.append({"id": r["id"], "header": cols[r["id"]]["header"], "truth": r["truth"], "model": m, "kind": kind,
                    "header_nn": [[str(train[i]["header"])[:30], str(tl[i]), round(float(sim[i]), 2)] for i in hi[:5]], "header_major": [hl, int(hn)],
                    "value_nn": [[str(train[i]["header"])[:30], str(tl[i]), [str(v)[:12] for v in train[i]["values"][:3]]] for i in vi[:5]], "value_major": [vl, int(vn)]})
    with open(os.path.join(HERE, "analogs.jsonl"), "w", encoding="utf-8") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    L = ["# 本体が誤った 73 列（M11）：学習の教材でいちばん似た列（`research/unknown/analogs.py`）", "",
         f"- 教材 b001〜b014 の確定した列 {len(train)}。列名が近い 10 列・値の形が近い 10 列の多数の種類を、本体の答え・正解と比べた", "",
         "| 分け | 列 |", "|---|---:|"]
    L += [f"| {k} | {n} |" for k, n in Counter(o["kind"] for o in out).most_common()]
    L += ["", "| id | 見出し | 正解 | 本体 | 列名の近い 10 列の多数 | 値の形の近い 10 列の多数 | 分け | いちばん列名が近い教材の列 |", "|---|---|---|---|---|---|---|---|"]
    for o in sorted(out, key=lambda o: o["kind"]):
        h = o["header_nn"][0]
        L.append(f"| {o['id']} | {str(o['header'])[:30].replace('|', '/')} | {o['truth']} | {o['model']} | {o['header_major'][0]} {o['header_major'][1]}/10 | "
                 f"{o['value_major'][0]} {o['value_major'][1]}/10 | {o['kind'][:1]} | {h[0].replace('|', '/')}（{h[1]}・{h[2]}） |")
    open(os.path.join(HERE, "analogs.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:12]))


if __name__ == "__main__":
    main()
