"""近い教材の列の見直し（neighbor_review.md）で見つかった付け方の食い違いの候補を、教材の全部から探す（2026-10-30 Claude。LABEL_GUIDE v2.3）。
  python research/labels/v23_targets.py   → research/labels/v23_targets.jsonl（Claude が 1 列ずつ決めて v23_decisions.jsonl）
"""
import json
import os
import re
from collections import Counter

import v22_targets as T

HERE = os.path.dirname(os.path.abspath(__file__))
URI2 = re.compile(r"^https?://(id\.\S+|\S+/(id|def|doc)/\S*)", re.I)
ACCT = re.compile(r"expense|expenditure ?type|cost ?type|kostenart|despesa|categoria_economica|elemento|natureza|receita|income ?type|revenue ?(category|type)|"
                  r"proclass|pesa|subjective|費目|科目|歳入|歳出|経費|款|^節$|支出区分|収入区分|merchant ?category|level_\d|区分[１２３1-3]?$", re.I)
TIME = re.compile(r"^\d{1,2}(:\d{2}(:\d{2})?\s*(am|pm)?|[.:]\d{2}\s*(am|pm)|\s*(am|pm))(\s*[-–~〜]\s*\d{1,2}([:.]\d{2})?\s*(am|pm)?)?$", re.I)
CODE_HDR = re.compile(r"^(measure|statistic|indicator|indicator_code|series|series_code|tlist.*)$", re.I)
CODE_VAL = re.compile(r"^[A-Z0-9_]{3,}$")


def rules(r):
    h, lab = str(r.get("header", "")), r.get("label")
    vals = [str(v).strip() for v in r.get("values", []) if str(v).strip()]
    out = []
    if lab != "id" and vals and not re.search(r"licen[cs]", h, re.I) and sum(bool(URI2.match(v)) for v in vals) >= max(1, len(vals) // 2):
        out.append(("B6_uri2", "id"))
    if lab in ("category", "text") and ACCT.search(h) and vals and not all(re.fullmatch(r"[\d.,\s-]+", v) for v in vals):
        out.append(("B7_account_check", None))
    if lab in ("text", "other", "category") and vals and sum(bool(TIME.match(v)) for v in vals) >= max(1, (len(vals) * 3) // 4):
        out.append(("B8_time", "date"))
    if CODE_HDR.match(h) and lab in ("category", "id") and vals:
        out.append(("B9_stat_code_check", None))
    if re.search(r"キーワード|keyword", h, re.I) and lab == "category":
        out.append(("text_keywords", "text"))
    if re.fullmatch(r"(parameter_)?decimals?", h, re.I) and lab == "category":
        out.append(("quantity_decimals", "quantity"))
    if r.get("batch") == "b009" and h == "Dept_Level_1" and lab == "account":
        out.append(("B2_ministry", "org"))
    return out


def main():
    out = []
    for name, k, r in T.rows():
        for rule, want in rules(r):
            out.append({"file": name, "line": k, "rule": rule, "header": r.get("header"), "unit": r.get("unit", ""), "label": r.get("label"),
                        "want": want, "values": [str(v) for v in r.get("values", [])[:5]], "context": r.get("context", [])[:8], "table": r.get("table")})
    with open(os.path.join(HERE, "v23_targets.jsonl"), "w", encoding="utf-8") as f:
        for x in out:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    print(Counter(x["rule"] for x in out))


if __name__ == "__main__":
    main()
