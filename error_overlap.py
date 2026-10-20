"""2 つの仕事が『未知の見出し』で外した行の重なりを数える（2026-10-21）。モデルを替えても同じ行を外すのかを見る小さな道具。
使い方：
  python error_overlap.py <置き場>:<仕事> <置き場>:<仕事> [--names 名前A,名前B] [--cond ft] [--out bench/error_overlap_xxx.md]
例：
  python error_overlap.py eval_reports/runs/39435238999:job2 eval_reports/runs/39496935773:job2 --names "mmBERT-small(1e-4),E5-base(3e-5)" --out bench/error_overlap_validation_seed1.md
検証モード（FT_VAL=1）の結果を読む。この中で FT_VAL=1 を設定する。固定試験・blind は読まない。
2 つの仕事は同じ検証の行（同じ試験・同じ並び・同じ見出しと正解）でなければならない。外れたかどうかは slice_eval.OK_OUTCOMES（correct と、other を不明と答えた other_ok）で決める。
"""
from __future__ import annotations

import os
import sys
from collections import Counter

import slice_eval as S


def unseen_rows(records_by_key, run, train_pairs, train_headers):
    """{(試験, 並び): (見出し, 正解, 予測, 当たりか)}。未知の見出しの行だけ。"""
    out = {}
    for (r, ds), rows in records_by_key.items():
        if r != run:
            continue
        for i, x in enumerate(rows):
            if S.slice_of(x["column"], x["truth"], train_pairs, train_headers) != S.SLICES[2]:
                continue
            pred = x.get("guarded_prediction") or x.get("prediction")
            out[(ds, i)] = (x["column"], x["truth"], pred, x["outcome"] in S.OK_OUTCOMES)
    return out


def overlap(a, b):
    """a, b は unseen_rows の結果。同じ行でなければ ValueError。"""
    if set(a) != set(b):
        raise ValueError(f"行の集合が違う（A {len(a)} 行・B {len(b)} 行）。同じ検証の結果を渡す")
    for k in a:
        if a[k][:2] != b[k][:2]:
            raise ValueError(f"同じ行で見出しか正解が違う：{k} {a[k][:2]} / {b[k][:2]}")
    wrong_a = {k for k in a if not a[k][3]}
    wrong_b = {k for k in b if not b[k][3]}
    both = sorted(wrong_a & wrong_b)
    return {
        "n": len(a), "wrong_a": len(wrong_a), "wrong_b": len(wrong_b), "both": both,
        "only_a": sorted(wrong_a - wrong_b), "only_b": sorted(wrong_b - wrong_a),
        "same_prediction_in_both": sum(1 for k in both if a[k][2] == b[k][2]),
        "both_confusions": Counter((a[k][1], a[k][2], b[k][2]) for k in both),
        "only_a_confusions": Counter((a[k][1], a[k][2]) for k in sorted(wrong_a - wrong_b)),
        "only_b_confusions": Counter((b[k][1], b[k][2]) for k in sorted(wrong_b - wrong_a)),
    }


def render(res, a, b, name_a, name_b, top=8):
    n, both = res["n"], res["both"]
    lines = [f"# 未知の見出しで外した行の重なり：{name_a} と {name_b}", "",
             "検証モード（学習側の表の 1/8 を外した検証。固定試験・blind は使っていない）。外れ＝`slice_eval.OK_OUTCOMES` に入らない行。", "",
             "| | 行数 |", "|---|---:|",
             f"| 未知の見出しの行 | {n} |",
             f"| {name_a} が外した | {res['wrong_a']} |",
             f"| {name_b} が外した | {res['wrong_b']} |",
             f"| **両方が外した** | **{len(both)}** |",
             f"| {name_a} だけが外した | {len(res['only_a'])} |",
             f"| {name_b} だけが外した | {len(res['only_b'])} |",
             f"| 両方が外した行のうち、予測も同じ | {res['same_prediction_in_both']} |", "",
             f"## 両方が外した行の取り違え（正解 → {name_a} の予測／{name_b} の予測）", "",
             "| 正解 | 予測A | 予測B | 行数 |", "|---|---|---|---:|"]
    for (t, pa, pb), c in res["both_confusions"].most_common(top):
        lines.append(f"| {t} | {pa} | {pb} | {c} |")
    for name, key, title in ((name_a, "only_a_confusions", "だけが外した"), (name_b, "only_b_confusions", "だけが外した")):
        lines += ["", f"## {name} {title}（正解 → 予測）", "", "| 正解 | 予測 | 行数 |", "|---|---|---:|"]
        for (t, p), c in res[key].most_common(top):
            lines.append(f"| {t} | {p} | {c} |")
    lines += ["", "## 両方が外した行の見出し（重複を除く）", ""]
    seen, items = set(), []
    for k in both:
        col, truth, pa = a[k][0], a[k][1], a[k][2]
        if (col, truth) not in seen:
            seen.add((col, truth))
            items.append(f"`{col}`（正解 {truth}）")
    lines.append("、".join(items) if items else "なし")
    lines += ["", "注意：検証の記録に表の ID は無いため、同じ表の列かどうかは数えていない（見出しからの推測にとどまる）。"
              "同じ表の列は似た誤りをまとめて出しやすいので、行数は独立な件数ではない。"]
    return "\n".join(lines) + "\n"


def parse_spec(text):
    if ":" not in text:
        raise SystemExit(f"{text!r} は <置き場>:<仕事> の形で書く")
    dir_, job = text.rsplit(":", 1)
    return dir_, job


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) < 2 or argv[0].startswith("--"):
        print(__doc__)
        return 2
    spec_a, spec_b = parse_spec(argv.pop(0)), parse_spec(argv.pop(0))
    names, cond, out = None, "ft", None
    while argv:
        arg = argv.pop(0)
        if arg == "--names":
            names = argv.pop(0).split(",")
        elif arg == "--cond":
            cond = argv.pop(0)
        elif arg == "--out":
            out = argv.pop(0)
        else:
            raise SystemExit(__doc__)
    name_a, name_b = names if names and len(names) == 2 else ("A", "B")
    os.environ["FT_VAL"] = "1"      # 検証モードの学習側の見出しで数える（encoder_exp を読む前に設定）
    pairs, heads = S.train_sets_from_encoder_exp()
    a = unseen_rows(S.load_records(spec_a[0], cond, [spec_a[1]]), spec_a[1], pairs, heads)
    b = unseen_rows(S.load_records(spec_b[0], cond, [spec_b[1]]), spec_b[1], pairs, heads)
    if not a or not b:
        raise SystemExit("未知の見出しの行が読めなかった（置き場・仕事・条件を確かめる）")
    text = render(overlap(a, b), a, b, name_a, name_b)
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
