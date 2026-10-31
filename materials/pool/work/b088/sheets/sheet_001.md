# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：OBJECTID
- 例1 値：68 | 225 | 104 | 159 | 127
  - 同じ表の列：PARK, PARK_NO, X_COORD, ARTIST, GISOBJID, OFFICIAL_N

## g0002（1 列）
- 見出し：PARK
- 例1 値：WASHINGTON (HAROLD) | WASHINGTON (GEORGE) | LINCOLN (ABRAHAM) | LINCOLN (ABRAHAM) | MIDWAY PLAISANCE
  - 同じ表の列：OBJECTID, PARK_NO, X_COORD, ARTIST, GISOBJID, OFFICIAL_N

## g0003（1 列）
- 見出し：PARK_NO
- 例1 値：100 | 40 | 147 | 108 | 8
  - 同じ表の列：OBJECTID, PARK, X_COORD, ARTIST, GISOBJID, OFFICIAL_N

## g0004（1 列）
- 見出し：X_COORD
- 例1 値：-87.6558247427 | -87.7247868652 | -87.7843536929 | -87.7123024056 | -87.6214771061
  - 同じ表の列：OBJECTID, PARK, PARK_NO, ARTIST, GISOBJID, OFFICIAL_N

## g0005（1 列）
- 見出し：ARTIST
- 例1 値：Gary Wojcik | Bernard Williams, Stephanie George, Jul… | Unknown | Mirtes Zwierzynski | Miklos Simon
  - 同じ表の列：OBJECTID, PARK, PARK_NO, X_COORD, GISOBJID, OFFICIAL_N

## g0006（1 列）
- 見出し：GISOBJID
- 例1 値：6140.0 | 1308.0 | 1293.0 | 1393.0 | 1272.0
  - 同じ表の列：OBJECTID, PARK, PARK_NO, X_COORD, ARTIST, OFFICIAL_N

## g0007（1 列）
- 見出し：OFFICIAL_N
- 例1 値：Fountain Figures | Invasive Species | Ghost Tree | Christopher Columbus Monument at Arrigo | Lead with the Heart
  - 同じ表の列：OBJECTID, PARK, PARK_NO, X_COORD, ARTIST, GISOBJID

## g0008（1 列）
- 見出し：OBJECTID_1
- 例1 値：598 | 654 | 445 | 597 | 528
  - 同じ表の列：PARK, PARK_NO, BLDG_ID, BLDG_TYPE, CITY_BLDG_, BLDG_STATU, WARD, COMM_AREA

## g0009（1 列）
- 見出し：PARK
- 例1 値：ARMSTRONG (LILLIAN HARDIN) | WARREN (LAURENCE) | LINCOLN (ABRAHAM) | DOUGLASS (ANNA & FREDERICK) | HORNER (HENRY)
  - 同じ表の列：OBJECTID_1, PARK_NO, BLDG_ID, BLDG_TYPE, CITY_BLDG_, BLDG_STATU, WARD, COMM_AREA

## g0010（1 列）
- 見出し：PARK_NO
- 例1 値：428.0 | 21.0 | 254.0 | 201.0 | 236.0
  - 同じ表の列：OBJECTID_1, PARK, BLDG_ID, BLDG_TYPE, CITY_BLDG_, BLDG_STATU, WARD, COMM_AREA

## g0011（1 列）
- 見出し：BLDG_ID
- 例1 値：0086-01 | 0034-13 | 0210-01 | 0237-01 | 0100-100
  - 同じ表の列：OBJECTID_1, PARK, PARK_NO, BLDG_TYPE, CITY_BLDG_, BLDG_STATU, WARD, COMM_AREA

## g0012（1 列）
- 見出し：BLDG_TYPE
- 例1 値：POOL BUILDING | COMFORT STATION | ZOO BUILDING | FIELDHOUSE C | STADIUM
  - 同じ表の列：OBJECTID_1, PARK, PARK_NO, BLDG_ID, CITY_BLDG_, BLDG_STATU, WARD, COMM_AREA

## g0013（1 列）
- 見出し：CITY_BLDG_
- 例1 値：395327.0 | 0.0 | 489450.0 | 429646.0 | 700580.0
  - 同じ表の列：OBJECTID_1, PARK, PARK_NO, BLDG_ID, BLDG_TYPE, BLDG_STATU, WARD, COMM_AREA

