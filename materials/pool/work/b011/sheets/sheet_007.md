# ラベル用シート 007 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_007.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0721（1 列）
- 見出し：Type
- 例1 値：EU1 - Residence Card | EU1 - Residence Card | EU1 - Residence Card | EU1 - Residence Card | EU2 - Permanent Residence Certificate
  - 同じ表の列：Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g0722（3 列）
- 見出し：Status
- 例1 値：Granted | Granted | Received | Received | Granted
  - 同じ表の列：Type, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022
- 例2 値：Closed | Closed | Closed | Closed | Closed
  - 同じ表の列：RFx No, Tender Type, Notice Type, Release Date, Closed Date/Time

## g0723（1 列）
- 見出し：Nationality
- 例1 値：Turkiye | Azerbaijan | Trinidad and Tobago | Solomon Islands | Comoros (the)
  - 同じ表の列：Type, Status, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g0724（1 列）
- 見出し：unsafe_2017
- 例1 値：0 | 38 | 0 | 0 | *
  - 同じ表の列：Type, Status, Nationality, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g0725（1 列）
- 見出し：unsafe_2018
- 例1 値：0 | 0 | 0 | * | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g0726（1 列）
- 見出し：unsafe_2019
- 例1 値：77 | 0 | 0 | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2020, unsafe_2021, unsafe_2022

## g0727（1 列）
- 見出し：unsafe_2020
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2021, unsafe_2022

## g0728（1 列）
- 見出し：unsafe_2021
- 例1 値：0 | 0 | 0 | 0 | 18
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2022

## g0729（1 列）
- 見出し：unsafe_2022
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g0730（1 列）
- 見出し：unsafe_2023
- 例1 値：0 | 0 | * | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g0731（1 列）
- 見出し：Statistic
- 例1 値：Expenditure on education, health and so… | Expenditure on education, health and so… | Expenditure on education, health and so… | Expenditure on education, health and so… | Expenditure on education, health and so…
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02196V02652, State, UNIT, VALUE

## g0732（1 列）
- 見出し：C02196V02652
- 例1 値：- | - | - | - | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, State, UNIT, VALUE

## g0733（1 列）
- 見出し：UNIT
- 例1 値：Euro | Euro | % | % | Euro
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, State, VALUE

## g0734（2 列）
- 見出し：period
- 例1 値：2015Q1 | 2015Q3 | 2017Q2 | 2017Q4 | 2016Q2
  - 同じ表の列：programme, scheme, basis, sex_code, sex, recipients
- 例2 値：2014Q2 | 2014Q1 | 2014Q1 | 2014Q1 | 2014Q2
  - 同じ表の列：programme, scheme, basis, county, county_code, recipients

## g0735（1 列）
- 見出し：programme
- 例1 値：Illness,Disability and Caring | Children | Working Age Income Supports | Children | Children
  - 同じ表の列：period, scheme, basis, sex_code, sex, recipients

## g0736（1 列）
- 見出し：scheme
- 例1 値：HHB1 | BTWF | SPNC | OFP | CARB
  - 同じ表の列：period, programme, basis, sex_code, sex, recipients

## g0737（2 列）
- 見出し：basis
- 例1 値：Social Assistance | Social Insurance | Social Assistance | Social Assistance | Social Assistance
  - 同じ表の列：period, programme, scheme, sex_code, sex, recipients
- 例2 値：Social Insurance | Social Assistance | Social Insurance | Social Assistance | Social Insurance
  - 同じ表の列：period, programme, scheme, county, county_code, recipients

## g0738（1 列）
- 見出し：sex_code
- 例1 値：2 | 2 | 1 | 1 | 1
  - 同じ表の列：period, programme, scheme, basis, sex, recipients

## g0739（2 列）
- 見出し：recipients
- 例1 値：11027.0 | 246522.0 | 187973.0 | 1433.0 | 49369.0
  - 同じ表の列：period, programme, scheme, basis, sex_code, sex
- 例2 値：9151.0 | 7791.0 | 12591.0 | 949.0 | 9863.0
  - 同じ表の列：period, programme, scheme, basis, county, county_code

## g0740（1 列）
- 見出し：Time
- 例1 値：2026-02-10T11:00:00 | 2026-01-22T12:00:00 | 2026-01-02T01:00:00 | 2026-01-15T02:00:00 | 2026-01-28T08:00:00
  - 同じ表の列：aston_quay_fitzgera…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…

