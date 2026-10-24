import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import guard as G
import numpy as np
from train3 import decide_with_details


class GuardV11Test(unittest.TestCase):
    def test_positive(self):
        for h, v in (("月", ["06", "11", "7"]), ("TLIST(Q1)", ["20094", "19811"]), ("指定年月日", ["28982.0", "21629"]),
                     ("Month of Processing", ["August", "Sept"]), ("年度（和暦）（年）", ["令和7", "平成30年度"]),
                     ("元利金支払期日下期（月日）", ["02.25"]), ("tlist_m1_", ["195808"]), ("Month", ["2019M06"]),
                     ("Fiscal Quarter", ["Q1", "Q3"]), ("Trimestre fiscal（quarter）", ["T3 - 2022"])):
            self.assertTrue(G.header_date_ok(h, v), (h, v))

    def test_negative(self):
        for h, v in (("Year 2007", ["15", "8"]),          # 年ごとの数の列
                     ("住民票の写し", ["5744"]),            # 日付の語が無い
                     ("月", ["06", "abc"]),                 # 値に日付の部品でないものがある
                     ("年度", ["1,234"]),                   # 区切りつきの数
                     ("date", []),                          # 空
                     ("month", ["120000"])):                # 6 桁でも 19xx/20xx の年月でない
            self.assertFalse(G.header_date_ok(h, v), (h, v))

    def test_v10_unchanged_and_v11_superset(self):
        classes = ["date", "id", "quantity"]
        P = np.array([[0.95, 0.03, 0.02]] * 3)
        rows = [("月", ["06", "11"], "", [], ""), ("Year 2007", ["15", "8"], "", [], ""), ("開始日", ["2021-04-01"], "", [], "")]
        v10 = [d["guarded_prediction"] for d in decide_with_details(classes, P, rows, guard_version="v10")]
        v11 = [d["guarded_prediction"] for d in decide_with_details(classes, P, rows, guard_version="v11")]
        self.assertEqual(v10, ["unknown", "unknown", "date"])
        self.assertEqual(v11, ["date", "unknown", "date"])
        self.assertEqual(G.GUARD_VERSION, "v10")   # 既定（固定した版）は変えない

    def test_header_ignored_without_v11(self):
        self.assertEqual(G.guard_with_reason("date", [("date", 0.95)], ["06", "11"])[1], "date_value_evidence_low")
        self.assertEqual(G.guard_with_reason("date", [("date", 0.95)], ["06", "11"], header="月")[0], "date")


if __name__ == "__main__":
    unittest.main()
