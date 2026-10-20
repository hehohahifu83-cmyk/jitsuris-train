"""複数のモデル（グループ）の結果を、同じ物差しで並べる（2026-10-20）。slice_eval.py の部品を使う。

使い方：
  python compare_models.py --group 名前=置き場:job1,job2,job3 [--group 名前2=置き場2:job1,job2,job3] [--cond ft] [--min-support 5] [--out bench/compare.md]
例：
  python compare_models.py --group E5-base=eval_reports/runs/111:job1,job2,job3 --group mmBERT-small=eval_reports/runs/222:job1,job2,job3 --out bench/compare_xxx.md

- 置き場には、Kaggle の回収で作られる job<番号>_probs_<試験>_<条件>.json（列名・正解・予測・上位3つの確率だけ。列の値は入らない）が入っている。
- 実表の試験（dev220 以外。検証モードなら val_*）を合わせた行で数える。dev220 は回帰診断として別の表にだけ出す。
- 学習側の見出しの一覧は encoder_exp から作る（検証モードの結果を数えるときは環境変数 FT_VAL=1 を付ける）。
- 全体の正解率だけで決めない：正解率（見送りの正解を含む）／macro-F1（全体・未知見出し）／重大誤り／誤断定（誤答＋その他の誤受理）／不明／クラス別の適合率・再現率。
未見セット（blind_set*）は読まない。
"""
from __future__ import annotations

import math
import re
import sys
from collections import defaultdict

import slice_eval as S

SEEN_NAMES = S.SLICES   # ("既知ペア", "既知見出し・別ラベル", "未知見出し")
UNSEEN = S.SLICES[2]


def mean_sd(xs):
    xs = [x for x in xs if x == x]
    if not xs:
        return float("nan"), float("nan"), float("nan"), float("nan")
    m = sum(xs) / len(xs)
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1)) if len(xs) > 1 else 0.0
    return m, sd, min(xs), max(xs)


def job_records(records_by_key, run, include_dev220=False):
    """1 つの仕事の、実表の試験（dev220 以外）を合わせた行。"""
    out = []
    for (r, ds), rs in records_by_key.items():
        if r != run:
            continue
        if ds == "dev220" and not include_dev220:
            continue
        out.extend(rs)
    return out


def job_metrics(records, train_pairs, train_headers, min_support=5):
    """1 つの仕事（実表の試験を合わせた行）の指標。"""
    c = S.count(records)
    unseen = [r for r in records if S.slice_of(r["column"], r["truth"], train_pairs, train_headers) == UNSEEN]
    cu = S.count(unseen)
    mf, k = S.macro_f1(records, min_support=min_support)
    mfu, ku = S.macro_f1(unseen, min_support=min_support)
    tp, fp, fn, sup = S.class_stats(records)
    tpu, fpu, fnu, supu = S.class_stats(unseen)
    return {
        "n": c["n"], "acc": c["acc"], "wrong": c["wrong"], "unknown": c["unknown"], "other_ng": c["other_ng"], "critical": c["critical"],
        "false_assert": c["wrong"] + c["other_ng"],
        "macro_f1": mf, "macro_classes": k,
        "unseen_n": cu["n"], "unseen_acc": cu["acc"], "unseen_wrong": cu["wrong"], "unseen_unknown": cu["unknown"], "unseen_other_ng": cu["other_ng"],
        "unseen_critical": cu["critical"], "unseen_false_assert": cu["wrong"] + cu["other_ng"],
        "unseen_macro_f1": mfu, "unseen_macro_classes": ku,
        "class": {cl: (S.prf(tp[cl], fp[cl], fn[cl]), sup[cl]) for cl in sup},
        "class_unseen": {cl: (S.prf(tpu[cl], fpu[cl], fnu[cl]), supu[cl]) for cl in supu},
    }


def dataset_metrics(records_by_key, run):
    """試験ごとの数（dev220 を含む）。回帰診断用。"""
    out = {}
    for (r, ds), rs in records_by_key.items():
        if r == run:
            c = S.count(rs)
            out[ds] = {"n": c["n"], "acc": c["acc"], "wrong": c["wrong"], "unknown": c["unknown"], "critical": c["critical"], "other_ng": c["other_ng"]}
    return out


def pct(x, digits=1):
    return "—" if x != x else f"{x * 100:.{digits}f}%"


def cell(xs, fmt="pct"):
    m, sd, lo, hi = mean_sd(xs)
    if m != m:
        return "—"
    if fmt == "pct":
        return f"{m * 100:.1f}% ±{sd * 100:.1f}（{lo * 100:.1f}〜{hi * 100:.1f}）"
    if lo == hi:
        return f"{lo:.0f}"
    return f"{m:.1f} ±{sd:.1f}（{lo:.0f}〜{hi:.0f}）"


SUMMARY_ROWS = [
    ("実表の行数", "n", "int"),
    ("正解率（見送りの正解を含む）", "acc", "pct"),
    ("macro-F1（全体）", "macro_f1", "pct"),
    ("重大誤り（日付/金額/数量/割合/ID の取り違え）", "critical", "int"),
    ("誤答（15種類の取り違え）", "wrong", "int"),
    ("不明（見送り）", "unknown", "int"),
    ("その他の誤受理", "other_ng", "int"),
    ("誤断定（誤答＋その他の誤受理）", "false_assert", "int"),
    ("【未知見出し】行数", "unseen_n", "int"),
    ("【未知見出し】正解率", "unseen_acc", "pct"),
    ("【未知見出し】macro-F1", "unseen_macro_f1", "pct"),
    ("【未知見出し】重大誤り", "unseen_critical", "int"),
    ("【未知見出し】誤断定", "unseen_false_assert", "int"),
    ("【未知見出し】不明", "unseen_unknown", "int"),
]


