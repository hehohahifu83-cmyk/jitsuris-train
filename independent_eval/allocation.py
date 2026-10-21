"""Deterministic publisher allocation for sealed evaluation sets.

This module operates on publisher identifiers only. It never reads catalog
records, dataset metadata, or table contents.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import unicodedata
from copy import deepcopy
from datetime import date
from pathlib import Path
from typing import Any


ALLOWED_POOLS = frozenset({"train", "eval2", "eval3", "main", "hold"})
ALLOCATABLE_POOLS = frozenset({"train", "eval2", "eval3", "hold"})
FIXED_ASSIGNMENTS = {
    "australia": "train",
    "canada": "train",
    "canada2": "train",
    "datagov_uk": "train",
    "datagov_uk2": "train",
    "direct": "train",
    "egov": "train",
    "egov_biz": "train",
    "egov_biz2": "train",
    "gittables": "train",
    "ireland": "train",
    "jp": "train",
    "jp2": "train",
    "kobe": "main",
    "nyc": "main",
    "sapporo": "main",
    "yokohama": "main",
}


def normalize_publisher_id(publisher_id: str) -> str:
    """Apply the protocol's NFKC, lowercase, and whitespace removal rule."""
    if not isinstance(publisher_id, str):
        raise TypeError("publisher_id must be a string")
    normalized = "".join(unicodedata.normalize("NFKC", publisher_id).lower().split())
    if not normalized:
        raise ValueError("publisher_id must not be empty")
    return normalized


def pool(publisher_id: str) -> str:
    """Return the stable protocol pool for a publisher identifier."""
    canonical = normalize_publisher_id(publisher_id)
    digest = hashlib.sha256(
        f"jitsuris-alloc-v1|{canonical}".encode("utf-8")
    ).hexdigest()
    bucket = int(digest[:8], 16) % 100
    return "eval2" if bucket < 15 else "eval3" if bucket < 30 else "train"


def _alias_map(aliases: dict[str, str]) -> dict[str, str]:
    normalized: dict[str, str] = {}
    for alias, canonical in aliases.items():
        key = normalize_publisher_id(alias)
        target = normalize_publisher_id(canonical)
        if key == target:
            raise ValueError(f"self-referential alias: {key}")
        if key in normalized and normalized[key] != target:
            raise ValueError(f"conflicting aliases for {key}")
        normalized[key] = target
    return normalized


def resolve_publisher_id(publisher_id: str, aliases: dict[str, str]) -> str:
    """Resolve aliases transitively and reject cycles."""
    current = normalize_publisher_id(publisher_id)
    alias_map = _alias_map(aliases)
    seen: set[str] = set()
    while current in alias_map:
        if current in seen:
            raise ValueError("publisher aliases contain a cycle")
        seen.add(current)
        current = alias_map[current]
    return current


def validate_allocation(allocation: dict[str, Any]) -> None:
    """Validate the registry shape and immutable publisher records."""
    if allocation.get("schema_version") != 1:
        raise ValueError("unsupported allocation schema_version")
    aliases = allocation.get("aliases")
    publishers = allocation.get("publishers")
    if not isinstance(aliases, dict) or not isinstance(publishers, list):
        raise ValueError("allocation must contain aliases and publishers")
    normalized_aliases = set(_alias_map(aliases))
    seen: set[str] = set()
    for record in publishers:
        if not isinstance(record, dict):
            raise ValueError("publisher records must be objects")
        publisher_id = normalize_publisher_id(record.get("publisher_id"))
        if publisher_id in seen:
            raise ValueError(f"duplicate publisher assignment: {publisher_id}")
        seen.add(publisher_id)
        if record.get("pool") not in ALLOWED_POOLS:
            raise ValueError(f"invalid pool for {publisher_id}")
        expected_pool = FIXED_ASSIGNMENTS.get(publisher_id)
        if expected_pool is not None and record["pool"] != expected_pool:
            raise ValueError(f"fixed publisher pool cannot change: {publisher_id}")
        if not isinstance(record.get("date"), str):
            raise ValueError(f"missing registry date for {publisher_id}")
        date.fromisoformat(record["date"])
    alias_conflicts = seen & normalized_aliases
    if alias_conflicts:
        raise ValueError(f"registered publisher cannot also be an alias: {sorted(alias_conflicts)[0]}")


def assignment_for(
    publisher_id: str, allocation: dict[str, Any], *, ambiguous: bool = False
) -> dict[str, str]:
    """Return an existing immutable assignment or calculate a new one.

    Ambiguous identities stay on hold until their publisher identity is resolved.
    """
    validate_allocation(allocation)
    canonical = resolve_publisher_id(publisher_id, allocation["aliases"])
    for record in allocation["publishers"]:
        if normalize_publisher_id(record["publisher_id"]) == canonical:
            return {"publisher_id": canonical, "pool": record["pool"], "date": record["date"]}
    destination = "hold" if ambiguous else pool(canonical)
    return {"publisher_id": canonical, "pool": destination}


def add_assignment(
    allocation: dict[str, Any], publisher_id: str, assigned_date: str, *, ambiguous: bool = False
) -> dict[str, Any]:
    """Return a copied registry with one new assignment; never reassign IDs."""
    validate_allocation(allocation)
    date.fromisoformat(assigned_date)
    candidate = assignment_for(publisher_id, allocation, ambiguous=ambiguous)
    existing = next(
        (
            record
            for record in allocation["publishers"]
            if normalize_publisher_id(record["publisher_id"]) == candidate["publisher_id"]
        ),
        None,
    )
    if existing is not None:
        if existing["pool"] != candidate["pool"]:
            raise ValueError(f"publisher already assigned to {existing['pool']}")
        return deepcopy(allocation)
    if candidate["pool"] not in ALLOCATABLE_POOLS:
        raise ValueError("new publishers must use train, eval2, eval3, or hold")
    updated = deepcopy(allocation)
    updated["publishers"].append(
        {"publisher_id": candidate["publisher_id"], "pool": candidate["pool"], "date": assigned_date}
    )
    updated["publishers"].sort(key=lambda item: item["publisher_id"])
    validate_allocation(updated)
    return updated


def load_allocation(path: str | Path) -> dict[str, Any]:
    allocation = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_allocation(allocation)
    return allocation


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Register a publisher before opening dataset metadata or contents."
    )
    parser.add_argument("publisher_id", help="publisher identifier only; do not pass dataset values")
    parser.add_argument("--date", required=True, help="registry entry date in YYYY-MM-DD form")
    parser.add_argument(
        "--registry",
        type=Path,
        default=Path(__file__).with_name("allocation.json"),
        help="allocation registry path",
    )
    parser.add_argument(
        "--ambiguous",
        action="store_true",
        help="keep unresolved publishers on hold until their identity is resolved",
    )
    args = parser.parse_args(argv)

    allocation = load_allocation(args.registry)
    updated = add_assignment(
        allocation, args.publisher_id, args.date, ambiguous=args.ambiguous
    )
    if updated != allocation:
        args.registry.write_text(
            json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    assigned = assignment_for(args.publisher_id, updated, ambiguous=args.ambiguous)
    print(f"{assigned['publisher_id']}\t{assigned['pool']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
