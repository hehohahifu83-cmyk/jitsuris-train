# ラベル用シート 003 / 008

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：CREATE_DAT
- 例1 値：15/02/2011 | 26/11/2007 | 15/02/2011 | 26/11/2007 | 26/11/2007
  - 同じ表の列：OBJECTID, TYPE_, ASSET_NUMB, CONDUIT_SI, COMMENTS, UPDATE_DAT, POSITIONAL, SHAPE_LEN

## g0242（1 列）
- 見出し：UPDATE_DAT
- 例1 値：26/11/2007 | 23/11/2007 | 23/11/2007 | 26/11/2007 | 26/11/2007
  - 同じ表の列：OBJECTID, TYPE_, ASSET_NUMB, CONDUIT_SI, COMMENTS, CREATE_DAT, POSITIONAL, SHAPE_LEN

## g0243（1 列）
- 見出し：POSITIONAL
- 例1 値：Design | GPS Corrected 1.0M | Design | GPS Corrected 1.0M | GPS Corrected 1.0M
  - 同じ表の列：OBJECTID, TYPE_, ASSET_NUMB, CONDUIT_SI, COMMENTS, CREATE_DAT, UPDATE_DAT, SHAPE_LEN

## g0244（1 列）
- 見出し：SHAPE_LEN
- 例1 値：14.96982366 | 106.2326452 | 40.39148339 | 120.8217019 | 136.5573342
  - 同じ表の列：OBJECTID, TYPE_, ASSET_NUMB, CONDUIT_SI, COMMENTS, CREATE_DAT, UPDATE_DAT, POSITIONAL

## g0245（1 列）
- 見出し：grs_zones
- 例1 値：484 | 135 | 485 | 369 | 2726
  - 同じ表の列：id_areas, settlement, 2011, 2016, 2021, 2026, 2031, 2036

## g0246（1 列）
- 見出し：id_areas
- 例1 値：Corio | Norlane - North Shore | Lovely Banks - Batesford - Moorabool | Norlane - North Shore | Leopold
  - 同じ表の列：grs_zones, settlement, 2011, 2016, 2021, 2026, 2031, 2036

## g0247（1 列）
- 見出し：settlement
- 例1 値：Leopold | Geelong | Ocean Grove | Geelong | Ocean Grove
  - 同じ表の列：grs_zones, id_areas, 2011, 2016, 2021, 2026, 2031, 2036

## g0248（1 列）
- 見出し：2011
- 例1 値：18 | 63 | 0 | 23 | 580
  - 同じ表の列：grs_zones, id_areas, settlement, 2016, 2021, 2026, 2031, 2036

## g0249（2 列）
- 見出し：2016
- 例1 値：821 | 91 | 596 | 659 | 567
  - 同じ表の列：grs_zones, id_areas, settlement, 2011, 2021, 2026, 2031, 2036
- 例2 値：547 | 1703 | 3847 | 8635 | 4356
  - 同じ表の列：Intended_Destination, 2014, 2015, 2017, 2018, 2019, 2020, 2021

## g0250（2 列）
- 見出し：2021
- 例1 値：665 | 78 | 363 | 537 | 629
  - 同じ表の列：grs_zones, id_areas, settlement, 2011, 2016, 2026, 2031, 2036
- 例2 値：20353 | 5339 | 1418 | 492 | 1729
  - 同じ表の列：Intended_Destination, 2014, 2015, 2016, 2017, 2018, 2019, 2020

## g0251（1 列）
- 見出し：2026
- 例1 値：670 | 118 | 19 | 461 | 0
  - 同じ表の列：grs_zones, id_areas, settlement, 2011, 2016, 2021, 2031, 2036

## g0252（1 列）
- 見出し：2031
- 例1 値：222 | 119 | 641 | 634 | 664
  - 同じ表の列：grs_zones, id_areas, settlement, 2011, 2016, 2021, 2026, 2036

## g0253（1 列）
- 見出し：2036
- 例1 値：97 | 133 | 80 | 1,090 | 618
  - 同じ表の列：grs_zones, id_areas, settlement, 2011, 2016, 2021, 2026, 2031

