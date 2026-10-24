# ラベル用シート 006 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_006.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0601（2 列）
- 見出し：Bibliographicrecordnumber
- 例1 値：b24117675 | b24066369 | b24139725 | b24172376 | b28366256
  - 同じ表の列：CollectionNumber, Author, CorporateAuthor, Date, Originalphysicalmat…, Subject:Topical
- 例2 値：b27753797 | b27756452 | b27753797 | b27756440 | b27753797
  - 同じ表の列：Captionformaponreco…, URLformap

## g0602（1 列）
- 見出し：CollectionNumber
- 例1 値：BA1994/10-18 | BA1595/10/641 | BA1595/10/640 | BA1595/10/570-571 | BA1595/10/635-636
  - 同じ表の列：Bibliographicrecord…, Author, CorporateAuthor, Date, Originalphysicalmat…, Subject:Topical

## g0603（1 列）
- 見出し：CorporateAuthor
- 例1 値：Tri-Tone Photographics. | Tri-Tone Photographics. | Sivyers. | Risco & Kos. | Foto Abeca.
  - 同じ表の列：Bibliographicrecord…, CollectionNumber, Author, Date, Originalphysicalmat…, Subject:Topical

## g0604（1 列）
- 見出し：Date
- 例1 値：1964 | 1987 | 1974 | 1964 | 1965-1966.
  - 同じ表の列：Bibliographicrecord…, CollectionNumber, Author, CorporateAuthor, Originalphysicalmat…, Subject:Topical

## g0605（1 列）
- 見出し：Originalphysicalmaterial
- 例1 値：1 negative :;1 negative : | 1 negative : | 15 photographic prints : | 2 photographic prints : | 25 photographic prints :
  - 同じ表の列：Bibliographicrecord…, CollectionNumber, Author, CorporateAuthor, Date, Subject:Topical

## g0606（1 列）
- 見出し：Subject:Topical
- 例1 値：High-rise apartment buildings;Architect… | Apartment houses;Architecture;Physical … | Hotels;Online image. | Apartment houses;Flats;Balconies;Archit… | Nightclubs;Online image.
  - 同じ表の列：Bibliographicrecord…, CollectionNumber, Author, CorporateAuthor, Date, Originalphysicalmat…

## g0607（1 列）
- 見出し：tree_id
- 例1 値：E01944 | E03777 | V00516 | E03646 | E05504
  - 同じ表の列：lat, long, feature_id, significan, genus, species, common_nam, area

## g0608（1 列）
- 見出し：feature_id
- 例1 値：R07690/T/V02081 | R05880/T/V01261 | R01490/T/E05511 | R01490/T/E06580 | R01490/T/E06491
  - 同じ表の列：lat, long, tree_id, significan, genus, species, common_nam, area

## g0609（1 列）
- 見出し：significan
- 例1 値：Memorial | Rare | Memorial | Memorial | Habitat
  - 同じ表の列：lat, long, tree_id, feature_id, genus, species, common_nam, area

## g0610（2 列）
- 見出し：species
- 例1 値：Xacerifolia | ficifolia | ficifolia | gomphocephala | acerifolius
  - 同じ表の列：lat, long, tree_id, feature_id, significan, genus, common_nam, area
- 例2 値：neesiana | neesiana | neesiana | trichotoma | neesiana
  - 同じ表の列：zoneid, common, genus, regulation

## g0611（1 列）
- 見出し：common_nam
- 例1 値：London Plane | Red-flowering Gum | Lawson's Cypress | Red-flowering Gum | Carob Tree
  - 同じ表の列：lat, long, tree_id, feature_id, significan, genus, species, area

## g0612（1 列）
- 見出し：area
- 例1 値：R-EE10 | R-EE10 | R-EE5 | R-EE5 | R-EE5
  - 同じ表の列：lat, long, tree_id, feature_id, significan, genus, species, common_nam

## g0613（1 列）
- 見出し：Location
- 例1 値：Point Grey | North Lorne bbq area | Cosy Corner | Voss Carpark | Bells Beach Coastal Reserve
  - 同じ表の列：ID, Suburb, operator, Male, Female, Disable_Male, Disable_Female, Unisex_Disable

## g0614（1 列）
- 見出し：operator
- 例1 値：GORCC | Surf Coast Shire | GORCC | Surf Coast Shire | Surf Coast Shire
  - 同じ表の列：ID, Suburb, Location, Male, Female, Disable_Male, Disable_Female, Unisex_Disable

