"""直し I の候補（2026-11-01 Claude。直し H を見送ったあと、ほかの誤りの調べ（オーナー「2番」）。**製品のコードは変えない**）。

  I1 金額の小数の桁の規則（recheck.py の amount_precision）が、千の区切りのカンマを小数点と読み違える不具合を直す。
     「3,205,468」「£2,000,000」「｣199,843,951」を最後の「,」で切って「468」を小数 3 桁とみなし、金額を不明に下げていた。
     I1：空でない値が全部「通貨の記号（任意）＋千の区切りの数（小数は 2 桁まで）」の形なら、amount_precision で下げない。
     使い済みの陣（決める陣・確かめる陣）で 6 列・3 本で 18 出力、全部が本体の当たりだった（research/h_why/columns.jsonl）。
使い方：with use(fixes): … の中だけ recheck.check_assert を差し替える。
"""
import contextlib
import re
import unicodedata

import recheck as R

_THOUSANDS = re.compile(r"[-−△▲]?\s*(?:[£$€¥｣」]|R\$|US\$)?\s*\d{1,3}(?:,\d{3})+(?:\.\d{1,2})?\s*(?:円)?")
_orig = R.check_assert


def thousands_only(values) -> bool:
    vals = [unicodedata.normalize("NFKC", str(v)).strip() for v in values]
    vals = [v for v in vals if v and v.lower() not in ("na", "nan", "-", "n/a")]
    nums = [v for v in vals if re.search(r"\d", v)]
    return bool(nums) and all(_THOUSANDS.fullmatch(v) for v in nums)


def _i1_check_assert(pred, top3, values, header, unit="", t_low=0.0, siblings=None):
    lab, reason = _orig(pred, top3, values, header, unit, t_low, siblings)
    if reason == "amount_precision" and thousands_only(values):
        # 下げる理由が読み違いだけなら、次の規則（確率の低さ）だけを見る
        p1 = top3[0]["probability"] if top3 else 1.0
        if p1 < t_low and pred not in R.cue_types(header, unit):
            return "unknown", "low_confidence_no_cue"
        return pred, None
    return lab, reason


@contextlib.contextmanager
def use(fixes):
    old = R.check_assert
    if "I1" in set(fixes):
        R.check_assert = _i1_check_assert
    try:
        yield
    finally:
        R.check_assert = old
