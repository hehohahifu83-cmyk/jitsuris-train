import json
import os
import tempfile
import unittest

import check_trained_model as C
import provenance as P


def make_model(d, weights=b"weights", with_manifest=True, status="completed"):
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "model.safetensors"), "wb") as f:
        f.write(weights)
    with open(os.path.join(d, "config.json"), "w") as f:
        f.write("{}")
    with open(os.path.join(d, "labels.json"), "w") as f:
        f.write('["a","b"]')
    if with_manifest:
        m = P.build_manifest(model_name="x", hf_repo_id="jhu-clsp/mmBERT-small", epochs=2.0, seed="1", labels=["a", "b"],
                             train_rows=[("h", ["1"], "a", None, "")], saved_model_dir=d, environ={"FT_LR": "1e-4"})
        m["status"] = status
        P.write_manifest(os.path.join(d, "manifest.json"), m)


class CheckTests(unittest.TestCase):
    def test_matching_manifest_and_expected_hash(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "ft_out_job1")
            make_model(d)
            sha = P.sha256_bytes(b"weights")
            r = C.check(d, expect_sha256=sha, require_manifest=True)
            self.assertTrue(r["ok"], r["problems"])
            self.assertEqual(r["weights_sha256"], sha)
            self.assertEqual(r["manifest"]["seed"], "1")
            self.assertEqual(r["manifest"]["env"], {"FT_LR": "1e-4"})
            self.assertEqual(C.main([d, "--expect-sha256", sha.upper(), "--require-manifest"]), 0)

    def test_expected_hash_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "m")
            make_model(d)
            r = C.check(d, expect_sha256="0" * 64)
            self.assertFalse(r["ok"])
            self.assertTrue(any("依頼に書いた" in p for p in r["problems"]))
            self.assertEqual(C.main([d, "--expect-sha256", "0" * 64]), 1)

    def test_weights_changed_after_manifest_fails(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "m")
            make_model(d)
            with open(os.path.join(d, "model.safetensors"), "wb") as f:
                f.write(b"other weights")
            r = C.check(d)
            self.assertFalse(r["ok"])
            self.assertTrue(any("manifest の重み" in p for p in r["problems"]))

    def test_tokenizer_or_config_changed_fails(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "m")
            make_model(d)
            with open(os.path.join(d, "labels.json"), "w") as f:
                f.write('["b","a"]')
            r = C.check(d)
            self.assertFalse(r["ok"])
            self.assertTrue(any("labels.json" in p for p in r["problems"]))

    def test_missing_manifest_warns_unless_required(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "m")
            make_model(d, with_manifest=False)
            r = C.check(d)
            self.assertTrue(r["ok"])
            self.assertTrue(r["warnings"])
            self.assertFalse(C.check(d, require_manifest=True)["ok"])

    def test_unfinished_manifest_fails(self):
        with tempfile.TemporaryDirectory() as t:
            d = os.path.join(t, "m")
            make_model(d, status="started")
            self.assertFalse(C.check(d)["ok"])

    def test_no_weights_fails(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertFalse(C.check(t)["ok"])


if __name__ == "__main__":
    unittest.main()
