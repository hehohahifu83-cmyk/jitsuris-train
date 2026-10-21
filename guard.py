"""安全の見張り（値と食い違う答えは「不明」にする）。重大な誤り（日付・金額・数量・率・番号の取り違え）を減らすため。
Sherlock（KDD 2019）の「自信のないものは人に回す」の考え方。column-ai.js の guard と同じ（変えたら両方を直し、guard_fixtures.json で一致を確かめる）。

2026-10-18 の改良（v9 の見張り）：
- 日付の値の読み方が狭すぎた（LABEL_GUIDE の「日付・日時・時刻・年月・年度・年だけ」に合わせた）。
  年だけ（2023）・年度（2012/13、2023-24、1994/4-3.）・四半期（2014Q1、Q1 2012）・月名（05-May-17、31st March）・
  日/月/年（1/28/2008 12:00 AM）・時刻（03:35）・和暦（平成30年）を日付の値として読む。
- 金額・数量・率の値の読み方が狭すぎた。通貨記号（£ € ₩ ¥ $ と文字化けした ｣）・通貨コード（USD）・単位（円/人、kg、件）つきも数として読む。
- 年だけ（2000、1200 など）は金額や番号とも見分けがつかないので、その根拠だけで日付と認めるのは、答えの確率が 0.9 以上のときに限る。
固定試験での再計算：2 回の学習×4 つの組み合わせ×5 試験の延べ 15,960 列で、「不明」1,475 → 527、誤り 515 → 515、重大 105 → 105（誤りも重大も増えていない）。
ただし規則は固定試験の失敗を見て作ったので、その分は甘い数字。見ていない新しい表で確かめるまでは見込み。

2026-10-18 の締め直し（v9.1。ChatGPT のレビュー 13:01 の指摘）：緩すぎて日付・数に読んでしまう所を狭めた。誤りや重大を増やす方向ではなく、「不明」を増やす方向の変更のみ。
- 年度（FY）は最後まで形を見る（FY2024xyz は日付にしない）。年-月は月が 1〜12 のときだけ。年度の範囲（2023-24）は後の年が前の年の次（2 桁）か 0〜30 年先（4 桁）のときだけ（2020-99 は日付にしない）。
- 月名は『日 月名 年』『月名 日 年』『月名 年』『年 月名 日』（曜日・時刻つきも）の形のときだけ。文の中の may や march は日付にしない。
- 数は区切りの形を見る（1,234 と 1,234.5、12,34,567、1.234,56、1 234、12.5。1,,2 や 1 2 3 は数にしない）。features.py の NUM_RE（『1,,2』も数にする）は見張りでは使わない（モデルの特徴としては変えない）。
- 空白は『前後を落とす集合』を Python と JS で同じに決め（正規表現の空白の略記は使わない）、64 文字は文字（コードポイント）で数える。
"""

"""2026-10-21 Guard v10 P1/P2（作業中。GUARD_VERSION は回帰検査完了後に設定）:
- P1: D1・D3・D4・D5・D6 と N1・N2・N8、P2: D2・D7・D8・D9 と N3〜N7。
- 規則は仕様の表記定義と学習側の集計から追加し、v9.1 が受け入れていた形は維持する。
- `_enabled_rules` は規則単独の回帰寄与を測るときだけ使う。固定試験は規則づくりに使わず、再生で回帰だけを確認する。
"""

import re
import unicodedata

from features import value_stats, STAT_NAMES, DATE_RES, DATETIME_RE, TIME_RE

NUMERIC = {"date", "amount", "quantity", "rate", "id"}
YEAR_CONFIDENCE = 0.9  # 年だけの列を日付と認めるときに要る、答えの確率

