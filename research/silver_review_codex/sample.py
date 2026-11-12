import gzip,json,random,hashlib
from collections import defaultdict
from pathlib import Path
root=Path(__file__).resolve().parents[2]; src=root/'materials/model_corpora/silver/train_A.jsonl.gz'
rows=[json.loads(l) for l in gzip.open(src,'rt') if l.strip()]; random.Random(20261112).shuffle(rows)
by=defaultdict(list); rules=defaultdict(set); tables=set()
for r in rows:
 t=r['label']
 if len(by[t])>=8 or r['rule'] in rules[t] or r['table'] in tables or not r['values']:continue
 by[t].append(r);rules[t].add(r['rule']);tables.add(r['table'])
items=[r for v in by.values() for r in v];random.Random(12112026).shuffle(items)
index=[]; blind=[]
for i,r in enumerate(items,1):
 cid=f's{i:03}';index.append({'id':cid,'label':r['label'],'rule':r['rule'],'table':r['table']})
 blind.append({'id':cid,**{k:r.get(k) for k in ('header','values','title','context')}})
out=root/'research/silver_review_codex'
(out/'sample_index.json').write_text(json.dumps(index,ensure_ascii=False,indent=1)+'\n')
print('source sha256',hashlib.sha256(src.read_bytes()).hexdigest(),'n',len(items))
# 値の転記はしない。必要な場合のみローカルで blind を表示して独立判定する。
