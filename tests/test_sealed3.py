import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "independent_eval"))
import sealed2 as S2  # noqa: E402
import sealed3 as S3  # noqa: E402


class Sealed3Tests(unittest.TestCase):
    def test_adopt_only_eval3(self):
        cands = [{"publisher_id": "a", "pool": "eval3", "resource_url": "https://x/1", "resource_id": "r1", "license_id": "cc-by",
                  "datastore_available": True, "title": "budget", "catalog_url": "https://data.bodik.jp/x"},
                 {"publisher_id": "b", "pool": "eval2", "resource_url": "https://x/2", "resource_id": "r2", "license_id": "cc-by",
                  "datastore_available": True, "title": "budget", "catalog_url": "https://data.bodik.jp/x"}]
        out, why = S2.adopt(cands, {"a": "eval3", "b": "eval2"}, set(), set(), pool="eval3", per_publisher=20)
        self.assertTrue(all(x["publisher_id"] == "a" for x in out))
        self.assertEqual(why["公開元が eval3 でない"], 1)

    def test_freeze_keeps_table_rows_and_sizes(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            work, out = d / "work", d / "out"
            work.mkdir()
            rows = []
            for t in range(30):
                for c in range(12):
                    rows.append({"table": f"https://u/{t}", "publisher": f"p{t % 12}", "header": f"h{t}_{c}", "values": [str(c)] * 5,
                                 "row_values": [str(c + k) for k in range(20)], "row_index": list(range(0, 40, 2)),
                                 "datastore_total": 99, "context": [f"h{t}_{k}" for k in range(12) if k != c], "language": "ja", "license": "cc-by"})
            (work / "corpus.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
            (work / "adopted.json").write_text(json.dumps({"adopted": []}), encoding="utf-8")
            old = (S3.WORK, S3.OUT, S2.pools, S2.training_headers)
            S3.WORK, S3.OUT = work, out
            S2.pools = lambda: {f"p{k}": "eval3" for k in range(12)}
            S2.training_headers = lambda: set()
            try:
                S3.cmd_freeze(SimpleNamespace(allow_small=True))
            finally:
                S3.WORK, S3.OUT, S2.pools, S2.training_headers = old
            s = json.loads((out / "sealed3.json").read_text(encoding="utf-8"))
            tr = json.loads((out / "table_rows.json").read_text(encoding="utf-8"))["tables"]
            self.assertTrue(all(len(c["values"]) <= 5 for c in s["columns"]))
            per_table = {}
            for c in s["columns"]:
                per_table[c["table"]] = per_table.get(c["table"], 0) + 1
            self.assertLessEqual(max(per_table.values()), S2.COLS_PER_TABLE)
            t1 = tr[s["columns"][0]["table"]]
            self.assertEqual(len(t1), 12)                      # 選ばなかった列も表の特徴のために残す
            self.assertEqual(len(t1[0]["rows"]), 20)
            self.assertEqual(sum(1 for x in t1 if x["column"]), per_table[s["columns"][0]["table"]])
            prov = json.loads((out / "provenance.json").read_text(encoding="utf-8"))
            self.assertFalse(prov["values_viewed"])
            self.assertIn("table_rows_sha256", prov)


if __name__ == "__main__":
    unittest.main()
