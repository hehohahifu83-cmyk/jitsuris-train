# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：ROW ID
- 例1 値：80 | 12 | 41 | 60 | 7
  - 同じ表の列：Division, Quarterly Indicator, Timeframe Actual, Year, Quarter, Quarterly Actuals, Cumulative Quarters, Quarterly Targets

## g0002（1 列）
- 見出し：Division
- 例1 値：Recycling | Illegal Dumping | Solid Waste | Illegal Dumping | Illegal Dumping
  - 同じ表の列：ROW ID, Quarterly Indicator, Timeframe Actual, Year, Quarter, Quarterly Actuals, Cumulative Quarters, Quarterly Targets

## g0003（1 列）
- 見出し：Quarterly Indicator
- 例1 値：Illegal Dumping Cleaned (tons) | Illegal Dumping Cleaned (tons) | # of collection requests from Neighborh… | Neighborhood Cleanups | Diversion rate
  - 同じ表の列：ROW ID, Division, Timeframe Actual, Year, Quarter, Quarterly Actuals, Cumulative Quarters, Quarterly Targets

## g0004（1 列）
- 見出し：Timeframe Actual
- 例1 値：FY 12-13 Q4 | FY 15-16 Q3 | FY 14-15 Q1 | FY 12-13 Q1 | FY 13-14 Q3
  - 同じ表の列：ROW ID, Division, Quarterly Indicator, Year, Quarter, Quarterly Actuals, Cumulative Quarters, Quarterly Targets

## g0005（1 列）
- 見出し：Year
- 例1 値：2014-2015 | 2013-2014 | 2012-2013 | 2013-2014 | 2015-2016
  - 同じ表の列：ROW ID, Division, Quarterly Indicator, Timeframe Actual, Quarter, Quarterly Actuals, Cumulative Quarters, Quarterly Targets

## g0006（1 列）
- 見出し：Quarter
- 例1 値：1 | 1 | 4 | 2 | 4
  - 同じ表の列：ROW ID, Division, Quarterly Indicator, Timeframe Actual, Year, Quarterly Actuals, Cumulative Quarters, Quarterly Targets

## g0007（1 列）
- 見出し：Quarterly Actuals
- 例1 値：486 | 789 | 1022 | 588 | 724
  - 同じ表の列：ROW ID, Division, Quarterly Indicator, Timeframe Actual, Year, Quarter, Cumulative Quarters, Quarterly Targets

## g0008（1 列）
- 見出し：Cumulative Quarters
- 例1 値：1023 | 0 | 1023 | 103 | 1723
  - 同じ表の列：ROW ID, Division, Quarterly Indicator, Timeframe Actual, Year, Quarter, Quarterly Actuals, Quarterly Targets

## g0009（1 列）
- 見出し：Quarterly Targets
- 例1 値：1809 | 375 | 1602 | 1794 | 375
  - 同じ表の列：ROW ID, Division, Quarterly Indicator, Timeframe Actual, Year, Quarter, Quarterly Actuals, Cumulative Quarters

## g0010（1 列）
- 見出し：Cumulative Quarterly Target
- 例1 値：3676 | 220 | 375 | 1125 | 5191
  - 同じ表の列：ROW ID, Division, Quarterly Indicator, Timeframe Actual, Year, Quarter, Quarterly Actuals, Cumulative Quarters

## g0011（1 列）
- 見出し：Year
- 例1 値：2012 | 2010 | 2008 | 2009 | 2001
  - 同じ表の列：Litter Index Rating, Date

## g0012（1 列）
- 見出し：Litter Index Rating
- 例1 値：2.12 | 1.68 | 1.47 | 1.50 | 1.44
  - 同じ表の列：Year, Date

## g0013（1 列）
- 見出し：Date
- 例1 値：2006-01-01T00:00:00.000 | 2003-01-01T00:00:00.000 | 2011-01-01T00:00:00.000 | 2001-01-01T00:00:00.000 | 2008-01-01T00:00:00.000
  - 同じ表の列：Year, Litter Index Rating

## g0014（1 列）
- 見出し：Key_Value
- 例1 値：c9004 | c5000 | c2000 | c9002 | c7000
  - 同じ表の列：LotDescription, ParkingID, TotalParkingSpaces, Occupied, FreeSpaces, FullCapacity, Color, DataExportDateTime

