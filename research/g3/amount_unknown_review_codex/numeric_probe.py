"""現行precisionの再現と境界の数値点検。Pは実装せず、生の値は保存しない。"""
import json
import math
import re
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/g3'))
import g3_eval as G


def hits(s):
    return bool(re.search(r'[.,]\d*[1-9]\d*$',s) and len(re.split(r'[.,]',s)[-1].rstrip('0'))>=3)


def classify(value):
    s=G.RC._norm(value)
    if not hits(s):return 'not_precision_trigger'
    if re.fullmatch(r'\$\d{1,3}(,\d{3})+',s):return 'currency_grouped_integer'
    try:
        d=Decimal(s)
        gap=abs(d-d.quantize(Decimal('.01')))
        ulp=Decimal(str(math.ulp(float(d))))
        return 'compatible_with_cent_within_2ulp_and_1e-8' if gap<=min(2*ulp,Decimal('1e-8')) else 'longer_precision_remains'
    except Exception:return 'not_parsed'


def main():
    labels=sys.argv[1]
    top=[{'label':'amount','probability':.99}]
    cases=[('$12,345','unknown','amount_precision'),('$12,345.00','amount',None),
           ('$0.123','unknown','amount_precision'),('$12,345.678','unknown','amount_precision'),
           ('123.44999999999999','unknown','amount_precision'),('123.456789','unknown','amount_precision')]
    for value,label,reason in cases:
        assert G.RC.check_assert('amount',top,[value],'Value',siblings=['Amount'])==(label,reason)
    assert G.RC.check_assert('amount',top,['$12,345'],'ID',siblings=['Amount'])[1].startswith('cue_conflict:')
    assert classify('123.44999999999999').startswith('compatible_')
    assert classify('123.456789')=='longer_precision_remains'
    assert classify('100000000000000.125')=='longer_precision_remains'
    assert not re.fullmatch(r'\$\d{1,3}(,\d{3})+','$12,34')
    targets={'g3-0063','g3-0261','g3-0480','g3-0481','g3-0485','g3-0743'}
    out={}
    for c in G.load_g3(labels)['g3']:
        if c['id'] not in targets:continue
        out[c['id']]={'precision_input_values5':dict(Counter(classify(v) for v in c['values5'])),
                     'other_stage_values_full':dict(Counter(classify(v) for v in c['values']))}
    print(json.dumps({'synthetic_checks':11,'columns':out},ensure_ascii=False,indent=1))

if __name__=='__main__':main()
