import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import rescore_guard as RG


def top(label, p, second=("org", 0.001)):
    return [{"label": label, "probability": p}, {"label": second[0], "probability": second[1]}]


class RescoreTest(unittest.TestCase):
    def guard(self, pred, order, values):
        return "unknown" if any(v == "bad" for v in values) else pred

    def test_decide_follows_threshold_guard_and_other(self):
        self.assertEqual(RG.decide_from_top3(top("date", 0.4), ["x"], self.guard), "unknown")        # 0.5 未満
        self.assertEqual(RG.decide_from_top3(top("date", 0.9), ["bad"], self.guard), "unknown")      # 見張りが止める
        self.assertEqual(RG.decide_from_top3(top("date", 0.9), ["ok"], self.guard), "date")
        self.assertEqual(RG.decide_from_top3(top("other", 0.9), ["ok"], lambda p, o, v: "unknown"), "unknown")

    def test_rescore_refuses_misaligned_rows(self):
        rows = [{"column": "年", "truth": "date", "top3": top("date", 0.9)}]
        ok = [("年", ["2020"], "date", None)]
        self.assertEqual(RG.rescore(rows, ok, self.guard), ["date"])
        with self.assertRaises(SystemExit):
            RG.rescore(rows, [("別の列", ["2020"], "date", None)], self.guard)
        with self.assertRaises(SystemExit):
            RG.rescore(rows, [("年", ["2020"], "amount", None)], self.guard)
        with self.assertRaises(SystemExit):
            RG.rescore(rows, ok + ok, self.guard)

    def test_header_normalization_matches_finetune_exp(self):
        self.assertEqual(RG.normalized_header("  Ｄａｔｅ　Paid  "), "date paid")


if __name__ == "__main__":
    unittest.main()
