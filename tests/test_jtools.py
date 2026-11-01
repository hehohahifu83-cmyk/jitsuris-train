"""ジツリスの道具（jtools/）の試験（2026-11-01 Claude）。JS 版との一致は jtools/parity.test.mjs（node --test）。"""
import json
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from jtools import check_digits as CD  # noqa: E402
from jtools import read_value as RV  # noqa: E402
from jtools import run_tools as RT  # noqa: E402
from jtools import table_arith as TA  # noqa: E402


def num(v):
    r = RV.read_value(v)
    return (r["value"], r["currency"], r["unit"]) if r["kind"] == "number" else r["kind"]


class ReadValue(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(num("１，２３４円"), (1234.0, "JPY", ""))
        self.assertEqual(num("△1,200"), (-1200.0, "", ""))
        self.assertEqual(num("(3,000)"), (-3000.0, "", ""))
        self.assertEqual(num("3万5千"), (35000.0, "", ""))
        self.assertEqual(num("千二百三十四"), (1234.0, "", ""))
        self.assertEqual(num("1.234,56 €"), (1234.56, "EUR", ""))
        self.assertEqual(num("1,234千円"), (1234.0, "JPY", "千円"))
        self.assertEqual(num("45%"), (45.0, "", "%"))
        self.assertEqual(num("〇"), "text")   # 有の印

    def test_dates(self):
        r = RV.read_value("令和7年4月1日")
        self.assertEqual((r["kind"], r["y"], r["m"], r["d"], r["era"]), ("date", 2025, 4, 1, "令和"))
        r = RV.read_value("H18. 1.26")
        self.assertEqual((r["y"], r["m"], r["d"]), (2006, 1, 26))
        self.assertTrue(RV.read_value("平成30年度")["fiscal"])
        self.assertEqual(RV.read_value("13/02/2020")["m"], 2)
        self.assertEqual(RV.read_value("20240401")["kind"], "number")   # 8 桁は数として返す（列名と合わせるのは呼ぶ側）

    def test_empty_and_time(self):
        self.assertEqual(RV.read_value("-")["kind"], "empty")
        self.assertEqual(RV.read_value("12:30")["kind"], "time")
        self.assertEqual(RV.read_value("25:00")["kind"], "text")


class CheckDigits(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(CD.check("7000012050002"), ["corp_jp"])          # 国税庁の法人番号
        self.assertEqual(CD.check("T7000012050002"), ["invoice_jp"])
        self.assertIn("gtin", CD.check("4901234567894"))
        self.assertIn("isbn", CD.check("ISBN 978-4-00-310101-8"))
        self.assertEqual(CD.check("GB82 WEST 1234 5698 7654 32"), ["iban"])
        self.assertEqual(CD.check("131016"), ["lgcode_jp"])                # 千代田区
        self.assertEqual(CD.check("SW1A 1AA"), ["postcode_uk"])

    def test_one_digit_off(self):
        self.assertNotIn("corp_jp", CD.check("7000012050003"))
        self.assertNotIn("gtin", CD.check("4901234567895"))
        self.assertNotIn("lgcode_jp", CD.check("131017"))
        self.assertNotIn("iban", CD.check("GB82WEST12345698765433"))
        self.assertNotIn("luhn16", CD.check("4111111111111112"))

    def test_summary_counts_distinct(self):
        s = CD.column_summary(["131016", "131016", "131016", "x"])
        self.assertEqual(s, {"n": 2, "lgcode_jp": 1})


def table(*cols):
    return [{"header": h, "rows": [str(v) for v in vs]} for h, vs in cols]


class TableArith(unittest.TestCase):
    def test_product_and_tax(self):
        price = [100, 250, 80, 1200, 55, 300]
        qty = [3, 2, 10, 1, 4, 7]
        amount = [p * q for p, q in zip(price, qty)]
        incl = [int(a * 1.1) for a in amount]
        rels = TA.relations(table(("単価", price), ("数量", qty), ("金額", amount), ("税込", incl)))
        kinds = {(r["rel"], tuple(r["cols"])) for r in rels}
        self.assertIn(("product", (0, 1, 2)), kinds)
        self.assertIn(("tax", (2, 3)), kinds)
        self.assertEqual(next(r for r in rels if r["rel"] == "tax")["rate"], 0.1)

    def test_sum_and_ratio(self):
        male = [362, 535, 1200, 48, 900]
        female = [401, 520, 1180, 52, 950]
        total = [m + f for m, f in zip(male, female)]
        share = [round(m / t * 100, 1) for m, t in zip(male, total)]
        rels = TA.relations(table(("男性", male), ("女性", female), ("総数", total), ("男性の割合", share)))
        kinds = {(r["rel"], tuple(r["cols"])) for r in rels}
        self.assertIn(("sum", (0, 1, 2)), kinds)
        self.assertIn(("ratio", (0, 2, 3)), kinds)   # 部分 ÷ 全体 × 100 の向き

    def test_one_side_and_noise(self):
        debit = [100, 0, 250, 0, 80, 0]
        credit = [0, 300, 0, 75, 0, 120]
        self.assertEqual([r["rel"] for r in TA.relations(table(("借方", debit), ("貸方", credit)))], ["one_side"])
        self.assertEqual(TA.relations(table(("a", [3, 9, 27, 4, 8]), ("b", [7, 1, 2, 5, 6]))), [])
        self.assertEqual(TA.relations(table(("a", [1, 2, 3, 4]), ("b", [1, 2, 3, 4]))), [])   # 行が 5 より少ない


class RunTools(unittest.TestCase):
    def test_text(self):
        res = RT.run_table([{"header": "法人番号", "values": ["7000012050002", "6190001023380", "1190002012718"]},
                            {"header": "日付", "values": ["令和7年4月1日", "令和6年3月1日", "R5.1.1"]}])
        self.assertIn("法人番号", res[0]["text"])
        self.assertIn("和暦", res[1]["text"])
        self.assertTrue(res[1]["text"].startswith("日付100%"))

    def test_fixtures_up_to_date(self):
        """fixtures.json の手の値の結果が、今の Python の結果と同じ（変えたら make_fixtures.py で作り直す）。"""
        fx = json.load(open(os.path.join(ROOT, "jtools", "fixtures.json"), encoding="utf-8"))
        for f in fx["values"]:
            self.assertEqual(RV.read_value(f["in"]), f["read"], f["in"])
            self.assertEqual(CD.check(f["in"]), f["check"], f["in"])


if __name__ == "__main__":
    unittest.main()