## g0741（1 列）
- 見出し：aston_quay_fitzgeralds
- 例1 値：13 | 43 | 54 | 25 | 14
  - 同じ表の列：Time, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…

## g0742（1 列）
- 見出し：aston_quay_fitzgeralds_in
- 例1 値：23 | 2 | 1 | 20 | 1
  - 同じ表の列：Time, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…

## g0743（1 列）
- 見出し：aston_quay_fitzgeralds_out
- 例1 値：16 | 8 | 13 | 6 | 8
  - 同じ表の列：Time, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…

## g0744（3 列）
- 見出し：bachelors_walk_bachelors_way__counter_nonrepsonsive___remove
- 例1 値：2 | 2 | 6 | 11 | 2
  - 同じ表の列：Time, aston_quay_fitzgera…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…
- 例2 値：1 | 4 | 2 | 1 | 5
  - 同じ表の列：Time, aston_quay_fitzgera…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…

## g0745（1 列）
- 見出し：baggot_st_upper_mespil_rd_bank
- 例1 値：8514 | 5908 | 7047 | 13803 | 3536
  - 同じ表の列：Time, aston_quay_fitzgera…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…

## g0746（1 列）
- 見出し：baggot_st_upper_mespil_rd_bank_pedestrians_in
- 例1 値：1264 | 3457 | 3896 | 2953 | 6672
  - 同じ表の列：Time, aston_quay_fitzgera…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…

## g0747（1 列）
- 見出し：baggot_st_upper_mespil_rd_bank_pedestrians_out
- 例1 値：948 | 1381 | 3237 | 38 | 515
  - 同じ表の列：Time, aston_quay_fitzgera…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…

## g0748（1 列）
- 見出し：Time
- 例1 値：Jan 9, 2022 5:00 AM | Jan 16, 2022 8:00 AM | Jan 28, 2022 12:00 PM | Feb 11, 2022 3:00 PM | Jan 25, 2022 8:00 PM
  - 同じ表の列：Clonskeagh Totem, Clonskeagh Totem IN, Clonskeagh Totem OUT, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…

## g0749（1 列）
- 見出し：Clonskeagh Totem
- 例1 値：75 | 42 | 23 | 187 | 54
  - 同じ表の列：Time, Clonskeagh Totem IN, Clonskeagh Totem OUT, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…

## g0750（1 列）
- 見出し：Clonskeagh Totem IN
- 例1 値：28 | 147 | 36 | 22 | 8
  - 同じ表の列：Time, Clonskeagh Totem, Clonskeagh Totem OUT, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…

## g0751（1 列）
- 見出し：Clonskeagh Totem OUT
- 例1 値：15 | 10 | 1 | 1 | 18
  - 同じ表の列：Time, Clonskeagh Totem, Clonskeagh Totem IN, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…

## g0752（1 列）
- 見出し：Dun Laoghaire @ Peoples Park Cyclist
- 例1 値：15 | 176 | 8 | 47 | 80
  - 同じ表の列：Time, Clonskeagh Totem, Clonskeagh Totem IN, Clonskeagh Totem OUT, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…

## g0753（1 列）
- 見出し：Dun Laoghaire @ Peoples Park Cyclists IN
- 例1 値：19 | 37 | 1 | 1 | 1
  - 同じ表の列：Time, Clonskeagh Totem, Clonskeagh Totem IN, Clonskeagh Totem OUT, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…

## g0754（1 列）
- 見出し：Dun Laoghaire @ Peoples Park Cyclists OUT
- 例1 値：37 | 14 | 28 | 33 | 17
  - 同じ表の列：Time, Clonskeagh Totem, Clonskeagh Totem IN, Clonskeagh Totem OUT, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…

## g0755（1 列）
- 見出し：Dun Laoghaire @ Seapoint Beach Cyclist
- 例1 値：1 | 61 | 82 | 21 | 37
  - 同じ表の列：Time, Clonskeagh Totem, Clonskeagh Totem IN, Clonskeagh Totem OUT, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…

## g0756（1 列）
- 見出し：Dun Laoghaire @ Seapoint Beach Cyclists IN
- 例1 値：6 | 11 | 47 | 30 | 45
  - 同じ表の列：Time, Clonskeagh Totem, Clonskeagh Totem IN, Clonskeagh Totem OUT, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…

