# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：Permit Number
- 例1 値：1023854 | 1037584 | 1057712 | 1063141 | 19573
  - 同じ表の列：Permit Category, Date Application Re…, Sanitarian, FoodID
- 例2 値：247354 | 226757 | 264026 | 251710 | 263523
  - 同じ表の列：Application Type, Work Type, Added Date, Issue Date, Final Date, Expired Date, Status, Building Area

## g0002（1 列）
- 見出し：Permit Category
- 例1 値：Food - New Construction | Pool - New Construction | Food - New Construction | Food - New Construction | Food - New Construction
  - 同じ表の列：Permit Number, Date Application Re…, Sanitarian, FoodID

## g0003（1 列）
- 見出し：Date Application Received
- 例1 値：2023-10-31T00:00:00.000 | 2023-02-24T00:00:00.000 | 2024-01-29T00:00:00.000 | 2023-03-30T00:00:00.000 | 2023-07-17T00:00:00.000
  - 同じ表の列：Permit Number, Permit Category, Sanitarian, FoodID

## g0004（1 列）
- 見出し：Sanitarian
- 例1 値：Murrell | Zenner | Murrell | Murrell | Zenner
  - 同じ表の列：Permit Number, Permit Category, Date Application Re…, FoodID

## g0005（1 列）
- 見出し：FoodID
- 例1 値：53824 | 60506 | 53744 | 55111 | 53778
  - 同じ表の列：Permit Number, Permit Category, Date Application Re…, Sanitarian

## g0006（1 列）
- 見出し：Application Type
- 例1 値：USE AND OCCUPANCY PERMIT | USE AND OCCUPANCY PERMIT | USE AND OCCUPANCY PERMIT | USE AND OCCUPANCY PERMIT | USE AND OCCUPANCY PERMIT
  - 同じ表の列：Permit Number, Work Type, Added Date, Issue Date, Final Date, Expired Date, Status, Building Area

## g0007（1 列）
- 見出し：Work Type
- 例1 値：OCCUPY | OCCUPY | OCCUPY | OCCUPY | OCCUPY
  - 同じ表の列：Application Type, Permit Number, Added Date, Issue Date, Final Date, Expired Date, Status, Building Area

## g0008（1 列）
- 見出し：Added Date
- 例1 値：2004-12-15T08:12:44.000 | 2008-02-13T01:02:52.000 | 2000-10-27T12:10:50.000 | 2000-09-14T02:09:26.000 | 2016-05-16T10:05:22.000
  - 同じ表の列：Application Type, Permit Number, Work Type, Issue Date, Final Date, Expired Date, Status, Building Area

## g0009（1 列）
- 見出し：Issue Date
- 例1 値：2013-04-09T09:04:42.000 | 2009-03-13T09:03:00.000 | 2022-09-19T01:09:16.000 | 2020-03-12T10:03:33.000 | 2011-07-18T09:07:00.000
  - 同じ表の列：Application Type, Permit Number, Work Type, Added Date, Final Date, Expired Date, Status, Building Area

## g0010（1 列）
- 見出し：Final Date
- 例1 値：2001-11-09T10:11:00.000 | 2015-12-15T10:12:59.000 | 2025-01-27T03:01:03.000 | 2023-07-28T09:07:20.000 | 2017-01-24T12:01:29.000
  - 同じ表の列：Application Type, Permit Number, Work Type, Added Date, Issue Date, Expired Date, Status, Building Area

## g0011（1 列）
- 見出し：Expired Date
- 例1 値：2022-10-10T12:10:00.000 | 2008-08-31T12:08:00.000 | 2025-12-31T12:12:00.000 | 2008-09-06T12:09:00.000 | 2018-06-25T12:06:00.000
  - 同じ表の列：Application Type, Permit Number, Work Type, Added Date, Issue Date, Final Date, Status, Building Area

## g0012（1 列）
- 見出し：Status
- 例1 値：Finaled | Finaled | Finaled | Issued | Finaled
  - 同じ表の列：Application Type, Permit Number, Work Type, Added Date, Issue Date, Final Date, Expired Date, Building Area

## g0013（1 列）
- 見出し：Building Area
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Application Type, Permit Number, Work Type, Added Date, Issue Date, Final Date, Expired Date, Status

## g0014（1 列）
- 見出し：Pre-direction
- 例1 値：W | E | W | E | E
  - 同じ表の列：Application Type, Permit Number, Work Type, Added Date, Issue Date, Final Date, Expired Date, Status

## g0015（1 列）
- 見出し：STATEFP10
- 例1 値：06 | 06 | 06 | 06 | 06
  - 同じ表の列：COUNTYFP10, TRACTCE10, GEOID10, MTFCC10, FUNCSTAT10, ALAND10, AWATER10, INTPTLAT10

## g0016（1 列）
- 見出し：COUNTYFP10
- 例1 値：001 | 001 | 001 | 001 | 001
  - 同じ表の列：STATEFP10, TRACTCE10, GEOID10, MTFCC10, FUNCSTAT10, ALAND10, AWATER10, INTPTLAT10

## g0017（1 列）
- 見出し：TRACTCE10
- 例1 値：438204 | 440100 | 408400 | 401600 | 402400
  - 同じ表の列：STATEFP10, COUNTYFP10, GEOID10, MTFCC10, FUNCSTAT10, ALAND10, AWATER10, INTPTLAT10

## g0018（1 列）
- 見出し：GEOID10
- 例1 値：06001420200 | 06001440200 | 06001437200 | 06001437000 | 06001422600
  - 同じ表の列：STATEFP10, COUNTYFP10, TRACTCE10, MTFCC10, FUNCSTAT10, ALAND10, AWATER10, INTPTLAT10

## g0019（1 列）
- 見出し：MTFCC10
- 例1 値：G5020 | G5020 | G5020 | G5020 | G5020
  - 同じ表の列：STATEFP10, COUNTYFP10, TRACTCE10, GEOID10, FUNCSTAT10, ALAND10, AWATER10, INTPTLAT10

## g0020（1 列）
- 見出し：FUNCSTAT10
- 例1 値：S | S | S | S | S
  - 同じ表の列：STATEFP10, COUNTYFP10, TRACTCE10, GEOID10, MTFCC10, ALAND10, AWATER10, INTPTLAT10

## g0021（1 列）
- 見出し：ALAND10
- 例1 値：724054 | 485745 | 173947 | 706609 | 7292552
  - 同じ表の列：STATEFP10, COUNTYFP10, TRACTCE10, GEOID10, MTFCC10, FUNCSTAT10, AWATER10, INTPTLAT10

## g0022（1 列）
- 見出し：AWATER10
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：STATEFP10, COUNTYFP10, TRACTCE10, GEOID10, MTFCC10, FUNCSTAT10, ALAND10, INTPTLAT10

## g0023（1 列）
- 見出し：INTPTLAT10
- 例1 値：+37.7688611 | +37.8114477 | +37.4902675 | +37.5592488 | +37.5183894
  - 同じ表の列：STATEFP10, COUNTYFP10, TRACTCE10, GEOID10, MTFCC10, FUNCSTAT10, ALAND10, AWATER10

## g0024（1 列）
- 見出し：INTPTLON10
- 例1 値：-122.1551539 | -121.9419571 | -122.0691461 | -121.9177415 | -122.0826040
  - 同じ表の列：STATEFP10, COUNTYFP10, TRACTCE10, GEOID10, MTFCC10, FUNCSTAT10, ALAND10, AWATER10

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
```
