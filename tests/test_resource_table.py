import contextlib
import io
import json
import os
import tempfile
import unittest

import resource_table as R


def manifest(train_s, gpu, seconds_a, seconds_b, fallback=None):
    stats = {"train": {"n": 1000, "max_length": 128, "truncated": 50, "truncated_rate": 0.05},
             "A": {"n": 100, "max_length": 128, "truncated": 10, "truncated_rate": 0.10},
             "B": {"n": 200, "max_length": 128, "truncated": 40, "truncated_rate": 0.20}}
    return {"amp": {"mode": "fp16", "fallback_step": fallback},
            "extra": {"token_stats": stats},
            "timing": {"train_loop_seconds": train_s, "peak_gpu_gib": gpu, "inference_seconds": {"A": seconds_a, "B": seconds_b},
                       "inference_rows": {"A": 100, "B": 200}}}


def write_manifest(folder, job, doc):
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, f"{job}_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(doc, fh)


class ParseTests(unittest.TestCase):
    def test_parse_group(self):
        self.assertEqual(R.parse_group("E5-base=eval_reports/runs/1:job1,job2"), ("E5-base", "eval_reports/runs/1", ["job1", "job2"]))
        for bad in ("job1", "a=b", "=x:job1", "a=x:"):
            with self.assertRaises(SystemExit):
                R.parse_group(bad)


class NumbersTests(unittest.TestCase):
    def test_per_row_milliseconds_and_truncation(self):
        got = R.job_numbers(manifest(100.0, 3.0, 1.0, 3.0), "x")
        self.assertAlmostEqual(got["sets"]["A"]["ms_per_row"], 10.0)
        self.assertAlmostEqual(got["sets"]["B"]["ms_per_row"], 15.0)
        self.assertEqual(got["sets"]["B"]["truncated_rate"], 0.20)
        self.assertEqual((got["train_s"], got["peak_gpu_gib"], got["amp"], got["train_truncated_rate"]), (100.0, 3.0, "fp16", 0.05))

    def test_missing_timing_or_stats_stops(self):
        doc = manifest(100.0, 3.0, 1.0, 3.0)
        del doc["timing"]["peak_gpu_gib"]
        with self.assertRaises(ValueError):
            R.job_numbers(doc, "x")
        doc = manifest(100.0, 3.0, 1.0, 3.0)
        doc["extra"]["token_stats"] = {}
        with self.assertRaises(ValueError):
            R.job_numbers(doc, "x")


class RenderTests(unittest.TestCase):
    def test_render_and_main(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = os.path.join(d, "a"), os.path.join(d, "b")
            write_manifest(a, "job1", manifest(100.0, 3.0, 1.0, 3.0))
            write_manifest(a, "job2", manifest(110.0, 3.2, 1.2, 3.0))
            write_manifest(b, "job1", manifest(200.0, 5.5, 2.0, 6.0, fallback=40))
            out = os.path.join(d, "out.md")
            with contextlib.redirect_stdout(io.StringIO()):
                R.main(["--group", f"小={a}:job1,job2", "--group", f"大={b}:job1", "--out", out])
            with open(out, encoding="utf-8") as fh:
                text = fh.read()
            self.assertIn("| 学習ループの秒数 | 105 ±7（100〜110） | 200 ±0（200〜200） |", text)
            self.assertIn("3.10 ±0.14（3.00〜3.20）", text)
            self.assertIn("| A（100） | 11.00 ±1.41（10.00〜12.00） | 20.00 ±0.00（20.00〜20.00） | 10.0 ±0.0（10.0〜10.0） % | 10.0 ±0.0（10.0〜10.0） % |", text)
            self.assertIn("途中で fp32 に戻った仕事あり", text)       # 大 の job1 は 40 歩で fp32 に戻った
            self.assertIn("戻りなし", text)                             # 小 は戻りなし

    def test_different_set_order_between_groups_is_refused(self):
        a = R.job_numbers(manifest(1, 1, 1.0, 1.0), "a")
        b = R.job_numbers(manifest(1, 1, 1.0, 1.0), "b")
        b["sets"] = {"B": b["sets"]["B"], "A": b["sets"]["A"]}
        with self.assertRaises(ValueError):
            R.render([("a", [a]), ("b", [b])])


if __name__ == "__main__":
    unittest.main()