## g0757（1 列）
- 見出し：Dun Laoghaire @ Seapoint Beach Cyclists OUT
- 例1 値：24 | 19 | 37 | 44 | 28
  - 同じ表の列：Time, Clonskeagh Totem, Clonskeagh Totem IN, Clonskeagh Totem OUT, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…

## g0758（2 列）
- 見出し：Statistic
- 例1 値：Container Traffic (Lift On/Lift Off) | Container Traffic (Lift On/Lift Off) | Container Traffic (Lift On/Lift Off) | Container Traffic (Lift On/Lift Off) | Container Traffic (Lift On/Lift Off)
  - 同じ表の列：STATISTIC, TLIST(Q1), Quarter, C02637V03195, Country, C02638V03194, Type of Traffic, UNIT
- 例2 値：Passenger Traffic (Roll On/Roll Off) | Passenger Traffic (Roll On/Roll Off) | Passenger Traffic (Roll On/Roll Off) | Passenger Traffic (Roll On/Roll Off) | Passenger Traffic (Roll On/Roll Off)
  - 同じ表の列：STATISTIC, TLIST(Q1), Quarter, C02635V03192, Shipping Corridor, C02638V03194, Type of Traffic, UNIT

## g0759（1 列）
- 見出し：C02637V03195
- 例1 値：IE1 | - | - | XI1 | IE1
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, Country, C02638V03194, Type of Traffic, UNIT

## g0760（1 列）
- 見出し：Country
- 例1 値：Ireland | Northern Ireland | Northern Ireland | Ireland | Ireland
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02637V03195, C02638V03194, Type of Traffic, UNIT

## g0761（2 列）
- 見出し：C02638V03194
- 例1 値：1 | 3 | 2 | 1 | 1
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02637V03195, Country, Type of Traffic, UNIT
- 例2 値：8 | 9 | 9 | 9 | 9
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02635V03192, Shipping Corridor, Type of Traffic, UNIT

## g0762（1 列）
- 見出し：Type of Traffic
- 例1 値：Laden traffic | Unladen traffic | Laden traffic | All container traffic | Laden traffic
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02637V03195, Country, C02638V03194, UNIT

## g0763（1 列）
- 見出し：UNIT
- 例1 値：TEU Twenty-foot Equivalent | TEU Twenty-foot Equivalent | TEU Twenty-foot Equivalent | TEU Twenty-foot Equivalent | TEU Twenty-foot Equivalent
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02637V03195, Country, C02638V03194, Type of Traffic

## g0764（1 列）
- 見出し：Neighbourhoods
- 例1 値：Local Studies & Archives | Kilcullen | Kilcock | Celbridge | Rathanagan
  - 同じ表の列：CultureDescription, OrganizationType, Eircode, PublicCategory, WebsiteUrl, ElectoralDivision

## g0765（1 列）
- 見出し：CultureDescription
- 例1 値：Books, movies and more, learning and st… | Books, movies and more, learning and st… | Books, movies and more, learning and st… | Books, movies and more, learning and st… | Books, movies and more, learning and st…
  - 同じ表の列：Neighbourhoods, OrganizationType, Eircode, PublicCategory, WebsiteUrl, ElectoralDivision

## g0766（1 列）
- 見出し：OrganizationType
- 例1 値：facility or amenity | facility or amenity | facility or amenity | facility or amenity | facility or amenity
  - 同じ表の列：Neighbourhoods, CultureDescription, Eircode, PublicCategory, WebsiteUrl, ElectoralDivision

## g0767（1 列）
- 見出し：Eircode
- 例1 値：W12 W86 | R14 HX97 | R51 YX65 | W23 VA47 | R56 Y438
  - 同じ表の列：Neighbourhoods, CultureDescription, OrganizationType, PublicCategory, WebsiteUrl, ElectoralDivision

## g0768（1 列）
- 見出し：PublicCategory
- 例1 値：Libraries | Libraries | Libraries | Libraries | Libraries
  - 同じ表の列：Neighbourhoods, CultureDescription, OrganizationType, Eircode, WebsiteUrl, ElectoralDivision

## g0769（1 列）
- 見出し：WebsiteUrl
- 例1 値：https://kildarecoco.ie/library/index.ht… | https://kildarecoco.ie/library/index.ht… | https://kildarecoco.ie/library/index.ht… | https://kildarecoco.ie/library/index.ht… | https://kildarecoco.ie/library/index.ht…
  - 同じ表の列：Neighbourhoods, CultureDescription, OrganizationType, Eircode, PublicCategory, ElectoralDivision

