import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import recheck  # noqa: E402
import verifier as V  # noqa: E402


class VerifierTest(unittest.TestCase):
    def test_features_dims_and_no_header(self):
        d, sp = V.features(["1,200", "3,400", "560"])
        self.assertEqual(len(d), V.DENSE_DIM)
        self.assertTrue(all(0 <= j < V.G_DIM for j in sp))
        self.assertEqual(len(V.dense_features([])), V.DENSE_DIM)
        self.assertEqual(V.matrix([["a"], []]).shape, (2, V.DENSE_DIM + V.G_DIM))

    def test_veto_only_lowers_numeric(self):
        labels = list(V.LABELS)
        p = [0.0] * len(labels)
        p[labels.index("id")] = 0.9
        p[labels.index("quantity")] = 0.005
        self.assertEqual(V.veto("quantity", p, labels, 0.01), ("unknown", "verifier:id"))
        self.assertEqual(V.veto("quantity", p, labels, 0.001), ("quantity", None))
        self.assertEqual(V.veto("text", p, labels, 0.5), ("text", None))      # 数字の種類でなければ触らない
        self.assertEqual(V.veto("unknown", p, labels, 0.5), ("unknown", None))  # 不明は不明のまま（種類を付けない）
        q = [0.0] * len(labels)
        q[labels.index("category")] = 0.99
        self.assertEqual(V.veto("quantity", q, labels, 0.5), ("quantity", None))  # 1 位が数字の種類でなければ下げない

    def test_apply_after_recheck_keeps_recheck(self):
        class Fake:
            labels = list(V.LABELS)
            tau = 0.01

            def proba(self, values_list):
                import numpy as np
                P = np.zeros((len(values_list), len(self.labels)))
                P[:, self.labels.index("date")] = 1.0
                return P
        dec = [("date", "recheck:header_date"), ("unknown", "low_confidence_no_cue")]
        out = V.apply_after_recheck(dec, [["2020"], ["x"]], Fake())
        self.assertEqual([o[:2] for o in out], dec)   # recheck の結果（再検査で戻した日付・不明）はそのまま
        rows = [{"guarded": "date", "top3": [{"label": "date", "probability": 0.99}], "header": "日付"},
                {"guarded": "unknown", "top3": [{"label": "date", "probability": 0.6}], "header": "開始"}]
        out = V.apply_after_recheck(dec, [["2020"], ["x"]], Fake(), rows=rows, rho=0.9)
        self.assertEqual(out[1], ("unknown", "low_confidence_no_cue", "date"))   # 判定は不明のまま、候補だけ添える
        self.assertIsNone(out[0][2])

    def test_candidate_skips_hard_unknown(self):
        labels = list(V.LABELS)
        p = [0.0] * len(labels)
        p[labels.index("amount")] = 0.99
        top = [{"label": "amount", "probability": 0.7}]
        self.assertEqual(V.candidate("unknown", "low_confidence_no_cue", "amount", top, "Cost", p, labels, 0.9), "amount")
        self.assertIsNone(V.candidate("unknown", "cue_conflict:quantity", "amount", top, "Cost", p, labels, 0.9))
        self.assertIsNone(V.candidate("unknown", "low_confidence_no_cue", "amount", top, "2015", p, labels, 0.9))  # 列名が年だけ
        self.assertIsNone(V.candidate("unknown", "low_confidence_no_cue", "amount", top, "Cost", p, labels, 0.999))

    def test_load_exported(self):
        p = Path(__file__).resolve().parents[1] / "models" / "verifier_v1.json"
        v = V.Verifier.load(p)
        P = v.proba([["2019-04-01", "2020-05-03"], ["12", "7", "30"]])
        self.assertEqual(P.shape, (2, len(V.LABELS)))
        self.assertAlmostEqual(float(P[0].sum()), 1.0, places=4)
        self.assertEqual(v.labels[int(P[0].argmax())], "date")
        self.assertIsNotNone(recheck.apply_table)


if __name__ == "__main__":
    unittest.main()
