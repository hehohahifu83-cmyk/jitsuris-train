#!/usr/bin/env python3
"""ブラウザ（JavaScript）の正規化が、学習のときに使った Hugging Face tokenizers（Rust）の正規化と同じ答えを出すか調べるための正解データを作る（2026-10-18）。

背景：Transformers.js は sentencepiece の正規化表（Precompiled）を NFKC で近似しているだけで、半角カナの濁点（ｿﾞ）を「ゾ」と合成してしまう。
学習時の HF tokenizers は表を書記素ごとに引き、「ソ」＋「゙」の 2 片にする。業務データの半角カナで実際にずれる（試験の文 492 本のうち 3 本）。
そこで JS 側に表を引く正規化（browser_test/charsmap.mjs）を作った。これはその正解データを作る側（Python）。GitHub Actions で動かす（tokenizers が要る）。

作るもの（--full の場所に全部、--small の場所に軽い版。小さい版はリポジトリに commit して、手元の Node でも試験できるようにする）：
  charsmap.b64        … tokenizer.json の Precompiled の表（sentencepiece の precompiled_charsmap。base64 のまま）
  norm_single.json    … 1 文字だけの文字列（全 Unicode スカラー値）の正規化のうち、元と変わるものだけ（残りは元のまま）
  norm_cases.json     … グループごとの [元, 正規化後]：pairs（基底の文字＋結合文字・書式文字など）／triples／random（偏らせたランダム文）／edge（変わった文字列）
正規化は tokenizers.normalizers.Precompiled（Rust 実装）で行う。Replace（空白の連続を 1 つに）は JS でも普通の正規表現なので、全体（tok.normalizer）との整合は
ここで確かめる（合わなければ失敗）。未見セット（blind）は扱わない。

使い方：python tokenizer_fixtures.py --model intfloat/multilingual-e5-small --full fx_full --small browser_test/fixtures
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import random
import re
import sys
import unicodedata

from edge_texts import EDGE_TEXTS


def scalar_values():
    """全 Unicode スカラー値（サロゲートを除く）。"""
    for cp in range(0, 0x110000):
        if 0xD800 <= cp <= 0xDFFF:
            continue
        yield cp


# 基底の文字（この後ろに結合文字などを付けて、書記素と正規化の動きを見る）
BASES = [
    "a", "e", "n", "1", " ", "\r", "\n", "\t",
    "ｱ", "ｶ", "ｿ", "ﾊ", "ﾜ", "ｦ", "ﾞ", "ﾟ",            # 半角カナ・半角の濁点
    "ア", "カ", "ソ", "ハ", "ウ", "か", "は", "あ",       # かな
    "漢", "한", "ᄀ", "क", "ส", "ا", "Ａ", "㈱", "①", "。",
    "🙂", "❤", "👍", "🇯", "1",
]


def extender_codepoints():
    """基底の文字の後ろに付けると書記素や正規化の動きが変わりうる文字：結合文字（Mn・Mc・Me）・書式文字（Cf）・異体字選択子・半角の濁点など。"""
    out = set()
    for cp in scalar_values():
        if unicodedata.category(chr(cp)) in ("Mn", "Mc", "Me", "Cf"):
            out.add(cp)
    out.update(range(0xFF9E, 0xFFA0))        # 半角の濁点・半濁点
    out.update(range(0x3099, 0x309D))        # かなの濁点類
    out.update(range(0x1F3FB, 0x1F400))      # 肌色
    out.update(range(0x1F1E6, 0x1F200))      # 国旗の文字
    out.update(range(0x1100, 0x1200))        # ハングルのジャモ
    out.update([0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF, 0xFE0E, 0xFE0F, 0x20E3, 0x0301, 0x0308])
    return sorted(out)


def random_alphabet():
    """ランダム文の部品。実際の表に出そうなもの（半角カナ・かな・全角英数・結合文字・空白類・絵文字など）に偏らせる。"""
    ranges = [
        (0xFF61, 0xFF9F), (0x3041, 0x30FF), (0x3099, 0x309C), (0x0020, 0x007E), (0x0300, 0x036F),
        (0xFF01, 0xFF5E), (0x3300, 0x33FF), (0x2460, 0x24FF), (0x3200, 0x32FF), (0x4E00, 0x4E80),
        (0xAC00, 0xAC40), (0x1100, 0x11FF), (0x1F300, 0x1F34F), (0x1F3FB, 0x1F3FF), (0x0600, 0x0650),
        (0x0900, 0x0950), (0xFE00, 0xFE0F), (0x2000, 0x206F), (0x00A0, 0x00FF), (0x2100, 0x218F),
    ]
    chars = []
    for a, b in ranges:
        chars.extend(chr(c) for c in range(a, b + 1) if not 0xD800 <= c <= 0xDFFF)
    # 空白・制御・表記ゆれの文字は多めに（重みを付けるため繰り返す）
    special = [" ", "\t", "\n", "\r", "\x0b", "\x0c", "\x7f", "\x85", "​", "‍", "﻿", "�", "　", "〜", "～", "~", "▁"]
    chars.extend(special * 12)
    chars.extend("ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾊﾋﾌﾍﾎﾞﾟ" * 3)
    return chars


def make_pairs(extenders):
    return [b + chr(e) for b in BASES for e in extenders]


def make_triples(extenders, n, rng):
    return [rng.choice(BASES) + chr(rng.choice(extenders)) + chr(rng.choice(extenders)) for _ in range(n)]


def make_random_strings(alphabet, n, rng, max_len=10):
    return ["".join(rng.choice(alphabet) for _ in range(rng.randint(1, max_len))) for _ in range(n)]


def precompiled(blob):
    """バイト列 → tokenizers.normalizers.Precompiled（バインディングによって bytes か list で受ける）。"""
    from tokenizers import normalizers
    try:
        return normalizers.Precompiled(blob)
    except TypeError:
        return normalizers.Precompiled(list(blob))


def load(model):
    from tokenizers import Tokenizer
    tok = Tokenizer.from_pretrained(model)
    tj = json.loads(tok.to_str())
    norm = tj.get("normalizer") or {}
    items = norm.get("normalizers") if norm.get("type") == "Sequence" else [norm]
    pre = next((n for n in (items or []) if n.get("type") == "Precompiled"), None)
    if pre is None:
        raise SystemExit("この tokenizer.json に Precompiled の正規化がない")
    blob = base64.b64decode(pre["precompiled_charsmap"])
    return tok, pre["precompiled_charsmap"], blob, [n.get("type") for n in items]


def dump(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="intfloat/multilingual-e5-small")
    ap.add_argument("--full", required=True, help="全部の正解データの置き場（commit しない）")
    ap.add_argument("--small", default="", help="軽い版の置き場（commit する）。空なら作らない")
    ap.add_argument("--seed", type=int, default=20261018)
    ap.add_argument("--n-random", type=int, default=120000)
    ap.add_argument("--n-triples", type=int, default=30000)
    ap.add_argument("--small-max-interesting", type=int, default=6000, help="軽い版に入れる『文脈で答えが変わる例』の上限")
    ap.add_argument("--small-random", type=int, default=2000)
    args = ap.parse_args(argv)

    import tokenizers
    tok, b64, blob, kinds = load(args.model)
    pre = precompiled(blob)
    full_norm = tok.normalizer
    rng = random.Random(args.seed)
    info = {"model": args.model, "tokenizers": tokenizers.__version__, "normalizers": kinds, "charsmap_bytes": len(blob), "seed": args.seed}
    print(f"tokenizers {tokenizers.__version__}　正規化 {kinds}　表 {len(blob):,} バイト", flush=True)

    # 1. 1 文字だけ：全スカラー値
    diff, n_single = {}, 0
    for cp in scalar_values():
        s = chr(cp)
        out = pre.normalize_str(s)
        n_single += 1
        if out != s:
            diff[str(cp)] = out
    print(f"1 文字：{n_single:,} 個中、正規化で変わるもの {len(diff):,} 個", flush=True)

    # 2. 組み合わせ・ランダム文・変わった文字列
    extenders = extender_codepoints()
    groups = {
        "pairs": make_pairs(extenders),
        "triples": make_triples(extenders, args.n_triples, rng),
        "random": make_random_strings(random_alphabet(), args.n_random, rng),
        "edge": ["query: " + t for t in EDGE_TEXTS] + list(EDGE_TEXTS),
    }
    cases = {}
    mismatch_full = 0
    for name, raws in groups.items():
        seen, rows = set(), []
        for raw in raws:
            if raw in seen:
                continue
            seen.add(raw)
            out = pre.normalize_str(raw)
            rows.append([raw, out])
            # 全体（Precompiled の次の Replace「空白の連続を 1 つに」まで）と整合するか
            if re.sub(" {2,}", " ", out) != full_norm.normalize_str(raw):
                mismatch_full += 1
                if mismatch_full <= 5:
                    print("整合しない例（Precompiled + Replace と tok.normalizer）:", repr(raw), repr(out), repr(full_norm.normalize_str(raw)), flush=True)
        cases[name] = rows
        changed = sum(1 for r, o in rows if r != o)
        print(f"{name}：{len(rows):,} 件（正規化で変わるもの {changed:,} 件）", flush=True)
    if mismatch_full:
        print(f"失敗：Precompiled + Replace と tok.normalizer が合わない例が {mismatch_full} 件", file=sys.stderr)

    # 3. 書き出し
    os.makedirs(args.full, exist_ok=True)
    open(os.path.join(args.full, "charsmap.b64"), "w", encoding="ascii").write(b64)
    dump(os.path.join(args.full, "norm_single.json"), {"info": info, "diff": diff})
    dump(os.path.join(args.full, "norm_cases.json"), {"info": info, "groups": cases})
    print("全部の正解データ：", args.full, flush=True)

    if args.small:
        os.makedirs(args.small, exist_ok=True)
        single_chars = {int(k): v for k, v in diff.items()}

        def naive(raw):   # 1 文字ずつ別々に正規化したときの答え（文脈で変わるかどうかの目安）
            return "".join(single_chars.get(ord(c), c) for c in raw)

        small = {}
        for name, rows in cases.items():
            if name == "edge":
                small[name] = rows
                continue
            interesting = [r for r in rows if r[1] != naive(r[0])]   # 文脈（書記素・複数文字の規則）で答えが変わる例
            rng.shuffle(interesting)
            boring = [r for r in rows if r[1] == naive(r[0])]
            rng.shuffle(boring)
            k = args.small_random if name in ("random", "triples") else args.small_random // 2
            small[name] = interesting[: args.small_max_interesting] + boring[:k]
            print(f"軽い版 {name}：文脈で変わる例 {min(len(interesting), args.small_max_interesting):,}／全 {len(interesting):,} ＋ 他 {min(len(boring), k):,}", flush=True)
        open(os.path.join(args.small, "charsmap.b64"), "w", encoding="ascii").write(b64)
        dump(os.path.join(args.small, "norm_single.json"), {"info": info, "diff": diff})
        dump(os.path.join(args.small, "norm_cases.json"), {"info": dict(info, small=True), "groups": small})
        print("軽い版：", args.small, flush=True)
    return 1 if mismatch_full else 0


if __name__ == "__main__":
    sys.exit(main())
