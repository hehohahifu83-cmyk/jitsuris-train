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


VOTE = {"id": "V1", "pattern": r"^(名称|name)$", "suffix_vote": {"address": ["公園", "広場", "park"], "org": ["小学校", "図書館"]}}


def test_suffix_vote_picks_majority_place():
    d = TD.Dictionary([VOTE])
    assert d.lookup("名称", ["舞浜公園", "高洲太陽の丘公園", "日の出広場", "東野公園"]) == [("address", "V1")]
    assert d.lookup("名称", ["真岡小学校", "亀山小学校", "市立図書館"]) == [("org", "V1")]
    assert d.lookup("名称", ["舞浜公園", "真岡小学校", "市立図書館", "日の出広場"]) == []      # 割れたら何もしない


def test_strong_entry_applies_when_sure_and_weak_does_not():
    strong = {"id": "S1", "pattern": r"^gebaeudekategorie_code$", "values": r"10\d\d", "type": "category", "strong": True}
    weak = {"id": "W1", "pattern": r"^gebaeudekategorie_code$", "values": r"10\d\d", "type": "category"}
    t3 = T3(("id", 0.97), ("category", 0.02), ("address", 0.01))
    assert TD.Dictionary([strong]).apply("id", t3, "gebaeudekategorie_code", ["1021", "1025"]) == ("category", "S1")
    assert TD.Dictionary([weak]).apply("id", t3, "gebaeudekategorie_code", ["1021", "1025"]) == ("id", None)


def test_vote_only_address_side():
    e = dict(VOTE, vote_only=["address"])
    d = TD.Dictionary([e])
    assert d.lookup("名称", ["舞浜公園", "東野公園", "日の出広場"]) == [("address", "V1")]
    assert d.lookup("名称", ["真岡小学校", "亀山小学校", "市立図書館"]) == []
