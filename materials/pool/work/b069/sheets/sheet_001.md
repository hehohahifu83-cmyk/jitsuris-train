# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Obs
- 例1 値：740 | 526 | 589 | 48 | 133
  - 同じ表の列：Data_Vintage, Publication_Month, Publication_Year, Controlling_Sub_Sec…, GOV_Dept_LA, Entity, Parent, NACE_Code

## g0002（1 列）
- 見出し：Data_Vintage
- 例1 値：2022 | 2022 | 2022 | 2022 | 2022
  - 同じ表の列：Obs, Publication_Month, Publication_Year, Controlling_Sub_Sec…, GOV_Dept_LA, Entity, Parent, NACE_Code

## g0003（1 列）
- 見出し：Publication_Month
- 例1 値：April | April | April | April | April
  - 同じ表の列：Obs, Data_Vintage, Publication_Year, Controlling_Sub_Sec…, GOV_Dept_LA, Entity, Parent, NACE_Code

## g0004（1 列）
- 見出し：Publication_Year
- 例1 値：2023 | 2023 | 2023 | 2023 | 2023
  - 同じ表の列：Obs, Data_Vintage, Publication_Month, Controlling_Sub_Sec…, GOV_Dept_LA, Entity, Parent, NACE_Code

## g0005（1 列）
- 見出し：Controlling_Sub_Sector
- 例1 値：S1311 | S1311 | S1311 | S1313 | S1311
  - 同じ表の列：Obs, Data_Vintage, Publication_Month, Publication_Year, GOV_Dept_LA, Entity, Parent, NACE_Code

## g0006（1 列）
- 見出し：GOV_Dept_LA
- 例1 値：Department of Environment, Climate and … | Department of Health | Department of Environment, Climate and … | Wicklow County Council | Sligo County Council
  - 同じ表の列：Obs, Data_Vintage, Publication_Month, Publication_Year, Controlling_Sub_Sec…, Entity, Parent, NACE_Code

## g0007（1 列）
- 見出し：Entity
- 例1 値：Kilkenny County Council | St Vincents Hospital Fairview | Post.Trust Ltd | Valuation Office | Dogpatch Labs Management DAC
  - 同じ表の列：Obs, Data_Vintage, Publication_Month, Publication_Year, Controlling_Sub_Sec…, GOV_Dept_LA, Parent, NACE_Code

## g0008（1 列）
- 見出し：Parent
- 例1 値：NTMA | Electricity Supply Board | Electricity Supply Board | Permanent TSB Group Holdings PLC | Ervia
  - 同じ表の列：Obs, Data_Vintage, Publication_Month, Publication_Year, Controlling_Sub_Sec…, GOV_Dept_LA, Entity, NACE_Code

## g0009（1 列）
- 見出し：NACE_Code
- 例1 値：L6820 | L6820 | K6411 | F4110 | H5223
  - 同じ表の列：Obs, Data_Vintage, Publication_Month, Publication_Year, Controlling_Sub_Sec…, GOV_Dept_LA, Entity, Parent

## g0010（1 列）
- 見出し：Obs
- 例1 値：200.0 | 572.0 | 92.0 | 577.0 | 293.0
  - 同じ表の列：Data Vintage, Publication Month, Publication Year, Sub Sector, Government Departme…, NACE Code

## g0011（1 列）
- 見出し：Data Vintage
- 例1 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：Obs, Publication Month, Publication Year, Sub Sector, Government Departme…, NACE Code

## g0012（1 列）
- 見出し：Publication Month
- 例1 値：April | April | April | April | April
  - 同じ表の列：Obs, Data Vintage, Publication Year, Sub Sector, Government Departme…, NACE Code

## g0013（1 列）
- 見出し：Publication Year
- 例1 値：2022 | 2022 | 2022 | 2022 | 2022
  - 同じ表の列：Obs, Data Vintage, Publication Month, Sub Sector, Government Departme…, NACE Code

