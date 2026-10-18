import importlib.util
import unittest
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "bench" / "cpu_benchmark.py"
spec = importlib.util.spec_from_file_location("cpu_benchmark", path)
cpu_benchmark = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cpu_benchmark)


class CpuBenchmarkTest(unittest.TestCase):
    def test_parse_train_eval_times_and_losses(self):
        output = "| model | x | 学習 12秒・評価 3秒 |\nstep_loss 1 0.123456\n"
        train, evaluation, losses = cpu_benchmark.parse_run(output)
        self.assertEqual((train, evaluation), (12.0, 3.0))
        self.assertEqual(losses, [0.123456])

    def test_loss_comparison_requires_twenty_steps(self):
        self.assertFalse(cpu_benchmark.compare_losses([1.0] * 19, [1.0] * 20))
        self.assertTrue(cpu_benchmark.compare_losses([1.0001] * 20, [1.0002] * 20))
        self.assertFalse(cpu_benchmark.compare_losses([1.0] * 20, [1.001] * 20))


if __name__ == "__main__":
    unittest.main()
