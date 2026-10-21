"""P1 の規則を一つずつ追加して、固定試験の保存済み v9.1 判定との差を集計する。
出力は run・規則・件数 A/B/C/D のみ。値や見出しは出さない。
"""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from guard_accounting import diff, load_records, rescore_records
from rescore_guard import load_tests
import guard as G

RULE_GROUPS = tuple((r,) for r in (
    "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9",
    "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8",
)) + (("N3", "N4"),)  # Spec example "$236.7 million*" composes modifier and magnitude rules.


def replay(run_dir: str, rule: str, tests: dict) -> tuple[int, Counter]:
    totals = Counter()
    n = 0
    for _filename, doc, baseline in load_records(run_dir):
        test_rows = tests.get(doc["test"])
        if test_rows is None:
            continue

        def guarded(label, order, values):
            return G.guard_with_reason(label, order, values, _enabled_rules=set(rule.split("+")))

        updated = rescore_records(baseline, test_rows, guarded)
        totals.update(diff(baseline, updated))
        n += len(baseline)

    if n == 0:
        raise SystemExit(f"{Path(run_dir).name}: 対応する固定試験レコードがありません")
    return n, totals


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dirs", nargs="+")
    args = parser.parse_args(argv)
    tests = load_tests()
    print("| run | rule | predictions | A | B | C | D |")
    print("|---|---|---:|---:|---:|---:|---:|")
    failed = []
    for run_dir in args.run_dirs:
        for rule_group in RULE_GROUPS:
            rule = "+".join(rule_group)
            n, counts = replay(run_dir, rule, tests)
            print(f"| {Path(run_dir).name} | {rule} | {n} | {counts['A']} | {counts['B']} | {counts['C']} | {counts['D']} |")
            if counts["C"] or counts["D"]:
                failed.append((Path(run_dir).name, rule, counts["C"], counts["D"]))
    if failed:
        raise SystemExit(f"C または D が 0 でない規則があります: {failed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
