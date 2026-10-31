<!-- b069：10/52 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b069.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0003（1 列）
- 見出し：Publication_Month
- 例1 値：April | April | April | April | April
  - 同じ表の列：Obs, Data_Vintage, Publication_Year, Controlling_Sub_Sec…, GOV_Dept_LA, Entity, Parent, NACE_Code

## g0009（1 列）
- 見出し：NACE_Code
- 例1 値：L6820 | L6820 | K6411 | F4110 | H5223
  - 同じ表の列：Obs, Data_Vintage, Publication_Month, Publication_Year, Controlling_Sub_Sec…, GOV_Dept_LA, Entity, Parent

## g0011（1 列）
- 見出し：Data Vintage
- 例1 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：Obs, Publication Month, Publication Year, Sub Sector, Government Departme…, NACE Code

## g0014（1 列）
- 見出し：Sub Sector
- 例1 値：S1311 | S1311 | S1311 | S1313 | S11001
  - 同じ表の列：Obs, Data Vintage, Publication Month, Publication Year, Government Departme…, NACE Code

## g0015（1 列）
- 見出し：Government Department/Local Authority
- 例1 値：Department of Finance | Department of Environment, Climate and … | Donegal County Council | Dublin City Council | Department of Education
  - 同じ表の列：Obs, Data Vintage, Publication Month, Publication Year, Sub Sector, NACE Code

## g0019（1 列）
- 見出し：TLIST(Q1)
- 例1 値：20001 | 19991 | 19993 | 19991 | 19991
  - 同じ表の列：STATISTIC CODE, STATISTIC, Quarter, C02422V02925, Assets and Liabilit…, C02419V02922, C02418V02921, Institutional Sector

## g0029（1 列）
- 見出し：Source_Country
- 例1 値：France | France | Austria | Italy | Denmark
  - 同じ表の列：Sampling_Year, Sampling_Month, Test_Result, Total

## g0037（1 列）
- 見出し：Marts
- 例1 値：1755803 | 1723498 | 1530690 | 1625660 | 1717558
  - 同じ表の列：Year, DAFM Slaughter plan…, Disposal in LA Abat…, Exports, Farm to Farm, Calves Born by Sire…, Calves Born by Sire…, Calves Born by Sire…

## g0038（1 列）
- 見出し：Calves Born by Sire Fresian
- 例1 値：809848 | 748093 | 762097 | 711812 | 732096
  - 同じ表の列：Year, DAFM Slaughter plan…, Disposal in LA Abat…, Exports, Farm to Farm, Marts, Calves Born by Sire…, Calves Born by Sire…

## g0043（1 列）
- 見出し：Number
- 例1 値：112 | 1 | 1 | 15 | Table in the Report
  - 同じ表の列：Month, %

## 答えの雛形

```
g0003	
g0009	
g0011	
g0014	
g0015	
g0019	
g0029	
g0037	
g0038	
g0043	
```
