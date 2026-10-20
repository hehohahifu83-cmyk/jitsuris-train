import unittest

import error_overlap as O


def rec(column, truth, pred, outcome):
    return {"column": column, "truth": truth, "guarded_prediction": pred, "prediction": pred, "outcome": outcome}


TRAIN_PAIRS = {("known", "date")}
TRAIN_HEADS = {"known"}


def records(rows):
    return {("job1", "val_x"): rows}


class UnseenRowsTests(unittest.TestCase):
    def test_keeps_only_unseen_headers_and_marks_outcome(self):
        rows = [rec("known", "date", "date", "correct"), rec("Zeta", "quantity", "category", "wrong"),
                rec("Eta", "other", "unknown", "other_ok"), rec("Theta", "rate", "unknown", "unknown")]
        got = O.unseen_rows(records(rows), "job1", TRAIN_PAIRS, TRAIN_HEADS)
        self.assertEqual(sorted(got), [("val_x", 1), ("val_x", 2), ("val_x", 3)])
        self.assertFalse(got[("val_x", 1)][3])
        self.assertTrue(got[("val_x", 2)][3])           # other を不明と答えたのは当たり
        self.assertFalse(got[("val_x", 3)][3])          # 不明は外れ（other 以外）

    def test_other_job_is_ignored(self):
        self.assertEqual(O.unseen_rows({("job2", "val_x"): [rec("Zeta", "date", "date", "correct")]}, "job1", TRAIN_PAIRS, TRAIN_HEADS), {})


class OverlapTests(unittest.TestCase):
    def setUp(self):
        a_rows = [rec("A1", "quantity", "category", "wrong"), rec("A2", "quantity", "category", "wrong"),
                  rec("A3", "rate", "category", "wrong"), rec("A4", "date", "date", "correct"), rec("A5", "other", "unknown", "other_ok")]
        b_rows = [rec("A1", "quantity", "category", "wrong"), rec("A2", "quantity", "unknown", "unknown"),
                  rec("A3", "rate", "rate", "correct"), rec("A4", "date", "id", "wrong"), rec("A5", "other", "unknown", "other_ok")]
        self.a = O.unseen_rows(records(a_rows), "job1", TRAIN_PAIRS, TRAIN_HEADS)
        self.b = O.unseen_rows(records(b_rows), "job1", TRAIN_PAIRS, TRAIN_HEADS)

    def test_counts(self):
        r = O.overlap(self.a, self.b)
        self.assertEqual((r["n"], r["wrong_a"], r["wrong_b"]), (5, 3, 3))
        self.assertEqual(len(r["both"]), 2)                       # A1・A2
        self.assertEqual((len(r["only_a"]), len(r["only_b"])), (1, 1))
        self.assertEqual(r["same_prediction_in_both"], 1)         # A1 は両方 category、A2 は category／unknown
        self.assertEqual(r["both_confusions"][("quantity", "category", "category")], 1)
        self.assertEqual(r["only_b_confusions"][("date", "id")], 1)

    def test_different_rows_are_refused(self):
        bad = dict(self.b)
        bad[("val_x", 0)] = ("changed", "quantity", "category", False)
        with self.assertRaises(ValueError):
            O.overlap(self.a, bad)
        with self.assertRaises(ValueError):
            O.overlap(self.a, {k: v for k, v in self.b.items() if k != ("val_x", 4)})

    def test_render_has_key_numbers_and_caution(self):
        text = O.render(O.overlap(self.a, self.b), self.a, self.b, "モデルA", "モデルB")
        for s in ("**両方が外した**", "モデルA だけが外した", "`A1`（正解 quantity）", "表の ID は無い"):
            self.assertIn(s, text)


class ParseTests(unittest.TestCase):
    def test_parse_spec(self):
        self.assertEqual(O.parse_spec("eval_reports/runs/1:job2"), ("eval_reports/runs/1", "job2"))
        with self.assertRaises(SystemExit):
            O.parse_spec("job2")


if __name__ == "__main__":
    unittest.main()
