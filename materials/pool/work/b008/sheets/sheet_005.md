# ラベル用シート 005 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_005.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0481（1 列）
- 見出し：利用可能曜日
- 例1 値：火水木金土日 | 火水木金土日 | 火水木金土日 | 火水木金土日 | 火水木金土日
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 町字ID, 建物名等(方書), 団体名, 開始時間

## g0482（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都瑞穂町 | 東京都瑞穂町 | 東京都瑞穂町 | 東京都瑞穂町 | 東京都瑞穂町
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 名称_英字, 内線番号, 利用可能曜日, 開始時間

## g0483（1 列）
- 見出し：名称
- 例1 値：瑞穂中央体育館 | 瑞穂町営プール | 瑞穂町営第2グランド | 瑞穂町営グランド | 瑞穂町営少年サッカー場
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ, 名称_英字, 内線番号, 利用可能曜日, 開始時間

## g0484（1 列）
- 見出し：名称_カナ
- 例1 値：ミズホチョウエイプール | ミズホチョウエイダイニテイキュウジョウ | シクラメンスポーツコウエン | ミズホブドウカン | ミズホチョウエイショウネンサッカージョウ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_英字, 内線番号, 利用可能曜日, 開始時間

## g0485（1 列）
- 見出し：名称_英字
- 例1 値：NAGAOKA community center
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 内線番号, 利用可能曜日, 開始時間

## g0486（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都日の出町 | 東京都日の出町 | 東京都日の出町 | 東京都日の出町 | 東京都日の出町
  - 同じ表の列：全国地方公共団体コード, 名称, 名称_カナ, 団体名, 利用可能曜日, 開始時間, 終了時間, 利用可能時間特記事項

## g0487（1 列）
- 見出し：名称
- 例1 値：日の出町塩田テニス場 | 日の出町民グランド | スポーツパーク・やすらぎとふれあいの丘 | スポーツと文化の森・谷戸沢サッカー場 | スポーツと文化の森・谷戸沢グランド
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称_カナ, 団体名, 利用可能曜日, 開始時間, 終了時間, 利用可能時間特記事項

## g0488（1 列）
- 見出し：名称_カナ
- 例1 値：ヒノデマチシオダテニスジョウ | スポーツトブンカノモリ・ヤトザワグランド | スポーツパーク・ヤスラギトフレアイノオカ | ヒノデチョウミングランド | スポーツトブンカノモリ・ヤトザワサッカージョウ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 団体名, 利用可能曜日, 開始時間, 終了時間, 利用可能時間特記事項

## g0489（1 列）
- 見出し：団体名
- 例1 値：日の出町 | 日の出町 | 日の出町 | 日の出町 | 日の出町
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 利用可能曜日, 開始時間, 終了時間, 利用可能時間特記事項

## g0490（1 列）
- 見出し：利用可能時間特記事項
- 例1 値：貸出期間は5/1~10/31まで | 7月~9月は午前7時~日没 | 日没まで | 日没まで
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 団体名, 利用可能曜日, 開始時間, 終了時間

## g0491（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都大島町 | 東京都大島町 | 東京都大島町 | 東京都大島町 | 東京都大島町
  - 同じ表の列：名称, 名称_カナ, 建物名等(方書), 連絡先FormURL, 団体名, 利用可能曜日, 開始時間, 終了時間

## g0492（1 列）
- 見出し：名称
- 例1 値：第三中学校グランド | 第一中学校グランド | さくら小学校体育館 | つばき小学校体育館 | つつじ小学校体育館
  - 同じ表の列：地方公共団体名, 名称_カナ, 建物名等(方書), 連絡先FormURL, 団体名, 利用可能曜日, 開始時間, 終了時間

## g0493（1 列）
- 見出し：名称_カナ
- 例1 値：ダイイチチュウガッコウグランド | スモウジョウ | ダイイチチュウガッコウタイイクカン | ダイニチュウガッコウタイイクカン | トレーニングセンター
  - 同じ表の列：地方公共団体名, 名称, 建物名等(方書), 連絡先FormURL, 団体名, 利用可能曜日, 開始時間, 終了時間

## g0494（1 列）
- 見出し：建物名等(方書)
- 例1 値：第三中学校 | 第二中学校 | つばき小学校 | つつじ小学校 | 第一中学校
  - 同じ表の列：地方公共団体名, 名称, 名称_カナ, 連絡先FormURL, 団体名, 利用可能曜日, 開始時間, 終了時間

