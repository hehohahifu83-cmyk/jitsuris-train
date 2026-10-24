# ラベル用シート 014 / 014

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_014.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1561（1 列）
- 見出し：Layer
- 例1 値：Sublayer | Sublayer | Sublayer | Sublayer | Sublayer
  - 同じ表の列：Project Lead, Date Sampled, SiteType, Sample Prep = fine …, Sample Location ID, Datum/ EPSG, Method of collectin…, State (eg NSW, QLD)

## g1562（1 列）
- 見出し：Sample Prep = fine earth <2mm (FE) or whole soil >2mm (WS)
- 例1 値：FE | FE | FE | FE | FE
  - 同じ表の列：Project Lead, Date Sampled, SiteType, Layer, Sample Location ID, Datum/ EPSG, Method of collectin…, State (eg NSW, QLD)

## g1563（1 列）
- 見出し：Sample Location ID
- 例1 値：581 | 18 | 85 | 511 | 733
  - 同じ表の列：Project Lead, Date Sampled, SiteType, Layer, Sample Prep = fine …, Datum/ EPSG, Method of collectin…, State (eg NSW, QLD)

## g1564（1 列）
- 見出し：Datum/ EPSG
- 例1 値：GDA2020 | GDA2020 | GDA2020 | GDA94 | GDA2020
  - 同じ表の列：Project Lead, Date Sampled, SiteType, Layer, Sample Prep = fine …, Sample Location ID, Method of collectin…, State (eg NSW, QLD)

## g1565（1 列）
- 見出し：Method of collecting coordites
- 例1 値：Handheld GPS | Handheld GPS | Handheld GPS | Handheld GPS | Handheld GPS
  - 同じ表の列：Project Lead, Date Sampled, SiteType, Layer, Sample Prep = fine …, Sample Location ID, Datum/ EPSG, State (eg NSW, QLD)

## g1566（1 列）
- 見出し：State (eg NSW, QLD)
- 例1 値：QLD | WA | WA | WA | WA
  - 同じ表の列：Project Lead, Date Sampled, SiteType, Layer, Sample Prep = fine …, Sample Location ID, Datum/ EPSG, Method of collectin…

## g1567（1 列）
- 見出し：Location geographic context (eg; Bega, Wagga Wagga)
- 例1 値：West Casuris | Alpha | Bogie | West Casuris | West Casuris
  - 同じ表の列：Project Lead, Date Sampled, SiteType, Layer, Sample Prep = fine …, Sample Location ID, Datum/ EPSG, Method of collectin…

## g1568（1 列）
- 見出し：Age_Group
- 例1 値：10-12 years | 07-09 years | Over 16 years | 04-06 years | 13-16 years
  - 同じ表の列：Gender, 2012, 2013, 2014, 2015, 2016, 2017, 2018

## g1569（1 列）
- 見出し：Gender
- 例1 値：Female | Male | Male | Female | Female
  - 同じ表の列：Age_Group, 2012, 2013, 2014, 2015, 2016, 2017, 2018

## g1570（1 列）
- 見出し：2012
- 例1 値：111 | 178 | 140 | 66 | 1620
  - 同じ表の列：Age_Group, Gender, 2013, 2014, 2015, 2016, 2017, 2018

## g1571（1 列）
- 見出し：2013
- 例1 値：735 | 557 | 34 | 140 | 195
  - 同じ表の列：Age_Group, Gender, 2012, 2014, 2015, 2016, 2017, 2018

## g1572（1 列）
- 見出し：2014
- 例1 値：139 | 520 | 150 | 85 | 694
  - 同じ表の列：Age_Group, Gender, 2012, 2013, 2015, 2016, 2017, 2018

## g1573（1 列）
- 見出し：2015
- 例1 値：763 | 567 | 1320 | 24 | 202
  - 同じ表の列：Age_Group, Gender, 2012, 2013, 2014, 2016, 2017, 2018

## g1574（1 列）
- 見出し：2016
- 例1 値：48 | 183 | 158 | 150 | 459
  - 同じ表の列：Age_Group, Gender, 2012, 2013, 2014, 2015, 2017, 2018

