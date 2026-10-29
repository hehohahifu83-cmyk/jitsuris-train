import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verifier as V  # noqa: E402


class AmountCueTests(unittest.TestCase):
    """2026-10-29：通貨の手がかりの無い金額は不明（bench/amount_cue_prereg_20261029.md）。"""

    def test_no_cue_becomes_unknown(self):
        self.assertEqual(V.amount_cue_veto("amount", "Fossil fuels", "", ["155975600", "153398500"]), "unknown")
        self.assertEqual(V.amount_cue_veto("amount", "wert", "", ["66", "0"]), "unknown")

    def test_cues_keep_amount(self):
        self.assertEqual(V.amount_cue_veto("amount", "Amount", "", ["12.50"]), "amount")
        self.assertEqual(V.amount_cue_veto("amount", "Wert", "Einheit: CHF", ["1200"]), "amount")
        self.assertEqual(V.amount_cue_veto("amount", "Total", "", ["£1,200.00"]), "amount")
        self.assertEqual(V.amount_cue_veto("amount", "支払金額", "", ["1200"]), "amount")
        self.assertEqual(V.amount_cue_veto("amount", "Kosten", "", ["1200"]), "amount")

    def test_other_labels_untouched(self):
        self.assertEqual(V.amount_cue_veto("quantity", "Fossil fuels", "", ["1"]), "quantity")
        self.assertEqual(V.amount_cue_veto("unknown", "x", "", []), "unknown")


if __name__ == "__main__":
    unittest.main()
