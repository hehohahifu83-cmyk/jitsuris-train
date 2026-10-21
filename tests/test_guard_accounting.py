import unittest

import guard_accounting as G


def rec(truth, raw, decision, reason="-", p1=0.9, column="x"):
    return {"truth": truth, "raw": raw, "decision": decision, "reason": reason, "p1": p1, "column": column,
            "top3": [{"label": raw, "probability": p1}, {"label": "category", "probability": 1 - p1}]}


class TallyTests(unittest.TestCase):
    def test_lost_saved_and_passed(self):
        records = [
            rec("date", "date", "unknown", "date_value_evidence_low"),        # 損（正しい答えを不明に）
            rec("date", "date", "unknown", "date_value_evidence_low"),        # 損
            rec("amount", "quantity", "unknown", "probability_below_threshold", p1=0.4),   # 得（重大な誤りを止めた）
            rec("text", "category", "unknown", "probability_below_threshold", p1=0.4),     # 得（重大ではない誤りを止めた）
            rec("amount", "quantity", "quantity", p1=0.95),                    # 通った重大
            rec("text", "category", "category", p1=0.8),                       # 通った誤り（重大でない）
            rec("amount", "amount", "amount", p1=0.99),                        # 正しく通った
            rec("other", "other", "unknown", "other_class"),                   # other は数えない
            rec("unknown", "date", "date", p1=0.7),                            # 正解が unknown の列は誤りに数えない
        ]
        t = G.tally(records)
        self.assertEqual(t["n"], 9)
        self.assertEqual(t["lost"], {"date_value_evidence_low": 2})
        self.assertEqual(t["saved"], {"probability_below_threshold": 2})
        self.assertEqual(t["saved_crit"], {"probability_below_threshold": 1})
        self.assertEqual(t["passed_wrong"], 2)
        self.assertEqual(t["passed_crit"], [("amount", "quantity", 0.95)])

    def test_threshold_scenarios(self):
        records = [rec("amount", "amount", "amount", p1=p) for p in (0.99, 0.97, 0.85, 0.65)] + [rec("amount", "quantity", "quantity", p1=0.9)]
        rows = G.threshold_scenarios(records, thresholds=(0.8, 0.95))
        self.assertEqual(rows[0], (0.8, 1, 4, 1, 1))     # 0.8 未満の正解は 1 件（0.65）。重大な誤り（0.9）は残る
        self.assertEqual(rows[1], (0.95, 2, 4, 0, 1))    # 0.95 未満の正解は 2 件。誤り（0.9）は消える

    def test_diff_counts_a_b_c_d(self):
        old = [rec("date", "date", "unknown"), rec("amount", "quantity", "unknown"), rec("text", "category", "unknown"),
               rec("date", "date", "date"), rec("id", "id", "id")]
        new = [rec("date", "date", "date"), rec("amount", "quantity", "quantity"), rec("text", "category", "category"),
               rec("date", "date", "unknown"), rec("id", "id", "id")]
        self.assertEqual(G.diff(old, new), {"A": 1, "B": 2, "C": 1, "D": 1})
        with self.assertRaises(ValueError):
            G.diff(old, new[:-1])

    def test_rescore_uses_threshold_other_and_guard(self):
        import rescore_guard as R
        tests = [("日付", ["2024-01-01"], "date", []), ("x", ["1"], "amount", []), ("y", ["a"], "text", []), ("z", ["a"], "other", [])]
        recs = [rec("date", "date", "date", column=R.normalized_header("日付"), p1=0.9),
                rec("amount", "amount", "amount", column="x", p1=0.4),          # 0.5 未満は不明
                rec("text", "text", "text", column="y", p1=0.9),
                rec("other", "other", "unknown", column="z", p1=0.9)]

        def fake_guard(pred, order, values):
            return ("unknown", "fake") if pred == "text" else (pred, None)

        out = G.rescore_records(recs, tests, fake_guard)
        self.assertEqual([(o["decision"], o["reason"]) for o in out],
                         [("date", "-"), ("unknown", "probability_below_threshold"), ("unknown", "fake"), ("unknown", "other_class")])

    def test_rescore_stops_when_order_differs(self):
        tests = [("a", ["1"], "amount", [])]
        with self.assertRaises(SystemExit):
            G.rescore_records([rec("text", "text", "text", column="a")], tests, lambda p, o, v: (p, None))

    def test_render_has_totals(self):
        t = G.tally([rec("date", "date", "unknown", "date_value_evidence_low")])
        text = G.render("見出し", t, G.threshold_scenarios([rec("amount", "amount", "amount")]), {"A": 1, "B": 0, "C": 0, "D": 0})
        self.assertIn("| date_value_evidence_low | 1 | 0 | 0 |", text)
        self.assertIn("A 不明→正解 1", text)


if __name__ == "__main__":
    unittest.main()
