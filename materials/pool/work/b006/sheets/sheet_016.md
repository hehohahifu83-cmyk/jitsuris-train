# ラベル用シート 016 / 018

- LABEL_GUIDE v1.8 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_016.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1801（1 列）
- 見出し：Permit application filing date
- 例1 値：2020-03-19 | 2019-10-10 | 2020-05-06 | 2020-11-09 | 2020-07-15
  - 同じ表の列：Permit application …, Zoning review appro…, Started appeal, Completed appeal, Permit issued, Permit application …, Permit application …, Permit issued date

## g1802（1 列）
- 見出し：Zoning review approved
- 例1 値：t | t | t | f | t
  - 同じ表の列：Permit application …, Permit application …, Started appeal, Completed appeal, Permit issued, Permit application …, Permit application …, Permit issued date

## g1803（1 列）
- 見出し：Started appeal
- 例1 値：f | f | f | f | f
  - 同じ表の列：Permit application …, Permit application …, Zoning review appro…, Completed appeal, Permit issued, Permit application …, Permit application …, Permit issued date

## g1804（1 列）
- 見出し：Completed appeal
- 例1 値：f | f | f | f | f
  - 同じ表の列：Permit application …, Permit application …, Zoning review appro…, Started appeal, Permit issued, Permit application …, Permit application …, Permit issued date

## g1805（1 列）
- 見出し：Permit issued
- 例1 値：t | f | f | t | t
  - 同じ表の列：Permit application …, Permit application …, Zoning review appro…, Started appeal, Completed appeal, Permit application …, Permit application …, Permit issued date

## g1806（1 列）
- 見出し：Permit application abandoned
- 例1 値：t | f | f | f | f
  - 同じ表の列：Permit application …, Permit application …, Zoning review appro…, Started appeal, Completed appeal, Permit issued, Permit application …, Permit issued date

## g1807（1 列）
- 見出し：Permit application inactive
- 例1 値：f | f | f | f | f
  - 同じ表の列：Permit application …, Permit application …, Zoning review appro…, Started appeal, Completed appeal, Permit issued, Permit application …, Permit issued date

## g1808（1 列）
- 見出し：Permit issued date
- 例1 値：2021-10-05 | 2020-10-08 | 2019-11-05 | 2020-12-09 | 2020-08-24
  - 同じ表の列：Permit application …, Permit application …, Zoning review appro…, Started appeal, Completed appeal, Permit issued, Permit application …, Permit application …

## g1809（1 列）
- 見出し：Days to permit issuance
- 例1 値：33 | 159 | 20 | 15 | 68
  - 同じ表の列：Permit application …, Permit application …, Zoning review appro…, Started appeal, Completed appeal, Permit issued, Permit application …, Permit application …

## g1810（1 列）
- 見出し：agency
- 例1 値：OED | OED | OED | BPDA | OED
  - 同じ表の列：neighborhood, developer, subcontractor, trade, period_ending, gender, race, boston_resident

## g1811（4 列）
- 見出し：neighborhood
- 例1 値：South Boston | Dorchester | Dorchester | Back Bay | Downtown
  - 同じ表の列：agency, developer, subcontractor, trade, period_ending, gender, race, boston_resident
- 例2 値：Boston | Hyde Park | Dorchester | East Boston | Allston
  - 同じ表の列：date, violation_type, year_built, year_remodeled, property_type

## g1812（1 列）
- 見出し：developer
- 例1 値：City of Boston | Mass General Hospital | The Community Builders, Inc. | Boston Communities LLC | Suffolk University
  - 同じ表の列：agency, neighborhood, subcontractor, trade, period_ending, gender, race, boston_resident

## g1813（1 列）
- 見出し：subcontractor
- 例1 値：Sunrise Erectors, Inc. | Colantonio Incorporated (SC) | Aldon Electric Inc. | S & F Concrete | Fred Deroma & Son (SC)
  - 同じ表の列：agency, neighborhood, developer, trade, period_ending, gender, race, boston_resident

## g1814（1 列）
- 見出し：trade
- 例1 値：Carpenter | Electrician | Electrician | Carpenter | Electrician
  - 同じ表の列：agency, neighborhood, developer, subcontractor, period_ending, gender, race, boston_resident

## g1815（1 列）
- 見出し：period_ending
- 例1 値：2026-10-18 | 2026-10-18 | 2026-10-18 | 2026-10-17 | 2026-10-17
  - 同じ表の列：agency, neighborhood, developer, subcontractor, trade, gender, race, boston_resident

