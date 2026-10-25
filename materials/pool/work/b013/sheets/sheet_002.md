# ラベル用シート 002 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：type
- 例1 値：Rubber Flap Steel Frame | Rubber Flap Steel Frame | Rubber Flap Steel Frame | Rubber Flap Steel Frame | Rubber Flap Steel Frame
  - 同じ表の列：ref

## g0122（6 列）
- 見出し：Year
- 例1 値：2021-22 | 2020-21 | 2019-20 | 2021-22 | 2021-22
  - 同じ表の列：services provided, value ($)
- 例2 値：2020-21 | 2023-24 | 2018-19 | 2014-15 | 2005-06
  - 同じ表の列：Revenue ($ million)

## g0123（1 列）
- 見出し：services provided
- 例1 値：Asset management consultancy | SAHA contribution for National consulta… | Cyber security internal audit | Crane and equipment hire | Commercial and financial advisory for B…
  - 同じ表の列：Year, value ($)

## g0124（1 列）
- 見出し：value ($)
- 例1 値：122,622.86 | 19,592.43 | 14,522.20 | $103,460 | 1,202,222.50
  - 同じ表の列：Year, services provided

## g0125（1 列）
- 見出し：X Values
- 例1 値：Lead and compounds | PM_{10} | Oxides of nitrogen | Total VOCs | Sulfur dioxide
  - 同じ表の列：Diesel, Petrol, %Diesel, %Petrol

## g0126（1 列）
- 見出し：Diesel
- 例1 値：0.15926761936021 | 0.909378153046068 | 0.06730303375616 | 0.832571291998202 | 0.907908831574866
  - 同じ表の列：X Values, Petrol, %Diesel, %Petrol

## g0127（1 列）
- 見出し：Petrol
- 例1 値：0.092091168425135 | 0.93269696624384 | 0.416029664960515 | 0.090621846953932 | 0.852506170011941
  - 同じ表の列：X Values, Diesel, %Diesel, %Petrol

## g0128（1 列）
- 見出し：%Diesel
- 例1 値：6.730303375616 | 15.926761936021 | 58.3970335039485 | 90.9378153046068 | 83.2571291998202
  - 同じ表の列：X Values, Diesel, Petrol, %Petrol

## g0129（1 列）
- 見出し：%Petrol
- 例1 値：41.6029664960515 | 93.269696624384 | 85.2506170011941 | 9.20911684251344 | 16.7428708001798
  - 同じ表の列：X Values, Diesel, Petrol, %Diesel

## g0130（1 列）
- 見出し：Hour
- 例1 値：12 | 0 | 50 | 29 | 66
  - 同じ表の列：Nox

## g0131（1 列）
- 見出し：Nox
- 例1 値：7.60E-01 | 1.75E-01 | 8.12E-01 | 1.35E-02 | 6.09E-01
  - 同じ表の列：Hour

## g0132（1 列）
- 見出し：Year
- 例1 値：Total VOCS | NOx | CO | SO_2 | PM_{2.5}
  - 同じ表の列：2015, 2016, 2017, 2018, 2019

## g0133（2 列）
- 見出し：2015
- 例1 値：940000000 | 32000000 | 1100000000 | 100000000 | 660000000
  - 同じ表の列：Year, 2016, 2017, 2018, 2019
- 例2 値：21 | 17 | 23 | 23 | 17
  - 同じ表の列：Class_Type, 2014, 2016, 2017, 2018, 2019, 2020, 2021

## g0134（3 列）
- 見出し：2016
- 例1 値：970000000 | 950000000 | 710000000 | 100000000 | 29000000
  - 同じ表の列：Year, 2015, 2017, 2018, 2019
- 例2 値：22 | 23 | 12 | 24 | 23
  - 同じ表の列：Class_Type, 2014, 2015, 2017, 2018, 2019, 2020, 2021

## g0135（3 列）
- 見出し：2017
- 例1 値：710000000 | 730000000 | 890000000 | 31000000 | 110000000
  - 同じ表の列：Year, 2015, 2016, 2018, 2019
- 例2 値：20 | 23 | 23 | 24 | 13
  - 同じ表の列：Class_Type, 2014, 2015, 2016, 2018, 2019, 2020, 2021

## g0136（3 列）
- 見出し：2018
- 例1 値：29000000 | 680000000 | 130000000 | 930000000 | 840000000
  - 同じ表の列：Year, 2015, 2016, 2017, 2019
- 例2 値：22 | 16 | 23 | 21 | 22
  - 同じ表の列：Class_Type, 2014, 2015, 2016, 2017, 2019, 2020, 2021

## g0137（3 列）
- 見出し：2019
- 例1 値：760000000 | 750000000 | 30000000 | 130000000 | 980000000
  - 同じ表の列：Year, 2015, 2016, 2017, 2018
- 例2 値：21 | 14 | 22 | 20 | 24
  - 同じ表の列：Class_Type, 2014, 2015, 2016, 2017, 2018, 2020, 2021

## g0138（2 列）
- 見出し：Revenue ($ million)
- 例1 値：44.1 | 103 | 119 | 83.9 | 117
  - 同じ表の列：Year
