"""原因の直し（2026-10-30 Claude。research/unknown/findings.md「最後の原因まで」の原因ごと）。**製品のコードは変えない**。
評価のときだけ recheck・verifier の関数を差し替える（with use(fixes): …）か、列の入力を直す（prepare）。採ったものだけ、あとで本物のコードに移す。
事前記録：bench/root_cause_fixes_prereg_20261030.md

  F1 M1：手がかりを探す前に、下線・大文字つなぎの列名を語に分ける（__floating_rate__ → floating rate、SumOfAmount → Sum Of Amount）
  F2 M2：文字化けの £（半角 ｣、NFKC で 」）を £ として読む（列名・単位・値）
  F3 M3：見張りの日付の判定を広げる（date_value_evidence_low で止めた列だけを見直す）
  F4 M12：表の単位の列（UNIT: %）を、軸の列（STATISTIC・TLIST・C#V#・年・四半期・月など）には当てない
  F5 M13：「Cost Centre」に金額の語を当てない
  F6 M6：手がかりの辞書にドイツ語・フランス語を足す
  F7 M14：列名に 1 つの強い手がかりがあり、それが下げる前の答えと同じなら、検査役は下げない
  F8 N1：0 ばかりの列を止める規則（no_value_evidence）を外す
2026-11-01（E1 の原因調査 research/e1_why/findings.md。オーナー「いいぞ」）：
  F1b F1 と同じだが、語に分けて新しく出た手がかりが「番号」だけなら足さない（karosserieform_code は種類のコード）
  G1 単位の列の手がかりを、列名に番号・日付の手がかりがある列には当てない（INDIKATOR_ID・INDIKATOR_JAHR に EINHEIT の % が漏れた）
  G2 空でない値の 8 割以上が % で終わる列は、率の手がかりだけにする（「Persons with Disabilities」4.5%）
  G3 率の語：prop_・rate で始まる語（ratecases・ratedeaths）・steuerfuss（税率。F6 の steuer を金額にしない）
  G4 F3 の日付の判定を広げる：列名の time・hour・heure・day・jour・tag・時、値の HHMMSS・年なしの月日（8/25、8/23,24）・仏独の月の名前・seit 2010・和暦の範囲（S58〜H27）
"""
import contextlib
import re
import unicodedata

import recheck as R

ALL = ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8")
G_ALL = ("F1b", "F3", "F6", "F7", "G1", "G2", "G3", "G4")

_orig_cue_types = R.cue_types
_orig_values_without_evidence = R._values_without_evidence

DIM_HEADER = re.compile(r"^(statistic|statistic label|tlist\(.*\)|c\d+v\d+|year|jahr|annee|année|quarter|quartal|month|monat|mois|week|woche|semaine|"
                        r"period|periode|période|time_period|temporal|date|datum|geo\w*|region|kanton|canton|gemeinde|unit|einheit)$", re.I)
EXTRA = {
    "amount": [r"\bchf\b", r"betrag", r"beitrag", r"kosten", r"ausgaben", r"einnahmen", r"\bpreis", r"tarif", r"lohn", r"gehalt", r"franken", r"steuer",
               r"umsatz", r"montant", r"\bprix\b", r"\bco[uû]t", r"d[ée]pense", r"recette", r"salaire"],
    "quantity": [r"anzahl", r"^anz", r"bestand$", r"^summe\b", r"\bmenge\b", r"einwohner", r"personen", r"f[äa]lle\b", r"\bnombre\b", r"effectif"],
    "rate": [r"prozent", r"\bquote\b", r"quote$", r"anteil", r"grad$", r"beteiligung", r"\btaux\b", r"pourcentage"],
    "date": [r"^jahr$", r"^monat$", r"datum", r"^quartal$", r"^woche$", r"stichtag", r"^semaine$", r"^ann[ée]e$", r"^mois$"],
    "id": [r"nummer$", r"_nr$", r"\bnr\.?$", r"kennung$", r"^num[ée]ro$"],
}
_EXTRA = {k: [re.compile(p, re.I) for p in v] for k, v in EXTRA.items()}


def split_words(h):
    h = str(h or "")
    h = re.sub(r"([a-z])([A-Z])", r"\1 \2", h)
    h = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", h)
    return re.sub(r"_+", " ", h).strip()