## g1575（1 列）
- 見出し：2017
- 例1 値：102 | 26 | 47 | 644 | 165
  - 同じ表の列：Age_Group, Gender, 2012, 2013, 2014, 2015, 2016, 2018

## g1576（1 列）
- 見出し：2018
- 例1 値：197 | 175 | 32 | 533 | 103
  - 同じ表の列：Age_Group, Gender, 2012, 2013, 2014, 2015, 2016, 2017

## g1577（1 列）
- 見出し：VALIDATION_DATE
- 例1 値：9/10/2025 | 17/11/2025 | 17/11/2025 | 1/12/2025 | 17/11/2025
  - 同じ表の列：NUM_MODE_TRANSPORT, ROUTE_CODE, ROUTE_DIRECTION, GTFS_ID, MEDIUM_TYPE, BAND_BOARDINGS, BAND_BOARDINGS_FLOOR

## g1578（1 列）
- 見出し：NUM_MODE_TRANSPORT
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：VALIDATION_DATE, ROUTE_CODE, ROUTE_DIRECTION, GTFS_ID, MEDIUM_TYPE, BAND_BOARDINGS, BAND_BOARDINGS_FLOOR

## g1579（1 列）
- 見出し：ROUTE_CODE
- 例1 値：147 | NOAR | J1A | T722 | 541G
  - 同じ表の列：VALIDATION_DATE, NUM_MODE_TRANSPORT, ROUTE_DIRECTION, GTFS_ID, MEDIUM_TYPE, BAND_BOARDINGS, BAND_BOARDINGS_FLOOR

## g1580（1 列）
- 見出し：ROUTE_DIRECTION
- 例1 値：2 | 1 | 2 | 2 | 1
  - 同じ表の列：VALIDATION_DATE, NUM_MODE_TRANSPORT, ROUTE_CODE, GTFS_ID, MEDIUM_TYPE, BAND_BOARDINGS, BAND_BOARDINGS_FLOOR

## g1581（1 列）
- 見出し：GTFS_ID
- 例1 値：101454 | 3096 | 3822 | 3362 | 4650
  - 同じ表の列：VALIDATION_DATE, NUM_MODE_TRANSPORT, ROUTE_CODE, ROUTE_DIRECTION, MEDIUM_TYPE, BAND_BOARDINGS, BAND_BOARDINGS_FLOOR

## g1582（1 列）
- 見出し：MEDIUM_TYPE
- 例1 値：11 | 1 | 1 | 1 | 1
  - 同じ表の列：VALIDATION_DATE, NUM_MODE_TRANSPORT, ROUTE_CODE, ROUTE_DIRECTION, GTFS_ID, BAND_BOARDINGS, BAND_BOARDINGS_FLOOR

## g1583（1 列）
- 見出し：BAND_BOARDINGS
- 例1 値：1-9 | 250-259 | 10-19 | 1-9 | 1-9
  - 同じ表の列：VALIDATION_DATE, NUM_MODE_TRANSPORT, ROUTE_CODE, ROUTE_DIRECTION, GTFS_ID, MEDIUM_TYPE, BAND_BOARDINGS_FLOOR

## g1584（1 列）
- 見出し：BAND_BOARDINGS_FLOOR
- 例1 値：1 | 1 | 1 | 80 | 1
  - 同じ表の列：VALIDATION_DATE, NUM_MODE_TRANSPORT, ROUTE_CODE, ROUTE_DIRECTION, GTFS_ID, MEDIUM_TYPE, BAND_BOARDINGS

## g1585（1 列）
- 見出し：DIS_SITE_CODE
- 例1 値：CA80 | D990 | FL10 | BHGZ | CS90
  - 同じ表の列：SITE_STATE_CD, ESA_CD_1

## g1586（1 列）
- 見出し：SITE_STATE_CD
- 例1 値：QLD | QLD | SA | NSW | VIC
  - 同じ表の列：DIS_SITE_CODE, ESA_CD_1

## g1587（1 列）
- 見出し：ESA_CD_1
- 例1 値：5RHN | 5TAS | 5CTW | 5PEW | QSWR
  - 同じ表の列：DIS_SITE_CODE, SITE_STATE_CD

