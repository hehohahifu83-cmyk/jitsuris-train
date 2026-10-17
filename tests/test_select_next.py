import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import select_next


class SelectNextTest(unittest.TestCase):
    def test_count_unique_and_only_corpus_inputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            materials = Path(tmp) / "materials"
            materials.mkdir()
            rows = []
            for i in range(240):
                rows.append({"source": f"src{i % 4}", "table": f"t{i}", "header": f"h{i}",
                             "values": [str(i), "sample", "v3"], "context": []})
            (materials / "real_corpus_sample.jsonl").write_text(
                "\n".join(json.dumps(r) for r in rows), encoding="utf-8")
            # This sentinel must not be opened; file discovery is corpus-only.
            (materials / "blind_set7.py").write_text("raise AssertionError('read blind set')", encoding="utf-8")
            candidates = select_next.load_candidates(materials)
            self.assertEqual(len(candidates), 240)
            self.assertEqual([p.name for p in select_next.discover_files(materials)], ["real_corpus_sample.jsonl"])
            classes = ["amount", "id", "date", "org", "account", "tax_class", "person", "product", "email", "phone"]
            probabilities = []
            for i in range(len(candidates)):
                row = [0.01] * len(classes)
                row[i % len(classes)] = 0.3 + (i % 7) / 20
                row[(i + 1) % len(classes)] = 0.25
                probabilities.append(row)
            selected = select_next.select_candidates(candidates, probabilities, classes, count=200, seed=3)
            self.assertEqual(len(selected), 200)
            keys = [(x["source"], x["table"], x["header"], tuple(x["values"])) for x in selected]
            self.assertEqual(len(keys), len(set(keys)))
            out = materials / "next_batch.txt"
            select_next.write_batch(selected, out)
            self.assertEqual(len(out.read_text(encoding="utf-8").splitlines()), 200)


if __name__ == "__main__":
    unittest.main()
