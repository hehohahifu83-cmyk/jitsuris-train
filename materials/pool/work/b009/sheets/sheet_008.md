# ラベル用シート 008 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_008.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0841（1 列）
- 見出し：HSE Regions
- 例1 値：HSE-Dublin/North-East | HSE-Dublin/North-East | HSE-Dublin/North-East | HSE-Dublin/North-East | HSE-West
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02842V03416, UNIT, VALUE

## g0842（1 列）
- 見出し：UNIT
- 例1 値：Number | % | % | % | %
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02842V03416, HSE Regions, VALUE

## g0843（1 列）
- 見出し：Statistic
- 例1 値：Container Traffic (Lift On/Lift Off) | Container Traffic (Lift On/Lift Off) | Container Traffic (Lift On/Lift Off) | Container Traffic (Lift On/Lift Off) | Container Traffic (Lift On/Lift Off)
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02636V03193, Imports or Exports, C02638V03194, Type of Traffic, C01855V02284

## g0844（1 列）
- 見出し：C02636V03193
- 例1 値：- | 01 | 01 | 01 | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Imports or Exports, C02638V03194, Type of Traffic, C01855V02284

## g0845（1 列）
- 見出し：Imports or Exports
- 例1 値：Imports | Imports and exports | Imports | Exports | Imports
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02636V03193, C02638V03194, Type of Traffic, C01855V02284

## g0846（1 列）
- 見出し：C02638V03194
- 例1 値：3 | 3 | 2 | 2 | 2
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02636V03193, Imports or Exports, Type of Traffic, C01855V02284

## g0847（1 列）
- 見出し：Type of Traffic
- 例1 値：Unladen traffic | Unladen traffic | Unladen traffic | Unladen traffic | Laden traffic
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02636V03193, Imports or Exports, C02638V03194, C01855V02284

## g0848（1 列）
- 見出し：C01855V02284
- 例1 値：IEFOV | IEDUB | IEWAT | IEDRO | IEORK
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02636V03193, Imports or Exports, C02638V03194, Type of Traffic

## g0849（1 列）
- 見出し：Port
- 例1 値：Dublin | Dublin | Waterford | All Irish ports | Warrenpoint
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02636V03193, Imports or Exports, C02638V03194, Type of Traffic

## g0850（1 列）
- 見出し：appendix_1__b_
- 例1 値：Payments made in excess of 30 days that… | Total invoices paid in Quarter | Parent Government Department: | Details | Payments made within 15 days
  - 同じ表の列：unsafe__2, unsafe__3, unsafe__4

## g0851（1 列）
- 見出し：unsafe__2
- 例1 値：0 | 2077507.4700000025 | 160 | 2432.2700000000004 | 43900633.74000115
  - 同じ表の列：appendix_1__b_, unsafe__3, unsafe__4

## g0852（1 列）
- 見出し：unsafe__3
- 例1 値：N/A | Percentage (%) of total number of payme… | 1 | 0.0003957653111704759 | 0.9686355990897397
  - 同じ表の列：appendix_1__b_, unsafe__2, unsafe__4

## g0853（1 列）
- 見出し：unsafe__4
- 例1 値：Div0 | Div0 | Div0 | N/A | Percentage (%) of the total amount paid
  - 同じ表の列：appendix_1__b_, unsafe__2, unsafe__3

## g0854（1 列）
- 見出し：Statistic Label
- 例1 値：Average Maximum Temperature | Average Maximum Temperature | Average Maximum Temperature | Average Maximum Temperature | Average Maximum Temperature
  - 同じ表の列：STATISTIC, tlist_m1_, Month, C02431V02938, Meteorological Weat…, UNIT, VALUE

## g0855（1 列）
- 見出し：tlist_m1_
- 例1 値：195808 | 196112 | 196006 | 196210 | 196108
  - 同じ表の列：STATISTIC, Statistic Label, Month, C02431V02938, Meteorological Weat…, UNIT, VALUE

## g0856（1 列）
- 見出し：Month
- 例1 値：1959M10 | 1963M01 | 1963M03 | 1959M04 | 1961M08
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, C02431V02938, Meteorological Weat…, UNIT, VALUE

## g0857（1 列）
- 見出し：C02431V02938
- 例1 値：007 | 010 | 003 | 003 | 009
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, Month, Meteorological Weat…, UNIT, VALUE

## g0858（1 列）
- 見出し：Meteorological Weather Station
- 例1 値：Galway | Roches Point | Rosslare | Cork airport | Valentia Observatory
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, Month, C02431V02938, UNIT, VALUE