## g1588（2 列）
- 見出し：Executive Classification
- 例1 値：SAES2 | EXEC0E | SAES1 | EXEC0E | SAES1
  - 同じ表の列：Financial Year, Quantity
- 例2 値：SAES2 | SAES1 | SAES1 | SAES2 | EXEC0F
  - 同じ表の列：Year, Number of Executives

## g1589（1 列）
- 見出し：Financial Year
- 例1 値：2012-13 | 2014-15 | 2015-16 | 2016-17 | 2015-16
  - 同じ表の列：Executive Classific…, Quantity

## g1590（1 列）
- 見出し：Quantity
- 例1 値：1 | 31 | 34 | 0 | 1
  - 同じ表の列：Executive Classific…, Financial Year

## g1591（1 列）
- 見出し：Number of Executives
- 例1 値：17 | 18 | 1 | 1 | 16
  - 同じ表の列：Year, Executive Classific…

## g1592（1 列）
- 見出し：CD_MAKE_VEH1
- 例1 値：B M W | SUBARU | PEUG | MAZDA | TOYOTA
  - 同じ表の列：CD_MODEL_VEH, CD_CLR_BDY_VEH_P, NB_YEAR_MFC_VEH, TOTAL1

## g1593（1 列）
- 見出し：CD_MODEL_VEH
- 例1 値：000003 | 125I | 000009 | 1500 | 200 DU
  - 同じ表の列：CD_MAKE_VEH1, CD_CLR_BDY_VEH_P, NB_YEAR_MFC_VEH, TOTAL1

## g1594（1 列）
- 見出し：TOTAL1
- 例1 値：1 | 3 | 2 | 1 | 1
  - 同じ表の列：CD_MAKE_VEH1, CD_MODEL_VEH, CD_CLR_BDY_VEH_P, NB_YEAR_MFC_VEH

## g1595（1 列）
- 見出し：Sitc 3 digit
- 例1 値：046 Wheat flour | 022 Milk, cream, whey & yoghurt | 073 Chocolate & preparations of cocoa | 011 Beef, f.c.f. | 073 Chocolate & preparations of cocoa
  - 同じ表の列：Year, Trade type, State, Partner country, Geographic level 1, Geographic level 2, Geographic level 3, APEC

## g1596（1 列）
- 見出し：Geographic level 1
- 例1 値：Asia | Asia | Asia | Asia | Asia
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Partner country, Geographic level 2, Geographic level 3, APEC

## g1597（1 列）
- 見出し：Geographic level 3
- 例1 値：North Asia | North America | North Asia | South East Asia | North Asia
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 2, APEC

## g1598（1 列）
- 見出し：Business Category
- 例1 値：State body,Volunteering | Volunteering | Volunteering | Volunteering | Volunteering
  - 同じ表の列：Suburb, State, LGA, Region

## g1599（1 列）
- 見出し：LGA
- 例1 値：Port Phillip | Hume | South Gippsland (S) | Murrindindi (S) | Melton
  - 同じ表の列：Suburb, State, Business Category, Region

## g1600（1 列）
- 見出し：Region
- 例1 値：Loddon-Mallee | Eastern Metro | North and West Metropolitan Region | Loddon-Mallee | Gippsland Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g1601（1 列）
- 見出し：No consultants were engaged.
- 例1 値：Nil to report | 2022-23 | Consultancies below $10 000 each | 2019-20 | Consultancies above $10 000 each
  - 同じ表の列：Number, Total $

## g1602（1 列）
- 見出し：Number
- 例1 値：Policy development support | Learning and development services | Purpose | Internal audit function | Purpose
  - 同じ表の列：No consultants were…, Total $

## g1603（1 列）
- 見出し：Total $
- 例1 値：$ Actual payment | 38,850 | Total $ | Total $ | $ Actual payment
  - 同じ表の列：No consultants were…, Number

