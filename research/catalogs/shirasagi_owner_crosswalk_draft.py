"""公開組織メタデータの確認用下書き。登録やallocationは変更しない。"""
import sys,json,re,csv,collections,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent));from shirasagi_owner_inventory import public_org,MUNICIPALITIES,ROOT
sys.path.insert(0,str(ROOT/'materials'));import shirasagi as S
from allocation import resolve_publisher_id
path=(ROOT/'research/catalogs/shirasagi_owner_inventory_20261105.json');doc=json.loads(path.read_text())
REG=json.load(open(ROOT/'independent_eval/allocation.json'));pools={r['publisher_id']:r['pool'] for r in REG['publishers']}
pref_by_site={'aomori':'青森県','shizuoka':'静岡県','tottori':'鳥取県','tokushima':'徳島県','kagawa':'香川県','ehime':'愛媛県'}
def pref_for(site):return next(v for k,v in pref_by_site.items() if k in site)
def mentions(value,pref):
 value=str(value or '').replace('\u3000',' ').strip()
 candidates=[r for r in MUNICIPALITIES if r['pref']==pref and value.startswith(r['city'] or r['pref'])]
 # 市川町/市川三郷町のような最長の名称を先に見る。
 if not candidates:return None
 return max(candidates,key=lambda r:len(r['city'] or r['pref']))
def map_row(r,pref):
 a=mentions(r['author'],pref);u=mentions(r['user_name'],pref)
 if not a and any(r['author'].startswith(x['city'] or x['pref']) for x in MUNICIPALITIES if x['pref']!=pref):
  return None,'基点の県外の自治体名がauthorにあり、提供元の追加確認が必要'
 if a:
  if u and a['code']!=u['code'] and u['city']:return None,'authorとuser.nameが異なる自治体'
  if not a['city'] and r['external_datasets']:return None,'県名のauthorに外部資料があり市町転載を否定できない'
  if not a['city'] and r['author'].strip()==pref and not u:
   # upstreamのauthor_nameはgroups名からも生成する。県名だけを所有者の証拠にしない。
   return None,'県名だけのauthorはgroupsからの既定表示の可能性があり、投稿者の所属も未確定'
  return a,'authorに自治体名の明記（HTMLの所属をClaudeが確認）'
 if u:
  return u,'user.nameに自治体名の明記、authorは部署等（投稿者と提供元の一致を要確認）'
 # 部署名と一致する階層付き所属。県名だけのgroupsは根拠にしない。
 for g in r['group_affiliations']:
  if not g.startswith(pref+'/'):continue
  tokens=g.split('/')[1:]
  # groupsに市町名がある場合は、author/userに名前がない以上勝手に所有者にしない。
  if any(t==x['city'] for t in tokens for x in MUNICIPALITIES if x['pref']==pref and x['city']):continue
  for v in (r['author'],r['user_name']):
   if v and v!='[非保存]' and len(v)>=3 and any(v in t for t in tokens):
    return next(x for x in MUNICIPALITIES if x['pref']==pref and not x['city']),'部署名と一致する県の階層付き所属（実際の部局所属を要確認）'
 return None,'author/userから自治体を特定できない（県名だけのgroups/areasで補完しない）'