_MONTH = r"(?:january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sept|sep|oct|nov|dec)"
# 空白の決め方を Python と JS で同じにする（\s は使わない：Python は \x1c〜\x1f・\x85 を含み、JS は \ufeff を含むなど集合が違う）
_SC = r" \t\n\r\f\v"                      # 文字クラスの中身
_S = "[" + _SC + "]"
_STRIP_CHARS = r"\t\n\v\f\r \x1c-\x1f\x85\xa0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff"   # 前後から落とす集合（JS の trim と Python の strip の違いをなくす）
_STRIP_RE = re.compile("^[" + _STRIP_CHARS + "]+|[" + _STRIP_CHARS + "]+$")
YEAR_ONLY = re.compile(r"^(19|20)[0-9]{2}$")
_MM = r"(?:0?[1-9]|1[0-2])"
DATE_EXTRA = [re.compile(p) for p in [
    r"^(19|20)[0-9]{2}" + _S + r"*[/\-]" + _S + r"*" + _MM + r"$",                                   # 2020-07  2020/7（月は 1〜12）
    r"^" + _MM + _S + r"*[/\-]" + _S + r"*(19|20)[0-9]{2}$",                                         # 07-2015（月は 1〜12）
    r"^(19|20)[0-9]{2}" + _S + r"*/" + _S + r"*[0-9]{1,2}" + _S + r"*-" + _S + r"*[0-9]{1,2}\.?$",    # 1994/4-3.（4月から3月の年度）
    r"^(19|20)[0-9]{2}年(度)?([0-9]{1,2}月)?$",                                                       # 2023年  2023年度  2023年4月
    r"^[0-9]{1,2}月([0-9]{1,2}日)?$",                                                                 # 4月  4月1日
    r"^(令和|平成|昭和|大正)[0-9元]+年",                                                                 # 平成30年
    r"^[rhs][0-9]{1,2}[./][0-9]{1,2}([./][0-9]{1,2})?$",                                             # H30/4/1
    r"^(19|20)[0-9]{2}" + _S + r"*-?" + _S + r"*q[1-4]$", r"^q[1-4]" + _S + r"*-?" + _S + r"*(19|20)?[0-9]{2}$",   # 2014Q1  Q1 2012
    r"^fy" + _S + r"*'?(19|20)?[0-9]{2}(?:" + _S + r"*[/\-–]" + _S + r"*(19|20)?[0-9]{2})?(?:" + _S + r"*-?" + _S + r"*(?:q[1-4]|h[12]))?$",   # FY2020  FY2020-21  FY20Q3（最後まで）
    r"^h[12]" + _S + r"*(19|20)[0-9]{2}$",                                                           # H1 2020
    r"^(19|20)[0-9]{2}m[0-9]{2}(d[0-9]{2})?$",                                                       # 2020M07D23
    r"^[0-9]{1,2}[/\-][0-9]{1,2}[/\-][0-9]{2,4}([ t][0-9]{1,2}:[0-9]{2}(:[0-9]{2})?" + _S + r"*(am|pm)?)?$",   # 1/28/2008  1/28/2008 12:00:00 AM
    r"^[0-9]{1,2}\.[0-9]{1,2}\.(19|20)[0-9]{2}$",                                                   # 31.12.2019
]]
_FY_RANGE = re.compile(r"^((?:19|20)[0-9]{2})" + _S + r"*[/\-–]" + _S + r"*((?:19|20)?[0-9]{2})(?:[_*\-" + _SC + r"]*(?:" + _MONTH + r"\.?|q[1-4]|h[12]))?[_*" + _SC + r"]*$")   # 2012/13  2012/2013  2023-24  2019/2020_  2017/2018_apr  2012/2013_q3
_D = r"[0-9]{1,2}(?:st|nd|rd|th)?"
_Y = r"(?:19|20)?[0-9]{2}"
_SEP = "[" + _SC + r"\-/.,]*"
_TIME = r"(?:[ t]+[0-9]{1,2}:[0-9]{2}(?::[0-9]{2})?" + _S + r"*(?:am|pm)?)?"
_WD = r"(?:(?:mon|tue|wed|thu|fri|sat|sun)(?:day|sday|nesday|rsday|urday)?\.?" + _SEP + r")?"
MONTH_FULL = [re.compile(p) for p in [
    r"^" + _WD + _D + _SEP + _MONTH + r"\.?(?:" + _SEP + _Y + r")?" + _TIME + r"$",                  # 05-may-17  31st march  5 may 2017
    r"^" + _WD + _MONTH + r"\.?" + _SEP + _D + r"(?:" + _SEP + _Y + r")?" + _TIME + r"$",             # may 5, 2017  march 31st
    r"^" + _MONTH + r"\.?" + _SEP + r"(?:19|20)[0-9]{2}$",                                           # march 2020
    r"^(?:19|20)[0-9]{2}" + _SEP + _MONTH + r"\.?(?:" + _SEP + _D + r")?" + _TIME + r"$",             # 2020 june 30  2020-mar-05  2016 mar 01 12:00:00 am
]]



