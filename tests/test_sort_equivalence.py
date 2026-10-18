"""長さ順の小さな束に分けても、64 文を一度に流したときと同じ勾配になること（torch と transformers がある環境だけで実行）。"""
import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from batching import pad_batch, plan_micro_batches

try:
    import torch
    from transformers import XLMRobertaConfig, XLMRobertaForSequenceClassification
except ImportError:  # 手元（torch なし）では飛ばす。GitHub Actions では実行する
    torch = None


@unittest.skipIf(torch is None, "torch / transformers がない")
class SortEquivalenceTest(unittest.TestCase):
    def setUp(self):
        torch.manual_seed(0)
        cfg = XLMRobertaConfig(vocab_size=120, hidden_size=32, num_hidden_layers=2, num_attention_heads=2, intermediate_size=64,
                               max_position_embeddings=140, num_labels=5, hidden_dropout_prob=0.0, attention_probs_dropout_prob=0.0, pad_token_id=1)
        self.model = XLMRobertaForSequenceClassification(cfg).float()
        rng = random.Random(3)
        self.seqs = [[0] + [rng.randrange(3, 120) for _ in range(rng.randint(3, 100))] + [2] for _ in range(64)]
        self.ys = [rng.randrange(5) for _ in self.seqs]

    def reference(self):
        ids, mask = pad_batch(self.seqs, 1)
        self.model.zero_grad(set_to_none=True)
        out = self.model(input_ids=torch.tensor(ids), attention_mask=torch.tensor(mask), labels=torch.tensor(self.ys))
        out.loss.backward()
        return out.loss.item(), {n: p.grad.clone() for n, p in self.model.named_parameters()}

    def test_gradients_match_for_every_micro_batch_size(self):
        ref_loss, ref = self.reference()
        for micro, multiple in ((16, 1), (8, 8), (5, 1), (64, 1), (1, 1), (3, 8)):
            self.model.zero_grad(set_to_none=True)
            total = 0.0
            for idx in plan_micro_batches([len(s) for s in self.seqs], micro):
                ids, mask = pad_batch([self.seqs[i] for i in idx], 1, multiple)
                out = self.model(input_ids=torch.tensor(ids), attention_mask=torch.tensor(mask), labels=torch.tensor([self.ys[i] for i in idx]))
                (out.loss * (len(idx) / 64)).backward()
                total += out.loss.item() * len(idx) / 64
            self.assertAlmostEqual(total, ref_loss, places=5, msg=f"micro={micro}")
            for n, p in self.model.named_parameters():
                torch.testing.assert_close(p.grad, ref[n], atol=1e-5, rtol=1e-4, msg=f"{n} micro={micro}")

    def test_padding_does_not_change_a_single_sample(self):
        # 同じ文を、短い詰め物と長い詰め物で流しても、出力が同じ
        self.model.eval()
        s = self.seqs[0]
        with torch.no_grad():
            a = self.model(input_ids=torch.tensor([s + [1] * 2]), attention_mask=torch.tensor([[1] * len(s) + [0] * 2])).logits
            b = self.model(input_ids=torch.tensor([s + [1] * 30]), attention_mask=torch.tensor([[1] * len(s) + [0] * 30])).logits
        torch.testing.assert_close(a, b, atol=1e-6, rtol=1e-5)


if __name__ == "__main__":
    unittest.main()