## g1816（1 列）
- 見出し：gender
- 例1 値：Man | Man | Man | Woman | Man
  - 同じ表の列：agency, neighborhood, developer, subcontractor, trade, period_ending, race, boston_resident

## g1817（1 列）
- 見出し：race
- 例1 値：Hispanic/Latino | Caucasian | Caucasian | Hispanic/Latino | African American
  - 同じ表の列：agency, neighborhood, developer, subcontractor, trade, period_ending, gender, boston_resident

## g1818（1 列）
- 見出し：boston_resident
- 例1 値：f | f | f | f | t
  - 同じ表の列：agency, neighborhood, developer, subcontractor, trade, period_ending, gender, race

## g1819（1 列）
- 見出し：worker_hours_this_period
- 例1 値：65 | 41.5 | 4 | 6 | 318
  - 同じ表の列：agency, neighborhood, developer, subcontractor, trade, period_ending, gender, race

## g1820（1 列）
- 見出し：statefp20
- 例1 値：25 | 25 | 25 | 25 | 25
  - 同じ表の列：countyfp20, tractce20, geoid20, namelsad20, mtfcc20, funcstat20, aland20, awater20

## g1821（1 列）
- 見出し：countyfp20
- 例1 値：025 | 025 | 025 | 025 | 025
  - 同じ表の列：statefp20, tractce20, geoid20, namelsad20, mtfcc20, funcstat20, aland20, awater20

## g1822（1 列）
- 見出し：tractce20
- 例1 値：020304 | 120600 | 010702 | 000302 | 061000
  - 同じ表の列：statefp20, countyfp20, geoid20, namelsad20, mtfcc20, funcstat20, aland20, awater20

## g1823（1 列）
- 見出し：geoid20
- 例1 値：25025981502 | 25025070201 | 25025070802 | 25025120700 | 25025140102
  - 同じ表の列：statefp20, countyfp20, tractce20, namelsad20, mtfcc20, funcstat20, aland20, awater20

## g1824（1 列）
- 見出し：namelsad20
- 例1 値：Census Tract | Census Tract | Census Tract | Census Tract | Census Tract
  - 同じ表の列：statefp20, countyfp20, tractce20, geoid20, mtfcc20, funcstat20, aland20, awater20

## g1825（1 列）
- 見出し：mtfcc20
- 例1 値：G5020 | G5020 | G5020 | G5020 | G5020
  - 同じ表の列：statefp20, countyfp20, tractce20, geoid20, namelsad20, funcstat20, aland20, awater20

## g1826（1 列）
- 見出し：funcstat20
- 例1 値：S | S | S | S | S
  - 同じ表の列：statefp20, countyfp20, tractce20, geoid20, namelsad20, mtfcc20, aland20, awater20

## g1827（1 列）
- 見出し：aland20
- 例1 値：268833.000000000000000 | 684300.000000000000000 | 348074.000000000000000 | 1417183.000000000000000 | 165170.000000000000000
  - 同じ表の列：statefp20, countyfp20, tractce20, geoid20, namelsad20, mtfcc20, funcstat20, awater20

## g1828（1 列）
- 見出し：awater20
- 例1 値：0.000000000000000 | 0.000000000000000 | 0.000000000000000 | 0.000000000000000 | 0.000000000000000
  - 同じ表の列：statefp20, countyfp20, tractce20, geoid20, namelsad20, mtfcc20, funcstat20, aland20

## g1829（1 列）
- 見出し：intptlat20
- 例1 値：+42.3465040 | +42.2996758 | +42.3500656 | +42.3060353 | +42.3419678
  - 同じ表の列：statefp20, countyfp20, tractce20, geoid20, namelsad20, mtfcc20, funcstat20, aland20

## g1830（1 列）
- 見出し：collection_date
- 例1 値：2017-07-05 | 2018-08-01 | 2017-05-05 | 2015-03-17 | 2015-12-30
  - 同じ表の列：crime_guns_recovered, guns_recovered_safe…, buyback_guns_recove…

## g1831（1 列）
- 見出し：crime_guns_recovered
- 例1 値：6 | 9 | 0 | 0 | 0
  - 同じ表の列：collection_date, guns_recovered_safe…, buyback_guns_recove…

## g1832（1 列）
- 見出し：guns_recovered_safeguard
- 例1 値：0 | 0 | 0 | 0 | 2
  - 同じ表の列：collection_date, crime_guns_recovered, buyback_guns_recove…

