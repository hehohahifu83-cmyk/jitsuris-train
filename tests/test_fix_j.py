"""直し J の候補（research/guard_dates/fix_j.py、2026-11-09 Claude）。"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "research" / "guard_dates"))
import fix_j  # noqa: E402


class FixJTests(unittest.TestCase):
    def test_reads_clear_dates(self):
        for v in ("平23", "令1", "令和 7年11月", "令和 5年平均", "11月4日午前9時ころ", "7月下旬", "毎年1月1日", "2025‐3‐31",
                  "JUNHO 2025", "Jan-Mar 2020", "Jan. / jan. 2013", "26/Oct/2019 18:15", "09NOV17:11:02:00",
                  "9:30-17:00", "令和元年"):
            self.assertTrue(fix_j.j_value(v), v)

    def test_leaves_ambiguous_and_numbers(self):
        for v in ("0300", "0.375", "5", "1996.0", "1876-1943", "4625 8433", "63 917 461", "12.5", "1,234",
                  # Codex の反例（research/guard_dates/fix_j_review_codex.md）
                  "marketing 2020", "maybe 2020", "marketing-marchandise 2020", "99/octopus/2020 99:99",
                  "平0", "昭99", "令和 0年99月", "99月99日午後99時99分", "99NOV17:99:99:99", "31.02.18", "2.8.12",
                  "00:02:37.00", "1.20-2.30", "16:35:00.00", "13.30–16.30", "15.01.18", "25:00-26:00"):  # 「2月30日」は今の見張り（is_date_value）が日付に読む。J の外の問題として別に記録
            self.assertFalse(fix_j.j_value(v), v)

    def test_column_share(self):
        self.assertTrue(fix_j.j_keeps_date(["平23", "昭55", "大5", "?"]))
        self.assertFalse(fix_j.j_keeps_date(["5", "6", "9"]))
        self.assertFalse(fix_j.j_keeps_date(["2.8.12", "2.8.13", "2.8.14", "2.8.15", "2.8.16"]))   # Codex の仮想の Ref 列


if __name__ == "__main__":
    unittest.main()
