<!-- b080：10/27 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b080.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Status
- 例1 値：Active | Expired | Active | Active | Active
  - 同じ表の列：Ref. Number, TIF District, Designation Date, Designation Year, End Date, Final Year, Blighting Factors, Conservation Factors

## g0002（1 列）
- 見出し：Ref. Number
- 例1 値：T-111 | T-077 | T-014 | T-093 | T-038
  - 同じ表の列：Status, TIF District, Designation Date, Designation Year, End Date, Final Year, Blighting Factors, Conservation Factors

## g0007（1 列）
- 見出し：Final Year
- 例1 値：2026 | 2040 | 2024 | 2028 | 2023
  - 同じ表の列：Status, Ref. Number, TIF District, Designation Date, Designation Year, End Date, Blighting Factors, Conservation Factors

## g0011（1 列）
- 見出し：Fund
- 例1 値：3090 | 3090 | 3090 | 3090 | 3090
  - 同じ表の列：Category, Organization Level …, Dept, Org, AU, Project #, Actual 2007-08, Actual 2008-09

## g0015（1 列）
- 見出し：AU
- 例1 値：A | A | B | A | B
  - 同じ表の列：Category, Fund, Organization Level …, Dept, Org, Project #, Actual 2007-08, Actual 2008-09

## g0016（1 列）
- 見出し：Project #
- 例1 値：89005409 | 89020107 | 89060081 | 70091306 | 82000135
  - 同じ表の列：Category, Fund, Organization Level …, Dept, Org, AU, Actual 2007-08, Actual 2008-09

## g0020（1 列）
- 見出し：Series
- 例1 値：003100 | 000600 | 003200 | 002400 | 200000
  - 同じ表の列：Class Code, Budget Level, Salary Schedule, FLSA Status

## g0022（1 列）
- 見出し：Budget Level
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Series, Class Code, Salary Schedule, FLSA Status

## g0024（1 列）
- 見出し：FLSA Status
- 例1 値：EX | NEX | EX | EX | NEX
  - 同じ表の列：Series, Class Code, Budget Level, Salary Schedule

## g0026（1 列）
- 見出し：Requesting/Relevant Department
- 例1 値：Health & Human Services | Technology Enterprise Business Solutions | Environmental Protection & Housing and … | Fire & Rescue and Sheriff's Office | Health & Human Services
  - 同じ表の列：Date, Number

## 答えの雛形

```
g0001	
g0002	
g0007	
g0011	
g0015	
g0016	
g0020	
g0022	
g0024	
g0026	
```
