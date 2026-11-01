"""止める段の直し G（2026-11-01、bench/stopfix_prereg_20261101.md）を recheck.py・guard.py に移したことの試験。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import guard  # noqa: E402
import recheck as R  # noqa: E402

T3 = lambda lab, p=0.97: [{"label": lab, "probability": p}, {"label": "quantity", "probability": 0.02}, {"label": "id", "probability": 0.01}]  # noqa: E731


def test_g3_rate_words():
    for h in ("prop_fully", "ratedeaths", "ratecases_total", "Anteil Ausländer", "gesamtsteuerfuss_kath"):
        assert "rate" in R.cue_types(h), h
    assert "amount" not in R.cue_types("gesamtsteuerfuss_kath")


def test_g2_percent_values_override_header():
    assert R.check_assert("rate", T3("rate"), ["4.5%", "5.3%", "5.5%"], "Persons with Disabilities") == ("rate", None)


def test_g1_unit_not_applied_to_id_and_year_headers():
    assert R.cue_types("INDIKATOR_ID", "%") == {"id"} or "rate" not in R.cue_types("INDIKATOR_ID", "%")
    assert "rate" not in R.cue_types("INDIKATOR_JAHR", "Prozent %")
    assert "rate" in R.cue_types("INDIKATOR_VALUE", "%")


def test_f1b_split_words_but_not_id_only():
    assert "amount" in R.cue_types("contractAmount")
    assert "id" not in R.cue_types("karosserieform_code") or R.cue_types("karosserieform code") == {"id"}


def test_guard_date_g4():
    ok = lambda h, v: guard.header_date_ok_g(h, v)  # noqa: E731
    assert ok("選抜日", ["8/25", "8/22"])
    assert ok("Time_UTC_HHMMSS", ["143611", "123005"])
    # 測った形（E2）では、月の名前は「時刻・日・週」などの列名のときだけ使う。列名が「月」の列は直らない（次の改善の候補、research/e1_why/findings.md）
    assert not ok("Mois - Months", ["Fevrier", "Novembre", "Juin"])
    assert ok("reporting_week", ["6", "43", "34"])
    assert not ok("Amount", ["8/25"])
    assert not ok("reporting_week", ["6", "143", "34", "77", "99"])
