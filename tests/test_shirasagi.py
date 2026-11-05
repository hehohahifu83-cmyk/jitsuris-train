import copy,json,re,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch,Mock
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'materials'))
import shirasagi as S
import pipeline as P
import fetch_rows as F
import pool_discover as D
U='12345678-1234-1234-1234-123456789abc'
CFG={'site':'https://catalog.test/data','publishers':[{'field':'user.id','value':'587','municipality_code':'020001','evidence_url':'https://catalog.test/about'}]}
REG={'aliases':{},'publishers':[{'publisher_id':'020001','pool':'train'},{'publisher_id':'221309','pool':'train'}]}
R={'id':7,'url':'https://catalog.test/a.csv','format':'CSV','license':{'uid':None,'name':'表示（CC BY）'}}
DATA={'uuid':U,'id':123,'name':'施設一覧','user':{'id':587},'resources':[R]}
class NativeTests(unittest.TestCase):
 def setUp(self):
  self.cfg=copy.deepcopy(CFG);self.data=copy.deepcopy(DATA)
 def run_discover(self,data=None,**kwargs):
  client=Mock();client.ids.return_value=[U];client.show.return_value=data or self.data
  with patch.object(S,'download_allowed',return_value=True):
   return S.discover(self.cfg,REG,set(),{},D.title_key,P.TITLE_DENY,client=client,**kwargs)
 def test_valid_codes(self):
  for code in ('020001','220001','221309','312011','384887','041009'):self.assertTrue(S.valid_municipality(code),code)
  for code in ('020000','02000',20001,None):self.assertFalse(S.valid_municipality(code))
 def test_train_alias(self):
  reg={'aliases':{'020001':'aomori'},'publishers':[{'publisher_id':'aomori','pool':'train'}]}
  self.assertEqual(S.allocated_train('020001',reg),'aomori')
 def test_non_train_and_unregistered(self):
  for pool in ('hold','eval','main'):
   with self.assertRaises(ValueError):S.allocated_train('020001',{'publishers':[{'publisher_id':'020001','pool':pool}]})
  with self.assertRaises(ValueError):S.allocated_train('020001',{'publishers':[]})
 def test_sendai_always_excluded(self):
  for reg in ({'publishers':[]},{'publishers':[{'publisher_id':'041009','pool':'train'}]}):
   with self.assertRaises(ValueError):S.allocated_train('041009',reg)
 def test_user_id_owner(self):self.assertEqual(S.publisher_for(self.data,R,self.cfg,REG),('020001','020001'))
 def test_groups_areas_do_not_establish_owner(self):
  self.data.pop('user');self.data.update(groups=[{'name':'青森県'}],areas=[{'name':'青森県'}])
  with self.assertRaises(ValueError):S.publisher_for(self.data,R,self.cfg,REG)
 def test_external_host_requires_city_crosswalk(self):
  r={**R,'url':'https://files.city.test/a.csv'}
  with self.assertRaises(ValueError):S.publisher_for(self.data,r,self.cfg,REG)
  self.cfg['publishers'].append({'field':'download_host','value':'files.city.test','municipality_code':'221309'})
  self.assertEqual(S.publisher_for(self.data,r,self.cfg,REG)[0],'221309')
 def test_conflicting_owner_rejected(self):
  self.cfg['publishers'].append({'field':'user.id','value':'587','municipality_code':'221309'})
  with self.assertRaises(ValueError):S.publisher_for(self.data,R,self.cfg,REG)
 def test_resource_license_only(self):
  self.assertEqual(S.resource_license(R),'cc-by')
  for lic in (None,{}, {'uid':'cc-by-nc','name':'CC BY'}, {'name':'CC BY-NC'}):
   with self.assertRaises(ValueError):S.resource_license({**R,'license':lic})
 def test_url_identity_numeric_vs_uuid(self):
  page,rid=S.identity(self.data,R,self.cfg)
  self.assertIn('/dataset/123.html?',page);self.assertIn(U,rid)
  with patch.object(S,'configurations',return_value=[self.cfg]):
   self.assertEqual(S.locate(page,rid),(self.cfg,U,'123','7'))
   self.assertEqual(P.platform_of({'platform':'shirasagi','resource_url':page,'resource_id':rid}),('shirasagi','catalog.test'))
   with self.assertRaises(ValueError):S.locate(page,'wrong')
   with self.assertRaises(ValueError):S.locate(page.replace('catalog.test','evil.test'),rid)
 def test_null_resource_id_stable(self):
  r={**R,'id':None};self.assertEqual(S.resource_token(r),S.resource_token(dict(r)))
  self.assertNotEqual(S.resource_token(r),S.resource_token({**r,'url':'https://catalog.test/b.csv'}))
 def test_missing_uuid_or_numeric_id(self):
  for d in ({**self.data,'uuid':'123'},{**self.data,'id':U}):
   with self.assertRaises(ValueError):S.identity(d,R,self.cfg)
 def test_download_exact_policy(self):
  with patch.object(P,'csv_domains',return_value={'catalog.test'}):
   self.assertTrue(S.download_allowed(R,self.cfg))
   self.assertFalse(S.download_allowed({**R,'url':'https://evil.test/a.csv'},self.cfg))
   self.assertFalse(S.download_allowed({**R,'url':'http://catalog.test/a.csv'},self.cfg))
 def test_config_explicit_crosswalk(self):
  with tempfile.TemporaryDirectory() as td,patch.object(P,'POOL',Path(td)):
   p=Path(td)/'allowed_hosts.json'
   self.assertEqual(S.configurations(),[])
   p.write_text(json.dumps({'shirasagi':[self.cfg]}));self.assertEqual(S.configurations(),[self.cfg])
   self.cfg['publishers'][0].pop('evidence_url');p.write_text(json.dumps({'shirasagi':[self.cfg]}))
   with self.assertRaises(ValueError):S.configurations()
 def test_discovery_resource_license_and_priority(self):
  self.data['resources']=[{**R,'id':8,'format':'xlsx','url':'https://catalog.test/a.xlsx'}, {**R,'id':9,'license':{'uid':'cc-by-nc'}},R]
  out,stats=self.run_discover();self.assertEqual(len(out),1);self.assertTrue(out[0]['resource_id'].endswith(':7'));self.assertEqual(stats['resource_rejected'],1)
 def test_dataset_used_skipped_before_metadata(self):
  client=Mock();client.ids.return_value=[U]
  out,stats=S.discover(self.cfg,REG,{f'shirasagi:catalog.test:{U}:old'},{},D.title_key,P.TITLE_DENY,client=client)
  self.assertEqual(out,[]);client.show.assert_not_called();self.assertEqual(stats['used_dataset'],1)
 def test_budget_stops_before_show(self):
  out,stats=self.run_discover(stop=lambda:True);self.assertEqual(out,[]);self.assertEqual(stats['stopped_by_budget'],1)
 def test_pool_cap(self):
  client=Mock();client.ids.return_value=[U];client.show.return_value=self.data
  with patch.object(S,'download_allowed',return_value=True):out,stats=S.discover(self.cfg,REG,set(),{'020001':15},D.title_key,P.TITLE_DENY,client=client)
  self.assertEqual(out,[]);self.assertEqual(stats['pool_full'],1)
 def test_client_list_and_uuid_verification(self):
  with patch.object(S.time,'sleep'):
   client=S.Client(self.cfg,lambda url:{'success':True,'result':[U,U,'bad']});self.assertEqual(client.ids(),[U])
   client=S.Client(self.cfg,lambda url:{'success':False})
   with self.assertRaises(ValueError):client.ids()
   client=S.Client(self.cfg,lambda url:self.data)
   self.assertEqual(client.show(U),self.data)
   with self.assertRaises(ValueError):client.show('00000000-0000-0000-0000-000000000000')
 def test_pagination_explicit_offset_and_cap(self):
  from urllib.parse import urlparse,parse_qs
  calls=[]
  def fetch(url):
   q=parse_qs(urlparse(url).query);calls.append(q)
   offset=int(q['offset'][0]);limit=int(q['limit'][0])
   return {'result':[f'{i:08x}-1234-1234-1234-123456789abc' for i in range(offset,offset+limit)]}
  with patch.object(S.time,'sleep'):
   ids=S.Client({**self.cfg,'max_datasets':150},fetch).ids()
  self.assertEqual(len(ids),150);self.assertEqual(calls,[{'limit':['100'],'offset':['0']},{'limit':['50'],'offset':['100']}])
 def test_list_budget_no_network(self):
  fetch=Mock();self.assertEqual(S.Client(self.cfg,fetch).ids(stop=lambda:True),[]);fetch.assert_not_called()
 def test_rate_limit_shared_by_clients(self):
  with patch.object(S.time,'monotonic',return_value=100),patch.object(S.time,'sleep') as sleep,patch.dict(S._LAST,{},clear=True):
   S.Client(self.cfg,lambda _:[]).ids();S.Client(self.cfg,lambda _:[]).ids();self.assertEqual(sleep.call_args.args,(2.0,))
 def fetch(self,mutate=None):
  page,rid=S.identity(self.data,R,self.cfg);item={'resource_url':page,'resource_id':rid,'publisher_id':'020001'}
  if mutate:mutate(self.data)
  with patch.object(S,'configurations',return_value=[self.cfg]),patch.object(S.Client,'show',return_value=self.data),patch.object(S,'allocation_registry',return_value=REG),patch.object(S,'download_allowed',return_value=True),patch.object(F,'http_bytes',return_value=('区分,件数\n施設,3\n'.encode(),False)) as download,patch.object(F,'ALLOWED_HOSTS',set()),patch.object(F,'REDIRECT_DOMAINS',set()):
   result=S.fetch_table(item,set());return result,download
 def test_fetch_roundtrip(self):
  (meta,fields,records,total),download=self.fetch();self.assertEqual(meta['platform'],'shirasagi');self.assertEqual(fields,['区分','件数']);self.assertEqual(total,1);download.assert_called_once()
 def test_adopt_then_fetch_routes_native(self):
  from collections import Counter
  candidates,_=self.run_discover()
  with patch.object(S,'configurations',return_value=[self.cfg]):
   adopted,reasons=P.adopt(candidates,{'020001':'train'},set(),set(),Counter(),Counter())
   self.assertEqual(len(adopted),1);self.assertEqual(reasons,Counter())
   sentinel=object()
   with patch.object(S,'fetch_table',return_value=sentinel) as native:
    self.assertIs(F.fetch_table(adopted[0],set()),sentinel);native.assert_called_once()
 def test_fetch_sheet_uses_existing_parser(self):
  self.data['resources'][0].update(format='XLSX',url='https://catalog.test/a.xlsx')
  page,rid=S.identity(self.data,self.data['resources'][0],self.cfg)
  item={'resource_url':page,'resource_id':rid,'publisher_id':'020001'}
  with patch.object(S,'configurations',return_value=[self.cfg]),patch.object(S.Client,'show',return_value=self.data),patch.object(S,'allocation_registry',return_value=REG),patch.object(S,'download_allowed',return_value=True),patch.object(F,'http_bytes',return_value=(b'xlsx',False)),patch.object(F,'parse_sheet',return_value=(['件数'],[{'件数':'3'}],1)) as parse,patch.object(F,'ALLOWED_HOSTS',set()),patch.object(F,'REDIRECT_DOMAINS',set()):
   result=S.fetch_table(item,set());self.assertEqual(result[0]['access'],'xlsx');parse.assert_called_once_with(b'xlsx','xlsx')
 def test_fetch_changed_owner_rejected(self):
  with self.assertRaises(ValueError):self.fetch(lambda d:d.update(user={'id':999}))
 def test_fetch_changed_license_rejected(self):
  with self.assertRaises(ValueError):self.fetch(lambda d:d['resources'][0].update(license={'uid':'cc-by-nc'}))
 def test_fetch_changed_numeric_id_rejected(self):
  with self.assertRaises(ValueError):self.fetch(lambda d:d.update(id=456))