# v10 P1/P2 additions. New date and number spellings are additive to v9.1.
MISSING_MARKERS = {
    "-", "−", "–", "—", "―", "ー", "…", "‥", ".", "..", "...",
    "*", "**", "***", "x", "n/a", "na", "n.a.", "nan", "nil", "null",
    "none", "#n/a", "#div/0!", "#value!", "#ref!", "#name?", "(na)", "(x)",
}
_MD_SLASH = re.compile(r"^(0?[1-9]|1[0-2])([/-])(0?[1-9]|[12][0-9]|3[01])$")
_MD_JP = re.compile(r"^(0?[1-9]|1[0-2])月(0?[1-9]|[12][0-9]|3[01])日$")
_JP_TIME_BODY = r"(?:午前|午後)?(?:0?[0-9]|1[0-9]|2[0-4])時(?:[0-5]?[0-9]分(?:[0-5]?[0-9]秒)?)?"
_JP_TIME = re.compile(r"^" + _JP_TIME_BODY + r"$")
_JP_TIME_RANGE = re.compile(r"^" + _JP_TIME_BODY + r"(?:[ \t]*から[ \t]*" + _JP_TIME_BODY + r")?$")
_MONTH_ONLY = re.compile(r"^" + _MONTH + r"\.?$")
_ERA_DATE = re.compile(r"^([mtshr])[ \t]*\.?[ \t]*([0-9]{1,2})[ \t]*[./-][ \t]*(0?[1-9]|1[0-2])(?:[ \t]*[./-][ \t]*(0?[1-9]|[12][0-9]|3[01])(?:日)?)?$")
_ERA_YEAR = re.compile(r"^([mtshr])[ \t]*([0-9]{1,2})(?:年度)?$")
_ERA_LIMITS = {"m": 45, "t": 15, "s": 64, "h": 31, "r": 30}
_AMBIGUOUS_QUARTER = re.compile(r"^(?:q[1-4]|[1-4]q)$")
_QUARTER_FULL = [re.compile(p) for p in [
    r"^(?:[0-9]{2}|(?:19|20)[0-9]{2})[ \t]*q[1-4]$",             # 24q1, 2024q1
    r"^[1-4](?:st|nd|rd|th)[ \t]+quarter$",
    r"^quarter[ \t]+[1-4]$",
    r"^第[1-4]四半期$",
    r"^(?:19|20)[0-9]{2}(?:年|年度)?第[1-4]四半期$",
    r"^(?:19|20)[0-9]{2}(?:年|年度)(?:上期|下期|上半期|下半期)$",
    r"^h[12]$",
]]
_DATE_PERIOD_SEP = re.compile(r"~|〜|～|" + _S + r"+-" + _S + r"+|–|—|から|" + _S + r"+to" + _S + r"+|" + _S + r"+au" + _S + r"+")
_YEAR_MONTH_PERIOD = re.compile(r"^(?:19|20)[0-9]{2}/[0-9]{1,2}-(?:19|20)[0-9]{2}/[0-9]{1,2}$")
_UNIX_TS = re.compile(r"^[1-9][0-9]*(?:\.[0-9]{1,6})?$")
_DATE_MONTH_PART = [re.compile(p) for p in [
    r"^(?:19|20)[0-9]{2}年$",
    r"^(?:19|20)[0-9]{2}年(?:0?[1-9]|1[0-2])月$",
    r"^(?:0?[1-9]|1[0-2])月$",
    r"^(?:令和|平成|昭和|大正)[0-9元]+年(?:0?[1-9]|1[0-2])月$",
]]
_WEEKDAY_NAME = r"(?:[月火水木金土日](?:曜日)?|mon(?:day)?|tue(?:sday)?|wed(?:nesday)?|thu(?:rsday)?|fri(?:day)?|sat(?:urday)?|sun(?:day)?)\.?"
_WEEKDAY_SUFFIX = re.compile(r"^(?P<base>.*?)(?:\((?:" + _WEEKDAY_NAME + r")\)|" + _S + r"+(?:" + _WEEKDAY_NAME + r"))(?P<tail>.*)$")


