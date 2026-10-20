import json
import os
import tempfile
import unittest

import compare_models as C


def rec(column, truth, pred, outcome, critical=False):
    return {"column": column, "truth": truth, "guarded_prediction": pred, "prediction": pred, "outcome": outcome, "critical": critical}


PAIRS = {("金額", "amount"), ("日付", "date")}
HEADS = {"金額", "日付"}


def make_rows(wrong_unseen=0):
    rows = [rec("金額", "amount", "amount", "correct"), rec("日付", "date", "date", "correct"),
            rec("謎1", "quantity", "quantity", "correct"), rec("謎2", "category", "category", "correct"),
            rec("謎3", "other", "unknown", "other_ok")]
    for i in range(wrong_unseen):
        rows.append(rec(f"謎w{i}", "quantity", "amount", "wrong", True))
    return rows


class MetricsTests(unittest.TestCase):
    def test_job_metrics_splits_unseen(self):
        m = C.job_metrics(make_rows(2), PAIRS, HEADS, min_support=1)
        self.assertEqual(m["n"], 7)
        self.assertEqual(m["critical"], 2)
        self.assertEqual(m["false_assert"], 2)
        self.assertEqual(m["unseen_n"], 5)            # 謎1・謎2・謎3・謎w0・謎w1
        self.assertAlmostEqual(m["unseen_acc"], 3 / 5)
        self.assertAlmostEqual(m["acc"], 5 / 7)
        self.assertIn("quantity", m["class"])

    def test_mean_sd(self):
        self.assertEqual(C.mean_sd([1.0, 3.0])[:2], (2.0, 1.4142135623730951))
        self.assertTrue(C.mean_sd([])[0] != C.mean_sd([])[0])

    def test_render_has_all_sections_and_both_groups(self):
        g = {}
        for name, wrong in (("A", 0), ("B", 3)):
            jobs = {f"job{i}": C.job_metrics(make_rows(wrong), PAIRS, HEADS, 1) for i in (1, 2)}
            g[name] = {"jobs": jobs, "datasets": {j: {"general": {"n": 7, "acc": 0.7, "wrong": 1, "unknown": 0, "critical": wrong, "other_ng": 0}} for j in jobs}, "runs": "x"}
        text = C.render(g, "t", 1)
        for s in ("実表の試験を合わせた結果", "クラス別の適合率・再現率（実表を合わせた行）", "未知見出しだけ", "試験ごと", "仕事ごとの値", "A（2 本）", "B（2 本）"):
            self.assertIn(s, text)
        self.assertNotIn("nan", text)

    def test_parse_group(self):
        self.assertEqual(C.parse_group("E5=runs/1:job1,job2"), ("E5", "runs/1", ["job1", "job2"]))
        with self.assertRaises(ValueError):
            C.parse_group("bad")

    def test_build_reads_probs_files(self):
        with tempfile.TemporaryDirectory() as d:
            for job in ("job1", "job2"):
                for ds in ("general", "dev220"):
                    with open(os.path.join(d, f"{job}_probs_{ds}_ft.json"), "w", encoding="utf-8") as f:
                        json.dump({"dataset": ds, "rows": make_rows(1)}, f, ensure_ascii=False)
            g = C.build([("M", d, ["job1", "job2"])], "ft", PAIRS, HEADS, 1)
            self.assertEqual(g["M"]["jobs"]["job1"]["n"], 6)          # dev220 は実表の合計に入れない
            self.assertIn("dev220", g["M"]["datasets"]["job1"])        # 試験ごとの表には入る
            with self.assertRaises(ValueError):
                C.build([("M", d, ["job9"])], "ft", PAIRS, HEADS, 1)


if __name__ == "__main__":
    unittest.main()
