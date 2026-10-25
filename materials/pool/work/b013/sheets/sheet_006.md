# ラベル用シート 006 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_006.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0601（2 列）
- 見出し：AREA_SQM
- 例1 値：3.929 | 123.071 | 23.157 | 156.164 | 67.868
  - 同じ表の列：CLASS, BOATING_FA, BOATING__1, BOATING__2, FINISH, GRADE, POWER_SUPP, WATER_SUPP
- 例2 値：31.63 | 42.61 | 49.87 | 27.685 | 100.52
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, PLATFORM_FUNCTION, DECK_MATERIAL, SUBSTRUCTURE_MATERI…, HANDRAIL_TYPE

## g0602（1 列）
- 見出し：ASSET_POSI
- 例1 値：GPS | GPS | GPS | GPS | GPS
  - 同じ表の列：CLASS, BOATING_FA, BOATING__1, BOATING__2, FINISH, GRADE, POWER_SUPP, WATER_SUPP

## g0603（1 列）
- 見出し：SAPOBJECTID
- 例1 値：6000094308 | 6000094543 | 6000058610 | 6000094480 | 6000030719
  - 同じ表の列：CLASS, GIS_USER_STATUS, OBJECT_TYPE, PLATFORM_FUNCTION, DECK_MATERIAL, SUBSTRUCTURE_MATERI…, HANDRAIL_TYPE, MAXIMUM_HEIGHT

## g0604（1 列）
- 見出し：CLASS
- 例1 値：PLATFORM | PLATFORM | PLATFORM | PLATFORM | PLATFORM
  - 同じ表の列：SAPOBJECTID, GIS_USER_STATUS, OBJECT_TYPE, PLATFORM_FUNCTION, DECK_MATERIAL, SUBSTRUCTURE_MATERI…, HANDRAIL_TYPE, MAXIMUM_HEIGHT

## g0605（1 列）
- 見出し：GIS_USER_STATUS
- 例1 値：INSV | INSV | INSV | INSV | INSV
  - 同じ表の列：SAPOBJECTID, CLASS, OBJECT_TYPE, PLATFORM_FUNCTION, DECK_MATERIAL, SUBSTRUCTURE_MATERI…, HANDRAIL_TYPE, MAXIMUM_HEIGHT

## g0606（1 列）
- 見出し：OBJECT_TYPE
- 例1 値：PLTF | PLTF | PLTF | PLTF | PLTF
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, PLATFORM_FUNCTION, DECK_MATERIAL, SUBSTRUCTURE_MATERI…, HANDRAIL_TYPE, MAXIMUM_HEIGHT

## g0607（1 列）
- 見出し：PLATFORM_FUNCTION
- 例1 値：VIEWING | OTHER | OTHER | VIEWING | VIEWING
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, DECK_MATERIAL, SUBSTRUCTURE_MATERI…, HANDRAIL_TYPE, MAXIMUM_HEIGHT

## g0608（1 列）
- 見出し：DECK_MATERIAL
- 例1 値：TIMBER | TIMBER | CONCRETE | TIMBER | TIMBER
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, PLATFORM_FUNCTION, SUBSTRUCTURE_MATERI…, HANDRAIL_TYPE, MAXIMUM_HEIGHT

## g0609（1 列）
- 見出し：SUBSTRUCTURE_MATERIAL
- 例1 値：TIMBER | TIMBER | TIMBER | TIMBER | TIMBER
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, PLATFORM_FUNCTION, DECK_MATERIAL, HANDRAIL_TYPE, MAXIMUM_HEIGHT

## g0610（1 列）
- 見出し：HANDRAIL_TYPE
- 例1 値：timber post, timber infill | NA | timber post, timber infill | timber sless_rail wire_infill | timber post, timber infill
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, PLATFORM_FUNCTION, DECK_MATERIAL, SUBSTRUCTURE_MATERI…, MAXIMUM_HEIGHT

## g0611（1 列）
- 見出し：MAXIMUM_HEIGHT
- 例1 値：1 | 1 | 3 | 1 | 0.4
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, PLATFORM_FUNCTION, DECK_MATERIAL, SUBSTRUCTURE_MATERI…, HANDRAIL_TYPE

## g0612（3 列）
- 見出し：COGG
- 例1 値：Y | N | N | Y | Y
  - 同じ表の列：long, lat
- 例2 値：Y | N | N | N | N
  - 同じ表の列：long, lat

