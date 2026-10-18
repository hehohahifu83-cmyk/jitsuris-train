import json
import tempfile
import unittest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from self_learning import _check_pool, approve, load_approved_replay


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
