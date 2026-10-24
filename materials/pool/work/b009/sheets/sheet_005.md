# ラベル用シート 005 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_005.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0481（1 列）
- 見出し：Amenities
- 例1 値：Heating and Cooling Car parking Outdoor…
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs

## g0482（1 列）
- 見出し：Hire_Agreements
- 例1 値：Click on the links to download hire agr…
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs

## g0483（1 列）
- 見出し：operation
- 例1 値：Manual Wind-Down | Not Applicable | Manual Wind-Down | Manual Wind-Down | Manual Wind-Down
  - 同じ表の列：ref, size_diam

## g0484（1 列）
- 見出し：size_diam
- 例1 値：800 | 375 | Not Applicable | 1000 | 600
  - 同じ表の列：ref, operation

## g0485（1 列）
- 見出し：type
- 例1 値：Park Tree | Park Tree | Park Tree | Park Tree | Park Tree
  - 同じ表の列：suburb, easting, northing, melway_ref, Genus, Species

## g0486（1 列）
- 見出し：easting
- 例1 値：311229.12 | 311217.96 | 311204.65 | 304862.05 | 311219.36
  - 同じ表の列：type, suburb, northing, melway_ref, Genus, Species

## g0487（1 列）
- 見出し：northing
- 例1 値：5806761.77 | 5809271.03 | 5806759.27 | 5806834.37 | 5809417.45
  - 同じ表の列：type, suburb, easting, melway_ref, Genus, Species

## g0488（1 列）
- 見出し：melway_ref
- 例1 値：53:G10 | 53:G10 | 53:G10 | 53:G10 | 55:C4
  - 同じ表の列：type, suburb, easting, northing, Genus, Species

## g0489（1 列）
- 見出し：Species
- 例1 値：styphelioides | sideroxylon | melliodora | sp. | sideroxylon
  - 同じ表の列：type, suburb, easting, northing, melway_ref, Genus

## g0490（2 列）
- 見出し：Agency
- 例1 値：Rous County Council | Albury City Council | Department of Planning and Infrastructu… | Cessnock City Council | Rous County Council
  - 同じ表の列：Application Accesss, Application Outcome, Application Transfe…, Calendar Year, Cluster, Count, Decision, Fiscal Year
- 例2 値：Coorong District Council | Mid Murray Council | District Council of Loxton Waikerie | Copper Coast Council | Naracoorte Lucindale Council
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0491（1 列）
- 見出し：Application Accesss
- 例1 値：Partly | Wholly | Wholly | Partly | Partly
  - 同じ表の列：Agency, Application Outcome, Application Transfe…, Calendar Year, Cluster, Count, Decision, Fiscal Year

## g0492（1 列）
- 見出し：Application Outcome
- 例1 値：Access Granted in Part | Access Granted in Full | Information not Held | Application Withdrawn | Application Withdrawn
  - 同じ表の列：Agency, Application Accesss, Application Transfe…, Calendar Year, Cluster, Count, Decision, Fiscal Year

## g0493（1 列）
- 見出し：Application Transferred
- 例1 値：Agency-Initiated Transfers | Agency-Initiated Transfers | Agency-Initiated Transfers | Applicant - Initiated Transfers | Agency-Initiated Transfers
  - 同じ表の列：Agency, Application Accesss, Application Outcome, Calendar Year, Cluster, Count, Decision, Fiscal Year

## g0494（1 列）
- 見出し：Calendar Year
- 例1 値：State Owned Corporations | State Owned Corporations | State Owned Corporations | State Owned Corporations | State Owned Corporations
  - 同じ表の列：Agency, Application Accesss, Application Outcome, Application Transfe…, Cluster, Count, Decision, Fiscal Year

## g0495（1 列）
- 見出し：Cluster
- 例1 値：Finance and Services | Councils | Family and Community Services | Councils | Transport
  - 同じ表の列：Agency, Application Accesss, Application Outcome, Application Transfe…, Calendar Year, Count, Decision, Fiscal Year

## g0496（1 列）
- 見出し：Decision
- 例1 値：Decision varied | Decision varied | Decision varied | Decision varied | Decision upheld
  - 同じ表の列：Agency, Application Accesss, Application Outcome, Application Transfe…, Calendar Year, Cluster, Count, Fiscal Year

## g0497（1 列）
- 見出し：Fiscal Year
- 例1 値：2014 | 2019 | 2015 | 2016 | 2019
  - 同じ表の列：Agency, Application Accesss, Application Outcome, Application Transfe…, Calendar Year, Cluster, Count, Decision