## g1604（1 列）
- 見出し：Date Time
- 例1 値：2026-04-01T17:20:00 | 2026-05-01T19:50:00 | 2026-01-01T09:00:00 | 2026-01-01T13:20:00 | 2026-03-01T17:50:00
  - 同じ表の列：Temperature Deg_C, TSR W/m2, Barometric Pressure…, Wind Speed m/s, Wind Direction deg, Dew Point Deg_C, Relative Humidity %, Wind Vector E/W m/s

## g1605（1 列）
- 見出し：Temperature Deg_C
- 例1 値：13.1 | 24.2 | 19.3 | 21.6 | 22.6
  - 同じ表の列：Date Time, TSR W/m2, Barometric Pressure…, Wind Speed m/s, Wind Direction deg, Dew Point Deg_C, Relative Humidity %, Wind Vector E/W m/s

## g1606（1 列）
- 見出し：TSR W/m2
- 例1 値：641 | 871 | 141 | 255 | 823
  - 同じ表の列：Date Time, Temperature Deg_C, Barometric Pressure…, Wind Speed m/s, Wind Direction deg, Dew Point Deg_C, Relative Humidity %, Wind Vector E/W m/s

## g1607（1 列）
- 見出し：Barometric Pressure hPa
- 例1 値：1013.2 | 1012.5 | 1011.6 | 1010.3 | 1009.9
  - 同じ表の列：Date Time, Temperature Deg_C, TSR W/m2, Wind Speed m/s, Wind Direction deg, Dew Point Deg_C, Relative Humidity %, Wind Vector E/W m/s

## g1608（1 列）
- 見出し：Wind Speed m/s
- 例1 値：1.4 | 1.8 | 1.0 | 0.9 | 1.5
  - 同じ表の列：Date Time, Temperature Deg_C, TSR W/m2, Barometric Pressure…, Wind Direction deg, Dew Point Deg_C, Relative Humidity %, Wind Vector E/W m/s

## g1609（1 列）
- 見出し：Wind Direction deg
- 例1 値：140 | 41 | 330 | 187 | 60
  - 同じ表の列：Date Time, Temperature Deg_C, TSR W/m2, Barometric Pressure…, Wind Speed m/s, Dew Point Deg_C, Relative Humidity %, Wind Vector E/W m/s

## g1610（1 列）
- 見出し：Dew Point Deg_C
- 例1 値：10.6 | 8.4 | 11.0 | 3.3 | 4.5
  - 同じ表の列：Date Time, Temperature Deg_C, TSR W/m2, Barometric Pressure…, Wind Speed m/s, Wind Direction deg, Relative Humidity %, Wind Vector E/W m/s

## g1611（1 列）
- 見出し：Relative Humidity %
- 例1 値：19 | 27 | 67 | 12 | 51
  - 同じ表の列：Date Time, Temperature Deg_C, TSR W/m2, Barometric Pressure…, Wind Speed m/s, Wind Direction deg, Dew Point Deg_C, Wind Vector E/W m/s

## g1612（1 列）
- 見出し：Wind Vector E/W m/s
- 例1 値：1.028 | -1.395 | 0.065 | 0.114 | 0.277
  - 同じ表の列：Date Time, Temperature Deg_C, TSR W/m2, Barometric Pressure…, Wind Speed m/s, Wind Direction deg, Dew Point Deg_C, Relative Humidity %

## g1613（1 列）
- 見出し：Wind Vector N/S m/s
- 例1 値：2.681 | -0.229 | -0.822 | -0.963 | -0.815
  - 同じ表の列：Date Time, Temperature Deg_C, TSR W/m2, Barometric Pressure…, Wind Speed m/s, Wind Direction deg, Dew Point Deg_C, Relative Humidity %

## g1614（1 列）
- 見出し：Whistle-blowers Disclosures
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year

## g1615（1 列）
- 見出し：pump_type
- 例1 値：Screw Pump | Not Applicable | Not Applicable | Not Applicable | Not Applicable
  - 同じ表の列：ref

## g1616（1 列）
- 見出し：Location
- 例1 値：Cherry Lake Reserve | Truganina Park | Hatt Reserve | Sadler Reserve | Frazer, R. Reserve
  - 同じ表の列：Suburb, Setting_Type, Material