## g0615（1 列）
- 見出し：Male
- 例1 値：Yes | Yes | No | Yes | Yes
  - 同じ表の列：ID, Suburb, Location, operator, Female, Disable_Male, Disable_Female, Unisex_Disable

## g0616（1 列）
- 見出し：Female
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：ID, Suburb, Location, operator, Male, Disable_Male, Disable_Female, Unisex_Disable

## g0617（1 列）
- 見出し：Disable_Male
- 例1 値：No | Yes | No | Yes | No
  - 同じ表の列：ID, Suburb, Location, operator, Male, Female, Disable_Female, Unisex_Disable

## g0618（1 列）
- 見出し：Disable_Female
- 例1 値：No | Yes | No | No | No
  - 同じ表の列：ID, Suburb, Location, operator, Male, Female, Disable_Male, Unisex_Disable

## g0619（1 列）
- 見出し：Unisex_Disable
- 例1 値：No | No | Yes | Yes | Yes
  - 同じ表の列：ID, Suburb, Location, operator, Male, Female, Disable_Male, Disable_Female

## g0620（1 列）
- 見出し：Regional WMG
- 例1 値：Barwon RWMG | Metropolitan WMG | Grampians RWMG | Gippsland RWMG | Metropolitan WMG
  - 同じ表の列：Service Standard Ca…, Metro Non-metro, Services ID, Type of Service, Reference year, Frequency of service, Primary bin, Percent primary bin

## g0621（1 列）
- 見出し：Service Standard Category
- 例1 値：Rural Township | Outer Metropolitan | Major Provincial | Inner Metropolitan | Outer Metropolitan
  - 同じ表の列：Regional WMG, Metro Non-metro, Services ID, Type of Service, Reference year, Frequency of service, Primary bin, Percent primary bin

## g0622（1 列）
- 見出し：Metro Non-metro
- 例1 値：Metro | Metro | Metro | Non-Metro | Metro
  - 同じ表の列：Regional WMG, Service Standard Ca…, Services ID, Type of Service, Reference year, Frequency of service, Primary bin, Percent primary bin

## g0623（1 列）
- 見出し：Services ID
- 例1 値：2752 | 1083 | 1602 | 620 | 1493
  - 同じ表の列：Regional WMG, Service Standard Ca…, Metro Non-metro, Type of Service, Reference year, Frequency of service, Primary bin, Percent primary bin

## g0624（1 列）
- 見出し：Type of Service
- 例1 値：Hard Waste | Garbage Service | Garbage Service | Green organics regular service | Garbage Service
  - 同じ表の列：Regional WMG, Service Standard Ca…, Metro Non-metro, Services ID, Reference year, Frequency of service, Primary bin, Percent primary bin

## g0625（1 列）
- 見出し：Reference year
- 例1 値：2001-2002 | 2004-2005 | 2001-2002 | 2001-2002 | 2001-2002
  - 同じ表の列：Regional WMG, Service Standard Ca…, Metro Non-metro, Services ID, Type of Service, Frequency of service, Primary bin, Percent primary bin

## g0626（1 列）
- 見出し：Frequency of service
- 例1 値：Weekly | Annual | Weekly | Weekly | Weekly
  - 同じ表の列：Regional WMG, Service Standard Ca…, Metro Non-metro, Services ID, Type of Service, Reference year, Primary bin, Percent primary bin

## g0627（1 列）
- 見出し：Primary bin
- 例1 値：240L | 120L | 240L split Recyclables and Garbage | 80L | 140L
  - 同じ表の列：Regional WMG, Service Standard Ca…, Metro Non-metro, Services ID, Type of Service, Reference year, Frequency of service, Percent primary bin

## g0628（1 列）
- 見出し：Percent primary bin
- 例1 値：100 | 80 | 100 | 100 | 95
  - 同じ表の列：Regional WMG, Service Standard Ca…, Metro Non-metro, Services ID, Type of Service, Reference year, Frequency of service, Primary bin

## g0629（1 列）
- 見出し：Disposal facility type
- 例1 値：Landfill | Landfill | Landfill | Landfill | Landfill
  - 同じ表の列：Regional WMG, Service Standard Ca…, Metro Non-metro, Services ID, Type of Service, Reference year, Frequency of service, Primary bin

## g0630（1 列）
- 見出し：Males 15-24 unemployment rate (%)
- 例1 値：14 | 10.5 | 13.4 | 11.3 | 16.3
  - 同じ表の列：Month, Males 25-34 unemplo…, Males 35-44 unemplo…, Males 45-54 unemplo…, Males 55-64 unemplo…, Males 65 and over u…, Males 15 and over u…, Males 15-64 unemplo…

