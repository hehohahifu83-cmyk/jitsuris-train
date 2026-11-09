"""F1（hold の評価の陣）の候補探し：登録しない・別名で自治体コードにつなぐ・外した組織は探さない（2026-11-09）。"""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "materials")); sys.path.insert(0, str(ROOT / "independent_eval"))
import pool_discover as D  # noqa: E402


class F1DiscoverTests(unittest.TestCase):
    def test_hold_registration_uses_aliases_only(self):
        alloc = {"schema_version": 1, "aliases": {"odp_jig:jp-fukui-sabae": "182079"},
                 "publishers": [{"publisher_id": "182079", "pool": "hold", "date": "2026-11-05"},
                                {"publisher_id": "222241", "pool": "train", "date": "2026-11-05"}]}
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "allocation.json"
            p.write_text(json.dumps(alloc))
            names = ["jp-fukui-sabae", "jp-shizuoka-kikugawa", "jp-go-soumu-stat"]
            with patch.object(D, "get_json", return_value={"result": names}), patch.object(D, "POOL_NAME", "hold"):
                found, stats = D.register_national_orgs(p, "2026-11-09", only=("ckan.odp.jig.jp",))
            after = json.loads(p.read_text())
        self.assertEqual(found["ckan.odp.jig.jp"][1], {"jp-fukui-sabae": "182079"})   # 外した組織（別名なし）は探さない
        self.assertEqual(after["publishers"], alloc["publishers"])                      # 登録しない
        self.assertNotIn("data.e-gov.go.jp", found)                                     # train のカタログは hold のとき探さない

    def test_train_skips_f1_catalogs(self):
        with patch.object(D, "POOL_NAME", "train"), patch.object(D, "get_json", side_effect=AssertionError("呼ばない")):
            with tempfile.TemporaryDirectory() as td:
                p = Path(td) / "allocation.json"
                p.write_text(json.dumps({"schema_version": 1, "aliases": {}, "publishers": []}))
                found, _ = D.register_national_orgs(p, "2026-11-09", only=("ckan.odp.jig.jp",))
        self.assertEqual(found, {})


if __name__ == "__main__":
    unittest.main()
