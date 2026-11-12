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


def probe(with_m, proposed=False):
    seen = {}
    col = {'id':'probe','header':'Funding','values':['1'], 'values5':['1'],
           'truth':'unknown','pred':'unknown','top3':[], 'unit':''}
    def base(cols):
        for h in ('Funding', 'Students', 'abfall_kwh'):
            seen[h] = sorted(G.RC.cue_types(h, ''))
        return [('unknown', None)]
    factory = G.D.EF.FX.make_cue_types
    def proposed_factory(fixes):
        inner = factory(fixes)
        return lambda h,u='': inner(h,u) | G.FM.extra_cues(h,u)
    with patch.object(G.D,'with_job',return_value={'probe':[col]}), \
         patch.object(G.D.EF,'probs',return_value=np.zeros((1,len(G.D.V.LABELS)))), \
         patch.object(G.D.EF.E,'base_decisions',side_effect=base), \
         patch.object(G.D.EF.E,'combine',return_value=[('unknown',None)]):
        if proposed:
            with patch.object(G.D.EF.FX,'make_cue_types',side_effect=proposed_factory):
                G.run({},None,list(G.D.V.LABELS),'L24',1,with_m,False)
        else:
            G.run({},None,list(G.D.V.LABELS),'L24',1,with_m,False)
    return seen


def main():
    original = G.RC.cue_types
    a,b,c = probe(False),probe(True),probe(True,proposed=True)
    assert a == b  # 現行のMは採点内で消えるという不具合の再現
    assert c['Funding']==['amount'] and c['Students']==['quantity'] and c['abfall_kwh']==['quantity']
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
    with tempfile.TemporaryDirectory() as td:
        fp=Path(td)/'pred.json'
        fp.write_text(json.dumps({'set_sha256':'wrong-set','checkpoint':{'seed':999,'weights_sha256':'wrong-weight'},'rows':[{'id':'probe','guarded_prediction':'unknown','top3':[]}]}))
        got=G.D.with_job({'probe':[{'id':'probe'}]},str(fp))
        assert got['probe'][0]['pred']=='unknown'
    print(json.dumps({'prediction_metadata_mismatch_accepted':True,'current_without_M':a,'current_with_M':b,'proposed_factory_M':c,
          'R_module_identity_and_behavior':'passed','context_restoration':'passed',
          'rows':len(data),'scored':len(scored),'titles':126,'publishers':len({c['publisher'] for c in data})},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
