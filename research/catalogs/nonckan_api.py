"""公開された独自APIの実応答と、明示されたカタログ一覧CSVだけを確認する。"""
import concurrent.futures,csv,io,json,re,sys
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urlsplit,urljoin,parse_qs
sys.path.insert(0,str(Path(__file__).resolve().parent))
from nonckan_probe import get,Links,ROOT

def check(r):
 out={'url':r['url'],'municipality_links_count':r.get('municipality_links_count'),'checks':[]}
 # package_list links are documented on webapi pages. Limit=0 is explicitly documented.
 docs=[p for p in r.get('pages',[]) if 'webapi' in p['url']]
 if docs:
  base=docs[0]['url'].rsplit('/',1)[0];out['checks'].append(check_json(base+'/api/package_list?limit=0','package_list'))
 show=next((x['url'] for p in r.get('pages',[]) for x in p.get('api_links',[]) if '/api/package_show?' in x['url']),None)
 if show:out['checks'].append(check_json(show,'package_show'))
 # Municipality count is listed in HTML; store link counts separately from verified publishers.
 try:
  raw,fu,ct=get(r['url']);p=Links();p.feed(raw.decode('utf-8','replace'))
  muni={urljoin(fu,h):l.strip() for h,l in p.links if re.search(r'(?:県|府|都|市|町|村|北海道)$',l.strip()) and re.search(r'chiiki|organization|group',h)}
  out['municipality_links']=muni;out['municipality_links_count']=len(muni)
 except Exception:pass
 # DataEye uses /resources/<id> metadata pages and licence icons, not .csv links on the dataset index.
 ds=next((p['url'] for p in r.get('pages',[]) if re.search(r'/datasets/\d+$',p['url'])),None)
 if ds:
  try:
   raw,fu,ct=get(ds);h=raw.decode('utf-8','replace');p=Links();p.feed(h)
   res=[{'url':urljoin(fu,x),'label':y[:80]} for x,y in p.links if re.search(r'/resources/\d+',x)]
   licenses=list(dict.fromkeys(re.findall(r'.{0,60}(?:creativecommons.org/licenses/[^"<> ]+|CC[-_ ]?BY|表示.{0,12}4\.0|PDL1\.0).{0,80}',h,re.I)))[:5]
   out['dataeye_metadata']={'dataset_url':ds,'resource_links':res[:5],'license_markup':licenses}
  except Exception as e:out['dataeye_metadata']={'error':str(e)[:100]}
 return out

def check_json(url,action):
 out={'url':url,'action':action}
 try:
  raw,fu,ct=get(url);out['content_type']=ct;p=json.loads(raw.decode('utf-8-sig'));data=p.get('result',p) if isinstance(p,dict) else p
  if action=='package_list':
   out['returned_type']=type(data).__name__;out['count']=len(data) if isinstance(data,list) else None;out['all_ids']=all(isinstance(x,str) for x in data) if isinstance(data,list) else None
  elif isinstance(data,dict):
   out['keys']=sorted(data);out['metadata']={k:data[k] for k in ('id','title','license_id','license_title') if k in data}
   out['resources']=[{k:x[k] for k in ('id','url','format','license','license_id') if k in x} for x in data.get('resources',[])][:4]
 except Exception as e:out['error']=type(e).__name__+': '+str(e)[:120]
 return out

def manifest():
 url='https://www.pref.miyagi.jp/documents/5880/od_20260325.csv';out={'url':url,'explicitly_catalogue_metadata':True}
 try:
  raw,fu,ct=get(url)
  for enc in ('utf-8-sig','cp932'):
   try:txt=raw.decode(enc);break
   except UnicodeError:continue
  rows=list(csv.DictReader(io.StringIO(txt)));out['headers']=list(rows[0]) if rows else [];out['records']=len(rows)
  out['url_fields']=[k for k in out['headers'] if re.search(r'URL|ＵＲＬ',str(k),re.I)];out['license_fields']=[k for k in out['headers'] if re.search(r'ライセンス|利用規約',str(k))]
 except Exception as e:out['error']=type(e).__name__+': '+str(e)[:100]
 return out

def main():
 rs=json.loads((ROOT/'research/catalogs/nonckan_detail_20261105.json').read_text())['results']
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:out=list(pool.map(check,rs))
 doc={'created_utc':datetime.now(timezone.utc).isoformat(),'metadata_only':True,'data_files_fetched':False,'results':out,'catalogue_manifest':manifest()}
 (ROOT/'research/catalogs/nonckan_api_20261105.json').write_text(json.dumps(doc,ensure_ascii=False,indent=1)+'\n')
 for r in out:print(r['url'],[(x['action'],x.get('count'),x.get('error')) for x in r['checks']])
if __name__=='__main__':main()
