"""D3 の判定（2026-10-31 Claude。事前記録 bench/d3_prereg_20261031.md。予測を評価する前に書いた）。

決める陣 materials/pool/work/d1dec で、L 種子 1〜3 の 4 つの形を同じ正解（列名の同じ列の裁定を入れたもの）で数える：
  L       ＝ pred_d2_job2〜4、製品の形
  L＋K    ＝ 同じ予測、製品の形＋辞書（凍結した辞書のファイル）
  L＋T    ＝ pred_d3t_job2〜4（値の引き直し k＝4）、製品の形
  L＋K＋T ＝ pred_d3t_job2〜4、製品の形＋辞書
  python research/d3_eval.py <凍結した辞書のファイル> [予測のフォルダ（試し用。書き出さない）]   → research/d3_eval_decide.md
採る決まり（L と比べる。D2 と同じ 1〜4）。
"""
import collections
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d1_eval as D  # noqa: E402
import d2_eval as D2  # noqa: E402

FIXES = os.path.join(D.ROOT, "research", "labels", "consistency_20261031", "decisions.jsonl")
SEEDS = (1, 2, 3)
PRED = {"L": "pred_d2_job{j}.json", "T": "pred_d3t_job{j}.json"}
ARMS = {"L": ("L", ()), "L+K": ("L", ("K",)), "L+T": ("T", ()), "L+K+T": ("T", ("K",))}


def main():
    dict_path = sys.argv[1]
    folder = sys.argv[2] if len(sys.argv) > 2 else os.path.join(D.ROOT, "materials", "pool", "work", "d1dec")
    os.environ["JITSURIS_DICT"] = dict_path
    dict_sha = hashlib.sha256(open(dict_path, "rb").read()).hexdigest()
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm],
                       np.array([c["truth"] for c in train])[okm])
    base = D.load_side("decide", D.label_fixes(FIXES))
    tshas = json.load(open(os.path.join(folder, "weights_sha256_d3t.json"), encoding="utf-8")) if len(sys.argv) <= 2 else None
    lshas = json.load(open(os.path.join(folder, "weights_sha256_d2.json"), encoding="utf-8"))
    if tshas is not None:
        for j in (2, 3, 4):
            if tshas[f"job{j}"]["sha256"] != lshas[f"job{j}"]["sha256"]:
                raise SystemExit(f"job{j}: T の重みが L と違う")
    res, per = {}, {}
    for arm, (pk, fx) in ARMS.items():
        for s in SEEDS:
            name = f"{arm}{s}"
            D.EF._PCACHE.clear()
            data = D.with_job(base, os.path.join(folder, PRED[pk].format(j=s + 1)))
            p = {}
            res[name] = D.EF.run(data, mv, labels, D.PRODUCT + fx, per=p)
            per[name] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}
    if len({res[n][0] for n in res}) != 1:
        raise SystemExit("採点列の数が形で違う")
    tables = {c["id"]: (c["batch"], c["table"]) for cols in base.values() for c in cols if c["id"] in per["L1"]}
    mean = {arm: {"ok": sum(100 * res[f"{arm}{s}"][1] / res[f"{arm}{s}"][0] for s in SEEDS) / 3,
                  "unk": sum(100 * res[f"{arm}{s}"][2] / res[f"{arm}{s}"][0] for s in SEEDS) / 3,
                  "crit": sum(res[f"{arm}{s}"][3] for s in SEEDS),
                  "wrong": sum(100 * res[f"{arm}{s}"][4] / res[f"{arm}{s}"][0] for s in SEEDS) / 3} for arm in ARMS}
    n = res["L1"][0]
    L = ["# D3 の判定：決める陣（`research/d3_eval.py`、探索の扱い）", "",
         f"- 事前記録 `bench/d3_prereg_20261031.md`。正解は列名の同じ列の裁定を入れたもの（`{os.path.relpath(FIXES, D.ROOT)}`）。採点 {n} 列。",
         f"- 辞書：`{os.path.relpath(dict_path, D.ROOT)}`（SHA-256 {dict_sha}）。", "",
         "| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |", "|---|---:|---:|---:|---:|---|"]
    for arm in ARMS:
        m = mean[arm]
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | "
                 + "・".join(str(res[f"{arm}{s}"][1]) for s in SEEDS) + " |")
    L += ["", "## 採る決まり（相手は L）", "", "| 形 | 1. 正しい | 2. 重大 | 3. ほか < 正しい | 4. 90% 区間 | 判定 | 変わった固有の列（良く／悪く、3 本中 2 本以上） |", "|---|---|---|---|---|---|---|"]
    adopt = {}
    for arm in ("L+K", "L+T", "L+K+T"):
        p2 = {f"A{s}": per[f"L{s}"] for s in SEEDS} | {f"L{s}": per[f"{arm}{s}"] for s in SEEDS}
        lo, hi = D2.pooled_boot(p2, tables)
        d_ok, d_crit, d_wrong, checks, ok = D2.verdict({"A": mean["L"], "L": mean[arm]}, lo)
        adopt[arm] = ok
        okn = lambda a, k: sum(per[f"{a}{s}"][k] == "ok" for s in SEEDS)  # noqa: E731
        up = sum(1 for k in per["L1"] if okn(arm, k) - okn("L", k) >= 2)
        dn = sum(1 for k in per["L1"] if okn("L", k) - okn(arm, k) >= 2)
        mk = lambda b: "○" if b else "×"  # noqa: E731
        L.append(f"| {arm} | {d_ok:+.2f} {mk(checks[0])} | {d_crit:+d} {mk(checks[1])} | {d_wrong:+.2f} {mk(checks[2])} | {lo:+.2f}〜{hi:+.2f} {mk(checks[3])} | "
                 f"{'**採る**' if ok else '採らない'} | {up}／{dn} |")
    final = "L+K+T" if adopt["L+K"] and adopt["L+T"] and adopt["L+K+T"] else (
        max((a for a in ("L+K", "L+T") if adopt[a]), key=lambda a: mean[a]["ok"], default="L"))
    L += ["", f"**この回の形：{final}**（K と T の両方を満たし、合わせた形も満たせば L＋K＋T。片方だけなら、その形）", "",
          "## 辞書が変えた列（L＋K、種子 1）", "", "| id | 列名 | 正解 | L | L＋K |", "|---|---|---|---|---|"]
    pl, pk = {}, {}
    D.EF._PCACHE.clear()
    D.EF.run(D.with_job(base, os.path.join(folder, PRED["L"].format(j=2))), mv, labels, D.PRODUCT, per=pl)
    D.EF._PCACHE.clear()
    D.EF.run(D.with_job(base, os.path.join(folder, PRED["L"].format(j=2))), mv, labels, D.PRODUCT + ("K",), per=pk)
    for k in sorted(pl):
        if pl[k][0] != pk[k][0]:
            L.append(f"| {k} | {str(pl[k][2])[:35]} | {pl[k][1]} | {pl[k][0]} | {pk[k][0]} |")
    text = "\n".join(L) + "\n"
    if len(sys.argv) > 2:
        print(text)
        return
    open(os.path.join(HERE, "d3_eval_decide.md"), "w", encoding="utf-8").write(text)
    json.dump(per, open(os.path.join(HERE, "d3_eval_decide_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(text)


if __name__ == "__main__":
    main()
