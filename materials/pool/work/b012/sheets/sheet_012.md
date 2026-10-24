# ラベル用シート 012 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_012.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1321（1 列）
- 見出し：April
- 例1 値：8420 | 18020 | 9180 | 11160 | 57140
  - 同じ表の列：Row Labels, January, February, March, May, June, July, August

## g1322（2 列）
- 見出し：May
- 例1 値：55240 | 1560 | 9780 | 174920 | 34400
  - 同じ表の列：Row Labels, January, February, March, April, June, July, August
- 例2 値：3 | 14 | 6 | 2 | 9
  - 同じ表の列：AreaID, RegionID, Area, Year, Jan, Feb, Mar, Apr

## g1323（1 列）
- 見出し：June
- 例1 値：9600 | 7200 | 56240 | 17580 | 178480
  - 同じ表の列：Row Labels, January, February, March, April, May, July, August

## g1324（1 列）
- 見出し：July
- 例1 値：32740 | 9900 | 7700 | 6720 | 22400
  - 同じ表の列：Row Labels, January, February, March, April, May, June, August

## g1325（1 列）
- 見出し：August
- 例1 値：34720 | 18180 | 8240 | 17820 | 23520
  - 同じ表の列：Row Labels, January, February, March, April, May, June, July

## g1326（1 列）
- 見出し：September
- 例1 値：10700 | 20900 | 1700 | 10460 | 8760
  - 同じ表の列：Row Labels, January, February, March, April, May, June, July

## g1327（1 列）
- 見出し：Statistic
- 例1 値：Bulk Traffic | Bulk Traffic | Bulk Traffic | Bulk Traffic | Bulk Traffic
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02638V03194, Type of Traffic, C01855V02284, Port, UNIT

## g1328（1 列）
- 見出し：Type of Traffic
- 例1 値：Liquid bulk traffic | Dry bulk traffic | Dry bulk traffic | Break bulk traffic | Liquid bulk traffic
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02638V03194, C01855V02284, Port, UNIT

## g1329（1 列）
- 見出し：C01855V02284
- 例1 値：XILAR | IE | IEBYT | IETRA | IETRA
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02638V03194, Type of Traffic, Port, UNIT

## g1330（1 列）
- 見出し：Port
- 例1 値：Dundalk | Dundalk | Warrenpoint | All Northern Irish ports | Warrenpoint
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02638V03194, Type of Traffic, C01855V02284, UNIT

## g1331（1 列）
- 見出し：UNIT
- 例1 値：000 Tonnes | 000 Tonnes | 000 Tonnes | 000 Tonnes | 000 Tonnes
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02638V03194, Type of Traffic, C01855V02284, Port

## g1332（1 列）
- 見出し：Valid to Hour
- 例1 値：1200 | 0600 | 0000 | 1200 | 1800
  - 同じ表の列：Valid to Date, Issued Hour, Issued Date, Gale Warning, Small Craft Warning, Time of Meteorologi…, Meteorological Situ…, Forecast for Area 1

## g1333（1 列）
- 見出し：Valid to Date
- 例1 値：2012-12-09T00:00:00 | 2012-11-03T00:00:00 | 2012-08-17T00:00:00 | 2012-10-11T00:00:00 | 2012-09-25T00:00:00
  - 同じ表の列：Valid to Hour, Issued Hour, Issued Date, Gale Warning, Small Craft Warning, Time of Meteorologi…, Meteorological Situ…, Forecast for Area 1

## g1334（1 列）
- 見出し：Issued Hour
- 例1 値：0000 | 0000 | 1800 | 0600 | 0600
  - 同じ表の列：Valid to Hour, Valid to Date, Issued Date, Gale Warning, Small Craft Warning, Time of Meteorologi…, Meteorological Situ…, Forecast for Area 1

## g1335（1 列）
- 見出し：Issued Date
- 例1 値：2012-12-09T00:00:00 | 2012-12-21T00:00:00 | 2013-01-30T00:00:00 | 2012-05-17T00:00:00 | 2012-06-13T00:00:00
  - 同じ表の列：Valid to Hour, Valid to Date, Issued Hour, Gale Warning, Small Craft Warning, Time of Meteorologi…, Meteorological Situ…, Forecast for Area 1

## g1336（1 列）
- 見出し：Gale Warning
- 例1 値：Nil | Southerly winds will reach gale force o… | West to northwest winds will reach gale… | Nil | Nil
  - 同じ表の列：Valid to Hour, Valid to Date, Issued Hour, Issued Date, Small Craft Warning, Time of Meteorologi…, Meteorological Situ…, Forecast for Area 1

