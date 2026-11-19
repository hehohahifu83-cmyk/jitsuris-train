"""G4 の道具（independent_eval/g4.py）の試験（2026-11-18 Claude）。採用の決まり・控え・除外・文脈の作り方と照合。実際の候補・値は使わない。"""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "independent_eval"))
import g4 as G  # noqa: E402


def cand(pub, ds, rid, lic="ogla", host="open.alberta.ca", title="Budget"):
    return {"publisher_id": pub, "pool": "hold", "platform": "ckan", "title": title, "resource_name": "CSV",
            "resource_url": f"https://{host}/dataset/{ds}/resource/{rid}", "resource_id": rid, "license": {"id": lic},
            "datastore_available": True, "access": "datastore"}


A, B, U = "alberta_cat:a-org", "govdata_cat:b-org", "alberta_cat:used-org"
POOLS = {A: "hold", B: "hold", U: "hold", "ontario_cat:o": "hold", "alberta_cat:train": "train"}


class AdoptTest(unittest.TestCase):
    def run_rule(self, cands, urls=(), rids=(), dss=()):
        return G.adopt_rule(cands, POOLS, {U}, set(urls), set(rids), set(dss))

    def test_drops_used_and_wrong_catalogs(self):
        cs = [cand(U, "d1", "r1"), cand("ontario_cat:o", "d2", "r2", host="data.ontario.ca"), cand("alberta_cat:train", "d3", "r3"),
              cand(A, "d4", "r4", lic="all-rights"), cand(A, "d5", "r5", title="Student enrolment"), cand(A, "d6", "r6")]
        adopted, _, why = self.run_rule(cs)
        self.assertEqual([x["resource_id"] for x in adopted], ["r6"])
        self.assertEqual(why["G1〜G3 で表を採った公開元"], 1)
        self.assertEqual(why["カタログが Alberta・GovData.de でない"], 1)
        self.assertEqual(why["公開元が hold でない"], 1)

    def test_used_resources_and_datasets(self):
        cs = [cand(A, "d1", "r1"), cand(A, "d2", "r2"), cand(A, "d3", "r3")]
        adopted, _, why = self.run_rule(cs, urls={cs[0]["resource_url"]}, dss={("open.alberta.ca", "d2")})
        self.assertEqual([x["resource_id"] for x in adopted], ["r3"])
        self.assertEqual(why["使い済みのデータセット"], 1)

    def test_one_table_per_dataset_and_caps_and_reserves(self):
        cs = [cand(A, f"d{i}", f"r{i}") for i in range(8)] + [cand(A, "d0", "r0b")]
        adopted, reserves, why = self.run_rule(cs)
        self.assertEqual(len(adopted), G.TABLES_PER_PUBLISHER)
        self.assertEqual(len(reserves[A]), G.RESERVES_PER_PUBLISHER)
        self.assertEqual(why["同じデータセットの 2 つ目より後"], 1)
        # 決まった順（h の順）で、並べ替えても同じ
        again, res2, _ = self.run_rule(list(reversed(cs)))
        self.assertEqual(adopted, again)
        self.assertEqual(reserves, res2)
        order = sorted((c for c in cs if c["resource_id"] != "r0b" or True), key=lambda c: G.h(c["resource_id"]))
        firsts = []
        seen = set()
        for c in order:
            k = G.dataset_key(c["resource_url"])
            if k not in seen:
                seen.add(k)
                firsts.append(c["resource_id"])
        self.assertEqual([x["resource_id"] for x in adopted], firsts[:G.TABLES_PER_PUBLISHER])

    def test_global_cap(self):
        old = G.MAX_TABLES
        G.MAX_TABLES = 2
        try:
            cs = [cand(A, "d1", "r1"), cand(B, "d2", "r2", host="ckan.govdata.de", lic="dl-de-by-2.0"), cand(A, "d3", "r3")]
            adopted, _, why = self.run_rule(cs)
            self.assertEqual(len(adopted), 2)
            self.assertEqual(why["全体で 2 表まで"], 1)
        finally:
            G.MAX_TABLES = old


