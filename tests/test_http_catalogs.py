"""設定した完全一致HTTPホストだけを候補・API・ファイル・転送で許す。"""
import json,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch,MagicMock
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'materials'))
import pipeline as P
import pool_discover as D
import fetch_rows as F
from urllib.request import Request

class HttpCatalogTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.pool=Path(self.tmp.name)
        (self.pool/'allowed_hosts.json').write_text(json.dumps({'http_hosts':['catalog.test'],'ckan':['catalog.test'],'csv_domains':{'catalog.test':['gov.test']}}))
        self.patch=patch.object(P,'POOL',self.pool);self.patch.start();self.addCleanup(self.patch.stop)
    def test_exact_host_only_no_subdomains_or_credentials_or_port(self):
        self.assertTrue(P.transport_allowed('http://catalog.test/a'))
        self.assertTrue(P.transport_allowed('http://CATALOG.test:80/a'))
        for u in ['http://sub.catalog.test/a','http://catalog.test.evil/a','http://gov.test/a','http://catalog.test:8080/a','http://u:p@catalog.test/a','ftp://catalog.test/a']:
            self.assertFalse(P.transport_allowed(u),u)
        self.assertTrue(P.transport_allowed('https://other.test/a'))
    def test_empty_or_missing_configuration_defaults_to_https(self):
        (self.pool/'allowed_hosts.json').write_text('{}')
        self.assertFalse(P.transport_allowed('http://catalog.test/a'))
        (self.pool/'allowed_hosts.json').unlink()
        self.assertFalse(P.transport_allowed('http://catalog.test/a'))
    def test_csv_and_xlsx_candidates_require_both_policies(self):
        site='http://catalog.test'
        for fmt,suffix,check in [('CSV','csv',D.csv_on_host),('xlsx','xlsx',D.sheet_on_host)]:
            self.assertTrue(check({'format':fmt,'url':site+'/a.'+suffix},site))
            self.assertFalse(check({'format':fmt,'url':'http://gov.test/a.'+suffix},site))
            self.assertFalse(check({'format':fmt,'url':'http://unknown.test/a.'+suffix},site))
    def test_redirect_checks_http_before_following(self):
        h=F.AllowedRedirect(P.transport_allowed)
        self.assertIsNotNone(h.redirect_request(Request('https://catalog.test/a'),None,302,'Found',{},'http://catalog.test/b'))
        for u in ['http://other.test/a','http://sub.catalog.test/a']:
            with self.assertRaisesRegex(ValueError,'outside'):h.redirect_request(Request('https://catalog.test/a'),None,302,'Found',{},u)
    def test_api_requires_host_and_transport_and_checks_final_url(self):
        r=MagicMock();r.__enter__.return_value=r;r.status=200;r.read.return_value=b'{"result":{}}';r.geturl.return_value='http://catalog.test/api'
        with patch.object(F,'ALLOWED_HOSTS',{'catalog.test'}),patch.object(F,'allowed_open',return_value=r),patch('time.sleep'):
            self.assertEqual(F.http_json('http://catalog.test/api'),{'result':{}})
            r.geturl.return_value='http://other.test/api'
            with self.assertRaises(ValueError):F.http_json('http://catalog.test/api')
        with patch.object(F,'ALLOWED_HOSTS',set()):
            with self.assertRaises(ValueError):F.http_json('http://catalog.test/api')
    def test_discovery_accepts_http_national_site(self):
        r=MagicMock();r.__enter__.return_value=r;r.read.return_value=b'{"result":[]}';r.geturl.return_value='http://catalog.test/api'
        with patch.object(D,'HOSTS',{'catalog.test'}),patch.object(D,'allowed_open',return_value=r),patch('time.sleep'):
            self.assertEqual(D.get_json('http://catalog.test/api'),{'result':[]})
            r.geturl.return_value='http://other.test/api'
            with self.assertRaises(ValueError):D.get_json('http://catalog.test/api')
    def test_download_does_not_upgrade_explicit_http(self):
        rid='00000000-0000-0000-0000-000000000001';url='http://catalog.test/dataset/x/resource/'+rid
        resource={'id':rid,'package_id':'x','url':'http://catalog.test/a.csv','format':'CSV','datastore_active':False}
        pkg={'license_id':'cc-by-4.0'}
        with patch.object(F,'http_json',side_effect=[{'result':resource},{'result':pkg}]),patch.object(F,'http_bytes',return_value=(b'Year,Count\n2020,1\n2021,2\n',False)) as get:
            meta,fields,recs,total=F.fetch_table({'platform':'ckan','publisher_id':'test','resource_url':url},set())
            self.assertEqual(get.call_args.args[0],'http://catalog.test/a.csv')
            self.assertEqual(meta['access'],'csv');self.assertEqual(fields,['Year','Count'])
    def test_binary_download_rejects_http_other_host(self):
        with patch.object(F,'ALLOWED_HOSTS',{'catalog.test','other.test'}),patch.object(F,'REDIRECT_DOMAINS',{'test'}):
            self.assertTrue(F._redirect_ok('http://catalog.test/a'))
            self.assertFalse(F._redirect_ok('http://other.test/a'))
            with self.assertRaises(ValueError):F.http_bytes('http://other.test/a')

if __name__=='__main__':unittest.main()
