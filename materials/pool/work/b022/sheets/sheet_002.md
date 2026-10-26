# ラベル用シート 002 / 002

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Greenspace per capita msq
- 例1 値：353.3558118 | 94.01853102 | 302.1454304 | 116.4694557 | 112.4050668
  - 同じ表の列：City, Percent of populati…

## g0122（1 列）
- 見出し：Disease outcome
- 例1 値：Coronary heart disease | Chronic obstructive pulmonary diseases | Stroke | Lung cancer | Lower respiratory infections
  - 同じ表の列：Percentage of deaths

## g0123（1 列）
- 見出し：Percentage of deaths
- 例1 値：70.3 | 25.9 | 0 | 1.4 | 2.4
  - 同じ表の列：Disease outcome

## g0124（1 列）
- 見出し：Service_Area_Identifier
- 例1 値：PMJG | FIFA | ALAM | WTRK | BRKS
  - 同じ表の列：Latlong, ID, Anticipatory Notice…, Date Completed, Estate Complete

## g0125（1 列）
- 見出し：Latlong
- 例1 値：-38.1114577,145.3582537 | -27.699255,152.844518 | -33.903740, 151.207080 | -37.8436784,144.6345907 | -32.2806771,115.9747554
  - 同じ表の列：Service_Area_Identi…, ID, Anticipatory Notice…, Date Completed, Estate Complete

## g0126（1 列）
- 見出し：ID
- 例1 値：884 | 442 | 130 | 225 | 789
  - 同じ表の列：Service_Area_Identi…, Latlong, Anticipatory Notice…, Date Completed, Estate Complete

## g0127（1 列）
- 見出し：Anticipatory Notice Reference Date
- 例1 値：2024-10-15 00:00:00 | 2025-06-10 00:00:00 | 2025-01-22 00:00:00 | 2024-10-28 00:00:00 | 2024-10-28 00:00:00
  - 同じ表の列：Service_Area_Identi…, Latlong, ID, Date Completed, Estate Complete

## g0128（1 列）
- 見出し：Date Completed
- 例1 値：2026-08-25 00:00:00 | 2026-08-27 00:00:00 | 2026-08-24 00:00:00 | 2026-08-28 00:00:00 | 2026-08-26 00:00:00
  - 同じ表の列：Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Estate Complete

## g0129（1 列）
- 見出し：Estate Complete
- 例1 値：N | N | N | Y | N
  - 同じ表の列：Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Date Completed

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
```
