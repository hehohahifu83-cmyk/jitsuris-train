"""G4再点検：合成データだけ。実データの収集・凍結・学習・予測を起動しない。"""
import contextlib,copy,hashlib,io,json,re,sys
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'independent_eval'),str(ROOT/'tests')]
import g4 as G
from test_g4 import AtomicFreezeTest
A='alberta_cat:a-org'

def main():
    checks=[]
    prereg=(ROOT/'bench/g4_prereg_20261118.md').read_text()
    for name,sha in re.findall(r'\| `([^`]+)`[^|]*\| `([0-9a-f]{64})` \|',prereg):
        if name.startswith(('independent_eval/','tests/')) or name in ('encoder_context.py','encoder_exp.py','finetune_exp.py','evaluate_independent.py'):
            assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==sha,name
            checks.append(name)
    def rec(url,rid):return {'resource_url':url,'resource_id':rid,'publisher_id':A,'platform':'ckan','host':'open.alberta.ca','access':'datastore','license':'ogla','title':'synthetic'}
    p1,p2,p3=rec('p1','pid1'),rec('p2','pid2'),rec('p3','pid3')
    first={'adopted':[dict(p1,n='1'),dict(p2,n='2'),dict(p3,n='3')],'reserves':{A:[rec('r1','rid1'),rec('r2','rid2')]}}
    expected=[dict(rec('r1','rid1'),n='4',replaces='p1'),dict(rec('r2','rid2'),n='5',replaces='p3')]
    assert G.expected_reserves(first,{'p2'})==(expected,2)
    valid={'adopted':expected,'failed':2}
    assert len(G.adopted_entries(first,valid,{'p2'}))==5
    rejected=[]
    def reject(label,doc,pages={'p2'}):
        try:G.adopted_entries(first,doc,pages)
        except SystemExit:rejected.append(label)
        else:raise AssertionError('受理された: '+label)
    for i in range(2):
        for key in expected[i]:
            doc=copy.deepcopy(valid);doc['adopted'][i][key]='tampered'
            reject(f'reserve[{i}].{key}',doc)
    doc=copy.deepcopy(valid);doc['adopted'][1]['replaces']='p1';reject('二重置換',doc)
    reject('失敗数',dict(valid,failed=3))
    reject('成功した元の置換',valid,{'p1','p2'})
    fixture=AtomicFreezeTest('test_ok_then_refuse_existing');fixture.setUp()
    artifact_rejected=[]
    try:
        out=Path(fixture.tmp)/'independent-probe'/'g4'
        G.atomic_freeze(out,fixture.rows,fixture.ent)
        raw={n:(out/n).read_bytes() for n in ('g4.json','provenance.json','titles.json')}
        with patch.object(G,'OUT',out),patch.object(G,'load_rows',return_value=fixture.rows),patch.object(G,'adopted_entries',return_value=fixture.ent):
            def verify():
                with contextlib.redirect_stdout(io.StringIO()):G.cmd_verify(None)
            verify()
            prov=json.loads(raw['provenance.json'])
            bads=[('titles.json',{'t001':'tampered title'},'titles'),('provenance.json',{},'空provenance'),('provenance.json',{**prov,'frozen_utc':''},'空時刻')]
            for k in prov:
                if k!='frozen_utc':bads.append(('provenance.json',{**prov,k:{'tampered':True}},'provenance.'+k))
            for name,doc,label in bads:
                (out/name).write_text(json.dumps(doc))
                try:verify()
                except SystemExit:artifact_rejected.append(label)
                else:raise AssertionError('受理された: '+label)
                (out/name).write_bytes(raw[name])
            (out/'g4.json').write_bytes(raw['g4.json']+b'\n')
            try:verify()
            except SystemExit:artifact_rejected.append('g4 bytes')
            else:raise AssertionError('バイト差が受理された')
            (out/'g4.json').write_bytes(raw['g4.json'])
            (out/'provenance.json').write_text(json.dumps({**prov,'frozen_utc':'2026-11-20T00:00:00+00:00'}))
            verify()  # 明示された時刻だけの差は受理
    finally:fixture.tearDown()
    print(json.dumps({'prereg_sha_matches':checks,'reserve_mutations_rejected':rejected,'artifact_mutations_rejected':artifact_rejected,'valid_cli_verify':'passed','timestamp_only_change':'allowed as specified','real_G4_operations':'none'},ensure_ascii=False,indent=1))

if __name__=='__main__':main()
