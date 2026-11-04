"""b124〜b141の豪州403をActionsから診断。本文は保存しない。"""
import json
import re
import io
import csv
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode, urlparse
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'materials'))
import fetch_rows as F
UA = 'jitsuris-train-s11/1.0 (source and license recorded)'
VARIANTS = {
 'original': {'User-Agent': UA},
 'accept_csv': {'User-Agent': UA, 'Accept': 'text/csv,application/octet-stream;q=0.9,*/*;q=0.1'},
 'contact': {'User-Agent': 'jitsuris-train/1.0 (+https://github.com/hehohahifu83-cmyk/jitsuris-train; open data research)', 'Accept': '*/*'},
}
def probe(url, headers):
    try:
        with urlopen(Request(url, headers=headers), timeout=30) as r:
            raw = r.read(3_000_001)
            lead = raw[:2048].lstrip().lower()
            parsed = {}
            try:
                fields, records, n = F.parse_csv(raw[:3_000_000], len(raw)>3_000_000, encodings=F.CP1252_FIRST)
                parsed = {'fields':len(fields),'records':n}
            except ValueError as e:
                parsed = {'parse_error':str(e)}
                try:
                    rows=list(csv.reader(io.StringIO(raw[:20000].decode('utf-8-sig'),newline='')))
                    parsed['first40_widths']=[len(row) for row in rows[:40]]
                    parsed['first40_filled']=[sum(bool(c.strip()) for c in row) for row in rows[:40]]
                except Exception: pass
            return {'parse':parsed, 'status': r.status, 'final_host': urlparse(r.geturl()).hostname,
                    'content_type': r.headers.get('Content-Type'), 'bytes_read': len(raw),
                    'html': lead.startswith((b'<!doctype',b'<html')), 'zip': raw[:4] == b'PK\x03\x04'}
    except HTTPError as e:
        return {'status': e.code, 'final_host': urlparse(e.geturl()).hostname, 'server': e.headers.get('Server')}
    except Exception as e:
        return {'error': type(e).__name__}

def main():
    selected, seen = [], set()
    for n in range(124,128):
        d=ROOT/f'materials/pool/work/b{n}'
        adopted={a['n']:a for a in json.loads((d/'adopted.json').read_text())['adopted']}
        for t in json.loads((d/'corpus_log.json').read_text())['tables']:
            error=t.get('error','')
            kind='403' if 'csv: HTTP 403' in error else 'header' if 'header row not found' in error else None
            if not kind:continue
            a=adopted[t['n']]
            # Two resources from each batch; retain no values or teacher labels.
            if a['resource_id'] in seen or sum(x['batch']==n and x['kind']==kind for x in selected)>=2: continue
            seen.add(a['resource_id'])
            selected.append({'batch':n,'kind':kind,**a})
    out=[]
    for a in selected:
        rid=a['resource_id']; base='https://data.gov.au/data/api/3/action/'
        r={'kind':a['kind'],'batch':a['batch'],'resource_id':rid,'resource_url':a['resource_url']}
        try:
            with urlopen(Request(base+'resource_show?'+urlencode({'id':rid}),headers={'User-Agent':UA,'Accept':'application/json'}),timeout=30) as resp:
                res=json.load(resp)['result']
            url=res['url']; r['metadata_url']=url
            if url.startswith('http://'):url='https://'+url[7:]
            r['tested_url']=url
            for variant,headers in VARIANTS.items():
                r[variant]=probe(url,headers); time.sleep(.5)
            # CKAN's advertised /download link may differ from the canonical metadata URL.
            path=urlparse(url).path
            r['catalog_download']=probe(a['resource_url']+'/download/'+path.rsplit('/',1)[-1],VARIANTS['original'])
            if urlparse(url).hostname=='data.gov.au' and '/download/' in url:
                canonical='https://data.gov.au'+path
                if canonical!=url: r['canonical_without_query']=probe(canonical,VARIANTS['original'])
        except Exception as e: r['error']=type(e).__name__
        out.append(r); print(json.dumps(r),flush=True)
    doc={'created_utc':datetime.now(timezone.utc).isoformat(),'runner':'GitHub Actions','rows':out}
    p=ROOT/'research/fetch_diag/recovery_probe.json';p.write_text(json.dumps(doc,ensure_ascii=False,indent=1)+'\n')
if __name__=='__main__':main()
