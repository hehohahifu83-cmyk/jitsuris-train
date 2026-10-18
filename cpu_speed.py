"""CPU setup helpers for faster, predictable Jitsuris fine-tuning."""
from __future__ import annotations

import math
import os
from pathlib import Path


def _quota_cores(root: Path) -> int | None:
    """Read cgroup v2 or v1 CPU quota; return the rounded-up core allowance."""
    try:
        quota, period = (root / "cpu.max").read_text(encoding="ascii").split()[:2]
        if quota != "max":
            q, p = int(quota), int(period)
            if q > 0 and p > 0:
                return max(1, math.ceil(q / p))
    except (OSError, ValueError):
        pass

    for base in (root / "cpu", root / "cpu" / "cpu"):
        try:
            q = int((base / "cpu.cfs_quota_us").read_text(encoding="ascii"))
            p = int((base / "cpu.cfs_period_us").read_text(encoding="ascii"))
            if q > 0 and p > 0:
                return max(1, math.ceil(q / p))
        except (OSError, ValueError):
            continue
    return None


def available_cpu_count(
    *, affinity: set[int] | None = None, cpu_count: int | None = None,
    cgroup_root: str | Path = "/sys/fs/cgroup",
) -> int:
    """Return CPUs available to this process, respecting affinity and cgroups."""
    if affinity is None and hasattr(os, "sched_getaffinity"):
        try:
            affinity = set(os.sched_getaffinity(0))
        except OSError:
            affinity = None
    host_count = max(1, len(affinity) if affinity else (cpu_count or os.cpu_count() or 1))
    quota = _quota_cores(Path(cgroup_root))
    return max(1, min(host_count, quota)) if quota else host_count


def configure_cpu_threads(
    environ: dict[str, str] | None = None, *, affinity: set[int] | None = None,
    cpu_count: int | None = None, cgroup_root: str | Path = "/sys/fs/cgroup",
) -> tuple[int, int]:
    """Set numeric-library thread limits before importing NumPy/PyTorch.

    The default uses half of the available CPUs, based on the project benchmark.
    FT_CPU_THREADS can override it; requests above the process allowance are
    capped to avoid thread oversubscription.
    Returns (available_cores, chosen_threads).
    """
    env = os.environ if environ is None else environ
    available = available_cpu_count(affinity=affinity, cpu_count=cpu_count, cgroup_root=cgroup_root)
    default_threads = max(1, available // 2)
    try:
        requested = int(env.get("FT_CPU_THREADS", default_threads))
    except (TypeError, ValueError):
        requested = available
    threads = max(1, min(requested, available))
    for key in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        env[key] = str(threads)
    env["OMP_DYNAMIC"] = "FALSE"
    env["MKL_DYNAMIC"] = "FALSE"
    env["FT_CPU_THREADS"] = str(threads)
    return available, threads


if __name__ == "__main__":
    available, threads = configure_cpu_threads()
    print(f"CPU cores available={available}; threads={threads}")