## g1833（1 列）
- 見出し：buyback_guns_recovered
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：collection_date, crime_guns_recovered, guns_recovered_safe…

## g1834（1 列）
- 見出し：fc_num
- 例1 値：FC25000681 | FC25000008 | FC25000814 | FC25000611 | FC25000844
  - 同じ表の列：supervisor, city, state, duration, circumstance, basis, vehicle_year, vehicle_state

## g1835（1 列）
- 見出し：supervisor
- 例1 値：010621 | 116141 | 010092 | 099722 | 009266
  - 同じ表の列：fc_num, city, state, duration, circumstance, basis, vehicle_year, vehicle_state

## g1836（1 列）
- 見出し：duration
- 例1 値：NULL | 5 | 0 | NULL | NULL
  - 同じ表の列：fc_num, supervisor, city, state, circumstance, basis, vehicle_year, vehicle_state

## g1837（1 列）
- 見出し：circumstance
- 例1 値：Stopped | Observed | Encountered | Stopped | Stopped
  - 同じ表の列：fc_num, supervisor, city, state, duration, basis, vehicle_year, vehicle_state

## g1838（1 列）
- 見出し：basis
- 例1 値：Reasonable Suspicion | Reasonable Suspicion | Encounter | Intel | Reasonable Suspicion
  - 同じ表の列：fc_num, supervisor, city, state, duration, circumstance, vehicle_year, vehicle_state

## g1839（1 列）
- 見出し：vehicle_year
- 例1 値：NULL | NULL | NULL | NULL | NULL
  - 同じ表の列：fc_num, supervisor, city, state, duration, circumstance, basis, vehicle_state

## g1840（1 列）
- 見出し：vehicle_state
- 例1 値：NULL | NULL | MI | NULL | NULL
  - 同じ表の列：fc_num, supervisor, city, state, duration, circumstance, basis, vehicle_year

## g1841（1 列）
- 見出し：vehicle_model
- 例1 値：NULL | NULL | 528I | NULL | NULL
  - 同じ表の列：fc_num, supervisor, city, state, duration, circumstance, basis, vehicle_year

## g1842（1 列）
- 見出し：user_count
- 例1 値：9443 | 7763 | 9521 | 9926 | 6492
  - 同じ表の列：date

## g1843（1 列）
- 見出し：CCL #
- 例1 値：CCL445153 | CCL475176 | CCL459488 | CCL423728 | CCL437374
  - 同じ表の列：Category, Add Date, Year, Quarter, Quarter Activity, Type, Contribution Date, Contribution Amount

## g1844（1 列）
- 見出し：Category
- 例1 値：CCCLIENT | CCLOBBY | CCLOBBY | CCCLIENT | CCLOBBY
  - 同じ表の列：CCL #, Add Date, Year, Quarter, Quarter Activity, Type, Contribution Date, Contribution Amount

## g1845（1 列）
- 見出し：Add Date
- 例1 値：2022-05-26 20:30:59.347+00 | 2022-04-19 18:55:58.72+00 | 2022-04-19 18:13:55.64+00 | 2022-04-20 17:12:19.68+00 | 2022-04-20 18:02:48.75+00
  - 同じ表の列：CCL #, Category, Year, Quarter, Quarter Activity, Type, Contribution Date, Contribution Amount

## g1846（1 列）
- 見出し：Quarter
- 例1 値：1st | 1st | 1st | 1st | 1st
  - 同じ表の列：CCL #, Category, Add Date, Year, Quarter Activity, Type, Contribution Date, Contribution Amount

## g1847（1 列）
- 見出し：Quarter Activity
- 例1 値：N | Y | N | Y | N
  - 同じ表の列：CCL #, Category, Add Date, Year, Quarter, Type, Contribution Date, Contribution Amount

## g1848（1 列）
- 見出し：Type
- 例1 値：Lobbyist Activity | Contribution | Lobbyist Activity | Client/Entity Activity | Contribution
  - 同じ表の列：CCL #, Category, Add Date, Year, Quarter, Quarter Activity, Contribution Date, Contribution Amount

## g1849（1 列）
- 見出し：Contribution Date
- 例1 値：2022-03-21 | 2022-02-17 | 2022-03-08 | 2022-01-24 | 2022-03-23
  - 同じ表の列：CCL #, Category, Add Date, Year, Quarter, Quarter Activity, Type, Contribution Amount

