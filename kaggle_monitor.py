"""Track fresh Kaggle observations and per-request state transitions."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

STATUS_RE = re.compile(r"KernelWorkerStatus\.([A-Z_]+)")
TERMINAL = {"COMPLETE", "ERROR", "CANCELED", "CANCELLED"}


def parse_status(raw: str, returncode: int = 0) -> str:
    """Return a Kaggle state only when the current API call succeeded."""
    match = STATUS_RE.search(raw or "")
    return match.group(1) if returncode == 0 and match else "UNKNOWN"


def update_monitor(
    path: str | Path,
    *,
    cycle_id: str,
    observed_at: str,
    state: str,
    raw: str,
    action_run_id: str,
) -> dict[str, Any]:
    """Persist bounded observations and the first confirmed lifecycle times."""
    target = Path(path)
    old: dict[str, Any] = {}
    if target.is_file():
        try:
            old = json.loads(target.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            old = {}

    if not cycle_id:
        cycle_id = "unknown"
    if old.get("cycle_id") != cycle_id:
        record: dict[str, Any] = {
            "cycle_id": cycle_id,
            "first_running_at": None,
            "first_complete_at": None,
            "terminal_state": None,
            "observations": [],
        }
    else:
        record = old

    observation = {
        "observed_at": observed_at,
        "state": state,
        "raw": (raw or "")[:500],
        "action_run_id": action_run_id,
    }
    observations = record.setdefault("observations", [])
    if not observations or observations[-1] != observation:
        observations.append(observation)
    record["observations"] = observations[-50:]
    record["last_observed_at"] = observed_at
    record["last_state"] = state

    if state == "RUNNING" and not record.get("first_running_at"):
        record["first_running_at"] = observed_at
    if state == "COMPLETE" and not record.get("first_complete_at"):
        record["first_complete_at"] = observed_at
    if state in TERMINAL:
        record["terminal_state"] = state
        record.setdefault("terminal_at", observed_at)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return record


def latest_training_cycle(log_text: str) -> str:
    """Use the timestamped Kaggle push record as a stable request identifier."""
    matches = re.findall(r"^(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ) train を依頼：", log_text, re.M)
    return matches[-1] if matches else ""
