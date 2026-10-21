import contextlib
import io
import json
import os
import tempfile
import unittest

import data_inventory as D


def row(source, table, header, values, label):
    return {"source": source, "table": table, "header": header, "values": values, "label": label}


ROWS = [
    row("egov:a", "t1", "金額", ["1,000", "2,000"], "amount"),
    row("egov:a", "t1", "日付", ["2024-01-01"], "date"),
    row("egov:b", "t2", "金額", ["5"], "amount"),
    row("gittables:x", "t3", "amount", ["1", "2"], "amount"),
    row("gittables:x", "t3", "note", ["", ""], "S"),          # 数えない
    row("gittables:x", "t3", "memo", ["a"], "unknown"),       # 数えない
    row("canada:z", "t4", "Value", ["10"], "quantity"),
]


class InventoryTests(unittest.TestCase):
    def test_counts_and_skips(self):
        inv = D.inventory(ROWS)
        self.assertEqual(inv["skipped"], 2)
        self.assertEqual(inv["total"], 5)
        a = inv["classes"]["amount"]
        self.assertEqual((a["columns"], a["tables"], a["datasets"], a["families"]), (3, 3, 3, 2))
        self.assertEqual(a["top_family"], "egov")
        self.assertAlmostEqual(a["top_family_share"], 2 / 3)
        self.assertEqual((a["ja_columns"], a["ja_tables"]), (2, 2))     # 見出しが日本語の 2 列（egov:a と egov:b）
        self.assertEqual(inv["classes"]["person"]["columns"], 0)
        self.assertEqual(inv["total_ja"], 3)                              # 金額（2 列）＋日付

    def test_japanese_detection_looks_at_header_and_values(self):
        self.assertTrue(D.has_japanese(row("s", "t", "x", ["東京"], "text")))
        self.assertTrue(D.has_japanese(row("s", "t", "金額", ["1"], "amount")))
        self.assertFalse(D.has_japanese(row("s", "t", "amount", ["1"], "amount")))

    def test_family(self):
        self.assertEqual(D.family_of("egov_biz:cc4e"), "egov_biz")
        self.assertEqual(D.family_of("plain"), "plain")
        self.assertEqual(D.family_of(None), "(なし)")

    def test_gaps_use_overrides_and_flag_family_share(self):
        inv = D.inventory(ROWS)
        targets = {"per_class": {"min_tables": 2, "min_ja_tables": 0, "min_datasets": 0, "max_family_share": 0.5}, "overrides": {"quantity": {"min_tables": 1, "max_family_share": 1.0}}}
        g = D.gaps(inv, targets)
        self.assertEqual(g["quantity"], [])                                # 上書きで 1 表あれば足りる
        self.assertTrue(any("表 1/2" in m for m in g["date"]))
        self.assertTrue(any("系統 egov" in m for m in g["amount"]))        # egov が 2/3 > 50%
        self.assertEqual(g["person"][0], "表 0/2")

    def test_render_and_main(self):
        with tempfile.TemporaryDirectory() as d:
            pattern = os.path.join(d, "real_labels_x.jsonl")
            with open(pattern, "w", encoding="utf-8") as fh:
                for r in ROWS:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            targets = os.path.join(d, "t.json")
            with open(targets, "w", encoding="utf-8") as fh:
                json.dump({"per_class": {"min_tables": 1}}, fh)
            out = os.path.join(d, "out.md")
            with contextlib.redirect_stdout(io.StringIO()):
                D.main(["--pattern", pattern, "--targets", targets, "--out", out])
            text = open(out, encoding="utf-8").read()
            self.assertIn("| amount | 3 | 3 | 3 | 2 | egov（67%） | 2 | 2 |", text)
            self.assertIn("日本語を含む列 3 列", text)
            self.assertIn("表 0/1", text)                                  # person などは足りない

    def test_empty_input_stops(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(SystemExit):
                D.main(["--pattern", os.path.join(d, "none*.jsonl"), "--out", os.path.join(d, "o.md")])


if __name__ == "__main__":
    unittest.main()
