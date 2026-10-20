"""保存した 1 列ごとの結果（probs_*.json）を、「見出しが学習側にあるか」で分けて数え直す。macro-F1・クラスごとの適合率／再現率も出す（2026-10-20）。

背景：試験は表ごとに分けてあるが、同じ見出し（例：「金額」「VALUE」）が学習側の別の表にも出る。実表 4 試験（1,941 行）のうち、同じ（見出し, ラベル）が学習側にもある行は 66.4%、
見出しが学習側に全く無い行は 32.7%（635 行）。全体の正解率だけでは、見知らぬ見出しに強いかが分からない。ここでは次の 3 つに分けて数える：
  既知ペア           … 同じ（見出し, ラベル）が学習の行にある
  既知見出し・別ラベル … 見出しは学習にあるが、そのラベルでは無い（学習側で別の種類になっていた）
  未知見出し         … 見出しが学習の行に 1 つも無い（見知らぬ見出しへの強さ）
列の値は一切読まない（probs_*.json に入っていない）。未見セット（blind_set*）は読まない。

使い方：python slice_eval.py eval_reports/latest [条件 ft|blend70 …（既定 ft）] [--jobs job1 job2 …] [--out 出力.md]
  学習側の見出しの一覧は encoder_exp.rows（今の学習データ）から作る（numpy・scipy・scikit-learn が要る。torch は要らない）。
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

SLICES = ("既知ペア", "既知見出し・別ラベル", "未知見出し")
OK_OUTCOMES = {"correct", "other_ok"}


def normalized_header(value):
    """finetune_exp.normalized_header と同じ（NFKC・空白をまとめる・大小文字をそろえる）。"""
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(value)).strip()).casefold()


def slice_of(column, truth, train_pairs, train_headers):
    h = normalized_header(column)
    if (h, truth) in train_pairs:
        return SLICES[0]
    if h in train_headers:
        return SLICES[1]
    return SLICES[2]


def count(records):
    """records → 件数の辞書（score_real と同じ意味の outcome を数える）。"""
    c = Counter(r["outcome"] for r in records)
    n = len(records)
    return {"n": n, "correct": c["correct"], "wrong": c["wrong"], "unknown": c["unknown"],
            "other_ok": c["other_ok"], "other_ng": c["other_ng"],
            "critical": sum(1 for r in records if r.get("critical")),
            "acc": (c["correct"] + c["other_ok"]) / n if n else float("nan")}


def class_stats(records, key="guarded_prediction"):
    """クラスごとの TP・FP・FN。unknown と答えた行は『どのクラスにも当たらなかった』ので、正解クラスの FN に数える（正解が other のときの unknown は other の当たり）。"""
    tp, fp, fn, support = Counter(), Counter(), Counter(), Counter()
    for r in records:
        t, p = r["truth"], r.get(key) or r.get("prediction")
        if t == "other" and p == "unknown":
            p = "other"          # 15 種類に入らない列を「不明」と答えたのは正しい見送り（other の当たり）
        support[t] += 1
        if p == t:
            tp[t] += 1
        else:
            fn[t] += 1
            if p not in (None, "unknown"):
                fp[p] += 1
    return tp, fp, fn, support


def prf(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp else float("nan")
    r = tp / (tp + fn) if tp + fn else float("nan")
    f = 2 * p * r / (p + r) if p == p and r == r and p + r else (0.0 if tp + fn else float("nan"))
    return p, r, f


def macro_f1(records, key="guarded_prediction", min_support=1):
    """正解側に min_support 行以上あるクラスだけで平均する。"""
    tp, fp, fn, support = class_stats(records, key)
    fs = [prf(tp[c], fp[c], fn[c])[2] for c in support if support[c] >= min_support]
    fs = [f for f in fs if f == f]
    return (sum(fs) / len(fs) if fs else float("nan")), len(fs)


def load_records(dir_, cond, jobs=None):
    """{(置き場, 試験): records}。置き場は job1 など。blind は読まない。"""
    out = {}
    for path in sorted(glob.glob(os.path.join(dir_, f"*probs_*_{cond}.json"))):
        base = os.path.basename(path)
        if "blind" in base.lower():
            raise RuntimeError("blind test sets must not be evaluated")
        run = base.split("probs_")[0].rstrip("_")
        if jobs and run not in jobs:
            continue
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        out[(run, d["dataset"])] = d["rows"]
    return out


def train_sets_from_encoder_exp():
    """今の学習データの（見出し, ラベル）と見出しの集合。"""
    sys.argv = sys.argv[:1]
    import encoder_exp as E
    pairs, heads = set(), set()
    for r in E.rows:
        h = normalized_header(r[0])
        heads.add(h)
        pairs.add((h, r[2]))
    return pairs, heads


def fmt_pct(x):
    return "—" if x != x else f"{x:.1%}"


def report(records_by_key, train_pairs, train_headers, title, real_only=True):
    """markdown を返す。"""
    lines = [f"## {title}", ""]
    by_run = defaultdict(dict)
    for (run, ds), recs in records_by_key.items():
        by_run[run][ds] = recs
    for run in sorted(by_run):
        lines += [f"### {run}", "",
                  "| 試験 | 見出しの区分 | 行 | 正解（見送り正解含む） | 誤り | 不明 | その他の誤受理 | 重大 |",
                  "|---|---|---:|---:|---:|---:|---:|---:|"]
        pooled = defaultdict(list)
        for ds in sorted(by_run[run]):
            recs = by_run[run][ds]
            parts = defaultdict(list)
            for r in recs:
                s = slice_of(r["column"], r["truth"], train_pairs, train_headers)
                parts[s].append(r)
                if ds != "dev220":
                    pooled[s].append(r)
            for name in ("全体",) + SLICES:
                rs = recs if name == "全体" else parts.get(name, [])
                if not rs:
                    continue
                c = count(rs)
                lines.append(f"| {ds} | {name} | {c['n']} | {c['correct'] + c['other_ok']} ({fmt_pct(c['acc'])}) | {c['wrong']} | {c['unknown']} | {c['other_ng']} | {c['critical']} |")
        # 実表 4 試験をまとめた行
        allreal = [r for ds, recs in by_run[run].items() if ds != "dev220" for r in recs]
        if allreal:
            for name in ("全体",) + SLICES:
                rs = allreal if name == "全体" else pooled.get(name, [])
                if not rs:
                    continue
                c = count(rs)
                lines.append(f"| **実表4つ合計** | {name} | {c['n']} | {c['correct'] + c['other_ok']} ({fmt_pct(c['acc'])}) | {c['wrong']} | {c['unknown']} | {c['other_ng']} | {c['critical']} |")
            mf, k = macro_f1(allreal, min_support=5)
            mfu, ku = macro_f1(pooled.get(SLICES[2], []), min_support=5)
            lines += ["", f"macro-F1（実表4つ合計・正解側に 5 行以上あるクラス {k} 個の平均）：{fmt_pct(mf)}　／　未知見出しだけ：{fmt_pct(mfu)}（{ku} クラス）", ""]
    return "\n".join(lines)


def class_table(records, title, min_support=10):
    tp, fp, fn, support = class_stats(records)
    lines = [f"### {title}", "", "| クラス | 正解側の行 | 適合率 | 再現率 | F1 |", "|---|---:|---:|---:|---:|"]
    for c in sorted(support, key=lambda k: -support[k]):
        if support[c] < min_support:
            continue
        p, r, f = prf(tp[c], fp[c], fn[c])
        lines.append(f"| {c} | {support[c]} | {fmt_pct(p)} | {fmt_pct(r)} | {fmt_pct(f)} |")
    return "\n".join(lines)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print(__doc__)
        return 2
    dir_ = argv.pop(0)
    out_path = None
    jobs = None
    conds = []
    while argv:
        a = argv.pop(0)
        if a == "--out":
            out_path = argv.pop(0)
        elif a == "--jobs":
            jobs = []
            while argv and not argv[0].startswith("--") and re.fullmatch(r"job\d+|report|", argv[0]):
                jobs.append(argv.pop(0))
        else:
            conds.append(a)
    conds = conds or ["ft"]
    pairs, heads = train_sets_from_encoder_exp()
    parts = [f"# 見出しが学習側にあるかで分けた結果（学習の見出し {len(heads):,} 種類）", ""]
    for cond in conds:
        recs = load_records(dir_, cond, jobs)
        if not recs:
            parts.append(f"（条件 {cond} の記録なし）")
            continue
        parts.append(report(recs, pairs, heads, f"条件 {cond}"))
        first_run = sorted({k[0] for k in recs})[0]
        pooled = [r for (run, ds), rs in recs.items() if run == first_run and ds != "dev220" for r in rs]
        parts.append(class_table(pooled, f"クラスごとの適合率・再現率（{first_run}・条件 {cond}・実表4つ合計）"))
    text = "\n\n".join(parts) + "\n"
    if out_path:
        open(out_path, "w", encoding="utf-8").write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
