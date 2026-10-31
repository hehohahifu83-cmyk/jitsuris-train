"""同じ表の UNIT 列の値を encoder の入力へ渡す小さな実験用ヘルパー。"""
import random
import re
from collections import defaultdict

# 2026-10-29：ドイツ語・フランス語・スペイン語・ポルトガル語と統計局の書き方を足した（einheit・unité・UNIT_MEAS・parameter_unit・data_value_unit など）。
# スイスの陣で単位の列があるのに本体に届いていなかった（bench/unit_header_prereg_20261029.md）。組織の単位（unidade_orcamentaria）は入れない
_UNIT_HEADER = re.compile(r"^(?:unit|units|uom|unit of measure|unit[_ ]of[_ ]measure|measurement[_ ]unit(?:[_ ].*)?|unit[_ ]meas(?:ure)?|data[_ ]value[_ ]unit|"
                          r"parameter[_ ]unit|obs[_ ]?unit(?:[_ ]uniteobs)?|einheit(?:[_ ](?:kurz|lang))?|masseinheit|maßeinheit|unité|unite|unité de mesure|"
                          r"unidad(?: de medida)?|unidade de medida|単位|単位名|(?:amt|amount)[-_ ]units?(?:[_ -].*)?)$", re.I)
_JUNK = {"", "nan", "none", "null", "n/a", "na", "-"}
TITLE_SEP = "\x1e"   # 単位の例の欄に表の題名を一緒に入れるときの区切り（FT_TITLE。encoder_exp.py が単位の例の対応表に足す）


# FT_VALSEL=1（2026-10-30、原因 M15）：本体に渡す 5 個の値のうち欠けの記号を、表の行（row_values）の欠けでない値に入れ替える。
# 欠けでない値はそのまま残すので、欠けのない列の入力は今までと同じ。学習（encoder_exp.py）と予測（evaluate_independent.py）で同じ関数を通す
MISSING = {"", "[x]", "[z]", "[c]", "[u]", ".", "..", ":", "na", "n/a", "nil", "-", "x", "z", "nan", "none", "null", "–", "—", "*", "#n/a"}


def is_missing(value) -> bool:
    return str(value if value is not None else "").strip().lower() in MISSING


def pick_values(values, row_values=None, k=5):
    """values（列ごとの 5 個）の欠けの位置を、row_values の欠けでない値で順に埋める。足りなければ欠けのまま残す。"""
    vals = [str(v) for v in (values or [])][:k]
    spare = iter([str(v) for v in (row_values or []) if not is_missing(v)])
    out = []
    for v in vals:   # 欠けの位置にだけ入れる（並びは変えない。入れる値が尽きたら欠けのまま）
        out.append(next(spare, v) if is_missing(v) else v)
    return out


# FT_UNITX=1（2026-10-30、原因 M7）：「value・Wert」のような汎用の値の列には、同じ表の指標の列（Statistic Label・Kennzahl・metrik など）の値も
# 単位の欄に足す（何の数かが入力に出る）。ほかの列には足さない（単位の列を軸の列に当てて手がかりがぶつかった M12 と同じことを起こさない）
_GENERIC_VALUE = re.compile(r"^(?:value|values|wert|werte|valeur|valore|valor|obs_value|observation|amount_value|数値|値|データ)$", re.I)
_INDICATOR_HEADER = re.compile(r"^(?:statistic(?:[_ ]label)?|indicator(?:[_ ](?:name|label))?|indikator|kennzahl|metrik|measure(?:[_ ]name)?|variable|merkmal|"
                               r"value[_ ]?category|dim|dimension|mesure|indicateur|series(?:[_ ]name)?|指標|項目名)$", re.I)


