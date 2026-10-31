"""encoder_context.apply_label_fix（FT_LABELFIX、2026-10-31 Claude）。"""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from encoder_context import apply_label_fix  # noqa: E402


def test_relabels_only_matching_rows(tmp_path):
    f = tmp_path / "fix.jsonl"
    f.write_text("\n".join(json.dumps(d, ensure_ascii=False) for d in [
        {"table": "t1", "header": "POIコード", "from": "id", "label": "category", "decision": "change"},
        {"table": "t1", "header": "PointID", "from": "id", "label": "id", "decision": "keep"}]) + "\n", encoding="utf-8")
    rows = [("POIコード", ["1"], "id", [], "t1"), ("POIコード", ["1"], "id", [], "t2"), ("PointID", ["1"], "id", [], "t1"),
            ("POIコード ", ["1"], "org", [], "t1")]
    out, n = apply_label_fix(rows, [str(f)])
    assert n == 1
    assert [r[2] for r in out] == ["category", "id", "id", "org"]


def test_stops_when_nothing_matches(tmp_path):
    f = tmp_path / "fix.jsonl"
    f.write_text(json.dumps({"table": "x", "header": "h", "from": "id", "label": "category", "decision": "change"}) + "\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        apply_label_fix([("h", [], "id", [], "y")], [str(f)])