## g0015（1 列）
- 見出し：LotDescription
- 例1 値：LOT 3 Occupancy Input | Lot Eco Occupancy | Lot 2A Occupancy | P1P Occupancy | Budget Lot (Input)
  - 同じ表の列：Key_Value, ParkingID, TotalParkingSpaces, Occupied, FreeSpaces, FullCapacity, Color, DataExportDateTime

## g0016（1 列）
- 見出し：ParkingID
- 例1 値：Budget | P3 | P2A | P2B | P5
  - 同じ表の列：Key_Value, LotDescription, TotalParkingSpaces, Occupied, FreeSpaces, FullCapacity, Color, DataExportDateTime

## g0017（1 列）
- 見出し：TotalParkingSpaces
- 例1 値：400 | 735 | 148 | 4232 | 435
  - 同じ表の列：Key_Value, LotDescription, ParkingID, Occupied, FreeSpaces, FullCapacity, Color, DataExportDateTime

## g0018（1 列）
- 見出し：Occupied
- 例1 値：268 | 226 | 554 | 830 | 903
  - 同じ表の列：Key_Value, LotDescription, ParkingID, TotalParkingSpaces, FreeSpaces, FullCapacity, Color, DataExportDateTime

## g0019（1 列）
- 見出し：FreeSpaces
- 例1 値：1397 | 289 | 300 | 64 | 1528
  - 同じ表の列：Key_Value, LotDescription, ParkingID, TotalParkingSpaces, Occupied, FullCapacity, Color, DataExportDateTime

## g0020（1 列）
- 見出し：FullCapacity
- 例1 値：82 | 64 | 67 | 68 | 79
  - 同じ表の列：Key_Value, LotDescription, ParkingID, TotalParkingSpaces, Occupied, FreeSpaces, Color, DataExportDateTime

## g0021（1 列）
- 見出し：Color
- 例1 値：Yellow | Yellow | Yellow | Yellow | Orange
  - 同じ表の列：Key_Value, LotDescription, ParkingID, TotalParkingSpaces, Occupied, FreeSpaces, FullCapacity, DataExportDateTime

## g0022（2 列）
- 見出し：DataExportDateTime
- 例1 値：2024-05-01T19:35:02.000 | 2024-05-01T19:35:04.000 | 2024-05-01T19:35:04.000 | 2024-05-01T19:35:03.000 | 2024-05-01T19:35:02.000
  - 同じ表の列：Key_Value, LotDescription, ParkingID, TotalParkingSpaces, Occupied, FreeSpaces, FullCapacity, Color
- 例2 値：2023-07-05T13:10:17.000 | 2023-11-28T16:16:42.000 | 2023-11-28T16:12:23.000 | 2023-07-05T13:10:38.000 | 2024-04-01T16:13:07.000
  - 同じ表の列：ID, SubjectText, BodyText, ExpiredDate, LastUpdated, DayOrNight, ClosureType, ConstructionStartDa…

## g0023（1 列）
- 見出し：Long
- 例1 値：-118.403672 | -118.404111 | -118.405185 | -118.400495 | -118.400495
  - 同じ表の列：Key_Value, LotDescription, ParkingID, TotalParkingSpaces, Occupied, FreeSpaces, FullCapacity, Color

## g0024（1 列）
- 見出し：DataExtractDate
- 例1 値：2018-04-18T15:12:41.000 | 2018-04-18T15:12:41.000 | 2018-04-18T15:12:41.000 | 2018-04-18T15:12:41.000 | 2019-01-30T07:34:09.000
  - 同じ表の列：ReportPeriod, Terminal, Arrival_Departure, Domestic_Internatio…, Passenger_Count

## g0025（1 列）
- 見出し：ReportPeriod
- 例1 値：2019-10-01T00:00:00.000 | 2019-11-01T00:00:00.000 | 2017-07-01T00:00:00.000 | 2015-01-01T00:00:00.000 | 2013-03-01T00:00:00.000
  - 同じ表の列：DataExtractDate, Terminal, Arrival_Departure, Domestic_Internatio…, Passenger_Count

## g0026（1 列）
- 見出し：Terminal
- 例1 値：T4 | T4 | T8 | T3 | T3
  - 同じ表の列：DataExtractDate, ReportPeriod, Arrival_Departure, Domestic_Internatio…, Passenger_Count

## g0027（1 列）
- 見出し：Arrival_Departure
- 例1 値：Arrival | Departure | Departure | Departure | Departure
  - 同じ表の列：DataExtractDate, ReportPeriod, Terminal, Domestic_Internatio…, Passenger_Count

