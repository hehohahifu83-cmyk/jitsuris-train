import unittest

from encoder_context import HEADER_MASK_TOKEN, mask_headers


def rows(n=2000):
    return [(f"h{i}", [str(i), str(i + 1)], "quantity" if i % 2 else "amount", ["a", "b"], "") for i in range(n)]


class HeaderMaskTests(unittest.TestCase):
    def test_zero_is_identity(self):
        rs = rows(10)
        self.assertEqual(mask_headers(rs, 0.0), rs)

    def test_fraction_is_close_and_only_header_changes(self):
        rs = rows()
        out = mask_headers(rs, 0.15)
        masked = [i for i, r in enumerate(out) if r[0] == HEADER_MASK_TOKEN]
        self.assertTrue(0.12 < len(masked) / len(rs) < 0.18, len(masked))
        for i in masked:
            self.assertEqual(out[i][1:], rs[i][1:])
        for i, (a, b) in enumerate(zip(rs, out)):
            if i not in masked:
                self.assertEqual(a, b)

    def test_deterministic_and_order_independent(self):
        rs = rows()
        a = mask_headers(rs, 0.15)
        b = mask_headers(list(reversed(rs)), 0.15)
        self.assertEqual(a, list(reversed(b)))

    def test_rejects_bad_fraction(self):
        for bad in (-0.1, 1.0, 1.5):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                mask_headers(rows(3), bad)


if __name__ == "__main__":
    unittest.main()
