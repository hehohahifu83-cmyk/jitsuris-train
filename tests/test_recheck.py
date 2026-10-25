import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import recheck as R  # noqa: E402
from guard import header_date_ok  # noqa: E402


def t3(*pairs):
    return [{"label": l, "probability": p} for l, p in pairs]


class RecheckTests(unittest.TestCase):
    def test_cues(self):
        self.assertEqual(R.single_cue("当初予算額（千円）"), "amount")
        self.assertEqual(R.single_cue("登録者数（人）"), "quantity")
        self.assertEqual(R.single_cue("構成比"), "rate")
        self.assertEqual(R.single_cue("全国地方公共団体コード"), "id")
        self.assertIsNone(R.single_cue("100万円以上200万円未満"))   # 区切りの列名は手がかりにしない
        self.assertIsNone(R.single_cue("VALUE", "UNIT: Number"))     # 番号の手がかりは単位の文字列から取らない
        self.assertNotIn("quantity", R.cue_types("号数"))

    def test_zero_values_have_no_evidence(self):
        self.assertEqual(R.check_assert("quantity", t3(("quantity", 0.99)), ["0", "0", "0"], "LA HOUSE")[0], "unknown")
        self.assertEqual(R.check_assert("id", t3(("id", 0.99)), ["270008"] * 5, "全国地方公共団体コード")[0], "id")   # 同じコードの繰り返しは根拠あり

    def test_period_header_and_month_counts(self):
        self.assertEqual(R.check_assert("amount", t3(("amount", 0.99)), ["895", "1", "5"], "2020")[1], "period_header_no_unit")
        self.assertEqual(R.check_assert("date", t3(("date", 0.9)), ["1", "51", "10"], "6月")[1], "period_header_counts")

    def test_conflicts(self):
        self.assertEqual(R.check_assert("amount", t3(("amount", 0.99)), ["3774.1", "3197.1"], "資源回収量 (t)")[0], "unknown")
        self.assertEqual(R.check_assert("rate", t3(("rate", 0.98)), ["0.5", "2.0", "3.66"], "total_sna_allocation")[1], "rate_without_cue")
        self.assertEqual(R.check_assert("rate", t3(("rate", 0.98)), ["63.8", "12.1"], "前年同月比")[0], "rate")
        self.assertEqual(R.check_assert("amount", t3(("amount", 0.97)), ["5805.763904", "78310.749617"], "disposal")[1], "amount_precision")
        self.assertEqual(R.check_assert("amount", t3(("amount", 0.98)), ["227", "0"], "Low income $603-$964 per wk")[1], "money_band_header")
        self.assertEqual(R.check_assert("amount", t3(("amount", 0.98)), ["3215", "3731"], "Total", siblings=["Date", "Burial"])[1], "amount_without_cue")
        self.assertEqual(R.check_assert("amount", t3(("amount", 0.98)), ["3215", "3731"], "Total", siblings=["Date", "Cost"])[0], "amount")

    def test_low_confidence_needs_cue(self):
        self.assertEqual(R.check_assert("quantity", t3(("quantity", 0.8)), ["3", "4"], "Atividades", t_low=0.95)[0], "unknown")
        self.assertEqual(R.check_assert("quantity", t3(("quantity", 0.8)), ["3", "4"], "人数", t_low=0.95)[0], "quantity")

    def test_recheck_unknown(self):
        self.assertEqual(R.recheck_unknown(t3(("other", 0.5), ("date", 0.3)), ["4", "5", "6"], "月", header_date_ok=header_date_ok)[0], "date")
        self.assertEqual(R.recheck_unknown(t3(("amount", 0.5), ("quantity", 0.4)), ["12", "30"], "世帯数")[0], "quantity")
        self.assertEqual(R.recheck_unknown(t3(("amount", 0.5), ("rate", 0.4)), ["12", "30"], "世帯数")[0], "unknown")   # 上位 3 つに無い種類にはしない
        self.assertEqual(R.recheck_unknown(t3(("id", 0.5), ("quantity", 0.4)), ["P42", "P97"], "頁数")[0], "unknown")

    def test_siblings(self):
        rows = [{"guarded": "quantity", "top3": t3(("quantity", 0.99)), "values": ["1", "2"], "header": f"男0{i}"} for i in range(3)]
        rows.append({"guarded": "unknown", "top3": t3(("other", 0.5), ("quantity", 0.4)), "values": ["3", "0"], "header": "男05"})
        self.assertEqual(R.apply_table(rows)[-1], ("quantity", "recheck:siblings"))


if __name__ == "__main__":
    unittest.main()