## g1850（1 列）
- 見出し：Contribution Amount
- 例1 値：0.00 | 0.00 | 0.00 | 200.00 | 200.00
  - 同じ表の列：CCL #, Category, Add Date, Year, Quarter, Quarter Activity, Type, Contribution Date

## g1851（1 列）
- 見出し：Incumbent/Candidate
- 例1 値：City Councilor | City Council, District 1 | City Councilor | Mayor | Boston city council candidate
  - 同じ表の列：CCL #, Category, Add Date, Year, Quarter, Quarter Activity, Type, Contribution Date

## g1852（1 列）
- 見出し：roll_call_id
- 例1 値：3246 | 3260 | 3266 | 3224 | 3261
  - 同じ表の列：docket_number, subject, vote_date, councillor, vote

## g1853（1 列）
- 見出し：docket_number
- 例1 値：0283 | 0168 | 0559 | 0285 | 0459
  - 同じ表の列：roll_call_id, subject, vote_date, councillor, vote

## g1854（1 列）
- 見出し：subject
- 例1 値：On the message and order, referred on F… | On the message and order, referred on O… | Message and order for your approval an … | On the message and order, referred on O… | On the message and ordinance, referred …
  - 同じ表の列：roll_call_id, docket_number, vote_date, councillor, vote

## g1855（1 列）
- 見出し：vote_date
- 例1 値：2023-12-13 | 2024-03-27 | 2023-12-13 | 2023-12-13 | 2024-03-20
  - 同じ表の列：roll_call_id, docket_number, subject, councillor, vote

## g1856（1 列）
- 見出し：councillor
- 例1 値：FitzGerald | Luoijeune | Breadon | Mejia | Weber
  - 同じ表の列：roll_call_id, docket_number, subject, vote_date, vote

## g1857（1 列）
- 見出し：vote
- 例1 値：Y | Y | NP | N | NP
  - 同じ表の列：roll_call_id, docket_number, subject, vote_date, councillor

## g1858（1 列）
- 見出し：issued_registration
- 例1 値：N | N | N | N | N
  - 同じ表の列：home-share eligible, limited-share eligi…, owners_current_lice…, income restricted, problem property, open violation count, legally restricted, units in building

## g1859（1 列）
- 見出し：home-share eligible
- 例1 値：N | N | N | N | N
  - 同じ表の列：issued_registration, limited-share eligi…, owners_current_lice…, income restricted, problem property, open violation count, legally restricted, units in building

## g1860（1 列）
- 見出し：limited-share eligible
- 例1 値：N | N | N | N | N
  - 同じ表の列：issued_registration, home-share eligible, owners_current_lice…, income restricted, problem property, open violation count, legally restricted, units in building

## g1861（1 列）
- 見出し：owners_current_license_types
- 例1 値：None | None | None | None | None
  - 同じ表の列：issued_registration, home-share eligible, limited-share eligi…, income restricted, problem property, open violation count, legally restricted, units in building

## g1862（1 列）
- 見出し：income restricted
- 例1 値：Y | N | N | Y | N
  - 同じ表の列：issued_registration, home-share eligible, limited-share eligi…, owners_current_lice…, problem property, open violation count, legally restricted, units in building

## g1863（1 列）
- 見出し：problem property
- 例1 値：N | N | N | N | N
  - 同じ表の列：issued_registration, home-share eligible, limited-share eligi…, owners_current_lice…, income restricted, open violation count, legally restricted, units in building

## g1864（1 列）
- 見出し：open violation count
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：issued_registration, home-share eligible, limited-share eligi…, owners_current_lice…, income restricted, problem property, legally restricted, units in building

## g1865（1 列）
- 見出し：legally restricted
- 例1 値：N | N | N | N | N
  - 同じ表の列：issued_registration, home-share eligible, limited-share eligi…, owners_current_lice…, income restricted, problem property, open violation count, units in building

## g1866（1 列）
- 見出し：units in building
- 例1 値：12 | 2 | 18 | 75 | 11
  - 同じ表の列：issued_registration, home-share eligible, limited-share eligi…, owners_current_lice…, income restricted, problem property, open violation count, legally restricted

## g1867（1 列）
- 見出し：oid
- 例1 値：834294657 | 2064192274 | 247114333 | 1423852628 | 543312657
  - 同じ表の列：cartegraph_id, locator_city_field, neighborhood_field, city_field, county_field, state_field, height_field_amount, height_field_unit

