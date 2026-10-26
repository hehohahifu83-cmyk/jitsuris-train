# ラベル用シート 001 / 002

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：State
- 例1 値：SA | NT | QLD | VIC | QLD
  - 同じ表の列：Station, Town, Talkback-number, Fax-number, Sms-number, PO-box, PO-suburb, Twitter
- 例2 値：SA | SA | SA | SA | SA
  - 同じ表の列：Agency, Subcategory, Suburb, Post Code, Country, Great Circle Distan…, Great Circle Distan…, X Region

## g0002（1 列）
- 見出し：Station
- 例1 値：ABC Riverina | ABC Mildura - Swan Hill | ABC North Coast | ABC Northern Tasmania | ABC Central Victoria
  - 同じ表の列：State, Town, Talkback-number, Fax-number, Sms-number, PO-box, PO-suburb, Twitter

## g0003（1 列）
- 見出し：Town
- 例1 値：Bundaberg | Gosford | Alice Springs | Wodonga | Mildura
  - 同じ表の列：State, Station, Talkback-number, Fax-number, Sms-number, PO-box, PO-suburb, Twitter

## g0004（1 列）
- 見出し：Talkback-number
- 例1 値：1300 747 222 | 1300 222 720 | 1300 925 222 | 1300 160 222 | 1300 147 222
  - 同じ表の列：State, Station, Town, Fax-number, Sms-number, PO-box, PO-suburb, Twitter

## g0005（1 列）
- 見出し：Fax-number
- 例1 値：07 4924 5199 | (08) 8638 4899 | 02 6627 2099 | 08 9083 2099 | 02 49 221 222
  - 同じ表の列：State, Station, Town, Talkback-number, Sms-number, PO-box, PO-suburb, Twitter

## g0006（1 列）
- 見出し：Sms-number
- 例1 値：0467 842 722 | 0467 922 891 | 0487 991 057 | 0467 922 783 | 0467 922 684
  - 同じ表の列：State, Station, Town, Talkback-number, Fax-number, PO-box, PO-suburb, Twitter

## g0007（1 列）
- 見出し：PO-box
- 例1 値：PO Box 318 | GPO Box 9994 | PO Box 7 | PO Box 42 | GPO Box 9994
  - 同じ表の列：State, Station, Town, Talkback-number, Fax-number, Sms-number, PO-suburb, Twitter

## g0008（1 列）
- 見出し：PO-suburb
- 例1 値：Wodonga | Bunbury | Kalgoorlie | Perth | Launceston
  - 同じ表の列：State, Station, Town, Talkback-number, Fax-number, Sms-number, PO-box, Twitter

## g0009（1 列）
- 見出し：Twitter
- 例1 値：abcsouthqld | abcgm | ABCMilduraSwanH | 891adelaide | abcwesternvic
  - 同じ表の列：State, Station, Town, Talkback-number, Fax-number, Sms-number, PO-box, PO-suburb

## g0010（1 列）
- 見出し：Facebook
- 例1 値：http://www.facebook.com/abcballaratands… | http://www.facebook.com/ABCSouthernQuee… | http://www.facebook.com/pages/ABC-South… | http://www.facebook.com/pages/1057-ABC-… | http://www.facebook.com/pages/ABC-Goulb…
  - 同じ表の列：State, Station, Town, Talkback-number, Fax-number, Sms-number, PO-box, PO-suburb

## g0011（1 列）
- 見出し：FL/EQ No
- 例1 値：F-ADNERA-ADNGMN | F-ADNERA-ADNGMN | F-ADNERA-ADNGMN | F-ADNERA-ADNGMN | F-ADNERA-ADNGMN
  - 同じ表の列：FL/EQ Desc, Occurence ID, Floor ID, Survey ID, FL/EQ Ind, Sample Analysis Date, Analysis Type, Asset

## g0012（1 列）
- 見出し：FL/EQ Desc
- 例1 値：NERANG ADMIN | NERANG ADMIN | NERANG ADMIN | NERANG ADMIN | NERANG ADMIN
  - 同じ表の列：FL/EQ No, Occurence ID, Floor ID, Survey ID, FL/EQ Ind, Sample Analysis Date, Analysis Type, Asset

## g0013（1 列）
- 見出し：Occurence ID
- 例1 値：2907 | 2910 | 2889 | 2894 | 2892
  - 同じ表の列：FL/EQ No, FL/EQ Desc, Floor ID, Survey ID, FL/EQ Ind, Sample Analysis Date, Analysis Type, Asset

## g0014（1 列）
- 見出し：Floor ID
- 例1 値：GROUND FLOOR | GROUND FLOOR | BASEMENT 1 | BASEMENT 1 | LEVEL 1
  - 同じ表の列：FL/EQ No, FL/EQ Desc, Occurence ID, Survey ID, FL/EQ Ind, Sample Analysis Date, Analysis Type, Asset

