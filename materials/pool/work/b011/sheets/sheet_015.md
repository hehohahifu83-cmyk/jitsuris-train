# ラベル用シート 015 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_015.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1681（1 列）
- 見出し：wind_speed__meters_sec_
- 例1 値：7.9 | 2.6 | 6.8 | 4.2 | 12.3
  - 同じ表の列：SensorTimestamp, air_temperature__de…, barometric_pressure…, wind_direction__deg…, wind_direction__deg…, wind_speed__knot_, barometric_pressure…

## g1682（1 列）
- 見出し：barometric_pressure__millibars_
- 例1 値：1016.7 | 1011.4 | 1013 | 1018.2 | 1016.5
  - 同じ表の列：SensorTimestamp, air_temperature__de…, barometric_pressure…, wind_direction__deg…, wind_direction__deg…, wind_speed__knot_, wind_speed__meters_…

## g1683（1 列）
- 見出し：Area
- 例1 値：Donegal | Dublin North | Sligo Leitrim West Cavan | Social Work Team for SCSA | Cavan Monaghan
  - 同じ表の列：AreaID, RegionID, Year, Jan, Feb, Mar, Apr, May

## g1684（1 列）
- 見出し：Location
- 例1 値：Greystones, South Beach | Aughrim | Wicklow, AIB | Rathdrum | Blessington, Dunnes Stores
  - 同じ表の列：OBJECTID, Site

## g1685（1 列）
- 見出し：Site
- 例1 値：The Murrough Recycling Centre | Car Park - Trafalgar Road | Newcastle Community Centre | Brockagh Resource Centre | Car Park, Arklow Recycling Centre
  - 同じ表の列：OBJECTID, Location

## g1686（1 列）
- 見出し：Sensor number
- 例1 値：20816320 | 20816320 | 20816320 | 20816321 | 20816320
  - 同じ表の列：ReadingNo, DateTime, Celcius, Date, Time, DateID, Farenheit, Humidity

## g1687（1 列）
- 見出し：ReadingNo
- 例1 値：263 | 269 | 394 | 443 | 772
  - 同じ表の列：Sensor number, DateTime, Celcius, Date, Time, DateID, Farenheit, Humidity

## g1688（1 列）
- 見出し：DateTime
- 例1 値：2020-06-02 20:56:00.000 | 2020-06-02 11:11:00.000 | 2020-05-29 05:26:00.000 | 2020-06-01 12:26:00.000 | 2020-05-29 09:26:00.000
  - 同じ表の列：Sensor number, ReadingNo, Celcius, Date, Time, DateID, Farenheit, Humidity

## g1689（1 列）
- 見出し：Celcius
- 例1 値：16.5997 | 16.4066 | 19.1415 | 13.4894 | 17.093
  - 同じ表の列：Sensor number, ReadingNo, DateTime, Date, Time, DateID, Farenheit, Humidity

## g1690（1 列）
- 見出し：Time
- 例1 値：00:26:00.0000000 | 11:11:00.0000000 | 18:41:00.0000000 | 07:26:00.0000000 | 16:55:00.0000000
  - 同じ表の列：Sensor number, ReadingNo, DateTime, Celcius, Date, DateID, Farenheit, Humidity

## g1691（1 列）
- 見出し：DateID
- 例1 値：20200602 | 20200601 | 20200531 | 20200603 | 20200531
  - 同じ表の列：Sensor number, ReadingNo, DateTime, Celcius, Date, Time, Farenheit, Humidity

## g1692（1 列）
- 見出し：Farenheit
- 例1 値：65.1227 | 62.6516 | 60.0647 | 62.0146 | 62.7288
  - 同じ表の列：Sensor number, ReadingNo, DateTime, Celcius, Date, Time, DateID, Humidity

## g1693（1 列）
- 見出し：Humidity
- 例1 値：66.7445 | 67.8172 | 84.2557 | 86.4271 | 61.5305
  - 同じ表の列：Sensor number, ReadingNo, DateTime, Celcius, Date, Time, DateID, Farenheit

## g1694（1 列）
- 見出し：Dewpoint
- 例1 値：43.7992 | 51.8046 | 48.164 | 58.5912 | 53.0242
  - 同じ表の列：Sensor number, ReadingNo, DateTime, Celcius, Date, Time, DateID, Farenheit

