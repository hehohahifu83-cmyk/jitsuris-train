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

    def test_ckan_uses_host_and_publisher_id_and_counts_licenses(self):
        pkgs = [
            {"name": "orcamento", "title": "Orçamento 2024", "license_id": "cc-by", "metadata_modified": "2024", "resources": [{"id": "r1", "datastore_active": True}]},
            {"name": "obras", "title": "Obras", "license_id": "odc-odbl", "metadata_modified": "2023", "resources": [{"id": "r2", "datastore_active": True}]},
            {"name": "servidores", "title": "Remuneração dos servidores", "license_id": "cc-by", "metadata_modified": "2022", "resources": [{"id": "r3", "datastore_active": True}]},
            {"name": "parques", "title": "Parques", "license_id": "odc-pddl", "metadata_modified": "2021", "resources": [{"id": "r4", "datastore_active": True}]},
        ]
        seen = []
        orig = D.get_json
        D.get_json = lambda url, tries=4: (seen.append(url), {"result": {"count": len(pkgs), "results": pkgs}})[1]
        try:
            out, stats = D.ckan_candidates("dados.pbh.gov.br", {"belotur": "world_ckan_dados_pbh_gov_br_belotur"}, "ckan")
        finally:
            D.get_json = orig
        self.assertTrue(seen[0].startswith("https://dados.pbh.gov.br/api/3/action/package_search?"))
        self.assertEqual([x["resource_id"] for x in out], ["r1", "r4"])
        self.assertEqual({x["publisher_id"] for x in out}, {"world_ckan_dados_pbh_gov_br_belotur"})
        self.assertEqual({x["platform"] for x in out}, {"ckan"})
        self.assertEqual(out[0]["resource_url"], "https://dados.pbh.gov.br/dataset/orcamento/resource/r1")
        self.assertEqual(stats["license:odc-odbl"], 1)
        self.assertEqual(stats["title_deny"], 1)

    def test_portuguese_personal_columns_and_values_are_dropped(self):
        import fetch_rows as F
        for h in ("Nome do servidor", "CPF", "Endereço", "Telefone", "Logradouro", "CEP"):
            self.assertTrue(F.blocked_header(h), h)
        for h in ("Bairro", "Valor", "Secretaria", "Quantidade"):
            self.assertFalse(F.blocked_header(h), h)
        for v in ("123.456.789-01", "(31) 3277-1234", "30130-010", "Rua da Bahia, 1148"):
            self.assertTrue(F.sensitive_value(v), v)
        self.assertFalse(F.sensitive_value("R$ 1.234,56"))
        for h in ("namelast", "namefirst", "legalowner", "ContactPhone", "BusinessName"):   # 語がつながった列名
            self.assertTrue(F.blocked_header(h), h)
        for h in ("licstatus", "FY27 Budget", "Neighborhood", "result"):
            self.assertFalse(F.blocked_header(h), h)
        from pipeline import TITLE_DENY
        self.assertTrue(TITLE_DENY.search("Food Establishment Inspections"))

    def test_national_orgs_register_as_train_children_before_dataset_search(self):
        import json, shutil, tempfile
        tmp = Path(tempfile.mkdtemp()) / "allocation.json"
        shutil.copy(Path(__file__).resolve().parents[1] / "independent_eval" / "allocation.json", tmp)
        calls = []
        def fake(url, tries=4):
            calls.append(url)
            return {"result": ["abs", "bom"]} if "organization_list" in url else {"result": {"count": 0, "results": []}}
        orig, orig_nat = D.get_json, D.NATIONAL
        D.get_json, D.NATIONAL = fake, [{"parent": "australia", "host": "data.gov.au", "site": "https://data.gov.au/data"}]
        try:
            found, stats = D.register_national_orgs(tmp, "2026-10-24")
        finally:
            D.get_json, D.NATIONAL = orig, orig_nat
        self.assertTrue(all("package_search" not in u for u in calls), "組織の登録ではデータセットを見ない")
        pubs = {p["publisher_id"]: p["pool"] for p in json.loads(tmp.read_text(encoding="utf-8"))["publishers"]}
        self.assertEqual(pubs["australia:abs"], "train")
        self.assertEqual(pubs["australia:bom"], "train")
        self.assertEqual(found["data.gov.au"][1], {"abs": "australia:abs", "bom": "australia:bom"})
        self.assertEqual(stats["data.gov.au"], {"organizations": 2, "train": 2})

    def test_ogl_canada_is_allowed_and_odbl_is_not(self):
        from pipeline import ALLOWED_LICENSES, normalize_license
        self.assertIn(normalize_license("OGL-Canada-2.0"), ALLOWED_LICENSES)
        self.assertIn(normalize_license("odc-pddl"), ALLOWED_LICENSES)
        self.assertNotIn(normalize_license("odc-odbl"), ALLOWED_LICENSES)


if __name__ == "__main__":
    unittest.main()