official=json.loads((ROOT/'research/catalogs/shirasagi_official_organizations_20261105.json').read_text())['results']
org_indexes={x['pref']:x for x in official}
representatives=json.loads((ROOT/'research/catalogs/shirasagi_owner_evidence_20261105.json').read_text())['results']
representatives={(x['site'],x['municipality_code']):x for x in representatives}
rows=[];site_summary=[];fields=[]
for site in doc['results']:
 # 個人名等を非保存へ射影した同一組は統合する。件数は保存し、privateな文字列の区別を公刊しない。
 combined={}
 for old in site['combinations']:
  r=dict(old);r['author']=public_org(r['author']);r['user_name']=public_org(r['user_name']);key=(r['author'],str(r['user_id']),r['user_name'])
  if key not in combined:combined[key]=r;continue
  dst=combined[key]
  for k in ('datasets','external_datasets','same_host_datasets'):dst[k]+=r[k]
  g=collections.Counter(dst['group_affiliations']);g.update(r['group_affiliations']);dst['group_affiliations']=dict(g)
  for k in ('evidence_pages','evidence_metadata_urls'):dst[k]=list(dict.fromkeys(dst.get(k,[])+r.get(k,[])))[:3]
 site['combinations']=list(combined.values())
 for i,r in enumerate(site['combinations'],1):r['combination_id']=f'owner_{i:03}'
 pref=pref_for(site['site']);offset=0
 for r in site['combinations']:
  r['author']=public_org(r['author']);r['user_name']=public_org(r['user_name']);r['group_affiliations']={public_org(k):v for k,v in r['group_affiliations'].items() if public_org(k)!='[非保存]'}
  m,reason=map_row(r,pref);code=m['code'] if m else '';name=(m['city'] or m['pref']) if m else '不明'
  if code:
   assert S.valid_municipality(code)
   pid=resolve_publisher_id(code,REG.get('aliases',{}));pool=pools.get(pid,'未登録')
  else:pid='';pool='不明'
  excluded=pool in ('main','hold','eval','eval2','eval3') or code=='131041'
  row={'site':site['site'],'combination_id':r['combination_id'],'author':r['author'],'user_id':r['user_id'],'user_name':r['user_name'],'datasets':r['datasets'],'municipality':name,'municipality_code':code,'allocation_publisher_id':pid,'allocation_pool':pool,'excluded':excluded or not code,'review_status':'除外' if excluded or not code else 'Claude確認待ち','reason':reason,'external_datasets':r['external_datasets'],'same_host_datasets':r['same_host_datasets'],'evidence_url':r['evidence_pages'][0] if r['evidence_pages'] else '', 'affiliation_evidence':list(r['group_affiliations'])}
  org=org_indexes.get(pref,{})
  matches=[x for x in org.get('organization_links',[]) if x['name'] in (r['author'],r['user_name']) or (len(x['name'])>=3 and any(v and v!='[非保存]' and x['name'] in v for v in (r['author'],r['user_name'])))]
  row['municipality_representative_evidence']=representatives.get((site['site'],code))
  row['privacy_redacted_fields']=[k for k in ('author','user_name') if r[k]=='[非保存]']
  row['official_department_evidence']=matches[:5] if m and not m['city'] else []
  row['official_prefecture_organization_url']=org.get('url','') if m and not m['city'] else ''
  row['evidence_metadata_urls']=r.get('evidence_metadata_urls',[])
  rows.append(row)
 for missing in site.get('unavailable_offsets',[]):
  rows.append({'site':site['site'],'combination_id':'api_unavailable_'+str(missing['offset']),'author':'[取得不可]','user_id':None,'user_name':'','datasets':1,'municipality':'不明','municipality_code':'','allocation_publisher_id':'','allocation_pool':'不明','excluded':True,'review_status':'除外','reason':missing['error'],'external_datasets':None,'same_host_datasets':None,'evidence_url':missing['url'],'affiliation_evidence':[],'privacy_redacted_fields':[],'official_department_evidence':[],'official_prefecture_organization_url':'','municipality_representative_evidence':None,'evidence_metadata_urls':[missing['url']]})
 # 単一フィールドが別自治体/不明の組と衝突する場合は登録案にしない。
 site_rows=[x for x in rows if x['site']==site['site']]
 byfield=collections.defaultdict(list)
 for r in site_rows:
  for f,k in [('author','author'),('user.id','user_id'),('user.name','user_name')]:
   if r[k] not in (None,'','[非保存]'):byfield[(f,str(r[k]))].append(r)
 for (f,v),rs in byfield.items():
  if not site['complete']:continue
  codes={x['municipality_code'] for x in rs}
  if len(codes)==1 and '' not in codes and not any(x['excluded'] for x in rs):
   fields.append({'site':site['site'],'field':f,'value':v,'municipality_code':rs[0]['municipality_code'],'municipality':rs[0]['municipality'],'datasets':sum(x['datasets'] for x in rs),'evidence_url':rs[0]['evidence_url'],'combination_ids':[x['combination_id'] for x in rs],'evidence_urls':sorted({x['evidence_url'] for x in rs}),'official_department_evidence':[e for x in rs for e in x['official_department_evidence']],'status':'下書き・全件根拠確認前、実登録用ではない'})
 site_summary.append({'site':site['site'],'datasets':site.get('datasets_counted',site['unique_datasets'])+len(site.get('unavailable_offsets',[])),'retrieved_datasets':site.get('datasets_counted',site['unique_datasets']),'unavailable_datasets':len(site.get('unavailable_offsets',[])),'all_offsets_attempted':site.get('all_offsets_attempted',site['complete']),'whole_run_uuid_uniqueness_checked':site.get('whole_run_uuid_uniqueness_checked',True),'reported_datasets':site['reported_datasets'],'complete':site['complete'],'combinations':len(site_rows),'known_combinations':sum(bool(x['municipality_code']) for x in site_rows),'unknown_combinations':sum(not x['municipality_code'] for x in site_rows),'excluded_combinations':sum(x['excluded'] for x in site_rows),'municipalities':len({x['municipality_code'] for x in site_rows if x['municipality_code']})})
