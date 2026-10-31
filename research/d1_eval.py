"""D1 の判定（2026-10-31 Claude。事前記録 bench/d1_prereg_20261030.md）。

決める陣（bench/d1_split_20261031.json の decide 側、set は materials/pool/work/d1dec）で、6 本の予測（pred_d1_job1〜6.json）を
今の製品の形（見張り → recheck F4・F8 → 検査役 v2 → rho 0.8 → 通貨の手がかり。research/fixes/eval_fixes.run と同じ）に通して数える。
正解は各陣の answers_final/（無い陣は ChatGPT、それも無い陣は Claude の答え。bench/d1_counts.batch_rows と同じ）。
採点は eval_fixes.run と同じ範囲（正解が unknown・S・other・person の列は数えない）。

  python research/d1_eval.py [decide|confirm] [予測のフォルダ（試し用。書き出さない）]   → research/d1_eval_<side>.md

採る決まり（事前記録）：A と比べて、正しいが種子 2 つの平均で +0.5 ポイント以上、重大の合計が増えない、ほかの誤りの増えが正しいの増えより少ない。
追加で読むだけ（オーナー許可 2026-10-31、research/next-steps-2026-10-31.md の 1）：同じ列どうしの McNemar と、表単位のブートストラップの差の 90% 区間。
"""
import json
import math
import os
import random
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
for p in (ROOT, os.path.join(ROOT, "research", "fixes"), os.path.join(ROOT, "bench")):
    sys.path.insert(0, p)
import pool_bench as B  # noqa: E402
import research.unknown.audit as A  # noqa: E402
import eval_fixes as EF  # noqa: E402
import d1_counts  # noqa: E402

V, E = A.V, A.E
PRODUCT = ("F4", "F8")   # 製品に入っている直し（research/fixes/confirm_adopted.md）
JOBS = {1: ("A", 1), 2: ("A", 2), 3: ("V", 1), 4: ("V", 2), 5: ("U", 1), 6: ("U", 2)}
BATCHES = [f"b{n:03d}" for n in range(66, 91) if n != 82]


def label_fixes(path):
    """正解の裁定（research/labels/*/decisions.jsonl）→ {列 id: 新しい正解}。D3 から使う（D1・D2 の数字は直さない）。"""
    return {d["id"]: d["decision"] for d in map(json.loads, open(path, encoding="utf-8")) if d["decision"] != d["current"]}


def load_side(side, fixes=None):
    """fixes：{列 id: 正解} を渡すと、その列の正解を差し替える（label_fixes の結果）。"""
    split = json.load(open(os.path.join(ROOT, "bench", "d1_split_20261031.json"), encoding="utf-8"))["publishers"]
    fixes = fixes or {}
    out = {}
    for b in BATCHES:
        w = B.WORK / b
        corpus, labels = d1_counts.batch_rows(b)
        sets = json.load(open(w / "set.json", encoding="utf-8"))["columns"]
        cols = []
        for i, (c, l, s) in enumerate(zip(corpus, labels, sets)):
            if split[c.get("publisher") or c.get("source", "?")] != side:
                continue
            vals = [str(v) for v in (c.get("row_values") or c["values"]) if str(v).strip() not in B.JUNK] or [str(v) for v in s["values"]]
            cols.append({"batch": b, "i": i, "id": s["id"], "table": c["table"], "header": str(c["header"]),
                         "values5": [str(v) for v in s["values"]], "values": vals, "context": [str(x) for x in s.get("siblings") or []],
                         "unit": str(s.get("unit") or ""), "language": c.get("language", ""), "truth": fixes.get(s["id"], l["label"]), "adjudicated": True,
                         "teacher": fixes.get(s["id"], l["label"]),
                         "tab": {"rows": c.get("row_values") or c["values"], "row_index": c.get("row_index"), "total": c.get("datastore_total")}})
        if cols:
            out[b] = cols
    return out


def with_job(data, pred_path):
    rows = {r["id"]: r for r in json.load(open(pred_path, encoding="utf-8"))["rows"]}
    res = {}
    for b, cols in data.items():
        te = []
        for c in cols:
            r = rows[c["id"]]
            te.append({**c, "pred": r["guarded_prediction"], "top3": r["top3"], "guard_reason": r.get("decision_reason")})
        res[b] = te
    return res


def outcome(final, truth):
    if final == "unknown":
        return "unk"
    if final == truth:
        return "ok"
    return "crit" if final in V.NUMERIC and truth in V.NUMERIC else "wrong"


def mcnemar(a, b):
    """同じ列で A が正しく B が誤り（n10）・その逆（n01）。連続補正つきの χ² と p（自由度 1）。"""
    n10 = sum(1 for k in a if a[k] == "ok" and b[k] != "ok")
    n01 = sum(1 for k in a if a[k] != "ok" and b[k] == "ok")
    if n10 + n01 == 0:
        return n10, n01, 1.0
    chi = (abs(n10 - n01) - 1) ** 2 / (n10 + n01)
    return n10, n01, math.erfc(math.sqrt(chi / 2))


