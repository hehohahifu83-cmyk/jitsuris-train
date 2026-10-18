"""guard.py と column-ai.js の guard の『値 1 つずつの読み方』が同じかを確かめる例（guard_value_fixtures.json）を作る。
Python の結果を正とし、ブラウザ版の guard.test.mjs が同じ入力で同じ出力になるかを確かめる（ランダムな文字列＋境界の文字列。値はすべて合成）。
各行は [元の文字列, _clean を通した後の文字列, 日付（年だけを除く）か, 日付（年だけを含む）か, 数か]。
使い方：python make_guard_value_fixtures.py > guard_value_fixtures.json"""
import json
import random
import unicodedata

import guard as G

rng = random.Random(20261018)
CURATED = [
    # 年度・年-月・範囲
    "fy2024", "fy2024xyz", "FY2024 Q3", "fy20q3", "FY'20", "fy2020-21", "FY2020/2021", "fy2020 - 21 h1", "2020-99", "2020-45", "2021-13", "2020-00", "2020-12", "2020/7", "13-2015", "7/2015", "07-2015",
    "2023-24", "2012/13", "1999/00", "2012/2013", "2019/2020_", "2017/2018_Apr", "2012/2013_Q3", "2020/2021_zzz", "2010-2020", "2010-2099", "2024-2020", "1994/4-3.", "2014Q1", "Q1 2012", "H1 2020", "2020M07D23",
    # 月名
    "may 5 items", "march of the penguins 2005", "05-May-17", "31st March", "March 2020", "2020 June 30", "Tue, 05 May 2017", "Tuesday 5 May 2017", "May 5, 2017 12:00 AM", "5 May 2017 (rev)", "Junior 2", "Sept. 3", "2016 Mar 01 12:00:00 AM",
    "mar", "may", "5 may", "may 5", "dec 25th", "december 25th, 2020", "2020 dec",
    # その他の日付
    "2024-01-05", "2024/1/5", "2024年1月5日", "令和6年5月1日", "平成30年", "H30/4/1", "R5.5.1", "1/28/2008", "1/28/2008 12:00 AM", "31.12.2019", "03:35", "23:59:10", "2023", "1999", "2023年度", "4月1日",
    # 数
    "1,234", "1,234.50", "1,,2", "1..2", "1 2 3", "12,34,567", "1.234,56", "1 234", "1 234,5", "12.5", "12,5", "1,234,56", "£1,234.50", "€1.234,56", "(1,234)", "330円/人", "5 kg", "3件", "USD 1,000", "｣8,549.00", "1234.", "12 345", "1 2345",
    "+5", "-5", "▲1,000", "¥1,000", "￥3,000", "2,000円", "12.5%", "０．５", "１，２３４", "1e5", "0x10", ".5", "5.", "1,234,", ",5", "1.2.3",
    # 空白・制御文字・BOM（Python の strip と JS の trim の違い）
    "﻿2024-01-05", "\x1c2024-01-05", "2024-01-05\x1f", "\x852024-01-05", " 2024-01-05 ", "　2024-01-05　", " 2024-01-05", " " + "2024-01-05", "᠎2024-01-05", "​2024-01-05",
    "2024-01-05\n", "\t2024-01-05\r\n", " 1,234 ", "1 234", "1　234", "1 234", "﻿1,234", "\x1c1,234",
    # 64 文字の境目（Python は文字、JS は UTF-16）
    "a" * 63 + "😀" + "b", "a" * 62 + "😀😀", "😀" * 40, "𠮷" * 70, "1" * 62 + "😀😀", "2024-01-05" + " " * 70 + "x", "x" * 64, "x" * 65, "1" * 70,
    # 小文字化の違い
    "İSTANBUL 2020", "ẞ 5", "ΣΑΣ 2020", "ǅ 1", "MAY 5", "MARCH 2020", "ＭＡＹ ５",
    "", " ", "　", "﻿",
]
TOKENS = {
    "digits": lambda: str(rng.choice([1, 2, 3, 5, 7, 9, 10, 12, 13, 19, 20, 24, 31, 45, 99, 100, 1234, 2000, 2019, 2020, 2024, 2025, 12345, 1234567])).zfill(rng.choice([1, 1, 2, 4])),
    "sep": lambda: rng.choice(["/", "-", "–", ".", ",", "_", "*", " ", "  ", "\t", "　", "\xa0", "﻿", "\x1c", "\x85", " ", "\n", ", ", " - ", "/ "]),
    "month": lambda: rng.choice(["jan", "March", "MAY", "sept.", "December", "may", "mar", "Aug", "oct", "nov."]),
    "prefix": lambda: rng.choice(["fy", "FY'", "q1", "Q3", "h2", "H1", "r", "s", "H", "tue,", "Monday", "wed", "sat."]),
    "suffix": lambda: rng.choice(["st", "nd", "rd", "th", "xyz", " AM", "pm", ":30", " 12:00:00", "_", "*", "(rev)", " items"]),
    "cur": lambda: rng.choice(["¥", "$", "£", "€", "₩", "円", "%", "kg", "件", "USD ", "R", "人", "円/人", "(", ")", "+", "−", "▲", "△"]),
    "cjk": lambda: rng.choice(["年", "月", "日", "令和", "平成", "度", "年度"]),
    "emoji": lambda: rng.choice(["😀", "𠮷", "👨‍👩‍👧"]),
    "full": lambda: "".join(rng.choice("０１２３４５６７８９") for _ in range(rng.randint(1, 4))),
    "word": lambda: rng.choice(["abc", "n/a", "total", "of the", "x", "Q", "年", "ａｂｃ", "ǅ", "İ", "ẞ", "Σ"]),
}
KINDS = list(TOKENS)
WEIGHTS = [6, 5, 2, 1, 2, 2, 1, 1, 1, 1]


def random_value():
    return "".join(TOKENS[rng.choices(KINDS, WEIGHTS)[0]]() for _ in range(rng.randint(1, 7)))


def entry(raw):
    cleaned = G._clean([raw])
    c = cleaned[0] if cleaned else ""
    return [raw, c, bool(c) and G.is_date_value(c, True), bool(c) and G.is_date_value(c, False), bool(c) and bool(G.NUM_LOOSE.match(c))]


if __name__ == "__main__":
    values = list(CURATED) + [random_value() for _ in range(4000)]
    print(json.dumps([entry(v) for v in values], ensure_ascii=False, separators=(",", ":")))
