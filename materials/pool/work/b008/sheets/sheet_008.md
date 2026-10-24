# ラベル用シート 008 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_008.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0841（1 列）
- 見出し：Beach
- 例1 値：Castaways Beach | Noosa Main Beach | Peregian Beach | Sunshine Beach | Noosa Little Cove
  - 同じ表の列：AssetNo, AssetNo_old, AssetType, BeachAccessNo, AccessType, Suburb, DogInfo, AlternativeAccess

## g0842（1 列）
- 見出し：DogInfo
- 例1 値：Dogs allowed off leash 38-47 | Dogs allowed on Leash 59-67 | Dogs Prohibited 27 - 38 | Dogs allowed on Leash 59-67 | Dogs Prohibited 8 - 25
  - 同じ表の列：AssetNo, AssetNo_old, AssetType, BeachAccessNo, AccessType, Suburb, Beach, AlternativeAccess

## g0843（1 列）
- 見出し：AlternativeAccess
- 例1 値：Claude Batten Drive | David Low Way | Park Road | Claude Batten Drive | Claude Batten Drive
  - 同じ表の列：AssetNo, AssetNo_old, AssetType, BeachAccessNo, AccessType, Suburb, Beach, DogInfo

## g0844（1 列）
- 見出し：OldBeachAccessNo
- 例1 値：New | New | M3A | 26 | 3
  - 同じ表の列：AssetNo, AssetNo_old, AssetType, BeachAccessNo, AccessType, Suburb, Beach, DogInfo

## g0845（2 列）
- 見出し：location
- 例1 値：Kempsey | Kempsey | Murwillumbah | Coffs Harbour | Narooma
  - 同じ表の列：epi_week, trap_date, week_ending_saturday, site_type, lat, lon, lga_code_2011, lga_code_2016
- 例2 値：Swan Hill | Nyah | Swan Hill | Swan Hill | Lake Boga
  - 同じ表の列：UID, TYPE, DESC, Road, IMAGE, LAT, LON

## g0846（1 列）
- 見出し：epi_week
- 例1 値：14 | 11 | 11 | 45 | 11
  - 同じ表の列：location, trap_date, week_ending_saturday, site_type, lat, lon, lga_code_2011, lga_code_2016

## g0847（1 列）
- 見出し：trap_date
- 例1 値：7/12/2025 | 5/04/2026 | 1/03/2026 | 21/12/2025 | 8/02/2026
  - 同じ表の列：location, epi_week, week_ending_saturday, site_type, lat, lon, lga_code_2011, lga_code_2016

## g0848（1 列）
- 見出し：week_ending_saturday
- 例1 値：15/11/2025 | 3/01/2026 | 6/12/2025 | 14/02/2026 | 28/03/2026
  - 同じ表の列：location, epi_week, trap_date, site_type, lat, lon, lga_code_2011, lga_code_2016

## g0849（1 列）
- 見出し：site_type
- 例1 値：Coastal | Coastal | Coastal | Coastal | Coastal
  - 同じ表の列：location, epi_week, trap_date, week_ending_saturday, lat, lon, lga_code_2011, lga_code_2016

## g0850（1 列）
- 見出し：lga_code_2011
- 例1 値：14350 | 12750 | 11800 | 14850 | 17550
  - 同じ表の列：location, epi_week, trap_date, week_ending_saturday, site_type, lat, lon, lga_code_2016

## g0851（1 列）
- 見出し：lga_code_2016
- 例1 値：14350 | 14350 | 15900 | 14350 | 11350
  - 同じ表の列：location, epi_week, trap_date, week_ending_saturday, site_type, lat, lon, lga_code_2011

## g0852（1 列）
- 見出し：lhd
- 例1 値：Mid North Coast | Northern NSW | Mid North Coast | Northern NSW | Northern NSW
  - 同じ表の列：location, epi_week, trap_date, week_ending_saturday, site_type, lat, lon, lga_code_2011

## g0853（1 列）
- 見出し：REGISTRATION ID
- 例1 値：10000201 | 4272 | 4237 | 3939 | 10000648
  - 同じ表の列：LAT, LON, Structure Type, Public Organisation, TRU LatLong Verified

## g0854（1 列）
- 見出し：Structure Type
- 例1 値：Fixed Structure - Structural on Water o… | Fixed Structure - Structural on Water o… | Fixed Structure - Petrochemical or Gas … | Fixed Structure - Structural on Water o… | Fixed Structure - Petrochemical or Gas …
  - 同じ表の列：REGISTRATION ID, LAT, LON, Public Organisation, TRU LatLong Verified

