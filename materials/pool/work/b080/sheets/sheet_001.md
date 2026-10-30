# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Status
- 例1 値：Active | Expired | Active | Active | Active
  - 同じ表の列：Ref. Number, TIF District, Designation Date, Designation Year, End Date, Final Year, Blighting Factors, Conservation Factors

## g0002（1 列）
- 見出し：Ref. Number
- 例1 値：T-111 | T-077 | T-014 | T-093 | T-038
  - 同じ表の列：Status, TIF District, Designation Date, Designation Year, End Date, Final Year, Blighting Factors, Conservation Factors

## g0003（1 列）
- 見出し：TIF District
- 例1 値：Lawrence/Kedzie | Harlem Industrial Park Conservation Area | Ohio/Wabash | Englewood Mall | Irving/Cicero
  - 同じ表の列：Status, Ref. Number, Designation Date, Designation Year, End Date, Final Year, Blighting Factors, Conservation Factors

## g0004（1 列）
- 見出し：Designation Date
- 例1 値：1999-09-29T00:00:00.000 | 1998-02-05T00:00:00.000 | 2008-01-09T00:00:00.000 | 2000-02-16T00:00:00.000 | 2007-09-05T00:00:00.000
  - 同じ表の列：Status, Ref. Number, TIF District, Designation Year, End Date, Final Year, Blighting Factors, Conservation Factors

## g0005（1 列）
- 見出し：Designation Year
- 例1 値：1999 | 1997 | 2000 | 2000 | 1998
  - 同じ表の列：Status, Ref. Number, TIF District, Designation Date, End Date, Final Year, Blighting Factors, Conservation Factors

## g0006（1 列）
- 見出し：End Date
- 例1 値：2026-12-31T00:00:00.000 | 2046-12-31T00:00:00.000 | 2026-12-31T00:00:00.000 | 2031-12-31T00:00:00.000 | 2012-12-31T00:00:00.000
  - 同じ表の列：Status, Ref. Number, TIF District, Designation Date, Designation Year, Final Year, Blighting Factors, Conservation Factors

## g0007（1 列）
- 見出し：Final Year
- 例1 値：2026 | 2040 | 2024 | 2028 | 2023
  - 同じ表の列：Status, Ref. Number, TIF District, Designation Date, Designation Year, End Date, Blighting Factors, Conservation Factors

## g0008（1 列）
- 見出し：Blighting Factors
- 例1 値：No | No | Yes | Yes | No
  - 同じ表の列：Status, Ref. Number, TIF District, Designation Date, Designation Year, End Date, Final Year, Conservation Factors

## g0009（1 列）
- 見出し：Conservation Factors
- 例1 値：Yes | No | No | No | Yes
  - 同じ表の列：Status, Ref. Number, TIF District, Designation Date, Designation Year, End Date, Final Year, Blighting Factors

## g0010（1 列）
- 見出し：Category
- 例1 値：Flood Control | Bridges | Curbs & Sidewalks | Buildings | Flood Control
  - 同じ表の列：Fund, Organization Level …, Dept, Org, AU, Project #, Actual 2007-08, Actual 2008-09

## g0011（1 列）
- 見出し：Fund
- 例1 値：3090 | 3090 | 3090 | 3090 | 3090
  - 同じ表の列：Category, Organization Level …, Dept, Org, AU, Project #, Actual 2007-08, Actual 2008-09

## g0012（1 列）
- 見出し：Organization Level 4 Code
- 例1 値：87 | 7 | 64 | 89 | 89
  - 同じ表の列：Category, Fund, Dept, Org, AU, Project #, Actual 2007-08, Actual 2008-09

## g0013（1 列）
- 見出し：Dept
- 例1 値：70 | 80 | 64 | 7 | 89
  - 同じ表の列：Category, Fund, Organization Level …, Org, AU, Project #, Actual 2007-08, Actual 2008-09

## g0014（1 列）
- 見出し：Org
- 例1 値：8055 | 8057 | 8944 | 7322 | 8843
  - 同じ表の列：Category, Fund, Organization Level …, Dept, AU, Project #, Actual 2007-08, Actual 2008-09

## g0015（1 列）
- 見出し：AU
- 例1 値：A | A | B | A | B
  - 同じ表の列：Category, Fund, Organization Level …, Dept, Org, Project #, Actual 2007-08, Actual 2008-09

## g0016（1 列）
- 見出し：Project #
- 例1 値：89005409 | 89020107 | 89060081 | 70091306 | 82000135
  - 同じ表の列：Category, Fund, Organization Level …, Dept, Org, AU, Actual 2007-08, Actual 2008-09

## g0017（1 列）
- 見出し：Actual 2007-08
- 例1 値：99848.00 | 0.00 | 0.00 | 0.00 | 232.00
  - 同じ表の列：Category, Fund, Organization Level …, Dept, Org, AU, Project #, Actual 2008-09

## g0018（1 列）
- 見出し：Actual 2008-09
- 例1 値：0.00 | 2096.00 | 0.00 | 0.00 | 0.00
  - 同じ表の列：Category, Fund, Organization Level …, Dept, Org, AU, Project #, Actual 2007-08

## g0019（1 列）
- 見出し：Actual 2009-10
- 例1 値：0.00 | 0.00 | 0.00 | 15305.00 | 0.00
  - 同じ表の列：Category, Fund, Organization Level …, Dept, Org, AU, Project #, Actual 2007-08

## g0020（1 列）
- 見出し：Series
- 例1 値：003100 | 000600 | 003200 | 002400 | 200000
  - 同じ表の列：Class Code, Budget Level, Salary Schedule, FLSA Status

## g0021（1 列）
- 見出し：Class Code
- 例1 値：000183 | 009238 | 005179 | 001055 | 004023
  - 同じ表の列：Series, Budget Level, Salary Schedule, FLSA Status

## g0022（1 列）
- 見出し：Budget Level
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Series, Class Code, Salary Schedule, FLSA Status

## g0023（1 列）
- 見出し：Salary Schedule
- 例1 値：SM | SL | GN | OP | OP
  - 同じ表の列：Series, Class Code, Budget Level, FLSA Status

## g0024（1 列）
- 見出し：FLSA Status
- 例1 値：EX | NEX | EX | EX | NEX
  - 同じ表の列：Series, Class Code, Budget Level, Salary Schedule

## g0025（1 列）
- 見出し：Date
- 例1 値：2024-01-19T00:00:00.000 | 2023-01-13T00:00:00.000 | 2021-04-23T00:00:00.000 | 2021-06-30T00:00:00.000 | 2025-02-03T00:00:00.000
  - 同じ表の列：Requesting/Relevant…, Number

## g0026（1 列）
- 見出し：Requesting/Relevant Department
- 例1 値：Health & Human Services | Technology Enterprise Business Solutions | Environmental Protection & Housing and … | Fire & Rescue and Sheriff's Office | Health & Human Services
  - 同じ表の列：Date, Number

## g0027（1 列）
- 見出し：Number
- 例1 値：#26-55 | #23-93 | #22-34 | #25-48 | #26-25
  - 同じ表の列：Date, Requesting/Relevant…

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
```