## g0770（1 列）
- 見出し：ElectoralDivision
- 例1 値：Athy | Clane/Maynooth | Kildare/Newbridge | Celbridge/Leixlip | Kildare/Newbridge
  - 同じ表の列：Neighbourhoods, CultureDescription, OrganizationType, Eircode, PublicCategory, WebsiteUrl

## g0771（1 列）
- 見出し：unsafe_
- 例1 値：2021-02-17T00:00:00 | 2021-05-19T00:00:00 | 2021-03-16T00:00:00 | 2021-10-27T00:00:00 | 2021-07-12T00:00:00
  - 同じ表の列：unsafe__2, unprotect cafo, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__8, Munster

## g0772（1 列）
- 見出し：unsafe__2
- 例1 値：Wind | Wind | Wind | Snow/Ice | Thunderstorm
  - 同じ表の列：unsafe_, unprotect cafo, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__8, Munster

## g0773（1 列）
- 見出し：unprotect cafo
- 例1 値：For Donegal | Valid from 05:00 Sun, 14-Feb-2021 | Expires: Monday 9/8/2021 00:00 | Meath, Cavan, Monaghan and Waterford | Daytime maximum temperatures generally …
  - 同じ表の列：unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__8, Munster

## g0774（1 列）
- 見出し：unsafe__3
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：unsafe_, unsafe__2, unprotect cafo, unsafe__4, unsafe__5, unsafe__6, unsafe__8, Munster

## g0775（1 列）
- 見出し：unsafe__4
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：unsafe_, unsafe__2, unprotect cafo, unsafe__3, unsafe__5, unsafe__6, unsafe__8, Munster

## g0776（1 列）
- 見出し：unsafe__5
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：unsafe_, unsafe__2, unprotect cafo, unsafe__3, unsafe__4, unsafe__6, unsafe__8, Munster

## g0777（1 列）
- 見出し：unsafe__6
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：unsafe_, unsafe__2, unprotect cafo, unsafe__3, unsafe__4, unsafe__5, unsafe__8, Munster

## g0778（1 列）
- 見出し：Munster
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：unsafe_, unsafe__2, unprotect cafo, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__8

## g0779（1 列）
- 見出し：unsafe__10
- 例1 値：0 | 0 | 0 | 1 | 0
  - 同じ表の列：unsafe_, unsafe__2, unprotect cafo, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__8

## g0780（1 列）
- 見出し：Route_No
- 例1 値：54-9 | 33-4 | 21-12 | 54-2 | 61-1
  - 同じ表の列：Comments_1, cdo, twoway, sruface_ch, bollardpro, temporary, mandatory, width

## g0781（1 列）
- 見出し：Comments_1
- 例1 値：Bus lane on opposite side of road | Bus lane on opposite side of road
  - 同じ表の列：Route_No, cdo, twoway, sruface_ch, bollardpro, temporary, mandatory, width

## g0782（2 列）
- 見出し：cdo
- 例1 値：SegregatedCycleLane | SegregatedCycleLane | CycleLane | CycleLane | SegregatedCycleLane
  - 同じ表の列：Route_No, Comments_1, twoway, sruface_ch, bollardpro, temporary, mandatory, width
- 例2 値：TrafficFree | SegregatedCycleLane | TrafficFree | SurfaceChange | TrafficFree
  - 同じ表の列：OID_, twoway, bollardpro

## g0783（2 列）
- 見出し：twoway
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Route_No, Comments_1, cdo, sruface_ch, bollardpro, temporary, mandatory, width
- 例2 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：OID_, cdo, bollardpro

## g0784（1 列）
- 見出し：sruface_ch
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Route_No, Comments_1, cdo, twoway, bollardpro, temporary, mandatory, width

## g0785（2 列）
- 見出し：bollardpro
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Route_No, Comments_1, cdo, twoway, sruface_ch, temporary, mandatory, width
- 例2 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：OID_, cdo, twoway

## g0786（1 列）
- 見出し：temporary
- 例1 値：1
  - 同じ表の列：Route_No, Comments_1, cdo, twoway, sruface_ch, bollardpro, mandatory, width

## g0787（1 列）
- 見出し：mandatory
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Route_No, Comments_1, cdo, twoway, sruface_ch, bollardpro, temporary, width

## g0788（1 列）
- 見出し：width
- 例1 値：1.5 | 1.2 | 2.0 | 1.4 | 1.7
  - 同じ表の列：Route_No, Comments_1, cdo, twoway, sruface_ch, bollardpro, temporary, mandatory