def crow(table, header, vals, idx, pub=A):
    return {"table": table, "header": header, "values": vals[:5], "row_values": vals, "row_index": idx, "context": [], "publisher": pub,
            "language": "en", "license": "ogla", "resource_page": table}


class FreezeTest(unittest.TestCase):
    def rows(self):
        idx = [4, 9, 12]
        return [crow("https://x/t1.csv", "When", ["2010", "2011", "2012"], idx), crow("https://x/t1.csv", "ValueType", ["dollars"] * 3, idx),
                crow("https://x/t1.csv", "Alberta", ["1", "2", "3"], idx),
                crow("https://x/t2.csv", "A", ["1", "2"], [1, 2]), crow("https://x/t2.csv", "B", ["x", "y"], [1, 3])]

    def test_build_and_check(self):
        rows = self.rows()
        doc, meta, sel = G.build_set(rows)
        self.assertEqual(set(doc["row_context"]) | set(doc["row_context_none"]), {c["table"] for c in doc["columns"]})
        self.assertIn("列ごとに row_index が違う", doc["row_context_none"].values())
        t1 = next(t for t, c in doc["row_context"].items())
        self.assertEqual(doc["row_context"][t1]["headers"], [c["header"] for c in doc["columns"] if c["table"] == t1])
        self.assertTrue(G.check_set(doc, rows))

    def test_check_rejects_tampering(self):
        rows = self.rows()
        doc, _, _ = G.build_set(rows)
        t1 = next(iter(doc["row_context"]))
        for bad in ({**doc, "row_context_none": {**doc["row_context_none"], t1: "x"}},
                    {**doc, "row_context": {t1: {**doc["row_context"][t1], "rows": [["9", "9", "9"]]}}}):
            with self.assertRaises(SystemExit):
                G.check_set(bad, rows)

    def test_unit_only_from_set_columns(self):
        # 表 u1 は 12 列で、Unit の列はハッシュの順で必ず選ばれない（固定の例。選ばれないことも確かめる）
        t = "https://x/u1.csv"
        rows = [crow(t, f"extra{i}", ["u"] * 3, [4, 9, 12]) for i in range(11)] + [crow(t, "Unit", ["SECRETUNIT"] * 3, [4, 9, 12])]
        doc, _, sel = G.build_set(rows)
        self.assertNotIn("Unit", {r["header"] for r in sel})
        self.assertTrue(all("SECRETUNIT" not in c["unit"] for c in doc["columns"]))
        self.assertNotIn("SECRETUNIT", str(doc["row_context"]))
        self.assertNotIn("SECRETUNIT", str(doc))

    def test_context_values_per_table(self):
        # 別の表の同じ名前の列の値を混ぜた文脈を拒否する（再生成の一致とは別の照合）
        idx = [1, 2]
        rows = [crow("https://x/a.csv", "Name", ["alpha", "beta"], idx), crow("https://x/a.csv", "N", ["1", "2"], idx),
                crow("https://x/b.csv", "Name", ["gamma", "delta"], idx), crow("https://x/b.csv", "M", ["3", "4"], idx)]
        doc, _, sel = G.build_set(rows)
        G.check_context_values(doc, sel)
        ta = next(t for t, c in doc["row_context"].items() if "N" in c["headers"])
        bad = {**doc, "row_context": {**doc["row_context"], ta: {**doc["row_context"][ta],
               "rows": [[("gamma" if h == "Name" else v) for h, v in zip(doc["row_context"][ta]["headers"], r)] for r in doc["row_context"][ta]["rows"]]}}}
        with self.assertRaises(SystemExit):
            G.check_context_values(bad, sel)


def ent(url, pub=A, batch="g4", replaces=None):
    e = {"resource_url": url, "publisher_id": pub, "batch": batch}
    if replaces:
        e["replaces"] = replaces
    return e


