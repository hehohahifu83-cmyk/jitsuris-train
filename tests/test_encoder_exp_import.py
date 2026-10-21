"""Regression test for the encoder_exp import-time FT_REAL_FRAC path."""
import importlib.util
import os
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def module(name, **attrs):
    result = types.ModuleType(name)
    for key, value in attrs.items():
        setattr(result, key, value)
    return result


class EncoderExpImportRegressionTest(unittest.TestCase):
    def _import_with_minimal_inputs(self):
        general = [
            ("Amount", ["10"], "amount", [], "general-table"),
            ("Tax", ["1"], "amount", [], "general-table"),
        ]
        business = [("Count", ["2"], "quantity", [], "business-table")]

        exp7 = module(
            "exp7",
            load_real=lambda paths: list(general if paths == ("materials/real_labels.jsonl",) else business),
            split=lambda rows: (list(rows), []),
            perturb=lambda _rng, header: header,
        )
        train3 = module(
            "train3",
            build_train=lambda *_args, **_kwargs: [("synthetic", ["x"], "category", [], "synthetic-table")],
            mat=lambda *_args, **_kwargs: None,
            split_curriculum=lambda: (None,),
            decide=lambda *_args, **_kwargs: None,
        )
        dev_eval = module("dev_eval", rows_of=lambda: [])
        gen = module("gen", HARD_NUMERIC=None)
        llm_baseline = module("llm_baseline", score_real=lambda *_args, **_kwargs: {})

        sparse = module("scipy.sparse", csr_matrix=lambda *a, **k: None, hstack=lambda *a, **k: None)
        scipy = module("scipy", sparse=sparse)
        linear_model = module("sklearn.linear_model", LogisticRegression=object)
        sklearn = module("sklearn", linear_model=linear_model)
        numpy = module("numpy", array=lambda values: list(values))

        fake_modules = {
            "numpy": numpy,
            "scipy": scipy,
            "scipy.sparse": sparse,
            "sklearn": sklearn,
            "sklearn.linear_model": linear_model,
            "exp7": exp7,
            "train3": train3,
            "dev_eval": dev_eval,
            "gen": gen,
            "llm_baseline": llm_baseline,
        }
        path = ROOT / "encoder_exp.py"
        spec = importlib.util.spec_from_file_location("encoder_exp_regression_probe", path)
        imported = importlib.util.module_from_spec(spec)
        exists = os.path.exists
        with patch.dict(sys.modules, fake_modules), \
             patch.dict(os.environ, {}, clear=True), \
             patch("os.path.exists", side_effect=lambda p: False if p in (
                 "materials/real_labels_biz2.jsonl", "materials/real_labels_jp.jsonl"
             ) else exists(p)):
            spec.loader.exec_module(imported)
        return imported, len(general) * 3 + len(business) * 6

    def test_import_without_ft_real_frac_keeps_all_real_rows(self):
        imported, legacy_real_rows = self._import_with_minimal_inputs()
        self.assertEqual(imported.REAL_FRAC, 1.0)
        # One synthetic row plus the full, unthinned augmented rows that predate S12.
        self.assertEqual(len(imported.rows), 1 + legacy_real_rows)
        self.assertEqual(len(imported.rows), 13)


if __name__ == "__main__":
    unittest.main()
