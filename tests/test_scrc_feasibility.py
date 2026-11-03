import math
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "research", "facility_names"))
import scrc_feasibility as S  # noqa: E402


class BoundTests(unittest.TestCase):
    def test_cp_upper_zero_events(self):
        # 0/n の片側上限は 1 − level^(1/n)（100 回で 5% → 約 0.0295、「3 の法則」に近い）
        self.assertAlmostEqual(S.cp_upper(0, 100, 0.05), 1 - 0.05 ** 0.01, places=9)

    def test_cp_upper_inverts_cdf(self):
        u = S.cp_upper(3, 100, 0.05)
        self.assertAlmostEqual(math.exp(S._log_binom_cdf(3, 100, u)), 0.05, places=6)
        self.assertGreater(u, 0.03)

    def test_chatgpt_example_hoeffding_fails(self):
        # ChatGPT の例：n=2223・α=0.005・q≈0.9・K=51・δ=0.05 では Hoeffding だと重大 0 でも通らない
        ok, u, r = S.passes(2223, 2001, 0, 0.005, 0.05, 51, "hoeffding")
        self.assertFalse(ok)
        self.assertGreater(u, 0.04)

    def test_binomial_tighter(self):
        _, ub, _ = S.passes(2223, 2001, 0, 0.005, 0.05, 51, "binomial")
        _, uh, _ = S.passes(2223, 2001, 0, 0.005, 0.05, 51, "hoeffding")
        self.assertLess(ub, uh)


class SelectTests(unittest.TestCase):
    def test_picks_most_accepting_passing(self):
        n = 2000
        table = [(0.00, 2000, 30), (0.10, 1900, 15), (0.20, 1800, 0), (0.30, 1700, 0)]
        self.assertEqual(S.select(n, table, 0.01, 0.05), 0.20)

    def test_none_when_nothing_passes(self):
        # 通る候補が無いときは None（0.25 へ戻さない＝「候補なし・変更なし」）
        self.assertIsNone(S.select(100, [(0.0, 100, 0), (0.25, 90, 0)], 0.005, 0.05))

    def test_min_n_monotone_in_alpha(self):
        a = S.min_n(0.05, 0.05, 51, 0.9, 0.0, cap=100_000)
        b = S.min_n(0.02, 0.05, 51, 0.9, 0.0, cap=100_000)
        self.assertLess(a, b)


class BlindSheetTests(unittest.TestCase):
    def test_check_blind(self):
        import pool_v24 as P
        lines = [["b001#1", "名称", "a | b", "x, y", "1"], ["b001#2", "名称", "c", "z", "2"]]
        keys = [("t1", "名称"), ("t2", "名称")]
        self.assertEqual(P.check_blind(lines, keys, set(), set()), [])
        self.assertTrue(P.check_blind(lines, keys, {"b001#2"}, set()))
        self.assertTrue(P.check_blind(lines, keys, set(), {("t1", "名称")}))
        self.assertTrue(P.check_blind(lines + [["b001#1", "名称", "", "", "1"]], keys + [("t3", "名称")], set(), set()))

    def test_cell_strips_newlines(self):
        import pool_v24 as P
        self.assertEqual(P._cell("a\nb\tc"), "a b c")


if __name__ == "__main__":
    unittest.main()
