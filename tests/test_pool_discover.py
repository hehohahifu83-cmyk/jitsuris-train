import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "materials"))
import pool_discover as D  # noqa: E402


class PoolDiscoverTests(unittest.TestCase):
    def test_title_key_merges_years(self):
        self.assertEqual(D.title_key("令和5年版 統計書 第2章"), D.title_key("令和6年版 統計書 第2章"))
        self.assertEqual(D.title_key("2019年度 決算"), D.title_key("2020年度 決算"))
        self.assertNotEqual(D.title_key("歳入"), D.title_key("歳出"))

    def test_bodik_picks_datastore_and_filters(self):
        pkgs = [
            {"name": "p1", "title": "令和5年 人口", "license_id": "cc-by-4.0", "metadata_modified": "2024", "resources": [{"id": "r1", "datastore_active": True}]},
            {"name": "p2", "title": "令和4年 人口", "license_id": "cc-by-4.0", "metadata_modified": "2023", "resources": [{"id": "r2", "datastore_active": True}]},
            {"name": "p3", "title": "犯罪の発生", "license_id": "cc-by-4.0", "metadata_modified": "2022", "resources": [{"id": "r3", "datastore_active": True}]},
            {"name": "p4", "title": "予算", "license_id": "cc-by-nc", "metadata_modified": "2022", "resources": [{"id": "r4", "datastore_active": True}]},
            {"name": "p5", "title": "施設一覧", "license_id": "cc-by-4.0", "metadata_modified": "2021", "resources": [{"id": "r5", "datastore_active": False}]},
            {"name": "p6", "title": "決算", "license_id": "cc-by", "metadata_modified": "2020", "resources": [{"id": "r6", "datastore_active": True}]},
        ]
        orig = D.get_json
        D.get_json = lambda url, tries=4: {"result": {"count": len(pkgs), "results": pkgs}}
        try:
            out, stats = D.bodik_candidates({"111111"})
        finally:
            D.get_json = orig
        self.assertEqual([x["resource_id"] for x in out], ["r1", "r6"])
        self.assertEqual(stats["same_title"], 1)
        self.assertEqual(stats["title_deny"], 1)
        self.assertEqual(stats["license"], 1)
        self.assertEqual(stats["no_datastore"], 1)
        self.assertTrue(out[0]["resource_url"].endswith("/dataset/p1/resource/r1"))


if __name__ == "__main__":
    unittest.main()