- 例2 値：544 | 720.1 | 440 | 555.3 | 819.2
  - 同じ表の列：Year

## g0139（1 列）
- 見出し：No.
- 例1 値：2 | 1 | 3 | 4 | 8
  - 同じ表の列：Anticipatory Notice…, Previous_Project_Ar…, Varied-Project_Area, Previous_Service_Ar…, Varied_Service_ Are…, Estimated_ Completi…, ID, Previous_Latlong

## g0140（1 列）
- 見出し：Anticipatory Notice Date Reference
- 例1 値：2024-01-19T00:00:00 | 2024-01-19T00:00:00 | 2024-01-19T00:00:00 | 2024-01-19T00:00:00 | 2024-01-19T00:00:00
  - 同じ表の列：No., Previous_Project_Ar…, Varied-Project_Area, Previous_Service_Ar…, Varied_Service_ Are…, Estimated_ Completi…, ID, Previous_Latlong

## g0141（1 列）
- 見出し：Previous_Project_Area
- 例1 値：Ripley Road | 290 NBR | Halcyon Vista Logan Village | Avid - Logan Reserve SDU | Halcyon Serrata Burpengary
  - 同じ表の列：No., Anticipatory Notice…, Varied-Project_Area, Previous_Service_Ar…, Varied_Service_ Are…, Estimated_ Completi…, ID, Previous_Latlong

## g0142（1 列）
- 見出し：Varied-Project_Area
- 例1 値：Halcyon Vista | Halcyon Dales | Amory | Halcyon Edgebrook | INDI Estate
  - 同じ表の列：No., Anticipatory Notice…, Previous_Project_Ar…, Previous_Service_Ar…, Varied_Service_ Are…, Estimated_ Completi…, ID, Previous_Latlong

## g0143（1 列）
- 見出し：Previous_Service_Area_ Identifier
- 例1 値：ERIP | AVLG | HCYV | IGSB | HCYS
  - 同じ表の列：No., Anticipatory Notice…, Previous_Project_Ar…, Varied-Project_Area, Varied_Service_ Are…, Estimated_ Completi…, ID, Previous_Latlong

## g0144（1 列）
- 見出し：Varied_Service_ Area_Identifier
- 例1 値：n/a | n/a | n/a | n/a | n/a
  - 同じ表の列：No., Anticipatory Notice…, Previous_Project_Ar…, Varied-Project_Area, Previous_Service_Ar…, Estimated_ Completi…, ID, Previous_Latlong

## g0145（1 列）
- 見出し：Estimated_ Completion_Date
- 例1 値：2030-12-01T00:00:00 | 2025-03-31T00:00:00 | 2026-11-01T00:00:00 | 2025-11-01T00:00:00 | 2025-12-31T00:00:00
  - 同じ表の列：No., Anticipatory Notice…, Previous_Project_Ar…, Varied-Project_Area, Previous_Service_Ar…, Varied_Service_ Are…, ID, Previous_Latlong

## g0146（1 列）
- 見出し：Previous_Latlong
- 例1 値：-37.5848965,144.6912308 | -26.8761353,152.9574556 | -27.6878169,152.7955798 | -27.1658425,152.9899018 | -31.5250863,115.6341556
  - 同じ表の列：No., Anticipatory Notice…, Previous_Project_Ar…, Varied-Project_Area, Previous_Service_Ar…, Varied_Service_ Are…, Estimated_ Completi…, ID

## g0147（1 列）
- 見出し：Varied_Latlong
- 例1 値：-30.2976861,153.0705533 | -37.5873192,144.6922959 | -27.7642264,153.1151262 | -26.8748509,152.9588304 | -31.5221891,115.6360907
  - 同じ表の列：No., Anticipatory Notice…, Previous_Project_Ar…, Varied-Project_Area, Previous_Service_Ar…, Varied_Service_ Are…, Estimated_ Completi…, ID

## g0148（1 列）
- 見出し：RevenueasaproportionofGDP201617
- 例1 値：Ofwhichtaxesonpayrollandworkforce | TotalRevenueasaporporitonofGDP | Ofwhichtaxesonproperty | OtherRevenue | Ofwhichtaxesonincomeprofitsandcapitalga…
  - 同じ表の列：201617FY

## g0149（1 列）
- 見出し：201617FY
- 例1 値：5 | 1 | 35 | 16 | 7
  - 同じ表の列：Revenueasaproportio…

## g0150（1 列）
- 見出し：REPORTING_PERIOD
- 例1 値：2026-04-30T00:00:00 | 2023-02-28T00:00:00 | 2024-04-30T00:00:00 | 2025-02-28T00:00:00 | 2023-09-30T00:00:00
  - 同じ表の列：SERIES_KEY, OBSERVATION_FREE, CONFIDENTIALITY_FLAG, FREQ, FREQ_DESC, REF_AREA, REF_AREA_DESC, PYMNT_SCHM

