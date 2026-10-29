"""不明になった列の調査：ChatGPT の決め手から作った手がかりの候補を、不明 329 列に当てて数える（2026-10-29 Claude）。
**決める陣（不明 329 列そのもの）での参考値**。採るかどうかは、事前記録を書いてから別の陣で確かめて決める（README）。
Grok の答えは使わない（compare.md：同じラベルが最大 16 行続き、答えた 162 列の正しい割合 35.2%・重大 89）。
出力：research/unknown/candidates.md
使い方：python research/unknown/candidates.py
"""
import json
import os
import re
import unicodedata
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
NUMERIC = {"date", "amount", "quantity", "rate", "id"}
SCORED = 2852


def norm(s):
    return unicodedata.normalize("NFKC", str(s or "")).replace("\n", " ").strip()


# 候補（名前, 種類, 列名に当てる正規表現, 値に当てる正規表現（なければ None））。列名・値は NFKC 後（｣ → 」）
CANDS = [
    ("A 文字化けの £（｣→」）を通貨に", "amount", re.compile(r"[(（]\s*」|」\s*m\b|\bin\s*」", re.I), None),
    ("A' 値の先頭が文字化けの £", "amount", None, re.compile(r"^」\s*-?\d[\d,]*(\.\d+)?$")),
    ("B 列名の URI・URL と値が http の識別子", "id", re.compile(r"ur[il]$", re.I), re.compile(r"^https?://\S+/(id|ID|doc|service|entertainment|def)/")),
    ("C 列名の kWh・MWh・GWh・filesize", "quantity", re.compile(r"(^|_|\b)[kmg]wh\b|_[kmg]wh$|filesize|megabytes", re.I), None),
    ("D1 ドイツ語の数量（anzahl・bestand・summe von・gemeinden・electorat）", "quantity", re.compile(r"anzahl|bestand$|^summe von|gemeinden$|^electorat", re.I), None),
    ("D2 ドイツ語の率（prozent・quote・grad・beteiligung）", "rate", re.compile(r"prozent|quote(_|$)|grad(_|$)|beteiligung", re.I), None),
    ("D3 ドイツ語・スイスの金額（chf・betrag・ausgaben・kosten）", "amount", re.compile(r"\bchf\b|_chf_|beitrag|betrag|ausgaben|kosten", re.I), None),
    ("D4 ドイツ語の日付（jahr・monat・datum・datierung）・pubdate", "date", re.compile(r"^(jahr|monat)$|datum|datierung_(von|bis)$|^pubdate", re.I), None),
    ("D5 ドイツ語の番号（_code・_nr・laufnummer）", "id", re.compile(r"_code$|_nr$|laufnummer", re.I), None),
    ("E 英語の金額の語（value of・contract value・paybill・surplus amount・income amount）", "amount", re.compile(r"\bvalue of\b|contract_?value|paybill|surplus ?amount|incomeamount|sumofamount|fare\b", re.I), None),
    ("F 英語の率（percent が語の中・per 1000）", "rate", re.compile(r"percent|per\s*1000", re.I), None),
]


def hit(cand, r):
    _, _, hp, vp = cand
    h = norm(r["header"])
    vals = [norm(v) for v in r["values"] if norm(v)]
    if hp is not None and not hp.search(h):
        return False
    if vp is not None:
        n = sum(bool(vp.search(v)) for v in vals)
        if not vals or n < max(1, len(vals) // 2):
            return False
    return True


def main():
    rows = [json.loads(l) for l in open(os.path.join(HERE, "compare.jsonl"), encoding="utf-8")]
    L = ["# 不明になった列の調査：手がかりの候補（`research/unknown/candidates.py`）", "",
         "- **決める陣（不明 329 列そのもの）での参考値**。ここで作った候補なので当てはまりは良く見える。採るかどうかは事前記録を書いてから別の陣で確かめる",
         "- 重大＝答えも正解も数字の種類で違うもの（score_real と同じ）。「ChatGPT と同じ」は ChatGPT の答えと一致した数",
         f"- 合格線（不明 10% 以下）まで {329 - int(SCORED * 0.10)} 列", "",
         "| 候補 | 種類 | 当たった列 | 表 | 陣 | 正しい | 重大 | ほかの誤り | ChatGPT と同じ |", "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    tab = {json.loads(l)["id"]: json.loads(l)["table"] for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")}
    got = {}
    for c in CANDS:
        hs = [r for r in rows if hit(c, r)]
        ok = sum(r["truth"] == c[1] for r in hs)
        crit = sum(r["truth"] != c[1] and r["truth"] in NUMERIC and c[1] in NUMERIC for r in hs)
        L.append(f"| {c[0]} | {c[1]} | {len(hs)} | {len({tab[r['id']] for r in hs})} | {len({r['batch'] for r in hs})} | {ok} | {crit} | {len(hs) - ok - crit} | {sum(r['chatgpt'] == c[1] for r in hs)} |")
        for r in hs:
            got.setdefault(r["u"], set()).add(c[1])
    conflict = sum(len(v) > 1 for v in got.values())
    union = [r for r in rows if len(got.get(r["u"], ())) == 1]
    lab = {r["u"]: next(iter(got[r["u"]])) for r in union}
    ok = sum(lab[r["u"]] == r["truth"] for r in union)
    crit = sum(lab[r["u"]] != r["truth"] and r["truth"] in NUMERIC and lab[r["u"]] in NUMERIC for r in union)
    ntab = len({tab[r["id"]] for r in union})
    after = 329 - ok - crit - (len(union) - ok - crit)
    L += ["", f"- すべての候補を合わせると：答えになる列 **{len(union)}**（{ntab} 表から。正しい {ok}・重大 {crit}・ほかの誤り {len(union) - ok - crit}）。2 つの種類が当たって決めない列 {conflict}",
          f"- 不明 {329} → {after}（採点 {SCORED} 列の {after / SCORED:.1%}）。正解率は {ok} 列ぶん上がる", ""]
    wrong = [r for r in union if lab[r["u"]] != r["truth"]]
    if wrong:
        L += ["## 候補が誤った列", "", "| u | 見出し | 値 | 正解 | 候補 |", "|---|---|---|---|---|"]
        L += [f"| {r['u']} | {norm(r['header'])[:40]} | {' / '.join(norm(v)[:15] for v in r['values'][:3])} | {r['truth']} | {lab[r['u']]} |" for r in wrong]
    rest = Counter((r["reason"], r["truth"]) for r in rows if r["u"] not in lab and r["chatgpt"] == r["truth"])
    L += ["", "## 候補で拾えず、ChatGPT は正しく決めた列（理由・正解の種類、多い順）", "", "| 理由 | 正解 | 列 |", "|---|---|---:|"]
    L += [f"| {a} | {b} | {n} |" for (a, b), n in rest.most_common(20)]
    open(os.path.join(HERE, "candidates.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
