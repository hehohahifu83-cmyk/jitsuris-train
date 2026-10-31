"""確かめる陣の誤り 200 列を、直せそうな知識の種類で分ける（2026-10-31 Claude。errors.jsonl を読んで決めた規則。読むだけ）。
  python research/confirm_why/groups.py
"""
import collections
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
G = [
    ("1 通貨の文字化け（｣＝£）で金額の手がかりが無い扱い", lambda o: o["truth"] == "amount" and any("｣" in v for v in o["values"] + [o["header"]])),
    ("2 日本語の金額の語（〜費・〜料・合計）で手がかりが無い扱い", lambda o: o["truth"] == "amount" and re.search(r"(費|料|料等|合\s*計|その他)$", o["header"])),
    ("3 Excel の日付の番号（5 桁）＋日付の列名", lambda o: o["truth"] == "date" and all(re.fullmatch(r"[34]\d{4}(\.0)?", v) for v in o["values"][:5] if v)),
    ("4 種類を表す公的なコードの一覧（GWR・NACE・ESA の部門・投票の種類・宗派など）", lambda o: o["truth"] == "category" and re.search(
        r"(_code$|code$|_id$|_ID$|-Code$|NACE|Sub.?Sector|sektor)", o["header"]) and o["top1"] == "id"),
    ("5 区域・物を指す番号（BFS の地区番号・鉄道の番号・UIC の国コードなど）", lambda o: o["truth"] in ("id", "address") and re.search(
        r"(bezirk|BEZIRK|numberShort|shortNumber|checkDigit|uicCountry|laufnummer|IDEDDP|BETREIBER_ID|FAHRT|Bezirks-ID|Dept$|PARK_NO|WARD|grundst|VZ-Sigel|Strassenbezeichnung Index|eingangs|BFS$|firmensitz|Obs$|index$|RBC Grant|STATISTIC)", o["header"])),
    ("6 名前の列が場所か団体か（〜公園・〜城・〜駐車場・駅の名前など、値の語尾）", lambda o: o["truth"] in ("address", "org") and o["top1"] in ("org", "address", "category", "text") and re.search(
        r"(名称|designation|Titel|Adresszusatz|staatsan)", o["header"])),
    ("7 有無の印（診療科・設備の列で値が 1・●）", lambda o: o["truth"] == "category" and all(v in ("1", "0", "●", "○", "1.0") for v in o["values"][:5] if v)),
    ("8 数えた数の列（EINWOHNER・AZ_・, Number・inflow・Flights など）", lambda o: o["truth"] == "quantity"),
    ("9 率の列（incidence・belegung・shr）", lambda o: o["truth"] == "rate"),
]


def main():
    rows = [json.loads(l) for l in open(os.path.join(HERE, "errors.jsonl"), encoding="utf-8")]
    got, rest = collections.defaultdict(list), []
    for o in rows:
        g = next((n for n, f in G if f(o)), None)
        (got[g] if g else rest).append(o)
    tot = sum(o["bad"] for o in rows)
    print(f"固有の列 {len(rows)}・誤りの出力（3 本の合計）{tot}")
    for n, _ in G:
        grp = got.get(n, [])
        reach = sum(1 for o in grp if o["truth_in_top3"] >= 2 and o["doubt"] >= 2)
        print(f"{n}：{len(grp)} 列・出力 {sum(o['bad'] for o in grp)}（迷いで届く {reach}）")
    print(f"そのほか：{len(rest)} 列・出力 {sum(o['bad'] for o in rest)}")
    for o in rest:
        print("   ", o["id"], o["header"][:30], o["truth"], o["top1"], "/", " ・ ".join(v[:12] for v in o["values"][:3]))


if __name__ == "__main__":
    main()
