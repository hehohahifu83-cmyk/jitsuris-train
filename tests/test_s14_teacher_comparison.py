import unittest
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from independent_eval.s14_teacher_comparison import label_ok, load_predictions, render_report, summarize


class S14TeacherComparisonTests(unittest.TestCase):
    def test_other_unknown_and_unscored_label_semantics(self):
        self.assertTrue(label_ok("unknown", "other"))
        self.assertFalse(label_ok("amount", "other"))
        self.assertTrue(label_ok("amount", "amount"))
        self.assertFalse(label_ok("unknown", "amount"))

    def test_summary_uses_only_aggregates_for_agreement_and_error_overlap(self):
        truth = {"a": "amount", "b": "other", "c": "unknown", "d": "S"}
        teachers = {
            "Claude": {"a": "amount", "b": "unknown", "c": "unknown", "d": "S"},
            "ChatGPT": {"a": "amount", "b": "category", "c": "unknown", "d": "S"},
        }
        models = {
            "E5-base": [
                {"a": "quantity", "b": "unknown", "c": "amount", "d": "S"},
                {"a": "amount", "b": "other", "c": "amount", "d": "S"},
            ],
            "mmBERT-small": [
                {"a": "amount", "b": "category", "c": "unknown", "d": "S"},
                {"a": "quantity", "b": "unknown", "c": "unknown", "d": "S"},
            ],
        }
        result = summarize(truth, teachers, models)
        self.assertEqual(result["total"], 4)
        self.assertEqual(result["scored"], 2)
        self.assertEqual(result["excluded"], {"S": 1, "unknown": 1})
        self.assertEqual(result["teacher_agreement"], 1)
        self.assertEqual(result["teacher_disagreement"], 1)
        self.assertEqual(result["teacher_accuracy"]["Claude"]["correct"], 2)
        self.assertEqual(result["teacher_accuracy"]["ChatGPT"]["correct"], 1)
        self.assertEqual(result["model_rates"]["E5-base"]["overall"]["mean_rate"], 0.75)
        self.assertEqual(result["error_overlap"]["Claude"]["E5-base"]["teacher_correct_model_wrong_mean"], 0.5)
        report = render_report(result)
        self.assertIn("裁定後ラベルはこの2つの初回ラベル", report)
        self.assertNotIn("| a |", report)
        self.assertNotIn("| b |", report)

    def test_rejects_missing_prediction_ids(self):
        truth = {"a": "amount"}
        teachers = {"Claude": {"a": "amount"}, "ChatGPT": {"a": "amount"}}
        models = {"E5-base": [{"other-id": "amount"}], "mmBERT-small": [{"a": "amount"}]}
        with self.assertRaisesRegex(ValueError, "IDs do not match"):
            summarize(truth, teachers, models)

    def test_prediction_loader_uses_the_saved_guarded_result(self):
        payload = {
            "schema_version": 1,
            "set_id": "independent-main-20261021-v1",
            "available_guard_versions": ["v9.1", "v10"],
            "rows": [{"id": "c001", "guard_predictions": {
                "v9.1": {"guarded_prediction": "amount", "decision_reason": "test"},
                "v10": {"guarded_prediction": "unknown", "decision_reason": "test"},
            }}],
        }
        with TemporaryDirectory() as directory:
            path = Path(directory) / "predictions.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            self.assertEqual(load_predictions(path), {"c001": "amount"})


if __name__ == "__main__":
    unittest.main()