class MetadataErrorTests(unittest.TestCase):
 def test_transport_causes(self):
  import errno,socket,ssl
  from urllib.error import URLError,HTTPError
  cases=[(URLError(socket.timeout('private')), 'timeout'),
         (TimeoutError('private'),'timeout'),
         (URLError(ConnectionRefusedError(errno.ECONNREFUSED,'private')),'connection_refused'),
         (URLError(ConnectionResetError(errno.ECONNRESET,'private')),'connection_reset'),
         (URLError(OSError(errno.ETIMEDOUT,'private')),'timeout'),
         (URLError(OSError(errno.EHOSTUNREACH,'private')),'unreachable'),
         (URLError(socket.gaierror(-2,'private')),'dns'),
         (URLError(ssl.SSLError('private')),'tls'),
         (HTTPError('https://private.test',429,'private',None,None),'http_429'),
         (HTTPError('https://private.test',503,'private',None,None),'http_5xx'),
         (HTTPError('https://private.test',403,'private',None,None),'http_other'),
         (URLError('Tunnel connection failed: 502 private'),'proxy_5xx'),
         (URLError('Tunnel connection failed: 429 private'),'proxy_429'),
         (URLError('private'),'url_other'),(ValueError('private'),'other')]
  for exc,want in cases:
   with self.subTest(want=want):self.assertEqual(S.metadata_error_cause(exc),want)
 def test_discover_keeps_totals_without_exception_text(self):
  import errno
  from urllib.error import URLError
  client=Mock();client.ids.return_value=[U];client.show.side_effect=URLError(ConnectionRefusedError(errno.ECONNREFUSED,'sensitive details'))
  out,stats=S.discover(CFG,REG,set(),{},D.title_key,P.TITLE_DENY,client=client)
  self.assertEqual(out,[])
  self.assertEqual(stats,{'metadata_error':1,'metadata_error:URLError':1,'metadata_cause:connection_refused':1,'tables':0,'publishers':0})
  self.assertNotIn('sensitive',json.dumps(stats))

if __name__=='__main__':unittest.main()
