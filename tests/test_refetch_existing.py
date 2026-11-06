"""再取得で教師の回答や評価の陣を壊さないこと。"""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('refetch_existing',Path(__file__).resolve().parents[1]/'materials/pool/refetch_existing.py')
R=importlib.util.module_from_spec(spec);spec.loader.exec_module(R)

class Guards(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        self.d=self.root/'materials/pool/work/b124';self.d.mkdir(parents=True)
        (self.d/'adopted.json').write_text(json.dumps({'pool':'train','adopted':[]}))
        (self.d/'corpus_log.json').write_text('{}')
        self.p=patch.object(R,'ROOT',self.root);self.p.start();self.addCleanup(self.p.stop)
    def test_all_teachers_block_regeneration(self):
        for teacher in ('answers','answers_codex','answers_claude','answers_grok','answers_final'):
            p=self.d/'sheets'/teacher/'sheet_001.tsv';p.parent.mkdir(parents=True);p.write_text('g0001\tamount\n')
            with self.assertRaisesRegex(ValueError,'回答'):R.validate_batch('b124')
            p.unlink()
    def test_labels_block_and_eval_is_rejected(self):
        p=self.d/'labels_codex.jsonl';p.write_text('{}')
        with self.assertRaisesRegex(ValueError,'回答'):R.validate_batch('b124')
        p.unlink();(self.d/'adopted.json').write_text('{"pool":"eval2"}')
        with self.assertRaisesRegex(ValueError,'教材'):R.validate_batch('b124')
    def test_outside_requested_range_is_rejected(self):
        for b in ('b018','F1','b123','b152','b186','b188','../b124','b124;anything'):
            with self.assertRaisesRegex(ValueError,'対象外'):R.validate_batch(b)
    def test_entire_input_is_validated_before_network_work(self):
        with patch.object(R.sys,'argv',['refetch','b124','b018']),patch.object(R,'run') as run:
            with self.assertRaisesRegex(ValueError,'対象外'):R.main()
            run.assert_not_called()
    def test_adoption_change_during_fetch_does_not_replace_corpus(self):
        (self.d/'corpus.jsonl').write_text('original\n')
        def change(*a,**k):(self.d/'adopted.json').write_text('{"pool":"train","changed":true}')
        with patch.object(R.subprocess,'run',side_effect=change):
            with self.assertRaisesRegex(ValueError,'同時に変わった'):R.run('b124')
        self.assertEqual((self.d/'corpus.jsonl').read_text(),'original\n')
if __name__=='__main__':unittest.main()
