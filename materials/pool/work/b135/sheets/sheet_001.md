# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：YEAR
- 例1 値：2020 | 2019 | 2020 | 2019 | 2018
  - 同じ表の列：LOCATION, CATTLE_BREED_TYPE, CATTLE_GENDER, CATTLE_AGE_0_6, CATTLE_AGE_6_6, CATTLE_AGE_6_12, CATTLE_AGE_12_18, CATTLE_AGE_18_24
- 例2 値：2020 | 2020 | 2020 | 2020 | 2020
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, CATEGORY, ODP_CATEGORY, INCOMING, RESOLVED

## g0002（1 列）
- 見出し：LOCATION
- 例1 値：Erriff | Dargle | Vartry | Nore | Vartry
  - 同じ表の列：YEAR, CATTLE_BREED_TYPE, CATTLE_GENDER, CATTLE_AGE_0_6, CATTLE_AGE_6_6, CATTLE_AGE_6_12, CATTLE_AGE_12_18, CATTLE_AGE_18_24

## g0003（1 列）
- 見出し：CATTLE_BREED_TYPE
- 例1 値：DAIRY | BEEF | BEEF | DAIRY | BEEF
  - 同じ表の列：YEAR, LOCATION, CATTLE_GENDER, CATTLE_AGE_0_6, CATTLE_AGE_6_6, CATTLE_AGE_6_12, CATTLE_AGE_12_18, CATTLE_AGE_18_24

## g0004（1 列）
- 見出し：CATTLE_GENDER
- 例1 値：F | C | F | C | F
  - 同じ表の列：YEAR, LOCATION, CATTLE_BREED_TYPE, CATTLE_AGE_0_6, CATTLE_AGE_6_6, CATTLE_AGE_6_12, CATTLE_AGE_12_18, CATTLE_AGE_18_24

## g0005（1 列）
- 見出し：CATTLE_AGE_0_6
- 例1 値：29 | 1475 | 17 | 16 | 12
  - 同じ表の列：YEAR, LOCATION, CATTLE_BREED_TYPE, CATTLE_GENDER, CATTLE_AGE_6_6, CATTLE_AGE_6_12, CATTLE_AGE_12_18, CATTLE_AGE_18_24

## g0006（1 列）
- 見出し：CATTLE_AGE_6_6
- 例1 値：3077 | 8 | 38 | 1 | 985
  - 同じ表の列：YEAR, LOCATION, CATTLE_BREED_TYPE, CATTLE_GENDER, CATTLE_AGE_0_6, CATTLE_AGE_6_12, CATTLE_AGE_12_18, CATTLE_AGE_18_24

## g0007（1 列）
- 見出し：CATTLE_AGE_6_12
- 例1 値：2670 | 193 | 477 | 435 | 34838
  - 同じ表の列：YEAR, LOCATION, CATTLE_BREED_TYPE, CATTLE_GENDER, CATTLE_AGE_0_6, CATTLE_AGE_6_6, CATTLE_AGE_12_18, CATTLE_AGE_18_24

## g0008（1 列）
- 見出し：CATTLE_AGE_12_18
- 例1 値：284 | 17 | 43 | 356 | 8
  - 同じ表の列：YEAR, LOCATION, CATTLE_BREED_TYPE, CATTLE_GENDER, CATTLE_AGE_0_6, CATTLE_AGE_6_6, CATTLE_AGE_6_12, CATTLE_AGE_18_24

## g0009（1 列）
- 見出し：CATTLE_AGE_18_24
- 例1 値：734 | 29023 | 53 | 148 | 27
  - 同じ表の列：YEAR, LOCATION, CATTLE_BREED_TYPE, CATTLE_GENDER, CATTLE_AGE_0_6, CATTLE_AGE_6_6, CATTLE_AGE_6_12, CATTLE_AGE_12_18

## g0010（1 列）
- 見出し：CATTLE_AGE_24_30
- 例1 値：186 | 2311 | 109 | 253 | 31
  - 同じ表の列：YEAR, LOCATION, CATTLE_BREED_TYPE, CATTLE_GENDER, CATTLE_AGE_0_6, CATTLE_AGE_6_6, CATTLE_AGE_6_12, CATTLE_AGE_12_18