def indicator_context_map(rows):
    """(header, values, label, context, table) 行から、表ごとに指標の列の値の短い例を作る（FT_UNITX）。"""
    out = {}
    for row in rows:
        if len(row) < 5:
            continue
        header, values, _label, _context, table = row[:5]
        if not _INDICATOR_HEADER.fullmatch(str(header or "").strip()):
            continue
        vals = []
        for value in values or []:
            value = str(value or "").strip()
            if value and value.lower() not in _JUNK and value not in vals:
                vals.append(value[:40])
            if len(vals) == 3:
                break
        if vals:
            out.setdefault(table, [])
            if len(out[table]) < 2:
                out[table].append(f"{str(header).strip()}: {', '.join(vals)}")
    return {t: "; ".join(v) for t, v in out.items()}


def unit_for(header, unit_text, indicator_text):
    """FT_UNITX の単位の欄：汎用の値の列にだけ、単位の例のあとに指標の列の例を足す。"""
    if indicator_text and _GENERIC_VALUE.fullmatch(str(header or "").strip()):
        return f"{unit_text}; {indicator_text}" if unit_text else indicator_text
    return unit_text


def unit_context_map(rows):
    """(header, values, label, context, table) 行から表ごとの UNIT 値の短い例を作る。"""
    out = {}
    for row in rows:
        if len(row) < 5:
            continue
        header, values, _label, _context, table = row[:5]
        if not _UNIT_HEADER.fullmatch(str(header or "").strip()):
            continue
        vals = []
        for value in values or []:
            value = str(value or "").strip()
            if value and value.lower() not in _JUNK and value not in vals:
                vals.append(value[:40])
            if len(vals) == 5:
                break
        if vals and table not in out:
            out[table] = f"{str(header).strip()}: {', '.join(vals)}"
    return out


def _with_indicator(header, unit_full, indicator_by_table, table):
    """単位の欄（単位の例＋区切り＋題名）の単位の例の部分に、FT_UNITX の指標の列の例を足す。indicator_by_table が None なら元のまま。"""
    if not indicator_by_table:
        return unit_full
    unit, sep, ttl = str(unit_full or "").partition(TITLE_SEP)
    return unit_for(header, unit, indicator_by_table.get(table, "")) + sep + ttl


def attach_unit_context(rows, by_table, indicator_by_table=None):
    """評価用の5列tupleへ、同一表の単位欄の短い値だけを追加する。"""
    return [tuple(row[:4]) + (_with_indicator(row[0], by_table.get(row[4], ""), indicator_by_table, row[4]),) if len(row) >= 5 else tuple(row) for row in rows]


LOAD_REAL_JUNK = {"nan", "None", "", "NaN", "null", "NULL"}   # exp7.JUNK と同じ（load_real が外す値）


def load_rows_valsel(files, junk=LOAD_REAL_JUNK):
    """exp7.load_real と同じ行の形で、値を pick_values（FT_VALSEL）で選ぶ。row_values のない教材は load_real と同じ値になる。"""
    import json
    import os
    out = []
    for fn in files:
        if not os.path.exists(fn):
            continue
        for line in open(fn, encoding="utf-8"):
            d = json.loads(line)
            vals = pick_values(d["values"], d.get("row_values"))
            out.append((d["header"].lstrip("\ufeff"), [v for v in vals if v.strip() not in junk], d["label"], d["context"], d["table"]))
    return out


def real_train_rows_with_units(rows, copies, seed, keep_other, unit_by_table, perturb_header, per_table=30, indicator_by_table=None):
    """exp7.real_train_rows と同じ抽出・水増しを行い、単位例を第5要素として保持する。"""
    rng = random.Random(seed)
    by = defaultdict(list)
    for row in rows:
        by[row[4]].append(row)
    capped = []
    for table_rows in by.values():
        capped += rng.sample(table_rows, per_table) if len(table_rows) > per_table else table_rows

    out = []
    for header, values, label, context, table in capped:
        if label == "other" and not keep_other:
            continue
        unit = _with_indicator(header, unit_by_table.get(table, ""), indicator_by_table, table)
        for _ in range(copies):
            vals = rng.sample(values, max(1, int(len(values) * rng.uniform(0.6, 1.0)))) if values else []
            ctx = rng.sample(context, max(1, int(len(context) * rng.uniform(0.4, 1.0)))) if context and rng.random() < 0.8 else None
            out.append((perturb_header(rng, header), vals, label, ctx, unit))
    return out


