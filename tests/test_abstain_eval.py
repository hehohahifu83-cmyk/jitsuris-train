import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import abstain_eval as ab
from evaluation_records import build_record


def row(truth, pred, p1):
    return build_record(index=0, dataset="test", seed=1, condition="blend70",
                        column="x", truth=truth, guarded_prediction=pred,
                        top3=[{"label": pred, "probability": p1}],
                        decision_reason="fixture_abstention" if pred == "unknown" else None)


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
                json.dump({"schema_version": 3, "test": name, "condition": "x", "rows": rows}, open(Path(d, f"probs_{name}_blend70.json"), "w"))
            tests = ab.load(d, "blend70")
            self.assertEqual(ab.smallest_safe_threshold(tests, ["a"]), 0.71)
            self.assertEqual(ab.smallest_safe_threshold(tests, ["a", "b"]), 0.81)
            text = ab.report(d, "blend70")
            self.assertIn("leave-one-test-out", text)
            self.assertIn("0.81", text)

    def test_legacy_schema_is_refused(self):
        with tempfile.TemporaryDirectory() as d:
            json.dump({"test": "t", "condition": "x", "rows": [row("id", "id", 0.99)]},
                      open(Path(d, "probs_t_blend70.json"), "w"))
            with self.assertRaisesRegex(ValueError, "schema_version=3"):
                ab.load(d, "blend70")

    def test_prediction_alias_mismatch_is_refused(self):
        item = row("amount", "amount", 0.9)
        item["prediction"] = "unknown"
        with tempfile.TemporaryDirectory() as d:
            json.dump({"schema_version": 3, "test": "t", "condition": "x", "rows": [item]},
                      open(Path(d, "probs_t_blend70.json"), "w"))
            with self.assertRaisesRegex(ValueError, "alias differs"):
                ab.load(d, "blend70")

    def test_blind_sets_are_refused(self):
        with tempfile.TemporaryDirectory() as d:
            json.dump({"test": "blind", "rows": []}, open(Path(d, "probs_blind_set7_blend70.json"), "w"))
            with self.assertRaises(RuntimeError):
                ab.load(d, "blend70")

    def test_kaggle_prefixed_names_and_multiple_runs(self):
        with tempfile.TemporaryDirectory() as d:
            for run, thr_row in (("job1", row("id", "amount", 0.8)), ("job2", row("id", "amount", 0.6))):
                json.dump({"schema_version": 3, "test": "t", "condition": "x", "rows": [thr_row, row("id", "id", 0.99)]}, open(Path(d, f"{run}_probs_t_blend70.json"), "w"))
            json.dump({"test": "t", "condition": "x", "rows": []}, open(Path(d, "job1_errors_t_blend70.json"), "w"))  # errors は読まない
            self.assertEqual(ab.runs(d, "blend70"), ["job1", "job2"])
            with self.assertRaises(ValueError):   # 置き場が複数あるのに指定しない → 取り違えを防いで止まる
                ab.load(d, "blend70")
            self.assertEqual(ab.smallest_safe_threshold(ab.load(d, "blend70", "job1"), ["t"]), 0.81)
            self.assertEqual(ab.smallest_safe_threshold(ab.load(d, "blend70", "job2"), ["t"]), 0.61)
            self.assertIn("0.61", ab.report(d, "blend70", "job2"))

    def test_single_prefixed_run_is_found_without_naming_it(self):
        with tempfile.TemporaryDirectory() as d:
            json.dump({"schema_version": 3, "test": "t", "condition": "x", "rows": [row("id", "id", 0.99)]}, open(Path(d, "report_probs_t_ft.json"), "w"))
            self.assertEqual(ab.runs(d, "ft"), ["report"])
            self.assertEqual(list(ab.load(d, "ft")), ["t"])
            self.assertEqual(ab.runs(d, "blend70"), [])


if __name__ == "__main__":
    unittest.main()