## g1337（1 列）
- 見出し：Small Craft Warning
- 例1 値：Nil | West to southwest winds will reach forc… | Nil | Southeast winds will reach force 6 at t… | Nil
  - 同じ表の列：Valid to Hour, Valid to Date, Issued Hour, Issued Date, Gale Warning, Time of Meteorologi…, Meteorological Situ…, Forecast for Area 1

## g1338（1 列）
- 見出し：Time of Meteorological Situation
- 例1 値：0300 | 1500 | 0300 | 1500 | 0900
  - 同じ表の列：Valid to Hour, Valid to Date, Issued Hour, Issued Date, Gale Warning, Small Craft Warning, Meteorological Situ…, Forecast for Area 1

## g1339（1 列）
- 見出し：Meteorological Situation
- 例1 値：A ridge of high pressure is intensifyin… | A slackening and stabilising easterly a… | A ridge of high pressure over Ireland c… | An anticyclone of 1022hPa is positioned… | A complex area of low pressure covers t…
  - 同じ表の列：Valid to Hour, Valid to Date, Issued Hour, Issued Date, Gale Warning, Small Craft Warning, Time of Meteorologi…, Forecast for Area 1

## g1340（1 列）
- 見出し：Forecast for Area 1
- 例1 値：Fair Head to Howth Head to Carnsore Poi… | Malin Head to Howth Head to Mizen Head … | Slyne Head to Rossan Point to Malin Head | Roche's Point to Slyne Head to Malin He… | Wicklow Head to Roche's Pt to Rossan Pt…
  - 同じ表の列：Valid to Hour, Valid to Date, Issued Hour, Issued Date, Gale Warning, Small Craft Warning, Time of Meteorologi…, Meteorological Situ…

## g1341（1 列）
- 見出し：wind__area_1_
- 例1 値：Southerly force 4 to 5, increasing forc… | Northwest force 5 to 6, decreasing forc… | Southwest force 4 or 5 and gusty at tim… | West force 4 to 5, increasing force 5 t… | Southeast force 4 to 5, veering south t…
  - 同じ表の列：Valid to Hour, Valid to Date, Issued Hour, Issued Date, Gale Warning, Small Craft Warning, Time of Meteorologi…, Meteorological Situ…

## g1342（1 列）
- 見出し：head_of_duty
- 例1 値：Bookmaking Premises number issued | MHLO Unleaded Petrol | Tobacco Cigars | Spirits Import | Kerosene
  - 同じ表の列：year, quantity_of_measure, volume

## g1343（1 列）
- 見出し：quantity_of_measure
- 例1 値：thousand litres | litres of alcohol | thousand litres | thousand litres | thousand litres
  - 同じ表の列：head_of_duty, year, volume

## g1344（1 列）
- 見出し：volume
- 例1 値：6492483.36 | 3065930.92 | 2845528 | 3098756 | 3434070
  - 同じ表の列：head_of_duty, year, quantity_of_measure

## g1345（1 列）
- 見出し：Ref
- 例1 値：57000 | 56200 | 57500 | 55650 | 57200
  - 同じ表の列：Doc, Heading, desc, Inc, PY, Sort, OBJECTID

## g1346（1 列）
- 見出し：desc
- 例1 値：Parking Fines &Charges | Irish Water | Agency Services & Repayable Works | Sale/leasing of other property/Industri… | Housing Loans Interest & Charges
  - 同じ表の列：Doc, Heading, Ref, Inc, PY, Sort, OBJECTID

## g1347（1 列）
- 見出し：Inc
- 例1 値：-211000 | -20000 | -130000 | -120500 | -91500
  - 同じ表の列：Doc, Heading, Ref, desc, PY, Sort, OBJECTID

## g1348（1 列）
- 見出し：PY
- 例1 値：-11425800 | -91500 | -5848000 | -246000 | -741500
  - 同じ表の列：Doc, Heading, Ref, desc, Inc, Sort, OBJECTID

## g1349（1 列）
- 見出し：Sort
- 例1 値：80 | 110 | 65 | 70 | 130
  - 同じ表の列：Doc, Heading, Ref, desc, Inc, PY, OBJECTID

## g1350（1 列）
- 見出し：AreaID
- 例1 値：4 | 17 | 9 | 22 | 1
  - 同じ表の列：RegionID, Area, Year, Jan, Feb, Mar, Apr, May

