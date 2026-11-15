"""Nの回帰表と除外列を確認。本体推論・学習なし。検証済み同一検査役を再利用。"""
import contextlib, hashlib, json, os, pickle, subprocess, sys, tempfile
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/fix_n'))
import fix_n_dev as F
import fix_n as N

def main():
    cache=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
    changed=subprocess.check_output(['git','diff','--name-only','1ebfa7d..HEAD'],cwd=ROOT,text=True).splitlines()
    assert all(p.startswith(('kaggle/','research/fix_n/','research/g3/amount_unknown')) for p in changed),changed
    # このworkspaceの前回588判定の完全再現時に自分で保存した検査役。外部pickleは使わない。
    with cache.open('rb') as fp: _,fitted=pickle.load(fp)
    original=F.D.EF.run; targets=[]
    def capture(data,mv,labels,fixes,per=None):
        if F.D.EF.R.check_assert is N._orig:
            for b,cols in data.items():
                for c in cols:
                    if c['header'] in ('Adjustments(5)','unsafe__3') and c['truth'] in ('unknown','S','other','person'):
                        targets.append((c['id'],c['truth'],data,mv,labels))
        return original(data,mv,labels,fixes,per=per)
    with tempfile.TemporaryDirectory() as tmp,patch.object(F,'HERE',tmp),patch.object(F.D.E,'fit',return_value=fitted),patch.object(F.D.EF,'run',side_effect=capture),patch.object(sys,'argv',['fix_n_dev.py','--f1','/workspace/ai-bridge/labels/f1/final.jsonl','--g1','/workspace/ai-bridge/labels/g1/final.jsonl','--g2','/workspace/ai-bridge/labels/g2/final.jsonl']):
        with (out/'stdout.txt').open('w') as fp,contextlib.redirect_stdout(fp):F.main()
        report=(Path(tmp)/'fix_n_dev.md').read_text()
    baseline=(ROOT/'research/fix_n/fix_n_dev.md').read_text()
    assert report.strip()==baseline.split('\n## 読み（')[0].strip(),'回帰表または変更全列が元のレポートと不一致'
    detail=[]
    for cid,truth,data,mv,labels in targets:
        # truthは採点フィルタだけに使われ、入力特徴や判定関数には使われない。
        # 元ラベルを保存・変更せず、その列も最終段まで通すためローカルコピーでフィルタだけ解除。
        probe={b:[dict(c,truth='amount') if c['id']==cid else c for c in cs] for b,cs in data.items()}
        arms={}
        for tag in ('current','N'):
            F.D.EF._PCACHE.clear();p={}
            if tag=='N':
                with N.use():original(probe,mv,labels,F.D.PRODUCT+('K',),per=p)
            else:original(probe,mv,labels,F.D.PRODUCT+('K',),per=p)
            arms[tag]={'final':p[cid][0],'reason':p[cid][3]}
        detail.append({'id':cid,'original_truth':truth,**arms})
    summary={'report_exact_match':True,'verifier_reused_from':'前回のG3原因点検で588判定を完全再現した検査役','cache_sha256':hashlib.sha256(cache.read_bytes()).hexdigest(),'excluded_columns':detail}
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=1)+'\n');print(json.dumps(summary,ensure_ascii=False,indent=1))

if __name__=='__main__':main()
