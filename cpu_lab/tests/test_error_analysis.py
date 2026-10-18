import json
import tempfile
import unittest
from pathlib import Path

from cpu_lab.error_analysis import analyze, load_reports


class ErrorAnalysisTests(unittest.TestCase):
    def write(self, root, name, rows):
        (root / name).write_text(json.dumps({"rows": rows}), encoding="utf-8")

    def test_allowlisted_reports_and_cross_seed_recurrence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = {"column": "Total invoices paid", "truth": "quantity", "prediction": "amount",
                   "critical": True, "top3": [{"label": "amount", "probability": 0.99}]}
            other_error = {"column": "unclassified field", "truth": "other", "prediction": "address",
                           "critical": False, "top3": [{"label": "address", "probability": 0.75}]}
            self.write(root, "job1_probs_business_ft.json", [row, other_error])
            self.write(root, "job2_probs_business_ft.json", [row, other_error])
            # A prohibited/unrecognized report is deliberately not opened.
            (root / "blind_set7_probs_business_ft.json").write_text("not json", encoding="utf-8")
            rows = load_reports(root)
            report = analyze(rows)
            self.assertEqual(len(rows), 4)
            self.assertIn("quantity→amount", report)
            self.assertIn("total invoices paid", report)
            self.assertIn("seed 1, seed 2", report)
            self.assertIn("other見落とし", report)
            self.assertIn("unclassified field", report)

    def test_forbidden_root_is_rejected(self):
        with self.assertRaises(ValueError):
            load_reports(Path("/tmp/blind_set7"))

    def test_no_allowed_reports_does_not_claim_analysis(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIn("原因分析は未実施", analyze(load_reports(Path(tmp))))


if __name__ == "__main__":
    unittest.main()
