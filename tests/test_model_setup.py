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


if __name__ == "__main__":
    unittest.main()
