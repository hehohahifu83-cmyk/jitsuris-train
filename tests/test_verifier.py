import math
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

            def proba(self, values_list, table=None):
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

    def test_table_features_subtotal_and_order(self):
        t = [{"rows": ["1", "2", "3", "4"], "row_index": [0, 1, 2, 3], "total": 4},
             {"rows": ["10", "20", "5", "7"], "row_index": [0, 1, 2, 3], "total": 4},
             {"rows": ["3", "4", "5", "8"], "row_index": [0, 1, 2, 3], "total": 4},
             {"rows": ["13", "24", "10", "15"], "row_index": [0, 1, 2, 3], "total": 4}]
        F = V.table_features(t)
        self.assertEqual(len(F), 4)
        self.assertTrue(all(len(f) == V.TABLE_DIM for f in F))
        self.assertEqual([f[12] for f in F], [0.0, 0.0, 0.0, 1.0])   # 最後の列はすぐ左の 2 列の和（合計の列）
        self.assertAlmostEqual(F[0][7], 1.0)                                # 最初の列は行の番号と同じ順に並ぶ（番号らしさ）
        self.assertEqual(V.table_features([{"rows": [], "row_index": [], "total": None}])[0][:3], [math.log(2), 0.0, 1.0])

    def test_load_exported(self):
        p = Path(__file__).resolve().parents[1] / "models" / "verifier_v1.json"
        v = V.Verifier.load(p)
        vals = [["2019-04-01", "2020-05-03"], ["12", "7", "30"]]
        tab = [{"rows": x, "row_index": list(range(len(x))), "total": 100} for x in vals]
        P = v.proba(vals, tab if v.table else None)
        self.assertEqual(P.shape, (2, len(V.LABELS)))
        self.assertAlmostEqual(float(P[0].sum()), 1.0, places=4)
        self.assertEqual(v.labels[int(P[0].argmax())], "date")
        self.assertIsNotNone(recheck.apply_table)

    def test_load_v2_with_risk(self):
        p = Path(__file__).resolve().parents[1] / "models" / "verifier_v2.json"
        v = V.Verifier.load(p)
        self.assertTrue(v.table and v.risk)
        vals = [["1", "2", "3", "4"], ["120", "80", "45", "300"], ["2019-04-01", "2019-05-01", "2019-06-01", "2019-07-01"]]
        tab = [{"rows": x, "row_index": [0, 5, 9, 14], "total": 20} for x in vals]
        dec = [("id", None), ("quantity", None), ("date", None)]
        rows = [{"guarded": d[0], "top3": [{"label": d[0], "probability": 0.9}], "header": "x"} for d in dec]
        out = V.apply_after_recheck(dec, vals, v, rows=rows, table=tab)
        self.assertEqual(len(out), 3)
        self.assertTrue(all(o[0] in (d[0], "unknown") for o, d in zip(out, dec)))   # 種類を付け替えない


if __name__ == "__main__":
    unittest.main()