## g1617（1 列）
- 見出し：Setting_Type
- 例1 値：2 Seat Picnic Setting | 2 Seat Picnic Setting | 2 Seat Picnic Setting | 2 Seat Picnic Setting | 2 Seat Picnic Setting
  - 同じ表の列：Location, Suburb, Material

## g1618（1 列）
- 見出し：Material
- 例1 値：Timber | Timber | Steel/Timber | Timber | Steel/Timber
  - 同じ表の列：Location, Suburb, Setting_Type

## g1619（1 列）
- 見出し：Regulation
- 例1 値：Horsham Rural City Council | Horsham Rural City Council | Horsham Rural City Council | Horsham Rural City Council | Horsham Rural City Council
  - 同じ表の列：Id, Status, X, Y

## g1620（1 列）
- 見出し：ip_office
- 例1 値：au | au | au | au | au
  - 同じ表の列：application_number

## g1621（1 列）
- 見出し：application_number
- 例1 値：867624 | 507243 | 1355589 | 2004830 | 1114329
  - 同じ表の列：ip_office

## g1622（1 列）
- 見出し：Reporting period
- 例1 値：FY25-26 | FY25-26 | FY25-26 | FY25-26 | FY25-26
  - 同じ表の列：Engagement expendit…, Purpose of engageme…, Benefits of engagem…

## g1623（1 列）
- 見出し：Engagement expenditure incurred during the reporting period
- 例1 値：127136.36 | 133000.00 | 60000.00 | 815000.00 | 28600.00
  - 同じ表の列：Reporting period, Purpose of engageme…, Benefits of engagem…

## g1624（1 列）
- 見出し：Purpose of engagement
- 例1 値：Strategic review of the Electoral Commi… | Forensic Science Queensland Review | Forensic Science Queensland Review | Forensic Science Queensland Review | Queensland Civil and Administrative Tri…
  - 同じ表の列：Reporting period, Engagement expendit…, Benefits of engagem…

## g1625（1 列）
- 見出し：Benefits of engagement
- 例1 値：Queensland Human Rights Act 2019 - revi… | Review of Forensic Science Queensland w… | Review of Forensic Science Queensland w… | For the provision of services as an exp… | Electoral Act 1992 - review required un…
  - 同じ表の列：Reporting period, Engagement expendit…, Purpose of engageme…

## g1626（1 列）
- 見出し：HOUSE_NO
- 例1 値：3 | 15 | 437 | 2 | 17
  - 同じ表の列：STR_TYPE, SUBURB, INSP_DATE, IDNO, POLE_TYPE, SIGN_HT, SIGN_TYPE, ASSETID

## g1627（1 列）
- 見出し：STR_TYPE
- 例1 値：Rd | Lane | Rd | Str | Rd
  - 同じ表の列：HOUSE_NO, SUBURB, INSP_DATE, IDNO, POLE_TYPE, SIGN_HT, SIGN_TYPE, ASSETID

## g1628（1 列）
- 見出し：INSP_DATE
- 例1 値：16/06/2006 | 16/06/2006 | 15/06/2006 | 14/06/2006 | 16/06/2006
  - 同じ表の列：HOUSE_NO, STR_TYPE, SUBURB, IDNO, POLE_TYPE, SIGN_HT, SIGN_TYPE, ASSETID

## g1629（1 列）
- 見出し：IDNO
- 例1 値：7.06 | 3.27 | 11.04 | 2.07 | 7.15
  - 同じ表の列：HOUSE_NO, STR_TYPE, SUBURB, INSP_DATE, POLE_TYPE, SIGN_HT, SIGN_TYPE, ASSETID

## g1630（1 列）
- 見出し：POLE_TYPE
- 例1 値：Street | Street | Power Pole | Power Pole | Power Pole
  - 同じ表の列：HOUSE_NO, STR_TYPE, SUBURB, INSP_DATE, IDNO, SIGN_HT, SIGN_TYPE, ASSETID