## g0613（1 列）
- 見出し：overlay
- 例1 値：HO309 | HO272 | HO259 | HO129 | HO308
  - 同じ表の列：heritage_bit, suburb, property_type, significance, estimated_build_date, property_id

## g0614（1 列）
- 見出し：heritage_bit
- 例1 値：part | part | part | part | part
  - 同じ表の列：overlay, suburb, property_type, significance, estimated_build_date, property_id

## g0615（4 列）
- 見出し：suburb
- 例1 値：Burnley | Richmond | Richmond | Richmond | Burnley
  - 同じ表の列：overlay, heritage_bit, property_type, significance, estimated_build_date, property_id
- 例2 値：Camperdown | Derrinallum | Timboon | Cobden | Lismore
  - 同じ表の列：assetType, lon, lat, fme_feature_type

## g0616（1 列）
- 見出し：property_type
- 例1 値：Howgate house | Metropolitan Gas Company Gas Inspector'… | New Australian Electric Lighting Co. Po… | State School No. 1490 | Corroboree Tree, Burnley Gardens
  - 同じ表の列：overlay, heritage_bit, suburb, significance, estimated_build_date, property_id

## g0617（1 列）
- 見出し：significance
- 例1 値：Contributory | Not contributory | Not contributory | Victorian Heritage Register | Victorian Heritage Register
  - 同じ表の列：overlay, heritage_bit, suburb, property_type, estimated_build_date, property_id

## g0618（1 列）
- 見出し：estimated_build_date
- 例1 値：1990-2000 | 1873-8 | 1861, 1939 | 1980-1990 | 1850-1890
  - 同じ表の列：overlay, heritage_bit, suburb, property_type, significance, property_id

## g0619（1 列）
- 見出し：property_id
- 例1 値：280160 | 160475 | 159310 | 159735 | 305860
  - 同じ表の列：overlay, heritage_bit, suburb, property_type, significance, estimated_build_date

## g0620（10 列）
- 見出し：lon
- 例1 値：144.9829515 | 144.9954896 | 144.983586 | 144.978063 | 144.9837522
  - 同じ表の列：lat, suburb, industry_code, industry_desc
- 例2 値：143.21947284 | 143.34192792 | 143.14458564 | 142.92339984 | 143.07697836
  - 同じ表の列：suburb, assetType, lat, fme_feature_type

## g0621（1 列）
- 見出し：industry_code
- 例1 値：4511 | 4511 | 4512 | 4129 | 4110
  - 同じ表の列：lat, lon, suburb, industry_desc

## g0622（1 列）
- 見出し：industry_desc
- 例1 値：Other Specialised Food Retailing | Cafes and Restaurants | Other Specialised Food Retailing | Cafes and Restaurants | Cafes and Restaurants
  - 同じ表の列：lat, lon, suburb, industry_code

## g0623（3 列）
- 見出し：assetType
- 例1 値：Kindergarten | Kindergarten | Kindergarten | Kindergarten | Kindergarten
  - 同じ表の列：suburb, lon, lat, fme_feature_type
- 例2 値：Hall | Hall | Hall | Hall | Hall
  - 同じ表の列：suburb, lon, lat, fme_feature_type

## g0624（3 列）
- 見出し：fme_feature_type
- 例1 値：dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings
  - 同じ表の列：suburb, assetType, lon, lat
- 例2 値：dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings
  - 同じ表の列：suburb, assetType, lon, lat

## g0625（1 列）
- 見出し：Mercer Consulting
- 例1 値：Galpins
  - 同じ表の列：Executive restructu…, CQR Australia Consu…, Data classification…, Dash Architects, Accommodation reloc…, Patricia Christie, Family Law Act pilo…, $44,250

## g0626（1 列）
- 見出し：Executive restructure and reclassification review
- 例1 値：Work, Health Safety & Injury Management…
  - 同じ表の列：Mercer Consulting, CQR Australia Consu…, Data classification…, Dash Architects, Accommodation reloc…, Patricia Christie, Family Law Act pilo…, $44,250

## g0627（1 列）
- 見出し：CQR Australia Consulting
- 例1 値：Galpins | ESS Pty Ltd | ESCIENT Pty Ltd
  - 同じ表の列：Mercer Consulting, Executive restructu…, Data classification…, Dash Architects, Accommodation reloc…, Patricia Christie, Family Law Act pilo…, $44,250