## g0495（1 列）
- 見出し：連絡先FormURL
- 例1 値：https://www.town.oshima.tokyo.jp/site/o… | https://www.town.oshima.tokyo.jp/site/o… | https://www.town.oshima.tokyo.jp/~oshim… | https://www.town.oshima.tokyo.jp/site/o… | https://www.town.oshima.tokyo.jp/~oshim…
  - 同じ表の列：地方公共団体名, 名称, 名称_カナ, 建物名等(方書), 団体名, 利用可能曜日, 開始時間, 終了時間

## g0496（1 列）
- 見出し：団体名
- 例1 値：大島町 | 大島町 | 大島町 | 大島町 | 大島町
  - 同じ表の列：地方公共団体名, 名称, 名称_カナ, 建物名等(方書), 連絡先FormURL, 利用可能曜日, 開始時間, 終了時間

## g0497（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都八丈町 | 東京都八丈町 | 東京都八丈町 | 東京都八丈町 | 東京都八丈町
  - 同じ表の列：全国地方公共団体コード, 名称, 名称_カナ, 法人番号, 団体名, 利用可能曜日, 開始時間, 終了時間

## g0498（1 列）
- 見出し：名称
- 例1 値：富士ゲートボール場 | 富士中学校運動場 | 中之郷屋内運動場 | 三根公民館 | 大賀郷小学校屋内運動場
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称_カナ, 法人番号, 団体名, 利用可能曜日, 開始時間, 終了時間

## g0499（1 列）
- 見出し：名称_カナ
- 例1 値：スエヨシオクナイウンドウジョウ | ハチジョウマチコミュニティセンター | カシタテオクナイウンドウジョウ | フジチュウガッコウウンドウジョウ | ミツネショウガッコウウンドウジョウ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 法人番号, 団体名, 利用可能曜日, 開始時間, 終了時間

## g0500（1 列）
- 見出し：団体名
- 例1 値：八丈町 | 八丈町 | 八丈町 | 八丈町 | 八丈町
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 法人番号, 利用可能曜日, 開始時間, 終了時間

## g0501（1 列）
- 見出し：利用可能曜日
- 例1 値：日月火水木金土 | 日月火水木金土 | 日月火水木金土 | 日月火水木金土 | 日月火水木金土
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 法人番号, 団体名, 開始時間, 終了時間

## g0502（2 列）
- 見出し：abn
- 例1 値：11014757615 | 11624618819 | 11846675799 | 12212586792 | 11443064118
  - 同じ表の列：registration status, charity website, charity size, basic religious cha…, ais due date, date ais received, financial report da…, conducted activities
- 例2 値：50649697383 | 90934786081 | 73896849034 | 35683908730 | 43390658595
  - 同じ表の列：ICN, Status Reason, Registered On, Deregistered On, Corporation Size, Industry Sector(s), Corporation registe…, 2023 Total Income

## g0503（1 列）
- 見出し：registration status
- 例1 値：Registered | Registered | Registered | Registered | Registered
  - 同じ表の列：abn, charity website, charity size, basic religious cha…, ais due date, date ais received, financial report da…, conducted activities

## g0504（1 列）
- 見出し：charity website
- 例1 値：https://www.coffscoastwildlifesanctuary… | http://www.handupcongo.org | https://bletchingt-p.schools.nsw.gov.au… | www.newlifert.com.au | www.scienceaustralia.org.au
  - 同じ表の列：abn, registration status, charity size, basic religious cha…, ais due date, date ais received, financial report da…, conducted activities

## g0505（1 列）
- 見出し：charity size
- 例1 値：Small | Small | Small | Small | Large
  - 同じ表の列：abn, registration status, charity website, basic religious cha…, ais due date, date ais received, financial report da…, conducted activities

## g0506（1 列）
- 見出し：basic religious charity
- 例1 値：n | n | n | n | n
  - 同じ表の列：abn, registration status, charity website, charity size, ais due date, date ais received, financial report da…, conducted activities

## g0507（1 列）
- 見出し：ais due date
- 例1 値：31/01/2025 | 31/01/2025 | 30/06/2025 | 31/01/2025 | 31/01/2025
  - 同じ表の列：abn, registration status, charity website, charity size, basic religious cha…, date ais received, financial report da…, conducted activities

## g0508（1 列）
- 見出し：date ais received
- 例1 値：31/03/2026 | 16/06/2025 | 31/01/2025 | 27/06/2025 | 09/10/2024
  - 同じ表の列：abn, registration status, charity website, charity size, basic religious cha…, ais due date, financial report da…, conducted activities

## g0509（1 列）
- 見出し：financial report date received
- 例1 値：08/07/2025 | 14/01/2025 | 10/07/2025 | 04/03/2025 | 03/12/2024
  - 同じ表の列：abn, registration status, charity website, charity size, basic religious cha…, ais due date, date ais received, conducted activities

