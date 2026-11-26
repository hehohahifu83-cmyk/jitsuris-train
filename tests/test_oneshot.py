"""1 回だけの予測の門（independent_eval/oneshot.py）の試験（2026-11-26 Claude）。"""
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "independent_eval"))
import oneshot as O  # noqa: E402

WANT = "run g4b-20261126-v1 once"


class OneShotTest(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.req, self.pred = self.d / "req", self.d / "pred"

    def test_skip_when_not_requested(self):
        self.req.write_text("done g4b-20261126-v1\n", encoding="utf-8")
        self.assertEqual(O.check(self.req, WANT, self.pred), "skip")

    def test_start_then_rerun_refused(self):
        self.req.write_text(WANT + "\n", encoding="utf-8")
        self.assertEqual(O.check(self.req, WANT, self.pred), "proceed")
        O.start(self.req, WANT, self.pred)
        self.assertTrue((self.pred / "STARTED").exists())
        self.assertEqual(self.req.read_text(encoding="utf-8").strip(), "started g4b-20261126-v1")
        # 途中まで予測して失敗した：依頼ファイルは started のまま → 同じ workflow の再実行は skip
        (self.pred / "pred_c_job1.json").write_text("{}", encoding="utf-8")
        self.assertEqual(O.check(self.req, WANT, self.pred), "skip")
        # 依頼ファイルを人が run に戻しても、印か予測が残っていれば止まる
        self.req.write_text(WANT + "\n", encoding="utf-8")
        with self.assertRaises(SystemExit):
            O.check(self.req, WANT, self.pred)
        (self.pred / "pred_c_job1.json").unlink()
        with self.assertRaises(SystemExit):   # STARTED だけでも止まる
            O.check(self.req, WANT, self.pred)


if __name__ == "__main__":
    unittest.main()
