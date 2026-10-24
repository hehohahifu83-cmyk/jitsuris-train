"""教材庫の「様式」（同じ見出しの組の表のまとまり）で、検証の分け方と表の数をそろえる（2026-10-24 Claude）。

背景：教材庫には、自治体ごとに同じ様式で出ている表が多い（小地域の人口の表 141 表、戸籍窓口の発行枚数の表 16 表など）。
- 表ごとに検証へ回すと、同じ様式の表が学習側にも残り、検証の成績が高く出る（b011 時点で検証の 430 表のうち 115 表）。
  → 様式ごとに検証へ回す（同じ様式の表は全部が学習側か、全部が検証側）。
- 同じ様式の表は、列の名前も値の形もほとんど同じで、増やしても学ぶことが増えない。学習の時間だけ増える。
  → 学習側では 1 様式あたりの表の数に上限を付ける（どの表を残すかは表の名前の md5 の順。見出し・値・ラベルは見ない）。

様式の鍵：表の列名を NFKC・小文字にし、数字を「#」にした集合（「0-4歳」と「5-9歳」は同じ「#-#歳」）。
行の形は exp7.load_real と同じ (見出し, 値, ラベル, 文脈, 表の名前)。
"""
from __future__ import annotations

import hashlib
import re
import unicodedata
from collections import defaultdict

FAMILY_SALT = "jitsuris-poolfamily-v1"


def normalize_header(h) -> str:
    return re.sub(r"[0-9]+", "#", unicodedata.normalize("NFKC", str(h)).strip().casefold())


def family_keys(rows) -> dict:
    """表の名前 → 様式の鍵（列名の集合）。"""
    heads = defaultdict(set)
    for r in rows:
        heads[str(r[4])].add(normalize_header(r[0]))
    return {t: "\x1f".join(sorted(h)) for t, h in heads.items()}


def _order(table: str, salt: str) -> str:
    return hashlib.md5(f"{salt}:{table}".encode("utf-8")).hexdigest()


def split_val_by_family(rows, salt: str, mod: int):
    """様式ごとに (学習側, 検証側) に分ける。様式の鍵の md5 で決めるので毎回同じ。"""
    fam = family_keys(rows)
    val_fams = {f for f in set(fam.values()) if int(_order(f, salt), 16) % mod == 0}
    train, val = [], []
    for r in rows:
        (val if fam[str(r[4])] in val_fams else train).append(r)
    return train, val


def adjudicated_keys(batch_files) -> set:
    """教材庫の batch_*.jsonl のうち、Claude が裁定した列（teacher が claude- で始まる）の (表の名前, 見出し)。
    見出しは exp7.load_real と同じく先頭の BOM を外す。"""
    import json
    keys = set()
    for fn in batch_files:
        with open(fn, encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                d = json.loads(line)
                if str(d.get("teacher", "")).startswith("claude-"):
                    keys.add((str(d["table"]), str(d["header"]).lstrip("﻿")))
    return keys


def cap_tables_per_family(rows, cap: int, salt: str = FAMILY_SALT):
    """1 様式あたり cap 表まで残す（cap が 0 以下なら何もしない）。(残した行, 外した表の数) を返す。"""
    if cap <= 0:
        return list(rows), 0
    fam = family_keys(rows)
    by_fam = defaultdict(list)
    for t, f in fam.items():
        by_fam[f].append(t)
    keep = set()
    for ts in by_fam.values():
        keep.update(sorted(ts, key=lambda t: _order(t, salt))[:cap])
    return [r for r in rows if str(r[4]) in keep], len(fam) - len(keep)
