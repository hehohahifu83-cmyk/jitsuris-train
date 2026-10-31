"""D2 の判定（2026-10-31 Claude。事前記録 bench/d2_prereg_20261031.md。予測を見る前に書いた）。

決める陣 materials/pool/work/d1dec で、A＝種子 1・2（D1 の pred_d1_job1・2）と種子 3（D2 の pred_d2_job1）、
L＝種子 1・2・3（D2 の pred_d2_job2〜4）を、research/d1_eval.py と同じ製品の形・正解・採点の範囲で数える。

  python research/d2_eval.py [予測のフォルダ（試し用。書き出さない）]   → research/d2_eval_decide.md

採る決まり（事前記録）：
  1. 正しいが種子 3 本の平均で A より +0.5 ポイント以上
  2. 重大の合計（3 本）が増えない
  3. ほかの誤りの増え（平均、ポイント）が正しいの増えより少ない
  4. 同じ列の差（L − A、種子 s どうしの 3 組をまとめた平均）の、表で引き直すブートストラップの 90% 区間の下限が 0 より大きい
"""
import json
import os
import random
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d1_eval as D  # noqa: E402

# 名前 → （形, 種子, 予測ファイル, 重みの記録ファイル, 記録の中の名前）
RUNS = {
    "A1": ("A", 1, "pred_d1_job1.json", "weights_sha256.json", "job1"),
    "A2": ("A", 2, "pred_d1_job2.json", "weights_sha256.json", "job2"),
    "A3": ("A", 3, "pred_d2_job1.json", "weights_sha256_d2.json", "job1"),
    "L1": ("L", 1, "pred_d2_job2.json", "weights_sha256_d2.json", "job2"),
    "L2": ("L", 2, "pred_d2_job3.json", "weights_sha256_d2.json", "job3"),
    "L3": ("L", 3, "pred_d2_job4.json", "weights_sha256_d2.json", "job4"),
}
SEEDS = (1, 2, 3)


def pooled_boot(per, tables, reps=2000, seed="d2-boot"):
    """表を引き直し、種子ごとの差（L_s − A_s、ポイント）の 3 組の平均の 90% 区間。"""
    by = {}
    for k, t in tables.items():
        by.setdefault(t, []).append(k)
    keys = list(by)
    rng = random.Random(seed)
    diffs = []
    for _ in range(reps):
        pick = [k for t in (rng.choice(keys) for _ in keys) for k in by[t]]
        n = len(pick)
        d = [100 * (sum(per[f"L{s}"][k] == "ok" for k in pick) - sum(per[f"A{s}"][k] == "ok" for k in pick)) / n for s in SEEDS]
        diffs.append(sum(d) / len(d))
    diffs.sort()
    return diffs[int(0.05 * reps)], diffs[int(0.95 * reps) - 1]


def verdict(mean, lo):
    a, l = mean["A"], mean["L"]
    d_ok, d_crit, d_wrong = l["ok"] - a["ok"], l["crit"] - a["crit"], l["wrong"] - a["wrong"]
    checks = [d_ok >= 0.5, d_crit <= 0, d_wrong < d_ok, lo > 0]
    return d_ok, d_crit, d_wrong, checks, all(checks)