## g0028（1 列）
- 見出し：Domestic_International
- 例1 値：Domestic | Domestic | International | Domestic | International
  - 同じ表の列：DataExtractDate, ReportPeriod, Terminal, Arrival_Departure, Passenger_Count

## g0029（1 列）
- 見出し：Passenger_Count
- 例1 値：104145 | 330408 | 40976 | 31103 | 111821
  - 同じ表の列：DataExtractDate, ReportPeriod, Terminal, Arrival_Departure, Domestic_Internatio…

## g0030（1 列）
- 見出し：ID
- 例1 値：473 | 476 | 481 | 479 | 474
  - 同じ表の列：SubjectText, BodyText, ExpiredDate, LastUpdated, DayOrNight, ClosureType, DataExportDateTime, ConstructionStartDa…

## g0031（1 列）
- 見出し：SubjectText
- 例1 値：Arrivals Sidewalk Bumpout: World Way So… | Departures Sidewalk Bumpout: World Way … | Arrivals Sidewalk Bumpout: World Way No… | Departures Sidewalk Bumpout: World Way … | Arrivals Sidewalk Bumpout: World Way No…
  - 同じ表の列：ID, BodyText, ExpiredDate, LastUpdated, DayOrNight, ClosureType, DataExportDateTime, ConstructionStartDa…

## g0032（1 列）
- 見出し：BodyText
- 例1 値：The Departures Level sidewalk along Wor… | The Arrivals Level sidewalk along World… | The Departures Level sidewalk along Wor… | The Arrivals Level sidewalk along World… | The Arrivals Level sidewalk along World…
  - 同じ表の列：ID, SubjectText, ExpiredDate, LastUpdated, DayOrNight, ClosureType, DataExportDateTime, ConstructionStartDa…

## g0033（1 列）
- 見出し：ExpiredDate
- 例1 値：2024-08-02T00:00:00.000 | 2025-12-31T00:00:00.000 | 2024-08-31T00:00:00.000 | 2025-12-31T00:00:00.000 | 2024-08-31T00:00:00.000
  - 同じ表の列：ID, SubjectText, BodyText, LastUpdated, DayOrNight, ClosureType, DataExportDateTime, ConstructionStartDa…

## g0034（1 列）
- 見出し：LastUpdated
- 例1 値：2023-11-28T16:16:42.000 | 2024-04-01T16:13:07.000 | 2023-11-28T16:12:23.000 | 2023-07-05T13:10:38.000 | 2023-07-05T13:10:17.000
  - 同じ表の列：ID, SubjectText, BodyText, ExpiredDate, DayOrNight, ClosureType, DataExportDateTime, ConstructionStartDa…

## g0035（1 列）
- 見出し：DayOrNight
- 例1 値：Continuous | Continuous | Continuous | Continuous | Continuous
  - 同じ表の列：ID, SubjectText, BodyText, ExpiredDate, LastUpdated, ClosureType, DataExportDateTime, ConstructionStartDa…

## g0036（1 列）
- 見出し：ClosureType
- 例1 値：Road Closure | Road Closure | Road Closure | Road Closure | Road Closure
  - 同じ表の列：ID, SubjectText, BodyText, ExpiredDate, LastUpdated, DayOrNight, DataExportDateTime, ConstructionStartDa…

## g0037（1 列）
- 見出し：ConstructionStartDate
- 例1 値：2023-06-30T00:00:00.000 | 2023-09-04T00:00:00.000 | 2024-03-01T00:00:00.000 | 2023-06-30T00:00:00.000 | 2023-06-30T00:00:00.000
  - 同じ表の列：ID, SubjectText, BodyText, ExpiredDate, LastUpdated, DayOrNight, ClosureType, DataExportDateTime

## g0038（1 列）
- 見出し：VoiceResponse
- 例1 値：The Arrivals Level sidewalk along World… | The Arrivals Level sidewalk along World… | The Departures Level sidewalk along Wor… | The Departures Level sidewalk along Wor… | The Arrivals Level sidewalk along World…
  - 同じ表の列：ID, SubjectText, BodyText, ExpiredDate, LastUpdated, DayOrNight, ClosureType, DataExportDateTime

## g0039（1 列）
- 見出し：BUSINESSID
- 例1 値：59891 | 51922 | 60145 | 54716 | 54682
  - 同じ表の列：YEAR_CD, OBJECTID, WBID, WB_CLS, IMP_SIZE, WB_SIZE, UNITS, POLLUTANT

