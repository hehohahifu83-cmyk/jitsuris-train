import unittest

from real_fraction import parse_real_fraction, select_real_fraction


def rows_for_tables(count=64):
    return [(f"h{i % 3}", [f"v{i}"], f"label{i % 2}", [], f"table-{i // 2}") for i in range(count)]


class RealFractionTests(unittest.TestCase):
    def test_parser_defaults_and_only_accepts_preregistered_fractions(self):
        self.assertEqual(parse_real_fraction(None), 1.0)
        self.assertEqual(parse_real_fraction("0.25"), 0.25)
        self.assertEqual(parse_real_fraction("0.50"), 0.5)
        self.assertEqual(parse_real_fraction("1"), 1.0)
        for invalid in ("0", "0.3", "nan", "inf", "bad"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                parse_real_fraction(invalid)

    def test_full_fraction_is_lossless(self):
        rows = rows_for_tables()
        self.assertEqual(select_real_fraction(rows, 1.0), rows)

    def test_selector_rejects_unregistered_fractions(self):
        for invalid in (0, 0.3, float("nan"), "bad"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                select_real_fraction(rows_for_tables(), invalid)

    def test_selection_is_deterministic_nested_and_keeps_whole_tables(self):
        rows = rows_for_tables()
        quarter = select_real_fraction(rows, 0.25)
        half = select_real_fraction(rows, 0.5)
        full = select_real_fraction(rows, 1.0)
        keys = lambda selected: {r[4] for r in selected}
        self.assertTrue(keys(quarter) <= keys(half) <= keys(full))
        self.assertEqual(select_real_fraction(rows, 0.25), quarter)
        self.assertEqual(select_real_fraction(list(reversed(rows)), 0.25), list(reversed(quarter)))
        for table in keys(full):
            present = [r for r in rows if r[4] == table]
            retained = [r for r in quarter if r[4] == table]
            self.assertIn(len(retained), (0, len(present)))
        self.assertLess(len(keys(quarter)), len(keys(half)))
        self.assertLess(len(keys(half)), len(keys(full)))

    def test_missing_table_key_is_rejected(self):
        with self.assertRaises(ValueError):
            select_real_fraction([("h", ["v"], "label", [])], 0.25)


if __name__ == "__main__":
    unittest.main()
