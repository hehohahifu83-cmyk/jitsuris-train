import json
import tempfile
import unittest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from self_learning import _check_pool, approve, load_approved_replay, load_pseudo_replay, pseudo_label_decision


def pool_row(id="public:1"):
    return {"id": id, "header": "amount", "values": ["3", "8"], "context": ["currency"],
            "source": "synthetic:fixture", "license": "CC0", "split": "unlabeled", "privacy_checked": True}


class ActiveLearningSafetyTests(unittest.TestCase):
    def test_fixed_eval_files_rejected(self):
        with self.assertRaises(ValueError):
            _check_pool(Path("blind_set1.jsonl"), [pool_row()])
        with self.assertRaises(ValueError):
            _check_pool(Path("pool.jsonl"), [{**pool_row(), "source": "set7"}])

    def test_unverified_labels_never_exported(self):
        with tempfile.TemporaryDirectory() as d:
            reviewed, out = Path(d) / "reviewed.jsonl", Path(d) / "replay.jsonl"
            item = {"row": pool_row(), "review": {"status": "pending", "label": "amount", "reviewer": "", "verified": False}}
            reviewed.write_text(json.dumps(item) + "\n", encoding="utf-8")
            from argparse import Namespace
            with self.assertRaises(ValueError):
                approve(Namespace(reviewed=str(reviewed), out=str(out)))

    def test_only_verified_rows_reach_training(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "approved.jsonl"
            row = pool_row()
            row.update(label="amount", split="train", reviewer="reviewer-1", verified=True)
            p.write_text(json.dumps(row) + "\n", encoding="utf-8")
            result = load_approved_replay(str(p), {"amount", "date"})
            self.assertEqual(result[0][:3], ("amount", ["3", "8"], "amount"))
            with self.assertRaises(ValueError):
                load_approved_replay(str(p), {"date"})

    def test_three_view_pseudolabel_gate_accepts_only_strong_agreement(self):
        strong = [[0.999, 0.001], [0.998, 0.002], [0.997, 0.003]]
        result = pseudo_label_decision(strong, ["amount", "date"])
        self.assertEqual(result["label"], "amount")
        self.assertEqual(result["agreement"], 3)
        self.assertIsNone(pseudo_label_decision([strong[0], strong[1], [0.001, 0.999]], ["amount", "date"]))
        self.assertIsNone(pseudo_label_decision([[0.8, 0.2]] * 3, ["amount", "date"]))

    def test_machine_pseudo_rows_are_separate_and_capped(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "pseudo.jsonl"
            row = pool_row()
            row.update(label="amount", split="train", verified=False)
            row["pseudo_label"] = {
                "method": "same-model-three-value-orders-v1", "label": "amount",
                "confidence_min": 0.997, "margin_min": 0.994, "agreement": 3,
                "views": ["amount", "amount", "amount"],
            }
            p.write_text(json.dumps(row) + "\n", encoding="utf-8")
            loaded = load_pseudo_replay(str(p), {"amount", "date"}, base_rows=100)
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0][2], "amount")
            second = dict(row)
            second["id"] = "public:2"
            p.write_text(json.dumps(row) + "\n" + json.dumps(second) + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_pseudo_replay(str(p), {"amount"}, base_rows=100)
            row["pseudo_label"]["confidence_min"] = 0.9
            p.write_text(json.dumps(row) + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_pseudo_replay(str(p), {"amount"}, base_rows=100)

    def test_approve_exports_explicit_human_review(self):
        with tempfile.TemporaryDirectory() as d:
            reviewed, out = Path(d) / "reviewed.jsonl", Path(d) / "approved.jsonl"
            item = {"row": pool_row(), "review": {"status": "approved", "label": "amount", "reviewer": "human-1", "verified": True}}
            reviewed.write_text(json.dumps(item) + "\n", encoding="utf-8")
            from argparse import Namespace
            approve(Namespace(reviewed=str(reviewed), out=str(out)))
            rows = load_approved_replay(str(out), {"amount"})
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0][2], "amount")


if __name__ == "__main__":
    unittest.main()
