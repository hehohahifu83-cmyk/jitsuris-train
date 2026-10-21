import unittest

import guard
import guard_train_side as T
from features import STAT_NAMES, value_stats


class ShapeTests(unittest.TestCase):
    def test_shape_collapses_digits_letters_and_kana(self):
        self.assertEqual(T.shape("9時00分"), "9K9K")
        self.assertEqual(T.shape("H28. 4. 1"), "a9. 9. 9")
        self.assertEqual(T.shape("１，２３４円"), "9,9K")                 # NFKC で全角が半角になる
        self.assertEqual(T.shape("x" * 50), "a")


class AnalyzeTests(unittest.TestCase):
    def test_counts_columns_that_fall_and_shapes(self):
        streams = {"s": [
            ("日付", ["53", "54", "55"], "date", None),                    # 数字だけの日付ラベルは値だけで読めない（v10 L4）
            ("日付2", ["2024-01-01", "2024-01-02"], "date", None),          # 読める → 落ちない
            ("金額", ["-", "-", "nil", "100"], "amount", None),             # 欠損の印が多い → 落ちる
            ("金額2", ["1,000", "2,000"], "amount", None),                  # 読める
            ("名前", ["a", "b"], "text", None),                             # 対象外のラベル
        ]}
        res = T.analyze(streams, guard, value_stats, STAT_NAMES)
        c = res["per"]["s"]
        self.assertEqual((c["date_total"], c["date_fail"], c["num_total"], c["num_fail"]), (2, 1, 2, 1))
        self.assertEqual(res["cols_with"]["date"]["9"], 1)
        self.assertEqual(res["cols_with"]["num"]["-"], 1)
        self.assertEqual(res["cols_with"]["num"]["a"], 1)
        text = T.render(res)
        self.assertIn("| s | 1／2 | 1／2 |", text)


if __name__ == "__main__":
    unittest.main()
