"""W2 P0: frozen input export and optional retained-seed1 inference; never trains."""
from pathlib import Path
import argparse, hashlib, json, re, subprocess, sys, types, unicodedata
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
OUT = Path(__file__).resolve().parent
BASE = '113dcab2a18ff7b753047b5f726e86cfb4efcefb'
# (unit metadata, acronym expansion); evidence: critical_label_review_codex.md and
# critical_label_adjudication.md. GEO_CANT has no physical unit; leave unchanged.
ADDITIONS = {
    925: ('USD', ''), 1407: ('USD', ''), 1409: ('USD', ''),
    1667: ('elapsed time (hours:minutes:seconds)', 'Avg. = Average'),
    1992: ('full-time equivalent (FTE)', 'SNA = Special Needs Assistant'),
    1993: ('full-time equivalent (FTE)', 'SNAs = Special Needs Assistants'),
    1994: ('full-time equivalent (FTE)', 'SNA = Special Needs Assistant'),
    2074: ('tonnes', ''),
    2220: ('EUR million', 'SSD = Sugar Sweetened Drinks'),
    2509: ('CAD per month', 'GIS = Guaranteed Income Supplement'),
    3096: ('%', ''), 3542: ('', 'GEO_CANT = canton geographical code'),
}

def blob(path):
    return subprocess.check_output(['git', 'show', f'{BASE}:{path}'], cwd=ROOT)

def snapshot_module(name):
    mod = types.ModuleType('_w2_' + name)
    exec(compile(blob(name + '.py'), name + '.py', 'exec'), mod.__dict__)
    return mod

def normalize(s):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', s)).strip().casefold()

def build():
    ec, pf = snapshot_module('encoder_context'), snapshot_module('pool_families')
    paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE,
                                     'materials/pool'], cwd=ROOT, text=True).splitlines()
    paths = [p for p in paths if re.fullmatch(r'materials/pool/batch_[^/]+\.jsonl', p)]
    assert not any('b018' in p for p in paths)
    docs = [json.loads(line) for p in paths for line in blob(p).decode().splitlines()]
    junk = {'nan', 'None', '', 'NaN', 'null', 'NULL'}
    rows = [(d['header'].lstrip('\ufeff'), [v for v in d['values'] if v.strip() not in junk],
             d['label'], d['context'], d['table']) for d in docs]
    fixes = [json.loads(s) for s in blob('materials/pool/labelfix_v24.jsonl').decode().splitlines()]
    fm = {(d['table'], d['header'].strip()): d for d in fixes if d.get('decision') == 'change'}
    fixed, nfix = [], 0
    for r in rows:
        d = fm.get((r[4], r[0].strip()))
        if d and r[2] == d['from']:
            r = r[:2] + (d['label'],) + r[3:]; nfix += 1
        fixed.append(r)
    _, val = pf.split_val_by_family(fixed, salt='jitsuris-poolval-v2', mod=8)
    assert (len(fixed), len(val), nfix) == (38654, 4551, 153)
    units = ec.unit_context_map(fixed)
    titles = json.loads(blob('materials/pool/titles.json'))
    saved = json.loads((ROOT/'eval_reports/latest/job1_probs_val_pool_ft.json').read_text())['rows']
    result = []
    for i, (unit_add, expansion) in ADDITIONS.items():
        h, v, truth, context, table = val[i]
        assert (normalize(h), truth) == (normalize(saved[i]['column']), saved[i]['truth'])
        title = titles.get(table, '')
        row = (h, v, truth, context, units.get(table, '') + ec.TITLE_SEP + title)
        baseline = ec.format_encoder_text(row, prefix='query: ', ctx_unit=True, title=True)
        # W2 already has first 40 title characters. Only relax that field's cap.
        title_arm = baseline.replace(' | 表の題名: ' + title[:40] + ' | 同じ表の列:',
                                     ' | 表の題名: ' + title + ' | 同じ表の列:', 1) if title else baseline
        unit_arm = baseline + (' | 単位: ' + unit_add if unit_add else '')
        acronym_arm = baseline.replace('列名: ' + h + ' | 値:',
                                      '列名: ' + h + (' (' + expansion + ')' if expansion else '') + ' | 値:', 1)
        arms = dict(baseline=baseline, title=title_arm, unit=unit_arm, acronym=acronym_arm)
        result.append(dict(index=i, header=h, values=v, truth=truth, table=table,
                           original_title=title, unit_addition=unit_add, acronym_addition=expansion,
                           inputs=arms, changed={k: x != baseline for k,x in arms.items()},
                           saved_seed1=saved[i]))
    return dict(commit=BASE, seed=1, max_length=160, status='inputs_ready_inference_pending', rows=result)

def infer(data, model_path):
    manifest = json.loads((ROOT/'eval_reports/latest/job1_manifest.json').read_text())
    for name, expected in manifest['saved_model']['files'].items():
        assert hashlib.sha256((model_path/name).read_bytes()).hexdigest() == expected, name
    for name, expected in manifest['saved_model']['weights'].items():
        assert hashlib.sha256((model_path/name).read_bytes()).hexdigest() == expected['sha256'], name
    import torch
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    labels = json.loads((model_path/'labels.json').read_text())
    tok = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
    model.eval(); torch.set_num_threads(2)
    guard = snapshot_module('guard')
    baseline_matches = 0
    for row in data['rows']:
        row['predictions'] = {}
        for arm, text in row['inputs'].items():
            tokens = tok(text, truncation=True, max_length=160, return_tensors='pt')
            with torch.inference_mode():
                probs = torch.softmax(model(**tokens).logits.float(), -1)[0].tolist()
            order = sorted(zip(labels, probs), key=lambda x: -x[1])
            pred, reason = (('unknown', 'probability_below_threshold') if order[0][1] < .5
                            else guard.guard_with_reason(order[0][0], order, row['values']))
            row['predictions'][arm] = dict(raw=order[0][0], guarded=pred, reason=reason,
                top3=order[:3], token_count_untruncated=len(tok(text)['input_ids']),
                visible_input=tok.decode(tokens['input_ids'][0]), token_ids=tokens['input_ids'][0].tolist())
        b, s = row['predictions']['baseline'], row['saved_seed1']
        baseline_matches += (b['raw'], b['guarded'], b['reason']) == (s['raw_prediction'], s['guarded_prediction'], s['decision_reason'])
    data['baseline_matches'] = baseline_matches
    data['status'] = 'measured' if baseline_matches == 12 else 'baseline_mismatch_do_not_interpret'
    data['runtime'] = dict(torch=torch.__version__, device='cpu', precision='fp32', model_weights=manifest['saved_model']['weights'])
    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', type=Path, help='Extracted W2 seed1 ft_out directory')
    parser.add_argument('--output', type=Path, default=OUT/'p0_inputs_codex.json')
    args = parser.parse_args()
    data = build()
    if args.model:
        data = infer(data, args.model)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(data['status'], len(data['rows']), args.output)
