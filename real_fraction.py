"""Deterministic whole-table sampling for the S12 fine-tuning learning curve."""
from __future__ import annotations

from decimal import Decimal, InvalidOperation
from hashlib import sha256
from typing import Iterable

DEFAULT_REAL_FRAC_SALT = "jitsuris-ft-real-v1"
SUPPORTED_REAL_FRACS = frozenset((Decimal("0.25"), Decimal("0.5"), Decimal("1.0")))
_REAL_FRAC_QUARTERS = {Decimal("0.25"): 1, Decimal("0.5"): 2, Decimal("1.0"): 4}


def parse_real_fraction(raw: str | None = None) -> float:
    """Accept only the preregistered real-data fractions; default to all rows."""
    if raw is None or raw == "":
        raw = "1.0"
    try:
        fraction = Decimal(raw)
    except (InvalidOperation, TypeError):
        raise ValueError("FT_REAL_FRAC must be one of 0.25, 0.5, or 1.0") from None
    if not fraction.is_finite() or fraction not in SUPPORTED_REAL_FRACS:
        raise ValueError("FT_REAL_FRAC must be one of 0.25, 0.5, or 1.0")
    return float(fraction)


def select_real_fraction(rows: Iterable[tuple], fraction: float, salt: str = DEFAULT_REAL_FRAC_SALT) -> list[tuple]:
    """Keep complete tables selected by a stable hash threshold, preserving input order."""
    try:
        fraction = Decimal(str(fraction))
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("fraction must be one of 0.25, 0.5, or 1.0") from None
    if not fraction.is_finite() or fraction not in SUPPORTED_REAL_FRACS:
        raise ValueError("fraction must be one of 0.25, 0.5, or 1.0")
    if not isinstance(salt, str) or not salt:
        raise ValueError("salt must be a non-empty string")

    rows = list(rows)
    tables: set[str] = set()
    for row in rows:
        if len(row) < 5 or row[4] is None or not str(row[4]).strip():
            raise ValueError("each real row must have a non-empty table key at index 4")
        tables.add(str(row[4]))

    threshold = ((1 << 256) * _REAL_FRAC_QUARTERS[fraction]) // 4
    selected = {
        table for table in tables
        if int.from_bytes(sha256(f"{salt}:{table}".encode("utf-8")).digest(), "big") < threshold
    }
    return [row for row in rows if str(row[4]) in selected]