## g1631（1 列）
- 見出し：SIGN_HT
- 例1 値：Above 2.1m | Above 2.1m | Above 2.1m | Above 2.1m | Above 2.1m
  - 同じ表の列：HOUSE_NO, STR_TYPE, SUBURB, INSP_DATE, IDNO, POLE_TYPE, SIGN_TYPE, ASSETID

## g1632（1 列）
- 見出し：SIGN_TYPE
- 例1 値：Blade Suburb Sign | Blade Suburb Sign | Blade Suburb Sign | Blade Suburb Sign | Blade Suburb Sign
  - 同じ表の列：HOUSE_NO, STR_TYPE, SUBURB, INSP_DATE, IDNO, POLE_TYPE, SIGN_HT, ASSETID

## g1633（1 列）
- 見出し：ASSETID
- 例1 値：SF000115 | SF000216 | SF000141 | SF000088 | SF000103
  - 同じ表の列：HOUSE_NO, STR_TYPE, SUBURB, INSP_DATE, IDNO, POLE_TYPE, SIGN_HT, SIGN_TYPE

## g1634（1 列）
- 見出し：SiteID
- 例1 値：60262 | 60252 | 60005 | 60253 | 60004
  - 同じ表の列：ProgramID, dateSamplingCommenc…, MethodCode, operationCode, TaxaCode, Abundance, inTimeStamp, isBiomassCalculated

## g1635（1 列）
- 見出し：ProgramID
- 例1 値：PRG0001 | PRG0001 | PRG0001 | PRG0001 | PRG0403
  - 同じ表の列：SiteID, dateSamplingCommenc…, MethodCode, operationCode, TaxaCode, Abundance, inTimeStamp, isBiomassCalculated

## g1636（1 列）
- 見出し：dateSamplingCommenced
- 例1 値：01/21/08 00:00:00 | 04/19/05 00:00:00 | 02/01/05 00:00:00 | 04/05/05 00:00:00 | 01/31/05 00:00:00
  - 同じ表の列：SiteID, ProgramID, MethodCode, operationCode, TaxaCode, Abundance, inTimeStamp, isBiomassCalculated

## g1637（1 列）
- 見出し：MethodCode
- 例1 値：EBP | BA | BA | BPV | EBP
  - 同じ表の列：SiteID, ProgramID, dateSamplingCommenc…, operationCode, TaxaCode, Abundance, inTimeStamp, isBiomassCalculated

## g1638（1 列）
- 見出し：operationCode
- 例1 値：6 | 13 | B4 | 19 | A3
  - 同じ表の列：SiteID, ProgramID, dateSamplingCommenc…, MethodCode, TaxaCode, Abundance, inTimeStamp, isBiomassCalculated

## g1639（1 列）
- 見出し：inTimeStamp
- 例1 値：12/10/08 16:52:00 | 08/14/05 10:10:00 | 08/14/05 10:10:00 | 08/14/05 10:10:00 | 08/14/05 10:10:00
  - 同じ表の列：SiteID, ProgramID, dateSamplingCommenc…, MethodCode, operationCode, TaxaCode, Abundance, isBiomassCalculated

## g1640（1 列）
- 見出し：isBiomassCalculated
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：SiteID, ProgramID, dateSamplingCommenc…, MethodCode, operationCode, TaxaCode, Abundance, inTimeStamp

## g1641（1 列）
- 見出し：weightSource
- 例1 値：Calc | Calc | Calc | Calc | Estimate
  - 同じ表の列：SiteID, ProgramID, dateSamplingCommenc…, MethodCode, operationCode, TaxaCode, Abundance, inTimeStamp

## g1642（1 列）
- 見出し：Local Government
- 例1 値：Douglas Shire Council | Toowoomba Regional Council | South Burnett Regional Council | Toowoomba Regional Council | Rockhampton Regional Council
  - 同じ表の列：Closing Date for Ob…, Case Number, Road, Locality, Item Type, Path

## g1643（1 列）
- 見出し：Closing Date for Objections
- 例1 値：2026-07-02 | 2026-07-09 | 2026-07-09 | 2026-07-09 | 2026-07-16
  - 同じ表の列：Local Government, Case Number, Road, Locality, Item Type, Path

