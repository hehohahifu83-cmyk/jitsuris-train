import json
import tempfile
import unittest
from pathlib import Path

from cpu_lab.eval_artifact_integrity import validate_report_dir


def row(index, truth, prediction, outcome, critical=False, column=None):
    return {"index": index, "column": column or f"col_{index}", "truth": truth,
            "prediction": prediction, "outcome": outcome, "critical": critical}


class EvalArtifactIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.datasets = ("dev220",)
        self.conditions = ("ft", "blend50", "blend60", "blend70")
        self.seeds = ("1", "2")
        self.rows = [row(0, "amount", "amount", "correct"),
                     row(1, "quantity", "unknown", "unknown"),
                     row(2, "date", "id", "wrong", True),
                     row(3, "other", "unknown", "other_ok"),
                     row(4, "other", "amount", "other_ng")]
        self.write_matrix()

    def tearDown(self):
        self.temp.cleanup()

    def write_matrix(self):
        for seed in self.seeds:
            for condition in self.conditions:
                job = f"job{seed}"
                base = {"schema_version": 3, "dataset": "dev220", "seed": seed,
                        "condition_id": condition}
                probs = dict(base, rows=self.rows)
                errors = dict(base, errors=[r for r in self.rows if r["outcome"] in ("wrong", "unknown", "other_ng")])
                (self.root / f"{job}_probs_dev220_{condition}.json").write_text(json.dumps(probs), encoding="utf-8")
                (self.root / f"{job}_errors_dev220_{condition}.json").write_text(json.dumps(errors), encoding="utf-8")

    def test_complete_matrix_and_counts(self):
        result = validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)
        self.assertEqual(result["reports"], 8)
        self.assertEqual(result["rows"], 40)
        self.assertEqual(result["paired_error_files"], 8)
        self.assertEqual(result["unique_dataset_rows"], 5)

    def test_missing_condition_is_detected(self):
        (self.root / "job2_probs_dev220_blend60.json").unlink()
        with self.assertRaisesRegex(ValueError, "report matrix mismatch"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)

    def test_duplicate_report_is_detected(self):
        source = self.root / "job1_probs_dev220_ft.json"
        (self.root / "job2_probs_dev220_ft.json").write_text(source.read_text(), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "job/seed mismatch"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)

    def test_duplicate_row_is_detected(self):
        path = self.root / "job1_probs_dev220_ft.json"
        obj = json.loads(path.read_text())
        obj["rows"].append(obj["rows"][0])
        path.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate row index"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)

    def test_error_list_must_match_predictions(self):
        path = self.root / "job1_errors_dev220_ft.json"
        obj = json.loads(path.read_text())
        obj["errors"].pop()
        path.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "errors/probs rows differ"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)

    def test_missing_error_file_is_detected(self):
        (self.root / "job1_errors_dev220_ft.json").unlink()
        with self.assertRaisesRegex(ValueError, "missing paired error report"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)

    def test_outcome_and_critical_semantics_are_checked(self):
        path = self.root / "job1_probs_dev220_ft.json"
        obj = json.loads(path.read_text())
        obj["rows"][2]["critical"] = False
        obj["rows"][0]["outcome"] = "wrong"
        path.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "outcome/label mismatch"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)

    def test_truth_mapping_must_match_across_conditions(self):
        path = self.root / "job2_probs_dev220_blend60.json"
        obj = json.loads(path.read_text())
        obj["rows"][0]["truth"] = "quantity"
        obj["rows"][0]["outcome"] = "wrong"
        path.write_text(json.dumps(obj), encoding="utf-8")
        errors_path = self.root / "job2_errors_dev220_blend60.json"
        errors = json.loads(errors_path.read_text())
        errors["errors"].append(row(0, "quantity", "amount", "wrong"))
        errors_path.write_text(json.dumps(errors), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "row identity/truth differs"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)


if __name__ == "__main__":
    unittest.main()