def boot_diff(a, b, tables, reps=2000, seed="d1-boot"):
    """表を引き直すブートストラップで、正しいの割合の差（b − a、ポイント）の 90% 区間。"""
    by = {}
    for k, t in tables.items():
        by.setdefault(t, []).append(k)
    keys = list(by)
    rng = random.Random(seed)
    diffs = []
    for _ in range(reps):
        pick = [k for t in (rng.choice(keys) for _ in keys) for k in by[t]]
        n = len(pick)
        diffs.append(100 * (sum(b[k] == "ok" for k in pick) - sum(a[k] == "ok" for k in pick)) / n)
    diffs.sort()
    return diffs[int(0.05 * reps)], diffs[int(0.95 * reps) - 1]


def main():
    side = sys.argv[1] if len(sys.argv) > 1 else "decide"
    folder = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "materials", "pool", "work", "d1dec" if side == "decide" else "d1conf")
    labels = list(V.LABELS)
    train = [c for b in A.TRAIN for c in E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = load_side(side)
    shas = json.load(open(os.path.join(folder, "weights_sha256.json"), encoding="utf-8"))
    res, per = {}, {}
    for j in JOBS:
        EF._PCACHE.clear()
        data = with_job(base, os.path.join(folder, f"pred_d1_job{j}.json"))
        p = {}
        res[j] = EF.run(data, mv, labels, PRODUCT, per=p)
        per[j] = {k: outcome(v[0], v[1]) for k, v in p.items()}
    tables = {c["id"]: (c["batch"], c["table"]) for cols in base.values() for c in cols if c["id"] in per[1]}
    L = [f"# D1 の判定：{'決める陣' if side == 'decide' else '確かめる陣'}（`research/d1_eval.py {side}`）", "",
         f"- 製品の形（見張り → recheck F4・F8 → 検査役 v2 → rho {A.RHO} → 通貨の手がかり）。採点は正解が unknown・S・other・person でない列。",
         "- 事前記録 `bench/d1_prereg_20261030.md` の採る決まりで読む。McNemar・表単位のブートストラップは追加で読むだけ。", "",
         "| 仕事 | 形 | 種子 | 重みの SHA-256（先頭） | 採点列 | 正しい | 不明 | 重大 | ほかの誤り |", "|---|---|---:|---|---:|---:|---:|---:|---:|"]
    for j, (arm, seed) in JOBS.items():
        n, ok, unk, crit, wrong = res[j]
        L.append(f"| {j} | {arm} | {seed} | {shas[f'job{j}']['sha256'][:12]} | {n} | {ok}（{ok / n:.2%}） | {unk}（{unk / n:.2%}） | {crit} | {wrong} |")
    mean = {}
    for arm in ("A", "V", "U"):
        js = [j for j, (a, _) in JOBS.items() if a == arm]
        n = res[js[0]][0]
        mean[arm] = {"ok": sum(100 * res[j][1] / res[j][0] for j in js) / 2, "unk": sum(100 * res[j][2] / res[j][0] for j in js) / 2,
                     "crit": sum(res[j][3] for j in js), "wrong": sum(100 * res[j][4] / res[j][0] for j in js) / 2, "n": n}
    L += ["", "## 種子 2 つの平均と採る決まり", "", "| 形 | 正しい | 不明 | 重大（合計） | ほかの誤り | A との差：正しい | 重大 | ほかの誤り | 採る決まり |", "|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for arm in ("A", "V", "U"):
        m, a = mean[arm], mean["A"]
        d_ok, d_crit, d_wrong = m["ok"] - a["ok"], m["crit"] - a["crit"], m["wrong"] - a["wrong"]
        verdict = "（基準）" if arm == "A" else ("**採る**" if d_ok >= 0.5 and d_crit <= 0 and d_wrong < d_ok else "採らない")
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | "
                 + ("—" if arm == "A" else f"{d_ok:+.2f} | {d_crit:+d} | {d_wrong:+.2f}") + (" | — | —" if arm == "A" else "") + f" | {verdict} |")
    L += ["", "## 追加で読むだけ：同じ列どうしの比べ（種子ごと）", "", "| 比べ | A だけ正しい | 相手だけ正しい | McNemar p | 差の 90% 区間（ポイント、表で引き直し） |", "|---|---:|---:|---:|---|"]
    for arm, js in (("V", (3, 4)), ("U", (5, 6))):
        for s, (ja, jb) in enumerate(zip((1, 2), js), 1):
            n10, n01, pval = mcnemar(per[ja], per[jb])
            lo, hi = boot_diff(per[ja], per[jb], tables)
            L.append(f"| A{s} 対 {arm}{s} | {n10} | {n01} | {pval:.3f} | {lo:+.2f} 〜 {hi:+.2f} |")
    text = "\n".join(L) + "\n"
    if len(sys.argv) > 2:   # 試しのフォルダのときは書かない
        print(text)
        return
    open(os.path.join(HERE, f"d1_eval_{side}.md"), "w", encoding="utf-8").write(text)
    json.dump({str(j): per[j] for j in per}, open(os.path.join(HERE, f"d1_eval_{side}_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(text)


if __name__ == "__main__":
    main()
