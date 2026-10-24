import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "materials"))
import label_sheets as S  # noqa: E402


def row(table, header, values, context=()):
    return {"table": table, "header": header, "values": list(values), "context": list(context), "unit": ""}


class LabelSheetTests(unittest.TestCase):
    def setUp(self):
        self.corpus = [
            row("t1", "全国地方公共団体コード", ["252123", "252123"]),
            row("t1", "人口", ["120", "3400"]),
            row("t2", "全国地方公共団体コード", ["262056", "262056"]),   # 同じ見出し・同じ形（数字の並び）→ 同じグループ
            row("t2", "人口", ["12.5%", "3.1%"]),             # 同じ見出しでも値の形が違う → 別のグループ
            row("t3", "備考", ["", ""]),
        ]
        self.groups = S.make_groups(self.corpus)
        for g in self.groups:
            g["sheet"] = 1

    def test_groups_by_header_and_value_shape(self):
        self.assertEqual([g["rows"] for g in self.groups], [[0, 2], [1], [3], [4]])
        # 漢字・かなの値は文字のまま比べる（施設の名称のように中身で種類が分かれる列をまとめない）
        other = S.make_groups([row("a", "名称", ["中央公民館"]), row("b", "名称", ["中央公園"])])
        self.assertEqual(len(other), 2)
        self.assertEqual([g["group"] for g in self.groups], ["g0001", "g0002", "g0003", "g0004"])

    def test_answers_are_checked_and_merged_to_every_row(self):
        d = Path(tempfile.mkdtemp())
        (d / "answers").mkdir()
        (d / "answers" / "sheet_001.tsv").write_text("```\ng0001\taddress\ng0002\tquantity\ng0003\trate\ng0004\t\n```\n", encoding="utf-8")
        got, problems = S.read_answers(d, self.groups)
        self.assertEqual(problems, [])
        with self.assertRaisesRegex(ValueError, "答えの無いグループ 1 件"):
            S.merge(self.corpus, self.groups, got)
        (d / "answers" / "sheet_001.tsv").write_text("g0001\taddress\ng0002\tquantity\ng0003\trate\ng0004\tS\n", encoding="utf-8")
        got, _ = S.read_answers(d, self.groups)
        labels = S.merge(self.corpus, self.groups, got)
        self.assertEqual([x["label"] for x in labels], ["address", "quantity", "address", "rate", "S"])
        self.assertEqual([x["header"] for x in labels], [r["header"] for r in self.corpus])

    def test_bad_answers_are_reported(self):
        d = Path(tempfile.mkdtemp())
        (d / "answers").mkdir()
        (d / "answers" / "sheet_001.tsv").write_text("g0001\tadres\ng0009\tdate\ng0002 quantity\ng0003\trate\ng0003\tquantity\n", encoding="utf-8")
        _, problems = S.read_answers(d, self.groups)
        text = "\n".join(problems)
        self.assertIn("決まりにない", text)
        self.assertIn("知らないグループ g0009", text)
        self.assertIn("形が", text)
        self.assertIn("違うラベルが 2 つ", text)

    def test_sheet_has_answer_template(self):
        md = S.render_sheet(1, self.groups, self.corpus, 1, "v1.8")
        self.assertIn("## g0001（2 列）", md)
        self.assertIn("g0004\t\n", md)
        self.assertIn("LABEL_GUIDE v1.8", md)


if __name__ == "__main__":
    unittest.main()
