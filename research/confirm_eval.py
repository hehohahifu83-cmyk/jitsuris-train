"""確かめる陣の 1 回だけの測り（2026-10-31 Claude。事前記録 bench/confirm_prereg_20261031.md。予測の前に書いた）。

  python research/confirm_eval.py [予測のフォルダ（試し用。書き出さない）]   → research/confirm_eval.md
A（D1 job1・2 ＋ D2 job1）、L（D2 job2〜4）、L＋K（同じ予測＋凍結した辞書）を、同じ正解で数える。
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d1_eval as D  # noqa: E402
import d2_eval as D2  # noqa: E402

FIXES = os.path.join(D.ROOT, "research", "labels", "consistency_20261031", "decisions.jsonl")
DICT = os.path.join(D.ROOT, "materials", "dictionary", "frozen_d3.jsonl")
DICT_SHA = "08a227016f1ad94ccf5e3408626c1e72358540761f70ef26343de9139a6f4a45"
SEEDS = (1, 2, 3)
# 形 → 種子 → 予測ファイル
PRED = {"A": {1: "pred_d1a_job1.json", 2: "pred_d1a_job2.json", 3: "pred_d2_job1.json"},
        "L": {1: "pred_d2_job2.json", 2: "pred_d2_job3.json", 3: "pred_d2_job4.json"}}
ARMS = {"A": ("A", ()), "L": ("L", ()), "L+K": ("L", ("K",))}
PAIRS = (("L+K", "A", "主な問い：L＋K は A より良いか"), ("L", "A", "D2 の付け直しの一般化"), ("L+K", "L", "D3 の辞書の一般化"))


def main():
    import hashlib
    if hashlib.sha256(open(DICT, "rb").read()).hexdigest() != DICT_SHA:
        raise SystemExit("辞書が凍結したものと違う")
    os.environ["JITSURIS_DICT"] = DICT
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D.ROOT, "materials", "pool", "work", "d1conf")
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm],
                       np.array([c["truth"] for c in train])[okm])
    base = D.load_side("confirm", D.label_fixes(FIXES))
    res, per, raw = {}, {}, {}
    for arm, (pk, fx) in ARMS.items():
        for s in SEEDS:
            D.EF._PCACHE.clear()
            p = {}
            res[f"{arm}{s}"] = D.EF.run(D.with_job(base, os.path.join(folder, PRED[pk][s])), mv, labels, D.PRODUCT + fx, per=p)
            per[f"{arm}{s}"] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}
            raw[f"{arm}{s}"] = p
    if len({r[0] for r in res.values()}) != 1:
        raise SystemExit("採点列の数が形で違う")
    tables = {c["id"]: (c["batch"], c["table"]) for cols in base.values() for c in cols if c["id"] in per["A1"]}
    mean = {arm: {"ok": sum(100 * res[f"{arm}{s}"][1] / res[f"{arm}{s}"][0] for s in SEEDS) / 3,
                  "unk": sum(100 * res[f"{arm}{s}"][2] / res[f"{arm}{s}"][0] for s in SEEDS) / 3,
                  "crit": sum(res[f"{arm}{s}"][3] for s in SEEDS),
                  "wrong": sum(100 * res[f"{arm}{s}"][4] / res[f"{arm}{s}"][0] for s in SEEDS) / 3} for arm in ARMS}
    n = res["A1"][0]
    L = ["# 確かめる陣の 1 回だけの測り（`research/confirm_eval.py`）", "",
         f"- 事前記録 `bench/confirm_prereg_20261031.md`。採点 {n} 列。正解は列名の同じ列の裁定を入れたもの。辞書 SHA-256 {DICT_SHA}。", "",
         "| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |", "|---|---:|---:|---:|---:|---|"]
    for arm in ARMS:
        m = mean[arm]
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | " + "・".join(str(res[f"{arm}{s}"][1]) for s in SEEDS) + " |")
    L += ["", "## 決まり 1〜4", "", "| 比べ | 1. 正しい | 2. 重大 | 3. ほか < 正しい | 4. 90% 区間 | 判定 | 良く／悪く（固有の列） |", "|---|---|---|---|---|---|---|"]
    mk = lambda b: "○" if b else "×"  # noqa: E731
    for new, old, what in PAIRS:
        p2 = {f"A{s}": per[f"{old}{s}"] for s in SEEDS} | {f"L{s}": per[f"{new}{s}"] for s in SEEDS}
        lo, hi = D2.pooled_boot(p2, tables)
        d_ok, d_crit, d_wrong, checks, ok = D2.verdict({"A": mean[old], "L": mean[new]}, lo)
        okn = lambda a, k: sum(per[f"{a}{s}"][k] == "ok" for s in SEEDS)  # noqa: E731
        up = sum(1 for k in per["A1"] if okn(new, k) - okn(old, k) >= 2)
        dn = sum(1 for k in per["A1"] if okn(old, k) - okn(new, k) >= 2)
        L.append(f"| {new} 対 {old}（{what}） | {d_ok:+.2f} {mk(checks[0])} | {d_crit:+d} {mk(checks[1])} | {d_wrong:+.2f} {mk(checks[2])} | "
                 f"{lo:+.2f}〜{hi:+.2f} {mk(checks[3])} | {'**確かめられた**' if ok else '確かめられなかった'} | {up}／{dn} |")
    L += ["", "## 辞書が変えた列（L と L＋K、3 本すべて）", "", "| 本 | id | 列名 | 正解 | L | L＋K |", "|---|---|---|---|---|---|"]
    for s in SEEDS:
        a, b = raw[f"L{s}"], raw[f"L+K{s}"]
        for k in sorted(a):
            if a[k][0] != b[k][0]:
                L.append(f"| {s} | {k} | {str(a[k][2])[:35]} | {a[k][1]} | {a[k][0]} | {b[k][0]} |")
    text = "\n".join(L) + "\n"
    if len(sys.argv) > 1:
        print(text)
        return
    open(os.path.join(HERE, "confirm_eval.md"), "w", encoding="utf-8").write(text)
    json.dump(per, open(os.path.join(HERE, "confirm_eval_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(text)


if __name__ == "__main__":
    main()