def _is_month_day(v):
    """Validate M/D, M-D, and M月D日 with calendar month bounds."""
    m = _MD_SLASH.match(v)
    if m:
        month, day = int(m.group(1)), int(m.group(3))
    else:
        m = _MD_JP.match(v)
        if not m:
            return False
        month, day = int(m.group(1)), int(m.group(2))
    return day <= (29 if month == 2 else 30 if month in (4, 6, 9, 11) else 31)


def _month_day_ge_13(v):
    m = _MD_SLASH.match(v) or _MD_JP.match(v)
    return bool(m and int(m.groups()[-1]) >= 13)


def _is_era_date(v):
    m = _ERA_DATE.match(v)
    if not m:
        return False
    era, year, month, day = m.groups()
    if not 1 <= int(year) <= _ERA_LIMITS[era]:
        return False
    return True


def _is_era_year(v):
    m = _ERA_YEAR.match(v)
    return bool(m and 1 <= int(m.group(2)) <= _ERA_LIMITS[m.group(1)])


def _is_quarter(v):
    return not _AMBIGUOUS_QUARTER.match(v) and any(r.match(v) for r in _QUARTER_FULL)


def _share_values(ne):
    """For N1, omit missing markers only when at least two real values remain."""
    usable = [v for v in ne if v not in MISSING_MARKERS]
    return usable if len(usable) >= 2 else ne


V10_RULES = frozenset({"D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"})


def _rule_enabled(rules, name):
    return rules is None or name in rules


def _date_base_without_weekday(v, rules):
    return bool(
        _is_month_day(v)
        or (_rule_enabled(rules, "D5") and _is_era_date(v))
        or any(r.match(v) for r in DATE_RES)
        or DATETIME_RE.match(v)
        or any(r.match(v) for r in DATE_EXTRA)
        or is_year_range(v)
        or any(r.match(v) for r in MONTH_FULL)
        or (_rule_enabled(rules, "D4") and _is_quarter(v))
    )


def _weekday_date(v, rules):
    m = _WEEKDAY_SUFFIX.match(v)
    if not m:
        return False
    base = m.group("base").rstrip(_SC)
    tail = m.group("tail").strip(_SC)
    if not base or (tail and not _JP_TIME_RANGE.match(tail)):
        return False
    return _date_base_without_weekday(base, rules)


def _is_date_month_part(v):
    return v.endswith("分") and any(r.fullmatch(v[:-1]) for r in _DATE_MONTH_PART)


def _is_unix_timestamp(v):
    if not _UNIX_TS.fullmatch(v):
        return False
    number = float(v)
    return 946684800 <= number <= 4102444800 or 946684800000 <= number <= 4102444800000


