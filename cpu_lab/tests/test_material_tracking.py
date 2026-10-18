import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from material_receipt import prepare, mark_trained
from progress_probe import compare


class MaterialTrackingTests(unittest.TestCase):
    def test_receipt_marks_only_accepted_pool_rows_then_training(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            pool = root / "pool.jsonl"
            pseudo = root / "pseudo.jsonl"
            receipt = root / "receipt.json"
            log = root / "train.log"
            out = root / "receipt-seed1.json"
            source = {"id":"synthetic:1","header":"金額","values":["100"],"context":[],"unit_context":"JPY",
                      "source":"synthetic:test-fixture","license":"internal","split":"unlabeled","privacy_checked":True}
            pool.write_text(json.dumps(source, ensure_ascii=False)+"\n"+json.dumps({**source,"id":"synthetic:2"},ensure_ascii=False)+"\n",encoding="utf-8")
            pseudo_row = {**source,"label":"amount","split":"train","verified":False,
                          "pseudo_label":{"method":"same-model-three-value-orders-v1","agreement":3}}
            pseudo.write_text(json.dumps(pseudo_row,ensure_ascii=False)+"\n",encoding="utf-8")
            r = prepare(pool,pseudo,"ft_out_job1",receipt)
            self.assertEqual(r["pseudo_candidate_count"],1)
            self.assertEqual([x["status"] for x in r["items"]],["pseudo_label_candidate","not_selected_by_gate"])
            log.write_text("CPU lab pseudo replay: 1 unverified rows (capped at 1% of 55213) from candidate.jsonl\n",encoding="utf-8")
            marked = mark_trained(receipt,log,1,out)
            self.assertEqual(marked["items"][0]["training_status"],"included_in_training")
            self.assertEqual(marked["items"][1]["training_status"],"not_yet_run")
            with self.assertRaises(ValueError):
                mark_trained(receipt,root/"missing.log",1,out)

    def test_receipt_rejects_material_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            poolrow={"id":"synthetic:1","header":"金額","values":["100"],"source":"internal","license":"internal","split":"unlabeled","privacy_checked":True}
            pool=root/"pool.jsonl"; pseudo=root/"pseudo.jsonl"
            pool.write_text(json.dumps(poolrow,ensure_ascii=False)+"\n",encoding="utf-8")
            pseudo.write_text(json.dumps({**poolrow,"header":"日付","label":"date","split":"train","verified":False},ensure_ascii=False)+"\n",encoding="utf-8")
            with self.assertRaises(ValueError):
                prepare(pool,pseudo,"checkpoint",root/"receipt.json")

    def test_probe_compare_flags_improved_regressed_and_no_difference(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            def write(path, oks):
                rows=[{"id":str(i),"target":"a","prediction":"a" if i in oks else "b","correct":i in oks} for i in range(100)]
                path.write_text(json.dumps({"probe_count":100,"accuracy":len(oks)/100,"errors":100-len(oks),"predictions":rows}),encoding="utf-8")
            b=root/"before.json"; a=root/"after.json"; o=root/"out.json"
            write(b,set(range(80))); write(a,set(range(82)))
            self.assertEqual(compare(str(b),str(a),str(o))["result"],"measurable_improvement")
            write(a,set(range(79)))
            self.assertEqual(compare(str(b),str(a),str(o))["result"],"measurable_regression")
            write(a,set(range(80)))
            self.assertEqual(compare(str(b),str(a),str(o))["result"],"no_difference_under_1_5pp")

    def test_checked_in_probe_is_separate_and_has_only_synthetic_gold(self):
        root=Path(__file__).resolve().parents[1]/"materials"
        probe_rows=[json.loads(x) for x in (root/"progress_probe.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
        pool_rows=[json.loads(x) for x in (root/"pool.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
        self.assertEqual(len({r["id"] for r in probe_rows}),len(probe_rows))
        self.assertTrue(all(r["split"]=="progress_probe" and r.get("target") for r in probe_rows))
        self.assertFalse({r["id"] for r in probe_rows}&{r["id"] for r in pool_rows})
        self.assertTrue(all(r["source"]=="synthetic:cpu-lab-progress-probe-v1" and r["privacy_checked"] is True for r in probe_rows))
        self.assertFalse(any("blind_set" in json.dumps(r).lower() or "set7" in json.dumps(r).lower() for r in probe_rows))


if __name__ == "__main__":
    unittest.main()
