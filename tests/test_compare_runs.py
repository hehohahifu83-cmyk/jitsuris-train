import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import compare_runs as C

A = """# 学習済みモデルの微調整（集計）

### Kaggle GPU 2026-10-17 23:31（試験：開発用220, 本物（一般））
| hfmodel/x 微調整 2.0周・微調整だけ | 開発用220 正97.7% 誤4 不明1 重大1 | 本物（一般） 正90.8% 誤6 不明21 重大1 その他見送り85/88 | 学習 8477秒 |
| hfmodel/x 微調整 2.0周・今の仕組みだけ | 開発用220 正88.2% 誤18 不明8 重大2 | 本物（一般） 正84.4% 誤14 不明32 重大1 その他見送り79/88 | 学習 8533秒 |
"""

B_SAME = """
### Kaggle GPU 仕事1（FT_SORT=1）2026-10-18 03:30（試験：開発用220, 本物（一般））
| hfmodel/x 微調整 2.0周・微調整だけ | 開発用220 正97.3% 誤5 不明1 重大1 | 本物（一般） 正90.2% 誤7 不明22 重大2 その他見送り84/88 | 学習 1900秒・評価 120秒 |
| hfmodel/x 微調整 2.0周・今の仕組みだけ | 開発用220 正88.2% 誤18 不明8 重大2 | 本物（一般） 正84.4% 誤14 不明32 重大1 その他見送り79/88 | 学習 1910秒・評価 120秒 |
"""

B_AUG = """
### Kaggle GPU 仕事2（FT_SORT=1 FT_AUG=1）2026-10-18 03:30（試験：開発用220, 本物（一般））
| hfmodel/x 微調整 2.0周・水増し・微調整だけ | 開発用220 正95.0% 誤9 不明1 重大3 | 本物（一般） 正93.0% 誤3 不明18 重大0 その他見送り85/88 | 学習 1920秒・評価 120秒 |
"""


class CompareRunsTest(unittest.TestCase):
    def test_parse_cells_and_both_second_formats(self):
        secs = C.parse_sections(A + B_SAME)
        self.assertEqual(len(secs), 2)
        r = secs[0]["rows"][0]
        self.assertEqual(r["cond"], "微調整だけ")
        self.assertEqual(r["tests"]["開発用220"], {"acc": 97.7, "wrong": 4, "unk": 1, "crit": 1, "oc": None, "ot": None})
        self.assertEqual(r["tests"]["本物（一般）"]["oc"], 85)
        self.assertEqual((r["train"], r["eval"]), (8477, None))
        self.assertEqual((secs[1]["rows"][0]["train"], secs[1]["rows"][0]["eval"]), (1900, 120))

    def test_within_noise_is_no_difference(self):
        secs = C.parse_sections(A + B_SAME)
        table, summary, out = C.compare(secs[0], secs[1])
        self.assertEqual(out, [])
        self.assertIn("差は 1.5 ポイント未満", summary)
        self.assertIn("4.46 倍", summary)  # 8477 / 1900
        self.assertIn("| 本物（一般） | 90.8% | 90.2% | -0.6 | 差なし | 1 | 2 |", table)

    def test_boundary_is_not_noise(self):
        self.assertEqual(C.verdict(1.4), "差なし")
        self.assertEqual(C.verdict(-1.4), "差なし")
        self.assertEqual(C.verdict(1.5), "上がった")
        self.assertEqual(C.verdict(-1.5), "下がった")

    def test_aug_row_has_its_own_condition_name_and_is_not_matched_with_base(self):
        secs = C.parse_sections(A + B_AUG)
        self.assertTrue(secs[1]["rows"][0]["aug"])
        self.assertEqual(secs[1]["rows"][0]["cond"], "微調整だけ")  # 条件名は同じ（水増しの有無は別に持つ）
        table, summary, out = C.compare(secs[0], secs[1])
        names = [n for (_, n, _, _) in out]
        self.assertIn("開発用220", names)   # 97.7 → 95.0 は 2.7 下がった
        self.assertIn("本物（一般）", names)  # 90.8 → 93.0 は 2.2 上がった

    def test_pick_requires_exactly_one_section(self):
        secs = C.parse_sections(A + B_SAME + B_AUG)
        with self.assertRaises(SystemExit):
            C.pick(secs, "Kaggle GPU")      # 3 件
        with self.assertRaises(SystemExit):
            C.pick(secs, "存在しない")        # 0 件
        self.assertIn("仕事1", C.pick(secs, "仕事1（")["heading"])

    def test_blind_sets_are_refused(self):
        text = "### Kaggle GPU 2026-10-18 01:00（試験：blind_set3）\n| m 微調整 2.0周・微調整だけ | blind_set3 正90.0% 誤1 不明1 重大0 | 学習 10秒 |\n"
        secs = C.parse_sections(text)
        with self.assertRaises(SystemExit):
            C.pick(secs, "blind")


if __name__ == "__main__":
    unittest.main()
