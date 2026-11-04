"""公的CSV由来の非CKAN基点を調査。カタログHTML/JSONだけを読み、表の本体は読まない。"""
import concurrent.futures,hashlib,json,re,sys,time
from collections import Counter
from datetime import datetime,timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,urljoin,urlunsplit
from urllib.request import Request,urlopen
ROOT=Path(__file__).resolve().parents[2]
UA='jitsuris-train/1.0 (metadata only; +https://github.com/hehohahifu83-cmyk/jitsuris-train)'
DENY_EXT=re.compile(r'\.(?:csv|tsv|xlsx?|zip|pdf|kml|geojson|shp|xml|png|jpe?g)(?:$|[?#])',re.I)
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.text=[];self.current=None
 def handle_starttag(self,t,a):
  attrs=dict(a)
  if t=='a' and attrs.get('href'):self.current=[attrs['href'],''];self.links.append(self.current)
 def handle_endtag(self,t):
  if t=='a':self.current=None
 def handle_data(self,s):
  self.text.append(s)
  if self.current is not None:self.current[1]+=s

def get(url):
 p=urlsplit(url)
 if p.scheme not in ('http','https') or not p.hostname or p.username or p.password:raise ValueError('not a public catalog URL')
 with urlopen(Request(url,headers={'User-Agent':UA,'Accept':'application/json,text/html;q=0.9'}),timeout=12) as r:
  raw=r.read(4_000_001)
  if len(raw)>4_000_000:raise ValueError('metadata exceeds 4MB')
  return raw,r.geturl(),r.headers.get('Content-Type','')

def seeds():
 old=json.loads((ROOT/'materials/pool/probe/jp_catalogs_20261104.json').read_text());ckan={urlsplit(h['base']).hostname for h in old['hosts'] if h['ckan']};seen=set();out=[]
 for r in old['catalog_references']:
  name=r['municipality'];url=r['url'];host=urlsplit(url).hostname or ''
  priority=bool(name and (name.endswith(('県','府','都')) or name=='北海道'))
  shared=bool(re.search(r'dataeye|harp\.lg|opendata\.cc|opendata\.go\.jp|opendata\.pref\.',host))
  if host in ckan or host in {'odcs.bodik.jp','data.bodik.jp'} or not(priority or shared) or url in seen:continue
  seen.add(url);out.append({'municipality':name,'url':url,'source':r['source'],'prefecture':priority})
 return out[:128]

def probe(seed):
 out={**seed,'metadata_only':True,'pages':[]};alllinks={};texts=[]
 try:
  raw,final,ctype=get(seed['url']);txt=raw.decode('utf-8','replace');parser=Links();parser.feed(txt);texts+=parser.text
  out['final_url']=final;out['html_sha256']=hashlib.sha256(raw).hexdigest();out['generator']='DKAN' if re.search(r'dkan',txt,re.I) else 'Drupal' if re.search(r'Drupal',txt,re.I) else None
  for href,label in parser.links:
   u=urljoin(final,href)
   if urlsplit(u).scheme in ('http','https'):alllinks[u]=label.strip()[:100]
  root=urlunsplit((*urlsplit(final)[:2],'','',''))
  # Catalogue endpoints, never datastore or dataset resource contents.
  endpoints=[root+'/data.json',root+'/api/1/metastore/schemas/dataset/items',root+'/api/dataset.json']
  if out['generator'] is None:endpoints=endpoints[:1]
  for u in endpoints:
   try:
    b,fu,ct=get(u);data=json.loads(b.decode('utf-8-sig'));datasets=data.get('dataset') if isinstance(data,dict) else data if isinstance(data,list) else None
    if isinstance(datasets,list) and datasets and isinstance(datasets[0],dict):
     sample=[];publishers=set()
     for x in datasets:
      pub=x.get('publisher');publishers.add(json.dumps(pub,ensure_ascii=False,sort_keys=True)) if pub else None
     for x in datasets[:3]:sample.append({k:x[k] for k in ('title','identifier','license','publisher','distribution','resources','landingPage') if k in x})
     out['pages'].append({'url':u,'format':'dataset_metadata_json','returned_datasets':len(datasets),'returned_publishers':len(publishers),'sample':sample,'complete_count_verified':u.endswith('/data.json')})
   except Exception:pass
  # One metadata listing and one licence page if published on the same host.
  chosen=[]
  for pattern in [r'(dataset|データ一覧|カタログ)',r'(licen|terms|利用規約|利用条件)']:
   cand=[u for u,l in alllinks.items() if urlsplit(u).hostname==urlsplit(final).hostname and re.search(pattern,u+' '+l,re.I) and not DENY_EXT.search(u)]
   if cand:chosen.append(sorted(cand,key=len)[0])
  for u in dict.fromkeys(chosen):
   try:
    b,fu,ct=get(u);page=Links();page.feed(b.decode('utf-8','replace'));text=' '.join(page.text)
    snippets=[re.sub(r'\s+',' ',text[max(0,m.start()-70):m.end()+110]) for m in re.finditer(r'(?:[0-9,]+\s*(?:件|datasets|データセット)|(?:データセット|検索結果|全)\s*[:：]?\s*[0-9,]+\s*件|CC.?BY|クリエイティブ.{0,20}表示|政府標準利用規約|公共データ利用規約)',text,re.I)][:12]
    out['pages'].append({'url':fu,'format':'catalogue_or_terms_html','count_or_license_snippets':snippets})
    for h,l in page.links:alllinks.setdefault(urljoin(fu,h),l.strip()[:100])
   except Exception as e:out['pages'].append({'url':u,'error':type(e).__name__})
  out['metadata_links']=[{'url':u,'label':l} for u,l in alllinks.items() if re.search(r'dataset|カタログ|データ一覧|licen|terms|利用規約|データセット|api|json',u+' '+l,re.I) and not DENY_EXT.search(u)][:35]
  out['catalogue_manifest_candidates']=[{'url':u,'label':l,'fetched':False} for u,l in alllinks.items() if re.search(r'一覧|カタログ|メタデータ',l) and re.search(r'\.(csv|json)(?:$|\?)',u,re.I)][:10]
  combined=' '.join(texts)
  out['home_count_or_license_snippets']=[re.sub(r'\s+',' ',combined[max(0,m.start()-60):m.end()+100]) for m in re.finditer(r'[0-9,]+\s*(?:件|データセット)|CC.?BY|政府標準利用規約',combined,re.I)][:8]
 except Exception as e:out['error']=type(e).__name__+': '+str(e)[:160]
 return out

def main():
 selected=seeds();print('metadata seeds',len(selected),flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
  results=[]
  for r in pool.map(probe,selected):results.append(r);print(r['municipality'],r['url'],r.get('generator'),r.get('error','ok'),flush=True)
 out={'created_utc':datetime.now(timezone.utc).isoformat(),'metadata_only':True,'seeds':len(selected),'results':results}
 (ROOT/'research/catalogs/nonckan_probe_20261105.json').write_text(json.dumps(out,ensure_ascii=False,indent=1)+'\n')
if __name__=='__main__':main()
