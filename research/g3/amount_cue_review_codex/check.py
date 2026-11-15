"""読むだけの語彙走査の再現と106判定の独立再集計。予測・規則は変更しない。"""
import contextlib, hashlib, io, json, re, sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT),str(ROOT/'research/g3'),str(ROOT/'research/fix_n')]
import fix_n as N

def main():
    assert hashlib.sha256((ROOT/'research/fix_n/fix_n.py').read_bytes()).hexdigest()=='672dd70566b70f16915a382f80dcc603194d92c178fac253a008d9452f2eda35'
    top=[{'label':'amount','probability':.99}]
    for sign in ('','-'):
        for zeros in (9,307,322,323,324):
            v=sign+'0.'+'0'*zeros+'1'
            assert N.n_check_assert('amount',top,[v],'Value',siblings=['Amount'])==('unknown','amount_precision'),v
    for v in ('0.0000000000','0.000','-0.000','0.12000000000000001'):
        assert N.n_check_assert('amount',top,[v],'Value',siblings=['Amount'])==('amount',None),v
    source=ROOT/'research/g3/amount_cue_vocab_scan.py'
    code=source.read_text();assert "B='/home/user/ai-bridge/labels'" in code
    code=code.replace("B='/home/user/ai-bridge/labels'","B='/workspace/ai-bridge/labels'")
    ns={'__name__':'scan_review','__file__':str(source)}
    with contextlib.redirect_stdout(io.StringIO()):exec(compile(code,str(source),'exec'),ns)
    fd=ns['FD']
    env={'python':'%d.%d'%sys.version_info[:2],'sklearn':fd.sklearn.__version__,'numpy':fd.np.__version__,'scipy':fd.scipy.__version__}
    assert env==fd.ENV
    counts={w:dict(Counter({lab:sum(n for (sn,l),n in c.items() if l==lab) for sn,lab in c})) for w,c in ns['out'].items()}
    ids={w:[c['id'] for data in ns['sets'].values() for cols in data.values() for c in cols if re.search(p,str(c['header']).lower())] for w,p in ns['words'].items()}
    for w,pat in ns['words'].items():
        independent=Counter(c['truth'] for data in ns['sets'].values() for cols in data.values() for c in cols if re.search(pat,str(c['header']).lower()))
        assert dict(independent)==counts.get(w,{}),(w,independent,counts.get(w))
        counts.setdefault(w,{})
    rows=json.loads((ROOT/'research/g3/amount_unknown.json').read_text())
    direct=[r for r in rows if r['truth']=='amount' and r['final']=='unknown' and (r['stage'].startswith('末尾の通貨確認') or (r['stage']=='再確認' and r['reason']=='amount_without_cue'))]
    assert len(direct)==106
    direct_tables=Counter(r['table'] for r in direct)
    # 元の独立追跡を使用（同じ採点コード・保存予測に対し588件完全一致を検証済み）。
    tr=json.loads((ROOT/'research/g3/amount_unknown_review_codex/trace.json').read_text())
    chosen=[r for r in tr if r['truth']=='amount' and r['final']=='unknown' and (r['actual_stage']=='通貨の手がかり' or (r['actual_stage']=='再確認' and r['recheck_reason']=='amount_without_cue'))]
    assert len(chosen)==106
    tables=dict(Counter(r['table'] for r in chosen))
    assert direct_tables==Counter(tables)
    assert tables=={'t012':20,'t022':24,'t045':3,'t062':21,'t069':2,'t098':30,'t103':3,'t118':3},tables
    f=json.loads((ROOT/'independent_eval/results/g3/g3.json').read_text())['columns']
    income=[c['id'] for c in f if c['table']=='t098' and 'income' in c['header'].lower()]
    cents=[{'id':c['id'],'header':c['header']} for c in f if c['id'] in ('g3-0440','g3-0441')]
    import g3_eval as G
    samples=[]
    for c in G.load_g3('/workspace/ai-bridge/labels/g3/final.jsonl')['g3']:
        if c['id'] in ('g3-0071','g3-0398'):
            samples.append({'id':c['id'],'table':c['table'],'sample_rows':len(c['tab']['rows']),'unique_sample_values':len(set(c['tab']['rows'])),'total_rows':c['tab']['total'],'row_indices_available':bool(c['tab']['row_index'])})
    out={'environment':env,'indicator_sample_metadata':samples,'N_tiny_boundary_checks':14,'vocabulary_label_counts':counts,'vocabulary_total_columns':{w:sum(c.values()) for w,c in counts.items()},'scan_duplicate_ids':{w:len(v)-len(set(v)) for w,v in ids.items()},'unknown_106_by_table':tables,'t098_income_columns':income,'t069_explicit_cent_headers':cents}
    print(json.dumps(out,ensure_ascii=False,indent=1))

if __name__=='__main__':main()
