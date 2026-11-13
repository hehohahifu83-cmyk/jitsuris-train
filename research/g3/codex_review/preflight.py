"""予測・学習なしのG3事前点検。固定済みの実装は変更しない。"""
import hashlib
import json
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch
import numpy as np
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/g3'))
import g3_eval as G


def probe(with_m, raise_in_eval=False):
    seen = {}
    col = {'id':'probe','header':'Funding','values':['1'], 'values5':['1'],
           'truth':'unknown','pred':'unknown','top3':[], 'unit':''}
    def base(cols):
        for h in ('Funding', 'Students', 'abfall_kwh'):
            seen[h] = sorted(G.RC.cue_types(h, ''))
        return [('unknown', None)]
    with patch.object(G.D,'with_job',return_value={'probe':[col]}), \
         patch.object(G.D.EF,'probs',return_value=np.zeros((1,len(G.D.V.LABELS)))), \
         patch.object(G.D.EF.E,'base_decisions',side_effect=RuntimeError('probe exception') if raise_in_eval else base), \
         patch.object(G.D.EF.E,'combine',return_value=[('unknown',None)]):
        G.run({},None,list(G.D.V.LABELS),'L24',1,with_m,False)
    return seen


def expect_prediction_rejected(ids, mutate=None):
    first_key = next(iter(G.WEIGHTS))
    model, seed = first_key
    path = Path(G.PRED_DIR) / G.PRED[model][seed]
    for (m, s), weight_sha in G.WEIGHTS.items():
        doc = {
            'set_sha256': G.SET_SHA, 'set_id': G.G.SET_ID,
            'checkpoint': {'weights_sha256': weight_sha, 'seed': s},
            'titles': {'sha256': G.TITLES_SHA},
            'rows': [{'id': x} for x in ids],
        }
        (Path(G.PRED_DIR) / G.PRED[m][s]).write_text(json.dumps(doc), encoding='utf-8')
    if mutate:
        doc = json.loads(path.read_text(encoding='utf-8'))
        mutate(doc)
        path.write_text(json.dumps(doc), encoding='utf-8')
    try:
        G.check_predictions(ids)
    except SystemExit:
        return
    raise AssertionError('invalid prediction metadata was accepted')


def prediction_guard():
    old = (G.PRED_DIR, G.SET_SHA, G.TITLES_SHA, G.G.SET_ID)
    ids = ['g3-id-1', 'g3-id-2']
    try:
        with tempfile.TemporaryDirectory() as td:
            G.PRED_DIR, G.SET_SHA, G.TITLES_SHA, G.G.SET_ID = td, 'set-sha', 'titles-sha', 'set-id'
            for mutate in (
                lambda d: d.update(set_sha256='wrong'),
                lambda d: d.update(set_id='wrong'),
                lambda d: d['checkpoint'].update(weights_sha256='wrong'),
                lambda d: d['checkpoint'].update(seed=999),
                lambda d: d['titles'].update(sha256='wrong'),
                lambda d: d.update(rows=[{'id': ids[0]}]),
                lambda d: d.update(rows=[{'id': ids[0]}, {'id': ids[0]}]),
                lambda d: d.update(rows=[{'id': ids[0]}, {'id': ids[1]}, {'id': 'extra'}]),
            ):
                expect_prediction_rejected(ids, mutate)
            expect_prediction_rejected([ids[0], ids[0]])
    finally:
        G.PRED_DIR, G.SET_SHA, G.TITLES_SHA, G.G.SET_ID = old


def main():
    original = G.RC.cue_types
    original_factory = G.D.EF.FX.make_cue_types
    a,b = probe(False),probe(True)
    assert a == {'Funding': [], 'Students': [], 'abfall_kwh': []}
    assert b == {'Funding': ['amount'], 'Students': ['quantity'], 'abfall_kwh': ['quantity']}
    assert G.RC.cue_types is original
    assert G.D.EF.FX.make_cue_types is original_factory
    try:
        try:
            probe(True,True)
        except RuntimeError:
            pass
        else:
            raise AssertionError('exception probe did not raise')
    finally:
        assert G.D.EF.FX.make_cue_types is original_factory
        assert G.RC.cue_types is original
    assert G.RG.V is G.D.EF.V
    candidate=G.RG.V.candidate
    with patch.object(G.RG.V,'candidate',candidate), patch.object(G.RG,'_orig',return_value='amount'):
        with G.RG.use():
            args=('unknown',None,'unknown',[],None,np.zeros(len(G.D.V.LABELS)),list(G.D.V.LABELS),.8)
            for header,expected in [('Value',None),('Budget','amount')]:
                arg=list(args);arg[4]=header
                assert G.RG.V.candidate(*arg)==expected
    assert G.RG.V.candidate is candidate
    with G.RG.use():
        assert G.RG.V.candidate is G.RG.guarded_candidate
    assert G.RG.V.candidate is candidate
    labels=Path(sys.argv[1])
    data=G.load_g3(str(labels))['g3']
    assert len(data)==len({c['id'] for c in data})==790
    scored=[c for c in data if c['truth'] not in ('unknown','S','other','person')]
    assert len(scored)==555
    titles=ROOT/'independent_eval/results/g3/titles.json'
    assert hashlib.sha256(titles.read_bytes()).hexdigest()=='281e038bc3c5994b5e368416fedeb2023cb4a079300abc8c67f0d4b15aa5773c'
    assert {c['table'] for c in data}==set(json.loads(titles.read_text()))
    prediction_guard()
    assert hashlib.sha256(Path(G.__file__).read_bytes()).hexdigest()=='b8b37850f5bce4285c57916e20fb6d8635eecc31bc9546edb54f910018d092c1'
    workflow=ROOT/'.github/workflows/g3-predict.yml'
    assert hashlib.sha256(workflow.read_bytes()).hexdigest()=='be37690399f6292d210322568f7663e627ede9b368f6ad6b6c39e2704af8ab7b'
    print(json.dumps({'current_without_M':a,'current_with_M':b,'M_exception_restoration':'passed',
          'prediction_origin_negative_cases_rejected':9,'workflow_and_evaluator_sha':'passed',
          'R_module_identity_and_behavior':'passed','context_restoration':'passed',
          'rows':len(data),'scored':len(scored),'titles':126,'publishers':len({c['publisher'] for c in data})},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