## g0014（1 列）
- 見出し：Sub Sector
- 例1 値：S1311 | S1311 | S1311 | S1313 | S11001
  - 同じ表の列：Obs, Data Vintage, Publication Month, Publication Year, Government Departme…, NACE Code

## g0015（1 列）
- 見出し：Government Department/Local Authority
- 例1 値：Department of Finance | Department of Environment, Climate and … | Donegal County Council | Dublin City Council | Department of Education
  - 同じ表の列：Obs, Data Vintage, Publication Month, Publication Year, Sub Sector, NACE Code

## g0016（1 列）
- 見出し：NACE Code
- 例1 値：O8411 | H4939 | L6820 | D3522 | L6820
  - 同じ表の列：Obs, Data Vintage, Publication Month, Publication Year, Sub Sector, Government Departme…

## g0017（1 列）
- 見出し：STATISTIC CODE
- 例1 値：ISQ02 | ISQ02 | ISQ02 | ISQ02 | ISQ02
  - 同じ表の列：STATISTIC, TLIST(Q1), Quarter, C02422V02925, Assets and Liabilit…, C02419V02922, C02418V02921, Institutional Sector

## g0018（1 列）
- 見出し：STATISTIC
- 例1 値：Quarterly Accounts | Quarterly Accounts | Quarterly Accounts | Quarterly Accounts | Quarterly Accounts
  - 同じ表の列：STATISTIC CODE, TLIST(Q1), Quarter, C02422V02925, Assets and Liabilit…, C02419V02922, C02418V02921, Institutional Sector

## g0019（1 列）
- 見出し：TLIST(Q1)
- 例1 値：20001 | 19991 | 19993 | 19991 | 19991
  - 同じ表の列：STATISTIC CODE, STATISTIC, Quarter, C02422V02925, Assets and Liabilit…, C02419V02922, C02418V02921, Institutional Sector

## g0020（1 列）
- 見出し：Quarter
- 例1 値：1999Q4 | 1999Q4 | 1999Q2 | 1999Q1 | 1999Q2
  - 同じ表の列：STATISTIC CODE, STATISTIC, TLIST(Q1), C02422V02925, Assets and Liabilit…, C02419V02922, C02418V02921, Institutional Sector

## g0021（1 列）
- 見出し：C02422V02925
- 例1 値：1 | 2 | 1 | 2 | 2
  - 同じ表の列：STATISTIC CODE, STATISTIC, TLIST(Q1), Quarter, Assets and Liabilit…, C02419V02922, C02418V02921, Institutional Sector

## g0022（1 列）
- 見出し：Assets and Liabilities
- 例1 値：Changes in assets | Changes in liabilities and net worth | Changes in liabilities and net worth | Changes in liabilities and net worth | Changes in assets
  - 同じ表の列：STATISTIC CODE, STATISTIC, TLIST(Q1), Quarter, C02422V02925, C02419V02922, C02418V02921, Institutional Sector

## g0023（1 列）
- 見出し：C02419V02922
- 例1 値：15 | 6 | 19 | 31 | 3
  - 同じ表の列：STATISTIC CODE, STATISTIC, TLIST(Q1), Quarter, C02422V02925, Assets and Liabilit…, C02418V02921, Institutional Sector

## g0024（1 列）
- 見出し：C02418V02921
- 例1 値：6 | 6 | 1 | 1 | 7
  - 同じ表の列：STATISTIC CODE, STATISTIC, TLIST(Q1), Quarter, C02422V02925, Assets and Liabilit…, C02419V02922, Institutional Sector

## g0025（1 列）
- 見出し：Institutional Sector
- 例1 値：Non-financial corporations (S.11) | All sectors (S.1+S.2) | General government (S.13) | Rest of World (S.2) | Households including NPISH (S.14+S.15)
  - 同じ表の列：STATISTIC CODE, STATISTIC, TLIST(Q1), Quarter, C02422V02925, Assets and Liabilit…, C02419V02922, C02418V02921