## g0789（1 列）
- 見出し：surface_ch
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Route_No, Comments_1, cdo, twoway, sruface_ch, bollardpro, temporary, mandatory

## g0790（1 列）
- 見出し：Region
- 例1 値：North West | South West | South East | North West | South West
  - 同じ表の列：Sub-Region, Point, Easting, Northing, unsafe_50__present, unsafe_20__present, unsafe_10__present, unsafe_5__present

## g0791（1 列）
- 見出し：Sub-Region
- 例1 値：South West | Shannon | North West | South | Shannon
  - 同じ表の列：Region, Point, Easting, Northing, unsafe_50__present, unsafe_20__present, unsafe_10__present, unsafe_5__present

## g0792（1 列）
- 見出し：Point
- 例1 値：NE20 | NW13 | NW41 | SW29 | W68
  - 同じ表の列：Region, Sub-Region, Easting, Northing, unsafe_50__present, unsafe_20__present, unsafe_10__present, unsafe_5__present

## g0793（1 列）
- 見出し：Easting
- 例1 値：462223.61 | 594649.82 | 466920.46 | 492318.87 | 577948.77
  - 同じ表の列：Region, Sub-Region, Point, Northing, unsafe_50__present, unsafe_20__present, unsafe_10__present, unsafe_5__present

## g0794（1 列）
- 見出し：Northing
- 例1 値：687677.17 | 613493.62 | 874130.98 | 703290.99 | 564225.52
  - 同じ表の列：Region, Sub-Region, Point, Easting, unsafe_50__present, unsafe_20__present, unsafe_10__present, unsafe_5__present

## g0795（1 列）
- 見出し：unsafe_50__present
- 例1 値：2.34 | 2.24 | 2.17 | 2.89 | 1.98
  - 同じ表の列：Region, Sub-Region, Point, Easting, Northing, unsafe_20__present, unsafe_10__present, unsafe_5__present

## g0796（1 列）
- 見出し：unsafe_20__present
- 例1 値：2.36 | 2.31 | 2.27 | 2.93 | 3.37
  - 同じ表の列：Region, Sub-Region, Point, Easting, Northing, unsafe_50__present, unsafe_10__present, unsafe_5__present

## g0797（1 列）
- 見出し：unsafe_10__present
- 例1 値：2.89 | 2.2 | 2.25 | 3.4 | 1.51
  - 同じ表の列：Region, Sub-Region, Point, Easting, Northing, unsafe_50__present, unsafe_20__present, unsafe_5__present

## g0798（1 列）
- 見出し：unsafe_5__present
- 例1 値：3.17 | 3.18 | 2.53 | 2.96 | 3.54
  - 同じ表の列：Region, Sub-Region, Point, Easting, Northing, unsafe_50__present, unsafe_20__present, unsafe_10__present

## g0799（1 列）
- 見出し：unsafe_2__present
- 例1 値：3.26 | 3.18 | 2.84 | 2.37 | 2.45
  - 同じ表の列：Region, Sub-Region, Point, Easting, Northing, unsafe_50__present, unsafe_20__present, unsafe_10__present

## g0800（1 列）
- 見出し：year_liability
- 例1 値：2025 | 2019 | 2020 | 2024 | 2023
  - 同じ表の列：period_start_date, period_end_date, number_of_supplier, total_units_supplie…, units_supplied_chp_…, units_supplied_elec…, units_supplied_hous…, units_supplied_hous…

## g0801（1 列）
- 見出し：period_start_date
- 例1 値：2020-01-01T00:00:00 | 2025-01-01T00:00:00 | 2023-01-01T00:00:00 | 2018-01-01T00:00:00 | 2021-01-01T00:00:00
  - 同じ表の列：year_liability, period_end_date, number_of_supplier, total_units_supplie…, units_supplied_chp_…, units_supplied_elec…, units_supplied_hous…, units_supplied_hous…

## g0802（1 列）
- 見出し：period_end_date
- 例1 値：2020-12-31T00:00:00 | 2018-12-31T00:00:00 | 2024-12-31T00:00:00 | 2016-12-31T00:00:00 | 2017-12-31T00:00:00
  - 同じ表の列：year_liability, period_start_date, number_of_supplier, total_units_supplie…, units_supplied_chp_…, units_supplied_elec…, units_supplied_hous…, units_supplied_hous…

