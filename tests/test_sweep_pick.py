import json
import os
import tempfile
import unittest

import sweep_pick as P


def row(job, lr, f1, critical=0, false_assert=0, problems=None):
    return {"job": job, "lr": lr, "problems": problems or [], "unseen_macro_f1": f1, "critical": critical, "false_assert": false_assert,
            "metrics": {"n": 889, "unseen_n": 255, "unseen_acc": f1, "macro_f1": f1, "acc": f1, "unknown": 3}}


class PickTests(unittest.TestCase):
    def test_best_wins_when_clear(self):
        r = P.pick([row("job1", 5e-5, 0.80), row("job2", 1e-4, 0.86), row("job3", 2e-4, 0.83), row("job4", 4e-4, 0.70)])
        self.assertEqual(r["chosen"]["job"], "job2")
        self.assertIsNone(r["edge"])

    def test_tie_within_1_5pp_prefers_fewer_critical_then_false_assert_then_small_lr(self):
        rows = [row("job1", 5e-5, 0.850, critical=3, false_assert=10), row("job2", 1e-4, 0.860, critical=2, false_assert=9),
                row("job3", 2e-4, 0.846, critical=2, false_assert=7), row("job4", 4e-4, 0.80)]
        r = P.pick(rows, 1.5)
        self.assertEqual({x["job"] for x in r["tied"]}, {"job1", "job2", "job3"})
        self.assertEqual(r["chosen"]["job"], "job3")                     # 重大 2 が同じ job2 / job3 のうち、誤断定が少ない方
        r2 = P.pick([row("job1", 5e-5, 0.85, 2, 7), row("job2", 1e-4, 0.86, 2, 7)], 1.5)
        self.assertEqual(r2["chosen"]["job"], "job1")                    # 全部同じなら小さい学習率

    def test_outside_tie_is_not_chosen(self):
        r = P.pick([row("job1", 5e-5, 0.80, 0, 0), row("job2", 1e-4, 0.86, 5, 20)], 1.5)
        self.assertEqual(r["chosen"]["job"], "job2")

    def test_ineligible_jobs_are_excluded(self):
        rows = [row("job1", 5e-5, 0.90, problems=["fp16 から fp32 に切り替えた（step 300）"]), row("job2", 1e-4, 0.80), row("job3", 2e-4, float("nan"))]
        r = P.pick(rows)
        self.assertEqual(r["chosen"]["job"], "job2")
        self.assertIsNone(P.pick([row("job1", 5e-5, 0.9, problems=["x"])])["chosen"])

    def test_edge_detection_uses_the_best_not_the_chosen(self):
        self.assertEqual(P.pick([row("job1", 5e-5, 0.80), row("job2", 1e-4, 0.82), row("job3", 4e-4, 0.90)])["edge"], "high")
        self.assertEqual(P.pick([row("job1", 5e-5, 0.90), row("job2", 1e-4, 0.82), row("job3", 4e-4, 0.80)])["edge"], "low")
        self.assertIsNone(P.pick([row("job1", 5e-5, 0.80)])["edge"])


class JobInfoTests(unittest.TestCase):
    def _write(self, d, job, manifest):
        with open(os.path.join(d, f"{job}_manifest.json"), "w", encoding="utf-8") as f:
            json.dump(manifest, f)

    def test_reads_lr_status_and_amp(self):
        with tempfile.TemporaryDirectory() as d:
            self._write(d, "job1", {"status": "completed", "run": {"env": {"FT_LR": "1e-4"}}, "amp": {"fallback_step": None}})
            self._write(d, "job2", {"status": "completed", "run": {"env": {"FT_LR": "2e-4"}}, "amp": {"fallback_step": 400}})
            self._write(d, "job3", {"status": "started", "run": {"env": {"FT_LR": "4e-4"}}})
            a, b, c = (P.job_info(d, j) for j in ("job1", "job2", "job3"))
            self.assertEqual((a["lr"], a["problems"]), (1e-4, []))
            self.assertEqual(b["lr"], 2e-4)
            self.assertTrue(any("fp32" in p for p in b["problems"]))
            self.assertTrue(any("completed" in p for p in c["problems"]))

    def test_missing_manifest_uses_lrs_but_is_excluded(self):
        with tempfile.TemporaryDirectory() as d:
            x = P.job_info(d, "job1", {"job1": 5e-5})
            self.assertEqual(x["lr"], 5e-5)
            self.assertTrue(any("manifest なし" in p for p in x["problems"]))
            self.assertTrue(any("学習率が分からない" in p for p in P.job_info(d, "job2")["problems"]))


class FormatTests(unittest.TestCase):
    def test_fmt_lr(self):
        self.assertEqual([P.fmt_lr(x) for x in (5e-5, 1e-4, 2e-4, 1.5e-4, 3e-5, None)], ["5e-5", "1e-4", "2e-4", "1.5e-4", "3e-5", "—"])


class RenderTests(unittest.TestCase):
    def test_render_mentions_choice_edge_and_caution(self):
        rows = [row("job1", 5e-5, 0.80), row("job2", 1e-4, 0.82), row("job3", 4e-4, 0.90)]
        text = P.render(rows, P.pick(rows), "題名")
        for s in ("選んだ学習率：4e-4（job3）", "外側へ 1 点足して再探索", "889 行（未知見出し 255 行）", "題名"):
            self.assertIn(s, text)
        self.assertNotIn("nan", text)

    def test_render_when_nothing_eligible(self):
        rows = [row("job1", 5e-5, 0.8, problems=["x"])]
        self.assertIn("候補が無い", P.render(rows, P.pick(rows), "t"))


if __name__ == "__main__":
    unittest.main()
