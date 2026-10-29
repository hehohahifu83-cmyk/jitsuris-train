"""本体は正しいのに決め方の段が止めた列のうち、まだ原因を分けていない列（root_cause の M10）を、止めた段の規則のコードに沿って 1 列ずつ分ける（2026-10-30 Claude）。
分け方は上から順に当てる。どれも recheck.py・guard.py の規則と列の列名・値・同じ表の列名を見て決める（列ごとの表は m10.md）。
出力：research/unknown/m10.md
使い方：python research/unknown/m10.py
"""
import json
import os
import re
import sys
import unicodedata
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
import recheck as R  # noqa: E402
from rules_draft import present  # noqa: E402

CUR_SIB = re.compile(r"waehrung|währung|currency|devise|valuta", re.I)
MONEY_WORDS = re.compile(r"value|fare|tarif|inlandprodukt|vat|bonus|turnover|umsatz|preis|kosten|\bpay", re.I)
RATE_SIB = re.compile(r"satisf|agree|percent|%|share|quartile", re.I)
ID_WORDS = re.compile(r"reference|sensor|replicate|id\d|code|nr|number|nummer|plz|position", re.I)
QTY_WORDS = re.compile(r"\bpop\b|pop$|anzahl|headcount|count|cons\d|upper|lower|generation|total", re.I)


def classify(c):
    r = c["guard_reason"] or c["base_reason"] or c["veto_reason"] or ""
    h = unicodedata.normalize("NFKC", c["header"])
    vals = present(c["values"])
    sib = " ".join(c["siblings"])
    p1 = c["model_top3"][0][1]
    if r == "no_value_evidence":
        return "N1 値が 0 ばかり（recheck の no_value_evidence。b013・b014 で決めた規則で、新しい陣では損だけ）"
    if r == "numeric_values_not_parseable":
        return "N2 値の書き方を数と読めない（4.28:1・97604|22805 などの区切り）"
    if r == "amount_without_cue":
        if CUR_SIB.search(sib):
            return "N3 同じ表に通貨の列があるのに、通貨の手がかりは列名と単位の列しか見ない"
        if MONEY_WORDS.search(h):
            return "N4 列名に金額の語があるが、手がかりの辞書にない（value・fare・Tarif・Bruttoinlandprodukt・VAT など）"
        return "N5 通貨の手がかりが表のどこにもない（Total・Q1 (April - June 2014) など。人も表の外の知識で決める）"
    if r == "rate_without_cue":
        if RATE_SIB.search(h + " " + sib):
            return "N6 率と分かるのは同じ表の列名・満足度の段階など列名の外（率の手がかりは列名と単位の列しか見ない）"
        return "N7 率の手がかりの辞書の抜け（per 1000・perPikaHabitat など）"
    if r in ("low_confidence_no_cue", "probability_below_threshold"):
        if ID_WORDS.search(h) or QTY_WORDS.search(h):
            return "N8 本体の確信が低く（1 位 0.64〜0.94）、列名の語（pop・Reference・sensor など）が手がかりの辞書にない"
        return "N9 本体の確信が低い（しきい値の下）。列名に手がかりの語もない（Type of Post・Variable・Version など、人は値の中身で決める）"
    if r.startswith("verifier:"):
        return "N10 検査役（値の形の分類）が下げた。列名の手がかりは別の種類を示さない"
    if r.startswith("cue_conflict") or r.startswith("recheck:cue"):
        return "N11 列名の Number・number の語が番号と数量の両方に当たる"
    return "N12 そのほか"


def main():
    rc = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "root_cause.jsonl"), encoding="utf-8")}
    cols = [json.loads(l) for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")]
    xs = [(classify(c), c) for c in cols if rc[c["id"]]["mechanism"].startswith("M10")]
    L = [f"# 本体は正しいのに決め方の段が止めた {len(xs)} 列（M10）の分け（`research/unknown/m10.py`）", "", "| 分け | 列 |", "|---|---:|"]
    L += [f"| {k} | {n} |" for k, n in sorted(Counter(k for k, _ in xs).items())]
    L += ["", "| 分け | id | 見出し | 正解 | 本体 1 位 | 値 |", "|---|---|---|---|---|---|"]
    for k, c in sorted(xs, key=lambda x: x[0]):
        L.append(f"| {k.split(' ')[0]} | {c['id']} | {c['header'][:36].replace('|', '/')} | {c['truth']} | {c['model_top3'][0][0]} {c['model_top3'][0][1]} | {' / '.join(v[:14] for v in c['values'][:3]).replace('|', '/')} |")
    open(os.path.join(HERE, "m10.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
