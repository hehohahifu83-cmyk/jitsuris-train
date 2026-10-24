# ラベル用シート 005 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_005.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0481（1 列）
- 見出し：Record number
- 例1 値：2429 | 2313 | 2238 | 1694 | 2336
  - 同じ表の列：Timestamp, Average Water Speed, Average Water Direc…, Chlorophyll, Chlorophyll [qualit…, Temperature, Temperature [qualit…, Dissolved Oxygen

## g0482（1 列）
- 見出し：Average Water Speed
- 例1 値：7.963 | 5.515 | 4.723 | 3.348 | 5.904
  - 同じ表の列：Timestamp, Record number, Average Water Direc…, Chlorophyll, Chlorophyll [qualit…, Temperature, Temperature [qualit…, Dissolved Oxygen

## g0483（1 列）
- 見出し：Average Water Direction
- 例1 値：199.145 | 69.065 | 63.004 | 316.727 | 19.139
  - 同じ表の列：Timestamp, Record number, Average Water Speed, Chlorophyll, Chlorophyll [qualit…, Temperature, Temperature [qualit…, Dissolved Oxygen

## g0484（1 列）
- 見出し：Chlorophyll
- 例1 値：2.388 | 2.57 | 2.689 | 2.324 | 4.968
  - 同じ表の列：Timestamp, Record number, Average Water Speed, Average Water Direc…, Chlorophyll [qualit…, Temperature, Temperature [qualit…, Dissolved Oxygen

## g0485（1 列）
- 見出し：Chlorophyll [quality]
- 例1 値：1020 | 1020 | 1020 | 1020 | 1020
  - 同じ表の列：Timestamp, Record number, Average Water Speed, Average Water Direc…, Chlorophyll, Temperature, Temperature [qualit…, Dissolved Oxygen

## g0486（1 列）
- 見出し：Temperature
- 例1 値：20.61 | 19.884 | 20.15 | 18.588 | 19.996
  - 同じ表の列：Timestamp, Record number, Average Water Speed, Average Water Direc…, Chlorophyll, Chlorophyll [qualit…, Temperature [qualit…, Dissolved Oxygen

## g0487（1 列）
- 見出し：Temperature [quality]
- 例1 値：1020 | 1020 | 1020 | 1020 | 1020
  - 同じ表の列：Timestamp, Record number, Average Water Speed, Average Water Direc…, Chlorophyll, Chlorophyll [qualit…, Temperature, Dissolved Oxygen

## g0488（1 列）
- 見出し：Dissolved Oxygen
- 例1 値：7.414 | 7.27 | 7.172 | 7.577 | 7.59
  - 同じ表の列：Timestamp, Record number, Average Water Speed, Average Water Direc…, Chlorophyll, Chlorophyll [qualit…, Temperature, Temperature [qualit…

## g0489（1 列）
- 見出し：Dissolved Oxygen [quality]
- 例1 値：1020 | 1020 | 1020 | 1020 | 1020
  - 同じ表の列：Timestamp, Record number, Average Water Speed, Average Water Direc…, Chlorophyll, Chlorophyll [qualit…, Temperature, Temperature [qualit…

## g0490（1 列）
- 見出し：Consultants
- 例1 値：Incenta Economic Consulting | Sapere Research Group Limited | Bureau of Meteorology | Incenta Economic Consulting | Cardno (Qld) Pty Ltd
  - 同じ表の列：Year, Purpose, Value

## g0491（1 列）
- 見出し：Purpose
- 例1 値：Market scan for regulatory case managem… | Review of regulatory models | Review the technical clauses in the EDC | Economic assessment of electricity dist… | Local Government Advice
  - 同じ表の列：Year, Consultants, Value

## g0492（1 列）
- 見出し：Value
- 例1 値：$21,804 | 33,460 | $2,300 | $20,700 | 22,050
  - 同じ表の列：Year, Consultants, Purpose

## g0493（1 列）
- 見出し：Complex_Type
- 例1 値：Recreation Reserve | Recreation Reserve | Recreation Reserve | Recreation Reserve | Recreation Reserve
  - 同じ表の列：Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs, LAT

## g0494（1 列）
- 見出し：Facility_Type
- 例1 値：Tennis Court | Tennis Court | Tennis Court | Tennis Court | Tennis Court
  - 同じ表の列：Complex_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs, LAT

## g0495（1 列）
- 見出し：Bookable_Item
- 例1 値：Mannibadar Tennis Reserve Tennis Court 2 | Inverleigh Tennis Reserve Tennis Court 4 | Napoleons Recreation Reserve Tennis Cou… | Lethbridge Recreation Reserve Tennis Co… | Ross Creek Recreation Reserve Tennis Co…
  - 同じ表の列：Complex_Type, Facility_Type, Assessment_No, Number, Locality, Post_Code, Home_Clubs, LAT

## g0496（1 列）
- 見出し：Assessment_No
- 例1 値：66379102 | 36600007 | 36600007 | 36600007 | 41400035
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Number, Locality, Post_Code, Home_Clubs, LAT

## g0497（3 列）
- 見出し：Number
- 例1 値：655 | 60 | 17 | 1462 | 396
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Locality, Post_Code, Home_Clubs, LAT
- 例2 値：3506 | 451 | 12685 | 13 | 13774
  - 同じ表の列：WEEK_NO, YEAR, DATE, CLASSIFICATION_CATE…, ANIMAL_CARCASE

## g0498（1 列）
- 見出し：Locality
- 例1 値：Enfield | Napoleons | Linton | Inverleigh | Grenville
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Post_Code, Home_Clubs, LAT

## g0499（1 列）
- 見出し：Post_Code
- 例1 値：3331 | 3321 | 3352 | 3333 | 3360
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Home_Clubs, LAT

## g0500（1 列）
- 見出し：Home_Clubs
- 例1 値：Bannockburn Tennis Club | Number of courts: 6 Surface: Asphalt/Sy… | Bannockburn Tennis Club | Sutherlands Creek Tennis Club | Gheringhap Tennis Club
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, LAT

## g0501（2 列）
- 見出し：ref
- 例1 値：PF00507 | PF00526 | PF00501 | PF00520 | PF00551
  - 同じ表の列：location, num_of, num_burner, type
- 例2 値：PF20257 | PF20823 | PF20659 | PF20121 | SF4339
  - 同じ表の列：seat, num_of, material, type

## g0502（1 列）
- 見出し：location
- 例1 値：Tatura Ornamental Lake Reserve | Aquamoves (Shepparton) | Deakin Park (Shepparton) | John Pick Reserve (Shepparton) | Victoria Park Lake Caravan Park (Shepp)
  - 同じ表の列：ref, num_of, num_burner, type

## g0503（2 列）
- 見出し：num_of
- 例1 値：1 | 1 | 1 | 1 | 2
  - 同じ表の列：ref, location, num_burner, type
- 例2 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：ref, seat, material, type

## g0504（1 列）
- 見出し：num_burner
- 例1 値：2 Burner | 1 Burner | 1 Burner | 2 Burner | 2 Burner
  - 同じ表の列：ref, location, num_of, type

## g0505（1 列）
- 見出し：type
- 例1 値：Brick/Steel | Steel/Aluminium | Brick/Steel | Steel/Aluminium | Brick/Steel
  - 同じ表の列：ref, location, num_of, num_burner

## g0506（1 列）
- 見出し：Contractors
- 例1 値：Bmp Marketing Pty Ltd | Baukultur Pty Ltd | Super Studio Australia Pty Ltd | Cerulean Creative Studios | Erin Bridges
  - 同じ表の列：Purpose, $ Actual payment

## g0507（1 列）
- 見出し：Purpose
- 例1 値：Purpose | Cleaning Contractor | Video and editing | Temporary ICT Support | Cleaning Contractor
  - 同じ表の列：Contractors, $ Actual payment

## g0508（1 列）
- 見出し：$ Actual payment
- 例1 値：$140,589 | $19,300 | $28,581 | $40,236 | $36,191
  - 同じ表の列：Contractors, Purpose

## g0509（1 列）
- 見出し：Location
- 例1 値：Newport Lakes | Gloucester Reserve | Williamstown Rotunda Gardens | Williamstown Railway Reserve | Paine Reserve
  - 同じ表の列：Suburb, Numberof, BicycleRackMaterial

## g0510（1 列）
- 見出し：Numberof
- 例1 値：1.00 | 1.00 | 1.00 | 1.00 | 1.00
  - 同じ表の列：Location, Suburb, BicycleRackMaterial

## g0511（1 列）
- 見出し：BicycleRackMaterial
- 例1 値：Stainless | Steel | Stainless | Stainless | Stainless
  - 同じ表の列：Location, Suburb, Numberof

## g0512（1 列）
- 見出し：appl_number
- 例1 値：2017904657 | 2008901188 | 2003204343 | 2001023611 | 2000PR0058
  - 同じ表の列：appl_year, abn, acn, entity_type, no_of_appl, ipa_id, fmr_ipa_id, party_id

## g0513（1 列）
- 見出し：appl_year
- 例1 値：2002 | 2014 | 2010 | 2014 | 2006
  - 同じ表の列：appl_number, abn, acn, entity_type, no_of_appl, ipa_id, fmr_ipa_id, party_id

## g0514（1 列）
- 見出し：abn
- 例1 値：13000421358 | 77064692888 | 90086451907 | 33003085112 | 33088778009
  - 同じ表の列：appl_number, appl_year, acn, entity_type, no_of_appl, ipa_id, fmr_ipa_id, party_id

## g0515（1 列）
- 見出し：acn
- 例1 値：62367097 | 131641542 | 421358 | 87621627 | 86451907
  - 同じ表の列：appl_number, appl_year, abn, entity_type, no_of_appl, ipa_id, fmr_ipa_id, party_id

## g0516（1 列）
- 見出し：entity_type
- 例1 値：PRV | PRV | PRV | PUB | PRV
  - 同じ表の列：appl_number, appl_year, abn, acn, no_of_appl, ipa_id, fmr_ipa_id, party_id

## g0517（1 列）
- 見出し：no_of_appl
- 例1 値：18 | 12 | 18 | 24 | 21
  - 同じ表の列：appl_number, appl_year, abn, acn, entity_type, ipa_id, fmr_ipa_id, party_id

## g0518（1 列）
- 見出し：ipa_id
- 例1 値：351315 | 155207 | 368306 | 343713 | 352045
  - 同じ表の列：appl_number, appl_year, abn, acn, entity_type, no_of_appl, fmr_ipa_id, party_id

## g0519（1 列）
- 見出し：fmr_ipa_id
- 例1 値：346634 | 343321 | 247235 | 510432 | 369412
  - 同じ表の列：appl_number, appl_year, abn, acn, entity_type, no_of_appl, ipa_id, party_id

## g0520（1 列）
- 見出し：party_id
- 例1 値：1148802 | 1172999 | 960471 | 1204604 | 1151626
  - 同じ表の列：appl_number, appl_year, abn, acn, entity_type, no_of_appl, ipa_id, fmr_ipa_id

## g0521（1 列）
- 見出し：SITE
- 例1 値：BLACKBURN RD | GEORGE - CHURCH | GEORGE ST | HIGH - LYNWOOD | TUNSTALL RD
  - 同じ表の列：ASSETID, LOCATION, SIGNPLAN, SITENO, SITETYPE, mapref, lat, long

## g0522（2 列）
- 見出し：ASSETID
- 例1 値：TS002 | TS005 | TS004 | TS001 | TS006
  - 同じ表の列：SITE, LOCATION, SIGNPLAN, SITENO, SITETYPE, mapref, lat, long
- 例2 値：BR146 | BR32 | BR73 | BR108 | BR35
  - 同じ表の列：class, subtype, mapref, lat, long

## g0523（1 列）
- 見出し：LOCATION
- 例1 値：Blackburn Road/The Pines Shopping Centr… | George Street/Church Road | High Street south of Mayfair Avenue | Tunstall Road Flashing Signals | George Street west of Worthing Avenue
  - 同じ表の列：SITE, ASSETID, SIGNPLAN, SITENO, SITETYPE, mapref, lat, long

## g0524（1 列）
- 見出し：SIGNPLAN
- 例1 値：850123A | 4828A | A3092-03P1 | 3297 | 135612
  - 同じ表の列：SITE, ASSETID, LOCATION, SITENO, SITETYPE, mapref, lat, long

## g0525（1 列）
- 見出し：SITENO
- 例1 値：677 | 0 | 805 | 706 | 341
  - 同じ表の列：SITE, ASSETID, LOCATION, SIGNPLAN, SITETYPE, mapref, lat, long

## g0526（1 列）
- 見出し：SITETYPE
- 例1 値：Pedestrian Crossing | Intersections | Intersections | Flashing Pedestrian | Pedestrian Crossing
  - 同じ表の列：SITE, ASSETID, LOCATION, SIGNPLAN, SITENO, mapref, lat, long

## g0527（1 列）
- 見出し：mapref
- 例1 値：33G11 | 33C7 | 33K11 | 33C7 | 48D2
  - 同じ表の列：SITE, ASSETID, LOCATION, SIGNPLAN, SITENO, SITETYPE, lat, long

## g0528（1 列）
- 見出し：SiteID
- 例1 値：BB07 | S76-KRF | CB11 | CB12 | WDDP03
  - 同じ表の列：Date, PAI, CE

## g0529（1 列）
- 見出し：Date
- 例1 値：23/03/2017 | 22/03/2017 | 15/03/2017 | 2/03/2017 | 3/03/2017
  - 同じ表の列：SiteID, PAI, CE

## g0530（1 列）
- 見出し：PAI
- 例1 値：1.51 | 0.328 | 0.488 | 0.92 | 0.31
  - 同じ表の列：SiteID, Date, CE

## g0531（1 列）
- 見出し：CE
- 例1 値：3.16666666666667 | 3.3 | 2.96666666666667 | 2.46875 | 4.03333333333333
  - 同じ表の列：SiteID, Date, PAI

## g0532（1 列）
- 見出し：Size
- 例1 値：Total | Less than 26 enrolments | 451 to 700 enrolments | 301 to 450 enrolments | 26 to 159 enrolments
  - 同じ表の列：2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015

## g0533（1 列）
- 見出し：2008
- 例1 値：449 | 183 | 248 | 1641 | 55
  - 同じ表の列：Size, 2009, 2010, 2011, 2012, 2013, 2014, 2015

## g0534（1 列）
- 見出し：2009
- 例1 値：1633 | 57 | 251 | 396 | 300
  - 同じ表の列：Size, 2008, 2010, 2011, 2012, 2013, 2014, 2015

## g0535（1 列）
- 見出し：2010
- 例1 値：381 | 453 | 253 | 177 | 62
  - 同じ表の列：Size, 2008, 2009, 2011, 2012, 2013, 2014, 2015

## g0536（1 列）
- 見出し：2011
- 例1 値：66 | 441 | 1630 | 184 | 259
  - 同じ表の列：Size, 2008, 2009, 2010, 2012, 2013, 2014, 2015

## g0537（1 列）
- 見出し：2012
- 例1 値：1622 | 292 | 453 | 70 | 167
  - 同じ表の列：Size, 2008, 2009, 2010, 2011, 2013, 2014, 2015

## g0538（1 列）
- 見出し：2013
- 例1 値：182 | 378 | 1617 | 285 | 85
  - 同じ表の列：Size, 2008, 2009, 2010, 2011, 2012, 2014, 2015

## g0539（1 列）
- 見出し：2014
- 例1 値：95 | 260 | 298 | 361 | 412
  - 同じ表の列：Size, 2008, 2009, 2010, 2011, 2012, 2013, 2015

## g0540（1 列）
- 見出し：2015
- 例1 値：178 | 350 | 411 | 263 | 1606
  - 同じ表の列：Size, 2008, 2009, 2010, 2011, 2012, 2013, 2014

## g0541（1 列）
- 見出し：2016
- 例1 値：407 | 269 | 106 | 335 | 308
  - 同じ表の列：Size, 2008, 2009, 2010, 2011, 2012, 2013, 2014

## g0542（1 列）
- 見出し：uniqueID
- 例1 値：CID00453 | CID00479 | CID00638 | CID00329 | CID00389
  - 同じ表の列：title, suburb, state, locationInstructions, driveThroughTesting, wheelchairAccessible, walkInAllowed, bookingRequired

## g0543（1 列）
- 見出し：title
- 例1 値：Robinvale District Health Service Hospi… | Warilla Southern.IML Pathology Drive-th… | Minchinbury Histopath Pathology Drive-t… | Hornsby Clinical Labs Pathology Drive-t… | Frenchs Forest Clinical Labs Pathology …
  - 同じ表の列：uniqueID, suburb, state, locationInstructions, driveThroughTesting, wheelchairAccessible, walkInAllowed, bookingRequired

## g0544（1 列）
- 見出し：locationInstructions
- 例1 値：Enter via Liverpool City Council car pa… | Enter off Showground Road at the traffi… | Opposite Emergency Department. | Enter from Penprase Lane and follow sig… | Park as close to the Purple Flag as pos…
  - 同じ表の列：uniqueID, title, suburb, state, driveThroughTesting, wheelchairAccessible, walkInAllowed, bookingRequired

## g0545（1 列）
- 見出し：driveThroughTesting
- 例1 値：Y | Y | N | N | Y
  - 同じ表の列：uniqueID, title, suburb, state, locationInstructions, wheelchairAccessible, walkInAllowed, bookingRequired

## g0546（1 列）
- 見出し：wheelchairAccessible
- 例1 値：Y | N | Y | Y | Y
  - 同じ表の列：uniqueID, title, suburb, state, locationInstructions, driveThroughTesting, walkInAllowed, bookingRequired

## g0547（1 列）
- 見出し：walkInAllowed
- 例1 値：Y | Y | N | Y | N
  - 同じ表の列：uniqueID, title, suburb, state, locationInstructions, driveThroughTesting, wheelchairAccessible, bookingRequired

## g0548（1 列）
- 見出し：bookingRequired
- 例1 値：N | N | Y | Y | N
  - 同じ表の列：uniqueID, title, suburb, state, locationInstructions, driveThroughTesting, wheelchairAccessible, walkInAllowed

## g0549（1 列）
- 見出し：bookingLink
- 例1 値：https://www.hotdoc.com.au/medical-centr… | https://www.hotdoc.com.au/medical-centr… | https://clinicallabs.simplybook.me/v2/ | https://www.hotdoc.com.au/medical-centr… | https://www.hotdoc.com.au/medical-centr…
  - 同じ表の列：uniqueID, title, suburb, state, locationInstructions, driveThroughTesting, wheelchairAccessible, walkInAllowed

## g0550（1 列）
- 見出し：Average Age
- 例1 値：77.8 | 78.64 | 77.76 | 77.55 | 78.32
  - 同じ表の列：Year

## g0551（1 列）
- 見出し：Workplace Injury Claims
- 例1 値：No. of notifiable incidents (WHS Act 20… | *number of claimants assessed during th… | WHS Regulations | Significant Injuries (where lost time e… | Total new workplace injury claims
  - 同じ表の列：2019-2020, 2018-2019, % Change (+/-)

## g0552（2 列）
- 見出し：2019-2020
- 例1 値：0 | 2019-2020 | 2019-2020 | 0 | 0
  - 同じ表の列：Workplace Injury Cl…, 2018-2019, % Change (+/-)
- 例2 値：0 | 0 | 0 | 2019-2020 | 0
  - 同じ表の列：Workplace Injury Cl…, 2020-2021, % Change (+/-)

## g0553（1 列）
- 見出し：2018-2019
- 例1 値：0 | 0 | 0 | 2018-2019 | 0
  - 同じ表の列：Workplace Injury Cl…, 2019-2020, % Change (+/-)

## g0554（2 列）
- 見出し：% Change (+/-)
- 例1 値：0 | % Change (+/-) | 0 | 0 | 0
  - 同じ表の列：Workplace Injury Cl…, 2019-2020, 2018-2019
- 例2 値：0 | 0 | % Change (+/-) | 0 | 0
  - 同じ表の列：Workplace Injury Cl…, 2020-2021, 2019-2020

## g0555（1 列）
- 見出し：agtrends_sector
- 例1 値：Fisheries and aquaculutre | Fisheries and aquaculutre | Agriculture | Processing | Agriculture
  - 同じ表の列：agtrends_subsector, agtrends_industry, agtrends_subindustry, agtrends_commodity, year_ending, gross_value

## g0556（1 列）
- 見出し：agtrends_subsector
- 例1 値：Livestock | Crops | Crops | Crops | Crops
  - 同じ表の列：agtrends_sector, agtrends_industry, agtrends_subindustry, agtrends_commodity, year_ending, gross_value

## g0557（1 列）
- 見出し：agtrends_industry
- 例1 値：Broadacre crops | Forestry and logging | Broadacre crops | Aquaculture | Livestock disposals
  - 同じ表の列：agtrends_sector, agtrends_subsector, agtrends_subindustry, agtrends_commodity, year_ending, gross_value

## g0558（1 列）
- 見出し：agtrends_subindustry
- 例1 値：Oilseeds and pulses | Finfish | Finfish | Grains | Vegetables
  - 同じ表の列：agtrends_sector, agtrends_subsector, agtrends_industry, agtrends_commodity, year_ending, gross_value

## g0559（1 列）
- 見出し：agtrends_commodity
- 例1 値：Barley | Melons (rock and cantaloupe) | Lettuce | Apples | Forestry and logging
  - 同じ表の列：agtrends_sector, agtrends_subsector, agtrends_industry, agtrends_subindustry, year_ending, gross_value

## g0560（1 列）
- 見出し：year_ending
- 例1 値：2016-06-30T00:00:00 | 2010-06-30T00:00:00 | 2009-06-30T00:00:00 | 2022-06-30T00:00:00 | 2016-06-30T00:00:00
  - 同じ表の列：agtrends_sector, agtrends_subsector, agtrends_industry, agtrends_subindustry, agtrends_commodity, gross_value

## g0561（1 列）
- 見出し：gross_value
- 例1 値：1112972 | 17839903 | 5900000 | 243000000 | 413000000
  - 同じ表の列：agtrends_sector, agtrends_subsector, agtrends_industry, agtrends_subindustry, agtrends_commodity, year_ending

## g0562（1 列）
- 見出し：Question
- 例1 値：E3b | C1.1 | C2a | A3.1 | E4.7
  - 同じ表の列：Value, Label

## g0563（7 列）
- 見出し：Value
- 例1 値：1 | 4 | 3 | 4 | 1
  - 同じ表の列：Question, Label
- 例2 値：3 | 27 | 3 | 7 | 4
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02351V02955, Type of Educational…, UNIT

## g0564（1 列）
- 見出し：Label
- 例1 値：Being developed | Yes - partially | Being developed | No | Yes
  - 同じ表の列：Question, Value

## g0565（1 列）
- 見出し：Service Area
- 例1 値：Timeliness of water service restoration… | Drinking water qualtiy complaint respon… | Timeliness of connection | Drinking water qualtiy complaint respon… | Timeliness of sewerage service restorat…
  - 同じ表の列：Service Standard, Target, 2015/2016

## g0566（1 列）
- 見出し：Service Standard
- 例1 値：Percentage of telephone calls answered … | Percentage of outside building overflow… | Percentage of Category 1 events restore… | Percentage of Priority 2 events attende… | Percentage of external (e.g. road or fo…
  - 同じ表の列：Service Area, Target, 2015/2016

## g0567（1 列）
- 見出し：Target
- 例1 値：99% | 95% | 99% | 95% | 95%
  - 同じ表の列：Service Area, Service Standard, 2015/2016

## g0568（1 列）
- 見出し：2015/2016
- 例1 値：100% | 100% | 96% | 99% | 100%
  - 同じ表の列：Service Area, Service Standard, Target

## g0569（1 列）
- 見出し：commonwealth_electoral_division_
- 例1 値：303 | Total | 329 | 146 | 505
  - 同じ表の列：commonwealth_electo…, state_of_commonweal…, abstudy__living_all…, abstudy__non_living…, age_pension, austudy, carer_allowance, carer_allowance__ch…

## g0570（1 列）
- 見出し：commonwealth_electoral_divisio00
- 例1 値：Melbourne | Boothby | Bonner | Parramatta | Maranoa
  - 同じ表の列：commonwealth_electo…, state_of_commonweal…, abstudy__living_all…, abstudy__non_living…, age_pension, austudy, carer_allowance, carer_allowance__ch…

## g0571（1 列）
- 見出し：state_of_commonwealth_electoral_
- 例1 値：New South Wales | New South Wales | Victoria | Queensland | Queensland
  - 同じ表の列：commonwealth_electo…, commonwealth_electo…, abstudy__living_all…, abstudy__non_living…, age_pension, austudy, carer_allowance, carer_allowance__ch…

## g0572（1 列）
- 見出し：abstudy__living_allowance_
- 例1 値：<20 | <20 | 31 | <20 | 85
  - 同じ表の列：commonwealth_electo…, commonwealth_electo…, state_of_commonweal…, abstudy__non_living…, age_pension, austudy, carer_allowance, carer_allowance__ch…

## g0573（1 列）
- 見出し：abstudy__non_living_allowance_
- 例1 値：335 | 64 | 57 | 146 | 213
  - 同じ表の列：commonwealth_electo…, commonwealth_electo…, state_of_commonweal…, abstudy__living_all…, age_pension, austudy, carer_allowance, carer_allowance__ch…

## g0574（1 列）
- 見出し：age_pension
- 例1 値：18755 | 17289 | 9258 | 15092 | 12222
  - 同じ表の列：commonwealth_electo…, commonwealth_electo…, state_of_commonweal…, abstudy__living_all…, abstudy__non_living…, austudy, carer_allowance, carer_allowance__ch…

## g0575（1 列）
- 見出し：austudy
- 例1 値：666 | 239 | 264 | 249 | 141
  - 同じ表の列：commonwealth_electo…, commonwealth_electo…, state_of_commonweal…, abstudy__living_all…, abstudy__non_living…, age_pension, carer_allowance, carer_allowance__ch…

## g0576（1 列）
- 見出し：carer_allowance
- 例1 値：2431 | 2594 | 4094 | 4043 | 1217
  - 同じ表の列：commonwealth_electo…, commonwealth_electo…, state_of_commonweal…, abstudy__living_all…, abstudy__non_living…, age_pension, austudy, carer_allowance__ch…

## g0577（1 列）
- 見出し：carer_allowance__child_hcc_only_
- 例1 値：177 | 158 | 151 | 186 | 146
  - 同じ表の列：commonwealth_electo…, commonwealth_electo…, state_of_commonweal…, abstudy__living_all…, abstudy__non_living…, age_pension, austudy, carer_allowance

## g0578（1 列）
- 見出し：carer_payment
- 例1 値：1572 | 866 | 794 | 551 | 1328
  - 同じ表の列：commonwealth_electo…, commonwealth_electo…, state_of_commonweal…, abstudy__living_all…, abstudy__non_living…, age_pension, austudy, carer_allowance

## g0579（1 列）
- 見出し：Business Category
- 例1 値：Market | Market | Market | Market | Market
  - 同じ表の列：Suburb, State, LGA, Region

## g0580（1 列）
- 見出し：LGA
- 例1 値：Boroondara (C) | Northern Grampians (S) | Kingston | Greater Shepparton | Wangaratta (RC)
  - 同じ表の列：Suburb, State, Business Category, Region

## g0581（1 列）
- 見出し：Region
- 例1 値：Grampians | Eastern Metro | North and West Metropolitan Region | Barwon S/W | North and West Metropolitan Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0582（2 列）
- 見出し：year end
- 例1 値：2018 | 2016 | 2015 | 2017 | 2013
  - 同じ表の列：VOCs billion kg per…
- 例2 値：2019 | 2017 | 2016 | 2020 | 2018
  - 同じ表の列：Category, Instance

## g0583（1 列）
- 見出し：VOCs billion kg per year
- 例1 値：3.155726758 | 3.165599564 | 3.180859603 | 3.156245768 | 3.152893776
  - 同じ表の列：year end

## g0584（2 列）
- 見出し：Category
- 例1 値：Total | Total | Total | Total | Total
  - 同じ表の列：Year end, Instance
- 例2 値：Total | Total | Total | Total | Total
  - 同じ表の列：Year ended, Number of executives

## g0585（1 列）
- 見出し：Instance
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year end, Category

## g0586（1 列）
- 見出し：State Government
- 例1 値：4058 | 10278 | 7918 | 4069 | 10596
  - 同じ表の列：Year, Local Government, Universities

## g0587（1 列）
- 見出し：Local Government
- 例1 値：269 | 447 | 659 | 358 | 602
  - 同じ表の列：Year, State Government, Universities

## g0588（1 列）
- 見出し：Universities
- 例1 値：34 | 12 | 32 | 64 | 20
  - 同じ表の列：Year, State Government, Local Government

## g0589（1 列）
- 見出し：Number of transactions
- 例1 値：3,047 | 2,728 | 7,678 | 3,245 | 3,916
  - 同じ表の列：Year, Revenue ($ million)

## g0590（1 列）
- 見出し：Revenue ($ million)
- 例1 値：152.05 | 457.83 | 222.07 | 100.91 | 110.5
  - 同じ表の列：Year, Number of transacti…

## g0591（2 列）
- 見出し：itemid
- 例1 値：414223 | 412386 | 414464 | 412848 | 412523
  - 同じ表の列：title, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink, highreslink
- 例2 値：24585 | 35007 | 22906 | 22569 | 19230
  - 同じ表の列：caption, collectiontitle, dateofwork, digitalordernumber, collectionitemlink, digitalitemlink, thumbnaillink, highreslink

## g0592（1 列）
- 見出し：title
- 例1 値：Sydney - photographs of streets, public… | Sydney - photographs of streets, public… | Sydney - photographs of streets, public… | Sydney - photographs of streets, public… | Sydney - photographs of streets, public…
  - 同じ表の列：itemid, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink, highreslink

## g0593（1 列）
- 見出し：albumnumber
- 例1 値：412050 | 412050 | 412050 | 412050 | 412050
  - 同じ表の列：itemid, title, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink, highreslink

## g0594（1 列）
- 見出し：dateofwork
- 例1 値：1882 | [ca. 1881] | 1875 | undated [ca. 1870s] | undated [ca. 1870s]
  - 同じ表の列：itemid, title, albumnumber, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink, highreslink

## g0595（2 列）
- 見出し：collectionitemlink
- 例1 値：http://acms.sl.nsw.gov.au/item/itemdeta… | http://acms.sl.nsw.gov.au/item/itemdeta… | http://acms.sl.nsw.gov.au/item/itemdeta… | http://acms.sl.nsw.gov.au/item/itemdeta… | http://acms.sl.nsw.gov.au/item/itemdeta…
  - 同じ表の列：itemid, title, albumnumber, dateofwork, digitalitemlink, digitalordernumber, thumbnaillink, highreslink
- 例2 値：http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta…
  - 同じ表の列：itemid, caption, collectiontitle, dateofwork, digitalordernumber, digitalitemlink, thumbnaillink, highreslink

## g0596（2 列）
- 見出し：digitalitemlink
- 例1 値：http://acms.sl.nsw.gov.au/item/itemdeta… | http://acms.sl.nsw.gov.au/item/itemdeta… | http://acms.sl.nsw.gov.au/item/itemdeta… | http://acms.sl.nsw.gov.au/item/itemdeta… | http://acms.sl.nsw.gov.au/item/itemdeta…
  - 同じ表の列：itemid, title, albumnumber, dateofwork, collectionitemlink, digitalordernumber, thumbnaillink, highreslink
- 例2 値：http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta…
  - 同じ表の列：itemid, caption, collectiontitle, dateofwork, digitalordernumber, collectionitemlink, thumbnaillink, highreslink

## g0597（1 列）
- 見出し：digitalordernumber
- 例1 値：a089929 | a325020 | a089803 | a089992 | a089435
  - 同じ表の列：itemid, title, albumnumber, dateofwork, collectionitemlink, digitalitemlink, thumbnaillink, highreslink

## g0598（2 列）
- 見出し：thumbnaillink
- 例1 値：http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1…
  - 同じ表の列：itemid, title, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, highreslink
- 例2 値：http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1…
  - 同じ表の列：itemid, caption, collectiontitle, dateofwork, digitalordernumber, collectionitemlink, digitalitemlink, highreslink

## g0599（2 列）
- 見出し：highreslink
- 例1 値：http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1…
  - 同じ表の列：itemid, title, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink
- 例2 値：http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1… | http://acms.sl.nsw.gov.au/_DAMx/image/1…
  - 同じ表の列：itemid, caption, collectiontitle, dateofwork, digitalordernumber, collectionitemlink, digitalitemlink, thumbnaillink

## g0600（1 列）
- 見出し：zoomablelink
- 例1 値：NULL | NULL | NULL | NULL | NULL
  - 同じ表の列：itemid, title, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber, thumbnaillink

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
