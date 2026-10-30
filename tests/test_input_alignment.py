"""学習と予測の入力をそろえる設定（2026-10-30、原因 M15・M7・M16）の試験。"""
import json
import os
import tempfile
import unittest

import encoder_context as E
import evaluate_independent as EI


class PickValuesTest(unittest.TestCase):
    def test_fills_missing_in_place(self):
        self.assertEqual(E.pick_values(["[x]", "5", "[z]"], ["[x]", "12", "7"]), ["12", "5", "7"])

    def test_keeps_values_without_rows_or_spares(self):
        self.assertEqual(E.pick_values(["1", "2"], None), ["1", "2"])
        self.assertEqual(E.pick_values([".", "0"], [".", "."]), [".", "0"])

    def test_columns_without_missing_unchanged(self):
        self.assertEqual(E.pick_values(["a", "b", "c", "d", "e"], ["x"] * 20), ["a", "b", "c", "d", "e"])


class IndicatorTest(unittest.TestCase):
    rows = [("Kennzahl", ["Total Fondsvolumen", "Anzahl"], "", [], "t"), ("Einheit", ["Tonnen (t)"], "", [], "t")]

    def test_generic_value_column_gets_indicator(self):
        u, i = E.unit_context_map(self.rows), E.indicator_context_map(self.rows)
        self.assertEqual(E.unit_for("Wert", u["t"], i["t"]), "Einheit: Tonnen (t); Kennzahl: Total Fondsvolumen, Anzahl")

    def test_other_columns_only_unit(self):
        u, i = E.unit_context_map(self.rows), E.indicator_context_map(self.rows)
        self.assertEqual(E.unit_for("Jahr", u["t"], i["t"]), "Einheit: Tonnen (t)")

    def test_title_kept_after_indicator(self):
        full = "Einheit: t" + E.TITLE_SEP + "Deponien"
        out = E._with_indicator("Wert", full, {"t": "Kennzahl: A"}, "t")
        self.assertEqual(out, "Einheit: t; Kennzahl: A" + E.TITLE_SEP + "Deponien")
        self.assertEqual(E._with_indicator("Wert", full, None, "t"), full)


class ModelRowsTest(unittest.TestCase):
    data = {"columns": [
        {"id": "a", "table": "t", "header": "Wert", "values": ["[x]", "3"], "siblings": ["Kennzahl"], "unit": "", "row_values": ["[x]", "8"]},
        {"id": "b", "table": "t", "header": "Kennzahl", "values": ["Anzahl"], "siblings": ["Wert"], "unit": ""},
        {"id": "c", "table": "t", "header": "Einheit", "values": ["Personen"], "siblings": ["Wert"], "unit": ""}]}

    def test_old_weights_unchanged(self):
        self.assertEqual(EI.model_rows_of(self.data, {}), EI.rows_of(self.data))

    def test_new_settings(self):
        rows = EI.model_rows_of(self.data, {"val_select": True, "unit_ext": True})
        self.assertEqual(rows[0][1], ["8", "3"])
        self.assertEqual(rows[0][4], "Einheit: Personen; Kennzahl: Anzahl")
        self.assertEqual(rows[1][4], "Einheit: Personen")


class LoadRowsTest(unittest.TestCase):
    def test_same_as_load_real_without_row_values(self):
        import exp7
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.jsonl")
            with open(p, "w", encoding="utf-8") as f:
                f.write(json.dumps({"header": "﻿A", "values": ["1", "nan", "2"], "label": "id", "context": [], "table": "t"}) + "\n")
            self.assertEqual(E.load_rows_valsel((p,)), exp7.load_real((p,)))
            self.assertEqual(E.LOAD_REAL_JUNK, exp7.JUNK)


if __name__ == "__main__":
    unittest.main()