def _strong_date_atom(v, rules):
    return bool(
        (_rule_enabled(rules, "D1") and _weekday_date(v, rules))
        or any(r.match(v) for r in DATE_RES)
        or DATETIME_RE.match(v)
        or TIME_RE.match(v)
        or (_rule_enabled(rules, "D3") and _JP_TIME.match(v))
        or (_rule_enabled(rules, "D5") and _is_era_date(v))
        or any(r.match(v) for r in DATE_EXTRA)
        or is_year_range(v)
        or any(r.match(v) for r in MONTH_FULL)
        or (_rule_enabled(rules, "D4") and _is_quarter(v))
        or (_rule_enabled(rules, "D9") and _is_date_month_part(v))
    )


def _is_date_period(v, rules):
    for m in _DATE_PERIOD_SEP.finditer(v):
        left, right = v[:m.start()].strip(_SC), v[m.end():].strip(_SC)
        if left and right and _strong_date_atom(left, rules) and _strong_date_atom(right, rules):
            return True
    if _YEAR_MONTH_PERIOD.fullmatch(v):
        left, right = v.split("-", 1)
        return _strong_date_atom(left, rules) and _strong_date_atom(right, rules)
    return False



def is_year_range(v):
    """年度の範囲（2012/13・2023-24・1999/00・2012/2013）。後の年が前の年の次（2 桁）か、0〜30 年先（4 桁）のときだけ。2020-99 は日付にしない。"""
    m = _FY_RANGE.match(v)
    if not m:
        return False
    a, b = m.group(1), m.group(2)
    if len(b) == 4:
        return 0 <= int(b) - int(a) <= 30
    return (int(b) - int(a[2:])) % 100 == 1


_CUR = "¥\\\\$£€₩₹」"   # NFKC 後の通貨記号（￥→¥、￡→£、半角の ｣ →「」」）
_CODE = r"(?:usd|aud|cad|eur|gbp|jpy|cny|krw|chf|nzd|hkd|sgd|rs|rm|r)"
_UNIT = (r"(?:kg|g|t|km|m|cm|mm|l|ml|pcs|pc|ea|units?|items?|years?|yrs?|months?|days?|hours?|hrs?|people|persons?"
         r"|件|個|人|台|回|年|月|日|時間|歳|才|本|枚|冊|箱|社|店|軒|世帯|名)")
_NUM_CORE = (r"(?:[0-9]{1,3}(?:,[0-9]{3})+(?:\.[0-9]+)?"           # 1,234,567  1,234.50
             r"|[0-9]{1,2}(?:,[0-9]{2})*,[0-9]{3}(?:\.[0-9]+)?"       # 12,34,567（インドの区切り）
             r"|[0-9]{1,3}(?:\.[0-9]{3})+(?:,[0-9]+)?"                # 1.234.567  1.234,56（ヨーロッパ）
             r"|[0-9]{1,3}(?: [0-9]{3})+(?:[.,][0-9]+)?"              # 1 234 567  1 234,56（空白の区切り）
             r"|[0-9]+(?:[.,][0-9]+)?)")                              # 1234  12.5  12,5

