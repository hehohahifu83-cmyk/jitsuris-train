import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jobs import MAX_JOBS, describe, job_environment, split_jobs


class JobsTest(unittest.TestCase):
    def test_single_job_passes_every_ft_variable(self):
        jobs = split_jobs(["m", "2", "FT_LR=2e-5", "FT_SEED=3", "FT_SORT=1"])
        self.assertEqual(len(jobs), 1)
        self.assertEqual(jobs[0]["args"], ["m", "2"])
        self.assertEqual(jobs[0]["env"], {"FT_LR": "2e-5", "FT_SEED": "3", "FT_SORT": "1"})

    def test_two_jobs_share_model_and_epochs(self):
        jobs = split_jobs(["m", "2", "FT_AUG=0", "++", "FT_AUG=1"])
        self.assertEqual([j["args"] for j in jobs], [["m", "2"], ["m", "2"]])
        self.assertEqual([j["env"] for j in jobs], [{"FT_AUG": "0"}, {"FT_AUG": "1"}])

    def test_second_job_may_change_epochs_only(self):
        jobs = split_jobs(["m", "2", "++", "3", "FT_SEED=2"])
        self.assertEqual(jobs[1]["args"], ["m", "3"])
        self.assertEqual(jobs[1]["env"], {"FT_SEED": "2"})

    def test_second_job_cannot_change_the_model(self):
        with self.assertRaises(ValueError):
            split_jobs(["m", "2", "++", "other-model", "2"])

    def test_too_many_jobs_and_missing_model_are_rejected(self):
        with self.assertRaises(ValueError):
            split_jobs(["m", "2", "++", "FT_A=1", "++", "FT_B=1"], max_jobs=2)
        with self.assertRaises(ValueError):
            split_jobs(["FT_A=1"])


    def test_later_jobs_inherit_ft_settings_and_may_override_or_remove(self):
        jobs = split_jobs(["m", "2", "FT_LR=2e-5", "FT_SORT=1", "FT_AUG=1", "++", "FT_SEED=2", "++", "FT_LR=5e-5", "FT_AUG=", "++", "3"])
        self.assertEqual(jobs[0]["env"], {"FT_LR": "2e-5", "FT_SORT": "1", "FT_AUG": "1"})
        self.assertEqual(jobs[1]["env"], {"FT_LR": "2e-5", "FT_SORT": "1", "FT_AUG": "1", "FT_SEED": "2"})   # 引き継ぐ＋追加
        self.assertEqual(jobs[2]["env"], {"FT_LR": "5e-5", "FT_SORT": "1"})                                    # 上書き＋「外す」
        self.assertEqual((jobs[3]["args"], jobs[3]["env"]), (["m", "3"], jobs[0]["env"]))                         # 周数だけ変える

    def test_empty_value_in_first_job_means_unset(self):
        self.assertEqual(split_jobs(["m", "FT_AUG=", "FT_SEED=1"])[0]["env"], {"FT_SEED": "1"})

    def test_describe_shows_only_differences_from_the_first_job(self):
        jobs = split_jobs(["m", "2", "FT_A=1", "FT_B=2", "++", "FT_B=3", "++", "FT_A=", "++", "3", "++"])
        self.assertEqual(describe(jobs, 0), "FT_A=1 FT_B=2")
        self.assertEqual(describe(jobs, 1), "仕事1との違い：FT_B=3")
        self.assertEqual(describe(jobs, 2), "仕事1との違い：FT_A=（外す）")
        self.assertEqual(describe(jobs, 3), "仕事1との違い：周数=3")
        self.assertEqual(describe(jobs, 4), "仕事1との違い：なし")

    def test_job_count_limit_is_max_jobs(self):
        ok = ["m", "2"] + ["++"] * (MAX_JOBS - 1)
        self.assertEqual(len(split_jobs(ok)), MAX_JOBS)
        with self.assertRaises(ValueError):
            split_jobs(ok + ["++"])

    def test_probe_style_args_keep_positionals(self):
        jobs = split_jobs(["m", "FT_PROBE=quick"])
        self.assertEqual(jobs[0]["args"], ["m"])

    def test_environment_gives_each_job_its_own_gpu(self):
        jobs = split_jobs(["m", "2", "++", "FT_SEED=2"])
        e0 = job_environment({"A": "1"}, jobs[0], 0, 2)
        e1 = job_environment({"A": "1"}, jobs[1], 1, 2)
        self.assertEqual((e0["CUDA_VISIBLE_DEVICES"], e1["CUDA_VISIBLE_DEVICES"]), ("0", "1"))
        self.assertEqual(e1["FT_SEED"], "2")
        self.assertEqual(job_environment({}, jobs[0], 0, 0).get("CUDA_VISIBLE_DEVICES"), None)


if __name__ == "__main__":
    unittest.main()


