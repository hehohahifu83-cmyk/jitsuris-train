# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Data as of
- 例1 値：02-Mar-21 | 02-Mar-21 | 02-Mar-21 | 02-Mar-21 | 02-Mar-21
  - 同じ表の列：Licence No, Start Date, Trading Status, Type, Filter Category, Suburb, SA2 Band, Subject to Cap

## g0002（1 列）
- 見出し：Licence No
- 例1 値：LIQC300229548 | LIQC300239004 | LIQC300236668 | LIQC300241181 | LIQC300226557
  - 同じ表の列：Data as of, Start Date, Trading Status, Type, Filter Category, Suburb, SA2 Band, Subject to Cap

## g0003（1 列）
- 見出し：Start Date
- 例1 値：6/04/1955 | 10/10/1947 | 26/11/1956 | 11/01/1966 | 14/06/1962
  - 同じ表の列：Data as of, Licence No, Trading Status, Type, Filter Category, Suburb, SA2 Band, Subject to Cap

## g0004（1 列）
- 見出し：Trading Status
- 例1 値：Trading | Trading | Trading | Trading | Trading
  - 同じ表の列：Data as of, Licence No, Start Date, Type, Filter Category, Suburb, SA2 Band, Subject to Cap

## g0005（2 列）
- 見出し：Type
- 例1 値：Club | Club | Club | Club | Club
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Filter Category, Suburb, SA2 Band, Subject to Cap
- 例2 値：Link | Status | Status | Link | Link
  - 同じ表の列：Post Message, Posted, Lifetime Post Total…, Lifetime Post organ…, Lifetime Post Paid …, Lifetime Post Total…, Lifetime Post Organ…, Lifetime Post Paid …

## g0006（1 列）
- 見出し：Filter Category
- 例1 値：Club - small | Club - small | Club - small | Club- medium | Club - non-gaming
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Suburb, SA2 Band, Subject to Cap

## g0007（1 列）
- 見出し：Suburb
- 例1 値：BOMADERRY | BANKSMEADOW | CUMNOCK | MOOREBANK | ROSEWOOD
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap

## g0008（1 列）
- 見出し：SA2 Band
- 例1 値：1 | 1 | 3 | 2 | 3
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, Suburb, Subject to Cap

## g0009（1 列）
- 見出し：Subject to Cap
- 例1 値：No | No | No | No | No
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, Suburb, SA2 Band

## g0010（1 列）
- 見出し：LGA
- 例1 値：Bathurst Regional Council | Lake Macquarie City Council | Shoalhaven City Council | Canterbury-Bankstown Council | Blayney Shire Council
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, Suburb, SA2 Band

## g0011（1 列）
- 見出し：Portfolio
- 例1 値：Prime Minister and Cabinet Porfolio | Attorney-General's Portfolio | Treasury Portfolio | Communications Portfolio | Treasury Portfolio
  - 同じ表の列：Department/Agency, Outcome, Program, Expense type, Appropriation type, 2014-15, 2015-16, 2016-17

## g0012（1 列）
- 見出し：Department/Agency
- 例1 値：Department of the Treasury | Australian National Audit Office | Department of Industry and Science | Department of Defence | Professional Services Review
  - 同じ表の列：Portfolio, Outcome, Program, Expense type, Appropriation type, 2014-15, 2015-16, 2016-17

## g0013（1 列）
- 見出し：Outcome
- 例1 値：Outcome 1:Increased knowledge, apprecia… | Outcome 1: Increased innovation, invest… | Outcome 1: More sustainable, productive… | Protection of people and the environmen… | Outcome 5: Primary Health Care
  - 同じ表の列：Portfolio, Department/Agency, Program, Expense type, Appropriation type, 2014-15, 2015-16, 2016-17

## g0014（1 列）
- 見出し：Program
- 例1 値：Programme 1.4: Australian Valuation Off… | Programmes transferred to the Departmen… | Programme 1.1: Veterans' Income Support… | Programme 1.2: Consumer safeguards, edu… | Programme 1.10: Agricultural Resources
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Expense type, Appropriation type, 2014-15, 2015-16, 2016-17

