# ラベル用シート 011 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_011.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1201（1 列）
- 見出し：Views
- 例1 値：400 | 102 | 11 | 12 | 28
  - 同じ表の列：Publisher Title, Visits

## g1202（1 列）
- 見出し：Visits
- 例1 値：46 | 30 | 0 | 28 | 4
  - 同じ表の列：Publisher Title, Views

## g1203（1 列）
- 見出し：SITC 3 digit
- 例1 値：012 Meat (excl beef), f.c.f. | 012 Meat (excl beef), f.c.f. | 024 Cheese & curd | 037 Seafood, prepared or preserved | 023 Butter
  - 同じ表の列：Year, Trade type, Country, Geographic level 1, Geographic level 2, Geographic level 3, APEC, ASEAN

## g1204（1 列）
- 見出し：Geographic level 2
- 例1 値：North America | East Asia | Middle East | East Asia | Pacific Islands
  - 同じ表の列：Year, Trade type, SITC 3 digit, Country, Geographic level 1, Geographic level 3, APEC, ASEAN

## g1205（1 列）
- 見出し：Geographic level 3
- 例1 値：South East Asia | Western Europe | North Africa | Southern Europe | North Africa
  - 同じ表の列：Year, Trade type, SITC 3 digit, Country, Geographic level 1, Geographic level 2, APEC, ASEAN

## g1206（1 列）
- 見出し：Business Category
- 例1 値：Rollerskating | Rollerskating | Rollerskating | Rollerskating | Rollerskating
  - 同じ表の列：Suburb, State, LGA, Region

## g1207（1 列）
- 見出し：LGA
- 例1 値：Yarra Ranges (S) | Nillumbik (S); Banyule (C) | Maroondah (C); Knox (C) | Mornington Peninsula (S) | Kingston (C)
  - 同じ表の列：Suburb, State, Business Category, Region

## g1208（1 列）
- 見出し：Region
- 例1 値：North and West Metropolitan Region | Gippsland Region | Southern Metropolitan Region | Southern Metropolitan Region | Eastern Metropolitan Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g1209（1 列）
- 見出し：operator
- 例1 値：Greater Shepparton City Council | Greater Shepparton City Council | Greater Shepparton City Council | Greater Shepparton City Council | Greater Shepparton City Council
  - 同じ表の列：lat, lon, wheelchair, needle_bin, ref

## g1210（1 列）
- 見出し：road_class
- 例1 値：VicRoads Main Road | VicRoads Main Road | VicRoads Main Road | VicRoads Main Road | VicRoads Main Road
  - 同じ表の列：type, suburb, maint_auth, area_sqm, length_m, width_m, bus_route, floodprone

## g1211（1 列）
- 見出し：maint_auth
- 例1 値：Hobsons Bay City Council | Hobsons Bay City Council | Hobsons Bay City Council | Hobsons Bay City Council | Hobsons Bay City Council
  - 同じ表の列：type, road_class, suburb, area_sqm, length_m, width_m, bus_route, floodprone

## g1212（1 列）
- 見出し：area_sqm
- 例1 値：1306.47 | 1829.02 | 2715.83 | 2531.92 | 2407.01
  - 同じ表の列：type, road_class, suburb, maint_auth, length_m, width_m, bus_route, floodprone

## g1213（1 列）
- 見出し：length_m
- 例1 値：93 | 241 | 111 | 44 | 63
  - 同じ表の列：type, road_class, suburb, maint_auth, area_sqm, width_m, bus_route, floodprone

## g1214（1 列）
- 見出し：width_m
- 例1 値：19.96 | 21.5 | 18.39 | 19.87 | 15.97
  - 同じ表の列：type, road_class, suburb, maint_auth, area_sqm, length_m, bus_route, floodprone

## g1215（1 列）
- 見出し：bus_route
- 例1 値：No | No | No | No | No
  - 同じ表の列：type, road_class, suburb, maint_auth, area_sqm, length_m, width_m, floodprone

