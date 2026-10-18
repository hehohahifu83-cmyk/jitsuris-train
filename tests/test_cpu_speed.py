import tempfile
import unittest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cpu_speed import available_cpu_count, configure_cpu_threads


class CpuSpeedTest(unittest.TestCase):
    def test_defaults_to_half_available_cores(self):
        env = {}
        available, threads = configure_cpu_threads(env, affinity={0, 1, 2, 3}, cgroup_root="/missing")
        self.assertEqual((available, threads), (4, 2))
        self.assertEqual(env["FT_CPU_THREADS"], "2")

    def test_respects_affinity_and_cgroup_quota(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "cpu.max").write_text("150000 100000\n", encoding="ascii")
            self.assertEqual(available_cpu_count(affinity={0, 1, 2, 3}, cgroup_root=tmp), 2)

    def test_thread_override_is_capped_and_sets_library_limits(self):
        env = {"FT_CPU_THREADS": "8"}
        available, threads = configure_cpu_threads(env, affinity={0, 1}, cgroup_root="/missing")
        self.assertEqual((available, threads), (2, 2))
        for key in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
            self.assertEqual(env[key], "2")


if __name__ == "__main__":
    unittest.main()

