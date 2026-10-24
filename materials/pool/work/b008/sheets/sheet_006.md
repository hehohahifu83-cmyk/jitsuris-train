# ラベル用シート 006 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_006.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0601（1 列）
- 見出し：Accessible
- 例1 値：No | Not Applicable | 1 | 1 | 1
  - 同じ表の列：Council_ID, Site, Type, Ambulant, DDA_Access, DoorsAuto, SocialUse, Lat

## g0602（1 列）
- 見出し：Ambulant
- 例1 値：Not Applicable | Not Applicable | Not Applicable | Not Applicable | Not Applicable
  - 同じ表の列：Council_ID, Site, Type, Accessible, DDA_Access, DoorsAuto, SocialUse, Lat

## g0603（1 列）
- 見出し：DDA_Access
- 例1 値：Yes | No | No | Yes | No
  - 同じ表の列：Council_ID, Site, Type, Accessible, Ambulant, DoorsAuto, SocialUse, Lat

## g0604（1 列）
- 見出し：DoorsAuto
- 例1 値：No | No | Not Applicable | No | No
  - 同じ表の列：Council_ID, Site, Type, Accessible, Ambulant, DDA_Access, SocialUse, Lat

## g0605（1 列）
- 見出し：SocialUse
- 例1 値：Public Facilities | Public Facilities | Public Facilities | Public Facilities | Commercial
  - 同じ表の列：Council_ID, Site, Type, Accessible, Ambulant, DDA_Access, DoorsAuto, Lat

## g0606（7 列）
- 見出し：Lat
- 例1 値：-37.5415188489038 | -37.5458642278571 | -37.5647113585289 | -37.5695563921373 | -37.4806413940983
  - 同じ表の列：Council_ID, Site, Type, Accessible, Ambulant, DDA_Access, DoorsAuto, SocialUse
- 例2 値：-37.949195 | -38.306855 | -37.871231 | -37.837667 | -37.847903
  - 同じ表の列：MARKER_ID, MARKER_STATUS, LON, A_ROAD_TYPE, A_ROAD_SUFFIX, B_ROAD_TYPE, B_ROAD_SUFFIX, LOCALITY

## g0607（2 列）
- 見出し：Long
- 例1 値：143.844745293213 | 143.848204812836 | 143.865391038314 | 143.862266366189 | 143.863071082074
  - 同じ表の列：Council_ID, Site, Type, Accessible, Ambulant, DDA_Access, DoorsAuto, SocialUse
- 例2 値：144.061903 | 144.17525 | 143.752532 | 143.714742 | 143.801014
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, LAT

## g0608（1 列）
- 見出し：Locality
- 例1 値：NOBLE PARK NORTH | KEYSBOROUGH | NOBLE PARK NORTH | SPRINGVALE | SPRINGVALE
  - 同じ表の列：Animal_Type, GENDER

## g0609（1 列）
- 見出し：Animal_Type
- 例1 値：Dog | Dog | Dog | Dog | Dog
  - 同じ表の列：Locality, GENDER

## g0610（1 列）
- 見出し：GENDER
- 例1 値：F | M | F | M | M
  - 同じ表の列：Locality, Animal_Type

## g0611（2 列）
- 見出し：date
- 例1 値：20201030 | 20201030 | 20201030 | 20201106 | 20201106
  - 同じ表の列：time, suburb, cleaning_category, litter_L, weeds_L, pit_lids_no, tree_surrounds_no, cleaning_duration
- 例2 値：20230102 | 20250425 | 20211225 | 20220425 | 20211004
  - 同じ表の列：ID, Information, More Information, Jurisdiction

## g0612（1 列）
- 見出し：time
- 例1 値：14:05:00 | 08:55:00 | 07:22:00 | 08:38:00 | 13:09:00
  - 同じ表の列：date, suburb, cleaning_category, litter_L, weeds_L, pit_lids_no, tree_surrounds_no, cleaning_duration

## g0613（2 列）
- 見出し：suburb
- 例1 値：Fitzroy | Richmond | Cremorne | Abbotsford | Cremorne
  - 同じ表の列：date, time, cleaning_category, litter_L, weeds_L, pit_lids_no, tree_surrounds_no, cleaning_duration
- 例2 値：Sherwood | Nanango | Blackbutt | Goombungee | Dirranbandi
  - 同じ表の列：Title, Mon am, Mon pm, Tues am, Tues pm, Wed am, Wed pm, Thurs am

## g0614（1 列）
- 見出し：cleaning_category
- 例1 値：Litter Removal | Pit Lid Cleaning | Litter Removal | Litter Removal | Litter Removal
  - 同じ表の列：date, time, suburb, litter_L, weeds_L, pit_lids_no, tree_surrounds_no, cleaning_duration

