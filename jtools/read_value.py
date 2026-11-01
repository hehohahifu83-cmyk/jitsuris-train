"""道具 1：値の読み取り（IMPROVEMENT_PLAN 9.5「値の読み取り」、2026-11-01 Claude）。

セル 1 つの文字列を、決まった規則で読む。AI は使わない。外と通信しない。JS 版 read_value.mjs と同じ結果にする（jtools/fixtures.json で試験）。
読むもの：全角（NFKC）、千の区切り、負の印（- △ ▲ (…)）、漢数字（千二百・3万5千・壱弐参）、通貨の記号と語（¥ $ € £ 円 ドル ユーロ CHF …）、
単位（% ‰ 千円 百万円 万円 kg m² …）、和暦（令和7年4月1日・R7.4.1・H18. 1.26・平成30年度）、西暦の日付（2024-04-01・2024/4/1・1.4.2024・2024年4月1日）、
年月（2024-04・2024年4月）、時刻（12:30・12:30:05）。

返り値（dict）：
  {"kind": "empty" | "number" | "date" | "time" | "text", ...}
  number：{"kind": "number", "value": 書いてある数（倍率は掛けない。1,234千円 → 1234、scale 1000）, "neg": 負か, "sep": 千の区切りがあったか, "decimals": 小数の桁, "currency": 通貨（ISO の 3 文字か ""）,
           "unit": 単位（"" ・ "%" ・ "千円" など）, "scale": 単位の倍率（千円なら 1000）, "kanji": 漢数字だったか}
  date：{"kind": "date", "y": 年, "m": 月（0 なら無し）, "d": 日（0 なら無し）, "era": 和暦の元号（"" なら西暦）, "fiscal": 年度か}
  time：{"kind": "time", "h": 時, "mi": 分, "s": 秒}
日付の判定は値の形だけで見る（8 桁の 20240401 や Excel の日付の番号は数として返す。列名と合わせて決めるのは呼ぶ側）。
"""
from __future__ import annotations

import re
import unicodedata

ERAS = {"明治": 1867, "大正": 1911, "昭和": 1925, "平成": 1988, "令和": 2018,
        "M": 1867, "T": 1911, "S": 1925, "H": 1988, "R": 2018}
ERA_NAME = {"M": "明治", "T": "大正", "S": "昭和", "H": "平成", "R": "令和"}

# 通貨：前に付く記号・後ろに付く語（長いものを先に見る）
CUR_PREFIX = [("US$", "USD"), ("C$", "CAD"), ("A$", "AUD"), ("NZ$", "NZD"), ("HK$", "HKD"), ("CHF", "CHF"), ("EUR", "EUR"), ("USD", "USD"),
              ("GBP", "GBP"), ("JPY", "JPY"), ("CAD", "CAD"), ("AUD", "AUD"), ("$", "USD"), ("€", "EUR"), ("£", "GBP"), ("¥", "JPY"), ("₩", "KRW"),
              ("Fr.", "CHF"), ("R$", "BRL")]
CUR_SUFFIX = [("百万円", "JPY", 1000000), ("千万円", "JPY", 10000000), ("億円", "JPY", 100000000), ("万円", "JPY", 10000), ("千円", "JPY", 1000),
              ("円", "JPY", 1), ("ドル", "USD", 1), ("ユーロ", "EUR", 1), ("ポンド", "GBP", 1), ("EUR", "EUR", 1), ("USD", "USD", 1), ("CHF", "CHF", 1),
              ("GBP", "GBP", 1), ("JPY", "JPY", 1), ("CAD", "CAD", 1), ("€", "EUR", 1), ("Fr.", "CHF", 1), ("€", "EUR", 1)]
# 通貨でない単位（倍率つき）
UNIT_SUFFIX = [("%", 1), ("‰", 1), ("pt", 1), ("ポイント", 1), ("百万", 1000000), ("千", 1000), ("万", 10000), ("億", 100000000),
               ("km2", 1), ("km²", 1), ("m2", 1), ("m²", 1), ("m3", 1), ("m³", 1), ("km", 1), ("kg", 1), ("mg", 1), ("ha", 1), ("kWh", 1), ("MWh", 1),
               ("cm", 1), ("mm", 1), ("ml", 1), ("t", 1), ("g", 1), ("m", 1), ("l", 1),
               ("人", 1), ("件", 1), ("個", 1), ("台", 1), ("回", 1), ("戸", 1), ("世帯", 1), ("箇所", 1), ("か所", 1), ("本", 1), ("枚", 1), ("歳", 1),
               ("才", 1), ("日", 1), ("時間", 1), ("分", 1), ("年", 1), ("か月", 1), ("ヶ月", 1)]