## g0026（1 列）
- 見出し：UNIT
- 例1 値：Euro Million | Euro Million | Euro Million | Euro Million | Euro Million
  - 同じ表の列：STATISTIC CODE, STATISTIC, TLIST(Q1), Quarter, C02422V02925, Assets and Liabilit…, C02419V02922, C02418V02921

## g0027（1 列）
- 見出し：Sampling_Year
- 例1 値：2021 | 2020 | 2021 | 2019 | 2017
  - 同じ表の列：Sampling_Month, Source_Country, Test_Result, Total

## g0028（1 列）
- 見出し：Sampling_Month
- 例1 値：Feb | Feb | Aug | Jun | Jan
  - 同じ表の列：Sampling_Year, Source_Country, Test_Result, Total

## g0029（1 列）
- 見出し：Source_Country
- 例1 値：France | France | Austria | Italy | Denmark
  - 同じ表の列：Sampling_Year, Sampling_Month, Test_Result, Total

## g0030（1 列）
- 見出し：Test_Result
- 例1 値：Neg | Neg | Pos | Neg | Pos
  - 同じ表の列：Sampling_Year, Sampling_Month, Source_Country, Total

## g0031（1 列）
- 見出し：Total
- 例1 値：27 | 8 | 102 | 5 | 5
  - 同じ表の列：Sampling_Year, Sampling_Month, Source_Country, Test_Result

## g0032（1 列）
- 見出し：Year
- 例1 値：2014 | 2019 | 2013 | 2020 | 2012
  - 同じ表の列：DAFM Slaughter plan…, Disposal in LA Abat…, Exports, Farm to Farm, Marts, Calves Born by Sire…, Calves Born by Sire…, Calves Born by Sire…

## g0033（1 列）
- 見出し：DAFM Slaughter plants
- 例1 値：1785481 | 1745594 | 1687235 | 1400858 | 1642334
  - 同じ表の列：Year, Disposal in LA Abat…, Exports, Farm to Farm, Marts, Calves Born by Sire…, Calves Born by Sire…, Calves Born by Sire…

## g0034（1 列）
- 見出し：Disposal in LA Abattoirs
- 例1 値：102598 | 72935 | 100414 | 92639 | 106861
  - 同じ表の列：Year, DAFM Slaughter plan…, Exports, Farm to Farm, Marts, Calves Born by Sire…, Calves Born by Sire…, Calves Born by Sire…

## g0035（1 列）
- 見出し：Exports
- 例1 値：301563 | 188874 | 182482 | 215780 | 162038
  - 同じ表の列：Year, DAFM Slaughter plan…, Disposal in LA Abat…, Farm to Farm, Marts, Calves Born by Sire…, Calves Born by Sire…, Calves Born by Sire…

## g0036（1 列）
- 見出し：Farm to Farm
- 例1 値：1180950 | 1027286 | 1542362 | 1636447 | 1301334
  - 同じ表の列：Year, DAFM Slaughter plan…, Disposal in LA Abat…, Exports, Marts, Calves Born by Sire…, Calves Born by Sire…, Calves Born by Sire…

## g0037（1 列）
- 見出し：Marts
- 例1 値：1755803 | 1723498 | 1530690 | 1625660 | 1717558
  - 同じ表の列：Year, DAFM Slaughter plan…, Disposal in LA Abat…, Exports, Farm to Farm, Calves Born by Sire…, Calves Born by Sire…, Calves Born by Sire…

## g0038（1 列）
- 見出し：Calves Born by Sire Fresian
- 例1 値：809848 | 748093 | 762097 | 711812 | 732096
  - 同じ表の列：Year, DAFM Slaughter plan…, Disposal in LA Abat…, Exports, Farm to Farm, Marts, Calves Born by Sire…, Calves Born by Sire…