## g0859（1 列）
- 見出し：AtcoCode
- 例1 値：8220DB001796 | 8220DB005144 | 8220DB001170 | 8220DB004389 | 8220DB001953
  - 同じ表の列：PlateCode, NptgLocalityRef, Easting, Northing, StopType, BusStopType, TimingStatus, CompassPoint

## g0860（1 列）
- 見出し：PlateCode
- 例1 値：2440 | 4938 | 2411 | 111341 | 2900
  - 同じ表の列：AtcoCode, NptgLocalityRef, Easting, Northing, StopType, BusStopType, TimingStatus, CompassPoint

## g0861（1 列）
- 見出し：NptgLocalityRef
- 例1 値：E0822010 | E0822019 | E0822019 | E0822041 | E0822071
  - 同じ表の列：AtcoCode, PlateCode, Easting, Northing, StopType, BusStopType, TimingStatus, CompassPoint

## g0862（1 列）
- 見出し：Easting
- 例1 値：713613 | 674335 | 645117 | 718043 | 715999
  - 同じ表の列：AtcoCode, PlateCode, NptgLocalityRef, Northing, StopType, BusStopType, TimingStatus, CompassPoint

## g0863（1 列）
- 見出し：Northing
- 例1 値：737492 | 730110 | 731921 | 675791 | 739698
  - 同じ表の列：AtcoCode, PlateCode, NptgLocalityRef, Easting, StopType, BusStopType, TimingStatus, CompassPoint

## g0864（1 列）
- 見出し：StopType
- 例1 値：BCT | BCT | BCT | BCT | BCT
  - 同じ表の列：AtcoCode, PlateCode, NptgLocalityRef, Easting, Northing, BusStopType, TimingStatus, CompassPoint

## g0865（1 列）
- 見出し：BusStopType
- 例1 値：MKD | MKD | MKD | MKD | MKD
  - 同じ表の列：AtcoCode, PlateCode, NptgLocalityRef, Easting, Northing, StopType, TimingStatus, CompassPoint

## g0866（1 列）
- 見出し：TimingStatus
- 例1 値：OTH | OTH | OTH | OTH | OTH
  - 同じ表の列：AtcoCode, PlateCode, NptgLocalityRef, Easting, Northing, StopType, BusStopType, CompassPoint

## g0867（1 列）
- 見出し：CompassPoint
- 例1 値：SW | N | E | NE | N
  - 同じ表の列：AtcoCode, PlateCode, NptgLocalityRef, Easting, Northing, StopType, BusStopType, TimingStatus

## g0868（1 列）
- 見出し：StopAreaRef
- 例1 値：822G002293 | 822G002658 | 822G002277 | 822G002348 | 822G002295
  - 同じ表の列：AtcoCode, PlateCode, NptgLocalityRef, Easting, Northing, StopType, BusStopType, TimingStatus

## g0869（1 列）
- 見出し：Suppliers
- 例1 値：Hegarty Demolition Ltd | PlanNet21 Communications | Polwarth Strategy Limited | BioSciences Limited a Thermo Fisher Com… | Connelly Partners
  - 同じ表の列：Contract Start Date, Contract End Date, common_procurement_…

## g0870（1 列）
- 見出し：Contract Start Date
- 例1 値：2024-02-19T00:00:00 | 2024-02-27T00:00:00 | 2024-02-08T00:00:00 | 2023-11-23T00:00:00 | 2024-02-01T00:00:00
  - 同じ表の列：Suppliers, Contract End Date, common_procurement_…

## g0871（1 列）
- 見出し：Contract End Date
- 例1 値：2027-01-31T00:00:00 | 2026-01-25T00:00:00 | 2026-03-03T00:00:00 | 2027-02-22T00:00:00 | 2028-01-31T00:00:00
  - 同じ表の列：Suppliers, Contract Start Date, common_procurement_…

## g0872（1 列）
- 見出し：common_procurement_vocabulary__cpv__codes
- 例1 値：Codes: 79341400 | Codes: 79212100 | Codes: 34134200 | Codes: 64121000 | Codes: 34134200
  - 同じ表の列：Suppliers, Contract Start Date, Contract End Date

## g0873（1 列）
- 見出し：Updated -
- 例1 値：Dublin 8 | Row Labels | Carlow | 2023 | Dublin 2
  - 同じ表の列：unsafe_01_10_2026, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0874（1 列）
