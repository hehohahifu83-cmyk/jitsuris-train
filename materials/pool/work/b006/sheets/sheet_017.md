# ラベル用シート 017 / 018

- LABEL_GUIDE v1.8 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_017.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1921（1 列）
- 見出し：DeliveryCost
- 例1 値：155.29 | 57 | 38.57 | 86.47 | 12.73
  - 同じ表の列：InvoiceID, AccountNumber, EnergyTypeName, InvoiceDate, FromDate, ToDate, UsagePeriodDays, SupplyCost

## g1922（1 列）
- 見出し：SupplyCost
- 例1 値：0 | 49.75 | 0 | 0 | 35.93
  - 同じ表の列：InvoiceID, AccountNumber, EnergyTypeName, InvoiceDate, FromDate, ToDate, UsagePeriodDays, DeliveryCost

## g1923（1 列）
- 見出し：TotalCost
- 例1 値：420.53 | 79.43 | 367.64 | 8.68 | 52.24
  - 同じ表の列：InvoiceID, AccountNumber, EnergyTypeName, InvoiceDate, FromDate, ToDate, UsagePeriodDays, DeliveryCost

## g1924（1 列）
- 見出し：BERDO ID
- 例1 値：100686 | 100031 | 100028 | 100514 | 100471
  - 同じ表の列：Tax Parcel ID, Reported Gross Floo…, Reported Enclosed P…, Largest Property Ty…, All Property Types …, Site EUI (Energy Us…, Energy Star Score, Total Site Energy U…

## g1925（1 列）
- 見出し：Tax Parcel ID
- 例1 値：500820000 | 1800257000 | 1810142000 | 1800257000 | 700540280
  - 同じ表の列：BERDO ID, Reported Gross Floo…, Reported Enclosed P…, Largest Property Ty…, All Property Types …, Site EUI (Energy Us…, Energy Star Score, Total Site Energy U…

## g1926（1 列）
- 見出し：Reported Gross Floor Area (Sq Ft)
- 例1 値：110488 | 28356 | 2434 | 1932 | 43971
  - 同じ表の列：BERDO ID, Tax Parcel ID, Reported Enclosed P…, Largest Property Ty…, All Property Types …, Site EUI (Energy Us…, Energy Star Score, Total Site Energy U…

## g1927（1 列）
- 見出し：Reported Enclosed Parking Area (Sq Ft)
- 例1 値：0 | 5560 | 44530 | 14110 | 0
  - 同じ表の列：BERDO ID, Tax Parcel ID, Reported Gross Floo…, Largest Property Ty…, All Property Types …, Site EUI (Energy Us…, Energy Star Score, Total Site Energy U…

## g1928（1 列）
- 見出し：Largest Property Type
- 例1 値：Multifamily Housing | Office | Multifamily Housing | Multifamily Housing | Multifamily Housing
  - 同じ表の列：BERDO ID, Tax Parcel ID, Reported Gross Floo…, Reported Enclosed P…, All Property Types …, Site EUI (Energy Us…, Energy Star Score, Total Site Energy U…

## g1929（1 列）
- 見出し：All Property Types and GFAs
- 例1 値：K-12 School (28467.0) | Multifamily Housing (3600.0) | Residence Hall/Dormitory (203525.0) | Multifamily Housing (2064.0) | Multifamily Housing (3600.0)
  - 同じ表の列：BERDO ID, Tax Parcel ID, Reported Gross Floo…, Reported Enclosed P…, Largest Property Ty…, Site EUI (Energy Us…, Energy Star Score, Total Site Energy U…

## g1930（1 列）
- 見出し：Site EUI (Energy Use Intensity kBtu/ft2)
- 例1 値：71.6 | 57.1 | 81.1 | 46.9 | 45.1
  - 同じ表の列：BERDO ID, Tax Parcel ID, Reported Gross Floo…, Reported Enclosed P…, Largest Property Ty…, All Property Types …, Energy Star Score, Total Site Energy U…

## g1931（1 列）
- 見出し：Energy Star Score
- 例1 値：94 | 15 | 100 | 76 | 2
  - 同じ表の列：BERDO ID, Tax Parcel ID, Reported Gross Floo…, Reported Enclosed P…, Largest Property Ty…, All Property Types …, Site EUI (Energy Us…, Total Site Energy U…

## g1932（1 列）
- 見出し：Total Site Energy Usage (kBtu)
- 例1 値：8150639.2 | 1047153.4 | 1541785.8 | 1738018.2 | 2306407.2
  - 同じ表の列：BERDO ID, Tax Parcel ID, Reported Gross Floo…, Reported Enclosed P…, Largest Property Ty…, All Property Types …, Site EUI (Energy Us…, Energy Star Score

## g1933（1 列）
- 見出し：Natural Gas Usage (kBtu)
- 例1 値：4386824.6 | 198600 | 1799700.1 | 7414254.9 | 404100
  - 同じ表の列：BERDO ID, Tax Parcel ID, Reported Gross Floo…, Reported Enclosed P…, Largest Property Ty…, All Property Types …, Site EUI (Energy Us…, Energy Star Score

## g1934（1 列）
- 見出し：app_no
- 例1 値：ERT1710286 | ALT1832991 | ALT1611921 | SF1805770 | ALT1798187
  - 同じ表の列：start_datetime, stop_datetime, ward

## g1935（1 列）
- 見出し：start_datetime
- 例1 値：2026-09-12 07:00:00 | 2026-10-10 08:00:00 | 2026-08-29 08:00:00 | 2026-09-19 07:00:00 | 2026-08-22 07:00:00
  - 同じ表の列：app_no, stop_datetime, ward

## g1936（1 列）
- 見出し：stop_datetime
- 例1 値：2026-09-19 15:00:00 | 2026-09-26 18:00:00 | 2026-08-16 16:00:00 | 2026-08-22 18:00:00 | 2026-09-12 16:00:00
  - 同じ表の列：app_no, start_datetime, ward

## g1937（1 列）
- 見出し：status
- 例1 値：Appeal Closed | Appeal Closed | Appeal Closed | Community Process | Appeal Closed
  - 同じ表の列：parent_apno, boa_apno, appeal_type, submitted_date, received_date, hearing_date, ever_deferred, num_deferrals

## g1938（1 列）
- 見出し：parent_apno
- 例1 値：ALT1677661 | ERT1819961 | ALT1670923 | ALT1677932 | U491804852
  - 同じ表の列：status, boa_apno, appeal_type, submitted_date, received_date, hearing_date, ever_deferred, num_deferrals

## g1939（1 列）
- 見出し：boa_apno
- 例1 値：BOA1738631 | BOA1906128 | BOA1890414 | BOA1800743 | BOA1881928
  - 同じ表の列：status, parent_apno, appeal_type, submitted_date, received_date, hearing_date, ever_deferred, num_deferrals

## g1940（1 列）
- 見出し：appeal_type
- 例1 値：Zoning | Building | Zoning | Zoning | Zoning
  - 同じ表の列：status, parent_apno, boa_apno, submitted_date, received_date, hearing_date, ever_deferred, num_deferrals

## g1941（1 列）
- 見出し：submitted_date
- 例1 値：2026-06-04 | 2026-05-29 | 2026-07-06 | 2026-01-07 | 2026-07-09
  - 同じ表の列：status, parent_apno, boa_apno, appeal_type, received_date, hearing_date, ever_deferred, num_deferrals

## g1942（1 列）
- 見出し：received_date
- 例1 値：2026-09-01 | 2026-03-10 | 2025-10-03 | 2026-03-25 | 2025-09-24
  - 同じ表の列：status, parent_apno, boa_apno, appeal_type, submitted_date, hearing_date, ever_deferred, num_deferrals

## g1943（1 列）
- 見出し：hearing_date
- 例1 値：2026-01-22 | 2026-03-24 | 2026-04-07 | 2026-01-13 | 2026-03-10
  - 同じ表の列：status, parent_apno, boa_apno, appeal_type, submitted_date, received_date, ever_deferred, num_deferrals

## g1944（1 列）
- 見出し：ever_deferred
- 例1 値：N | N | N | N | N
  - 同じ表の列：status, parent_apno, boa_apno, appeal_type, submitted_date, received_date, hearing_date, num_deferrals

## g1945（1 列）
- 見出し：num_deferrals
- 例1 値：0 | 1 | 0 | 0 | 0
  - 同じ表の列：status, parent_apno, boa_apno, appeal_type, submitted_date, received_date, hearing_date, ever_deferred

## g1946（1 列）
- 見出し：final_decision_date
- 例1 値：2025-12-26 | 2026-09-18 | 2025-11-14 | 2025-01-24 | 2025-10-31
  - 同じ表の列：status, parent_apno, boa_apno, appeal_type, submitted_date, received_date, hearing_date, ever_deferred

## g1947（1 列）
- 見出し：metric
- 例1 値：count | count | count | count | count
  - 同じ表の列：zone_id, objClass, result, time

## g1948（1 列）
- 見出し：objClass
- 例1 値：pedestrian | pedestrian | pedestrian | pedestrian | pedestrian
  - 同じ表の列：zone_id, metric, result, time

## g1949（1 列）
- 見出し：result
- 例1 値：35.0 | 28.0 | 6.0 | 29.0 | 41.0
  - 同じ表の列：zone_id, metric, objClass, time

## g1950（1 列）
- 見出し：time
- 例1 値：2020-08-15T20:00:00-04:00 | 2020-07-16T21:00:00-04:00 | 2020-08-15T00:00:00-04:00 | 2020-08-21T17:00:00-04:00 | 2020-07-29T03:00:00-04:00
  - 同じ表の列：zone_id, metric, objClass, result

## g1951（1 列）
- 見出し：wkt_geom
- 例1 値：MultiPolygon (((-71.07844529019857305 4… | MultiPolygon (((-71.07902488955177489 4… | MultiPolygon (((-71.081599925484241 42.… | MultiPolygon (((-71.07973424995424239 4… | MultiPolygon (((-71.08038593877924427 4…
  - 同じ表の列：score, ns_spread, ew_spread, Area (sq ft), Volume (Cb ft), ndvi_avg, savi_avg, evi_avg

## g1952（1 列）
- 見出し：score
- 例1 値：0.909090909090909 | 0.8 | 0.666666666666667 | 0.666666666666667 | 0.818181818181818
  - 同じ表の列：wkt_geom, ns_spread, ew_spread, Area (sq ft), Volume (Cb ft), ndvi_avg, savi_avg, evi_avg

## g1953（1 列）
- 見出し：ns_spread
- 例1 値：22 | 16 | 29 | 25 | 24
  - 同じ表の列：wkt_geom, score, ew_spread, Area (sq ft), Volume (Cb ft), ndvi_avg, savi_avg, evi_avg

## g1954（1 列）
- 見出し：ew_spread
- 例1 値：21 | 17 | 21 | 21 | 21
  - 同じ表の列：wkt_geom, score, ns_spread, Area (sq ft), Volume (Cb ft), ndvi_avg, savi_avg, evi_avg

## g1955（1 列）
- 見出し：Area (sq ft)
- 例1 値：757 | 746 | 452 | 343 | 361
  - 同じ表の列：wkt_geom, score, ns_spread, ew_spread, Volume (Cb ft), ndvi_avg, savi_avg, evi_avg

## g1956（1 列）
- 見出し：Volume (Cb ft)
- 例1 値：13708.5 | 7611 | 3735.75 | 5689.125 | 10692
  - 同じ表の列：wkt_geom, score, ns_spread, ew_spread, Area (sq ft), ndvi_avg, savi_avg, evi_avg

## g1957（1 列）
- 見出し：ndvi_avg
- 例1 値：0.513869941234589 | 0.552127480506897 | 0.432188302278519 | 0.788993299007416 | 0.693820536136627
  - 同じ表の列：wkt_geom, score, ns_spread, ew_spread, Area (sq ft), Volume (Cb ft), savi_avg, evi_avg

## g1958（1 列）
- 見出し：savi_avg
- 例1 値：1.17530786991119 | 0.8116215467453 | 1.13449871540069 | 0.962033569812775 | 0.565967321395874
  - 同じ表の列：wkt_geom, score, ns_spread, ew_spread, Area (sq ft), Volume (Cb ft), ndvi_avg, evi_avg

## g1959（1 列）
- 見出し：evi_avg
- 例1 値：1.23531150817871 | 1.57553315162658 | 1.99011516571044 | 1.02915227413177 | 1.7090880870819
  - 同じ表の列：wkt_geom, score, ns_spread, ew_spread, Area (sq ft), Volume (Cb ft), ndvi_avg, savi_avg

## g1960（1 列）
- 見出し：tree health
- 例1 値：Good | Fair | Good | Good | Good
  - 同じ表の列：wkt_geom, score, ns_spread, ew_spread, Area (sq ft), Volume (Cb ft), ndvi_avg, savi_avg

## g1961（1 列）
- 見出し：GEOID
- 例1 値：250250711014 | 250250002023 | 250250916002 | 250251006012 | 250250605011
  - 同じ表の列：Census Tract, DRI_Category, DRI_Amenities Score

## g1962（1 列）
- 見出し：Census Tract
- 例1 値：912 | 1005 | 505 | 705.02 | 1201.05
  - 同じ表の列：GEOID, DRI_Category, DRI_Amenities Score

## g1963（1 列）
- 見出し：DRI_Category
- 例1 値：Moderately High | Low | Medium | Moderately Low | High
  - 同じ表の列：GEOID, Census Tract, DRI_Amenities Score

## g1964（1 列）
- 見出し：DRI_Amenities Score
- 例1 値：0.362717747699 | 0.176289083532 | 0.202796829452 | 0.391834877819 | 0.288362183188
  - 同じ表の列：GEOID, Census Tract, DRI_Category

## g1965（1 列）
- 見出し：TtlProjUnits
- 例1 値：25 | 69 | 16 | 2 | 3
  - 同じ表の列：Neighborhood, RentUnits, OwnUnits, TtlMarket, MarketRent, MarketOwn, Total Income-Restri…, Income-Restricted R…

## g1966（1 列）
- 見出し：RentUnits
- 例1 値：2 | 1 | 42 | 241 | 1
  - 同じ表の列：Neighborhood, TtlProjUnits, OwnUnits, TtlMarket, MarketRent, MarketOwn, Total Income-Restri…, Income-Restricted R…

## g1967（1 列）
- 見出し：OwnUnits
- 例1 値：0 | 1 | 108 | 54 | 12
  - 同じ表の列：Neighborhood, TtlProjUnits, RentUnits, TtlMarket, MarketRent, MarketOwn, Total Income-Restri…, Income-Restricted R…

## g1968（1 列）
- 見出し：TtlMarket
- 例1 値：0 | 14 | 122 | 0 | 0
  - 同じ表の列：Neighborhood, TtlProjUnits, RentUnits, OwnUnits, MarketRent, MarketOwn, Total Income-Restri…, Income-Restricted R…

## g1969（1 列）
- 見出し：MarketRent
- 例1 値：0 | 0 | 0 | 0 | 16
  - 同じ表の列：Neighborhood, TtlProjUnits, RentUnits, OwnUnits, TtlMarket, MarketOwn, Total Income-Restri…, Income-Restricted R…

## g1970（1 列）
- 見出し：MarketOwn
- 例1 値：0 | 0 | 0 | 38 | 0
  - 同じ表の列：Neighborhood, TtlProjUnits, RentUnits, OwnUnits, TtlMarket, MarketRent, Total Income-Restri…, Income-Restricted R…

## g1971（1 列）
- 見出し：Total Income-Restricted
- 例1 値：9 | 4 | 60 | 24 | 13
  - 同じ表の列：Neighborhood, TtlProjUnits, RentUnits, OwnUnits, TtlMarket, MarketRent, MarketOwn, Income-Restricted R…

## g1972（1 列）
- 見出し：Income-Restricted Rental
- 例1 値：2 | 26 | 2 | 24 | 1
  - 同じ表の列：Neighborhood, TtlProjUnits, RentUnits, OwnUnits, TtlMarket, MarketRent, MarketOwn, Total Income-Restri…

## g1973（1 列）
- 見出し：Income-Restricted Ownership
- 例1 値：0 | 0 | 3 | 2 | 0
  - 同じ表の列：Neighborhood, TtlProjUnits, RentUnits, OwnUnits, TtlMarket, MarketRent, MarketOwn, Total Income-Restri…

## g1974（1 列）
- 見出し：Revenue Category
- 例1 値：Departmental | State Aid | Licenses & Permits | Departmental | Penalties & Interest
  - 同じ表の列：Cabinet, Dept, FY24 Actual, FY25 Actual, FY26 Budget, FY27 Budget

## g1975（1 列）
- 見出し：Cabinet
- 例1 値：Finance | Public Safety | Finance | Public Safety | Finance
  - 同じ表の列：Revenue Category, Dept, FY24 Actual, FY25 Actual, FY26 Budget, FY27 Budget

## g1976（1 列）
- 見出し：Dept
- 例1 値：Boston Public Schools | Mayor's Office of Housing | Department of Innovation and Technology | Fair Housing & Equity | Property Management Department
  - 同じ表の列：Revenue Category, Cabinet, FY24 Actual, FY25 Actual, FY26 Budget, FY27 Budget

## g1977（1 列）
- 見出し：FY24 Actual
- 例1 値：2457 | 2957200804 | 8266 | 2080862 | 93687
  - 同じ表の列：Revenue Category, Cabinet, Dept, FY25 Actual, FY26 Budget, FY27 Budget

## g1978（1 列）
- 見出し：FY25 Actual
- 例1 値：10000 | 2511874 | 1610363 | 2787 | 8041595
  - 同じ表の列：Revenue Category, Cabinet, Dept, FY24 Actual, FY26 Budget, FY27 Budget

## g1979（1 列）
- 見出し：FY26 Budget
- 例1 値：1750000 | 150000 | 3500000 | 274415692 | 1500000
  - 同じ表の列：Revenue Category, Cabinet, Dept, FY24 Actual, FY25 Actual, FY27 Budget

## g1980（1 列）
- 見出し：FY27 Budget
- 例1 値：1500000 | 13400000 | 24000000 | 430000 | 5000000
  - 同じ表の列：Revenue Category, Cabinet, Dept, FY24 Actual, FY25 Actual, FY26 Budget

## g1981（1 列）
- 見出し：Cabinet
- 例1 値：Human Services Cabinet | Worker Empowerment Cabinet | Equity & Inclusion Cabinet | Public Safety Cabinet | People Operations Cabinet
  - 同じ表の列：Dept, Program, Expense Category, FY24 Actual Expense, FY25 Actual Expense, FY26 Appropriation, FY27 Budget

## g1982（1 列）
- 見出し：Dept
- 例1 値：Treasury Department | Police Department | Mayor's Office | Public Works Department | Planning Department
  - 同じ表の列：Cabinet, Program, Expense Category, FY24 Actual Expense, FY25 Actual Expense, FY26 Appropriation, FY27 Budget

## g1983（1 列）
- 見出し：Program
- 例1 値：Office of Finance | Core Infrastructure | BAT-Operations | Strategy | Election Administration
  - 同じ表の列：Cabinet, Dept, Expense Category, FY24 Actual Expense, FY25 Actual Expense, FY26 Appropriation, FY27 Budget

## g1984（1 列）
- 見出し：Expense Category
- 例1 値：Personnel Services | Personnel Services | Contractual Services | Supplies & Materials | Contractual Services
  - 同じ表の列：Cabinet, Dept, Program, FY24 Actual Expense, FY25 Actual Expense, FY26 Appropriation, FY27 Budget

## g1985（1 列）
- 見出し：FY24 Actual Expense
- 例1 値：6472560.75 | 1079199.02 | 1053610.06 | #Missing | 591542.79
  - 同じ表の列：Cabinet, Dept, Program, Expense Category, FY25 Actual Expense, FY26 Appropriation, FY27 Budget

## g1986（1 列）
- 見出し：FY25 Actual Expense
- 例1 値：31870.69 | 5375559.01 | 115997.33 | 5000 | 1517823.84
  - 同じ表の列：Cabinet, Dept, Program, Expense Category, FY24 Actual Expense, FY26 Appropriation, FY27 Budget

## g1987（1 列）
- 見出し：FY26 Appropriation
- 例1 値：26733.06 | 837765.43 | 250 | 94000 | 4589405.74
  - 同じ表の列：Cabinet, Dept, Program, Expense Category, FY24 Actual Expense, FY25 Actual Expense, FY27 Budget

## g1988（1 列）
- 見出し：FY27 Budget
- 例1 値：1271980.8 | 23302002 | 1400 | 80148 | #Missing
  - 同じ表の列：Cabinet, Dept, Program, Expense Category, FY24 Actual Expense, FY25 Actual Expense, FY26 Appropriation

## g1989（1 列）
- 見出し：Proj ID
- 例1 値：CPW25352 | CPR25170 | CAR25391 | CPR25335 | CND25105
  - 同じ表の列：Department, PM_Department, Project_Status, Neighborhood, Authorization_Exist…, Authorization_FY, Authorization_Future, OC_Existing

## g1990（1 列）
- 見出し：Department
- 例1 値：Fire Department | Boston Public Library | Boston Public Schools | Public Works Department | Public Works Department
  - 同じ表の列：Proj ID, PM_Department, Project_Status, Neighborhood, Authorization_Exist…, Authorization_FY, Authorization_Future, OC_Existing

## g1991（1 列）
- 見出し：PM_Department
- 例1 値：Parks and Recreation Department | Public Works Department | Department of Innovation and Technology | Boston Housing Authority | Public Works Department
  - 同じ表の列：Proj ID, Department, Project_Status, Neighborhood, Authorization_Exist…, Authorization_FY, Authorization_Future, OC_Existing

## g1992（1 列）
- 見出し：Project_Status
- 例1 値：In Construction | Annual Program | To Be Scheduled | In Design | In Construction
  - 同じ表の列：Proj ID, Department, PM_Department, Neighborhood, Authorization_Exist…, Authorization_FY, Authorization_Future, OC_Existing

## g1993（1 列）
- 見出し：Authorization_Existing
- 例1 値：750000 | 31510000 | 5000000 | 1892212 | 250000
  - 同じ表の列：Proj ID, Department, PM_Department, Project_Status, Neighborhood, Authorization_FY, Authorization_Future, OC_Existing

## g1994（1 列）
- 見出し：Authorization_FY
- 例1 値：0 | 105000 | 0 | 2000000 | 0
  - 同じ表の列：Proj ID, Department, PM_Department, Project_Status, Neighborhood, Authorization_Exist…, Authorization_Future, OC_Existing

## g1995（1 列）
- 見出し：Authorization_Future
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Proj ID, Department, PM_Department, Project_Status, Neighborhood, Authorization_Exist…, Authorization_FY, OC_Existing

## g1996（1 列）
- 見出し：OC_Existing
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Proj ID, Department, PM_Department, Project_Status, Neighborhood, Authorization_Exist…, Authorization_FY, Authorization_Future

## g1997（1 列）
- 見出し：OC_FY
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Proj ID, Department, PM_Department, Project_Status, Neighborhood, Authorization_Exist…, Authorization_FY, Authorization_Future

## g1998（1 列）
- 見出し：Business Type
- 例1 値：Retail | Creative Economy | Professional Services, software testing… | Retail | Salon
  - 同じ表の列：Business Zipcode, Other Information

## g1999（1 列）
- 見出し：Business Zipcode
- 例1 値：02135 | 02128 | 02101 | 02121 | 02126
  - 同じ表の列：Business Type, Other Information

## g2000（1 列）
- 見出し：Other Information
- 例1 値：Minority-owned | Minority-owned | Minority-owned, Immigrant-owned | Minority-owned | Minority-owned
  - 同じ表の列：Business Type, Business Zipcode

## g2001（1 列）
- 見出し：services_provided
- 例1 値：Middlesex General Contractor is a gener… | Marketing; Consulting; Branding; Social… | Full Service Food Truck, Catering, Priv… | Moving; Cleaning; Long haul freight; Re… | Leadership Coaching, Team Retreats, Lea…
  - 同じ表の列：mbe_wbe_cert, small_local_cert, veteran_cert, sdo_certified, city_registered, city, state, zipcode

## g2002（1 列）
- 見出し：mbe_wbe_cert
- 例1 値：WBE | WBE | MWBE | MWBE | WBE
  - 同じ表の列：services_provided, small_local_cert, veteran_cert, sdo_certified, city_registered, city, state, zipcode

## g2003（1 列）
- 見出し：small_local_cert
- 例1 値：SBE | SLBE | SBE | SLBE | SBE
  - 同じ表の列：services_provided, mbe_wbe_cert, veteran_cert, sdo_certified, city_registered, city, state, zipcode

## g2004（1 列）
- 見出し：veteran_cert
- 例1 値：SVOB | SVOB | SVOB, SDVOB | SVOB, SDVOB | SVOB, SDVOB
  - 同じ表の列：services_provided, mbe_wbe_cert, small_local_cert, sdo_certified, city_registered, city, state, zipcode

## g2005（1 列）
- 見出し：sdo_certified
- 例1 値：No | Yes | No | Yes | Yes
  - 同じ表の列：services_provided, mbe_wbe_cert, small_local_cert, veteran_cert, city_registered, city, state, zipcode

## g2006（1 列）
- 見出し：city_registered
- 例1 値：No | Yes | No | No | No
  - 同じ表の列：services_provided, mbe_wbe_cert, small_local_cert, veteran_cert, sdo_certified, city, state, zipcode

## g2007（1 列）
- 見出し：business_type
- 例1 値：Limited Liability Company (LLC) | Limited Liability Company (LLC) | Limited Liability Company (LLC) | Corporation | Sole Proprietorship
  - 同じ表の列：services_provided, mbe_wbe_cert, small_local_cert, veteran_cert, sdo_certified, city_registered, city, state

## g2008（1 列）
- 見出し：ID
- 例1 値：311-5qD | 416-NaW | 303-SMb | 331-Uks | 402-nqd
  - 同じ表の列：Department, Category, Solicitation Opens, Work Starts, Work Ends, Estimated Total Val…, Expected Procuremen…, UNSPSC

## g2009（1 列）
- 見出し：Department
- 例1 値：Inspectional Services Department | Transportation Department | Environment Department | Parks and Recreation | Department of Innovation and Technology
  - 同じ表の列：ID, Category, Solicitation Opens, Work Starts, Work Ends, Estimated Total Val…, Expected Procuremen…, UNSPSC

## g2010（1 列）
- 見出し：Category
- 例1 値：Services | Services | Goods & Supplies | Services | Services
  - 同じ表の列：ID, Department, Solicitation Opens, Work Starts, Work Ends, Estimated Total Val…, Expected Procuremen…, UNSPSC

## g2011（1 列）
- 見出し：Solicitation Opens
- 例1 値：Jan-27 | Apr-26 | Dec-26 | Procured Regularly, As Needed | Feb-27
  - 同じ表の列：ID, Department, Category, Work Starts, Work Ends, Estimated Total Val…, Expected Procuremen…, UNSPSC

## g2012（1 列）
- 見出し：Work Starts
- 例1 値：Jul-26 | Jul-26 | Jul-26 | Jul-26 | Jul-26
  - 同じ表の列：ID, Department, Category, Solicitation Opens, Work Ends, Estimated Total Val…, Expected Procuremen…, UNSPSC

## g2013（1 列）
- 見出し：Work Ends
- 例1 値：Jun-27 | Oct-27 | Jun-27 | Apr-30 | Jul-29
  - 同じ表の列：ID, Department, Category, Solicitation Opens, Work Starts, Estimated Total Val…, Expected Procuremen…, UNSPSC

## g2014（1 列）
- 見出し：Estimated Total Value (Range)
- 例1 値：$0-$10,000 | $10,001-$50,000 | $250,001-$500,000 | $250,001-$500,000 | $0-$10,000
  - 同じ表の列：ID, Department, Category, Solicitation Opens, Work Starts, Work Ends, Expected Procuremen…, UNSPSC

## g2015（1 列）
- 見出し：Expected Procurement Method
- 例1 値：Lowest Public Bid (IFB) | Solicit Written Quotes (WQC or IQC) | Statewide or General Services Administr… | Statewide or General Services Administr… | Lowest Public Bid (IFB)
  - 同じ表の列：ID, Department, Category, Solicitation Opens, Work Starts, Work Ends, Estimated Total Val…, UNSPSC

## g2016（1 列）
- 見出し：UNSPSC
- 例1 値：78131602 - File archive storage | 49100000 - Awards, Gifts, Collectable I… | 72101500 - Building Maintenance & Repai… | 72140000 - Heavy Construction Services | 44120000 - Office Supplies
  - 同じ表の列：ID, Department, Category, Solicitation Opens, Work Starts, Work Ends, Estimated Total Val…, Expected Procuremen…

## g2017（1 列）
- 見出し：Bonding & Prequalification Requirements
- 例1 値：DCAMM certification, 100% payment bond,… | 50% payment bonds required for ch. 30/3… | 50% payment bonds required for ch. 30/3… | 50% payment bonds required for ch. 30/3… | 50% payment bonds required for ch. 30/3…
  - 同じ表の列：ID, Department, Category, Solicitation Opens, Work Starts, Work Ends, Estimated Total Val…, Expected Procuremen…

## g2018（1 列）
- 見出し：Day Index
- 例1 値：07/13/2014 12:00:00 AM | 09/06/2014 12:00:00 AM | 10/11/2014 12:00:00 AM | 11/20/2014 12:00:00 AM | 12/16/2014 12:00:00 AM
  - 同じ表の列：Pageviews

## g2019（1 列）
- 見出し：year_of_death
- 例1 値：1878 | 1883 | 1898 | 1833 | 1831
  - 同じ表の列：month_of_year, day_of_month, location_number

## g2020（1 列）
- 見出し：month_of_year
- 例1 値：0 | 0 | NOVEMBER | 10 | MARCH
  - 同じ表の列：year_of_death, day_of_month, location_number

## g2021（1 列）
- 見出し：day_of_month
- 例1 値：2 | 3 | 18 | 25 | 0
  - 同じ表の列：year_of_death, month_of_year, location_number

## g2022（1 列）
- 見出し：location_number
- 例1 値：BS-C-35 | BS-D-93 | BS-D-14 | BS-D-59 | BS-D-33
  - 同じ表の列：year_of_death, month_of_year, day_of_month

## g2023（1 列）
- 見出し：voucher_voucher_id
- 例1 値：02649495 | 02679095 | 02649495 | 02668526 | 02648088
  - 同じ表の列：voucher_line_vouche…, distrib_line_distri…, fy_voucher_entered_…, fyq_voucher_entered…, distrib_line_deptid, dept_tbl_descr_3_di…, distrib_line_moneta…, city_or_state_mbe_w…

## g2024（1 列）
- 見出し：voucher_line_voucher_line_num
- 例1 値：4 | 1 | 1 | 1 | 6
  - 同じ表の列：voucher_voucher_id, distrib_line_distri…, fy_voucher_entered_…, fyq_voucher_entered…, distrib_line_deptid, dept_tbl_descr_3_di…, distrib_line_moneta…, city_or_state_mbe_w…

## g2025（1 列）
- 見出し：distrib_line_distrib_line_num
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：voucher_voucher_id, voucher_line_vouche…, fy_voucher_entered_…, fyq_voucher_entered…, distrib_line_deptid, dept_tbl_descr_3_di…, distrib_line_moneta…, city_or_state_mbe_w…

## g2026（1 列）
- 見出し：fy_voucher_entered_dt
- 例1 値：2019 | 2019 | 2019 | 2019 | 2019
  - 同じ表の列：voucher_voucher_id, voucher_line_vouche…, distrib_line_distri…, fyq_voucher_entered…, distrib_line_deptid, dept_tbl_descr_3_di…, distrib_line_moneta…, city_or_state_mbe_w…

## g2027（1 列）
- 見出し：fyq_voucher_entered_dt
- 例1 値：01 | 01 | 02 | 01 | 02
  - 同じ表の列：voucher_voucher_id, voucher_line_vouche…, distrib_line_distri…, fy_voucher_entered_…, distrib_line_deptid, dept_tbl_descr_3_di…, distrib_line_moneta…, city_or_state_mbe_w…

## g2028（1 列）
- 見出し：distrib_line_deptid
- 例1 値：211311 | 311000 | 101000 | 311801 | 211203
  - 同じ表の列：voucher_voucher_id, voucher_line_vouche…, distrib_line_distri…, fy_voucher_entered_…, fyq_voucher_entered…, dept_tbl_descr_3_di…, distrib_line_moneta…, city_or_state_mbe_w…

## g2029（1 列）
- 見出し：dept_tbl_descr_3_digit
- 例1 値：Police Department | Boston Public School Dept | Emergency Preparedness | Workers Compensation Fund | Boston Public School Dept
  - 同じ表の列：voucher_voucher_id, voucher_line_vouche…, distrib_line_distri…, fy_voucher_entered_…, fyq_voucher_entered…, distrib_line_deptid, distrib_line_moneta…, city_or_state_mbe_w…

## g2030（1 列）
- 見出し：distrib_line_monetary_amount
- 例1 値：16472.63 | 880 | 2560.8 | 1647.94 | 1065.36
  - 同じ表の列：voucher_voucher_id, voucher_line_vouche…, distrib_line_distri…, fy_voucher_entered_…, fyq_voucher_entered…, distrib_line_deptid, dept_tbl_descr_3_di…, city_or_state_mbe_w…

## g2031（1 列）
- 見出し：city_or_state_mbe_wbe_certified
- 例1 値：Not certified | MBE | Not certified | Not certified | Not certified
  - 同じ表の列：voucher_voucher_id, voucher_line_vouche…, distrib_line_distri…, fy_voucher_entered_…, fyq_voucher_entered…, distrib_line_deptid, dept_tbl_descr_3_di…, distrib_line_moneta…

## g2032（1 列）
- 見出し：city_slbe_sbe_certified
- 例1 値：Not certified | Not certified | Not certified | Not certified | Not certified
  - 同じ表の列：voucher_voucher_id, voucher_line_vouche…, distrib_line_distri…, fy_voucher_entered_…, fyq_voucher_entered…, distrib_line_deptid, dept_tbl_descr_3_di…, distrib_line_moneta…

## g2033（1 列）
- 見出し：main_id
- 例1 値：12 | 97 | 412 | 498 | 194
  - 同じ表の列：dist, start_time, end_time, side, from, to, miles, one_way

## g2034（1 列）
- 見出し：dist
- 例1 値：1S | 1B | 3 | 3 | 2
  - 同じ表の列：main_id, start_time, end_time, side, from, to, miles, one_way

## g2035（1 列）
- 見出し：start_time
- 例1 値：08:00 | 08:00 | 12:00 | 08:00 | 08:00
  - 同じ表の列：main_id, dist, end_time, side, from, to, miles, one_way

## g2036（1 列）
- 見出し：end_time
- 例1 値：13:00 | 12:00 | 12:00 | 16:00 | 12:00
  - 同じ表の列：main_id, dist, start_time, side, from, to, miles, one_way

## g2037（1 列）
- 見出し：side
- 例1 値：Even | Even | Even | Even | Odd
  - 同じ表の列：main_id, dist, start_time, end_time, from, to, miles, one_way

## g2038（1 列）
- 見出し：from
- 例1 値：Tibbetts Town Way | Washington St | Massachusetts Ave | C St | Warren St
  - 同じ表の列：main_id, dist, start_time, end_time, side, to, miles, one_way

## g2039（1 列）
- 見出し：to
- 例1 値：Laurel St | Dead End | Porter St | Kelton St | Massachusetts Ave
  - 同じ表の列：main_id, dist, start_time, end_time, side, from, miles, one_way

## g2040（1 列）
- 見出し：miles
- 例1 値：0.34905303 | 0.233143939393939 | 0.084469696969697 | 0.268560606060606 | 0.193371212121212
  - 同じ表の列：main_id, dist, start_time, end_time, side, from, to, one_way

## 答えの雛形

```
g1921	
g1922	
g1923	
g1924	
g1925	
g1926	
g1927	
g1928	
g1929	
g1930	
g1931	
g1932	
g1933	
g1934	
g1935	
g1936	
g1937	
g1938	
g1939	
g1940	
g1941	
g1942	
g1943	
g1944	
g1945	
g1946	
g1947	
g1948	
g1949	
g1950	
g1951	
g1952	
g1953	
g1954	
g1955	
g1956	
g1957	
g1958	
g1959	
g1960	
g1961	
g1962	
g1963	
g1964	
g1965	
g1966	
g1967	
g1968	
g1969	
g1970	
g1971	
g1972	
g1973	
g1974	
g1975	
g1976	
g1977	
g1978	
g1979	
g1980	
g1981	
g1982	
g1983	
g1984	
g1985	
g1986	
g1987	
g1988	
g1989	
g1990	
g1991	
g1992	
g1993	
g1994	
g1995	
g1996	
g1997	
g1998	
g1999	
g2000	
g2001	
g2002	
g2003	
g2004	
g2005	
g2006	
g2007	
g2008	
g2009	
g2010	
g2011	
g2012	
g2013	
g2014	
g2015	
g2016	
g2017	
g2018	
g2019	
g2020	
g2021	
g2022	
g2023	
g2024	
g2025	
g2026	
g2027	
g2028	
g2029	
g2030	
g2031	
g2032	
g2033	
g2034	
g2035	
g2036	
g2037	
g2038	
g2039	
g2040	
```