## g0510（1 列）
- 見出し：conducted activities
- 例1 値：y | y | y | n | y
  - 同じ表の列：abn, registration status, charity website, charity size, basic religious cha…, ais due date, date ais received, financial report da…

## g0511（1 列）
- 見出し：why charity did not conduct activities
- 例1 値：Due to the small number and age of our … | Charity is still in the process of ding… | Lack of resourcing and funding for FY20… | We were awaiting grants and sponsorship… | per 2023 AIS
  - 同じ表の列：abn, registration status, charity website, charity size, basic religious cha…, ais due date, date ais received, financial report da…

## g0512（1 列）
- 見出し：language_code
- 例1 値：K52 | E90 | E7 | W7 | N171
  - 同じ表の列：language_synonym, uri

## g0513（1 列）
- 見出し：language_synonym
- 例1 値：Lairmairrener|Big River tribe|Big River… | Tjalkanti|Tjalkadjara|Barduwonga|Djalga… | Pitjara|Bidjera|Bithara|Bitjara|Minkaba… | Ngarrket|Narrinyeri|Jarijari|Jere jere|… | Gugadja|Kokatja|Gogada|Gogadja|Gogadya|…
  - 同じ表の列：language_code, uri

## g0514（1 列）
- 見出し：uri
- 例1 値：https://collection.aiatsis.gov.au/austl… | https://collection.aiatsis.gov.au/austl… | https://collection.aiatsis.gov.au/austl… | https://collection.aiatsis.gov.au/austl… | https://collection.aiatsis.gov.au/austl…
  - 同じ表の列：language_code, language_synonym

## g0515（1 列）
- 見出し：grim
- 例1 値：GRIM0000 | GRIM0000 | GRIM0000 | GRIM0000 | GRIM0000
  - 同じ表の列：cause_of_death, year, sex, age_group, deaths, crude_rate_per_1000…, age_standardised_ra…

## g0516（1 列）
- 見出し：cause_of_death
- 例1 値：All causes combined (ICD-10 all) | All causes combined (ICD-10 all) | All causes combined (ICD-10 all) | All causes combined (ICD-10 all) | All causes combined (ICD-10 all)
  - 同じ表の列：grim, year, sex, age_group, deaths, crude_rate_per_1000…, age_standardised_ra…

## g0517（17 列）
- 見出し：year
- 例1 値：1912 | 1922 | 1908 | 1912 | 1921
  - 同じ表の列：grim, cause_of_death, sex, age_group, deaths, crude_rate_per_1000…, age_standardised_ra…
- 例2 値：2017 | 2023 | 2019 | 2019 | 2018
  - 同じ表の列：Council, Location, Count, Month, Date

## g0518（1 列）
- 見出し：sex
- 例1 値：Persons | Females | Females | Females | Females
  - 同じ表の列：grim, cause_of_death, year, age_group, deaths, crude_rate_per_1000…, age_standardised_ra…

## g0519（1 列）
- 見出し：age_group
- 例1 値：0–4 | 10–14 | 65–69 | 35–39 | 0–4
  - 同じ表の列：grim, cause_of_death, year, sex, deaths, crude_rate_per_1000…, age_standardised_ra…

## g0520（1 列）
- 見出し：deaths
- 例1 値：5835 | 403 | 1292 | 1072 | 405
  - 同じ表の列：grim, cause_of_death, year, sex, age_group, crude_rate_per_1000…, age_standardised_ra…

## g0521（1 列）
- 見出し：crude_rate_per_100000
- 例1 値：432.4 | 507.7 | 792.6 | 993.8 | 5565.9
  - 同じ表の列：grim, cause_of_death, year, sex, age_group, deaths, age_standardised_ra…

## g0522（1 列）
- 見出し：age_standardised_rate_per_100000
- 例1 値：2241.7 | 1967.6 | 1779.4 | 2255.1 | 2188.2
  - 同じ表の列：grim, cause_of_death, year, sex, age_group, deaths, crude_rate_per_1000…

## g0523（1 列）
- 見出し：Council
- 例1 値：Rural City of Wangaratta | Rural City of Wangaratta | Alpine Shire Council | Alpine Shire Council | Alpine Shire Council
  - 同じ表の列：Location, Count, Month, Year, Date

## g0524（1 列）
- 見出し：Location
- 例1 値：Wangaratta South East | Oxley (Snow Road) | Wangaratta North | Everton (Boundary Road) | Tarrawingee
  - 同じ表の列：Council, Count, Month, Year, Date