## g0151（1 列）
- 見出し：SERIES_KEY
- 例1 値：PCI.M.IE.W2.PCS_ALL.11.PN | PCI.M.IE.W2.PCS_ALL.13.PN | PCI.M.IE.W2.PCS_ALL.11.PN | PCI.M.IE.W2.PCS_ALL.13.PN | PCI.M.IE.W2.PCS_ALL.11.PN
  - 同じ表の列：REPORTING_PERIOD, OBSERVATION_FREE, CONFIDENTIALITY_FLAG, FREQ, FREQ_DESC, REF_AREA, REF_AREA_DESC, PYMNT_SCHM

## g0152（1 列）
- 見出し：OBSERVATION_FREE
- 例1 値：7645297 | 1566511 | 7920313 | 7998821 | 1614477
  - 同じ表の列：REPORTING_PERIOD, SERIES_KEY, CONFIDENTIALITY_FLAG, FREQ, FREQ_DESC, REF_AREA, REF_AREA_DESC, PYMNT_SCHM

## g0153（1 列）
- 見出し：CONFIDENTIALITY_FLAG
- 例1 値：F | F | F | F | F
  - 同じ表の列：REPORTING_PERIOD, SERIES_KEY, OBSERVATION_FREE, FREQ, FREQ_DESC, REF_AREA, REF_AREA_DESC, PYMNT_SCHM

## g0154（1 列）
- 見出し：FREQ
- 例1 値：M | M | M | M | M
  - 同じ表の列：REPORTING_PERIOD, SERIES_KEY, OBSERVATION_FREE, CONFIDENTIALITY_FLAG, FREQ_DESC, REF_AREA, REF_AREA_DESC, PYMNT_SCHM

## g0155（1 列）
- 見出し：FREQ_DESC
- 例1 値：Monthly | Monthly | Monthly | Monthly | Monthly
  - 同じ表の列：REPORTING_PERIOD, SERIES_KEY, OBSERVATION_FREE, CONFIDENTIALITY_FLAG, FREQ, REF_AREA, REF_AREA_DESC, PYMNT_SCHM

## g0156（1 列）
- 見出し：REF_AREA
- 例1 値：IE | IE | IE | IE | IE
  - 同じ表の列：REPORTING_PERIOD, SERIES_KEY, OBSERVATION_FREE, CONFIDENTIALITY_FLAG, FREQ, FREQ_DESC, REF_AREA_DESC, PYMNT_SCHM

## g0157（1 列）
- 見出し：REF_AREA_DESC
- 例1 値：Ireland | Ireland | Ireland | Ireland | Ireland
  - 同じ表の列：REPORTING_PERIOD, SERIES_KEY, OBSERVATION_FREE, CONFIDENTIALITY_FLAG, FREQ, FREQ_DESC, REF_AREA, PYMNT_SCHM

## g0158（1 列）
- 見出し：PYMNT_SCHM
- 例1 値：PCS_ALL | PCS_ALL | PCS_ALL | PCS_ALL | PCS_ALL
  - 同じ表の列：REPORTING_PERIOD, SERIES_KEY, OBSERVATION_FREE, CONFIDENTIALITY_FLAG, FREQ, FREQ_DESC, REF_AREA, REF_AREA_DESC

## g0159（1 列）
- 見出し：PYMNT_SCHM_DESC
- 例1 値：ALL payment card schemes | ALL payment card schemes | ALL payment card schemes | ALL payment card schemes | ALL payment card schemes
  - 同じ表の列：REPORTING_PERIOD, SERIES_KEY, OBSERVATION_FREE, CONFIDENTIALITY_FLAG, FREQ, FREQ_DESC, REF_AREA, REF_AREA_DESC

## g0160（1 列）
- 見出し：AVERAGE_YEAR
- 例1 値：2020 | 2020 | 2020 | 2020 | 2020
  - 同じ表の列：COUNTY, ELECTORAL_DIVISION, NUMBER_OF_HERDS, AVERAGE_NUMBER_CATT…, AVERAGE_CATTLE_BEEF, AVERAGE_CATTLE_DAIRY, AVERAGE_CATTLE_AGE_…, AVERAGE_CATTLE_AGE_…

## g0161（5 列）
- 見出し：COUNTY
- 例1 値：DONEGAL | DONEGAL | GALWAY | DONEGAL | CAVAN
  - 同じ表の列：AVERAGE_YEAR, ELECTORAL_DIVISION, NUMBER_OF_HERDS, AVERAGE_NUMBER_CATT…, AVERAGE_CATTLE_BEEF, AVERAGE_CATTLE_DAIRY, AVERAGE_CATTLE_AGE_…, AVERAGE_CATTLE_AGE_…
- 例2 値：Cavan | Offaly | Donegal | Laois | Donegal
  - 同じ表の列：Scheme, Amount Paid

## g0162（1 列）
- 見出し：ELECTORAL_DIVISION
- 例1 値：CORRANNEARY | DRUNG | KEALE | RATHCORMACK | ROSNAKILL
  - 同じ表の列：AVERAGE_YEAR, COUNTY, NUMBER_OF_HERDS, AVERAGE_NUMBER_CATT…, AVERAGE_CATTLE_BEEF, AVERAGE_CATTLE_DAIRY, AVERAGE_CATTLE_AGE_…, AVERAGE_CATTLE_AGE_…

