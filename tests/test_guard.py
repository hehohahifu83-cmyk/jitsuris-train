import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import guard as G

HI = [("date", 0.99), ("org", 0.005)]


def g(pred, values, top=0.99, second=("org", 0.005)):
    return G.guard(pred, [(pred, top), second], values)


class GuardDateTest(unittest.TestCase):
    def test_old_formats_still_pass(self):
        self.assertEqual(g("date", ["2024-01-05", "2024-02-10", "2023-12-31"]), "date")
        self.assertEqual(g("date", ["2024年1月5日", "2024年2月10日"]), "date")
        self.assertEqual(g("date", ["令和6年5月1日", "令和5年4月1日"]), "date")
        self.assertEqual(g("date", ["1/28/2008", "11/28/2003"]), "date")

    def test_new_date_formats_pass(self):
        cases = {
            "fiscal slash": ["2012/13", "2016/17", "2013/14"], "fiscal dash": ["2023-24", "2023-24", "2022-23"],
            "fiscal jp": ["1994/4-3.", "2015/4-3.", "2004/4-3."], "period underscore": ["2019/2020_", "2017/2018", "2015/2016_"],
            "quarter": ["2014Q1", "2016Q1", "2015Q3"], "quarter2": ["Q1 2012", "Q3 2011", "Q2 2008"],
            "year-month": ["2020-07", "2020/08", "2021-01"], "month-year": ["07-2015", "09-2015", "11-2015"],
            "statcan": ["2020M07D23", "2020M04D22"], "month names": ["05-May-17", "18-May-17", "25-May-17"],
            "day month": ["31st March", "30th September", "31st March"], "year month name": ["2020 June 30", "2020 May 1", "2020 July 4"],
            "datetime am/pm": ["2/6/1998 12:00:00 AM", "11/30/1989 1:30 PM", "2/13/1985 9:00 AM"], "dotted": ["31.12.2019", "01.01.2020"],
            "time": ["03:35", "12:10", "23:59:10"], "jp era": ["平成30年", "令和元年", "昭和60年"], "jp year": ["2023年度", "2022年度", "2021年度"],
            "jp month day": ["4月1日", "5月15日", "12月31日"], "era dotted": ["H30.4.1", "R5.5.1", "S60.1.1"], "fullwidth": ["２０２０／０７", "２０２１／０８"],
        }
        for name, values in cases.items():
            with self.subTest(name):
                self.assertEqual(g("date", values), "date", values)

    def test_year_only_needs_high_confidence(self):
        years = ["2015", "2016", "2017", "2023"]
        self.assertEqual(g("date", years, top=0.99), "date")
        self.assertEqual(g("date", years, top=0.90), "date")
        self.assertEqual(g("date", years, top=0.73, second=("amount", 0.21)), "unknown")   # 金額かもしれない（Grant in Dollars 型）
        self.assertEqual(g("date", ["2000", "2000", "1200", "2000", "2000"], top=0.73, second=("amount", 0.21)), "unknown")

    def test_non_dates_are_still_vetoed(self):
        self.assertEqual(g("date", ["hello", "world", "foo"]), "unknown")
        self.assertEqual(g("date", ["3rd quintile", "2nd quintile", "1st quintile"]), "unknown")
        self.assertEqual(g("date", ["Junior 2", "Senior 3", "Marketing 1"]), "unknown")   # 月名の頭文字だけでは日付と読まない
        self.assertEqual(g("date", ["10160000", "10160001", "10160002"]), "unknown")   # 8桁コード
        self.assertEqual(g("date", ["12345.5", "20200.5", "3.14"]), "unknown")
        self.assertEqual(g("date", ["2020.5", "2021.5", "2022.25"]), "unknown")       # 小数は年月ではない

    def test_mixed_columns_follow_the_half_rule(self):
        self.assertEqual(g("date", ["2024-01-05", "2024-02-10", "n/a", "n/a"]), "date")
        self.assertEqual(g("date", ["2024-01-05", "n/a", "n/a", "n/a"]), "unknown")


class GuardNumberTest(unittest.TestCase):
    def test_currency_and_units_read_as_numbers(self):
        cases = {
            "pound": ["£1,234.50", "£10.99", "£70.00"], "mojibake pound": ["｣8,549.00", "｣23,306.00", "｣113.64"], "euro": ["€1.234,56", "€10,00"],
            "code": ["USD 1,000", "USD 2,500.50"], "per person": ["330円/人", "4,598円/人", "27,045円/人"], "yen": ["¥1,000", "2,000円", "￥3,000"],
            "paren negative": ["(1,234)", "(500)", "(70)"], "unit": ["5 kg", "12 pcs", "3 items"], "count": ["3件", "10個", "5人"],
        }
        for name, values in cases.items():
            for pred in ("amount", "quantity"):
                with self.subTest((name, pred)):
                    self.assertEqual(g(pred, values, second=("text", 0.005)), pred, values)

    def test_text_is_still_vetoed_for_amount_quantity_rate(self):
        for pred in ("amount", "quantity", "rate"):
            self.assertEqual(g(pred, ["alpha", "beta", "gamma"], second=("text", 0.005)), "unknown")
        self.assertEqual(g("amount", ["3rd quintile", "2nd quintile", "1st quintile"], second=("text", 0.005)), "unknown")
        self.assertEqual(g("rate", ["#DIV/0!", "#DIV/0!", "#DIV/0!"], second=("text", 0.005)), "unknown")

    def test_rate_accepts_percent_and_loose_numbers(self):
        self.assertEqual(g("rate", ["12.5%", "30%", "8.1%"], second=("text", 0.005)), "rate")
        self.assertEqual(g("rate", ["0.125", "0.3", "0.081"], second=("text", 0.005)), "rate")


