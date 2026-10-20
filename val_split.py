"""検証用の分け方（2026-10-20）。学習率などを選ぶときに、固定の試験（開発用220・一般・業務・業務2・調達）に触れないための分け方。

背景：ChatGPT からの依頼（mmBERT-small への切り替え）で『ハイパーパラメータを調べるなら、学習に使わない検証だけで、両方に同じ予算で』と決まった。
固定の試験で学習率を選ぶと、試験に合わせた選び方になり、最終の判定に使えなくなる。

やり方：本物の表の『学習側』（すでに表ごとに 8:2 で試験側と分けた残りの 8 割）を、さらに表ごとに 1/8 だけ検証に回す。
- 試験側の表（exp7.split の 2 割）は一切使わない。
- 表の名前に塩（VAL_SALT）を付けた md5 で決めるので、毎回同じ分け方になり、exp7.split の分け方とは独立。
- 検証に回した表の行は、学習の行（水増しした行も含む）に入らない。
この検証は『学習と同じ公開表の集まりの中の、見ていない表』であり、独立した新しい出どころの試験ではない。最終の判定には使わない（モデルや学習率の選択だけに使う）。
未見セット（blind_set*）は読まない。
"""
from __future__ import annotations

import hashlib

VAL_SALT = "jitsuris-val-v1"
VAL_MOD = 8          # 8 つに 1 つの表を検証に回す
VAL_PREFIX = "検証"  # 試験の名前の頭（finetune_exp.safe_test_name がこの名前を英字の名前にする）


def is_val_table(table, salt=VAL_SALT, mod=VAL_MOD):
    return int(hashlib.md5(f"{salt}:{table}".encode("utf-8")).hexdigest(), 16) % mod == 0


def split_val(rows, salt=VAL_SALT, mod=VAL_MOD):
    """本物の行 (見出し, 値, ラベル, 文脈, 表の名前) を、表の名前で（学習側, 検証側）に分ける。"""
    train, val = [], []
    for r in rows:
        (val if is_val_table(r[4], salt, mod) else train).append(r)
    return train, val


def tables_of(rows):
    return {r[4] for r in rows}
