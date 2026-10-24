import sys
import unittest
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "independent_eval"))
import sealed2 as S  # noqa: E402


def rows_for(n_tables, cols, pub=lambda t: f"p{t % 20}", heads=lambda t, c: f"h{t}_{c}"):
    return [{"table": f"u{t}", "publisher": pub(t), "header": heads(t, c), "values": ["1"], "language": "ja"}
            for t in range(n_tables) for c in range(cols)]


class Sealed2Tests(unittest.TestCase):
    def test_caps_columns_per_table_and_publisher_share(self):
        rows = rows_for(100, 14)
        cols, _ = S.select(rows, set())
        per_table = Counter(rows[i]["table"] for i in cols)
        self.assertLessEqual(max(per_table.values()), S.COLS_PER_TABLE)
        per_pub = Counter(rows[i]["publisher"] for i in cols)
        self.assertLessEqual(max(per_pub.values()), S.PUBLISHER_SHARE * len(cols))

    def test_same_header_sets_at_most_two_tables(self):
        rows = rows_for(40, 3, pub=lambda t: f"p{t}", heads=lambda t, c: f"same{c}" if t < 10 else f"h{t}_{c}")
        cols, stats = S.select(rows, set())
        same = {rows[i]["table"] for i in cols if rows[i]["header"].startswith("same")}
        self.assertEqual(len(same), 2)
        self.assertEqual(stats["drop_same_headers"], 8)

    def test_known_headers_at_most_20_percent(self):
        rows = rows_for(40, 10, heads=lambda t, c: "known" if c < 5 else f"h{t}_{c}")
        rows = [dict(r, header=r["header"] + ("" if r["header"] != "known" else r["table"])) for r in rows]
        train = {S.norm(r["header"]) for r in rows if r["header"].startswith("known")}
        cols, _ = S.select(rows, train)
        known = sum(S.norm(rows[i]["header"]) in train for i in cols)
        self.assertLessEqual(known, 0.2 * len(cols) + 1e-9)
        self.assertGreater(known, 0)

    def test_adopt_only_eval2(self):
        c = {"publisher_id": "a", "pool": "eval2", "resource_url": "https://data.bodik.jp/dataset/x/resource/" + "0" * 8 + "-0000-0000-0000-" + "0" * 12,
             "resource_id": "r1", "license": {"id": "cc-by-4.0"}, "datastore_available": True, "title": "予算"}
        out, why = S.adopt([c, dict(c, publisher_id="b", resource_id="r2")], {"a": "eval2", "b": "train"}, set(), set())
        self.assertEqual([x["publisher_id"] for x in out], ["a"])
        self.assertEqual(why["公開元が eval2 でない"], 1)


if __name__ == "__main__":
    unittest.main()
