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


def attach_unit_context(rows, by_table, indicator_by_table=None, rowctx_by_table=None):
    """評価用の5列tupleへ、同一表の単位欄の短い値だけを追加する。rowctx_by_table を渡すと同じ行の文も付ける（FT_ROWCTX）。"""
    def unit(row):
        u = _with_indicator(row[0], by_table.get(row[4], ""), indicator_by_table, row[4])
        return with_row_context(u, rowctx_by_table.get(row[4]), row[0]) if rowctx_by_table is not None else u
    return [tuple(row[:4]) + (unit(row),) if len(row) >= 5 else tuple(row) for row in rows]


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


def real_train_rows_with_units(rows, copies, seed, keep_other, unit_by_table, perturb_header, per_table=30, indicator_by_table=None, rowctx_by_table=None):
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
        if rowctx_by_table is not None:   # 同じ行の文は元の列名で自分を除いて作る（水増しで列名を変える前）
            _ctx = rowctx_by_table.get(table)
            if _ctx and str(header) in _ctx["headers"]:   # 文脈に使える列の集合に入っていない列（決められない列の足しなど）には付けない
                unit = with_row_context(unit, _ctx, header)
        for _ in range(copies):
            vals = rng.sample(values, max(1, int(len(values) * rng.uniform(0.6, 1.0)))) if values else []
            ctx = rng.sample(context, max(1, int(len(context) * rng.uniform(0.4, 1.0)))) if context and rng.random() < 0.8 else None
            out.append((perturb_header(rng, header), vals, label, ctx, unit))
    return out


def format_encoder_text(row, prefix="", ctx_unit=False, val_profile=False, title=False, row_ctx=False):
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
    unit, _, row_text = str(unit or "").partition(ROW_SEP)   # FT_ROWCTX：同じ行の文は単位の欄の最後（無ければ空）
    unit, _, table_title = unit.partition(TITLE_SEP)
    # title=True（FT_TITLE=1、2026-10-25）：表の題名を値の後に入れる（research/root-cause-audit-2026-10-24.md 原因 3：件数か金額かは題名で決まる列が多い）
    ttl = f" | 表の題名: {table_title[:40]}" if title and table_title else ""
    # row_ctx=True（FT_ROWCTX=1、方法 T1）：同じ行のほかの列の値を、題名の後・同じ表の列名の前に入れる
    rctx = f" | 同じ行: {row_text}" if row_ctx and row_text else ""
    base = f"{prefix}列名: {header} | 値: {', '.join(str(x)[:30] for x in values[:5])}{shape}{ttl}{rctx} | 同じ表の列: {', '.join(str(x)[:20] for x in context[:12])}"
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
            n += 1
            # 2026-11-09：付け直した先が S・unknown（学習に使わない）の行は外す（学習にも教材庫の検証にも入れない）。
            # S をラベルとして残すと知らない種類になる。数の n には外した行も数える（今までのファイルに S・unknown は無い）
            if f[1] in ("S", "unknown"):
                continue
            r = (r[0], r[1], f[1]) + tuple(r[3:])
        out.append(r)
    if fix and n == 0:
        raise SystemExit(f"FT_LABELFIX：{files} のどの行も教材と合わない")
    return out, n


def cp932_to_cp1252(s):
    """CP1252 のバイトを CP932 で読んで化けた文字列を戻す（2026-11-01、FT_VALUEFIX）。0xA3（£）は「｣」、0x92 0x73（’s）は「痴」に化けていた。
    CP932 に戻せない・CP1252 で読めない文字列は止める（化けていない表を誤って一覧に入れたとき）。"""
    s = str(s)
    if all(ord(c) < 128 for c in s):
        return s
    try:
        return s.encode("cp932").decode("cp1252")
    except UnicodeError as e:
        raise ValueError(f"CP932→CP1252 に戻せない：{s[:40]!r}") from e


