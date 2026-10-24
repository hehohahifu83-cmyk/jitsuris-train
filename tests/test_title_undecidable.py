import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from encoder_context import TITLE_SEP, format_encoder_text


class TitleTextTest(unittest.TestCase):
    row = ("Total", ["12", "34"], "", ["Year", "Type"], "UNIT: Number")

    def test_default_text_unchanged(self):
        old = "query: 列名: Total | 値: 12, 34 | 同じ表の列: Year, Type"
        self.assertEqual(format_encoder_text(self.row, "query: "), old)
        self.assertEqual(format_encoder_text(self.row, "query: ", ctx_unit=True), old + " | 同じ表の単位列の値: UNIT: Number")

    def test_title_only_when_enabled(self):
        r = self.row[:4] + ("UNIT: Number" + TITLE_SEP + "Calls answered",)
        self.assertNotIn("題名", format_encoder_text(r, ""))
        self.assertEqual(format_encoder_text(r, "", ctx_unit=True), format_encoder_text(self.row, "", ctx_unit=True))
        t = format_encoder_text(r, "", title=True)
        self.assertIn("| 表の題名: Calls answered | 同じ表の列", t)


class EncoderExpEnvTest(unittest.TestCase):
    def run_env(self, **env):
        code = "import encoder_exp as E, collections; print(len(E.rows)); print(sum(1 for r in E.rows if r[2]=='other'))"
        out = subprocess.run([sys.executable, "-c", code], cwd=ROOT, env={**os.environ, **env}, capture_output=True, text=True, timeout=900)
        self.assertEqual(out.returncode, 0, out.stderr[-2000:])
        return [int(x) for x in out.stdout.strip().splitlines()[-2:]], out.stdout

    def test_undecidable_adds_other_rows_only_on_train_side(self):
        (n0, o0), _ = self.run_env(FT_POOL="1", FT_VAL="1")
        (n1, o1), log = self.run_env(FT_POOL="1", FT_VAL="1", FT_POOL_UNDECIDABLE="2", FT_TITLE="1")
        self.assertGreater(n1, n0)
        self.assertEqual(n1 - n0, o1 - o0)         # 足したのは other の行だけ
        self.assertIn("FT_TITLE=1: table titles", log)


if __name__ == "__main__":
    unittest.main()