## g0163（1 列）
- 見出し：NUMBER_OF_HERDS
- 例1 値：29 | 51 | 98 | 44 | 53
  - 同じ表の列：AVERAGE_YEAR, COUNTY, ELECTORAL_DIVISION, AVERAGE_NUMBER_CATT…, AVERAGE_CATTLE_BEEF, AVERAGE_CATTLE_DAIRY, AVERAGE_CATTLE_AGE_…, AVERAGE_CATTLE_AGE_…

## g0164（1 列）
- 見出し：AVERAGE_NUMBER_CATTLE
- 例1 値：2014.5 | 2964.25 | 1517.75 | 1564.75 | 2141.25
  - 同じ表の列：AVERAGE_YEAR, COUNTY, ELECTORAL_DIVISION, NUMBER_OF_HERDS, AVERAGE_CATTLE_BEEF, AVERAGE_CATTLE_DAIRY, AVERAGE_CATTLE_AGE_…, AVERAGE_CATTLE_AGE_…

## g0165（1 列）
- 見出し：AVERAGE_CATTLE_BEEF
- 例1 値：913.75 | 480.5 | 348 | 1772.75 | 1447.5
  - 同じ表の列：AVERAGE_YEAR, COUNTY, ELECTORAL_DIVISION, NUMBER_OF_HERDS, AVERAGE_NUMBER_CATT…, AVERAGE_CATTLE_DAIRY, AVERAGE_CATTLE_AGE_…, AVERAGE_CATTLE_AGE_…

## g0166（1 列）
- 見出し：AVERAGE_CATTLE_DAIRY
- 例1 値：3270.25 | 2.25 | 2426.25 | 2169.25 | 944.25
  - 同じ表の列：AVERAGE_YEAR, COUNTY, ELECTORAL_DIVISION, NUMBER_OF_HERDS, AVERAGE_NUMBER_CATT…, AVERAGE_CATTLE_BEEF, AVERAGE_CATTLE_AGE_…, AVERAGE_CATTLE_AGE_…

## g0167（1 列）
- 見出し：AVERAGE_CATTLE_AGE_0_3MTH
- 例1 値：45.25 | 41.25 | 4.5 | 87.5 | 167.25
  - 同じ表の列：AVERAGE_YEAR, COUNTY, ELECTORAL_DIVISION, NUMBER_OF_HERDS, AVERAGE_NUMBER_CATT…, AVERAGE_CATTLE_BEEF, AVERAGE_CATTLE_DAIRY, AVERAGE_CATTLE_AGE_…

## g0168（1 列）
- 見出し：AVERAGE_CATTLE_AGE_3_6MTH
- 例1 値：53.25 | 142.25 | 201.5 | 97 | 202.5
  - 同じ表の列：AVERAGE_YEAR, COUNTY, ELECTORAL_DIVISION, NUMBER_OF_HERDS, AVERAGE_NUMBER_CATT…, AVERAGE_CATTLE_BEEF, AVERAGE_CATTLE_DAIRY, AVERAGE_CATTLE_AGE_…

## g0169（1 列）
- 見出し：AVERAGE_CATTLE_AGE_6_12MTH
- 例1 値：231.75 | 369 | 179.75 | 150.25 | 1030.75
  - 同じ表の列：AVERAGE_YEAR, COUNTY, ELECTORAL_DIVISION, NUMBER_OF_HERDS, AVERAGE_NUMBER_CATT…, AVERAGE_CATTLE_BEEF, AVERAGE_CATTLE_DAIRY, AVERAGE_CATTLE_AGE_…

## g0170（1 列）
- 見出し：Scheme
- 例1 値：REAP | BPS | BPS | SIM | ANC
  - 同じ表の列：County, Amount Paid

## g0171（1 列）
- 見出し：Amount Paid
- 例1 値：1065809.72 | 777836.82 | 377970.99 | 825688.27 | 28314.78
  - 同じ表の列：County, Scheme

## g0172（5 列）
- 見出し：STATISTIC
- 例1 値：HSM12 | HSM12 | HSM12 | HSM12 | HSM12
  - 同じ表の列：Statistic, TLIST(M1), Month, C01947V02657, Local Authority, C02424V02930, Residential Units C…, UNIT
- 例2 値：HSM09 | HSM09 | HSM09 | HSM09 | HSM09
  - 同じ表の列：Statistic, TLIST(M1), Month, C02196V02652, State, UNIT, VALUE

## g0173（1 列）
- 見出し：Statistic
- 例1 値：Commencement Notices | Commencement Notices | Commencement Notices | Commencement Notices | Commencement Notices
  - 同じ表の列：STATISTIC, TLIST(M1), Month, C01947V02657, Local Authority, C02424V02930, Residential Units C…, UNIT

## g0174（1 列）
- 見出し：TLIST(M1)
- 例1 値：200408 | 200405 | 200407 | 200402 | 200405
  - 同じ表の列：STATISTIC, Statistic, Month, C01947V02657, Local Authority, C02424V02930, Residential Units C…, UNIT

