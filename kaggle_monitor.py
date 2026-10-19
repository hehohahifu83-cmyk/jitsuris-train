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


DISPLAY_STATE = {
    "QUEUED": "GPU割当待ち（Kaggle QUEUED）",
    "RUNNING": "Kaggleで実行中（RUNNINGを今回確認）",
    "COMPLETE": "Kaggle完了（COMPLETEを今回確認）",
    "ERROR": "Kaggle失敗（ERRORを今回確認）",
    "CANCELED": "Kaggleがキャンセル（CANCELEDを今回確認）",
    "CANCELLED": "Kaggleがキャンセル（CANCELLEDを今回確認）",
    "UNKNOWN": "未確認（新しいKaggle状態を確認できず）",
}


def render_progress(*, state: str, observed_at: str, raw: str,
                    cycle_id: str, action_run_id: str) -> str:
    """Render the latest observation only; never reuse an older state."""
    label = DISPLAY_STATE.get(state, DISPLAY_STATE["UNKNOWN"])
    evidence = " ".join((raw or "").split()) or "今回の状態取得結果なし"
    lines = [
        "# Kaggle 最新観測",
        "",
        f"- 判定: {label}",
        f"- 観測時刻 (UTC): {observed_at or '未記録'}",
        f"- 学習依頼ID: {cycle_id or '未特定'}",
        f"- GitHub Actions確認run: {action_run_id or '未特定'}",
        f"- Kaggle API応答: {evidence[:500]}",
        "",
    ]
    return "\n".join(lines)


def update_monitor(
    path: str | Path,
    *,
    cycle_id: str,
    observed_at: str,
    state: str,
    raw: str,
    action_run_id: str,
    execution_evidence: list[str] | None = None,
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
    if execution_evidence:
        record["training_execution_confirmed"] = True
        record.setdefault("execution_confirmed_at", observed_at)
        existing = record.setdefault("execution_evidence", [])
        record["execution_evidence"] = list(dict.fromkeys(existing + execution_evidence))

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return record


def latest_training_cycle(log_text: str) -> str:
    """Use the timestamped Kaggle push record as a stable request identifier."""
    matches = re.findall(r"^(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ) train を依頼：", log_text, re.M)
    return matches[-1] if matches else ""


def is_unsubmitted_request(*, event_name: str, request: str, previous_cycle: str, current_cycle: str) -> bool:
    """A new train push without a fresh Kaggle submission must not inherit stale status."""
    return event_name == "push" and request.startswith("train ") and current_cycle == previous_cycle