## g0011（1 列）
- 見出し：ACCT_ID
- 例1 値：4610983981 | 4610983981 | 4610983981 | 4610983981 | 4610983981
  - 同じ表の列：MPRN, GMPRN, SA_ID, START_OPT_CD, START_Date, END_Date, KWH (kilo watt per …

## g0012（1 列）
- 見出し：MPRN
- 例1 値：10290005129 | 10290005260 | 10290004904 | 10290004960 | 10290004953
  - 同じ表の列：ACCT_ID, GMPRN, SA_ID, START_OPT_CD, START_Date, END_Date, KWH (kilo watt per …

## g0013（1 列）
- 見出し：GMPRN
- 例1 値：91290000017 | 91290000017 | 91290000017 | 91290000017 | 91290000017
  - 同じ表の列：ACCT_ID, MPRN, SA_ID, START_OPT_CD, START_Date, END_Date, KWH (kilo watt per …

## g0014（1 列）
- 見出し：SA_ID
- 例1 値：4610983686 | 4610983252 | 4610983346 | 4610983709 | 4610983976
  - 同じ表の列：ACCT_ID, MPRN, GMPRN, START_OPT_CD, START_Date, END_Date, KWH (kilo watt per …

## g0015（1 列）
- 見出し：START_OPT_CD
- 例1 値：BURN24 | BURN24 | BURN24 | BURN24 | BURN24
  - 同じ表の列：ACCT_ID, MPRN, GMPRN, SA_ID, START_Date, END_Date, KWH (kilo watt per …

## g0016（1 列）
- 見出し：START_Date
- 例1 値：2011-03-31T00:00:00 | 2011-08-31T00:00:00 | 2011-02-28T00:00:00 | 2011-07-31T00:00:00 | 2011-09-30T00:00:00
  - 同じ表の列：ACCT_ID, MPRN, GMPRN, SA_ID, START_OPT_CD, END_Date, KWH (kilo watt per …

## g0017（1 列）
- 見出し：END_Date
- 例1 値：2011-10-31T00:00:00 | 2011-09-30T00:00:00 | 2011-06-30T00:00:00 | 2011-03-31T00:00:00 | 2011-05-31T00:00:00
  - 同じ表の列：ACCT_ID, MPRN, GMPRN, SA_ID, START_OPT_CD, START_Date, KWH (kilo watt per …

## g0018（1 列）
- 見出し：KWH (kilo watt per hour)
- 例1 値：267 | 335 | 298 | 584 | 223
  - 同じ表の列：ACCT_ID, MPRN, GMPRN, SA_ID, START_OPT_CD, START_Date, END_Date

## g0019（1 列）
- 見出し：unsafe_
- 例1 値：2 | 2 | 1 | 2 | 1
  - 同じ表の列：unsafe__2, unsafe__3

## g0020（1 列）
- 見出し：unsafe__2
- 例1 値：no | Yes | Yes | Yes | no
  - 同じ表の列：unsafe_, unsafe__3

## g0021（1 列）
- 見出し：unsafe__3
- 例1 値：yes | yes | no | Public Accessible Toilets | no
  - 同じ表の列：unsafe_, unsafe__2

## g0022（1 列）
- 見出し：Thoroughfare
- 例1 値：carraig glen | burdett avenue | lakelands estate | drummartin park, close, crescent | meadow close
  - 同じ表の列：Day, Week

## g0023（1 列）
- 見出し：Day
- 例1 値：Thursday | Wednesday | Thursday | Wednesday | Monday
  - 同じ表の列：Thoroughfare, Week

## g0024（1 列）
- 見出し：Week
- 例1 値：week 3 | week 4 | week 1 | week 2 | week 4
  - 同じ表の列：Thoroughfare, Day

## g0025（3 列）
- 見出し：Time
- 例1 値：11:00 | 02:00 | 13:00 | 08:00 | 03:00
  - 同じ表の列：Report, Temperature oC, wind_speed_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa
- 例2 値：15:00 | 05:00 | 11:00 | 06:00 | 02:00
  - 同じ表の列：Report, Temperature oC, wind_speed_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0026（1 列）
- 見出し：Report
- 例1 値："Light Drizzle " | "Rain/Drizzle " | "Recent Rain" | "Cloudy" | "Cloudy"
  - 同じ表の列：Time, Temperature oC, wind_speed_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0027（3 列）
- 見出し：Temperature oC
- 例1 値：7 | 7 | 7 | 10 | 7
  - 同じ表の列：Time, Report, wind_speed_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa
- 例2 値：10 | 7 | 7 | 7 | 7
  - 同じ表の列：Time, Report, wind_speed_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0028（3 列）
- 見出し：wind_speed_km_h
- 例1 値：20 | 19 | 11 | 24 | 13
  - 同じ表の列：Time, Report, Temperature oC, Wind Direction o, rainfall_mm_h, Pressure hPa
- 例2 値：17 | 11 | 15 | 13 | 13
  - 同じ表の列：Time, Report, Temperature oC, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0029（3 列）
- 見出し：Wind Direction o
- 例1 値：90 | 135 | 45 | 90 | 135
  - 同じ表の列：Time, Report, Temperature oC, wind_speed_km_h, rainfall_mm_h, Pressure hPa
- 例2 値：135 | 135 | 90 | 135 | 45
  - 同じ表の列：Time, Report, Temperature oC, wind_speed_km_h, rainfall_mm_h, Pressure hPa

## g0030（3 列）
- 見出し：rainfall_mm_h
- 例1 値：0.1 | 0.01 | 0.1 | 0.0 | 0.01
  - 同じ表の列：Time, Report, Temperature oC, wind_speed_km_h, Wind Direction o, Pressure hPa
- 例2 値：0.0 | 0.1 | 0.01 | 0.0 | 0.0
  - 同じ表の列：Time, Report, Temperature oC, wind_speed_km_h, Wind Direction o, Pressure hPa

## g0031（3 列）
- 見出し：Pressure hPa
- 例1 値：1000 | 999 | 1000 | 997 | 997
  - 同じ表の列：Time, Report, Temperature oC, wind_speed_km_h, Wind Direction o, rainfall_mm_h
- 例2 値：997 | 998 | 995 | 998 | 998
  - 同じ表の列：Time, Report, Temperature oC, wind_speed_km_h, Wind Direction o, rainfall_mm_h

## g0032（1 列）
- 見出し：Report
- 例1 値："Rain shower" | "Cloudy" | "Cloudy" | "Light rain " | "Cloudy"
  - 同じ表の列：Time, Temperature oC, wind_speed_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0033（1 列）
- 見出し：Report
- 例1 値："Cloudy" | "Cloudy" | "Cloudy" | "Cloudy" | "Cloudy"
  - 同じ表の列：Time, Temperature oC, wind_speed_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0034（1 列）
- 見出し：County
- 例1 値：Meath | Cork | Leitrim | Galway | Cork
  - 同じ表の列：Roll No, School Type, Class Type, No of Classes

## g0035（1 列）
- 見出し：Roll No
- 例1 値：09190G | 16677C | 70830N | 70570N | 76076M
  - 同じ表の列：County, School Type, Class Type, No of Classes

## g0036（1 列）
- 見出し：School Type
- 例1 値：Post Primary | Post Primary | Primary | Primary | Primary
  - 同じ表の列：County, Roll No, Class Type, No of Classes

## g0037（1 列）
- 見出し：Class Type
- 例1 値：Autism/Autistic Spectrum Disorders | Moderate General Learning Disability | ASD Early Intervention | ASD Early Intervention | Autism/Autistic Spectrum Disorders
  - 同じ表の列：County, Roll No, School Type, No of Classes

## g0038（1 列）
- 見出し：No of Classes
- 例1 値：1 | 2 | 2 | 2 | 2
  - 同じ表の列：County, Roll No, School Type, Class Type

## g0039（1 列）
- 見出し：JURISDICTION
- 例1 値：District Court | High Court | High Court | Court Of Appeal | Circuit Court
  - 同じ表の列：AREA_OF_LAW, YEAR, CATEGORY, ODP_CATEGORY, INCOMING, RESOLVED

## g0040（1 列）
- 見出し：AREA_OF_LAW
- 例1 値：Supreme Court | Civil | Civil | Civil | Civil
  - 同じ表の列：JURISDICTION, YEAR, CATEGORY, ODP_CATEGORY, INCOMING, RESOLVED

## g0041（1 列）
- 見出し：CATEGORY
- 例1 値：Dissolution Of Partnership | Dissolution Of Partnership | Revenue To High Court | Bankruptcy Petitions (Creditors) | Rape
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, ODP_CATEGORY, INCOMING, RESOLVED

## g0042（1 列）
- 見出し：ODP_CATEGORY
- 例1 値：Disqualify Directors | Larceny/Fraud/Robbery | Foreign Proceedings (Other) | Manslaughter | Rape
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, CATEGORY, INCOMING, RESOLVED

## g0043（1 列）
- 見出し：INCOMING
- 例1 値：720 | 22 | 516 | 97 | 1
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, CATEGORY, ODP_CATEGORY, RESOLVED

## g0044（1 列）
- 見出し：RESOLVED
- 例1 値：62 | 1120 | 8 | 471 | 35
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, CATEGORY, ODP_CATEGORY, INCOMING

## g0045（1 列）
- 見出し：Objective
- 例1 値：CPO 10.9 | CPO 10.9 | CPO 10.9 | CPO 10.9 | CPO 10.9
  - 同じ表の列：CoreRetailArea_CDP2…, Maps, OBJECTID, SHAPE__Area, SHAPE__Length

## g0046（1 列）
- 見出し：CoreRetailArea_CDP2021_2027
- 例1 値：Bray 1 | Wicklow | Blessingtion | Bray 2 | Greystones
  - 同じ表の列：Objective, Maps, OBJECTID, SHAPE__Area, SHAPE__Length

## g0047（1 列）
- 見出し：Maps
- 例1 値：Map No. 10.01a | Map No. 10.01a | Map No. 10.01c | Map No. 10.01b | Map No. 10.01b
  - 同じ表の列：Objective, CoreRetailArea_CDP2…, OBJECTID, SHAPE__Area, SHAPE__Length

## g0048（1 列）
- 見出し：OBJECTID
- 例1 値：5 | 4 | 1 | 6 | 3
  - 同じ表の列：Objective, CoreRetailArea_CDP2…, Maps, SHAPE__Area, SHAPE__Length

## g0049（1 列）
- 見出し：SHAPE__Area
- 例1 値：74173.2167663574 | 40344.3398132324 | 78518.593963623 | 44047.3954772949 | 41916.098449707
  - 同じ表の列：Objective, CoreRetailArea_CDP2…, Maps, OBJECTID, SHAPE__Length

## g0050（1 列）
- 見出し：SHAPE__Length
- 例1 値：1294.88593495581 | 2042.51168736535 | 1896.42633738677 | 524.015166238533 | 1536.04132785771
  - 同じ表の列：Objective, CoreRetailArea_CDP2…, Maps, OBJECTID, SHAPE__Area

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
```
