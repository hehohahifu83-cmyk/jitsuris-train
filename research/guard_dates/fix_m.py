"""直し M の候補（2026-11-12 Claude）：再確認（recheck）の強い手がかりに、海外の表でよく出る金額・数量の語を足す。
G1 の調べ（Codex 20261111-2128）：数の列の不明は再確認が最多（金額の手がかり無し 41・期間の見出しで単位無し 33 など）。G1 は使い済みなので G1 には当てない。
足すのは列名・単位の文字列の語だけ。値は見ない。
"""
import re
import recheck as R

NEW = {
    "amount": [r"\bfunding\b", r"\bgrants?\b", r"\bansatz\b", r"¢", r"\bcents?\b", r"\bsubsid", r"\bmio\.?\s*(eur|€)"],
    "quantity": [r"\bkwh\b", r"\bmwh\b", r"\bgwh\b", r"\bkwh/a\b", r"\(ml\)", r"\bm3\b", r"m³", r"\blitres?\b", r"\bliters?\b",
                 r"\bstudents\b", r"\bpatients\b", r"\bclients\b", r"\bbeneficiaries\b", r"\bemployees\b", r"\bfte", r"\bdeaths\b",
                 r"\bbirths\b", r"\bmarriages\b", r"\bvolunteers\b", r"\bhunters\b", r"\bcasualties\b", r"\bprescriptions\b", r"\btrips\b"],
}
_C = {k: [re.compile(p, re.I) for p in v] for k, v in NEW.items()}


def extra_cues(header, unit=""):
    t = R._norm(R.split_words(header)) + " " + R._norm(unit)
    if R._BAND.search(R._norm(header)):
        return set()
    return {k for k, ps in _C.items() if any(p.search(t) for p in ps)}
