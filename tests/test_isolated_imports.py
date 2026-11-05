"""Actions は python -I（スクリプトのフォルダが import の探し先に入らない）で動かす。その形で shirasagi の候補を扱えるか（2026-11-05）。"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class IsolatedImportTests(unittest.TestCase):
    def test_pipeline_platform_of_shirasagi_under_python_I(self):
        code = (
            "import runpy\n"
            f"m = runpy.run_path({str(ROOT / 'materials' / 'pipeline.py')!r})\n"
            "print(m['platform_of']({'platform': 'shirasagi', 'resource_url': 'https://example.invalid/x', 'resource_id': 'x'})[0])\n"
        )
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "probe.py"
            f.write_text(code, encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", str(f)], capture_output=True, text=True, cwd=td)
        self.assertEqual(r.returncode, 0, r.stderr[-800:])
        self.assertEqual(r.stdout.strip(), "None")   # 登録外のサイトは None（ModuleNotFoundError で落ちない）


if __name__ == "__main__":
    unittest.main()