_G3_RATE = re.compile(r"(^|[\s_])prop(_|\b)|(^|[\s_])rate[a-z]|steuerfuss|steuerfu[sß]", re.I)
_G1_HEAD = re.compile(r"(_id$|\bid$|_nr$|jahr$|\byear$|_year$|datum$|\bdate$)", re.I)


def _pct_values(values):
    vals = [R._norm(v) for v in values or [] if R._norm(v) not in R._EMPTY]
    return bool(vals) and sum(bool(re.search(r"[%％]\s*\*?$", v)) for v in vals) >= 0.8 * len(vals)


def make_cue_types(fixes):
    def cue_types(header, unit=""):
        u = "" if ("F4" in fixes and DIM_HEADER.match(R._norm(header))) else unit
        if "G1" in fixes and (_G1_HEAD.search(R._norm(header)) or _orig_cue_types(header, "") & {"id", "date"}):
            u = ""
        hits = set(_orig_cue_types(header, u))
        if "F1" in fixes or "F1b" in fixes:
            new = _orig_cue_types(split_words(header), u) - hits
            if "F1b" in fixes and new == {"id"}:
                new = set()
            hits |= new
        if "F6" in fixes:
            h = R._norm(split_words(header) if ("F1" in fixes or "F1b" in fixes) else header)
            for k, pats in _EXTRA.items():
                if any(p.search(h) for p in pats):
                    if k == "amount" and "G3" in fixes and re.search(r"steuerfu", h, re.I):
                        continue
                    hits.add(k)
        if "G3" in fixes and _G3_RATE.search(R._norm(header)):
            hits.add("rate")
            if re.search(r"steuerfu", R._norm(header), re.I):
                hits.discard("amount")
        if "F5" in fixes and re.search(r"cost\s*cent(re|er)", R._norm(header), re.I):
            rest = re.sub(r"cost\s*cent(re|er)", "", R._norm(header), flags=re.I)
            if "amount" not in _orig_cue_types(rest, ""):
                hits.discard("amount")
        return hits
    return cue_types


_orig_check_assert = R.check_assert


def _g2_check_assert(pred, top3, values, header, unit="", t_low=0.0, siblings=None):
    """G2：値の 8 割以上が % の列は、列名・単位の手がかりの代わりに率の手がかりだけで見る。"""
    if _pct_values(values):
        old = R.cue_types
        R.cue_types = lambda h, u="": {"rate"}
        try:
            return _orig_check_assert(pred, top3, values, header, unit, t_low, siblings)
        finally:
            R.cue_types = old
    return _orig_check_assert(pred, top3, values, header, unit, t_low, siblings)


@contextlib.contextmanager
def use(fixes):
    """recheck の関数を差し替える（with の中だけ）。"""
    fixes = set(fixes)
    old = (R.cue_types, R._values_without_evidence, R.check_assert)
    R.cue_types = make_cue_types(fixes)
    if "G2" in fixes:
        R.check_assert = _g2_check_assert
    if "F8" in fixes:
        R._values_without_evidence = lambda values: False if values and all(R._norm(v) not in R._EMPTY for v in values) else _orig_values_without_evidence(values)
    try:
        yield
    finally:
        R.cue_types, R._values_without_evidence, R.check_assert = old


def _pound(s):
    return str(s).replace("｣", "£").replace("」", "£")


def prepare(cols, fixes):
    """列の入力を直す（F2）。cols は verifier_eval.load_batch の列（with_pred のあと）。"""
    if "F2" not in fixes:
        return cols
    out = []
    for c in cols:
        d = dict(c)
        d["header"] = _pound(c["header"])
        d["unit"] = _pound(c.get("unit") or "")
        d["values"] = [_pound(v) for v in c["values"]]
        d["values5"] = [_pound(v) for v in c.get("values5", [])]
        out.append(d)
    return out


# ---------------------------------------------------------------- F3：日付
DATE_HEADER = re.compile(r"date|datum|datierung|pubdate|\bjahr\b|^jahr|year|monat|month|\bweek|woche|semaine|^kw$|quarter|quartal|period|temporal|fiscal|"
                         r"legislatur|^time_period$|年|月|日", re.I)
