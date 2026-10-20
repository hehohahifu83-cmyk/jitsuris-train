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
                rows = [dict(r, dataset="dev220", seed=seed, condition=condition) for r in self.rows]
                probs = dict(base, rows=rows)
                errors = dict(base, errors=[r for r in rows if r["outcome"] in ("wrong", "unknown", "other_ng")])
                (self.root / f"{job}_probs_dev220_{condition}.json").write_text(json.dumps(probs), encoding="utf-8")
                (self.root / f"{job}_errors_dev220_{condition}.json").write_text(json.dumps(errors), encoding="utf-8")

    def test_complete_matrix_and_counts(self):
        result = validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)
        self.assertEqual(result["reports"], 8)
        self.assertEqual(result["rows"], 40)
        self.assertEqual(result["paired_error_files"], 8)
        self.assertEqual(result["unique_dataset_rows"], 5)

    def test_row_metadata_is_checked(self):
        path = self.root / "job1_probs_dev220_ft.json"
        obj = json.loads(path.read_text())
        obj["rows"][0]["condition"] = "blend50"
        path.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "row metadata mismatch"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)

    def test_missing_condition_is_detected(self):
        (self.root / "job2_probs_dev220_blend60.json").unlink()
        with self.assertRaisesRegex(ValueError, "report matrix mismatch"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)

    def test_job_seed_mapping_is_checked(self):
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

    def test_outcome_semantics_are_checked(self):
        path = self.root / "job1_probs_dev220_ft.json"
        obj = json.loads(path.read_text())
        obj["rows"][0]["outcome"] = "wrong"
        path.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "outcome/label mismatch"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)

    def test_critical_requires_numeric_to_numeric_misclassification(self):
        path = self.root / "job1_probs_dev220_ft.json"
        obj = json.loads(path.read_text())
        obj["rows"][2]["critical"] = False
        path.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "critical flag/labels mismatch"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)

    def test_truth_mapping_must_match_across_conditions(self):
        path = self.root / "job2_probs_dev220_blend60.json"
        obj = json.loads(path.read_text())
        obj["rows"][0]["truth"] = "quantity"
        obj["rows"][0]["outcome"] = "wrong"
        obj["rows"][0]["critical"] = True
        path.write_text(json.dumps(obj), encoding="utf-8")
        errors_path = self.root / "job2_errors_dev220_blend60.json"
        errors = json.loads(errors_path.read_text())
        errors["errors"].append(dict(row(0, "quantity", "amount", "wrong", True), dataset="dev220", seed="2", condition="blend60"))
        errors_path.write_text(json.dumps(errors), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "row identity/truth differs"):
            validate_report_dir(self.root, datasets=self.datasets, seeds=self.seeds, conditions=self.conditions)


class GenericLayoutTests(unittest.TestCase):
    """2026-10-20：仕事の数・種子・試験の名前が従来の対の設計に限られない実行（学習率の探索・検証モード・3 種子の比較）。"""

    CONDITIONS = ("sparse", "ft", "blend50", "blend60", "blend70")

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.rows = [row(0, "amount", "amount", "correct"),
                     row(1, "quantity", "unknown", "unknown"),
                     row(2, "date", "id", "wrong", True),
                     row(3, "other", "unknown", "other_ok")]

    def tearDown(self):
        self.temp.cleanup()

    def write(self, job, dataset, seed, conditions=None):
        for condition in conditions or self.CONDITIONS:
            base = {"schema_version": 3, "dataset": dataset, "seed": seed, "condition_id": condition}
            rows = [dict(r, dataset=dataset, seed=seed, condition=condition) for r in self.rows]
            (self.root / f"{job}_probs_{dataset}_{condition}.json").write_text(json.dumps(dict(base, rows=rows)), encoding="utf-8")
            errors = [r for r in rows if r["outcome"] in ("wrong", "unknown", "other_ng")]
            (self.root / f"{job}_errors_{dataset}_{condition}.json").write_text(json.dumps(dict(base, errors=errors)), encoding="utf-8")

    def test_three_jobs_with_the_same_seed_and_validation_names(self):
        for job in ("job1", "job2", "job3"):
            for ds in ("val_general", "val_japan_procurement"):
                self.write(job, ds, "1")
        result = validate_report_dir(self.root, layout="generic")
        self.assertEqual(result["layout"], "generic")
        self.assertEqual(result["reports"], 3 * 2 * 5)
        with self.assertRaisesRegex(ValueError, "report matrix mismatch"):   # 従来の対の設計としては合わない
            validate_report_dir(self.root, layout="paired")

    def test_job3_with_seed_3_is_accepted(self):
        self.write("job3", "general", "3")
        self.assertEqual(validate_report_dir(self.root, layout="generic")["reports"], 5)

    def test_single_job_report_directory_name(self):
        self.write("report", "business", "default")
        self.assertEqual(validate_report_dir(self.root, layout="generic")["reports"], 5)

    def test_missing_condition_in_generic_is_detected(self):
        self.write("job1", "general", "1", conditions=("ft", "blend50", "blend60", "blend70"))
        with self.assertRaisesRegex(ValueError, "report matrix mismatch"):
            validate_report_dir(self.root, layout="generic")

    def test_empty_directory_fails_in_generic(self):
        with self.assertRaisesRegex(ValueError, "no probs report"):
            validate_report_dir(self.root, layout="generic")

    def test_per_file_checks_still_apply_in_generic(self):
        self.write("job1", "general", "1")
        path = self.root / "job1_probs_general_ft.json"
        obj = json.loads(path.read_text())
        obj["rows"][2]["critical"] = False      # 重大の印が結果と合わない
        path.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "critical flag/labels mismatch"):
            validate_report_dir(self.root, layout="generic")

    def test_auto_chooses_paired_only_for_the_classic_design(self):
        from cpu_lab.eval_artifact_integrity import detect_layout
        self.assertEqual(detect_layout(self.root), "generic")
        self.write("job1", "dev220", "1")
        self.write("job2", "dev220", "2")
        self.assertEqual(detect_layout(self.root), "paired")
        self.write("job2", "dev220", "3")      # 仕事2 の種子が 2 でないなら対の設計ではない
        self.assertEqual(detect_layout(self.root), "generic")


if __name__ == "__main__":
    unittest.main()
