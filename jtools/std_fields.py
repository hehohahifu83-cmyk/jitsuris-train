"""自治体標準項目の完全一致検索。曖昧な名称は候補を全部返す。"""
import json
from pathlib import Path
import unicodedata

DATA = json.loads(Path(__file__).with_name('std_fields_data.json').read_text(encoding='utf-8'))


def key(value):
    return unicodedata.normalize('NFKC', '' if value is None else str(value)).strip(' \t\r\n\u00a0\ufeff').lower()


INDEX = {}
for dataset, name, name_en, fmt in DATA['fields']:
    item = {'dataset': dataset, 'name': name, 'name_en': name_en, 'format': fmt}
    for alias in dict.fromkeys((key(name), key(name_en))):
        if alias:
            INDEX.setdefault(alias, []).append(item)


def lookup(header):
    return [dict(item) for item in INDEX.get(key(header), [])]
