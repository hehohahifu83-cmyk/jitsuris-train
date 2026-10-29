"""C3 の判断のルールに入れる候補（下書き。2026-10-29 Claude）。不明・重大になった列の調査（research/unknown/）から作る。
**まだ製品の決め方には入れていない**。事前記録を書き、決める陣（新しい陣 8 つ）と確かめる陣を分けて試してから入れる。

使い方（決め方の段から）：
    from research.unknown.rules_draft import decide
    lab, rid = decide(header, unit, values, siblings)   # 当たらなければ (None, None)。2 つの種類が当たれば決めない (None, "conflict")
    lab, rid = guard_name_numeric(final, header, values) # 言い切った答えの安全の規則：名前の種類なのに値が数字だけ → id か不明へ

規則の出どころ（source）：A〜F＝ChatGPT が正しく決めた列の決め手（candidates.py）、G＝Claude の推論（claude_reasoning.py）、
H＝ChatGPT の説明（explain_compare.py で足す）。値は NFKC 後（文字化けの £ ｣ は 」 になる）。
"""
import re
import unicodedata

NUMERIC = {"date", "amount", "quantity", "rate", "id"}
NAME_KINDS = {"org", "address", "person", "product", "account", "text"}

# 欠けを表す記号（英国統計の [x] [z] [c]、アイルランド CSO の「.」、NA など）。値の形を読む前に外す（G1）
MISSING = re.compile(r"^\s*(\[[a-z]\]|\.{1,2}|-|–|—|:|\*|x|na|n/a|nan|nil|null|none|\.\.|<\s*\d+|s|c)\s*$", re.I)


def norm(s):
    return unicodedata.normalize("NFKC", str(s or "")).replace("\n", " ").strip()


def present(values):
    """欠けの記号と空を外した値（G1）。"""
    return [v for v in (norm(x) for x in values) if v and not MISSING.match(v)]


INT = re.compile(r"^[+-]?\d+$")
DEC = re.compile(r"^[+-]?\d+[.,]\d+$")
WEEK_VAL = re.compile(r"^((19|20)\d{2}[-_ ]?(W|KW)?\d{1,2}|(19|20)\d{2}\s*Q[1-4]|Q[1-4]\s*(19|20)\d{2}|Qtr\s*[1-4].*|(19|20)\d{2}-M\d{2}|\d{1,2})$", re.I)
TIME_RANGE = re.compile(r"^\d{1,2}[.:]\d{2}\s*[-–]\s*\d{1,2}[.:]\d{2}$")
LIKERT = re.compile(r"\b(very |fairly )?(satisfied|dissatisfied)\b|neither satisfied|got (everything|most|some|none) of what|\b(strongly )?(agree|disagree)\b", re.I)


def _share(vals, pat):
    return sum(bool(pat.search(v)) for v in vals) / len(vals) if vals else 0.0


def _ints(vals):
    return vals and all(INT.match(v.replace(",", "").replace("'", "")) for v in vals)