## g0175（2 列）
- 見出し：Month
- 例1 値：2004M05 | 2004M07 | 2004M01 | 2004M07 | 2004M04
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), C01947V02657, Local Authority, C02424V02930, Residential Units C…, UNIT
- 例2 値：1981M11 | 1988M09 | 2005M04 | 2006M09 | 2017M08
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), C02196V02652, State, UNIT, VALUE

## g0176（1 列）
- 見出し：C01947V02657
- 例1 値：23 | 11 | 24 | 22 | 3
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, Local Authority, C02424V02930, Residential Units C…, UNIT

## g0177（1 列）
- 見出し：Local Authority
- 例1 値：Carlow (County Council) | Cavan (County Council) | Dublin (City Council) | Galway (County Council) | Cavan (County Council)
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, C01947V02657, C02424V02930, Residential Units C…, UNIT

## g0178（1 列）
- 見出し：C02424V02930
- 例1 値：02 | 01 | 02 | - | 01
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, C01947V02657, Local Authority, Residential Units C…, UNIT

## g0179（1 列）
- 見出し：Residential Units Commenced
- 例1 値：All residential dwellings | Multiple dwellings | All residential dwellings | All residential dwellings | Single dwellings
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, C01947V02657, Local Authority, C02424V02930, UNIT

## g0180（8 列）
- 見出し：UNIT
- 例1 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, C01947V02657, Local Authority, C02424V02930, Residential Units C…
- 例2 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02351V02955, Type of School, C02447V03042, School Programme

## g0181（9 列）
- 見出し：VALUE
- 例1 値：1 | 195 | 37 | 156 | 206
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, C01947V02657, Local Authority, C02424V02930, Residential Units C…
- 例2 値：35214 | 46270 | 67624 | 7106 | 1225
  - 同じ表の列：Contractor, Purpose

## g0182（1 列）
- 見出し：RecordID
- 例1 値：436 | 725 | 776 | 240 | 283
  - 同じ表の列：Date, VehicleID, JobID, Grease

## g0183（2 列）
- 見出し：Date
- 例1 値：2009-11-14T00:00:00 | 2010-01-21T00:00:00 | 2009-12-30T00:00:00 | 2010-01-22T00:00:00 | 2010-11-01T00:00:00
  - 同じ表の列：RecordID, VehicleID, JobID, Grease
- 例2 値：2011-02-04T00:00:00 | 2011-04-20T00:00:00 | 2011-04-05T00:00:00 | 2011-04-30T00:00:00 | 2011-04-16T00:00:00
  - 同じ表の列：Values, 00:00, 00:15, 00:30, 00:45, 01:00, 01:15, 01:30

## g0184（1 列）
- 見出し：VehicleID
- 例1 値：1 | 4 | 6 | 11 | 13
  - 同じ表の列：RecordID, Date, JobID, Grease

## g0185（1 列）
- 見出し：JobID
- 例1 値：1 | 4 | 1 | 2 | 11
  - 同じ表の列：RecordID, Date, VehicleID, Grease

## g0186（1 列）
- 見出し：Grease
- 例1 値：FALSE | FALSE | FALSE | FALSE | FALSE
  - 同じ表の列：RecordID, Date, VehicleID, JobID

## g0187（1 列）
- 見出し：tax_type_or_activity_area
- 例1 値：Sheriff Enforcement | Sheriff Enforcement | Self-assessed Income Tax | Excise - Vehicle Registration Tax | Revenue petitioned bankruptcies
  - 同じ表の列：year, gross_receipts__m, net_receipts__m, properties_returned…, number_of_contracts, value_of_contracts_…, number_of_payments, value_of_payments__b

## g0188（1 列）
- 見出し：gross_receipts__m
- 例1 値：1674 | 1959 | 25196 | 466 | 5842
  - 同じ表の列：year, tax_type_or_activit…, net_receipts__m, properties_returned…, number_of_contracts, value_of_contracts_…, number_of_payments, value_of_payments__b

## g0189（1 列）
- 見出し：net_receipts__m
- 例1 値：282 | 381 | 593 | 2 | 3640
  - 同じ表の列：year, tax_type_or_activit…, gross_receipts__m, properties_returned…, number_of_contracts, value_of_contracts_…, number_of_payments, value_of_payments__b

## g0190（1 列）
- 見出し：properties_returned_m
- 例1 値：1.93 | 1.87 | 1.997 | 1.94 | 1.97
  - 同じ表の列：year, tax_type_or_activit…, gross_receipts__m, net_receipts__m, number_of_contracts, value_of_contracts_…, number_of_payments, value_of_payments__b

## g0191（1 列）
- 見出し：number_of_contracts
- 例1 値：790176 | 665233 | 612004 | 370920 | 749755
  - 同じ表の列：year, tax_type_or_activit…, gross_receipts__m, net_receipts__m, properties_returned…, value_of_contracts_…, number_of_payments, value_of_payments__b

