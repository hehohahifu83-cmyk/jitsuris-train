import json
import os
import tempfile
import unittest

import provenance as P


class DigestTests(unittest.TestCase):
    def test_rows_digest_changes_with_content_and_order(self):
        a = ("金額", ["1", "2"], "amount", ["日付"], "円")
        b = ("日付", ["2026-01-01"], "date", None, "")
        d1 = P.rows_digest([a, b])
        d2 = P.rows_digest([b, a])
        self.assertEqual(d1["count"], 2)
        self.assertNotEqual(d1["sha256_ordered"], d2["sha256_ordered"])      # 並びが違えば別
        self.assertEqual(d1["sha256_unordered"], d2["sha256_unordered"])     # 並びを問わない方は同じ
        c = ("金額", ["1", "3"], "amount", ["日付"], "円")
        self.assertNotEqual(P.rows_digest([a, b])["sha256_unordered"], P.rows_digest([c, b])["sha256_unordered"])

    def test_rows_digest_accepts_four_and_five_element_rows_and_numbers(self):
        self.assertEqual(P.rows_digest([("h", [1, 2], "id", None)])["count"], 1)
        self.assertEqual(P.rows_digest([("h", [1, 2], "id", [], "")])["sha256_unordered"],
                         P.rows_digest([("h", ["1", "2"], "id", None)])["sha256_unordered"])   # 値は文字列にそろえる・空の文脈と無しは同じ

    def test_rows_digest_does_not_contain_values(self):
        d = json.dumps(P.rows_digest([("秘密の見出し", ["秘密の値"], "text", ["秘密の列"], "")]), ensure_ascii=False)
        self.assertNotIn("秘密", d)

    def test_labels_digest_depends_on_order(self):
        self.assertNotEqual(P.labels_digest(["a", "b"])["sha256"], P.labels_digest(["b", "a"])["sha256"])
        self.assertEqual(P.labels_digest(["a", "b"])["count"], 2)

    def test_ft_env_only_ft_vars_and_drops_empty(self):
        env = {"FT_LR": "1e-4", "FT_X": "", "PATH": "/bin", "FT_SEED": "1"}
        self.assertEqual(P.ft_env(env), {"FT_LR": "1e-4", "FT_SEED": "1"})

    def test_hf_repo_id_from_path(self):
        self.assertEqual(P.hf_repo_id_from_path("hfmodel/jhu-clsp__mmBERT-small"), "jhu-clsp/mmBERT-small")
        self.assertEqual(P.hf_repo_id_from_path("intfloat/multilingual-e5-base"), "intfloat/multilingual-e5-base")
        self.assertEqual(P.hf_repo_id_from_path("hfmodel/plain"), "hfmodel/plain")

    def test_length_stats(self):
        s = P.length_stats([10, 20, 30, 200], 128)
        self.assertEqual(s["n"], 4)
        self.assertEqual(s["truncated"], 1)
        self.assertAlmostEqual(s["truncated_rate"], 0.25)
        self.assertEqual(s["max"], 200)
        self.assertEqual(P.length_stats([], 128)["n"], 0)


class FileDigestTests(unittest.TestCase):
    def test_weights_and_outputs_digests(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "model.safetensors"), "wb") as f:
                f.write(b"abc")
            with open(os.path.join(d, "config.json"), "w") as f:
                f.write("{}")
            with open(os.path.join(d, "notes.txt"), "w") as f:
                f.write("x")
            w = P.weights_digests(d)
            self.assertEqual(list(w), ["model.safetensors"])
            self.assertEqual(w["model.safetensors"]["bytes"], 3)
            self.assertEqual(w["model.safetensors"]["sha256"], P.sha256_bytes(b"abc"))
            self.assertEqual(list(P.small_files_digests(d)), ["config.json"])
            os.makedirs(os.path.join(d, "progress_probe_results"))
            with open(os.path.join(d, "probs_a_ft.json"), "w") as f:
                f.write("1")
            with open(os.path.join(d, "progress_probe_results", "after.json"), "w") as f:
                f.write("2")
            o = P.output_digests(d, ("probs_*.json", "progress_probe_results/*.json", "missing.md"))
            self.assertEqual(sorted(o), ["probs_a_ft.json", "progress_probe_results/after.json"])

    def test_weights_sha256_single_and_multi(self):
        one = {"saved_model": {"weights": {"model.safetensors": {"sha256": "aa", "bytes": 1}}}}
        self.assertEqual(P.weights_sha256(one), "aa")
        many = {"saved_model": {"weights": {"a.safetensors": {"sha256": "aa", "bytes": 1}, "b.safetensors": {"sha256": "bb", "bytes": 1}}}}
        self.assertEqual(len(P.weights_sha256(many)), 64)
        self.assertIsNone(P.weights_sha256({}))


class ManifestTests(unittest.TestCase):
    def test_build_and_write_manifest(self):
        with tempfile.TemporaryDirectory() as d:
            model_dir = os.path.join(d, "ft_out")
            os.makedirs(model_dir)
            with open(os.path.join(model_dir, "model.safetensors"), "wb") as f:
                f.write(b"w")
            with open(os.path.join(model_dir, "tokenizer.json"), "w") as f:
                f.write("{}")
            rows = [("金額", ["1"], "amount", None, "")]
            m = P.build_manifest(model_name="hfmodel/jhu-clsp__mmBERT-small", hf_repo_id="jhu-clsp/mmBERT-small", epochs=2.0, seed="1",
                                 labels=["amount", "date"], train_rows=rows, replay_rows=[], tests={"t": P.rows_digest(rows)},
                                 source_model_dir=model_dir, saved_model_dir=model_dir, environ={"FT_LR": "1e-4", "HOME": "/x"}, code_root=os.path.dirname(P.__file__) or ".")
            self.assertEqual(m["schema_version"], P.SCHEMA_VERSION)
            self.assertEqual(m["run"]["env"], {"FT_LR": "1e-4"})
            self.assertEqual(m["train_rows"]["count"], 1)
            self.assertEqual(m["replay_rows"], {"count": 0})
            self.assertIn("provenance.py", m["code"])
            self.assertIn("tokenizer.json", m["model"]["source_files"])
            self.assertEqual(P.weights_sha256(m), P.sha256_bytes(b"w"))
            path = P.write_manifest(os.path.join(d, "sub", "manifest.json"), m)
            self.assertEqual(json.load(open(path, encoding="utf-8"))["model"]["hf_repo_id"], "jhu-clsp/mmBERT-small")


if __name__ == "__main__":
    unittest.main()
