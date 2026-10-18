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
"""
import re
import unicodedata

from features import value_stats, STAT_NAMES, DATE_RES, DATETIME_RE, TIME_RE

NUMERIC = {"date", "amount", "quantity", "rate", "id"}
YEAR_CONFIDENCE = 0.9  # 年だけの列を日付と認めるときに要る、答えの確率

_MONTH = r"(?:january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sept|sep|oct|nov|dec)"
YEAR_ONLY = re.compile(r"^(19|20)[0-9]{2}$")
DATE_EXTRA = [re.compile(p) for p in [
    r"^(19|20)[0-9]{2}\s*[/\-–]\s*((19|20)?[0-9]{2})[_*\s]*$",                 # 2012/13  2012/2013  2023-24
    r"^(19|20)[0-9]{2}\s*[/\-]\s*[0-9]{1,2}$",                                  # 2020-07  2020/7
    r"^[0-9]{1,2}\s*[/\-]\s*(19|20)[0-9]{2}$",                                  # 07-2015
    r"^(19|20)[0-9]{2}\s*/\s*[0-9]{1,2}\s*-\s*[0-9]{1,2}\.?$",                  # 1994/4-3.（4月から3月の年度）
    r"^(19|20)[0-9]{2}年(度)?([0-9]{1,2}月)?$",                                  # 2023年  2023年度  2023年4月
    r"^[0-9]{1,2}月([0-9]{1,2}日)?$",                                            # 4月  4月1日
    r"^(令和|平成|昭和|大正)[0-9元]+年",                                            # 平成30年
    r"^[rhs][0-9]{1,2}[./][0-9]{1,2}([./][0-9]{1,2})?$",                        # H30/4/1
    r"^(19|20)[0-9]{2}\s*-?\s*q[1-4]$", r"^q[1-4]\s*-?\s*(19|20)?[0-9]{2}$",    # 2014Q1  Q1 2012
    r"^fy\s*'?(19|20)?[0-9]{2}", r"^h[12]\s*(19|20)[0-9]{2}$",                  # FY2020  H1 2020
    r"^(19|20)[0-9]{2}m[0-9]{2}(d[0-9]{2})?$",                                  # 2020M07D23
    r"^[0-9]{1,2}[/\-][0-9]{1,2}[/\-][0-9]{2,4}([ t][0-9]{1,2}:[0-9]{2}(:[0-9]{2})?\s*(am|pm)?)?$",   # 1/28/2008  1/28/2008 12:00:00 AM
    r"^[0-9]{1,2}\.[0-9]{1,2}\.(19|20)[0-9]{2}$",                               # 31.12.2019
]]
MONTH_RE = re.compile(r"(^|[^a-z])" + _MONTH + r"\.?([^a-z]|$)")                # 05-May-17  31st March  March 2020

_CUR = "¥\\\\$£€₩₹」"   # NFKC 後の通貨記号（￥→¥、￡→£、半角の ｣ →「」」）
_CODE = r"(?:usd|aud|cad|eur|gbp|jpy|cny|krw|chf|nzd|hkd|sgd|rs|rm|r)"
_UNIT = (r"(?:kg|g|t|km|m|cm|mm|l|ml|pcs|pc|ea|units?|items?|years?|yrs?|months?|days?|hours?|hrs?|people|persons?"
         r"|件|個|人|台|回|年|月|日|時間|歳|才|本|枚|冊|箱|社|店|軒|世帯|名)")
NUM_LOOSE = re.compile(r"^[+\-−▲△]?\(?\s*(?:" + _CODE + r"\s?)?[" + _CUR + r"]?\s*[+\-−]?[0-9][0-9,. ]*(?:[.,][0-9]+)?\s*(?:円|％|%|" + _UNIT + r"|円/[^0-9\s]{1,4}|" + _UNIT + r"/[^0-9\s]{1,4})?\.?\)?$")


def _clean(values):
    """NFKC・前後の空白なし・小文字にして、空を除く。長い値は 64 文字までで判断する（正規表現の時間を抑える）。"""
    vals = [unicodedata.normalize("NFKC", str(v or "")).strip().lower()[:64] for v in values]
    return [v for v in vals if v]


def is_date_value(v, strong_only=False):
    """1 つの値（NFKC・小文字・前後の空白なし）が日付・時刻・年度などに読めるか。strong_only なら年だけ（2023）は含めない。"""
    if any(r.match(v) for r in DATE_RES) or DATETIME_RE.match(v) or TIME_RE.match(v):
        return True
    if any(r.match(v) for r in DATE_EXTRA):
        return True
    if MONTH_RE.search(v) and any(ch.isdigit() for ch in v):
        return True
    return False if strong_only else bool(YEAR_ONLY.match(v))


def date_shares(values):
    """(年だけを除いた日付の値の割合, 年だけの値の割合)。"""
    ne = _clean(values)
    if not ne:
        return 0.0, 0.0
    strong = sum(is_date_value(v, True) for v in ne) / len(ne)
    year = sum(bool(YEAR_ONLY.match(v)) for v in ne) / len(ne)
    return strong, year


def num_loose_share(values):
    ne = _clean(values)
    return sum(bool(NUM_LOOSE.match(v)) for v in ne) / len(ne) if ne else 0.0


def bad_ymd8(values):
    """8桁の数字が多いのに、年月日（19xx/20xx・1〜12月・1〜31日）として読めないものが半分以上"""
    v8 = [str(v).strip() for v in values if re.fullmatch(r"[0-9]{8}", str(v).strip())]
    ne = [v for v in values if str(v).strip()]
    if not ne or len(v8) < len(ne) / 2:
        return False
    ok = sum(v[:2] in ("19", "20") and 1 <= int(v[4:6]) <= 12 and 1 <= int(v[6:]) <= 31 for v in v8)
    return ok < len(v8) / 2


def guard(pred, probs_sorted, values):
    """pred：一番の答え。probs_sorted：[(種類, 確率)] の大きい順。values：値の一覧"""
    if pred == "other":  # 15種類のどれにも当たらない列（測定値・座標・URL など）は決めずに人に回す（v6〜）
        return "unknown"
    s = dict(zip(STAT_NAMES, value_stats(values))) if values else None
    has = s is not None and s["empty"] < 0.999
    if has:
        if pred == "date":
            strong, year = date_shares(values)
            old = s["date"] + s["datetime"]
            top = probs_sorted[0][1] if probs_sorted else 0.0
            if not (max(old, strong) >= 0.5 or (max(old, strong) + year >= 0.5 and top >= YEAR_CONFIDENCE)):
                return "unknown"
            if bad_ymd8(values):  # 10160000 のような8桁のコードを日付と取り違えない（v7〜）
                return "unknown"
        loose = num_loose_share(values) if pred in ("amount", "quantity", "rate") else 0.0
        if pred in ("amount", "quantity") and max(s["num"], loose) < 0.5:
            return "unknown"
        if pred == "rate" and max(s["num"] + s["pct"], loose) < 0.5:
            return "unknown"
    # 上位2つがどちらも数字の種類で、差が小さいときは決めない
    if len(probs_sorted) > 1:
        (a, pa), (b, pb) = probs_sorted[0], probs_sorted[1]
        if a in NUMERIC and b in NUMERIC and pa - pb < 0.25:
            return "unknown"
    return pred
