import json

import pytest

import table_dictionary as TD

E = [{"id": "K1", "pattern": r"(^|[^a-z])fsa$", "type": "address", "values": r"[a-z]\d[a-z]"},
     {"id": "K2", "pattern": r"^poiコード$", "type": "category"},
     {"id": "K3", "pattern": r"^region$", "type": "address"},
     {"id": "K4", "pattern": r"^region$", "type": "id"}]
T3 = lambda *lp: [{"label": l, "probability": p} for l, p in lp]  # noqa: E731


def test_doubtful_unknown_uses_entry_in_top3():
    d = TD.Dictionary(E)
    assert d.apply("unknown", T3(("org", 0.79), ("address", 0.17), ("id", 0.02)), "FSA", ["T4K", "T5H", "V0R"]) == ("address", "K1")


def test_values_condition_blocks():
    d = TD.Dictionary(E)
    assert d.apply("unknown", T3(("org", 0.79), ("address", 0.17), ("id", 0.02)), "FSA", ["Toronto", "Calgary"]) == ("unknown", None)


def test_confident_answer_not_changed():
    d = TD.Dictionary(E)
    assert d.apply("id", T3(("id", 0.97), ("category", 0.02), ("quantity", 0.01)), "POIコード", ["1309"]) == ("id", None)


def test_low_confidence_answer_changed_only_if_in_top3():
    d = TD.Dictionary(E)
    assert d.apply("id", T3(("id", 0.80), ("category", 0.15), ("quantity", 0.01)), "ＰＯＩコード", ["1309"]) == ("category", "K2")
    assert d.apply("id", T3(("id", 0.80), ("quantity", 0.15), ("date", 0.01)), "POIコード", ["1309"]) == ("id", None)


def test_conflicting_entries_do_nothing():
    d = TD.Dictionary(E)
    assert d.apply("unknown", T3(("address", 0.5), ("id", 0.4), ("org", 0.1)), "Region", ["SO"]) == ("unknown", None)


def test_bad_type_and_duplicate_id(tmp_path):
    with pytest.raises(ValueError):
        TD.Dictionary([{"id": "X", "pattern": "a", "type": "place"}])
    p = tmp_path / "t.jsonl"
    p.write_text("\n".join(json.dumps(e) for e in (E[0], E[0])), encoding="utf-8")
    with pytest.raises(ValueError):
        TD.Dictionary.load(p)
