"""確定教材を番号順に再生。先例には対象陣より前の陣だけを使う。"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'materials'))
import label_sheets as S


def load_fixes(pool):
    fixes = {}
    for name in S.LABELFIX_FILES:
        path = pool / name
        if path.exists():
            for line in path.read_text(encoding='utf-8').splitlines():
                row = json.loads(line)
                if row.get('decision') == 'change':
                    fixes[row['table'], str(row['header']).strip()] = row['from'], row['label']
    return fixes


def corrected(row, fixes):
    label = row['label']
    fix = fixes.get((row['table'], str(row['header']).strip()))
    return fix[1] if fix and label == fix[0] else label


def replay(batches, fixes=None):
    """batches: [(番号, 行のリスト)]。同じ陣の行は全件採点してから先例へ足す。"""
    seen, reports, errors = {}, [], Counter()
    for number, rows in sorted(batches):
        candidates = {}
        for key, (counts, publishers) in seen.items():
            if len(counts) == 1 and sum(counts.values()) >= S.PRECEDENT_MIN_N and len(publishers) >= S.PRECEDENT_MIN_PUB:
                label = next(iter(counts))
                if label in S.LABELS and label != 'unknown':
                    candidates[key] = label
        matched = correct = 0
        for row in rows:
            expected = corrected(row, fixes or {})
            guess = candidates.get(S.head_key(row['header']))
            if guess is not None:
                matched += 1
                correct += guess == expected
                if guess != expected:
                    errors[S.head_key(row['header']), guess, expected] += 1
        reports.append({'batch': f'b{number:03d}', 'rows': len(rows), 'matched': matched, 'correct': correct})
        for row in rows:
            counts, publishers = seen.setdefault(S.head_key(row['header']), (Counter(), set()))
            counts[corrected(row, fixes or {})] += 1
            publishers.add(row.get('publisher'))
    return reports, errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pool', type=Path, default=ROOT / 'materials/pool')
    ap.add_argument('--out', type=Path, default=ROOT / 'bench/precedent_replay_20261104.md')
    args = ap.parse_args()
    batches = []
    for path in sorted(args.pool.glob('batch_b*.jsonl')):
        number = int(re.fullmatch(r'batch_b(\d+)\.jsonl', path.name)[1])
        if number == 18:
            raise SystemExit('禁止されたb018が教材庫にあるため停止')
        batches.append((number, [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]))
    reports, errors = replay(batches, load_fixes(args.pool))
    totals = {k: sum(r[k] for r in reports) for k in ['rows', 'matched', 'correct']}
    def line(name, row):
        coverage = f"{row['matched']/row['rows']:.2%}" if row['rows'] else '—'
        accuracy = f"{row['correct']/row['matched']:.2%}" if row['matched'] else '—'
        return f"| {name} | {row['rows']} | {row['matched']} | {coverage} | {row['correct']} | {accuracy} |"
    text = ['# 先例の時系列再生（2026-11-04、Codex）', '',
            '確定した教材陣だけを番号順に使用。対象陣を採点したあとに先例へ追加。同じ見出し5回以上・2公開元以上・ラベル1種類（unknown除外）。',
            'LABELFIX_FILESの現在の付け直しを、先例と比較対象の両方へ当てる。したがって過去当時のラベル規則を再現した将来性能の推定ではなく、現在の規則での回顧検証。公開元の重なりは除かない。F1には使用しない。', '',
            '| 陣 | 列 | 先例適用 | 適用率 | 一致 | 一致率 |', '|---|---:|---:|---:|---:|---:|']
    text += [line(r['batch'], r) for r in reports] + [line('合計', totals), '',
            f"不一致 {totals['matched']-totals['correct']} 列。Claudeの参考値（28.1%・99.48%・46列）と比較するため丸め前の件数を併記。", '',
            '## 外れた見出しとラベルの組（上位20）', '', '| 見出し | 先例 | 確定（付け直し後） | 列 |', '|---|---|---|---:|']
    text += [f'| {h.replace(chr(124), "&#124;")} | {guess} | {expected} | {n} |' for (h, guess, expected), n in errors.most_common(20)]
    args.out.write_text('\n'.join(text)+'\n', encoding='utf-8')
    print(json.dumps(totals), 'errors', sum(errors.values()))


if __name__ == '__main__':
    main()
