"""方法 T1（FT_ROWCTX、同じ行のほかの列の値）の文の作り方の試験（2026-11-17 Claude）。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import encoder_context as ec  # noqa: E402


def col(h, vals, idx):
    return {"header": h, "row_values": vals, "row_index": idx}


T = "https://example.org/t.csv"
IDX = [3, 8, 15, 21]
COLS = [col("When", ["2010", "2011", "2012", "2013"], IDX), col("ValueType", ["Chained (2007) dollars"] * 4, IDX),
        col("Alberta", ["12002000000", "64839000000", "11865000000", "11429000000"], IDX)]


class RowContextTest(unittest.TestCase):
    def test_off_is_unchanged(self):
        row = ("Alberta", ["1", "2"], "", ["When", "ValueType"], "u" + ec.TITLE_SEP + "GDP")
        a = ec.format_encoder_text(row, "query: ", title=True)
        b = ec.format_encoder_text(row, "query: ", title=True, row_ctx=True)   # 文が付いていなければ同じ
        self.assertEqual(a, b)
        self.assertNotIn("同じ行", a)

    def test_deterministic_rows_same_for_all_columns(self):
        c1, w1 = ec.table_row_context(T, COLS)
        c2, _ = ec.table_row_context(T, list(COLS))
        self.assertIsNone(w1)
        self.assertEqual(c1, c2)
        self.assertEqual(len(c1["rows"]), ec.ROWCTX_ROWS)
        # 選んだ行は、どの列でも同じ元の行（When の値は行ごとに違うので、そこから位置が決まる）
        for r in c1["rows"]:
            p = COLS[0]["row_values"].index(r[0])
            self.assertEqual(r, [c["row_values"][p] for c in COLS])

    def test_excludes_self_and_renders(self):
        ctx, _ = ec.table_row_context(T, COLS)
        txt = ec.render_row_context(ctx, "Alberta")
        self.assertIn("ValueType=Chained (2007) dollars", txt)
        self.assertNotIn("Alberta=", txt)
        unit = ec.with_row_context("u" + ec.TITLE_SEP + "GDP", ctx, "Alberta")
        s = ec.format_encoder_text(("Alberta", ["1"], "", ["When"], unit), "", title=True, row_ctx=True)
        self.assertIn("表の題名: GDP | 同じ行: ", s)
        self.assertTrue(s.index("同じ行") < s.index("同じ表の列"))
        self.assertNotIn(ec.ROW_SEP, s)

    def test_not_aligned(self):
        bad = [col("A", ["1", "2"], [1, 2]), col("B", ["x", "y"], [1, 3])]
        self.assertEqual(ec.table_row_context(T, bad), (None, "列ごとに row_index が違う"))
        self.assertEqual(ec.table_row_context(T, [col("A", ["1"], [1]), col("A", ["2"], [1])])[1], "同じ列名が 2 つ以上")
        self.assertEqual(ec.table_row_context(T, [col("A", ["1"], [1, 2])])[1], "row_values と row_index の長さが違う")
        self.assertEqual(ec.table_row_context(T, [col("A", ["1", "2"], [1, 1])])[1], "同じ行番号の重複")
        self.assertEqual(ec.table_row_context(T, [col("A", [], [])])[1], "row_index が空の列がある")

    def test_limits(self):
        many = [col(f"c{i}", [f"v{i}" * 20] * 4, IDX) for i in range(15)]
        ctx, _ = ec.table_row_context(T, many)
        txt = ec.render_row_context(ctx, "c0")
        first = txt.split(" / ")[0].split("; ")
        self.assertEqual(len(first), ec.ROWCTX_MAX_COLS)
        self.assertTrue(all(len(x.split("=", 1)[1]) <= ec.ROWCTX_MAX_CELL for x in first))
        self.assertEqual(ec.render_row_context(None, "x"), "")
        self.assertEqual(ec.with_row_context("u", None, "x"), "u")

    def test_training_rows_use_original_header(self):
        ctx, _ = ec.table_row_context(T, COLS)
        rows = [("Alberta", ["1", "2"], "amount", ["When"], T)]
        out = ec.real_train_rows_with_units(rows, 2, 1, True, {}, lambda rng, h: h.upper(), rowctx_by_table={T: ctx})
        for r in out:
            self.assertEqual(r[0], "ALBERTA")
            self.assertIn(ec.ROW_SEP, r[4])
            self.assertNotIn("Alberta=", r[4])
        plain = ec.real_train_rows_with_units(rows, 2, 1, True, {}, lambda rng, h: h)
        self.assertTrue(all(ec.ROW_SEP not in r[4] for r in plain))


    def test_prediction_side_matches_training_text(self):
        import evaluate_independent as ev
        ctx, _ = ec.table_row_context(T, COLS)
        spec = {"version": ec.ROWCTX_VERSION, "rows": ec.ROWCTX_ROWS, "max_cols": ec.ROWCTX_MAX_COLS, "max_cell": ec.ROWCTX_MAX_CELL, "max_header": ec.ROWCTX_MAX_HEADER}
        info = {"row_ctx": True, "row_ctx_spec": spec, "prefix": "", "ctx_unit": False}
        set_data = {"columns": [{"header": "Alberta", "values": ["1"], "siblings": ["When"], "table": "t001"}], "row_context": {"t001": ctx}}
        rows = [("Alberta", ["1"], "", ["When"], "")]
        out, meta = ev.with_row_contexts(rows, set_data, info)
        train_unit = ec.with_row_context("", ctx, "Alberta")
        self.assertEqual(out[0][4], train_unit)
        self.assertEqual(meta["columns_with_context"], 1)
        self.assertEqual(ev.texts_of(out, info), [ec.format_encoder_text(("Alberta", ["1"], "", ["When"], train_unit), "", row_ctx=True)])
        with self.assertRaises(SystemExit):
            ev.with_row_contexts(rows, {"columns": set_data["columns"]}, info)
        with self.assertRaises(SystemExit):
            ev.with_row_contexts(rows, set_data, dict(info, row_ctx_spec=dict(spec, rows=3)))


if __name__ == "__main__":
    unittest.main()