## g1868（1 列）
- 見出し：cartegraph_id
- 例1 値：2729 | 6063 | PB-26G_SIGN112087 | 4390 | R1-6a_SIGN109712
  - 同じ表の列：oid, locator_city_field, neighborhood_field, city_field, county_field, state_field, height_field_amount, height_field_unit

## g1869（1 列）
- 見出し：locator_city_field
- 例1 値：South Boston | Roslindale | Boston | Allston | SOUTH BOSTON
  - 同じ表の列：oid, cartegraph_id, neighborhood_field, city_field, county_field, state_field, height_field_amount, height_field_unit

## g1870（1 列）
- 見出し：neighborhood_field
- 例1 値：ROXBURY | FENWAY | ROXBURY
  - 同じ表の列：oid, cartegraph_id, locator_city_field, city_field, county_field, state_field, height_field_amount, height_field_unit

## g1871（1 列）
- 見出し：city_field
- 例1 値：East Boston | Roxbury | Boston | Boston | Hyde Park
  - 同じ表の列：oid, cartegraph_id, locator_city_field, neighborhood_field, county_field, state_field, height_field_amount, height_field_unit

## g1872（1 列）
- 見出し：county_field
- 例1 値：Suffolk | Suffolk | Suffolk | Suffolk | Suffolk
  - 同じ表の列：oid, cartegraph_id, locator_city_field, neighborhood_field, city_field, state_field, height_field_amount, height_field_unit

## g1873（1 列）
- 見出し：state_field
- 例1 値：Massachusetts | Massachusetts | Massachusetts | Massachusetts | Massachusetts
  - 同じ表の列：oid, cartegraph_id, locator_city_field, neighborhood_field, city_field, county_field, height_field_amount, height_field_unit

## g1874（1 列）
- 見出し：height_field_amount
- 例1 値：18.0 | 18.0 | 18.0 | 18.0 | 18.0
  - 同じ表の列：oid, cartegraph_id, locator_city_field, neighborhood_field, city_field, county_field, state_field, height_field_unit

## g1875（1 列）
- 見出し：height_field_unit
- 例1 値：in | in | in | in | in
  - 同じ表の列：oid, cartegraph_id, locator_city_field, neighborhood_field, city_field, county_field, state_field, height_field_amount

## g1876（1 列）
- 見出し：width_field_amount
- 例1 値：24.0 | 12.0 | 12.0 | 30.0 | 24.0
  - 同じ表の列：oid, cartegraph_id, locator_city_field, neighborhood_field, city_field, county_field, state_field, height_field_amount

## g1877（1 列）
- 見出し：Voucher
- 例1 値：03738636 | 03738407 | 03738827 | 03738394 | 03739187
  - 同じ表の列：Voucher Line, Distribution Line, Entered, Month(Number), Month, Fiscal Month, Fiscal Year, Year

## g1878（1 列）
- 見出し：Voucher Line
- 例1 値：1 | 1 | 2 | 2 | 4
  - 同じ表の列：Voucher, Distribution Line, Entered, Month(Number), Month, Fiscal Month, Fiscal Year, Year

## g1879（1 列）
- 見出し：Distribution Line
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Voucher, Voucher Line, Entered, Month(Number), Month, Fiscal Month, Fiscal Year, Year

## g1880（1 列）
- 見出し：Entered
- 例1 値：7/7/2026 | 7/7/2026 | 7/6/2026 | 7/6/2026 | 7/6/2026
  - 同じ表の列：Voucher, Voucher Line, Distribution Line, Month(Number), Month, Fiscal Month, Fiscal Year, Year

## g1881（1 列）
- 見出し：Month(Number)
- 例1 値：07 | 07 | 07 | 07 | 07
  - 同じ表の列：Voucher, Voucher Line, Distribution Line, Entered, Month, Fiscal Month, Fiscal Year, Year

## g1882（1 列）
- 見出し：Month
- 例1 値：July | July | July | July | July
  - 同じ表の列：Voucher, Voucher Line, Distribution Line, Entered, Month(Number), Fiscal Month, Fiscal Year, Year

## g1883（1 列）
- 見出し：Fiscal Month
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Voucher, Voucher Line, Distribution Line, Entered, Month(Number), Month, Fiscal Year, Year

## g1884（1 列）
- 見出し：Fiscal Year
- 例1 値：2027 | 2027 | 2027 | 2027 | 2027
  - 同じ表の列：Voucher, Voucher Line, Distribution Line, Entered, Month(Number), Month, Fiscal Month, Year

