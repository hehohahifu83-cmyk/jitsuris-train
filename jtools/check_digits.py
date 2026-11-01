"""道具 2：番号の検査数字と形（IMPROVEMENT_PLAN 9.5「番号の検査数字」、2026-11-01 Claude）。

値 1 つが、決まった番号の体系に合うかを見る。AI は使わない。外と通信しない。JS 版 check_digits.mjs と同じ結果にする。
検査数字で確かめるもの（偶然に合う割合が低い）：
  corp_jp   法人番号（13 桁。先頭が検査数字。国税庁「法人番号の指定」：9 −（Σ Pn×Qn mod 9）、Qn は下の桁から奇数番目 1・偶数番目 2）
  invoice_jp インボイスの登録番号（T＋法人番号の 13 桁）
  gtin      JAN・EAN-8・EAN-13・UPC-A・GTIN-14（mod 10、重み 3・1）
  isbn      ISBN-10（mod 11）・ISBN-13（978・979 で始まる GTIN）
  iban      IBAN（国の 2 文字＋2 桁＋口座。mod 97 ＝ 1）
  luhn16    Luhn の 16 桁（カードの番号の形。個人の情報の疑いの印として使う）
形だけで見るもの（偶然に合いやすいので、列名と合わせて使う）：
  postcode_jp 123-4567・〒付き、postcode_uk SW1A 1AA、postcode_ca K1A 0B1、postcode_us 12345-6789（ZIP+4 だけ）、
  lgcode_jp 地方公共団体コード（6 桁。末尾が検査数字：11 − (Σ 各桁×(6,5,4,3,2) mod 11) の下 1 桁）
返り値：check(value) → 当たった体系の名前の並び（決まった順）。column_summary(values) → 体系ごとの当たった数。
"""
from __future__ import annotations

import re
import unicodedata

SCHEMES = ("corp_jp", "invoice_jp", "gtin", "isbn", "iban", "luhn16", "lgcode_jp", "postcode_jp", "postcode_uk", "postcode_ca", "postcode_us")


def _c(v) -> str:
    return unicodedata.normalize("NFKC", str(v if v is not None else "")).strip()


def corp_jp(s: str) -> bool:
    if not re.fullmatch(r"[0-9]{13}", s):
        return False
    body = s[1:]
    total = sum(int(ch) * (1 if n % 2 == 1 else 2) for n, ch in enumerate(reversed(body), 1))
    return int(s[0]) == 9 - total % 9


def invoice_jp(s: str) -> bool:
    t = s.replace("-", "").replace(" ", "")
    return bool(re.fullmatch(r"[Tt][0-9]{13}", t)) and corp_jp(t[1:])


def _gtin_ok(d: str) -> bool:
    total = sum(int(ch) * (3 if i % 2 == 0 else 1) for i, ch in enumerate(reversed(d[:-1])))
    return (10 - total % 10) % 10 == int(d[-1])


def gtin(s: str) -> bool:
    t = s.replace(" ", "")   # 「-」入りは日付・電話などと紛れるので見ない
    if not re.fullmatch(r"[0-9]{8}|[0-9]{12,14}", t) or set(t) == {"0"}:
        return False
    return _gtin_ok(t)


def isbn(s: str) -> bool:
    t = re.sub(r"^isbn[:\s-]*", "", s, flags=re.I).replace("-", "").replace(" ", "")
    if re.fullmatch(r"97[89][0-9]{10}", t):
        return _gtin_ok(t)
    if re.fullmatch(r"[0-9]{9}[0-9Xx]", t):
        total = sum((10 - i) * (10 if ch in "Xx" else int(ch)) for i, ch in enumerate(t))
        return total % 11 == 0 and set(t) != {"0"}
    return False


def iban(s: str) -> bool:
    t = s.replace(" ", "").upper()
    if not re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}", t):
        return False
    r = t[4:] + t[:4]
    num = "".join(str(int(ch, 36)) for ch in r)
    rem = 0
    for i in range(0, len(num), 9):
        rem = int(str(rem) + num[i:i + 9]) % 97
    return rem == 1


def luhn16(s: str) -> bool:
    t = s.replace(" ", "").replace("-", "")
    if not re.fullmatch(r"[0-9]{16}", t) or len(set(t)) == 1:
        return False
    total = 0
    for i, ch in enumerate(reversed(t)):
        d = int(ch)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def lgcode_jp(s: str) -> bool:
    if not re.fullmatch(r"[0-9]{6}", s) or not (1 <= int(s[:2]) <= 47):
        return False
    total = sum(int(ch) * w for ch, w in zip(s[:5], (6, 5, 4, 3, 2)))
    return (11 - total % 11) % 10 == int(s[5])


def postcode_jp(s: str) -> bool:
    return bool(re.fullmatch(r"〒?\s?[0-9]{3}-[0-9]{4}", s))


def postcode_uk(s: str) -> bool:
    return bool(re.fullmatch(r"(GIR 0AA|[A-PR-UWYZ][A-HK-Y]?[0-9][0-9A-HJKMNPR-Y]? ?[0-9][ABD-HJLNP-UW-Z]{2})", s.upper()))


def postcode_ca(s: str) -> bool:
    return bool(re.fullmatch(r"[ABCEGHJ-NPRSTVXY][0-9][ABCEGHJ-NPRSTV-Z] ?[0-9][ABCEGHJ-NPRSTV-Z][0-9]", s.upper()))


def postcode_us(s: str) -> bool:
    return bool(re.fullmatch(r"[0-9]{5}-[0-9]{4}", s))   # 5 桁だけの形は普通の数と区別できないので見ない（列名で見る）


_FN = {"corp_jp": corp_jp, "invoice_jp": invoice_jp, "gtin": gtin, "isbn": isbn, "iban": iban, "luhn16": luhn16,
       "lgcode_jp": lgcode_jp, "postcode_jp": postcode_jp, "postcode_uk": postcode_uk, "postcode_ca": postcode_ca, "postcode_us": postcode_us}


def check(value) -> list:
    s = _c(value)
    if not s:
        return []
    return [k for k in SCHEMES if _FN[k](s)]


def column_summary(values) -> dict:
    """{"n": 空でない値の種類の数, 体系: 当たった種類の数}。同じ値は 1 回だけ数える（同じ値の並ぶ列が偶然 100% にならないように）。
    1 つも当たらない体系は書かない（整数。割合は呼ぶ側で n と比べる）。"""
    vals = sorted({_c(v) for v in values if _c(v)})
    out = {"n": len(vals)}
    for k in SCHEMES:
        hit = sum(1 for v in vals if _FN[k](v))
        if hit:
            out[k] = hit
    return out
