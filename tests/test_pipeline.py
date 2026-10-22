import unittest

from materials import pipeline as P


def cand(pub="111111", rid="00000000-0000-0000-0000-000000000001", lic="cc-by-4.0", ds=True, heads=("a", "b")):
    return {"publisher_id": pub, "resource_url": f"https://data.bodik.jp/dataset/x/resource/{rid}", "resource_id": rid,
            "license": {"id": lic}, "datastore_available": ds, "safe_headers": list(heads), "title": "t"}


def rid(n):
    return f"00000000-0000-0000-0000-{n:012d}"


class AdoptTests(unittest.TestCase):
    pools = {"111111": "train", "222222": "eval2"}

    def run_adopt(self, cands, known_urls=(), known_rids=(), pool_pub=None, pool_hsets=None):
        return P.adopt(cands, self.pools, set(known_urls), set(known_rids), P.Counter(pool_pub or {}), P.Counter(pool_hsets or {}))

    def test_rules(self):
        cands = [cand(rid=rid(1)), cand(pub="222222", rid=rid(2)), cand(rid=rid(3), lic="cc-by-nc"),
                 cand(rid=rid(4), ds=False), cand(rid=rid(1)), cand(rid=rid(5), heads=("c",)), cand(rid=rid(6), heads=("d",)),
                 cand(rid=rid(7), heads=("e",))]
        adopted, why = self.run_adopt(cands)
        self.assertEqual([a["resource_url"][-12:] for a in adopted], ["000000000001", "000000000005", "000000000006"])
        self.assertEqual(why["公開元が train でない"], 1)
        self.assertEqual(why["ライセンスが許可の一覧にない"], 1)
        self.assertEqual(why["もう使った表"], 1)
        self.assertEqual(why["この陣で 1 公開元 3 表まで"], 1)

    def test_known_and_pool_caps(self):
        adopted, why = self.run_adopt([cand(rid=rid(1))], known_rids={rid(1)})
        self.assertEqual(adopted, [])
        adopted, why = self.run_adopt([cand(rid=rid(2))], pool_pub={"111111": 15})
        self.assertEqual(why["教材庫で 1 公開元 15 表まで"], 1)
        adopted, why = self.run_adopt([cand(rid=rid(3))], pool_hsets={("111111", frozenset({"a", "b"})): 3})
        self.assertEqual(why["同じ公開元で見出しの組が同じ表が 3 つ以上"], 1)


def corpus(n):
    return [{"table": f"t{i // 3}", "header": h, "values": ["1"], "context": [], "publisher": "111111"}
            for i, h in enumerate(["金額", "数量", "日付"] * (n // 3))]


class ReconcileFinalizeTests(unittest.TestCase):
    def setUp(self):
        self.c = corpus(60)
        self.l = [{"table": r["table"], "header": r["header"], "label": "amount" if i % 3 == 0 else "quantity" if i % 3 == 1 else "date", "teacher": "chatgpt-x"} for i, r in enumerate(self.c)]
        self.p = [{"guarded_prediction": l["label"]} for l in self.l]
        self.p[0] = {"guarded_prediction": "quantity"}   # 金額↔数量の食い違い
        self.p[2] = {"guarded_prediction": "id"}
        self.split, self.rows = P.reconcile(self.c, self.l, self.p, seed="s")

    def test_reconcile_orders_and_audits(self):
        self.assertEqual(self.split["disagree"][0], 0)   # 金額↔数量が先
        self.assertEqual(len(self.split["audit"]), 10)
        self.assertEqual(self.split, P.reconcile(self.c, self.l, self.p, seed="s")[0])

    def test_finalize_requires_decisions_and_blocks_bad_audit(self):
        with self.assertRaises(ValueError):
            P.finalize(self.c, self.l, self.p, self.rows, [], "b1", "chatgpt-x")
        good = [{"i": r["i"], "label": self.l[r["i"]]["label"] if r["kind"] == "audit" else "amount", "reason": "r"} for r in self.rows if r["kind"] != "dropped"]
        out, record, stat, audit = P.finalize(self.c, self.l, self.p, self.rows, good, "b1", "chatgpt-x")
        self.assertEqual(len(out), 60)
        self.assertEqual(audit["audit_errors"], 0)
        bad = [dict(d, label="other") if r["kind"] == "audit" else d for d, r in zip(good, [r for r in self.rows if r["kind"] != "dropped"])]
        with self.assertRaisesRegex(ValueError, "5%"):
            P.finalize(self.c, self.l, self.p, self.rows, bad, "b1", "chatgpt-x")

    def test_mismatched_rows_rejected(self):
        bad = [dict(self.l[0], header="x")] + self.l[1:]
        with self.assertRaises(ValueError):
            P.reconcile(self.c, bad, self.p, seed="s")


if __name__ == "__main__":
    unittest.main()
