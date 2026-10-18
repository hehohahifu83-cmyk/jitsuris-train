import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from batching import micro_weights, pad_batch, padded_tokens, plan_micro_batches


class BatchingTest(unittest.TestCase):
    def test_everyone_appears_exactly_once(self):
        rng = random.Random(1)
        lengths = [rng.randint(5, 128) for _ in range(64)]
        for micro in (1, 2, 5, 8, 16, 64, 100):
            plan = plan_micro_batches(lengths, micro)
            flat = [i for p in plan for i in p]
            self.assertEqual(sorted(flat), list(range(64)))
            self.assertTrue(all(len(p) <= micro for p in plan))

    def test_longest_first_and_sorted_inside(self):
        lengths = [10, 90, 30, 70, 50, 20, 80, 60]
        plan = plan_micro_batches(lengths, 3)
        self.assertEqual(plan[0][0], 1)  # 最長（90）が先頭
        seq = [lengths[i] for p in plan for i in p]
        self.assertEqual(seq, sorted(seq, reverse=True))
        asc = plan_micro_batches(lengths, 3, longest_first=False)
        seq = [lengths[i] for p in asc for i in p]
        self.assertEqual(seq, sorted(seq))

    def test_weights_sum_to_one_and_follow_sizes(self):
        plan = plan_micro_batches(list(range(10)), 4)  # 4, 4, 2
        w = micro_weights(plan)
        self.assertAlmostEqual(sum(w), 1.0)
        self.assertEqual([round(x, 3) for x in w], [0.4, 0.4, 0.2])

    def test_pad_batch_shapes_masks_and_multiple(self):
        ids, mask = pad_batch([[5, 6, 7], [8]], pad_id=1)
        self.assertEqual(ids, [[5, 6, 7], [8, 1, 1]])
        self.assertEqual(mask, [[1, 1, 1], [1, 0, 0]])
        ids, mask = pad_batch([[5, 6, 7], [8]], pad_id=1, multiple=8)
        self.assertEqual(len(ids[0]), 8)
        self.assertEqual(sum(mask[0]), 3)
        self.assertEqual(sum(mask[1]), 1)
        with self.assertRaises(ValueError):
            pad_batch([], pad_id=1)

    def test_sorting_never_computes_more_than_random_split(self):
        rng = random.Random(7)
        worse = 0
        for _ in range(200):
            lengths = [min(128, max(8, int(rng.lognormvariate(4.0, 0.5)))) for _ in range(64)]
            idx = list(range(64)); rng.shuffle(idx)
            random_plan = [idx[s:s + 16] for s in range(0, 64, 16)]
            sorted_plan = plan_micro_batches(lengths, 16)
            if padded_tokens(lengths, sorted_plan) > padded_tokens(lengths, random_plan):
                worse += 1
        self.assertEqual(worse, 0)

    def test_padded_tokens_counts_padding(self):
        lengths = [10, 20, 30, 40]
        self.assertEqual(padded_tokens(lengths, [[0, 1, 2, 3]]), 160)
        self.assertEqual(padded_tokens(lengths, [[3, 2], [1, 0]]), 40 * 2 + 20 * 2)
        self.assertEqual(padded_tokens(lengths, [[0, 1]], multiple=8), 24 * 2)


if __name__ == "__main__":
    unittest.main()
