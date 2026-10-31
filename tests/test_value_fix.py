"""encoder_context.apply_value_fix（FT_VALUEFIX、2026-11-01 Claude）。"""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from encoder_context import apply_value_fix, cp932_to_cp1252  # noqa: E402


def mojibake(s):
    return s.encode("cp1252").decode("cp932")


def test_reverses_pound_and_apostrophe():
    assert mojibake("£1,250.00") == "｣1,250.00"
    assert cp932_to_cp1252("｣1,250.00") == "£1,250.00"
    assert cp932_to_cp1252(mojibake("Counsel’s Office")) == "Counsel’s Office"
    assert cp932_to_cp1252("plain ascii") == "plain ascii"


def test_refuses_real_japanese():
    with pytest.raises(ValueError):
        cp932_to_cp1252("長与町イメージキャラクター｢ナガヨ　ミックン｣")


def test_fixes_only_listed_tables(tmp_path):
    f = tmp_path / "fix.jsonl"
    f.write_text(json.dumps({"table": "uk", "columns": 2}) + "\n", encoding="utf-8")
    rows = [("Amount", ["｣10", "｣20"], "amount", ["Supplier", "Amount"], "uk"),
            ("Supplier", ["A Ltd"], "org", ["Supplier", "Amount"], "uk"),
            ("説明", ["｢ナガヨ｣"], "text", [], "jp")]
    out, n = apply_value_fix(rows, [str(f)])
    assert n == 2
    assert out[0][1] == ["£10", "£20"] and out[0][2] == "amount"
    assert out[2] == rows[2]


def test_stops_when_column_count_differs(tmp_path):
    f = tmp_path / "fix.jsonl"
    f.write_text(json.dumps({"table": "uk", "columns": 3}) + "\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        apply_value_fix([("Amount", ["｣10"], "amount", [], "uk")], [str(f)])


def test_pool_list_matches_pool():
    """実の教材庫と一覧が合う（43 表・263 列）。直したあと英語の表に「｣」が残らない。"""
    import glob
    root = Path(__file__).resolve().parents[1]
    files = sorted(glob.glob(str(root / "materials" / "pool" / "batch_*.jsonl")))
    rows = []
    for fn in files:
        for line in open(fn, encoding="utf-8"):
            d = json.loads(line)
            rows.append((d["header"], d["values"], d["label"], d["context"], d["table"]))
    out, n = apply_value_fix(rows, [str(root / "materials" / "pool" / "valuefix_cp1252.jsonl")])
    assert n == 263
    listed = {json.loads(l)["table"] for l in open(root / "materials" / "pool" / "valuefix_cp1252.jsonl", encoding="utf-8")}
    assert not any("｣" in v for r in out if r[4] in listed for v in r[1])
