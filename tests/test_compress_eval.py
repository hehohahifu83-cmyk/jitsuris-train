import importlib.util
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import compress_eval as C

HAS_TORCH = bool(importlib.util.find_spec("torch") and importlib.util.find_spec("transformers"))


class PureFunctionsTest(unittest.TestCase):
    def test_single_char_ids_keep_only_japanese_and_english_characters(self):
        vocab = {"<s>": 0, "▁": 4, "a": 5, "▁b": 6, "の": 7, "漢": 8, "я": 9, "ab": 10, "▁ab": 11, "한": 12, "，": 13, "▁Я": 14}
        self.assertEqual(C.single_char_ids(vocab), [4, 5, 6, 7, 8, 13])

    def test_choose_kept_ids_is_sorted_unique_and_in_range(self):
        kept = C.choose_kept_ids([[0, 10, 10, 2], [7, 99]], vocab_size=50, special_ids=[0, 1, 2, 3, 49], single_ids=[20, 5], top_k=6)
        self.assertEqual(kept, [0, 1, 2, 3, 4, 5, 7, 10, 20, 49])   # 99 は範囲外で落ちる。上位 K=6 は 0〜5

    def test_remap_sends_dropped_tokens_to_unk_and_keeps_order(self):
        remap = C.build_remap([0, 1, 2, 3, 10, 20], 30, 3)
        self.assertEqual([int(remap[i]) for i in (0, 1, 2, 3, 10, 20)], [0, 1, 2, 3, 4, 5])
        self.assertEqual([int(remap[i]) for i in (4, 7, 29)], [3, 3, 3])
        with self.assertRaises(ValueError):
            C.build_remap([0, 1, 2, 10], 30, 3)   # unk が残っていない

    def test_special_positions_must_not_move(self):
        remap = C.build_remap([0, 1, 2, 3, 10], 30, 3)
        C.check_special_positions([0, 1, 2, 3, 10], remap, [0, 1, 2, 3])
        bad = C.build_remap([0, 3, 4, 10], 30, 3)   # pad(1) が残らない（unk の新しい番号がたまたま 1 でも見逃さない）
        with self.assertRaises(ValueError):
            C.check_special_positions([0, 3, 4, 10], bad, [1])
        shifted = C.build_remap([0, 1, 3, 10], 30, 3)   # 2 が残らず、3 が 2 番になる
        with self.assertRaises(ValueError):
            C.check_special_positions([0, 1, 3, 10], shifted, [3])
        C.check_special_positions([0, 1, 2, 3, 10], remap, [None, 1, 3])   # None は読み飛ばす

    def test_apply_vocab_unk_chars_and_length_cap(self):
        kept = [0, 1, 2, 3, 10, 20]
        remap = C.build_remap(kept, 30, 3)
        ks = set(kept)
        self.assertEqual(C.apply_vocab([[0, 10, 7, 2]], ks, remap), [[0, 4, 3, 2]])
        self.assertEqual(C.apply_vocab([[0, 10, 7, 2]], ks, remap, expand=lambda t: [20, 20]), [[0, 4, 5, 5, 2]])
        # 1 文字に分けて長さが上限を超えたら、末尾を </s> にして切る
        self.assertEqual(C.apply_vocab([[0, 10, 7, 2]], ks, remap, expand=lambda t: [20, 20], max_len=4), [[0, 4, 5, 2]])

    def test_coverage_counts_dropped_tokens_and_columns(self):
        self.assertEqual(C.coverage([[0, 10, 7, 2], [0, 10, 2]], {0, 2, 10}), (7, 1, 1))

    def test_int8_rounding_error_is_below_half_a_step_and_zero_rows_stay_zero(self):
        rng = np.random.default_rng(0)
        w = rng.normal(size=(5, 16)).astype(np.float32)
        w[2] = 0
        q = C.fake_quant_rows_int8(w)
        step = np.abs(w).max(axis=1, keepdims=True) / 127.0
        self.assertTrue(np.all(np.abs(q - w) <= step / 2 + 1e-5))
        self.assertTrue(np.all(q[2] == 0))
        self.assertTrue(np.allclose(C.fake_quant_rows_int8(q), q, atol=1e-6))   # 2 回丸めても変わらない

    def test_size_report(self):
        s = C.size_report(n_total=1000, n_embed_full=600, hidden=10, n_kept=20)
        self.assertEqual((s["body_params"], s["kept_embed_params"]), (400, 200))
        self.assertAlmostEqual(s["full_fp32_mb"], 4000 / 1e6)
        self.assertAlmostEqual(s["trim_int8_mb"], 600 / 1e6)
        self.assertAlmostEqual(s["trim_fp16_mb"], 1200 / 1e6)

    def test_order_by_length_is_a_stable_permutation(self):
        lists = [[1, 2, 3], [1], [1, 2], [9]]
        order = C.order_by_length(lists)
        self.assertEqual(order, [1, 3, 2, 0])
        self.assertEqual(sorted(order), [0, 1, 2, 3])


    def test_edit_tokenizer_json_keeps_scores_unk_and_renumbers_special_tokens(self):
        tj = {"model": {"type": "Unigram", "unk_id": 3, "vocab": [["<s>", 0.0], ["<pad>", 0.0], ["</s>", 0.0], ["<unk>", 0.0], ["\u2581a", -1.0], ["b", -2.0], ["c", -3.0], ["<mask>", 0.0]]},
              "added_tokens": [{"id": 0, "content": "<s>"}, {"id": 3, "content": "<unk>"}, {"id": 7, "content": "<mask>"}],
              "post_processor": {"type": "TemplateProcessing", "special_tokens": {"<s>": {"id": "<s>", "ids": [0], "tokens": ["<s>"]}, "</s>": {"id": "</s>", "ids": [2], "tokens": ["</s>"]}}}}
        out = C.edit_tokenizer_json(tj, [0, 1, 2, 3, 4, 7])
        self.assertEqual([v[0] for v in out["model"]["vocab"]], ["<s>", "<pad>", "</s>", "<unk>", "\u2581a", "<mask>"])
        self.assertEqual(out["model"]["vocab"][4][1], -1.0)
        self.assertEqual(out["model"]["unk_id"], 3)
        self.assertEqual([a["id"] for a in out["added_tokens"]], [0, 3, 5])   # <mask> は 7 → 5
        self.assertEqual(out["post_processor"]["special_tokens"]["</s>"]["ids"], [2])
        with self.assertRaises(ValueError):
            C.edit_tokenizer_json({"model": {"type": "BPE"}}, [0])

    def test_cap_ids(self):
        self.assertEqual(C.cap_ids([[0, 5, 6, 2], [0, 5, 6, 7, 8, 2]], 5, 2), [[0, 5, 6, 2], [0, 5, 6, 7, 2]])