## g0855（1 列）
- 見出し：Public Organisation
- 例1 値：Cape Flattery Silica Mines | GLNG Operations Pty Ltd | Sunwater Limited | BM Alliance Coal Operations Pty Ltd | Sunwater Limited
  - 同じ表の列：REGISTRATION ID, LAT, LON, Structure Type, TRU LatLong Verified

## g0856（1 列）
- 見出し：TRU LatLong Verified
- 例1 値：Verified | Verified | Verified | Verified | Verified
  - 同じ表の列：REGISTRATION ID, LAT, LON, Structure Type, Public Organisation

## g0857（1 列）
- 見出し：ICN
- 例1 値：260 | 801 | 140 | 648 | 208
  - 同じ表の列：Status Reason, Registered On, Deregistered On, Corporation Size, ABN, Industry Sector(s), Corporation registe…, 2023 Total Income

## g0858（1 列）
- 見出し：Status Reason
- 例1 値：Deregistered | Deregistered | Registered | Deregistered | Deregistered
  - 同じ表の列：ICN, Registered On, Deregistered On, Corporation Size, ABN, Industry Sector(s), Corporation registe…, 2023 Total Income

## g0859（1 列）
- 見出し：Registered On
- 例1 値：16/03/1989 | 24/04/1989 | 13/02/1990 | 3/02/1987 | 9/10/1984
  - 同じ表の列：ICN, Status Reason, Deregistered On, Corporation Size, ABN, Industry Sector(s), Corporation registe…, 2023 Total Income

## g0860（1 列）
- 見出し：Deregistered On
- 例1 値：27/08/1996 | 9/06/1999 | 8/12/2020 | 30/05/2006 | 12/05/1999
  - 同じ表の列：ICN, Status Reason, Registered On, Corporation Size, ABN, Industry Sector(s), Corporation registe…, 2023 Total Income

## g0861（1 列）
- 見出し：Corporation Size
- 例1 値：Small | Small | Small | Large | Small
  - 同じ表の列：ICN, Status Reason, Registered On, Deregistered On, ABN, Industry Sector(s), Corporation registe…, 2023 Total Income

## g0862（1 列）
- 見出し：Industry Sector(s)
- 例1 値：Other services, Land and waters managem… | Health care and health promotion, Commu… | Education and training > Cultural teach… | Land and waters management?care for Cou… | Health care and health promotion > Drug…
  - 同じ表の列：ICN, Status Reason, Registered On, Deregistered On, Corporation Size, ABN, Corporation registe…, 2023 Total Income

## g0863（1 列）
- 見出し：Corporation registered with ACNC?
- 例1 値：Yes | No | No | No | Yes
  - 同じ表の列：ICN, Status Reason, Registered On, Deregistered On, Corporation Size, ABN, Industry Sector(s), 2023 Total Income

## g0864（1 列）
- 見出し：2023 Total Income
- 例1 値：<$100k | <$100k | $100k-<$5m | <$100k | 0
  - 同じ表の列：ICN, Status Reason, Registered On, Deregistered On, Corporation Size, ABN, Industry Sector(s), Corporation registe…

## g0865（1 列）
- 見出し：2023 Total Assets
- 例1 値：>=$2.5m | 0 | <$100k | 0 | $100k-<$2.5m
  - 同じ表の列：ICN, Status Reason, Registered On, Deregistered On, Corporation Size, ABN, Industry Sector(s), Corporation registe…

## g0866（1 列）
- 見出し：Information
- 例1 値：Always celebrated on 26 January | Public Holiday as part of Easter. | Celebrated on second Monday in June exc… | As 25 December (Christmas Day) falls on… | Always celebrated on 26 January
  - 同じ表の列：ID, Date, More Information, Jurisdiction

## g0867（1 列）
- 見出し：More Information
- 例1 値：https://www.safework.sa.gov.au/resource… | https://www.nsw.gov.au/about-nsw/public… | https://www.safework.sa.gov.au/resource… | https://www.business.vic.gov.au/victori… | https://worksafe.tas.gov.au/topics/laws…
  - 同じ表の列：ID, Date, Information, Jurisdiction

## g0868（1 列）
- 見出し：Jurisdiction
- 例1 値：act | sa | nsw | tas | qld
  - 同じ表の列：ID, Date, Information, More Information

