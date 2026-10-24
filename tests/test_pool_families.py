import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pool_families as F


def table(name, heads, label="quantity"):
    return [(h, ["1", "2"], label, [], name) for h in heads]


class PoolFamiliesTest(unittest.TestCase):
    def setUp(self):
        self.rows = []
        for i in range(10):   # 同じ様式（数字だけ違う見出し）の表 10
            self.rows += table(f"t{i}", ["0-4歳", "5-9歳", "地域名"])
        for i in range(30):   # 別々の様式の表 30
            self.rows += table(f"u{i}", [f"列{chr(0x41 + i)}", "名称"])

    def test_digits_are_one_family(self):
        keys = F.family_keys(self.rows)
        self.assertEqual(len({keys[f"t{i}"] for i in range(10)}), 1)
        self.assertEqual(len({keys[f"u{i}"] for i in range(30)}), 30)

    def test_family_never_straddles_split(self):
        train, val = F.split_val_by_family(self.rows, salt="s", mod=4)
        tr_t, va_t = {r[4] for r in train}, {r[4] for r in val}
        same = {f"t{i}" for i in range(10)}
        self.assertTrue(same <= tr_t or same <= va_t)
        self.assertFalse(tr_t & va_t)
        self.assertEqual(len(train) + len(val), len(self.rows))
        self.assertEqual(F.split_val_by_family(self.rows, salt="s", mod=4), (train, val))

    def test_cap(self):
        kept, dropped = F.cap_tables_per_family(self.rows, 3)
        self.assertEqual(dropped, 7)
        self.assertEqual(len({r[4] for r in kept if r[4].startswith("t")}), 3)
        self.assertEqual(len({r[4] for r in kept if r[4].startswith("u")}), 30)
        self.assertEqual(F.cap_tables_per_family(self.rows, 0), (self.rows, 0))


if __name__ == "__main__":
    unittest.main()
