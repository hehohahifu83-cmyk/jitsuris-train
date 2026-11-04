import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research'))
import precedent_replay as R


def rows(label='id', n=6, publishers=2):
    return [{'table': str(i), 'header': ' Code ', 'label': label, 'publisher': f'p{i % publishers}'} for i in range(n)]


class ReplayTests(unittest.TestCase):
    def test_no_self_or_future_leakage(self):
        report, _ = R.replay([(2, rows()), (1, rows())])
        self.assertEqual([r['matched'] for r in report], [0, 6])

    def test_support_publishers_and_unanimity(self):
        for first in [rows(n=4), rows(publishers=1), rows(n=5)+rows('quantity', n=1), rows('unknown')]:
            report, _ = R.replay([(1, first), (2, rows())])
            self.assertEqual(report[-1]['matched'], 0)

    def test_mismatch_and_fix_on_both_sides(self):
        first, second = rows(), rows('quantity')
        report, errors = R.replay([(1, first), (2, second)])
        self.assertEqual(report[-1]['correct'], 0)
        self.assertEqual(errors[('code', 'id', 'quantity')], 6)
        fixes = {(str(i), 'Code'): ('quantity', 'id') for i in range(6)}
        report, errors = R.replay([(1, first), (2, second)], fixes)
        self.assertEqual(report[-1]['correct'], 6)
        self.assertFalse(errors)


if __name__ == '__main__':
    unittest.main()
