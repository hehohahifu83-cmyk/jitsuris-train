"""guard.py と column-ai.js の guard が同じ答えを返すかを確かめるための例（guard_fixtures.json）を作る。
Python の結果を正とし、ブラウザ版の guard.test.mjs が同じ入力で同じ出力になるかを確かめる。値はすべて合成（本物の列は入れない）。
使い方：python make_guard_fixtures.py > guard_fixtures.json"""
import json
import random

import guard as G

rng = random.Random(20261018)
DATE_T = {
    "iso": lambda: f"{rng.randint(1995, 2025)}-{rng.randint(1, 12):02d}-{rng.randint(1, 28):02d}", "jp": lambda: f"{rng.randint(2000, 2025)}年{rng.randint(1, 12)}月{rng.randint(1, 28)}日",
    "reiwa": lambda: f"令和{rng.randint(1, 8)}年{rng.randint(1, 12)}月{rng.randint(1, 28)}日", "mdy": lambda: f"{rng.randint(1, 12)}/{rng.randint(1, 28)}/{rng.randint(1990, 2025)}",
    "mdy_time": lambda: f"{rng.randint(1, 12)}/{rng.randint(1, 28)}/{rng.randint(1990, 2025)} {rng.randint(1, 12)}:{rng.randint(0, 59):02d}:00 {rng.choice(['AM', 'PM'])}",
    "fy_slash": lambda: f"{(y := rng.randint(2000, 2024))}/{str(y + 1)[2:]}", "fy_full": lambda: f"{(y := rng.randint(2000, 2024))}/{y + 1}_", "fy_dash": lambda: f"{(y := rng.randint(2000, 2024))}-{str(y + 1)[2:]}",
    "fy_jp": lambda: f"{rng.randint(1990, 2020)}/4-3.", "quarter": lambda: f"{rng.randint(2005, 2024)}Q{rng.randint(1, 4)}", "quarter2": lambda: f"Q{rng.randint(1, 4)} {rng.randint(2005, 2024)}",
    "ym": lambda: f"{rng.randint(2005, 2024)}-{rng.randint(1, 12):02d}", "my": lambda: f"{rng.randint(1, 12):02d}-{rng.randint(2005, 2024)}",
    "statcan": lambda: f"{rng.randint(2005, 2024)}M{rng.randint(1, 12):02d}D{rng.randint(1, 28):02d}",
    "month_abbr": lambda: f"{rng.randint(1, 28):02d}-{rng.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])}-{rng.randint(10, 24)}",
    "day_month": lambda: f"{rng.randint(1, 28)}{rng.choice(['st', 'nd', 'rd', 'th'])} {rng.choice(['March', 'June', 'September', 'December'])}",
    "year_month_name": lambda: f"{rng.randint(2010, 2024)} {rng.choice(['January', 'May', 'July'])} {rng.randint(1, 28)}",
    "time": lambda: f"{rng.randint(0, 23):02d}:{rng.randint(0, 59):02d}", "dotted": lambda: f"{rng.randint(1, 28):02d}.{rng.randint(1, 12):02d}.{rng.randint(1995, 2025)}",
    "era": lambda: f"{rng.choice(['平成', '昭和'])}{rng.randint(1, 30)}年", "era_dotted": lambda: f"{rng.choice(['H', 'R', 'S'])}{rng.randint(1, 30)}.{rng.randint(1, 12)}.{rng.randint(1, 28)}",
    "jp_year": lambda: f"{rng.randint(2000, 2025)}年度", "jp_md": lambda: f"{rng.randint(1, 12)}月{rng.randint(1, 28)}日", "fullwidth_ym": lambda: f"２０２０／{rng.randint(1, 9):02d}".translate(str.maketrans("0123456789", "０１２３４５６７８９")),
}
NUM_T = {
    "plain": lambda: f"{rng.randint(1, 99999)}", "comma": lambda: f"{rng.randint(1, 999):,}.{rng.randint(0, 99):02d}", "yen": lambda: f"¥{rng.randint(1, 99999):,}", "yen_kanji": lambda: f"{rng.randint(1, 99999):,}円",
    "pound": lambda: f"£{rng.randint(1, 9999):,}.{rng.randint(0, 99):02d}", "mojibake": lambda: f"｣{rng.randint(1, 9999):,}.{rng.randint(0, 99):02d}", "euro": lambda: f"€{rng.randint(1, 9999)},{rng.randint(0, 99):02d}",
    "code": lambda: f"USD {rng.randint(1, 9999):,}", "per_person": lambda: f"{rng.randint(1, 99999):,}円/人", "paren": lambda: f"({rng.randint(1, 9999):,})", "unit": lambda: f"{rng.randint(1, 99)} {rng.choice(['kg', 'pcs', 'items', 'years'])}",
    "count_ja": lambda: f"{rng.randint(1, 99)}{rng.choice(['件', '個', '人', '台'])}", "pct": lambda: f"{rng.randint(0, 100)}.{rng.randint(0, 9)}%", "fraction": lambda: f"0.{rng.randint(1, 999):03d}", "year_like": lambda: f"{rng.randint(1900, 2099)}",
}
TEXT = ["alpha", "beta", "gamma", "3rd quintile", "Junior 2", "Marketing 1", "n/a", "#DIV/0!", "One-off", "10160000", "10160001", "ABC123", "abc-9", "", " "]
CASES = []


def add(pred, values, top, second):
    order = [[pred, top], [second[0], second[1]]]
    CASES.append({"pred": pred, "order": order, "values": values, "expected": G.guard(pred, [tuple(o) for o in order], values)})


for name, mk in DATE_T.items():
    for junk in (0.0, 0.3, 0.7):
        vals = [mk() if rng.random() >= junk else rng.choice(TEXT) for _ in range(rng.randint(3, 8))]
        add("date", vals, rng.choice([0.99, 0.95, 0.8]), ("org", 0.004))
for name, mk in NUM_T.items():
    for pred in ("amount", "quantity", "rate"):
        for junk in (0.0, 0.6):
            vals = [mk() if rng.random() >= junk else rng.choice(TEXT) for _ in range(rng.randint(3, 8))]
            add(pred, vals, rng.choice([0.99, 0.9]), ("text", 0.004))
for top in (0.99, 0.92, 0.9, 0.89, 0.73):   # 年だけ：確率の境目
    add("date", [str(rng.randint(1990, 2025)) for _ in range(5)], top, ("amount", 0.2))
    add("date", ["2000", "2000", "1200", "2000", "2000"], top, ("amount", 0.2))
add("date", ["2020", "x", "y", "z"], 0.99, ("org", 0.004))   # 年だけが半分未満
add("date", ["2020", "2021", "x", "y"], 0.99, ("org", 0.004))  # ちょうど半分
add("date", ["2020", "2021", "x", "y"], 0.5, ("org", 0.004))
for tie in ((0.5, 0.4), (0.9, 0.05), (0.6, 0.36)):
    add("amount", ["1", "2", "3"], tie[0], ("quantity", tie[1]))
add("other", ["a", "b"], 0.9, ("text", 0.05))
add("date", [], 0.9, ("org", 0.01))
add("amount", ["", " ", ""], 0.9, ("org", 0.01))
add("id", ["A1", "B2"], 0.9, ("text", 0.01))
add("text", ["hello", "world"], 0.9, ("category", 0.05))
if __name__ == "__main__":
    print(json.dumps(CASES, ensure_ascii=False, indent=0))
