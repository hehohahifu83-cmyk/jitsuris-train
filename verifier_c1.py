"""検査役 v2 と重大検知役を、製品に入れる本体 C1（教材庫を学習した版、run 40118170559 の種子 1）に重ねて測る（2026-10-25 Claude）。

C1 は b012 までの教材庫で学習したので、教材庫では測れない。C1 が見ていない陣（b013 から。`pred_c1_seed1.json`）で測る。
- 検査役 v2・重大検知役は、測る陣を除いた陣（版 31 の予測）で学ぶ（測る陣の正解は見ない）
- 重大検知役は本体の確率を入力にするので、版 31 で学んだものが C1 にそのまま効くかを見る（効かなければ C1 の予測で作り直す）
- tau・th は verifier_eval.py（版 31、陣を外して決めた）の 0.05・0.7 をそのまま使う（ここでは選ばない）
候補つきの不明を言い切りに戻す線（rho_assert）の曲線も出す（オーナー指示「8〜10%を目指そう」。線は測る陣で選ばず、別の陣で確かめる）。
使い方：python verifier_c1.py --test b013 [--out bench/verifier_c1_b013.md]
"""
from __future__ import annotations

import argparse
import json

import numpy as np

import pool_bench as B
import verifier as V
import verifier_eval as E

TAU, TH = 0.05, 0.7


