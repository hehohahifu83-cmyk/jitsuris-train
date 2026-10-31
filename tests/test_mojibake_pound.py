import unittest

import verifier as V


class MojibakePoundTests(unittest.TestCase):
    def test_halfwidth_bracket_before_digits_is_pound(self):
        self.assertTrue(V.has_amount_cue("Accommodation", "", ["｣0.00", "｣63.98"]))
        self.assertEqual(V.amount_cue_veto("amount", "Hospitality", "", ["｣0.00"]), "amount")

    def test_japanese_quote_is_not_pound(self):
        self.assertFalse(V.has_amount_cue("備考", "", ["「東」と「西」", "なし"]))
        self.assertEqual(V.amount_cue_veto("amount", "Trees", "", ["12", "15"]), "unknown")
