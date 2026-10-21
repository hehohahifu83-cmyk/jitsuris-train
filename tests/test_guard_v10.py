import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import guard as G
from guard_accounting import v10_gate_failures

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
        positive = ["2024/3/5(火)", "2024年3月5日(火曜日)", "3月5日(火)", "3/15(火)", "2024-03-05 tue", "2024/03/05 火"]
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


class GuardV10P2Tests(unittest.TestCase):
    """P2 acceptance examples come from the written format definitions."""

    def test_d2_month_day_columns_need_a_day_at_least_thirteen(self):
        slash_column = ["3/15", "4/20", "5/1", "6/30", "7/25"]
        dash_column = ["3-15", "4-20", "5-1", "6-30", "7-25"]
        self.assertEqual(decide("date", slash_column), "date")
        self.assertEqual(G.guard_with_reason("date", [("date", 0.99), ("text", 0.005)], slash_column, _enabled_rules={"D2"})[0], "date")
        self.assertEqual(G.guard_with_reason("date", [("date", 0.99), ("text", 0.005)], dash_column, _enabled_rules={"D2"})[0], "date")
        self.assertEqual(decide("date", ["3月15日", "4月20日", "5月1日", "6月30日", "7月25日"]), "date")
        self.assertTrue(G.is_date_value(G._clean(["3/15(火)"])[0]))  # D1 permits a weekday suffix without D2's column condition
        for values in (["1/2", "3/4", "5/6", "7/8", "9/10"],
                       ["1-2", "3-4", "5-6", "7-8", "9-10"],
                       ["13/5", "2/30", "4/31", "0/5", "3/0"],
                       ["3/15", "4/20", "junk", "junk", "junk"]):
            with self.subTest(values=values):
                self.assertEqual(decide("date", values), "unknown")
        # v9.1 already accepts M月D日 via DATE_EXTRA; the v10 rule is additive.
        self.assertEqual(decide("date", ["1月2日", "3月4日", "5月6日", "7月8日", "9月10日"]), "date")

    def test_d7_date_periods_require_two_strong_endpoints(self):
        positive = [
            "2025年12月~2026年3月", "01/04/2016 - 30/06/2016",
            "2009/10-2011/12", "april 1 to june 30, 2024",
            "april 2017 - march 2018",
        ]
        for value in positive:
            with self.subTest(value=value):
                self.assertEqual(decide("date", [value, value]), "date")
        negative = ["1-2", "10~20", "2024/03/05 ~", "a - b", "2024/03/05 to"]
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.is_date_value(G._clean([value])[0]))

    def test_d8_unix_seconds_and_milliseconds_need_all_values_and_high_confidence(self):
        positive = ["1333085198.0", "1709600000", "1709600000000", "946684800", "4102444800000"]
        self.assertEqual(decide("date", positive), "date")
        self.assertEqual(G.guard("date", [("date", 0.89), ("text", 0.005)], positive), "unknown")
        negative_columns = [
            ["0312345678", "0312345678"], ["99999999999", "99999999999"],
            ["-1709600000", "-1709600000"], ["1709600000000000", "1709600000000000"],
            ["1709600000", "1709600000", "99999999999"],
        ]
        for values in negative_columns:
            with self.subTest(values=values):
                self.assertEqual(decide("date", values), "unknown")

    def test_d9_month_and_year_period_suffix(self):
        positive = ["2024年3月分", "3月分", "令和6年3月分", "2024年分", "平成30年4月分"]
        for value in positive:
            with self.subTest(value=value):
                self.assertEqual(decide("date", [value, value]), "date")
        negative = ["分", "3分", "2時間分", "2024年13月分", "令和年3月分"]
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.is_date_value(G._clean([value])[0]))
        self.assertTrue(G.is_date_value(G._clean(["令和6年0月分"])[0]))  # accepted by v9.1's era prefix; monotonicity preserves it

    def test_n3_qualifiers_comparators_and_annotations_are_bounded(self):
        positive = ["約1,000", "1,000以上", "1,234円(税込)", "税込1,234円", ">100", "100+", "$236.7 million*"]
        self.assertEqual(decide("amount", positive), "amount")
        probs = [("amount", 0.99), ("text", 0.005)]
        for value in positive[:-1]:
            with self.subTest(rule="N3", value=value):
                self.assertEqual(G.guard_with_reason("amount", probs, [value], _enabled_rules={"N3"})[0], "amount")
        self.assertEqual(G.guard_with_reason("amount", probs, [positive[-1]], _enabled_rules={"N3", "N4"})[0], "amount")
        self.assertTrue(G.NUM_LOOSE_N3N4.match(G._clean([positive[-1]])[0]))
        negative = ["約", "以上", "約abc", "1,000以上abc", ">", "100++"]
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.NUM_LOOSE.match(G._clean([value])[0]))

    def test_n4_japanese_and_english_magnitude_words(self):
        positive = ["1.5万円", "3億2,000万円", "12億", "100万", "5千円",
                    "1,234千円", "1,234百万円", "2.5兆円", "$1.2m", "1.2 million", "2bn", "3.4mn", "1.5k"]
        self.assertEqual(decide("amount", positive), "amount")
        self.assertTrue(G.NUM_LOOSE_N4_M.match(G._clean(["$1.2m"])[0]))
        self.assertFalse(G.NUM_LOOSE_N4_M.match(G._clean(["1.2m"])[0]))
        negative = ["万円", "1.5万万円", "億万", "3 b", "million", "1e3x"]
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.NUM_LOOSE.match(G._clean([value])[0]))

    def test_n5_exponent_notation_is_strict(self):
        positive = ["1.2e+05", "1e6", "3e-4", "-2.3E5", "+5e0"]
        self.assertEqual(decide("amount", positive), "amount")
        negative = ["e5", "1e", "1e+", "12e3x", "1ee3"]
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.NUM_LOOSE.match(G._clean([value])[0]))

    def test_n6_trailing_minus_is_not_a_range_or_arbitrary_suffix(self):
        positive = ["1,234-", "1234-", "1,234.50-", "¥1,234-", "1 234−"]
        self.assertEqual(decide("amount", positive), "amount")
        negative = ["-", "1-2", "12-34-56", "abc-", "1,234--"]
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.NUM_LOOSE.match(G._clean([value])[0]))

    def test_n7_rate_words_and_units_are_bounded(self):
        positive = ["35.0パーセント", "5.1ポイント", "12.5pt", "2.5倍", "3割",
                    "12.5％ポイント", "25bps", "100ppm", "100‰"]
        self.assertEqual(decide("rate", positive), "rate")
        self.assertEqual(decide("rate", ["12.5％ポイント"]), "rate")
        probs = [("rate", 0.99), ("text", 0.005)]
        for value in positive:
            with self.subTest(rule="N7", value=value):
                self.assertEqual(G.guard_with_reason("rate", probs, [value], _enabled_rules={"N7"})[0], "rate")
        negative = ["パーセント", "5ポイントカード", "12ptx", "3割引き", "ppm"]
        for value in negative:
            with self.subTest(value=value):
                self.assertFalse(G.NUM_LOOSE.match(G._clean([value])[0]))

    def test_p2_rules_can_be_replayed_one_at_a_time(self):
        probs = [("date", 0.99), ("text", 0.005)]
        self.assertEqual(G.guard_with_reason("date", probs, ["3/15", "4/20", "5/1", "6/30", "7/25"], _enabled_rules={"D2"})[0], "date")
        self.assertEqual(G.guard_with_reason("date", probs, ["2025年12月~2026年3月"], _enabled_rules={"D7"})[0], "date")
        self.assertEqual(G.guard_with_reason("date", probs, ["1709600000", "1709600000"], _enabled_rules={"D8"})[0], "date")
        self.assertEqual(G.guard_with_reason("date", probs, ["2024年3月分"], _enabled_rules={"D9"})[0], "date")
        amount_probs = [("amount", 0.99), ("text", 0.005)]
        for rule, value in (("N3", "約1,000"), ("N4", "1.2 million"), ("N5", "1e6"), ("N6", "1,234-"), ("N7", "12.5pt")):
            with self.subTest(rule=rule):
                self.assertEqual(G.guard_with_reason("amount", amount_probs, [value], _enabled_rules={rule})[0], "amount")


class GuardV10ReplayGateTests(unittest.TestCase):
    def test_gate_requires_zero_critical_and_regression_counts_and_a_five_to_one_gain(self):
        self.assertEqual(v10_gate_failures({"A": 10, "B": 2, "C": 0, "D": 0}), [])
        self.assertEqual(v10_gate_failures({"A": 9, "B": 2, "C": 0, "D": 0}), ["A must be at least 5 times B"])
        self.assertEqual(v10_gate_failures({"A": 10, "B": 2, "C": 1, "D": 0}), ["C must be 0"])
        self.assertEqual(v10_gate_failures({"A": 10, "B": 2, "C": 0, "D": 1}), ["D must be 0"])


if __name__ == "__main__":
    unittest.main()
