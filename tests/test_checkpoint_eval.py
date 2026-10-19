import tempfile
import unittest
from pathlib import Path

from evaluate_checkpoint import compare_rows, find_checkpoint


class CheckpointEvaluationTests(unittest.TestCase):
    def test_rowwise_parity_allows_rounding_noise(self):
        prior = [{"truth": "date", "prediction": "date", "column": "posted date",
                  "top3": [{"label": "date", "probability": 0.900001},
                           {"label": "amount", "probability": 0.05}]}]
        current = [{"truth": "date", "guarded_prediction": "date", "column": "posted date",
                    "top3": [{"label": "date", "probability": 0.9},
                             {"label": "amount", "probability": 0.05}]}]
        self.assertTrue(compare_rows(prior, current)["passed"])

    def test_lower_rank_ties_do_not_fail_when_top1_and_probabilities_match(self):
        prior = [{"truth": "date", "prediction": "date", "column": "posted date",
                  "top3": [{"label": "date", "probability": 0.9},
                           {"label": "amount", "probability": 0.0501},
                           {"label": "quantity", "probability": 0.05}]}]
        tied = [{"truth": "date", "prediction": "date", "column": "posted date",
                 "top3": [{"label": "date", "probability": 0.9},
                          {"label": "quantity", "probability": 0.05},
                          {"label": "amount", "probability": 0.0501}]}]
        self.assertTrue(compare_rows(prior, tied)["passed"])
        changed = [{"truth": "date", "prediction": "date", "column": "posted date",
                    "top3": [{"label": "amount", "probability": 0.9},
                             {"label": "quantity", "probability": 0.05},
                             {"label": "date", "probability": 0.0501}]}]
        self.assertFalse(compare_rows(prior, changed)["passed"])
        drift = [{"truth": "date", "prediction": "date", "column": "posted date",
                  "top3": [{"label": "date", "probability": 0.89},
                           {"label": "amount", "probability": 0.05},
                           {"label": "quantity", "probability": 0.04}]}]
        self.assertFalse(compare_rows(prior, drift)["passed"])

    def test_checkpoint_discovery_requires_exactly_one_complete_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            model = Path(tmp) / "ft_out_job1"
            model.mkdir()
            for name in ("labels.json", "config.json", "model.safetensors"):
                (model / name).touch()
            self.assertEqual(find_checkpoint(tmp), model)
            other = Path(tmp) / "ft_out_job2"
            other.mkdir()
            for name in ("labels.json", "config.json", "model.safetensors"):
                (other / name).touch()
            with self.assertRaises(RuntimeError):
                find_checkpoint(tmp)


if __name__ == "__main__":
    unittest.main()