class GuardOtherTest(unittest.TestCase):
    def test_other_and_numeric_tie_become_unknown(self):
        self.assertEqual(G.guard("other", [("other", 0.9), ("text", 0.05)], ["a"]), "unknown")
        self.assertEqual(G.guard("amount", [("amount", 0.5), ("quantity", 0.4)], ["1", "2"]), "unknown")
        self.assertEqual(G.guard("amount", [("amount", 0.9), ("quantity", 0.05)], ["1", "2"]), "amount")

    def test_no_values_means_no_value_veto(self):
        self.assertEqual(G.guard("date", [("date", 0.9), ("org", 0.01)], []), "date")
        self.assertEqual(G.guard("amount", [("amount", 0.9), ("org", 0.01)], ["", " ", ""]), "amount")

    def test_long_values_do_not_hang(self):
        import time
        t0 = time.time()
        G.guard("amount", [("amount", 0.9), ("text", 0.01)], ["1," * 5000 + "x", "9" * 20000 + "!"])
        self.assertLess(time.time() - t0, 1.0)


class GuardBoundaryTest(unittest.TestCase):
    """ChatGPT のレビュー（2026-10-18 13:01）で挙がった境界。v9.1 で締めた所（誤りを増やさず『不明』が増える方向）。"""

    def test_fy_needs_the_whole_form(self):
        self.assertEqual(g("date", ["fy2024xyz"] * 3), "unknown")
        for ok in ("FY2024", "FY2023-24", "FY20Q3", "FY'20"):
            self.assertEqual(g("date", [ok] * 3), "date", ok)

    def test_year_month_and_year_range(self):
        for bad in ("2020-99", "2021-13", "2020-00", "2020-45", "2010-2099", "2020/2021_zzz"):
            self.assertEqual(g("date", [bad] * 3), "unknown", bad)
        for ok in ("2020-12", "2020/7", "2023-24", "1999/00", "2012/2013", "2017/2018_Apr", "2012/2013_Q3", "07-2015"):
            self.assertEqual(g("date", [ok] * 3), "date", ok)

    def test_month_names_need_a_date_shape(self):
        for bad in ("may 5 items", "march of the penguins 2005", "5 May 2017 (rev)"):
            self.assertEqual(g("date", [bad] * 3), "unknown", bad)
        for ok in ("Tue, 05 May 2017", "2016 Mar 01 12:00:00 AM", "5 May 2017", "31st March", "March 2020", "05-May-17"):
            self.assertEqual(g("date", [ok] * 3), "date", ok)

    def test_number_separators_need_a_number_shape(self):
        for pred in ("amount", "quantity", "rate"):
            for bad in (["1,,2", "1..2", "3,,4"], ["1 2 3", "4 5 6"], ["1,234,56", "2,345,67"]):
                self.assertEqual(g(pred, bad, second=("text", 0.004)), "unknown", (pred, bad))
            for ok in (["1,234.50", "10,000"], ["12,34,567", "1,23,456"], ["1.234,56", "2.345,67"], ["1 234", "5 678"], ["12.5", "0,5"]):
                self.assertEqual(g(pred, ok, second=("text", 0.004)), pred, (pred, ok))

    def test_whitespace_sets_match_the_js_side(self):
        # Python の strip は \x1c〜\x1f・\x85 を落とし \ufeff を落とさない／JS の trim は逆。どちらでも同じ集合で落とす
        self.assertEqual(G._clean(["\ufeff 2024-01-05 \x1c"]), ["2024-01-05"])
        self.assertEqual(G._clean(["\x852024-01-05\x1f", "\u00a0x\u3000", "\u1680y\u2003"]), ["2024-01-05", "x", "y"])
        self.assertEqual(G.guard("date", [("date", 0.99), ("org", 0.004)], ["\ufeff2024-01-05", "\x1c2024-02-05", "2024-03-05\x1f"]), "date")

    def test_the_64_char_cut_counts_code_points(self):
        v = "a" * 63 + "\U0001F600" + "b"
        self.assertEqual(G._clean([v]), ["a" * 63 + "\U0001F600"])   # JS では Array.from で数える

    def test_none_is_empty_in_both_places(self):
        self.assertEqual(G._clean([None, "x", ""]), ["x"])
        self.assertFalse(G.bad_ymd8([None, "20240101", "20240102"]))   # None は空の値として数えない（JS の ?? '' と同じ）


if __name__ == "__main__":
    unittest.main()
