"""追加依頼の原因調査とb148〜b151の非破壊再取得。生値・教師回答は保存しない。"""
import collections, hashlib, json, subprocess, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urlparse
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'materials'))
import fetch_rows as F
import pool_discover as D

def semantic_digest(path):
    rows=[json.loads(s) for s in path.read_text().splitlines() if s.strip()]
    for r in rows:r.pop('fetched_utc',None)
    return hashlib.sha256(json.dumps(rows,ensure_ascii=False,sort_keys=True).encode()).hexdigest()

def main():
    result_path=ROOT/'research/fetch_diag/round2_probe.json'
    retry='--retry' in sys.argv
    previous=json.loads(result_path.read_text()) if retry else None
    out={'started_utc':datetime.now(timezone.utc).isoformat(),'catalogs':previous['catalogs'] if retry else [],'refetch':[]}
    if retry:(ROOT/'research/fetch_diag/round2_probe_initial.json').write_text(json.dumps(previous,ensure_ascii=False,indent=1)+'\n')
    for host in ['gifu-opendata.pref.gifu.lg.jp','data.city.fukuyama.hiroshima.jp','opdt.city.toyama.lg.jp','opendata.city.imizu.toyama.jp']:
        if retry:continue
        F.ALLOWED_HOSTS.add(host); site='https://'+host
        stats=collections.Counter(); formats=collections.Counter();reasons=collections.Counter()
        try:
            pkgs=F.http_json(site+'/api/3/action/package_search?'+urlencode({'rows':1000}),'package_search')['result']
            stats['packages_total']=pkgs['count'];stats['packages_inspected']=len(pkgs['results'])
            for p in pkgs['results']:
                if any(r.get('datastore_active') for r in p.get('resources',[])):continue
                stats['packages_without_datastore']+=1
                for r in p.get('resources',[]):
                    fmt=str(r.get('format') or '').lower();formats[fmt]+=1
                    if D.csv_on_host(r,site):stats['direct_csv_resources']+=1
                    elif fmt in ('csv','text/csv') or str(r.get('url') or '').lower().split('?')[0].endswith('.csv'):
                        u=urlparse(str(r.get('url') or ''));reasons[f'{u.scheme}://{u.hostname}']+=1
            out['catalogs'].append({'host':host,'stats':dict(stats),'no_datastore_resource_formats':dict(formats),'csv_rejected_scheme_host':dict(reasons)})
        except Exception as e:out['catalogs'].append({'host':host,'error':type(e).__name__+': '+str(e)[:150]})
    with tempfile.TemporaryDirectory() as tmp:
        for n in range(148,152):
            b=f'b{n}'
            prior=next((r for r in previous['refetch'] if r['batch']==b),None) if retry else None
            if prior and prior['same_content']:
                out['refetch'].append(prior);continue
            d=ROOT/'materials/pool/work'/b;path=Path(tmp)/f'{b}.jsonl';log=Path(tmp)/f'{b}.log.json'
            subprocess.run([sys.executable,'-I','materials/fetch_rows.py','--adopted',str(d/'adopted.json'),'--out',str(path),'--log',str(log)],cwd=ROOT,check=True)
            result=json.loads(log.read_text());before=semantic_digest(d/'corpus.jsonl');after=semantic_digest(path)
            out['refetch'].append({'batch':b,'columns':result['columns'],'ok_tables':result['ok_tables'],'tables':result['tables'],'before_semantic_sha256':before,'after_semantic_sha256':after,'same_content':before==after})
    (ROOT/'research/fetch_diag/round2_probe.json').write_text(json.dumps(out,ensure_ascii=False,indent=1)+'\n')
    print(json.dumps(out,ensure_ascii=False))
if __name__=='__main__':main()