## g0015（1 列）
- 見出し：Expense type
- 例1 値：Departmental expenses | Departmental expenses | Administered expenses | Administered expenses | Administered expenses
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Appropriation type, 2014-15, 2015-16, 2016-17

## g0016（1 列）
- 見出し：Appropriation type
- 例1 値：Ordinary annual services (Appropriation… | Expenses not requiring appropriation in… | Expenses not requiring appropriation in… | Departmental appropriation | Ordinary annual services (Appropriation…
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, 2014-15, 2015-16, 2016-17

## g0017（1 列）
- 見出し：2014-15
- 例1 値：33524 | 9004 | 14331 | 16503 | 719802
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2015-16, 2016-17

## g0018（1 列）
- 見出し：2015-16
- 例1 値：26300 | 11190 | 378 | 16880 | 10000
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2014-15, 2016-17

## g0019（2 列）
- 見出し：2016-17
- 例1 値：30745 | 15789 | 73731 | 1165 | 0
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2014-15, 2015-16
- 例2 値：1859 | 13185100 | 12 | 352 | 5258
  - 同じ表の列：Activity, 2018-19, 2017-18

## g0020（2 列）
- 見出し：2017-18
- 例1 値：0 | 0 | 8148 | 0 | 6087
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2014-15, 2015-16
- 例2 値：84461 | 57 | 111 | 1600 | 292
  - 同じ表の列：Activity, 2018-19, 2016-17

## g0021（1 列）
- 見出し：Year
- 例1 値：1994-95 | 2004-05 | 2000-01 | 2005-06 | 1997-98
  - 同じ表の列：Annual Notifications

## g0022（1 列）
- 見出し：Annual Notifications
- 例1 値：3877 | NA | 6979 | 7852 | 9174
  - 同じ表の列：Year

## g0023（1 列）
- 見出し：Section A
- 例1 値：352 | 66 | 96 | 283 | 142
  - 同じ表の列：Section B, Section C, Section D, Section E, Section G, Notes

## g0024（1 列）
- 見出し：Section B
- 例1 値：Yes | Yes | No | no | No
  - 同じ表の列：Section A, Section C, Section D, Section E, Section G, Notes

## g0025（1 列）
- 見出し：Section C
- 例1 値：House | House | House | House | House
  - 同じ表の列：Section A, Section B, Section D, Section E, Section G, Notes

## g0026（1 列）
- 見出し：Section D
- 例1 値：None | Destroyed | Minor | Minor | Minor
  - 同じ表の列：Section A, Section B, Section C, Section E, Section G, Notes

## g0027（1 列）
- 見出し：Section E
- 例1 値：Electricity, unstable structure(s) (res… | Gas Falling Debris Unstable structures | Unstable structure(s), falling debris | Unstable Structure(s) | Identified Hazards
  - 同じ表の列：Section A, Section B, Section C, Section D, Section G, Notes

## g0028（1 列）
- 見出し：Section G
- 例1 値：Unreinforced masonry | Steel Frame, Steel Clad and Roof | Unreinforced masonry | timber frame cladding | Unreinforced masonry
  - 同じ表の列：Section A, Section B, Section C, Section D, Section E, Notes

## g0029（1 列）
- 見出し：Notes
- 例1 値：G1 | A8 | D3 | G11 | G10
  - 同じ表の列：Section A, Section B, Section C, Section D, Section E, Section G

## g0030（1 列）
- 見出し：Publisher Title
- 例1 値：Department of the Premier and Cabinet | Attorney-General's Department | Mount Barker District Council | SA Tourism Commission | State Records
  - 同じ表の列：Views, Visits

## g0031（2 列）
- 見出し：Views
- 例1 値：13 | 1594 | 253 | 2 | 1513
  - 同じ表の列：Publisher Title, Visits
- 例2 値：31 | 2 | 11 | 2 | 28
  - 同じ表の列：date, country_id, watch_time_minutes, average_view_durati…, comments, likes, dislikes, unique_cookies_web_…

## g0032（1 列）
- 見出し：Visits
- 例1 値：1 | 6 | 747 | 4 | 24
  - 同じ表の列：Publisher Title, Views

## g0033（1 列）
- 見出し：Post Message
- 例1 値：Have a look at this amazing tool that P… | Interested in places to safely exercise… | Unleashed Connections | DEWNR have updated an incredible 41 soi… | Mount Gambier Unleashed Information Ses…
  - 同じ表の列：Type, Posted, Lifetime Post Total…, Lifetime Post organ…, Lifetime Post Paid …, Lifetime Post Total…, Lifetime Post Organ…, Lifetime Post Paid …

## g0034（1 列）
- 見出し：Posted
- 例1 値：6/23/16 6:56 PM | 6/23/16 6:41 PM | 6/28/16 6:10 PM | 6/16/16 12:14 AM | 6/9/16 11:30 PM
  - 同じ表の列：Post Message, Type, Lifetime Post Total…, Lifetime Post organ…, Lifetime Post Paid …, Lifetime Post Total…, Lifetime Post Organ…, Lifetime Post Paid …

## g0035（1 列）
- 見出し：Lifetime Post Total Reach
- 例1 値：43 | 167 | 41 | 0 | 0
  - 同じ表の列：Post Message, Type, Posted, Lifetime Post organ…, Lifetime Post Paid …, Lifetime Post Total…, Lifetime Post Organ…, Lifetime Post Paid …

## g0036（1 列）
- 見出し：Lifetime Post organic reach
- 例1 値：291 | 6 | 0 | 0 | 21
  - 同じ表の列：Post Message, Type, Posted, Lifetime Post Total…, Lifetime Post Paid …, Lifetime Post Total…, Lifetime Post Organ…, Lifetime Post Paid …

## g0037（1 列）
- 見出し：Lifetime Post Paid Reach
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Post Message, Type, Posted, Lifetime Post Total…, Lifetime Post organ…, Lifetime Post Total…, Lifetime Post Organ…, Lifetime Post Paid …

## g0038（1 列）
- 見出し：Lifetime Post Total Impressions
- 例1 値：230 | 107 | 27 | 362 | 210
  - 同じ表の列：Post Message, Type, Posted, Lifetime Post Total…, Lifetime Post organ…, Lifetime Post Paid …, Lifetime Post Organ…, Lifetime Post Paid …

## g0039（1 列）
- 見出し：Lifetime Post Organic Impressions
- 例1 値：107 | 266 | 18 | 230 | 15
  - 同じ表の列：Post Message, Type, Posted, Lifetime Post Total…, Lifetime Post organ…, Lifetime Post Paid …, Lifetime Post Total…, Lifetime Post Paid …

## g0040（1 列）
- 見出し：Lifetime Post Paid Impressions
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Post Message, Type, Posted, Lifetime Post Total…, Lifetime Post organ…, Lifetime Post Paid …, Lifetime Post Total…, Lifetime Post Organ…

## g0041（1 列）
- 見出し：Lifetime Engaged Users
- 例1 値：12 | 4 | 6 | 2 | Lifetime: The number of people who clic…
  - 同じ表の列：Post Message, Type, Posted, Lifetime Post Total…, Lifetime Post organ…, Lifetime Post Paid …, Lifetime Post Total…, Lifetime Post Organ…

## g0042（1 列）
- 見出し：date
- 例1 値：6/7/2016 | 6/9/2016 | 6/10/2016 | 6/2/2016 | 6/9/2016
  - 同じ表の列：country_id, watch_time_minutes, views, average_view_durati…, comments, likes, dislikes, unique_cookies_web_…

## g0043（1 列）
- 見出し：country_id
- 例1 値：AU | AU | ES | AU | UA
  - 同じ表の列：date, watch_time_minutes, views, average_view_durati…, comments, likes, dislikes, unique_cookies_web_…

## g0044（1 列）
- 見出し：watch_time_minutes
- 例1 値：4 | 15 | 1 | 16 | 7
  - 同じ表の列：date, country_id, views, average_view_durati…, comments, likes, dislikes, unique_cookies_web_…

## g0045（1 列）
- 見出し：average_view_duration
- 例1 値：2.6 | 1.6 | 1.3 | 2.2 | 0.1
  - 同じ表の列：date, country_id, watch_time_minutes, views, comments, likes, dislikes, unique_cookies_web_…

## g0046（1 列）
- 見出し：comments
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：date, country_id, watch_time_minutes, views, average_view_durati…, likes, dislikes, unique_cookies_web_…

## g0047（1 列）
- 見出し：likes
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：date, country_id, watch_time_minutes, views, average_view_durati…, comments, dislikes, unique_cookies_web_…

## g0048（1 列）
- 見出し：dislikes
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：date, country_id, watch_time_minutes, views, average_view_durati…, comments, likes, unique_cookies_web_…

## g0049（1 列）
- 見出し：unique_cookies_web_only
- 例1 値：1 | 7 | 7 | 5 | 2
  - 同じ表の列：date, country_id, watch_time_minutes, views, average_view_durati…, comments, likes, dislikes

## g0050（1 列）
- 見出し：subscribers_gained
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：date, country_id, watch_time_minutes, views, average_view_durati…, comments, likes, dislikes

## g0051（1 列）
- 見出し：School code
- 例1 値：2055 | 1372 | 4386 | 1414 | 2485
  - 同じ表の列：COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…

## g0052（1 列）
- 見出し：COMPOSITE_CLASS_COUNT_14
- 例1 値：2 | 4 | 0 | 7 | 2
  - 同じ表の列：School code, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…

## g0053（1 列）
- 見出し：COMPOSITE_CLASS_STUDENTS_14
- 例1 値：174 | 69 | 42 | 273 | 120
  - 同じ表の列：School code, COMPOSITE_CLASS_COU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…

## g0054（1 列）
- 見出し：PCT_COMPOSITE_CLASSES_14
- 例1 値：28.6 | 100 | 19 | 0 | 70
  - 同じ表の列：School code, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…

## g0055（1 列）
- 見出し：PCT_COMPOSITE_CLASS_STUDENTS_14
- 例1 値：39.7 | 4.9 | 100 | 65.5 | 67.3
  - 同じ表の列：School code, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…

## g0056（1 列）
- 見出し：COMPOSITE_CLASS_COUNT_15
- 例1 値：6 | 2 | 2 | 3 | 2
  - 同じ表の列：School code, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…

## g0057（1 列）
- 見出し：COMPOSITE_CLASS_STUDENTS_15
- 例1 値：27 | 0 | 24 | 47 | 157
  - 同じ表の列：School code, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…, COMPOSITE_CLASS_COU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…

## g0058（1 列）
- 見出し：PCT_COMPOSITE_CLASSES_15
- 例1 値：69.2 | 12.1 | 33.3 | 84.6 | 81.8
  - 同じ表の列：School code, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…

## g0059（1 列）
- 見出し：PCT_COMPOSITE_CLASS_STUDENTS_15
- 例1 値：NULL | 100 | 80.8 | 66.5 | 43.6
  - 同じ表の列：School code, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…

## g0060（1 列）
- 見出し：COMPOSITE_CLASS_COUNT_16
- 例1 値：5 | 1 | 8 | 5 | 4
  - 同じ表の列：School code, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…, PCT_COMPOSITE_CLASS…, COMPOSITE_CLASS_COU…, COMPOSITE_CLASS_STU…, PCT_COMPOSITE_CLASS…

## g0061（1 列）
- 見出し：classification_desc
- 例1 値：District School | Public School | Public School | Provisional School | Provisional School
  - 同じ表の列：start_month, start_year, end_month, end_year, transferred_to, half_time_partner_s…

## g0062（1 列）
- 見出し：start_month
- 例1 値：Mar | Feb | Jan | Jan | Oct
  - 同じ表の列：classification_desc, start_year, end_month, end_year, transferred_to, half_time_partner_s…

## g0063（1 列）
- 見出し：start_year
- 例1 値：1957 | 1953 | 1928 | 1938 | 1964
  - 同じ表の列：classification_desc, start_month, end_month, end_year, transferred_to, half_time_partner_s…

## g0064（1 列）
- 見出し：end_month
- 例1 値：Dec | May | Dec | open | Dec
  - 同じ表の列：classification_desc, start_month, start_year, end_year, transferred_to, half_time_partner_s…

## g0065（1 列）
- 見出し：end_year
- 例1 値：1891 | 1944 | 1888 | 1863 | 1883
  - 同じ表の列：classification_desc, start_month, start_year, end_month, transferred_to, half_time_partner_s…

## g0066（1 列）
- 見出し：transferred_to
- 例1 値：to ACT | to ACT | to Victoria | to ACT | ACT
  - 同じ表の列：classification_desc, start_month, start_year, end_month, end_year, half_time_partner_s…

## g0067（1 列）
- 見出し：half_time_partner_school_id
- 例1 値：8528 | 7540 | 4534 | 4139 | 7478
  - 同じ表の列：classification_desc, start_month, start_year, end_month, end_year, transferred_to

## g0068（1 列）
- 見出し：Central Region
- 例1 値：Births | Ethnicity of mother | Marital status | Method of birth | Singleton pregnancy
  - 同じ表の列：2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014

## g0069（1 列）
- 見出し：2007
- 例1 値：525 | 4652 | 614 | 2099 | 3769
  - 同じ表の列：Central Region, 2008, 2009, 2010, 2011, 2012, 2013, 2014

## g0070（1 列）
- 見出し：2008
- 例1 値：230 | 126 | 634 | 0 | 585
  - 同じ表の列：Central Region, 2007, 2009, 2010, 2011, 2012, 2013, 2014

## g0071（1 列）
- 見出し：2009
- 例1 値：315 | 259 | 0 | 21 | 107
  - 同じ表の列：Central Region, 2007, 2008, 2010, 2011, 2012, 2013, 2014

## g0072（1 列）
- 見出し：2010
- 例1 値：4780 | 90 | 3432 | 683 | 256
  - 同じ表の列：Central Region, 2007, 2008, 2009, 2011, 2012, 2013, 2014

## g0073（1 列）
- 見出し：2011
- 例1 値：594 | 406 | 31 | 1317 | 4183
  - 同じ表の列：Central Region, 2007, 2008, 2009, 2010, 2012, 2013, 2014

## g0074（1 列）
- 見出し：2012
- 例1 値：17 | 121 | 1034 | 3601 | 4273
  - 同じ表の列：Central Region, 2007, 2008, 2009, 2010, 2011, 2013, 2014

## g0075（1 列）
- 見出し：2013
- 例1 値：102 | 411 | 4356 | 759 | 24
  - 同じ表の列：Central Region, 2007, 2008, 2009, 2010, 2011, 2012, 2014

## g0076（1 列）
- 見出し：2014
- 例1 値：31 | 817 | 786 | 18 | 2953
  - 同じ表の列：Central Region, 2007, 2008, 2009, 2010, 2011, 2012, 2013

## g0077（1 列）
- 見出し：2015
- 例1 値：3124 | 4 | 4807 | 291 | 854
  - 同じ表の列：Central Region, 2007, 2008, 2009, 2010, 2011, 2012, 2013

## g0078（1 列）
- 見出し：Inspections
- 例1 値：Number of Businesses | Inspections Conducted | Inspections from Complaints | Follow-up Inspections
  - 同じ表の列：Food Safety Risk Cl…, Total

## g0079（1 列）
- 見出し：Food Safety Risk Classification
- 例1 値：1996 | 6732 | P1 | 4959 | 514
  - 同じ表の列：Inspections, Total

## g0080（1 列）
- 見出し：Total
- 例1 値：2754 | 8620 | 706 | 16140
  - 同じ表の列：Inspections, Food Safety Risk Cl…

## g0081（1 列）
- 見出し：Activity
- 例1 値：New items created | New government agencies created | Total holdings (items) | Agency Enquiries - FOI | New series registered
  - 同じ表の列：2018-19, 2017-18, 2016-17

## g0082（1 列）
- 見出し：2018-19
- 例1 値：707 | 116 | 445 | 187631 | 77
  - 同じ表の列：Activity, 2017-18, 2016-17

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
```