_UNIT_EXTRA = r"(?:分|秒|m2|m3|坪|畳|部|点|品|戸|棟|室|床|number|numbers|no)"
_UNIT_V10 = r"(?:" + _UNIT + r"|" + _UNIT_EXTRA + r")"
_PERIOD_UNIT = r"(?:か月|" + _UNIT_V10 + r")"
_PER_UNIT = r"(?:円|" + _UNIT_V10 + r")/[0-9]*" + _PERIOD_UNIT
_CURRENCY_WORD = r"(?:yen|dollars|euros|pounds|ドル|ユーロ|円)"
_CURRENCY_SUFFIX = r"(?:" + _CODE + r"|" + _CURRENCY_WORD + r"|[" + _CUR + r"])"
_NUM_SUFFIX_V91 = r"(?:円/[^0-9" + _SC + r"]{1,4}|" + _UNIT + r"/[^0-9" + _SC + r"]{1,4}|円|％|%|" + _UNIT + r")"
_MAG_JP = r"(?:千万|百万|千|万|億|兆)"
_MAG_EN = r"(?:million|billion|thousand|trillion|bn|mn|k)"
_MAG_CURRENCY_UNIT = r"(?:円|％|%|" + _UNIT_V10 + r"|" + _CURRENCY_SUFFIX + r")"
_MAG_SUFFIX = r"(?:" + _MAG_JP + r"(?:" + _NUM_CORE + _MAG_JP + r")?(?:" + _MAG_CURRENCY_UNIT + r")?|" + _MAG_EN + r"(?:" + _MAG_CURRENCY_UNIT + r")?)"
_RATE_SUFFIX = r"(?:％ポイント|パーセント|ポイント|bps|ppm|‰|pt|bp|割|倍)"
_NUM_SUFFIX = r"(?:円/[^0-9" + _SC + r"]{1,4}|" + _UNIT_V10 + r"/[^0-9" + _SC + r"]{1,4}|" + _PER_UNIT + r"|" + _MAG_SUFFIX + r"|" + _RATE_SUFFIX + r"|%ポイント|円|％|%|" + _UNIT_V10 + r"|" + _CURRENCY_SUFFIX + r")"
_NUM_PREFIX = r"^[+\-−▲△]?\(?" + _S + r"*(?:" + _CODE + _S + r"?)?[" + _CUR + r"]?" + _S + r"*[+\-−]?" + _NUM_CORE
NUM_LOOSE_V91 = re.compile(r"^[+\-−▲△]?\(?" + _S + r"*(?:" + _CODE + _S + r"?)?[" + _CUR + r"]?" + _S + r"*[+\-−]?" + _NUM_CORE + _S + r"*(?:円|％|%|" + _UNIT + r"|円/[^0-9" + _SC + r"]{1,4}|" + _UNIT + r"/[^0-9" + _SC + r"]{1,4})?\.?\)?$")
NUM_LOOSE_N2 = re.compile(_NUM_PREFIX + _S + r"*(?:" + _CURRENCY_SUFFIX + r")\.?\)?$")
NUM_LOOSE_N8 = re.compile(_NUM_PREFIX + _S + r"*(?:" + _UNIT_EXTRA + r"|" + _PER_UNIT + r")\.?\)?$")
_N3_PREFIX_ITEM = r"(?:>=|<=|>|<|≥|≤|約|およそ|概ね|≒|≈|~|税込|税抜|税別)" + _S + r"*"
_N3_PREFIX = r"(?:" + _N3_PREFIX_ITEM + r")?"
_N3_SUFFIX = r"(?:以上|以下|未満|超|程度|前後|強|弱|\(税込\)|\(税抜\)|税込|\*|※|†|\+)"
NUM_LOOSE_N3 = re.compile(r"^(?:" + _N3_PREFIX_ITEM + _NUM_PREFIX[1:] + _S + r"*(?:" + _NUM_SUFFIX_V91 + r")?" + _S + r"*(?:" + _N3_SUFFIX + r")?|" + _NUM_PREFIX[1:] + _S + r"*(?:" + _NUM_SUFFIX_V91 + r")?" + _S + r"*" + _N3_SUFFIX + r")\.?\)?$")
NUM_LOOSE_N4 = re.compile(_NUM_PREFIX + _S + r"*(?:" + _MAG_SUFFIX + r")\.?\)?$")
_CURRENCY_PREFIX = r"(?:[" + _CUR + r"]|" + _CODE + r")"
NUM_LOOSE_N4_M = re.compile(r"^" + _CURRENCY_PREFIX + _S + r"*[+\-−]?" + _NUM_CORE + r"m$")
NUM_LOOSE_N5 = re.compile(r"^[+\-]?[0-9]+(?:\.[0-9]+)?e[+\-]?[0-9]+$")
NUM_LOOSE_N6 = re.compile(_NUM_PREFIX + _S + r"*(?:" + _NUM_SUFFIX_V91 + r")?[-−]\)?$")
NUM_LOOSE_N7 = re.compile(_NUM_PREFIX + _S + r"*(?:" + _RATE_SUFFIX + r"|%ポイント)$")
NUM_LOOSE_N3N4 = re.compile(r"^(?:" + _N3_PREFIX_ITEM + _NUM_PREFIX[1:] + _S + r"*" + _MAG_SUFFIX + _S + r"*(?:" + _N3_SUFFIX + r")?|" + _NUM_PREFIX[1:] + _S + r"*" + _MAG_SUFFIX + _S + r"*" + _N3_SUFFIX + r")\.?\)?$")
_NUM_LOOSE_MAIN = re.compile(r"^" + _N3_PREFIX + _NUM_PREFIX[1:] + _S + r"*(?:" + _NUM_SUFFIX + r")?" + _S + r"*(?:[-−])?" + _S + r"*(?:" + _N3_SUFFIX + r")?\.?\)?$")
NUM_LOOSE = re.compile(r"(?:" + _NUM_LOOSE_MAIN.pattern + r"|" + NUM_LOOSE_N5.pattern + r")")


