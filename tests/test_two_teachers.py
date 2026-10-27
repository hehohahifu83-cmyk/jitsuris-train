"""ChatGPT と Grok の 2 人の先生で突き合わせる（2026-10-28）。"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "materials"))
import label_sheets as LS  # noqa: E402
import pipeline as P  # noqa: E402


class TwoTeachersTest(unittest.TestCase):
    def test_answers_are_read_from_each_teachers_own_folder(self):
        groups = [{"group": "g0001", "sheet": 1, "rows": [0]}, {"group": "g0002", "sheet": 1, "rows": [1]}]
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            (d / "answers").mkdir()
            (d / "answers_grok").mkdir()
            (d / "answers" / "sheet_001.tsv").write_text("g0001\tdate\ng0002\tid\n", encoding="utf-8")
            (d / "answers_grok" / "sheet_001.tsv").write_text("g0001\tdate\ng0002\tquantity\n", encoding="utf-8")
            self.assertEqual(LS.read_answers(d, groups)[0], {"g0001": "date", "g0002": "id"})
            self.assertEqual(LS.read_answers(d, groups, "grok")[0], {"g0001": "date", "g0002": "quantity"})

    def test_grok_labels_take_the_place_of_model_predictions(self):
        with tempfile.TemporaryDirectory() as td:
            w = Path(td)
            (w / "labels_grok.jsonl").write_text("".join(json.dumps({"label": x}) + "\n" for x in ("date", "id")), encoding="utf-8")
            self.assertEqual([p["guarded_prediction"] for p in P.load_preds(w, "grok")], ["date", "id"])

    def test_agreed_rows_record_both_teachers(self):
        corpus = [{"table": "t", "header": "h", "publisher": "p"}]
        labels = [{"label": "date"}]
        out, _, _, _ = P.finalize(corpus, labels, [{"guarded_prediction": "date"}], [], [], "b999", "ChatGPT", "grok")
        self.assertEqual(out[0]["teacher"], "ChatGPT+grok-agree")


if __name__ == "__main__":
    unittest.main()