- 見出し：unsafe_01_10_2026
- 例1 値：9 | 38 | 3 | 5 | 67
  - 同じ表の列：Updated -, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0875（1 列）
- 見出し：unsafe_
- 例1 値：57 | 3 | Count of RPB New Opening Type | 9 | 5
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0876（1 列）
- 見出し：unsafe__2
- 例1 値：1 | 5 | 2 | 1 | 1
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe_, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0877（1 列）
- 見出し：unsafe__3
- 例1 値：2 | 1 | 1 | 3 | 1
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe_, unsafe__2, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0878（1 列）
- 見出し：unsafe__4
- 例1 値：45 | 10 | 1 | 1 | 1
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe_, unsafe__2, unsafe__3, unsafe__5, unsafe__6, unsafe__7

## g0879（1 列）
- 見出し：unsafe__5
- 例1 値：40 | 1 | 1 | 2 | 1
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__6, unsafe__7

## g0880（1 列）
- 見出し：unsafe__6
- 例1 値：6 | 1 | 1 | 2 | 1
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__7

## g0881（1 列）
- 見出し：unsafe__7
- 例1 値：6 | 1 | 2 | 5 | 4
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6

## g0882（1 列）
- 見出し：unsafe__8
- 例1 値：3 | 2 | 1 | 4 | 3
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6

## g0883（1 列）
- 見出し：ED_ID_STR
- 例1 値：247117 | 77112 | 57148 | 87089 | 37155
  - 同じ表の列：ED_ENGLISH, TOTPOP22, AGEDEP22, LONEPA22, EDLOW_22, EDHIGH22, HLPROF22, LCLASS22

## g0884（1 列）
- 見出し：ED_ENGLISH
- 例1 値：MAGHERACLOGHER | PALMERSTON WEST | RAHEENAKEERAN | TULLAMAIN | MEENCARGAGH
  - 同じ表の列：ED_ID_STR, TOTPOP22, AGEDEP22, LONEPA22, EDLOW_22, EDHIGH22, HLPROF22, LCLASS22

## g0885（1 列）
- 見出し：TOTPOP22
- 例1 値：628 | 1,543.00 | 171 | 200 | 2,831.00
  - 同じ表の列：ED_ID_STR, ED_ENGLISH, AGEDEP22, LONEPA22, EDLOW_22, EDHIGH22, HLPROF22, LCLASS22

## g0886（1 列）
- 見出し：AGEDEP22
- 例1 値：38.07 | 37.07 | 36.42 | 32.7 | 35.59
  - 同じ表の列：ED_ID_STR, ED_ENGLISH, TOTPOP22, LONEPA22, EDLOW_22, EDHIGH22, HLPROF22, LCLASS22

## g0887（1 列）
- 見出し：LONEPA22
- 例1 値：6.25 | 19.88 | 28.13 | 18.57 | 50
  - 同じ表の列：ED_ID_STR, ED_ENGLISH, TOTPOP22, AGEDEP22, EDLOW_22, EDHIGH22, HLPROF22, LCLASS22

## g0888（1 列）
- 見出し：EDLOW_22
- 例1 値：13.92 | 14 | 8.92 | 15.2 | 11.71
  - 同じ表の列：ED_ID_STR, ED_ENGLISH, TOTPOP22, AGEDEP22, LONEPA22, EDHIGH22, HLPROF22, LCLASS22

## g0889（1 列）
- 見出し：EDHIGH22
- 例1 値：20 | 19.48 | 33.93 | 31.4 | 28.41
  - 同じ表の列：ED_ID_STR, ED_ENGLISH, TOTPOP22, AGEDEP22, LONEPA22, EDLOW_22, HLPROF22, LCLASS22

## g0890（1 列）
- 見出し：HLPROF22
- 例1 値：21.16 | 38.19 | 44.11 | 42.3 | 23.56
  - 同じ表の列：ED_ID_STR, ED_ENGLISH, TOTPOP22, AGEDEP22, LONEPA22, EDLOW_22, EDHIGH22, LCLASS22

## g0891（1 列）
- 見出し：LCLASS22
- 例1 値：21.43 | 32.96 | 29.43 | 17.91 | 40.35
  - 同じ表の列：ED_ID_STR, ED_ENGLISH, TOTPOP22, AGEDEP22, LONEPA22, EDLOW_22, EDHIGH22, HLPROF22