## g0615（1 列）
- 見出し：litter_L
- 例1 値：55 | 55 | 13.75 | 55 | 55
  - 同じ表の列：date, time, suburb, cleaning_category, weeds_L, pit_lids_no, tree_surrounds_no, cleaning_duration

## g0616（1 列）
- 見出し：weeds_L
- 例1 値：27.5 | 55 | 110 | 27.5 | 110
  - 同じ表の列：date, time, suburb, cleaning_category, litter_L, pit_lids_no, tree_surrounds_no, cleaning_duration

## g0617（1 列）
- 見出し：pit_lids_no
- 例1 値：1 | More than 5 | 2 | More than 5 | More than 5
  - 同じ表の列：date, time, suburb, cleaning_category, litter_L, weeds_L, tree_surrounds_no, cleaning_duration

## g0618（1 列）
- 見出し：tree_surrounds_no
- 例1 値：1 | 2 | 1 | 1 | 2
  - 同じ表の列：date, time, suburb, cleaning_category, litter_L, weeds_L, pit_lids_no, cleaning_duration

## g0619（1 列）
- 見出し：cleaning_duration
- 例1 値：15 mins | 15 mins | 30 mins | 15 mins | 15 mins
  - 同じ表の列：date, time, suburb, cleaning_category, litter_L, weeds_L, pit_lids_no, tree_surrounds_no

## g0620（1 列）
- 見出し：Title
- 例1 値：Camperdown Show | Camperdown Rotary Market | Australia Day celebrations | Inner Varnika | National Simultaneous Storytime - Famil…
  - 同じ表の列：Start Date, End Date, Id, CreateDate, ActivateDate, DeactivateDate, Cost, Website

## g0621（2 列）
- 見出し：Start Date
- 例1 値：2023-01-21T11:00:00 | 2023-01-28T07:50:00 | 2023-06-08T16:00:00 | 2023-05-13T09:00:00 | 2023-02-26T11:00:00
  - 同じ表の列：Title, End Date, Id, CreateDate, ActivateDate, DeactivateDate, Cost, Website
- 例2 値：2024-10-04T00:00:00 | 2024-05-25T00:00:00 | 2024-08-28T00:00:00 | 2024-09-06T00:00:00 | 2024-07-28T00:00:00
  - 同じ表の列：Event Type, County, Is Free To Visit, Price, End Date, Start Time, End Time, Recurring Dates

## g0622（2 列）
- 見出し：End Date
- 例1 値：2023-02-05T23:59:00 | 2023-05-14T23:59:00 | 2023-06-08T18:00:00 | 2023-05-11T18:00:00 | 2023-01-21T15:00:00
  - 同じ表の列：Title, Start Date, Id, CreateDate, ActivateDate, DeactivateDate, Cost, Website
- 例2 値：2024-04-13T00:00:00 | 2024-05-17T00:00:00 | 2024-08-03T00:00:00 | 2024-09-17T00:00:00 | 2024-10-18T00:00:00
  - 同じ表の列：Event Type, County, Is Free To Visit, Price, Start Date, Start Time, End Time, Recurring Dates

## g0623（1 列）
- 見出し：Id
- 例1 値：87c4fa90-8b12-4877-bd24-41a5dd7264e7 | 1a52ac84-5d83-4881-85be-d9d5f4b516ad | 0d36209c-aae8-4b65-a526-bfa95e3c2ef2 | 399bc6eb-8bbf-4387-b448-a967532d7996 | 7d3a6aea-7e46-4450-afb7-143670ab4434
  - 同じ表の列：Title, Start Date, End Date, CreateDate, ActivateDate, DeactivateDate, Cost, Website

## g0624（1 列）
- 見出し：CreateDate
- 例1 値：2019-09-16T04:45:58Z | 2020-02-06T05:01:50Z | 2021-02-11T01:15:47Z | 2021-01-12T01:56:58Z | 2020-01-28T04:27:37Z
  - 同じ表の列：Title, Start Date, End Date, Id, ActivateDate, DeactivateDate, Cost, Website

## g0625（1 列）
- 見出し：ActivateDate
- 例1 値：2022-01-06T01:09:33Z | 2023-01-13T00:17:11Z | 2022-11-03T06:00:20Z | 2023-01-12T03:37:51Z | 2023-01-09T05:48:41Z
  - 同じ表の列：Title, Start Date, End Date, Id, CreateDate, DeactivateDate, Cost, Website

## g0626（1 列）
- 見出し：DeactivateDate
- 例1 値：9999-12-31T23:59:59Z | 9999-12-31T23:59:59Z | 9999-12-31T23:59:59Z | 9999-12-31T23:59:59Z | 9999-12-31T23:59:59Z
  - 同じ表の列：Title, Start Date, End Date, Id, CreateDate, ActivateDate, Cost, Website

