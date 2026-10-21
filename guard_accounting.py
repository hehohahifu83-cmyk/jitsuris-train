"""見張り（guard）の収支表。2026-10-21、Claude。

保存した予測（eval_reports/runs/<run>/job*_probs_<試験>_ft.json）から、見張りが
  ・正しい答えを不明にした件数（損）
  ・誤りを止めた件数（得。うち重大）
  ・誤りのまま通した件数（うち重大。組・確率）
を、理由ごとに数える。--rescore を付けると、いまの guard.py で答えを決め直し（値は materials の公開データから。rescore_guard.py と同じ作り）、
保存した答え（学習のときの見張り）との差を 4 つに分けて出す：
  A 不明 → 正解（取り戻した） / B 不明 → 誤り（増えた誤断定） / C B のうち重大 / D 通っていた → 不明（絞った）
見張りの規則を緩める変更（v10）の合格は、C が 0（重大な誤りが増えない）で、A が B を大きく上回ること。

使い方：
  python guard_accounting.py eval_reports/runs/39506074807            # 保存した答えの収支
  python guard_accounting.py eval_reports/runs/39506074807 --rescore  # いまの guard.py で決め直した差
  --out bench/xxx.md で表を保存。--include-val で検証（val_*）も数える（既定は実表の試験だけ。dev220 は除く）。
値は出力に書かない（列の番号と集計だけ）。未見セット（blind_set*）は扱わない。
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from collections import Counter

CRITICAL = {"date", "amount", "quantity", "rate", "id"}
THRESHOLD = 0.5


def is_critical(truth, pred):
    return truth != pred and truth in CRITICAL and pred in CRITICAL


def top1(row):
    return row["top3"][0]["probability"]


def tally(records):
    """records: [{truth, raw, decision, reason, p1}]。見張りの収支を数える。"""
    lost, saved, saved_crit, passed_wrong, passed_crit = Counter(), Counter(), Counter(), 0, []
    n = 0
    for r in records:
        n += 1
        t, raw, dec, reason = r["truth"], r["raw"], r["decision"], r["reason"]
        if dec == "unknown" and raw != "other":
            if raw == t:
                lost[reason] += 1
            else:
                saved[reason] += 1
                if is_critical(t, raw):
                    saved_crit[reason] += 1
        elif dec == raw and raw != t and t != "unknown":
            passed_wrong += 1
            if is_critical(t, raw):
                passed_crit.append((t, raw, r["p1"]))
    return {"n": n, "lost": lost, "saved": saved, "saved_crit": saved_crit, "passed_wrong": passed_wrong, "passed_crit": passed_crit}


def threshold_scenarios(records, thresholds=(0.6, 0.7, 0.8, 0.9, 0.95, 0.98)):
    """重大 5 種類の予測にだけ、確率の下限を上げたら（見張りを通った予測が対象）、正解をいくつ手放し、重大な誤りがいくつ残るか。"""
    ok = [r["p1"] for r in records if r["decision"] == r["raw"] and r["raw"] in CRITICAL and r["truth"] == r["raw"]]
    err = [r["p1"] for r in records if r["decision"] == r["raw"] and is_critical(r["truth"], r["raw"])]
    rows = []
    for thr in thresholds:
        rows.append((thr, sum(p < thr for p in ok), len(ok), sum(p >= thr for p in err), len(err)))
    return rows


def diff(old, new):
    """同じ並びの 2 つの決定を比べる。A 不明→正解、B 不明→誤り、C B のうち重大、D 通っていた→不明。"""
    if len(old) != len(new):
        raise ValueError("並びの長さが違います")
    a = b = c = d = 0
    for o, n in zip(old, new):
        t, raw = o["truth"], o["raw"]
        if o["decision"] == "unknown" and n["decision"] != "unknown":
            if n["decision"] == t:
                a += 1
            else:
                b += 1
                if is_critical(t, n["decision"]):
                    c += 1
        elif o["decision"] != "unknown" and n["decision"] == "unknown":
            d += 1
    return {"A": a, "B": b, "C": c, "D": d}


def load_records(run_dir, include_val=False):
    out = []
    for f in sorted(glob.glob(os.path.join(run_dir, "job*_probs_*_ft.json"))):
        with open(f, encoding="utf-8") as fh:
            doc = json.load(fh)
        ds = doc["dataset"]
        if "dev220" in ds or "dev220" in f:
            continue
        if ds.startswith("val_") and not include_val:
            continue
        out.append((os.path.basename(f), doc, [{"truth": r["truth"], "raw": r["raw_prediction"], "decision": r["guarded_prediction"],
                                              "reason": r["decision_reason"] or "-", "p1": top1(r), "top3": r["top3"], "column": r["column"]} for r in doc["rows"]]))
    return out


def rescore_records(records, tests_rows, guard_with_reason, thr=THRESHOLD):
    """保存した確率（上位 3 つ）と試験の値で、いまの見張りで決め直す。並びと正解が保存と違えば止まる。"""
    from rescore_guard import normalized_header
    if len(records) != len(tests_rows):
        raise SystemExit(f"試験の列の数が違う：保存 {len(records)}／今 {len(tests_rows)}")
    out = []
    for r, t in zip(records, tests_rows):
        if r["column"] != normalized_header(t[0]) or r["truth"] != t[2]:
            raise SystemExit("列名か正解が保存と違う（試験の並びが変わった）")
        order = [(x["label"], x["probability"]) for x in r["top3"]]
        if order[0][1] < thr:
            dec, reason = "unknown", "probability_below_threshold"
        else:
            dec, reason = guard_with_reason(order[0][0], order, t[1])
            if dec == "other":
                dec, reason = "unknown", "other_class"
        out.append({**r, "decision": dec, "reason": reason or "-"})
    return out


def render(title, stats, scen=None, delta=None):
    n = stats["n"]
    L = [f"## {title}", "", f"予測 {n} 件。見張りを通った誤り {stats['passed_wrong']} 件（{stats['passed_wrong'] / max(1, n):.2%}）、うち重大 {len(stats['passed_crit'])} 件。", "",
         "| 理由 | 正しい答えを不明にした（損） | 誤りを止めた（得） | うち重大 |", "|---|---:|---:|---:|"]
    for reason in sorted(set(stats["lost"]) | set(stats["saved"])):
        L.append(f"| {reason} | {stats['lost'][reason]} | {stats['saved'][reason]} | {stats['saved_crit'][reason]} |")
    L.append(f"| **合計** | **{sum(stats['lost'].values())}**（{sum(stats['lost'].values()) / max(1, n):.2%}） | **{sum(stats['saved'].values())}**（{sum(stats['saved'].values()) / max(1, n):.2%}） | **{sum(stats['saved_crit'].values())}** |")
    pairs = Counter((t, p) for t, p, _ in stats["passed_crit"])
    if pairs:
        L += ["", "見張りを通った重大な取り違え（正解→予測：件数）：" + "、".join(f"{t}→{p}：{c}" for (t, p), c in pairs.most_common()),
              "その確率（最上位）：" + " ".join(f"{p:.2f}" for _, _, p in sorted(stats["passed_crit"], key=lambda x: x[2]))]
    if scen:
        L += ["", "重大 5 種類の予測にだけ確率の下限を上げたら（見張りを通った予測が対象）：", "", "| 下限 | 手放す正解 | 残る重大な誤り |", "|---:|---:|---:|"]
        for thr, lostc, total_ok, rem, total_err in scen:
            L.append(f"| {thr} | {lostc}／{total_ok}（{lostc / max(1, total_ok):.1%}） | {rem}／{total_err} |")
    if delta:
        L += ["", f"保存した答え → いまの guard.py：A 不明→正解 {delta['A']}、B 不明→誤り {delta['B']}（うち重大 C {delta['C']}）、D 通っていた→不明 {delta['D']}。"]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("--rescore", action="store_true")
    ap.add_argument("--include-val", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    files = load_records(a.run_dir, a.include_val)
    if not files:
        raise SystemExit(f"予測ファイルがありません：{a.run_dir}")
    old_all, new_all = [], []
    if a.rescore:
        from guard import guard_with_reason
        from rescore_guard import load_tests
        tests = load_tests()
    for name, doc, recs in files:
        old_all += recs
        if a.rescore:
            if doc["test"] not in tests:
                raise SystemExit(f"試験の列を作れません：{doc['test']}（--include-val の検証は load_tests に未対応）")
            new_all += rescore_records(recs, tests[doc["test"]], guard_with_reason)
    text = [f"# 見張りの収支（{os.path.basename(a.run_dir.rstrip('/'))}、予測ファイル {len(files)} 本）", ""]
    text.append(render("保存した答え（学習のときの見張り）", tally(old_all), threshold_scenarios(old_all)))
    if a.rescore:
        text.append(render("いまの guard.py で決め直した答え", tally(new_all), threshold_scenarios(new_all), diff(old_all, new_all)))
    out = "\n".join(text)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(out)
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