## g0628（1 列）
- 見出し：Data classification review
- 例1 値：Work, Health Safety & Injury Management… | New court system cloud position paper | Information technology strategic plan
  - 同じ表の列：Mercer Consulting, Executive restructu…, CQR Australia Consu…, Dash Architects, Accommodation reloc…, Patricia Christie, Family Law Act pilo…, $44,250

## g0629（1 列）
- 見出し：Dash Architects
- 例1 値：Wallis Nominees (Computing) Pty Ltd | SMS Consulting Group Ltd | Galpins
  - 同じ表の列：Mercer Consulting, Executive restructu…, CQR Australia Consu…, Data classification…, Accommodation reloc…, Patricia Christie, Family Law Act pilo…, $44,250

## g0630（1 列）
- 見出し：Accommodation relocation and compliance advice
- 例1 値：Network survey and cloud architecture | Integration Strategy | Work health & Safety compliance review
  - 同じ表の列：Mercer Consulting, Executive restructu…, CQR Australia Consu…, Data classification…, Dash Architects, Patricia Christie, Family Law Act pilo…, $44,250

## g0631（1 列）
- 見出し：Patricia Christie
- 例1 値：JRM Consulting | Escient Pty Ltd | ASG Group Limited | Mukurta Pty Ltd | Deloitte Risk Advisory Pty Ltd
  - 同じ表の列：Mercer Consulting, Executive restructu…, CQR Australia Consu…, Data classification…, Dash Architects, Accommodation reloc…, Family Law Act pilo…, $44,250

## g0632（1 列）
- 見出し：Family Law Act pilot scoping study; Review into wrongful det
- 例1 値：Library review | ECMS post implementation review - Proba… | ECMS quality assurance services; CAA re… | ECMS quality assurance services | Security review for ECMS Probate Implem…
  - 同じ表の列：Mercer Consulting, Executive restructu…, CQR Australia Consu…, Data classification…, Dash Architects, Accommodation reloc…, Patricia Christie, $44,250

## g0633（1 列）
- 見出し：$44,250
- 例1 値：$254,574 | $43,807 | $26,500 | $26,918 | $29,220
  - 同じ表の列：Mercer Consulting, Executive restructu…, CQR Australia Consu…, Data classification…, Dash Architects, Accommodation reloc…, Patricia Christie, Family Law Act pilo…

## g0634（1 列）
- 見出し：Jurisdiction
- 例1 値：Vic | NT | NSW | ACT | Qld
  - 同じ表の列：Year, Category, Management, Fate, Core or non-core

## g0635（1 列）
- 見出し：Category
- 例1 値：Glass | Organics | Paper & cardboard | Hazardous wastes | Textiles, leather & rubber (excl. tyres)
  - 同じ表の列：Year, Jurisdiction, Management, Fate, Core or non-core

## g0636（1 列）
- 見出し：Management
- 例1 値：Landfill | Recycling | Recycling | Recycling | Recycling
  - 同じ表の列：Year, Jurisdiction, Category, Fate, Core or non-core

## g0637（1 列）
- 見出し：Fate
- 例1 値：Energy recovery | Energy recovery | Recycling | Recycling | Disposal
  - 同じ表の列：Year, Jurisdiction, Category, Management, Core or non-core

## g0638（1 列）
- 見出し：Core or non-core
- 例1 値：Core waste | Core waste | Core waste | Core waste | Core waste
  - 同じ表の列：Year, Jurisdiction, Category, Management, Fate

## g0639（1 列）
- 見出し：Class_Type
- 例1 値：Year 2 / Year 3 | Year 1 / Year 2 / Year 3 | Reception / Year 1 / Year 2 | Average State | Reception / Year 1 / Year 2 / Year 3
  - 同じ表の列：2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021

## g0640（1 列）
- 見出し：2014
- 例1 値：18 | 24 | 24 | 19 | 23
  - 同じ表の列：Class_Type, 2015, 2016, 2017, 2018, 2019, 2020, 2021

## g0641（2 列）
- 見出し：Data as of
- 例1 値：10/05/2021 | 10/05/2021 | 10/05/2021 | 10/05/2021 | 10/05/2021
  - 同じ表の列：Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA
- 例2 値：6/06/2021 | 6/06/2021 | 6/06/2021 | 6/06/2021 | 6/06/2021
  - 同じ表の列：Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA

