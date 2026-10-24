import os
import sys
import tempfile
import unittest

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pool_tools as T


class PoolToolsTest(unittest.TestCase):
    labels = ["amount", "category", "quantity"]

    def cols(self):
        cols = []
        for t in range(40):   # 金額の表（amount が多い）と件数の表（quantity が多い）
            kind = "amount" if t % 2 else "quantity"
            for j in range(3):
                cols.append({"batch": "b1", "table": f"t{t}", "truth": kind if j < 2 else "category"})
        return cols

    def probs(self, cols):
        rng = np.random.default_rng(0)
        P = []
        for c in cols:
            p = np.array([0.4, 0.2, 0.4]) if c["truth"] != "category" else np.array([0.1, 0.8, 0.1])
            P.append(p + rng.uniform(0, 0.01, 3))
        P = np.array(P)
        return P / P.sum(axis=1, keepdims=True)

    def test_table_features_shape_and_exclusion(self):
        cols = self.cols(); P = self.probs(cols)
        X = T.table_features(P, cols)
        self.assertEqual(X.shape, (len(cols), 3 * 3 + 1))
        np.testing.assert_allclose(X[0, 3:6], (P[1] + P[2]) / 2)   # 自分は平均に入れない

    def test_export_roundtrip(self):
        cols = self.cols(); P = self.probs(cols)
        lr = T.table_pass_fit(P, cols, self.labels)
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "tp.json")
            T.table_pass_export(lr, self.labels, path, {})
            a = T.table_pass_apply(lr, P, cols, self.labels)
            b = T.table_pass_load_apply(path, P, cols, self.labels)
        np.testing.assert_allclose(a, b, atol=1e-4)

    def test_abstain_only_numeric(self):
        P = np.array([[0.5, 0.3, 0.2], [0.5, 0.3, 0.2]])
        self.assertEqual(T.abstain(["amount", "category", "x"], P, ["amount", "category"], 0.7), ["unknown", "category"])

    def test_tta_first_view_only(self):
        PV = np.array([[[1.0, 0.0], [0.0, 1.0]]])
        np.testing.assert_allclose(T.tta(PV, 1), [[1.0, 0.0]])
        np.testing.assert_allclose(T.tta(PV, 2), [[0.5, 0.5]])


if __name__ == "__main__":
    unittest.main()
