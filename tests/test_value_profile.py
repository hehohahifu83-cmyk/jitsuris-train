import unittest

from encoder_context import format_encoder_text
from value_profile import value_profile


class ValueProfileTests(unittest.TestCase):
    def test_amounts_with_yen_and_separators(self):
        self.assertEqual(value_profile(["1,200円", "3,450円", "980円"]), "数値 3/3 整数 桁3〜4 区切り 円")

    def test_decimal_negative_and_parentheses(self):
        self.assertEqual(value_profile(["-1.5", "(2.25)", "△3"]), "数値 3/3 小数2桁 桁1 負")

    def test_codes_keep_leading_zero_and_fixed_length(self):
        self.assertEqual(value_profile(["00123", "04567", "01234"]), "数値 3/3 整数 桁5 先頭0 長さ一定")

    def test_dates_are_marked(self):
        self.assertTrue(value_profile(["2024-10-21", "2024-11-02", "2024-12-01"]).startswith("日付形 3/3 数値 0/3"))
        self.assertTrue(value_profile(["令和5年4月1日", "R5.10.1"]).startswith("日付形 2/2"))

    def test_text_values_and_duplicates(self):
        self.assertEqual(value_profile(["東京都", "大阪府", "東京都"]), "数値 0/3 長さ3 字漢 重複")
        self.assertEqual(value_profile(["Apple", "りんご"]), "数値 0/2 長さ3〜5 字英・かな")

    def test_fullwidth_is_normalized_and_junk_ignored(self):
        self.assertEqual(value_profile(["１２３", "", "NaN", "45"]), "数値 2/2 整数 桁2〜3")
        self.assertEqual(value_profile([]), "")
        self.assertEqual(value_profile(["", "-"]), "")

    def test_percent(self):
        self.assertEqual(value_profile(["12.5%", "8%", "100%"]), "数値 3/3 小数1桁 桁1〜3 %")

    def test_format_unchanged_without_flag(self):
        row = ("金額", ["1,200", "980"], "amount", ["品名", "数量"], "")
        self.assertEqual(format_encoder_text(row, "query: "), "query: 列名: 金額 | 値: 1,200, 980 | 同じ表の列: 品名, 数量")

    def test_format_places_profile_after_values(self):
        row = ("金額", ["1,200", "980"], "amount", ["品名", "数量"], "")
        self.assertEqual(format_encoder_text(row, "", val_profile=True),
                         "列名: 金額 | 値: 1,200, 980 | 値の形: 数値 2/2 整数 桁3〜4 区切り | 同じ表の列: 品名, 数量")

    def test_only_shown_values_are_used(self):
        self.assertEqual(value_profile(["1", "2", "3", "4", "5", "x"]), value_profile(["1", "2", "3", "4", "5"]))


if __name__ == "__main__":
    unittest.main()