## g0192（1 列）
- 見出し：value_of_contracts__m
- 例1 値：49.12 | 38.21 | 31.69 | 51.25
  - 同じ表の列：year, tax_type_or_activit…, gross_receipts__m, net_receipts__m, properties_returned…, number_of_contracts, number_of_payments, value_of_payments__b

## g0193（1 列）
- 見出し：number_of_payments
- 例1 値：1295503 | 1622895 | 1019570 | 1691509 | 2000379
  - 同じ表の列：year, tax_type_or_activit…, gross_receipts__m, net_receipts__m, properties_returned…, number_of_contracts, value_of_contracts_…, value_of_payments__b

## g0194（1 列）
- 見出し：value_of_payments__b
- 例1 値：121.6 | 50.62 | 42.08 | 17.48 | 13.91
  - 同じ表の列：year, tax_type_or_activit…, gross_receipts__m, net_receipts__m, properties_returned…, number_of_contracts, value_of_contracts_…, number_of_payments

## g0195（1 列）
- 見出し：number_of_usage
- 例1 値：668230 | 97270 | 896008 | 177467 | 13152
  - 同じ表の列：year, tax_type_or_activit…, gross_receipts__m, net_receipts__m, properties_returned…, number_of_contracts, value_of_contracts_…, number_of_payments

## g0196（1 列）
- 見出し：vat_internal__m
- 例1 値：38.52 | 1421.09 | 2061.94 | 160.52 | 530.84
  - 同じ表の列：county, year, paye_income_tax_and…, self_employed_incom…, corporation_tax__m, capital_gains_tax__m

## g0197（1 列）
- 見出し：paye_income_tax_and_usc__m
- 例1 値：119.14 | 202.77 | 58.65 | 198 | 444.29
  - 同じ表の列：county, year, vat_internal__m, self_employed_incom…, corporation_tax__m, capital_gains_tax__m

## g0198（1 列）
- 見出し：self_employed_income_tax__m
- 例1 値：13.53 | 35.14 | 1131.04 | 15.56 | 17.4
  - 同じ表の列：county, year, vat_internal__m, paye_income_tax_and…, corporation_tax__m, capital_gains_tax__m

## g0199（1 列）
- 見出し：corporation_tax__m
- 例1 値：60.36 | 21.71 | 13.78 | 19.96 | 78.01
  - 同じ表の列：county, year, vat_internal__m, paye_income_tax_and…, self_employed_incom…, capital_gains_tax__m

## g0200（1 列）
- 見出し：capital_gains_tax__m
- 例1 値：74.21 | 23.12 | 18.09 | 23 | 52.44
  - 同じ表の列：county, year, vat_internal__m, paye_income_tax_and…, self_employed_incom…, corporation_tax__m

## g0201（1 列）
- 見出し：taxhead
- 例1 値：Enviromental Levy On Plastic Bags | PAYE Income Tax | Stamp Duty on Shares | Local Property Tax | Local Property Tax
  - 同じ表の列：year, amount__m

## g0202（1 列）
- 見出し：amount__m
- 例1 値：232 | 4288 | 24 | 128 | 720
  - 同じ表の列：year, taxhead

## g0203（1 列）
- 見出し：Doc
- 例1 値：App1 | App1 | App1 | App1 | App1
  - 同じ表の列：Heading, Ref, Desc, CY_Exp, PY_Exp, OBJECTID

## g0204（2 列）
- 見出し：Heading
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Doc, Ref, Desc, CY_Exp, PY_Exp, OBJECTID
- 例2 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Doc, Ref, Ref_desc, Ref1, Ref1_desc, Exp_Adop, Inc_Adop, EstMgr_Exp

## g0205（1 列）
- 見出し：Desc
- 例1 値：Corporate Affairs Overhead | Corporate Buildings Overhead | Pension & Lump Sum Overhead | Area Office Overhead | IT Services Overhead
  - 同じ表の列：Doc, Heading, Ref, CY_Exp, PY_Exp, OBJECTID

## g0206（1 列）
- 見出し：CY_Exp
- 例1 値：220000 | 1200000 | 1351600 | 3769000 | 1029100
  - 同じ表の列：Doc, Heading, Ref, Desc, PY_Exp, OBJECTID

## g0207（1 列）
- 見出し：PY_Exp
- 例1 値：914200 | 720500 | 1273500 | 786200 | 1381900
  - 同じ表の列：Doc, Heading, Ref, Desc, CY_Exp, OBJECTID

## g0208（5 列）
- 見出し：OBJECTID
- 例1 値：3 | 2 | 5 | 1 | 4
  - 同じ表の列：Doc, Heading, Ref, Desc, CY_Exp, PY_Exp
- 例2 値：114 | 9 | 13 | 101 | 117
  - 同じ表の列：LE_ID, ENGLISH, CONTAE, COUNTY, PROVINCE, GUID, CENTROID_X, CENTROID_Y

## g0209（1 列）
- 見出し：Doc
- 例1 値：TableB | TableB | TableB | TableB | TableB
  - 同じ表の列：Heading, Ref, Ref_desc, Ref1, Ref1_desc, Exp_Adop, Inc_Adop, EstMgr_Exp

