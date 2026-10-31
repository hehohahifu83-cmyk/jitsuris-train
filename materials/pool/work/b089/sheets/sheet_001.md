# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Month/Year
- 例1 値：2020-04-01T00:00:00.000 | 2024-05-01T00:00:00.000 | 2020-10-01T00:00:00.000 | 2025-06-01T00:00:00.000 | 2020-06-01T00:00:00.000
  - 同じ表の列：Facilities, Fleet, Total

## g0002（1 列）
- 見出し：Facilities
- 例1 値：4597 | 6011 | 3856 | 4007 | 4820
  - 同じ表の列：Month/Year, Fleet, Total

## g0003（1 列）
- 見出し：Fleet
- 例1 値：2433 | 3491 | 3803 | 4861 | 4277
  - 同じ表の列：Month/Year, Facilities, Total

## g0004（1 列）
- 見出し：Total
- 例1 値：10764 | 8477 | 9613 | 11214 | 9913
  - 同じ表の列：Month/Year, Facilities, Fleet

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
```
