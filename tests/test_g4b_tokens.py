"""G4b の切り詰めの数え（research/g4b/g4b_tokens.py）の区間の作り方の試験（2026-11-26 Claude、Codex の点検 3）。トークナイザーは使わない。"""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [ROOT, os.path.join(ROOT, "research", "g4b")]
import encoder_context as ec  # noqa: E402
import g4b_tokens as T  # noqa: E402

INFO = {"prefix": "query: ", "ctx_unit": True}


class BoundaryTest(unittest.TestCase):
    def test_delimiters_inside_values(self):
        ctx = {"headers": ["A / x", "B | 同じ表の列: y", "Alberta"], "rows": [["v / 1", " | 同じ表の列: z", "9"], ["w", "q", "8"]]}
        unit = "Unit: USD / | 同じ表の列: x" + ec.TITLE_SEP + "題名 / | 同じ行: x"
        row = ("Alberta", ["1 / 2", " | 同じ表の列: 3"], "", ["A / x", "B | 同じ表の列: y"], ec.with_row_context(unit, ctx, "Alberta"))
        t = ec.format_encoder_text(row, "query: ", ctx_unit=True, title=True, row_ctx=True)
        b = T.row_ends(T.boundaries(row, INFO), ctx, "Alberta")
        self.assertEqual(b["text"], t)
        self.assertTrue(t[:b["row1_end"]].endswith("B | 同じ表の列: y=| 同じ表の列: z"))
        self.assertTrue(t[:b["row2_end"]].endswith("B | 同じ表の列: y=q"))
        self.assertTrue(t[:b["siblings_end"]].endswith(" | 同じ表の列: A / x, B | 同じ表の列: y"))
        self.assertEqual(b["unit_end"], len(t))
        self.assertEqual(t[b["row1_end"]:b["row1_end"] + 3], " / ")

    def test_without_row_context_and_unit(self):
        row = ("A", ["1"], "", ["B"], "")
        t = ec.format_encoder_text(row, "query: ", ctx_unit=True, title=True)
        b = T.boundaries(row, INFO)
        self.assertEqual(b["text"], t)
        self.assertIsNone(b["row1_end"])
        self.assertIsNone(b["unit_end"])
        self.assertEqual(b["siblings_end"], len(t))

    def test_mismatch_is_refused(self):
        ctx = {"headers": ["A", "B"], "rows": [["1", "2"]]}
        row = ("A", ["1"], "", ["B"], ec.with_row_context("", ctx, "A"))
        b = T.boundaries(row, INFO)
        with self.assertRaises(SystemExit):
            T.row_ends(b, {"headers": ["A", "B"], "rows": [["1", "3"]]}, "A")


if __name__ == "__main__":
    unittest.main()