## g0631（1 列）
- 見出し：Males 25-34 unemployment rate (%)
- 例1 値：4.4 | 6.5 | 3.6 | 5.1 | 4.6
  - 同じ表の列：Month, Males 15-24 unemplo…, Males 35-44 unemplo…, Males 45-54 unemplo…, Males 55-64 unemplo…, Males 65 and over u…, Males 15 and over u…, Males 15-64 unemplo…

## g0632（1 列）
- 見出し：Males 35-44 unemployment rate (%)
- 例1 値：4.1 | 4.7 | 2.5 | 5.7 | 2.9
  - 同じ表の列：Month, Males 15-24 unemplo…, Males 25-34 unemplo…, Males 45-54 unemplo…, Males 55-64 unemplo…, Males 65 and over u…, Males 15 and over u…, Males 15-64 unemplo…

## g0633（1 列）
- 見出し：Males 45-54 unemployment rate (%)
- 例1 値：3.9 | 4.3 | 7.3 | 3.1 | 2.6
  - 同じ表の列：Month, Males 15-24 unemplo…, Males 25-34 unemplo…, Males 35-44 unemplo…, Males 55-64 unemplo…, Males 65 and over u…, Males 15 and over u…, Males 15-64 unemplo…

## g0634（1 列）
- 見出し：Males 55-64 unemployment rate (%)
- 例1 値：3.6 | 6.5 | 12.8 | 2.9 | 3.7
  - 同じ表の列：Month, Males 15-24 unemplo…, Males 25-34 unemplo…, Males 35-44 unemplo…, Males 45-54 unemplo…, Males 65 and over u…, Males 15 and over u…, Males 15-64 unemplo…

## g0635（1 列）
- 見出し：Males 65 and over unemployment rate (%)
- 例1 値：1.6 | 1 | 1.8 | - | 1.8
  - 同じ表の列：Month, Males 15-24 unemplo…, Males 25-34 unemplo…, Males 35-44 unemplo…, Males 45-54 unemplo…, Males 55-64 unemplo…, Males 15 and over u…, Males 15-64 unemplo…

## g0636（1 列）
- 見出し：Males 15 and over unemployment rate (%)
- 例1 値：5 | 4.9 | 6.4 | 5.5 | 5.4
  - 同じ表の列：Month, Males 15-24 unemplo…, Males 25-34 unemplo…, Males 35-44 unemplo…, Males 45-54 unemplo…, Males 55-64 unemplo…, Males 65 and over u…, Males 15-64 unemplo…

## g0637（1 列）
- 見出し：Males 15-64 unemployment rate (%)
- 例1 値：5.8 | 5.1 | 11.9 | 8.3 | 5.8
  - 同じ表の列：Month, Males 15-24 unemplo…, Males 25-34 unemplo…, Males 35-44 unemplo…, Males 45-54 unemplo…, Males 55-64 unemplo…, Males 65 and over u…, Males 15 and over u…

## g0638（1 列）
- 見出し：UID
- 例1 値：23 | 146 | 264 | 8 | 267
  - 同じ表の列：Type, Size, Enclosure, Lat, Lon

## g0639（1 列）
- 見出し：Type
- 例1 値：Multi-use (waste/recycling) | Waste | Waste | Waste | Waste
  - 同じ表の列：UID, Size, Enclosure, Lat, Lon

## g0640（1 列）
- 見出し：Size
- 例1 値：240L | 240L | 240L | 120L | 240L
  - 同じ表の列：UID, Type, Enclosure, Lat, Lon

## g0641（1 列）
- 見出し：Enclosure
- 例1 値：Green Enclosure | Wheelie Bin Single Stand | Wheelie Bin Single Stand | Wheelie Bin Single Stand | Green Enclosure
  - 同じ表の列：UID, Type, Size, Lat, Lon

## g0642（1 列）
- 見出し：Workplace injury claims
- 例1 値：Income support payments - gross ($) | Return to work costs** | Fatalities | Total new workplace injury claims** | Seriously injured workers*
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0643（1 列）
- 見出し：2024-25
- 例1 値：0 | 0 | 3 | 6.4 | 1,999,009
  - 同じ表の列：Workplace injury cl…, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0644（1 列）
- 見出し：2023-24
- 例1 値：45 | 229,042 | 25 | 1,735,369 | 0
  - 同じ表の列：Workplace injury cl…, 2024-25, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0645（1 列）
- 見出し：2022-23
- 例1 値：475,001 | 5.8 | 1,953,478 | 0 | 2
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0646（1 列）
- 見出し：2021-22
- 例1 値：350,190 | 0 | 0 | 35 | 4
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2020-21, 2019-20, 2018-19, 2017-18