def format_encoder_text(row, prefix="", ctx_unit=False, val_profile=False, title=False):
    """従来の encoder 入力。ctx_unit=True のときだけ UNIT 例を末尾に追加する。
    val_profile=True（W3a、FT_VALPROF=1）のときだけ、値の直後に「値の形」（value_profile.py）を入れる。切り詰めで先に落ちるのが同じ表の列名になるよう、値の直後に置く。"""
    header, values = row[0], row[1]
    context = row[3] if len(row) > 3 and row[3] else []
    shape = ""
    if val_profile:
        from value_profile import value_profile
        prof = value_profile(values[:5])
        shape = f" | 値の形: {prof}" if prof else ""
    unit = row[4] if len(row) > 4 else ""
    unit, _, table_title = str(unit or "").partition(TITLE_SEP)
    # title=True（FT_TITLE=1、2026-10-25）：表の題名を値の後に入れる（research/root-cause-audit-2026-10-24.md 原因 3：件数か金額かは題名で決まる列が多い）
    ttl = f" | 表の題名: {table_title[:40]}" if title and table_title else ""
    base = f"{prefix}列名: {header} | 値: {', '.join(str(x)[:30] for x in values[:5])}{shape}{ttl} | 同じ表の列: {', '.join(str(x)[:20] for x in context[:12])}"
    if ctx_unit and unit:
        base += f" | 同じ表の単位列の値: {str(unit)[:240]}"
    return base


HEADER_MASK_TOKEN = "（なし）"


def mask_headers(rows, fraction, salt="jitsuris-hmask-v1"):
    """W4（S13）：学習の行のうち決まった割合の見出しを HEADER_MASK_TOKEN に替える（見出しへの頼りすぎを減らす）。
    どの行を替えるかは行の中身と salt の SHA-256 だけで決める（種子・順番に依らない）。評価の行には使わない。"""
    import hashlib
    if not 0.0 <= fraction < 1.0:
        raise ValueError("header mask fraction must be in [0, 1)")
    if fraction == 0.0:
        return list(rows)
    threshold = int(fraction * (1 << 64))
    out = []
    for row in rows:
        key = repr((row[0], tuple(map(str, row[1] or [])), row[2], tuple(map(str, row[3] or [])))).encode("utf-8")
        if int.from_bytes(hashlib.sha256(salt.encode("utf-8") + b"|" + key).digest()[:8], "big") < threshold:
            row = (HEADER_MASK_TOKEN,) + tuple(row[1:])
        out.append(row)
    return out


def apply_label_fix(rows, files):
    """FT_LABELFIX（2026-10-31、D2）：(表, 列名) が決めたことの change の行と合う教材の行のラベルを付け直す。行の形は load_real と同じ
    (列名, 値, ラベル, 同じ表の列, 表)。付け直した行の数を返す。1 行も合わなければ止める（ファイルの取り違え）。"""
    import json
    fix = {}
    for fn in files:
        for line in open(fn, encoding="utf-8"):
            d = json.loads(line)
            if d.get("decision") == "change":
                fix[(d["table"], str(d["header"]).strip())] = (d["from"], d["label"])
    out, n = [], 0
    for r in rows:
        f = fix.get((r[4], str(r[0]).strip()))
        if f and r[2] == f[0]:
            r = (r[0], r[1], f[1]) + tuple(r[3:])
            n += 1
        out.append(r)
    if fix and n == 0:
        raise SystemExit(f"FT_LABELFIX：{files} のどの行も教材と合わない")
    return out, n