## g1885（1 列）
- 見出し：Dept
- 例1 値：180201 | 101046 | 175200 | 151100 | 300600
  - 同じ表の列：Voucher, Voucher Line, Distribution Line, Entered, Month(Number), Month, Fiscal Month, Fiscal Year

## g1886（1 列）
- 見出し：date
- 例1 値：2026-10-20 00:00:00+00 | 2026-10-22 00:00:00+00 | 2026-10-22 00:00:00+00 | 2026-10-22 00:00:00+00 | 2026-10-21 00:00:00+00
  - 同じ表の列：violation_type, neighborhood, year_built, year_remodeled, property_type

## g1887（1 列）
- 見出し：violation_type
- 例1 値：Enforcement Violations | Housing Complaints | Enforcement Violations | Enforcement Violations | Enforcement Violations
  - 同じ表の列：date, neighborhood, year_built, year_remodeled, property_type

## g1888（1 列）
- 見出し：year_built
- 例1 値：1890 | 1900 | 1900 | 1899 | 1980
  - 同じ表の列：date, violation_type, neighborhood, year_remodeled, property_type

## g1889（1 列）
- 見出し：year_remodeled
- 例1 値：1980 | 1980 | 2004 | 2017 | 1997
  - 同じ表の列：date, violation_type, neighborhood, year_built, property_type

## g1890（1 列）
- 見出し：property_type
- 例1 値：Residential 3-family | Condominium Main* | Residential 2-family | Residential 4 or more family | Residential 1-family
  - 同じ表の列：date, violation_type, neighborhood, year_built, year_remodeled

## g1891（1 列）
- 見出し：score_calculated_ts
- 例1 値：2026-08-22T07:21:24 | 2026-05-16T07:20:17 | 2026-08-21T07:36:46 | 2026-07-22T14:57:58 | 2026-03-25T11:25:11
  - 同じ表の列：target, metric_logic, day_score, day_numerator, week_score, week_numerator, month_score, quarter_score

## g1892（1 列）
- 見出し：target
- 例1 値：0.8 | 0.8 | 0.8 | 0.8 | 0.8
  - 同じ表の列：score_calculated_ts, metric_logic, day_score, day_numerator, week_score, week_numerator, month_score, quarter_score

