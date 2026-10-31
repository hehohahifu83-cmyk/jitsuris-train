"""bench/d1_split.py の分け方の決まり（2026-10-31 Claude）。"""
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "bench"))
from d1_split import half  # noqa: E402


def test_half_is_sha256_parity():
    for p in ("swiss:oevch", "datagov_uk:cabinet-office", "bodik:401307"):
        want = "decide" if int(hashlib.sha256(p.encode()).hexdigest(), 16) % 2 == 0 else "confirm"
        assert half(p) == want


def test_half_is_stable_and_two_sided():
    names = [f"pub{i}" for i in range(200)]
    got = [half(n) for n in names]
    assert got == [half(n) for n in names]
    assert 60 < got.count("decide") < 140
