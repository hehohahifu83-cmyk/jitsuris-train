"""公開元のフィールドの意味を調査。表本体・連絡先・個人名は保存しない。"""
import json,re,sys,time
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from nonckan_probe import get,ROOT

def safe(x):
 if isinstance(x,dict):
  return {k:safe(v) for k,v in x.items() if k in ('id','name','type','filename','parent_id','code','url','groups','areas')}
 if isinstance(x,list):return [safe(v) for v in x[:6]]
 if isinstance(x,str):
  if len(x)>100 or '@' in x or re.search(r'\d{2,4}[-－]\d{2,4}[-－]\d{3,4}',x):return '(omitted)'
  return x if re.search(r'県|市|町|村|課|部|局|センター|組合|政府|/dataset/',x) else '(omitted)'
 return x

def main():
 prior=json.loads((ROOT/'research/catalogs/nonckan_api_20261105.json').read_text());out=[]
 for r in prior['results']:
  shows=[x['url'] for x in r['checks'] if x['action']=='package_show']
  for u in shows:
   time.sleep(2)
   row={'url':u}
   try:
    raw,fu,ct=get(u);p=json.loads(raw.decode('utf-8-sig'));d=p.get('result',p)
    row['owner_fields']={k:{'type':type(d[k]).__name__,'keys':sorted(d[k]) if isinstance(d[k],dict) else None,'safe_evidence':safe(d[k])} for k in ('author','user','groups','areas','site') if k in d}
   except Exception as e:row['error']=type(e).__name__+': '+str(e)[:100]
   out.append(row)
 (ROOT/'research/catalogs/shirasagi_publishers_20261105.json').write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),'metadata_only':True,'results':out},ensure_ascii=False,indent=1)+'\n')
if __name__=='__main__':main()