## g1216（1 列）
- 見出し：floodprone
- 例1 値：Yes | No | No | No | Yes
  - 同じ表の列：type, road_class, suburb, maint_auth, area_sqm, length_m, width_m, bus_route

## g1217（1 列）
- 見出し：dist_services
- 例1 値：<100m | <100m | <100m | 100m - 300m | 100m - 300m
  - 同じ表の列：type, road_class, suburb, maint_auth, area_sqm, length_m, width_m, bus_route

## g1218（1 列）
- 見出し：YEAR_DISPLAY
- 例1 値：1825 | 1833 | 1841 | 1835 | 1863
  - 同じ表の列：YEAR

## g1219（1 列）
- 見出し：bin_cat
- 例1 値：Open Space | Open Space | Open Space | Open Space | Open Space
  - 同じ表の列：suburb, no_colls, coll_day, empties, lat, long

## g1220（1 列）
- 見出し：no_colls
- 例1 値：7 | 0 | 0 | 3 | 7
  - 同じ表の列：suburb, bin_cat, coll_day, empties, lat, long

## g1221（1 列）
- 見出し：coll_day
- 例1 値：MON/WED/FRI | MON/WED/FRI | MON/WED/FRI/SAT | MON/WED/FRI | MON/WED/FRI
  - 同じ表の列：suburb, bin_cat, no_colls, empties, lat, long

## g1222（1 列）
- 見出し：empties
- 例1 値：Council | Council | Contractor | Council | Council
  - 同じ表の列：suburb, bin_cat, no_colls, coll_day, lat, long

## g1223（1 列）
- 見出し：School Code
- 例1 値：2133 | 2094 | 2642 | 2379 | 1537
  - 同じ表の列：SA4, Status, Year

## g1224（1 列）
- 見出し：SA4
- 例1 値：Central Coast | Newcastle and Lake Macquarie | Sydney - Baulkham Hills and Hawkesbury | Sydney - Inner West | Central West
  - 同じ表の列：School Code, Status, Year

## g1225（1 列）
- 見出し：public users
- 例1 値：Visitors to reading rooms | Geelong Heritage Centre | Victorian Archives Centre | government users | Bendigo Regional Archives Centre
  - 同じ表の列：28,808

## g1226（1 列）
- 見出し：28,808
- 例1 値：3181 | 531 | 201 | 3,255 | 67
  - 同じ表の列：public users

## g1227（1 列）
- 見出し：Organisation
- 例1 値：Tarerer Festival | Bunjilaka Aboriginal Cultural Centre | lbijerri Theatre Company | Kirrit Barreet | Koorie Heritage Trust
  - 同じ表の列：Suburb/Town, Website

## g1228（1 列）
- 見出し：Suburb/Town
- 例1 値：Melbourne | Ballarat | Melbourne | Noth Melbourne | Bairnsdale
  - 同じ表の列：Organisation, Website

## g1229（1 列）
- 見出し：Website
- 例1 値：http://www.aboriginalballarat.com.au/ | http://www.ngv.vic.gov.au/ | http://www.koorieheritagetrust.com/ | http://www.ilbijerri.org.au/ | http://www.tarerer.com.au/
  - 同じ表の列：Organisation, Suburb/Town

## g1230（1 列）
- 見出し：public housing probationary
- 例1 値：1542 | 1931 | 1687 | 2132 | 1568
  - 同じ表の列：year, public housing dire…, public housing shor…, aboriginal housing …, aboriginal housing …, aboriginal housing …

## g1231（1 列）
- 見出し：public housing direct lease
- 例1 値：14 | 81 | 32 | 76 | 99
  - 同じ表の列：year, public housing prob…, public housing shor…, aboriginal housing …, aboriginal housing …, aboriginal housing …