## g0627（1 列）
- 見出し：Cost
- 例1 値：$5 entry, free entry for kids | Ticket prices TBC - between $25-$35 | Entry Fee and Camping Fee for competito… | Individual Entry $55 / Team Entry (2, 3… | $8
  - 同じ表の列：Title, Start Date, End Date, Id, CreateDate, ActivateDate, DeactivateDate, Website

## g0628（1 列）
- 見出し：Website
- 例1 値：https://www.camperdowntheatrecompany.co… | https://calendly.com/businessworkshops/… | https://innervarnika.com/ | https://www.facebook.com/events/8202427… | https://www.trybooking.com/events/landi…
  - 同じ表の列：Title, Start Date, End Date, Id, CreateDate, ActivateDate, DeactivateDate, Cost

## g0629（1 列）
- 見出し：Venue
- 例1 値：Terang Racecourse | Under the Elms | Cobden Outdoor Swimming Pool | Mt Elephant | Noorat Recreation Reserve
  - 同じ表の列：Title, Start Date, End Date, Id, CreateDate, ActivateDate, DeactivateDate, Cost

## g0630（1 列）
- 見出し：Title
- 例1 値：Mossman QGAP | Coen Police Station | Aurukun Police Station | Silkwood Police Station | Carseldine Transport and Main Roads Cus…
  - 同じ表の列：Suburb, Mon am, Mon pm, Tues am, Tues pm, Wed am, Wed pm, Thurs am

## g0631（1 列）
- 見出し：Mon am
- 例1 値：8:30 | 9:00 - 12:30 | 8:30 | 8:30 | 8:30 - 12:30
  - 同じ表の列：Title, Suburb, Mon pm, Tues am, Tues pm, Wed am, Wed pm, Thurs am

## g0632（1 列）
- 見出し：Mon pm
- 例1 値：16:30 | 13:00 - 16:30 | 13:30 - 15:30 | 15:30 | 16:30
  - 同じ表の列：Title, Suburb, Mon am, Tues am, Tues pm, Wed am, Wed pm, Thurs am

## g0633（1 列）
- 見出し：Tues am
- 例1 値：8:00 | 8:30 | 9:00 - 12:00 | 8:30 | 9:00 - 12:00
  - 同じ表の列：Title, Suburb, Mon am, Mon pm, Tues pm, Wed am, Wed pm, Thurs am

## g0634（1 列）
- 見出し：Tues pm
- 例1 値：17:00 | 15:30 | NA | 16:00 | 16:00
  - 同じ表の列：Title, Suburb, Mon am, Mon pm, Tues am, Wed am, Wed pm, Thurs am

## g0635（1 列）
- 見出し：Wed am
- 例1 値：9:30 | 9:00 | 9:00 | 9:30 | 8:00
  - 同じ表の列：Title, Suburb, Mon am, Mon pm, Tues am, Tues pm, Wed pm, Thurs am

## g0636（1 列）
- 見出し：Wed pm
- 例1 値：16:30 | 13:30 - 16:00 | 16:30 | 12:30 - 14:30 | 14:00
  - 同じ表の列：Title, Suburb, Mon am, Mon pm, Tues am, Tues pm, Wed am, Thurs am

## g0637（1 列）
- 見出し：Thurs am
- 例1 値：8:30 - 12:30 | 9:00 - 13:00 | 8:30 | 8:30 - 13:00 | 8:30
  - 同じ表の列：Title, Suburb, Mon am, Mon pm, Tues am, Tues pm, Wed am, Wed pm

## g0638（1 列）
- 見出し：Thurs pm
- 例1 値：13:00 - 16:30 | 16:30 | 16:30 | 13:30 - 16:30 | 16:30
  - 同じ表の列：Title, Suburb, Mon am, Mon pm, Tues am, Tues pm, Wed am, Wed pm

## g0639（1 列）
- 見出し：ApplStandard
- 例1 値：[SEER Non Multi-Split <=65kW] GEMS (Air… | [SEER Non Multi-Split <=65kW] GEMS (Air… | [SEER Non Multi-Split >65kW] GEMS (Air … | [SEER Non Multi-Split <=65kW] GEMS (Air… | [SEER Non Multi-Split <=65kW] GEMS (Air…
  - 同じ表の列：MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1, Configuration2

## g0640（1 列）
- 見出し：MEPSComp
- 例1 値：MEPS 2019 | MEPS 2019 | MEPS 2019 | MEPS 2019 | MEPS 2019
  - 同じ表の列：ApplStandard, N-Standard, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1, Configuration2

## g0641（1 列）
- 見出し：N-Standard
- 例1 値：AS/NZS 3823.1.1:2012 | AS/NZS 3823.1.2:2012 | AS/NZS 3823.1.4:2012 | AS/NZS 3823.1.1:2012 | AS/NZS 3823.1.4:2012
  - 同じ表の列：ApplStandard, MEPSComp, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1, Configuration2

## g0642（1 列）
- 見出し：Model_No
- 例1 値：KASHSAC80TA | SUZ-M35VAD-A/SEZ-M35DA | RAQ/K/WP/112 | RZA50C2V1 / FDYAN50AV1 | RZAV125FV1 / FDMA125AV1A
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1, Configuration2

## g0643（1 列）
- 見出し：avg_pwr_standby_mode
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, Brand, C-Dehumid_Rated, Configuration1, Configuration2

## g0644（1 列）
- 見出し：Brand
- 例1 値：Haier | LENNOX | MITSUBISHI ELECTRIC | HITACHI | Coates
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, C-Dehumid_Rated, Configuration1, Configuration2

## g0645（1 列）
- 見出し：C-Dehumid_Rated
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, Brand, Configuration1, Configuration2

## g0646（1 列）
- 見出し：Configuration1
- 例1 値：Ducted | Ducted | Non Ducted | Non Ducted | Non Ducted
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration2

## g0647（1 列）
- 見出し：Configuration2
- 例1 値：Packaged | Single Split System | Single Split System | Single Split System | Single Split System
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1

## g0648（1 列）
- 見出し：Configuration2-unitmount
- 例1 値：Wall Hung | Wall Hung | N/A | - | -
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1

## g0649（1 列）
- 見出し：Employment Category
- 例1 値：Education & Children's Services Act | Education Act | Children's Services Act | Education & Children's Services Act | Education Act
  - 同じ表の列：Role, Highest qualificati…, fin_year, Headcount

## g0650（1 列）
- 見出し：Role
- 例1 値：Preschool teachers | School teachers in SA Government Schools | Preschool directors | Preschool directors | Preschool directors
  - 同じ表の列：Employment Category, Highest qualificati…, fin_year, Headcount

## g0651（1 列）
- 見出し：Highest qualification held
- 例1 値：Bachelor degree with honours/graduate c… | Advanced diploma/associate degree | Masters degree | Certificate level/no qualification reco… | Bachelor degree with honours/graduate c…
  - 同じ表の列：Employment Category, Role, fin_year, Headcount

## g0652（1 列）
- 見出し：fin_year
- 例1 値：2025 | 2020 | 2016 | 2020 | 2023
  - 同じ表の列：Employment Category, Role, Highest qualificati…, Headcount

## g0653（2 列）
- 見出し：Headcount
- 例1 値：30 | 17 | 691 | 28 | 74
  - 同じ表の列：Employment Category, Role, Highest qualificati…, fin_year
- 例2 値：128 | 174 | 164 | 40 | 55
  - 同じ表の列：Entity, FTE, Female %, Male %, Female median age, Male median age, Agency median age, Age less than 20

## g0654（1 列）
- 見出し：TITLE
- 例1 値：Broadband | Broadband | Broadband | Broadband | Broadband
  - 同じ表の列：SUBTITLE, INTRODUCTI, DESCRIPTIO, NUM_CONNCT, TOT_FUNDG, MORE_INFO, INFO_LINK, CUST_ENQRY

## g0655（1 列）
- 見出し：SUBTITLE
- 例1 値：Australian Broadband Guarantee | Australian Broadband Guarantee | Australian Broadband Guarantee | Australian Broadband Guarantee | Australian Broadband Guarantee
  - 同じ表の列：TITLE, INTRODUCTI, DESCRIPTIO, NUM_CONNCT, TOT_FUNDG, MORE_INFO, INFO_LINK, CUST_ENQRY

## g0656（1 列）
- 見出し：INTRODUCTI
- 例1 値：This Australian Government initiative h… | This Australian Government initiative h… | This Australian Government initiative h… | This Australian Government initiative h… | This Australian Government initiative h…
  - 同じ表の列：TITLE, SUBTITLE, DESCRIPTIO, NUM_CONNCT, TOT_FUNDG, MORE_INFO, INFO_LINK, CUST_ENQRY

## g0657（1 列）
- 見出し：DESCRIPTIO
- 例1 値：ABG subsidised satellite services have … | ABG subsidised satellite services have … | ABG subsidised satellite services have … | ABG subsidised satellite services have … | ABG subsidised wireless and satellite s…
  - 同じ表の列：TITLE, SUBTITLE, INTRODUCTI, NUM_CONNCT, TOT_FUNDG, MORE_INFO, INFO_LINK, CUST_ENQRY

## g0658（1 列）
- 見出し：NUM_CONNCT
- 例1 値：26 | 38 | 17 | 41 | 21
  - 同じ表の列：TITLE, SUBTITLE, INTRODUCTI, DESCRIPTIO, TOT_FUNDG, MORE_INFO, INFO_LINK, CUST_ENQRY

## g0659（1 列）
- 見出し：TOT_FUNDG
- 例1 値：2376355 | 2500 | 43256 | 7500 | 8340
  - 同じ表の列：TITLE, SUBTITLE, INTRODUCTI, DESCRIPTIO, NUM_CONNCT, MORE_INFO, INFO_LINK, CUST_ENQRY

## g0660（1 列）
- 見出し：MORE_INFO
- 例1 値：The Australian Broadband Guarantee | The Australian Broadband Guarantee | The Australian Broadband Guarantee | The Australian Broadband Guarantee | The Australian Broadband Guarantee
  - 同じ表の列：TITLE, SUBTITLE, INTRODUCTI, DESCRIPTIO, NUM_CONNCT, TOT_FUNDG, INFO_LINK, CUST_ENQRY

## g0661（1 列）
- 見出し：INFO_LINK
- 例1 値：http://www.dbcde.gov.au/broadband/austr… | http://www.dbcde.gov.au/broadband/austr… | http://www.dbcde.gov.au/broadband/austr… | http://www.dbcde.gov.au/broadband/austr… | http://www.dbcde.gov.au/broadband/austr…
  - 同じ表の列：TITLE, SUBTITLE, INTRODUCTI, DESCRIPTIO, NUM_CONNCT, TOT_FUNDG, MORE_INFO, CUST_ENQRY

## g0662（1 列）
- 見出し：CUST_ENQRY
- 例1 値：1800883488 | 1800883488 | 1800883488 | 1800883488 | 1800883488
  - 同じ表の列：TITLE, SUBTITLE, INTRODUCTI, DESCRIPTIO, NUM_CONNCT, TOT_FUNDG, MORE_INFO, INFO_LINK

## g0663（1 列）
- 見出し：UPDATED
- 例1 値：29 July 2011 | 29 July 2011 | 29 July 2011 | 29 July 2011 | 29 July 2011
  - 同じ表の列：TITLE, SUBTITLE, INTRODUCTI, DESCRIPTIO, NUM_CONNCT, TOT_FUNDG, MORE_INFO, INFO_LINK

## g0664（1 列）
- 見出し：2014Students1stTermFTE
- 例1 値：38.6 | 724.4 | 146.1 | 272 | 380.8
  - 同じ表の列：2015Students1stTerm…, 2014FinalFFM$, 2015FinalFFM$, 2014FinalSRP$, 2015FinalSRP$, 2013OENI, 2014OENI, ARIA+

## g0665（1 列）
- 見出し：2015Students1stTermFTE
- 例1 値：128 | 230.2 | 291.2 | 22 | 578
  - 同じ表の列：2014Students1stTerm…, 2014FinalFFM$, 2015FinalFFM$, 2014FinalSRP$, 2015FinalSRP$, 2013OENI, 2014OENI, ARIA+

## g0666（1 列）
- 見出し：2014FinalFFM$
- 例1 値：262331 | 440253 | 277745 | 481693 | 141570
  - 同じ表の列：2014Students1stTerm…, 2015Students1stTerm…, 2015FinalFFM$, 2014FinalSRP$, 2015FinalSRP$, 2013OENI, 2014OENI, ARIA+

## g0667（1 列）
- 見出し：2015FinalFFM$
- 例1 値：259084 | 366537 | 698823 | 457196 | 208069
  - 同じ表の列：2014Students1stTerm…, 2015Students1stTerm…, 2014FinalFFM$, 2014FinalSRP$, 2015FinalSRP$, 2013OENI, 2014OENI, ARIA+

## g0668（1 列）
- 見出し：2014FinalSRP$
- 例1 値：339991 | 136604 | 305343 | 727745 | 683964
  - 同じ表の列：2014Students1stTerm…, 2015Students1stTerm…, 2014FinalFFM$, 2015FinalFFM$, 2015FinalSRP$, 2013OENI, 2014OENI, ARIA+

## g0669（1 列）
- 見出し：2015FinalSRP$
- 例1 値：600405 | 280705 | 1238325 | 580233 | 1373848
  - 同じ表の列：2014Students1stTerm…, 2015Students1stTerm…, 2014FinalFFM$, 2015FinalFFM$, 2014FinalSRP$, 2013OENI, 2014OENI, ARIA+

## g0670（1 列）
- 見出し：2013OENI
- 例1 値：0.6563 | 0.5078 | 0.3856 | 0.9057 | 0.6027
  - 同じ表の列：2014Students1stTerm…, 2015Students1stTerm…, 2014FinalFFM$, 2015FinalFFM$, 2014FinalSRP$, 2015FinalSRP$, 2014OENI, ARIA+

## g0671（1 列）
- 見出し：2014OENI
- 例1 値：0.6341 | 0.5294 | 0.3821 | 0.7113 | 0.5824
  - 同じ表の列：2014Students1stTerm…, 2015Students1stTerm…, 2014FinalFFM$, 2015FinalFFM$, 2014FinalSRP$, 2015FinalSRP$, 2013OENI, ARIA+

## g0672（1 列）
- 見出し：ARIA+
- 例1 値：1.85 | 1.83 | 4.83 | 2.75 | 2.13
  - 同じ表の列：2014Students1stTerm…, 2015Students1stTerm…, 2014FinalFFM$, 2015FinalFFM$, 2014FinalSRP$, 2015FinalSRP$, 2013OENI, 2014OENI

## g0673（1 列）
- 見出し：2014Headcount
- 例1 値：302 | 163 | 249 | 512 | 410
  - 同じ表の列：2014Students1stTerm…, 2015Students1stTerm…, 2014FinalFFM$, 2015FinalFFM$, 2014FinalSRP$, 2015FinalSRP$, 2013OENI, 2014OENI

## g0674（1 列）
- 見出し：Site Code
- 例1 値：L70095 | L71002 | L70873 | L70264 | L70199
  - 同じ表の列：Provider, Site Provider, Site Suburb, Site State, Post Code

## g0675（1 列）
- 見出し：Provider
- 例1 値：TAFE Commission | TAFE Queensland | STEPS Education & Training | TAFE Commission | TAFE Queensland
  - 同じ表の列：Site Code, Site Provider, Site Suburb, Site State, Post Code

## g0676（1 列）
- 見出し：Site Provider
- 例1 値：MAX Solutions | Wyndham Community Education Centre Inc | MAX Solutions | Department Of Employment And Training | Career Employment Australia Incorporated
  - 同じ表の列：Site Code, Provider, Site Suburb, Site State, Post Code

## g0677（1 列）
- 見出し：Site Suburb
- 例1 値：Callemondah | Maroochydore | Werribee | Busselton | Goodna
  - 同じ表の列：Site Code, Provider, Site Provider, Site State, Post Code

## g0678（1 列）
- 見出し：Site State
- 例1 値：VIC | QLD | NSW | QLD | NSW
  - 同じ表の列：Site Code, Provider, Site Provider, Site Suburb, Post Code

## g0679（1 列）
- 見出し：Post Code
- 例1 値：2168 | 2700 | 3073 | 4020 | 2834
  - 同じ表の列：Site Code, Provider, Site Provider, Site Suburb, Site State

## g0680（1 列）
- 見出し：AGGREGATES
- 例1 値：Net Assets(a) | Assets | Revenue(a) | Liabilities | Fiscal Balance
  - 同じ表の列：ACTUAL 2000-2001 Ju…, ACTUAL 2000-2001 Au…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…

## g0681（1 列）
- 見出し：ACTUAL 2000-2001 July $m
- 例1 値：-194 | 12308 | 178870 | 132570 | 1894
  - 同じ表の列：AGGREGATES, ACTUAL 2000-2001 Au…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…

## g0682（1 列）
- 見出し：ACTUAL 2000-2001 August $m
- 例1 値：-5263 | -1455 | 178980 | -47843 | -4800
  - 同じ表の列：AGGREGATES, ACTUAL 2000-2001 Ju…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…

## g0683（1 列）
- 見出し：ACTUAL 2000-2001 YTD September $m
- 例1 値：-4245 | -5519 | 38993 | 129280 | 182205
  - 同じ表の列：AGGREGATES, ACTUAL 2000-2001 Ju…, ACTUAL 2000-2001 Au…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…

## g0684（1 列）
- 見出し：ACTUAL 2000-2001 YTD October $m
- 例1 値：-3002 | 124819 | 47438 | -4549 | -4918
  - 同じ表の列：AGGREGATES, ACTUAL 2000-2001 Ju…, ACTUAL 2000-2001 Au…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…

## g0685（1 列）
- 見出し：ACTUAL 2000-2001 YTD November $m
- 例1 値：-1403 | 177291 | 61614 | -3156 | 64770
  - 同じ表の列：AGGREGATES, ACTUAL 2000-2001 Ju…, ACTUAL 2000-2001 Au…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…

## g0686（1 列）
- 見出し：ACTUAL 2000-2001 YTD December $m
- 例1 値：-3528 | 76831 | 127208 | -50134 | 700
  - 同じ表の列：AGGREGATES, ACTUAL 2000-2001 Ju…, ACTUAL 2000-2001 Au…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…

## g0687（1 列）
- 見出し：ACTUAL 2000-2001 YTD January $m
- 例1 値：91260 | -69 | 125861 | -47464 | -366
  - 同じ表の列：AGGREGATES, ACTUAL 2000-2001 Ju…, ACTUAL 2000-2001 Au…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…

## g0688（1 列）
- 見出し：ACTUAL 2000-2001 YTD February $m
- 例1 値：103031 | 896 | 5182 | 173537 | 104176
  - 同じ表の列：AGGREGATES, ACTUAL 2000-2001 Ju…, ACTUAL 2000-2001 Au…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…

## g0689（1 列）
- 見出し：ACTUAL 2000-2001 YTD April $m
- 例1 値：134363 | 3523 | 5643 | 4141 | 131113
  - 同じ表の列：AGGREGATES, ACTUAL 2000-2001 Ju…, ACTUAL 2000-2001 Au…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…, ACTUAL 2000-2001 YT…

## g0690（1 列）
- 見出し：FacilityID
- 例1 値：605 | 557 | 395 | 115 | 548
  - 同じ表の列：FacilityType, Town, State, Parking, ParkingAccessible, ParkingNote, KeyRequired, MLAK24

## g0691（1 列）
- 見出し：FacilityType
- 例1 値：Caravan park | Park or reserve | Rest area | Park or reserve | Car park
  - 同じ表の列：FacilityID, Town, State, Parking, ParkingAccessible, ParkingNote, KeyRequired, MLAK24

## g0692（2 列）
- 見出し：Town
- 例1 値：Nyngan | Bentleigh | Forrestdale | Stawell | Woorree
  - 同じ表の列：FacilityID, FacilityType, State, Parking, ParkingAccessible, ParkingNote, KeyRequired, MLAK24
- 例2 値：Murtoa | Hamilton | Wangaratta | Stawell | Benalla
  - 同じ表の列：Type

## g0693（7 列）
- 見出し：State
- 例1 値：SA | QLD | WA | VIC | SA
  - 同じ表の列：FacilityID, FacilityType, Town, Parking, ParkingAccessible, ParkingNote, KeyRequired, MLAK24
- 例2 値：NSW | NSW | WA | NSW | Victoria
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0694（1 列）
- 見出し：Parking
- 例1 値：True | True | True | True | False
  - 同じ表の列：FacilityID, FacilityType, Town, State, ParkingAccessible, ParkingNote, KeyRequired, MLAK24

## g0695（1 列）
- 見出し：ParkingAccessible
- 例1 値：False | False | False | True | False
  - 同じ表の列：FacilityID, FacilityType, Town, State, Parking, ParkingNote, KeyRequired, MLAK24

## g0696（1 列）
- 見出し：ParkingNote
- 例1 値：Parking for cars and buses | Car parking is available in front of th… | On-street parking available in Campbell… | Access from the parking and information… | Parking is right next to toilet block.
  - 同じ表の列：FacilityID, FacilityType, Town, State, Parking, ParkingAccessible, KeyRequired, MLAK24

## g0697（1 列）
- 見出し：KeyRequired
- 例1 値：False | False | False | False | False
  - 同じ表の列：FacilityID, FacilityType, Town, State, Parking, ParkingAccessible, ParkingNote, MLAK24

## g0698（1 列）
- 見出し：MLAK24
- 例1 値：False | False | False | False | False
  - 同じ表の列：FacilityID, FacilityType, Town, State, Parking, ParkingAccessible, ParkingNote, KeyRequired

## g0699（1 列）
- 見出し：MLAKAfterHours
- 例1 値：False | False | False | False | False
  - 同じ表の列：FacilityID, FacilityType, Town, State, Parking, ParkingAccessible, ParkingNote, KeyRequired

## g0700（5 列）
- 見出し：Suburb
- 例1 値：FALCON | MOUNT RICHON | GREENMOUNT | VIVEASH | CUBALLING
  - 同じ表の列：0 bed, 1 bed, 2 bed, 3 bed, 4 bed, 5 bed, 6 bed, 7 bed
- 例2 値：Belmont | Balwyn North | Mount Waverley | Yarraville | Mt Martha
  - 同じ表の列：State, Business Category, LGA, Region

## g0701（1 列）
- 見出し：0 bed
- 例1 値：37.0 | 38.0 | 37.0 | 39.0 | 43.25
  - 同じ表の列：Suburb, 1 bed, 2 bed, 3 bed, 4 bed, 5 bed, 6 bed, 7 bed

## g0702（1 列）
- 見出し：1 bed
- 例1 値：21.25 | 26.81 | 38.0 | 14.0 | 2.0
  - 同じ表の列：Suburb, 0 bed, 2 bed, 3 bed, 4 bed, 5 bed, 6 bed, 7 bed

## g0703（1 列）
- 見出し：2 bed
- 例1 値：17.0 | 19.0 | 21.31 | 35.17 | 4.5
  - 同じ表の列：Suburb, 0 bed, 1 bed, 3 bed, 4 bed, 5 bed, 6 bed, 7 bed

## g0704（1 列）
- 見出し：3 bed
- 例1 値：35.2 | 32.14 | 40.48 | 41.43 | 33.14
  - 同じ表の列：Suburb, 0 bed, 1 bed, 2 bed, 4 bed, 5 bed, 6 bed, 7 bed

## g0705（1 列）
- 見出し：4 bed
- 例1 値：39.0 | 30.71 | 24.0 | 29.44 | 19.44
  - 同じ表の列：Suburb, 0 bed, 1 bed, 2 bed, 3 bed, 5 bed, 6 bed, 7 bed

## g0706（1 列）
- 見出し：5 bed
- 例1 値：20.75 | 19.14 | 17.0 | 16.0 | 27.0
  - 同じ表の列：Suburb, 0 bed, 1 bed, 2 bed, 3 bed, 4 bed, 6 bed, 7 bed

## g0707（1 列）
- 見出し：6 bed
- 例1 値：2.75 | 9.5 | 21.0 | 8.25 | 16.0
  - 同じ表の列：Suburb, 0 bed, 1 bed, 2 bed, 3 bed, 4 bed, 5 bed, 7 bed

## g0708（1 列）
- 見出し：7 bed
- 例1 値：7.0 | 2.0 | 23.0 | 4.0 | 4.0
  - 同じ表の列：Suburb, 0 bed, 1 bed, 2 bed, 3 bed, 4 bed, 5 bed, 6 bed

## g0709（1 列）
- 見出し：8 bed
- 例1 値：4.0 | 4.0
  - 同じ表の列：Suburb, 0 bed, 1 bed, 2 bed, 3 bed, 4 bed, 5 bed, 6 bed

## g0710（1 列）
- 見出し：Managing Organisation
- 例1 値：ANSTO | ANSTO | CSIRO | AIMS | CSIRO
  - 同じ表の列：Facility, Sub facility, What sectors or ind…, Case studies of bus…, Main partners or re…

## g0711（1 列）
- 見出し：Facility
- 例1 値：National Research Collections Australia | Australian Institute of Marine Science … | Australia Telescope National Facility (… | Australia Telescope National Facility (… | Open Pool Australian Lightwater (OPAL) …
  - 同じ表の列：Managing Organisati…, Sub facility, What sectors or ind…, Case studies of bus…, Main partners or re…

## g0712（1 列）
- 見出し：Sub facility
- 例1 値：RV Cape Ferguson | Australian National Herbarium (ANH) | Australia Telescope Compact Array | Australian National Algae Culture Colle… | Parkes Radio Telescope
  - 同じ表の列：Managing Organisati…, Facility, What sectors or ind…, Case studies of bus…, Main partners or re…

## g0713（1 列）
- 見出し：What sectors or industries use, or can use the facility
- 例1 値：THE MNF has multi-disciplinary research… | OPAL has the capability to irradiate ma… | Pharmaceutical and biotechnology indust… | The DEA and ODC platforms are available… | The NRCA has been used in the medical, …
  - 同じ表の列：Managing Organisati…, Facility, Sub facility, Case studies of bus…, Main partners or re…

## g0714（1 列）
- 見出し：Case studies of business use or commercial application resul
- 例1 値：In 2014, AIMS, Shell Australia and INPE… | ATNF has a long history of supporting N… | Recent industrial clients are distribut… | The data and information held within Ge… | The Great Australian Bight (GAB) resear…
  - 同じ表の列：Managing Organisati…, Facility, Sub facility, What sectors or ind…, Main partners or re…

## g0715（1 列）
- 見出し：Main partners or relationships
- 例1 値：The Offshore petroleum exploration indu… | Work undertaken in the SeaSim often dra… | NCRA is hosted by CSIRO Within CSIRO, D… | AIMS collaborates with a number of inte… | NCRA is hosted by CSIRO Within CSIRO, D…
  - 同じ表の列：Managing Organisati…, Facility, Sub facility, What sectors or ind…, Case studies of bus…

## g0716（1 列）
- 見出し：Title
- 例1 値：Huonville | Scottsdale | Hobart | New Norfolk | Launceston
  - 同じ表の列：Hours, Googlemap

## g0717（1 列）
- 見出し：Hours
- 例1 値：Monday to Friday 9.00am - 4.30pm | Monday to Friday 8.45am - 4.45pm | Monday to Friday 9.30am to 4.00pm | Monday to Friday 9.00am - 4.30pm | Monday to Friday 9.00am - 4.30pm
  - 同じ表の列：Title, Googlemap

## g0718（1 列）
- 見出し：Googlemap
- 例1 値：https://goo.gl/maps/21YmL | https://goo.gl/maps/f8ffU | https://goo.gl/maps/QQjH8 | https://goo.gl/maps/cfiyQ | https://goo.gl/maps/OF1mU
  - 同じ表の列：Title, Hours

## g0719（1 列）
- 見出し：Paymenttype
- 例1 値：Youth Allowance (other) | Parenting Payment Single | Youth Allowance (apprentice) | Youth Allowance (student) | Sickness Allowance
  - 同じ表の列：Totalentries (Betwe…, Exitedwithintwelvem…, Percentexitedwithin…

## g0720（1 列）
- 見出し：Totalentries (Between1Apr2013-31Mar2014)
- 例1 値：456368.0 | 5099.0 | 122679.0 | 18697.0 | 38252.0
  - 同じ表の列：Paymenttype, Exitedwithintwelvem…, Percentexitedwithin…

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
