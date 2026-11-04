import json,sys,unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research/catalogs'))
import shirasagi_owner_inventory as I
class InventoryTests(unittest.TestCase):
 def test_person_surnames_with_place_characters_are_not_kept(self):
  for v in ('岡村 太郎','南部 花子','市川 次郎','町田 一郎','佐藤 太郎','香川県 岡村 太郎','web-admin'):
   self.assertEqual(I.public_org(v),'[非保存]')
 def test_contacts_are_not_kept(self):
  for v in ('担当課 x@example.com','情報政策課 03-1234-5678'):
   self.assertEqual(I.public_org(v),'[非保存]')
 def test_departments_and_municipalities_kept(self):
  for v in ('青森県','鳥取市','南部町','神山町役場','総務課','政策推進担当','香川県 政策部 統計調査課'):
   self.assertEqual(I.public_org(v),v)
 def test_counts_and_safe_projection(self):
  doc={'success':True,'result':{'count':2,'results':[{'uuid':'a','id':1,'author':'統計課','user':{'id':7,'name':'岡村 太郎','email':'secret@example.com'},'groups':[{'name':'青森県/統計課'}],'resources':[{'url':'https://catalog.test/a.csv'}]},{'uuid':'b','id':2,'author':'統計課','user':{'id':7,'name':'岡村 太郎'},'resources':[{'url':'https://external.test/b.csv'}]}]}}
  with patch.object(I,'get',return_value=(json.dumps(doc).encode(),'https://catalog.test','application/json')),patch.object(I.time,'sleep'):
   r=I.scan('https://catalog.test')
  self.assertTrue(r['complete']);self.assertEqual(r['unique_datasets'],2);self.assertEqual(len(r['combinations']),1)
  c=r['combinations'][0];self.assertEqual(c['datasets'],2);self.assertEqual(c['external_datasets'],1);self.assertEqual(c['same_host_datasets'],1)
  out=json.dumps(r,ensure_ascii=False);self.assertNotIn('太郎',out);self.assertNotIn('secret@example.com',out);self.assertNotIn('external.test',out)
 def test_resume_preserves_counts_and_marks_uuid_scope(self):
  prior={'pages':[{'url':'https://catalog.test/api/package_search?rows=100&start=0','count':1}], 'reported_datasets':2,'combinations':[{'author':'統計課','user_id':7,'user_name':'統計課','datasets':1,'evidence_pages':['https://catalog.test/dataset/1.html'],'group_affiliations':{'青森県/統計課':1},'external_datasets':0,'same_host_datasets':1}]}
  doc={'result':{'count':2,'results':[{'uuid':'b','id':2,'author':'統計課','user':{'id':7,'name':'統計課'}}]}}
  with patch.object(I,'get',return_value=(json.dumps(doc).encode(),'https://catalog.test','application/json')) as get,patch.object(I.time,'sleep'):
   r=I.scan('https://catalog.test',prior)
  self.assertIn('start=1',get.call_args.args[0]);self.assertTrue(r['complete']);self.assertEqual(r['datasets_counted'],2)
  self.assertFalse(r['whole_run_uuid_uniqueness_checked']);self.assertIsNone(r['unique_datasets']);self.assertEqual(r['combinations'][0]['datasets'],2)
 def test_unavailable_record_does_not_hide_later_metadata(self):
  prior={'pages':[{'url':'https://catalog.test/old','count':1}],'reported_datasets':3,'last_page_size':1,'combinations':[{'author':'統計課','user_id':7,'user_name':'統計課','datasets':1,'evidence_pages':[],'group_affiliations':{},'external_datasets':0,'same_host_datasets':0}]}
  def get(url,**kwargs):
   if 'start=1' in url:raise ValueError('one bad metadata record')
   return json.dumps({'result':{'count':3,'results':[{'uuid':'c','id':3,'author':'統計課','user':{'id':7,'name':'統計課'}}]}}).encode(),url,'application/json'
  with patch.object(I,'get',side_effect=get),patch.object(I.time,'sleep'):
   r=I.scan('https://catalog.test',prior)
  self.assertTrue(r['all_offsets_attempted']);self.assertFalse(r['complete']);self.assertEqual(r['datasets_counted'],2);self.assertEqual([x['offset'] for x in r['unavailable_offsets']],[1])
 def test_retry_and_failure_are_recorded(self):
  with patch.object(I,'get',side_effect=TimeoutError('metadata timeout')) as get,patch.object(I.time,'sleep'):
   r=I.scan('https://catalog.test')
  self.assertGreaterEqual(get.call_count,3);self.assertFalse(r['complete']);self.assertTrue(r['errors'])
 def test_duplicate_page_fails_instead_of_claiming_complete(self):
  doc={'result':{'count':3,'results':[{'uuid':'a','id':1,'author':'統計課'}]}}
  with patch.object(I,'get',return_value=(json.dumps(doc).encode(),'https://catalog.test','application/json')),patch.object(I.time,'sleep'):
   r=I.scan('https://catalog.test')
  self.assertFalse(r['complete']);self.assertIn('pagination repeated',r['unavailable_offsets'][0]['error']);self.assertEqual(r['unique_datasets'],1)
if __name__=='__main__':unittest.main()
