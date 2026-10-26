"""手順書 v0 の線 T_H を、教材庫の全列（交差検証の「見ていない答え」）で決める（2026-10-26 Claude。事前記録 bench/crossval_body_h_20261026.md）。

- 本体：research/experts/preds/cvbody_jobK_<陣>.json（組 k を外して学んだ本体が組 k を予測）
- H：research/experts/preds/hcv_jobK_<陣>.json（同じく H）
- 検査役 v2：組 k を外して学び、組 k を予測
- 線の決まり：bench/hard_model_router_20261026.md と同じ（重大 ≤ 0.2% かつ正解率 ≥ 今の製品の形、満たす一番低い T_H）
使い方：python research/experts/router_cv.py [--out bench/crossval_body_h_20261026.md]
"""
import argparse
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from verifier_c1 import TAU  # noqa: E402
from research.experts.hard_list import FOLDS  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402

NUM = set(V.NUMERIC)
TS = (0.7, 0.8, 0.9, 0.95, 0.98)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--hard-prefix", default="hcv")
    a = ap.parse_args(argv)
    labels = list(V.LABELS)
    cols, H, fold = [], {}, []
    for job, bs in FOLDS.items():
        for b in bs:
            cs, _ = with_pred(E.load_batch(b), os.path.join(ROOT, "research", "experts", "preds", f"cvbody_{job}_{b}.json"))
            cols += cs
            fold += [job] * len(cs)
            for r in json.load(open(os.path.join(ROOT, "research", "experts", "preds", f"{a.hard_prefix}_{job}_{b}.json"), encoding="utf-8"))["rows"]:
                H[r["id"]] = (r["guarded_prediction"], r["top3"])
    fold = np.array(fold)
    X = np.hstack([V.matrix([c["values"] for c in cols]), E.table_matrix(cols)])
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in cols])
    y = np.array([c["truth"] if o else "" for c, o in zip(cols, ok)])
    P = np.zeros((len(cols), len(labels)), dtype="float32")
    for job in FOLDS:
        m, _, _ = E.fit(X[ok & (fold != job)], y[ok & (fold != job)])
        p = m.predict_proba(X[fold == job])
        for j, lab in enumerate(m.classes_):
            P[fold == job, labels.index(lab)] = p[:, j]
        print("verifier fold", job, flush=True)
    base = E.base_decisions(cols)
    idx = list(range(len(cols)))
    fin = E.combine(base, P, np.zeros(len(cols)), labels, TAU, None, idx)
    no_rho = [fin[k] for k in idx]

    def with_rho(decs):
        out = []
        for k, d in enumerate(decs):
            c = V.candidate(d[0], d[1], cols[k]["pred"], cols[k]["top3"], cols[k]["header"], P[k], labels, 0.7)
            out.append((c, "assert") if c else d)
        return out

    def router(T):
        out, back, down = [], 0, 0
        for k, d in enumerate(no_rho):
            hl, ht = H[cols[k]["id"]]
            hp = (ht or [{}])[0].get("probability", 0)
            top3 = [t["label"] for t in (cols[k]["top3"] or [])][:3]
            if d[0] == "unknown" and hl != "unknown" and hp >= T and hl in top3:
                if hl in NUM and P[k][labels.index(hl)] < TAU:
                    out.append(d)
                else:
                    out.append((hl, "hard_model")); back += 1
                continue
            if d[0] in NUM and hl in NUM and hl != d[0] and hp >= T:
                out.append(("unknown", "hard_model_check")); down += 1
                continue
            out.append(d)
        return out, back, down

    def row(name, decs, back=0, down=0):
        s = E.score([d[0] for d in decs], cols)
        return f"| {name} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} | {back} | {down} |", s

    L = ["## 手順書 v0 の線を教材庫の全列で決める（交差検証、`research/experts/router_cv.py`）", "",
         "| 形 | 結果 | 不明 | 重大 | H で言い切り | H で不明に |", "|---|---|---:|---:|---:|---:|"]
    r0, s0 = row("(0) 今の製品の形（rho 0.7）", with_rho(no_rho))
    L += [r0, row("(0') rho なし", no_rho)[0]]
    picks = []
    for T in TS:
        dec, bk, dn = router(T)
        r1, s1 = row(f"(1) 手順書 v0 T_H={T}", dec, bk, dn)
        L += [r1, row(f"(2) 手順書 v0＋rho T_H={T}", with_rho(dec), bk, dn)[0]]
        if s1["critical"] <= 0.002 * s1["n"] and s1["correct"] >= s0["correct"]:
            picks.append(T)
    L += ["", f"- 線の決まりを満たす T_H：{picks or 'なし'} → 選ぶ値：{min(picks) if picks else 'なし'}"]
    print("\n".join(L))
    if a.out:
        with open(a.out, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    main()