KANJI_DIGIT = {"〇": 0, "零": 0, "一": 1, "壱": 1, "二": 2, "弐": 2, "三": 3, "参": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
KANJI_SMALL = {"十": 10, "拾": 10, "百": 100, "千": 1000}
KANJI_BIG = {"万": 10000, "億": 100000000, "兆": 1000000000000}

_NUM = re.compile(r"[0-9]+(\.[0-9]+)?|\.[0-9]+")
_EMPTY = {"", "-", "−", "—", "–", "na", "n/a", "nan", "null", "none", "…", "x", "*", "..", "."}


def clean(s) -> str:
    t = unicodedata.normalize("NFKC", str(s if s is not None else ""))
    t = t.replace("​", "").replace("﻿", "").replace("−", "-").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", t).strip()


def _kanji_number(s: str):
    """漢数字（と数字の混ざり：3万5千）を整数にする。読めなければ None。"""
    if not s or not re.fullmatch(r"[0-9〇零一壱二弐三参四五六七八九十拾百千万億兆]+", s) or re.fullmatch(r"[0-9]+", s):
        return None
    if s in ("〇", "零"):   # 〇 だけは「有」の印として使われることが多い（AED設置＝〇）
        return None
    total, section, digits = 0, 0, ""
    for ch in s:
        if ch in "0123456789" or ch in KANJI_DIGIT:
            digits += ch if ch in "0123456789" else str(KANJI_DIGIT[ch])
        elif ch in KANJI_SMALL:
            section += (int(digits) if digits else 1) * KANJI_SMALL[ch]
            digits = ""
        elif ch in KANJI_BIG:
            section += int(digits) if digits else 0
            if section == 0:
                return None
            total += section * KANJI_BIG[ch]
            section, digits = 0, ""
    section += int(digits) if digits else 0
    return total + section


def _date(t: str):
    m = re.fullmatch(r"(明治|大正|昭和|平成|令和)\s?([0-9]{1,2}|元)\s?年(度)?(?:\s?([0-9]{1,2})\s?月(?:\s?([0-9]{1,2})\s?日)?)?", t)
    if m:
        y = 1 if m.group(2) == "元" else int(m.group(2))
        return _mk(ERAS[m.group(1)] + y, int(m.group(4) or 0), int(m.group(5) or 0), m.group(1), bool(m.group(3)))
    m = re.fullmatch(r"([MTSHR])\s?([0-9]{1,2})\s?[.\-/]\s?([0-9]{1,2})\s?[.\-/]\s?([0-9]{1,2})", t, re.I)
    if m:
        e = m.group(1).upper()
        return _mk(ERAS[e] + int(m.group(2)), int(m.group(3)), int(m.group(4)), ERA_NAME[e], False)
    m = re.fullmatch(r"([0-9]{4})\s?年\s?(度)?(?:\s?([0-9]{1,2})\s?月(?:\s?([0-9]{1,2})\s?日)?)?", t)
    if m:
        return _mk(int(m.group(1)), int(m.group(3) or 0), int(m.group(4) or 0), "", bool(m.group(2)))
    m = re.fullmatch(r"([0-9]{4})([\-/.])([0-9]{1,2})(?:\2([0-9]{1,2}))?(?:[ T]([0-9]{1,2}):([0-9]{2})(?::([0-9]{2})(?:\.[0-9]+)?)?(?:Z|[+\-][0-9]{2}:?[0-9]{2})?)?", t)
    if m:
        return _mk(int(m.group(1)), int(m.group(3)), int(m.group(4) or 0), "", False)
    m = re.fullmatch(r"([0-9]{1,2})\.([0-9]{1,2})\.([0-9]{4})", t)            # 1.4.2024（欧州：日.月.年）
    if m:
        return _mk(int(m.group(3)), int(m.group(2)), int(m.group(1)), "", False)
    m = re.fullmatch(r"([0-9]{1,2})/([0-9]{1,2})/([0-9]{4})(?: [0-9]{1,2}:[0-9]{2}(?::[0-9]{2})?(?: ?[AP]M)?)?", t, re.I)   # 1/28/2008（米：月/日/年。13 以上なら日/月/年）
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        mo, d = (b, a) if a > 12 else (a, b)
        return _mk(int(m.group(3)), mo, d, "", False)
    return None


def _mk(y, m, d, era, fiscal):
    if not (1800 <= y <= 2200) or not (0 <= m <= 12) or not (0 <= d <= 31) or (d and not m):
        return None
    return {"kind": "date", "y": y, "m": m, "d": d, "era": era, "fiscal": fiscal}


def read_value(raw) -> dict:
    t = clean(raw)
    if t.lower() in _EMPTY:
        return {"kind": "empty"}
    d = _date(t)
    if d:
        return d
    m = re.fullmatch(r"([0-9]{1,2}):([0-9]{2})(?::([0-9]{2}))?", t)
    if m and int(m.group(1)) <= 24 and int(m.group(2)) < 60 and int(m.group(3) or 0) < 60:
        return {"kind": "time", "h": int(m.group(1)), "mi": int(m.group(2)), "s": int(m.group(3) or 0)}
    return _number(t) or {"kind": "text"}


def _number(t: str):
    s = t.replace(" ", "")
    neg = False
    if s.startswith("(") and s.endswith(")"):
        neg, s = True, s[1:-1]
    if s[:1] in ("-", "△", "▲"):
        neg, s = True, s[1:]
    elif s[:1] == "+":
        s = s[1:]
    currency, unit, scale = "", "", 1
    for sym, code in CUR_PREFIX:
        if s.startswith(sym) and len(s) > len(sym):
            currency, s = code, s[len(sym):]
            break
    if s[:1] in ("-", "△", "▲") and not neg:   # $-12
        neg, s = True, s[1:]
    for suf, code, sc in CUR_SUFFIX:
        if s.endswith(suf) and len(s) > len(suf):
            if currency and currency != code:
                return None
            currency, s, scale = code, s[: -len(suf)], sc
            unit = suf if sc != 1 else ""
            break
    k = _kanji_number(s)
    if k is not None:
        return {"kind": "number", "value": float(-k if neg else k), "neg": neg, "sep": False, "decimals": 0,
                "currency": currency, "unit": unit, "scale": scale, "kanji": True}
    if not unit:
        for suf, sc in UNIT_SUFFIX:
            if s.endswith(suf) and len(s) > len(suf):
                head = s[: -len(suf)]
                if not re.search(r"[0-9〇零一壱二弐三参四五六七八九十拾百千万億兆]$", head):
                    continue
                unit, s, scale = suf, head, sc
                break
    if s.endswith("-"):   # 1,234-（会計の負）
        neg, s = True, s[:-1]
    k = _kanji_number(s)
    if k is not None:   # 3千（数字＋漢数字の単位は上で単位として取った残り）
        return {"kind": "number", "value": float(-k if neg else k), "neg": neg, "sep": False, "decimals": 0,
                "currency": currency, "unit": unit, "scale": scale, "kanji": True}
    sep = False
    if re.fullmatch(r"[0-9]{1,3}(,[0-9]{3})+(\.[0-9]+)?", s):
        sep, s = True, s.replace(",", "")
    elif re.fullmatch(r"[0-9]{1,3}(\.[0-9]{3})+,[0-9]+", s):        # 1.234,56（独仏）
        sep, s = True, s.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"[0-9]{1,3}('[0-9]{3})+(\.[0-9]+)?", s):      # 1'234.50（スイス）
        sep, s = True, s.replace("'", "")
    elif re.fullmatch(r"[0-9]+,[0-9]{1,2}", s):                      # 12,5（独仏の小数）
        s = s.replace(",", ".")
    if not _NUM.fullmatch(s):
        return None
    dec = len(s.partition(".")[2])
    v = float(s)
    return {"kind": "number", "value": -v if neg else v, "neg": neg, "sep": sep, "decimals": dec,
            "currency": currency, "unit": unit, "scale": scale, "kanji": False}


def column_summary(values) -> dict:
    """列の値をまとめて読んだ数（空でない値の数 n と、種類ごとの数）。割合は呼ぶ側で n と比べる（Python と JS で丸めを揃えるため整数）。"""
    rs = [read_value(v) for v in values]
    ne = [r for r in rs if r["kind"] != "empty"]
    nums = [r for r in ne if r["kind"] == "number"]
    curs = sorted({r["currency"] for r in nums if r["currency"]})
    units = sorted({r["unit"] for r in nums if r["unit"]})
    return {"n": len(ne),
            "number": len(nums),
            "date": sum(1 for r in ne if r["kind"] == "date"),
            "time": sum(1 for r in ne if r["kind"] == "time"),
            "text": sum(1 for r in ne if r["kind"] == "text"),
            "currency": curs[0] if len(curs) == 1 else ("mixed" if curs else ""),
            "unit": units[0] if len(units) == 1 else ("mixed" if units else ""),
            "era": sum(1 for r in ne if r["kind"] == "date" and r["era"]),
            "kanji": sum(1 for r in nums if r["kanji"]),
            "neg": sum(1 for r in nums if r["neg"])}
