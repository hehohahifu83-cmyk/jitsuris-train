import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tokenizer_fixtures as T
from edge_texts import EDGE_TEXTS


class FixtureHelpersTest(unittest.TestCase):
    def test_scalar_values_skip_only_surrogates(self):
        cps = list(T.scalar_values())
        self.assertEqual(len(cps), 0x110000 - 0x800)
        self.assertEqual(cps[0], 0)
        self.assertEqual(cps[-1], 0x10FFFF)
        self.assertNotIn(0xD800, cps)
        self.assertNotIn(0xDFFF, cps)
        self.assertIn(0xD7FF, cps)
        self.assertIn(0xE000, cps)

    def test_extenders_cover_the_marks_that_change_graphemes(self):
        ext = set(T.extender_codepoints())
        for cp in (0x0301, 0x3099, 0x309A, 0xFF9E, 0xFF9F, 0x200D, 0xFE0F, 0x1F3FD, 0x20E3):
            self.assertIn(cp, ext, hex(cp))
        self.assertNotIn(0x0041, ext)   # 普通の文字は入らない
        self.assertTrue(all(not 0xD800 <= c <= 0xDFFF for c in ext))

    def test_random_strings_are_reproducible_and_never_contain_surrogates(self):
        a = T.make_random_strings(T.random_alphabet(), 200, random.Random(1))
        b = T.make_random_strings(T.random_alphabet(), 200, random.Random(1))
        self.assertEqual(a, b)
        self.assertTrue(all(1 <= len(s) <= 10 for s in a))
        for s in a:
            s.encode("utf-8")   # サロゲートが混ざっていれば UnicodeEncodeError
        c = T.make_random_strings(T.random_alphabet(), 200, random.Random(2))
        self.assertNotEqual(a, c)

    def test_pairs_and_triples_have_a_base_then_marks(self):
        ext = [0x3099, 0x0301]
        pairs = T.make_pairs(ext)
        self.assertEqual(len(pairs), len(T.BASES) * 2)
        self.assertIn("ｿ゙", pairs)
        triples = T.make_triples(ext, 50, random.Random(3))
        self.assertTrue(all(len(t) == 3 and t[0] in T.BASES for t in triples))

    def test_edge_texts_contain_the_half_width_katakana_cases_that_failed_in_the_browser(self):
        joined = "\n".join(EDGE_TEXTS)
        self.assertIn("ｱｲｳｴｵ ﾊﾟﾋﾟﾌﾟ ｶﾞｷﾞ", EDGE_TEXTS)
        self.assertIn("゙", joined)       # 分解形の濁点
        self.assertIn("<mask>", EDGE_TEXTS)   # 文中の特別な記号
        self.assertEqual(len(EDGE_TEXTS), len(set(EDGE_TEXTS)))


if __name__ == "__main__":
    unittest.main()