class RunJobsTest(unittest.TestCase):
    def test_two_jobs_run_side_by_side_with_separate_outputs(self):
        import os, tempfile
        from jobs import prepare_workdir, run_jobs
        with tempfile.TemporaryDirectory() as root:
            Path(root, "materials").mkdir()
            Path(root, "materials", "data.txt").write_text("shared", encoding="utf-8")
            Path(root, "stub.py").write_text(
                "import os, sys\n"
                "open('out_' + os.environ.get('FT_TAG', 'x') + '.txt', 'w').write(' '.join(sys.argv[1:]) + '|' + os.environ.get('CUDA_VISIBLE_DEVICES', '-') + '|' + open('materials/data.txt').read())\n",
                encoding="utf-8")
            specs = split_jobs(["modelA", "2", "FT_TAG=a", "++", "FT_TAG=b"])
            codes = run_jobs(specs, "stub.py", dict(os.environ), root, 2)
            self.assertEqual(codes, [0, 0])
            self.assertEqual(Path(root, "job1", "out_a.txt").read_text(encoding="utf-8"), "modelA 2|0|shared")
            self.assertEqual(Path(root, "job2", "out_b.txt").read_text(encoding="utf-8"), "modelA 2|1|shared")
            self.assertFalse(Path(root, "out_a.txt").exists())  # 元の場所は汚れない

    def test_single_job_runs_in_the_root(self):
        import os, tempfile
        from jobs import run_jobs
        with tempfile.TemporaryDirectory() as root:
            Path(root, "stub.py").write_text("open('done.txt', 'w').write('ok')\n", encoding="utf-8")
            codes = run_jobs(split_jobs(["m", "1"]), "stub.py", dict(os.environ), root, 0)
            self.assertEqual(codes, [0])
            self.assertTrue(Path(root, "done.txt").exists())

    def test_failing_job_reports_nonzero(self):
        import os, tempfile
        from jobs import run_jobs
        with tempfile.TemporaryDirectory() as root:
            Path(root, "stub.py").write_text("import sys\nsys.exit(3 if sys.argv[-1] == 'bad' else 0)\n", encoding="utf-8")
            specs = [{"args": ["m", "good"], "env": {}}, {"args": ["m", "bad"], "env": {}}]
            self.assertEqual(run_jobs(specs, "stub.py", dict(os.environ), root, 2), [0, 3])

    def test_queue_runs_more_jobs_than_gpus_two_at_a_time_each_on_its_own_gpu(self):
        import os, tempfile, time
        from jobs import run_jobs
        with tempfile.TemporaryDirectory() as root:
            Path(root, "stub.py").write_text(
                "import os, sys, time\n"
                "t0 = time.time(); time.sleep(0.4); t1 = time.time()\n"
                "os.makedirs('ft_out', exist_ok=True); open('ft_out/model.bin', 'w').write('big')\n"
                "open('rec.txt', 'w').write('%s %s %r %r' % (os.environ.get('FT_TAG'), os.environ.get('CUDA_VISIBLE_DEVICES'), t0, t1))\n",
                encoding="utf-8")
            specs = split_jobs(["m", "2", "FT_TAG=a", "++", "FT_TAG=b", "++", "FT_TAG=c", "++", "FT_TAG=d", "++", "FT_TAG=e"])
            codes = run_jobs(specs, "stub.py", dict(os.environ), root, 2)
            self.assertEqual(codes, [0] * 5)
            recs = []
            for i in range(1, 6):
                tag, gpu, t0, t1 = Path(root, f"job{i}", "rec.txt").read_text(encoding="utf-8").split()
                recs.append((tag, gpu, float(t0), float(t1)))
                self.assertFalse(Path(root, f"job{i}", "ft_out").exists())   # 終わった仕事のモデルは消える（ディスクを守る）
            self.assertEqual([r[0] for r in recs], ["a", "b", "c", "d", "e"])
            for gpu in ("0", "1"):   # 同じ GPU の仕事は重ならない
                mine = sorted((r[2], r[3]) for r in recs if r[1] == gpu)
                self.assertTrue(len(mine) >= 2)
                for (a0, a1), (b0, b1) in zip(mine, mine[1:]):
                    self.assertLessEqual(a1, b0 + 0.05)
            # 同時に走るのは 2 つまで
            events = sorted([(r[2], 1) for r in recs] + [(r[3], -1) for r in recs])
            cur = peak = 0
            for _, d in events:
                cur += d; peak = max(peak, cur)
            self.assertEqual(peak, 2)

    def test_one_gpu_or_cpu_runs_the_queue_one_by_one_without_pinning(self):
        import os, tempfile
        from jobs import run_jobs
        for n_gpu in (0, 1):
            with tempfile.TemporaryDirectory() as root:
                Path(root, "stub.py").write_text("import os\nopen('rec.txt', 'w').write(str(os.environ.get('CUDA_VISIBLE_DEVICES')))\n", encoding="utf-8")
                specs = split_jobs(["m", "1", "++", "FT_X=1", "++", "FT_X=2"])
                base = {k: v for k, v in os.environ.items() if k != "CUDA_VISIBLE_DEVICES"}
                self.assertEqual(run_jobs(specs, "stub.py", base, root, n_gpu), [0, 0, 0])
                for i in (1, 2, 3):
                    self.assertEqual(Path(root, f"job{i}", "rec.txt").read_text(encoding="utf-8"), "None")

    def test_failed_job_does_not_stop_the_queue(self):
        import os, tempfile
        from jobs import run_jobs
        with tempfile.TemporaryDirectory() as root:
            Path(root, "stub.py").write_text("import os, sys\nopen('ran.txt', 'w').write('x')\nsys.exit(7 if os.environ.get('FT_BAD') else 0)\n", encoding="utf-8")
            specs = split_jobs(["m", "1", "++", "FT_BAD=1", "++", "FT_BAD=", "++", "FT_BAD=1"])
            self.assertEqual(run_jobs(specs, "stub.py", dict(os.environ), root, 2), [0, 7, 0, 7])
            self.assertTrue(all(Path(root, f"job{i}", "ran.txt").exists() for i in (1, 2, 3, 4)))

    def test_unlaunchable_job_is_reported_as_failure(self):
        import os, tempfile
        from jobs import run_jobs
        with tempfile.TemporaryDirectory() as root:
            specs = [{"args": ["m"], "env": {}}, {"args": ["m"], "env": {}}]
            codes = run_jobs(specs, "missing_script.py", dict(os.environ), root, 2)   # python は起動するがスクリプトが無いので 2
            self.assertTrue(all(c != 0 for c in codes))
