import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jobs import job_environment, split_jobs


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
