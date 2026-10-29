import unittest

from encoder_context import attach_unit_context, format_encoder_text, real_train_rows_with_units, unit_context_map


def identity(_rng, header):
    return header


class EncoderUnitContextTest(unittest.TestCase):
    def test_default_off_keeps_the_existing_text_byte_for_byte(self):
        row = ("Amount", ["1", "2"], "amount", ["Unit", "Date"], "USD, EUR")
        self.assertEqual(
            format_encoder_text(row, "query: ", ctx_unit=False),
            "query: 列名: Amount | 値: 1, 2 | 同じ表の列: Unit, Date",
        )

    def test_unit_values_are_opt_in(self):
        row = ("Amount", ["1", "2"], "amount", ["Unit", "Date"], "Unit: USD, EUR")
        self.assertNotIn("USD", format_encoder_text(row))
        self.assertIn("同じ表の単位列の値: Unit: USD, EUR", format_encoder_text(row, ctx_unit=True))

    def test_only_explicit_unit_headers_are_used(self):
        rows = [
            ("Unit", ["USD", "EUR", "USD"], "category", [], "table-a"),
            ("Unit Price", ["4.1", "5.2"], "amount", [], "table-a"),
            ("金額", ["10", "20"], "amount", [], "table-a"),
            ("単位", ["人", "件"], "category", [], "table-b"),
            ("Amt-units_Mnt-unite", ["thousands", "millions"], "category", [], "table-c"),
        ]
        got = unit_context_map(rows)
        self.assertEqual(got["table-a"], "Unit: USD, EUR")
        self.assertEqual(got["table-b"], "単位: 人, 件")
        self.assertEqual(got["table-c"], "Amt-units_Mnt-unite: thousands, millions")

    def test_evaluation_rows_keep_unit_values_outside_the_header_context(self):
        rows = [("VALUE", ["7.4", "4.9"], "amount", ["UNIT"], "table-a")]
        got = attach_unit_context(rows, {"table-a": "UNIT: USD"})
        self.assertEqual(got[0][:4], rows[0][:4])
        self.assertEqual(got[0][4], "UNIT: USD")

    def test_training_expansion_is_deterministic_and_preserves_unit_values(self):
        rows = [("VALUE", ["7.4", "4.9"], "amount", ["UNIT"], "table-a")]
        a = real_train_rows_with_units(rows, 2, 5, True, {"table-a": "UNIT: USD"}, identity)
        b = real_train_rows_with_units(rows, 2, 5, True, {"table-a": "UNIT: USD"}, identity)
        self.assertEqual(a, b)
        self.assertEqual(len(a), 2)
        self.assertTrue(all(row[4] == "UNIT: USD" for row in a))


if __name__ == "__main__":
    unittest.main()


class UnitHeaderLanguagesTests(unittest.TestCase):
    """2026-10-29：単位の列の見出しを広げた（bench/unit_header_prereg_20261029.md）。"""

    def test_new_headers_found(self):
        from encoder_context import _UNIT_HEADER
        for h in ("Einheit", "einheit_kurz", "EINHEIT_LANG", "UNIT_MEAS", "parameter_unit", "data_value_unit", "unité", "unidad de medida",
                  "measurement_unit__ha_", "unit", "単位"):
            self.assertTrue(_UNIT_HEADER.fullmatch(h), h)

    def test_org_units_not_found(self):
        from encoder_context import _UNIT_HEADER
        for h in ("unidade_orcamentaria", "unit count", "dwelling_units", "Business Unit", "unit type"):
            self.assertFalse(_UNIT_HEADER.fullmatch(h), h)
