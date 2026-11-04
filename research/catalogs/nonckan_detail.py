"""非CKAN共同ポータルの件数・機械可読メタデータの具体例を確認。本体ファイルは開かない。"""
import concurrent.futures,json,re,sys
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urljoin,urlsplit,parse_qs
sys.path.insert(0,str(Path(__file__).resolve().parent))
from nonckan_probe import get,Links,DENY_EXT,ROOT
TARGETS=['https://www.harp.lg.jp/opendata/','https://opendata.pref.aomori.lg.jp/','https://opendata.pref.akita.lg.jp/','https://opendata.pref.shizuoka.jp/','https://odp-pref-tottori.tori-info.co.jp/','https://opendata.pref.tokushima.lg.jp/','https://opendata.pref.kagawa.lg.jp/','https://shimane-opendata.jp/','https://miyagi.dataeye.jp/','https://hiroshima-opendata.dataeye.jp/','https://www.pref.ehime.jp/opendata-catalog/','https://opendata.pref.kanagawa.jp/']
def detail(url):
 out={'url':url,'pages':[],'data_files_fetched':False}
 try:
  raw,final,ct=get(url);html=raw.decode('utf-8','replace');p=Links();p.feed(html)
  links={urljoin(final,h):l.strip() for h,l in p.links};host=urlsplit(final).hostname;text=' '.join(p.text)
  out['final_url']=final;out['software_evidence']=list(dict.fromkeys(re.findall(r'.{0,40}(?:shirasagi|Drupal|DKAN|dataeye|FileMaker).{0,70}',html,re.I)))[:5]
  municipality={}
  for u,l in links.items():
   if re.search(r'/dataset/chiiki/[^/]+/[^/]+',u) or 'organization_id=' in u:
    if re.search(r'(?:県|都|府|市|町|村|北海道)$',l):municipality[u.rstrip('/')]=l
  out['municipality_links_count']=len(municipality);out['municipality_links']=municipality
  out['home_counts']=re.findall(r'.{0,50}(?:[0-9,]+\s*(?:件|データセット)|データセット.{0,20}[0-9,]+).{0,80}',text)[:8]
  docs=[u for u,l in links.items() if re.search(r'Web.?API|APIの|APIについて|api.html|/api/?$',u+' '+l,re.I) and not DENY_EXT.search(u)]
  ds=[u for u in links if urlsplit(u).hostname==host and (re.search(r'/datasets/\d+$|/dataset/\d+\.html$',u))]
  listings=[u for u in links if urlsplit(u).hostname==host and re.search(r'/datasets$|/dataset/$|/dataset/search/$',u)]
  terms=[u for u,l in links.items() if urlsplit(u).hostname==host and re.search(r'利用規約|terms|kiyaku|privacy',u+' '+l) and not DENY_EXT.search(u)]
  out['api_documentation_links']=docs[:6]
  chosen=list(dict.fromkeys(docs[:1]+listings[:1]+ds[:1]+terms[:1]))
  for u in chosen:
   try:
    b,fu,ct=get(u);h=b.decode('utf-8','replace');page=Links();page.feed(h);body=re.sub(r'\s+',' ',' '.join(page.text));ll=[(urljoin(fu,x),y.strip()) for x,y in page.links]
    files=[{'url':x,'label':y[:120]} for x,y in ll if re.search(r'\.(csv|xlsx?)(?:$|[?#])',x,re.I)]
    lic=list(dict.fromkeys(re.findall(r'.{0,60}(?:CC.?BY|クリエイティブ.{0,35}表示|表示.{0,10}CC|政府標準利用規約|公共データ利用規約|ライセンス.{0,25}).{0,150}',body,re.I)))[:8]
    counts=re.findall(r'.{0,30}(?:[0-9,]+\s*件|データセット.{0,10}[0-9,]+).{0,70}',body)[:5]
    api=[{'url':x,'label':y[:120]} for x,y in ll if re.search(r'/api/|Web.?API',x+' '+y,re.I)]
    out['pages'].append({'url':fu,'files':files[:6],'license_evidence':lic,'count_evidence':counts,'api_links':api[:10]})
   except Exception as e:out['pages'].append({'url':u,'error':str(e)[:100]})
  # JSON-LD is catalog metadata, not source records.
  blocks=re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',html,re.S)
  out['json_ld_blocks']=len(blocks)
  out['javascript_or_api_urls']=list(dict.fromkeys(re.findall(r'["\']([^"\']+(?:/api/|\.js(?:\?[^"\']*)?)[^"\']*)["\']',html)))[:12]
 except Exception as e:out['error']=str(e)[:160]
 return out

def main():
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:results=list(p.map(detail,TARGETS))
 (ROOT/'research/catalogs/nonckan_detail_20261105.json').write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),'metadata_only':True,'results':results},ensure_ascii=False,indent=1)+'\n')
 for r in results:print(r['url'],r.get('municipality_links_count'),r.get('error','ok'))
if __name__=='__main__':main()