## g0015（1 列）
- 見出し：Survey ID
- 例1 値：2899 | 2898 | 2914 | 4618 | 2891
  - 同じ表の列：FL/EQ No, FL/EQ Desc, Occurence ID, Floor ID, FL/EQ Ind, Sample Analysis Date, Analysis Type, Asset

## g0016（1 列）
- 見出し：FL/EQ Ind
- 例1 値：Functional Location | Functional Location | Functional Location | Functional Location | Functional Location
  - 同じ表の列：FL/EQ No, FL/EQ Desc, Occurence ID, Floor ID, Survey ID, Sample Analysis Date, Analysis Type, Asset

## g0017（1 列）
- 見出し：Sample Analysis Date
- 例1 値：8/04/2010 | 8/04/2010 | 8/04/2010
  - 同じ表の列：FL/EQ No, FL/EQ Desc, Occurence ID, Floor ID, Survey ID, FL/EQ Ind, Analysis Type, Asset

## g0018（1 列）
- 見出し：Analysis Type
- 例1 値：PLM + DS | PLM + DS | PLM + DS | PLM + DS | PLM + DS
  - 同じ表の列：FL/EQ No, FL/EQ Desc, Occurence ID, Floor ID, Survey ID, FL/EQ Ind, Sample Analysis Date, Asset

## g0019（1 列）
- 見出し：Asset
- 例1 値：20008251 | 20008251 | 20008251 | 20008251 | 20008251
  - 同じ表の列：FL/EQ No, FL/EQ Desc, Occurence ID, Floor ID, Survey ID, FL/EQ Ind, Sample Analysis Date, Analysis Type

## g0020（1 列）
- 見出し：Application
- 例1 値：FIRE DOOR | FIRE DOOR | FIRE DOOR | CEILING LINING | WALL LINING
  - 同じ表の列：FL/EQ No, FL/EQ Desc, Occurence ID, Floor ID, Survey ID, FL/EQ Ind, Sample Analysis Date, Analysis Type

