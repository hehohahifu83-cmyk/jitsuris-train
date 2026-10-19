import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from guard import guard, guard_with_reason
from train3 import decide, decide_with_details


class DecisionReasonTest(unittest.TestCase):
    def test_guard_reason_codes_preserve_legacy_decisions(self):
        cases = [
            ("other", [("other", 0.99)], [], "other_class"),
            ("date", [("date", 0.99)], ["hello", "world"], "date_value_evidence_low"),
            ("date", [("date", 0.99), ("id", 0.01)], ["20191340"], "date_invalid_8digit"),
            ("amount", [("amount", 0.99)], ["alpha", "beta"], "numeric_values_not_parseable"),
            ("amount", [("amount", 0.55), ("quantity", 0.45)], [], "numeric_top2_too_close"),
        ]
        for pred, probs, values, expected_reason in cases:
            with self.subTest(reason=expected_reason):
                final, reason = guard_with_reason(pred, probs, values)
                self.assertEqual(final, guard(pred, probs, values))
                self.assertEqual(final, "unknown")
                self.assertEqual(reason, expected_reason)

    def test_legacy_decide_matches_details_output(self):
        classes = ["amount", "org", "quantity"]
        probs = np.array([[0.7, 0.2, 0.1], [0.4, 0.4, 0.2]])
        rows = [("revenue", ["100", "200"]), ("name", [])]
        details = decide_with_details(classes, probs, rows, use_guard=False)
        self.assertEqual(decide(classes, probs, rows, use_guard=False),
                         [x["guarded_prediction"] for x in details])
        self.assertEqual(details[0]["decision_reason"], None)
        self.assertEqual(details[1]["decision_reason"], "probability_below_threshold")
        self.assertEqual(details[0]["raw_prediction"], "amount")


if __name__ == "__main__":
    unittest.main()
