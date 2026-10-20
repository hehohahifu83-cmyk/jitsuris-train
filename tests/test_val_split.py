import unittest

import val_split as V


def row(table, header="h"):
    return (header, ["1"], "amount", None, table)


class ValSplitTests(unittest.TestCase):
    def test_split_is_disjoint_by_table_and_complete(self):
        rows = [row(f"t{i}", f"h{i}") for i in range(400)] + [row("t3", "again")]
        train, val = V.split_val(rows)
        self.assertEqual(len(train) + len(val), len(rows))
        self.assertFalse(V.tables_of(train) & V.tables_of(val))   # 同じ表の行は、学習と検証に分かれて入らない
        self.assertTrue(val)

    def test_split_is_deterministic_and_roughly_one_eighth(self):
        rows = [row(f"table-{i}") for i in range(4000)]
        a = V.split_val(rows)
        b = V.split_val(list(reversed(rows)))
        self.assertEqual(sorted(V.tables_of(a[1])), sorted(V.tables_of(b[1])))
        share = len(a[1]) / len(rows)
        self.assertTrue(0.10 < share < 0.15, share)

    def test_salt_makes_it_independent_of_exp7_split(self):
        # exp7.split は md5(表) % 5 == 0 が試験側。検証の分け方は塩つきなので、別の決まり方になる
        import hashlib
        tables = [f"table-{i}" for i in range(2000)]
        test_side = {t for t in tables if int(hashlib.md5(t.encode()).hexdigest(), 16) % 5 == 0}
        val_side = {t for t in tables if V.is_val_table(t)}
        self.assertNotEqual(test_side, val_side)
        both = test_side & val_side
        self.assertTrue(0 < len(both) < len(val_side))   # 完全には一致も排他もしない（独立）


if __name__ == "__main__":
    unittest.main()
