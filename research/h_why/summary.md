# 直し G のあとに残る不明・誤り（`research/h_why/analyze.py`。使い済みの陣、探索用）

| 陣 | 採点（3 本） | 正しい | 不明 | 重大 | ほか |
|---|---:|---:|---:|---:|---:|
| E1 | 3645 | 3214 | 282 | 9 | 140 |
| E2 | 3759 | 3399 | 203 | 1 | 156 |
| decide | 3621 | 3239 | 209 | 4 | 169 |
| confirm | 3741 | 3228 | 278 | 18 | 217 |

## 不明の理由（3 本・4 陣の合計。本体の 1 位が正解だった数）

| 理由 | 不明 | うち本体の 1 位が正解 |
|---|---:|---:|
| None | 339 | 3 |
| low_confidence_no_cue | 300 | 178 |
| verifier | 131 | 92 |
| amount_without_cue | 79 | 59 |
| period_header_no_unit | 45 | 27 |
| cue_conflict | 42 | 24 |
| rate_without_cue | 18 | 14 |
| amount_precision | 18 | 18 |

## 誤り（正解 → 答え）

| 正解 → 答え | 出力 |
|---|---:|
| category → id | 144 |
| address → org | 140 |
| id → category | 57 |
| address → category | 39 |
| category → text | 35 |
| category → address | 29 |
| text → category | 25 |
| quantity → category | 25 |
| category → quantity | 22 |
| account → category | 19 |
| org → category | 17 |
| org → account | 17 |
| org → address | 16 |
| category → account | 15 |
| account → org | 14 |
| id → address | 12 |
| product → category | 9 |
| id → quantity | 8 |
| amount → quantity | 6 |
| date → category | 6 |
| id → org | 6 |
| category → org | 5 |
| address → id | 5 |
| quantity → id | 5 |
| quantity → amount | 4 |
