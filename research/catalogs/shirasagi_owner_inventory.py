"""提供元対応表のための公開カタログメタデータ集計。資料・連絡先は保存しない。"""
import concurrent.futures,hashlib,json,re,sys,time
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urlencode,urlparse
sys.path.insert(0,str(Path(__file__).resolve().parent))
from nonckan_probe import ROOT,get

MUNICIPALITIES=json.loads((ROOT/'materials/dict/jp_municipalities.json').read_text())
MUNICIPAL_NAMES={r['city'] or r['pref'] for r in MUNICIPALITIES}
PREF_NAMES={r['pref'] for r in MUNICIPALITIES}
def public_org(value):
 value=str(value or '').strip()
 if not value:return ''
 if len(value)>180 or '@' in value or re.search(r'\d{2,4}[-－]\d{2,4}[-－]\d{3,4}',value):return '[非保存]'
 # 「村」などを含む姓を組織名と誤認しない。自治体の完全一致か部署の接尾辞。
 if value in MUNICIPAL_NAMES or value.split('/')[-1] in MUNICIPAL_NAMES:return value
 if re.search(r'(課|部|局|室|係|担当|センター|グループ|組合|協会|法人|大学|研究所|事務所|委員会|班|管理者|本部|役場|役所|県庁)$',value):return value
 return '[非保存]'

def scan(site,prior=None):
 counts={};seen=set();offset=0;total=None;pages=[];errors=[];prefix=0;whole_uuid_check=True;unavailable=[];count_changed=False
 if prior:
  pages=list(prior['pages']);offset=sum(p['count'] for p in pages);prefix=prior.get('datasets_counted') or prior.get('unique_datasets') or offset;offset=prior.get('next_offset',offset);total=prior['reported_datasets'];unavailable=list(prior.get('unavailable_offsets',[]))
  whole_uuid_check=False
  for old in prior['combinations']:
   r=dict(old);r['group_affiliations']=Counter(r['group_affiliations']);r.setdefault('evidence_metadata_urls',[])
   key=(public_org(r['author']),str(r['user_id']) if r['user_id'] is not None else '',public_org(r['user_name']))
   if key in counts:
    dest=counts[key]
    for k in ('datasets','external_datasets','same_host_datasets'):dest[k]+=r[k]
    dest['group_affiliations'].update(r['group_affiliations'])
   else:counts[key]=r
 normal_step=50 if 'shizuoka' in site else 100
 step=prior.get('last_page_size',normal_step) if prior else normal_step
 while total is None or offset<total:
  if offset:time.sleep(2)
  url=site+'/api/package_search?'+urlencode({'q':'','rows':step,'start':offset})
  try:
   for attempt in range(3):
    try:
     raw,final,_=get(url,timeout=45);break
    except (OSError,ValueError):
     if attempt==2:raise
     time.sleep(2)
   doc=json.loads(raw);data=doc.get('result',doc)
   if doc.get('success') is False:raise ValueError('API unsuccessful')
   rows=data['results'];new_total=int(data['count'])
   if total is not None and new_total!=total:count_changed=True
   total=new_total
   fresh=0
   for d in rows:
    uuid=d.get('uuid');nid=d.get('id')
    if not uuid or uuid in seen:continue
    seen.add(uuid);fresh+=1
    user=d.get('user') or {};author=str(d.get('author') or '');name=str(user.get('name') or '');uid=user.get('id')
    key=(public_org(author),str(uid) if uid is not None else '',public_org(name))
    if key not in counts:counts[key]={'author':public_org(author),'user_id':uid,'user_name':public_org(name),'datasets':0,'evidence_pages':[],'evidence_metadata_urls':[],'group_affiliations':Counter(),'external_datasets':0,'same_host_datasets':0}
    r=counts[key];r['datasets']+=1
    page=site+'/dataset/'+str(nid)+'.html'
    if len(r['evidence_pages'])<3:r['evidence_pages'].append(page)
    if url not in r['evidence_metadata_urls'] and len(r['evidence_metadata_urls'])<3:r['evidence_metadata_urls'].append(url)
    for group in d.get('groups') or []:
     g=public_org(group.get('name'))
     if g and g!='[非保存]':r['group_affiliations'][g]+=1
    hosts={urlparse(str(x.get('url') or '')).hostname for x in d.get('resources') or [] if x.get('url')}
    if urlparse(site).hostname in hosts:r['same_host_datasets']+=1
    if hosts-{None,urlparse(site).hostname}:r['external_datasets']+=1
   if not fresh and offset<total:raise ValueError('pagination repeated or empty before count')
   pages.append({'url':url,'count':len(rows),'sha256':hashlib.sha256(raw).hexdigest()})
   offset+=len(rows)
   if step<normal_step:step=min(normal_step,step*2)
   if offset%500==0:print(site,'metadata progress',offset,'/',total,flush=True)
  except Exception as e:
   if step>1:
    step=max(1,step//2);print(site,'retry smaller page',offset,step,type(e).__name__,flush=True);time.sleep(2);continue
   if total is not None and len(unavailable)<25:
    unavailable.append({'offset':offset,'url':url,'error':type(e).__name__+': '+str(e)[:150]});offset+=1
    print(site,'unavailable metadata index',offset-1,flush=True);continue
   errors.append(type(e).__name__+': '+str(e)[:150]);break
 out={'site':site,'reported_datasets':total,'datasets_counted':prefix+len(seen),'unique_datasets':len(seen) if whole_uuid_check else None,'whole_run_uuid_uniqueness_checked':whole_uuid_check,'resumed_after_records':prefix,'next_offset':offset,'last_page_size':step,'catalog_count_changed':count_changed,'unavailable_offsets':unavailable,'all_offsets_attempted':total is not None and offset>=total,'complete':total==prefix+len(seen) and not errors and not unavailable and not count_changed,'pages':pages,'errors':errors,'combinations':[]}
 for i,(key,r) in enumerate(sorted(counts.items(),key=lambda x:(x[1]['author'],str(x[1]['user_id']),x[1]['user_name'])),1):
  r['combination_id']=f'owner_{i:03}';r['group_affiliations']=dict(r['group_affiliations']);out['combinations'].append(r)
 print(site,prefix+len(seen),len(counts),'complete',out['complete'],flush=True)
 return out

def main():
 sites=[r['site'] for r in json.loads((ROOT/'research/catalogs/shirasagi_adapter_smoke_20261105.json').read_text())['results']]
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(scan,sites))
 doc={'created_utc':datetime.now(timezone.utc).isoformat(),'metadata_only':True,'data_files_fetched':False,'personal_names_and_contacts_saved':False,'results':results}
 (ROOT/'research/catalogs/shirasagi_owner_inventory_20261105.json').write_text(json.dumps(doc,ensure_ascii=False,indent=1)+'\n')
if __name__=='__main__':main()