## g0869（1 列）
- 見出し：Government
- 例1 値：Aust Govt | Aust Govt | Aust Govt | Aust Govt | Aust Govt
  - 同じ表の列：Place of exp (State…, Year, Exp code, Direct or Indirect …, Indigenous specific…, Indigenous or non-I…, Component of Indige…, Unit

## g0870（1 列）
- 見出し：Place of exp (State/Territory)
- 例1 値：Vic | NSW | Vic | NSW | WA
  - 同じ表の列：Government, Year, Exp code, Direct or Indirect …, Indigenous specific…, Indigenous or non-I…, Component of Indige…, Unit

## g0871（1 列）
- 見出し：Exp code
- 例1 値：_0990 | _0419b | _1120 | _0431c | _0610.5
  - 同じ表の列：Government, Place of exp (State…, Year, Direct or Indirect …, Indigenous specific…, Indigenous or non-I…, Component of Indige…, Unit

## g0872（1 列）
- 見出し：Direct or Indirect exp
- 例1 値：Direct | Direct | Direct | Direct | Direct
  - 同じ表の列：Government, Place of exp (State…, Year, Exp code, Indigenous specific…, Indigenous or non-I…, Component of Indige…, Unit

## g0873（1 列）
- 見出し：Indigenous specific or Mainstream exp
- 例1 値：Mainstream | Mainstream | Mainstream | Mainstream | Mainstream
  - 同じ表の列：Government, Place of exp (State…, Year, Exp code, Direct or Indirect …, Indigenous or non-I…, Component of Indige…, Unit

## g0874（1 列）
- 見出し：Indigenous or non-Indigenous exp
- 例1 値：Indigenous | Indigenous | Indigenous | Indigenous | Indigenous
  - 同じ表の列：Government, Place of exp (State…, Year, Exp code, Direct or Indirect …, Indigenous specific…, Component of Indige…, Unit

## g0875（1 列）
- 見出し：Component of Indigenous exp
- 例1 値：Service use component | Service use component | Service use component | Service use component | Service use component
  - 同じ表の列：Government, Place of exp (State…, Year, Exp code, Direct or Indirect …, Indigenous specific…, Indigenous or non-I…, Unit

## g0876（1 列）
- 見出し：Unit
- 例1 値：$'000 | $'000 | $'000 | $'000 | $'000
  - 同じ表の列：Government, Place of exp (State…, Year, Exp code, Direct or Indirect …, Indigenous specific…, Indigenous or non-I…, Component of Indige…

## g0877（1 列）
- 見出し：Data
- 例1 値：11775.83114 | 1020.635376 | 225487.9856 | 37145.02189 | 868.1282028
  - 同じ表の列：Government, Place of exp (State…, Year, Exp code, Direct or Indirect …, Indigenous specific…, Indigenous or non-I…, Component of Indige…

## g0878（1 列）
- 見出し：Entity
- 例1 値：Department of Sport and Recreation | Department of State Development | Department of Fisheries | Corruption and Crime Commission | Office of the Auditor General
  - 同じ表の列：Headcount, FTE, Female %, Male %, Female median age, Male median age, Agency median age, Age less than 20

## g0879（1 列）
- 見出し：FTE
- 例1 値：40 | 133 | 127 | 449 | 35696
  - 同じ表の列：Entity, Headcount, Female %, Male %, Female median age, Male median age, Agency median age, Age less than 20

## g0880（1 列）
- 見出し：Female %
- 例1 値：47.00% | 35.00% | 71.70% | 56.90% | 80.30%
  - 同じ表の列：Entity, Headcount, FTE, Male %, Female median age, Male median age, Agency median age, Age less than 20

## g0881（1 列）
- 見出し：Male %
- 例1 値：56.10% | 53.20% | 28.10% | 36.90% | 53.80%
  - 同じ表の列：Entity, Headcount, FTE, Female %, Female median age, Male median age, Agency median age, Age less than 20

## g0882（1 列）
- 見出し：Female median age
- 例1 値：42.7 | 36.6 | 46.4 | 41.1 | 38.3
  - 同じ表の列：Entity, Headcount, FTE, Female %, Male %, Male median age, Agency median age, Age less than 20

## g0883（1 列）
- 見出し：Male median age
- 例1 値：50.8 | 37.5 | 48.3 | 40.7 | 53.2
  - 同じ表の列：Entity, Headcount, FTE, Female %, Male %, Female median age, Agency median age, Age less than 20

## g0884（1 列）
- 見出し：Agency median age
- 例1 値：43.6 | 50.9 | 50.1 | 45.9 | 39
  - 同じ表の列：Entity, Headcount, FTE, Female %, Male %, Female median age, Male median age, Age less than 20

## g0885（1 列）
- 見出し：Age less than 20
- 例1 値：0.90% | 0.30% | 1.70% | 0.00% | 0.20%
  - 同じ表の列：Entity, Headcount, FTE, Female %, Male %, Female median age, Male median age, Agency median age

## g0886（1 列）
- 見出し：Age 20 to 24
- 例1 値：1.90% | 2.80% | 2.30% | 1.00% | 4.80%
  - 同じ表の列：Entity, Headcount, FTE, Female %, Male %, Female median age, Male median age, Agency median age

## g0887（1 列）
- 見出し：Display Date
- 例1 値：Friday, 26 June 2026 | Saturday, 4 July 2026 | Saturday, 4 July 2026 | Saturday, 4 July 2026 | Friday, 26 June 2026
  - 同じ表の列：Times(s), Suburb, PCode, Event Type, Display Type

## g0888（1 列）
- 見出し：Times(s)
- 例1 値：21:00:00 | 14:00:00 | 20:00:00 | 14:00, 15:00 | 14:00, 15:00, 20:00, 21:00
  - 同じ表の列：Display Date, Suburb, PCode, Event Type, Display Type

## g0889（1 列）
- 見出し：Suburb
- 例1 値：STREETS SOUTH BRISBANE | WYNNUM | STREETS SOUTH BRISBANE | MALANDA | Boondall
  - 同じ表の列：Display Date, Times(s), PCode, Event Type, Display Type

## g0890（2 列）
- 見出し：Event Type
- 例1 値：PUBLIC | PUBLIC | PRIVATE | Public | Public
  - 同じ表の列：Display Date, Times(s), Suburb, PCode, Display Type
- 例2 値：Event | Event | Event | Event | Festival
  - 同じ表の列：County, Is Free To Visit, Price, Start Date, End Date, Start Time, End Time, Recurring Dates

## g0891（1 列）
- 見出し：Display Type
- 例1 値：Outdoor Displays | Outdoor Display | Outdoor Displays | Close Proximity | Close Proximity
  - 同じ表の列：Display Date, Times(s), Suburb, PCode, Event Type

## g0892（1 列）
- 見出し：Month of Processing
- 例1 値：August | August | August | August | August
  - 同じ表の列：Year, Group, Sub-Group, Item Number, State, Services, Benefit

## g0893（1 列）
- 見出し：Group
- 例1 値：A8 Consultant Psychiatrist | A28 Geriatric Medicine | A7 Acupuncture and Non-Specialist Pract… | A8 Consultant Psychiatrist | A7 Acupuncture and Non-Specialist Pract…
  - 同じ表の列：Year, Month of Processing, Sub-Group, Item Number, State, Services, Benefit

## g0894（1 列）
- 見出し：Sub-Group
- 例1 値：6 Prescribed medical practitioner chron… | 1 No subgroup | 1 No subgroup | 1 GP Attendances | 1 Acupuncture
  - 同じ表の列：Year, Month of Processing, Group, Item Number, State, Services, Benefit

## g0895（1 列）
- 見出し：Item Number
- 例1 値：342 | 239 | 393 | 214 | 116
  - 同じ表の列：Year, Month of Processing, Group, Sub-Group, State, Services, Benefit

## g0896（1 列）
- 見出し：Services
- 例1 値：5 | 390 | 5,026 | 385 | 67
  - 同じ表の列：Year, Month of Processing, Group, Sub-Group, Item Number, State, Benefit

## g0897（1 列）
- 見出し：Benefit
- 例1 値：$45,076.80 | $23,701.45 | $41.75 | $1,404.00 | $4,772.40
  - 同じ表の列：Year, Month of Processing, Group, Sub-Group, Item Number, State, Services

## g0898（1 列）
- 見出し：Service_Area
- 例1 値：Anticipatory Notice - October 2020 | Anticipatory Notice | Anticipatory Notice | Anticipatory Notice | Anticipatory Notice
  - 同じ表の列：Service_Area_Identi…, Contract, Network_Infrastruct…, Estimated_Completio…, Contract_Entered_Da…

## g0899（1 列）
- 見出し：Service_Area_Identifier
- 例1 値：11069 | 11218 | 11115 | 11186 | 11287
  - 同じ表の列：Service_Area, Contract, Network_Infrastruct…, Estimated_Completio…, Contract_Entered_Da…

## g0900（1 列）
- 見出し：Contract
- 例1 値：LBNCo Pty Ltd has entered into a real e… | LBNCo Pty Ltd has entered into a real e… | LBNCo Pty Ltd has entered into a real e… | LBNCo Pty Ltd has entered into a real e… | LBNCo Pty Ltd has entered into a real e…
  - 同じ表の列：Service_Area, Service_Area_Identi…, Network_Infrastruct…, Estimated_Completio…, Contract_Entered_Da…

## g0901（2 列）
- 見出し：Network_Infrastructure
- 例1 値：FTTP | FTTP | FTTP | FTTP | FTTP
  - 同じ表の列：Service_Area, Service_Area_Identi…, Contract, Estimated_Completio…, Contract_Entered_Da…
- 例2 値：FTTB | FTTB | FTTB | FTTB | FTTB
  - 同じ表の列：id, Service_Area, Contract, Estimated_Completio…

## g0902（1 列）
- 見出し：Estimated_Completion_Date
- 例1 値：2022-03-01 00:00:00 | 2022-06-01 00:00:00 | 2022-12-01 00:00:00 | 2021-10-01 00:00:00 | Complete - Declaration 21 April 2021
  - 同じ表の列：Service_Area, Service_Area_Identi…, Contract, Network_Infrastruct…, Contract_Entered_Da…

## g0903（1 列）
- 見出し：Contract_Entered_Date
- 例1 値：2019-06-24T00:00:00 | 2019-12-11T00:00:00 | 2020-04-16T00:00:00 | 2018-09-17T00:00:00 | 2020-05-07T00:00:00
  - 同じ表の列：Service_Area, Service_Area_Identi…, Contract, Network_Infrastruct…, Estimated_Completio…

## g0904（1 列）
- 見出し：Service_Area
- 例1 値：Nominated Service Area | Nominated Service Area | Nominated Service Area | Nominated Service Area | Nominated Service Area
  - 同じ表の列：id, Contract, Network_Infrastruct…, Estimated_Completio…

## g0905（1 列）
- 見出し：Contract
- 例1 値：Completed | Completed | Completed | Completed | Completed
  - 同じ表の列：id, Service_Area, Network_Infrastruct…, Estimated_Completio…

## g0906（1 列）
- 見出し：Estimated_Completion_Date
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：id, Service_Area, Contract, Network_Infrastruct…

## g0907（2 列）
- 見出し：itemid
- 例1 値：423850 | 423850 | 423850 | 423850 | 423850
  - 同じ表の列：title, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink
- 例2 値：476634 | 478690 | 478665 | 476909 | 464349
  - 同じ表の列：title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0908（1 列）
- 見出し：title
- 例1 値：Exhibition of war photographs / taken b… | Exhibition of war photographs / taken b… | Exhibition of war photographs / taken b… | Exhibition of war photographs / taken b… | Exhibition of war photographs / taken b…
  - 同じ表の列：itemid, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink

## g0909（2 列）
- 見出し：albumnumber
- 例1 値：824019 | 824019 | 824019 | 824019 | 824019
  - 同じ表の列：itemid, title, creator, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink
- 例2 値：861563 | 866598 | 866584 | 862714 | 861611
  - 同じ表の列：itemid, title, caption, creator, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0910（1 列）
- 見出し：dateofwork
- 例1 値：Aug 1917 - Aug 1918 | Aug 1917 - Aug 1918 | Aug 1917 - Aug 1918 | Aug 1917 - Aug 1918 | Aug 1917 - Aug 1918
  - 同じ表の列：itemid, title, creator, albumnumber, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink

## g0911（2 列）
- 見出し：collectionitemlink
- 例1 値：http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta…
  - 同じ表の列：itemid, title, creator, albumnumber, dateofwork, digitalitemlink, digitalordernumber, thumbnaillink
- 例2 値：http://library.sl.nsw.gov.au/record=b22… | http://library.sl.nsw.gov.au/record=b22… | http://library.sl.nsw.gov.au/record=b22… | http://library.sl.nsw.gov.au/record=b22… | http://library.sl.nsw.gov.au/record=b22…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, digitalitemlink, digitalordernumber

## g0912（2 列）
- 見出し：digitalitemlink
- 例1 値：http://acms.sl.nsw.gov.au/album/albumVi… | http://acms.sl.nsw.gov.au/album/albumVi… | http://acms.sl.nsw.gov.au/album/albumVi… | http://acms.sl.nsw.gov.au/album/albumVi… | http://acms.sl.nsw.gov.au/album/albumVi…
  - 同じ表の列：itemid, title, creator, albumnumber, dateofwork, collectionitemlink, digitalordernumber, thumbnaillink
- 例2 値：http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalordernumber

## g0913（2 列）
- 見出し：digitalordernumber
- 例1 値：a479086 | a479086 | a479086 | a479086 | a479086
  - 同じ表の列：itemid, title, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, thumbnaillink
- 例2 値：a1367556 | a1367709 | a1367498 | a1367553 | a1367173
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink

## g0914（2 列）
- 見出し：thumbnaillink
- 例1 値：http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1…
  - 同じ表の列：itemid, title, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber
- 例2 値：http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink

## g0915（1 列）
- 見出し：highreslink
- 例1 値：http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1…
  - 同じ表の列：itemid, title, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0916（1 列）
- 見出し：collectionday
- 例1 値：Tuesday | Monday | Friday | Friday | Thursday
  - 同じ表の列：propnum, nextwaste, nextrecycle, nextgreen, servicetype, Calendar_Link

## g0917（1 列）
- 見出し：propnum
- 例1 値：4960 | 8846 | 10868 | 10650 | 5381
  - 同じ表の列：collectionday, nextwaste, nextrecycle, nextgreen, servicetype, Calendar_Link

## g0918（1 列）
- 見出し：nextwaste
- 例1 値：2026-10-28 | 2026-10-27 | 2026-10-27 | 2026-10-27 | 2026-10-27
  - 同じ表の列：collectionday, propnum, nextrecycle, nextgreen, servicetype, Calendar_Link

## g0919（1 列）
- 見出し：nextrecycle
- 例1 値：2026-11-04 | 2026-10-27 | 2026-11-03 | 2026-10-29 | 2026-10-30
  - 同じ表の列：collectionday, propnum, nextwaste, nextgreen, servicetype, Calendar_Link

## g0920（1 列）
- 見出し：nextgreen
- 例1 値：2026-10-26 | 2026-10-27 | 2026-10-27 | 2026-10-28 | 2026-10-23
  - 同じ表の列：collectionday, propnum, nextwaste, nextrecycle, servicetype, Calendar_Link

## g0921（1 列）
- 見出し：Calendar_Link
- 例1 値：https://www.sthgrampians.vic.gov.au/fil… | https://www.sthgrampians.vic.gov.au/fil… | https://www.sthgrampians.vic.gov.au/fil… | https://www.sthgrampians.vic.gov.au/fil… | https://www.sthgrampians.vic.gov.au/fil…
  - 同じ表の列：collectionday, propnum, nextwaste, nextrecycle, nextgreen, servicetype

## g0922（1 列）
- 見出し：Location
- 例1 値：Melbourne | Sydney | Adelaide | Brisbane | Perth
  - 同じ表の列：Year 2007, Year 2020, Year 2050

## g0923（1 列）
- 見出し：Year 2007
- 例1 値：134 | 200 | 294 | 176 | 289
  - 同じ表の列：Location, Year 2020, Year 2050

## g0924（1 列）
- 見出し：Year 2020
- 例1 値：593 | 391 | 673 | 357 | 177
  - 同じ表の列：Location, Year 2007, Year 2050

## g0925（1 列）
- 見出し：Year 2050
- 例1 値：1015 | 573 | 1149 | 1072 | 1419
  - 同じ表の列：Location, Year 2007, Year 2020

## g0926（1 列）
- 見出し：Year end
- 例1 値：2014 | 2017 | 2024 | 2021 | 2020
  - 同じ表の列：Category, No of disclosures

## g0927（1 列）
- 見出し：Category
- 例1 値：Total | Total | Total | Total | Total
  - 同じ表の列：Year end, No of disclosures

## g0928（1 列）
- 見出し：No of disclosures
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year end, Category

## g0929（1 列）
- 見出し：title
- 例1 値：City of Sydney section Sydney sections … | City of Sydney section Sydney sections … | City of Sydney section Paddington ... [… | City of Sydney section Sydney sections … | City of Sydney section Sydney sections …
  - 同じ表の列：itemid, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0930（1 列）
- 見出し：caption
- 例1 値：Balmain, Sheet 71, 1890 | Alexandria, Sheet 20, 1892 | Leichhardt, Sheet 21, 1893 | City of Sydney, Sheet K, 1888 | Balmain, Sheet 9, 1889
  - 同じ表の列：itemid, title, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0931（1 列）
- 見出し：creator
- 例1 値：NSW Department of Lands | NSW Department of Lands | NSW Department of Lands | NSW Department of Lands | NSW Department of Lands
  - 同じ表の列：itemid, title, caption, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0932（1 列）
- 見出し：dateofwork
- 例1 値：1917- | 1917- | 1917- | 1917- | 1917-
  - 同じ表の列：itemid, title, caption, creator, albumnumber, collectionitemlink, digitalitemlink, digitalordernumber

## g0933（1 列）
- 見出し：Catalogue
- 例1 値：http://www.catalog.slsa.sa.gov.au/recor… | http://www.catalog.slsa.sa.gov.au/recor… | http://www.catalog.slsa.sa.gov.au/recor… | http://www.catalog.slsa.sa.gov.au/recor… | http://www.catalog.slsa.sa.gov.au/recor…
  - 同じ表の列：ID, XML, Title, Publication, Topical, Image

## g0934（1 列）
- 見出し：XML
- 例1 値：http://www.catalog.slsa.sa.gov.au/xreco… | http://www.catalog.slsa.sa.gov.au/xreco… | http://www.catalog.slsa.sa.gov.au/xreco… | http://www.catalog.slsa.sa.gov.au/xreco… | http://www.catalog.slsa.sa.gov.au/xreco…
  - 同じ表の列：ID, Catalogue, Title, Publication, Topical, Image

## g0935（1 列）
- 見出し：Title
- 例1 値：Angaston | Congregational Church | A Tent Dwelling | Aldgate.Church of Ascension | Members of the Imperial Force at Morphe…
  - 同じ表の列：ID, Catalogue, XML, Publication, Topical, Image

## g0936（1 列）
- 見出し：Publication
- 例1 値：1890 | 1925 | 1926 | 1902 | 1895
  - 同じ表の列：ID, Catalogue, XML, Title, Topical, Image

## g0937（1 列）
- 見出し：Topical
- 例1 値：Gardens -- South Australia -- Angaston … | Plants -- South Australia -- Athelstone | Dentists -- South Australia -- Angaston | Rock Deformation | Railroad construction workers -- South …
  - 同じ表の列：ID, Catalogue, XML, Title, Publication, Image

## g0938（1 列）
- 見出し：Image
- 例1 値：http://images.slsa.sa.gov.au/mpcimg/290… | http://images.slsa.sa.gov.au/mpcimg/507… | http://images.slsa.sa.gov.au/mpcimg/685… | http://images.slsa.sa.gov.au/mpcimg/442… | http://images.slsa.sa.gov.au/mpcimg/227…
  - 同じ表の列：ID, Catalogue, XML, Title, Publication, Topical

## g0939（1 列）
- 見出し：PostalSuburb
- 例1 値：Ravensthorpe | Seville Grove | Carnamah | Lake Grace | Karratha
  - 同じ表の列：PostalState, PostalPostcode, ElevationfromSeaLev…

## g0940（1 列）
- 見出し：PostalState
- 例1 値：WA | WA | WA | WA | WA
  - 同じ表の列：PostalSuburb, PostalPostcode, ElevationfromSeaLev…

## g0941（1 列）
- 見出し：PostalPostcode
- 例1 値：6337 | 6722 | 6630 | 6281 | 6432
  - 同じ表の列：PostalSuburb, PostalState, ElevationfromSeaLev…

## g0942（1 列）
- 見出し：ElevationfromSeaLevel(inm)
- 例1 値：290 | 78 | 66 | 281 | 16
  - 同じ表の列：PostalSuburb, PostalState, PostalPostcode

## g0943（1 列）
- 見出し：Ride
- 例1 値：Hub & Spoke Cycling Route | Bump & Grind Cycling Route | Bump & Grind Cycling Route | Hub & Spoke / Bump & Grind Cycling Route | Hub & Spoke
  - 同じ表の列：Mode, Start_Fin, Difficulty, Distance, Elevation, Topography, Surfaces, Surfaces2

## g0944（1 列）
- 見出し：Mode
- 例1 値：Road bike (or any other) | Gravel Grinder, MTB, Hybrid, eBike (fat… | Road cycling | Gravel Grinder | Gravel grinder, MTB, Hybrid
  - 同じ表の列：Ride, Start_Fin, Difficulty, Distance, Elevation, Topography, Surfaces, Surfaces2

## g0945（1 列）
- 見出し：Start_Fin
- 例1 値：Nagambie Railway Station Prentice St., … | Nagambie Railway Station | Violet Town Railway Station Corner Prim… | Avenel Railway Station, Avenel 3664 | Euroa Railway Station Railway St., Euro…
  - 同じ表の列：Ride, Mode, Difficulty, Distance, Elevation, Topography, Surfaces, Surfaces2

## g0946（1 列）
- 見出し：Difficulty
- 例1 値：Easy to intermediate (not for road bike… | Moderate | Intermediate (modest rises) | Intermediate: modest rises | Intermediate
  - 同じ表の列：Ride, Mode, Start_Fin, Distance, Elevation, Topography, Surfaces, Surfaces2

## g0947（1 列）
- 見出し：Distance
- 例1 値：17km, 1 to 2hrs | 12km | 23km | 27km, 2hrs | 17km
  - 同じ表の列：Ride, Mode, Start_Fin, Difficulty, Elevation, Topography, Surfaces, Surfaces2

## g0948（1 列）
- 見出し：Elevation
- 例1 値：158 to 199m | Between 168 and 232m | 159 to 184m | 136 to 155mm | 211 to 145m
  - 同じ表の列：Ride, Mode, Start_Fin, Difficulty, Distance, Topography, Surfaces, Surfaces2

## g0949（1 列）
- 見出し：Topography
- 例1 値：Flat | Flat with slight rises. | Flat | Flat with one small rise. | Undulating plateau
  - 同じ表の列：Ride, Mode, Start_Fin, Difficulty, Distance, Elevation, Surfaces, Surfaces2

## g0950（1 列）
- 見出し：Surfaces
- 例1 値：Good condition bitumen, with a nice wid… | Good condition bitumen. Variable gravel… | Loose gravel, dirt, clay with patches o… | Bitumen, some ridging from tree roots i… | Good condition bitumen and gravel. Reyn…
  - 同じ表の列：Ride, Mode, Start_Fin, Difficulty, Distance, Elevation, Topography, Surfaces2

## g0951（1 列）
- 見出し：Surfaces2
- 例1 値：not too bad. If you wish to join the Ra…
  - 同じ表の列：Ride, Mode, Start_Fin, Difficulty, Distance, Elevation, Topography, Surfaces

## g0952（1 列）
- 見出し：Descript
- 例1 値：A loop west past Mangalore aerodrome an… | Nagambie is well serviced, Murchison le… | The dirt tracks and roads through Heath… | A pleasant loop that follows the line b… | A nice and flat, often gravel, loop for…
  - 同じ表の列：Ride, Mode, Start_Fin, Difficulty, Distance, Elevation, Topography, Surfaces

## g0953（1 列）
- 見出し：Victorian regions
- 例1 値：Moyne | Murrindindi | Mildura | Mount Alexander | Melbourne
  - 同じ表の列：Homes, Horizontal radiatio…, CO2e saved kilotons, Cars off road thous…, Black balloons mill…

## g0954（1 列）
- 見出し：Homes
- 例1 値：4944 | 5093 | 12931 | 9797 | 89983
  - 同じ表の列：Victorian regions, Horizontal radiatio…, CO2e saved kilotons, Cars off road thous…, Black balloons mill…

## g0955（1 列）
- 見出し：Horizontal radiation MJ/sq m/day
- 例1 値：20 | 18 | 19 | 18 | 18
  - 同じ表の列：Victorian regions, Homes, CO2e saved kilotons, Cars off road thous…, Black balloons mill…

## g0956（1 列）
- 見出し：CO2e saved kilotons
- 例1 値：13 | 24 | 16 | 8 | 233
  - 同じ表の列：Victorian regions, Homes, Horizontal radiatio…, Cars off road thous…, Black balloons mill…

## g0957（1 列）
- 見出し：Cars off road thousands
- 例1 値：68 | 3 | 3 | 3 | 5
  - 同じ表の列：Victorian regions, Homes, Horizontal radiatio…, CO2e saved kilotons, Black balloons mill…

## g0958（1 列）
- 見出し：Black balloons millions
- 例1 値：277 | 1362 | 223 | 337 | 1514
  - 同じ表の列：Victorian regions, Homes, Horizontal radiatio…, CO2e saved kilotons, Cars off road thous…

## g0959（1 列）
- 見出し：Financial year
- 例1 値：2014-15 | 2005-06 | 2007-08 | 2010-11 | 2003-04
  - 同じ表の列：Passenger cars (bil…, Buses (billion pass…, Rail (billion passe…, Air (billion passen…, Other (billion pass…, Total (billion pass…

## g0960（1 列）
- 見出し：Passenger cars (billion passenger kilometres)
- 例1 値：249.45 | 260.42 | 275.02 | 261.87 | 267.18
  - 同じ表の列：Financial year, Buses (billion pass…, Rail (billion passe…, Air (billion passen…, Other (billion pass…, Total (billion pass…

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
