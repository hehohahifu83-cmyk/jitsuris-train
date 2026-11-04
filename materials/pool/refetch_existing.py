"""既存の採用だけを再取得しシートを再生成。回答済みの陣は変更しない。"""
import concurrent.futures
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def validate_batch(batch):
    if not re.fullmatch(r'b1(?:2[4-9]|[34][0-9]|5[01])',batch):raise ValueError('対象外の陣')
    d=ROOT/'materials/pool/work'/batch
    if any((d/'sheets').glob('answers*/*.tsv')) or any(d.glob('labels_*.jsonl')):
        raise ValueError(f'{batch}: 回答があるので再生成しない')
    if json.loads((d/'adopted.json').read_text()).get('pool','train') != 'train':
        raise ValueError(f'{batch}: 教材の採用ではない')
    if not (d/'corpus_log.json').is_file():
        raise ValueError(f'{batch}: 元の取り出し記録がない')
    return d


def run(batch):
    d=validate_batch(batch)
    adopted_sha=digest(d/'adopted.json')
    before=json.loads((d/'corpus_log.json').read_text())
    tmp=d/'corpus.recovery.jsonl'; log=d/'corpus.recovery_log.json'
    cmds=[['materials/fetch_rows.py','--adopted',str(d/'adopted.json'),'--out',str(tmp),'--log',str(log)]]
    subprocess.run([sys.executable,'-I',*cmds[0]],cwd=ROOT,check=True)
    if digest(d/'adopted.json')!=adopted_sha:raise ValueError('採用が同時に変わった')
    after=json.loads(log.read_text())
    before_by={t['n']:t for t in before['tables']}
    transitions=Counter((before_by[t['n']]['status'],t['status']) for t in after['tables'])
    redirects=Counter()
    for t in after['tables']:
        m=re.search(r'redirected outside the allowed hosts: ([A-Za-z0-9.-]+)',t.get('error',''))
        if m:redirects[m.group(1)]+=1
    after['adopted']=f'materials/pool/work/{batch}/adopted.json'
    after['recovery']={'adopted_sha256':adopted_sha,'before_columns':before['columns'],'before_ok_tables':before['ok_tables'],
                       'transitions':{' -> '.join(k):v for k,v in sorted(transitions.items())},'blocked_redirect_hosts':dict(redirects)}
    os.replace(tmp,d/'corpus.jsonl'); log.unlink()
    (d/'corpus_log.json').write_text(json.dumps(after,ensure_ascii=False,indent=1)+'\n')
    for args in (['materials/corpus_to_set.py',str(d/'corpus.jsonl'),str(d/'set.json'),batch],
                 ['materials/label_sheets.py','make','--batch',batch,'--precedent']):
        subprocess.run([sys.executable,'-I',*args],cwd=ROOT,check=True)
    print(f'{batch}: {before["columns"]} -> {after["columns"]}',flush=True)
    return batch

def main():
    batches=sys.argv[1:]
    if not batches or len(set(batches))!=len(batches):raise SystemExit('陣の指定が空か重複')
    for batch in batches:validate_batch(batch)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(run,batches))
if __name__=='__main__':main()