## g0803（1 列）
- 見出し：number_of_supplier
- 例1 値：20 | 19 | 20 | 20 | 19
  - 同じ表の列：year_liability, period_start_date, period_end_date, total_units_supplie…, units_supplied_chp_…, units_supplied_elec…, units_supplied_hous…, units_supplied_hous…

## g0804（1 列）
- 見出し：total_units_supplied_MWh
- 例1 値：25034927 | 26178504 | 28691093 | 25188253 | 26497925
  - 同じ表の列：year_liability, period_start_date, period_end_date, number_of_supplier, units_supplied_chp_…, units_supplied_elec…, units_supplied_hous…, units_supplied_hous…

## g0805（1 列）
- 見出し：units_supplied_chp_generation_MWh
- 例1 値：10 | 13 | 5610 | 30 | 1411
  - 同じ表の列：year_liability, period_start_date, period_end_date, number_of_supplier, total_units_supplie…, units_supplied_elec…, units_supplied_hous…, units_supplied_hous…

## g0806（1 列）
- 見出し：units_supplied_electricity_generation_MWh
- 例1 値：17585 | 10687 | 54270 | 17379 | 16944
  - 同じ表の列：year_liability, period_start_date, period_end_date, number_of_supplier, total_units_supplie…, units_supplied_chp_…, units_supplied_hous…, units_supplied_hous…

## g0807（1 列）
- 見出し：units_supplied_household_use_MWh
- 例1 値：8486021 | 7614819 | 8243102 | 7659659 | 8605484
  - 同じ表の列：year_liability, period_start_date, period_end_date, number_of_supplier, total_units_supplie…, units_supplied_chp_…, units_supplied_elec…, units_supplied_hous…

## g0808（1 列）
- 見出し：units_supplied_household_use_renewable_sources_MWh
- 例1 値：5293214.36 | 5214627.006 | 3563262.558 | 5369666.957 | 5803059.537
  - 同じ表の列：year_liability, period_start_date, period_end_date, number_of_supplier, total_units_supplie…, units_supplied_chp_…, units_supplied_elec…, units_supplied_hous…

## g0809（1 列）
- 見出し：units_supplied_household_exemption_MWh
- 例1 値：4051556.442 | 3526537.182 | 4311253.371 | 3271393.994 | 2949887.64
  - 同じ表の列：year_liability, period_start_date, period_end_date, number_of_supplier, total_units_supplie…, units_supplied_chp_…, units_supplied_elec…, units_supplied_hous…

## g0810（2 列）
- 見出し：Doc
- 例1 値：TableF | TableF | TableF | TableF | TableF
  - 同じ表の列：Heading, Ref, Ref_desc, Ref1, Ref1_desc, Ref2, Ref2_desc, Adop
- 例2 値：TableE | TableE | TableE | TableE | TableE
  - 同じ表の列：Heading, Ref, desc, Inc, PY, OBJECTID

## g0811（2 列）
- 見出し：Heading
- 例1 値：2 | 1 | 1 | 1 | 2
  - 同じ表の列：Doc, Ref, Ref_desc, Ref1, Ref1_desc, Ref2, Ref2_desc, Adop
- 例2 値：2 | 2 | 1 | 2 | 2
  - 同じ表の列：Doc, Ref, desc, Inc, PY, OBJECTID

## g0812（1 列）
- 見出し：Ref
- 例1 値：D | H | H | D | B
  - 同じ表の列：Doc, Heading, Ref_desc, Ref1, Ref1_desc, Ref2, Ref2_desc, Adop

## g0813（1 列）
- 見出し：Ref_desc
- 例1 値：Housing and Building | Environmental Services | Road Transport & Safety | Agriculture, Education, Health & Welfare | Environmental Services
  - 同じ表の列：Doc, Heading, Ref, Ref1, Ref1_desc, Ref2, Ref2_desc, Adop

## g0814（1 列）
- 見出し：Ref1
- 例1 値：H09 | D05 | F04 | GOODS | E08
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1_desc, Ref2, Ref2_desc, Adop

## g0815（1 列）
- 見出し：Ref1_desc
- 例1 値：Fire Prevention | Operation of Arts Programme | Support to Roads Capital Prog | Veterinary Service | Goods & Services
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1, Ref2, Ref2_desc, Adop

## g0816（1 列）
- 見出し：Ref2
- 例1 値：G57800 | H1099 | A0399 | D1099 | D0902
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1, Ref1_desc, Ref2_desc, Adop