## g0642（2 列）
- 見出し：Licence No
- 例1 値：LIQC300235068 | LIQC300241955 | LIQC300230643 | LIQC300228975 | LIQC300239705
  - 同じ表の列：Data as of, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA
- 例2 値：LIQC300242285 | LIQC300237079 | LIQC300240479 | LIQC300238342 | LIQC300200108
  - 同じ表の列：Data as of, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA

## g0643（2 列）
- 見出し：Start Date
- 例1 値：20/10/1948 | 10/12/1947 | 24/09/1952 | 8/06/1955 | 27/07/1964
  - 同じ表の列：Data as of, Licence No, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA
- 例2 値：10/03/1967 | 6/07/1956 | 18/05/1955 | 7/04/1955 | 5/06/1957
  - 同じ表の列：Data as of, Licence No, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA

## g0644（2 列）
- 見出し：Trading Status
- 例1 値：Trading | Trading | Trading | Trading | Trading
  - 同じ表の列：Data as of, Licence No, Start Date, Type, Filter Category, SA2 Band, Subject to Cap, LGA
- 例2 値：Trading | Trading | Trading | Trading | Trading
  - 同じ表の列：Data as of, Licence No, Start Date, Type, Filter Category, SA2 Band, Subject to Cap, LGA

## g0645（3 列）
- 見出し：Type
- 例1 値：club | club | club | club | club
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Filter Category, SA2 Band, Subject to Cap, LGA
- 例2 値：Club | Club | Club | Club | Club
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Filter Category, SA2 Band, Subject to Cap, LGA

## g0646（1 列）
- 見出し：Filter Category
- 例1 値：Club - medium | Club - non gaming | Club - medium | Club - medium | Club - small
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, SA2 Band, Subject to Cap, LGA

## g0647（1 列）
- 見出し：SA2 Band
- 例1 値：3 | 1 | 3 | 2 | 1
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, Subject to Cap, LGA

## g0648（1 列）
- 見出し：Subject to Cap
- 例1 値：No | Yes | No | No | No
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, LGA

## g0649（1 列）
- 見出し：LGA
- 例1 値：Ku-ring-gai Council | Warrumbungle Shire Council | Willoughby City Council | Shoalhaven City Council | Inner West Council
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap

## g0650（1 列）
- 見出し：Region
- 例1 値：Country | Country | Country | Country | Country
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap

## g0651（1 列）
- 見出し：Filter Category
- 例1 値：Club- medium | Club- medium | Club - non-gaming | Club - non-gaming | Club- medium
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, SA2 Band, Subject to Cap, LGA

## g0652（1 列）
- 見出し：SA2 Band
- 例1 値：TENTERFIELD | Tamworth - West | Cronulla - Kurnell - Bundeena | WINDALE | WINGHAM
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, Subject to Cap, LGA

## g0653（1 列）
- 見出し：Subject to Cap
- 例1 値：1 | 1 | 1 | 2 | 3
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, LGA

## g0654（1 列）
- 見出し：LGA
- 例1 値：No | No | Yes | No | Yes
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap

## g0655（1 列）
- 見出し：Region
- 例1 値：Central Coast Council | Council of the City of Sydney | Northern Beaches Council | Kyogle Council | Northern Beaches Council
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap

## g0656（1 列）
- 見出し：DN
- 例1 値：ou=Australian Public Service Commission… | ou=Australian Border Force,ou=Departmen… | ou=Remuneration Tribunal Secretariat,ou… | ou=Australian Institute of Family Studi… | ou=Medibank Health Solutions Pty Ltd,ou…
  - 同じ表の列：Report URI

## g0657（1 列）
- 見出し：Report URI
- 例1 値：http://directory.gov.au/reports/departm… | http://directory.gov.au/reports/departm… | http://directory.gov.au/reports/departm… | http://directory.gov.au/reports/departm… | http://directory.gov.au/reports/departm…
  - 同じ表の列：DN

## g0658（1 列）
- 見出し：NGO Organisation
- 例1 値：Lifeline South East (SA) | Milang Old School House Community Centr… | Port Augusta Youth Centre Total | UnitingCare Wesley Bowden | Gawler Community House Total
  - 同じ表の列：Region, Strategy, Base Funding $ per …

## g0659（1 列）
- 見出し：Region
- 例1 値：Yorke & Mid North | Eastern Adelaide | Western Adelaide | Eastern Adelaide | Northern Adelaide
  - 同じ表の列：NGO Organisation, Strategy, Base Funding $ per …

