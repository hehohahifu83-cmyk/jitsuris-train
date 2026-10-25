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

    def test_pool_valonly_same_validation_no_training_rows(self):
        code = "import encoder_exp as E; print(len(E.rows)); print(len(E.poolval)); print(len(E.pooltr))"
        def run(**env):
            out = subprocess.run([sys.executable, "-c", code], cwd=ROOT, env={**os.environ, **env}, capture_output=True, text=True, timeout=900)
            self.assertEqual(out.returncode, 0, out.stderr[-2000:])
            return [int(x) for x in out.stdout.strip().splitlines()[-3:]]
        base = run(FT_VAL="1")
        valonly = run(FT_VAL="1", FT_POOL_VALONLY="1")
        pool = run(FT_VAL="1", FT_POOL="1")
        self.assertEqual(base[0], valonly[0])      # 学習の行は教材庫なしと同じ
        self.assertEqual(valonly[2], 0)
        self.assertEqual(valonly[1], pool[1])      # 検証（教材庫）は FT_POOL=1 と同じ列
        self.assertGreater(valonly[1], 0)

    def test_pool_exclude_same_validation_fewer_training_rows(self):
        code = "import encoder_exp as E; print(len(E.poolval)); print(len(E.pooltr)); print(len({r[4] for r in E.pooltr} & E.pool_excluded_tables))"
        def run(**env):
            out = subprocess.run([sys.executable, "-c", code], cwd=ROOT, env={**os.environ, **env}, capture_output=True, text=True, timeout=900)
            self.assertEqual(out.returncode, 0, out.stderr[-2000:])
            return [int(x) for x in out.stdout.strip().splitlines()[-3:]]
        pool = run(FT_VAL="1", FT_POOL="1")
        excl = run(FT_VAL="1", FT_POOL="1", FT_POOL_EXCLUDE="b013,b014")
        self.assertEqual(pool[0], excl[0])         # 検証（教材庫）は同じ列
        self.assertLess(excl[1], pool[1])
        self.assertEqual(excl[2], 0)               # 外した陣の表は学習に残らない


if __name__ == "__main__":
    unittest.main()
