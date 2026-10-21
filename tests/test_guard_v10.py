import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import guard as G

HI_DATE = [("date", 0.99), ("org", 0.005)]
HI_AMOUNT = [("amount", 0.99), ("text", 0.005)]


def decide(pred, values):
    return G.guard(pred, [(pred, 0.99), ("text", 0.005)], values)


class GuardV10InitialTests(unittest.TestCase):
    """First v10 slice: missing markers, Japanese times, and abbreviated era dates."""

    def test_n1_missing_markers_do_not_shrink_numeric_denominator(self):
        positive_columns = [
            ["1,234", "-", "n/a", "2,345", "…", "nil", "3,456"],
            ["¥1,000", "--", "n.a.", "2,000", "none", "3,000", ".."],
            ["30 kg", "—", "(x)", "1,200 kg", "nan", "2,000 kg", "*"],
            ["12.5%", "*", "null", "15%", "...", "20%", "x"],
            ["100", "-", "−", "200", "...", "n/a", "n/a", "300"],
        ]
        for values in positive_columns:
            with self.subTest(values=values):
                self.assertEqual(decide("amount", values), "amount")

    def test_n1_falls_back_when_fewer_than_two_numeric_values_remain(self):
        negative_columns = [
            ["1,234", "-", "n/a", "...", "nil"],
            ["100", "—", "na", "none", "(x)"],
            ["-", "−", "–", "—", "―", "ー"],
            ["...", "..", ".", "*", "**", "***"],
            ["x", "n/a", "#n/a", "#div/0!", "#value!"],
        ]
        for values in negative_columns:
            with self.subTest(values=values):
                self.assertEqual(decide("amount", values), "unknown")

    def test_d3_accepts_japanese_times_but_not_durations_or_invalid_times(self):
        positive = ["9時00分", "午後3時", "午前9時30分", "10時", "13時45分30秒"]
        negative = ["3時間", "2時間30分", "25時10分", "10時60分", "時"]
        for value in positive:
            with self.subTest(value=value):
                self.assertTrue(G.is_date_value(G._clean([value])[0]))
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.is_date_value(G._clean([value])[0]))

    def test_d5_accepts_valid_abbreviated_era_dates_and_rejects_invalid_ones(self):
        positive = ["h28. 4. 1", "r 5.10.28", "s.46/03/01", "s62. 8.30", "r6.3.5"]
        negative = ["r35", "h32", "s65", "r0", "x28", "h28.13.1", "s.46/13/01", "r06a"]
        for value in positive:
            with self.subTest(value=value):
                self.assertTrue(G.is_date_value(G._clean([value])[0]))
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.is_date_value(G._clean([value])[0]))

    def test_v91_accepted_date_and_number_shapes_remain_accepted(self):
        old_dates = ["2024-01-05", "2024年1月5日", "令和6年5月1日", "1/28/2008", "2012/13", "FY2020", "05-May-17"]
        old_numbers = ["£1,234.50", "¥1,000", "1.234,56 €", "5 kg", "12.5%", "100 usd"]
        for value in old_dates:
            with self.subTest(value=value):
                self.assertEqual(decide("date", [value, value, value]), "date")
        for value in old_numbers:
            with self.subTest(value=value):
                self.assertEqual(decide("amount", [value, value, value]), "amount")


if __name__ == "__main__":
    unittest.main()