## g0660（1 列）
- 見出し：Strategy
- 例1 値：Community Neighbourhood & Development | Family Support & Early Intervention | Low Income Support | Community Neighbourhood & Development | Family Support & Early Intervention
  - 同じ表の列：NGO Organisation, Region, Base Funding $ per …

## g0661（1 列）
- 見出し：Base Funding $ per annum
- 例1 値：$283,129 | $73,038 | $97,036 | $516,483 | $104,340
  - 同じ表の列：NGO Organisation, Region, Strategy

## g0662（1 列）
- 見出し：CODE_OF_ORIGIN
- 例1 値：259 | 161 | 228 | 450 | 260
  - 同じ表の列：COUNTRY_OR_STATE, CATEGORY, METRO, RURAL, OTHER

## g0663（1 列）
- 見出し：COUNTRY_OR_STATE
- 例1 値：ERITREA | PERU | MOROCCO | IRAQ | GHANA
  - 同じ表の列：CODE_OF_ORIGIN, CATEGORY, METRO, RURAL, OTHER

## g0664（1 列）
- 見出し：METRO
- 例1 値：65 | 26 | 1 | 1 | 1
  - 同じ表の列：CODE_OF_ORIGIN, COUNTRY_OR_STATE, CATEGORY, RURAL, OTHER

## g0665（1 列）
- 見出し：RURAL
- 例1 値：176 | 9 | 1 | 183 | 2
  - 同じ表の列：CODE_OF_ORIGIN, COUNTRY_OR_STATE, CATEGORY, METRO, OTHER

## g0666（1 列）
- 見出し：Business Category
- 例1 値：Recreation Group | Recreation Group | Recreation Group | Recreation Group | Orienteering Club,Recreation Group,Walk…
  - 同じ表の列：Suburb, State, LGA, Region

## g0667（1 列）
- 見出し：LGA
- 例1 値：Port Phillip | Mildura Rural | Greater Dandenong (C) | Wyndham ; Melton ; Brimbank | Ballarat
  - 同じ表の列：Suburb, State, Business Category, Region

## g0668（1 列）
- 見出し：Region
- 例1 値：Eastern Metro | Southern Metro | Eastern Metro | Loddon-Mallee, Grampians | North and West Metropolitan Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0669（1 列）
- 見出し：Title
- 例1 値：Brunswick Library | Bacchus Marsh Library | Community Information Diamond Valley | Maryborough Library | Wodonga Senior Secondary College
  - 同じ表の列：Suburb, State, Cost, Bookings, Opening_Hours_Mon_O…, Opening_Hours_Mon_C…, Opening_Hours_Tue_O…, Opening_Hours_Tue_C…

## g0670（1 列）
- 見出し：Cost
- 例1 値：Free Access | Free Access | Free Access | $4 per hour | Free Access
  - 同じ表の列：Title, Suburb, State, Bookings, Opening_Hours_Mon_O…, Opening_Hours_Mon_C…, Opening_Hours_Tue_O…, Opening_Hours_Tue_C…

## g0671（1 列）
- 見出し：Bookings
- 例1 値：Yes | Yes | Yes | Yes | No
  - 同じ表の列：Title, Suburb, State, Cost, Opening_Hours_Mon_O…, Opening_Hours_Mon_C…, Opening_Hours_Tue_O…, Opening_Hours_Tue_C…

## g0672（1 列）
- 見出し：Opening_Hours_Mon_Open
- 例1 値：10:00AM | 09:00AM | 09:00AM | 10:00AM | 02:00PM
  - 同じ表の列：Title, Suburb, State, Cost, Bookings, Opening_Hours_Mon_C…, Opening_Hours_Tue_O…, Opening_Hours_Tue_C…

## g0673（1 列）
- 見出し：Opening_Hours_Mon_Close
- 例1 値：05:00PM | 04:00PM | 03:00PM | 6:00PM | 05:00PM
  - 同じ表の列：Title, Suburb, State, Cost, Bookings, Opening_Hours_Mon_O…, Opening_Hours_Tue_O…, Opening_Hours_Tue_C…