## g1644（1 列）
- 見出し：Case Number
- 例1 値：2026/000223 | 2026/000221 | 2026/000078 | 2026/000219 | 2026/000514
  - 同じ表の列：Local Government, Closing Date for Ob…, Road, Locality, Item Type, Path

## g1645（1 列）
- 見出し：Road
- 例1 値：Hazelwood | Part of Owens Scrub Road | part of Costigan Street | Part of King Road | unnamed road off Rubys Road
  - 同じ表の列：Local Government, Closing Date for Ob…, Case Number, Locality, Item Type, Path

## g1646（1 列）
- 見出し：Item Type
- 例1 値：Item | Item | Item | Item | Item
  - 同じ表の列：Local Government, Closing Date for Ob…, Case Number, Road, Locality, Path

## g1647（1 列）
- 見出し：Path
- 例1 値：sites/SLAM/Advertising/Advertisements | sites/SLAM/Advertising/Advertisements | sites/SLAM/Advertising/Advertisements | sites/SLAM/Advertising/Advertisements | sites/SLAM/Advertising/Advertisements
  - 同じ表の列：Local Government, Closing Date for Ob…, Case Number, Road, Locality, Item Type

## g1648（1 列）
- 見出し：AsseID
- 例1 値：FTP126049 | FTP129232 | FTP125353 | FTP125704 | FTP127025
  - 同じ表の列：Type, Asset Status, Asset Category, Asset Criticality, Asset Workgroup, Maintenance Asset T…, Maintenance Asset S…, Asset Suburb

## g1649（1 列）
- 見出し：Asset Status
- 例1 値：Active | Active | Active | Active | Active
  - 同じ表の列：AsseID, Type, Asset Category, Asset Criticality, Asset Workgroup, Maintenance Asset T…, Maintenance Asset S…, Asset Suburb

## g1650（1 列）
- 見出し：Asset Category
- 例1 値：Pathways | Pathways | Pathways | Pathways | Pathways
  - 同じ表の列：AsseID, Type, Asset Status, Asset Criticality, Asset Workgroup, Maintenance Asset T…, Maintenance Asset S…, Asset Suburb

## g1651（1 列）
- 見出し：Asset Criticality
- 例1 値：Cat 2 - Residential & Commercial | Cat 3 - Major Community Facility | Cat 3 - Major Community Facility | Cat 3 - Major Community Facility | Cat 3 - Major Community Facility
  - 同じ表の列：AsseID, Type, Asset Status, Asset Category, Asset Workgroup, Maintenance Asset T…, Maintenance Asset S…, Asset Suburb

## g1652（1 列）
- 見出し：Asset Workgroup
- 例1 値：Infrastructure Operations - Stawell | Infrastructure Operations - Stawell | Infrastructure Operations - St Arnaud | Infrastructure Operations - Stawell | Infrastructure Operations - Stawell
  - 同じ表の列：AsseID, Type, Asset Status, Asset Category, Asset Criticality, Maintenance Asset T…, Maintenance Asset S…, Asset Suburb

## g1653（1 列）
- 見出し：Maintenance Asset Type
- 例1 値：Pathways - Sealed | Pathways - Concrete | Pathways - Concrete | Pathways - Sealed | Pathways - Sealed
  - 同じ表の列：AsseID, Type, Asset Status, Asset Category, Asset Criticality, Asset Workgroup, Maintenance Asset S…, Asset Suburb

## g1654（1 列）
- 見出し：Maintenance Asset Sub Type
- 例1 値：None | None | None | None | None
  - 同じ表の列：AsseID, Type, Asset Status, Asset Category, Asset Criticality, Asset Workgroup, Maintenance Asset T…, Asset Suburb

## g1655（1 列）
- 見出し：Asset Suburb
- 例1 値：Stawell | Stawell | St Arnaud | Stawell | Stawell
  - 同じ表の列：AsseID, Type, Asset Status, Asset Category, Asset Criticality, Asset Workgroup, Maintenance Asset T…, Maintenance Asset S…