def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D.ROOT, "materials", "pool", "work", "d1dec")
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm],
                       np.array([c["truth"] for c in train])[okm])
    base = D.load_side("decide")
    res, per, shas = {}, {}, {}
    for name, (_, _, pred, wfile, wkey) in RUNS.items():
        shas[name] = json.load(open(os.path.join(folder, wfile), encoding="utf-8"))[wkey]
        D.EF._PCACHE.clear()
        data = D.with_job(base, os.path.join(folder, pred))
        p = {}
        res[name] = D.EF.run(data, mv, labels, D.PRODUCT, per=p)
        per[name] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}
    if len({res[n][0] for n in RUNS}) != 1:
        raise SystemExit("採点列の数が仕事で違う")
    tables = {c["id"]: (c["batch"], c["table"]) for cols in base.values() for c in cols if c["id"] in per["A1"]}
    # 記録の設定が事前記録どおりか
    for name, (arm, seed, *_r) in RUNS.items():
        if str(shas[name].get("seed")) != str(seed) or bool(shas[name].get("FT_LABELFIX")) != (arm == "L"):
            raise SystemExit(f"{name}: 重みの記録が事前記録と違う")
    L = ["# D2 の判定：決める陣（`research/d2_eval.py`）", "",
         f"- 製品の形（見張り → recheck F4・F8 → 検査役 v2 → rho {D.A.RHO} → 通貨の手がかり）。採点は正解が unknown・S・other・person でない列。D1 と同じ。",
         "- 事前記録 `bench/d2_prereg_20261031.md` の採る決まり 1〜4 で読む。", "",
         "| 名前 | 形 | 種子 | 重みの SHA-256（先頭） | 採点列 | 正しい | 不明 | 重大 | ほかの誤り |", "|---|---|---:|---|---:|---:|---:|---:|---:|"]
    for name, (arm, seed, *_r) in RUNS.items():
        n, ok, unk, crit, wrong = res[name]
        L.append(f"| {name} | {arm} | {seed} | {shas[name]['sha256'][:12]} | {n} | {ok}（{ok / n:.2%}） | {unk}（{unk / n:.2%}） | {crit} | {wrong} |")
    mean = {}
    for arm in ("A", "L"):
        ns = [f"{arm}{s}" for s in SEEDS]
        mean[arm] = {"ok": sum(100 * res[x][1] / res[x][0] for x in ns) / 3, "unk": sum(100 * res[x][2] / res[x][0] for x in ns) / 3,
                     "crit": sum(res[x][3] for x in ns), "wrong": sum(100 * res[x][4] / res[x][0] for x in ns) / 3}
    lo, hi = pooled_boot(per, tables)
    d_ok, d_crit, d_wrong, checks, adopt = verdict(mean, lo)
    L += ["", "## 種子 3 本の平均と採る決まり", "", "| 形 | 正しい | 不明 | 重大（3 本の合計） | ほかの誤り |", "|---|---:|---:|---:|---:|"]
    for arm in ("A", "L"):
        m = mean[arm]
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% |")
    mark = lambda b: "満たす" if b else "満たさない"  # noqa: E731
    L += ["", "| 決まり | 値 | 判定 |", "|---|---|---|",
          f"| 1. 正しい +0.5 ポイント以上 | {d_ok:+.2f} | {mark(checks[0])} |",
          f"| 2. 重大が増えない | {d_crit:+d} | {mark(checks[1])} |",
          f"| 3. ほかの誤りの増え < 正しいの増え | {d_wrong:+.2f} 対 {d_ok:+.2f} | {mark(checks[2])} |",
          f"| 4. 差の 90% 区間の下限 > 0（表で引き直し、3 組の平均） | {lo:+.2f} 〜 {hi:+.2f} | {mark(checks[3])} |",
          "", f"**判定：L を{'採る' if adopt else '採らない'}**", "",
          "## 追加で読むだけ：種子ごとの同じ列どうし", "", "| 比べ | A だけ正しい | L だけ正しい | McNemar p | 差の 90% 区間 |", "|---|---:|---:|---:|---|"]
    for s in SEEDS:
        n10, n01, pval = D.mcnemar(per[f"A{s}"], per[f"L{s}"])
        a, b = D.boot_diff(per[f"A{s}"], per[f"L{s}"], tables)
        L.append(f"| A{s} 対 L{s} | {n10} | {n01} | {pval:.3f} | {a:+.2f} 〜 {b:+.2f} |")
    text = "\n".join(L) + "\n"
    if len(sys.argv) > 1:
        print(text)
        return
    open(os.path.join(HERE, "d2_eval_decide.md"), "w", encoding="utf-8").write(text)
    json.dump(per, open(os.path.join(HERE, "d2_eval_decide_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(text)


if __name__ == "__main__":
    main()
