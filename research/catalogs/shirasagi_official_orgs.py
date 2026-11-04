"""6県の公開組織ページから部署名とリンクだけを保存する。"""
import concurrent.futures,json,re,sys
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urljoin,urlparse
sys.path.insert(0,str(Path(__file__).resolve().parent))
from nonckan_probe import get,Links,ROOT
SITES={'青森県':'https://www.pref.aomori.lg.jp/soshiki/','静岡県':'https://www.pref.shizuoka.jp/kensei/introduction/soshiki/index.html','鳥取県':'https://www.pref.tottori.lg.jp/soshiki/','徳島県':'https://www.pref.tokushima.lg.jp/kenseijoho/soshiki/','香川県':'https://www.pref.kagawa.lg.jp/soshiki/','愛媛県':'https://www.pref.ehime.jp/soshiki/'}
def extract(pref,url):
 raw,final,ct=get(url);text=raw.decode('utf-8','replace')
 if 'json' in ct:text=json.loads(text).get('static_html','')
 parser=Links();parser.feed(text);out=[];seen=set()
 for href,label in parser.links:
  name=label.strip().split('\n')[0].strip();link=urljoin(final,href)
  if not re.fullmatch(r'[\w\s・･（）()／/、～ー−－]+(?:課|部|局|室|センター|委員会|本部|事務所)',name):continue
  if urlparse(link).hostname!=urlparse(final).hostname or (link,name) in seen:continue
  out.append({'url':link,'name':name});seen.add((link,name))
 return {'pref':pref,'url':final,'organization_links':out}
def main():
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(lambda kv:extract(*kv),SITES.items()))
 (ROOT/'research/catalogs/shirasagi_official_organizations_20261105.json').write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),'metadata_only':True,'results':rows},ensure_ascii=False,indent=1)+'\n')
 for row in rows:print(row['pref'],len(row['organization_links']),flush=True)
if __name__=='__main__':main()
