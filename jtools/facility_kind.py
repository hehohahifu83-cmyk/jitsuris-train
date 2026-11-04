"""B10の規則による補助候補。教材・既存ラベル・手動裁定に依存しない。"""
import json
from pathlib import Path
import re

DATA = json.loads(Path(__file__).with_name('facility_rules.json').read_text(encoding='utf-8'))
PAT = {k: re.compile(v[0], re.I if v[1] else 0) for k, v in DATA.items() if k not in ('KINDS', 'FIXED')}
KINDS = [(kind, re.compile(p)) for kind, p in DATA['KINDS']]
FIXED = [(re.compile(p), label, reason) for p, label, reason in DATA['FIXED']]


def is_name(header):
    h = str(header or '')
    return bool(PAT['HEAD'].search(h) and not PAT['NOT'].search(h))


def decide(header, values, context):
    h = str(header or '')
    def result(label, reason, rule):
        return {'label': label, 'reason': reason, 'rule': rule}
    if not is_name(h) or PAT['READING'].search(h):
        return result('unknown', '名称列以外・読みの列は元の名称列で確認', '')
    for pat, label, reason in FIXED:
        if pat.search(h): return result(label, reason, 'fixed')
    vals = [str(v) for v in (values or []) if v is not None and str(v).strip() and str(v).strip() not in ('nan', 'None', '-')]
    ctx = ' '.join(str(c) for c in (context or []))
    kinds = {kind for v in vals for kind, pat in KINDS if pat.search(v)}
    org = sum(bool(PAT['ORG_V'].search(v)) for v in vals)
    place = sum(bool(PAT['PLACE_V'].search(v)) for v in vals)
    inst = sum(bool(PAT['INST_V'].search(v)) and not PAT['PLACE_V'].search(v) for v in vals)
    n = max(len(vals), 1)
    if PAT['LIC'].search(ctx): return result('org', '営業許可・登録の台帳の店名（B10-2）', 'B10-2')
    if org * 5 >= 3 * n: return result('org', '値の多くが団体・会社の名前（B10-4）', 'B10-4')
    if PAT['USE_LOC'].search(ctx): return result('address', '避難所・投票所・設置場所など場所として使う一覧（B10-3）', 'B10-3')
    if len(kinds) >= 3 and not PAT['INST_C'].search(ctx): return result('address', f'いろいろな種類の施設が並ぶ一覧（{len(kinds)} 種類、B10-3）', 'B10-3')
    if place * 2 >= n: return result('address', '値の多くが場所そのものの名前（体育館・校庭・公園など、v1.7、B10-3）', 'B10-3')
    if inst * 5 >= 3 * n: return result('org', '同じ種類の機関の名簿（B10-1）', 'B10-1')
    if PAT['LOC_C'].search(ctx) and not PAT['INST_C'].search(ctx): return result('address', 'いろいろな施設の一覧で場所の属性が付く（B10-3）', 'B10-3')
    return result('unknown', '規則で決めきれない', '')