## g0040（1 列）
- 見出し：YEAR_CD
- 例1 値：2016 | 2016 | 2016 | 2016 | 2012
  - 同じ表の列：BUSINESSID, OBJECTID, WBID, WB_CLS, IMP_SIZE, WB_SIZE, UNITS, POLLUTANT

## g0041（1 列）
- 見出し：OBJECTID
- 例1 値：29 | 164 | 536 | 171 | 156
  - 同じ表の列：BUSINESSID, YEAR_CD, WBID, WB_CLS, IMP_SIZE, WB_SIZE, UNITS, POLLUTANT

## g0042（1 列）
- 見出し：WBID
- 例1 値：7399 | 7352 | 7135 | 7071 | 7334
  - 同じ表の列：BUSINESSID, YEAR_CD, OBJECTID, WB_CLS, IMP_SIZE, WB_SIZE, UNITS, POLLUTANT

## g0043（1 列）
- 見出し：WB_CLS
- 例1 値：L3 | L2 | L3 | L3 | L3
  - 同じ表の列：BUSINESSID, YEAR_CD, OBJECTID, WBID, IMP_SIZE, WB_SIZE, UNITS, POLLUTANT

## g0044（1 列）
- 見出し：IMP_SIZE
- 例1 値：7 | 453 | 1635 | 148 | 273
  - 同じ表の列：BUSINESSID, YEAR_CD, OBJECTID, WBID, WB_CLS, WB_SIZE, UNITS, POLLUTANT

## g0045（1 列）
- 見出し：WB_SIZE
- 例1 値：20 | 7 | 45 | 42 | 1000
  - 同じ表の列：BUSINESSID, YEAR_CD, OBJECTID, WBID, WB_CLS, IMP_SIZE, UNITS, POLLUTANT

## g0046（1 列）
- 見出し：UNITS
- 例1 値：Ac. | Ac. | Ac. | Ac. | Ac.
  - 同じ表の列：BUSINESSID, YEAR_CD, OBJECTID, WBID, WB_CLS, IMP_SIZE, WB_SIZE, POLLUTANT

## g0047（1 列）
- 見出し：POLLUTANT
- 例1 値：Mercury in Fish Tissue (T) | Phosphorus, Total (W) | Mercury in Fish Tissue (T) | Phosphorus, Total (W) | Mercury in Fish Tissue (T)
  - 同じ表の列：BUSINESSID, YEAR_CD, OBJECTID, WBID, WB_CLS, IMP_SIZE, WB_SIZE, UNITS

## g0048（1 列）
- 見出し：SRC_DESC
- 例1 値：Atmospheric Deposition - Toxics | Rural NPS | Atmospheric Deposition - Toxics | Atmospheric Deposition - Toxics | Atmospheric Deposition - Toxics
  - 同じ表の列：BUSINESSID, YEAR_CD, OBJECTID, WBID, WB_CLS, IMP_SIZE, WB_SIZE, UNITS

## g0049（1 列）
- 見出し：Parking District
- 例1 値：S | B | S | B | B
  - 同じ表の列：Parking Number, Located At, Hours Requiring Pay…, Parking Rate, Duration, Who Can Park, Payment Options

## g0050（1 列）
- 見出し：Parking Number
- 例1 値：3472010 | 3352240 | 3402098 | 3071018 | 3550057
  - 同じ表の列：Parking District, Located At, Hours Requiring Pay…, Parking Rate, Duration, Who Can Park, Payment Options

## g0051（1 列）
- 見出し：Located At
- 例1 値：On Street | GAR 60 | GAR 16 | On Street | GAR 11
  - 同じ表の列：Parking District, Parking Number, Hours Requiring Pay…, Parking Rate, Duration, Who Can Park, Payment Options

## g0052（1 列）
- 見出し：Hours Requiring Payment
- 例1 値：7:00AM-10:00PM Monday through Friday | 7:00AM-10:00PM Monday through Friday | 7:00AM-10:00PM Monday through Friday | 7:00AM-7:00PM Monday through Friday | 7:00AM-7:00PM Monday through Friday;7:0…
  - 同じ表の列：Parking District, Parking Number, Located At, Parking Rate, Duration, Who Can Park, Payment Options

## g0053（1 列）
- 見出し：Parking Rate
- 例1 値：$0.65/hr | $0.80/hr | $0.65/hr | $0.65/hr | $0.65/hr
  - 同じ表の列：Parking District, Parking Number, Located At, Hours Requiring Pay…, Duration, Who Can Park, Payment Options

