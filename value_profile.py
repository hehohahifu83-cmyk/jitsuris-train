"""W3a：列の値の形を短い文にする（IMPROVEMENT_PLAN 9.5「値の統計」、2026-10-21 Claude）。

入力の文に見せる値（先頭 5 つ）だけから、決まった規則で作る。モデルの外の計算なので、ブラウザでも同じ規則を JS で書けば同じ結果になる
（採用されたら JS 版と一致の試験を足す）。ラベル・見出しは使わない。

例：["1,200円", "3,450円", "980円"] → "数値 3/3 整数 桁3〜4 区切り 円"
"""
from __future__ import annotations

import re
import unicodedata

_JUNK = {"", "nan", "none", "null", "n/a", "na", "-", "—", "－"}
_SYMBOLS = ("円", "¥", "$", "€", "£", "%")
_NUM = re.compile(r"\d+(?:\.\d+)?")
_DATE = (
    re.compile(r"\d{4}[-/.年]\d{1,2}([-/.月]\d{1,2}日?)?"),          # 2024-10-21・2024/10・2024年10月21日
    re.compile(r"\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}"),                  # 21/10/2024・10-21-24
    re.compile(r"(令和|平成|昭和|[RHS])\s*\d{1,2}[年./-]"),            # 令和5年・R5.10
    re.compile(r"\d{1,2}月\d{1,2}日"),                                # 10月21日
    re.compile(r"\d{8}"),                                              # 20241021（数値とも数える）
)


def _clean(value):
    return unicodedata.normalize("NFKC", str(value)).strip()


def _number(text):
    """数として読めれば (整数部の桁数, 小数の桁数, 負か, 区切りがあるか, 記号の集合, 先頭が 0 か)。読めなければ None。"""
    s = text.replace(" ", "")
    neg = False
    if s.startswith("(") and s.endswith(")"):
        neg, s = True, s[1:-1]
    if s[:1] in ("-", "△", "▲"):
        neg, s = True, s[1:]
    elif s[:1] == "+":
        s = s[1:]
    syms = set()
    for sym in _SYMBOLS:
        if sym in s:
            syms.add(sym)
            s = s.replace(sym, "")
    sep = "," in s
    s = s.replace(",", "")
    if not _NUM.fullmatch(s):
        return None
    whole, _, frac = s.partition(".")
    return len(whole), len(frac), neg, sep, syms, len(whole) > 1 and whole.startswith("0")


def _kinds(text):
    kinds = []
    if re.search(r"[一-鿿]", text):
        kinds.append("漢")
    if re.search(r"[぀-ヿ]", text):
        kinds.append("かな")
    if re.search(r"[A-Za-z]", text):
        kinds.append("英")
    if re.search(r"\d", text):
        kinds.append("数")
    return kinds


def value_profile(values, limit=5):
    """値の形の短い文。値が無ければ空文字。"""
    vals = [_clean(v) for v in list(values)[:limit]]
    vals = [v for v in vals if v.lower() not in _JUNK]
    n = len(vals)
    if not n:
        return ""
    parts = []
    nums = [x for x in (_number(v) for v in vals) if x is not None]
    dates = sum(1 for v in vals if any(p.fullmatch(v) or p.match(v) for p in _DATE))
    if dates:
        parts.append(f"日付形 {dates}/{n}")
    parts.append(f"数値 {len(nums)}/{n}")
    if nums and len(nums) * 2 >= n:
        dec = max(x[1] for x in nums)
        parts.append(f"小数{dec}桁" if dec else "整数")
        lo, hi = min(x[0] for x in nums), max(x[0] for x in nums)
        parts.append(f"桁{lo}" if lo == hi else f"桁{lo}〜{hi}")
        if any(x[2] for x in nums):
            parts.append("負")
        if any(x[3] for x in nums):
            parts.append("区切り")
        syms = set().union(*(x[4] for x in nums))
        parts += [s for s in _SYMBOLS if s in syms]
        if any(x[5] for x in nums):
            parts.append("先頭0")
        if n >= 3 and len({len(v) for v in vals}) == 1:
            parts.append("長さ一定")
    else:
        lens = [len(v) for v in vals]
        lo, hi = min(lens), max(lens)
        parts.append(f"長さ{lo}" if lo == hi else f"長さ{lo}〜{hi}")
        kinds = []
        for v in vals:
            kinds += [k for k in _kinds(v) if k not in kinds]
        if kinds:
            parts.append("字" + "・".join(kinds))
    if n >= 3 and len(set(vals)) < n:
        parts.append("重複")
    return " ".join(parts)