for site in doc['results']:
 assert sum(r['datasets'] for r in site['combinations'])==site.get('datasets_counted',site['unique_datasets']),site['site']
for field in fields:
 members=[r for r in rows if r['site']==field['site'] and r['combination_id'] in field['combination_ids']]
 assert members and {r['municipality_code'] for r in members}=={field['municipality_code']} and not any(r['excluded'] for r in members)
 assert field['field'] in ('author','user.id','user.name')
# 同じ自治体の同じ組を何度も確認しないための、重複を減らした確認順。
remaining={(r['site'],r['combination_id']) for r in rows if not r['excluded']}
queue=[]
while remaining:
 ranked=[(len({(f['site'],i) for i in f['combination_ids']} & remaining),f) for f in fields]
 if not ranked:break
 count,best=max(ranked,key=lambda pair:(pair[0],pair[1]['datasets'],pair[1]['field']=='author'))
 if not count:break
 queue.append(best);remaining-={(best['site'],i) for i in best['combination_ids']}
path.write_text(json.dumps(doc,ensure_ascii=False,indent=1)+'\n')
(ROOT/'research/catalogs/shirasagi_owner_crosswalk_draft_20261105.json').write_text(json.dumps({'metadata_only':True,'draft_only':True,'allocation_changed':False,'inventory_created_utc':doc['created_utc'],'sites':site_summary,'combinations':rows,'allocation_sha256':hashlib.sha256((ROOT/'independent_eval/allocation.json').read_bytes()).hexdigest(),'municipality_dictionary_sha256':hashlib.sha256((ROOT/'materials/dict/jp_municipalities.json').read_bytes()).hexdigest(),'nonconflicting_field_suggestions':fields,'reduced_review_queue':queue},ensure_ascii=False,indent=1)+'\n')
with open(ROOT/'research/catalogs/shirasagi_owner_crosswalk_draft_20261105.tsv','w') as f:
 keys=['site','combination_id','author','user_id','user_name','datasets','municipality','municipality_code','allocation_pool','review_status','external_datasets','reason','evidence_url']
 w=csv.DictWriter(f,fieldnames=keys,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
print(json.dumps(site_summary,ensure_ascii=False,indent=1));print('suggestions',len(fields),'total combos',len(rows))
