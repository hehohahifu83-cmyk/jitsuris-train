import importlib.util
from pathlib import Path
import unittest
import json
import tempfile
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('jp_catalogs', Path(__file__).resolve().parents[1] / 'materials/pool/jp_catalogs.py')
J = importlib.util.module_from_spec(spec); spec.loader.exec_module(J)


class CatalogTests(unittest.TestCase):
    def test_sources_and_url_fields(self):
        self.assertEqual(J.csv_links('<a href="/x.csv">x</a><a href="/x.xlsx">x</a>'), ['https://www.digital.go.jp/x.csv'])
        rows = J.catalog_rows('団体コード,団体名,サイトのURL1,備考\n01,市,https://catalog.example/data/?x=1,https://ignore.example\n', 'source')
        self.assertEqual([r['url'] for r in rows], ['https://catalog.example/data'])
        self.assertEqual(J.decode_csv('団体名'.encode('cp932')), '団体名')

    def test_url_boundaries(self):
        for url in ['file:///tmp/x', 'http://127.0.0.1', 'http://a:b@catalog.example', 'http://catalog.example:8000']:
            self.assertIsNone(J.canonical(url))
        self.assertEqual(J.bases('https://catalog.example/data/'), ['https://catalog.example/data', 'https://catalog.example'])
        self.assertEqual(J.bases('https://catalog.example/index.html'), ['https://catalog.example'])

    def test_counts_only_metadata_endpoints(self):
        urls = []
        def fetch(url):
            urls.append(url)
            if 'status_show' in url: result = {'ckan_version': '2.10'}
            elif 'offset=0' in url: result = [{'name': 'city', 'package_count': 3}]
            else: result = []
            return {'success': True, 'result': result}
        out = J.probe('https://catalog.example', fetch)
        self.assertTrue(out['organizations_complete'])
        self.assertEqual((out['n_organizations'], out['n_datasets']), (1, 3))
        self.assertTrue(all('status_show' in u or 'organization_list' in u for u in urls))

    def test_missing_counts_and_repeating_pagination(self):
        def fetch(url):
            return {'success': True, 'result': {} if 'status_show' in url else [{'name': 'city'}]}
        out = J.probe('https://catalog.example', fetch)
        self.assertFalse(out['organizations_complete'])
        self.assertIsNone(out['n_datasets'])
        self.assertIn('repeated', out['error'])

    def test_merge_requires_complete_disjoint_shards(self):
        directory = Path(tempfile.mkdtemp())
        out = directory / 'result.json'
        for shard in range(2):
            (directory / f'jp_catalogs_20261104_part{shard}.json').write_text(json.dumps({
                'shard': shard, 'shards': 2, 'sources': [], 'source_errors': [],
                'hosts': [{'base': f'https://catalog{shard}.example', 'ckan': True}]}))
        with patch('sys.argv', ['jp_catalogs', '--merge', str(directory), '--out', str(out)]):
            J.main()
        self.assertEqual(len(json.loads(out.read_text())['hosts']), 2)
        (directory / 'jp_catalogs_20261104_part1.json').unlink()
        with patch('sys.argv', ['jp_catalogs', '--merge', str(directory), '--out', str(out)]):
            with self.assertRaises(SystemExit): J.main()


if __name__ == '__main__': unittest.main()
