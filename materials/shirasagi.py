"""Shirasagi独自APIのメタデータ・提供元・資料の識別。登録/割り当ては変更しない。"""
from __future__ import annotations
import errno,hashlib,json,re,socket,ssl,threading,time,sys
from urllib.error import HTTPError,URLError
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse,urlencode,parse_qs
from urllib.request import Request
from url_policy import allowed_open
import pipeline as P
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"independent_eval"))

UUID=re.compile(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',re.I)
_LAST={};_LOCK=threading.Lock()
# F1の自治体。現行allocationに未登録の場合もfail closed（オーナーの評価元を保護）。
EXCLUDED_MUNICIPALITIES={'041009'}
OWNER_FIELDS={'author','user.id','user.name'}

def configurations():
    path=P.POOL/'allowed_hosts.json'
    if not path.exists():return []
    with path.open(encoding='utf-8') as f:entries=json.load(f).get('shirasagi',[])
    if not isinstance(entries,list):raise ValueError('shirasagi must be a list')
    out=[]
    for cfg in entries:
        site=str(cfg.get('site','')).rstrip('/');u=urlparse(site)
        if not P.transport_allowed(site) or u.query or u.fragment or u.port not in (None,80,443):raise ValueError('invalid shirasagi site')
        if not isinstance(cfg.get('publishers',[]),list):raise ValueError('publishers must be an explicit crosswalk')
        for owner in cfg.get('publishers',[]):
            if owner.get('field') not in OWNER_FIELDS|{'download_host'} or not owner.get('value') or not owner.get('evidence_url'):
                raise ValueError('publisher crosswalk needs verified owner field/value/evidence_url')
            if not valid_municipality(owner.get('municipality_code','')):raise ValueError('invalid municipality code')
            if owner['field']=='download_host' and owner['value'].lower()==u.hostname:raise ValueError('catalog storage host is not a municipality identity')
        out.append({**cfg,'site':site})
    if len({c['site'] for c in out})!=len(out):raise ValueError('duplicate shirasagi sites')
    return out

def valid_municipality(code):
    if not isinstance(code,str) or not re.fullmatch(r'\d{6}',code):return False
    return int(code[-1])==((11-sum(int(a)*b for a,b in zip(code[:5],(6,5,4,3,2)))%11)%10)

def allocation_registry():
    with (P.ROOT/'independent_eval/allocation.json').open(encoding='utf-8') as f:return json.load(f)

def allocated_train(code,registry):
    if not valid_municipality(code) or code in EXCLUDED_MUNICIPALITIES:raise ValueError('municipality is excluded or invalid')
    from allocation import resolve_publisher_id
    pid=resolve_publisher_id(code,registry.get('aliases',{}))
    pools={x['publisher_id']:x['pool'] for x in registry['publishers']}
    if pools.get(pid)!='train':raise ValueError('municipality is not registered train')
    return pid

def owner_value(dataset,field):
    value=dataset
    for part in field.split('.'):
        if not isinstance(value,dict):return None
        value=value.get(part)
    return str(value) if isinstance(value,(str,int)) else None

def publisher_for(dataset,resource,cfg,registry):
    host=(urlparse(str(resource.get('url',''))).hostname or '').lower();catalog=urlparse(cfg['site']).hostname
    if host!=catalog:
        # 県の一括転載でも、外部市町ファイルの提供者を県のgroupsに取り違えない。
        matches=[o['municipality_code'] for o in cfg.get('publishers',[]) if o['field']=='download_host' and o['value'].lower()==host]
    else:
        matches=[o['municipality_code'] for o in cfg.get('publishers',[]) if o['field'] in OWNER_FIELDS and owner_value(dataset,o['field'])==str(o['value'])]
    if len(set(matches))!=1:raise ValueError('publisher unknown or conflicting; areas/groups are not ownership evidence')
    code=matches[0];return allocated_train(code,registry),code

def resource_license(resource):
    lic=resource.get('license')
    if not isinstance(lic,dict):raise ValueError('resource license missing')
    normalized=P.license_from_pkg({'license_id':lic.get('uid'),'license_title':lic.get('name')})
    if normalized not in P.ALLOWED_LICENSES:raise ValueError('resource license not allowed')
    return normalized

def resource_kind(resource):
    url=str(resource.get('url') or '');u=urlparse(url);fmt=str(resource.get('format') or '').strip().lower();ext=u.path.lower().rsplit('.',1)[-1]
    if fmt in ('csv','text/csv') or ext=='csv':return 'csv'
    if fmt in ('xlsx','ms-excel xlsx','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') or ext=='xlsx':return 'xlsx'
    if fmt in ('xls','ms-excel','application/vnd.ms-excel') or ext=='xls':return 'xls'
    raise ValueError('unsupported resource format')

def download_allowed(resource,cfg):
    url=str(resource.get('url') or '')
    return P.transport_allowed(url) and P.host_in(urlparse(url).hostname,P.csv_domains(urlparse(cfg['site']).hostname))

def resource_token(resource):
    rid=resource.get('id')
    if rid is not None and str(rid):return str(rid)
    return 'url-'+hashlib.sha256(str(resource.get('url') or '').encode()).hexdigest()

def identity(dataset,resource,cfg):
    uuid=str(dataset.get('uuid') or '').lower();nid=str(dataset.get('id') or '')
    if not UUID.fullmatch(uuid) or not nid.isdigit():raise ValueError('dataset uuid/numeric id missing')
    token=resource_token(resource)
    rid=f'shirasagi:{urlparse(cfg["site"]).hostname}:{uuid}:{token}'
    page=cfg['site']+'/dataset/'+nid+'.html?'+urlencode({'uuid':uuid,'resource':token})
    return page,rid

def locate(page,rid=None):
    u=urlparse(page);q=parse_qs(u.query)
    if set(q)!={'uuid','resource'} or any(len(v)!=1 for v in q.values()) or not UUID.fullmatch(q['uuid'][0]):raise ValueError('invalid shirasagi resource URL')
    for cfg in configurations():
        base=urlparse(cfg['site']);m=re.fullmatch(re.escape(base.path)+r'/dataset/(\d+)\.html',u.path)
        if (u.scheme,u.netloc)==(base.scheme,base.netloc) and m and not u.fragment:
            expected=f'shirasagi:{u.hostname}:{q["uuid"][0].lower()}:{q["resource"][0]}'
            if rid is not None and rid!=expected:raise ValueError('resource identifier mismatch')
            return cfg,q['uuid'][0].lower(),m.group(1),q['resource'][0]
    raise ValueError('shirasagi catalog is not registered')

def metadata_error_cause(exc):
    """失敗原因を固定語だけで記録する。例外本文や応答本文は保存しない。"""
    if isinstance(exc,HTTPError):
        return 'http_429' if exc.code==429 else 'http_5xx' if 500<=exc.code<600 else 'http_other'
    reason=exc.reason if isinstance(exc,URLError) else exc
    if isinstance(reason,(TimeoutError,socket.timeout)):return 'timeout'
    if isinstance(reason,ssl.SSLError):return 'tls'
    if isinstance(reason,socket.gaierror):return 'dns'
    if isinstance(reason,OSError):
        if reason.errno==errno.ETIMEDOUT:return 'timeout'
        if reason.errno==errno.ECONNREFUSED:return 'connection_refused'
        if reason.errno==errno.ECONNRESET:return 'connection_reset'
        if reason.errno in (errno.ENETUNREACH,errno.EHOSTUNREACH):return 'unreachable'
    # urllib のプロキシCONNECTエラーは reason が文字列になる。
    # 決まったエラー種別だけを抽出し、ホスト・資格情報などを転記しない。
    if isinstance(reason,str):
        if re.search(r'tunnel connection failed:\s*429\b',reason,re.I):return 'proxy_429'
        if re.search(r'tunnel connection failed:\s*5\d\d\b',reason,re.I):return 'proxy_5xx'
    return 'url_other' if isinstance(exc,URLError) else 'other'

class Client:
    def __init__(self,cfg,fetch_json=None):self.cfg=cfg;self.site=cfg['site'];self.fetch_json=fetch_json
    def request(self,action,params):
        if action not in ('package_list','package_show'):raise ValueError('metadata action not allowed')
        url=self.site+'/api/'+action+'?'+urlencode(params);host=urlparse(url).hostname
        # インスタンスをまたいでも同一ホストで2秒以上空ける。並列取得しない。
        with _LOCK:
            time.sleep(max(0,2.0- (time.monotonic()-_LAST.get(host,0))))
            try:
                if self.fetch_json is not None:doc=self.fetch_json(url)
                else:
                    check=lambda v:P.transport_allowed(v) and urlparse(v).hostname==host
                    with allowed_open(Request(url,headers={'User-Agent':'jitsuris-train/1.0 (metadata only; +https://github.com/hehohahifu83-cmyk/jitsuris-train)'}),timeout=30,check=check) as r:
                        if r.status!=200:raise ValueError(f'metadata HTTP {r.status}')
                        raw=r.read(10_000_001)
                        if len(raw)>10_000_000:raise ValueError('metadata too large')
                        doc=json.loads(raw.decode('utf-8-sig'))
                if isinstance(doc,dict) and doc.get('success') is False:raise ValueError('metadata API unsuccessful')
                return doc.get('result',doc) if isinstance(doc,dict) else doc
            finally:_LAST[host]=time.monotonic()
    def ids(self,stop=lambda:False):
        cap=int(self.cfg.get('max_datasets',1000))
        if not 1<=cap<=5000:raise ValueError('max_datasets must be 1..5000')
        out=[];seen=set()
        for offset in range(0,cap,100):
            if stop():break
            limit=min(100,cap-offset)
            # 青森・香川・愛媛はoffsetの省略がValidation Error。全サイトで明示する。
            data=self.request('package_list',{'limit':limit,'offset':offset})
            if isinstance(data,dict):data=data.get('results',data.get('items',data.get('packages')))
            if not isinstance(data,list):raise ValueError('package_list is not a dataset list')
            fresh=0
            for x in data:
                val=x.get('uuid') if isinstance(x,dict) else x
                if isinstance(val,str) and UUID.fullmatch(val) and val.lower() not in seen:
                    seen.add(val.lower());out.append(val.lower());fresh+=1
            # offsetを無視する実装で同じページを繰り返さない。
            if len(data)<limit or not fresh:break
        return out[:cap]
    def show(self,uuid):
        data=self.request('package_show',{'id':uuid})
        if not isinstance(data,dict) or str(data.get('uuid','')).lower()!=uuid.lower():raise ValueError('dataset uuid changed or metadata invalid')
        return data

def discover(cfg,registry,known_rids,pool_pub,title_key,title_deny,stop=lambda:False,limit_publishers=None,query=None,client=None):
    stats=Counter();out=[];seen_titles=set();counts=Counter();client=client or Client(cfg)
    cap=int(cfg.get('max_datasets',1000))
    if not 1<=cap<=5000:raise ValueError('max_datasets must be 1..5000')
    for uuid in client.ids(stop=stop)[:cap]:
        if any(rid.startswith(f'shirasagi:{urlparse(cfg["site"]).hostname}:{uuid}:') for rid in known_rids):
            stats['used_dataset']+=1;continue
        if stop():stats['stopped_by_budget']+=1;break
        try:dataset=client.show(uuid)
        except Exception as exc:
            stats['metadata_error']+=1
            stats['metadata_error:'+type(exc).__name__]+=1
            stats['metadata_cause:'+metadata_error_cause(exc)]+=1
            continue
        title=str(dataset.get('name') or '')
        if not title or title_deny.search(title):stats['title_denied']+=1;continue
        if query and query.lower() not in (title+' '+str(dataset.get('text',''))).lower():continue
        resources=dataset.get('resources') or []
        resources=sorted(resources,key=lambda r: {'csv':0,'xlsx':1,'xls':2}.get(str(r.get('format','')).lower(),3))
        for resource in resources:
            try:
                kind=resource_kind(resource);lic=resource_license(resource)
                if not download_allowed(resource,cfg):raise ValueError('download not allowed')
                pid,code=publisher_for(dataset,resource,cfg,registry);page,rid=identity(dataset,resource,cfg)
            except (ValueError,TypeError):stats['resource_rejected']+=1;continue
            if rid in known_rids:stats['used']+=1;continue
            if pool_pub.get(pid,0)+counts[pid]>=P.PER_PUBLISHER_POOL:stats['pool_full']+=1;break
            if limit_publishers and pid not in counts and len(counts)>=limit_publishers:break
            key=(pid,title_key(title))
            if key in seen_titles:stats['same_title']+=1;break
            out.append({'publisher_id':pid,'pool':'train','platform':'shirasagi','resource_url':page,'resource_id':rid,'title':title,'resource_name':str(resource.get('name') or ''),'license':{'id':lic},'access':'csv','datastore_available':False,'safe_headers':[]})
            seen_titles.add(key);counts[pid]+=1;stats[kind]+=1;break
    stats['tables']=len(out);stats['publishers']=len(counts);return out,stats

def fetch_table(item,known):
    import fetch_rows as F
    cfg,uuid,nid,token=locate(item['resource_url'],item.get('resource_id'));dataset=Client(cfg).show(uuid)
    if str(dataset.get('id'))!=nid:raise ValueError('numeric dataset id changed')
    resources=[r for r in dataset.get('resources',[]) if resource_token(r)==token]
    if len(resources)!=1:raise ValueError('resource missing or ambiguous')
    r=resources[0];pid,code=publisher_for(dataset,r,cfg,allocation_registry())
    if item.get('publisher_id')!=pid:raise ValueError('publisher changed')
    lic=resource_license(r);kind=resource_kind(r);url=str(r.get('url') or '')
    if not download_allowed(r,cfg):raise ValueError('download no longer allowed')
    if url in known or item['resource_url'] in known:raise ValueError('URL overlaps the training corpus or the main set')
    F.ALLOWED_HOSTS.add(urlparse(url).hostname);F.REDIRECT_DOMAINS.clear();F.REDIRECT_DOMAINS.update(P.csv_domains(urlparse(cfg['site']).hostname))
    raw,truncated=F.http_bytes(url,kind,limit=F.CSV_MAX_BYTES if kind=='csv' else F.SHEET_MAX_BYTES)
    if kind=='csv':fields,records,total=F.parse_csv(raw,truncated,encodings=F.CP932_FIRST)
    else:
        if truncated:raise ValueError('spreadsheet exceeds byte limit')
        fields,records,total=F.parse_sheet(raw,kind)
    from datetime import datetime,timezone
    meta={'platform':'shirasagi','resource_id':item['resource_id'],'publisher_id':pid,'resource_url':item['resource_url'],'download_url':url,'license':lic,'fetched_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_prefix':'jp-shirasagi','language':'ja','access':kind}
    return meta,fields,records,total