class CorpusJoinTest(unittest.TestCase):
    def row(self, page, table=None, pub=A, batch="g4"):
        return {"table": table or page + ".csv", "resource_page": page, "publisher": pub, "batch_src": batch, "header": "h"}

    def test_ok_and_missing(self):
        e = {"p1": ent("p1"), "p2": ent("p2"), "p3": ent("p3", batch="g4x", replaces="p2")}
        rows = [self.row("p1"), self.row("p3", batch="g4x")]
        self.assertEqual(G.check_corpus(rows, e), 1)   # p2 は取れず、p3 が置き換え

    def test_rejects(self):
        e = {"p1": ent("p1"), "p2": ent("p2"), "p3": ent("p3", batch="g4x", replaces="p2")}
        bads = [[self.row("zz")],                                        # 採用していない表
                [self.row("p1"), self.row("p1", table="other.csv")],    # 同じ資源が 2 つの表
                [self.row("p1", pub=B)],                                 # 公開元が違う
                [self.row("p1", batch="g4x")],                           # 取り出しが違う
                [self.row("p2"), self.row("p3", batch="g4x")],           # 置き換えた元も入っている
                [self.row("p1", table="same.csv"), self.row("p2", table="same.csv")]]   # 別の資源が同じ表
        for rows in bads:
            with self.assertRaises(SystemExit):
                G.check_corpus(rows, e)


class AtomicFreezeTest(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp = tempfile.mkdtemp()
        self.old = (G.WORK, G.WORK_X, G.pools, G.used_publishers)
        from pathlib import Path
        G.WORK, G.WORK_X = Path(self.tmp) / "g4", Path(self.tmp) / "g4x"
        G.pools = lambda: {A: "hold"}
        G.used_publishers = lambda: set()
        idx = [4, 9, 12]
        self.rows = [dict(crow("https://x/t1.csv", "When", ["2010", "2011", "2012"], idx), batch_src="g4", resource_page="p1"),
                     dict(crow("https://x/t1.csv", "Alberta", ["1", "2", "3"], idx), batch_src="g4", resource_page="p1")]
        self.ent = {"p1": ent("p1")}

    def tearDown(self):
        import shutil
        G.WORK, G.WORK_X, G.pools, G.used_publishers = self.old
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_ok_then_refuse_existing(self):
        from pathlib import Path
        out = Path(self.tmp) / "out" / "g4"
        G.atomic_freeze(out, self.rows, self.ent)
        self.assertEqual(sorted(p.name for p in out.iterdir()), ["g4.json", "provenance.json", "titles.json"])
        with self.assertRaises(SystemExit):
            G.atomic_freeze(out, self.rows, self.ent)
        self.assertEqual([p.name for p in out.parent.iterdir()], ["g4"])   # 一時ディレクトリが残らない

    def test_failure_leaves_nothing(self):
        from pathlib import Path
        out = Path(self.tmp) / "out2" / "g4"
        with self.assertRaises(SystemExit):
            G.atomic_freeze(out, self.rows + [dict(self.rows[0], resource_page="zz", table="https://x/z.csv")], self.ent)
        self.assertFalse(out.exists())
        self.assertEqual(list(out.parent.iterdir()), [])
        orig = G.check_set
        G.check_set = lambda doc, rows: (_ for _ in ()).throw(SystemExit("照合の失敗"))
        try:
            with self.assertRaises(SystemExit):
                G.atomic_freeze(out, self.rows, self.ent)
        finally:
            G.check_set = orig
        self.assertFalse(out.exists())
        self.assertEqual(list(out.parent.iterdir()), [])


class NoSealedTest(unittest.TestCase):
    def test_does_not_open_sealed(self):
        import subprocess
        code = ("import sys\nopened=[]\nsys.addaudithook(lambda e,a: opened.append(a[0]) if e=='open' and isinstance(a[0],str) else None)\n"
                "sys.path.insert(0,'independent_eval')\nimport g4\ng4.used_resources(); g4.used_publishers(); g4.pools()\n"
                "bad=[p for p in opened if 'sealed' in p or 'blind_set' in p or 'b018' in p]\nprint(len(bad))\n")
        out = subprocess.run([sys.executable, "-c", code], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        self.assertEqual(out, "0")
        self.assertNotIn("sealed2", sys.modules)


if __name__ == "__main__":
    unittest.main()
