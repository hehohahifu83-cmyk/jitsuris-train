import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "materials"))
import fetch_rows as F  # noqa: E402
import pipeline as P  # noqa: E402


class SocrataTests(unittest.TestCase):
    def setUp(self):
        self.calls = []
        def fake(url, step="", tries=3):
            self.calls.append(url)
            if "/api/views/" in url:
                return {"licenseId": self.lic, "columns": [
                    {"fieldName": "fy", "name": "Fiscal Year", "dataTypeName": "text"},
                    {"fieldName": "amt", "name": "Amount", "dataTypeName": "number"},
                    {"fieldName": "geo", "name": "Location", "dataTypeName": "point"},
                    {"fieldName": ":id", "name": "id", "dataTypeName": "meta_data"}]}
            return [{"fy": "2020", "amt": "12.5", "geo": {"type": "Point"}}, {"fy": "2021", "amt": "13"}]
        self.orig = F.http_json
        F.http_json = fake
        self.item = {"n": 1, "publisher_id": "world_socrata_data_cityofchicago_org", "resource_url": "https://data.cityofchicago.org/x/abcd-1234",
                     "platform": "socrata", "host": "data.cityofchicago.org", "resource_id": "abcd-1234"}

    def tearDown(self):
        F.http_json = self.orig

    def test_socrata_maps_names_and_drops_geo(self):
        self.lic = "PUBLIC_DOMAIN"
        meta, fields, recs, total = F.fetch_table(self.item, set())
        self.assertEqual(fields, ["Fiscal Year", "Amount"])
        self.assertEqual(recs[0], {"Fiscal Year": "2020", "Amount": "12.5"})
        self.assertEqual(meta["license"], "public-domain")
        self.assertEqual(meta["language"], "en")
        self.assertTrue(any("%24order=%3Aid" in u for u in self.calls))

    def test_socrata_rejects_bad_license_and_mismatched_host(self):
        self.lic = "CC_BY_NC_40"
        with self.assertRaises(ValueError):
            F.fetch_table(self.item, set())
        self.lic = "PUBLIC_DOMAIN"
        bad = dict(self.item, publisher_id="world_socrata_data_other_gov")
        with self.assertRaises(ValueError):
            F.fetch_table(bad, set())

    def test_known_url_rejected(self):
        self.lic = "CC0_10"
        with self.assertRaises(ValueError):
            F.fetch_table(self.item, {"https://data.cityofchicago.org/resource/abcd-1234.json"})


class LicenseTitleTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(P.normalize_license("name-public-domain-public-domain"), "public-domain")
        self.assertEqual(P.normalize_license("name-creative-commons-1.0-universal-public-domain-dedication-logourl-images-licenses-cczero.png"), "public-domain")
        self.assertEqual(P.normalize_license("CC0_10"), "cc0")
        self.assertNotIn(P.normalize_license("cc-by-sa-4.0"), P.ALLOWED_LICENSES)
        self.assertNotIn(P.normalize_license("cc-by-nc"), P.ALLOWED_LICENSES)

    def test_title_deny(self):
        for t in ("Crime Reports", "Campaign Finance - FPPC Form 460", "311 OPCD Calls", "School Admission Offers",
                  "Internal Affairs Allegations", "Montgomery College Enrollment Data",
                  "KCPD Calls for Service 2023", "Building and Property Violations",
                  "Relação de Estudantes das Instituições da Rede Parceira", "Relação de Profissionais das Instituições da Rede Parceira",
                  "Resultado Concurso PBH Ativos 001/2018"):
            self.assertTrue(P.TITLE_DENY.search(t), t)
        self.assertFalse(P.TITLE_DENY.search("Budget - Operating Expenditures"))

    def test_license_spellings(self):
        for raw in ("https://creativecommons.org/licenses/by/4.0", "cc-by-2.5", "cc-by-3.0-au", "Creative Commons CC-BY 4.0",
                    "creative commons attribution 3.0 australia", "ca-ogl-lgo", "qc-cc-by"):
            self.assertIn(P.normalize_license(raw), P.ALLOWED_LICENSES, raw)
        for raw in ("cc-by-sa-4.0", "cc-by-nc-3.0-au", "cc-by-nd", "cc-nc-nd", "https://creativecommons.org/licenses/by-nc/4.0", "ab-ogla", "notspecified"):
            self.assertNotIn(P.normalize_license(raw), P.ALLOWED_LICENSES, raw)
        self.assertEqual(P.normalize_license("cc-by-4.0"), "cc-by-4.0")

    def test_license_from_extras_and_resources(self):
        self.assertEqual(P.license_from_pkg({"license_id": "", "license_title": "", "extras": [{"key": "利用規約", "value": "政府標準利用規約（第2.0版）"}]}), "cc-by-4.0")
        self.assertEqual(P.license_from_pkg({"license_id": None, "resources": [{"license": "CC BY 4.0"}]}), "cc-by-4.0")
        self.assertEqual(P.license_from_pkg({"license_id": "", "extras": [{"key": "theme", "value": "CC BY 4.0"}]}), "")
        self.assertNotIn(P.license_from_pkg({"license_id": "", "resources": [{"license": "CC BY-NC 4.0"}]}), P.ALLOWED_LICENSES)

    def test_blocked_header_initials(self):
        for h in ("INPUT BY", "PURCHASING AGENT", "Entered_By", "namelast", "legalowner"):
            self.assertTrue(F.blocked_header(h), h)
        for h in ("PURCHASE ORDER NUMBER", "TOTAL AMOUNT", "Agency", "COST CENTER"):
            self.assertFalse(F.blocked_header(h), h)


