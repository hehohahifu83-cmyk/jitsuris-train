# ラベル用シート 012 / 018

- LABEL_GUIDE v1.8 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_012.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1321（1 列）
- 見出し：名称_英字
- 例1 値：Okinawa Prefectural Comprehensive Menta… | Tsukazan Dental Clinic | Tsukazan Clinic | Ichinichibashi Clinic | Ebisu ENT Clinic
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 医療機関の種類, 町字ID, 建物名等(方書)

## g1322（1 列）
- 見出し：医療機関の種類
- 例1 値：無床診療所 | 無床診療所 | 無床診療所 | 無床診療所 | 無床診療所
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 町字ID, 建物名等(方書)

## g1323（1 列）
- 見出し：建物名等(方書)
- 例1 値：2F | メディカルプラザつかざん3階 | 103号室 | メディカルプラザはえばる3F | 2階
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 医療機関の種類, 町字ID

## g1324（1 列）
- 見出し：介護サービス事業所名称
- 例1 値：デイサービスセンターベストかねぐすく | 通所介護事業所寿デイサービス | 介護老人保健施設嬉野の園 | 通所介護事業所寿デイサービス | 介護老人保健施設嬉野の園
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 介護サービス事業所名称_カナ, 介護サービス事業所名称_英字, 実施サービス, 町字ID, 建物名等(方書)

## g1325（1 列）
- 見出し：介護サービス事業所名称_カナ
- 例1 値：ホウモンカンゴステーションハッピー | ヘルパーステーションベストカネグスク | ヘルパーマジュン | ホウモンカイゴジギョウショカエデ | ヘルスアンドケアジャパンカブシキカイシャ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 介護サービス事業所名称, 介護サービス事業所名称_英字, 実施サービス, 町字ID, 建物名等(方書)

## g1326（1 列）
- 見出し：介護サービス事業所名称_英字
- 例1 値：Ureshinosato Home Care Management Office | Mercy Pharmacy Kanegusuku | Welfare Facility for the Elderly Ureshi… | Day Service LATATA | Home Visit Rehabilitation Service, Kari…
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 介護サービス事業所名称, 介護サービス事業所名称_カナ, 実施サービス, 町字ID, 建物名等(方書)

## g1327（1 列）
- 見出し：実施サービス
- 例1 値：介護老人保健施設 | 訪問看護 | 通所型サービス(独自) | 訪問看護 | 短期入所生活介護
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 介護サービス事業所名称, 介護サービス事業所名称_カナ, 介護サービス事業所名称_英字, 町字ID, 建物名等(方書)

## g1328（1 列）
- 見出し：建物名等(方書)
- 例1 値：南星マンション202号 | 1階 | セレクション202号室 | 野原店舗102号 | 1階
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 介護サービス事業所名称, 介護サービス事業所名称_カナ, 介護サービス事業所名称_英字, 実施サービス, 町字ID

## g1329（1 列）
- 見出し：市区町村名
- 例1 値：南大東村 | 南大東村 | 南大東村 | 南大東村 | 南大東村
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 名称, 名称_カナ, 方書, 設置位置, 法人番号

## g1330（1 列）
- 見出し：名称
- 例1 値：JAおきなわ南大東支店本所 | 南大東村役場 | 南大東村高齢者生活福祉センター | 大東糖業(株)南大東事業所 | 南大東村商工会
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, 名称_カナ, 方書, 設置位置, 法人番号

## g1331（1 列）
- 見出し：名称_カナ
- 例1 値：ミナミダイトウソンリツミナミダイトウショウチュウガッコウ | ヨシザトカイカン | ダイトウトウギョウ(カブ)ミナミダイトウジギョウショ | スパークミナミダイトウ シママルゴトカン | チイキスポーツセンター
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, 名称, 方書, 設置位置, 法人番号

## g1332（1 列）
- 見出し：方書
- 例1 値：南大東村高齢者生活福祉センター | 南大東村役場
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, 名称, 名称_カナ, 設置位置, 法人番号

## g1333（1 列）
- 見出し：設置位置
- 例1 値：ホテル吉里受付前 | スパーク南大東事務所内 | ミレニアムパーク内東屋1F入口 | 事務所内 | 事務所入口
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, 名称, 名称_カナ, 方書, 法人番号

## g1334（1 列）
- 見出し：団体名
- 例1 値：南大東村 | 南大東村 | 大東糖業 | 南大東村 | 南大東村
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, 名称, 名称_カナ, 方書, 設置位置

## g1335（1 列）
- 見出し：小地域
- 例1 値：島尻郡南大東村字旧東 | 島尻郡南大東村字新東 | 島尻郡南大東村字池之沢 | 島尻郡南大東村字在所 | 島尻郡南大東村字南
  - 同じ表の列：KEY_CODE, 人口総数, 男, 女, 世帯総数

