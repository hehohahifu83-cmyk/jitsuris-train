"""保存済みG3予測を再現し、各段の出力を独立追跡する。本体予測・元レポートは変更しない。"""
import contextlib
import hashlib
import json
import os
import sys
import tempfile
import numpy as np
from collections import Counter
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/g3'))
import amount_unknown as A
G=A.E
original_base=G.D.EF.E.base_decisions
original_combine=G.D.EF.E.combine
original_candidate=G.D.EF.V.candidate
original_veto=G.D.EF.V.amount_cue_veto
original_dictionary=G.D.EF._dictionary
state={}; traces=[]

def base(cols):
    result=original_base(cols)
    state['rows']=[{'id':c['id'],'truth':c['truth'],'header':c['header'],'table':c['table'],
                    'guarded':c['pred'],'guard_reason':c.get('guard_reason'),'recheck':r[0],'recheck_reason':r[1]} for c,r in zip(cols,result)]
    state['scored']=[r for r in state['rows'] if r['truth'] and r['truth'] not in ('unknown','S','other','person')]
    state['next']=0
    return result

def combine(*args,**kwargs):
    result=original_combine(*args,**kwargs)
    for k,r in enumerate(state['rows']):
        x=result[k];r.update(verifier=x[0],verifier_reason=x[1])
    return result

def candidate(*args,**kwargs):
    result=original_candidate(*args,**kwargs)
    row=state['scored'][state['next']];state['next']+=1
    state['active']=row
    row['rho']=result if result else args[0]
    return result

class Dictionary:
    def __init__(self,obj):self.obj=obj
    def apply(self,*args,**kwargs):
        result=self.obj.apply(*args,**kwargs);state['active']['dictionary']=result[0];return result

def dictionary():return Dictionary(original_dictionary())

def veto(*args,**kwargs):
    result=original_veto(*args,**kwargs)
    row=state['active'];row['final']=result
    if row['truth'] in ('amount','quantity','rate'):
        if result!='unknown':stage='答えた'
        else:
            seq=[('本体・見張り',row['guarded']),('再確認',row['recheck']),('検査役',row['verifier']),('rho',row['rho']),('辞書',row['dictionary']),('通貨の手がかり',result)]
            prev=None;stage='本体・見張り'
            for name,value in seq:
                if value=='unknown' and prev!='unknown':stage=name
                prev=value
        row['actual_stage']=stage;traces.append(dict(row))
    return result

def main():
    labels=Path(sys.argv[1]).resolve();out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
    for path,expected in ((ROOT/'materials/dictionary'/G.R.DICTS['K'][0],G.R.DICTS['K'][1]),):
        assert hashlib.sha256(path.read_bytes()).hexdigest()==expected
    os.environ['JITSURIS_DICT']=str(ROOT/'materials/dictionary'/G.R.DICTS['K'][0])
    with tempfile.TemporaryDirectory() as tmp, \
         patch.object(A,'HERE',tmp), \
         patch.object(sys,'argv',['amount_unknown.py','--labels',str(labels)]), \
         patch.object(G.D.EF.E,'base_decisions',side_effect=base), \
         patch.object(G.D.EF.E,'combine',side_effect=combine), \
         patch.object(G.D.EF.V,'candidate',side_effect=candidate), \
         patch.object(G.D.EF,'_dictionary',side_effect=dictionary), \
         patch.object(G.D.EF.V,'amount_cue_veto',side_effect=veto):
        col={'id':'probe','batch':'probe','header':'Value','table':'t',
             'truth':'amount','pred':'amount','top3':[{'label':'amount','probability':.99}],
             'values':['$1.00'],'values5':['$1.00'],'unit':'','context':[]}
        with patch.object(G.D.EF,'probs',return_value=np.zeros((1,len(G.D.V.LABELS)))):
            G.D.EF.run({'probe':[col]},None,list(G.D.V.LABELS),G.D.PRODUCT+('K',),per={})
        assert len(traces)==1 and traces[0]['id']=='probe'
        traces.clear();state.clear()
        with (out/'replay_stdout.txt').open('w') as stdout,contextlib.redirect_stdout(stdout):A.main()
        replay=json.loads((Path(tmp)/'amount_unknown.json').read_text())
    expected=json.loads((ROOT/'research/g3/amount_unknown.json').read_text())
    assert replay==expected,'元の列ごとのJSONと不一致'
    assert len(traces)==len(replay)==588
    for r,t in zip(replay,traces):
        assert (r['id'],r['final'])==(t['id'],t['final'])
        t['seed']=r['seed']
    # 元データの値は転記せず、各段の判定だけを保存する。
    (out/'trace.json').write_text(json.dumps(traces,ensure_ascii=False,indent=1)+'\n')
    diff=[{'id':r['id'],'seed':r['seed'],'reported':r['stage'],'actual':t['actual_stage'],'truth':r['truth']} for r,t in zip(replay,traces) if r['final']=='unknown' and not r['stage'].startswith(t['actual_stage'])]
    summary={'replay_exact_match':True,'rows':len(replay),'amount':dict(Counter(r['stage'] for r in replay if r['truth']=='amount')),'last_unknown_stage_amount':dict(Counter(t['actual_stage'] for t in traces if t['truth']=='amount')),'stage_differences':diff,'first_reason_vs_last_stage_amount':dict(Counter(r['stage']+' -> '+t['actual_stage'] for r,t in zip(replay,traces) if r['truth']=='amount' and r['final']=='unknown'))}
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=1)+'\n');print(json.dumps(summary,ensure_ascii=False,indent=1))

if __name__=='__main__':main()