## g0021（1 列）
- 見出し：Library
- 例1 値：Corio | Geelong | Chilwell | Ocean Grove | Mobile Libraries
  - 同じ表の列：LGA, Long, Lat, FloorSpace(m2), OpeningHours(perwee…

## g0022（1 列）
- 見出し：LGA
- 例1 値：City of Greater Geelong | City of Greater Geelong | City of Greater Geelong | City of Greater Geelong | City of Greater Geelong
  - 同じ表の列：Library, Long, Lat, FloorSpace(m2), OpeningHours(perwee…

## g0023（1 列）
- 見出し：Long
- 例1 値：144.3556703 | 144.327897 | 144.3162487 | 144.3437481 | 144.6613501
  - 同じ表の列：Library, LGA, Lat, FloorSpace(m2), OpeningHours(perwee…

## g0024（1 列）
- 見出し：Lat
- 例1 値：-38.1698708 | -38.12479 | -38.2810499 | -38.15711673 | -38.17489473
  - 同じ表の列：Library, LGA, Long, FloorSpace(m2), OpeningHours(perwee…

## g0025（1 列）
- 見出し：FloorSpace(m2)
- 例1 値：600 | 380 | 603 | 443 | 180
  - 同じ表の列：Library, LGA, Long, Lat, OpeningHours(perwee…

## g0026（1 列）
- 見出し：OpeningHours(perweek)
- 例1 値：44.5 | 49 | 50 | 36.5 | 45.5
  - 同じ表の列：Library, LGA, Long, Lat, FloorSpace(m2)

## g0027（1 列）
- 見出し：census_year
- 例1 値：2007 | 2007 | 2007 | 2008 | 2007
  - 同じ表の列：property_id, base_property_id, clue_small_area, industry_anzsic4_co…, seating_type, number_of_seats, location

## g0028（1 列）
- 見出し：property_id
- 例1 値：103942 | 103187 | 102063 | 101204 | 110717
  - 同じ表の列：census_year, base_property_id, clue_small_area, industry_anzsic4_co…, seating_type, number_of_seats, location

## g0029（1 列）
- 見出し：base_property_id
- 例1 値：103507 | 101142 | 101142 | 108093 | 101154
  - 同じ表の列：census_year, property_id, clue_small_area, industry_anzsic4_co…, seating_type, number_of_seats, location

## g0030（1 列）
- 見出し：clue_small_area
- 例1 値：Melbourne (CBD) | Melbourne (CBD) | Melbourne (CBD) | Melbourne (CBD) | South Yarra
  - 同じ表の列：census_year, property_id, base_property_id, industry_anzsic4_co…, seating_type, number_of_seats, location

## g0031（1 列）
- 見出し：industry_anzsic4_code
- 例1 値：4511 | 4511 | 4511 | 4511 | 4511
  - 同じ表の列：census_year, property_id, base_property_id, clue_small_area, seating_type, number_of_seats, location

## g0032（1 列）
- 見出し：seating_type
- 例1 値：Seats - Indoor | Seats - Outdoor | Seats - Indoor | Seats - Indoor | Seats - Outdoor
  - 同じ表の列：census_year, property_id, base_property_id, clue_small_area, industry_anzsic4_co…, number_of_seats, location

## g0033（1 列）
- 見出し：number_of_seats
- 例1 値：65 | 36 | 80 | 60 | 71
  - 同じ表の列：census_year, property_id, base_property_id, clue_small_area, industry_anzsic4_co…, seating_type, location

## g0034（1 列）
- 見出し：location
- 例1 値：-37.81970334, 144.957970182 | -37.81137862, 144.971698403 | -37.81311056, 144.96797783 | -37.81867684, 144.954359995 | -37.8170965, 144.96683471
  - 同じ表の列：census_year, property_id, base_property_id, clue_small_area, industry_anzsic4_co…, seating_type, number_of_seats

## g0035（1 列）
- 見出し：number
- 例1 値：11.6 | 6.4 | 10.6 | 9.3 | 20.1
  - 同じ表の列：indicator_theme, indicator_variable, indicator_descriptor, type, greater_melbourne_v…, greater_melbourne_y…, greater_melbourne_u…, melbourne_municipal…

## g0036（1 列）
- 見出し：indicator_theme
- 例1 値：Solid Waste | Wastewater | Fire and Emergency Response | Education | Finance
  - 同じ表の列：number, indicator_variable, indicator_descriptor, type, greater_melbourne_v…, greater_melbourne_y…, greater_melbourne_u…, melbourne_municipal…

## g0037（1 列）
- 見出し：indicator_variable
- 例1 値：Disposal by Other | Voter Participation Rate | Improved Sanitation Access | Number of Registered Voters | Number of Fire-Related Deaths
  - 同じ表の列：number, indicator_theme, indicator_descriptor, type, greater_melbourne_v…, greater_melbourne_y…, greater_melbourne_u…, melbourne_municipal…

## g0038（1 列）
- 見出し：indicator_descriptor
- 例1 値：Percentage of the city's solid waste th… | Percentage of commuters using a travel … | Energy (electricity) consumption of pub… | Percentage of the city's solid waste th… | Number of cell phone connections per 10…
  - 同じ表の列：number, indicator_theme, indicator_variable, type, greater_melbourne_v…, greater_melbourne_y…, greater_melbourne_u…, melbourne_municipal…

## g0039（2 列）
- 見出し：type
- 例1 値：Supporting | Supporting | Core | Supporting | Core
  - 同じ表の列：number, indicator_theme, indicator_variable, indicator_descriptor, greater_melbourne_v…, greater_melbourne_y…, greater_melbourne_u…, melbourne_municipal…
- 例2 値：Liveability | Social | Liveability | Liveability | Liveability
  - 同じ表の列：topic, id, indicator, period, numerator, denominator, value, value_type

## g0040（1 列）
- 見出し：greater_melbourne_value
- 例1 値：100.0 | 100.0 | 15.1977 | 156.88 | 349.7489
  - 同じ表の列：number, indicator_theme, indicator_variable, indicator_descriptor, type, greater_melbourne_y…, greater_melbourne_u…, melbourne_municipal…

## g0041（1 列）
- 見出し：greater_melbourne_year
- 例1 値：2010 | 2014 | 2014 | 2013 | 2013
  - 同じ表の列：number, indicator_theme, indicator_variable, indicator_descriptor, type, greater_melbourne_v…, greater_melbourne_u…, melbourne_municipal…

## g0042（1 列）
- 見出し：greater_melbourne_units
- 例1 値：?g/m3 | % | % | /100 000 | min
  - 同じ表の列：number, indicator_theme, indicator_variable, indicator_descriptor, type, greater_melbourne_v…, greater_melbourne_y…, melbourne_municipal…

## g0043（1 列）
- 見出し：melbourne_municipality_value
- 例1 値：5024.5894 | 58.5449 | 0.0 | 20.9427 | 38.8065
  - 同じ表の列：number, indicator_theme, indicator_variable, indicator_descriptor, type, greater_melbourne_v…, greater_melbourne_y…, greater_melbourne_u…

## g0044（1 列）
- 見出し：melbourne_municipality_year
- 例1 値：2011 | 2014 | 2015 | 2015 | 2010
  - 同じ表の列：number, indicator_theme, indicator_variable, indicator_descriptor, type, greater_melbourne_v…, greater_melbourne_y…, greater_melbourne_u…

## g0045（1 列）
- 見出し：topic
- 例1 値：Profile - people | Water, energy and environment | Profile - people | Recreation and urban planning | Water, energy and environment
  - 同じ表の列：type, id, indicator, period, numerator, denominator, value, value_type

## g0046（1 列）
- 見出し：id
- 例1 値：ACT_4 | FIRE_1 | WAT_5 | ECO_4 | PHYS_1
  - 同じ表の列：type, topic, indicator, period, numerator, denominator, value, value_type

## g0047（1 列）
- 見出し：indicator
- 例1 値：Square metres of public indoor recreati… | Own-source revenue as a percentage of t… | Number of mental health practitioners p… | Subjective Wellbeing: Residents' satisf… | Kilometres of light passenger public tr…
  - 同じ表の列：type, topic, id, period, numerator, denominator, value, value_type

## g0048（1 列）
- 見出し：period
- 例1 値：2016 (at 30 June) | 2018 | 2018 | FY 202013/14 | 2018 (at 30 June)
  - 同じ表の列：type, topic, id, indicator, numerator, denominator, value, value_type

## g0049（1 列）
- 見出し：numerator
- 例1 値：N/A | 1,343.01 | 210,588 | N/A | 46,353
  - 同じ表の列：type, topic, id, indicator, period, denominator, value, value_type

## g0050（1 列）
- 見出し：denominator
- 例1 値：1.37 | N/A | N/A | 2,631 | 15,006.77
  - 同じ表の列：type, topic, id, indicator, period, numerator, value, value_type

## g0051（1 列）
- 見出し：value
- 例1 値：9.63 | 9.49 | 10053.19 | 60.6 | 1652.42
  - 同じ表の列：type, topic, id, indicator, period, numerator, denominator, value_type

## g0052（1 列）
- 見出し：value_type
- 例1 値：Percentage | Percentage | Number | Number | Percentage
  - 同じ表の列：type, topic, id, indicator, period, numerator, denominator, value

## g0053（1 列）
- 見出し：sources
- 例1 値：1. Australian Bureau of Statistics, 816… | Australian Government Department of Emp… | City of Melbourne Social Indicators Sur… | 1. City of Melbourne, Urban Sustainabil… | 1. Department of Health, National Healt…
  - 同じ表の列：type, topic, id, indicator, period, numerator, denominator, value

## g0054（1 列）
- 見出し：School_Number
- 例1 値：0339 | 0318 | 0775 | 1019 | 0905
  - 同じ表の列：Suburb, Post_Code, Type_of_Schooling, Index_of_Educationa…

## g0055（5 列）
- 見出し：Suburb
- 例1 値：Macclesfield | Gawler | Modbury North | Prospect | Wasleys
  - 同じ表の列：School_Number, Post_Code, Type_of_Schooling, Index_of_Educationa…
- 例2 値：Marden | Quorn | Bordertown | Port Augusta | Whyalla Norrie
  - 同じ表の列：Agency, Subcategory, State, Post Code, Country, Great Circle Distan…, Great Circle Distan…, X Region

## g0056（1 列）
- 見出し：Post_Code
- 例1 値：5075 | 5063 | 5096 | 5290 | 5163
  - 同じ表の列：School_Number, Suburb, Type_of_Schooling, Index_of_Educationa…

## g0057（1 列）
- 見出し：Type_of_Schooling
- 例1 値：Secondary Education | Primary Education | Primary Education | Primary Education | Primary Education
  - 同じ表の列：School_Number, Suburb, Post_Code, Index_of_Educationa…

## g0058（1 列）
- 見出し：Index_of_Educational_Disadvantage
- 例1 値：6 | 2 | 6 | 6 | 4
  - 同じ表の列：School_Number, Suburb, Post_Code, Type_of_Schooling

## g0059（1 列）
- 見出し：Vehicle Make
- 例1 値：MODERN | MG | LEXUS | MODERN | MODERN
  - 同じ表の列：Vehicle Body Type, Vehicle Number of C…, Vehicle Year of Man…, Count of Vehicle RO…

## g0060（1 列）
- 見出し：Vehicle Body Type
- 例1 値：CARAVAN | STATION WAGON | TRAILER | FORK-LIFT | SEDAN
  - 同じ表の列：Vehicle Make, Vehicle Number of C…, Vehicle Year of Man…, Count of Vehicle RO…

## g0061（1 列）
- 見出し：Vehicle Number of Cylinders
- 例1 値：4 Cylinders | 4 Cylinders | 4 Cylinders | 4 Cylinders | 4 Cylinders
  - 同じ表の列：Vehicle Make, Vehicle Body Type, Vehicle Year of Man…, Count of Vehicle RO…

## g0062（1 列）
- 見出し：Vehicle Year of Manufacture
- 例1 値：2023 | 2015 | 2005 | 2015 | 2006
  - 同じ表の列：Vehicle Make, Vehicle Body Type, Vehicle Number of C…, Count of Vehicle RO…

## g0063（1 列）
- 見出し：Count of Vehicle ROIDs
- 例1 値：1 | 1 | 1 | 1 | 2
  - 同じ表の列：Vehicle Make, Vehicle Body Type, Vehicle Number of C…, Vehicle Year of Man…

## g0064（1 列）
- 見出し：Gender
- 例1 値：Female | Male | Female | Male | Female
  - 同じ表の列：Age Group, The digital governm…, Digital government …, Digital government …, Which of the follow…

## g0065（1 列）
- 見出し：Age Group
- 例1 値：20-29 | 20-29 | 20-29 | 40-59 | 40-59
  - 同じ表の列：Gender, The digital governm…, Digital government …, Digital government …, Which of the follow…

## g0066（1 列）
- 見出し：The digital government roadmap will include more opportuniti
- 例1 値：Survey | Survey | Survey | Survey | Survey
  - 同じ表の列：Gender, Age Group, Digital government …, Digital government …, Which of the follow…

## g0067（1 列）
- 見出し：Digital government could provide benefits and opportunities.
- 例1 値：Having your say – community participati… | Easier transactions – simple, secure on… | Better service – enhancing phone and fa… | Better service – enhancing phone and fa… | Easier transactions – simple, secure on…
  - 同じ表の列：Gender, Age Group, The digital governm…, Digital government …, Which of the follow…

## g0068（1 列）
- 見出し：Digital government could provide benefits and opportunities.
- 例1 値：Having your say – community participati… | Open government – more open data and pu… | Open government – more open data and pu… | Digital economy – fostering industry, r… | Open government – more open data and pu…
  - 同じ表の列：Gender, Age Group, The digital governm…, Digital government …, Which of the follow…

## g0069（1 列）
- 見出し：Which of the following statements do you agree with? Tick
- 例1 値：Neither Agree nor Disagree | Agree | Agree | Agree | Agree
  - 同じ表の列：Gender, Age Group, The digital governm…, Digital government …, Digital government …

## g0070（1 列）
- 見出し：S1. Which of the following age groups do you fall into?
- 例1 値：55-59 years | 18-20 years | 18-20 years | 50-54 years | 40-44 years
  - 同じ表の列：S2. S2_INT (Are you…, S3. Where do you li…, S4A. Do you live...?, Q20. Are you ...?, Q2AC1. Which of the…, Q2AC2. Which of the…, Q2AC3. Which of the…, Q2AC4. Which of the…

## g0071（1 列）
- 見出し：S2. S2_INT (Are you happy to co-operate with these quality c
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：S1. Which of the fo…, S3. Where do you li…, S4A. Do you live...?, Q20. Are you ...?, Q2AC1. Which of the…, Q2AC2. Which of the…, Q2AC3. Which of the…, Q2AC4. Which of the…

## g0072（1 列）
- 見出し：S3. Where do you live?
- 例1 値：South Australia | South Australia | South Australia | South Australia | South Australia
  - 同じ表の列：S1. Which of the fo…, S2. S2_INT (Are you…, S4A. Do you live...?, Q20. Are you ...?, Q2AC1. Which of the…, Q2AC2. Which of the…, Q2AC3. Which of the…, Q2AC4. Which of the…

## g0073（1 列）
- 見出し：S4A. Do you live...?
- 例1 値：In a metropolitan area | In a metropolitan area | In a metropolitan area | In a metropolitan area | In a metropolitan area
  - 同じ表の列：S1. Which of the fo…, S2. S2_INT (Are you…, S3. Where do you li…, Q20. Are you ...?, Q2AC1. Which of the…, Q2AC2. Which of the…, Q2AC3. Which of the…, Q2AC4. Which of the…

## g0074（1 列）
- 見出し：Q20. Are you ...?
- 例1 値：Female | Female | Female | Female | Male
  - 同じ表の列：S1. Which of the fo…, S2. S2_INT (Are you…, S3. Where do you li…, S4A. Do you live...?, Q2AC1. Which of the…, Q2AC2. Which of the…, Q2AC3. Which of the…, Q2AC4. Which of the…

## g0075（1 列）
- 見出し：Q2AC1. Which of these services would you like to be able to
- 例1 値：No | No | No | No | No
  - 同じ表の列：S1. Which of the fo…, S2. S2_INT (Are you…, S3. Where do you li…, S4A. Do you live...?, Q20. Are you ...?, Q2AC2. Which of the…, Q2AC3. Which of the…, Q2AC4. Which of the…

## g0076（1 列）
- 見出し：Q2AC2. Which of these services would you like to be able to
- 例1 値：No | No | No | No | No
  - 同じ表の列：S1. Which of the fo…, S2. S2_INT (Are you…, S3. Where do you li…, S4A. Do you live...?, Q20. Are you ...?, Q2AC1. Which of the…, Q2AC3. Which of the…, Q2AC4. Which of the…

## g0077（1 列）
- 見出し：Q2AC3. Which of these services would you like to be able to
- 例1 値：Yes | Yes | No | No | No
  - 同じ表の列：S1. Which of the fo…, S2. S2_INT (Are you…, S3. Where do you li…, S4A. Do you live...?, Q20. Are you ...?, Q2AC1. Which of the…, Q2AC2. Which of the…, Q2AC4. Which of the…

## g0078（1 列）
- 見出し：Q2AC4. Which of these services would you like to be able to
- 例1 値：No | No | No | No | No
  - 同じ表の列：S1. Which of the fo…, S2. S2_INT (Are you…, S3. Where do you li…, S4A. Do you live...?, Q20. Are you ...?, Q2AC1. Which of the…, Q2AC2. Which of the…, Q2AC3. Which of the…

## g0079（1 列）
- 見出し：Q2AC5. Which of these services would you like to be able to
- 例1 値：No | No | No | No | No
  - 同じ表の列：S1. Which of the fo…, S2. S2_INT (Are you…, S3. Where do you li…, S4A. Do you live...?, Q20. Are you ...?, Q2AC1. Which of the…, Q2AC2. Which of the…, Q2AC3. Which of the…

## g0080（1 列）
- 見出し：Agency
- 例1 値：HEALTH | TAFE | TAFE | TAFE | HEALTH
  - 同じ表の列：Subcategory, Suburb, State, Post Code, Country, Great Circle Distan…, Great Circle Distan…, X Region

## g0081（1 列）
- 見出し：Subcategory
- 例1 値：Courtroom 3 | TAFE | DEWNR | TAFE | Boylan Ward
  - 同じ表の列：Agency, Suburb, State, Post Code, Country, Great Circle Distan…, Great Circle Distan…, X Region

## g0082（1 列）
- 見出し：Post Code
- 例1 値：5065 | 5374 | 5000 | 5000 | 5355
  - 同じ表の列：Agency, Subcategory, Suburb, State, Country, Great Circle Distan…, Great Circle Distan…, X Region

## g0083（1 列）
- 見出し：Country
- 例1 値：Australia | Australia | Australia | Australia | Australia
  - 同じ表の列：Agency, Subcategory, Suburb, State, Post Code, Great Circle Distan…, Great Circle Distan…, X Region

## g0084（1 列）
- 見出し：Great Circle Distance
- 例1 値：59.85210576 | 0.250520746 | 3.345196446 | 14.73539173 | 144.0510247
  - 同じ表の列：Agency, Subcategory, Suburb, State, Post Code, Country, Great Circle Distan…, X Region

## g0085（1 列）
- 見出し：Great Circle Distance (X Only)
- 例1 値：238.769488 | 0.433914142 | 238.178356 | 15411.54768 | 186.663586
  - 同じ表の列：Agency, Subcategory, Suburb, State, Post Code, Country, Great Circle Distan…, X Region

## g0086（1 列）
- 見出し：X Region
- 例1 値：East | East | East | East | East
  - 同じ表の列：Agency, Subcategory, Suburb, State, Post Code, Country, Great Circle Distan…, Great Circle Distan…

## g0087（1 列）
- 見出し：X Suffix
- 例1 値：Outer | Outer | Outer | Outer | Far
  - 同じ表の列：Agency, Subcategory, Suburb, State, Post Code, Country, Great Circle Distan…, Great Circle Distan…

## g0088（1 列）
- 見出し：australian_appl_no
- 例1 値：2017218599 | 2017218566 | 2017217522 | 2017219748 | 2017214443
  - 同じ表の列：application_year, sealing_year, australian, foreign, entity, non_entity, patent_status_type, patent_type

## g0089（1 列）
- 見出し：application_year
- 例1 値：2018 | 2018 | 2018 | 2018 | 2018
  - 同じ表の列：australian_appl_no, sealing_year, australian, foreign, entity, non_entity, patent_status_type, patent_type

## g0090（1 列）
- 見出し：sealing_year
- 例1 値：2018 | 2019 | 2018 | 2019 | 2018
  - 同じ表の列：australian_appl_no, application_year, australian, foreign, entity, non_entity, patent_status_type, patent_type

## g0091（1 列）
- 見出し：australian
- 例1 値：False | False | False | False | True
  - 同じ表の列：australian_appl_no, application_year, sealing_year, foreign, entity, non_entity, patent_status_type, patent_type

## g0092（1 列）
- 見出し：foreign
- 例1 値：True | True | True | True | True
  - 同じ表の列：australian_appl_no, application_year, sealing_year, australian, entity, non_entity, patent_status_type, patent_type

## g0093（1 列）
- 見出し：entity
- 例1 値：True | False | True | True | True
  - 同じ表の列：australian_appl_no, application_year, sealing_year, australian, foreign, non_entity, patent_status_type, patent_type

## g0094（1 列）
- 見出し：non_entity
- 例1 値：False | False | False | False | False
  - 同じ表の列：australian_appl_no, application_year, sealing_year, australian, foreign, entity, patent_status_type, patent_type

## g0095（1 列）
- 見出し：patent_status_type
- 例1 値：FILED | FILED | FILED | FILED | FILED
  - 同じ表の列：australian_appl_no, application_year, sealing_year, australian, foreign, entity, non_entity, patent_type

## g0096（1 列）
- 見出し：patent_type
- 例1 値：Standard | Standard | Standard | Standard | Standard
  - 同じ表の列：australian_appl_no, application_year, sealing_year, australian, foreign, entity, non_entity, patent_status_type

## g0097（1 列）
- 見出し：primary_ipc_mark_value
- 例1 値：A01B 29/00 | B65B 31/02 | A42B 3/32 | C09J 161/06 | H01B 13/00
  - 同じ表の列：australian_appl_no, application_year, sealing_year, australian, foreign, entity, non_entity, patent_status_type

## g0098（1 列）
- 見出し：Centre
- 例1 値：Port Wakefield | Freeling | Booleroo Centre | Port Augusta | Fullarton
  - 同じ表の列：Suburb

## g0099（2 列）
- 見出し：DHS_ID
- 例1 値：4322 | 184 | 249 | 19 | 145
  - 同じ表の列：SUBURB, SUBTYPE, X, Y
- 例2 値：109 | 121 | 232 | 124 | 202
  - 同じ表の列：SUBURB, SUBTYPE, X, Y, HospitalNumber, births2011, births2012, births2013

## g0100（2 列）
- 見出し：SUBTYPE
- 例1 値：Public Acute | Public Acute | Private Acute | Public Acute | Public Acute
  - 同じ表の列：DHS_ID, SUBURB, X, Y
- 例2 値：Public Acute | Private Acute | Public Acute | Public Acute | Public Acute
  - 同じ表の列：DHS_ID, SUBURB, X, Y, HospitalNumber, births2011, births2012, births2013

## g0101（2 列）
- 見出し：X
- 例1 値：990032.863 | 1363032.5 | 1481181.354 | 1325326.834 | 1329520.831
  - 同じ表の列：DHS_ID, SUBURB, SUBTYPE, Y
- 例2 値：926875.948 | 1279612.685 | 1329349.83 | 874994.021 | 1237475.911
  - 同じ表の列：DHS_ID, SUBURB, SUBTYPE, Y, HospitalNumber, births2011, births2012, births2013

## g0102（1 列）
- 見出し：Y
- 例1 値：1647400.989 | 1660239.591 | 1436067.446 | 1811172.252 | 1675546.162
  - 同じ表の列：DHS_ID, SUBURB, SUBTYPE, X

## g0103（1 列）
- 見出し：Y
- 例1 値：1668264.596 | 1811910 | 1706984.509 | 1647283.203 | 1713557.295
  - 同じ表の列：DHS_ID, SUBURB, SUBTYPE, X, HospitalNumber, births2011, births2012, births2013

## g0104（1 列）
- 見出し：HospitalNumber
- 例1 値：3 | 88 | 4302 | 5 | 223
  - 同じ表の列：DHS_ID, SUBURB, SUBTYPE, X, Y, births2011, births2012, births2013

## g0105（1 列）
- 見出し：births2011
- 例1 値：0 | 293 | 38 | 32 | 3292
  - 同じ表の列：DHS_ID, SUBURB, SUBTYPE, X, Y, HospitalNumber, births2012, births2013

## g0106（1 列）
- 見出し：births2012
- 例1 値：0 | 40 | 1200 | 929 | 1
  - 同じ表の列：DHS_ID, SUBURB, SUBTYPE, X, Y, HospitalNumber, births2011, births2013

## g0107（1 列）
- 見出し：births2013
- 例1 値：44 | 570 | 54 | 780 | 0
  - 同じ表の列：DHS_ID, SUBURB, SUBTYPE, X, Y, HospitalNumber, births2011, births2012

## g0108（1 列）
- 見出し：births2014
- 例1 値：0 | 40 | 545 | 0 | 51
  - 同じ表の列：DHS_ID, SUBURB, SUBTYPE, X, Y, HospitalNumber, births2011, births2012

## g0109（2 列）
- 見出し：id
- 例1 値：b22919351 | b22917305 | b22913671 | b22918358 | b22914973
  - 同じ表の列：TITLE, PUBL/DATES, DESCRIPT., SOURCE
- 例2 値：b22921527 | b22921850 | b22915254 | b22921606 | b22913907
  - 同じ表の列：TITLE, PUBL/DATES, DESCRIPT., SOURCE

## g0110（1 列）
- 見出し：TITLE
- 例1 値：[Private Claude Hooker] | [Charles Leonard Garnett] | Major James Way | [Private F. H. Myers] | [Private Maurice Theobald]
  - 同じ表の列：id, PUBL/DATES, DESCRIPT., SOURCE

## g0111（2 列）
- 見出し：PUBL/DATES
- 例1 値：1918 | 1917 | 1918 | 1915 | 1917
  - 同じ表の列：id, TITLE, DESCRIPT., SOURCE
- 例2 値：1915 | 1917 | 1918 | 1917 | 1916
  - 同じ表の列：id, TITLE, DESCRIPT., SOURCE

## g0112（1 列）
- 見出し：DESCRIPT.
- 例1 値：reference in newspaper | reference in newspaper | reference in newspaper;portrait (16 Oct… | photograph in newspaper | reference in newspaper;portrait (page 4…
  - 同じ表の列：id, TITLE, PUBL/DATES, SOURCE

## g0113（2 列）
- 見出し：SOURCE
- 例1 値：Chronicle, 21 August 1915, p. 31, col. … | Chronicle, 17 August 1918, p. 12, col. … | Chronicle, 29 July 1916, p. 31, col. d … | Chronicle, 13 May 1916, p. 30, col. d;C… | Chronicle, 31 July 1915, p. 43, col. b
  - 同じ表の列：id, TITLE, PUBL/DATES, DESCRIPT.
- 例2 値：Chronicle, 7 April 1917, p. 44, col. a;… | Chronicle, 31 March 1917, p. 31, col. e… | Chronicle, 19 August 1916, p. 43, col. d | Chronicle, 11 September 1915, p. 44, co… | Chronicle, 5 May 1917, p. 46, col. e
  - 同じ表の列：id, TITLE, PUBL/DATES, DESCRIPT.

## g0114（1 列）
- 見出し：TITLE
- 例1 値：[Private William Brokenshire] | [Driver A. Davey] | [Private R. Duthie] | [Private William Allen] | [Private Fred Mason]
  - 同じ表の列：id, PUBL/DATES, DESCRIPT., SOURCE

## g0115（1 列）
- 見出し：DESCRIPT.
- 例1 値：reference in newspaper;portrait (10 Jul… | reference in newspaper;portrait (page 2… | reference in newspaper;portrait | reference in newspaper;portrait (7 Augu… | reference in newspaper;portrait
  - 同じ表の列：id, TITLE, PUBL/DATES, SOURCE

## g0116（1 列）
- 見出し：Knowledge gaps hindering effective management of biodiversit
- 例1 値：Long–term datasets/large–scale monitori… | Other | Knowing–doing gap | Impact of climate change | Disease
  - 同じ表の列：Proportion of respo…, Proportion of total…

## g0117（1 列）
- 見出し：Proportion of respondents
- 例1 値：1.818181818 | 36.36363636 | 16.36363636 | 4.545454545 | 46.36363636
  - 同じ表の列：Knowledge gaps hind…, Proportion of total…

## g0118（1 列）
- 見出し：Proportion of total responses for each category
- 例1 値：1.10864745 | 8.869179601 | 4.65631929 | 3.99113082 | 12.63858093
  - 同じ表の列：Knowledge gaps hind…, Proportion of respo…

## g0119（1 列）
- 見出し：City
- 例1 値：Melbourne | Hobart | Perth | Sydney | Canberra
  - 同じ表の列：Percent of populati…, Greenspace per capi…

## g0120（1 列）
- 見出し：Percent of population with access to greenspace
- 例1 値：92 | 88 | 95 | 79 | 91
  - 同じ表の列：City, Greenspace per capi…

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
g0008	
g0009	
g0010	
g0011	
g0012	
g0013	
g0014	
g0015	
g0016	
g0017	
g0018	
g0019	
g0020	
g0021	
g0022	
g0023	
g0024	
g0025	
g0026	
g0027	
g0028	
g0029	
g0030	
g0031	
g0032	
g0033	
g0034	
g0035	
g0036	
g0037	
g0038	
g0039	
g0040	
g0041	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0051	
g0052	
g0053	
g0054	
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
g0067	
g0068	
g0069	
g0070	
g0071	
g0072	
g0073	
g0074	
g0075	
g0076	
g0077	
g0078	
g0079	
g0080	
g0081	
g0082	
g0083	
g0084	
g0085	
g0086	
g0087	
g0088	
g0089	
g0090	
g0091	
g0092	
g0093	
g0094	
g0095	
g0096	
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
```