class CkanDatastoreFallbackTests(unittest.TestCase):
    """data.gov.au：datastore_search が HTTP 302 のとき、同じホストの CSV を読む（2026-10-24）。"""
    RID = "78a56b2c-1744-420e-8f38-bf24814d5039"

    def setUp(self):
        self.orig = (F.http_json, F.http_bytes)
        self.csv_url = f"https://data.gov.au/data/dataset/x/resource/{self.RID}/download/a.csv"
        def fake_json(url, step="", tries=3):
            if "resource_show" in url:
                return {"result": {"package_id": "p1", "url": self.csv_url, "format": self.fmt, "datastore_active": True}}
            if "package_show" in url:
                return {"result": {"license_id": "cc-by-4.0"}}
            raise RuntimeError("datastore_search: HTTP 302")
        F.http_json = fake_json
        F.http_bytes = lambda url, step="", tries=3, limit=0: ("year,count\n2020,5\n2021,7\n".encode(), False)
        self.item = {"n": 1, "publisher_id": "australia:x", "resource_url": f"https://data.gov.au/data/dataset/x/resource/{self.RID}",
                     "platform": "ckan", "host": "data.gov.au"}

    def tearDown(self):
        F.http_json, F.http_bytes = self.orig

    def test_falls_back_to_csv_on_same_host(self):
        self.fmt = "CSV"
        meta, fields, recs, total = F.fetch_table(self.item, set())
        self.assertEqual(fields, ["year", "count"])
        self.assertEqual(meta["access"], "csv")
        self.assertTrue(meta["datastore_failed"])

    def test_falls_back_to_csv_on_state_gov_au(self):
        # data.gov.au は州のポータルの目録で、ファイルは州のサイト（gov.au）にある（b009 で 110 表ほど。2026-10-24）
        self.fmt = "CSV"
        self.csv_url = "https://www.data.qld.gov.au/dataset/y/resource/z/download/a.csv"
        meta, fields, recs, total = F.fetch_table(self.item, set())
        self.assertEqual(meta["access"], "csv")
        self.assertTrue(P.host_in("data.sa.gov.au", P.csv_domains("data.gov.au")))
        self.assertFalse(P.host_in("gov.au.example.com", P.csv_domains("data.gov.au")))

    def test_uses_datastore_dump_when_no_csv(self):
        self.fmt = "XLSX"
        self.csv_url = f"https://data.gov.au/data/dataset/x/resource/{self.RID}/download/a.xlsx"
        seen = []
        def fake_bytes(url, step="", tries=3, limit=0):
            seen.append(url)
            return "year,count\n2020,5\n".encode(), False
        F.http_bytes = fake_bytes
        meta, fields, recs, total = F.fetch_table(self.item, set())
        self.assertEqual(seen, [f"https://data.gov.au/data/datastore/dump/{self.RID}"])
        self.assertEqual(meta["access"], "datastore_dump")

    def test_error_names_format_and_host_when_all_fail(self):
        self.fmt = "XLSX"
        self.csv_url = f"https://example.org/a.xlsx"
        def fail(url, step="", tries=3, limit=0):
            raise RuntimeError(f"{step}: HTTP 302")
        F.http_bytes = fail
        with self.assertRaisesRegex(RuntimeError, "XLSX on example.org"):
            F.fetch_table(self.item, set())


if __name__ == "__main__":
    unittest.main()