## g0647（1 列）
- 見出し：2020-21
- 例1 値：0 | 0 | 0 | 232,937 | 4
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2021-22, 2019-20, 2018-19, 2017-18

## g0648（1 列）
- 見出し：2019-20
- 例1 値：261,841 | 2 | 5.2 | 0 | 0
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2018-19, 2017-18

## g0649（1 列）
- 見出し：2018-19
- 例1 値：1 | 1 001 790 | 2.27 | 3 | 167 864
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2017-18

## g0650（1 列）
- 見出し：2017-18
- 例1 値：0 | 6.36 | 0 | 376 955 | 0
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19

## g0651（1 列）
- 見出し：2016-17
- 例1 値：1 104 518 | 8 | 0 | 3.98 | 0
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19

## g0652（1 列）
- 見出し：Group Code
- 例1 値：CSNoise | CSOdour | CSStrtFurn | CSTree | CSPrkIrig
  - 同じ表の列：Category Code, Year, Month, Date, Request Count

## g0653（1 列）
- 見出し：Category Code
- 例1 値：CSAttack | CSWBNpr | CSVegCoast | CSWtrLSv | CSTraf&Rds
  - 同じ表の列：Group Code, Year, Month, Date, Request Count

## g0654（2 列）
- 見出し：Month
- 例1 値：10 | 11 | 9 | 8 | 10
  - 同じ表の列：Group Code, Category Code, Year, Date, Request Count
- 例2 値：9 | 6 | 5 | 6 | 2
  - 同じ表の列：Year, Metropolitan train, Metropolitan tram, Metropolitan bus, V/Line train, V/Line coach, Regional bus

## g0655（2 列）
- 見出し：Date
- 例1 値：2018-08-01 00:00:00 | 2018-09-01 00:00:00 | 2018-09-01 00:00:00 | 2018-10-01 00:00:00 | 2018-07-01 00:00:00
  - 同じ表の列：Group Code, Category Code, Year, Month, Request Count
- 例2 値：2015-10-15 00:00:00 | 2015-10-15 00:00:00 | 2015-10-15 00:00:00 | 2015-10-15 00:00:00 | 2015-10-15 00:00:00
  - 同じ表の列：SurveyProgram, SurvYear, Band, Number, SubNumber, Combo, Fx_Group, SppCode

## g0656（1 列）
- 見出し：Request Count
- 例1 値：14 | 2 | 5 | 29 | 57
  - 同じ表の列：Group Code, Category Code, Year, Month, Date

## g0657（1 列）
- 見出し：Contractor
- 例1 値：Communikate | Frame Creative Pty Ltd | Miranda Brown Publicity | MacLeay Williams | ASP Computers
  - 同じ表の列：Purpose, Value

## g0658（1 列）
- 見出し：Purpose
- 例1 値：Legal services | PR Services | Web design | CRM Support and Implementation | Design Services
  - 同じ表の列：Contractor, Value

## g0659（1 列）
- 見出し：Value
- 例1 値：Total value of 'Commercial in confidenc… | $0 (Commercial in confidence) | $0 (Commercial in confidence) | $100,257 | $0 (Commercial in confidence)
  - 同じ表の列：Contractor, Purpose

## g0660（3 列）
- 見出し：_id
- 例1 値：5 | 4 | 3 | 1 | 2
  - 同じ表の列：Library, Wireless sessions, Wireless downloads …
- 例2 値：4 | 1 | 7 | 2 | 5
  - 同じ表の列：Contractors, 2015-16*, 2016-17*, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0661（2 列）
- 見出し：Library
- 例1 値：Point Cook | Plaza | Werribee | Wyndham Vale | Julia Gillard Library Tarneit
  - 同じ表の列：_id, Wireless sessions, Wireless downloads …
- 例2 値：Werribee | Wyndham Vale | Point Cook | Julia Gillard Library Tarneit | Plaza
  - 同じ表の列：_id, Door Counter

## g0662（1 列）
- 見出し：Wireless sessions
- 例1 値：74680 | 28137 | 11632 | 25384 | 50196
  - 同じ表の列：_id, Library, Wireless downloads …

## g0663（1 列）
- 見出し：Wireless downloads (gb)
- 例1 値：2324.105 | 8596.91 | 7758.08 | 4547.51 | 2807.15
  - 同じ表の列：_id, Library, Wireless sessions

