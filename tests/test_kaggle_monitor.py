import json
import tempfile
import unittest
from pathlib import Path

from kaggle_monitor import latest_training_cycle, parse_status, render_progress, update_monitor


class KaggleMonitorTests(unittest.TestCase):
    def test_parse_status_requires_fresh_successful_observation(self):
        self.assertEqual(parse_status('jitsurio has status "KernelWorkerStatus.RUNNING"'), "RUNNING")
        self.assertEqual(parse_status('KernelWorkerStatus.COMPLETE', 1), "UNKNOWN")
        self.assertEqual(parse_status("authentication failed"), "UNKNOWN")

    def test_tracks_queue_start_and_completion_for_same_cycle(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "MONITOR.json"
            for state, at in [("QUEUED", "t1"), ("RUNNING", "t2"), ("COMPLETE", "t3")]:
                update_monitor(path, cycle_id="cycle-a", observed_at=at, state=state,
                               raw=f"KernelWorkerStatus.{state}", action_run_id="42")
            record = json.loads(path.read_text())
            self.assertEqual(record["first_running_at"], "t2")
            self.assertEqual(record["first_complete_at"], "t3")
            self.assertEqual(record["terminal_state"], "COMPLETE")
            self.assertEqual([o["state"] for o in record["observations"]], ["QUEUED", "RUNNING", "COMPLETE"])

    def test_does_not_claim_start_if_first_observation_is_complete(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "MONITOR.json"
            record = update_monitor(path, cycle_id="cycle-a", observed_at="t1", state="COMPLETE",
                                   raw="KernelWorkerStatus.COMPLETE", action_run_id="42",
                                   execution_evidence=["evaluation results recovered"])
            self.assertIsNone(record["first_running_at"])
            self.assertEqual(record["first_complete_at"], "t1")
            self.assertTrue(record["training_execution_confirmed"])
            self.assertEqual(record["execution_confirmed_at"], "t1")
            self.assertEqual(record["execution_evidence"], ["evaluation results recovered"])

    def test_new_cycle_resets_lifecycle_timestamps(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "MONITOR.json"
            update_monitor(path, cycle_id="cycle-a", observed_at="t1", state="RUNNING",
                           raw="KernelWorkerStatus.RUNNING", action_run_id="42")
            record = update_monitor(path, cycle_id="cycle-b", observed_at="t2", state="QUEUED",
                                    raw="KernelWorkerStatus.QUEUED", action_run_id="43")
            self.assertIsNone(record["first_running_at"])
            self.assertEqual(record["cycle_id"], "cycle-b")
            self.assertEqual(len(record["observations"]), 1)


    def test_render_progress_uses_latest_state_and_identifies_queue(self):
        body = render_progress(state="QUEUED", observed_at="t1", raw="KernelWorkerStatus.QUEUED",
                               cycle_id="cycle-a", action_run_id="run-1")
        self.assertIn("判定: GPU割当待ち", body)
        self.assertIn("観測時刻 (UTC): t1", body)
        self.assertIn("学習依頼ID: cycle-a", body)
        self.assertIn("確認run: run-1", body)

    def test_render_progress_does_not_reuse_prior_complete_after_unknown(self):
        body = render_progress(state="UNKNOWN", observed_at="t2", raw="authentication failed",
                               cycle_id="cycle-a", action_run_id="run-2")
        self.assertIn("判定: 未確認", body)
        self.assertNotIn("Kaggle完了", body)
        self.assertIn("authentication failed", body)

    def test_extracts_latest_timestamped_training_request(self):
        log = "2026-01-01T00:00:00Z train を依頼：old\n2026-01-02T00:00:00Z train を依頼：new\n"
        self.assertEqual(latest_training_cycle(log), "2026-01-02T00:00:00Z")


if __name__ == "__main__":
    unittest.main()