# (id, 種類, 説明, 当たるか (header, unit, vals, siblings) -> bool, 出どころ)
RULES = [
    ("A", "amount", "列名に文字化けの £（｣→」）：「(｣)」「｣m」「in ｣」", lambda h, u, v, s: bool(re.search(r"[(（]\s*」|」\s*m\b|\bin\s*」", h, re.I)), "A ChatGPT"),
    ("A2", "amount", "値の半分以上が文字化けの £ で始まる数", lambda h, u, v, s: _share(v, re.compile(r"^」\s*-?\d[\d,]*(\.\d+)?$")) >= 0.5, "A ChatGPT"),
    ("B", "id", "列名が URI・URL で終わり、値の半分以上が http://…/id|doc|service|def/…",
     lambda h, u, v, s: bool(re.search(r"ur[il]$", h, re.I)) and _share(v, re.compile(r"^https?://\S+/(id|doc|service|entertainment|def)/", re.I)) >= 0.5, "B ChatGPT"),
    ("C", "quantity", "列名に kWh・MWh・GWh・filesize・megabytes", lambda h, u, v, s: bool(re.search(r"(^|_|\b)[kmg]wh\b|_[kmg]wh$|filesize|megabytes", h, re.I)), "C ChatGPT"),
    ("D1", "quantity", "ドイツ語の数量：anzahl・…bestand・summe von・…gemeinden・electorat", lambda h, u, v, s: bool(re.search(r"anzahl|bestand$|^summe von|gemeinden$|^electorat", h, re.I)), "D ChatGPT"),
    ("D2", "rate", "ドイツ語の率：prozent・quote・…grad・…beteiligung", lambda h, u, v, s: bool(re.search(r"prozent|quote(_|$)|grad(_|$)|beteiligung", h, re.I)), "D ChatGPT"),
    ("D3", "amount", "ドイツ語・スイスの金額：chf・beitrag・betrag・ausgaben・kosten", lambda h, u, v, s: bool(re.search(r"\bchf\b|_chf_|beitrag|betrag|ausgaben|kosten", h, re.I)), "D ChatGPT"),
    ("D4", "date", "ドイツ語の日付：jahr・monat（列名がそれだけ）・datum・datierung_von/bis・pubdate", lambda h, u, v, s: bool(re.search(r"^(jahr|monat)$|datum|datierung_(von|bis)$|^pubdate", h, re.I)), "D ChatGPT"),
    ("D5", "id", "ドイツ語の番号：…_code・…_nr・laufnummer", lambda h, u, v, s: bool(re.search(r"_code$|_nr$|laufnummer", h, re.I)), "D ChatGPT"),
    ("E", "amount", "英語の金額の語：value of・contract value・paybill・surplus amount・income amount・sumofamount・fare",
     lambda h, u, v, s: bool(re.search(r"\bvalue of\b|contract_?value|paybill|surplus ?amount|incomeamount|sumofamount|fare\b", h, re.I)), "E ChatGPT"),
    ("F", "rate", "英語の率：語の中の percent・per 1000", lambda h, u, v, s: bool(re.search(r"percent|per\s*1000", h, re.I)), "F ChatGPT"),
    # ここから Claude の推論（claude_reasoning.md の「規則」）
    ("G2", "date", "週・四半期・期間の列名（week・woche・semaine・kw・yearweek・quarter・quartal・time_period・temporal・fiscal_year）で、値が週の番号・年と週・年と四半期",
     lambda h, u, v, s: bool(re.search(r"^(week|woche|semaine|kw|yearweek(iso)?|quarter|quartal|trimestre|time_period|temporal|fiscal_year)$", h.replace(" ", "_"), re.I))
     and _share(v, WEEK_VAL) >= 0.8 and not (_ints(v) and max(int(x) for x in v) > 53), "G Claude"),
    ("G3", "rate", "満足度・賛否の段階の列名で、値に小数があり 0〜100",
     lambda h, u, v, s: bool(LIKERT.search(h)) and any(DEC.match(x) for x in v) and all(_num(x) is not None and 0 <= _num(x) <= 100 for x in v), "G Claude"),
    ("G5", "id", "列名が「Id …」「… Id」「… Nr」「nummer」「Signatur」「reference」で、値が数字・コード",
     lambda h, u, v, s: bool(re.search(r"^id\b|\bid$|_id$|^id_|\bnr\.?$|_nr\b|nummer|^signatur$|reference$|\bref$", h, re.I)), "G Claude"),
    ("G6", "quantity", "列名が「No. …」（No. ill・No. laboratory confirmed）で値が整数", lambda h, u, v, s: bool(re.search(r"^no\.?\s+[a-z]", h, re.I)) and _ints(v), "G Claude"),
    ("G6b", "id", "列名が「No.」「No」だけで、値が 1 から並ぶ整数（行の番号）", lambda h, u, v, s: bool(re.fullmatch(r"no\.?", h, re.I)) and _ints(v), "G Claude"),
    ("G7", "date", "時刻の幅（09.00-11.45）が値の 8 割以上で、列名に uhrzeit・zeit・time", lambda h, u, v, s: bool(re.search(r"uhrzeit|zeit|time", h, re.I)) and _share(v, TIME_RANGE) >= 0.8, "G Claude"),
    ("G9", "quantity", "列名に decimals・nachkommastellen（小数の桁数）で値が整数", lambda h, u, v, s: bool(re.search(r"decimals|nachkommastellen", h, re.I)) and _ints(v), "G Claude"),
]


def _num(x):
    try:
        return float(x.replace(",", ""))
    except ValueError:
        return None


def decide(header, unit, values, siblings=()):
    """不明になった列に当てる。1 つの種類だけが当たればその種類、2 つ以上なら決めない。"""
    h, u = norm(header), norm(unit)
    v = present(values)
    hits = {}
    for rid, lab, _, f, _ in RULES:
        try:
            if f(h, u, v, siblings):
                hits.setdefault(lab, rid)
        except (ValueError, TypeError):
            continue
    if len(hits) == 1:
        lab, rid = next(iter(hits.items()))
        return lab, rid
    return (None, "conflict") if hits else (None, None)


def guard_name_numeric(final, header, values):
    """G8：名前の種類（org・address・person・product・account・text）なのに、欠けを除いた値がすべて数字だけ → 名前ではない。
    列名に番号の語（code・nr・number・id・no）があれば id、なければ不明。"""
    v = present(values)
    if final not in NAME_KINDS or not v or not all(re.fullmatch(r"[\d.,' ]+", x) for x in v):
        return final, None
    return ("id", "G8") if re.search(r"code|_nr|\bnr\b|number|\bid\b|_id|\bno\b", norm(header), re.I) else ("unknown", "G8")