## g1695（1 列）
- 見出し：Age_Group
- 例1 値：25-34 | 25-34 | 15-24 | 45-54 | 35-44
  - 同じ表の列：Gender, All, Sole_Parent, Indigenous, Ex_Offender, Mental_Health, NESB, Disability

## g1696（1 列）
- 見出し：Gender
- 例1 値：Male | Female | Female | Male | Male
  - 同じ表の列：Age_Group, All, Sole_Parent, Indigenous, Ex_Offender, Mental_Health, NESB, Disability

## g1697（1 列）
- 見出し：All
- 例1 値：510 | 3494 | 3387 | 3154 | 2078
  - 同じ表の列：Age_Group, Gender, Sole_Parent, Indigenous, Ex_Offender, Mental_Health, NESB, Disability

## g1698（1 列）
- 見出し：Sole_Parent
- 例1 値：94.0 | 1354.0 | 1419.0 | 62.0 | 260.0
  - 同じ表の列：Age_Group, Gender, All, Indigenous, Ex_Offender, Mental_Health, NESB, Disability

## g1699（1 列）
- 見出し：Indigenous
- 例1 値：83 | 43 | 77 | 101 | 19
  - 同じ表の列：Age_Group, Gender, All, Sole_Parent, Ex_Offender, Mental_Health, NESB, Disability

## g1700（1 列）
- 見出し：Ex_Offender
- 例1 値：45 | 5 | 73 | 192 | 17
  - 同じ表の列：Age_Group, Gender, All, Sole_Parent, Indigenous, Mental_Health, NESB, Disability

## g1701（1 列）
- 見出し：Mental_Health
- 例1 値：36 | 266 | 27 | 312 | 286
  - 同じ表の列：Age_Group, Gender, All, Sole_Parent, Indigenous, Ex_Offender, NESB, Disability

## g1702（1 列）
- 見出し：NESB
- 例1 値：375 | 652 | 687 | 309 | 338
  - 同じ表の列：Age_Group, Gender, All, Sole_Parent, Indigenous, Ex_Offender, Mental_Health, Disability

## g1703（1 列）
- 見出し：Disability
- 例1 値：701 | 55 | 790 | 64 | 437
  - 同じ表の列：Age_Group, Gender, All, Sole_Parent, Indigenous, Ex_Offender, Mental_Health, NESB

## g1704（1 列）
- 見出し：Refugee
- 例1 値：9 | 29 | 13 | 85 | 50
  - 同じ表の列：Age_Group, Gender, All, Sole_Parent, Indigenous, Ex_Offender, Mental_Health, NESB

## g1705（1 列）
- 見出し：BIOEVC
- 例1 値：6.2 83 | 3.1 641 | 6.2 30 | 6.2 55 | 3.1 125
  - 同じ表の列：BIOREGNO, BIOREGION, EVC, Native Revegetation…

## g1706（1 列）
- 見出し：BIOREGNO
- 例1 値：6.1 | 6.2 | 6.2 | 3.1 | 6.2
  - 同じ表の列：BIOEVC, BIOREGION, EVC, Native Revegetation…

## g1707（1 列）
- 見出し：BIOREGION
- 例1 値：Central Victorian Uplands | Central Victorian Uplands | Central Victorian Uplands | Central Victorian Uplands | Goldfields
  - 同じ表の列：BIOEVC, BIOREGNO, EVC, Native Revegetation…

## g1708（1 列）
- 見出し：EVC
- 例1 値：175 | 55 | 53 | 83 | 175
  - 同じ表の列：BIOEVC, BIOREGNO, BIOREGION, Native Revegetation…

## g1709（1 列）
- 見出し：Native Revegetation Species List
- 例1 値：https://www.mrsc.vic.gov.au/files/asset… | https://www.mrsc.vic.gov.au/files/asset… | https://www.mrsc.vic.gov.au/files/asset… | https://www.mrsc.vic.gov.au/files/asset… | https://www.mrsc.vic.gov.au/files/asset…
  - 同じ表の列：BIOEVC, BIOREGNO, BIOREGION, EVC

## 答えの雛形

```
g1681	
g1682	
g1683	
g1684	
g1685	
g1686	
g1687	
g1688	
g1689	
g1690	
g1691	
g1692	
g1693	
g1694	
g1695	
g1696	
g1697	
g1698	
g1699	
g1700	
g1701	
g1702	
g1703	
g1704	
g1705	
g1706	
g1707	
g1708	
g1709	
```