## g1893（1 列）
- 見出し：metric_logic
- 例1 値：sum(numerator_value)/sum(denominator_va… | sum(numerator_value)/sum(denominator_va… | current_average / historical_average | sum(numerator_value)/sum(denominator_va… | historical_average / current_average
  - 同じ表の列：score_calculated_ts, target, day_score, day_numerator, week_score, week_numerator, month_score, quarter_score

## g1894（1 列）
- 見出し：day_score
- 例1 値：0.729166666666667 | 0.913180386864597 | 1.25 | 0.75 | 1.25
  - 同じ表の列：score_calculated_ts, target, metric_logic, day_numerator, week_score, week_numerator, month_score, quarter_score

## g1895（1 列）
- 見出し：day_numerator
- 例1 値：6 | 91 | 978 | 18 | 4
  - 同じ表の列：score_calculated_ts, target, metric_logic, day_score, week_score, week_numerator, month_score, quarter_score

## g1896（1 列）
- 見出し：week_score
- 例1 値：0.65 | 1.16666666666667 | 0.914677635242738 | 0.878653942742341 | 0.626459143968872
  - 同じ表の列：score_calculated_ts, target, metric_logic, day_score, day_numerator, week_numerator, month_score, quarter_score

## g1897（1 列）
- 見出し：week_numerator
- 例1 値：7 | 161 | 1.53571428571429 | 5106 | 1510
  - 同じ表の列：score_calculated_ts, target, metric_logic, day_score, day_numerator, week_score, month_score, quarter_score

## g1898（1 列）
- 見出し：month_score
- 例1 値：0.892193308550186 | 1.87694370868493 | 0.793859649122807 | 1.19827586206897 | 0.941666666666667
  - 同じ表の列：score_calculated_ts, target, metric_logic, day_score, day_numerator, week_score, week_numerator, quarter_score

## g1899（1 列）
- 見出し：quarter_score
- 例1 値：0.894994075829384 | 0.645454545454546 | 1.20326086956522 | 0.824074074074074 | 1.21951219512195
  - 同じ表の列：score_calculated_ts, target, metric_logic, day_score, day_numerator, week_score, week_numerator, month_score

## g1900（1 列）
- 見出し：latest_score_flag
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：score_calculated_ts, target, metric_logic, day_score, day_numerator, week_score, week_numerator, month_score

## g1901（1 列）
- 見出し：city_council_district
- 例1 値：9 | 3 | 3 | 4 | 3
  - 同じ表の列：city_council_counci…, city_council_image, city_council_webpage, ons_liaison_ons, ons_liaison_neighbo…, ons_liaison_webpage, public_libraries_br…, public_libraries_di…

## g1902（1 列）
- 見出し：city_council_councilor
- 例1 値：Brian Worrell | Ed Flynn | John Fitzgerald | John Fitzgerald | John Fitzgerald
  - 同じ表の列：city_council_distri…, city_council_image, city_council_webpage, ons_liaison_ons, ons_liaison_neighbo…, ons_liaison_webpage, public_libraries_br…, public_libraries_di…

## g1903（1 列）
- 見出し：city_council_image
- 例1 値：https://boston.maps.arcgis.com/sharing/… | https://boston.maps.arcgis.com/sharing/… | https://boston.maps.arcgis.com/sharing/… | https://boston.maps.arcgis.com/sharing/… | https://boston.maps.arcgis.com/sharing/…
  - 同じ表の列：city_council_distri…, city_council_counci…, city_council_webpage, ons_liaison_ons, ons_liaison_neighbo…, ons_liaison_webpage, public_libraries_br…, public_libraries_di…

## g1904（1 列）
- 見出し：city_council_webpage
- 例1 値：https://bit.ly/3RPZZ1I | https://bit.ly/2Fszgn5 | https://bit.ly/3RPZZ1I | https://bit.ly/3RPZZ1I | https://bit.ly/3RPZZ1I
  - 同じ表の列：city_council_distri…, city_council_counci…, city_council_image, ons_liaison_ons, ons_liaison_neighbo…, ons_liaison_webpage, public_libraries_br…, public_libraries_di…

## g1905（1 列）
- 見出し：ons_liaison_ons
- 例1 値：7 | 7 | 13 | 14 | 7
  - 同じ表の列：city_council_distri…, city_council_counci…, city_council_image, city_council_webpage, ons_liaison_neighbo…, ons_liaison_webpage, public_libraries_br…, public_libraries_di…

## g1906（1 列）
- 見出し：ons_liaison_neighborhood
- 例1 値：Charlestown | Dorchester | Dorchester | Mid-Dorchester | Dorchester
  - 同じ表の列：city_council_distri…, city_council_counci…, city_council_image, city_council_webpage, ons_liaison_ons, ons_liaison_webpage, public_libraries_br…, public_libraries_di…

## g1907（1 列）
- 見出し：ons_liaison_webpage
- 例1 値：https://www.boston.gov/departments/neig… | https://www.boston.gov/departments/neig… | https://www.boston.gov/departments/neig… | https://www.boston.gov/departments/neig… | https://www.boston.gov/departments/neig…
  - 同じ表の列：city_council_distri…, city_council_counci…, city_council_image, city_council_webpage, ons_liaison_ons, ons_liaison_neighbo…, public_libraries_br…, public_libraries_di…

## g1908（1 列）
- 見出し：public_libraries_branch
- 例1 値：Parker Hill | Fields Corner | Charlestown | Honan-Allston | West Roxbury
  - 同じ表の列：city_council_distri…, city_council_counci…, city_council_image, city_council_webpage, ons_liaison_ons, ons_liaison_neighbo…, ons_liaison_webpage, public_libraries_di…

## g1909（1 列）
- 見出し：public_libraries_district
- 例1 値：JAMAICA PLAIN | DORCHESTER | MATTAPAN | HYDE PARK | ROXBURY
  - 同じ表の列：city_council_distri…, city_council_counci…, city_council_image, city_council_webpage, ons_liaison_ons, ons_liaison_neighbo…, ons_liaison_webpage, public_libraries_br…

## g1910（1 列）
- 見出し：public_libraries_zipcode
- 例1 値：02122 | 02122 | 02122 | 02120 | 02136
  - 同じ表の列：city_council_distri…, city_council_counci…, city_council_image, city_council_webpage, ons_liaison_ons, ons_liaison_neighbo…, ons_liaison_webpage, public_libraries_br…

## g1911（1 列）
- 見出し：usage_datetime_start_eastern_time
- 例1 値：2023-01-13 18:05:00 | 2023-01-14 06:50:00 | 2023-01-13 10:15:00 | 2023-01-15 18:00:00 | 2023-01-13 00:35:00
  - 同じ表の列：usage_datetime_end_…, usage_kw

## g1912（1 列）
- 見出し：usage_datetime_end_eastern_time
- 例1 値：2023-01-14 17:35:00 | 2023-01-14 22:00:00 | 2023-01-13 12:35:00 | 2023-01-16 10:30:00 | 2023-01-15 09:50:00
  - 同じ表の列：usage_datetime_star…, usage_kw

## g1913（1 列）
- 見出し：usage_kw
- 例1 値：1044 | 1087.2 | 1000.8 | 1000.8 | 1008
  - 同じ表の列：usage_datetime_star…, usage_datetime_end_…

## g1914（1 列）
- 見出し：InvoiceID
- 例1 値：9908319 | 17559642 | 13242629 | 6754508 | 6827960
  - 同じ表の列：AccountNumber, EnergyTypeName, InvoiceDate, FromDate, ToDate, UsagePeriodDays, DeliveryCost, SupplyCost

## g1915（1 列）
- 見出し：AccountNumber
- 例1 値：30765750010 | 102696000 | 1196041 | 26437911006 | 1118314
  - 同じ表の列：InvoiceID, EnergyTypeName, InvoiceDate, FromDate, ToDate, UsagePeriodDays, DeliveryCost, SupplyCost

## g1916（1 列）
- 見出し：EnergyTypeName
- 例1 値：Electric | Electric | Electric | Electric | Electric
  - 同じ表の列：InvoiceID, AccountNumber, InvoiceDate, FromDate, ToDate, UsagePeriodDays, DeliveryCost, SupplyCost

## g1917（1 列）
- 見出し：InvoiceDate
- 例1 値：2023-02-28 | 2023-11-15 | 2019-11-18 | 2019-02-22 | 2015-01-07
  - 同じ表の列：InvoiceID, AccountNumber, EnergyTypeName, FromDate, ToDate, UsagePeriodDays, DeliveryCost, SupplyCost

## g1918（1 列）
- 見出し：FromDate
- 例1 値：2015-01-07 | 2011-03-17 | 2019-04-11 | 2024-01-23 | 2016-05-09
  - 同じ表の列：InvoiceID, AccountNumber, EnergyTypeName, InvoiceDate, ToDate, UsagePeriodDays, DeliveryCost, SupplyCost

## g1919（1 列）
- 見出し：ToDate
- 例1 値：2018-02-12 | 2024-04-29 | 2017-07-12 | 2015-08-20 | 2017-02-08
  - 同じ表の列：InvoiceID, AccountNumber, EnergyTypeName, InvoiceDate, FromDate, UsagePeriodDays, DeliveryCost, SupplyCost

## g1920（1 列）
- 見出し：UsagePeriodDays
- 例1 値：29 | 30 | 30 | 32 | 33
  - 同じ表の列：InvoiceID, AccountNumber, EnergyTypeName, InvoiceDate, FromDate, ToDate, DeliveryCost, SupplyCost

## 答えの雛形

```
g1801	
g1802	
g1803	
g1804	
g1805	
g1806	
g1807	
g1808	
g1809	
g1810	
g1811	
g1812	
g1813	
g1814	
g1815	
g1816	
g1817	
g1818	
g1819	
g1820	
g1821	
g1822	
g1823	
g1824	
g1825	
g1826	
g1827	
g1828	
g1829	
g1830	
g1831	
g1832	
g1833	
g1834	
g1835	
g1836	
g1837	
g1838	
g1839	
g1840	
g1841	
g1842	
g1843	
g1844	
g1845	
g1846	
g1847	
g1848	
g1849	
g1850	
g1851	
g1852	
g1853	
g1854	
g1855	
g1856	
g1857	
g1858	
g1859	
g1860	
g1861	
g1862	
g1863	
g1864	
g1865	
g1866	
g1867	
g1868	
g1869	
g1870	
g1871	
g1872	
g1873	
g1874	
g1875	
g1876	
g1877	
g1878	
g1879	
g1880	
g1881	
g1882	
g1883	
g1884	
g1885	
g1886	
g1887	
g1888	
g1889	
g1890	
g1891	
g1892	
g1893	
g1894	
g1895	
g1896	
g1897	
g1898	
g1899	
g1900	
g1901	
g1902	
g1903	
g1904	
g1905	
g1906	
g1907	
g1908	
g1909	
g1910	
g1911	
g1912	
g1913	
g1914	
g1915	
g1916	
g1917	
g1918	
g1919	
g1920	
```