## g0892（1 列）
- 見出し：UNEMPM22
- 例1 値：7.79 | 6.91 | 8.45 | 12.17 | 8.84
  - 同じ表の列：ED_ID_STR, ED_ENGLISH, TOTPOP22, AGEDEP22, LONEPA22, EDLOW_22, EDHIGH22, HLPROF22

## g0893（1 列）
- 見出し：taxpayer_type
- 例1 値：Total | Other | Total | Other | Total
  - 同じ表の列：year, number_of_claimants, amount_claimed__m, exchequer_cost__m

## g0894（1 列）
- 見出し：number_of_claimants
- 例1 値：981 | 573 | 843 | 138 | 679
  - 同じ表の列：year, taxpayer_type, amount_claimed__m, exchequer_cost__m

## g0895（1 列）
- 見出し：amount_claimed__m
- 例1 値：199 | 410 | 707 | 155 | 211
  - 同じ表の列：year, taxpayer_type, number_of_claimants, exchequer_cost__m

## g0896（1 列）
- 見出し：exchequer_cost__m
- 例1 値：62 | 177 | 85 | 142 | 98
  - 同じ表の列：year, taxpayer_type, number_of_claimants, amount_claimed__m

## g0897（1 列）
- 見出し：Statistic
- 例1 値：Killed Casualties | Killed Casualties | Killed Casualties | All Fatal and Injury Collisions | Injury Collisions
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02451V02968, County, UNIT, VALUE

## g0898（1 列）
- 見出し：County
- 例1 値：Laois | South Tipperary | Louth | Laois | Meath
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02451V02968, UNIT, VALUE

## g0899（1 列）
- 見出し：Chimney_Fires_in_Houses
- 例1 値：96 | 144 | 112 | 162 | 69
  - 同じ表の列：Year, Other_House_Fires, Apartments,_flats_a…, Other_Institutions, Factories, Storage_Buildings/_…, Shops_/_Supermarkets, Hotels/_Guesthouses…

## g0900（1 列）
- 見出し：Other_House_Fires
- 例1 値：34 | 23 | 11 | 44 | 27
  - 同じ表の列：Year, Chimney_Fires_in_Ho…, Apartments,_flats_a…, Other_Institutions, Factories, Storage_Buildings/_…, Shops_/_Supermarkets, Hotels/_Guesthouses…

## g0901（1 列）
- 見出し：Apartments,_flats_and_bedsitters
- 例1 値：4 | 3
  - 同じ表の列：Year, Chimney_Fires_in_Ho…, Other_House_Fires, Other_Institutions, Factories, Storage_Buildings/_…, Shops_/_Supermarkets, Hotels/_Guesthouses…

## g0902（1 列）
- 見出し：Other_Institutions
- 例1 値：1
  - 同じ表の列：Year, Chimney_Fires_in_Ho…, Other_House_Fires, Apartments,_flats_a…, Factories, Storage_Buildings/_…, Shops_/_Supermarkets, Hotels/_Guesthouses…

## g0903（1 列）
- 見出し：Factories
- 例1 値：1 | 1
  - 同じ表の列：Year, Chimney_Fires_in_Ho…, Other_House_Fires, Apartments,_flats_a…, Other_Institutions, Storage_Buildings/_…, Shops_/_Supermarkets, Hotels/_Guesthouses…

## g0904（1 列）
- 見出し：Storage_Buildings/_Warehouses
- 例1 値：2 | 1
  - 同じ表の列：Year, Chimney_Fires_in_Ho…, Other_House_Fires, Apartments,_flats_a…, Other_Institutions, Factories, Shops_/_Supermarkets, Hotels/_Guesthouses…

## g0905（1 列）
- 見出し：Shops_/_Supermarkets
- 例1 値：2 | 2 | 2
  - 同じ表の列：Year, Chimney_Fires_in_Ho…, Other_House_Fires, Apartments,_flats_a…, Other_Institutions, Factories, Storage_Buildings/_…, Hotels/_Guesthouses…

## g0906（1 列）
- 見出し：Hotels/_Guesthouses/_Boarding_Houses_etc
- 例1 値：1 | 3 | 5 | 1
  - 同じ表の列：Year, Chimney_Fires_in_Ho…, Other_House_Fires, Apartments,_flats_a…, Other_Institutions, Factories, Storage_Buildings/_…, Shops_/_Supermarkets

## g0907（1 列）
- 見出し：Public_Houses
- 例1 値：1 | 1
  - 同じ表の列：Year, Chimney_Fires_in_Ho…, Other_House_Fires, Apartments,_flats_a…, Other_Institutions, Factories, Storage_Buildings/_…, Shops_/_Supermarkets