## g0254（1 列）
- 見出し：2041
- 例1 値：239 | 2,086 | 1,547 | 0 | 1,284
  - 同じ表の列：grs_zones, id_areas, settlement, 2011, 2016, 2021, 2026, 2031

## g0255（1 列）
- 見出し：Suburb
- 例1 値：Point Lonsdale | 20Drysdale | 30Thomson/Breakwater | Avalon (Vic.) | 10Clifton Springs
  - 同じ表の列：LUM, LUMquintile, TrainDistThresh, TrainPres, BusDistThresh, BusPres, AccUtDestPres, AccUtDestPresquinti…

## g0256（1 列）
- 見出し：LUM
- 例1 値：0.486351259 | 0.000120424 | 0.140498297 | 0.213629758 | 0.188262116
  - 同じ表の列：Suburb, LUMquintile, TrainDistThresh, TrainPres, BusDistThresh, BusPres, AccUtDestPres, AccUtDestPresquinti…

## g0257（1 列）
- 見出し：LUMquintile
- 例1 値：1 | 5 | 4 | 1 | 1
  - 同じ表の列：Suburb, LUM, TrainDistThresh, TrainPres, BusDistThresh, BusPres, AccUtDestPres, AccUtDestPresquinti…

## g0258（1 列）
- 見出し：TrainDistThresh
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Suburb, LUM, LUMquintile, TrainPres, BusDistThresh, BusPres, AccUtDestPres, AccUtDestPresquinti…

## g0259（1 列）
- 見出し：TrainPres
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Suburb, LUM, LUMquintile, TrainDistThresh, BusDistThresh, BusPres, AccUtDestPres, AccUtDestPresquinti…

## g0260（1 列）
- 見出し：BusDistThresh
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Suburb, LUM, LUMquintile, TrainDistThresh, TrainPres, BusPres, AccUtDestPres, AccUtDestPresquinti…

## g0261（1 列）
- 見出し：BusPres
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Suburb, LUM, LUMquintile, TrainDistThresh, TrainPres, BusDistThresh, AccUtDestPres, AccUtDestPresquinti…

## g0262（1 列）
- 見出し：AccUtDestPres
- 例1 値：1 | 7 | 2 | 6 | 1
  - 同じ表の列：Suburb, LUM, LUMquintile, TrainDistThresh, TrainPres, BusDistThresh, BusPres, AccUtDestPresquinti…

## g0263（1 列）
- 見出し：AccUtDestPresquintile
- 例1 値：2 | 1 | 1 | 1 | 3
  - 同じ表の列：Suburb, LUM, LUMquintile, TrainDistThresh, TrainPres, BusDistThresh, BusPres, AccUtDestPres

## g0264（1 列）
- 見出し：AccUtDestDist
- 例1 値：4 | 6 | 7 | 1 | 2
  - 同じ表の列：Suburb, LUM, LUMquintile, TrainDistThresh, TrainPres, BusDistThresh, BusPres, AccUtDestPres

## g0265（5 列）
- 見出し：type
- 例1 値：Secondary Public | Primary Public | Primary Private | Primary Public | Primary Private
  - 同じ表の列：long, lat
- 例2 値：bicycle racking | bicycle racking | bicycle racking | bicycle racking | bicycle racking
  - 同じ表の列：lon, lat, ref, desc, subtype, suburb

## g0266（1 列）
- 見出し：date
- 例1 値：20201104 | 20201104 | 20201105 | 20201112 | 20201029
  - 同じ表の列：time, suburb, waste_type, volume_m3

## g0267（1 列）
- 見出し：time
- 例1 値：13:33:00 | 13:32:00 | 11:48:00 | 14:06:00 | 14:50:00
  - 同じ表の列：date, suburb, waste_type, volume_m3

## g0268（9 列）
- 見出し：suburb
- 例1 値：Fitzroy | Abbotsford | Alphington | Fitzroy | Carlton North
  - 同じ表の列：date, time, waste_type, volume_m3
- 例2 値：Fairfield | Fitzroy | Richmond | Clifton Hill | Cremorne
  - 同じ表の列：lat, lon, elevation, status, ref

## g0269（1 列）
- 見出し：waste_type
- 例1 値：General waste | General waste | General waste | General waste | General waste
  - 同じ表の列：date, time, suburb, volume_m3

