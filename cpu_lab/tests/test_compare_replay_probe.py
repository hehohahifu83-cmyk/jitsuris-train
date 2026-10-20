import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
import sys
sys.path.insert(0, str(ROOT / "cpu_lab"))
from compare_replay_probe import compare

class ReplayProbeComparisonTests(unittest.TestCase):
    def write_result(self, root, name, seed, correct):
        p = root / name
        p.write_text(json.dumps({
            "stage":"after", "seed":seed, "model_name":"e5-base",
            "probe_count":2, "split":"progress_probe", "training_overlap":0,
            "fixed_test_sets_used":False,
            "predictions":[
                {"id":"a","target":"text","correct":correct,"prediction":"text" if correct else "number"},
                {"id":"b","target":"number","correct":True,"prediction":"number"}]}))
        return str(p)

    def test_matched_seed_comparison(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            b=[self.write_result(root,"b1.json","1",False), self.write_result(root,"b2.json","2",False)]
            r=[self.write_result(root,"r1.json","1",True), self.write_result(root,"r2.json","2",True)]
            got=compare(b,r,str(root/"report.json"))
            self.assertEqual(got["mean_delta_pp"],50)
            self.assertEqual(got["result"],"replay_benefit_signal")

    def test_seed_mismatch_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            b=[self.write_result(root,"b1.json","1",False),self.write_result(root,"b2.json","2",False)]
            r=[self.write_result(root,"r1.json","9",True),self.write_result(root,"r2.json","2",True)]
            with self.assertRaisesRegex(ValueError,"seeds"):
                compare(b,r,str(root/"report.json"))

if __name__ == "__main__":
    unittest.main()
