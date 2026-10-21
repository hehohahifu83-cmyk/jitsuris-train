import json
import os
import tempfile
import unittest

import independent_report as R


def write(path, data):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False)


def record(truth, pred, p=0.9):
    outcome = "correct" if truth == pred else ("unknown" if pred == "unknown" else "wrong")
    crit = outcome == "wrong" and truth in R.NUMERIC and pred in R.NUMERIC
    return {"truth": truth, "guarded_prediction": pred, "outcome": outcome, "critical": crit,
            "top3": [{"label": pred, "probability": p}]}


class IndependentReportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        cols = [{"id": f"x{i}", "table": f"t{i // 2}", "source": "a" if i < 4 else "b", "language": "ja", "header": f"h{i}"} for i in range(8)]
        write(os.path.join(self.tmp, "set.json"), {"columns": cols})
        truth = {f"x{i}": ("date" if i % 2 else "quantity") for i in range(8)}
        truth["x7"] = "unknown"   # 採点から外れる
        write(os.path.join(self.tmp, "labels.json"), truth)
        write(os.path.join(self.tmp, "th.json"), {"pairs": [["h0", "quantity"]], "headers": ["h0"]})
        kept = [f"x{i}" for i in range(7)]
        for model, wrong in (("base", {"x1"}), ("cand", {"x1", "x2", "x3"})):
            d = os.path.join(self.tmp, model)
            os.makedirs(d)
            for job in ("job1", "job2"):
                rows = [record(truth[i], ("amount" if truth[i] == "quantity" else "quantity") if i in wrong else truth[i]) for i in kept]
                write(os.path.join(d, f"{job}_probs_independent_main_ft.json"), {"rows": rows})
                write(os.path.join(d, f"{job}_independent_manifest.json"), {"unknown_asserted": 1})

    def run_report(self):
        out = os.path.join(self.tmp, "out.md")
        R.main(["--set", os.path.join(self.tmp, "set.json"), "--train-headers", os.path.join(self.tmp, "th.json"),
                "--labels", "L=" + os.path.join(self.tmp, "labels.json"),
                "--scored", "L=" + os.path.join(self.tmp, "base") + "," + os.path.join(self.tmp, "cand"),
                "--primary", "L", "--baseline", "B", "--candidate", "C", "--jobs", "job1,job2", "--reps", "200", "--out", out])
        with open(out, encoding="utf-8") as fh:
            return fh.read()

    def test_worse_candidate_keeps_baseline_and_is_deterministic(self):
        text = self.run_report()
        self.assertIn("**結論：B を残す**", text)
        self.assertIn("| L | 7 | 6 |", text)   # 採点 7 列（unknown を除く）、未知見出し 6 列（h0 は学習側にある）
        self.assertEqual(text, self.run_report())

    def test_no_column_ids_in_output(self):
        text = self.run_report()
        for i in range(8):
            self.assertNotIn(f"x{i}", text)

    def test_row_count_mismatch_is_rejected(self):
        with self.assertRaises(ValueError):
            R.attach([{}], ["a", "b"])


if __name__ == "__main__":
    unittest.main()