## g1351（1 列）
- 見出し：RegionID
- 例1 値：21 | 20 | 20 | 18 | 18
  - 同じ表の列：AreaID, Area, Year, Jan, Feb, Mar, Apr, May

## g1352（1 列）
- 見出し：Area
- 例1 値：Dublin South West Kildare West Wicklow | Kerry | Mayo | The Midwest | Donegal
  - 同じ表の列：AreaID, RegionID, Year, Jan, Feb, Mar, Apr, May

## g1353（1 列）
- 見出し：Jan
- 例1 値：2 | 3 | 6 | 4 | 11
  - 同じ表の列：AreaID, RegionID, Area, Year, Feb, Mar, Apr, May

## g1354（1 列）
- 見出し：Feb
- 例1 値：13 | 5 | 3 | 5 | 5
  - 同じ表の列：AreaID, RegionID, Area, Year, Jan, Mar, Apr, May

## g1355（1 列）
- 見出し：Mar
- 例1 値：14 | 2 | 3 | 6 | 2
  - 同じ表の列：AreaID, RegionID, Area, Year, Jan, Feb, Apr, May

## g1356（1 列）
- 見出し：Apr
- 例1 値：3 | 17 | 6 | 9 | 4
  - 同じ表の列：AreaID, RegionID, Area, Year, Jan, Feb, Mar, May

## g1357（1 列）
- 見出し：Jun
- 例1 値：1 | 1 | 2 | 3 | 5
  - 同じ表の列：AreaID, RegionID, Area, Year, Jan, Feb, Mar, Apr

## g1358（1 列）
- 見出し：Prehistoric_Monuments_Buffer
- 例1 値：50m Buffer around Prehistoric Monument | 50m Buffer around Prehistoric Monument | 50m Buffer around Prehistoric Monument | 50m Buffer around Prehistoric Monument | 50m Buffer around Prehistoric Monument
  - 同じ表の列：OBJECTID, SHAPE__Area, SHAPE__Length

## g1359（1 列）
- 見出し：SHAPE__Area
- 例1 値：2912966.79052734 | 752960.118682861 | 752942.879638672 | 3272259.27377319 | 5235200.19100952
  - 同じ表の列：Prehistoric_Monumen…, OBJECTID, SHAPE__Length

## g1360（1 列）
- 見出し：SHAPE__Length
- 例1 値：7491.57820140087 | 9550.06886087633 | 9865.30333555662 | 3111.95502341628 | 3111.88136528818
  - 同じ表の列：Prehistoric_Monumen…, OBJECTID, SHAPE__Area

## g1361（1 列）
- 見出し：Self-managed super fund statistical report - September 2023
- 例1 値：Table 10: Flow of funds | Contents | Explanatory Notes | Table 4: Membership size | Table 6: Member demographics - age and …
  - 同じ表の列：end of row

## g1362（1 列）
- 見出し：end of row
- 例1 値：end of row | end of row | end of row | end of row | end of row
  - 同じ表の列：Self-managed super …

