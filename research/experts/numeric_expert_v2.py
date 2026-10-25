"""数字の専門家 v2（2026-10-26 Claude）。v1（bench/numeric_expert_v1.md）の失敗を直す。

v1 の失敗：線 T を「数字の列ぜんぶ」（易しい列）で選んだので、実際に戻す難しい列（製品の形で不明になった列）では正しさが約 5 割だった。
v2 の直し（ChatGPT の指摘 C・F を入れた）：
1. 線は**同じ集団**で選ぶ：教材庫 b001〜b012 で、版 31 の予測（load_batch の pred・top3）から製品の形（見張り → recheck v1 → 検査役 v2（陣を外して学ぶ）→ rho 0.7）を作り、不明になった列だけで数える。専門家も陣を外して学んだ予測を使う
2. 「不明からの救済」と「危ない言い切りの再検査」を分けて測る
3. 戻す条件の型を 3 つ比べる：(a) 専門家の 1 位が本体の上位 2 つに入る (b) さらに本体の 1 位と同じ (c) さらに列名・単位の手がかり（recheck.cue_types）がその種類を示す
- 線の決まり：救済は「戻した列（採点できる列）の正しさ ≥ 95%・かつ戻した列の重大 ≤ 戻した列の 2%」で一番低い T。再検査は「下げた列のうち本当に誤りだった割合 ≥ 50%」で一番高い D（検査役 v2 と同じ考え）
- 測る：b013・b014（C1 種子 1）。開発用の数字（b013 は rho を決めた陣）。採否は b015、確かめは b016
使い方：python research/experts/numeric_expert_v2.py [--out bench/numeric_expert_v2.md]
"""
from __future__ import annotations

import argparse
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import pool_bench as B  # noqa: E402
import recheck  # noqa: E402
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from research.experts.numeric_expert import NUM, Expert, top2  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402
from verifier_c1 import TAU  # noqa: E402

TRAIN = tuple(f"b{n:03d}" for n in range(1, 13))
TEST = ("b013", "b014")
RHO = 0.7
TS = (0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.98, 0.99)
DS = (0.001, 0.003, 0.01, 0.03, 0.05, 0.1)
KINDS = ("a", "b", "c")


def scored(c):
    return bool(c["truth"]) and c["truth"] not in B.NOT_USED and c["truth"] not in ("person", "other")


def product(cols, P, labels):
    """製品の形の判定（merge_eval.score と同じ）。P は検査役 v2 の確率。"""
    base = E.base_decisions(cols)
    idx = list(range(len(cols)))
    fin = E.combine(base, P, np.zeros(len(cols)), labels, TAU, None, idx)
    out = []
    for k in idx:
        d = fin[k]
        c = V.candidate(d[0], d[1], cols[k]["pred"], cols[k]["top3"], cols[k]["header"], P[k], labels, RHO)
        out.append((c, "assert") if c else d)
    return out


def verifier_oof(cols, labels):
    X = np.hstack([V.matrix([c["values"] for c in cols]), E.table_matrix(cols)])
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in cols])
    y = np.array([c["truth"] if o else "" for c, o in zip(cols, ok)])
    bt = np.array([c["batch"] for c in cols])
    P = np.zeros((len(cols), len(labels)), dtype="float32")
    for b in sorted(set(bt)):
        m, _, _ = E.fit(X[ok & (bt != b)], y[ok & (bt != b)])
        p = m.predict_proba(X[bt == b])
        for j, lab in enumerate(m.classes_):
            P[bt == b, labels.index(lab)] = p[:, j]
        print("verifier fold", b, flush=True)
    return P


def expert_oof(cols):
    bt = np.array([c["batch"] for c in cols])
    PX = np.zeros((len(cols), len(NUM)), dtype="float32")
    num = np.array([c["truth"] in NUM for c in cols])
    for b in sorted(set(bt)):
        tr = [c for c, n, bb in zip(cols, num, bt) if n and bb != b]
        te = np.where(bt == b)[0]
        PX[te] = Expert().fit(tr).proba([cols[k] for k in te])
        print("expert fold", b, flush=True)
    return PX


def rescue_ok(kind, c, p):
    lab = NUM[int(p.argmax())]
    t2 = top2(c)
    if lab not in t2:
        return None
    if kind in ("b", "c") and t2[:1] != [lab]:
        return None
    if kind == "c" and lab not in recheck.cue_types(c["header"], c.get("unit", "")):
        return None
    return lab