## g0908（1 列）
- 見出し：Proposal ID
- 例1 値：04/BRG/0581/UR06.2 | 05/IN3/B761 | 02/CE1/B124/EC07 | 02/W/B13 | 02/IN.1/I99s1
  - 同じ表の列：Sub-Programme, Supplement, Research Body, Crossref Funder Reg…, Proposal Title, Start Date, End Date, Current Total Commi…

## g0909（1 列）
- 見出し：Sub-Programme
- 例1 値：Principal Investigator Career Advanceme… | Basic Research Grant | Feasibility | Basic Research Grant | Planning
  - 同じ表の列：Proposal ID, Supplement, Research Body, Crossref Funder Reg…, Proposal Title, Start Date, End Date, Current Total Commi…

## g0910（1 列）
- 見出し：Supplement
- 例1 値：Equipment Supplement | Equipment Supplement | Equipment Supplement | Equipment Supplement | Equipment Supplement
  - 同じ表の列：Proposal ID, Sub-Programme, Research Body, Crossref Funder Reg…, Proposal Title, Start Date, End Date, Current Total Commi…

## g0911（1 列）
- 見出し：Research Body
- 例1 値：National University of Ireland, Galway … | University College Cork (UCC) | National University of Ireland, Galway … | University College Cork (UCC) | University College Dublin (UCD)
  - 同じ表の列：Proposal ID, Sub-Programme, Supplement, Crossref Funder Reg…, Proposal Title, Start Date, End Date, Current Total Commi…

## g0912（1 列）
- 見出し：Crossref Funder Registry ID
- 例1 値：10.13039/501100001602 | 10.13039/501100001602 | 10.13039/501100001602 | 10.13039/501100001602 | 10.13039/501100001602
  - 同じ表の列：Proposal ID, Sub-Programme, Supplement, Research Body, Proposal Title, Start Date, End Date, Current Total Commi…

## g0913（1 列）
- 見出し：Proposal Title
- 例1 値：Equipment Supplement | Incorporating the modular static timing… | Institute Development Award | Microstructural Study of Electrodeposit… | Investigating the mode of action of the…
  - 同じ表の列：Proposal ID, Sub-Programme, Supplement, Research Body, Crossref Funder Reg…, Start Date, End Date, Current Total Commi…

## g0914（1 列）
- 見出し：Start Date
- 例1 値：2003-04-01T00:00:00 | 2008-06-23T00:00:00 | 2005-06-01T00:00:00 | 2006-07-24T00:00:00 | 2005-06-01T00:00:00
  - 同じ表の列：Proposal ID, Sub-Programme, Supplement, Research Body, Crossref Funder Reg…, Proposal Title, End Date, Current Total Commi…

## g0915（1 列）
- 見出し：End Date
- 例1 値：2005-09-18T00:00:00 | 2006-09-17T00:00:00 | 2004-05-29T00:00:00 | 2006-08-11T00:00:00 | 2003-08-28T00:00:00
  - 同じ表の列：Proposal ID, Sub-Programme, Supplement, Research Body, Crossref Funder Reg…, Proposal Title, Start Date, Current Total Commi…

## g0916（1 列）
- 見出し：Current Total Commitment
- 例1 値：7280 | 70533.68 | 23000 | 11471 | 4660000
  - 同じ表の列：Proposal ID, Sub-Programme, Supplement, Research Body, Crossref Funder Reg…, Proposal Title, Start Date, End Date

## g0917（1 列）
- 見出し：Sensor Raw Data
- 例1 値：02/11/2015,10:13:20.144,$PSMB9DOF,2015-… | 02/11/2015,15:44:57.923,$PSMB9DOF,2015-… | 02/12/2015,10:18:22.063,$PSMB9DOF,2015-… | 02/11/2015,12:04:36.441,$PSMB9DOF,2015-… | 02/12/2015,02:18:21.438,$PSMB9DOF,2015-…
  - 同じ表の列：Data Stored Date

## g0918（1 列）
- 見出し：Data Stored Date
- 例1 値：2015-02-11T13:58:08 | 2015-02-11T10:15:58 | 2015-02-13T00:52:56 | 2015-02-11T16:17:46 | 2015-02-11T09:45:10
  - 同じ表の列：Sensor Raw Data

