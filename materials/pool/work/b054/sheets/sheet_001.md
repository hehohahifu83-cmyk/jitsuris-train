# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：STATISTIC
- 例1 値：MIDWIVES | MIDWIVES | MIDWIVES | MIDWIVES | MIDWIVES
  - 同じ表の列：Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE, FLAG

## g0002（1 列）
- 見出し：Statistic Label
- 例1 値：Midwives | Midwives | Midwives | Midwives | Midwives
  - 同じ表の列：STATISTIC, YEAR, Year, MEASURE, Measure, UNIT, VALUE, FLAG

## g0003（2 列）
- 見出し：YEAR
- 例1 値：2018 | 2022 | 2019 | 2024 | 2022
  - 同じ表の列：STATISTIC, Statistic Label, Year, MEASURE, Measure, UNIT, VALUE, FLAG
- 例2 値：2021 | 2020 | 2021 | 2019 | 2023
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, MEASURE, Measure, UNIT, VALUE, FLAG

## g0004（1 列）
- 見出し：MEASURE
- 例1 値：PRACMID | LICENSEMID | LICENSEMID | LICENSEMID | LICENSEMID
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Measure, UNIT, VALUE, FLAG

## g0005（1 列）
- 見出し：Measure
- 例1 値：Midwives licensed to practice | Practising midwives | Practising midwives | Midwives licensed to practice | Midwives licensed to practice
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, UNIT, VALUE, FLAG

## g0006（1 列）
- 見出し：UNIT
- 例1 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, VALUE, FLAG

## g0007（1 列）
- 見出し：VALUE
- 例1 値：10645 | 10663 | 9398 | 10518 | 4210
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, FLAG

## g0008（1 列）
- 見出し：FLAG
- 例1 値：M | D | D | D | D
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE

## g0009（1 列）
- 見出し：Flag
- 例1 値：Missing | Deviation from definition | Deviation from definition | Deviation from definition | Deviation from definition
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE

## g0010（1 列）
- 見出し：unsafe_
- 例1 値：MCCANN FITZGERALD | RONAN DALY JERMYN CORK | iii) Some expenditure may be excluded i… | ii) Legal Advisory fees, while paid by … | FEXCO ASSET FINANCE LTD
  - 同じ表の列：unsafe__2, unsafe__3

## g0011（1 列）
- 見出し：unsafe__2
- 例1 値：Facility professional fees - legal serv… | Facility professional fees - legal serv… | Description | Loan administration services
  - 同じ表の列：unsafe_, unsafe__3

## g0012（1 列）
- 見出し：unsafe__3
- 例1 値：€135,090 | €123,845 | Payment Amount € | €20,836
  - 同じ表の列：unsafe_, unsafe__2

## g0013（1 列）
- 見出し：unsafe_
- 例1 値：Byrne Wallace | iii) Some expenditure may be excluded i… | Supplier | Aon Risk Solutions | Ronan Daky Jermyn
  - 同じ表の列：unsafe__2, unsafe__3

## g0014（1 列）
- 見出し：unsafe__2
- 例1 値：Description | Facility Professional Fees | Other Advisory | Facility Professional Fees | Insurance
  - 同じ表の列：unsafe_, unsafe__3

## g0015（1 列）
- 見出し：unsafe__3
- 例1 値：Payment Amount € | 162,759.36 | 44,950.00 | 35,000.00 | 83,826.30
  - 同じ表の列：unsafe_, unsafe__2

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
g0008	
g0009	
g0010	
g0011	
g0012	
g0013	
g0014	
g0015	
```
