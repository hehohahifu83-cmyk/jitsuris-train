import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guard import guard, guard_with_reason


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

    def test_retained_prediction_has_no_reason(self):
        final, reason = guard_with_reason("amount", [("amount", 0.99)], ["100", "200"])
        self.assertEqual((final, reason), ("amount", None))


if __name__ == "__main__":
    unittest.main()