## g0210（1 列）
- 見出し：Ref
- 例1 値：F | D | E | B | B
  - 同じ表の列：Doc, Heading, Ref_desc, Ref1, Ref1_desc, Exp_Adop, Inc_Adop, EstMgr_Exp

## g0211（1 列）
- 見出し：Ref_desc
- 例1 値：Environmental Services | Road Transport & Safety | Environmental Services | Development Management | Recreation and Amenity
  - 同じ表の列：Doc, Heading, Ref, Ref1, Ref1_desc, Exp_Adop, Inc_Adop, EstMgr_Exp

## g0212（1 列）
- 見出し：Ref1
- 例1 値：B05 | A02 | E05 | G02 | H07
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1_desc, Exp_Adop, Inc_Adop, EstMgr_Exp

## g0213（1 列）
- 見出し：Ref1_desc
- 例1 値：Unfinished Housing Estates | Land Drainage Costs | Community Sport and Recreational Develo… | Forward Planning | Administration of Homeless Service
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1, Exp_Adop, Inc_Adop, EstMgr_Exp

## g0214（1 列）
- 見出し：Exp_Adop
- 例1 値：348400 | 156400 | 802500 | 4100 | 832200
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1, Ref1_desc, Inc_Adop, EstMgr_Exp

## g0215（1 列）
- 見出し：Inc_Adop
- 例1 値：-65700 | -1787400 | -81500 | -55800 | -1800
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1, Ref1_desc, Exp_Adop, EstMgr_Exp

## g0216（1 列）
- 見出し：EstMgr_Exp
- 例1 値：412600 | 437600 | 10178200 | 87500 | 50300
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1, Ref1_desc, Exp_Adop, Inc_Adop

## g0217（1 列）
- 見出し：EstMgr_Inc
- 例1 値：-1900 | -65700 | -198000 | -6900 | -22100
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1, Ref1_desc, Exp_Adop, Inc_Adop

## g0218（2 列）
- 見出し：Month
- 例1 値：11 | 12 | 1 | 2 | 10
  - 同じ表の列：Year, YearMonth, Port1, Port2, Route, $Value, $Real
- 例2 値：6 | 6 | 6 | 6 | 6
  - 同じ表の列：Park, Location, PointID, Year, Day, Species, Time.1st.Detected, #detected_0-3m20s

## g0219（1 列）
- 見出し：YearMonth
- 例1 値：201010 | 201009 | 201009 | 201012 | 201012
  - 同じ表の列：Year, Month, Port1, Port2, Route, $Value, $Real

## g0220（1 列）
- 見出し：Port1
- 例1 値：Ayers Rock | Darwin | Melbourne | Adelaide | Perth
  - 同じ表の列：Year, Month, YearMonth, Port2, Route, $Value, $Real

## g0221（1 列）
- 見出し：Port2
- 例1 値：Mildura | Sydney | Sydney | Perth | Townsville
  - 同じ表の列：Year, Month, YearMonth, Port1, Route, $Value, $Real

## g0222（1 列）
- 見出し：Route
- 例1 値：Adelaide - Canberra | Brisbane - Darwin | Coffs Harbour - Sydney | Melbourne - Mildura | Adelaide - Perth
  - 同じ表の列：Year, Month, YearMonth, Port1, Port2, $Value, $Real

## g0223（1 列）
- 見出し：$Value
- 例1 値：774 | 484 | 168 | 158 | 249.9
  - 同じ表の列：Year, Month, YearMonth, Port1, Port2, Route, $Real

## g0224（1 列）
- 見出し：$Real
- 例1 値：312.0253327 | 554.0985075 | 1170.610542 | 289.1372687 | 87.82819117
  - 同じ表の列：Year, Month, YearMonth, Port1, Port2, Route, $Value

## g0225（3 列）
- 見出し：date
- 例1 値：2023-06 | 2023-06 | 2023-06 | 2023-06 | 2023-09
  - 同じ表の列：LGA_code, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…, Carer Payment
- 例2 値：2023-09 | 2023-06 | 2024-03 | 2024-03 | 2023-12
  - 同じ表の列：CED_CODE_2021, Commonwealth electo…, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…

## g0226（1 列）
- 見出し：LGA_code
- 例1 値：11450 | 21180 | 18100 | 34580 | 11650
  - 同じ表の列：date, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…, Carer Payment

## g0227（3 列）
- 見出し：ABSTUDY (Living allowance)
- 例1 値：5 | 5 | 45 | 15 | 5
  - 同じ表の列：date, LGA_code, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…, Carer Payment
- 例2 値：20 | 85 | 115 | 45 | 45
  - 同じ表の列：Date, CED_CODE_2021, Commonwealth electo…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…

