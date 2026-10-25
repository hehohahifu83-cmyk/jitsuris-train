"""recheck v1 の規則を 1 つずつ外したら製品の形（見張り → recheck → 検査役 v2 → rho 0.7）がどう変わるか（2026-10-25 Claude。開発用：b013・b014、C1 種子 1）。

強化案 V1（research/strengthen-plan-2026-10-25.md）。ここで決めた変更は C2 の線を b015 で決め直すときに入れ、b015 で確かめる。封印セット #3 の C1 の凍結構成は変えない。
使い方：python research/recheck_review.py > 結果
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import recheck  # noqa: E402
from research.merge import merge_eval  # noqa: E402

ORIG = recheck.check_assert
CONFIGS = [(), ("period_header_no_unit",), ("low_confidence_no_cue",), ("amount_without_cue",),
           ("period_header_no_unit", "low_confidence_no_cue")]


def patched(off):
    def f(*a, **k):
        lab, why = ORIG(*a, **k)
        if why in off:
            return a[0], None
        return lab, why
    return f


for off in CONFIGS:
    recheck.check_assert = patched(set(off))
    print("外す:", "・".join(off) or "（なし＝今の形）", flush=True)
    merge_eval.main(["score", "--tags", "c1", "--out", os.devnull])
recheck.check_assert = ORIG
