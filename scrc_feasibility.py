"""SCRC-I を参考にした 1 パラメータの選択的リスク制御：境界と、固定前の標本数の見積り（2026-11-04 Claude）。

ChatGPT の見直し（ai-bridge messages/20261101-2138_chatgpt-to-claude_scrc-review.md）に合わせた定義：
  S_τ = 1[数の種類どうしの 1 位と 2 位の差 ≥ τ]（受け入れ）
  q(τ) = E[S_τ]（受け入れの割合）、N(τ) = E[S_τ × 重大]（受け入れて重大になる割合）
  条件付きの重大リスク R(τ) = N(τ) / q(τ)
  固定した K 個の候補の全部に同時に有効な q_LCB(τ) と N_UCB(τ) を作り、N_UCB(τ) ≤ α·q_LCB(τ) を満たす候補のうち
  受け入れがいちばん多いもの（いちばん小さい τ）を選ぶ。どれも満たさなければ「候補なし・変更なし」。
  このとき、較正の陣について確率 1−δ 以上で、選んだ τ の R(τ) ≤ α（独立・同分布の単位の仮定の下）。

δ は 2 つに分ける：δ_q（q の下限）＋ δ_N（N の上限）＝ δ。
  q_LCB：S_τ は τ について単調なので、片側 DKW で全候補に同時に q̂(τ) − √(ln(1/δ_q)/(2n))。
  N_UCB：候補ごとに Bonferroni（δ_N/K）。境界は 2 種類を出す：
    hoeffding … N̂ + √(ln(K/δ_N)/(2n))（ChatGPT の例の形。0/1 の損失ではとても緩い）
    binomial  … S_τ×重大 は 0/1 なので、Clopper–Pearson の片側上限（水準 δ_N/K）。こちらを本命にする。
単位（n）は独立な単位の数。列は同じ表の中で独立でないので、表ごとに 1 列（事前に決めた種で選ぶ）を単位にする。

  python scrc_feasibility.py                    → 見積りの表（α・δ・K・q・重大の数ごとに要る n）
  python scrc_feasibility.py --n 2223 --q 0.9   → その n での判定
"""
from __future__ import annotations

import argparse
import math


def _log_binom_cdf(k: int, n: int, p: float) -> float:
    """log P(X ≤ k)、X ~ Bin(n, p)。"""
    if p <= 0.0:
        return 0.0
    if p >= 1.0:
        return 0.0 if k >= n else -math.inf
    lp, lq = math.log(p), math.log1p(-p)
    terms = [math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1) + i * lp + (n - i) * lq for i in range(0, min(k, n) + 1)]
    m = max(terms)
    return m + math.log(sum(math.exp(t - m) for t in terms))


def cp_upper(k: int, n: int, level: float) -> float:
    """Clopper–Pearson の片側上限：P(X ≤ k | p) = level となる p（k 回 / n 回、外れの確率 level）。"""
    if n <= 0:
        return 1.0
    if k >= n:
        return 1.0
    if k == 0:
        return 1.0 - level ** (1.0 / n)
    lo, hi, target = k / n, 1.0, math.log(level)
    for _ in range(60):
        mid = (lo + hi) / 2
        if _log_binom_cdf(k, n, mid) > target:
            lo = mid
        else:
            hi = mid
    return hi


def dkw_eps(n: int, delta_q: float) -> float:
    return math.sqrt(math.log(1.0 / delta_q) / (2 * n))


def hoeffding_eps(n: int, K: int, delta_n: float) -> float:
    return math.sqrt(math.log(K / delta_n) / (2 * n))


def passes(n: int, accepted: int, severe: int, alpha: float, delta: float, K: int, bound: str = "binomial") -> tuple[bool, float, float]:
    """1 つの候補 τ の判定。戻り値（通るか, N_UCB, α·q_LCB）。accepted＝受け入れた単位数、severe＝受け入れて重大の単位数。"""
    dq = dn = delta / 2
    q_lcb = max(0.0, accepted / n - dkw_eps(n, dq))
    if bound == "hoeffding":
        n_ucb = severe / n + hoeffding_eps(n, K, dn)
    else:
        n_ucb = cp_upper(severe, n, dn / K)
    return n_ucb <= alpha * q_lcb, n_ucb, alpha * q_lcb


def select(n: int, table: list[tuple[float, int, int]], alpha: float, delta: float, bound: str = "binomial"):
    """table＝[(τ, 受け入れ数, 重大数)]（固定した候補の全部）。通る候補のうち受け入れ最大（同じなら小さい τ）。無ければ None。"""
    K = len(table)
    ok = [(acc, -tau, tau) for tau, acc, sev in table if passes(n, acc, sev, alpha, delta, K, bound)[0]]
    return max(ok)[2] if ok else None


def scan_n(alpha: float, delta: float, K: int, q: float, severe_rate: float = 0.0, bound: str = "binomial", cap: int = 20_000):
    """n を 1 から cap まで全部調べる（2026-11-04：二分探索は round・floor の段差で通る／通らないが単調でないため、ChatGPT の指摘で置き換えた）。
    戻り値 (first, stable)：first＝最初に通る n、stable＝それ以降 cap まで全部通る最小の n（保守的な見積り）。届かなければ None。"""
    first, last_fail = None, 0
    for n in range(1, cap + 1):
        if passes(n, round(q * n), math.floor(severe_rate * n), alpha, delta, K, bound)[0]:
            if first is None:
                first = n
        else:
            last_fail = n
    stable = last_fail + 1 if last_fail < cap else None
    return first, stable


def min_n(alpha: float, delta: float, K: int, q: float, severe_rate: float = 0.0, bound: str = "binomial", cap: int = 20_000) -> int | None:
    """保守的な見積り：それ以上の n（cap まで）で必ず通る最小の n。"""
    return scan_n(alpha, delta, K, q, severe_rate, bound, cap)[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int)
    ap.add_argument("--q", type=float, default=0.9)
    ap.add_argument("--severe", type=int, default=0)
    ap.add_argument("--alpha", type=float, default=0.005)
    ap.add_argument("--delta", type=float, default=0.05)
    ap.add_argument("--K", type=int, default=51)
    a = ap.parse_args()
    if a.n:
        for b in ("hoeffding", "binomial"):
            ok, u, r = passes(a.n, round(a.q * a.n), a.severe, a.alpha, a.delta, a.K, b)
            print(f"{b:9s} n={a.n} q={a.q} 重大={a.severe}: N_UCB={u:.5f}  α·q_LCB={r:.5f}  → {'通る' if ok else '通らない'}")
        return
    print("| α | δ | K | q | 受け入れて重大の割合 | binomial 最初に通る n | binomial 以後ずっと通る n | hoeffding 最初 | hoeffding 以後ずっと |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for alpha in (0.005, 0.01, 0.02, 0.05):
        for sr in (0.0, alpha / 4):
            bf, bs = scan_n(alpha, a.delta, a.K, a.q, sr, "binomial", 20_000)
            hf, hs = scan_n(alpha, a.delta, a.K, a.q, sr, "hoeffding", 500_000)
            f = lambda v: v if v else "届かない"
            print(f"| {alpha} | {a.delta} | {a.K} | {a.q} | {sr:.5f} | {f(bf)} | {f(bs)} | {f(hf)} | {f(hs)} |")

if __name__ == "__main__":
    main()