## g0664（1 列）
- 見出し：Town
- 例1 値：MINYIP | YAAPEET | RUPANYUP | PATCHEWOLLOCK | MURTOA
  - 同じ表の列：Lon, Lat, Organisation

## g0665（1 列）
- 見出し：Organisation
- 例1 値：Woobine Inc | Hopetoun Football/Netball Club | Speed Lions Club | Warracknabeal Golf Club | Rural Northwest Health - Beulah Campus
  - 同じ表の列：Lon, Lat, Town

## g0666（1 列）
- 見出し：Reporting date
- 例1 値：2016-02-29T00:00:00 | 2010-04-30T00:00:00 | 2007-03-30T00:00:00 | 2009-02-27T00:00:00 | 2006-03-31T00:00:00
  - 同じ表の列：loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…

## g0667（1 列）
- 見出し：loans_to_households_for_house_purchase__interest_rate____
- 例1 値：3.51 | 3.34 | 3.38 | 3.06 | 3.37
  - 同じ表の列：Reporting date, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…

## g0668（1 列）
- 見出し：loans_to_households_for_house_purchase__o_w_new_lending_ex__
- 例1 値：3.97 | 4.04 | .. | .. | ..
  - 同じ表の列：Reporting date, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…

## g0669（1 列）
- 見出し：loans_to_households_for_house_purchase__floating_rate_and_up
- 例1 値：4.13 | 3.3 | 3.03 | 3.19 | 3.16
  - 同じ表の列：Reporting date, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…

## g0670（1 列）
- 見出し：loans_to_households_for_house_purchase__floating_rate_and_up
- 例1 値：3.21 | 3.38 | 3.42 | 3.26 | ..
  - 同じ表の列：Reporting date, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…

## g0671（1 列）
- 見出し：loans_to_households_for_house_purchase__over_1_year_fixation
- 例1 値：2.62 | 2.7 | 4.37 | 4.42 | 3.72
  - 同じ表の列：Reporting date, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…

## g0672（1 列）
- 見出し：loans_to_households_for_house_purchase__over_1_year_fixation
- 例1 値：.. | 4.03 | 3.5 | .. | 3.41
  - 同じ表の列：Reporting date, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…

## g0673（1 列）
- 見出し：loans_to_households_for_house_purchase__aprc__interest_rate_
- 例1 値：2.93 | 2.81 | 2.86 | 3.5 | 2.97
  - 同じ表の列：Reporting date, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…

## g0674（1 列）
- 見出し：loans_to_households__for_consumer_purposes__interest_rate___
- 例1 値：6.65 | 8.19 | 6.57 | 7.3 | 6.24
  - 同じ表の列：Reporting date, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…

## g0675（1 列）
- 見出し：loans_to_households__for_consumer_purposes__floating_rate_an
- 例1 値：8.05 | 7.6 | 6.62 | 5.03 | 3.65
  - 同じ表の列：Reporting date, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…, loans_to_households…

## g0676（1 列）
- 見出し：JH
- 例1 値：PRC | RTV0 | JH | JF | COL
  - 同じ表の列：table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0677（1 列）
- 見出し：table_1_1_amarach_research___online_s22163
- 例1 値：OC | PREPARED 03 February 2023 | Income / Securing funding | Between 20,001 and 50,000 | My charity has not changed how it fundr…
  - 同じ表の列：JH, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0678（1 列）
- 見出し：unsafe_
- 例1 値：899 | TOTAL | 6% | 31% | 9%
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0679（1 列）
- 見出し：unsafe__2
- 例1 値：83% | 24% | 25 | 6% | 296
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0680（1 列）
- 見出し：unsafe__3
- 例1 値：6% | 47 | 100% | 28% | 1
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0681（1 列）
- 見出し：unsafe__4
- 例1 値：10 | 2% | 0 | 19 | 88
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__5, unsafe__6, unsafe__7

## g0682（1 列）
- 見出し：unsafe__5
- 例1 値：33% | 0 | 0 | 3 | 7
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__6, unsafe__7

## g0683（1 列）
- 見出し：unsafe__6
- 例1 値：Yes | 4% | 9% | 23 | 6%
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__7

## g0684（1 列）
- 見出し：unsafe__7
- 例1 値：68 | 2% | 3 | 11 | 1%
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6

## g0685（2 列）
- 見出し：unsafe__8
- 例1 値：22 | 36 | 33 | 13 | 232
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6
- 例2 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：unsafe_, unsafe__2, unprotect cafo, unsafe__3, unsafe__4, unsafe__5, unsafe__6, Munster