## g0817（1 列）
- 見出し：Ref2_desc
- 例1 値：Other Grants & Subsidies | Commercial Refuse Charges | Landfill Charges | Environment, Planning & Local Government | Other Grants & Subsidies
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1, Ref1_desc, Ref2, Adop

## g0818（1 列）
- 見出し：Adop
- 例1 値：-720000 | 97100 | -8400 | 10000 | 631300
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1, Ref1_desc, Ref2, Ref2_desc

## g0819（1 列）
- 見出し：Estmgr
- 例1 値：745000 | 427000 | 3500 | 10000 | 60000
  - 同じ表の列：Doc, Heading, Ref, Ref_desc, Ref1, Ref1_desc, Ref2, Ref2_desc

## g0820（1 列）
- 見出し：Award Status
- 例1 値：Declined | Declined | Declined | Declined | Awarded
  - 同じ表の列：Year, Amount Requested, Amount funded

## g0821（1 列）
- 見出し：Amount Requested
- 例1 値：20000 | 80000 | 470000 | 120000 | 830000
  - 同じ表の列：Year, Award Status, Amount funded

## g0822（1 列）
- 見出し：Amount funded
- 例1 値：50000 | 480000 | 790000 | 930000 | 90000
  - 同じ表の列：Year, Award Status, Amount Requested

## g0823（2 列）
- 見出し：SensorTimestamp
- 例1 値：2014-09-29T01:05:11 | 2014-09-29T01:00:09 | 2014-09-29T01:04:59 | 2014-09-29T01:04:10 | 2014-09-29T01:04:50
  - 同じ表の列：SensorValue, SequenceNo, SensorUnit
- 例2 値：2015-08-16T20:22:29 | 2015-08-16T22:32:45 | 2015-08-15T01:41:23 | 2015-08-16T21:27:32 | 2015-08-14T10:37:58
  - 同じ表の列：air_temperature__de…, barometric_pressure…, wind_direction__deg…, wind_direction__deg…, wind_speed__knot_, wind_speed__meters_…, barometric_pressure…

## g0824（1 列）
- 見出し：SensorValue
- 例1 値：1.4665 | 1.4665 | 1.5504 | 1.5224 | 1.4665
  - 同じ表の列：SensorTimestamp, SequenceNo, SensorUnit

## g0825（1 列）
- 見出し：SequenceNo
- 例1 値：849 | 705 | 592 | 54 | 30
  - 同じ表の列：SensorTimestamp, SensorValue, SensorUnit

## g0826（1 列）
- 見出し：SensorUnit
- 例1 値：kN | kN | kN | kN | kN
  - 同じ表の列：SensorTimestamp, SensorValue, SequenceNo

## g0827（2 列）
- 見出し：RegionID
- 例1 値：19 | 20 | 18 | 21 | 20
  - 同じ表の列：AreaID, Area, Year, Q1, Q2, Q3, Q4
- 例2 値：21 | 19 | 22 | 20 | 20
  - 同じ表の列：AreaID, Area, Year, Jan, Feb, Mar, Apr, May

## g0828（2 列）
- 見出し：AreaID
- 例1 値：6 | 1 | 15 | 2 | 4
  - 同じ表の列：RegionID, Area, Year, Q1, Q2, Q3, Q4
- 例2 値：3 | 15 | 11 | 4 | 1
  - 同じ表の列：RegionID, Area, Year, Jan, Feb, Mar, Apr, May

## g0829（1 列）
- 見出し：Area
- 例1 値：The Midlands | Dublin South Central | Dublin City North | Louth Meath | Dublin South East Wicklow
  - 同じ表の列：RegionID, AreaID, Year, Q1, Q2, Q3, Q4

## g0830（2 列）
- 見出し：Q1
- 例1 値：12 | 16 | 5 | 28 | 1
  - 同じ表の列：RegionID, AreaID, Area, Year, Q2, Q3, Q4
- 例2 値：7 | 5 | 5 | 3 | 2
  - 同じ表の列：QUEST, STYPE, CPO_STATUS, QF, Q2, Q3, Q4A, Q4B

## g0831（2 列）
- 見出し：Q2
- 例1 値：7 | 21 | 1 | 18 | 2
  - 同じ表の列：RegionID, AreaID, Area, Year, Q1, Q3, Q4
