"""保存した確率（probs_*.json）から、今の guard.py で答えを決め直して採点する（学習をやり直さずに、見張りの規則の変更を確かめる）。

何をするか：Kaggle の学習が eval_reports/latest/ に残す probs（上位3つの確率）と、同じ固定試験の列の値（materials の公開データ）を突き合わせ、
  decide() と同じ手順（確率 0.5 未満は不明 → guard → その他は不明）で答えを決め直す。保存されている答え（その学習のときの見張りの結果）と並べて出す。
安全のための確認：列名と正解が保存したものと一致しなければ止まる（試験の並びが違うまま採点しない）。
使い方：python rescore_guard.py eval_reports/latest [条件名（ft・sparse・blend50・blend60・blend70。省略で全部）] [置き場（job1・job2・report。省略で全部）]
未見セット（blind_set*）は扱わない。
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
import unicodedata

THRESHOLD = 0.5  # train3.decide の既定


def normalized_header(value):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(value)).strip()).casefold()


def load_tests():
    """encoder_exp.py と同じ作り方の固定試験 {試験名: [(列名, 値, 正解, 同じ表の列名)]}。"""
    from exp7 import load_real, split
    from dev_eval import rows_of
    strip = lambda rs: [(h, v, l, c) for h, v, l, c, _ in rs]
    jp_files = tuple(f for f in ("materials/real_labels_jp.jsonl", "materials/real_labels_jp2.jsonl") if os.path.exists(f))
    return {
        "開発用220": rows_of(),
        "本物（一般）": strip(split(load_real(("materials/real_labels.jsonl",)))[1]),
        "本物（業務）": strip(split(load_real(("materials/real_labels_biz.jsonl",)))[1]),
        "本物（業務2）": strip(split(load_real(("materials/real_labels_biz2.jsonl", "materials/real_labels_direct.jsonl")))[1]),
        "本物（日本の調達）": strip(split(load_real(jp_files))[1]) if jp_files else [],
    }


def decide_from_top3(top3, values, guard_fn, thr=THRESHOLD):
    order = [(t["label"], t["probability"]) for t in top3]
    lab = order[0][0] if order[0][1] >= thr else "unknown"
    if lab != "unknown":
        lab = guard_fn(lab, order, values)
    return "unknown" if lab == "other" else lab


def rescore(prob_rows, test_rows, guard_fn):
    """保存した行と試験の列を突き合わせて決め直す。返すのは決め直した答えの並び。"""
    if len(prob_rows) != len(test_rows):
        raise SystemExit(f"試験の列の数が違う：保存 {len(prob_rows)}／今 {len(test_rows)}")
    out = []
    for r, t in zip(prob_rows, test_rows):
        if r["column"] != normalized_header(t[0]) or r["truth"] != t[2]:
            raise SystemExit(f"列名か正解が保存と違う（試験の並びが変わった）：{r['column']!r} / {t[0]!r}")
        out.append(decide_from_top3(r["top3"], t[1], guard_fn))
    return out


def main(argv):
    import abstain_eval as ab
    from guard import guard
    from llm_baseline import score_real
    d = argv[1] if len(argv) > 1 else "eval_reports/latest"
    conds = [argv[2]] if len(argv) > 2 and argv[2] else ["ft", "sparse", "blend50", "blend60", "blend70"]
    tests = load_tests()
    lines = ["| 置き場 | 条件 | 試験 | 保存した答え | 今の guard.py で決め直し |", "|---|---|---|---|---|"]
    cell = lambda s: f"正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}"
    for cond in conds:
        for run in ([argv[3]] if len(argv) > 3 else ab.runs(d, cond)):
            for name, rows in ab.load(d, cond, run).items():
                if name not in tests:
                    continue
                truth = [r["truth"] for r in rows]
                new = rescore(rows, tests[name], guard)
                lines.append(f"| {run or '-'} | {cond} | {name} | {cell(score_real([r['prediction'] for r in rows], truth))} | {cell(score_real(new, truth))} |")
    print("\n".join(lines))


if __name__ == "__main__":
    main(sys.argv)