## g1336（1 列）
- 見出し：CENSUS TRACT
- 例1 値：22033002802 | 22033003703 | 22033003202 | 22033003906 | 22033004508
  - 同じ表の列：2010 POPULATION, LACKING HEALTH INSU…, ARTHRITIS, BINGE DRINKING, HIGH BLOOD PRESSURE, BLOOD PRESSURE MEDI…, CANCER (EXCLUDING S…, ASTHMA

## g1337（1 列）
- 見出し：2010 POPULATION
- 例1 値：1795 | 3435 | 4757 | 6877 | 2682
  - 同じ表の列：CENSUS TRACT, LACKING HEALTH INSU…, ARTHRITIS, BINGE DRINKING, HIGH BLOOD PRESSURE, BLOOD PRESSURE MEDI…, CANCER (EXCLUDING S…, ASTHMA

## g1338（1 列）
- 見出し：LACKING HEALTH INSURANCE
- 例1 値：0.114 | 0.19 | 0.112 | 0.116 | 0.126
  - 同じ表の列：CENSUS TRACT, 2010 POPULATION, ARTHRITIS, BINGE DRINKING, HIGH BLOOD PRESSURE, BLOOD PRESSURE MEDI…, CANCER (EXCLUDING S…, ASTHMA

## g1339（1 列）
- 見出し：ARTHRITIS
- 例1 値：0.298 | 0.217 | 0.259 | 0.217 | 0.234
  - 同じ表の列：CENSUS TRACT, 2010 POPULATION, LACKING HEALTH INSU…, BINGE DRINKING, HIGH BLOOD PRESSURE, BLOOD PRESSURE MEDI…, CANCER (EXCLUDING S…, ASTHMA

## g1340（1 列）
- 見出し：BINGE DRINKING
- 例1 値：0.197 | 0.199 | 0.165 | 0.224 | 0.259
  - 同じ表の列：CENSUS TRACT, 2010 POPULATION, LACKING HEALTH INSU…, ARTHRITIS, HIGH BLOOD PRESSURE, BLOOD PRESSURE MEDI…, CANCER (EXCLUDING S…, ASTHMA

## g1341（1 列）
- 見出し：HIGH BLOOD PRESSURE
- 例1 値：0.14 | 0.43 | 0.519 | 0.411 | 0.449
  - 同じ表の列：CENSUS TRACT, 2010 POPULATION, LACKING HEALTH INSU…, ARTHRITIS, BINGE DRINKING, BLOOD PRESSURE MEDI…, CANCER (EXCLUDING S…, ASTHMA

## g1342（1 列）
- 見出し：BLOOD PRESSURE MEDICINE
- 例1 値：0.797 | 0.75 | 0.755 | 0.718 | 0.73
  - 同じ表の列：CENSUS TRACT, 2010 POPULATION, LACKING HEALTH INSU…, ARTHRITIS, BINGE DRINKING, HIGH BLOOD PRESSURE, CANCER (EXCLUDING S…, ASTHMA

## g1343（1 列）
- 見出し：CANCER (EXCLUDING SKIN CANCER)
- 例1 値：0.05 | 0.052 | 0.066 | 0.057 | 0.071
  - 同じ表の列：CENSUS TRACT, 2010 POPULATION, LACKING HEALTH INSU…, ARTHRITIS, BINGE DRINKING, HIGH BLOOD PRESSURE, BLOOD PRESSURE MEDI…, ASTHMA

## g1344（1 列）
- 見出し：ASTHMA
- 例1 値：0.089 | 0.089 | 0.095 | 0.117 | 0.074
  - 同じ表の列：CENSUS TRACT, 2010 POPULATION, LACKING HEALTH INSU…, ARTHRITIS, BINGE DRINKING, HIGH BLOOD PRESSURE, BLOOD PRESSURE MEDI…, CANCER (EXCLUDING S…

## g1345（1 列）
- 見出し：CERVICAL CANCER SCREENING
- 例1 値：0.85 | 0.843 | 0.885 | 0.813 | 0.891
  - 同じ表の列：CENSUS TRACT, 2010 POPULATION, LACKING HEALTH INSU…, ARTHRITIS, BINGE DRINKING, HIGH BLOOD PRESSURE, BLOOD PRESSURE MEDI…, CANCER (EXCLUDING S…

## g1346（5 列）
- 見出し：YEAR
- 例1 値：2023 | 2018 | 2022 | 2021 | 2024
  - 同じ表の列：FUND ID, FUND, DEPARTMENT ID, DEPARTMENT, FUNCTION ID, FUNCTION, DIVISION ID, DIVISION
- 例2 値：2017 | 2017 | 2017 | 2017 | 2017
  - 同じ表の列：StateAbbr, StateDesc, CityName, GeographicLevel, DataSource, Category, UniqueID, Measure

## g1347（1 列）
- 見出し：FUND ID
- 例1 値：1000 | 5810 | 1000 | 2202 | 2610
  - 同じ表の列：YEAR, FUND, DEPARTMENT ID, DEPARTMENT, FUNCTION ID, FUNCTION, DIVISION ID, DIVISION

## g1348（1 列）
- 見出し：FUND
- 例1 値：AIRPORT OPERATIONS FUND | GENERAL FUND | GENERAL FUND | AIRPORT OPERATIONS FUND | LIBRARY BOARD OF CONTROL
  - 同じ表の列：YEAR, FUND ID, DEPARTMENT ID, DEPARTMENT, FUNCTION ID, FUNCTION, DIVISION ID, DIVISION

## g1349（1 列）
- 見出し：DEPARTMENT ID
- 例1 値：7000 | 1200 | 7900 | 1600 | 0900
  - 同じ表の列：YEAR, FUND ID, FUND, DEPARTMENT, FUNCTION ID, FUNCTION, DIVISION ID, DIVISION

## g1350（1 列）
- 見出し：DEPARTMENT
- 例1 値：GREATER BR AIRPORT DISTRICT | CLERK OF COURT | EMPLOY BR WORKFORCE DEVELOPMT | EMPLOY BR WORKFORCE DEVELOPMT | BUILDINGS AND GROUNDS
  - 同じ表の列：YEAR, FUND ID, FUND, DEPARTMENT ID, FUNCTION ID, FUNCTION, DIVISION ID, DIVISION

## g1351（1 列）
- 見出し：FUNCTION ID
- 例1 値：10 | 50 | 60 | 20 | 10
  - 同じ表の列：YEAR, FUND ID, FUND, DEPARTMENT ID, DEPARTMENT, FUNCTION, DIVISION ID, DIVISION

## g1352（1 列）
- 見出し：FUNCTION
- 例1 値：GENERAL GOVERNMENT EXPEND | CULTURE - RECREATION EXPEND | GENERAL GOVERNMENT EXPEND | CULTURE - RECREATION EXPEND | PUBL SAF REV-CHARGES FOR SERV
  - 同じ表の列：YEAR, FUND ID, FUND, DEPARTMENT ID, DEPARTMENT, FUNCTION ID, DIVISION ID, DIVISION

## g1353（1 列）
- 見出し：DIVISION ID
- 例1 値：0530 | 5210 | 7910 | 3020 | 3200
  - 同じ表の列：YEAR, FUND ID, FUND, DEPARTMENT ID, DEPARTMENT, FUNCTION ID, FUNCTION, DIVISION

## g1354（1 列）
- 見出し：DIVISION
- 例1 値：MOHSEP | EMS-OPERATIONS | ENV-SEWER DIVISION | EMS-OPERATIONS | CENTRAL GARAGE OPER & MAINT
  - 同じ表の列：YEAR, FUND ID, FUND, DEPARTMENT ID, DEPARTMENT, FUNCTION ID, FUNCTION, DIVISION ID

## g1355（1 列）
- 見出し：JOURNAL ENTRY PERIOD
- 例1 値：5 | 1 | 11 | 4 | 2
  - 同じ表の列：YEAR, FUND ID, FUND, DEPARTMENT ID, DEPARTMENT, FUNCTION ID, FUNCTION, DIVISION ID

## g1356（1 列）
- 見出し：VOTING PRECINCT
- 例1 値：1-004 | 1-010 | 3-049 | 3-060 | 1-078
  - 同じ表の列：WARD, PRECINCT, METRO COUNCIL, US HOUSE, PSC, BESE, LA HOUSE, LA SENATE

## g1357（2 列）
- 見出し：WARD
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：VOTING PRECINCT, PRECINCT, METRO COUNCIL, US HOUSE, PSC, BESE, LA HOUSE, LA SENATE
- 例2 値：09 | 14 | 03 | 21 | 03
  - 同じ表の列：app_no, start_datetime, stop_datetime

## g1358（1 列）
- 見出し：PRECINCT
- 例1 値：74 | 19 | 86 | 54 | 71
  - 同じ表の列：VOTING PRECINCT, WARD, METRO COUNCIL, US HOUSE, PSC, BESE, LA HOUSE, LA SENATE

## g1359（1 列）
- 見出し：METRO COUNCIL
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：VOTING PRECINCT, WARD, PRECINCT, US HOUSE, PSC, BESE, LA HOUSE, LA SENATE

## g1360（1 列）
- 見出し：US HOUSE
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：VOTING PRECINCT, WARD, PRECINCT, METRO COUNCIL, PSC, BESE, LA HOUSE, LA SENATE

## g1361（1 列）
- 見出し：PSC
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：VOTING PRECINCT, WARD, PRECINCT, METRO COUNCIL, US HOUSE, BESE, LA HOUSE, LA SENATE

## g1362（1 列）
- 見出し：BESE
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：VOTING PRECINCT, WARD, PRECINCT, METRO COUNCIL, US HOUSE, PSC, LA HOUSE, LA SENATE

## g1363（1 列）
- 見出し：LA HOUSE
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：VOTING PRECINCT, WARD, PRECINCT, METRO COUNCIL, US HOUSE, PSC, BESE, LA SENATE

## g1364（1 列）
- 見出し：LA SENATE
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：VOTING PRECINCT, WARD, PRECINCT, METRO COUNCIL, US HOUSE, PSC, BESE, LA HOUSE

## g1365（1 列）
- 見出し：State
- 例1 値：New Hampshire | Maine | Massachusetts | Rhode Island | United States
  - 同じ表の列：2012, 2014

## g1366（1 列）
- 見出し：2012
- 例1 値：86 | 69 | 78 | 73 | 84
  - 同じ表の列：State, 2014

## g1367（1 列）
- 見出し：2014
- 例1 値：85 | 87 | 70 | 85 | 87
  - 同じ表の列：State, 2012

## g1368（1 列）
- 見出し：StateAbbr
- 例1 値：AL | AL | AL | AL | US
  - 同じ表の列：Year, StateDesc, CityName, GeographicLevel, DataSource, Category, UniqueID, Measure

## g1369（1 列）
- 見出し：StateDesc
- 例1 値：Alabama | Alabama | Alabama | Alabama | Alabama
  - 同じ表の列：Year, StateAbbr, CityName, GeographicLevel, DataSource, Category, UniqueID, Measure

## g1370（1 列）
- 見出し：CityName
- 例1 値：Birmingham | Birmingham | Birmingham | Birmingham | Birmingham
  - 同じ表の列：Year, StateAbbr, StateDesc, GeographicLevel, DataSource, Category, UniqueID, Measure

## g1371（1 列）
- 見出し：GeographicLevel
- 例1 値：Census Tract | Census Tract | Census Tract | Census Tract | Census Tract
  - 同じ表の列：Year, StateAbbr, StateDesc, CityName, DataSource, Category, UniqueID, Measure

## g1372（2 列）
- 見出し：DataSource
- 例1 値：BRFSS | BRFSS | BRFSS | BRFSS | BRFSS
  - 同じ表の列：Year, StateAbbr, StateDesc, CityName, GeographicLevel, Category, UniqueID, Measure
- 例2 値：BRFSS | BRFSS | BRFSS | BRFSS | BRFSS
  - 同じ表の列：Rowid, Year, LocationAbbr, LocationDesc, Category, Indicator, Response, Data_Value_Unit

## g1373（1 列）
- 見出し：Category
- 例1 値：Health Outcomes | Prevention | Prevention | Health Outcomes | Health Outcomes
  - 同じ表の列：Year, StateAbbr, StateDesc, CityName, GeographicLevel, DataSource, UniqueID, Measure

## g1374（1 列）
- 見出し：UniqueID
- 例1 値：0107000-01073005101 | 0107000-01073012703 | 0107000-01073011210 | 0107000-01073005702 | 0107000-01073005701
  - 同じ表の列：Year, StateAbbr, StateDesc, CityName, GeographicLevel, DataSource, Category, Measure

## g1375（1 列）
- 見出し：Measure
- 例1 値：Taking medicine for high blood pressure… | Binge drinking among adults aged >=18 Y… | Visits to doctor for routine checkup wi… | High blood pressure among adults aged >… | Current asthma among adults aged >=18 Y…
  - 同じ表の列：Year, StateAbbr, StateDesc, CityName, GeographicLevel, DataSource, Category, UniqueID

## g1376（2 列）
- 見出し：Data_Value_Unit
- 例1 値：% | % | % | % | %
  - 同じ表の列：Year, StateAbbr, StateDesc, CityName, GeographicLevel, DataSource, Category, UniqueID
- 例2 値：% | % | % | % | %
  - 同じ表の列：Rowid, Year, LocationAbbr, LocationDesc, DataSource, Category, Indicator, Response

## g1377（1 列）
- 見出し：Rowid
- 例1 値：2016~1~YESNO01~ECIG~DISSTAT~DISABL~RACE… | 2016~1~YESNO01~UTDCERV~DISSTAT~DISABL~R… | 2016~1~BMI02~BMI~DISSTAT~DISABL~RACE~HI… | 2016~1~YESNO02~HEART~DISSTAT~DISABL~RAC… | 2016~1~YESNO01~UTDCRC~DISSTAT~DISABL~RA…
  - 同じ表の列：Year, LocationAbbr, LocationDesc, DataSource, Category, Indicator, Response, Data_Value_Unit

## g1378（1 列）
- 見出し：LocationAbbr
- 例1 値：AL | AL | AL | AL | AL
  - 同じ表の列：Rowid, Year, LocationDesc, DataSource, Category, Indicator, Response, Data_Value_Unit

## g1379（1 列）
- 見出し：LocationDesc
- 例1 値：Alabama | Alabama | Alabama | Alabama | Alabama
  - 同じ表の列：Rowid, Year, LocationAbbr, DataSource, Category, Indicator, Response, Data_Value_Unit

## g1380（1 列）
- 見出し：Category
- 例1 値：Health Risks & Behaviors | Barriers & Costs of Health Care | Prevention & Screenings | Barriers & Costs of Health Care | Chronic Conditions
  - 同じ表の列：Rowid, Year, LocationAbbr, LocationDesc, DataSource, Indicator, Response, Data_Value_Unit

## g1381（1 列）
- 見出し：Indicator
- 例1 値：Up-to-date cervical cancer screening am… | Disability status and types among adult… | Average hours of sleep in a 24-hour per… | Ever had chronic obstructive pulmonary … | Body mass index category among adults 1…
  - 同じ表の列：Rowid, Year, LocationAbbr, LocationDesc, DataSource, Category, Response, Data_Value_Unit

## g1382（1 列）
- 見出し：Response
- 例1 値：Yes | 7-9 Hours | Yes | 10+ Hours | Yes
  - 同じ表の列：Rowid, Year, LocationAbbr, LocationDesc, DataSource, Category, Indicator, Data_Value_Unit

## g1383（1 列）
- 見出し：Data_Value_Type
- 例1 値：Age-adjusted Prevalence | Age-adjusted Prevalence | Prevalence | Prevalence | Age-adjusted Prevalence
  - 同じ表の列：Rowid, Year, LocationAbbr, LocationDesc, DataSource, Category, Indicator, Response

## g1384（1 列）
- 見出し：building_id
- 例1 値：124870 | 35750 | 73252 | 135103 | 28762
  - 同じ表の列：parcel_id, building_type, dwelling_units, building_built_year, building_sqft, building_value, building_from_st, building_dir

## g1385（1 列）
- 見出し：parcel_id
- 例1 値：31325 | 110466 | 56484 | 64489 | 1721
  - 同じ表の列：building_id, building_type, dwelling_units, building_built_year, building_sqft, building_value, building_from_st, building_dir

## g1386（1 列）
- 見出し：building_type
- 例1 値：Single Family (Non-Mobile Home Park) | Single Family (Non-Mobile Home Park) | Single Family (Non-Mobile Home Park) | Single Family (Non-Mobile Home Park) | Single Family (Non-Mobile Home Park)
  - 同じ表の列：building_id, parcel_id, dwelling_units, building_built_year, building_sqft, building_value, building_from_st, building_dir

## g1387（1 列）
- 見出し：dwelling_units
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：building_id, parcel_id, building_type, building_built_year, building_sqft, building_value, building_from_st, building_dir

## g1388（1 列）
- 見出し：building_built_year
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：building_id, parcel_id, building_type, dwelling_units, building_sqft, building_value, building_from_st, building_dir

## g1389（1 列）
- 見出し：building_sqft
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：building_id, parcel_id, building_type, dwelling_units, building_built_year, building_value, building_from_st, building_dir

## g1390（1 列）
- 見出し：building_value
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：building_id, parcel_id, building_type, dwelling_units, building_built_year, building_sqft, building_from_st, building_dir

## g1391（1 列）
- 見出し：building_from_st
- 例1 値：6011.0000 | 2020.0000 | 6001.0000 | 4216.0000 | 5927.0000
  - 同じ表の列：building_id, parcel_id, building_type, dwelling_units, building_built_year, building_sqft, building_value, building_dir

## g1392（1 列）
- 見出し：building_dir
- 例1 値：E | E | E | N | E
  - 同じ表の列：building_id, parcel_id, building_type, dwelling_units, building_built_year, building_sqft, building_value, building_from_st

## g1393（1 列）
- 見出し：building_city
- 例1 値：Kansas City | Kansas City | Kansas City | Kansas City | Kansas City
  - 同じ表の列：building_id, parcel_id, building_type, dwelling_units, building_built_year, building_sqft, building_value, building_from_st

## g1394（1 列）
- 見出し：Duration
- 例1 値：1:35 | 0:09 | 0:59 | 1:20 | 1:25
  - 同じ表の列：1-year, 2-year, 5-year, 10-year, 25-year, 50-year, 100-year, 500-year

## g1395（1 列）
- 見出し：1-year
- 例1 値：2.3199999999999998 | 2.29 | 1.28 | 0.74 | 1.52
  - 同じ表の列：Duration, 2-year, 5-year, 10-year, 25-year, 50-year, 100-year, 500-year

## g1396（1 列）
- 見出し：2-year
- 例1 値：1.32 | 2.04 | 2.06 | 2.84 | 2.56
  - 同じ表の列：Duration, 1-year, 5-year, 10-year, 25-year, 50-year, 100-year, 500-year

## g1397（1 列）
- 見出し：5-year
- 例1 値：3.12 | 1.21 | 2.79 | 1.54 | 1.17
  - 同じ表の列：Duration, 1-year, 2-year, 10-year, 25-year, 50-year, 100-year, 500-year

## g1398（1 列）
- 見出し：10-year
- 例1 値：1.88 | 4.3600000000000003 | 1.97 | 5.12 | 3.73
  - 同じ表の列：Duration, 1-year, 2-year, 5-year, 25-year, 50-year, 100-year, 500-year

## g1399（1 列）
- 見出し：25-year
- 例1 値：2.97 | 4.62 | 2.15 | 3.23 | 1.88
  - 同じ表の列：Duration, 1-year, 2-year, 5-year, 10-year, 50-year, 100-year, 500-year

## g1400（1 列）
- 見出し：50-year
- 例1 値：4.37 | 2.1800000000000002 | 3.01 | 4.7699999999999996 | 1.1200000000000001
  - 同じ表の列：Duration, 1-year, 2-year, 5-year, 10-year, 25-year, 100-year, 500-year

## g1401（1 列）
- 見出し：100-year
- 例1 値：3.23 | 6.52 | 2.98 | 5.14 | 2.48
  - 同じ表の列：Duration, 1-year, 2-year, 5-year, 10-year, 25-year, 50-year, 500-year

## g1402（1 列）
- 見出し：500-year
- 例1 値：6.71 | 7.28 | 2.77 | 9.84 | 6.82
  - 同じ表の列：Duration, 1-year, 2-year, 5-year, 10-year, 25-year, 50-year, 100-year

## g1403（1 列）
- 見出し：Type
- 例1 値：General plaintiff record | General plaintiff record | Civil record | General plaintiff record | Criminal record
  - 同じ表の列：Years, File size (in MB)

## g1404（1 列）
- 見出し：Years
- 例1 値：1976 through July 1979 | 1966_1970 | 1976 through July 1979 | 1966_1970 | 1966_1970
  - 同じ表の列：Type, File size (in MB)

## g1405（1 列）
- 見出し：File size (in MB)
- 例1 値：11 | 177 | 7 | 48.69 | 17.09
  - 同じ表の列：Type, Years

## g1406（1 列）
- 見出し：contest_id
- 例1 値：43257 | 43666 | 43555 | 43275 | 43368
  - 同じ表の列：ballot_title_1, ballot_title_2, candidate_id, party_id, party, districtname1, district_id, group_type

## g1407（1 列）
- 見出し：ballot_title_1
- 例1 値：Precinct Committee Officer | Precinct Committee Officer | Precinct Committee Officer | Precinct Committee Officer | Precinct Committee Officer
  - 同じ表の列：contest_id, ballot_title_2, candidate_id, party_id, party, districtname1, district_id, group_type

## g1408（1 列）
- 見出し：ballot_title_2
- 例1 値：BOT 01-0260 PCO | HOLLYWOOD PCO | RNT 11-0354 PCO | ROUNDTABLE PCO | MABEL PCO
  - 同じ表の列：contest_id, ballot_title_1, candidate_id, party_id, party, districtname1, district_id, group_type

## g1409（1 列）
- 見出し：candidate_id
- 例1 値：17706 | 17330 | 19056 | 17924 | 17902
  - 同じ表の列：contest_id, ballot_title_1, ballot_title_2, party_id, party, districtname1, district_id, group_type

## g1410（1 列）
- 見出し：party_id
- 例1 値：19 | 19 | 19 | 19 | 19
  - 同じ表の列：contest_id, ballot_title_1, ballot_title_2, candidate_id, party, districtname1, district_id, group_type

## g1411（1 列）
- 見出し：party
- 例1 値：RPC | RPC | DPC | RPC | RPC
  - 同じ表の列：contest_id, ballot_title_1, ballot_title_2, candidate_id, party_id, districtname1, district_id, group_type

## g1412（1 列）
- 見出し：districtname1
- 例1 値：PRECINCT ISS 05-0548 PCO | PRECINCT MABEL PCO | PRECINCT NPK 33-0857 PCO | PRECINCT BEL 48-0223 PCO | PRECINCT BUR 34-1104 PCO
  - 同じ表の列：contest_id, ballot_title_1, ballot_title_2, candidate_id, party_id, party, district_id, group_type

## g1413（1 列）
- 見出し：district_id
- 例1 値：11643 | 11847 | 12106 | 11908 | 11987
  - 同じ表の列：contest_id, ballot_title_1, ballot_title_2, candidate_id, party_id, party, districtname1, group_type

## g1414（1 列）
- 見出し：group_type
- 例1 値：PCO | PCO | PCO | PCO | PCO
  - 同じ表の列：contest_id, ballot_title_1, ballot_title_2, candidate_id, party_id, party, districtname1, district_id

## g1415（1 列）
- 見出し：partisan
- 例1 値：N | N | N | N | N
  - 同じ表の列：contest_id, ballot_title_1, ballot_title_2, candidate_id, party_id, party, districtname1, district_id

## g1416（1 列）
- 見出し：Elected official
- 例1 値：[個人名のため削除] | [個人名のため削除] | [個人名のため削除] | [個人名のため削除] | [個人名のため削除]
  - 同じ表の列：Position, Start year, End year

## g1417（1 列）
- 見出し：Position
- 例1 値：Superior Court Judge | Superior Court Judge | Superior Court Clerk | Superior Court Clerk | Treasurer
  - 同じ表の列：Elected official, Start year, End year

## g1418（1 列）
- 見出し：Start year
- 例1 値：2019 | 1909 | 1882 | 1890 | 1980
  - 同じ表の列：Elected official, Position, End year

## g1419（1 列）
- 見出し：End year
- 例1 値：1890 | 1900 | 1888 | 2005 | 1896
  - 同じ表の列：Elected official, Position, Start year

## g1420（1 列）
- 見出し：Date of Issuance
- 例1 値：2005-01-15T00:00:00.000 | 2013-07-30T00:00:00.000 | 2005-08-30T00:00:00.000 | 2014-06-02T00:00:00.000 | 2012-07-15T00:00:00.000
  - 同じ表の列：Face Amount, Outstanding Balance, Interest Rate

## g1421（1 列）
- 見出し：Face Amount
- 例1 値：3815867 | 4600000 | 1762345 | 562199 | 500000
  - 同じ表の列：Date of Issuance, Outstanding Balance, Interest Rate

## g1422（1 列）
- 見出し：Outstanding Balance
- 例1 値：NOT PROVIDED | NOT PROVIDED | 480000 | NOT PROVIDED | NOT PROVIDED
  - 同じ表の列：Date of Issuance, Face Amount, Interest Rate

## g1423（1 列）
- 見出し：Interest Rate
- 例1 値：2 | NOT PROVIDED | NOT PROVIDED | NOT PROVIDED | NOT PROVIDED
  - 同じ表の列：Date of Issuance, Face Amount, Outstanding Balance

## g1424（1 列）
- 見出し：REF_NUM
- 例1 値：00000804 | 00000435 | 00000030 | 00000041 | 00000662
  - 同じ表の列：DATE_COMPL, CERT_NUM, WELL_NUM, WELL_TYPE, WELL_USE, SUBDIV_1, SUBDIV_2, SUBDIV_3

## g1425（1 列）
- 見出し：DATE_COMPL
- 例1 値：1987-04-01T00:00:00.000Z | 1987-03-31T00:00:00.000Z | 1987-01-06T00:00:00.000Z | 1987-05-29T00:00:00.000Z | 1987-07-03T00:00:00.000Z
  - 同じ表の列：REF_NUM, CERT_NUM, WELL_NUM, WELL_TYPE, WELL_USE, SUBDIV_1, SUBDIV_2, SUBDIV_3

## g1426（1 列）
- 見出し：CERT_NUM
- 例1 値：A000095 | A000754 | A000070 | A000307 | A001380
  - 同じ表の列：REF_NUM, DATE_COMPL, WELL_NUM, WELL_TYPE, WELL_USE, SUBDIV_1, SUBDIV_2, SUBDIV_3

## g1427（1 列）
- 見出し：WELL_NUM
- 例1 値：NORTH WELL | 2 | 1 | SOUTH WELL
  - 同じ表の列：REF_NUM, DATE_COMPL, CERT_NUM, WELL_TYPE, WELL_USE, SUBDIV_1, SUBDIV_2, SUBDIV_3

## g1428（1 列）
- 見出し：WELL_TYPE
- 例1 値：Water Well | Water Well | Water Well | Water Well | Water Well
  - 同じ表の列：REF_NUM, DATE_COMPL, CERT_NUM, WELL_NUM, WELL_USE, SUBDIV_1, SUBDIV_2, SUBDIV_3

## g1429（1 列）
- 見出し：WELL_USE
- 例1 値：Domestic | Domestic | Domestic | Domestic | Domestic
  - 同じ表の列：REF_NUM, DATE_COMPL, CERT_NUM, WELL_NUM, WELL_TYPE, SUBDIV_1, SUBDIV_2, SUBDIV_3

## g1430（1 列）
- 見出し：SUBDIV_1
- 例1 値：SE 1/4 | NW 1/4 | NW 1/4 | NE 1/4 | NE 1/4
  - 同じ表の列：REF_NUM, DATE_COMPL, CERT_NUM, WELL_NUM, WELL_TYPE, WELL_USE, SUBDIV_2, SUBDIV_3

## g1431（1 列）
- 見出し：SUBDIV_2
- 例1 値：NW 1/4 | NE 1/4 | SW 1/4 | SE 1/4 | SE 1/4
  - 同じ表の列：REF_NUM, DATE_COMPL, CERT_NUM, WELL_NUM, WELL_TYPE, WELL_USE, SUBDIV_1, SUBDIV_3

## g1432（1 列）
- 見出し：SUBDIV_3
- 例1 値：SE 1/4 | NE 1/4 | NW 1/4 | SW 1/4 | SW 1/4
  - 同じ表の列：REF_NUM, DATE_COMPL, CERT_NUM, WELL_NUM, WELL_TYPE, WELL_USE, SUBDIV_1, SUBDIV_2

## g1433（1 列）
- 見出し：TWN_NUM
- 例1 値：29 | 39 | 35 | 35 | 34
  - 同じ表の列：REF_NUM, DATE_COMPL, CERT_NUM, WELL_NUM, WELL_TYPE, WELL_USE, SUBDIV_1, SUBDIV_2

## g1434（1 列）
- 見出し：Report Number
- 例1 値：MCP2001001Z | MCP3296001Z | MCP2962008G | MCP3245004S | DD56300026
  - 同じ表の列：Local Case Number, ACRS Report Type, Crash Date/Time, Route Type, Municipality, Related Non-Motorist, Collision Type, Weather

## g1435（1 列）
- 見出し：Local Case Number
- 例1 値：220010551 | 16036336 | 16009979 | 210040088 | 210045627
  - 同じ表の列：Report Number, ACRS Report Type, Crash Date/Time, Route Type, Municipality, Related Non-Motorist, Collision Type, Weather

## g1436（1 列）
- 見出し：ACRS Report Type
- 例1 値：Injury Crash | Injury Crash | Injury Crash | Injury Crash | Fatal Crash
  - 同じ表の列：Report Number, Local Case Number, Crash Date/Time, Route Type, Municipality, Related Non-Motorist, Collision Type, Weather

## g1437（1 列）
- 見出し：Crash Date/Time
- 例1 値：2023-09-20T15:12:00.000 | 2022-08-17T16:00:00.000 | 2021-11-14T12:45:00.000 | 2021-09-18T16:51:00.000 | 2016-08-20T12:40:00.000
  - 同じ表の列：Report Number, Local Case Number, ACRS Report Type, Route Type, Municipality, Related Non-Motorist, Collision Type, Weather

## g1438（1 列）
- 見出し：Route Type
- 例1 値：County | Other Public Roadway | County | Maryland (State) | County
  - 同じ表の列：Report Number, Local Case Number, ACRS Report Type, Crash Date/Time, Municipality, Related Non-Motorist, Collision Type, Weather

## g1439（1 列）
- 見出し：Municipality
- 例1 値：N/A | SOMERSET | N/A | N/A | N/A
  - 同じ表の列：Report Number, Local Case Number, ACRS Report Type, Crash Date/Time, Route Type, Related Non-Motorist, Collision Type, Weather

## g1440（1 列）
- 見出し：Related Non-Motorist
- 例1 値：BICYCLIST | PEDESTRIAN | BICYCLIST | PEDESTRIAN | PEDESTRIAN
  - 同じ表の列：Report Number, Local Case Number, ACRS Report Type, Crash Date/Time, Route Type, Municipality, Collision Type, Weather

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
