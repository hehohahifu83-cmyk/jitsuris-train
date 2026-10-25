"""数字の専門家 v1（2026-10-25 Claude。CPU の木のモデル）。設計：research/experts-plan-2026-10-25.md

数字の種類（date・amount・quantity・rate・id）どうしで迷った列だけを受け持ち、5 つのどれかを当てる。
- 入力：列名＋単位の文字（char n-gram → 64 次元に圧縮）、値の並び（verifier.matrix）、同じ表の列との関係（table_features）。本体の確率は使わない（本体と別の見方にする）
- 学ぶ：教材庫 b001〜b012 の正解が数字の種類の列（C1 も b012 まで学んだので、測る陣と重ならない）
- 線 T：b001〜b012 で陣を 1 つずつ外した予測（版 31 の本体の上位 2 つ）から、「専門家の 1 位が本体の上位 2 つに入り、確率 ≥ T の列の正しい割合 ≥ 99.5%」になる一番低い T を選ぶ（測る陣は見ない）
- 使い方（製品の形の最後に足す）：不明になった列のうち、本体の上位 2 つに数字の種類があり、専門家の 1 位がその中に入り、確率 ≥ T なら言い切りに戻す
- 測る：C1 が見ていない b013・b014。製品の形（見張り → recheck v1 → 検査役 v2 → rho 0.7）と、それに専門家を足した形を比べる
使い方：python research/experts/numeric_expert.py [--out bench/numeric_expert_v1.md]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import pool_bench as B  # noqa: E402
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402
from verifier_c1 import TAU  # noqa: E402

NUM = list(V.NUMERIC)
TRAIN = tuple(f"b{n:03d}" for n in range(1, 13))
TEST = ("b013", "b014")
RHO = 0.7
GRID = (0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.93, 0.95, 0.97, 0.98, 0.99)
MIN_ACC = 0.995


def header_text(c):
    return f"{c['header']} | {c.get('unit', '')}"


class Expert:
    def __init__(self):
        from sklearn.decomposition import TruncatedSVD
        from sklearn.feature_extraction.text import HashingVectorizer
        self.hv = HashingVectorizer(analyzer="char_wb", ngram_range=(1, 3), n_features=2 ** 14, alternate_sign=False, norm="l2")
        self.svd = TruncatedSVD(64, random_state=0)

    def feats(self, cols, fit=False):
        H = self.hv.transform([header_text(c) for c in cols])
        H = self.svd.fit_transform(H) if fit else self.svd.transform(H)
        return np.hstack([V.matrix([c["values"] for c in cols]), E.table_matrix(cols), H.astype("float32")])

    def fit(self, cols):
        from sklearn.ensemble import HistGradientBoostingClassifier
        X = self.feats(cols, fit=True)
        self.m = HistGradientBoostingClassifier(max_iter=300, learning_rate=0.08, max_leaf_nodes=31, l2_regularization=1.0, random_state=0)
        self.m.fit(X, [c["truth"] for c in cols])
        return self

    def proba(self, cols):
        P = np.zeros((len(cols), len(NUM)), dtype="float32")
        p = self.m.predict_proba(self.feats(cols))
        for j, lab in enumerate(self.m.classes_):
            P[:, NUM.index(lab)] = p[:, j]
        return P


def is_num(c):
    return c["truth"] in NUM


def top2(c):
    return [t["label"] for t in (c["top3"] or [])][:2]


def pick_threshold(train):
    """陣を外した予測で T を選ぶ（本体は版 31＝load_batch の pred・top3）。"""
    num = [c for c in train if is_num(c)]
    P = np.zeros((len(num), len(NUM)), dtype="float32")
    bt = np.array([c["batch"] for c in num])
    for b in TRAIN:
        tr = [c for c in num if c["batch"] != b]
        te_idx = np.where(bt == b)[0]
        if len(te_idx) == 0:
            continue
        P[te_idx] = Expert().fit(tr).proba([num[k] for k in te_idx])
        print("fold", b, flush=True)
    rows = []
    for T in GRID:
        hit = ok = 0
        for c, p in zip(num, P):
            lab = NUM[int(p.argmax())]
            if p.max() >= T and lab in top2(c):
                hit += 1
                ok += lab == c["truth"]
        rows.append((T, hit, ok / hit if hit else 1.0))
        print(f"T={T} 戻す {hit} 正しい {ok / hit if hit else 1:.4f}", flush=True)
    good = [r for r in rows if r[2] >= MIN_ACC]
    return (good[0][0] if good else None), rows


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="bench/numeric_expert_v1.md")
    ap.add_argument("--pred", default="research/merge/preds/c1_{b}.json")
    a = ap.parse_args(argv)
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    T, curve = pick_threshold(train)
    print("T =", T, flush=True)
    ex = Expert().fit([c for c in train if is_num(c)])
    # 製品の形（merge_eval.score と同じ）
    Xtr = np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(Xtr[ok], np.array([c["truth"] for c in train])[ok])
    te = []
    for b in TEST:
        cs, _ = with_pred(E.load_batch(b), a.pred.format(b=b))
        te += cs
    base = E.base_decisions(te)
    Xte = np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)])
    Pte = np.zeros((len(te), len(labels)), dtype="float32")
    p = mv.predict_proba(Xte)
    for j, c in enumerate(mv.classes_):
        Pte[:, labels.index(c)] = p[:, j]
    idx = list(range(len(te)))
    fin = E.combine(base, Pte, np.zeros(len(te)), labels, TAU, None, idx)
    prod = []
    for k in idx:
        d = fin[k]
        c = V.candidate(d[0], d[1], te[k]["pred"], te[k]["top3"], te[k]["header"], Pte[k], labels, RHO)
        prod.append((c, "assert") if c else d)
    PX = ex.proba(te)
    L = ["# 数字の専門家 v1（b013・b014、2026-10-25 Claude。`research/experts/numeric_expert.py`）", "",
         "- 設計：`research/experts-plan-2026-10-25.md`。専門家は b001〜b012 の数字の列で学んだ（列名＋単位の文字・値の並び・同じ表の列。本体の確率は使わない）",
         f"- 線 T＝{T}（b001〜b012 で陣を外した予測から選んだ。「戻した列の正しい割合 ≥ {MIN_ACC:.1%}」の一番低い T。測る陣は見ていない）",
         "- 本体：C1 種子 1。製品の形＝見張り → recheck v1 → 検査役 v2（b001〜b012）→ rho 0.7。**開発用の数字**（b013 は rho を決めた陣でもある。採否は b015 で確かめてから）", "",
         "## 線を選んだ曲線（b001〜b012、陣を外した予測。本体は版 31）", "| T | 戻す列 | 正しい割合 |", "|---:|---:|---:|"]
    L += [f"| {t} | {h} | {acc:.2%} |" for t, h, acc in curve]
    L += ["", "## b013・b014（採点 other 以外）", "| 形 | 結果 | 不明 | 重大 |", "|---|---|---:|---:|"]
    s0 = E.score([d[0] for d in prod], te)
    L.append(f"| 今の製品の形 | {E.fmt(s0)} | {s0['unknown'] / s0['n']:.1%} | {s0['critical'] / s0['n']:.2%} |")
    for t in sorted({T} | {0.9, 0.95, 0.98} - {None}):
        out, back = [], 0
        for k, d in enumerate(prod):
            lab = NUM[int(PX[k].argmax())]
            if d[0] == "unknown" and PX[k].max() >= t and lab in top2(te[k]):
                out.append((lab, "numeric_expert"))
                back += 1
            else:
                out.append(d)
        s = E.score([d[0] for d in out], te)
        mark = "（選んだ線）" if t == T else "（参考）"
        L.append(f"| ＋ 数字の専門家 T={t}{mark}・戻した {back} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} |")
        print(t, back, E.fmt(s), flush=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
