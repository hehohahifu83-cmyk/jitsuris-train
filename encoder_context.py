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


def attach_unit_context(rows, by_table):
    """評価用の5列tupleへ、同一表の単位欄の短い値だけを追加する。"""
    return [tuple(row[:4]) + (by_table.get(row[4], ""),) if len(row) >= 5 else tuple(row) for row in rows]


def real_train_rows_with_units(rows, copies, seed, keep_other, unit_by_table, perturb_header, per_table=30):
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
        unit = unit_by_table.get(table, "")
        for _ in range(copies):
            vals = rng.sample(values, max(1, int(len(values) * rng.uniform(0.6, 1.0)))) if values else []
            ctx = rng.sample(context, max(1, int(len(context) * rng.uniform(0.4, 1.0)))) if context and rng.random() < 0.8 else None
            out.append((perturb_header(rng, header), vals, label, ctx, unit))
    return out


TITLE_SEP = "\x1e"   # 単位の例の欄に表の題名を一緒に入れるときの区切り（FT_TITLE。encoder_exp.py が単位の例の対応表に足す）


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