def with_c1(cols, batch):
    """陣の列の本体の答えを C1 の予測に差し替える（id で合わせる）。"""
    pred = json.load(open(B.WORK / batch / "pred_c1_seed1.json", encoding="utf-8"))
    by = {r["id"]: r for r in pred["rows"]}
    for c in cols:
        r = by[c["id"]]
        c["pred"], c["top3"] = r["guarded_prediction"], r["top3"]
    return cols, pred.get("checkpoint", {}).get("weights_sha256", "")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", nargs="+", default=["b013"])
    ap.add_argument("--out", default=None)
    ap.add_argument("--save", default=None, help="検査役の確率・重大検知役の確率を npz に保存（再利用）")
    a = ap.parse_args(argv)
    train_b = [b for b in E.BATCHES if b not in a.test]
    labels = list(V.LABELS)
    tr = [c for b in train_b for c in E.load_batch(b)]
    te, sha = [], set()
    for b in a.test:
        cs, s = with_c1(E.load_batch(b), b)
        te += cs
        sha.add(s)
    base_tr, base_te = E.base_decisions(tr), E.base_decisions(te)
    Xtr = np.hstack([V.matrix([c["values"] for c in tr]), E.table_matrix(tr)])
    Xte = np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)])
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in tr])
    y = np.array([c["truth"] if o else "" for c, o in zip(tr, ok)])
    # 検査役 v2（測る陣を除いて学ぶ）。重大検知役の学習の入力には、陣を外して出した確率を使う（verifier_eval と同じ）
    bt = np.array([c["batch"] for c in tr])
    Ptr = np.zeros((len(tr), len(labels)), dtype="float32")
    for b in train_b:
        m, _, _ = E.fit(Xtr[ok & (bt != b)], y[ok & (bt != b)])
        p = m.predict_proba(Xtr[bt == b])
        for j, c in enumerate(m.classes_):
            Ptr[bt == b, labels.index(c)] = p[:, j]
        print("fold", b, flush=True)
    mv, _, _ = E.fit(Xtr[ok], y[ok])
    Pte = np.zeros((len(te), len(labels)), dtype="float32")
    p = mv.predict_proba(Xte)
    for j, c in enumerate(mv.classes_):
        Pte[:, labels.index(c)] = p[:, j]
    XRtr = E.risk_matrix(Xtr, Ptr, base_tr, tr, labels)
    asserted = np.array([d[0] in V.NUMERIC for d in base_tr])
    scored = np.array([bool(c["truth"]) and c["truth"] not in B.NOT_USED and c["truth"] != "person" for c in tr])
    yr = np.array([int(c["truth"] in V.NUMERIC and d[0] != c["truth"]) for c, d in zip(tr, base_tr)])
    mr = E.fit_risk(XRtr[asserted & scored], yr[asserted & scored])
    XRte = E.risk_matrix(Xte, Pte, base_te, te, labels)
    Rte = np.where([d[0] in V.NUMERIC for d in base_te], mr.predict_proba(XRte)[:, 1], 0.0)
    idx = list(range(len(te)))
    guard = [(c["pred"], None) for c in te]
    only_v = E.combine(base_te, Pte, Rte, labels, TAU, None, idx)
    both = E.combine(base_te, Pte, Rte, labels, TAU, TH, idx)
    rows = [("見張りだけ", guard), ("＋ recheck v1", base_te), ("＋ recheck v1 ＋ 検査役 v2", [only_v[k] for k in idx]),
            ("＋ recheck v1 ＋ 検査役 v2 ＋ 重大検知役（版 31 で学んだもの）", [both[k] for k in idx])]
    scores = [(n, E.score([d[0] for d in x], te)) for n, x in rows]
    vc = E.vetoed([both[k] for k in idx], base_te, te)
    cp = [E.crit_pairs([d[0] for d in x], te) for _, x in rows]
    out = a.out or f"bench/verifier_c1_{'_'.join(a.test)}.md"
    L = [f"# 検査役 v2 ＋ 重大検知役を C1 に重ねる（{', '.join(a.test)}、2026-10-25 Claude。`verifier_c1.py`）", "",
         f"- 本体：C1（教材庫を学習、run 40118170559 の種子 1、重み {', '.join(sorted(sha))}）。C1 はこの陣を学習に使っていない",
         f"- 検査役 v2・重大検知役は {train_b[0]}〜{train_b[-1]}（本体は版 31）で学んだ。測る陣の正解は見ていない。tau＝{TAU}・th＝{TH} は版 31 で決めた値をそのまま使った",
         "", "| 判定 | 結果 |", "|---|---|"] + [f"| {n} | {E.fmt(s)} |" for n, s in scores] + [
         "", f"- 検査役 v2 ＋ 重大検知役が下げた列 {sum(vc.values())}：本体が正しかった {vc['was_correct']}・重大な誤り {vc['was_critical']}・ほかの誤り {vc['was_wrong']}・正解が決められない列 {vc['truth_unknown']}",
         "", "### 重大（種類の組）", "| 組 | " + " | ".join(n for n, _ in rows) + " |", "|---|" + "---:|" * len(rows)]
    keys = sorted(set().union(*cp), key=lambda k: -cp[1].get(k, 0))
    for k in keys:
        L.append(f"| {k} | " + " | ".join(str(c.get(k, 0)) for c in cp) + " |")
    # 候補つきの不明を言い切りに戻す：本体の 1 位と検査役の 1 位が同じ数字の種類で、検査役の確率が rho 以上（verifier.candidate）
    fin = [both[k] for k in idx]
    n = len([c for c in te if c["truth"] and c["truth"] not in B.NOT_USED and c["truth"] != "person"])
    L += ["", "## 候補つきの不明を言い切りに戻したら（参考の曲線。線はこの陣では選ばない）",
          "| rho | 結果 | 不明の割合 | 重大の割合 |", "|---:|---|---:|---:|"]
    for r in (None, 0.5, 0.7, 0.8, 0.9, 0.95, 0.98, 0.99):
        if r is None:
            f2 = fin
        else:
            f2 = []
            for k, d in enumerate(fin):
                c = V.candidate(d[0], d[1], te[k]["pred"], te[k]["top3"], te[k]["header"], Pte[k], labels, r)
                f2.append((c, "assert") if c else d)
        s2 = E.score([d[0] for d in f2], te)
        L.append(f"| {r if r is not None else '戻さない'} | {E.fmt(s2)} | {s2['unknown'] / s2['n']:.1%} | {s2['critical'] / s2['n']:.2%} |")
        print("rho", r, E.fmt(s2), flush=True)
    if a.save:
        np.savez(a.save, P=Pte, R=Rte)
    L += ["", "- **注意**：1 陣だけの数字で、列が少ない。合格判定は封印セット #3 で事前登録して測る"]
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    for n, s in scores:
        print(n, E.fmt(s))
    print(vc)


if __name__ == "__main__":
    main()
