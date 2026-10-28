import gzip
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from encoder_context import TITLE_SEP, format_encoder_text  # noqa: E402

TRAIN = ROOT / "materials" / "model_corpora" / "silver" / "train_A.jsonl.gz"
LABELS = {"date", "amount", "quantity", "rate", "id", "org", "product", "account", "tax_class", "text", "category", "email", "phone",
          "address", "other"}


class SilverTrainFileTests(unittest.TestCase):
    """C3b の 1 段目の教材（silver.py train、2026-10-29）。finetune_exp.py の FT_SILVER が読む形と同じか。"""

    @classmethod
    def setUpClass(cls):
        with gzip.open(TRAIN, "rt", encoding="utf-8") as f:
            cls.rows = [json.loads(l) for l in f if l.strip()]

    def test_fields_and_labels(self):
        self.assertGreater(len(self.rows), 10000)
        for d in self.rows:
            self.assertTrue({"header", "values", "label", "context", "table", "title"} <= set(d))
            self.assertIn(d["label"], LABELS)          # person・unknown・S は入れない
            self.assertIsInstance(d["values"], list)
            self.assertTrue(d["header"])               # 見出しのない SOTAB の列は決まった語

    def test_label_cap(self):
        from collections import Counter
        c = Counter(d["label"] for d in self.rows)
        self.assertLessEqual(max(c.values()), 4000 * 1.05)

    def test_text_matches_gold_format_with_title(self):
        d = next(d for d in self.rows if d["title"])
        row = (d["header"], d["values"], d["label"], d["context"], TITLE_SEP + d["title"])
        t = format_encoder_text(row, "query: ", ctx_unit=True, title=True)
        self.assertTrue(t.startswith(f"query: 列名: {d['header']} | 値: "))
        self.assertIn(f" | 表の題名: {d['title'][:40]}", t)
        self.assertNotIn("同じ表の単位列の値", t)    # 題名だけで単位の列は無い

    def test_no_overlap_with_gold_tables(self):
        self.assertTrue(all(d["table"].startswith(("sotab_v2:", "wikidbs10k:")) for d in self.rows))


if __name__ == "__main__":
    unittest.main()