## g0270（1 列）
- 見出し：volume_m3
- 例1 値：2.5 | 0.5 | 4.5 | 1 | 2.5
  - 同じ表の列：date, time, suburb, waste_type

## g0271（1 列）
- 見出し：operator
- 例1 値：Private | Broadmeadows Uniting Care | Private | University of Melbourne | Yarra City Council
  - 同じ表の列：licence_capacity, ref

## g0272（1 列）
- 見出し：licence_capacity
- 例1 値：52 places | 22 places | 43 places | 75 places | 48 places
  - 同じ表の列：operator, ref

## g0273（1 列）
- 見出し：ref
- 例1 値：22 | 37 | 6 | 34 | 23
  - 同じ表の列：operator, licence_capacity

## g0274（1 列）
- 見出し：elevation
- 例1 値：29.55 | 70.969 | 26.829 | 62.811 | 52.184
  - 同じ表の列：lat, lon, status, ref, suburb

## g0275（3 列）
- 見出し：status
- 例1 値：built | built | built | built | built
  - 同じ表の列：lat, lon, elevation, ref, suburb
- 例2 値：ceased | certified | registered | registered | certified
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g0276（1 列）
- 見出し：ref
- 例1 値：yarracity | yarracity | yarracity | yarracity | yarracity
  - 同じ表の列：lat, lon, elevation, status, suburb

## g0277（4 列）
- 見出し：ref
- 例1 値：SF00460 | SF00436 | SF00519 | SF00489 | SF00553
  - 同じ表の列：lon, lat, subtype, suburb, type
- 例2 値：SF00218 | SF00042 | SF00084 | SF00222 | SF00217
  - 同じ表の列：lon, lat, desc, subtype, suburb, type

## g0278（1 列）
- 見出し：subtype
- 例1 値：Bin/Hide Garbage | Bin/Hide Garbage | Bin/Hide Garbage | Bin/Hide Garbage | Bin/Hide Garbage
  - 同じ表の列：lon, lat, ref, suburb, type

## g0279（4 列）
- 見出し：type
- 例1 値：bin | bin | bin | bin | bin
  - 同じ表の列：lon, lat, ref, subtype, suburb
- 例2 値：bbq | bbq | bbq | bbq | bbq
  - 同じ表の列：lon, lat, ref, desc, subtype, suburb

## g0280（1 列）
- 見出し：desc
- 例1 値：Curdie Street Cobden Rack | Montgomery Street Skipton Rack | Montogomery Street Skipton Rack | High Street Terang Rack | MANIFOLD STREET NODE NO 1 - at BENALLAC…
  - 同じ表の列：lon, lat, ref, subtype, suburb, type

## g0281（2 列）
- 見出し：subtype
- 例1 値：Bicycle Rack | Bicycle Rack | Bicycle Rack | Bicycle Rack | Bicycle Rack
  - 同じ表の列：lon, lat, ref, desc, suburb, type
- 例2 値：Electric BBQ | Electric BBQ
  - 同じ表の列：lon, lat, ref, desc, suburb, type

## g0282（8 列）
- 見出し：suburb
- 例1 値：Terang | Camperdown | Terang | Skipton | Camperdown
  - 同じ表の列：lon, lat, ref, desc, subtype, type
- 例2 値：Noorat | Timboon | Cobden | Camperdown | Lismore
  - 同じ表の列：lon, lat, ref, desc, subtype, type

## g0283（1 列）
- 見出し：desc
- 例1 値：Apex Park Cobden BBQ | Avenue of Elms Terang BBQ | MEDIAN CENTRE DERRINALLUM | Apex Park Terang BBQ | Apex Park Camperdown BBQ
  - 同じ表の列：lon, lat, ref, subtype, suburb, type

## g0284（1 列）
- 見出し：POE* searches
- 例1 値：Jurors empanelled | Sheriff痴 Office Enforcement | The impact of the change in data manage… | Warrants issued | Juries
  - 同じ表の列：615715, 556155, 581045, 565739, 491939

## g0285（1 列）
- 見出し：615715
- 例1 値：59 | 1628 | 5352 | 3300 | 1093
  - 同じ表の列：POE* searches, 556155, 581045, 565739, 491939

