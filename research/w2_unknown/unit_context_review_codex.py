"""W2 unit-context audit: allowed pool only; no training or label changes."""
import collections, hashlib, json, re
from pathlib import Path
import p0_input_diagnostic as P
OUT = Path(__file__).resolve().parent
MONEY = re.compile(r'\b(?:usd|eur|gbp|cad|dollars?|euros?)\b|[$€£]', re.I)

def counts(rows):
    return dict(sorted(collections.Counter(r[2] for r in rows).items()))

def run():
    paths = P.subprocess.check_output(['git','ls-tree','-r','--name-only',P.BASE,'materials/pool'],cwd=P.ROOT,text=True).splitlines()
    paths = [p for p in paths if re.fullmatch(r'materials/pool/batch_[^/]+\.jsonl',p)]
    assert not any('b018' in p for p in paths)
    docs = [json.loads(s) for p in paths for s in P.blob(p).decode().splitlines()]
    junk = {'nan','None','','NaN','null','NULL'}
    rows = [(d['header'].lstrip('\ufeff'),[v for v in d['values'] if v.strip() not in junk],d['label'],d['context'],d['table']) for d in docs]
    fixes = [json.loads(s) for s in P.blob('materials/pool/labelfix_v24.jsonl').decode().splitlines()]
    fm = {(d['table'],d['header'].strip()):d for d in fixes if d.get('decision')=='change'}
    rows = [r[:2]+(fm[r[4],r[0].strip()]['label'],)+r[3:] if (r[4],r[0].strip()) in fm and r[2]==fm[r[4],r[0].strip()]['from'] else r for r in rows]
    ec, pf = P.snapshot_module('encoder_context'),P.snapshot_module('pool_families')
    before, val = pf.split_val_by_family(rows,salt='jitsuris-poolval-v2',mod=8)
    train, capped = pf.cap_tables_per_family(before,4)
    assert (len(rows),len(before),len(train),len(val),capped)==(38654,34103,29696,4551,576)
    units = ec.unit_context_map(rows)
    scopes = {}
    for name,rs in [('pool_all',rows),('pool_train_before_cap',before),('pool_train',train)]:
        attached = [r for r in rs if units.get(r[4])]
        currency = [r for r in attached if MONEY.search(units[r[4]])]
        scopes[name] = dict(n=len(rs),unit_rows=len(attached),unit_labels=counts(attached),
            currency_rows=len(currency),currency_tables=len({r[4] for r in currency}),currency_labels=counts(currency),
            currency_amount_quantity=counts([r for r in currency if r[2] in {'amount','quantity'}]))
    examples = []
    for table,unit in units.items():
        if MONEY.search(unit):
            rs=[r for r in train if r[4]==table]
            examples.append(dict(table=table,unit=unit,train_labels=counts(rs),
                train_columns=[dict(header=r[0],truth=r[2]) for r in rs]))
    # Count label exposure after per-table<=60 and x3. Header perturbation cannot
    # change the earlier capped row selection or any label. Not a token audit.
    aug=ec.real_train_rows_with_units(train,3,10,True,units,lambda rng,h:h,per_table=60)
    ac=[r for r in aug if MONEY.search(r[4])]
    assert all(not r[4] or r[4] in units.values() for r in aug)
    results={}
    ds={}
    for suffix in ('4arms','5arms'):
        path=OUT/f'p0_results_{suffix}.json';d=json.loads(path.read_text());ds[suffix]=d
        assert d['baseline_matches']==12 and d['status']=='measured'
        arms={}
        for arm in d['rows'][0]['predictions']:
            c=collections.Counter()
            for r in d['rows']:
                p=r['predictions'][arm];c['correct' if p['guarded']==r['truth'] else 'unknown' if p['guarded']=='unknown' else 'wrong']+=1
            arms[arm]=dict(c)
        results[suffix]=dict(sha256=hashlib.sha256(path.read_bytes()).hexdigest(),counts=arms)
    max_probability_delta=0.0
    for a,b in zip(ds['4arms']['rows'],ds['5arms']['rows']):
        assert a['index']==b['index']
        for arm in a['predictions']:
            x,y=a['predictions'][arm],b['predictions'][arm]
            for k in ('raw','guarded','reason','token_ids'):assert x[k]==y[k]
            for (lx,px),(ly,py) in zip(x['top3'],y['top3']):
                assert lx==ly
                max_probability_delta=max(max_probability_delta,abs(px-py))
    assert max_probability_delta < 1e-5
    effects=[]
    for r in ds['5arms']['rows']:
        base=r['predictions']['baseline']
        effects.append(dict(index=r['index'],header=r['header'],truth=r['truth'],
            predictions={a:dict(raw=p['raw'],guarded=p['guarded'],reason=p['reason'],top1=p['top3'][0]) for a,p in r['predictions'].items()},
            changed_units={a:r['predictions'][a]['token_ids']!=base['token_ids'] for a in ('unit','unit_trainfmt')}))
    return dict(commit=P.BASE,currency_regex=MONEY.pattern,unit_tables=len(units),scopes=scopes,
        pool_augmented_label_exposure=dict(n=len(aug),currency_rows=len(ac),currency_labels=counts(ac)),
        currency_table_details=examples,p0=results,p0_effects=effects,common_arm_max_probability_delta=max_probability_delta,
        limitations=['pool only; excludes synthetic and other real training sources',
          'currency pattern explicit; not a universal currency detector',
          'marginal label counts do not identify conditional feature use or causal training effects'])

if __name__=='__main__':
    result=run()
    (OUT/'unit_context_review_codex.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k in ('scopes','pool_augmented_label_exposure','p0')},ensure_ascii=False,indent=2))
