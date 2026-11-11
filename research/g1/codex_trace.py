"""固定予測を G1 の --dry で再採点し、段階ごとの答えを観測する（正解・採否を変更しない）。"""
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import platform
import sys
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location('g1_eval_observed', ROOT / 'research/g1/g1_eval.py')
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--labels', required=True)
    ap.add_argument('--output', required=True, help='新しい診断ファイルの接頭辞（公式レポートを指定しない）')
    a = ap.parse_args()
    prefix = Path(a.output)
    outputs = [Path(str(prefix) + suffix) for suffix in ('.stdout.md', '.json')]
    protected = {(ROOT / 'research/g1/g1_eval.md').resolve(),
                 (ROOT / 'research/g1/g1_eval_per_column.json').resolve(), Path(a.labels).resolve()}
    if any(p.resolve() in protected or p.exists() for p in outputs):
        ap.error('既存ファイル・公式ファイルへの書き込みは禁止')
    prefix.parent.mkdir(parents=True, exist_ok=True)
    EF, E, FX, V = G.D.EF, G.D.EF.E, G.D.EF.FX, G.D.EF.V
    trace, active, seq, eligible, counters = {}, [None], [0], [[]], {}

    def record(i, key, value):
        trace[active[0]].setdefault(i, {})[key] = value

    orig_fix = FX.fix_guard
    def fix(te, fixes):
        for c in te:
            record(c['id'], 'input_guard', {'label': c['pred'], 'reason': c.get('guard_reason')})
        out = orig_fix(te, fixes)
        for c in out:
            record(c['id'], 'guard_G', {'label': c['pred'], 'reason': c.get('guard_reason')})
        return out

    orig_base = E.base_decisions
    def base(cols):
        out = orig_base(cols)
        eligible[0] = [c['id'] for c in cols if c['truth'] and c['truth'] not in ('unknown', 'S', 'other', 'person')]
        for c, v in zip(cols, out):
            record(c['id'], 'truth', c['truth'])
            record(c['id'], 'header', c['header'])
            record(c['id'], 'recheck', {'label': v[0], 'reason': v[1]})
        return out

    orig_combine = E.combine
    def combine(bs, *args, **kwargs):
        out = orig_combine(bs, *args, **kwargs)
        ids = list(trace[active[0]])
        for k, v in out.items():
            record(ids[k], 'verifier', {'label': v[0], 'reason': v[1]})
        return out

    orig_candidate = V.candidate
    def candidate(*args, **kwargs):
        out = orig_candidate(*args, **kwargs)
        k = counters.setdefault('candidate', 0)
        i = eligible[0][k]
        counters['candidate'] = k + 1
        record(i, 'rho', {'label': out if out else args[0], 'replacement': out})
        return out

    orig_amount = V.amount_cue_veto
    def amount(*args, **kwargs):
        out = orig_amount(*args, **kwargs)
        k = counters.setdefault('amount', 0)
        i = eligible[0][k]
        counters['amount'] = k + 1
        record(i, 'dictionary', {'label': args[0]})
        record(i, 'final', {'label': out})
        return out

    orig_run = EF.run
    def observed_run(data, mv, labels, fixes, per=None):
        model = 'L' if seq[0] < 3 else 'L24'
        seed = seq[0] % 3 + 1
        seq[0] += 1
        active[0] = f'{model}+G{seed}'
        trace[active[0]] = {}
        counters.clear()
        result = orig_run(data, mv, labels, fixes, per=per)
        for i, v in per.items():
            assert trace[active[0]][i]['final']['label'] == v[0]
        return result

    orig_no = G.run_no_verifier
    def no(data, mv, labels, fixes, per):
        active[0] = f'L24+G-V{seq[0] - 3}'
        trace[active[0]] = {}
        counters.clear()
        result = orig_no(data, mv, labels, fixes, per)
        for i, v in per.items():
            assert trace[active[0]][i]['final']['label'] == v[0]
        return result

    FX.fix_guard, E.base_decisions, E.combine = fix, base, combine
    V.candidate, V.amount_cue_veto, EF.run, G.run_no_verifier = candidate, amount, observed_run, no
    stream = io.StringIO()
    try:
        with contextlib.redirect_stdout(stream):
            G.main(['--labels', str(Path(a.labels).resolve()), '--dry'])
    finally:
        FX.fix_guard, E.base_decisions, E.combine = orig_fix, orig_base, orig_combine
        V.candidate, V.amount_cue_veto, EF.run, G.run_no_verifier = orig_candidate, orig_amount, orig_run, orig_no
    for rows in trace.values():
        for i in list(rows):
            if rows[i].get('truth') in (None, 'unknown', 'S', 'other', 'person'):
                del rows[i]
    metadata = {'python': platform.python_version(), 'machine': platform.machine(),
                'packages': {p: version(p) for p in ('numpy', 'scipy', 'scikit-learn')},
                'labels_sha256': hashlib.sha256(Path(a.labels).read_bytes()).hexdigest(),
                'eval_sha256': G.sha(ROOT / 'research/g1/g1_eval.py')}
    stored = json.loads((ROOT / 'research/g1/g1_eval_per_column.json').read_text())
    metadata['outcome_drift'] = [
        {'arm': arm, 'id': i, 'stored': stored[arm][i],
         'now': G.D.outcome(d['final']['label'], d['truth'])}
        for arm, rows in trace.items() for i, d in rows.items()
        if stored[arm][i] != G.D.outcome(d['final']['label'], d['truth'])]
    outputs[0].write_text(stream.getvalue(), encoding='utf-8')
    outputs[1].write_text(json.dumps({'environment': metadata, 'trace': trace}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('診断を保存:', ', '.join(str(p) for p in outputs))


if __name__ == '__main__':
    main()
