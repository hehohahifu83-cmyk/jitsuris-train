import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analyze_errors as ae


def row(col, truth, pred, p1, truth_p=None):
    top3 = [{"label": pred, "probability": p1}]
    if truth_p is not None and truth != pred:
        top3.append({"label": truth, "probability": truth_p})
    return {"index": 0, "column": col, "truth": truth, "prediction": pred, "critical": False, "top3": top3}


class AnalyzeErrorsTest(unittest.TestCase):
    def test_classify_follows_score_real(self):
        self.assertEqual(ae.classify(row("a", "org", "org", 0.9)), "correct")
        self.assertEqual(ae.classify(row("a", "org", "person", 0.9)), "wrong")
        self.assertEqual(ae.classify(row("a", "org", "unknown", 0.4)), "unknown")
        self.assertEqual(ae.classify(row("a", "other", "unknown", 0.4)), "other_ok")
        self.assertEqual(ae.classify(row("a", "other", "id", 0.9)), "other_ng")

    def test_report_lists_pairs_unknown_and_critical(self):
        rows = [row("単価", "amount", "rate", 0.91, 0.07), row("数量", "quantity", "quantity", 0.99),
                row("氏名", "person", "org", 0.6), row("備考", "text", "unknown", 0.3), row("メモ", "other", "unknown", 0.3)]
        text = ae.analyze({"業務": rows})
        self.assertIn("重大 1", text)
        self.assertIn("amount→rate 1", text)
        self.assertIn("person→org 1", text)
        self.assertIn("text 1", text)  # 不明にした正解の種類
        self.assertIn("「単価」 amount→rate（予測 0.91、正解 0.07）", text)
        self.assertNotIn("メモ", text)  # other を不明にしたのは正しい扱いで、一覧には出さない

    def test_truth_missing_from_top3_is_said_so(self):
        text = ae.analyze({"t": [row("x", "date", "id", 0.8)]})
        self.assertIn("上位3に無い", text)


if __name__ == "__main__":
    unittest.main()
