"""unknown が複数段を通るときの重複計上と原因段の取り違えを防ぐ。"""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('g1_codex_summary', Path(__file__).resolve().parents[1] / 'research/g1/codex_summarize.py')
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


class UnknownOriginTest(unittest.TestCase):
    def test_continuing_unknown_counts_guard_once(self):
        row = {s: {'label': 'unknown'} for s in M.STAGES}
        row['input_guard']['reason'] = 'amount_without_cue'
        self.assertEqual(M.origin(row), ('input_guard', 'amount_without_cue'))

    def test_recovery_and_later_veto_is_attributed_to_veto(self):
        row = {s: {'label': 'unknown'} for s in M.STAGES}
        row['recheck'] = {'label': 'amount'}
        row['verifier'] = {'label': 'unknown', 'reason': 'verifier:quantity'}
        self.assertEqual(M.origin(row), ('verifier', 'verifier:quantity'))

    def test_final_recovery_is_not_counted_as_unknown(self):
        row = {s: {'label': 'unknown'} for s in M.STAGES}
        row['final']['label'] = 'quantity'
        self.assertEqual(M.origin(row), ('', ''))

    def test_late_currency_veto_overrides_earlier_episode(self):
        row = {s: {'label': 'unknown'} for s in M.STAGES}
        row['dictionary']['label'] = 'amount'
        self.assertEqual(M.origin(row), ('final', ''))

    def test_missing_verifier_stage_is_allowed(self):
        row = {'input_guard': {'label': 'quantity'}, 'recheck': {'label': 'unknown', 'reason': 'cue_conflict'}, 'final': {'label': 'unknown'}}
        self.assertEqual(M.origin(row), ('recheck', 'cue_conflict'))


class OutcomeTest(unittest.TestCase):
    def test_numeric_to_id_is_critical_under_official_definition(self):
        self.assertEqual(M.outcome('id', 'quantity'), 'crit')

    def test_text_to_date_is_not_critical(self):
        self.assertEqual(M.outcome('date', 'text'), 'wrong')