def render(groups, title="モデルの比較", min_support=5, extras=None):
    """groups: {名前: {"jobs": {job: metrics}, "datasets": {job: {ds: m}}, "runs": 説明}}。markdown を返す。"""
    names = list(groups)
    lines = [f"# {title}", "", f"クラス別・macro-F1 は正解側に {min_support} 行以上あるクラスだけで平均。平均 ±標準偏差（最小〜最大）は仕事（種子）ごとの値から。", ""]
    if extras:
        lines += extras + [""]
    lines += ["## 実表の試験を合わせた結果", "", "| 指標 | " + " | ".join(f"{n}（{len(groups[n]['jobs'])} 本）" for n in names) + " |", "|---|" + "---|" * len(names)]
    for label, key, fmt in SUMMARY_ROWS:
        cells = [cell([m[key] for m in groups[n]["jobs"].values()], "pct" if fmt == "pct" else "int") for n in names]
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    # クラス別
    for key, ttl in (("class", "クラス別の適合率・再現率（実表を合わせた行）"), ("class_unseen", "クラス別の適合率・再現率（未知見出しだけ）")):
        classes = set()
        for n in names:
            for m in groups[n]["jobs"].values():
                classes |= set(m[key])
        first = groups[names[0]]["jobs"]
        sup = {c: max((m[key].get(c, (None, 0))[1] for m in first.values()), default=0) for c in classes}
        order = sorted((c for c in classes if sup[c] > 0), key=lambda c: -sup[c])
        lines += ["", f"## {ttl}", "", "| クラス | 正解側の行 | " + " | ".join(f"{n} 適合率 | {n} 再現率" for n in names) + " |", "|---|---:|" + "---:|---:|" * len(names)]
        for c in order:
            row = [c, str(sup[c])]
            for n in names:
                ps = [m[key][c][0][0] for m in groups[n]["jobs"].values() if c in m[key]]
                rs = [m[key][c][0][1] for m in groups[n]["jobs"].values() if c in m[key]]
                row += [pct(mean_sd(ps)[0]), pct(mean_sd(rs)[0])]
            lines.append("| " + " | ".join(row) + " |")
    # 試験ごと
    lines += ["", "## 試験ごと（回帰診断。dev220 を含む。判定には使わない）", "", "| 試験 | " + " | ".join(f"{n} 正解率 | {n} 重大 | {n} 不明" for n in names) + " |", "|---|" + "---:|---:|---:|" * len(names)]
    all_ds = sorted({ds for n in names for d in groups[n]["datasets"].values() for ds in d})
    for ds in all_ds:
        row = [ds]
        for n in names:
            accs = [d[ds]["acc"] for d in groups[n]["datasets"].values() if ds in d]
            cr = [d[ds]["critical"] for d in groups[n]["datasets"].values() if ds in d]
            un = [d[ds]["unknown"] for d in groups[n]["datasets"].values() if ds in d]
            row += [pct(mean_sd(accs)[0]), f"{mean_sd(cr)[0]:.1f}" if cr else "—", f"{mean_sd(un)[0]:.1f}" if un else "—"]
        lines.append("| " + " | ".join(row) + " |")
    lines += ["", "## 仕事ごとの値（実表を合わせた行）", "", "| 群 | 仕事 | 正解率 | macro-F1 | 重大 | 誤断定 | 不明 | 未知見出しの正解率 | 未知見出しの macro-F1 |", "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for n in names:
        for job, m in sorted(groups[n]["jobs"].items()):
            lines.append(f"| {n} | {job} | {pct(m['acc'])} | {pct(m['macro_f1'])} | {m['critical']} | {m['false_assert']} | {m['unknown']} | {pct(m['unseen_acc'])} | {pct(m['unseen_macro_f1'])} |")
    return "\n".join(lines) + "\n"


def parse_group(text):
    m = re.fullmatch(r"([^=]+)=([^:]+):((?:job\d+|report)(?:,(?:job\d+|report))*)", text)
    if not m:
        raise ValueError(f"--group は 名前=置き場:job1,job2 の形で書く: {text}")
    return m.group(1), m.group(2), m.group(3).split(",")


def build(group_specs, cond, train_pairs, train_headers, min_support=5):
    groups = {}
    for name, dir_, jobs in group_specs:
        rec = S.load_records(dir_, cond, jobs)
        if not rec:
            raise ValueError(f"{name}: {dir_} に条件 {cond} の記録がない")
        g = {"jobs": {}, "datasets": {}, "runs": dir_}
        for job in jobs:
            rs = job_records(rec, job)
            if not rs:
                raise ValueError(f"{name}: {dir_} の {job} に実表の記録がない")
            g["jobs"][job] = job_metrics(rs, train_pairs, train_headers, min_support)
            g["datasets"][job] = dataset_metrics(rec, job)
        groups[name] = g
    return groups


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    specs, cond, out, min_support, title = [], "ft", None, 5, "モデルの比較"
    while argv:
        a = argv.pop(0)
        if a == "--group":
            specs.append(parse_group(argv.pop(0)))
        elif a == "--cond":
            cond = argv.pop(0)
        elif a == "--out":
            out = argv.pop(0)
        elif a == "--min-support":
            min_support = int(argv.pop(0))
        elif a == "--title":
            title = argv.pop(0)
        else:
            raise SystemExit(__doc__)
    if not specs:
        print(__doc__)
        return 2
    pairs, heads = S.train_sets_from_encoder_exp()
    groups = build(specs, cond, pairs, heads, min_support)
    text = render(groups, f"{title}（条件 {cond}）", min_support, extras=[f"学習側の見出し {len(heads):,} 種類（encoder_exp の学習行）。置き場：" + "、".join(f"{n}={g['runs']}" for n, g in groups.items())])
    if out:
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