## g0498（1 列）
- 見出し：Information made publicly available
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Agency, Application Accesss, Application Outcome, Application Transfe…, Calendar Year, Cluster, Count, Decision

## g0499（1 列）
- 見出し：Variable type
- 例1 値：VARCHAR2(3) | VARCHAR2(1) | NUMBER | NUMBER | VARCHAR2(7)
  - 同じ表の列：Nullable

## g0500（1 列）
- 見出し：Nullable
- 例1 値：Y | Y | Y
  - 同じ表の列：Variable type

## g0501（1 列）
- 見出し：Leash Free Times
- 例1 値：Sunrise to 10am daily (except market da… | All times | All times | Sunrise to 10am weekdays only | All times
  - 同じ表の列：Suburb

## g0502（1 列）
- 見出し：asset_id
- 例1 値：BU002 | BU282 | BU272 | BU257 | BU356
  - 同じ表の列：class, subtype, manager, ward, lat

## g0503（1 列）
- 見出し：class
- 例1 値：Sporting Facilities | Council Work Places | Heritage | Community Facility | Sporting Facilities
  - 同じ表の列：asset_id, subtype, manager, ward, lat

## g0504（1 列）
- 見出し：subtype
- 例1 値：Swimming Pools | Public Hall | Community Facility | Sports Pavilions | Nursing Home
  - 同じ表の列：asset_id, class, manager, ward, lat

## g0505（1 列）
- 見出し：manager
- 例1 値：Owned and Maintained by Manningham City… | Owned and Maintained by Manningham City… | Crown Land - Managed by Manningham City… | Owned and Maintained by Manningham City… | Owned and Maintained by Manningham City…
  - 同じ表の列：asset_id, class, subtype, ward, lat

## g0506（1 列）
- 見出し：ward
- 例1 値：Mullum Mullum | Heide | Mullum Mullum | Mullum Mullum | Koonung
  - 同じ表の列：asset_id, class, subtype, manager, lat

## g0507（1 列）
- 見出し：val_date
- 例1 値：2022-11-30T09:15:17Z | 2022-12-01T09:00:15Z | 2022-11-27T17:15:18Z | 2022-11-30T08:30:19Z | 2022-12-01T10:00:16Z
  - 同じ表の列：dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g0508（1 列）
- 見出し：dev_netid
- 例1 値：mil-gw01 | mil-gw01 | mil-gw01 | mil-gw01 | mil-gw01
  - 同じ表の列：val_date, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g0509（1 列）
- 見出し：dev_chid
- 例1 値：2 | 1 | 2 | 2 | 2
  - 同じ表の列：val_date, dev_netid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g0510（1 列）
- 見出し：val_raw
- 例1 値：1316 | 133 | 133 | 321 | 329
  - 同じ表の列：val_date, dev_netid, dev_chid, val_type, dev_tag, dev_site, val_cal, val_offset

## g0511（1 列）
- 見出し：val_type
- 例1 値：Gateway Messages | Gateway Messages | Gateway Messages | Gateway Messages | Gateway Messages
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, dev_tag, dev_site, val_cal, val_offset

## g0512（1 列）
- 見出し：dev_tag
- 例1 値：MIL-GW01 | MIL-GW01 | MIL-GW01 | MIL-GW01 | MIL-GW01
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_site, val_cal, val_offset

## g0513（1 列）
- 見出し：dev_site
- 例1 値：Gateways - MRCC | Gateways - MRCC | Gateways - MRCC | Gateways - MRCC | Gateways - MRCC
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, val_cal, val_offset

## g0514（1 列）
- 見出し：val_cal
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_offset

## g0515（1 列）
- 見出し：val_offset
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal

## g0516（1 列）
- 見出し：dev_type
- 例1 値：gateway | gateway | gateway | gateway | gateway
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal

## g0517（1 列）
- 見出し：SurveyProgram
- 例1 値：Specified Environmental Assets (SEA) | Specified Environmental Assets (SEA) | Specified Environmental Assets (SEA) | Specified Environmental Assets (SEA) | Specified Environmental Assets (SEA)
  - 同じ表の列：SurvYear, Date, Identifier, Wetland, Subwetland, Fx_Group, SppCode, ReplicateCount

## g0518（1 列）
- 見出し：SurvYear
- 例1 値：2008 | 2008 | 2007 | 2008 | 2008
  - 同じ表の列：SurveyProgram, Date, Identifier, Wetland, Subwetland, Fx_Group, SppCode, ReplicateCount

## g0519（1 列）
- 見出し：Date
- 例1 値：14/11/2007 | 13/11/2007 | 14/11/2007 | 13/11/2008 | 13/11/2008
  - 同じ表の列：SurveyProgram, SurvYear, Identifier, Wetland, Subwetland, Fx_Group, SppCode, ReplicateCount

## g0520（1 列）
- 見出し：Identifier
- 例1 値：7 | 7 | 7 | 15 | 7
  - 同じ表の列：SurveyProgram, SurvYear, Date, Wetland, Subwetland, Fx_Group, SppCode, ReplicateCount

## g0521（1 列）
- 見出し：Wetland
- 例1 値：River Murray Channel | River Murray Channel | Murray Bridge | Lindsay-Walpolla-Chowilla | Albury
  - 同じ表の列：SurveyProgram, SurvYear, Date, Identifier, Subwetland, Fx_Group, SppCode, ReplicateCount

## g0522（1 列）
- 見出し：Subwetland
- 例1 値：Lacepede Bay | Murray 3 | Murray 1B | Lake Alexandrina A | Mannum E
  - 同じ表の列：SurveyProgram, SurvYear, Date, Identifier, Wetland, Fx_Group, SppCode, ReplicateCount

## g0523（1 列）
- 見出し：Fx_Group
- 例1 値：He | Pi | Du | Du | La
  - 同じ表の列：SurveyProgram, SurvYear, Date, Identifier, Wetland, Subwetland, SppCode, ReplicateCount

## g0524（1 列）
- 見出し：SppCode
- 例1 値：LGW | MNU | BDU | SMW | MHE
  - 同じ表の列：SurveyProgram, SurvYear, Date, Identifier, Wetland, Subwetland, Fx_Group, ReplicateCount

## g0525（1 列）
- 見出し：ReplicateCount
- 例1 値：1 | 2 | 1 | 1 | 2
  - 同じ表の列：SurveyProgram, SurvYear, Date, Identifier, Wetland, Subwetland, Fx_Group, SppCode

## g0526（1 列）
- 見出し：SumOfCount
- 例1 値：20 | 280 | 697 | 10 | 240
  - 同じ表の列：SurveyProgram, SurvYear, Date, Identifier, Wetland, Subwetland, Fx_Group, SppCode

## g0527（1 列）
- 見出し：Location_Type
- 例1 値：LGA | LGA | LGA | LGA | LGA
  - 同じ表の列：Location_code, STATE, agrn, cat_A, cat_B, cat_C, cat_D, highest_drfa_catego…

## g0528（1 列）
- 見出し：Location_code
- 例1 値：12700 | 16200 | 18350 | 21180 | 21110
  - 同じ表の列：Location_Type, STATE, agrn, cat_A, cat_B, cat_C, cat_D, highest_drfa_catego…

## g0529（1 列）
- 見出し：STATE
- 例1 値：New South Wales | New South Wales | New South Wales | New South Wales | New South Wales
  - 同じ表の列：Location_Type, Location_code, agrn, cat_A, cat_B, cat_C, cat_D, highest_drfa_catego…

## g0530（1 列）
- 見出し：agrn
- 例1 値：1205 | 1034 | 1096 | 987 | 960
  - 同じ表の列：Location_Type, Location_code, STATE, cat_A, cat_B, cat_C, cat_D, highest_drfa_catego…

## g0531（1 列）
- 見出し：cat_A
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Location_Type, Location_code, STATE, agrn, cat_B, cat_C, cat_D, highest_drfa_catego…

## g0532（1 列）
- 見出し：cat_B
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Location_Type, Location_code, STATE, agrn, cat_A, cat_C, cat_D, highest_drfa_catego…

## g0533（1 列）
- 見出し：cat_C
- 例1 値：0 | 0 | 0 | 0 | 1
  - 同じ表の列：Location_Type, Location_code, STATE, agrn, cat_A, cat_B, cat_D, highest_drfa_catego…

## g0534（1 列）
- 見出し：cat_D
- 例1 値：1 | 0 | 1 | 0 | 0
  - 同じ表の列：Location_Type, Location_code, STATE, agrn, cat_A, cat_B, cat_C, highest_drfa_catego…

## g0535（1 列）
- 見出し：highest_drfa_category_group
- 例1 値：C/D | C/D | C/D | A/B | A/B
  - 同じ表の列：Location_Type, Location_code, STATE, agrn, cat_A, cat_B, cat_C, cat_D

## g0536（1 列）
- 見出し：AGDRP
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Location_Type, Location_code, STATE, agrn, cat_A, cat_B, cat_C, cat_D

## g0537（1 列）
- 見出し：State/Territory
- 例1 値：WA | NSW | SA | TAS | ACT
  - 同じ表の列：Month, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0538（2 列）
- 見出し：Month
- 例1 値：August | April | May | November | December
  - 同じ表の列：State/Territory, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22
- 例2 値：March | June | May | December | July
  - 同じ表の列：Port of Entry, Fiscal Year, Count of Delays, Percentage Met Serv…

## g0539（1 列）
- 見出し：2015-16
- 例1 値：83357464 | 907141876 | 76629717 | 277837576 | 653263304
  - 同じ表の列：State/Territory, Month, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0540（1 列）
- 見出し：project_type
- 例1 値：Local Economic Recovery Funding | Local Economic Recovery Funding | Local Economic Recovery Funding | Local Economic Recovery Funding | Local Economic Recovery Funding
  - 同じ表の列：id, lat, long, location, lga, cwlth_state_funding, project_status, recovery_type

## g0541（1 列）
- 見出し：location
- 例1 値：n/a | Batlow | Uralla | Maclean | Esk (Qld)
  - 同じ表の列：id, lat, long, project_type, lga, cwlth_state_funding, project_status, recovery_type

## g0542（1 列）
- 見出し：lga
- 例1 値：Towong (S) | Kyogle (A) | East Gippsland (S) | Eurobodalla (A) | Bega Valley (A)
  - 同じ表の列：id, lat, long, project_type, location, cwlth_state_funding, project_status, recovery_type

## g0543（1 列）
- 見出し：cwlth_state_funding
- 例1 値：Up to $919,206 | Up to $720,500 | Up to $189,000 | Up to $724,190 | Up to $205,000
  - 同じ表の列：id, lat, long, project_type, location, lga, project_status, recovery_type

## g0544（1 列）
- 見出し：project_status
- 例1 値：In progress | Not yet commenced | Not yet commenced | Not yet commenced | In progress
  - 同じ表の列：id, lat, long, project_type, location, lga, cwlth_state_funding, recovery_type

## g0545（1 列）
- 見出し：recovery_type
- 例1 値：Infrastructure | Human/Social | Economic | Economic | Human/Social
  - 同じ表の列：id, lat, long, project_type, location, lga, cwlth_state_funding, project_status

## g0546（1 列）
- 見出し：Primary Breed
- 例1 値：Labrador | Pomerania | Maltese | JackRusslX | TerrierYk
  - 同じ表の列：Gender

## g0547（1 列）
- 見出し：school_code
- 例1 値：1199 | 5265 | 2970 | 2053 | 2056
  - 同じ表の列：town_suburb, operational_directo…, principal_network, electorate, class_type, level_of_schooling

## g0548（1 列）
- 見出し：town_suburb
- 例1 値：WARATAH | Macksville | Enfield | Fennell Bay | SMITHFIELD
  - 同じ表の列：school_code, operational_directo…, principal_network, electorate, class_type, level_of_schooling

## g0549（1 列）
- 見出し：operational_directorate
- 例1 値：Regional North | Metropolitan South and West | Metropolitan South and West | Regional North and West | Metropolitan South and West
  - 同じ表の列：school_code, town_suburb, principal_network, electorate, class_type, level_of_schooling

## g0550（1 列）
- 見出し：principal_network
- 例1 値：Cowra | Iron Cove | Chullora | Bankstown | Pittwater
  - 同じ表の列：school_code, town_suburb, operational_directo…, electorate, class_type, level_of_schooling

## g0551（1 列）
- 見出し：electorate
- 例1 値：Castle Hill | Cabramatta | Auburn | Liverpool | Albury
  - 同じ表の列：school_code, town_suburb, operational_directo…, principal_network, class_type, level_of_schooling

## g0552（1 列）
- 見出し：class_type
- 例1 値：Supporting students with a range of dis… | Supporting students with mild intellect… | Supporting students with mild intellect… | Supporting students with a range of dis… | Supporting students with a range of dis…
  - 同じ表の列：school_code, town_suburb, operational_directo…, principal_network, electorate, level_of_schooling

## g0553（1 列）
- 見出し：level_of_schooling
- 例1 値：Primary School | Central/Community School | Primary School | Primary School | Primary School
  - 同じ表の列：school_code, town_suburb, operational_directo…, principal_network, electorate, class_type

## g0554（1 列）
- 見出し：test_date
- 例1 値：2020-03-09 | 2020-03-09 | 2020-03-09 | 2020-03-09 | 2020-03-09
  - 同じ表の列：age_group

## g0555（1 列）
- 見出し：age_group
- 例1 値：AgeGroup_0-9 | AgeGroup_20-29 | AgeGroup_10-19 | AgeGroup_20-29 | AgeGroup_20-29
  - 同じ表の列：test_date

## g0556（1 列）
- 見出し：Civil
- 例1 値：29423 | 30758 | 21080 | 29862 | 31676
  - 同じ表の列：Year, Religious

## g0557（1 列）
- 見出し：Religious
- 例1 値：6069 | 7417 | 8867 | 9861 | 8143
  - 同じ表の列：Year, Civil

## g0558（1 列）
- 見出し：Requests for personal information
- 例1 値：No data | No data | 22033 | No data | 25119
  - 同じ表の列：Year, Requests for other …, Total requests, Application fees AUD, Internal review fee…, Charges notified AUD, Charges collected A…, Total fees and char…

## g0559（1 列）
- 見出し：Requests for other information
- 例1 値：6364 | 2764 | No data | 3517 | 4335
  - 同じ表の列：Year, Requests for person…, Total requests, Application fees AUD, Internal review fee…, Charges notified AUD, Charges collected A…, Total fees and char…

## g0560（1 列）
- 見出し：Total requests
- 例1 値：5576 | 23543 | 36512 | 33804 | 38787
  - 同じ表の列：Year, Requests for person…, Requests for other …, Application fees AUD, Internal review fee…, Charges notified AUD, Charges collected A…, Total fees and char…

## g0561（1 列）
- 見出し：Application fees AUD
- 例1 値：413044 | 256172 | 163180 | 147966 | 374396
  - 同じ表の列：Year, Requests for person…, Requests for other …, Total requests, Internal review fee…, Charges notified AUD, Charges collected A…, Total fees and char…

## g0562（1 列）
- 見出し：Internal review fees AUD
- 例1 値：3787 | 4345 | 0 | 5600 | 5760
  - 同じ表の列：Year, Requests for person…, Requests for other …, Total requests, Application fees AUD, Charges notified AUD, Charges collected A…, Total fees and char…

## g0563（1 列）
- 見出し：Charges notified AUD
- 例1 値：386726 | 129392 | 501189 | 113043 | 22247
  - 同じ表の列：Year, Requests for person…, Requests for other …, Total requests, Application fees AUD, Internal review fee…, Charges collected A…, Total fees and char…

## g0564（1 列）
- 見出し：Charges collected AUD
- 例1 値：2067.14 | 305178 | 81353 | 240458 | 75537
  - 同じ表の列：Year, Requests for person…, Requests for other …, Total requests, Application fees AUD, Internal review fee…, Charges notified AUD, Total fees and char…

## g0565（1 列）
- 見出し：Total fees and charges collected AUD
- 例1 値：309998 | 393865 | 73067 | 502554 | 81353
  - 同じ表の列：Year, Requests for person…, Requests for other …, Total requests, Application fees AUD, Internal review fee…, Charges notified AUD, Charges collected A…

## g0566（1 列）
- 見出し：Estimated costs AUD
- 例1 値：12723097 | 13336864 | 27484129 | 13066029 | 59844983
  - 同じ表の列：Year, Requests for person…, Requests for other …, Total requests, Application fees AUD, Internal review fee…, Charges notified AUD, Charges collected A…

## g0567（1 列）
- 見出し：2017-18
- 例1 値：0 | 2013-14 | 2014-15 | 0 | 0
  - 同じ表の列：2016-17, % Change (+/-)

## g0568（1 列）
- 見出し：2016-17
- 例1 値：0 | 0 | 0 | 0 | 2012-13
  - 同じ表の列：2017-18, % Change (+/-)

## g0569（1 列）
- 見出し：% Change (+/-)
- 例1 値：0 | % Change (+/-) | 0 | % Change (+/-) | 0
  - 同じ表の列：2017-18, 2016-17

## g0570（1 列）
- 見出し：2019-20
- 例1 値：Total all consultancies | Total value of consultancies below $10,… | Total consultants combined | University of South Australia | All consultancies above $10,000 each
  - 同じ表の列：Purpose, Value

## g0571（1 列）
- 見出し：Purpose
- 例1 値：Research into community mental health t… | Subtotal | Various | Not applicable
  - 同じ表の列：2019-20, Value

## g0572（1 列）
- 見出し：Value
- 例1 値：19,702 | 19,702 | 19,702 | Nil
  - 同じ表の列：2019-20, Purpose

## g0573（1 列）
- 見出し：Jun-21
- 例1 値：55-64 | 25-34 | Classification | Gender | Under 25
  - 同じ表の列：57, 33, 24, 50.85, 10.2

## g0574（1 列）
- 見出し：57
- 例1 値：Number (Headcount) | 1 | 0 | 12 | 12
  - 同じ表の列：Jun-21, 33, 24, 50.85, 10.2

## g0575（1 列）
- 見出し：33
- 例1 値：0 | 6.7 | 0.7 | 36 | 1
  - 同じ表の列：Jun-21, 57, 24, 50.85, 10.2

## g0576（1 列）
- 見出し：24
- 例1 値：2.6 | 2 | 2.2 | 3 | Fixed-term & Casual
  - 同じ表の列：Jun-21, 57, 33, 50.85, 10.2

## g0577（1 列）
- 見出し：50.85
- 例1 値：18 | 35 | 1 | 14 | 51.1
  - 同じ表の列：Jun-21, 57, 33, 24, 10.2

## g0578（1 列）
- 見出し：10.2
- 例1 値：10.7 | 0.7 | 19.2 | 9.3 | 7.7
  - 同じ表の列：Jun-21, 57, 33, 24, 50.85

## g0579（1 列）
- 見出し：ANZSCO group
- 例1 値：Other Hospitality, Retail and Service M… | Purchasing and Supply Logistics Clerks | Environmental Scientists | Librarians | Education Aides
  - 同じ表の列：4-digit ANZSCO code, FTE, % Female, % Male, % below age 25, % age 25-44, % age 45 and over, PSGOGA Equivalent S…

## g0580（1 列）
- 見出し：4-digit ANZSCO code
- 例1 値：5999 | 4115 | 5619 | 1413 | 1342
  - 同じ表の列：ANZSCO group, FTE, % Female, % Male, % below age 25, % age 25-44, % age 45 and over, PSGOGA Equivalent S…

## g0581（1 列）
- 見出し：FTE
- 例1 値：233 | 547 | 453 | 165 | 322
  - 同じ表の列：ANZSCO group, 4-digit ANZSCO code, % Female, % Male, % below age 25, % age 25-44, % age 45 and over, PSGOGA Equivalent S…

## g0582（1 列）
- 見出し：% Female
- 例1 値：63.4% | 65.0% | 20.4% | 70.6% | 60.5%
  - 同じ表の列：ANZSCO group, 4-digit ANZSCO code, FTE, % Male, % below age 25, % age 25-44, % age 45 and over, PSGOGA Equivalent S…

## g0583（1 列）
- 見出し：% Male
- 例1 値：35.0% | 16.8% | 37.0% | 54.7% | 81.9%
  - 同じ表の列：ANZSCO group, 4-digit ANZSCO code, FTE, % Female, % below age 25, % age 25-44, % age 45 and over, PSGOGA Equivalent S…

## g0584（1 列）
- 見出し：% below age 25
- 例1 値：11.7% | 2.7% | 0.4% | 14.1% | 1.5%
  - 同じ表の列：ANZSCO group, 4-digit ANZSCO code, FTE, % Female, % Male, % age 25-44, % age 45 and over, PSGOGA Equivalent S…

## g0585（1 列）
- 見出し：% age 25-44
- 例1 値：36.4% | 24.0% | 45.8% | 33.8% | 33.8%
  - 同じ表の列：ANZSCO group, 4-digit ANZSCO code, FTE, % Female, % Male, % below age 25, % age 45 and over, PSGOGA Equivalent S…

## g0586（1 列）
- 見出し：% age 45 and over
- 例1 値：39.8% | 63.3% | 8.6% | 67.1% | 54.1%
  - 同じ表の列：ANZSCO group, 4-digit ANZSCO code, FTE, % Female, % Male, % below age 25, % age 25-44, PSGOGA Equivalent S…

## g0587（1 列）
- 見出し：PSGOGA Equivalent Salary Bands Level 1 and below
- 例1 値：0.5% | 3.5% | 0.3% | 1.4% | 0.0%
  - 同じ表の列：ANZSCO group, 4-digit ANZSCO code, FTE, % Female, % Male, % below age 25, % age 25-44, % age 45 and over

## g0588（1 列）
- 見出し：PSGOGA Equivalent Salary Bands Level 2
- 例1 値：60.2% | 20.4% | 0.0% | 2.8% | 0.4%
  - 同じ表の列：ANZSCO group, 4-digit ANZSCO code, FTE, % Female, % Male, % below age 25, % age 25-44, % age 45 and over

## g0589（1 列）
- 見出し：financial_year
- 例1 値：2008-2009 | 2008-2009 | 2007-2008 | 2013-2014 | 2012-2013
  - 同じ表の列：wpm_material_type, waste_stream, recycled, waste_to_energy, export_interstate, export_international, disposal, recovery_rate

## g0590（1 列）
- 見出し：wpm_material_type
- 例1 値：Paper and cardboard | Aggregate, masonry and soils | Metals | Aggregate, masonry and soils | Tyres and rubber
  - 同じ表の列：financial_year, waste_stream, recycled, waste_to_energy, export_interstate, export_international, disposal, recovery_rate

## g0591（1 列）
- 見出し：waste_stream
- 例1 値：Commercial and Industrial | Construction and Demolition | Commercial and Industrial | Municipal Solid Waste | Construction and Demolition
  - 同じ表の列：financial_year, wpm_material_type, recycled, waste_to_energy, export_interstate, export_international, disposal, recovery_rate

## g0592（1 列）
- 見出し：recycled
- 例1 値：438310.000000000000000 | 113451.000000000000000 | 42359.000000000000000 | 43673.000000000000000 | 0.000000000000000
  - 同じ表の列：financial_year, wpm_material_type, waste_stream, waste_to_energy, export_interstate, export_international, disposal, recovery_rate

## g0593（1 列）
- 見出し：waste_to_energy
- 例1 値：0.000000000000000 | 0.000000000000000 | 0.000000000000000 | 0.000000000000000 | 0.000000000000000
  - 同じ表の列：financial_year, wpm_material_type, waste_stream, recycled, export_interstate, export_international, disposal, recovery_rate

## g0594（1 列）
- 見出し：export_interstate
- 例1 値：0.000000000000000 | 0.000000000000000 | 0.000000000000000 | 0.000000000000000 | 0.000000000000000
  - 同じ表の列：financial_year, wpm_material_type, waste_stream, recycled, waste_to_energy, export_international, disposal, recovery_rate

## g0595（1 列）
- 見出し：export_international
- 例1 値：0.000000000000000 | 205881.519908000000000 | 0.000000000000000 | 0.000000000000000 | 0.000000000000000
  - 同じ表の列：financial_year, wpm_material_type, waste_stream, recycled, waste_to_energy, export_interstate, disposal, recovery_rate

## g0596（1 列）
- 見出し：disposal
- 例1 値：5805.763904000000000 | 78310.749617000000000 | 0.000000000000000 | 74930.349871000000000 | 0.000000000000000
  - 同じ表の列：financial_year, wpm_material_type, waste_stream, recycled, waste_to_energy, export_interstate, export_international, recovery_rate

## g0597（1 列）
- 見出し：recovery_rate
- 例1 値：0.000000 | 0.028371 | 1.000000 | 0.108683 | 0.916858
  - 同じ表の列：financial_year, wpm_material_type, waste_stream, recycled, waste_to_energy, export_interstate, export_international, disposal

## g0598（1 列）
- 見出し：Workplace injury claims
- 例1 値：Seriously injured workers* | Work health and safety regulation | Income support payments - gross ($) | Total gross workers compensation expend… | Significant injuries (where lost time e…
  - 同じ表の列：WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…

## g0599（1 列）
- 見出し：WHS and return to work performance 2016-17
- 例1 値：0 | 0 | 1 | 0 | 0
  - 同じ表の列：Workplace injury cl…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…

## g0600（1 列）
- 見出し：WHS and return to work performance 2017-18
- 例1 値：1 | 0 | 0 | 0 | 26335
  - 同じ表の列：Workplace injury cl…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…, WHS and return to w…

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