## g0525（1 列）
- 見出し：Count
- 例1 値：611 | 388 | 6370 | 612 | 946
  - 同じ表の列：Council, Location, Month, Year, Date

## g0526（2 列）
- 見出し：Month
- 例1 値：December | December | July | January | November
  - 同じ表の列：Council, Location, Count, Year, Date
- 例2 値：November | January | October | August | July
  - 同じ表の列：State/Territory, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0527（2 列）
- 見出し：Date
- 例1 値：2024-02 | 2019-03 | 2015-11 | 2020-12 | 2017-09
  - 同じ表の列：Council, Location, Count, Month, Year
- 例2 値：2025-05 | 2024-03 | 2023-12 | 2021-05 | 2024-09
  - 同じ表の列：Value, obs__status, obs__conf_, Series key, Title complement, Decimals, Units, Issuance Type

## g0528（1 列）
- 見出し：Festival
- 例1 値：Woodend Winter Arts Festival | Mildura Wentworth Arts Festival | Southern Grampians Promenade of Sacred … | Darebin Music Feast | Eltham Jazz and Blues Heritage Festival
  - 同じ表の列：Town/Suburb, Website, Dates

## g0529（1 列）
- 見出し：Town/Suburb
- 例1 値：Castlemaine | Westen Suburbs, Melbourne | Melbourne City | Grampians | Darebin
  - 同じ表の列：Festival, Website, Dates

## g0530（1 列）
- 見出し：Website
- 例1 値：http://www.melbournefilmfestival.com.au/ | http://inside.nextwave.org.au/ | http://www.eelfestival.org.au | http://www.apollobaymusicfestival.com/ | http://www.elthamtown.com.au//index.php…
  - 同じ表の列：Festival, Town/Suburb, Dates

## g0531（1 列）
- 見出し：Dates
- 例1 値：8-23 October 2010 | Late April Dates to be announced | 6-14 February 2010 | 23-29 August 2010 | 8-10 October 2010
  - 同じ表の列：Festival, Town/Suburb, Website

## g0532（1 列）
- 見出し：Distance
- 例1 値：1.4km | 1.7km | 0.8km | 1.3km | 0.7km
  - 同じ表の列：Time

## g0533（1 列）
- 見出し：Time
- 例1 値：about 37 min | 21 mins | 20 mins | 4 mins | about 4 min
  - 同じ表の列：Distance

## g0534（1 列）
- 見出し：Artform
- 例1 値：Dance | Community Partnerships | ATSIA | Community Partnerships | Music
  - 同じ表の列：Main Genre, Main Location: Regi…, Funding Category, Primary purpose, Main target group, Secondary target gr…, Main artist demogra…, Main artist demogra…

## g0535（1 列）
- 見出し：Main Genre
- 例1 値：Visual Arts | Writing / curating | Contemporary dance | Multi-genre (2 or more genres) | Multi-genre (2 or more genres)
  - 同じ表の列：Artform, Main Location: Regi…, Funding Category, Primary purpose, Main target group, Secondary target gr…, Main artist demogra…, Main artist demogra…

## g0536（1 列）
- 見出し：Main Location: Regional / Metro
- 例1 値：M | M | M | M | M
  - 同じ表の列：Artform, Main Genre, Funding Category, Primary purpose, Main target group, Secondary target gr…, Main artist demogra…, Main artist demogra…

## g0537（1 列）
- 見出し：Funding Category
- 例1 値：Key Organisations | Key Organisations | Key Organisations | Key Organisations | Key Organisations
  - 同じ表の列：Artform, Main Genre, Main Location: Regi…, Primary purpose, Main target group, Secondary target gr…, Main artist demogra…, Main artist demogra…

## g0538（1 列）
- 見出し：Primary purpose
- 例1 値：Core funding | Publication | Sector development | Core funding | Core funding
  - 同じ表の列：Artform, Main Genre, Main Location: Regi…, Funding Category, Main target group, Secondary target gr…, Main artist demogra…, Main artist demogra…