## g1363（1 列）
- 見出し：STBIOH - Bio Hazards (inc vomit
- 例1 値：STBIOH - Bio Hazards (inc vomit | STBIOH - Bio Hazards (inc vomit | STBIOH - Bio Hazards (inc vomit | STBIOH - Bio Hazards (inc vomit | STBIOH - Bio Hazards (inc vomit
  - 同じ表の列：condoms, 2011/2012, April, Apr-2012, CY 2012, ST KILDA, 12

## g1364（1 列）
- 見出し：condoms
- 例1 値：condoms | condoms | condoms | condoms | condoms
  - 同じ表の列：STBIOH - Bio Hazard…, 2011/2012, April, Apr-2012, CY 2012, ST KILDA, 12

## g1365（1 列）
- 見出し：2011/2012
- 例1 値：2012/2013 | 2013/2014 | 2017/2018 | 2013/2014 | 2018/2019
  - 同じ表の列：STBIOH - Bio Hazard…, condoms, April, Apr-2012, CY 2012, ST KILDA, 12

## g1366（1 列）
- 見出し：April
- 例1 値：July | September | October | May | February
  - 同じ表の列：STBIOH - Bio Hazard…, condoms, 2011/2012, Apr-2012, CY 2012, ST KILDA, 12

## g1367（1 列）
- 見出し：Apr-2012
- 例1 値：Feb-2013 | Mar-2018 | Jan-2019 | Mar-2016 | Oct-2017
  - 同じ表の列：STBIOH - Bio Hazard…, condoms, 2011/2012, April, CY 2012, ST KILDA, 12

## g1368（1 列）
- 見出し：CY 2012
- 例1 値：CY 2016 | CY 2017 | CY 2012 | CY 2016 | CY 2020
  - 同じ表の列：STBIOH - Bio Hazard…, condoms, 2011/2012, April, Apr-2012, ST KILDA, 12

## g1369（1 列）
- 見出し：ST KILDA
- 例1 値：ST KILDA | ST KILDA | ELWOOD | ALBERT PARK | SOUTH MELBOURNE
  - 同じ表の列：STBIOH - Bio Hazard…, condoms, 2011/2012, April, Apr-2012, CY 2012, 12

## g1370（1 列）
- 見出し：12
- 例1 値：3 | 9 | 1 | 2 | 1
  - 同じ表の列：STBIOH - Bio Hazard…, condoms, 2011/2012, April, Apr-2012, CY 2012, ST KILDA

## g1371（1 列）
- 見出し：Number of dedicated commercialisation staff (FTE)
- 例1 値：2 | 0.5 | 2 | 5 | 0
  - 同じ表の列：Year, Number of invention…, Number of LOA execu…, Number of LOAs yiel…, Tota value income y…, Value reported inco…, Number of start-ups…, Number of start-ups…

## g1372（1 列）
- 見出し：Number of invention disclosures
- 例1 値：28 | 14 | 65 | 78 | 10
  - 同じ表の列：Year, Number of dedicated…, Number of LOA execu…, Number of LOAs yiel…, Tota value income y…, Value reported inco…, Number of start-ups…, Number of start-ups…

## g1373（1 列）
- 見出し：Number of LOA executed
- 例1 値：0 | 11 | 0 | 0 | 5
  - 同じ表の列：Year, Number of dedicated…, Number of invention…, Number of LOAs yiel…, Tota value income y…, Value reported inco…, Number of start-ups…, Number of start-ups…

## g1374（1 列）
- 見出し：Number of LOAs yielding income
- 例1 値：13 | 0 | 1 | 0 | 1
  - 同じ表の列：Year, Number of dedicated…, Number of invention…, Number of LOA execu…, Tota value income y…, Value reported inco…, Number of start-ups…, Number of start-ups…

## g1375（1 列）
- 見出し：Tota value income yielded from active LOAs
- 例1 値：$0.00 | $27,444.00 | $43,000.00 | $85,000.00 | $78,426.00
  - 同じ表の列：Year, Number of dedicated…, Number of invention…, Number of LOA execu…, Number of LOAs yiel…, Value reported inco…, Number of start-ups…, Number of start-ups…

## g1376（1 列）
- 見出し：Value reported income paid to other institutions or entitie
- 例1 値：$0.00 | $0.00 | $0.00 | $0.00 | $23,052.00
  - 同じ表の列：Year, Number of dedicated…, Number of invention…, Number of LOA execu…, Number of LOAs yiel…, Tota value income y…, Number of start-ups…, Number of start-ups…

## g1377（1 列）
- 見出し：Number of start-ups operational year end dependent on assig
- 例1 値：20 | 19 | 1 | 3 | 0
  - 同じ表の列：Year, Number of dedicated…, Number of invention…, Number of LOA execu…, Number of LOAs yiel…, Tota value income y…, Value reported inco…, Number of start-ups…

## g1378（1 列）
- 見出し：Number of start-ups operational at year end dependent on as
- 例1 値：17 | 0 | 0 | 3 | 0
  - 同じ表の列：Year, Number of dedicated…, Number of invention…, Number of LOA execu…, Number of LOAs yiel…, Tota value income y…, Value reported inco…, Number of start-ups…

## g1379（1 列）
- 見出し：Number of start-ups created
- 例1 値：0 | 2 | 1 | 0 | 0
  - 同じ表の列：Year, Number of dedicated…, Number of invention…, Number of LOA execu…, Number of LOAs yiel…, Tota value income y…, Value reported inco…, Number of start-ups…

## g1380（1 列）
- 見出し：ip_right_type
- 例1 値：design | design | design | design | design
  - 同じ表の列：application_number, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g1381（1 列）
- 見出し：application_number
- 例1 値：201412621 | 201611122 | 201412851 | 201610926 | 201610791
  - 同じ表の列：ip_right_type, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g1382（1 列）
- 見出し：ip_right_sub_type
- 例1 値：design | design | design | design | design
  - 同じ表の列：ip_right_type, application_number, status, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g1383（1 列）
- 見出し：earliest_filed_date
- 例1 値：2016-03-03 | 2014-05-23 | 2016-01-29 | 2016-02-26 | 2016-02-02
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, priority_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g1384（1 列）
- 見出し：priority_date
- 例1 値：2014-03-26 | 2016-02-03 | 2015-09-11 | 2015-09-02 | 2015-09-02
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, earliest_filed_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g1385（1 列）
- 見出し：gained_registration_status_date
- 例1 値：2016-02-25 | 2016-03-03 | 2016-02-29 | 2016-05-26 | 2016-04-22
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_enforceable_…, enforceable_from_da…

## g1386（1 列）
- 見出し：gained_enforceable_status_date
- 例1 値：2016-05-04 | 2016-07-21 | 2016-08-16 | 2014-09-18 | 2016-05-25
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_registration…, enforceable_from_da…

## g1387（1 列）
- 見出し：enforceable_from_date
- 例1 値：2016-05-02 | 2016-07-29 | 2018-03-26 | 2014-09-05 | 2016-04-01
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…

## g1388（1 列）
- 見出し：deemed_retired_date
- 例1 値：2014-08-24 | 2019-06-11 | 2019-06-10 | 2019-06-03 | 2019-05-19
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…

## g1389（1 列）
- 見出し：Property_ID
- 例1 値：500937 | 157177 | 151022 | 135502 | 127471
  - 同じ表の列：Service_No, Service_Type, Service_Status, Service_Qty, Shared_Service, LOTPLAN, LandStatus, Date_Effective

## g1390（1 列）
- 見出し：Service_No
- 例1 値：6317671 | 6191123 | 6320241 | 6288163 | 6318261
  - 同じ表の列：Property_ID, Service_Type, Service_Status, Service_Qty, Shared_Service, LOTPLAN, LandStatus, Date_Effective

## g1391（1 列）
- 見出し：Service_Type
- 例1 値：DWB240_3 | N-DWB | DWB360_3 | N-DGB | DWB240_3
  - 同じ表の列：Property_ID, Service_No, Service_Status, Service_Qty, Shared_Service, LOTPLAN, LandStatus, Date_Effective

## g1392（1 列）
- 見出し：Service_Status
- 例1 値：N | N | N | N | N
  - 同じ表の列：Property_ID, Service_No, Service_Type, Service_Qty, Shared_Service, LOTPLAN, LandStatus, Date_Effective

## g1393（1 列）
- 見出し：Service_Qty
- 例1 値：1.00 | 1.00 | 1.00 | 1.00 | 1.00
  - 同じ表の列：Property_ID, Service_No, Service_Type, Service_Status, Shared_Service, LOTPLAN, LandStatus, Date_Effective

## g1394（1 列）
- 見出し：Shared_Service
- 例1 値：False | False | False | False | True
  - 同じ表の列：Property_ID, Service_No, Service_Type, Service_Status, Service_Qty, LOTPLAN, LandStatus, Date_Effective

## g1395（1 列）
- 見出し：LOTPLAN
- 例1 値：1RP214051 | 5GTP106817 | 125RP88934 | 2SP287117 | 2SP288946
  - 同じ表の列：Property_ID, Service_No, Service_Type, Service_Status, Service_Qty, Shared_Service, LandStatus, Date_Effective

## g1396（1 列）
- 見出し：LandStatus
- 例1 値：C | C | C | C | C
  - 同じ表の列：Property_ID, Service_No, Service_Type, Service_Status, Service_Qty, Shared_Service, LOTPLAN, Date_Effective

## g1397（1 列）
- 見出し：Date_Effective
- 例1 値：20180101 | 20180817 | 20180101 | 20180607 | 20180530
  - 同じ表の列：Property_ID, Service_No, Service_Type, Service_Status, Service_Qty, Shared_Service, LOTPLAN, LandStatus

## g1398（1 列）
- 見出し：GIS_LoadDate
- 例1 値：20190815 | 20190815 | 20190815 | 20190815 | 20190815
  - 同じ表の列：Property_ID, Service_No, Service_Type, Service_Status, Service_Qty, Shared_Service, LOTPLAN, LandStatus

## g1399（1 列）
- 見出し：Status
- 例1 値：Contains Water | Contains Water | Contains Water | Contains Water | Contains Water
  - 同じ表の列：Lat, Long, Reserve, Photo

## g1400（1 列）
- 見出し：Reserve
- 例1 値：Wal Wal Swamp Wildlife Reserve | Willenabrina I86 Bushland Reserve | Burrereo Bushland Reserve | Watchem I120 Bushland Reserve | Crow Swamp (Phillips Dam) Wildlife Rese…
  - 同じ表の列：Lat, Long, Status, Photo

## g1401（1 列）
- 見出し：Photo
- 例1 値：http://www.wcma.vic.gov.au/images/defau… | http://www.wcma.vic.gov.au/images/defau… | http://www.wcma.vic.gov.au/images/defau… | http://www.wcma.vic.gov.au/images/defau… | http://www.wcma.vic.gov.au/images/defau…
  - 同じ表の列：Lat, Long, Status, Reserve

## g1402（1 列）
- 見出し：Origin
- 例1 値：UNKNOWN | UNITED STATES | UNITED STATES | UNKNOWN | CANADA
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origine, Product, Produit, Organic - Biologique, Date Sampled - Date…

## g1403（1 列）
- 見出し：Origine
- 例1 値：ÉTATS-UNIS | INCONNU | CANADA | INCONNU | ÉTATS-UNIS
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Product, Produit, Organic - Biologique, Date Sampled - Date…

## g1404（1 列）
- 見出し：Product
- 例1 値：Infant Food - Snack | Infant Formula - Dairy | Infant Formula - Dairy | Infant Food - Snack | Infant Food - Cereal
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Produit, Organic - Biologique, Date Sampled - Date…

## g1405（1 列）
- 見出し：Produit
- 例1 値：Craquelins | Céréales - Nourrissons | Aliment pour nourrissons - collation | Céréales - Nourrissons | Mélange à pâte
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Organic - Biologique, Date Sampled - Date…

## g1406（1 列）
- 見出し：Type of test
- 例1 値：METALS | METALS | POLAR PESTICIDES GROUP A | METALS | METALS
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Organic - Biologique

## g1407（1 列）
- 見出し：AMP identifier
- 例1 値：2017-AMP-04 | 2018-AMP-01 | 2017-AMP-06 | 2017-AMP-08 | 2018-AMP-03
  - 同じ表の列：Date issued, Issuing division, Licensed activity, Provision, Violation category, Penalty amount (CAD), Penalty amount (CAD…

## g1408（1 列）
- 見出し：Date issued
- 例1 値：9/13/2017 | 12/12/2017 | 4/23/2018 | 3/10/2017 | 4/30/2018
  - 同じ表の列：AMP identifier, Issuing division, Licensed activity, Provision, Violation category, Penalty amount (CAD), Penalty amount (CAD…

## g1409（1 列）
- 見出し：Issuing division
- 例1 値：Operations Inspection Division | Transport Licensing and Strategic Suppo… | Operations Inspection Division | Operations Inspection Division | Nuclear Processing Facilities Division
  - 同じ表の列：AMP identifier, Date issued, Licensed activity, Provision, Violation category, Penalty amount (CAD), Penalty amount (CAD…

## g1410（1 列）
- 見出し：Licensed activity
- 例1 値：Exposure device operator | Portable gauges | Nuclear fuel facility | Industrial radiography | Transport
  - 同じ表の列：AMP identifier, Date issued, Issuing division, Provision, Violation category, Penalty amount (CAD), Penalty amount (CAD…

## g1411（1 列）
- 見出し：Provision
- 例1 値：25(4)(a) PTNSR | 17(b) GNSCR | 48(c) NSCA | Gen 12(1)(c) | 48(c) NSCA
  - 同じ表の列：AMP identifier, Date issued, Issuing division, Licensed activity, Violation category, Penalty amount (CAD), Penalty amount (CAD…

## g1412（1 列）
- 見出し：Violation category
- 例1 値：B | B | B | C | B
  - 同じ表の列：AMP identifier, Date issued, Issuing division, Licensed activity, Provision, Penalty amount (CAD), Penalty amount (CAD…

## g1413（1 列）
- 見出し：Penalty amount (CAD)
- 例1 値：17830 | 9190 | 11920 | 3970 | 3970
  - 同じ表の列：AMP identifier, Date issued, Issuing division, Licensed activity, Provision, Violation category, Penalty amount (CAD…

## g1414（1 列）
- 見出し：Penalty amount (CAD) after Commission's review (if applicab
- 例1 値：17830 | 11920
  - 同じ表の列：AMP identifier, Date issued, Issuing division, Licensed activity, Provision, Violation category, Penalty amount (CAD)

## g1415（1 列）
- 見出し：Province/Territory
- 例1 値：Nova Scotia | Prince Edward Island | Non-resident | Non-resident | Saskatchewan
  - 同じ表の列：Filing Method, On time returns, 1-7 days late, 8-28 days late, 29-56 days late, 57-112 days late, 113-168 days late, 169+ days late

## g1416（1 列）
- 見出し：Filing Method
- 例1 値：SimpleFile services | Paper | EFILE | SimpleFile services | SimpleFile services
  - 同じ表の列：Province/Territory, On time returns, 1-7 days late, 8-28 days late, 29-56 days late, 57-112 days late, 113-168 days late, 169+ days late

## g1417（1 列）
- 見出し：On time returns
- 例1 値：221210 | 1542790 | 0 | 1245570 | 6020
  - 同じ表の列：Province/Territory, Filing Method, 1-7 days late, 8-28 days late, 29-56 days late, 57-112 days late, 113-168 days late, 169+ days late

## g1418（1 列）
- 見出し：1-7 days late
- 例1 値：20 | 3680 | 310 | 110 | 0
  - 同じ表の列：Province/Territory, Filing Method, On time returns, 8-28 days late, 29-56 days late, 57-112 days late, 113-168 days late, 169+ days late

## g1419（1 列）
- 見出し：8-28 days late
- 例1 値：350 | 10480 | 13160 | 910 | 96000
  - 同じ表の列：Province/Territory, Filing Method, On time returns, 1-7 days late, 29-56 days late, 57-112 days late, 113-168 days late, 169+ days late

## g1420（1 列）
- 見出し：29-56 days late
- 例1 値：640 | 1680 | 1220 | 0 | 27690
  - 同じ表の列：Province/Territory, Filing Method, On time returns, 1-7 days late, 8-28 days late, 57-112 days late, 113-168 days late, 169+ days late

## g1421（1 列）
- 見出し：57-112 days late
- 例1 値：300 | 740 | 0 | 950 | 11030
  - 同じ表の列：Province/Territory, Filing Method, On time returns, 1-7 days late, 8-28 days late, 29-56 days late, 113-168 days late, 169+ days late

## g1422（1 列）
- 見出し：113-168 days late
- 例1 値：130 | 56600 | 660 | 10 | 42950
  - 同じ表の列：Province/Territory, Filing Method, On time returns, 1-7 days late, 8-28 days late, 29-56 days late, 57-112 days late, 169+ days late

## g1423（1 列）
- 見出し：169+ days late
- 例1 値：3680 | 107170 | 3640 | 380 | 1250
  - 同じ表の列：Province/Territory, Filing Method, On time returns, 1-7 days late, 8-28 days late, 29-56 days late, 57-112 days late, 113-168 days late

## g1424（1 列）
- 見出し：All late returns
- 例1 値：0 | 250 | 490 | 2960 | 32620
  - 同じ表の列：Province/Territory, Filing Method, On time returns, 1-7 days late, 8-28 days late, 29-56 days late, 57-112 days late, 113-168 days late

## g1425（1 列）
- 見出し：title_translated_en
- 例1 値：Notice to Importers Butter, Dairy Sprea… | CPTPP Butter Quota Holders List - 2023-… | CUSMA: Butter and Cream Powder TRQ - Se… | CPTPP Butter Quota Holders List - 2022-… | CPTPP Butter Quota Holders List - 2019-…
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g1426（1 列）
- 見出し：title_translated_fr
- 例1 値：2019-2020 – Crème, poudre de lactosésum… | OMC : CT du Beurre, pâtes à tartiner la… | Liste des détenteurs de contingent pour… | Avis Articles 159, 159.1 et 160 - Beurr… | PTPGP : CT du beurre – No de série : 97…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g1427（1 列）
- 見出し：notes_translated_en
- 例1 値：WTO: Butter, Dairy Spreads, Fats and Oi… | CUSMA Butter and Cream Powder Quota Hol… | CPTPP Butter Quota Holders List | CUSMA: Butter and Cream Powder TRQ | WTO: Butter, Dairy Spreads, Fats and Oi…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g1428（1 列）
- 見出し：notes_translated_fr
- 例1 値：ACEUM : CT pour le beurre et la crème e… | Liste des détenteurs de contingent pour… | 1.1 Le present Avis a pour objet: a. D'… | ACEUM : CT pour le beurre et la crème e… | Liste des détenteurs de contingent pour…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g1429（1 列）
- 見出し：Code
- 例1 値：A.01.e.02 | J.01.b.02 | G.03.a | G.04 | A.04.b.01
  - 同じ表の列：Structure Type

## g1430（1 列）
- 見出し：Structure Type
- 例1 値：Similarity Group | Descriptor | Descriptor | Descriptor | Descriptor
  - 同じ表の列：Code

## g1431（1 列）
- 見出し：arena
- 例1 値：OT-1 | OT-1 | OT-1 | OT-1 | OT-1
  - 同じ表の列：sdt, edt, dt, co_ppm, no2_ppm, zamboni_stime, zamboni_etime, centreice_stime

## g1432（1 列）
- 見出し：sdt
- 例1 値：09NOV17:11:02:00 | 07NOV17:11:23:37 | 06NOV17:14:56:00 | 08NOV17:12:05:13 | 09NOV17:11:22:08
  - 同じ表の列：arena, edt, dt, co_ppm, no2_ppm, zamboni_stime, zamboni_etime, centreice_stime

## g1433（1 列）
- 見出し：edt
- 例1 値：10NOV17:10:52:56 | 12NOV17:16:35:00 | 08NOV17:10:14:28 | 09NOV17:11:11:02 | 09NOV17:11:11:02
  - 同じ表の列：arena, sdt, dt, co_ppm, no2_ppm, zamboni_stime, zamboni_etime, centreice_stime

## g1434（1 列）
- 見出し：dt
- 例1 値：09NOV17:19:42:25 | 07NOV17:12:43:40 | 07NOV17:20:58:58 | 06NOV17:15:05:46 | 08NOV17:20:45:30
  - 同じ表の列：arena, sdt, edt, co_ppm, no2_ppm, zamboni_stime, zamboni_etime, centreice_stime

## g1435（1 列）
- 見出し：co_ppm
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：arena, sdt, edt, dt, no2_ppm, zamboni_stime, zamboni_etime, centreice_stime

## g1436（1 列）
- 見出し：no2_ppm
- 例1 値：0.05 | 0.04 | 0.05 | 0 | 0.07
  - 同じ表の列：arena, sdt, edt, dt, co_ppm, zamboni_stime, zamboni_etime, centreice_stime

## g1437（1 列）
- 見出し：zamboni_stime
- 例1 値：9:44 | 10:00 | 19:50 | 14:50 | 19:50
  - 同じ表の列：arena, sdt, edt, dt, co_ppm, no2_ppm, zamboni_etime, centreice_stime

## g1438（1 列）
- 見出し：zamboni_etime
- 例1 値：15:00 | 14:55 | 9:20 | 10:40 | 9:54
  - 同じ表の列：arena, sdt, edt, dt, co_ppm, no2_ppm, zamboni_stime, centreice_stime

## g1439（1 列）
- 見出し：centreice_stime
- 例1 値：15:10 | 20:10 | 14:56 | 9:40 | 15:10
  - 同じ表の列：arena, sdt, edt, dt, co_ppm, no2_ppm, zamboni_stime, zamboni_etime

## g1440（1 列）
- 見出し：centreice_etime
- 例1 値：16:35:00.00 | 20:40:00.00 | 10:45:00.00 | 20:40:00.00 | 16:35:00.00
  - 同じ表の列：arena, sdt, edt, dt, co_ppm, no2_ppm, zamboni_stime, zamboni_etime

## 答えの雛形

```
g1321	
g1322	
g1323	
g1324	
g1325	
g1326	
g1327	
g1328	
g1329	
g1330	
g1331	
g1332	
g1333	
g1334	
g1335	
g1336	
g1337	
g1338	
g1339	
g1340	
g1341	
g1342	
g1343	
g1344	
g1345	
g1346	
g1347	
g1348	
g1349	
g1350	
g1351	
g1352	
g1353	
g1354	
g1355	
g1356	
g1357	
g1358	
g1359	
g1360	
g1361	
g1362	
g1363	
g1364	
g1365	
g1366	
g1367	
g1368	
g1369	
g1370	
g1371	
g1372	
g1373	
g1374	
g1375	
g1376	
g1377	
g1378	
g1379	
g1380	
g1381	
g1382	
g1383	
g1384	
g1385	
g1386	
g1387	
g1388	
g1389	
g1390	
g1391	
g1392	
g1393	
g1394	
g1395	
g1396	
g1397	
g1398	
g1399	
g1400	
g1401	
g1402	
g1403	
g1404	
g1405	
g1406	
g1407	
g1408	
g1409	
g1410	
g1411	
g1412	
g1413	
g1414	
g1415	
g1416	
g1417	
g1418	
g1419	
g1420	
g1421	
g1422	
g1423	
g1424	
g1425	
g1426	
g1427	
g1428	
g1429	
g1430	
g1431	
g1432	
g1433	
g1434	
g1435	
g1436	
g1437	
g1438	
g1439	
g1440	
```
