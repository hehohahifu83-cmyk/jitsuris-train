"""Nの安全境界のレビュー用probe。製品や候補Nは変更しない。"""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(ROOT/'research/fix_n'))
import fix_n as N

def main():
    top=[{'label':'amount','probability':.99}]
    cases=['$12,345','12,345.00','12,345.678','1.234,567','1,2345','0.125',
           '123.44999999999999','147233988.24099997','663216.16324774758',
           '0.120000001','0.1200000010','0.0000000001',
           '123456789012345678901234567890.0000000001','US$12,345','R$12,345','CA$12,345']
    rows=[]
    for text in cases:
        norm=N.R._norm(text)
        old=N._orig('amount',top,[text],'Value',siblings=['Amount'])
        try:new=N.n_check_assert('amount',top,[text],'Value',siblings=['Amount']);err=None
        except Exception as e:new=None;err=type(e).__name__
        rows.append({'synthetic':text,'current':old,'N':new,'exception':err})
    by={r['synthetic']:r for r in rows}
    assert by['0.120000001']['N']!=by['0.1200000010']['N']
    assert by['0.0000000001']['N']==('amount',None)
    assert by['123456789012345678901234567890.0000000001']['exception']=='InvalidOperation'
    assert N.R.check_assert is N._orig
    with N.use():
        assert N.R.check_assert is N.n_check_assert
        for header in ('ID','2020'):
            assert N.R.check_assert('amount',top,['$12,345'],header,siblings=['Amount'])==N._orig('amount',top,['$12,345'],header,siblings=['Amount'])
        assert N.R.check_assert('amount',top,['$12,345','0.125'],'Value',siblings=['Amount'])[1]=='amount_precision'
    assert N.R.check_assert is N._orig
    print(json.dumps({'synthetic_cases':rows,'context_restored':True,'other_stops_and_mixed_precision_preserved':True},ensure_ascii=False,indent=1))

if __name__=='__main__':main()