- 例2 値：5 | 5 | 2 | 5 | 5
  - 同じ表の列：QUEST, STYPE, CPO_STATUS, QF, Q1, Q3, Q4A, Q4B

## g0832（2 列）
- 見出し：Q3
- 例1 値：27 | 1 | 20 | 13 | 17
  - 同じ表の列：RegionID, AreaID, Area, Year, Q1, Q2, Q4
- 例2 値：7 | 2 | 7 | 3 | 4
  - 同じ表の列：QUEST, STYPE, CPO_STATUS, QF, Q1, Q2, Q4A, Q4B

## g0833（1 列）
- 見出し：Q4
- 例1 値：4 | 5 | 20 | 5 | 27
  - 同じ表の列：RegionID, AreaID, Area, Year, Q1, Q2, Q3

## g0834（1 列）
- 見出し：Eff_From
- 例1 値：2018 | 2022 | 2022 | 2018 | 2018
  - 同じ表の列：OBJECTID, Eff_To, Zoning, Area_Ha, Generic_Zoning, MyPlan_GZT, Designation, Information

## g0835（1 列）
- 見出し：Eff_To
- 例1 値：2028 | 2028 | 2024 | 2028 | 2024
  - 同じ表の列：OBJECTID, Eff_From, Zoning, Area_Ha, Generic_Zoning, MyPlan_GZT, Designation, Information

## g0836（1 列）
- 見出し：Zoning
- 例1 値：RE | LSS | New Residential | RE | RE
  - 同じ表の列：OBJECTID, Eff_From, Eff_To, Area_Ha, Generic_Zoning, MyPlan_GZT, Designation, Information

## g0837（1 列）
- 見出し：Area_Ha
- 例1 値：0.121166138650291 | 4.65689320313827 | 1.10588113127133 | 0.504259612776442 | 0.223929975622812
  - 同じ表の列：OBJECTID, Eff_From, Eff_To, Zoning, Generic_Zoning, MyPlan_GZT, Designation, Information

## g0838（1 列）
- 見出し：Generic_Zoning
- 例1 値：TC | RE | RE | OS2 | RE
  - 同じ表の列：OBJECTID, Eff_From, Eff_To, Zoning, Area_Ha, MyPlan_GZT, Designation, Information

## g0839（1 列）
- 見出し：MyPlan_GZT
- 例1 値：R1.3 | R2.6 | R2.6 | R2.6 | S5
  - 同じ表の列：OBJECTID, Eff_From, Eff_To, Zoning, Area_Ha, Generic_Zoning, Designation, Information

## g0840（1 列）
- 見出し：Designation
- 例1 値：These lands are already zoned as a ‘nat… | These lands are already zoned for resid… | These lands are already zoned for open … | These lands are already zoned for mixed… | These lands are already zoned for resid…
  - 同じ表の列：OBJECTID, Eff_From, Eff_To, Zoning, Area_Ha, Generic_Zoning, MyPlan_GZT, Information

## 答えの雛形

```
g0721	
g0722	
g0723	
g0724	
g0725	
g0726	
g0727	
g0728	
g0729	
g0730	
g0731	
g0732	
g0733	
g0734	
g0735	
g0736	
g0737	
g0738	
g0739	
g0740	
g0741	
g0742	
g0743	
g0744	
g0745	
g0746	
g0747	
g0748	
g0749	
g0750	
g0751	
g0752	
g0753	
g0754	
g0755	
g0756	
g0757	
g0758	
g0759	
g0760	
g0761	
g0762	
g0763	
g0764	
g0765	
g0766	
g0767	
g0768	
g0769	
g0770	
g0771	
g0772	
g0773	
g0774	
g0775	
g0776	
g0777	
g0778	
g0779	
g0780	
g0781	
g0782	
g0783	
g0784	
g0785	
g0786	
g0787	
g0788	
g0789	
g0790	
g0791	
g0792	
g0793	
g0794	
g0795	
g0796	
g0797	
g0798	
g0799	
g0800	
g0801	
g0802	
g0803	
g0804	
g0805	
g0806	
g0807	
g0808	
g0809	
g0810	
g0811	
g0812	
g0813	
g0814	
g0815	
g0816	
g0817	
g0818	
g0819	
g0820	
g0821	
g0822	
g0823	
g0824	
g0825	
g0826	
g0827	
g0828	
g0829	
g0830	
g0831	
g0832	
g0833	
g0834	
g0835	
g0836	
g0837	
g0838	
g0839	
g0840	
```