def apply(prod, cols, PX, kind=None, T=None, D=None):
    out, back, down = [], 0, 0
    for k, d in enumerate(prod):
        p = PX[k]
        if T is not None and d[0] == "unknown" and p.max() >= T:
            lab = rescue_ok(kind, cols[k], p)
            if lab:
                out.append((lab, "numeric_expert"))
                back += 1
                continue
        if D is not None and d[0] in NUM and p[NUM.index(d[0])] < D:
            out.append(("unknown", "numeric_expert_check"))
            down += 1
            continue
        out.append(d)
    return out, back, down


def pick_T(prod, cols, PX, kind):
    best = None
    for T in sorted(TS, reverse=True):
        n = ok = crit = 0
        for k, d in enumerate(prod):
            if d[0] != "unknown" or PX[k].max() < T or not scored(cols[k]):
                continue
            lab = rescue_ok(kind, cols[k], PX[k])
            if not lab:
                continue
            n += 1
            ok += lab == cols[k]["truth"]
            crit += cols[k]["truth"] in NUM and lab != cols[k]["truth"]
        print(f"  kind {kind} T={T}: 戻す {n} 正しい {ok / n if n else 1:.3f} 重大 {crit}", flush=True)
        if n and ok / n >= 0.95 and crit <= 0.02 * n:
            best = (T, n, ok / n, crit)
    return best


def pick_D(prod, cols, PX):
    best = None
    for D in DS:
        n = wrong = 0
        for k, d in enumerate(prod):
            if d[0] in NUM and PX[k][NUM.index(d[0])] < D:
                n += 1
                wrong += (not scored(cols[k])) or d[0] != cols[k]["truth"]
        print(f"  D={D}: 下げる {n} 本当に誤り {wrong / n if n else 0:.3f}", flush=True)
        if n and wrong / n >= 0.5:
            best = (D, n, wrong / n)
    return best


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="bench/numeric_expert_v2.md")
    a = ap.parse_args(argv)
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    prod_tr = product(train, verifier_oof(train, labels), labels)
    PX_tr = expert_oof(train)
    picks = {k: pick_T(prod_tr, train, PX_tr, k) for k in KINDS}
    pd = pick_D(prod_tr, train, PX_tr)
    print("picks", picks, "D", pd, flush=True)
    # 測る陣
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    Xtr = np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])
    mv, _, _ = E.fit(Xtr[ok], np.array([c["truth"] for c in train])[ok])
    te = []
    for b in TEST:
        cs, _ = with_pred(E.load_batch(b), f"research/merge/preds/c1_{b}.json")
        te += cs
    Xte = np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)])
    Pte = np.zeros((len(te), len(labels)), dtype="float32")
    p = mv.predict_proba(Xte)
    for j, lab in enumerate(mv.classes_):
        Pte[:, labels.index(lab)] = p[:, j]
    prod = product(te, Pte, labels)
    ex = Expert().fit([c for c in train if c["truth"] in NUM])
    PX = ex.proba(te)
    rows = [("今の製品の形", prod, 0, 0)]
    for k in KINDS:
        if picks[k]:
            o, bk, dn = apply(prod, te, PX, k, picks[k][0], None)
            rows.append((f"＋ 救済（型 {k}、T={picks[k][0]}）", o, bk, dn))
    if pd:
        o, bk, dn = apply(prod, te, PX, None, None, pd[0])
        rows.append((f"＋ 再検査（D={pd[0]}）", o, bk, dn))
        for k in KINDS:
            if picks[k]:
                o, bk, dn = apply(prod, te, PX, k, picks[k][0], pd[0])
                rows.append((f"＋ 救済（型 {k}）＋ 再検査", o, bk, dn))
    L = ["# 数字の専門家 v2（b013・b014、2026-10-26 Claude。`research/experts/numeric_expert_v2.py`）", "",
         "- v1 の失敗（`bench/numeric_expert_v1.md`）を直した：線は b001〜b012 で**製品の形で不明になった列だけ**で選んだ（本体は版 31、検査役・専門家は陣を外した予測）",
         "- 救済の線：戻した列の正しさ ≥ 95% かつ重大 ≤ 2%。再検査の線：下げた列のうち本当に誤り ≥ 50%。型 a＝専門家の 1 位が本体の上位 2 つに入る、b＝さらに本体の 1 位と同じ、c＝さらに列名・単位の手がかりがある",
         f"- 選んだ線（b001〜b012）：救済 {picks}、再検査 {pd}",
         "- **開発用の数字**（b013 は rho を決めた陣）。採否は b015、確かめは b016", "",
         "| 形 | 結果 | 不明 | 重大 | 戻した | 下げた |", "|---|---|---:|---:|---:|---:|"]
    for name, o, bk, dn in rows:
        s = E.score([d[0] for d in o], te)
        L.append(f"| {name} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} | {bk} | {dn} |")
        print(name, E.fmt(s), bk, dn, flush=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