## g0286（1 列）
- 見出し：556155
- 例1 値：994 | 2021-22 | 46 | 3896 | 8589
  - 同じ表の列：POE* searches, 615715, 581045, 565739, 491939

## g0287（1 列）
- 見出し：581045
- 例1 値：1116 | 69% | 92 | 4460 | 41
  - 同じ表の列：POE* searches, 615715, 556155, 565739, 491939

## g0288（1 列）
- 見出し：565739
- 例1 値：955 | 4024 | 2023-24 | 78% | 41
  - 同じ表の列：POE* searches, 615715, 556155, 581045, 491939

## g0289（1 列）
- 見出し：491939
- 例1 値：41 | 2028 | 169 | 681 | 12826
  - 同じ表の列：POE* searches, 615715, 556155, 581045, 565739

## g0290（1 列）
- 見出し：Workplace injury claims
- 例1 値：Income support payments ? gross ($) | Number of notifiable incidents (Work He… | Work health and safety regulations | Total gross workers compensation expend… | Total new workplace injury claims
  - 同じ表の列：Current Year, Past year, % Change

## g0291（1 列）
- 見出し：Current Year
- 例1 値：Current Year | Current Year | 49 | $0.7m | 2023-24
  - 同じ表の列：Workplace injury cl…, Past year, % Change

## g0292（1 列）
- 見出し：Past year
- 例1 値：52 | $2.3m | 2022-23 | 0 | 2022-23
  - 同じ表の列：Workplace injury cl…, Current Year, % Change

## g0293（1 列）
- 見出し：% Change
- 例1 値：0% | % Change | -8% | (+ / -) | 50%
  - 同じ表の列：Workplace injury cl…, Current Year, Past year

## g0294（1 列）
- 見出し：Consultant
- 例1 値：Sub total | Value $10 000 or more | Value below $10 000 | Consultant | Sub total
  - 同じ表の列：Purpose of consulta…, $

## g0295（1 列）
- 見出し：Purpose of consultancy
- 例1 値：0 | 0 | 0 | Purpose of consultancy | 0
  - 同じ表の列：Consultant, $

## g0296（1 列）
- 見出し：$
- 例1 値：$
  - 同じ表の列：Consultant, Purpose of consulta…

## g0297（1 列）
- 見出し：Youth DNR rank - population weighted
- 例1 値：73 | 35 | 34 | 103 | 25
  - 同じ表の列：Youth DNR rank, Families DNR rank -…, Families DNR rank

## g0298（1 列）
- 見出し：Youth DNR rank
- 例1 値：3 | 22 | 79 | 61 | 64
  - 同じ表の列：Youth DNR rank - po…, Families DNR rank -…, Families DNR rank

## g0299（1 列）
- 見出し：Families DNR rank - population weighted
- 例1 値：103 | 90 | 47 | 102 | 121
  - 同じ表の列：Youth DNR rank - po…, Youth DNR rank, Families DNR rank

## g0300（1 列）
- 見出し：Families DNR rank
- 例1 値：119 | 114 | 22 | 98 | 60
  - 同じ表の列：Youth DNR rank - po…, Youth DNR rank, Families DNR rank -…

## g0301（1 列）
- 見出し：Category
- 例1 値：1 | 6 | 4 | 5 | 3
  - 同じ表の列：No. of Sites (Start…, No. of Sites End of…, Interpretation (One…

## g0302（1 列）
- 見出し：No. of Sites (Start of Year)
- 例1 値：4 | 0 | 3 | 43 | 0
  - 同じ表の列：Category, No. of Sites End of…, Interpretation (One…

## g0303（1 列）
- 見出し：No. of Sites End of Year)
- 例1 値：2 | 2 | 43 | 2 | 0
  - 同じ表の列：Category, No. of Sites (Start…, Interpretation (One…

## g0304（1 列）
- 見出し：Interpretation (One or more items at these sites)
- 例1 値：May need removal during maintenance wor… | Should be scheduled for removal at a pr… | These sites not yet categorised or some… | Has asbestos present. Inspect according… | Should be removed promptly
  - 同じ表の列：Category, No. of Sites (Start…, No. of Sites End of…

## g0305（1 列）
- 見出し：Winners 2017 GovHack in SA Awards
- 例1 値：Vibrant Adelaide | Smart Lifestyles | South Australian Commercialisation | Advancing South Australia | Best Entry from South Australia
  - 同じ表の列：Sponsors, Competition Entry

## g0306（1 列）
- 見出し：Sponsors
- 例1 値：Department of the Premier and Cabinet | Location SA | Department for Education and Child Deve… | Department of Environment, Water and Na… | Adelaide Smart City Studio
  - 同じ表の列：Winners 2017 GovHac…, Competition Entry

## g0307（1 列）
- 見出し：Competition Entry
- 例1 値：https://2017.hackerspace.govhack.org/pr… | https://2017.hackerspace.govhack.org/pr… | https://2017.hackerspace.govhack.org/pr… | https://2017.hackerspace.govhack.org/pr… | https://2017.hackerspace.govhack.org/pr…
  - 同じ表の列：Winners 2017 GovHac…, Sponsors

## g0308（1 列）
- 見出し：CD_MAKE_VEH1
- 例1 値：CITRN | L ROV | AUSTRL | J L G | H DAV
  - 同じ表の列：CD_CLR_BDY_VEH_P, TOTAL1

## g0309（1 列）
- 見出し：CD_CLR_BDY_VEH_P
- 例1 値：OGE | PUR | WHI | BLU | BLK
  - 同じ表の列：CD_MAKE_VEH1, TOTAL1

## g0310（1 列）
- 見出し：TOTAL1
- 例1 値：127 | 2 | 1 | 1 | 1
  - 同じ表の列：CD_MAKE_VEH1, CD_CLR_BDY_VEH_P

## g0311（1 列）
- 見出し：Coding date
- 例1 値：10/07/2023 | 10/07/2023 | 7/05/2023 | 13/07/2023 | 10/07/2023
  - 同じ表の列：Road survey date, Image reference, Section, Distance, Length, Landmark, Carriageway, Land use - driver-s…

## g0312（1 列）
- 見出し：Road survey date
- 例1 値：24/02/2022 | 24/02/2022 | 22/02/2022 | 24/02/2022 | 21/02/2022
  - 同じ表の列：Coding date, Image reference, Section, Distance, Length, Landmark, Carriageway, Land use - driver-s…

## g0313（1 列）
- 見出し：Image reference
- 例1 値：2010_HOPKINS HWY _F_S1_0_48461 Frame 22… | 2500_PRINCES HWY WEST_F_S3_42646_109507… | 2190_SURFCOAST HWY _R_S1_64_17680 Frame… | 2500_PRINCES HWY WEST_F_S3_42646_109507… | 2010_HOPKINS HWY _F_S1_0_48461 Frame 806
  - 同じ表の列：Coding date, Road survey date, Section, Distance, Length, Landmark, Carriageway, Land use - driver-s…

## g0314（1 列）
- 見出し：Section
- 例1 値：S1 | S1 | S3 | S1 | S1
  - 同じ表の列：Coding date, Road survey date, Image reference, Distance, Length, Landmark, Carriageway, Land use - driver-s…

## g0315（1 列）
- 見出し：Distance
- 例1 値：4.159 | 45.099 | 44.547 | 6.798 | 46.147
  - 同じ表の列：Coding date, Road survey date, Image reference, Section, Length, Landmark, Carriageway, Land use - driver-s…

## g0316（1 列）
- 見出し：Length
- 例1 値：0.1 | 0.1 | 0.1 | 0.1 | 0.1
  - 同じ表の列：Coding date, Road survey date, Image reference, Section, Distance, Landmark, Carriageway, Land use - driver-s…

## g0317（1 列）
- 見出し：Landmark
- 例1 値：B120 | Beacon BLVD | Colac | Torquay | Mt Duneed
  - 同じ表の列：Coding date, Road survey date, Image reference, Section, Distance, Length, Carriageway, Land use - driver-s…

## g0318（1 列）
- 見出し：Carriageway
- 例1 値：3 | 3 | 3 | 1 | 3
  - 同じ表の列：Coding date, Road survey date, Image reference, Section, Distance, Length, Landmark, Land use - driver-s…

## g0319（1 列）
- 見出し：Land use - driver-side
- 例1 値：3 | 1 | 1 | 3 | 1
  - 同じ表の列：Coding date, Road survey date, Image reference, Section, Distance, Length, Landmark, Carriageway

## g0320（1 列）
- 見出し：Land use - passenger-side
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Coding date, Road survey date, Image reference, Section, Distance, Length, Landmark, Carriageway

## g0321（4 列）
- 見出し：State
- 例1 値：VIC | VIC | VIC | VIC | VIC
  - 同じ表の列：Suburb, Business Category, LGA, Region
- 例2 値：VIC | VIC | VIC | VIC | VIC
  - 同じ表の列：Suburb, Business Category, LGA, Region

## g0322（1 列）
- 見出し：Business Category
- 例1 値：Pony Club | Pony Club | Pony Club | Pony Club | Pony Club
  - 同じ表の列：Suburb, State, LGA, Region

## g0323（1 列）
- 見出し：LGA
- 例1 値：Golden Plains (S) | Ballarat (C); Ballarat (C) | Mornington Peninsula (S); Frankston (C)… | Mount ［個人名のため削除］ander (S) | Wangaratta (RC)
  - 同じ表の列：Suburb, State, Business Category, Region

## g0324（1 列）
- 見出し：Region
- 例1 値：North and West Metropolitan Region | Southern Metropolitan Region | Eastern Metropolitan Region | Southern Metropolitan Region | Loddon-Mallee Region; Hume Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0325（1 列）
- 見出し：Business Category
- 例1 値：Orienteering Club | Orienteering Club | Orienteering Club | Orienteering Club | Orienteering Club,Recreation Group,Walk…
  - 同じ表の列：Suburb, State, LGA, Region

## g0326（2 列）
- 見出し：LGA
- 例1 値：Darebin (C) | Greater Bendigo (C) | Boroondara (C) | Glen Eira (C) | Whitehorse (C)
  - 同じ表の列：Suburb, State, Business Category, Region
- 例2 値：East Gippsland (S) | Loddon (S) | Yarra Ranges (S) | Macedon Ranges (S) | Greater Geelong (C)
  - 同じ表の列：Suburb, State, Business Category, Region

## g0327（1 列）
- 見出し：Region
- 例1 値：Loddon-Mallee Region | Loddon-Mallee Region | Southern Metropolitan Region | Eastern Metropolitan Region | Southern Metropolitan Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0328（1 列）
- 見出し：Business Category
- 例1 値：Neighbourhood house | Neighbourhood house | Neighbourhood house | Neighbourhood house,Strength Training,T… | Neighbourhood house
  - 同じ表の列：Suburb, State, LGA, Region

## g0329（1 列）
- 見出し：Region
- 例1 値：Southern Metropolitan Region | North and West Metropolitan Region | Hume Region | Loddon-Mallee Region; Hume Region | Southern Metropolitan Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0330（1 列）
- 見出し：Complex_Type
- 例1 値：Recreation Reserve | Public Open Space | Recreation Reserve | Recreation Reserve | Recreation Reserve
  - 同じ表の列：Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, LAT, LONG

## g0331（1 列）
- 見出し：Facility_Type
- 例1 値：Public Toilet | Public Toilet | Public Toilet | Public Toilet | Public Toilet
  - 同じ表の列：Complex_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, LAT, LONG

## g0332（1 列）
- 見出し：Bookable_Item
- 例1 値：Enfield Harrison Reserve Public Toilet | Linton Community Precinct Public Toilet | Enfield Recreation Reserve Public Toilet | Corindhap Recreation Reserve Public Toi… | Bannockburn Victoria Park Recreation Re…
  - 同じ表の列：Complex_Type, Facility_Type, Assessment_No, Number, Locality, Post_Code, LAT, LONG

## g0333（2 列）
- 見出し：Assessment_No
- 例1 値：66379102 | 91002388 | 91000633 | 41400956 | 36600007
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Number, Locality, Post_Code, LAT, LONG
- 例2 値：91001666 | 91001666 | 66379102 | 66300008 | 66116405
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Number, Locality, Post_Code, LAT, LONG

## g0334（1 列）
- 見出し：Locality
- 例1 値：Lethbridge | Rokewood | Enfield | Cape Clear | Linton
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Post_Code, LAT, LONG

## g0335（3 列）
- 見出し：Post_Code
- 例1 値：3329 | 3330 | 0 | 3360 | 3351
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, LAT, LONG
- 例2 値：3351 | 3331 | 3331 | 3351 | 3360
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, LAT, LONG

## g0336（1 列）
- 見出し：Complex_Type
- 例1 値：Stadium | Recreation Reserve | Recreation Reserve | Recreation Reserve | Recreation Reserve
  - 同じ表の列：Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, LAT, LONG

## g0337（1 列）
- 見出し：Facility_Type
- 例1 値：Stadium | Stadium | Stadium | Stadium | Stadium
  - 同じ表の列：Complex_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, LAT, LONG

## g0338（1 列）
- 見出し：Bookable_Item
- 例1 値：Linton Recreation Reserve Stadium | Woady Yaloak Recreation Reserve Stadium | Bannockburn Recreation Centre Court 2 | Bannockburn Community Sports Stadium Co… | Bannockburn Recreation Centre Court 1
  - 同じ表の列：Complex_Type, Facility_Type, Assessment_No, Number, Locality, Post_Code, LAT, LONG

## g0339（1 列）
- 見出し：Locality
- 例1 値：Bannockburn | Haddon | Linton | Bannockburn | Smythesdale
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Post_Code, LAT, LONG

## g0340（1 列）
- 見出し：Zone
- 例1 値：Zone 54 | Zone 74 | Zone 89 | Zone 29 | Zone 31
  - 同じ表の列：Type

## g0341（1 列）
- 見出し：location
- 例1 値：Poplar (Urban) Avenue (Shepparton) | Fryers Street (Shepparton) | North Street (Shepparton) | Morrell Street (Mooroopna) | Knight Street (Shepparton)
  - 同じ表の列：ref, material, type, number_of, capacity

## g0342（1 列）
- 見出し：material
- 例1 値：Steel | Steel | Steel | Steel | Steel
  - 同じ表の列：ref, location, type, number_of, capacity

## g0343（1 列）
- 見出し：number_of
- 例1 値：3 | 1 | 3 | 1 | 1
  - 同じ表の列：ref, location, material, type, capacity

## g0344（2 列）
- 見出し：capacity
- 例1 値：2 | 4 | 2 | 2 | 2
  - 同じ表の列：ref, location, material, type, number_of
- 例2 値：15 | 23 | 11 | 19 | 38
  - 同じ表の列：station_id, rental_method, lat, lon, location

## g0345（2 列）
- 見出し：maint_auth
- 例1 値：Hobsons Bay City Council | Hobsons Bay City Council | Hobsons Bay City Council | Hobsons Bay City Council | Hobsons Bay City Council
  - 同じ表の列：suburb, area_sqm, melway_ref
- 例2 値：Hobsons Bay City Council | Hobsons Bay City Council | Hobsons Bay City Council | Hobsons Bay City Council | Hobsons Bay City Council
  - 同じ表の列：site, location, type, area_sqm, length_m, width_m, clearance, span

## g0346（1 列）
- 見出し：melway_ref
- 例1 値：55:G3 | 56:C11 | 54:H11 | 56:D12 | Unknown
  - 同じ表の列：suburb, maint_auth, area_sqm

## g0347（1 列）
- 見出し：location
- 例1 値：Altona Golf Course | Churchill St - Culvert | Bay West Trail | Bay West Trail | Bay West Trail
  - 同じ表の列：site, type, maint_auth, area_sqm, length_m, width_m, clearance, span

## g0348（1 列）
- 見出し：area_sqm
- 例1 値：1009.62 | 28.75 | 69.46 | 755.66 | 2.31
  - 同じ表の列：site, location, type, maint_auth, length_m, width_m, clearance, span

## g0349（1 列）
- 見出し：length_m
- 例1 値：114 | 3 | 20 | 6.5 | 20
  - 同じ表の列：site, location, type, maint_auth, area_sqm, width_m, clearance, span

## g0350（1 列）
- 見出し：width_m
- 例1 値：5 | 1.2 | 2.2 | 2.4 | 1.1
  - 同じ表の列：site, location, type, maint_auth, area_sqm, length_m, clearance, span

## g0351（1 列）
- 見出し：clearance
- 例1 値：0.15 | 0 | 0 | 0 | 0.6
  - 同じ表の列：site, location, type, maint_auth, area_sqm, length_m, width_m, span

## g0352（1 列）
- 見出し：span
- 例1 値：3 x 7.5 | 2 x 3 x 1.2 | 4 x 2.4 x 1.8 | 1 x 2.1 | 4 x 28.5
  - 同じ表の列：site, location, type, maint_auth, area_sqm, length_m, width_m, clearance

## g0353（1 列）
- 見出し：CENSUS_DISTRICT
- 例1 値：New Town | Hobart | Hobart | Bothwell | Richmond
  - 同じ表の列：PAGE, UNDER14, YEAR_DISPLAY, YEAR

## g0354（2 列）
- 見出し：PAGE
- 例1 値：155 | 55 | 201 | 159 | 75
  - 同じ表の列：CENSUS_DISTRICT, UNDER14, YEAR_DISPLAY, YEAR
- 例2 値：7 | 17 | 8 | 8 | 28
  - 同じ表の列：Heading, Category, Title, Date, TrovePageUrl, Illustrated, WordCount, Relevance

## g0355（1 列）
- 見出し：UNDER14
- 例1 値：No | No | Yes | No | No
  - 同じ表の列：CENSUS_DISTRICT, PAGE, YEAR_DISPLAY, YEAR

## g0356（1 列）
- 見出し：YEAR_DISPLAY
- 例1 値：1842 | 1842 | 1837 | 1851 | 1842
  - 同じ表の列：CENSUS_DISTRICT, PAGE, UNDER14, YEAR

## g0357（1 列）
- 見出し：device
- 例1 値：Speed Hump | Roundabout | Speed Hump | Speed Hump | Gate
  - 同じ表の列：lat, long

## g0358（1 列）
- 見出し：location
- 例1 値：High St, Templestowe Lower | Church Rd, Doncaster | Wilsons Rd, Doncaster | Knees Rd, Park Orchards | Pleasant Rd, Bulleen
  - 同じ表の列：between_, school, mapref, hours, lat

## g0359（1 列）
- 見出し：between_
- 例1 値：Bilby St & Heath St | Bordeaus St & Brendan Av | Taroona Ave & Yarra St | Eastway Ave & Roy St | Derrick Ave & Ronald Ave
  - 同じ表の列：location, school, mapref, hours, lat

## g0360（1 列）
- 見出し：school
- 例1 値：Heatherwood & Donvale Primary School | Templestowe Valley Primary School | Templestowe Heights Primary School | Birralee Primary School | Anderson Creek Primary School
  - 同じ表の列：location, between_, mapref, hours, lat

## 答えの雛形

```
g0241	
g0242	
g0243	
g0244	
g0245	
g0246	
g0247	
g0248	
g0249	
g0250	
g0251	
g0252	
g0253	
g0254	
g0255	
g0256	
g0257	
g0258	
g0259	
g0260	
g0261	
g0262	
g0263	
g0264	
g0265	
g0266	
g0267	
g0268	
g0269	
g0270	
g0271	
g0272	
g0273	
g0274	
g0275	
g0276	
g0277	
g0278	
g0279	
g0280	
g0281	
g0282	
g0283	
g0284	
g0285	
g0286	
g0287	
g0288	
g0289	
g0290	
g0291	
g0292	
g0293	
g0294	
g0295	
g0296	
g0297	
g0298	
g0299	
g0300	
g0301	
g0302	
g0303	
g0304	
g0305	
g0306	
g0307	
g0308	
g0309	
g0310	
g0311	
g0312	
g0313	
g0314	
g0315	
g0316	
g0317	
g0318	
g0319	
g0320	
g0321	
g0322	
g0323	
g0324	
g0325	
g0326	
g0327	
g0328	
g0329	
g0330	
g0331	
g0332	
g0333	
g0334	
g0335	
g0336	
g0337	
g0338	
g0339	
g0340	
g0341	
g0342	
g0343	
g0344	
g0345	
g0346	
g0347	
g0348	
g0349	
g0350	
g0351	
g0352	
g0353	
g0354	
g0355	
g0356	
g0357	
g0358	
g0359	
g0360	
```
