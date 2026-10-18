"""長さ順の小さな束（マイクロバッチ）の計画と、詰め物（パディング）。torch には依存しない純粋な関数だけ。

目的：学習の結果（計算）を変えずに、GPU の無駄な計算を減らす。
- 実効バッチ（例：64 文）は今までどおり乱数で選ぶ。変えるのは「その 64 文を GPU に何回に分けて流すか」だけ。
- 64 文を長さ順に並べて小さな束に分けると、短い文に長い文の分の詰め物をしなくて済む。
- 損失は「束の文数 / 実効バッチの文数」で重みを付けて足すので、勾配は 64 文を一度に流したときと同じ（数値の丸め誤差を除く）。
"""
from __future__ import annotations


def plan_micro_batches(lengths, micro, longest_first=True):
    """実効バッチ内の文の長さ（トークン数）の並び → 小さな束の計画。

    返すのは「元の位置の番号」の並びのリスト。全員がちょうど 1 回ずつ入る。
    longest_first=True なら最も長い束が先に来る（GPU のメモリの最大値を最初に使い、後からの不足を防ぐ）。
    """
    if micro < 1:
        raise ValueError("micro must be a positive integer")
    order = sorted(range(len(lengths)), key=lambda i: (lengths[i], i), reverse=longest_first)
    return [order[s:s + micro] for s in range(0, len(order), micro)]


def pad_batch(seqs, pad_id, multiple=1):
    """トークン番号の並びのリスト → (input_ids, attention_mask)。右側を pad_id で埋める。

    multiple が 2 以上なら、幅をその倍数に切り上げる（GPU の fp16 の計算が速い形にする）。
    """
    if not seqs:
        raise ValueError("seqs must not be empty")
    width = max(len(s) for s in seqs)
    if multiple and multiple > 1:
        width = -(-width // multiple) * multiple
    ids = [list(s) + [pad_id] * (width - len(s)) for s in seqs]
    mask = [[1] * len(s) + [0] * (width - len(s)) for s in seqs]
    return ids, mask


def micro_weights(plan):
    """各束の損失の重み（束の文数 / 実効バッチの文数）。合計は 1。"""
    n = sum(len(p) for p in plan)
    return [len(p) / n for p in plan]


def padded_tokens(lengths, plan, multiple=1):
    """計画どおりに流したときに GPU が計算するトークン数（詰め物を含む）。"""
    total = 0
    for p in plan:
        width = max(lengths[i] for i in p)
        if multiple and multiple > 1:
            width = -(-width // multiple) * multiple
        total += width * len(p)
    return total