## g0686（1 列）
- 見出し：Administrative_Authority
- 例1 値：Cork City Council | Cork City Council | Cork City Council | Cork City Council | Cork City Council
  - 同じ表の列：OBJECTID, Town, Eircode, County, Services_Available, Website, Opening_Hours_Monday, Opening_Hours_Tuesd…

## g0687（1 列）
- 見出し：Town
- 例1 値：Cork | Cork | Cork | Cork | Co. Cork
  - 同じ表の列：OBJECTID, Administrative_Auth…, Eircode, County, Services_Available, Website, Opening_Hours_Monday, Opening_Hours_Tuesd…

## g0688（1 列）
- 見出し：Eircode
- 例1 値：T12WP57 | T23N250 | T45E033 | T12NT99 | T23E651
  - 同じ表の列：OBJECTID, Administrative_Auth…, Town, County, Services_Available, Website, Opening_Hours_Monday, Opening_Hours_Tuesd…

## g0689（2 列）
- 見出し：County
- 例1 値：Cork | Cork | Cork | Cork | Cork
  - 同じ表の列：OBJECTID, Administrative_Auth…, Town, Eircode, Services_Available, Website, Opening_Hours_Monday, Opening_Hours_Tuesd…
- 例2 値：Donegal | Tipperary | Meath | All | Donegal
  - 同じ表の列：period, programme, scheme, basis, county_code, recipients

## g0690（1 列）
- 見出し：Services_Available
- 例1 値：Internet, Wifi, Public Access PCs, Phot… | Internet, Wifi, Public Access PCs, | Internet, Wifi, Public Access PCs | Internet, Wifi, Public Access | Internet, Wifi, Public Access PCs
  - 同じ表の列：OBJECTID, Administrative_Auth…, Town, Eircode, County, Website, Opening_Hours_Monday, Opening_Hours_Tuesd…

## g0691（2 列）
- 見出し：Website
- 例1 値：https://www.corkcitylibraries.ie/en/loc… | https://www.corkcitylibraries.ie/en/loc… | https://www.corkcitylibraries.ie/en/loc… | https://www.corkcitylibraries.ie/en/loc… | https://www.corkcitylibraries.ie/en/loc…
  - 同じ表の列：OBJECTID, Administrative_Auth…, Town, Eircode, County, Services_Available, Opening_Hours_Monday, Opening_Hours_Tuesd…
- 例2 値：https://www.corkcity.ie/corkcityco/en/t… | https://www.corkcity.ie/corkcityco/en/t… | https://www.corkcity.ie/corkcityco/en/t… | https://www.corkcity.ie/corkcityco/en/t… | https://www.corkcity.ie/corkcityco/en/t…
  - 同じ表の列：OBJECTID, Type, MUGA

## g0692（1 列）
- 見出し：Opening_Hours_Monday
- 例1 値：Closed | Closed | Closed | 10.00 a.m. to 5.30 p.m | Closed
  - 同じ表の列：OBJECTID, Administrative_Auth…, Town, Eircode, County, Services_Available, Website, Opening_Hours_Tuesd…

## g0693（1 列）
- 見出し：Opening_Hours_Tuesday
- 例1 値：10.00 a.m. - 5.30 p.m | 10.00 a.m. – 1.00 p.m., 2.00 p.m. – 5.3… | 10.00 a.m. - 8.00 p.m | 9:30am-5:30pm | Closed
  - 同じ表の列：OBJECTID, Administrative_Auth…, Town, Eircode, County, Services_Available, Website, Opening_Hours_Monday

## g0694（1 列）
- 見出し：Opening_Hours_Wednesday
- 例1 値：10.00 a.m. to 5.30 p.m | 10.00 a.m. – 1.00 p.m., 2.00 p.m. – 5.3… | 10.00 a.m. - 5.30 p.m, 10.30 a.m. on th… | 10.00am - 1.00pm ., 2.00pm - 5.30pm | 10:00 a.m. – 1:00 p.m., 2:00 p.m. – 5:3…
  - 同じ表の列：OBJECTID, Administrative_Auth…, Town, Eircode, County, Services_Available, Website, Opening_Hours_Monday

## g0695（1 列）
- 見出し：WEEK_NO
- 例1 値：45 | 51 | 14 | 30 | 8
  - 同じ表の列：YEAR, DATE, CLASSIFICATION_CATE…, ANIMAL_CARCASE, NUMBER

## g0696（1 列）
- 見出し：DATE
- 例1 値：2021-10-11T00:00:00 | 2022-07-04T00:00:00 | 2021-11-15T00:00:00 | 2020-08-03T00:00:00 | 2021-05-10T00:00:00
  - 同じ表の列：WEEK_NO, YEAR, CLASSIFICATION_CATE…, ANIMAL_CARCASE, NUMBER