## g0054（1 列）
- 見出し：Duration
- 例1 値：15 hour limit | 15 hour limit | 15 hour limit | 12 hour limit | 12 hour limit
  - 同じ表の列：Parking District, Parking Number, Located At, Hours Requiring Pay…, Parking Rate, Who Can Park, Payment Options

## g0055（1 列）
- 見出し：Who Can Park
- 例1 値：General Public | General Public | General Public | General Public | General Public
  - 同じ表の列：Parking District, Parking Number, Located At, Hours Requiring Pay…, Parking Rate, Duration, Payment Options

## g0056（1 列）
- 見出し：Payment Options
- 例1 値：Coins, Pay-By-Cell | Coins,Pay-By-Cell, Metered | Coins,Pay-By-Cell, Metered | Bills, Coins,Cashier | Bills, Coins,Cashier
  - 同じ表の列：Parking District, Parking Number, Located At, Hours Requiring Pay…, Parking Rate, Duration, Who Can Park

## g0057（1 列）
- 見出し：Citation No
- 例1 値：6Z42259552 | 5Z46805680 | 4Z42321045 | 1Z42299566 | 3Z36235482
  - 同じ表の列：Department, Status, Open Date, Citation Date, Status Date, Citation Amount, Disposition Code, Disposition Date

## g0058（1 列）
- 見出し：Department
- 例1 値：Department of Environmental Protection | Office of Animal Services | Office of Animal Services | Office of Animal Services | Department of Environmental Protection
  - 同じ表の列：Citation No, Status, Open Date, Citation Date, Status Date, Citation Amount, Disposition Code, Disposition Date

## g0059（1 列）
- 見出し：Status
- 例1 値：Open | Open | Open | Open | Open
  - 同じ表の列：Citation No, Department, Open Date, Citation Date, Status Date, Citation Amount, Disposition Code, Disposition Date

## g0060（1 列）
- 見出し：Open Date
- 例1 値：2024-07-16T00:00:00.000 | 2021-05-20T00:00:00.000 | 2021-07-09T00:00:00.000 | 2021-06-16T00:00:00.000 | 2022-03-30T00:00:00.000
  - 同じ表の列：Citation No, Department, Status, Citation Date, Status Date, Citation Amount, Disposition Code, Disposition Date

## g0061（1 列）
- 見出し：Citation Date
- 例1 値：2023-10-20T00:00:00.000 | 2022-07-18T00:00:00.000 | 2022-10-14T00:00:00.000 | 2021-11-29T00:00:00.000 | 2019-03-08T00:00:00.000
  - 同じ表の列：Citation No, Department, Status, Open Date, Status Date, Citation Amount, Disposition Code, Disposition Date

## g0062（1 列）
- 見出し：Status Date
- 例1 値：2023-05-02T00:00:00.000 | 2022-12-05T00:00:00.000 | 2022-06-06T00:00:00.000 | 2023-02-03T00:00:00.000 | 2022-12-27T00:00:00.000
  - 同じ表の列：Citation No, Department, Status, Open Date, Citation Date, Citation Amount, Disposition Code, Disposition Date

## g0063（1 列）
- 見出し：Citation Amount
- 例1 値：500 | 1000 | 500 | 100 | 150
  - 同じ表の列：Citation No, Department, Status, Open Date, Citation Date, Status Date, Disposition Code, Disposition Date

## g0064（1 列）
- 見出し：Disposition Code
- 例1 値：Default Judgment | Guilty | Body Attachment issued | AE - Abatement Order entered | Abatement Order entered
  - 同じ表の列：Citation No, Department, Status, Open Date, Citation Date, Status Date, Citation Amount, Disposition Date

## g0065（1 列）
- 見出し：Disposition Date
- 例1 値：2024-04-09T00:00:00.000 | 2018-09-11T00:00:00.000 | 2021-07-13T00:00:00.000 | 2022-03-08T00:00:00.000 | 2021-11-23T00:00:00.000
  - 同じ表の列：Citation No, Department, Status, Open Date, Citation Date, Status Date, Citation Amount, Disposition Code

## g0066（1 列）
- 見出し：Violation Code
- 例1 値：48-19-a-1 | 5-203-C | 1-18-a-2 | 5-203-a-9 | 39-4
  - 同じ表の列：Citation No, Department, Status, Open Date, Citation Date, Status Date, Citation Amount, Disposition Code

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
g0053	
g0054	
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
```
