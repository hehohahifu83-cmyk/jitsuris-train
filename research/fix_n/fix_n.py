"""直し N の候補（2026-11-14 Claude。相談では仮に「P」と呼んだ。製品のコードは変えない。評価の段だけ差し替える）。
原因：G3 の調べ（research/g3/amount_unknown.md・Codex の点検 research/g3/amount_unknown_review_codex/）。
recheck.py の amount_precision（金額なのに小数が 3 桁以上）が、次の 2 つを細かい小数と読み違えて金額を不明に下げる。
  (a) 千の区切り：「$74,374」「3,205,468」を最後の「,」で切り、「374」を小数 3 桁とみなす（過去の直し I1 と同じ不具合）。
  (b) 表計算の小数の誤差：「159417.82999999999」（本来 159417.83）を小数 17 桁とみなす。
直し N：amount_precision で下げたときだけ、値ごとに「本当に細かい小数か」を次の厳しい決まりで見直し、1 つも無ければ次の規則（確率の低さ）だけを見る。
  - 千の区切り：英語式の厳密な形だけ（通貨の記号は任意、1〜3 桁＋「,3 桁」の繰り返し、小数は「.」の後ろ）。小数カンマ・欧州式・崩れた区切りは今の決まりのまま。
    区切りの後ろの小数は、今と同じく 0 を除いて 3 桁以上なら細かい小数。
  - 表計算の誤差：「数字.数字」で小数 10 桁以上の値だけ。Decimal で小数 2 桁に丸めた値との差が 1e-8 以下（値の大きさで広げない絶対の上限）なら 2 桁とみなす。
    それ以外（差が大きい・桁が少ない）は今の決まりのまま。
  - 1 つでも本当に細かい小数が残れば、止めたまま。通貨の記号があるだけでは通さない。元の値は書き換えない。
ほかの止め（amount_without_cue・手がかりのぶつかり・期間の列名・検査役・rho・辞書・末尾の通貨確認）は変えない。
使い方：with use(): の中だけ recheck.check_assert を包む（製品の形 PRODUCT は check_assert を置き換えないので、外から包めば効く。
        G2・I1 の直しを入れた形とは組み合わせない。use() は入るときにそれを確かめる）。
"""
import re
from decimal import Decimal, InvalidOperation

import recheck as R

_THOUSANDS = re.compile(r"[-−]?\s*(?:[$€£¥]|R\$|US\$|C\$|CA\$)?\s*\d{1,3}(?:,\d{3})+(?:\.(\d+))?")
_FLOAT_NOISE = re.compile(r"-?\d+\.(\d{10,})")
_NOISE_MAX = Decimal("1e-8")


def _precise_now(v):
    """今の amount_precision の値ごとの判定（recheck.py:185 と同じ）。"""
    return bool(re.search(r"[.,]\d*[1-9]\d*$", v)) and len(re.split(r"[.,]", v)[-1].rstrip("0")) >= 3


def truly_precise(v):
    """直し N の値ごとの判定：本当に 3 桁以上の小数を持つか。"""
    m = _THOUSANDS.fullmatch(v)
    if m:
        return len((m.group(1) or "").rstrip("0")) >= 3
    m = _FLOAT_NOISE.fullmatch(v)
    if m:
        try:
            d = Decimal(v)
        except InvalidOperation:
            return _precise_now(v)
        if abs(d - d.quantize(Decimal("0.01"))) <= _NOISE_MAX:
            return False
    return _precise_now(v)


_orig = R.check_assert


def n_check_assert(pred, top3, values, header, unit="", t_low=0.0, siblings=None):
    lab, reason = _orig(pred, top3, values, header, unit, t_low, siblings)
    if reason != "amount_precision":
        return lab, reason
    vals = [R._norm(v) for v in values if R._norm(v) not in R._EMPTY]
    if any(truly_precise(v) for v in vals):
        return lab, reason
    p1 = top3[0]["probability"] if top3 else 1.0
    cues = {"rate"} if R.pct_values(values) else R.cue_types(header, unit)
    if p1 < t_low and pred not in cues:
        return "unknown", "low_confidence_no_cue"
    return pred, None


class use:
    def __enter__(self):
        if R.check_assert is not _orig:
            raise RuntimeError("recheck.check_assert がもう差し替えられている（G2・I1 などと組み合わせない）")
        R.check_assert = n_check_assert

    def __exit__(self, *a):
        R.check_assert = _orig
