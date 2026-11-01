"""直し H の候補（research/fixes/fixes_h.py）の小さな試験。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "research", "fixes"))
import fixes_h as H  # noqa: E402


class TypeCodeHeader(unittest.TestCase):
    def test_type_codes(self):
        for h in ["gebaeudekategorie_code", "hh_typ_nr", "NACE Code", "Naics code\nCode Scian", "中分類コード", "heizsystem_code"]:
            self.assertTrue(H.type_code_header(h), h)

    def test_not_type_codes(self):
        for h in ["Code", "formular_id", "quartier_bfs_nr", "typengenehmigungs_nr", "Obj-cat-code_Code-cat-art", "PRODUKT_ID"]:
            self.assertFalse(H.type_code_header(h), h)

    def test_h1_needs_category_in_top3(self):
        c = {"header": "hh_typ_nr", "top3": [{"label": "id"}, {"label": "quantity"}]}
        self.assertEqual(H.h1("id", c), "id")
        c["top3"].append({"label": "category"})
        self.assertEqual(H.h1("id", dict(c, top3=c["top3"][1:])), "category")
        self.assertEqual(H.h1("quantity", c), "quantity")


class DateShape(unittest.TestCase):
    def test_dates(self):
        self.assertTrue(H.date_shape("FR_MOIS", ["nov.", "juil.", "sept."]))
        self.assertTrue(H.date_shape("FR_TRIMESTRE", ["T3", "T1"]))
        self.assertTrue(H.date_shape("指定有効期限", ["46295", "44957.0"]))
        self.assertTrue(H.date_shape("measured_at", ["1723010401.69"]))

    def test_not_dates(self):
        self.assertFalse(H.date_shape("日数", ["12", "3"]))
        self.assertFalse(H.date_shape("DAY_SURV", ["4", "27"]))
        self.assertFalse(H.date_shape("金額", ["46295"]))

    def test_h2_only_from_unknown(self):
        c = {"header": "FR_MOIS", "values": ["nov.", "juin"]}
        self.assertEqual(H.h2("unknown", c), "date")
        self.assertEqual(H.h2("category", c), "category")


if __name__ == "__main__":
    unittest.main()