## g0228（3 列）
- 見出し：ABSTUDY (Non-living allowance)
- 例1 値：20 | 20 | 660 | 60 | 5
  - 同じ表の列：date, LGA_code, ABSTUDY (Living all…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…, Carer Payment
- 例2 値：15 | 65 | 100 | 115 | 80
  - 同じ表の列：Date, CED_CODE_2021, Commonwealth electo…, ABSTUDY (Living all…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…

## g0229（3 列）
- 見出し：Age Pension
- 例1 値：1280 | 80 | 525 | 825 | 1220
  - 同じ表の列：date, LGA_code, ABSTUDY (Living all…, ABSTUDY (Non-living…, Austudy, Carer Allowance, Carer Allowance (Ch…, Carer Payment
- 例2 値：10760 | 16875 | 13550 | 26385 | 11330
  - 同じ表の列：Date, CED_CODE_2021, Commonwealth electo…, ABSTUDY (Living all…, ABSTUDY (Non-living…, Austudy, Carer Allowance, Carer Allowance (Ch…

## g0230（3 列）
- 見出し：Austudy
- 例1 値：0 | 5 | 0 | 10 | 0
  - 同じ表の列：date, LGA_code, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Carer Allowance, Carer Allowance (Ch…, Carer Payment
- 例2 値：320 | 130 | 100 | 75 | 190
  - 同じ表の列：Date, CED_CODE_2021, Commonwealth electo…, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Carer Allowance, Carer Allowance (Ch…

## g0231（3 列）
- 見出し：Carer Allowance
- 例1 値：3070 | 45 | 20 | 215 | 360
  - 同じ表の列：date, LGA_code, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance (Ch…, Carer Payment
- 例2 値：3210 | 4675 | 3225 | 4610 | 2845
  - 同じ表の列：Date, CED_CODE_2021, Commonwealth electo…, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance (Ch…

## g0232（3 列）
- 見出し：Carer Allowance (Child Health Care Card only)
- 例1 値：5 | 0 | 5 | 15 | 5
  - 同じ表の列：date, LGA_code, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Payment
- 例2 値：60 | 75 | 45 | 10 | 35
  - 同じ表の列：Date, CED_CODE_2021, Commonwealth electo…, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance

## g0233（3 列）
- 見出し：Carer Payment
- 例1 値：70 | 735 | 25 | 150 | 430
  - 同じ表の列：date, LGA_code, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…
- 例2 値：995 | 2040 | 600 | 2590 | 3080
  - 同じ表の列：Date, CED_CODE_2021, Commonwealth electo…, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance

## g0234（1 列）
- 見出し：Commonwealth Rent Assistance
- 例1 値：30890 | 2170 | 80 | 3415 | 8645
  - 同じ表の列：date, LGA_code, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…

## g0235（1 列）
- 見出し：CED_CODE_2021
- 例1 値：115 | 133 | 231 | 216 | 139
  - 同じ表の列：Date, Commonwealth electo…, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…

## g0236（1 列）
- 見出し：Commonwealth electoral division state
- 例1 値：Victoria | Victoria | Queensland | Western Australia | New South Wales
  - 同じ表の列：Date, CED_CODE_2021, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…

## g0237（1 列）
- 見出し：sa2_5digitcode_2016
- 例1 値：11584 | 11521 | 21358 | 21457 | 11326
  - 同じ表の列：date, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…, Carer Payment

## g0238（1 列）
- 見出し：Commonwealth Seniors Health Card
- 例1 値：56 | 169 | 361 | 606 | 111
  - 同じ表の列：date, sa2_5digitcode_2016, ABSTUDY (Living all…, ABSTUDY (Non-living…, Age Pension, Austudy, Carer Allowance, Carer Allowance (Ch…

## g0239（1 列）
- 見出し：2023 Revenue from hire of school facilities
- 例1 値：Grenfell Public School | Emmaville Central School | Australia Street Infants School | Glendore Public School | Auburn West Public School
  - 同じ表の列：$37,067,234.86

## g0240（1 列）
- 見出し：$37,067,234.86
- 例1 値：2,835.00 | 4,828.81 | 2,609.64 | 4,290.45 | 67,581.68
  - 同じ表の列：2023 Revenue from h…

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
g0151	
g0152	
g0153	
g0154	
g0155	
g0156	
g0157	
g0158	
g0159	
g0160	
g0161	
g0162	
g0163	
g0164	
g0165	
g0166	
g0167	
g0168	
g0169	
g0170	
g0171	
g0172	
g0173	
g0174	
g0175	
g0176	
g0177	
g0178	
g0179	
g0180	
g0181	
g0182	
g0183	
g0184	
g0185	
g0186	
g0187	
g0188	
g0189	
g0190	
g0191	
g0192	
g0193	
g0194	
g0195	
g0196	
g0197	
g0198	
g0199	
g0200	
g0201	
g0202	
g0203	
g0204	
g0205	
g0206	
g0207	
g0208	
g0209	
g0210	
g0211	
g0212	
g0213	
g0214	
g0215	
g0216	
g0217	
g0218	
g0219	
g0220	
g0221	
g0222	
g0223	
g0224	
g0225	
g0226	
g0227	
g0228	
g0229	
g0230	
g0231	
g0232	
g0233	
g0234	
g0235	
g0236	
g0237	
g0238	
g0239	
g0240	
```
