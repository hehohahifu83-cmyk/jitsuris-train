import unittest

import slice_eval as S


def rec(column, truth, guarded, outcome, critical=False):
    return {"column": column, "truth": truth, "guarded_prediction": guarded, "outcome": outcome, "critical": critical}


class SliceTests(unittest.TestCase):
    def test_normalized_header_matches_training_normalization(self):
        self.assertEqual(S.normalized_header("  ＡＢＣ　 Ｄ "), "abc d")
        self.assertEqual(S.normalized_header("Ｖａｌｕｅ"), "value")

    def test_slice_of_three_ways(self):
        pairs = {("金額", "amount"), ("名称", "org")}
        heads = {"金額", "名称", "区分"}
        self.assertEqual(S.slice_of("金額", "amount", pairs, heads), "既知ペア")
        self.assertEqual(S.slice_of("名称", "text", pairs, heads), "既知見出し・別ラベル")
        self.assertEqual(S.slice_of("区分", "category", pairs, heads), "既知見出し・別ラベル")
        self.assertEqual(S.slice_of("全く新しい", "date", pairs, heads), "未知見出し")

    def test_count_and_accuracy(self):
        rs = [rec("a", "date", "date", "correct"), rec("b", "amount", "quantity", "wrong", True),
              rec("c", "id", "unknown", "unknown"), rec("d", "other", "unknown", "other_ok"),
              rec("e", "other", "date", "other_ng")]
        c = S.count(rs)
        self.assertEqual((c["n"], c["correct"], c["wrong"], c["unknown"], c["other_ok"], c["other_ng"], c["critical"]), (5, 1, 1, 1, 1, 1, 1))
        self.assertAlmostEqual(c["acc"], 2 / 5)

    def test_macro_f1_treats_unknown_as_miss_and_other_reject_as_hit(self):
        rs = [rec("a", "date", "date", "correct"), rec("b", "date", "unknown", "unknown"),
              rec("c", "amount", "date", "wrong"), rec("d", "amount", "amount", "correct"),
              rec("e", "other", "unknown", "other_ok")]
        tp, fp, fn, support = S.class_stats(rs)
        self.assertEqual((tp["date"], fp["date"], fn["date"]), (1, 1, 1))      # date: 当たり 1、amount を取り違えた 1（FP）、unknown 1（FN）
        self.assertEqual((tp["amount"], fp["amount"], fn["amount"]), (1, 0, 1))
        self.assertEqual((tp["other"], fn["other"]), (1, 0))                     # 見送りは other の当たり
        p, r, f = S.prf(tp["date"], fp["date"], fn["date"])
        self.assertAlmostEqual(p, 0.5); self.assertAlmostEqual(r, 0.5); self.assertAlmostEqual(f, 0.5)
        mf, k = S.macro_f1(rs)
        self.assertEqual(k, 3)

    def test_report_runs_without_values(self):
        recs = {("job1", "business"): [rec("金額", "amount", "amount", "correct"), rec("新", "date", "unknown", "unknown")],
                ("job1", "dev220"): [rec("金額", "amount", "amount", "correct")]}
        text = S.report(recs, {("金額", "amount")}, {"金額"}, "試験")
        self.assertIn("未知見出し", text)
        self.assertIn("実表4つ合計", text)


if __name__ == "__main__":
    unittest.main()
