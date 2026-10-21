"""学習側の元の列（水増しなし）で、見張り（guard）に落ちる列と、読めない値の形を数える。2026-10-21、Claude。

使う列は encoder_exp の学習側の表（gtr btr b2tr jtr）だけ。固定の試験側・主セット・封印セットは読まない。
規則（GUARD_V10_SPEC.md）を足す前の根拠づくりと、足した後の取りこぼしの確認に使う。出すのは集計と『形』（数字→9、英字→a、仮名漢字→K に潰した文字列と、代表の 1 例）。
使い方：python guard_train_side.py --out bench/guard_train_side_YYYYMMDD.md
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
import unicodedata
from collections import Counter, defaultdict

NUMERIC_LABELS = ("amount", "quantity", "rate")
_KANJI = re.compile(r"[ぁ-んァ-ン一-龥]")


def shape(v):
    """値を『形』に潰す。数字→9、英字→a、仮名漢字→K、同じ文字の連続は 1 つにまとめる。"""
    v = unicodedata.normalize("NFKC", str(v)).strip()[:30]
    out = []
    for ch in v:
        if ch.isdigit():
            out.append("9")
        elif "a" <= ch.lower() <= "z":
            out.append("a")
        elif _KANJI.match(ch):
            out.append("K")
        else:
            out.append(ch)
    return re.sub(r"9+", "9", re.sub(r"a+", "a", re.sub(r"K+", "K", "".join(out))))


def analyze(columns_by_stream, guard, value_stats, stat_names, first_n=5):
    """columns_by_stream: {名前: [(見出し, 値, ラベル, …)]}。guard＝guard モジュール、value_stats／stat_names＝features のもの。"""
    per = defaultdict(Counter)
    cols_with = {"date": Counter(), "num": Counter()}
    vals_with = {"date": Counter(), "num": Counter()}
    example = {"date": {}, "num": {}}
    for name, cols in columns_by_stream.items():
        for c in cols:
            vals, lab = list(c[1])[:first_n], c[2]
            if lab == "date":
                per[name]["date_total"] += 1
                strong, year = guard.date_shares(vals)
                s = dict(zip(stat_names, value_stats(vals)))
                best = max(s["date"] + s["datetime"], strong)
                if best < 0.5 and best + year < 0.5:
                    per[name]["date_fail"] += 1
                    seen = set()
                    for v in guard._clean(vals):
                        if not guard.is_date_value(v):
                            k = shape(v)
                            vals_with["date"][k] += 1
                            example["date"].setdefault(k, v)
                            if k not in seen:
                                cols_with["date"][k] += 1
                                seen.add(k)
            if lab in NUMERIC_LABELS:
                per[name]["num_total"] += 1
                if guard.num_loose_share(vals) < 0.5 and any(str(v).strip() for v in vals):
                    per[name]["num_fail"] += 1
                    seen = set()
                    for v in guard._clean(vals):
                        if not guard.NUM_LOOSE.match(v):
                            k = shape(v)
                            vals_with["num"][k] += 1
                            example["num"].setdefault(k, v)
                            if k not in seen:
                                cols_with["num"][k] += 1
                                seen.add(k)
    return {"per": per, "cols_with": cols_with, "vals_with": vals_with, "example": example}


def monotonicity(columns_by_stream, baseline_guard, current_guard, first_n=5):
    """Compare v9.1 and current acceptance on every real date/number column's first values.

    Only aggregate counts are returned; no source values or headers are emitted.
    """
    per = defaultdict(Counter)
    for name, cols in columns_by_stream.items():
        for c in cols:
            values, label = list(c[1])[:first_n], c[2]
            if label not in ("date", *NUMERIC_LABELS):
                continue
            old_values = baseline_guard._clean(values)
            new_values = current_guard._clean(values)
            per[name]["columns"] += 1
            if old_values != new_values:
                per[name]["cleaning_changes"] += 1
            if label == "date":
                for v in old_values:
                    if baseline_guard.is_date_value(v, True):
                        per[name]["date_strong_accepted_values"] += 1
                        if not current_guard.is_date_value(v, True):
                            per[name]["date_strong_losses"] += 1
                    if baseline_guard.is_date_value(v, False):
                        per[name]["date_accepted_values"] += 1
                        if not current_guard.is_date_value(v, False):
                            per[name]["date_value_losses"] += 1
                rival = "org"
            else:
                for v in old_values:
                    if baseline_guard.NUM_LOOSE.match(v):
                        per[name]["numeric_accepted_values"] += 1
                        if not current_guard.NUM_LOOSE.match(v):
                            per[name]["numeric_value_losses"] += 1
                rival = "text"
            order = [(label, 0.99), (rival, 0.001)]
            old_accept = baseline_guard.guard(label, order, values) == label
            new_accept = current_guard.guard(label, order, values) == label
            if old_accept:
                per[name]["v91_accepted_columns"] += 1
                if not new_accept:
                    per[name]["column_losses"] += 1
            if not old_accept and new_accept:
                per[name]["newly_accepted_columns"] += 1
    return per


def render_monotonicity(per):
    total = Counter()
    lines = ["", "## v9.1 受理の単調性（学習側の実データ）", "",
             "各学習列の先頭 5 値で、v9.1 の受理を v10 が失わないことを確認。値や見出しは出力しない。", "",
             "| 系統 | v9.1 受理列 | 新規受理列 | 日付強値 loss | 日付値 loss | 数値 loss | 列判定 loss | 正規化差 |",
             "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for name, c in per.items():
        total.update(c)
        lines.append(f"| {name} | {c['v91_accepted_columns']} | {c['newly_accepted_columns']} | {c['date_strong_losses']} | {c['date_value_losses']} | {c['numeric_value_losses']} | {c['column_losses']} | {c['cleaning_changes']} |")
    lines.append(f"| **合計** | **{total['v91_accepted_columns']}** | **{total['newly_accepted_columns']}** | **{total['date_strong_losses']}** | **{total['date_value_losses']}** | **{total['numeric_value_losses']}** | **{total['column_losses']}** | **{total['cleaning_changes']}** |")
    lines.append("")
    return "\n".join(lines)


def render(res, top=30):
    per = res["per"]
    total = Counter()
    L = ["# 学習側の元の列で、見張りに落ちる列（guard_train_side.py）", "",
         "学習側の表（gtr btr b2tr jtr。固定の試験側は含まない）。水増しなしの元の列。先頭 5 値で判定。",
         "日付：ラベルが date で、日付の値の割合が足りず date_value_evidence_low になる列。数：ラベルが金額・数量・率で、数に読めない値が半分以上の列（numeric_values_not_parseable）。", "",
         "| 学習の系統 | 日付の列（落ちる／全体） | 金額・数量・率の列（落ちる／全体） |", "|---|---:|---:|"]
    for name, c in per.items():
        total.update(c)
        L.append(f"| {name} | {c['date_fail']}／{c['date_total']} | {c['num_fail']}／{c['num_total']} |")
    L.append(f"| **合計** | **{total['date_fail']}／{total['date_total']}（{total['date_fail'] / max(1, total['date_total']):.1%}）** | **{total['num_fail']}／{total['num_total']}（{total['num_fail'] / max(1, total['num_total']):.1%}）** |")
    for key, title in (("date", "日付：読めない値の形（列の数の多い順）"), ("num", "数：読めない値の形（列の数の多い順）")):
        L += ["", f"## {title}", "", "| 列 | 値 | 形 | 代表の 1 例 |", "|---:|---:|---|---|"]
        for k, n in res["cols_with"][key].most_common(top):
            L.append(f"| {n} | {res['vals_with'][key][k]} | `{k}` | `{res['example'][key][k]}` |")
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--baseline", help="v9.1 guard.py loaded from the recorded v9.1 commit")
    a = ap.parse_args(argv)
    sys.argv = sys.argv[:1]
    import encoder_exp as E
    import guard
    from features import STAT_NAMES, value_stats
    streams = {"general": E.gtr, "biz": E.btr, "biz2": E.b2tr, "jp": E.jtr}
    report = render(analyze(streams, guard, value_stats, STAT_NAMES))
    failed = False
    if a.baseline:
        spec = importlib.util.spec_from_file_location("guard_v91_baseline", a.baseline)
        if spec is None or spec.loader is None:
            raise SystemExit("v9.1 guard baseline を読み込めません")
        baseline = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(baseline)
        mono = monotonicity(streams, baseline, guard)
        report += render_monotonicity(mono)
        failed = any(c[k] for c in mono.values() for k in ("date_strong_losses", "date_value_losses", "numeric_value_losses", "column_losses", "cleaning_changes"))
    text = report
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
