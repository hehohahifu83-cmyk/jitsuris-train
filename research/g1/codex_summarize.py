"""codex_trace の観測結果を数値列の段階別に集計する。標本値は出力しない。"""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

STAGES = ['input_guard', 'guard_G', 'recheck', 'verifier', 'rho', 'dictionary', 'final']
NUMERIC = {'amount', 'rate', 'quantity'}
OFFICIAL_NUMERIC = NUMERIC | {'date', 'id'}

def outcome(pred, truth):
    if pred == 'unknown':
        return 'unk'
    if pred == truth:
        return 'ok'
    return 'crit' if pred in OFFICIAL_NUMERIC and truth in OFFICIAL_NUMERIC else 'wrong'



def origin(row):
    """最後に unknown になった段（その後の unknown 継続を重複計上しない）。"""
    if row['final']['label'] != 'unknown':
        return '', ''
    last_label, at, reason = None, None, None
    for step in STAGES:
        if step not in row:
            continue
        label = row[step]['label']
        if label == 'unknown' and last_label != 'unknown':
            at, reason = step, row[step].get('reason')
        last_label = label
    assert at
    return at, reason or ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--trace', required=True)
    ap.add_argument('--stored', required=True)
    ap.add_argument('--output', required=True)
    a = ap.parse_args()
    p = Path(a.output)
    outputs = [Path(str(p) + ext) for ext in ('.csv', '.summary.json')]
    if any(x.exists() for x in outputs):
        ap.error('既存ファイルには上書きしない')
    payload = json.loads(Path(a.trace).read_text())
    trace = payload['trace']
    stored = json.loads(Path(a.stored).read_text())
    summary = {'environment': payload['environment'], 'arms': {}, 'numeric_drift': [], 'without_verifier': {}}
    rows = []
    for arm, data in trace.items():
        assert sum(d['truth'] in NUMERIC for d in data.values()) == 192
        n, unknown, stages, reasons = Counter(), Counter(), Counter(), Counter()
        for i, d in data.items():
            t, pred = d['truth'], d['final']['label']
            if t not in NUMERIC:
                continue
            assert t in NUMERIC
            n[t] += 1
            at, why = origin(d)
            if at:
                unknown[t] += 1
                stages[at] += 1
                reasons[(at, why)] += 1
            out = 'unk' if pred == 'unknown' else 'ok' if pred == t else 'crit' if pred in {'date', 'amount', 'quantity', 'rate', 'id'} else 'wrong'
            if stored[arm][i] != out:
                summary['numeric_drift'].append({'arm': arm, 'id': i, 'stored': stored[arm][i], 'now': out})
            row = {'arm': arm, 'id': i, 'truth': t, 'header': d['header'], 'unknown_origin': at, 'reason': why}
            row.update({step: d.get(step, {}).get('label', '') for step in STAGES})
            rows.append(row)
        summary['arms'][arm] = {'n': dict(n), 'unknown': dict(unknown), 'stage': dict(stages),
                                'reasons': [{'stage': s, 'reason': w, 'n': k} for (s, w), k in sorted(reasons.items())]}
    for s in (1, 2, 3):
        effects = Counter()
        for i, d in trace[f'L24+G{s}'].items():
            e = trace[f'L24+G-V{s}'][i]
            if d['truth'] not in NUMERIC:
                continue
            if d['final']['label'] != e['final']['label']:
                effects['changed'] += 1
                effects['transition:' + d['final']['label'] + '->' + e['final']['label']] += 1
            if d['final']['label'] == d['truth'] and e['final']['label'] != d['truth']:
                effects['correct_lost'] += 1
            if d['final']['label'] != d['truth'] and e['final']['label'] == d['truth']:
                effects['correct_gained'] += 1
            if d['final']['label'] == 'unknown' and e['final']['label'] != 'unknown':
                effects['unknown_removed'] += 1
                effects['correct' if e['final']['label'] == d['truth'] else 'critical' if e['final']['label'] in {'date', 'amount', 'quantity', 'rate', 'id'} else 'wrong'] += 1
        summary['without_verifier'][str(s)] = dict(effects)
    with outputs[0].open('w') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    outputs[1].write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