## g0539（1 列）
- 見出し：Main target group
- 例1 値：No specific group | Culturally and linguistically diverse p… | No specific group | Aboriginal communities (including Abori… | Remote or Regional communities
  - 同じ表の列：Artform, Main Genre, Main Location: Regi…, Funding Category, Primary purpose, Secondary target gr…, Main artist demogra…, Main artist demogra…

## g0540（1 列）
- 見出し：Secondary target group
- 例1 値：No specific group | Young People | Older People | Young People | Emerging artists
  - 同じ表の列：Artform, Main Genre, Main Location: Regi…, Funding Category, Primary purpose, Main target group, Main artist demogra…, Main artist demogra…

## g0541（1 列）
- 見出し：Main artist demographic
- 例1 値：No specific group | Aboriginal communities (including Abori… | No specific group | No specific group | Aboriginal communities (including Abori…
  - 同じ表の列：Artform, Main Genre, Main Location: Regi…, Funding Category, Primary purpose, Main target group, Secondary target gr…, Main artist demogra…

## g0542（1 列）
- 見出し：Main artist demographic role
- 例1 値：Paid professional involvement | Artistic control | Paid professional involvement | Paid professional involvement | Artistic control
  - 同じ表の列：Artform, Main Genre, Main Location: Regi…, Funding Category, Primary purpose, Main target group, Secondary target gr…, Main artist demogra…

## g0543（1 列）
- 見出し：City
- 例1 値：BARTON | Braddon | WOOLLOOMOOLOO | SOUTH BRISBANE | UNIVERSITY OF ADELAIDE
  - 同じ表の列：Artform, Main Genre, Main Location: Regi…, Funding Category, Primary purpose, Main target group, Secondary target gr…, Main artist demogra…

## g0544（2 列）
- 見出し：Month
- 例1 値：Dec-23 | Jul-21 | Sep-18 | Jul-14 | May-13
  - 同じ表の列：Number of transitio…, Number of non-trans…, Number of transacti…, Total number of tra…, Number of transacti…, Number of transacti…, Number of transacti…, Number of transacti…
- 例2 値：Apr-04 | Apr-04 | Feb-04 | Jan-04 | Jan-04
  - 同じ表の列：Route, Departing_Port, Arriving_Port, Airline, Sectors_Scheduled, Sectors_Flown, Cancellations, Departures_On_Time

## g0545（1 列）
- 見出し：Number of transitional registrations created
- 例1 値：2427 | 1987 | 1543 | 238 | 133
  - 同じ表の列：Month, Number of non-trans…, Number of transacti…, Total number of tra…, Number of transacti…, Number of transacti…, Number of transacti…, Number of transacti…

## g0546（1 列）
- 見出し：Number of non-transitional registrations created
- 例1 値：119314 | 179343 | 156843 | 139789 | 153091
  - 同じ表の列：Month, Number of transitio…, Number of transacti…, Total number of tra…, Number of transacti…, Number of transacti…, Number of transacti…, Number of transacti…

## g0547（1 列）
- 見出し：Number of transactions to create registrations for Web UI ac
- 例1 値：57587 | 32868 | 48726 | 33758 | 43925
  - 同じ表の列：Month, Number of transitio…, Number of non-trans…, Total number of tra…, Number of transacti…, Number of transacti…, Number of transacti…, Number of transacti…

## g0548（1 列）
- 見出し：Total number of transactions to create registrations (financ
- 例1 値：120865 | 199247 | 181467 | 146424 | 163446
  - 同じ表の列：Month, Number of transitio…, Number of non-trans…, Number of transacti…, Number of transacti…, Number of transacti…, Number of transacti…, Number of transacti…

## g0549（1 列）
- 見出し：Number of transactions to amend registrations: change regist
- 例1 値：10504 | 14789 | 30901 | 19426 | 55494
  - 同じ表の列：Month, Number of transitio…, Number of non-trans…, Number of transacti…, Total number of tra…, Number of transacti…, Number of transacti…, Number of transacti…

## g0550（1 列）
- 見出し：Number of transactions to amend registrations: transfer all
- 例1 値：5533 | 5532 | 1060 | 88683 | 7235
  - 同じ表の列：Month, Number of transitio…, Number of non-trans…, Number of transacti…, Total number of tra…, Number of transacti…, Number of transacti…, Number of transacti…

## g0551（1 列）
- 見出し：Number of transactions to amend registrations: transfer mult
- 例1 値：258 | 2 | 785 | 100 | 625
  - 同じ表の列：Month, Number of transitio…, Number of non-trans…, Number of transacti…, Total number of tra…, Number of transacti…, Number of transacti…, Number of transacti…

## g0552（1 列）
- 見出し：Number of transactions to amend registrations: transfer Sing
- 例1 値：959 | 2221 | 3145 | 791 | 1248
  - 同じ表の列：Month, Number of transitio…, Number of non-trans…, Number of transacti…, Total number of tra…, Number of transacti…, Number of transacti…, Number of transacti…

## g0553（1 列）
- 見出し：Total number of transactions to amend registrations (financi
- 例1 値：120016 | 35108 | 342869 | 257926 | 158095
  - 同じ表の列：Month, Number of transitio…, Number of non-trans…, Number of transacti…, Total number of tra…, Number of transacti…, Number of transacti…, Number of transacti…

## g0554（1 列）
- 見出し：FISHERY
- 例1 値：CSF | CSF | CSF | CTS | CSF
  - 同じ表の列：YEAR, CAAB, RETAINED_CATCH_KG, CATCH_RESEARCH_KG, DATA_SOURCE

## g0555（1 列）
- 見出し：CAAB
- 例1 値：37445001 | 37017003 | 37441001 | 37346038 | 37384007
  - 同じ表の列：FISHERY, YEAR, RETAINED_CATCH_KG, CATCH_RESEARCH_KG, DATA_SOURCE

## g0556（1 列）
- 見出し：RETAINED_CATCH_KG
- 例1 値：1 | 104.5 | 76 | 19 | 3
  - 同じ表の列：FISHERY, YEAR, CAAB, CATCH_RESEARCH_KG, DATA_SOURCE

## g0557（1 列）
- 見出し：CATCH_RESEARCH_KG
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：FISHERY, YEAR, CAAB, RETAINED_CATCH_KG, DATA_SOURCE

## g0558（1 列）
- 見出し：DATA_SOURCE
- 例1 値：CDR | CDR | CDR | CDR | CDR
  - 同じ表の列：FISHERY, YEAR, CAAB, RETAINED_CATCH_KG, CATCH_RESEARCH_KG

## g0559（1 列）
- 見出し：waypoint
- 例1 値：L071 | L077 | L125 | L009 | L060
  - 同じ表の列：distance, leg_length, course

## g0560（1 列）
- 見出し：distance
- 例1 値：10.4 | 172.4 | 116.2 | 18.4 | 322.5
  - 同じ表の列：waypoint, leg_length, course

## g0561（1 列）
- 見出し：leg_length
- 例1 値：2.0 km | 2.0 km | 621 m | 3.6 km | 2.4 km
  - 同じ表の列：waypoint, distance, course

## g0562（1 列）
- 見出し：course
- 例1 値：318° true | 14° true | 209° true | 235° true | 288° true
  - 同じ表の列：waypoint, distance, leg_length

## g0563（1 列）
- 見出し：Question
- 例1 値：17 | 18 | 8 | 20 | 6
  - 同じ表の列：Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0564（1 列）
- 見出し：Question_Text
- 例1 値：Marriage should only be between a man a… | How much government regulation should t… | Trade unions have too much power in the… | Private health insurance rebates should… | How much should the federal government …
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0565（1 列）
- 見出し：category1_definition_1
- 例1 値：Strongly disagree | Much Less | Much Less | Strongly disagree | Strongly disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0566（1 列）
- 見出し：category1_definition_2
- 例1 値：Somewhat disagree | Somewhat Less | Somewhat disagree | Somewhat disagree | Somewhat fewer
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0567（1 列）
- 見出し：category1_definition_3
- 例1 値：About the same as now | Neutral | About the same as now | Neutral | About the same as now
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0568（1 列）
- 見出し：category1_definition_4
- 例1 値：Somewhat agree | Somewhat agree | Somewhat agree | Somewhat agree | Somewhat agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0569（1 列）
- 見出し：category1_definition_5
- 例1 値：Much more | Strongly agree | Much more | Much more | Strongly agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0570（1 列）
- 見出し：category1_definition_DK
- 例1 値：Dont Know | Dont Know | Dont Know | Dont Know | Dont Know
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0571（2 列）
- 見出し：pcode
- 例1 値：36121 | 48916 | 48916 | 30462 | 48495
  - 同じ表の列：regno, regdate
- 例2 値：4034 | 4570 | 4490 | 4101 | 4740
  - 同じ表の列：Display Date, Times(s), Suburb, Event Type, Display Type

## g0572（1 列）
- 見出し：regno
- 例1 値：1205 | 0401 | 0506 | 0209 | 0201
  - 同じ表の列：pcode, regdate

## g0573（1 列）
- 見出し：regdate
- 例1 値：9/01/2001 12:00:00 AM | 14/11/2013 12:00:00 AM | 16/06/2011 12:00:00 AM | 27/03/1997 12:00:00 AM | 20/02/2002 12:00:00 AM
  - 同じ表の列：pcode, regno

## g0574（1 列）
- 見出し：State / Territory
- 例1 値：NSW | ACT | NT | NT | ACT
  - 同じ表の列：Occupations, Number of individua…, Salary or wages no., Salary or wages $, Total Income or Los…, Total Income or Los…, Total work related …, Total work related …

## g0575（1 列）
- 見出し：Occupations
- 例1 値：3223 Structural Steel and Welding Trade… | 2541 Midwives | 4111 Ambulance Officers and Paramedics | 8993 Handypersons | 3996 Signwriters
  - 同じ表の列：State / Territory, Number of individua…, Salary or wages no., Salary or wages $, Total Income or Los…, Total Income or Los…, Total work related …, Total work related …

## g0576（1 列）
- 見出し：Number of individuals
- 例1 値：49 | 80 | 10431 | 1196 | 6150
  - 同じ表の列：State / Territory, Occupations, Salary or wages no., Salary or wages $, Total Income or Los…, Total Income or Los…, Total work related …, Total work related …

## g0577（1 列）
- 見出し：Salary or wages no.
- 例1 値：9023 | 9 | 822 | 3906 | 491
  - 同じ表の列：State / Territory, Occupations, Number of individua…, Salary or wages $, Total Income or Los…, Total Income or Los…, Total work related …, Total work related …

## g0578（1 列）
- 見出し：Salary or wages $
- 例1 値：8150003 | 13934267 | 1590225 | 103540052 | 51052550
  - 同じ表の列：State / Territory, Occupations, Number of individua…, Salary or wages no., Total Income or Los…, Total Income or Los…, Total work related …, Total work related …

## g0579（1 列）
- 見出し：Total Income or Loss3 no.
- 例1 値：100 | 639 | 17 | 130 | 73
  - 同じ表の列：State / Territory, Occupations, Number of individua…, Salary or wages no., Salary or wages $, Total Income or Los…, Total work related …, Total work related …

## g0580（1 列）
- 見出し：Total Income or Loss3 $
- 例1 値：12636308 | 4707258 | 991196660 | 59384025 | 244212513
  - 同じ表の列：State / Territory, Occupations, Number of individua…, Salary or wages no., Salary or wages $, Total Income or Los…, Total work related …, Total work related …

## g0581（1 列）
- 見出し：Total work related expenses no.
- 例1 値：1046 | 197 | 72642 | 754 | 503
  - 同じ表の列：State / Territory, Occupations, Number of individua…, Salary or wages no., Salary or wages $, Total Income or Los…, Total Income or Los…, Total work related …

## g0582（1 列）
- 見出し：Total work related expenses $
- 例1 値：209454 | 28300 | 1054404 | 117114 | 11332082
  - 同じ表の列：State / Territory, Occupations, Number of individua…, Salary or wages no., Salary or wages $, Total Income or Los…, Total Income or Los…, Total work related …

## g0583（1 列）
- 見出し：Gifts or donations no.
- 例1 値：4 | 1491 | 2359 | 37 | 35
  - 同じ表の列：State / Territory, Occupations, Number of individua…, Salary or wages no., Salary or wages $, Total Income or Los…, Total Income or Los…, Total work related …

## g0584（1 列）
- 見出し：Route
- 例1 値：Sunshine Coast-Melbourne | Melbourne-Sunshine Coast | Newcastle-Melbourne | Newcastle-Melbourne | Adelaide-Brisbane
  - 同じ表の列：Departing_Port, Arriving_Port, Airline, Month, Sectors_Scheduled, Sectors_Flown, Cancellations, Departures_On_Time

## g0585（1 列）
- 見出し：Departing_Port
- 例1 値：Launceston | Perth | Brisbane | Coffs Harbour | Sydney
  - 同じ表の列：Route, Arriving_Port, Airline, Month, Sectors_Scheduled, Sectors_Flown, Cancellations, Departures_On_Time

## g0586（1 列）
- 見出し：Arriving_Port
- 例1 値：Melbourne | Sydney | Hobart | Brisbane | Cairns
  - 同じ表の列：Route, Departing_Port, Airline, Month, Sectors_Scheduled, Sectors_Flown, Cancellations, Departures_On_Time

## g0587（1 列）
- 見出し：Airline
- 例1 値：All Airlines | QantasLink | QantasLink | Virgin Australia | All Airlines
  - 同じ表の列：Route, Departing_Port, Arriving_Port, Month, Sectors_Scheduled, Sectors_Flown, Cancellations, Departures_On_Time

## g0588（1 列）
- 見出し：Sectors_Scheduled
- 例1 値：87 | 303 | 31 | 165 | 146
  - 同じ表の列：Route, Departing_Port, Arriving_Port, Airline, Month, Sectors_Flown, Cancellations, Departures_On_Time

## g0589（1 列）
- 見出し：Sectors_Flown
- 例1 値：159 | 112 | 7205 | 17 | 30
  - 同じ表の列：Route, Departing_Port, Arriving_Port, Airline, Month, Sectors_Scheduled, Cancellations, Departures_On_Time

## g0590（1 列）
- 見出し：Cancellations
- 例1 値：2 | 0 | 0 | 0 | 1
  - 同じ表の列：Route, Departing_Port, Arriving_Port, Airline, Month, Sectors_Scheduled, Sectors_Flown, Departures_On_Time

## g0591（1 列）
- 見出し：Departures_On_Time
- 例1 値：147 | 167 | 42 | 56 | 56
  - 同じ表の列：Route, Departing_Port, Arriving_Port, Airline, Month, Sectors_Scheduled, Sectors_Flown, Cancellations

## g0592（1 列）
- 見出し：Arrivals_On_Time
- 例1 値：26 | 678 | 256 | 29 | 239
  - 同じ表の列：Route, Departing_Port, Arriving_Port, Airline, Month, Sectors_Scheduled, Sectors_Flown, Cancellations

## g0593（1 列）
- 見出し：title
- 例1 値：SunSmart app | Australian Climate Observations Referen… | e-Atlas | Drought Statement | Royal Australian Navy Australian Hydrog…
  - 同じ表の列：id, blurb, custodian, active, tags

## g0594（1 列）
- 見出し：blurb
- 例1 値：This website provides information about… | The AGOS infrastructure will enable col… | This publication provides detailed info… | Seasonal climatic outlooks are produced… | Frost potential maps show forecast low …
  - 同じ表の列：id, title, custodian, active, tags

## g0595（1 列）
- 見出し：custodian
- 例1 値：<a href="http://www.bom.gov.au/">BoM</a> | <a href="http://www.abs.gov.au/">ABS</a> | <a href="http://www.abs.gov.au/">ABS</a> | <a href="http://www.defence.gov.au/">De… | <a href="http://ga.gov.au/">GA</a>
  - 同じ表の列：id, title, blurb, active, tags

## g0596（1 列）
- 見出し：active
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：id, title, blurb, custodian, tags

## g0597（1 列）
- 見出し：tags
- 例1 値：Land,Water,Aquatic and estuarine commun… | Land,Marine,Cultural sites,Administrati… | Air,Climate,Natural hazards,Bureau of M… | Marine,Climate,Oceanography,Bureau of M… | Land,Land use,Land management,Land cove…
  - 同じ表の列：id, title, blurb, custodian, active

## g0598（1 列）
- 見出し：Council_ID
- 例1 値：36943 | 38031 | 36532 | 36815 | 36686
  - 同じ表の列：Site, Type, Accessible, Ambulant, DDA_Access, DoorsAuto, SocialUse, Lat

## g0599（1 列）
- 見出し：Site
- 例1 値：Charles Edward Brown Reserve | Ballarat Showgrounds | Lake Learmonth | Lake Wendouree Reserve | Miners Rest Reserve
  - 同じ表の列：Council_ID, Type, Accessible, Ambulant, DDA_Access, DoorsAuto, SocialUse, Lat

## g0600（1 列）
- 見出し：Type
- 例1 値：B-Public Toilet | B-Public Toilet | B-Public Toilet | B-Public Toilet | B-Public Toilet
  - 同じ表の列：Council_ID, Site, Accessible, Ambulant, DDA_Access, DoorsAuto, SocialUse, Lat

## 答えの雛形

```
g0481	
g0482	
g0483	
g0484	
g0485	
g0486	
g0487	
g0488	
g0489	
g0490	
g0491	
g0492	
g0493	
g0494	
g0495	
g0496	
g0497	
g0498	
g0499	
g0500	
g0501	
g0502	
g0503	
g0504	
g0505	
g0506	
g0507	
g0508	
g0509	
g0510	
g0511	
g0512	
g0513	
g0514	
g0515	
g0516	
g0517	
g0518	
g0519	
g0520	
g0521	
g0522	
g0523	
g0524	
g0525	
g0526	
g0527	
g0528	
g0529	
g0530	
g0531	
g0532	
g0533	
g0534	
g0535	
g0536	
g0537	
g0538	
g0539	
g0540	
g0541	
g0542	
g0543	
g0544	
g0545	
g0546	
g0547	
g0548	
g0549	
g0550	
g0551	
g0552	
g0553	
g0554	
g0555	
g0556	
g0557	
g0558	
g0559	
g0560	
g0561	
g0562	
g0563	
g0564	
g0565	
g0566	
g0567	
g0568	
g0569	
g0570	
g0571	
g0572	
g0573	
g0574	
g0575	
g0576	
g0577	
g0578	
g0579	
g0580	
g0581	
g0582	
g0583	
g0584	
g0585	
g0586	
g0587	
g0588	
g0589	
g0590	
g0591	
g0592	
g0593	
g0594	
g0595	
g0596	
g0597	
g0598	
g0599	
g0600	
```
