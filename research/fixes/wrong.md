# 言い切って誤った列：どの段から出たか（`research/fixes/wrong.py`）

## 決める陣（誤り 127、うち重大 1）

| 出どころ | 列 | 重大 |
|---|---:|---:|
| 本体の答えがそのまま通った | 119 | 1 |
| rho（不明を候補に戻した） | 7 | 0 |
| recheck が不明から戻した（recheck:cue_id） | 1 | 0 |

| 正解 → 答え | 列 |
|---|---:|
| text → category | 15 |
| id → category | 14 |
| quantity → category | 13 |
| address → id | 12 |
| org → account | 9 |
| category → text | 8 |
| address → category | 8 |
| category → account | 8 |
| category → id | 6 |
| org → category | 6 |
| account → category | 5 |
| id → org | 4 |
| address → org | 3 |
| category → product | 2 |
| account → text | 2 |

## 確かめる陣（誤り 57、うち重大 1）

| 出どころ | 列 | 重大 |
|---|---:|---:|
| 本体の答えがそのまま通った | 56 | 0 |
| rho（不明を候補に戻した） | 1 | 1 |

| 正解 → 答え | 列 |
|---|---:|
| quantity → category | 10 |
| text → category | 9 |
| category → text | 5 |
| account → category | 5 |
| id → category | 3 |
| category → account | 3 |
| org → address | 3 |
| category → address | 3 |
| text → account | 3 |
| address → category | 2 |
| category → org | 2 |
| org → category | 2 |
| category → tax_class | 1 |
| address → text | 1 |
| org → account | 1 |