## g0674（1 列）
- 見出し：Opening_Hours_Tue_Open
- 例1 値：1:00PM | 10:00AM | 05:00AM | 9:00AM | 10:00AM
  - 同じ表の列：Title, Suburb, State, Cost, Bookings, Opening_Hours_Mon_O…, Opening_Hours_Mon_C…, Opening_Hours_Tue_C…

## g0675（1 列）
- 見出し：Opening_Hours_Tue_Close
- 例1 値：08:00PM | 12:00AM | 04:00PM | 09:00PM | 3:30PM
  - 同じ表の列：Title, Suburb, State, Cost, Bookings, Opening_Hours_Mon_O…, Opening_Hours_Mon_C…, Opening_Hours_Tue_O…

## g0676（1 列）
- 見出し：Opening_Hours_Wen_Open
- 例1 値：1.00PM | 09:00AM | 8:30am | 9:00AM | 02:00PM
  - 同じ表の列：Title, Suburb, State, Cost, Bookings, Opening_Hours_Mon_O…, Opening_Hours_Mon_C…, Opening_Hours_Tue_O…

## g0677（3 列）
- 見出し：Locality
- 例1 値：Smythesdale | Inverleigh | Rokewood | Bannockburn | Rokewood
  - 同じ表の列：ID, GPSC, OperatedBy, Programs, Operating
- 例2 値：Inverleigh | Lethbridge | Inverleigh | Murgheboluc | Bannockburn
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Post_Code, Home_Clubs, LAT

## g0678（1 列）
- 見出し：GPSC
- 例1 値：t | t | t | t | t
  - 同じ表の列：ID, Locality, OperatedBy, Programs, Operating

## g0679（1 列）
- 見出し：OperatedBy
- 例1 値：Golden Plains Shire Council | Golden Plains Shire Council | Golden Plains Shire Council | Golden Plains Shire Council | Golden Plains Shire Council
  - 同じ表の列：ID, Locality, GPSC, Programs, Operating

## g0680（1 列）
- 見出し：Programs
- 例1 値：Maternal and Child Health | Maternal and Child Health | Maternal and Child Health | Maternal and Child Health | Maternal and Child Health
  - 同じ表の列：ID, Locality, GPSC, OperatedBy, Operating