def _strip(v):
    return _STRIP_RE.sub("", v)


def _text(v):
    return "" if v is None else str(v)


def _clean(values):
    """NFKC・前後の空白なし・小文字にして、空を除く。長い値は 64 文字（コードポイント）までで判断する（正規表現の時間を抑える）。"""
    vals = [_strip(unicodedata.normalize("NFKC", _text(v))).lower()[:64] for v in values]
    return [v for v in vals if v]



def is_date_value(v, strong_only=False, _enabled_rules=None):
    """1 つの値（NFKC・小文字・前後の空白なし）が日付・時刻・年度などに読めるか。"""
    if _rule_enabled(_enabled_rules, "D1") and _weekday_date(v, _enabled_rules):
        return True
    if any(r.match(v) for r in DATE_RES) or DATETIME_RE.match(v) or TIME_RE.match(v):
        return True
    if _rule_enabled(_enabled_rules, "D3") and _JP_TIME.match(v):
        return True
    if _rule_enabled(_enabled_rules, "D5") and _is_era_date(v):
        return True
    if any(r.match(v) for r in DATE_EXTRA) or is_year_range(v) or any(r.match(v) for r in MONTH_FULL):
        return True
    if _rule_enabled(_enabled_rules, "D4") and _is_quarter(v):
        return True
    if _rule_enabled(_enabled_rules, "D7") and _is_date_period(v, _enabled_rules):
        return True
    if _rule_enabled(_enabled_rules, "D9") and _is_date_month_part(v):
        return True
    return False if strong_only else bool(YEAR_ONLY.match(v))


def date_shares(values, _enabled_rules=None):
    """(年だけを除いた日付の値の割合, 年だけの値の割合)。N1 markers are ignored with >=2 usable values."""
    ne = _clean(values)
    if _rule_enabled(_enabled_rules, "N1"):
        ne = _share_values(ne)
    if not ne:
        return 0.0, 0.0
    month_only = [v for v in ne if _MONTH_ONLY.match(v)] if _rule_enabled(_enabled_rules, "D6") else []
    quarter_only = [v for v in ne if _AMBIGUOUS_QUARTER.match(v)] if _rule_enabled(_enabled_rules, "D4") else []
    month_days = [v for v in ne if _is_month_day(v)] if _rule_enabled(_enabled_rules, "D2") else []
    month_column = bool(month_only) and len(month_only) / len(ne) >= 0.8 and len(set(month_only)) >= 2
    quarter_column = bool(quarter_only) and len(quarter_only) / len(ne) >= 0.8
    month_day_column = bool(month_days) and len(month_days) / len(ne) >= 0.8 and any(_month_day_ge_13(v) for v in month_days)
    strong = sum(
        is_date_value(v, True, _enabled_rules)
        or (month_column and bool(_MONTH_ONLY.match(v)))
        or (quarter_column and bool(_AMBIGUOUS_QUARTER.match(v)))
        or (month_day_column and _is_month_day(v))
        for v in ne
    ) / len(ne)
    era_year_column = _rule_enabled(_enabled_rules, "D5") and all(_is_era_year(v) for v in ne)
    unix_timestamp_column = _rule_enabled(_enabled_rules, "D8") and all(_is_unix_timestamp(v) for v in ne)
    year = 1.0 if era_year_column or unix_timestamp_column else sum(bool(YEAR_ONLY.match(v)) for v in ne) / len(ne)
    return strong, year