## g1232（1 列）
- 見出し：public housing short term lease
- 例1 値：450 | 475 | 480 | 391 | 399
  - 同じ表の列：year, public housing prob…, public housing dire…, aboriginal housing …, aboriginal housing …, aboriginal housing …

## g1233（1 列）
- 見出し：aboriginal housing probationary
- 例1 値：115 | 86 | 107 | 90 | 59
  - 同じ表の列：year, public housing prob…, public housing dire…, public housing shor…, aboriginal housing …, aboriginal housing …

## g1234（1 列）
- 見出し：aboriginal housing direct lease
- 例1 値：0 | 0 | 1 | 0 | 0
  - 同じ表の列：year, public housing prob…, public housing dire…, public housing shor…, aboriginal housing …, aboriginal housing …

## g1235（1 列）
- 見出し：aboriginal housing short term lease
- 例1 値：20 | 17 | 20 | 16 | 26
  - 同じ表の列：year, public housing prob…, public housing dire…, public housing shor…, aboriginal housing …, aboriginal housing …

## g1236（1 列）
- 見出し：2016-17
- 例1 値：37.89 | 152 | $4 124 220 | 0 | 1
  - 同じ表の列：2017-18, 2018-19, 2019-20, 2020-21, 2021-22, 2022-23, % Change (+/-)

## g1237（1 列）
- 見出し：2017-18
- 例1 値：$587 537 | 140 | 0 | 35.83 | $3 267 807
  - 同じ表の列：2016-17, 2018-19, 2019-20, 2020-21, 2021-22, 2022-23, % Change (+/-)

## g1238（1 列）
- 見出し：2018-19
- 例1 値：32.58 | $3 090 732 | 1 | 118 | 0
  - 同じ表の列：2016-17, 2017-18, 2019-20, 2020-21, 2021-22, 2022-23, % Change (+/-)

## g1239（1 列）
- 見出し：2019-20
- 例1 値：39.29 | 2 212 909 | 138 | 2 | 0
  - 同じ表の列：2016-17, 2017-18, 2018-19, 2020-21, 2021-22, 2022-23, % Change (+/-)

## g1240（1 列）
- 見出し：2020-21
- 例1 値：0 | 4 | 4 | 143 | 33.52
  - 同じ表の列：2016-17, 2017-18, 2018-19, 2019-20, 2021-22, 2022-23, % Change (+/-)

## g1241（1 列）
- 見出し：2021-22
- 例1 値：163 | 2 | 32.5 | 3 182 408 | 3
  - 同じ表の列：2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2022-23, % Change (+/-)

## g1242（1 列）
- 見出し：2022-23
- 例1 値：0 | 2 | 3 412 377 | 41 | 8 490 155
  - 同じ表の列：2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22, % Change (+/-)

## g1243（1 列）
- 見出し：% Change (+/-)
- 例1 値：0% | 7.30% | -66.60% | -21.00% | 6.90%
  - 同じ表の列：2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22, 2022-23

## g1244（1 列）
- 見出し：X Values
- 例1 値：CO | NOx | PM_{10} | PM_{2.5} | Total VOCs
  - 同じ表の列：commercial, domestic commercial, industrial, Long titles, %commercial, %domestic commercial, %industrial

## g1245（1 列）
- 見出し：commercial
- 例1 値：2.85E-05 | 0.21708824458017 | 0 | 0.008242036038323 | 9.32E-05
  - 同じ表の列：X Values, domestic commercial, industrial, Long titles, %commercial, %domestic commercial, %industrial

## g1246（1 列）
- 見出し：domestic commercial
- 例1 値：0.143737970300761 | 0.117641856324047 | 0.001387076103444 | 0.025599614061327 | 0.039976304792586
  - 同じ表の列：X Values, commercial, industrial, Long titles, %commercial, %domestic commercial, %industrial

