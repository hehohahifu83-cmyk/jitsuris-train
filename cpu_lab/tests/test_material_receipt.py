import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from material_receipt import mark_trained, prepare_reviewed


def reviewed_row():
    return {
        "id": "synthetic-reviewed-001",
        "header": "請求金額",
        "values": ["1200", "850"],
        "context": ["請求番号"],
        "unit_context": "JPY",
        "label": "amount",
        "source": "synthetic:cpu-lab-contrast-v1",
        "license": "generated-internal; no external source",
        "split": "train",
        "privacy_checked": True,
        "reviewer": "codex-audit-test",
        "verified": True,
        "audit_confidence": "high",
    }


class MaterialReceiptTests(unittest.TestCase):
    def test_receipt_tracks_audited_material_and_successful_training_exposure(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            materials = root / "materials.jsonl"
            receipt_before = root / "receipt-before.json"
            receipt_after = root / "receipt-after.json"
            log = root / "train.log"
            materials.write_text(json.dumps(reviewed_row(), ensure_ascii=False) + "\\n", encoding="utf-8")
            receipt = prepare_reviewed(materials, "run:123/ft_out_job1", receipt_before)
            self.assertEqual(receipt["material_count"], 1)
            self.assertEqual(receipt["items"][0]["training_status"], "not_yet_run")
            log.write_text("CPU lab replay: 1 audited rows from materials.jsonl\\n", encoding="utf-8")
            result = mark_trained(receipt_before, log, 1, receipt_after)
            self.assertEqual(result["seed_runs"][0]["rows_confirmed"], 1)
            self.assertEqual(result["items"][0]["training_status"], "included_in_training")

    def test_receipt_refuses_unreviewed_material(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            materials = root / "materials.jsonl"
            row = reviewed_row()
            row["verified"] = False
            materials.write_text(json.dumps(row, ensure_ascii=False) + "\\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                prepare_reviewed(materials, "run:123/ft_out_job1", root / "receipt.json")


if __name__ == "__main__":
    unittest.main()
