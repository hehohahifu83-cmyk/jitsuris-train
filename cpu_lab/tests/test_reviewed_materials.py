import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "cpu_lab"))
from self_learning import load_approved_replay

MATERIALS = ROOT / "cpu_lab" / "materials" / "reviewed_replay.jsonl"
LABELS = {"date", "amount", "quantity", "rate", "id", "org", "person",
          "product", "account", "tax_class", "category", "text", "email",
          "phone", "address", "other"}
EXCLUDED_AMBIGUOUS_IDS = {
    "synthetic-unlabeled-008", "synthetic-unlabeled-012",
    "synthetic-unlabeled-013", "synthetic-unlabeled-025",
    "synthetic-unlabeled-026", "synthetic-unlabeled-030",
    "synthetic-unlabeled-034", "synthetic-unlabeled-036",
}


class AuditedMaterialTests(unittest.TestCase):
    def test_only_audited_materials_with_known_taxonomy_are_trainable(self):
        rows = [json.loads(line) for line in MATERIALS.read_text(encoding="utf-8").splitlines() if line]
        self.assertEqual(len(rows), 28)
        self.assertTrue(all(r["id"] not in EXCLUDED_AMBIGUOUS_IDS for r in rows))
        self.assertTrue(all(r.get("audit_confidence") in {"high", "medium"} for r in rows))
        tuples = load_approved_replay(str(MATERIALS), LABELS)
        self.assertEqual(len(tuples), len(rows))
        self.assertTrue(all(t[2] in LABELS for t in tuples))

    def test_ambiguous_candidates_are_not_promoted_into_replay(self):
        rows = [json.loads(line) for line in MATERIALS.read_text(encoding="utf-8").splitlines() if line]
        ids = {r["id"] for r in rows}
        self.assertTrue(EXCLUDED_AMBIGUOUS_IDS.isdisjoint(ids))


if __name__ == "__main__":
    unittest.main()
