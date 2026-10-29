import json
import os
import tempfile
import unittest

import numpy as np

import evaluate_independent as E
import provenance as P
import slice_eval as S

LABELS = ["amount", "category", "date", "other"]


def column(cid, header, values, siblings=None, unit=""):
    return {"id": cid, "table": "t1", "source": "s", "language": "en", "header": header, "values": values, "siblings": siblings or [], "unit": unit}


def sample_set():
    return {"schema_version": 1, "set_id": "demo", "columns": [
        column("c1", "Date Of Sale", ["2024-01-01", "2024-02-01", "2024-03-05", "2024-03-09", "2024-04-01"], ["Price", "Notes"]),
        column("c2", "Notes", ["a", "b", "c", "d", "e"], ["Date Of Sale", "Price"]),
        column("c3", "Price", ["100", "200", "300", "400", "500"], ["Date Of Sale", "Notes"], unit="Unit: JPY"),
    ]}


def write(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)


def make_checkpoint(d, weights=b"weights-bytes", prefix="query: ", ctx_unit="1", status="completed"):
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "model.safetensors"), "wb") as fh:
        fh.write(weights)
    write(os.path.join(d, "config.json"), {"model_type": "xlm-roberta"})
    write(os.path.join(d, "tokenizer.json"), {"x": 1})
    write(os.path.join(d, "labels.json"), LABELS)
    manifest = {"status": status, "commit": "c0ffee", "saved_model": {"files": P.small_files_digests(d), "weights": P.weights_digests(d)},
                "model": {"hf_repo_id": "org/model", "hf_revision": {"revision": "rev123"}},
                "extra": {"model_type": "xlm-roberta", "prefix": prefix, "max_length": 128},
                "run": {"env": {"FT_CTX_UNIT": ctx_unit}, "seed": "2"}}
    write(os.path.join(d, "manifest.json"), manifest)
    return d


def fake_infer(checkpoint_dir, texts, info):
    # c1 → date 0.9、c2 → category 0.3（しきい値より低い＝不明）、c3 → amount 0.8
    probs = np.array([[0.02, 0.05, 0.90, 0.03], [0.20, 0.30, 0.25, 0.25], [0.80, 0.10, 0.05, 0.05]])
    fake_infer.texts = texts
    fake_infer.calls = getattr(fake_infer, "calls", 0) + 1
    return probs, 0.5


class SetTests(unittest.TestCase):
    def test_load_set_ok_and_rows_have_empty_label(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "set.json")
            write(path, sample_set())
            data, sha = E.load_set(path)
            self.assertEqual(len(sha), 64)
            rows = E.rows_of(data)
            self.assertEqual(rows[0], ("Date Of Sale", ["2024-01-01", "2024-02-01", "2024-03-05", "2024-03-09", "2024-04-01"], "", ["Price", "Notes"], ""))
            self.assertEqual(rows[2][4], "Unit: JPY")

    def test_load_set_rejects_bad_shapes(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "set.json")
            for mutate, message in ((lambda s: s.update(schema_version=2), "schema_version"),
                                    (lambda s: s["columns"].append(column("c1", "Dup", ["x"])), "重複"),
                                    (lambda s: s["columns"].append(column("c9", " ", ["x"])), "header"),
                                    (lambda s: s["columns"].append(column("c9", "H", [])), "values"),
                                    (lambda s: s.update(columns=[]), "columns")):
                data = sample_set()
                mutate(data)
                write(path, data)
                with self.assertRaises(ValueError) as ctx:
                    E.load_set(path)
                self.assertIn(message, str(ctx.exception))


class CheckpointTests(unittest.TestCase):
    def test_info_reads_settings_from_manifest(self):
        with tempfile.TemporaryDirectory() as d:
            info = E.checkpoint_info(make_checkpoint(os.path.join(d, "ft_out_job2")))
            self.assertEqual((info["prefix"], info["max_length"], info["ctx_unit"], info["model"], info["hf_revision"]), ("query: ", 128, True, "org/model", "rev123"))
            self.assertEqual(info["labels"], LABELS)
            self.assertEqual(len(info["weights_sha256"]), 64)

    def test_tampered_weights_or_unfinished_run_are_refused(self):
        with tempfile.TemporaryDirectory() as d:
            ck = make_checkpoint(os.path.join(d, "a"))
            with open(os.path.join(ck, "model.safetensors"), "wb") as fh:
                fh.write(b"changed")
            with self.assertRaises(ValueError):
                E.checkpoint_info(ck)
            with self.assertRaises(ValueError):
                E.checkpoint_info(make_checkpoint(os.path.join(d, "b"), status="started"))

    def test_texts_follow_training_format(self):
        with tempfile.TemporaryDirectory() as d:
            info = E.checkpoint_info(make_checkpoint(os.path.join(d, "x")))
            rows = E.rows_of(sample_set())
            texts = E.texts_of(rows, info)
            self.assertTrue(texts[2].startswith("query: 列名: Price | 値: 100, 200, 300, 400, 500 | 同じ表の列: Date Of Sale, Notes"))
            self.assertTrue(texts[2].endswith("| 同じ表の単位列の値: Unit: JPY"))
            self.assertNotIn("単位列", texts[0])
            info2 = dict(info, ctx_unit=False, prefix="")
            self.assertTrue(E.texts_of(rows, info2)[2].startswith("列名: Price"))
            self.assertNotIn("単位列", E.texts_of(rows, info2)[2])


class PredictAndScoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = self.tmp.name
        self.set_path = os.path.join(self.d, "set.json")
        write(self.set_path, sample_set())
        self.ck = make_checkpoint(os.path.join(self.d, "ft_out_job1"))
        self.ledger = os.path.join(self.d, "ledger.jsonl")
        self.out = os.path.join(self.d, "preds.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_predict_writes_label_free_predictions_and_ledger(self):
        doc = E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer)
        self.assertEqual([r["guarded_prediction"] for r in doc["rows"]], ["date", "unknown", "amount"])
        self.assertEqual(doc["rows"][1]["decision_reason"], "probability_below_threshold")
        self.assertEqual(doc["rows"][0]["column"], "date of sale")
        text = E.read_bytes(self.out).decode("utf-8")
        self.assertNotIn("2024-01-01", text)                      # 値は出力に書かない
        self.assertNotIn('"truth"', text)                         # ラベルは読まない
        self.assertEqual(doc["timing"]["columns"], 3)
        self.assertEqual(doc["guard_version"], "v9.1")
        self.assertEqual(doc["guard_implementation_version"], "v10")
        self.assertEqual(doc["available_guard_versions"], ["v9.1", "v10"])
        self.assertEqual(doc["rows"][0]["guard_predictions"]["v9.1"]["guarded_prediction"], "date")
        self.assertIn("v10", doc["rows"][0]["guard_predictions"])
        entries = E.ledger_entries(self.ledger)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["weights_sha256"], doc["checkpoint"]["weights_sha256"])
        self.assertTrue(fake_infer.texts[0].startswith("query: 列名: Date Of Sale"))

    def test_titles_go_into_model_input_only_when_asked(self):
        # --titles（2026-10-30）：渡したときだけ「表の題名」を入力に入れる（学習の FT_TITLE=1 と同じ位置）。既定は今までどおり入れない
        doc = E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer)
        self.assertNotIn("表の題名", fake_infer.texts[2])
        self.assertNotIn("titles", doc)
        tp = os.path.join(self.d, "titles.json")
        write(tp, {"t1": "Sales Ledger"})
        doc = E.predict(self.set_path, self.ck, os.path.join(self.d, "p2.json"), self.ledger, repeat_reason="titles", infer=fake_infer, titles_path=tp)
        self.assertIn("| 値: 100, 200, 300, 400, 500 | 表の題名: Sales Ledger | 同じ表の列:", fake_infer.texts[2])
        self.assertTrue(fake_infer.texts[2].endswith("| 同じ表の単位列の値: Unit: JPY"))   # 単位の欄に題名は混ざらない
        self.assertEqual(doc["titles"]["columns_with_title"], 3)
        self.assertEqual([r["guarded_prediction"] for r in doc["rows"]], ["date", "unknown", "amount"])

    def test_saved_prediction_scores_v91_and_v10_without_inference(self):
        data = sample_set()
        data["columns"][0]["values"] = ["3/15", "4/20", "5/1", "6/30", "7/25"]
        write(self.set_path, data)
        calls_before = getattr(fake_infer, "calls", 0)
        doc = E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer)
        self.assertEqual(doc["rows"][0]["guard_predictions"]["v9.1"]["guarded_prediction"], "unknown")
        self.assertEqual(doc["rows"][0]["guard_predictions"]["v10"]["guarded_prediction"], "date")
        calls_after_predict = fake_infer.calls
        self.assertEqual(calls_after_predict, calls_before + 1)

        labels = os.path.join(self.d, "labels.json")
        write(labels, {"c1": "date", "c2": "category", "c3": "amount"})
        score_v91 = E.score(self.out, labels, os.path.join(self.d, "scored_v91"), "job1", guard_version="v9.1")
        score_v10 = E.score(self.out, labels, os.path.join(self.d, "scored_v10"), "job1", guard_version="v10")
        self.assertEqual(fake_infer.calls, calls_after_predict)
        self.assertEqual(score_v91["guard_version"], "v9.1")
        self.assertEqual(score_v10["guard_version"], "v10")
        self.assertEqual(score_v91["counts"], {"unknown": 2, "correct": 1})
        self.assertEqual(score_v10["counts"], {"correct": 2, "unknown": 1})

    def test_same_pair_is_refused_twice_unless_reason_given(self):
        E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer)
        with self.assertRaises(ValueError):
            E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer)
        E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer, repeat_reason="出力先のディスクが満杯で書けなかった")
        entries = E.ledger_entries(self.ledger)
        self.assertEqual(len(entries), 2)
        self.assertIn("ディスク", entries[1]["repeat_reason"])
        other = make_checkpoint(os.path.join(self.d, "ft_out_job2"), weights=b"another-weights")
        E.predict(self.set_path, other, self.out, self.ledger, infer=fake_infer)       # 別の重みは通る
        self.assertEqual(len(E.ledger_entries(self.ledger)), 3)

    def test_score_writes_records_readable_by_slice_eval(self):
        E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer)
        labels = os.path.join(self.d, "labels.json")
        write(labels, {"c1": "date", "c2": "category", "c3": "amount"})
        out_dir = os.path.join(self.d, "scored")
        link = E.score(self.out, labels, out_dir, "job1")
        self.assertEqual(link["counts"], {"correct": 2, "unknown": 1})
        records = S.load_records(out_dir, "ft")
        rows = records[("job1", "independent_main")]
        self.assertEqual([r["outcome"] for r in rows], ["correct", "unknown", "correct"])
        self.assertEqual([r["truth"] for r in rows], ["date", "category", "amount"])
        manifest = E.read_json(os.path.join(out_dir, "job1_independent_manifest.json"))
        self.assertEqual(len(manifest["labels_sha256"]), 64)
        self.assertEqual(manifest["checkpoint"]["seed"], "2")

    def test_score_leaves_out_unknown_and_S_columns_and_says_so(self):
        E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer)
        labels = os.path.join(self.d, "labels.json")
        write(labels, {"c1": "date", "c2": "unknown", "c3": "S"})
        out_dir = os.path.join(self.d, "scored_ex")
        link = E.score(self.out, labels, out_dir, "job1")
        self.assertEqual((link["n"], link["n_excluded"], sorted(link["excluded_ids"])), (1, 2, ["c2", "c3"]))
        self.assertEqual(link["counts"], {"correct": 1})
        rows = S.load_records(out_dir, "ft")[("job1", "independent_main")]
        self.assertEqual([r["column"] for r in rows], ["date of sale"])

    def test_score_counts_assertions_on_unknown_labeled_columns(self):
        # fake_infer の答え：c1 → date、c2 → 不明（しきい値未満）、c3 → amount
        E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer)
        labels = os.path.join(self.d, "labels.json")
        write(labels, {"c1": "unknown", "c2": "unknown", "c3": "amount"})
        link = E.score(self.out, labels, os.path.join(self.d, "scored_u"), "job1")
        self.assertEqual((link["n_unknown_labeled"], link["unknown_asserted"], link["unknown_asserted_ids"]), (2, 1, ["c1"]))
        self.assertEqual((link["n"], link["n_excluded"]), (1, 2))
        # S の列は「決められない列」に数えない（言い切っても数えない）
        write(labels, {"c1": "S", "c2": "unknown", "c3": "amount"})
        link = E.score(self.out, labels, os.path.join(self.d, "scored_s"), "job1")
        self.assertEqual((link["n_unknown_labeled"], link["unknown_asserted"], link["unknown_asserted_ids"]), (1, 0, []))
        self.assertEqual(link["n_excluded"], 2)
        # unknown のラベルが無ければ 0 件
        write(labels, {"c1": "date", "c2": "category", "c3": "amount"})
        link = E.score(self.out, labels, os.path.join(self.d, "scored_n"), "job1")
        self.assertEqual((link["n_unknown_labeled"], link["unknown_asserted"], link["unknown_asserted_ids"]), (0, 0, []))

    def test_score_refuses_when_nothing_is_left_to_evaluate(self):
        E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer)
        labels = os.path.join(self.d, "labels.json")
        write(labels, {"c1": "unknown", "c2": "S", "c3": "unknown"})
        with self.assertRaises(ValueError) as ctx:
            E.score(self.out, labels, os.path.join(self.d, "o4"), "job1")
        self.assertIn("1 つもない", str(ctx.exception))

    def test_score_refuses_mismatched_or_unknown_labels(self):
        E.predict(self.set_path, self.ck, self.out, self.ledger, infer=fake_infer)
        labels = os.path.join(self.d, "labels.json")
        write(labels, {"c1": "date", "c2": "category"})
        with self.assertRaises(ValueError):
            E.score(self.out, labels, os.path.join(self.d, "o1"), "job1")                      # c3 のラベルが無い
        write(labels, {"c1": "date", "c2": "category", "c3": "amount", "c4": "date"})
        with self.assertRaises(ValueError):
            E.score(self.out, labels, os.path.join(self.d, "o2"), "job1")                      # 予測にない id
        write(labels, {"c1": "date", "c2": "category", "c3": "person"})
        with self.assertRaises(ValueError):
            E.score(self.out, labels, os.path.join(self.d, "o3"), "job1")                      # 重みが知らないラベル


if __name__ == "__main__":
    unittest.main()