## g0681（1 列）
- 見出し：Operating
- 例1 値：Tuesdays and every 2nd Thurs (2nd & 4th… | Not yet active - the Rokewood service w… | Thursday fortnightly 1st & 3rd week | Monday and Friday, new parent group eac… | Thursday fortnightly 1st & 3rd week
  - 同じ表の列：ID, Locality, GPSC, OperatedBy, Programs

## g0682（1 列）
- 見出し：Complex_Type
- 例1 値：Recreation Reserve | Recreation Reserve | Recreation Reserve | Recreation Reserve | Recreation Reserve
  - 同じ表の列：Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs, LAT

## g0683（2 列）
- 見出し：Facility_Type
- 例1 値：Oval | Oval | Oval | Oval | Oval
  - 同じ表の列：Complex_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs, LAT
- 例2 値：Playground | Playground | Playground | Playground | Playground
  - 同じ表の列：Complex_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs, LAT

## g0684（1 列）
- 見出し：Bookable_Item
- 例1 値：Shelford Recreation Reserve Oval | Lethbridge Recreation Reserve Oval 1 | Haddon Recreation Reserve Oval | Teesdale Oval | Bannockburn Victoria Park Recreation Re…
  - 同じ表の列：Complex_Type, Facility_Type, Assessment_No, Number, Locality, Post_Code, Home_Clubs, LAT

## g0685（2 列）
- 見出し：Assessment_No
- 例1 値：41400011 | 36600007 | 66379102 | 41400011 | 41400035
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Number, Locality, Post_Code, Home_Clubs, LAT
- 例2 値：91000665 | 91000207 | 91000723 | 91001669 | 54005014
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Number, Locality, Post_Code, Home_Clubs, LAT

## g0686（2 列）
- 見出し：Number
- 例1 値：396 | 1164 | 14 | 17 | 8
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Locality, Post_Code, Home_Clubs, LAT
- 例2 値：14 | 3 | 1164 | 9 | 12
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Locality, Post_Code, Home_Clubs, LAT

## g0687（2 列）
- 見出し：Post_Code
- 例1 値：3321 | 3332 | 3351 | 3321 | 3331
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Home_Clubs, LAT
- 例2 値：3332 | 3351 | 3351 | 3328 | 3352
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Home_Clubs, LAT

## g0688（1 列）
- 見出し：Home_Clubs
- 例1 値：NIL
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, LAT

## g0689（1 列）
- 見出し：Complex_Type
- 例1 値：Public Open Space | Recreation Reserve | Public Open Space | Public Open Space | Public Open Space
  - 同じ表の列：Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs, LAT

## g0690（1 列）
- 見出し：Bookable_Item
- 例1 値：Maude Recreation Reserve Playground | Linton Recreation Reserve Playground | Murgheboluc Recreation Reserve Playgrou… | Inverleigh Tennis Reserve Playground | Dereel Hall & Recreation Centre Playgro…
  - 同じ表の列：Complex_Type, Facility_Type, Assessment_No, Number, Locality, Post_Code, Home_Clubs, LAT

## g0691（1 列）
- 見出し：Locality
- 例1 値：Sutherlands Creek | Ross Creek | Cape Clear | Lethbridge | Smythesdale
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Post_Code, Home_Clubs, LAT

## g0692（1 列）
- 見出し：Home_Clubs
- 例1 値：Sutherlands Creek Tennis Club
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, LAT

## g0693（1 列）
- 見出し：num_of
- 例1 値：1 | 57 | 1 | 1 | 1
  - 同じ表の列：ref, material, accessible

## g0694（1 列）
- 見出し：accessible
- 例1 値：No | No | No | Not Applicable | No
  - 同じ表の列：ref, num_of, material

## g0695（1 列）
- 見出し：genus
- 例1 値：Lophostemon | Prunus | Eucalyptus | Eucalyptus | Ulmus
  - 同じ表の列：lat, lon, species, dbh, dbh_min, dbh_max, crown, crown_min

## g0696（1 列）
- 見出し：species
- 例1 値：Citriodora | Styphelioides | Excelsior | X Blireana | Negundo 'Sensation'
  - 同じ表の列：lat, lon, genus, dbh, dbh_min, dbh_max, crown, crown_min

## g0697（1 列）
- 見出し：dbh
- 例1 値：15.5 | 15.5 | 5 | 40.5 | 15.5
  - 同じ表の列：lat, lon, genus, species, dbh_min, dbh_max, crown, crown_min

## g0698（1 列）
- 見出し：dbh_min
- 例1 値：0 | 0 | 11 | 31 | 11
  - 同じ表の列：lat, lon, genus, species, dbh, dbh_max, crown, crown_min

## g0699（1 列）
- 見出し：dbh_max
- 例1 値：70 | 10 | 10 | 30 | 10
  - 同じ表の列：lat, lon, genus, species, dbh, dbh_min, crown, crown_min

## g0700（1 列）
- 見出し：crown
- 例1 値：2.5 | 35.5 | 2.5 | 8 | 8
  - 同じ表の列：lat, lon, genus, species, dbh, dbh_min, dbh_max, crown_min

## g0701（2 列）
- 見出し：crown_min
- 例1 値：0 | 6 | 0 | 6 | 6
  - 同じ表の列：lat, lon, genus, species, dbh, dbh_min, dbh_max, crown
- 例2 値：10 | 8 | 9 | 10 | 15
  - 同じ表の列：lat, lon, species, common, dbh, crown, crown_max, height

## g0702（2 列）
- 見出し：crown_max
- 例1 値：5 | 5 | 10 | 10 | 5
  - 同じ表の列：lat, lon, genus, species, dbh, dbh_min, dbh_max, crown
- 例2 値：9 | 14 | 14 | 14 | 7
  - 同じ表の列：lat, lon, species, common, dbh, crown, crown_min, height

## g0703（1 列）
- 見出し：links
- 例1 値：http://libraries.hobsonsbay.vic.gov.au/… | http://libraries.hobsonsbay.vic.gov.au/… | http://libraries.hobsonsbay.vic.gov.au/… | http://libraries.hobsonsbay.vic.gov.au/… | http://libraries.hobsonsbay.vic.gov.au/…
  - 同じ表の列：suburb

## g0704（1 列）
- 見出し：Location
- 例1 値：Newport Lakes, South-western section | Doug Grant Reserve Altona | Bladin Street Reserve Laverton | Williamstown Beach | Doug Grant Reserve Altona
  - 同じ表の列：Id, Dog_Restrictions

## g0705（1 列）
- 見出し：Dog_Restrictions
- 例1 値：Off-lead: Unrestricted | Off-lead: Unrestricted | On-lead: All times | Off-lead: Unrestricted | Off-lead: Unrestricted
  - 同じ表の列：Id, Location

## g0706（1 列）
- 見出し：Month Year
- 例1 値：May-26 | Sep-24 | Dec-25 | Jun-24 | Jul-25
  - 同じ表の列：Site Type, EGM Range, Operational EGMs, Operational Sites

## g0707（1 列）
- 見出し：Site Type
- 例1 値：Hotel | Hotel | Club | Hotel | Club
  - 同じ表の列：Month Year, EGM Range, Operational EGMs, Operational Sites

## g0708（1 列）
- 見出し：EGM Range
- 例1 値：41 to 100 | 6 to 10 | 41 to 45 | 41 to 100 | 11 to 20
  - 同じ表の列：Month Year, Site Type, Operational EGMs, Operational Sites

## g0709（1 列）
- 見出し：Operational EGMs
- 例1 値：2872 | 5503 | 5463 | 5923 | 1050
  - 同じ表の列：Month Year, Site Type, EGM Range, Operational Sites

## g0710（1 列）
- 見出し：Operational Sites
- 例1 値：63 | 217 | 40 | 215 | 37
  - 同じ表の列：Month Year, Site Type, EGM Range, Operational EGMs

## g0711（1 列）
- 見出し：DEPARTURE_PORT
- 例1 値：Launceston | Launceston | Hobart | Launceston | Hobart
  - 同じ表の列：DEPARTURE_DATE, SHIP, BOUND, YEAR, SHIP_TO_COLONY, REMARKS

## g0712（1 列）
- 見出し：DEPARTURE_DATE
- 例1 値：1846-05-01T00:00:00 | 1824-03-28T00:00:00 | 1846-03-19T00:00:00 | 1852-04-29T00:00:00 | 1852-05-21T00:00:00
  - 同じ表の列：DEPARTURE_PORT, SHIP, BOUND, YEAR, SHIP_TO_COLONY, REMARKS

## g0713（1 列）
- 見出し：SHIP
- 例1 値：Velocity | Raven | Water Witch | Peri | Raven
  - 同じ表の列：DEPARTURE_PORT, DEPARTURE_DATE, BOUND, YEAR, SHIP_TO_COLONY, REMARKS

## g0714（1 列）
- 見出し：BOUND
- 例1 値：Mauritius | Port Phillip | Melbourne | Port Albert | Whaling Voyage
  - 同じ表の列：DEPARTURE_PORT, DEPARTURE_DATE, SHIP, YEAR, SHIP_TO_COLONY, REMARKS

## g0715（1 列）
- 見出し：SHIP_TO_COLONY
- 例1 値：Antares | Yarra Yarra | William Metcalfe | Persian | Mariposa
  - 同じ表の列：DEPARTURE_PORT, DEPARTURE_DATE, SHIP, BOUND, YEAR, REMARKS

## g0716（1 列）
- 見出し：REMARKS
- 例1 値：Family of Mr. and Mrs. Abbott | Probably Joseph Ackroyd | Convict of this name not known | Child of Mr and Mrs Absey | Lascar
  - 同じ表の列：DEPARTURE_PORT, DEPARTURE_DATE, SHIP, BOUND, YEAR, SHIP_TO_COLONY

## g0717（1 列）
- 見出し：date1
- 例1 値：7/07/2008 | 13/06/2008 | 27/06/2008 | 10/06/2008 | 30/06/2008
  - 同じ表の列：house, str_type, suburb, pcode, alphatree, species, height, dbh

## g0718（1 列）
- 見出し：house
- 例1 値：55 | 20 | 22 | 10-12 | 699
  - 同じ表の列：date1, str_type, suburb, pcode, alphatree, species, height, dbh

## g0719（1 列）
- 見出し：str_type
- 例1 値：Rd | Gr | Crt | Dr | Rd
  - 同じ表の列：date1, house, suburb, pcode, alphatree, species, height, dbh

## g0720（2 列）
- 見出し：pcode
- 例1 値：3109 | 3109 | 3109 | 3109 | 3108
  - 同じ表の列：date1, house, str_type, suburb, alphatree, species, height, dbh
- 例2 値：2106 | 2070 | 2223 | 2736 | 2539
  - 同じ表の列：OBJECTID, Operator, Number_of_plugs, Charger_Type, Charger_rating, Source

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
