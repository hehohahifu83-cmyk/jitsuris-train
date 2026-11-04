"""自治体ごとの代表メタデータページを確認。HTML・連絡先・本文は保存しない。"""
import argparse,concurrent.futures,json,sys,time
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from nonckan_probe import get,Links,ROOT

def verify(rows):
 out=[]
 for r in rows:
  if out:time.sleep(2)
  url=r['evidence_url'];entry={k:r[k] for k in ('site','municipality','municipality_code','evidence_url')}
  try:
   raw,final,ct=get(url,timeout=30);html=raw.decode('utf-8','replace')
   if 'json' in ct:html=json.loads(html).get('static_html','')
   p=Links();p.feed(html);text=' '.join(p.text)
   entry.update(retrieved=True,final_url=final,municipality_name_on_page=r['municipality'] in text,author_text_on_page=bool(r['author'] and r['author']!='[非保存]' and r['author'] in text),user_name_text_on_page=bool(r['user_name'] and r['user_name']!='[非保存]' and r['user_name'] in text))
  except Exception as e:entry.update(retrieved=False,error=type(e).__name__+': '+str(e)[:100])
  out.append(entry)
 print(rows[0]['site'],len(out),'metadata pages checked',flush=True)
 return out

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--skip-shizuoka',action='store_true');args=parser.parse_args()
 doc=json.loads((ROOT/'research/catalogs/shirasagi_owner_crosswalk_draft_20261105.json').read_text());bycity={}
 for r in doc['combinations']:
  if not r['municipality_code'] or (args.skip_shizuoka and 'shizuoka' in r['site']):continue
  key=(r['site'],r['municipality_code'])
  # 自治体名がauthorに明記されている組を先に確認する。
  if key not in bycity or r['author'].startswith(r['municipality']):bycity[key]=r
 bysite=defaultdict(list)
 for r in bycity.values():bysite[r['site']].append(r)
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:results=[r for rs in pool.map(verify,bysite.values()) for r in rs]
 (ROOT/'research/catalogs/shirasagi_owner_evidence_20261105.json').write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),'metadata_only':True,'scope':'自治体ごとの代表ページ。全組のHTML確認ではない。','skip_shizuoka':args.skip_shizuoka,'results':results},ensure_ascii=False,indent=1)+'\n')
if __name__=='__main__':main()
