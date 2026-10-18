import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import abstain_eval as ab


def row(truth, pred, p1):
    return {"index": 0, "column": "x", "truth": truth, "prediction": pred, "critical": False, "top3": [{"label": pred, "probability": p1}]}


class AbstainTest(unittest.TestCase):
    def test_threshold_turns_low_confidence_numeric_into_unknown(self):
        rows = [row("amount", "quantity", 0.6), row("amount", "amount", 0.99), row("org", "org", 0.55)]
        base = ab.apply(rows, 0.0)
        self.assertEqual((base["correct"], base["wrong"], base["critical"]), (2, 1, 1))
        strict = ab.apply(rows, 0.9)
        self.assertEqual((strict["correct"], strict["wrong"], strict["unknown"], strict["critical"]), (2, 0, 1, 0))
        self.assertEqual(strict["answered"], 2 / 3)

    def test_other_truth_is_correct_when_unknown(self):
        m = ab.apply([row("other", "unknown", 0.9), row("other", "id", 0.4)], 0.0)
        self.assertEqual((m["n"], m["other_ng"]), (0, 1))

    def test_smallest_safe_threshold_and_leave_one_out(self):
        with tempfile.TemporaryDirectory() as d:
            for name, rows in (("a", [row("amount", "quantity", 0.7), row("date", "date", 0.99)]),
                               ("b", [row("id", "amount", 0.8), row("id", "id", 0.97)])):
                json.dump({"test": name, "condition": "x", "rows": rows}, open(Path(d, f"probs_{name}_blend70.json"), "w"))
            tests = ab.load(d, "blend70")
            self.assertEqual(ab.smallest_safe_threshold(tests, ["a"]), 0.71)
            self.assertEqual(ab.smallest_safe_threshold(tests, ["a", "b"]), 0.81)
            text = ab.report(d, "blend70")
            self.assertIn("leave-one-test-out", text)
            self.assertIn("0.81", text)

    def test_blind_sets_are_refused(self):
        with tempfile.TemporaryDirectory() as d:
            json.dump({"test": "blind", "rows": []}, open(Path(d, "probs_blind_set7_blend70.json"), "w"))
            with self.assertRaises(RuntimeError):
                ab.load(d, "blend70")


if __name__ == "__main__":
    unittest.main()