## g1656（1 列）
- 見出し：Asset Asset Catalogue
- 例1 値：Transport Infrastructure | Transport Infrastructure | Transport Infrastructure | Transport Infrastructure | Transport Infrastructure
  - 同じ表の列：AsseID, Type, Asset Status, Asset Category, Asset Criticality, Asset Workgroup, Maintenance Asset T…, Maintenance Asset S…

## g1657（1 列）
- 見出し：SA4 Groupings
- 例1 値：Sydney-Inner | Sydney-West | North East NSW | North West NSW | NSW government schools by FOEI bands an…
  - 同じ表の列：Less than 50, 50 to 90, 90 to 110, 110 to 150, 150 or more, N/A, Total, > = 110 (%)

## g1658（1 列）
- 見出し：Less than 50
- 例1 値：26 | 22 | 1 | 126 | 340
  - 同じ表の列：SA4 Groupings, 50 to 90, 90 to 110, 110 to 150, 150 or more, N/A, Total, > = 110 (%)

## g1659（1 列）
- 見出し：50 to 90
- 例1 値：71 | 213 | 28 | 234 | 24
  - 同じ表の列：SA4 Groupings, Less than 50, 90 to 110, 110 to 150, 150 or more, N/A, Total, > = 110 (%)

## g1660（1 列）
- 見出し：90 to 110
- 例1 値：35 | 22 | 38 | 27 | 323
  - 同じ表の列：SA4 Groupings, Less than 50, 50 to 90, 110 to 150, 150 or more, N/A, Total, > = 110 (%)

## g1661（1 列）
- 見出し：110 to 150
- 例1 値：77 | 37 | 128 | 34 | 28
  - 同じ表の列：SA4 Groupings, Less than 50, 50 to 90, 90 to 110, 150 or more, N/A, Total, > = 110 (%)

## g1662（1 列）
- 見出し：150 or more
- 例1 値：22 | 2 | 13 | 8 | 2
  - 同じ表の列：SA4 Groupings, Less than 50, 50 to 90, 90 to 110, 110 to 150, N/A, Total, > = 110 (%)

## g1663（1 列）
- 見出し：N/A
- 例1 値：2 | 18 | 3 | 2 | 1
  - 同じ表の列：SA4 Groupings, Less than 50, 50 to 90, 90 to 110, 110 to 150, 150 or more, Total, > = 110 (%)

## g1664（1 列）
- 見出し：> = 110 (%)
- 例1 値：41.4% | 41.3% | 27.4% | 76.6% | 71.5%
  - 同じ表の列：SA4 Groupings, Less than 50, 50 to 90, 90 to 110, 110 to 150, 150 or more, N/A, Total

## g1665（1 列）
- 見出し：Count
- 例1 値：275 | 229 | 8,984 | 215 | 11,181
  - 同じ表の列：Year, Rank

## 答えの雛形

```
g1561	
g1562	
g1563	
g1564	
g1565	
g1566	
g1567	
g1568	
g1569	
g1570	
g1571	
g1572	
g1573	
g1574	
g1575	
g1576	
g1577	
g1578	
g1579	
g1580	
g1581	
g1582	
g1583	
g1584	
g1585	
g1586	
g1587	
g1588	
g1589	
g1590	
g1591	
g1592	
g1593	
g1594	
g1595	
g1596	
g1597	
g1598	
g1599	
g1600	
g1601	
g1602	
g1603	
g1604	
g1605	
g1606	
g1607	
g1608	
g1609	
g1610	
g1611	
g1612	
g1613	
g1614	
g1615	
g1616	
g1617	
g1618	
g1619	
g1620	
g1621	
g1622	
g1623	
g1624	
g1625	
g1626	
g1627	
g1628	
g1629	
g1630	
g1631	
g1632	
g1633	
g1634	
g1635	
g1636	
g1637	
g1638	
g1639	
g1640	
g1641	
g1642	
g1643	
g1644	
g1645	
g1646	
g1647	
g1648	
g1649	
g1650	
g1651	
g1652	
g1653	
g1654	
g1655	
g1656	
g1657	
g1658	
g1659	
g1660	
g1661	
g1662	
g1663	
g1664	
g1665	
```