## g1247（1 列）
- 見出し：industrial
- 例1 値：0.302439144950174 | 0.820675924230237 | 0.642273821994514 | 0.234792594397572 | 0.999496927585845
  - 同じ表の列：X Values, commercial, domestic commercial, Long titles, %commercial, %domestic commercial, %industrial

## g1248（1 列）
- 見出し：Long titles
- 例1 値：PM_{2.5} | Oxides of\\nitrogen | Lead and\\compounds | Sulfur\\dioxide | Carbon\\monoxide
  - 同じ表の列：X Values, commercial, domestic commercial, industrial, %commercial, %domestic commercial, %industrial

## g1249（1 列）
- 見出し：%commercial
- 例1 値：0.001299528790546 | 0.000388170047298 | 0 | 21.708824458017 | 0.824203603832263
  - 同じ表の列：X Values, commercial, domestic commercial, industrial, Long titles, %domestic commercial, %industrial

## g1250（1 列）
- 見出し：%domestic commercial
- 例1 値：2.55996140613267 | 14.3737970300761 | 0.009390685064226 | 0.138707610344412 | 11.7641856324047
  - 同じ表の列：X Values, commercial, domestic commercial, industrial, Long titles, %commercial, %industrial

## g1251（1 列）
- 見出し：%industrial
- 例1 値：64.2273821994514 | 30.2439144950174 | 23.4792594397572 | 82.0675924230238 | 26.1096415017469
  - 同じ表の列：X Values, commercial, domestic commercial, industrial, Long titles, %commercial, %domestic commercial

## g1252（1 列）
- 見出し：itemid
- 例1 値：478059 | 821815 | 478018 | 477996 | 821809
  - 同じ表の列：title, caption, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink

## g1253（1 列）
- 見出し：title
- 例1 値：Orbis terrarum nova et accuratissima ta… | Botany Bay [cartographic material] / Wi… | Nova, et integra universi orbis descrip… | A new map of the world, with Captain Co… | The antiquity & excellency of globes : …
  - 同じ表の列：itemid, caption, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink

## g1254（1 列）
- 見出し：caption
- 例1 値：Claudii Ptholemaei Alexandrini Liber ge… | Moll. In Wallis's copy of The English P… | Liber cronicarum | Benedict Arias Montanus sacrae geograph… | Liber cronicarum
  - 同じ表の列：itemid, title, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink

## g1255（1 列）
- 見出し：albumnumber
- 例1 値：861493 | 861463 | 861434 | 861208 | 861422
  - 同じ表の列：itemid, title, caption, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink

## g1256（1 列）
- 見出し：dateofwork
- 例1 値：1756 | 1752 | 1798-9 | [1570?] | 1493
  - 同じ表の列：itemid, title, caption, albumnumber, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink

## g1257（1 列）
- 見出し：collectionitemlink
- 例1 値：http://library.sl.nsw.gov.au/record=b20… | http://library.sl.nsw.gov.au/record=b20… | http://library.sl.nsw.gov.au/record=b14… | http://library.sl.nsw.gov.au/record=b20… | http://library.sl.nsw.gov.au/record=b20…
  - 同じ表の列：itemid, title, caption, albumnumber, dateofwork, digitalitemlink, digitalordernumber, thumbnaillink

## g1258（1 列）
- 見出し：digitalitemlink
- 例1 値：http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?…
  - 同じ表の列：itemid, title, caption, albumnumber, dateofwork, collectionitemlink, digitalordernumber, thumbnaillink

## g1259（1 列）
- 見出し：digitalordernumber
- 例1 値：a127077 | a127002 | a127011 | a127021 | a127073
  - 同じ表の列：itemid, title, caption, albumnumber, dateofwork, collectionitemlink, digitalitemlink, thumbnaillink

## g1260（1 列）
- 見出し：thumbnaillink
- 例1 値：http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/2…
  - 同じ表の列：itemid, title, caption, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g1261（1 列）
