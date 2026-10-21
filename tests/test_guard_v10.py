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
        negative = ["r35", "h32", "s65", "r0", "x28", "s.46/13/01", "r06a"]
        for value in positive:
            with self.subTest(value=value):
                self.assertTrue(G.is_date_value(G._clean([value])[0]))
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.is_date_value(G._clean([value])[0]))

    @unittest.skip("Claude consultation pending: h28.13.1 is accepted by v9.1, conflicting with D5's negative example and the v10 monotonicity requirement")
    def test_d5_13th_month_negative_example_after_spec_adjudication(self):
        self.assertFalse(G.is_date_value(G._clean(["h28.13.1"])[0]))


    def test_d5_era_year_only_requires_a_consistent_column_and_high_confidence(self):
        values = ["r06", "h28", "s62", "m45", "t15"]
        self.assertEqual(G.guard("date", [("date", 0.99), ("amount", 0.005)], values), "date")
        self.assertEqual(G.guard("date", [("date", 0.89), ("amount", 0.10)], values), "unknown")
        self.assertEqual(G.guard("date", [("date", 0.99), ("amount", 0.005)], ["r06", "h28", "2023", "r05"]), "unknown")


    def test_v91_accepted_date_and_number_shapes_remain_accepted(self):
        old_dates = ["2024-01-05", "2024年1月5日", "令和6年5月1日", "1/28/2008", "2012/13", "FY2020", "05-May-17"]
        old_numbers = ["£1,234.50", "¥1,000", "€1.234,56", "5 kg", "12.5%", "USD 1,000"]
        for value in old_dates:
            with self.subTest(value=value):
                self.assertEqual(decide("date", [value, value, value]), "date")
        for value in old_numbers:
            with self.subTest(value=value):
                self.assertEqual(decide("amount", [value, value, value]), "amount")


    def test_d1_weekday_suffixes_require_a_date_before_the_day_name(self):
        positive = ["2024/3/5(火)", "2024年3月5日(火曜日)", "3月5日(火)", "2024-03-05 tue", "2024/03/05 火"]
        negative = ["火", "(火)", "5(火)", "2024(火)", "月曜日"]
        for value in positive:
            with self.subTest(value=value):
                self.assertEqual(decide("date", [value, value]), "date")
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.is_date_value(G._clean([value])[0]))

    def test_d4_quarters_and_half_years_with_ambiguous_q1_column_condition(self):
        positive = ["第1四半期", "2024年度第1四半期", "4th quarter", "24q1", "2024年度下半期"]
        negative = ["q5", "第5四半期", "5th quarter", "quarterly", "1qa"]
        self.assertEqual(decide("date", positive), "date")
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.is_date_value(G._clean([value])[0]))
        self.assertFalse(G.is_date_value("q1"))
        self.assertEqual(decide("date", ["q1", "abc", "xyz", "foo", "bar"]), "unknown")
        self.assertEqual(decide("date", ["q1", "q1", "q1", "q1", "q1"]), "date")

    def test_d6_standalone_english_month_names_need_two_months_and_eighty_percent(self):
        self.assertEqual(decide("date", ["march", "jan", "april", "may", "june"]), "date")
        negative_columns = [
            ["may be", "may be", "may be", "may be", "may be"],
            ["march", "march 2020", "foo", "bar", "baz"],
            ["mar", "mar", "mar", "mar", "mar"],
            ["march", "march", "foo", "bar", "baz"],
            ["march", "jan", "foo", "bar", "baz"],
        ]
        for values in negative_columns:
            with self.subTest(values=values):
                self.assertEqual(decide("date", values), "unknown")

    def test_n2_trailing_currency_symbols_codes_and_words(self):
        positive = ["220.00 」", "1.234,56 €", "100 usd", "1,000 yen", "5,000ドル"]
        negative = ["100 abc", "100 $ 200", "$", "100 e", "5,000 cats"]
        for value in positive:
            with self.subTest(value=value):
                self.assertEqual(decide("amount", [value, value]), "amount")
        for value in negative:
            with self.subTest(value=value):
                self.assertEqual(decide("amount", [value, value]), "unknown")

    def test_n8_duration_and_unit_terms_are_bounded(self):
        positive = ["8,250円/1時間", "0円/1か月", "30分", "3,000㎡", "10.00 number"]
        negative = ["100 abc", "100 numbering", "円/", "5 unknown", "30 fans"]
        for value in positive:
            with self.subTest(value=value):
                self.assertEqual(decide("quantity", [value, value]), "quantity")
        for value in negative:
            with self.subTest(value=value):
                self.assertEqual(decide("quantity", [value, value]), "unknown")


    def test_rules_can_be_replayed_one_at_a_time(self):
        probs = [("date", 0.99), ("text", 0.005)]
        self.assertEqual(G.guard_with_reason("date", probs, ["9時00分"], _enabled_rules=set())[0], "unknown")
        self.assertEqual(G.guard_with_reason("date", probs, ["9時00分"], _enabled_rules={"D3"})[0], "date")
        self.assertEqual(G.guard_with_reason("date", probs, ["r 5.10.28"], _enabled_rules={"D3"})[0], "unknown")
        self.assertEqual(G.guard_with_reason("date", probs, ["r 5.10.28"], _enabled_rules={"D5"})[0], "date")
        amount_probs = [("amount", 0.99), ("text", 0.005)]
        self.assertEqual(G.guard_with_reason("amount", amount_probs, ["100 usd", "100 usd"], _enabled_rules={"N8"})[0], "unknown")
        self.assertEqual(G.guard_with_reason("amount", amount_probs, ["100 usd", "100 usd"], _enabled_rules={"N2"})[0], "amount")
        self.assertEqual(G.guard_with_reason("amount", amount_probs, ["30分", "30分"], _enabled_rules={"N2"})[0], "unknown")
        self.assertEqual(G.guard_with_reason("amount", amount_probs, ["30分", "30分"], _enabled_rules={"N8"})[0], "amount")


if __name__ == "__main__":
    unittest.main()