## g0697（1 列）
- 見出し：CLASSIFICATION_CATEOGORY
- 例1 値：D | B | C | V | A
  - 同じ表の列：WEEK_NO, YEAR, DATE, ANIMAL_CARCASE, NUMBER

## g0698（1 列）
- 見出し：ANIMAL_CARCASE
- 例1 値：Steer | Cow | Cow | Steer | Bull
  - 同じ表の列：WEEK_NO, YEAR, DATE, CLASSIFICATION_CATE…, NUMBER

## g0699（4 列）
- 見出し：STATISTIC
- 例1 値：SCA11C02 | SCA11C01 | SCA11C02 | SCA11C01 | SCA11C02
  - 同じ表の列：Statistic, TLIST(A1), Year, C02199V02655, Sex, C02842V03416, HSE Regions, UNIT
- 例2 値：HSQ13C01 | HSQ13C02 | HSQ13C01 | HSQ13C01 | HSQ13C01
  - 同じ表の列：Statistic, TLIST(Q1), Quarter, C01947V02657, Local Authority, UNIT, VALUE

## g0700（1 列）
- 見出し：Statistic
- 例1 値：Children aged 10 - 17 years who present… | Children aged 10 - 17 years who present… | Children aged 10 - 17 years who present… | Children aged 10 - 17 years who present… | Children aged 10 - 17 years who present…
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02199V02655, Sex, C02842V03416, HSE Regions, UNIT

## g0701（5 列）
- 見出し：TLIST(A1)
- 例1 値：2014 | 2016 | 2013 | 2009 | 2014
  - 同じ表の列：STATISTIC, Statistic, Year, C02199V02655, Sex, C02842V03416, HSE Regions, UNIT
- 例2 値：2017 | 2002 | 2014 | 2009 | 2006
  - 同じ表の列：STATISTIC, Statistic, Year, C02351V02955, Type of Educational…, UNIT, VALUE

## g0702（1 列）
- 見出し：C02199V02655
- 例1 値：1 | 1 | 2 | 2 | 2
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Sex, C02842V03416, HSE Regions, UNIT

## g0703（3 列）
- 見出し：Sex
- 例1 値：Male | Male | Both sexes | Male | Male
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, C02842V03416, HSE Regions, UNIT
- 例2 値：Female | Male | Both Sexes | Both Sexes | Female
  - 同じ表の列：period, programme, scheme, basis, sex_code, recipients

## g0704（1 列）
- 見出し：C02842V03416
- 例1 値：-01 | X03 | -01 | -01 | X02
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, HSE Regions, UNIT

## g0705（1 列）
- 見出し：HSE Regions
- 例1 値：Ireland | HSE-West | Ireland | HSE-West | HSE-West
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C02842V03416, UNIT

## g0706（1 列）
- 見出し：UNIT
- 例1 値：Rate per 1,000 Children | Rate per 1,000 Children | Number | Rate per 1,000 Children | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C02842V03416, HSE Regions

## g0707（4 列）
- 見出し：STATISTIC
- 例1 値：EDA41 | EDA41 | EDA41 | EDA41 | EDA41
  - 同じ表の列：Statistic, TLIST(A1), Year, C02351V02955, Type of Educational…, UNIT, VALUE
- 例2 値：IMQ07 | IMQ07 | IMQ07 | IMQ07 | IMQ07
  - 同じ表の列：Statistic, TLIST(Q1), Quarter, C02637V03195, Country, C02638V03194, Type of Traffic, UNIT

## g0708（1 列）
- 見出し：Statistic
- 例1 値：Educational Institutions | Educational Institutions | Educational Institutions | Educational Institutions | Educational Institutions
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02351V02955, Type of Educational…, UNIT, VALUE

## g0709（2 列）
- 見出し：C02351V02955
- 例1 値：12 | 314 | X313 | 211 | 311
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Type of Educational…, UNIT, VALUE
- 例2 値：X313 | 21 | 11 | 313 | 315
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age, C02199V02655, Sex

## g0710（1 列）
- 見出し：Type of Educational Institution
- 例1 値：Aided technology sector | Non-aided commercial second level educa… | Non-aided first level education institu… | Community schools | Community schools
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02351V02955, UNIT, VALUE

## g0711（5 列）
- 見出し：UNIT
- 例1 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02351V02955, Type of Educational…, VALUE
- 例2 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, HOSPSECTOR, Sector, VALUE

