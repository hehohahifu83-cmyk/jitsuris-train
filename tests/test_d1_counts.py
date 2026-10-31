"""bench/d1_counts.py の表ごとの言語の決まり（2026-10-31 Claude）。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "bench"))
from d1_counts import table_lang  # noqa: E402


def rows(*headers, values=()):
    return [{"header": h, "values": list(values)} for h in headers]


def test_japanese_char_wins():
    assert table_lang(rows("year", "人口", values=["1", "2"])) == "ja"


def test_german_headers_with_camel_case():
    assert table_lang(rows("Anfangszeit", "Temperatur", "Druck", "Feuchte")) == "defr"


def test_french_function_words():
    assert table_lang(rows("Nombre de logements", "Commune", "Année")) == "defr"


def test_english_and_codes_stay_english():
    assert table_lang(rows("PERIOD_REF", "REGION", "VALUE", "Type of Slaughter", values=["2019", "cases"])) == "en"


def test_two_german_words_are_not_enough():
    assert table_lang(rows("Jahr", "Anzahl", "id")) == "en"
