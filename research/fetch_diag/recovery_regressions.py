"""再取得で失った表の差を、値やラベルを保存せず調べる。"""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'materials'))
import fetch_rows as F
orig=F._find_header
shapes=[]
def inspect(rows):
    shapes.append({'widths':[len(r) for r in rows[:40]],'filled':[sum(bool(c.strip()) for c in r) for r in rows[:40]]})
    return orig(rows)
F._find_header=inspect
out=[]
for batch,n in ((128,3),(128,26),(131,14),(133,7)):
    shapes.clear()
    item=next(a for a in json.loads((ROOT/f'materials/pool/work/b{batch}/adopted.json').read_text())['adopted'] if a['n']==n)
    result={'batch':batch,'n':n,'resource_url':item['resource_url']}
    try:
        m,f,r,t=F.fetch_table(item,set());cols,reasons=F.build_rows(m,f,r,t)
        result.update({'status':'ok','fields':len(f),'records':len(r),'columns':len(cols)})
    except Exception as e:result.update({'status':'error','error':str(e)[:200]})
    result['layouts']=list(shapes)
    out.append(result);print(json.dumps(result),flush=True)
(ROOT/'research/fetch_diag/recovery_regressions.json').write_text(json.dumps(out,ensure_ascii=False,indent=1)+'\n')
