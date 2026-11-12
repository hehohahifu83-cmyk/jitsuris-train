"""独立回答確定後だけ実行する。値は出力しない。"""
import json
from pathlib import Path
from collections import defaultdict
HERE = Path(__file__).resolve().parent
answers = dict(line.split() for line in (HERE / 'answers.tsv').read_text().splitlines())
index = json.loads((HERE / 'sample_index.json').read_text())
assert len(answers) == len(index) == 75
by = defaultdict(list)
comparison = []
for item in index:
    by[item['label']].append(item)
    comparison.append(dict(item, codex=answers[item['id']], teacher='codex'))
for label, rows in sorted(by.items()):
    ok = sum(answers[r['id']] == label for r in rows)
    print(f'{label}: {ok}/{len(rows)} ({ok/len(rows):.1%})')
(HERE / 'comparison.json').write_text(json.dumps(comparison, ensure_ascii=False, indent=1) + '\n')
