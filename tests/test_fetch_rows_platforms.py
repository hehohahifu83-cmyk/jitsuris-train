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
                  "Internal Affairs Allegations", "Montgomery College Enrollment Data"):
            self.assertTrue(P.TITLE_DENY.search(t), t)
        self.assertFalse(P.TITLE_DENY.search("Budget - Operating Expenditures"))

    def test_blocked_header_initials(self):
        for h in ("INPUT BY", "PURCHASING AGENT", "Entered_By", "namelast", "legalowner"):
            self.assertTrue(F.blocked_header(h), h)
        for h in ("PURCHASE ORDER NUMBER", "TOTAL AMOUNT", "Agency", "COST CENTER"):
            self.assertFalse(F.blocked_header(h), h)


if __name__ == "__main__":
    unittest.main()