- 見出し：highreslink
- 例1 値：http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1…
  - 同じ表の列：itemid, title, caption, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g1262（1 列）
- 見出し：TITLE
- 例1 値：Entr'acte | The Collie Mail | The Wickepin Argus and Eastern District… | Joondalup Times | The Floreat Times
  - 同じ表の列：DATES, FORMERTITLE, LATERTITLE, AREA

## g1263（1 列）
- 見出し：DATES
- 例1 値：1976 - 1984 | 1987 - 1990 | 2005 - present | 1983 - 1986 | 1997?
  - 同じ表の列：TITLE, FORMERTITLE, LATERTITLE, AREA

## g1264（1 列）
- 見出し：FORMERTITLE
- 例1 値：South Suburban News | Western Australian Pensioners' News | Newman Chronicle | Perth Gazette, and Independent Journal … | Melville Section
  - 同じ表の列：TITLE, DATES, LATERTITLE, AREA

## g1265（1 列）
- 見出し：LATERTITLE
- 例1 値：Goldfields Weekender | Labor Voice | Western Australian No. 54 (1849)? | Swan Leader | Nor-West Echo
  - 同じ表の列：TITLE, DATES, FORMERTITLE, AREA

## g1266（1 列）
- 見出し：AREA
- 例1 値：Menzies; Malcolm; Lawlers; Leonora; Gwa… | Mukinbudin; Merredin; Narembeen; Corrig… | Harrismith; Kulin | Bedford; Coolbinia; Highgate; Inglewood… | Geraldton; Mingenew; Irwin
  - 同じ表の列：TITLE, DATES, FORMERTITLE, LATERTITLE

## g1267（1 列）
- 見出し：ZoneID
- 例1 値：142272 | 142634 | 142221 | 140432 | 141941
  - 同じ表の列：RCACConsVa, RCACScore, SiteCode, TravelDire, EVCCode, LengthM, HabitatSco, SimpleDate

## g1268（1 列）
- 見出し：RCACConsVa
- 例1 値：Medium | Medium | High | Medium | Medium
  - 同じ表の列：ZoneID, RCACScore, SiteCode, TravelDire, EVCCode, LengthM, HabitatSco, SimpleDate

## g1269（1 列）
- 見出し：RCACScore
- 例1 値：13 | 11 | 16 | 10 | 30
  - 同じ表の列：ZoneID, RCACConsVa, SiteCode, TravelDire, EVCCode, LengthM, HabitatSco, SimpleDate

## g1270（1 列）
- 見出し：SiteCode
- 例1 値：ST013 | ST026 | ST001 | ST024 | ST002
  - 同じ表の列：ZoneID, RCACConsVa, RCACScore, TravelDire, EVCCode, LengthM, HabitatSco, SimpleDate

## g1271（1 列）
- 見出し：TravelDire
- 例1 値：SE | S | S | S | S
  - 同じ表の列：ZoneID, RCACConsVa, RCACScore, SiteCode, EVCCode, LengthM, HabitatSco, SimpleDate

## g1272（1 列）
- 見出し：EVCCode
- 例1 値：408 | 2263 | 235 | 235 | 22
  - 同じ表の列：ZoneID, RCACConsVa, RCACScore, SiteCode, TravelDire, LengthM, HabitatSco, SimpleDate

## g1273（1 列）
- 見出し：LengthM
- 例1 値：706 | 443 | 1037 | 8160 | 859
  - 同じ表の列：ZoneID, RCACConsVa, RCACScore, SiteCode, TravelDire, EVCCode, HabitatSco, SimpleDate

## g1274（1 列）
- 見出し：HabitatSco
- 例1 値：41 | 40 | 49 | 59 | 57
  - 同じ表の列：ZoneID, RCACConsVa, RCACScore, SiteCode, TravelDire, EVCCode, LengthM, SimpleDate

