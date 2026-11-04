"""公的な自治体一覧からカタログ候補を抽出し、CKANのメタデータAPIだけを調べる。"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
from datetime import datetime, timezone
from html.parser import HTMLParser
import io
import ipaddress
import json
from pathlib import Path
import time
from urllib.parse import urljoin, urlsplit, urlunsplit, urlencode
from urllib.error import HTTPError
from urllib.request import Request, urlopen

DIGITAL = 'https://www.digital.go.jp/resources/data_local_governments'
EGOV = 'https://data.e-gov.go.jp/data/api/3/action/package_show?id=digi_20220315_0064'
AGENT = 'jitsuris-jp-catalogs/1.0 (metadata only; +https://github.com/hehohahifu83-cmyk/jitsuris-train)'


def get_bytes(url):
    with urlopen(Request(url, headers={'User-Agent': AGENT}), timeout=12) as response:
        raw = response.read(12_000_001)
        if len(raw) > 12_000_000:
            raise ValueError('metadata response too large')
        return raw


def get_json(url):
    return json.loads(get_bytes(url).decode('utf-8-sig'))


class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.urls.extend(v for k, v in attrs if k == 'href' and v)


def csv_links(html, base=DIGITAL):
    parser = Links(); parser.feed(html)
    return sorted({urljoin(base, u) for u in parser.urls if urlsplit(u).path.lower().endswith('.csv')})


def decode_csv(raw):
    for encoding in ('utf-8-sig', 'cp932'):
        try:
            return raw.decode(encoding)
        except UnicodeError:
            pass
    raise ValueError('CSV encoding is neither UTF-8 nor CP932')


def canonical(url):
    p = urlsplit(url.strip())
    if p.scheme not in ('https', 'http') or not p.hostname or p.username or p.password:
        return None
    if p.port not in (None, 80, 443) or '.' not in p.hostname or p.hostname.endswith('.local'):
        return None
    try:
        ipaddress.ip_address(p.hostname)
        return None
    except ValueError:
        pass
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path.rstrip('/'), '', ''))


def catalog_rows(text, source):
    out = []
    for row in csv.DictReader(io.StringIO(text)):
        for key, value in row.items():
            if key and 'URL' in key.upper() and value:
                try:
                    url = canonical(value)
                except ValueError:
                    url = None
                if url:
                    out.append({'url': url, 'municipality_code': row.get('団体コード', ''),
                                'municipality': row.get('団体名', ''), 'source': source, 'field': key})
    return out


def bases(url):
    p = urlsplit(url)
    root = urlunsplit((p.scheme, p.netloc, '', '', ''))
    # 実際に一覧に記載されたサブパスも確認。ページの拡張子をAPIの基点にしない。
    parts = p.path.strip('/').split('/') if p.path.strip('/') else []
    found = [root]
    if parts and '.' not in parts[-1] and len(parts) <= 2:
        found.insert(0, root + '/' + '/'.join(parts))
    return found


def probe(base, fetch=get_json):
    result = {'base': base, 'reachable': False, 'ckan': False, 'organizations_complete': False,
              'n_organizations': None, 'n_datasets': None}
    start = time.monotonic()
    try:
        status = fetch(base + '/api/3/action/status_show')
        result['reachable'] = True
        if status.get('success') is not True or not isinstance(status.get('result'), dict):
            result['error'] = 'status_show did not identify a CKAN API'
            return result
        result['ckan'] = True
        orgs, seen = [], set()
        for page in range(20):
            data = fetch(base + '/api/3/action/organization_list?' + urlencode({'all_fields': 'true', 'limit': 1000, 'offset': page * 1000}))
            values = data.get('result')
            if data.get('success') is not True or not isinstance(values, list):
                raise ValueError('organization_list failed')
            if not values:
                result['organizations_complete'] = True
                break
            added = []
            for org in values:
                if not isinstance(org, dict) or not org.get('name'):
                    raise ValueError('organization_list did not return all_fields')
                name = org['name']
                if name not in seen:
                    seen.add(name); added.append({'name': name, 'package_count': org.get('package_count')})
            if not added:
                raise ValueError('organization_list repeated a page; offset may be ignored')
            orgs.extend(added)
        result['n_organizations'] = len(orgs)
        result['organizations'] = orgs
        counts = [o['package_count'] for o in orgs]
        # organization_list の件数は、可視組織が所有するデータセットの合計。無所属・非公開の数は含まない。
        if result['organizations_complete'] and all(isinstance(n, int) and n >= 0 for n in counts):
            result['n_datasets'] = sum(counts)
            result['dataset_count_scope'] = 'sum of visible organizations package_count; unowned/private datasets excluded'
        if not result['organizations_complete']:
            result['error'] = 'organization pagination limit reached'
    except Exception as exc:
        if isinstance(exc, (HTTPError, json.JSONDecodeError)):
            result['reachable'] = True
        if isinstance(exc, HTTPError):
            result['http_status'] = exc.code
        result['error'] = f'{type(exc).__name__}: {str(exc)[:160]}'
    finally:
        result['seconds'] = round(time.monotonic() - start, 3)
    return result


def discover():
    sources, rows, errors = [], [], []
    urls = []
    try:
        urls.extend(csv_links(get_bytes(DIGITAL).decode('utf-8')))
    except Exception as exc:
        errors.append({'source': DIGITAL, 'error': type(exc).__name__})
    try:
        data = get_json(EGOV)
        urls.extend(r['url'] for r in data['result']['resources'] if r.get('format', '').upper() == 'CSV')
    except Exception as exc:
        errors.append({'source': EGOV, 'error': type(exc).__name__})
    for url in sorted(set(urls)):
        try:
            raw = get_bytes(url)
            current = catalog_rows(decode_csv(raw), url)
            import hashlib
            sources.append({'url': url, 'sha256': hashlib.sha256(raw).hexdigest(), 'catalog_references': len(current)})
            rows.extend(current)
        except Exception as exc:
            errors.append({'source': url, 'error': type(exc).__name__})
    return sources, rows, errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--workers', type=int, default=12)
    ap.add_argument('--max-sites', type=int, default=3000)
    ap.add_argument('--shard', type=int, default=0)
    ap.add_argument('--shards', type=int, default=1)
    ap.add_argument('--merge', type=Path)
    args = ap.parse_args()
    if args.merge:
        docs = [json.loads(p.read_text(encoding='utf-8')) for p in sorted(args.merge.glob('jp_catalogs_*_part*.json'))]
        if not docs or len(docs) != docs[0]['shards'] or {d['shard'] for d in docs} != set(range(docs[0]['shards'])):
            ap.error('missing or duplicate shards')
        if any(d['sources'] != docs[0]['sources'] for d in docs):
            ap.error('source list changed between shards; do not merge')
        doc = docs[0].copy()
        doc['hosts'] = sorted([h for d in docs for h in d['hosts']], key=lambda h: h['base'])
        if len({h['base'] for h in doc['hosts']}) != len(doc['hosts']):
            ap.error('duplicate API bases between shards')
        doc['shards_complete'] = len(docs)
        doc['source_errors'] = [e for d in docs for e in d['source_errors']]
        doc.pop('shard', None)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(doc, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        print(f"merged={len(docs)} probed={len(doc['hosts'])} ckan={sum(h['ckan'] for h in doc['hosts'])}")
        return
    if not 1 <= args.workers <= 16 or not 1 <= args.max_sites <= 3000:
        ap.error('workers=1..16, max-sites=1..3000')
    if not 0 <= args.shard < args.shards <= 16:
        ap.error('require 0 <= shard < shards <= 16')
    sources, rows, errors = discover()
    candidates = sorted({b for r in rows for b in bases(r['url'])})
    selected = candidates[:args.max_sites][args.shard::args.shards]
    hosts = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        jobs = {executor.submit(probe, base): base for base in selected}
        for future in as_completed(jobs):
            hosts.append(future.result())
    doc = {'created_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'metadata_only': True,
           'shard': args.shard, 'shards': args.shards,
           'allowed_catalog_actions': ['status_show', 'organization_list'], 'sources': sources,
           'source_errors': errors, 'catalog_references': rows, 'candidate_count': len(candidates),
           'unprobed': candidates[args.max_sites:], 'hosts': sorted(hosts, key=lambda h: h['base'])}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(doc, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f"references={len(rows)} candidates={len(candidates)} probed={len(hosts)} ckan={sum(h['ckan'] for h in hosts)} source_errors={len(errors)}")
    if not rows:
        raise SystemExit('no catalog URLs discovered; see source_errors')


if __name__ == '__main__':
    main()
