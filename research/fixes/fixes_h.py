"""直し H（2026-11-01 Claude。直し G のあとに残る誤りの調べ research/h_why/findings.md）。**製品のコードは変えない**。
評価のときだけ、最終の答えのあとに当てる（research/fixes/eval_fixes.py の run で、fixes に "H1"・"H2" があるとき）。

  H1 種類のコード：列名が「種類の語＋コードの語尾」（gebaeudekategorie_code・hh_typ_nr・NACE Code・中分類コード）で、
     最終が id、本体の上位 3 に category があれば category にする（LABEL_GUIDE B3：種類を表すコードは category）。
  H2 日付の形：最終が unknown で、列名に日付の語があり、値の 8 割以上がはっきりした日付の形
     （仏独英の月の名前、四半期 Q1〜Q4・T1〜T4、和暦の年月日、時刻の HHMMSS、seit 2010、和暦の範囲、
      列名が日付のときの Excel の日付の番号・UNIX 時刻）なら date にする。1〜2 桁の数だけの列は見ない。
"""
import re
import unicodedata

# ---------------------------------------------------------------- H1
# 種類の語（語の終わりで見る。ドイツ語の合成語 gebaeudekategorie・fahrzeugart に当てるため）
_H1_STEM_END = re.compile(r"(kategorie|category|klasse|art|typ|type|status|form|system|herkunft|sprache|gruppe|group|grp|sektor|sector|zustand|"
                          r"level|lvl|variety)$", re.I)
_H1_STEM_WORD = re.compile(r"^(naics|nace|noga\d*|sic|scian|hs\d*|sh\d*|isic|anzsic|kind|class)$", re.I)
_H1_JA = re.compile(r"(分類|種別|種類|区分|業種|用途|構造)(コード|番号|cd|code)$", re.I)
_H1_SUFFIX = {"code", "nr", "id", "cd", "kode", "codigo"}
# 個々の物・区域・組織を指す語（B3：これは id）
_H1_NOT = re.compile(r"(bfs|gemeinde|gde|geo|kanton|quartier|plz|postal|zip|egid|ewid|parcel|parzelle|objekt|person|org|school|schule|"
                     r"formular|genehmigung|antrag|vertrag|record|row|case|fall|partner|eidg)", re.I)


def _tokens(h):
    h = unicodedata.normalize("NFKC", str(h or "")).replace("\n", " ")
    h = re.sub(r"([a-z])([A-Z])", r"\1 \2", h)
    return [t for t in re.split(r"[\s_\-/|.()]+", h) if t]


def type_code_header(header) -> bool:
    h = unicodedata.normalize("NFKC", str(header or "")).replace("\n", " ").strip()
    if _H1_JA.search(h):
        return True
    toks = [t.lower() for t in _tokens(h)]
    if not toks or _H1_NOT.search(h):
        return False
    # 「コードの語尾」がどこかにある（Naics code / Code Scian のような 2 か国語の列名も見る）
    if not any(t in _H1_SUFFIX for t in toks):
        return False
    stems = [t for t in toks if t not in _H1_SUFFIX]
    # 「art」だけの語は見ない（仏語の Code-art＝品目のコード。合成語の fahrzeugart は見る）
    return any(_H1_STEM_WORD.match(t) or (_H1_STEM_END.search(t) and t != "art") for t in stems)


def h1(final, c):
    if final != "id" or not type_code_header(c["header"]):
        return final
    if any(t.get("label") == "category" for t in (c.get("top3") or [])[:3]):
        return "category"
    return final


# ---------------------------------------------------------------- H2
_H2_HEADER = re.compile(r"date|datum|\bjahr|year|monat|month|mois|mes|trimestre|quarter|quartal|period|p[ée]riode|time|heure|zeit|seit|"
                        r"week|woche|semaine|_at$|年|月|日|期限|時期|時刻|期間", re.I)
_MON = (r"(jan(uary|vier|uar)?|janv|f[ée]v(rier)?|feb(ruary|ruar)?|mar(ch|s)?|m[äa]rz|avr(il)?|apr(il)?|mai|may|juin|june?|juil(let)?|july?|"
        r"ao[uû]t|aug(ust)?|sept?(ember|embre)?|oct(ober|obre)?|okt(ober)?|nov(ember|embre)?|d[ée]c(ember|embre)?|dez(ember)?)\.?")
_H2_VALUE = [re.compile(p, re.I) for p in (
    _MON,
    _MON + r"\s*/\s*" + _MON,                                   # JAN./JAN.（英仏）
    _MON + r"[\s\-]+(19|20)\d{2}",                              # March 2021
    r"[qt][1-4]",                                               # 四半期（列名が日付のとき）
    r"[MTSHR]\s?\d{1,2}\s*\.\s*\d{1,2}\s*\.\s*\d{1,2}",         # 和暦の年月日（H18. 1.26）
    r"[MTSHR]\s?\d{1,2}\s*[〜~～-]\s*[MTSHR]\s?\d{1,2}",          # 和暦の範囲
    r"seit\s+(19|20)\d{2}",
    r"(19|20)\d{2}-\d{2}-\d{2}(/(19|20)\d{2}-\d{2}-\d{2})?([ T]\d{2}:\d{2}(:\d{2})?)?",   # ISO の日付・期間
)]
_H2_TIME = re.compile(r"time|heure|zeit|時刻", re.I)
_H2_SERIAL = re.compile(r"date|datum|年月日|日$|期限|開設|_at$", re.I)


def _vals(values):
    return [unicodedata.normalize("NFKC", str(v)).strip() for v in values
            if str(v).strip() and str(v).strip().lower() not in ("na", "nan", "-", "none", "null")]


def date_shape(header, values) -> bool:
    h = unicodedata.normalize("NFKC", str(header or "")).replace("\n", " ")
    if not _H2_HEADER.search(h):
        return False
    vals = _vals(values)
    if not vals:
        return False

    def one(v):
        if any(p.fullmatch(v) for p in _H2_VALUE):
            return True
        if _H2_TIME.search(h) and re.fullmatch(r"([01]\d|2[0-3])[0-5]\d([0-5]\d)?", v):
            return True
        if _H2_SERIAL.search(h):
            m = re.fullmatch(r"(\d{5})(\.0)?", v)
            if m and 20000 <= int(m.group(1)) <= 60000:     # Excel の日付の番号（1954〜2064 年）
                return True
            if re.search(r"_at$", h) and re.fullmatch(r"1[2-9]\d{8}(\.\d+)?", v):   # UNIX 時刻（2008〜2033 年）
                return True
        return False
    return sum(one(v) for v in vals) / len(vals) >= 0.8


def h2(final, c):
    if final != "unknown":
        return final
    return "date" if date_shape(c["header"], c.get("values5") or c["values"]) else final


def apply(final, c, fixes):
    if "H1" in fixes:
        final = h1(final, c)
    if "H2" in fixes:
        final = h2(final, c)
    return final