## g0712（2 列）
- 見出し：STATISTIC
- 例1 値：HBEDSEC | HBEDSEC | HBEDSEC | HBEDSEC | HBEDSEC
  - 同じ表の列：Statistic Label, YEAR, Year, HOSPSECTOR, Sector, UNIT, VALUE
- 例2 値：HOSPBEDFUNC | HOSPBEDFUNC | HOSPBEDFUNC | HOSPBEDFUNC | HOSPBEDFUNC
  - 同じ表の列：Statistic Label, YEAR, Year, FUNCTION, Type of function, BEDTYPE, Bed type, UNIT

## g0713（1 列）
- 見出し：Statistic Label
- 例1 値：Hospital beds by sector | Hospital beds by sector | Hospital beds by sector | Hospital beds by sector | Hospital beds by sector
  - 同じ表の列：STATISTIC, YEAR, Year, HOSPSECTOR, Sector, UNIT, VALUE

## g0714（1 列）
- 見出し：HOSPSECTOR
- 例1 値：PUB | PRIV | PRIV | PUB | PRIV
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Sector, UNIT, VALUE

## g0715（1 列）
- 見出し：Sector
- 例1 値：Total hospitals | Publicly owned hospitals | Privately owned hospitals | Publicly owned hospitals | Publicly owned hospitals
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, HOSPSECTOR, UNIT, VALUE

## g0716（1 列）
- 見出し：Statistic
- 例1 値：Total Loan Book (Number) | Total Loan Book (Number) | Total Loan Book (Euro) | Total Loan Book (Number) | Total Loan Book (Euro)
  - 同じ表の列：STATISTIC, TLIST(Q1), Quarter, C01947V02657, Local Authority, UNIT, VALUE

## g0717（2 列）
- 見出し：TLIST(Q1)
- 例1 値：20163 | 20172 | 20182 | 20164 | 20171
  - 同じ表の列：STATISTIC, Statistic, Quarter, C01947V02657, Local Authority, UNIT, VALUE
- 例2 値：20072 | 20081 | 20123 | 20102 | 20094
  - 同じ表の列：STATISTIC, Statistic, Quarter, C02637V03195, Country, C02638V03194, Type of Traffic, UNIT

## g0718（3 列）
- 見出し：Quarter
- 例1 値：2017Q3 | 2018Q4 | 2018Q3 | 2017Q1 | 2015Q4
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), C01947V02657, Local Authority, UNIT, VALUE
- 例2 値：2011Q2 | 2009Q4 | 2012Q2 | 2010Q4 | 2008Q3
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), C02637V03195, Country, C02638V03194, Type of Traffic, UNIT

## g0719（1 列）
- 見出し：C01947V02657
- 例1 値：7 | 18 | 2 | 3 | 8
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, Local Authority, UNIT, VALUE

## g0720（1 列）
- 見出し：Local Authority
- 例1 値：Sligo (County Council) | Cavan (County Council) | Clare (County Council) | Roscommon (County Council) | Westmeath (County Council)
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C01947V02657, UNIT, VALUE

## 答えの雛形

```
g0601	
g0602	
g0603	
g0604	
g0605	
g0606	
g0607	
g0608	
g0609	
g0610	
g0611	
g0612	
g0613	
g0614	
g0615	
g0616	
g0617	
g0618	
g0619	
g0620	
g0621	
g0622	
g0623	
g0624	
g0625	
g0626	
g0627	
g0628	
g0629	
g0630	
g0631	
g0632	
g0633	
g0634	
g0635	
g0636	
g0637	
g0638	
g0639	
g0640	
g0641	
g0642	
g0643	
g0644	
g0645	
g0646	
g0647	
g0648	
g0649	
g0650	
g0651	
g0652	
g0653	
g0654	
g0655	
g0656	
g0657	
g0658	
g0659	
g0660	
g0661	
g0662	
g0663	
g0664	
g0665	
g0666	
g0667	
g0668	
g0669	
g0670	
g0671	
g0672	
g0673	
g0674	
g0675	
g0676	
g0677	
g0678	
g0679	
g0680	
g0681	
g0682	
g0683	
g0684	
g0685	
g0686	
g0687	
g0688	
g0689	
g0690	
g0691	
g0692	
g0693	
g0694	
g0695	
g0696	
g0697	
g0698	
g0699	
g0700	
g0701	
g0702	
g0703	
g0704	
g0705	
g0706	
g0707	
g0708	
g0709	
g0710	
g0711	
g0712	
g0713	
g0714	
g0715	
g0716	
g0717	
g0718	
g0719	
g0720	
```
