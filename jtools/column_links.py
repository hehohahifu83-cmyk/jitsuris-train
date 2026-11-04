"""列名と値の形から、同一表内の関連候補を返す。列番号は0始まり。"""
import re
from jtools import read_value as RV
from jtools import facility_kind as FK

READING = re.compile(r'(カナ|かな|ｶﾅ|フリガナ|ふりがな|よみ|読み|英字|英語|ローマ字|通称|_en$|_kana$|_english$|Kana$|English$|En$)', re.I)
UNIT = re.compile(r'^(単位|単位名|unit|units|uom|einheit|unit[_ ]of[_ ]measure|unit_meas|measurement[_ ]unit)$', re.I)
ID = re.compile(r'(^id$|(^|[_ ])(id|code)($|[_ ])|コード|番号|識別子|code$|identifier$)', re.I)
OPERATOR = re.compile(r'^(運営|管理|設置)(者|主体|団体|法人|機関|組織)(名|名称)?$|^(operator|owner|managed_by|operated_by)$', re.I)


def norm(header):
    return str(header or '').replace('\n', ' ').strip(' \t\r\n\u00a0\ufeff')


def base_header(header):
    h = norm(header)
    b = re.sub(r'[_＿（(]?(カナ|かな|ｶﾅ|フリガナ|ふりがな|よみ|読み|英字|英語|ローマ字|通称)[）)]?.*$', '', h)
    if b == h:
        b = re.sub(r'_(en|kana|english)$', '', h, flags=re.I)
        if b == h:
            b = re.sub(r'(Kana|English|En)$', '', h)
    b = re.sub(r'[\s_＿]+$', '', b)
    return b or h


def find_links(columns):
    headers = [norm(c.get('header')) for c in columns]
    units = [i for i, h in enumerate(headers) if UNIT.fullmatch(h)]
    names = [i for i, h in enumerate(headers) if FK.is_name(h) and not READING.search(h)]
    numeric = []
    for i, c in enumerate(columns):
        summary = RV.column_summary(c.get('rows') or c.get('values') or [])
        if summary['n'] and summary['number'] * 5 >= summary['n'] * 4 and i not in units and not ID.search(headers[i]):
            numeric.append(i)
    out = []
    for i, h in enumerate(headers):
        base = base_header(h)
        targets = [j for j, v in enumerate(headers) if j != i and v.lower() == base.lower()]
        if READING.search(h) and base != h:
            for j in targets:
                out.append({'kind': 'reading', 'source': i, 'target': j, 'ambiguous': len(targets) > 1})
    for i in units:
        for j in numeric:
            out.append({'kind': 'unit', 'source': i, 'target': j, 'ambiguous': len(units) > 1})
    for i, h in enumerate(headers):
        if OPERATOR.fullmatch(h):
            for j in names:
                if i != j:
                    out.append({'kind': 'operator', 'source': i, 'target': j, 'ambiguous': len(names) > 1})
    return out
