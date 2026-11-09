"""Read-only counterexample audit for frozen fix J; excludes F1 and sealed sets."""
import collections, hashlib, json, re, sys, unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'research/w2_unknown'))
import fix_j as J
import p0_input_diagnostic as P
OUT=Path(__file__).resolve().parent
CASES=[
 ('J1','平0','era year zero'),
 ('J1','昭99','outside Showa era'),
 ('J2','令和 0年99月','invalid year and month'),
 ('J3','99月99日午後99時99分','out-of-range components'),
 ('J4','marketing 2020','ordinary English word'),
 ('J4','maybe 2020','ordinary English word'),
 ('J5','marketing-marchandise 2020','ordinary English words'),
 ('J6','99/octopus/2020 99:99','invalid month token and fields'),
 ('J7','99NOV17:99:99:99','invalid SAS day and time'),
 ('J8','00:02:37.00','elapsed duration can have identical syntax'),
 ('J9','1.20-2.30','decimal interval can have identical syntax'),
 ('J10','2.8.12','reference identifier observed in pool'),
 ('J10','31.02.18','impossible calendar date'),
]

def norm(v):
 return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',str(v)).strip().lower().translate(J.DASHES))
def classify(v):
 return [f'J{i+1}' for i,p in enumerate(J.J_RES) if p.match(norm(v))]
def load():
 paths=P.subprocess.check_output(['git','ls-tree','-r','--name-only',P.BASE,'materials/pool'],cwd=ROOT,text=True).splitlines()
 paths=[p for p in paths if re.fullmatch(r'materials/pool/batch_[^/]+\.jsonl',p)]
 assert not any('b018' in p for p in paths)
 docs=[json.loads(s) for p in paths for s in P.blob(p).decode().splitlines()]
 fix=[json.loads(s) for s in P.blob('materials/pool/labelfix_v24.jsonl').decode().splitlines()]
 fm={(d['table'],d['header'].strip()):d for d in fix if d.get('decision')=='change'}
 rows=[]
 for d in docs:
  h=d['header'].lstrip('\ufeff');t=d['table'];label=d['label'];f=fm.get((t,h.strip()))
  if f and label==f['from']:label=f['label']
  rows.append((h,[v for v in d['values'] if v.strip() not in {'nan','None','','NaN','null','NULL'}],label,d['context'],t))
 assert len(rows)==38654
 return rows

def run():
 digest=hashlib.sha256((OUT/'fix_j.py').read_bytes()).hexdigest()
 assert digest=='3f273c999ed17e62e0e5db7c646506c6660c19b7092b7b07c2d5a49b85052a7c'
 rows=load();per_rule={f'J{i+1}':dict(matching_columns=0,nondate_columns=0,nondate_examples=[]) for i in range(len(J.J_RES))}
 new=collections.Counter();candidates=[]
 for r in rows:
  h,vs,truth,ctx,table=r
  rules={k for v in vs for k in classify(v)}
  for k in rules:
   per_rule[k]['matching_columns']+=1
   if truth!='date':
    per_rule[k]['nondate_columns']+=1
    per_rule[k]['nondate_examples'].append(dict(header=h,truth=truth,table=table,
       matching_values=[v for v in vs if k in classify(v)],column_passes_J=J.j_keeps_date(vs)))
  # Counterfactual gate is explicit: this is potential exposure if raw=date .95,
  # not a new observed model prediction or automatic label correction.
  old,reason=J.guard.guard_with_reason('date',[('date',.95),('other',.05)],vs,header=h)
  if old=='unknown' and reason=='date_value_evidence_low' and J.j_keeps_date(vs):
   new[truth]+=1
   candidates.append(dict(header=h,truth=truth,table=table,values=vs,rules=sorted(rules)))
 synthetic=[]
 for rule,value,meaning in CASES:
  assert rule in classify(value) and J.j_value(value)
  synthetic.append(dict(rule=rule,value=value,meaning=meaning,current_J_accepts=True,
      guard_G_reason=J.guard.guard_with_reason('date',[('date',.95),('other',.05)],[value]*5,header='Value')[1]))
 # A column of reference hierarchy codes passes J although current guard+G rejects.
 codes=['2.8.12','2.8.13','2.8.14','2.8.15','2.8.16']
 assert J.j_keeps_date(codes)
 assert J.guard.guard_with_reason('date',[('date',.95),('other',.05)],codes,header='Ref.')[1]=='date_value_evidence_low'
 pf=P.snapshot_module('pool_families');_,val=pf.split_val_by_family(rows,salt='jitsuris-poolval-v2',mod=8)
 observed=collections.Counter()
 for job in range(1,7):
  ps=json.loads((ROOT/f'eval_reports/latest/job{job}_probs_val_pool_ft.json').read_text())['rows']
  assert len(ps)==len(val)==4551
  for p in ps:
   r=val[p['index']];h,v=r[0],r[1]
   assert (P.normalize(h),r[2])==(P.normalize(p['column']),p['truth'])
   if p['raw_prediction']=='date' and p['decision_reason']=='date_value_evidence_low':
    if J.guard.header_date_ok(h,v) or J.guard.header_date_ok_g(h,v):observed['G_before_J']+=1
    elif J.j_keeps_date(v):observed['recovered' if p['truth']=='date' else 'new_error']+=1
 assert dict(observed)=={'recovered':111,'G_before_J':185}
 return dict(snapshot=P.BASE,fix_j_sha256=digest,rows=len(rows),per_rule=per_rule,
   potential_new_columns_given_date_raw=dict(new),potential_examples=candidates,
   newly_passing_strong_share=dict(collections.Counter(r[2] for r in rows if J.guard.date_shares(r[1])[0]<.5 and J.j_keeps_date(r[1]))),
   observed_pool_six_jobs=dict(observed),synthetic_counterexamples=synthetic,
   synthetic_reference_column=codes,
   warning='Synthetic/potential matches do not establish actual model errors; F1 was not read.')
if __name__=='__main__':
 d=run();(OUT/'fix_j_review_codex.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:d[k] for k in ('rows','potential_new_columns_given_date_raw','observed_pool_six_jobs')},ensure_ascii=False))
 print({k:(v['matching_columns'],v['nondate_columns']) for k,v in d['per_rule'].items()})
