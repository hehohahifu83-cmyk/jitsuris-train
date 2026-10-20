import math
import os
import tempfile
import unittest
from types import SimpleNamespace

import model_setup as M


class ModernBertOverrideTests(unittest.TestCase):
    def test_old_transformers_config_with_reference_compile(self):
        cfg = SimpleNamespace(reference_compile=None, classifier_pooling="mean", attention_dropout=0.0, mlp_dropout=0.0,
                              embedding_dropout=0.0, classifier_dropout=0.0, num_labels=2)
        ch = M.apply_modernbert_overrides(cfg, num_labels=15)
        self.assertIs(cfg.reference_compile, False)
        self.assertEqual(cfg.num_labels, 15)
        self.assertEqual(ch, {"reference_compile": False, "num_labels": 15})
        self.assertEqual(cfg.classifier_pooling, "mean")        # 指定しなければ config のまま

    def test_new_transformers_config_without_reference_compile(self):
        cfg = SimpleNamespace(classifier_pooling="mean", num_labels=2)
        ch = M.apply_modernbert_overrides(cfg, num_labels=15)
        self.assertFalse(hasattr(cfg, "reference_compile"))      # 持っていないものは作らない（5.x でモデルの初期化に渡って落ちる）
        self.assertEqual(ch, {"num_labels": 15})

    def test_pooling_override_and_validation(self):
        cfg = SimpleNamespace(classifier_pooling="mean", num_labels=2)
        self.assertEqual(M.apply_modernbert_overrides(cfg, pooling="cls")["classifier_pooling"], "cls")
        self.assertEqual(cfg.classifier_pooling, "cls")
        with self.assertRaises(ValueError):
            M.apply_modernbert_overrides(cfg, pooling="max")

    def test_no_dropout_sets_existing_attributes_only(self):
        cfg = SimpleNamespace(attention_dropout=0.1, mlp_dropout=0.1, num_labels=2)
        ch = M.apply_modernbert_overrides(cfg, no_dropout=True)
        self.assertEqual(cfg.attention_dropout, 0.0)
        self.assertEqual(sorted(ch), ["attention_dropout", "mlp_dropout"])

    def test_xlmr_path_is_unchanged(self):
        self.assertEqual(M.no_dropout_args("xlm-roberta"), {"hidden_dropout_prob": 0.0, "attention_probs_dropout_prob": 0.0})
        self.assertEqual(M.no_dropout_args("modernbert"), {})


class BinConversionTests(unittest.TestCase):
    def _dir(self, files):
        d = tempfile.mkdtemp()
        for n in files:
            open(os.path.join(d, n), "wb").write(b"x")
        self.addCleanup(lambda: __import__("shutil").rmtree(d, ignore_errors=True))
        return d

    def test_version_tuple(self):
        self.assertEqual(M.torch_version_tuple("2.5.1+cu124"), (2, 5))
        self.assertEqual(M.torch_version_tuple("2.14.1+cpu"), (2, 14))
        self.assertEqual(M.torch_version_tuple(None), (0, 0))
        self.assertEqual(M.torch_version_tuple("weird"), (0, 0))

    def test_old_torch_with_bin_only_needs_conversion(self):
        d = self._dir(["pytorch_model.bin", "config.json"])
        self.assertTrue(M.needs_bin_conversion(d, "2.5.1+cu124"))
        self.assertTrue(M.needs_bin_conversion(d, None))             # 版が分からないときは変換する側に倒す
        self.assertFalse(M.needs_bin_conversion(d, "2.6.0"))
        self.assertFalse(M.needs_bin_conversion(d, "2.14.1+cpu"))
        self.assertTrue(M.needs_bin_conversion(d, "2.14.1", force=True))

    def test_safetensors_or_no_bin_never_converts(self):
        self.assertFalse(M.needs_bin_conversion(self._dir(["model.safetensors", "pytorch_model.bin"]), "2.0", force=True))
        self.assertFalse(M.needs_bin_conversion(self._dir(["config.json"]), "2.0"))
        self.assertFalse(M.needs_bin_conversion("/no/such/dir", "2.0"))
        self.assertFalse(M.needs_bin_conversion("intfloat/multilingual-e5-base", "2.0"))


class NonFiniteGuardTests(unittest.TestCase):
    def test_finite_resets_counter(self):
        g = M.NonFiniteGuard(amp_on=True, fallback=True)
        self.assertEqual(g.observe(float("nan"), 100), "ok")
        self.assertEqual(g.observe(float("inf"), 200), "ok")
        self.assertEqual(g.observe(0.5, 300), "ok")                 # 有限に戻れば数え直し
        self.assertEqual(g.observe(float("nan"), 400), "ok")
        self.assertEqual(g.observe(float("nan"), 500), "ok")
        self.assertEqual(g.count, 2)

    def test_fallback_after_three_in_a_row_when_fp16_and_allowed(self):
        g = M.NonFiniteGuard(amp_on=True, fallback=True)
        self.assertEqual([g.observe(float("nan"), s) for s in (100, 200)], ["ok", "ok"])
        self.assertEqual(g.observe(float("nan"), 300), "fallback")
        self.assertFalse(g.amp_on)
        self.assertEqual(g.fallback_step, 300)
        self.assertEqual(g.count, 0)
        for s in (400, 500):                                         # fp32 に切り替えた後に、まだ有限でないなら止める
            self.assertEqual(g.observe(float("nan"), s), "ok")
        with self.assertRaises(RuntimeError):
            g.observe(float("nan"), 600)

    def test_raises_without_fallback(self):
        for amp_on, fallback in ((True, False), (False, True), (False, False)):
            g = M.NonFiniteGuard(amp_on=amp_on, fallback=fallback)
            g.observe(float("nan"), 100); g.observe(float("nan"), 200)
            with self.assertRaises(RuntimeError):
                g.observe(float("nan"), 300)


if __name__ == "__main__":
    unittest.main()
