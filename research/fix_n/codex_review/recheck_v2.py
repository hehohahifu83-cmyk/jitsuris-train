"""N修正版の境界確認。製品・候補本体は変更しない。"""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT),str(ROOT/'research/fix_n')]
import fix_n as N

def main():
    assert hashlib.sha256((ROOT/'research/fix_n/fix_n.py').read_bytes()).hexdigest()=='d6a73e871fa1931aec7e199b0e1a455755e1bd6e3cb8acbfcb8fff42408c3be2'
    top=[{'label':'amount','probability':.99}]
    cases={'0.120000001':True,'0.1200000010':True,'0.0000000001':True,
           '0.12000000000000001':False,'123456789012345678901234567890.0000000001':True,
           '0.125':True,'147233988.24099997':True,'663216.16324774758':True,
           '1.234,567':True,'1,2345':True,'1,234.567':True,'$0.123':True,
           '$12,345':False,'3,205,468':False,'159417.82999999999':False,'41636.120000000003':False}
    result=[]
    for value,expected in cases.items():
        assert N.truly_precise(N.R._norm(value))==expected,value
        got=N.n_check_assert('amount',top,[value],'Value',siblings=['Amount'])
        assert got==(('unknown','amount_precision') if expected else ('amount',None)),(value,got)
        result.append({'synthetic':value,'precision_stop':expected})
    for value in ('0.120000001','0.12000000000000001','0.125','123456789012345678901234567890.0000000001'):
        assert len({N.truly_precise(value+'0'*k) for k in range(12)})==1
    original=N.R.check_assert
    try:
        with N.use():
            for header in ('ID','2020'):
                assert N.R.check_assert('amount',top,['$12,345'],header,siblings=['Amount'])==N._orig('amount',top,['$12,345'],header,siblings=['Amount'])
            assert N.R.check_assert('amount',top,['$12,345','0.125'],'Value',siblings=['Amount'])[1]=='amount_precision'
            assert N.R.check_assert('amount',[{'label':'amount','probability':.1}],['$12,345'],'Value',t_low=.5,siblings=['Amount'])[1]=='low_confidence_no_cue'
            raise RuntimeError('probe')
    except RuntimeError as exc:assert str(exc)=='probe'
    assert N.R.check_assert is original
    tiny='0.'+'0'*323+'1'
    assert N._precise_now(tiny) and not N.truly_precise(tiny)
    assert N.n_check_assert('amount',top,[tiny],'Value',siblings=['Amount'])==('amount',None)
    print(json.dumps({'additional_underflow_gap':{'nonzero_decimal':'1e-324 in decimal notation','current_N':'amount','should_preserve_precision_stop':True},'candidate_sha256':'d6a73e871fa1931aec7e199b0e1a455755e1bd6e3cb8acbfcb8fff42408c3be2','cases':result,'equivalent_trailing_zeros_48_cases':'passed','other_stops_mixed_values_and_exception_restoration':'passed'},ensure_ascii=False,indent=1))

if __name__=='__main__':main()
