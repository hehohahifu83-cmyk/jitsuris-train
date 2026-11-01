# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（3 列）
- 見出し：DataExtractDate
- 例1 値：2019-03-22T10:49:20.000 | 2018-04-18T15:12:41.000 | 2018-04-18T15:12:41.000 | 2018-04-18T15:12:41.000 | 2018-04-18T15:12:41.000
  - 同じ表の列：ReportPeriod, Arrival_Departure, Domestic_Internatio…, FlightType, Passenger_Count
- 例2 値：2018-04-18T15:12:41.000 | 2018-04-18T15:12:41.000 | 2018-04-18T15:12:41.000 | 2020-04-29T07:14:24.000 | 2018-04-18T15:12:41.000
  - 同じ表の列：ReportPeriod, FlightType, Arrival_Departure, Domestic_Internatio…, FlightOpsCount

## g0002（3 列）
- 見出し：ReportPeriod
- 例1 値：2020-04-01T00:00:00.000 | 2012-02-01T00:00:00.000 | 2013-10-01T00:00:00.000 | 2010-01-01T00:00:00.000 | 2011-08-01T00:00:00.000
  - 同じ表の列：DataExtractDate, Arrival_Departure, Domestic_Internatio…, FlightType, Passenger_Count
- 例2 値：2012-07-01T00:00:00.000 | 2008-07-01T00:00:00.000 | 2013-08-01T00:00:00.000 | 2019-12-01T00:00:00.000 | 2011-01-01T00:00:00.000
  - 同じ表の列：DataExtractDate, FlightType, Arrival_Departure, Domestic_Internatio…, FlightOpsCount

## g0003（3 列）
- 見出し：Arrival_Departure
- 例1 値：Arrival | Departure | Departure | Departure | Arrival
  - 同じ表の列：DataExtractDate, ReportPeriod, Domestic_Internatio…, FlightType, Passenger_Count
- 例2 値：Departure | Arrival | Arrival | Departure | Arrival
  - 同じ表の列：DataExtractDate, ReportPeriod, FlightType, Domestic_Internatio…, FlightOpsCount

## g0004（3 列）
- 見出し：Domestic_International
- 例1 値：International | Domestic | Domestic | Domestic | International
  - 同じ表の列：DataExtractDate, ReportPeriod, Arrival_Departure, FlightType, Passenger_Count
- 例2 値：Domestic | International | Domestic | Domestic | International
  - 同じ表の列：DataExtractDate, ReportPeriod, FlightType, Arrival_Departure, FlightOpsCount

## g0005（1 列）
- 見出し：FlightType
- 例1 値：Scheduled Carriers | Scheduled Carriers | Scheduled Carriers | Charter | Charter
  - 同じ表の列：DataExtractDate, ReportPeriod, Arrival_Departure, Domestic_Internatio…, Passenger_Count

## g0006（1 列）
- 見出し：Passenger_Count
- 例1 値：1701184 | 740 | 62949 | 737176 | 43
  - 同じ表の列：DataExtractDate, ReportPeriod, Arrival_Departure, Domestic_Internatio…, FlightType

## g0007（1 列）
- 見出し：FlightType
- 例1 値：Scheduled | Charter | Charter | Scheduled | Charter
  - 同じ表の列：DataExtractDate, ReportPeriod, Arrival_Departure, Domestic_Internatio…, FlightOpsCount

## g0008（1 列）
- 見出し：FlightOpsCount
- 例1 値：6 | 3 | 3372 | 5 | 3409
  - 同じ表の列：DataExtractDate, ReportPeriod, FlightType, Arrival_Departure, Domestic_Internatio…

## g0009（1 列）
- 見出し：CargoType
- 例1 値：Mail | Freight | Freight | Freight | Mail
  - 同じ表の列：DataExtractDate, ReportPeriod, Arrival_Departure, Domestic_Internatio…, AirCargoTons

## g0010（1 列）
- 見出し：AirCargoTons
- 例1 値：2175 | 56553 | 29972 | 36738 | 931
  - 同じ表の列：DataExtractDate, ReportPeriod, Arrival_Departure, Domestic_Internatio…, CargoType

## g0011（1 列）
- 見出し：Year
- 例1 値：2021 | 2016 | 2021 | 2015 | 2016
  - 同じ表の列：Lobbyist’s Firm, Additional Lobbyists, Second Half (July1 …

## g0012（1 列）
- 見出し：Lobbyist’s Firm
- 例1 値：Alexander & Cleaver, P.A. | Harris Jones & Malone, LLC | Harris Jones & Malone, LLC | Lerch, Early & Brewer, Chtd. | Lerch, Early & Brewer, Chtd.
  - 同じ表の列：Year, Additional Lobbyists, Second Half (July1 …

## g0013（1 列）
- 見出し：Additional Lobbyists
- 例1 値：Hayley Evans, Ron Young | Heather Dlhopolsky | Yum Yu Cheng | Phillip A. Hummel | Matt Bohle
  - 同じ表の列：Year, Lobbyist’s Firm, Second Half (July1 …

## g0014（1 列）
- 見出し：Second Half (July1 – DEC 31)
- 例1 値：1766 | 10602 | 949 | 1410 | 0
  - 同じ表の列：Year, Lobbyist’s Firm, Additional Lobbyists

## g0015（1 列）
- 見出し：Site
- 例1 値：Barnsley, Lucy Elementary School | Executive Office Building | Somerset Elementary School | Seven Locks Elementary School | Ashburton Elementary School
  - 同じ表の列：Facility Type, Function, Paid Hours, Free Hours, Admin Hours

## g0016（1 列）
- 見出し：Facility Type
- 例1 値：Field, Artificial Turf | Room, Meeting | All Purpose Room | Gymnasium | Classroom
  - 同じ表の列：Site, Function, Paid Hours, Free Hours, Admin Hours

## g0017（1 列）
- 見出し：Function
- 例1 値：Meeting/Seminar | Other, General | I-Sports, Basketball (Youth) | O-Sports, Baseball (Youth) | LB Meeting
  - 同じ表の列：Site, Facility Type, Paid Hours, Free Hours, Admin Hours

## g0018（1 列）
- 見出し：Paid Hours
- 例1 値：18 | 0 | 6.5 | 0 | 15
  - 同じ表の列：Site, Facility Type, Function, Free Hours, Admin Hours

## g0019（1 列）
- 見出し：Free Hours
- 例1 値：0 | 0 | 0 | 24 | 0
  - 同じ表の列：Site, Facility Type, Function, Paid Hours, Admin Hours

## g0020（1 列）
- 見出し：Admin Hours
- 例1 値：0 | 0 | 0 | 0 | 384.58
  - 同じ表の列：Site, Facility Type, Function, Paid Hours, Free Hours

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
```