## g0039（1 列）
- 見出し：Calves Born by Sire Limousin
- 例1 値：427416 | 425924 | 395908 | 416706 | 382919
  - 同じ表の列：Year, DAFM Slaughter plan…, Disposal in LA Abat…, Exports, Farm to Farm, Marts, Calves Born by Sire…, Calves Born by Sire…

## g0040（1 列）
- 見出し：Calves Born by Sire Aberdeen Angus
- 例1 値：215535 | 238479 | 387488 | 346772 | 394690
  - 同じ表の列：Year, DAFM Slaughter plan…, Disposal in LA Abat…, Exports, Farm to Farm, Marts, Calves Born by Sire…, Calves Born by Sire…

## g0041（1 列）
- 見出し：Calves Born by Sire Charolais
- 例1 値：304694 | 362268 | 301349 | 357922 | 344389
  - 同じ表の列：Year, DAFM Slaughter plan…, Disposal in LA Abat…, Exports, Farm to Farm, Marts, Calves Born by Sire…, Calves Born by Sire…

## g0042（1 列）
- 見出し：Month
- 例1 値：No Parking Except Buses/Coaches Sign | Parking Tag - General | Other | Only a Technical Offence | Alleged Error by PEC
  - 同じ表の列：Number, %

## g0043（1 列）
- 見出し：Number
- 例1 値：112 | 1 | 1 | 15 | Table in the Report
  - 同じ表の列：Month, %

## g0044（1 列）
- 見出し：%
- 例1 値：0.17 | 3.7520391517128875E-2 | 5.872756933115824E-2 | 47 | 6.1191626409017714E-2
  - 同じ表の列：Month, Number

## g0045（1 列）
- 見出し：DateOfOffence
- 例1 値：2020-10-11T00:00:00 | 2021-07-17T00:00:00 | 2021-06-15T00:00:00 | 2020-09-03T00:00:00 | 2021-06-28T00:00:00
  - 同じ表の列：Issue_Date, Section_No

## g0046（1 列）
- 見出し：Issue_Date
- 例1 値：2021-11-24T00:00:00 | 2021-10-01T00:00:00 | 2021-12-10T00:00:00 | 2021-02-15T00:00:00 | 2021-11-24T00:00:00
  - 同じ表の列：DateOfOffence, Section_No

## g0047（1 列）
- 見出し：Section_No
- 例1 値：3.1 | 3.1 | 3.1 | 3.1 | 3.1
  - 同じ表の列：DateOfOffence, Issue_Date

## g0048（1 列）
- 見出し：AreaID
- 例1 値：23 | 16 | 22 | 4 | 12
  - 同じ表の列：AreaCode, RegionID, CoverageID, CoverageCode

## g0049（1 列）
- 見出し：AreaCode
- 例1 値：CKST | NAT | SLWC | DML | DNE
  - 同じ表の列：AreaID, RegionID, CoverageID, CoverageCode

## g0050（1 列）
- 見出し：RegionID
- 例1 値：20 | 21 | 20 | 20 | 21
  - 同じ表の列：AreaID, AreaCode, CoverageID, CoverageCode

## g0051（1 列）
- 見出し：CoverageID
- 例1 値：3 | 1 | 2 | 3 | 3
  - 同じ表の列：AreaID, AreaCode, RegionID, CoverageCode

## g0052（1 列）
- 見出し：CoverageCode
- 例1 値：A | A | A | A | A
  - 同じ表の列：AreaID, AreaCode, RegionID, CoverageID

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
g0016	
g0017	
g0018	
g0019	
g0020	
g0021	
g0022	
g0023	
g0024	
g0025	
g0026	
g0027	
g0028	
g0029	
g0030	
g0031	
g0032	
g0033	
g0034	
g0035	
g0036	
g0037	
g0038	
g0039	
g0040	
g0041	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0051	
g0052	
```