## g1275（1 列）
- 見出し：SimpleDate
- 例1 値：25/09/2017 | 27/09/2017 | 26/10/2017 | 11/12/2019 | 24/10/2017
  - 同じ表の列：ZoneID, RCACConsVa, RCACScore, SiteCode, TravelDire, EVCCode, LengthM, HabitatSco

## g1276（1 列）
- 見出し：ManPrescri
- 例1 値：235M.pdf | 2257H.pdf | 235M.pdf | 697M.pdf | 235L.pdf
  - 同じ表の列：ZoneID, RCACConsVa, RCACScore, SiteCode, TravelDire, EVCCode, LengthM, HabitatSco

## g1277（1 列）
- 見出し：Holes
- 例1 値：9 | 18 | 18 | 18 | 18
  - 同じ表の列：Locality, Long, Lat

## g1278（1 列）
- 見出し：val_date
- 例1 値：2023-06-26T17:30:21Z | 2023-06-27T12:15:29Z | 2023-06-26T18:15:21Z | 2023-07-01T02:15:26Z | 2023-06-30T23:45:25Z
  - 同じ表の列：dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g1279（1 列）
- 見出し：dev_netid
- 例1 値：835907406 | 835907406 | 835907406 | 835907406 | 835907406
  - 同じ表の列：val_date, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g1280（1 列）
- 見出し：dev_chid
- 例1 値：9 | 10 | 9 | 10 | 9
  - 同じ表の列：val_date, dev_netid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g1281（1 列）
- 見出し：val_raw
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_type, dev_tag, dev_site, val_cal, val_offset

## g1282（1 列）
- 見出し：val_type
- 例1 値：Count | Count | Count | Count | Count
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, dev_tag, dev_site, val_cal, val_offset

## g1283（1 列）
- 見出し：dev_tag
- 例1 値：SWH-CAM01 | SWH-CAM01 | SWH-CAM01 | SWH-CAM01 | SWH-CAM01
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_site, val_cal, val_offset

## g1284（1 列）
- 見出し：dev_site
- 例1 値：Airports - SHRCC | Airports - SHRCC | Airports - SHRCC | Airports - SHRCC | Airports - SHRCC
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, val_cal, val_offset

## g1285（1 列）
- 見出し：val_cal
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_offset

## g1286（1 列）
- 見出し：val_offset
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal

## g1287（1 列）
- 見出し：dev_type
- 例1 値：device | device | device | device | device
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal

## g1288（1 列）
- 見出し：Electoral Division
- 例1 値：Division 1 | Division 1 | Division 1 | Division 1 | Division 1
  - 同じ表の列：Suburb, Year, Month Received, Tree Maintenance, Road Defects, Grass Cutting, Potholes, Public Toilet Maint…

## g1289（1 列）
- 見出し：Month Received
- 例1 値：Dec | Nov | Sep | Jul | Jul
  - 同じ表の列：Electoral Division, Suburb, Year, Tree Maintenance, Road Defects, Grass Cutting, Potholes, Public Toilet Maint…

## g1290（1 列）
- 見出し：Tree Maintenance
- 例1 値：1 | 3 | 5 | 1 | 3
  - 同じ表の列：Electoral Division, Suburb, Year, Month Received, Road Defects, Grass Cutting, Potholes, Public Toilet Maint…

## g1291（1 列）
- 見出し：Road Defects
- 例1 値：1 | 1 | 4 | 1 | 3
  - 同じ表の列：Electoral Division, Suburb, Year, Month Received, Tree Maintenance, Grass Cutting, Potholes, Public Toilet Maint…

## g1292（1 列）
- 見出し：Grass Cutting
- 例1 値：1 | 1 | 2 | 2 | 2
  - 同じ表の列：Electoral Division, Suburb, Year, Month Received, Tree Maintenance, Road Defects, Potholes, Public Toilet Maint…