def _num_loose_match(v, _enabled_rules=None):
    if _enabled_rules is None:
        return bool(NUM_LOOSE.match(v))
    return bool(
        NUM_LOOSE_V91.match(v)
        or (_rule_enabled(_enabled_rules, "N2") and NUM_LOOSE_N2.match(v))
        or (_rule_enabled(_enabled_rules, "N8") and NUM_LOOSE_N8.match(v))
        or (_rule_enabled(_enabled_rules, "N3") and NUM_LOOSE_N3.match(v))
        or (_rule_enabled(_enabled_rules, "N4") and (NUM_LOOSE_N4.match(v) or NUM_LOOSE_N4_M.match(v)))
        or (_rule_enabled(_enabled_rules, "N3") and _rule_enabled(_enabled_rules, "N4") and NUM_LOOSE_N3N4.match(v))
        or (_rule_enabled(_enabled_rules, "N5") and NUM_LOOSE_N5.match(v))
        or (_rule_enabled(_enabled_rules, "N6") and NUM_LOOSE_N6.match(v))
        or (_rule_enabled(_enabled_rules, "N7") and NUM_LOOSE_N7.match(v))
    )


def num_loose_share(values, _enabled_rules=None):
    ne = _clean(values)
    if _rule_enabled(_enabled_rules, "N1"):
        ne = _share_values(ne)
    return sum(_num_loose_match(v, _enabled_rules) for v in ne) / len(ne) if ne else 0.0


def bad_ymd8(values):
    """8桁の数字が多いのに、年月日（19xx/20xx・1〜12月・1〜31日）として読めないものが半分以上"""
    v8 = [_strip(_text(v)) for v in values if re.fullmatch(r"[0-9]{8}", _strip(_text(v)))]
    ne = [v for v in values if _strip(_text(v))]
    if not ne or len(v8) < len(ne) / 2:
        return False
    ok = sum(v[:2] in ("19", "20") and 1 <= int(v[4:6]) <= 12 and 1 <= int(v[6:]) <= 31 for v in v8)
    return ok < len(v8) / 2


def guard_with_reason(pred, probs_sorted, values, _enabled_rules=None):
    """Return (final label, reason code); reason is None when the label is retained."""
    if pred == "other":
        return "unknown", "other_class"
    s = dict(zip(STAT_NAMES, value_stats(values))) if values else None
    has = s is not None and s["empty"] < 0.999
    if has:
        if pred == "date":
            strong, year = date_shares(values, _enabled_rules)
            old = s["date"] + s["datetime"]
            top = probs_sorted[0][1] if probs_sorted else 0.0
            if not (max(old, strong) >= 0.5 or (max(old, strong) + year >= 0.5 and top >= YEAR_CONFIDENCE)):
                return "unknown", "date_value_evidence_low"
            if bad_ymd8(values):
                return "unknown", "date_invalid_8digit"
        loose = num_loose_share(values, _enabled_rules) if pred in ("amount", "quantity", "rate") else 0.0
        if pred in ("amount", "quantity", "rate") and loose < 0.5:
            return "unknown", "numeric_values_not_parseable"
    if len(probs_sorted) > 1:
        (a, pa), (b, pb) = probs_sorted[0], probs_sorted[1]
        if a in NUMERIC and b in NUMERIC and pa - pb < 0.25:
            return "unknown", "numeric_top2_too_close"
    return pred, None


def guard(pred, probs_sorted, values):
    """Backward-compatible label-only wrapper."""
    return guard_with_reason(pred, probs_sorted, values)[0]
