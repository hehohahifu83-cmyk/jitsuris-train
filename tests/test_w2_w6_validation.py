import unittest

import numpy as np

from bench.w2_w6_validation import (
    LABELS,
    apply_binary_temperature,
    build_features,
    fit_binary_temperature,
    hoeffding_table_risk_bound,
)


def row(group, label, probability, position=0):
    vector = np.zeros(len(LABELS), dtype=float)
    vector[LABELS.index(label)] = probability
    return {
        "group": group,
        "position": position,
        "top3": [{"label": label, "probability": probability}],
        "probs": vector,
    }


class W2W6ValidationTests(unittest.TestCase):
    def test_context_features_use_other_columns_in_same_table_only(self):
        a = row("table-a", "amount", 0.8, 0)
        b = row("table-a", "quantity", 0.7, 1)
        c = row("table-b", "date", 0.9, 0)
        x = build_features([a, b, c])
        amount_i = LABELS.index("amount")
        quantity_i = LABELS.index("quantity")
        date_i = LABELS.index("date")
        self.assertAlmostEqual(x[0][len(LABELS) + quantity_i], 0.7)
        self.assertAlmostEqual(x[0][len(LABELS) + amount_i], 0.0)
        self.assertAlmostEqual(x[0][2 * len(LABELS) + quantity_i], 0.7)
        self.assertTrue(np.all(x[2][len(LABELS):2 * len(LABELS)] == 0))
        self.assertTrue(np.all(x[2][2 * len(LABELS):3 * len(LABELS)] == 0))
        self.assertAlmostEqual(x[2][date_i], 0.9)

    def test_binary_temperature_is_finite_and_monotone(self):
        p = np.asarray([0.65, 0.75, 0.85, 0.95])
        y = np.asarray([0, 1, 0, 1])
        temperature = fit_binary_temperature(p, y)
        calibrated = apply_binary_temperature(p, temperature)
        self.assertGreater(temperature, 0)
        self.assertTrue(np.all(np.diff(calibrated) > 0))
        self.assertTrue(np.isfinite(calibrated).all())

    def test_table_risk_bound_is_bounded_and_tightens_with_more_tables(self):
        few = hoeffding_table_risk_bound([0.0] * 20)
        many = hoeffding_table_risk_bound([0.0] * 2000)
        self.assertLessEqual(few, 1.0)
        self.assertLess(many, few)
        self.assertLess(many, 0.05)


if __name__ == "__main__":
    unittest.main()