def apply_value_fix(rows, files):
    """FT_VALUEFIX（2026-11-01）：一覧（materials/pool/valuefix_cp1252.jsonl）の表の行の列名・値・兄弟の列を cp932_to_cp1252 で戻す。
    行の形は load_real と同じ (列名, 値, ラベル, 同じ表の列, 表)。教材庫のファイルは書き換えない。直した行の数を返す。
    一覧の表の列の数が教材と合わなければ止める（ファイルの取り違え）。"""
    import json
    want = {}
    for fn in files:
        for line in open(fn, encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                want[d["table"]] = d["columns"]
    seen, out = {}, []
    for r in rows:
        if r[4] in want:
            seen[r[4]] = seen.get(r[4], 0) + 1
            r = (cp932_to_cp1252(r[0]), [cp932_to_cp1252(v) for v in r[1]], r[2], [cp932_to_cp1252(c) for c in (r[3] or [])]) + tuple(r[4:])
        out.append(r)
    if seen != want:
        bad = [t for t in want if seen.get(t, 0) != want[t]][:3]
        raise SystemExit(f"FT_VALUEFIX：一覧の列の数が教材と合わない {bad}")
    return out, sum(seen.values())


# ---------------------------------------------------------------- 方法 T1：同じ行のほかの列の値（FT_ROWCTX=1）
# 2026-11-17 Claude（bench/table_reading_plan_20261116.md の改訂の節。Codex の点検 bench/table_reading_review_codex_20261116.md）。
# 列ごとの入力に、同じ表のほかの列の「同じ行の値」を足す。行は表の id と元の行番号（row_index）の固定のハッシュで ROWCTX_ROWS 行を選び、
# 同じ表の全列で同じ行にする。ラベル・列名・予測では選ばない。行がそろわない表（row_index の不一致・重複・長さの違い・同じ列名が 2 つ以上）には足さない。
# 既定はオフで、オフなら入力の文は今までと同じ。学習（encoder_exp.py）と予測（evaluate_independent.py）で同じ関数を通す。
ROW_SEP = "\x1d"          # 単位の欄の最後に、作った「同じ行」の文を付けるときの区切り（TITLE_SEP より後ろ）
ROWCTX_VERSION = "rowctx-v1"
ROWCTX_ROWS = 2           # 足す行の数
ROWCTX_MAX_COLS = 9       # 足すほかの列の数の上限（元の列の順に先頭から）
ROWCTX_MAX_CELL = 24      # 1 つの値の文字の上限
ROWCTX_MAX_HEADER = 20    # ほかの列の名前の文字の上限


def table_row_context(table, cols):
    """cols：同じ表の列（元の列の順）の dict（header・row_values・row_index）。(文脈 or None, 理由 or None) を返す。
    文脈：{"headers": [...], "rows": [[値, ...], ...]}（rows は選んだ行ごと、headers と同じ順）。"""
    import hashlib
    if not cols:
        return None, "列が無い"
    heads = [str(c.get("header")) for c in cols]
    if len(set(heads)) != len(heads):
        return None, "同じ列名が 2 つ以上"
    ri = [tuple(c.get("row_index") or ()) for c in cols]
    if any(not r for r in ri):
        return None, "row_index が空の列がある"
    if len(set(ri)) != 1:
        return None, "列ごとに row_index が違う"
    idx = list(ri[0])
    if len(set(idx)) != len(idx):
        return None, "同じ行番号の重複"
    if any(len(c.get("row_values") or []) != len(idx) for c in cols):
        return None, "row_values と row_index の長さが違う"
    key = lambda p: hashlib.sha256(f"{table}|{idx[p]}".encode("utf-8")).hexdigest()  # noqa: E731
    pos = sorted(sorted(range(len(idx)), key=key)[:ROWCTX_ROWS])
    return {"headers": heads, "rows": [[str(c["row_values"][p]) for c in cols] for p in pos]}, None


def row_context_map(records, allowed=None):
    """records：教材庫の行の dict（table・header・row_values・row_index）。表ごとの文脈と、足さない表の理由を返す。列の順は records の順。
    allowed：文脈に使ってよい列の (表, 列名) の集合（2026-11-17 Codex の点検 1）。学習ではモデルに渡す行（付け直しで S・unknown にして外した列は入らない）、
    評価では主セットの列だけ。入っていない列は文脈にも入れない（除いた列を文脈で戻さない）。None は全部（試験用）。"""
    by = defaultdict(list)
    for d in records:
        if allowed is not None and (d["table"], str(d["header"])) not in allowed:
            continue
        by[d["table"]].append(d)
    ctx, why = {}, {}
    for t, cols in by.items():
        c, w = table_row_context(t, cols)
        if c is None:
            why[t] = w
        else:
            ctx[t] = c
    return ctx, why


def check_row_context(ctx, header):
    """文脈の形を確かめる（2026-11-17 Codex の点検 2）。違えば ValueError。
    headers は重ならない文字列の並び、rows は 1〜ROWCTX_ROWS 行で各行は headers と同じ幅の文字列、対象の列名はちょうど 1 回入っている。"""
    if not isinstance(ctx, dict) or set(ctx) != {"headers", "rows"}:
        raise ValueError("文脈は headers と rows だけを持つ dict")
    heads, rows = ctx["headers"], ctx["rows"]
    if not isinstance(heads, list) or not all(isinstance(h, str) for h in heads) or len(set(heads)) != len(heads):
        raise ValueError("headers は重ならない文字列の並び")
    if not isinstance(rows, list) or not 1 <= len(rows) <= ROWCTX_ROWS:
        raise ValueError(f"rows は 1〜{ROWCTX_ROWS} 行")
    if any(not isinstance(r, list) or len(r) != len(heads) or not all(isinstance(v, str) for v in r) for r in rows):
        raise ValueError("各行は headers と同じ幅の文字列の並び")
    if heads.count(str(header)) != 1:
        raise ValueError(f"対象の列 {header!r} が文脈にちょうど 1 回入っていない")


def render_row_context(ctx, header):
    """対象の列（header）を除いて「名前=値; …」を行ごとに作り、行を「 / 」でつなぐ。足すものが無ければ空。文脈の形が違えば ValueError。"""
    if not ctx:
        return ""
    check_row_context(ctx, header)
    keep = [i for i, h in enumerate(ctx["headers"]) if h != str(header)][:ROWCTX_MAX_COLS]
    if not keep:
        return ""
    rows = []
    for r in ctx["rows"]:
        rows.append("; ".join(f"{ctx['headers'][i][:ROWCTX_MAX_HEADER]}={str(r[i]).strip()[:ROWCTX_MAX_CELL]}" for i in keep))
    return " / ".join(rows)


def with_row_context(unit_full, ctx, header):
    """単位の欄（単位の例＋TITLE_SEP＋題名）の最後に ROW_SEP＋同じ行の文を付ける。足すものが無ければ元のまま。"""
    txt = render_row_context(ctx, header)
    return f"{unit_full}{ROW_SEP}{txt}" if txt else unit_full