## g0919（1 列）
- 見出し：Sampling_Point
- 例1 値：(101010) Brittas River, Bridge North Ea… | (101310) Liffey River, Leixlip Bridge (… | (101420) Griffeen River, Gauging Statio… | (101115) Camac River, Bridge SE of Bald… | (101315) Liffey River, Weir 1.8km D/S L…
  - 同じ表の列：OBJECTID, X, Y, Sampled_Date, Received_Date, Sample_Number, Ammonia_mg_l_as_N, Arsenic_μg_l

## g0920（1 列）
- 見出し：X
- 例1 値：701189 | 702079 | 713529 | 705516 | 700751
  - 同じ表の列：OBJECTID, Sampling_Point, Y, Sampled_Date, Received_Date, Sample_Number, Ammonia_mg_l_as_N, Arsenic_μg_l

## g0921（1 列）
- 見出し：Y
- 例1 値：728933 | 729273 | 735831 | 735379 | 729273
  - 同じ表の列：OBJECTID, Sampling_Point, X, Sampled_Date, Received_Date, Sample_Number, Ammonia_mg_l_as_N, Arsenic_μg_l

## g0922（1 列）
- 見出し：Sampled_Date
- 例1 値：2016-09-15T09:30:00 | 2018-10-18T08:45:00 | 2015-03-06T09:25:00 | 2020-12-17T08:15:00 | 2021-07-23T10:00:00
  - 同じ表の列：OBJECTID, Sampling_Point, X, Y, Received_Date, Sample_Number, Ammonia_mg_l_as_N, Arsenic_μg_l

## g0923（1 列）
- 見出し：Received_Date
- 例1 値：2016-11-18T12:02:00 | 2018-11-08T11:44:00 | 2017-02-02T12:42:00 | 2015-10-08T12:46:00 | 2018-10-18T12:29:00
  - 同じ表の列：OBJECTID, Sampling_Point, X, Y, Sampled_Date, Sample_Number, Ammonia_mg_l_as_N, Arsenic_μg_l

## g0924（1 列）
- 見出し：Sample_Number
- 例1 値：1274275 | 1345491 | 1752089 | 1924791 | 1087058
  - 同じ表の列：OBJECTID, Sampling_Point, X, Y, Sampled_Date, Received_Date, Ammonia_mg_l_as_N, Arsenic_μg_l

## g0925（1 列）
- 見出し：Ammonia_mg_l_as_N
- 例1 値：0.03 | 0.04 | 0.12 | <0.01 | 0.01
  - 同じ表の列：OBJECTID, Sampling_Point, X, Y, Sampled_Date, Received_Date, Sample_Number, Arsenic_μg_l

## g0926（1 列）
- 見出し：Arsenic_μg_l
- 例1 値：1
  - 同じ表の列：OBJECTID, Sampling_Point, X, Y, Sampled_Date, Received_Date, Sample_Number, Ammonia_mg_l_as_N

## g0927（1 列）
- 見出し：B_O_D__mg_l
- 例1 値：1 | <1 | <1 | <1 | <1
  - 同じ表の列：OBJECTID, Sampling_Point, X, Y, Sampled_Date, Received_Date, Sample_Number, Ammonia_mg_l_as_N

## g0928（1 列）
- 見出し：JURISDICTION
- 例1 値：Circuit Court | Circuit Court | Circuit Court | District Court | High Court
  - 同じ表の列：AREA_OF_LAW, YEAR, CATEGORY, ODP_CATEGORY, INCOMING, RESOLVED

## g0929（1 列）
- 見出し：AREA_OF_LAW
- 例1 値：Family | Family | Civil | Criminal | Criminal
  - 同じ表の列：JURISDICTION, YEAR, CATEGORY, ODP_CATEGORY, INCOMING, RESOLVED

## g0930（1 列）
- 見出し：CATEGORY
- 例1 値：Satisfaction Piece | Sexual | Drugs/Misuse Of Drugs | Adoption | Liquidated Debt
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, ODP_CATEGORY, INCOMING, RESOLVED

## g0931（1 列）
- 見出し：ODP_CATEGORY
- 例1 値：Maintenance | Appeals (Current) | Article 40/Habeas Corpus | Guardianship Custody And Access | Liquidated Debt
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, CATEGORY, INCOMING, RESOLVED

## g0932（1 列）
- 見出し：INCOMING
- 例1 値：115 | 108 | 205 | 2156 | 315
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, CATEGORY, ODP_CATEGORY, RESOLVED

## g0933（1 列）
- 見出し：RESOLVED
- 例1 値：1 | 4217 | 260 | 36 | 193
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, CATEGORY, ODP_CATEGORY, INCOMING

## g0934（1 列）
- 見出し：Community return
- 例1 値：Percentage of successful completions ov… | Percentage of successful completions ov… | Percentage of successful completions ov… | Number of successful completions over t… | Number of successful completions over t…
  - 同じ表の列：Year, Number

## g0935（1 列）
- 見出し：Number
- 例1 値：0.89 | 287 | 206 | 66 | 218
  - 同じ表の列：Community return, Year

## g0936（1 列）
- 見出し：RID
- 例1 値：N01D2ML003 | N01D2ML002 | N01D2ML004 | N01D2ML004 | N01D2ML001
  - 同じ表の列：DTIMS_Chain, SU, SurveyDate, CSC, ITM_E, ITM_N

## g0937（1 列）
- 見出し：DTIMS_Chain
- 例1 値：6.393 | 13.092 | 9.794 | 15.793 | 5.294
  - 同じ表の列：RID, SU, SurveyDate, CSC, ITM_E, ITM_N

## g0938（1 列）
- 見出し：SU
- 例1 値：231 | 122 | 192 | 79 | 52
  - 同じ表の列：RID, DTIMS_Chain, SurveyDate, CSC, ITM_E, ITM_N

## g0939（1 列）
- 見出し：SurveyDate
- 例1 値：06-Jul-17 | 06-Jul-17 | 06-Jul-17 | 06-Jul-17 | 06-Jul-17
  - 同じ表の列：RID, DTIMS_Chain, SU, CSC, ITM_E, ITM_N

## g0940（1 列）
- 見出し：CSC
- 例1 値：0.43 | 0.42 | 0.44 | 0.44 | 0.43
  - 同じ表の列：RID, DTIMS_Chain, SU, SurveyDate, ITM_E, ITM_N

## g0941（1 列）
- 見出し：ITM_E
- 例1 値：706910.1 | 712103.5 | 719302 | 718157.5 | 702351.6
  - 同じ表の列：RID, DTIMS_Chain, SU, SurveyDate, CSC, ITM_N

## g0942（1 列）
- 見出し：ITM_N
- 例1 値：747783.8 | 802791.6 | 764654.2 | 818245.2 | 760808.6
  - 同じ表の列：RID, DTIMS_Chain, SU, SurveyDate, CSC, ITM_E

## g0943（1 列）
- 見出し：RegionID
- 例1 値：20 | 19 | 21 | 20 | 21
  - 同じ表の列：AreaID, Area, Year, Jan, Feb, Mar, Apr, May

## g0944（1 列）
- 見出し：AreaID
- 例1 値：6 | 11 | 9 | 15 | 16
  - 同じ表の列：RegionID, Area, Year, Jan, Feb, Mar, Apr, May

## g0945（1 列）
- 見出し：Area
- 例1 値：Midlands | Dublin South East/Wicklow | Kerry | Dublin South Central | SLWC
  - 同じ表の列：RegionID, AreaID, Year, Jan, Feb, Mar, Apr, May

## g0946（1 列）
- 見出し：id
- 例1 値："456" | "844" | "457" | "886" | "768"
  - 同じ表の列：From, To, Not_day_month_speci…, Functions, LegalForms, PolicyDomains, Ranks, Counties

## g0947（1 列）
- 見出し：From
- 例1 値："2020-10-21" | "1922-04-01" | "1991-01-21" | "1982-02-08" | "1987-12-08"
  - 同じ表の列：id, To, Not_day_month_speci…, Functions, LegalForms, PolicyDomains, Ranks, Counties

## g0948（1 列）
- 見出し：To
- 例1 値："1986-02-19" | "1945-06-18" | "1975-04-01" | "2010-06-02" | "1984-12-01"
  - 同じ表の列：id, From, Not_day_month_speci…, Functions, LegalForms, PolicyDomains, Ranks, Counties

## g0949（1 列）
- 見出し：Not_day_month_specific
- 例1 値："1" | "1" | "1" | "1" | "1"
  - 同じ表の列：id, From, To, Functions, LegalForms, PolicyDomains, Ranks, Counties

## g0950（1 列）
- 見出し：Functions
- 例1 値："Delivery" | "Regulatory (over public and private se… | "Regulatory (over public and private se… | "Adjudication - Grievance Handling;Regu… | "Regulatory (over public and private se…
  - 同じ表の列：id, From, To, Not_day_month_speci…, LegalForms, PolicyDomains, Ranks, Counties

## g0951（1 列）
- 見出し：LegalForms
- 例1 値：" Ministerial Departments" | " Statutory Corporation" | " Company limited by guarantee" | " Statutory Corporation" | " Company limited by guarantee"
  - 同じ表の列：id, From, To, Not_day_month_speci…, Functions, PolicyDomains, Ranks, Counties

## g0952（1 列）
- 見出し：PolicyDomains
- 例1 値："Health" | "Enterprise and Economic Development;Ho… | "Transport" | "Public Order and Safety" | "General Public Services"
  - 同じ表の列：id, From, To, Not_day_month_speci…, Functions, LegalForms, Ranks, Counties

## g0953（1 列）
- 見出し：Ranks
- 例1 値："Principal" | "Secretary General" | "Principal" | "Principal" | "Principal"
  - 同じ表の列：id, From, To, Not_day_month_speci…, Functions, LegalForms, PolicyDomains, Counties

## g0954（1 列）
- 見出し：Counties
- 例1 値："Dublin " | "Dublin " | "Kildare " | "Galway " | "Dublin "
  - 同じ表の列：id, From, To, Not_day_month_speci…, Functions, LegalForms, PolicyDomains, Ranks

## g0955（1 列）
- 見出し：Administrative_Authority_ID
- 例1 値：23 | 23 | 23 | 23 | 23
  - 同じ表の列：X, Y, FID, OBJECTID, Administrative_Auth…, Town, County

## g0956（1 列）
- 見出し：Administrative_Authority
- 例1 値：Wexford County Council | Wexford County Council | Wexford County Council | Wexford County Council | Wexford County Council
  - 同じ表の列：X, Y, FID, OBJECTID, Administrative_Auth…, Town, County

## g0957（1 列）
- 見出し：ID
- 例1 値：TPO_28 | TPO_B17 | TPO_B5 | TPO_18 | TPO_B6
  - 同じ表の列：Location, Reference, OBJECTID, SHAPE__Length

## g0958（1 列）
- 見出し：Location
- 例1 値：Coolattin Estate, Shillelagh, County Wi… | Grounds of Presentation College, Bray, … | Oldcourt House and Vevay House, Swan Ri… | Ballywaltrim Grove, Killarney Road, Bra… | Parochial Hall, St Patrick's Road, Wick…
  - 同じ表の列：ID, Reference, OBJECTID, SHAPE__Length

## g0959（1 列）
- 見出し：Reference
- 例1 値：78/3198D | 78/3198K | 78/3198G | 78/3198N | 78/3290
  - 同じ表の列：ID, Location, OBJECTID, SHAPE__Length

## g0960（1 列）
- 見出し：SHAPE__Length
- 例1 値：518.222245527399 | 227.63368058973 | 149.249028202499 | 51.5867565638574 | 624.35298756983
  - 同じ表の列：ID, Location, Reference, OBJECTID

## 答えの雛形

```
g0841	
g0842	
g0843	
g0844	
g0845	
g0846	
g0847	
g0848	
g0849	
g0850	
g0851	
g0852	
g0853	
g0854	
g0855	
g0856	
g0857	
g0858	
g0859	
g0860	
g0861	
g0862	
g0863	
g0864	
g0865	
g0866	
g0867	
g0868	
g0869	
g0870	
g0871	
g0872	
g0873	
g0874	
g0875	
g0876	
g0877	
g0878	
g0879	
g0880	
g0881	
g0882	
g0883	
g0884	
g0885	
g0886	
g0887	
g0888	
g0889	
g0890	
g0891	
g0892	
g0893	
g0894	
g0895	
g0896	
g0897	
g0898	
g0899	
g0900	
g0901	
g0902	
g0903	
g0904	
g0905	
g0906	
g0907	
g0908	
g0909	
g0910	
g0911	
g0912	
g0913	
g0914	
g0915	
g0916	
g0917	
g0918	
g0919	
g0920	
g0921	
g0922	
g0923	
g0924	
g0925	
g0926	
g0927	
g0928	
g0929	
g0930	
g0931	
g0932	
g0933	
g0934	
g0935	
g0936	
g0937	
g0938	
g0939	
g0940	
g0941	
g0942	
g0943	
g0944	
g0945	
g0946	
g0947	
g0948	
g0949	
g0950	
g0951	
g0952	
g0953	
g0954	
g0955	
g0956	
g0957	
g0958	
g0959	
g0960	
```