DATE_VALUE = [re.compile(p, re.I) for p in (
    r"(1[0-9]|20)\d{2}",                                   # 年（1000〜2099）
    r"(19|20)\d{2}[-_ ]?(w|kw)\d{1,2}",                    # 2026-W01
    r"(19|20)\d{2}-m\d{2}",                                # 2024-M04（SDMX の月）
    r"(19|20)\d{2}[_/-](19|20)?\d{2}",                     # 2012_2013・2026_03・2019-20
    r"(19|20)\d{2}(0[1-9]|[1-4]\d|5[0-3])",                # 202441（年と週）・195808
    r"qtr\s*[1-4].*|q[1-4]\s*(19|20)?\d{2}|(19|20)\d{2}\s*q[1-4]",
    r"\d{1,2}\.\d{1,2}\.\d{4}(\s*-\s*\d{1,2}\.\d{1,2}\.\d{4})?",
    r"\d{1,2}",                                            # 週・月・日の番号（列名が週・月・日のとき）
)]


G4_HEADER = re.compile(r"\btime\b|_time|^time|hour|heure|stunde|\bday\b|_day$|^day|jour|\btag\b|時|日|seit|abdeckung|期間|week|_week", re.I)
G4_MONTHS = r"(janv?|f[ée]v(rier)?|fevrier|mars|avr(il)?|mai|juin|juil(let)?|ao[uû]t|sept?(embre)?|oct(obre)?|nov(embre)?|d[ée]c(embre)?|januar|februar|m[äa]rz|juni|juli|oktober|dezember)\.?"
G4_VALUE = [re.compile(p, re.I) for p in (
    r"([01]\d|2[0-3])[0-5]\d[0-5]\d",               # HHMMSS（列名が時刻のとき）
    r"\d{1,2}/\d{1,2}(,\d{1,2})*",                   # 年なしの月日（8/25・8/23,24）
    G4_MONTHS,
    r"seit\s+(19|20)\d{2}",
    r"[MTSHR]\s?\d{1,2}\s*[〜~～-]\s*[MTSHR]\s?\d{1,2}",   # 和暦の範囲（S58〜H27）
)]
_G4 = [False]


def date_ok(header, values):
    h = unicodedata.normalize("NFKC", str(header or ""))
    if _G4[0] and G4_HEADER.search(h):
        vals = [str(v).strip() for v in values if str(v).strip() and str(v).strip().lower() not in ("na", "nan", "-", "")]
        if vals and sum(bool(any(p.fullmatch(unicodedata.normalize("NFKC", v)) for p in G4_VALUE + DATE_VALUE[:-1]) or
                             (re.fullmatch(r"\d{1,2}", v) and int(v) <= 53)) for v in vals) / len(vals) >= 0.8:
            return True
    if not DATE_HEADER.search(h):
        return False
    vals = [str(v).strip() for v in values if str(v).strip() and str(v).strip().lower() not in ("na", "nan", "-", "")]
    if not vals:
        return False
    small = [v for v in vals if re.fullmatch(r"\d{1,2}", v)]
    if small and not re.search(r"week|woche|semaine|^kw$|monat|month|日|月|mois", h, re.I):
        return False
    if small and max(int(v) for v in small) > 53:
        return False
    # Excel の日付の数（列名に date があるときだけ。20000〜60000 は 1954〜2064 年）
    if re.search(r"date|datum", h, re.I) and all(re.fullmatch(r"\d{5}", v) and 20000 <= int(v) <= 60000 for v in vals):
        return True
    return sum(any(p.fullmatch(v) for p in DATE_VALUE) for v in vals) / len(vals) >= 0.8


def fix_guard(cols, fixes):
    """F3：見張りが date_value_evidence_low で止めた列（本体の 1 位が date）を、広げた日付の判定で見直す。"""
    if "F3" not in fixes:
        return cols
    _G4[0] = "G4" in fixes
    out = []
    for c in cols:
        if c.get("guard_reason") == "date_value_evidence_low" and c.get("top3") and c["top3"][0]["label"] == "date" and date_ok(c["header"], c["values5"]):
            c = dict(c, pred="date")
        out.append(c)
    return out
