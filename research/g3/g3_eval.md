# G3 の 1 回だけの測り：直し M と銀教材（`research/g3/g3_eval.py`）

- 事前記録 `bench/fixm_prereg_20261112.md`・`bench/silver24_prereg_20261113.md`。採点 555 列（正解が unknown・S・other・person の列を除く）。環境 {'python': '3.12', 'sklearn': '1.8.0', 'numpy': '2.3.5', 'scipy': '1.17.0'}。
- 正解：先生 2 人の独立のラベル（互いに SHA だけを連絡）の裁定と Codex の見直し。SHA-256 1162b62032d580e59345f0ca44ed588d1e8d05a707fb0453d54adb380994bbeb。G3 は Alberta・Ontario・Berlin の金額・単位の語の表。

| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |
|---|---:|---:|---:|---:|---|
| L+G | 74.17% | 19.22% | 5 | 6.31% | 407・413・415 |
| L24+G | 74.17% | 19.40% | 4 | 6.19% | 410・416・409 |
| L24+G+M | 74.59% | 19.16% | 4 | 6.01% | 413・418・411 |
| L24S+G | 74.83% | 18.02% | 13 | 6.37% | 414・416・416 |
| L24+G+R | 74.17% | 19.52% | 4 | 6.07% | 410・416・409 |
| L24S+G+R | 74.83% | 18.20% | 13 | 6.19% | 414・416・416 |

## 主 1：直し M（L24+G+M 対 L24+G、表で引き直す）

- 1. 正しい +0.42 ×
- 2. 重大 +0 ○
- 3. ほかの誤り -0.18 ○
- 4. 90% 区間 +0.06〜+0.90 ○
- **判定：確かめられなかった**

## 主 2：銀教材（L24S+G 対 L24+G、公開元で引き直す）

- 1. 正しい +0.66 ○
- 2. 重大 +9 ×
- 3. ほかの誤り +0.18 ○
- 4. 90% 区間 -0.54〜+1.69 ×
- **判定：確かめられなかった（銀は使わないまま）**

## 読むだけ：rho の金額の守りを入れたとき（L24S+G+R 対 L24+G+R、公開元で引き直す）

- 正しいの差 +0.66、90% 区間 -0.54〜+1.69、重大の差 +9、ほかの誤りの差 +0.12

## 読むだけ：L24+G 対 L+G（公開元で引き直す）

- 正しいの差 +0.00、90% 区間 -0.67〜+0.62、重大の差 -1

## 読むだけ：正解の種類ごとの正しい・不明（3 本の合計）

| 正解 | 列 | 正しい L+G | 正しい L24+G | 正しい L24+G+M | 正しい L24S+G | 正しい L24+G+R | 正しい L24S+G+R | 不明 L+G | 不明 L24+G | 不明 L24+G+M | 不明 L24S+G | 不明 L24+G+R | 不明 L24S+G+R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| category | 96 | 261 | 261 | 261 | 264 | 261 | 264 | 10 | 12 | 12 | 9 | 12 | 9 |
| quantity | 94 | 223 | 220 | 221 | 221 | 220 | 221 | 58 | 58 | 57 | 54 | 58 | 54 |
| amount | 90 | 114 | 114 | 120 | 114 | 114 | 114 | 154 | 153 | 147 | 153 | 153 | 153 |
| date | 78 | 198 | 198 | 198 | 198 | 198 | 198 | 36 | 36 | 36 | 29 | 36 | 29 |
| address | 74 | 202 | 202 | 202 | 205 | 202 | 205 | 3 | 5 | 5 | 3 | 5 | 3 |
| id | 58 | 128 | 126 | 126 | 127 | 126 | 127 | 29 | 30 | 30 | 27 | 30 | 27 |
| text | 25 | 39 | 41 | 41 | 41 | 41 | 41 | 8 | 6 | 9 | 5 | 8 | 8 |
| org | 17 | 45 | 45 | 45 | 45 | 45 | 45 | 0 | 0 | 0 | 1 | 0 | 1 |
| rate | 12 | 15 | 14 | 14 | 17 | 14 | 17 | 21 | 22 | 22 | 19 | 22 | 19 |
| account | 10 | 7 | 11 | 11 | 11 | 11 | 11 | 1 | 1 | 1 | 0 | 1 | 0 |
| phone | 1 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |

## 読むだけ：重大の列（銀 × rho の守り、3 本）

| 形 | 本 | id | 列名 | 正解 | 答え | 理由 |
|---|---|---|---|---|---|---|
| L24+G | 1 | g3-0044 | Sample | id | quantity | None |
| L24+G | 1 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24+G | 2 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24+G | 3 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24S+G | 1 | g3-0167 | FS Rec'd | date | id | None |
| L24S+G | 1 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24S+G | 2 | g3-0163 | FIR Rec'd | date | id | None |
| L24S+G | 2 | g3-0165 | SIR Rec'd | date | id | None |
| L24S+G | 2 | g3-0167 | FS Rec'd | date | id | None |
| L24S+G | 2 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24S+G | 2 | g3-0520 | Range | id | date | None |
| L24S+G | 3 | g3-0044 | Sample | id | quantity | None |
| L24S+G | 3 | g3-0163 | FIR Rec'd | date | id | None |
| L24S+G | 3 | g3-0165 | SIR Rec'd | date | id | None |
| L24S+G | 3 | g3-0167 | FS Rec'd | date | id | None |
| L24S+G | 3 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24S+G | 3 | g3-0633 | WMU | id | quantity | None |
| L24+G+R | 1 | g3-0044 | Sample | id | quantity | None |
| L24+G+R | 1 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24+G+R | 2 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24+G+R | 3 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24S+G+R | 1 | g3-0167 | FS Rec'd | date | id | None |
| L24S+G+R | 1 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24S+G+R | 2 | g3-0163 | FIR Rec'd | date | id | None |
| L24S+G+R | 2 | g3-0165 | SIR Rec'd | date | id | None |
| L24S+G+R | 2 | g3-0167 | FS Rec'd | date | id | None |
| L24S+G+R | 2 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24S+G+R | 2 | g3-0520 | Range | id | date | None |
| L24S+G+R | 3 | g3-0044 | Sample | id | quantity | None |
| L24S+G+R | 3 | g3-0163 | FIR Rec'd | date | id | None |
| L24S+G+R | 3 | g3-0165 | SIR Rec'd | date | id | None |
| L24S+G+R | 3 | g3-0167 | FS Rec'd | date | id | None |
| L24S+G+R | 3 | g3-0339 | Retail Margin/Marge de détail | amount | rate | rate_without_cue |
| L24S+G+R | 3 | g3-0633 | WMU | id | quantity | None |

## 直し M が変えた列（3 本）

| 本 | id | 列名 | 正解 | L24+G | +M |
|---|---|---|---|---|---|
| 1 | g3-0069 | Patients | quantity | unknown | quantity |
| 1 | g3-0101 | Funding Status*
(Effective Date) | text | date | unknown |
| 1 | g3-0261 | Approved Funding | amount | unknown | amount |
| 1 | g3-0482 | Provincial Library Operating Grant | amount | unknown | amount |
| 2 | g3-0101 | Funding Status*
(Effective Date) | text | date | unknown |
| 2 | g3-0261 | Approved Funding | amount | unknown | amount |
| 2 | g3-0482 | Provincial Library Operating Grant | amount | unknown | amount |
| 3 | g3-0101 | Funding Status*
(Effective Date) | text | date | unknown |
| 3 | g3-0261 | Approved Funding | amount | unknown | amount |
| 3 | g3-0482 | Provincial Library Operating Grant | amount | unknown | amount |