@unittest.skipUnless(HAS_TORCH, "torch と transformers が要る（CI で実行）")
class TorchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import torch
        from transformers import XLMRobertaConfig, XLMRobertaForSequenceClassification
        torch.manual_seed(0)
        cfg = XLMRobertaConfig(vocab_size=60, hidden_size=16, num_hidden_layers=2, num_attention_heads=2, intermediate_size=32,
                               max_position_embeddings=64, pad_token_id=1, bos_token_id=0, eos_token_id=2, num_labels=3)
        cls.model = XLMRobertaForSequenceClassification(cfg).eval()

    def test_trimmed_model_gives_identical_logits_on_kept_tokens(self):
        import torch
        from batching import pad_batch
        kept = sorted(set(range(4)) | {10, 11, 12, 20, 30, 59})
        remap = C.build_remap(kept, 60, 3)
        trimmed = C.trimmed_copy(self.model, kept)
        ids = [[0, 10, 11, 20, 2], [0, 30, 2], [0, 59, 12, 10, 11, 2]]
        pids, pmask = pad_batch(ids, 1)
        pids_t, mask = torch.tensor(pids), torch.tensor(pmask)
        with torch.no_grad():
            a = self.model(input_ids=pids_t, attention_mask=mask).logits
            b = trimmed(input_ids=torch.from_numpy(remap)[pids_t], attention_mask=mask).logits
        self.assertTrue(torch.allclose(a, b, atol=1e-6))
        self.assertEqual(trimmed.get_input_embeddings().weight.shape[0], len(kept))

    def test_cpu_copy_is_equal_and_independent(self):
        import torch
        m = C.cpu_copy(self.model)
        ids = torch.tensor([[0, 10, 11, 2]])
        with torch.no_grad():
            self.assertTrue(torch.allclose(self.model(input_ids=ids).logits, m(input_ids=ids).logits, atol=1e-6))
        with torch.no_grad():
            m.get_input_embeddings().weight.zero_()
        self.assertGreater(float(self.model.get_input_embeddings().weight.abs().sum()), 0.0)

    def test_probs_cpu_restores_the_original_order_across_batches(self):
        import torch
        ids = [[0, 10, 11, 20, 2], [0, 30, 2], [0, 59, 12, 10, 11, 2], [0, 5, 2], [0, 6, 7, 8, 9, 10, 2]]
        p = C.probs_dev(self.model, ids, pad_id=1, batch=2)
        self.assertEqual(p.shape, (5, 3))
        for i, s in enumerate(ids):
            with torch.no_grad():
                one = torch.softmax(self.model(input_ids=torch.tensor([s])).logits, -1).numpy()[0]
            self.assertTrue(np.allclose(p[i], one, atol=1e-5))

    def test_round_linear_int8_changes_weights_by_less_than_half_a_step(self):
        import torch
        m = C.cpu_copy(self.model)
        before = {n: mod.weight.detach().clone() for n, mod in m.named_modules() if isinstance(mod, torch.nn.Linear)}
        C.round_linear_int8(m)
        self.assertGreater(len(before), 4)
        for n, mod in m.named_modules():
            if isinstance(mod, torch.nn.Linear):
                w0, w1 = before[n], mod.weight.detach()
                step = w0.abs().amax(dim=1, keepdim=True) / 127.0
                self.assertTrue(bool((w0 - w1).abs().le(step / 2 + 1e-5).all()), n)

    def test_int8_and_fp16_variants_run_and_stay_close(self):
        import torch
        ids = torch.tensor([[0, 10, 11, 20, 2]])
        with torch.no_grad():
            ref = self.model(input_ids=ids).logits
            q = C.int8_linear(self.model)(input_ids=ids).logits
            h = C.round_weights_fp16(C.cpu_copy(self.model))(input_ids=ids).logits
        self.assertTrue(torch.isfinite(q).all())
        self.assertTrue(torch.allclose(ref, h, atol=1e-2))     # fp16 に丸めた重み：ほぼ同じ
        self.assertLess(float((ref - q).abs().max()), 0.5)     # INT8：ランダムな小さなモデルなので緩い基準（動くこと中心）

    @unittest.skipUnless(importlib.util.find_spec("tokenizers"), "tokenizers が要る")
    def test_trimmed_tokenizer_matches_full_tokenizer_when_all_pieces_are_kept(self):
        import types
        from tokenizers import Tokenizer, models, pre_tokenizers, processors
        vocab = [("<s>", 0.0), ("<pad>", 0.0), ("</s>", 0.0), ("<unk>", 0.0), ("\u2581", -2.0), ("\u2581ab", -3.0), ("a", -4.0), ("b", -4.0), ("c", -4.0),
                 ("\u2581a", -3.5), ("ab", -3.2), ("<mask>", 0.0)]
        tk = Tokenizer(models.Unigram(vocab, unk_id=3, byte_fallback=False))
        tk.pre_tokenizer = pre_tokenizers.Metaspace(replacement="\u2581", prepend_scheme="always")
        tk.post_processor = processors.TemplateProcessing(single="<s> $A </s>", special_tokens=[("<s>", 0), ("</s>", 2)])
        kept = [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]   # \u2581a(9) と ab(10) を落とす
        remap = C.build_remap(kept, len(vocab), 3)
        trimmed = C.trimmed_tokenizer(types.SimpleNamespace(backend_tokenizer=tk), kept)
        for text in ["ab", "ab c", "c b"]:
            full_ids = tk.encode(text).ids
            self.assertTrue(all(i in kept for i in full_ids), text)
            self.assertEqual([int(remap[i]) for i in full_ids], trimmed.encode(text).ids, text)
        self.assertEqual(tk.encode("a").ids, [0, 9, 2])           # 元：\u2581a 1 つ
        self.assertEqual(trimmed.encode("a").ids, [0, 4, 6, 2])   # 縮めた：\u2581 と a に分かれる
        self.assertTrue(all(i < len(kept) for i in trimmed.encode("a ab zz").ids))

    def test_run_end_to_end_with_a_fake_tokenizer(self):
        import torch
        from transformers import XLMRobertaConfig, XLMRobertaForSequenceClassification

        class FakeTok:
            pad_token_id, unk_token_id, sep_token_id = 1, 3, 2

            def __init__(self):
                self.pieces = ["<s>", "<pad>", "</s>", "<unk>", "▁"] + list("abcdefghijklmnopqrstuvwxyz0123456789 :|,「」の金額") + ["amount", "date", "金額", "日付"]
                self.index = {p: i for i, p in enumerate(self.pieces)}
                self.all_special_ids = [0, 1, 2, 3]
                self.cls_token_id = 0

            def get_vocab(self):
                return dict(self.index)

            def convert_ids_to_tokens(self, i):
                return self.pieces[i]

            def convert_tokens_to_ids(self, t):
                return self.index.get(t, self.unk_token_id)

            def __call__(self, texts, truncation=True, max_length=128, padding=False):
                out = []
                for t in texts:
                    ids, i = [], 0
                    while i < len(t):
                        for j in range(min(len(t), i + 6), i, -1):
                            if t[i:j] in self.index:
                                ids.append(self.index[t[i:j]]); i = j; break
                        else:
                            ids.append(3); i += 1
                    out.append([0] + ids[:max_length - 2] + [2])
                return {"input_ids": out}

        tok = FakeTok()
        torch.manual_seed(1)
        cfg = XLMRobertaConfig(vocab_size=len(tok.pieces), hidden_size=16, num_hidden_layers=2, num_attention_heads=2, intermediate_size=32,
                               max_position_embeddings=64, pad_token_id=1, bos_token_id=0, eos_token_id=2, num_labels=3)
        model = XLMRobertaForSequenceClassification(cfg).eval()
        labels = ["amount", "date", "text"]
        mk = lambda h, v, lab: (h, v, lab, ["amount", "date"])
        rows = [mk("amount", ["1,000", "2,500"], "amount"), mk("date", ["2024-01-01"], "date"), mk("日付", ["2024-01-02"], "date"), mk("金額", ["300"], "amount")]
        tests = {"t1": [mk("amount", ["10"], "amount"), mk("date", ["2024-03-01"], "date"), mk("note", ["abc"], "text")]}
        lr_probs = {"t1": np.full((3, 3), 1 / 3)}
        decide = lambda classes, P, rs: [classes[int(i)] for i in P.argmax(1)]

        def score_real(pred, truth):
            ok = sum(p == t for p, t in zip(pred, truth))
            return {"acc_all": ok / len(truth), "wrong": len(truth) - ok, "unknown": 0, "critical": 0, "other_ok": 0, "other_ng": 0}

        text_fn = lambda r, prefix: f"{prefix}{r[0]} | {', '.join(r[1])}"
        lines, notes = C.run(model, tok, tests, rows, labels, lr_probs, text_fn, "", decide, score_real, "fake", top_k=0, max_len=32)
        self.assertEqual(len(lines), 12)   # 6 通りの縮め方 × 2 つの組み合わせ
        self.assertTrue(all(l.startswith("| fake・圧縮【") and " t1 正" in l for l in lines))
        self.assertTrue(any("圧縮なしとの top-1 一致" in n for n in notes))
        self.assertTrue(notes[0].startswith("- 圧縮の試験（fake）"))


if __name__ == "__main__":
    unittest.main()
