"""取り出し回復：誤った見出し・ZIPの境界・転送の安全性。"""
import io
import sys
import unittest
import zipfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'materials'))
import fetch_rows as F

class RecoveryTests(unittest.TestCase):
    def archive(self, files):
        b=io.BytesIO()
        with zipfile.ZipFile(b,'w',compression=zipfile.ZIP_DEFLATED) as z:
            for name,data in files.items():z.writestr(name,data)
        return b.getvalue()
    def test_one_csv_zip_with_readme(self):
        f,r,n=F.parse_csv(self.archive({'folder/a.CSV':b'Year,Count\n2020,5\n2021,7\n','README.txt':b'public data'}))
        self.assertEqual((f,n),(['Year','Count'],2))
        self.assertEqual(r[1]['Count'],'7')
    def test_ambiguous_or_missing_csv(self):
        for files in ({'a.csv':b'a,b','b.csv':b'a,b'},{'a.txt':b'a,b'}):
            with self.assertRaisesRegex(ValueError,'exactly one'):F.parse_csv(self.archive(files))
    def test_zip_expanded_limit_and_partial(self):
        raw=self.archive({'a.csv':b'a,b\n'+b'1,2\n'*800000})
        with self.assertRaisesRegex(ValueError,'too large'):F.parse_csv(raw)
        with self.assertRaisesRegex(ValueError,'byte limit'):F.parse_csv(self.archive({'a.csv':b'a,b\n1,2'}),truncated=True)
    def test_broken_zip(self):
        with self.assertRaisesRegex(ValueError,'unreadable'):F.parse_csv(b'PK\x03\x04not a zip')
    def test_header_after_ten_lines_and_padded_preamble(self):
        raw=('Note: preliminary,,,\n'*14+'Title,,,,,source\nArea,Count,Year\nEast,10,2020\nWest,20,2021\nSouth,30,2022\nNorth,40,2023\nCentral,50,2024\n').encode()
        f,r,n=F.parse_csv(raw)
        self.assertEqual(f,['Area','Count','Year']);self.assertEqual(n,5)
    def test_note_with_multiple_cells_is_not_header(self):
        raw=b'Source: Agency,2024\nYear,Count\n2020,1\n2021,2\n2022,3\n2023,4\n2024,5\n'
        self.assertEqual(F.parse_csv(raw)[0],['Year','Count'])
    def test_mac_line_endings(self):
        self.assertEqual(F.parse_csv(b'Year,Count\r2020,5\r2021,7\r')[2],2)
    def test_sparse_real_header_keeps_column_alignment(self):
        f,r,n=F.parse_csv(b'Year,,Count\n2020,,5\n2021,,7\n')
        self.assertEqual(f,['Year','Count']);self.assertEqual(r[1],{'Year':'2021','Count':'7'})
    def test_http_redirect_disallowed_even_for_initial_host(self):
        old=set(F.ALLOWED_HOSTS)
        try:
            F.ALLOWED_HOSTS.add('data.gov.au')
            self.assertFalse(F._redirect_ok('http://data.gov.au/a.csv'))
            self.assertFalse(F._redirect_ok('https://data.gov.au.evil.test/a.csv'))
        finally:F.ALLOWED_HOSTS.clear();F.ALLOWED_HOSTS.update(old)
if __name__=='__main__':unittest.main()

class NetworkRecoveryTests(unittest.TestCase):
    def test_redirect_is_rejected_before_following(self):
        handler=F.AllowedRedirect(lambda u:False)
        with self.assertRaisesRegex(ValueError,'outside the allowed hosts: unapproved.test'):
            handler.redirect_request(F.Request('https://data.gov.au/a'),None,302,'Found',{},'https://unapproved.test/a')
    def test_http403_is_not_retried_but_429_is(self):
        from unittest.mock import patch
        from urllib.error import HTTPError
        url='https://data.bodik.jp/a'
        for status,tries in ((403,1),(429,3)):
            with patch.object(F,'allowed_open',side_effect=HTTPError(url,status,'Denied',{},None)) as op, patch('time.sleep'):
                with self.assertRaisesRegex(RuntimeError,str(status)):F.http_bytes(url,'csv')
                self.assertEqual(op.call_count,tries)