## g0014（1 列）
- 見出し：BLDG_STATU
- 例1 値：ACTIVE | ACTIVE | ACTIVE | ACTIVE | ACTIVE
  - 同じ表の列：OBJECTID_1, PARK, PARK_NO, BLDG_ID, BLDG_TYPE, CITY_BLDG_, WARD, COMM_AREA

## g0015（1 列）
- 見出し：WARD
- 例1 値：45.0 | 28.0 | 42.0 | 3.0 | 22.0
  - 同じ表の列：OBJECTID_1, PARK, PARK_NO, BLDG_ID, BLDG_TYPE, CITY_BLDG_, BLDG_STATU, COMM_AREA

## g0016（1 列）
- 見出し：COMM_AREA
- 例1 値：10.0 | 22.0 | 16.0 | 69.0 | 74.0
  - 同じ表の列：OBJECTID_1, PARK, PARK_NO, BLDG_ID, BLDG_TYPE, CITY_BLDG_, BLDG_STATU, WARD

## g0017（1 列）
- 見出し：REGION
- 例1 値：S | S | S | S | N
  - 同じ表の列：OBJECTID_1, PARK, PARK_NO, BLDG_ID, BLDG_TYPE, CITY_BLDG_, BLDG_STATU, WARD

## g0018（1 列）
- 見出し：Department
- 例1 値：HHS | HHS | POL | POL | DGS-FMS
  - 同じ表の列：Division, Model#, Shipping Date, Warranty Expiry Date, CPU, Memory, HDD/SSD

## g0019（1 列）
- 見出し：Division
- 例1 値：MC311 | PSTA | DTS | SHS | SECURITY
  - 同じ表の列：Department, Model#, Shipping Date, Warranty Expiry Date, CPU, Memory, HDD/SSD

## g0020（1 列）
- 見出し：Model#
- 例1 値：M83 | X1 YOGA | M710S | M710S | M6700
  - 同じ表の列：Department, Division, Shipping Date, Warranty Expiry Date, CPU, Memory, HDD/SSD

## g0021（1 列）
- 見出し：Shipping Date
- 例1 値：2017-02-15T00:00:00.000 | 2017-06-16T00:00:00.000 | 2017-06-16T00:00:00.000 | 2017-06-16T00:00:00.000 | 2014-12-30T00:00:00.000
  - 同じ表の列：Department, Division, Model#, Warranty Expiry Date, CPU, Memory, HDD/SSD

## g0022（1 列）
- 見出し：Warranty Expiry Date
- 例1 値：2017-05-03T00:00:00.000 | 2020-07-30T00:00:00.000 | 2017-08-28T00:00:00.000 | 2020-07-30T00:00:00.000 | 2019-07-30T00:00:00.000
  - 同じ表の列：Department, Division, Model#, Shipping Date, CPU, Memory, HDD/SSD

## g0023（1 列）
- 見出し：CPU
- 例1 値：3200 | 3200 | 2900 | 3400 | 2600
  - 同じ表の列：Department, Division, Model#, Shipping Date, Warranty Expiry Date, Memory, HDD/SSD

## g0024（1 列）
- 見出し：Memory
- 例1 値：4096 | 8192 | 8192 | 8192 | 8192
  - 同じ表の列：Department, Division, Model#, Shipping Date, Warranty Expiry Date, CPU, HDD/SSD

## g0025（1 列）
- 見出し：HDD/SSD
- 例1 値：238472 | 244191 | 238472 | 476937 | 476937
  - 同じ表の列：Department, Division, Model#, Shipping Date, Warranty Expiry Date, CPU, Memory

## g0026（1 列）
- 見出し：Date
- 例1 値：2019-10-07T08:10:07.000 | 2019-10-11T08:17:34.000 | 2019-11-21T09:49:40.000 | 2019-11-15T07:33:23.000 | 2019-10-15T08:04:21.000
  - 同じ表の列：Item, Quantity, Unit Of Measure

## g0027（1 列）
- 見出し：Item
- 例1 値：234758 | 94773 | 79529 | 233226 | 23397
  - 同じ表の列：Date, Quantity, Unit Of Measure

## g0028（1 列）
- 見出し：Quantity
- 例1 値：6 | 12 | 1 | 30 | 120
  - 同じ表の列：Date, Item, Unit Of Measure

## g0029（1 列）
- 見出し：Unit Of Measure
- 例1 値：BTL | BTL | BTL | BTL | BTL
  - 同じ表の列：Date, Item, Quantity

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
```