## g1293（1 列）
- 見出し：Potholes
- 例1 値：4 | 1 | 1 | 3 | 1
  - 同じ表の列：Electoral Division, Suburb, Year, Month Received, Tree Maintenance, Road Defects, Grass Cutting, Public Toilet Maint…

## g1294（1 列）
- 見出し：Public Toilet Maintenance
- 例1 値：2 | 4 | 2 | 2 | 2
  - 同じ表の列：Electoral Division, Suburb, Year, Month Received, Tree Maintenance, Road Defects, Grass Cutting, Potholes

## g1295（1 列）
- 見出し：CKOs Only
- 例1 値：384613 | 334460 | 166742 | 139286 | 151565
  - 同じ表の列：_id, Library, Total Loans, RFID CKOs only, RFID loans

## g1296（1 列）
- 見出し：Total Loans
- 例1 値：551573 | 480015 | 189070 | 220656 | 207388
  - 同じ表の列：_id, Library, CKOs Only, RFID CKOs only, RFID loans

## g1297（1 列）
- 見出し：RFID CKOs only
- 例1 値：310859 | 375156 | 143789 | 131874 | 163577
  - 同じ表の列：_id, Library, CKOs Only, Total Loans, RFID loans

## g1298（1 列）
- 見出し：RFID loans
- 例1 値：433829 | 174476 | 187275 | 408634 | 157983
  - 同じ表の列：_id, Library, CKOs Only, Total Loans, RFID CKOs only

## g1299（2 列）
- 見出し：Statistic
- 例1 値：Second Chance Education | Second Chance Education | Second Chance Education | Second Chance Education | Second Chance Education
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02199V02655, Sex, C02460V02978, Type of Second Chan…, UNIT
- 例2 値：New House Prices | New House Prices | New House Prices | New House Prices | New House Prices
  - 同じ表の列：STATISTIC, TLIST(Q1), Quarter, C02343V02817, Area, UNIT, VALUE

## g1300（1 列）
- 見出し：C02199V02655
- 例1 値：1 | - | 1 | 1 | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Sex, C02460V02978, Type of Second Chan…, UNIT

## g1301（1 列）
- 見出し：Sex
- 例1 値：Male | Female | Female | Female | Both sexes
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, C02460V02978, Type of Second Chan…, UNIT

## g1302（1 列）
- 見出し：C02460V02978
- 例1 値：12 | 31 | 11 | 11 | 22
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, Type of Second Chan…, UNIT

## g1303（1 列）
- 見出し：Type of Second Chance Education
- 例1 値：All senior traveller training (STT) | Core VTOS | Foundation level senior traveller train… | All VTOS | Foundation level senior traveller train…
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C02460V02978, UNIT

## g1304（1 列）
- 見出し：Statistic Label
- 例1 値：Surgical Procedure | Surgical Procedure | Surgical Procedure | Surgical Procedure | Surgical Procedure
  - 同じ表の列：STATISTIC, YEAR, Year, PROCTYPE, Type of surigcal pr…, CASETYPE, Case type, UNIT

## g1305（1 列）
- 見出し：PROCTYPE
- 例1 値：MAST | TONSILLECT | TOTKNEE | TONSILLECT | MAST
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Type of surigcal pr…, CASETYPE, Case type, UNIT

## g1306（1 列）
- 見出し：Type of surigcal proceudre
- 例1 値：Caesarean section | Total knee replacement | Tonsillectomy | Total knee replacement | Caesarean section
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, PROCTYPE, CASETYPE, Case type, UNIT

## g1307（1 列）
- 見出し：CASETYPE
- 例1 値：TOT | INP | DAY | TOT | INP
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, PROCTYPE, Type of surigcal pr…, Case type, UNIT

## g1308（1 列）
- 見出し：Case type
- 例1 値：Inpatient cases | Day cases | Day cases | Total cases | Inpatient cases
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, PROCTYPE, Type of surigcal pr…, CASETYPE, UNIT

