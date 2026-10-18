"""間違いの中身を見る：どの種類をどの種類と取り違えたか、重大な取り違えの列、「不明」にした正解の種類。

入力：probs_*_<条件>.json（Kaggle の学習が eval_reports/latest/ に残す。列名は正規化済み・列の値は入らない）。
使い方：python analyze_errors.py eval_reports/latest [条件名（既定 blend70）] [置き場（job1・job2・report。省略で全部）]
未見セット（blind_set*）は読まない。
"""
from __future__ import annotations

import sys
from collections import Counter

import abstain_eval as ab

NUMERIC = ab.NUMERIC


def classify(r):
    """1 列の結果 → 'correct' / 'wrong' / 'unknown' / 'other_ok' / 'other_ng'（score_real と同じ意味）。"""
    pred, truth = r["prediction"], r["truth"]
    if truth == "other":
        return "other_ok" if pred in ("unknown", "other") else "other_ng"
    if pred in ("unknown", "other"):
        return "unknown"
    return "correct" if pred == truth else "wrong"


def p_of(r, label):
    for t in r.get("top3", []):
        if t["label"] == label:
            return t["probability"]
    return None


def analyze(tests, top_pairs=8, max_critical=25):
    lines = []
    for name, rows in tests.items():
        kinds = Counter(classify(r) for r in rows)
        crit = [r for r in rows if classify(r) == "wrong" and r["prediction"] in NUMERIC and r["truth"] in NUMERIC]
        n = kinds["correct"] + kinds["wrong"] + kinds["unknown"]
        lines += [f"### {name}（種類つきの列 {n}、正解 {kinds['correct']}、誤り {kinds['wrong']}、不明 {kinds['unknown']}、重大 {len(crit)}、その他の見落とし {kinds['other_ng']}）", ""]
        pairs = Counter((r["truth"], r["prediction"]) for r in rows if classify(r) == "wrong")
        if pairs:
            lines += ["誤りの多い取り違え（正解 → 予測）：" + "、".join(f"{t}→{p} {c}" for (t, p), c in pairs.most_common(top_pairs)), ""]
        unk = Counter(r["truth"] for r in rows if classify(r) == "unknown")
        if unk:
            lines += ["「不明」にしてしまった正解の種類：" + "、".join(f"{t} {c}" for t, c in unk.most_common(top_pairs)), ""]
        if crit:
            lines += ["重大な取り違え（列名・正解→予測・予測の確率・正解の確率）：", ""]
            for r in sorted(crit, key=lambda r: -(r["top3"][0]["probability"] if r.get("top3") else 0))[:max_critical]:
                p1 = r["top3"][0]["probability"] if r.get("top3") else None
                pt = p_of(r, r["truth"])
                lines.append(f"- 「{r['column']}」 {r['truth']}→{r['prediction']}（予測 {p1:.2f}、正解 {('%.2f' % pt) if pt is not None else '上位3に無い'}）" if p1 is not None else f"- 「{r['column']}」 {r['truth']}→{r['prediction']}")
            lines.append("")
    return "\n".join(lines)


def main(argv):
    d = argv[1] if len(argv) > 1 else "eval_reports/latest"
    cond = argv[2] if len(argv) > 2 else "blend70"
    run = argv[3] if len(argv) > 3 else None
    for r in ([run] if run is not None else (ab.runs(d, cond) or [""])):
        print(f"## 置き場：{r or '（なし）'}／条件 {cond}\n")
        tests = ab.load(d, cond, r)
        print(analyze(tests) if tests else f"{d} に {cond} の probs が無い")
        print()


if __name__ == "__main__":
    main(sys.argv)
