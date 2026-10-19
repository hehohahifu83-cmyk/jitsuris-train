import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from evaluation_records import (
    assert_metrics_match,
    build_record,
    classify_outcome,
    summarize_records,
)
from llm_baseline import score_real


def rec(i, truth, guarded, raw=None):
    top3 = [] if raw is None else [{"label": raw, "probability": 0.7}]
    return build_record(
        index=i, dataset="business", seed=1, condition="ft", column=f"c{i}",
        truth=truth, guarded_prediction=guarded, top3=top3,
    )


class EvaluationRecordsTest(unittest.TestCase):
    def test_other_unknown_is_not_counted_as_unknown(self):
        self.assertEqual(classify_outcome("other", "unknown"), "other_ok")
        self.assertEqual(classify_outcome("other", "id"), "other_ng")
        self.assertEqual(classify_outcome("amount", "unknown"), "unknown")

    def test_raw_and_guarded_labels_are_distinct(self):
        row = rec(0, "amount", "unknown", raw="quantity")
        self.assertEqual(row["raw_prediction"], "quantity")
        self.assertEqual(row["guarded_prediction"], "unknown")
        self.assertEqual(row["prediction"], "unknown")
        self.assertEqual(row["outcome"], "unknown")

    def test_records_recompute_official_score_exactly(self):
        truth = ["amount", "quantity", "org", "other", "other", "date"]
        pred = ["quantity", "unknown", "org", "unknown", "id", "id"]
        official = score_real(pred, truth)
        rows = [rec(i, t, p, raw=p) for i, (t, p) in enumerate(zip(truth, pred))]
        assert_metrics_match(rows, official)
        metrics = summarize_records(rows)
        self.assertEqual(metrics["wrong"], 2)
        self.assertEqual(metrics["unknown"], 1)
        self.assertEqual(metrics["critical"], 1)
        self.assertEqual(metrics["other_ok"], 1)
        self.assertEqual(metrics["other_ng"], 1)

    def test_outcome_field_mismatch_is_not_silently_accepted(self):
        row = rec(0, "other", "unknown", raw="other")
        row["outcome"] = "unknown"
        self.assertEqual(summarize_records([row])["unknown"], 1)  # summarizer consumes declared outcomes
        with self.assertRaises(AssertionError):
            assert_metrics_match([row], score_real(["unknown"], ["other"]))


if __name__ == "__main__":
    unittest.main()