## g1309（1 列）
- 見出し：C02343V02817
- 例1 値：04 | 01 | - | 05 | 01
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, Area, UNIT, VALUE

## g1310（1 列）
- 見出し：Area
- 例1 値：Other areas | National | Other areas | Limerick | Waterford
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02343V02817, UNIT, VALUE

## g1311（1 列）
- 見出し：Type
- 例1 値：Domestic Residence & Permissions applic… | Domestic Residence & Permissions applic… | Domestic Residence & Permissions applic… | Domestic Residence & Permissions applic… | Domestic Residence & Permissions applic…
  - 同じ表の列：Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g1312（1 列）
- 見出し：Nationality
- 例1 値：Tonga | Åland Islands | Western Sahara | Venezuela (Bolivarian Republic of) | Malawi
  - 同じ表の列：Type, Status, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g1313（1 列）
- 見出し：unsafe_2019
- 例1 値：20 | 0 | * | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2020, unsafe_2021, unsafe_2022

## g1314（1 列）
- 見出し：unsafe_2021
- 例1 値：11 | 270 | 0 | * | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2022

## g1315（1 列）
- 見出し：unsafe_2022
- 例1 値：1030 | * | 9 | * | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g1316（1 列）
- 見出し：programme
- 例1 値：Working Age Income Supports | Working Age Income Supports | Supplementary Payments and Miscellaneou… | Supplementary Payments and Miscellaneou… | Pensions
  - 同じ表の列：period, scheme, basis, recipients

## g1317（1 列）
- 見出し：Row Labels
- 例1 値：GRANGE GORMAN | BALLYFERMOT | WINDMILL ROAD | ORWELL ROAD | EAMONN CEANT
  - 同じ表の列：January, February, March, April, May, June, July, August

## g1318（1 列）
- 見出し：January
- 例1 値：236660 | 73000 | 25240 | 10580 | 8540
  - 同じ表の列：Row Labels, February, March, April, May, June, July, August

## g1319（1 列）
- 見出し：February
- 例1 値：10380 | 48520 | 161480 | 29860 | 12680
  - 同じ表の列：Row Labels, January, March, April, May, June, July, August

## g1320（1 列）
- 見出し：March
- 例1 値：19920 | 19740 | 9720 | 47400 | 172440
  - 同じ表の列：Row Labels, January, February, April, May, June, July, August

## 答えの雛形

```
g1201	
g1202	
g1203	
g1204	
g1205	
g1206	
g1207	
g1208	
g1209	
g1210	
g1211	
g1212	
g1213	
g1214	
g1215	
g1216	
g1217	
g1218	
g1219	
g1220	
g1221	
g1222	
g1223	
g1224	
g1225	
g1226	
g1227	
g1228	
g1229	
g1230	
g1231	
g1232	
g1233	
g1234	
g1235	
g1236	
g1237	
g1238	
g1239	
g1240	
g1241	
g1242	
g1243	
g1244	
g1245	
g1246	
g1247	
g1248	
g1249	
g1250	
g1251	
g1252	
g1253	
g1254	
g1255	
g1256	
g1257	
g1258	
g1259	
g1260	
g1261	
g1262	
g1263	
g1264	
g1265	
g1266	
g1267	
g1268	
g1269	
g1270	
g1271	
g1272	
g1273	
g1274	
g1275	
g1276	
g1277	
g1278	
g1279	
g1280	
g1281	
g1282	
g1283	
g1284	
g1285	
g1286	
g1287	
g1288	
g1289	
g1290	
g1291	
g1292	
g1293	
g1294	
g1295	
g1296	
g1297	
g1298	
g1299	
g1300	
g1301	
g1302	
g1303	
g1304	
g1305	
g1306	
g1307	
g1308	
g1309	
g1310	
g1311	
g1312	
g1313	
g1314	
g1315	
g1316	
g1317	
g1318	
g1319	
g1320	
```
