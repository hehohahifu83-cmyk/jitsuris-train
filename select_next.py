"""Select an unlabeled review batch for active learning.

Only materials/real_corpus*.jsonl files are considered. The training rows come
from the normal train3 curriculum and synthetic/municipal teaching data; no
blind evaluation files are opened.
"""
from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path

RARE_CLASSES = ("tax_class", "person", "product", "email", "phone")
BOUNDARY_PAIRS = (("amount", "id"), ("date", "id"), ("org", "account"))


def discover_files(materials_dir: Path) -> list[Path]:
    """Return only unlabeled-corpus JSONL inputs; never enumerate test files."""
    return sorted(
        p for p in materials_dir.glob("real_corpus*.jsonl")
        if p.is_file() and "blind_set" not in p.name.lower()
    )


def _is_labeled(row: dict) -> bool:
    for key in ("label", "class", "target"):
        value = row.get(key)
        if value not in (None, "", "unknown"):
            return True
    return bool(row.get("labels")) or row.get("labeled") is True


def load_candidates(materials_dir: Path) -> list[dict]:
    """Load unlabeled columns from the corpus files, preserving source/table."""
    candidates, seen = [], set()
    for path in discover_files(materials_dir):
        with path.open(encoding="utf-8") as stream:
            for line_no, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                row = json.loads(line)
                if not isinstance(row, dict) or _is_labeled(row):
                    continue
                header = str(row.get("header", "")).strip()
                values = row.get("values", [])
                if not header or not isinstance(values, list):
                    continue
                item = {
                    "source": str(row.get("source", path.stem)),
                    "table": str(row.get("table", "")),
                    "header": header,
                    "values": [str(v) for v in values if str(v).strip()][:5],
                    "context": row.get("context") or [],
                    "file": path.name,
                    "line": line_no,
                }
                key = (item["source"], item["table"], item["header"], tuple(item["values"]))
                if key not in seen:
                    seen.add(key)
                    candidates.append(item)
    return candidates


def _rank_indices(probabilities, classes):
    index = {name: i for i, name in enumerate(classes)}
    top_gap = []
    for i, row in enumerate(probabilities):
        vals = sorted((float(x) for x in row), reverse=True)
        top_gap.append((vals[0] - vals[1] if len(vals) > 1 else vals[0], i))
    return index, top_gap


def _take(ranked, selected, used, count):
    out = []
    for idx in ranked:
        if idx not in used:
            used.add(idx)
            out.append(idx)
            if len(out) == count:
                break
    selected.extend(out)
    return len(out)


def select_candidates(candidates, probabilities, classes, count=200, seed=42):
    """Select in 4:2:2:2 proportions: uncertain, rare, boundaries, stratified random."""
    if count <= 0 or count % 10:
        raise ValueError("count must be a positive multiple of 10")
    if len(candidates) < count:
        raise ValueError(f"need at least {count} unique candidates; found {len(candidates)}")
    if len(probabilities) != len(candidates):
        raise ValueError("probability rows must match candidate count")
    index, gaps = _rank_indices(probabilities, classes)
    used, selected = set(), []

    # (a) 80 columns with the smallest top-two confidence gap.
    _take([i for _, i in sorted(gaps)], selected, used, count * 4 // 10)

    # (b) Eight likely candidates for each requested rare class.
    rare_n = count * 2 // 10
    per_class = rare_n // len(RARE_CLASSES)
    rare_ranked = []
    for name in RARE_CLASSES:
        if name not in index:
            continue
        col = index[name]
        ranked = sorted(range(len(candidates)), key=lambda i: (-float(probabilities[i][col]), i))
        _take(ranked, selected, used, per_class)
    # Fill any missing rare-class slots from the highest rare-class probability.
    missing = rare_n - (len(selected) - count * 4 // 10)
    if missing:
        available = [i for i in range(len(candidates)) if i not in used]
        rare_cols = [index[n] for n in RARE_CLASSES if n in index]
        rare_ranked = sorted(available, key=lambda i: (-max(float(probabilities[i][c]) for c in rare_cols), i)) if rare_cols else available
        _take(rare_ranked, selected, used, missing)

    # (c) 40 columns near one of the critical confusion boundaries.
    boundary_n = count * 2 // 10
    pairs = [(a, b) for a, b in BOUNDARY_PAIRS if a in index and b in index]
    pair_quota = [boundary_n // len(pairs) + (1 if j < boundary_n % len(pairs) else 0) for j in range(len(pairs))]
    for (a, b), quota in zip(pairs, pair_quota):
        ai, bi = index[a], index[b]
        ranked = sorted(
            range(len(candidates)),
            key=lambda i: (abs(float(probabilities[i][ai]) - float(probabilities[i][bi]))
                           + 0.1 * (1 - float(probabilities[i][ai]) - float(probabilities[i][bi])), i),
        )
        _take(ranked, selected, used, quota)
    missing = boundary_n - (len(selected) - count * 6 // 10)
    if missing:
        _take([i for _, i in sorted(gaps)], selected, used, missing)

    # (d) 40 reproducible random choices, round-robin across data sources.
    random_n = count * 2 // 10
    rng = random.Random(seed)
    by_source = defaultdict(list)
    for i, candidate in enumerate(candidates):
        if i not in used:
            by_source[candidate.get("source", "")].append(i)
    for bucket in by_source.values():
        rng.shuffle(bucket)
    random_ranked = []
    sources = sorted(by_source)
    while sources:
        next_sources = []
        for source in sources:
            if by_source[source]:
                random_ranked.append(by_source[source].pop())
            if by_source[source]:
                next_sources.append(source)
        sources = next_sources
    _take(random_ranked, selected, used, random_n)

    # Keep the requested total even if class or pair columns were scarce.
    if len(selected) < count:
        _take([i for _, i in sorted(gaps)], selected, used, count - len(selected))
    assert len(selected) == count and len(set(selected)) == count
    return [candidates[i] for i in selected]


def train_and_select(candidates, count=200, seed=42):
    # Import lazily so candidate selection and its tests do not read training or
    # evaluation modules. train3 imports only its ordinary (non-blind) eval set.
    import numpy as np
    from sklearn.linear_model import LogisticRegression
    from train3 import build_train, mat, split_curriculum

    train_rows = build_train({"syn": 1200, "muni": 3, "cur": 8}, split_curriculum()[0])
    model = LogisticRegression(C=8, max_iter=3000).fit(
        mat(train_rows), np.asarray([row[2] for row in train_rows])
    )
    rows = [(c["header"], c["values"], None, c.get("context")) for c in candidates]
    return select_candidates(candidates, model.predict_proba(mat(rows)), list(model.classes_), count, seed)


def write_batch(selected, output: Path):
    def clean(value):
        return " ".join(str(value).replace("|", " ").replace("\n", " ").split())
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as stream:
        for number, row in enumerate(selected, 1):
            values = list(row.get("values", []))[:3]
            values += [""] * (3 - len(values))
            stream.write("|".join((str(number), clean(row.get("source", "")), clean(row.get("header", "")), *(clean(v) for v in values))) + "\n")


def main():
    root = Path(__file__).resolve().parent
    candidates = load_candidates(root / "materials")
    selected = train_and_select(candidates)
    write_batch(selected, root / "materials" / "next_batch.txt")
    print(f"selected {len(selected)} columns from {len(candidates)} candidates")


if __name__ == "__main__":
    main()
