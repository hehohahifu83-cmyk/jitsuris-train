# ラベル用シート 002 / 006

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Payroll staff
- 例1 値：1 | 256 | 16 | 59 | 435
  - 同じ表の列：Organisation type, Main, parent or spo…, Number of non-payro…, Grand Total (workfo…, Payroll staff costs…, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0122（1 列）
- 見出し：Number of non-payroll staff (contingent labour and consultan
- 例1 値：16 | 1 | 9 | 3 | 17
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs…, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0123（2 列）
- 見出し：Grand Total (workforce numbers)
- 例1 値：82 | 68 | 1,414 | 40 | 186
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs…, Non-Payroll staff (…, Grand Total paybill…, Comments and notes
- 例2 値：108 | 193 | 26 | 1,299 | 2,546
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0124（1 列）
- 見出し：Payroll staff costs (」)
- 例1 値：452,885.37 | 4,524,815.00 | 3,390,292.86 | 4,311,545.65 | 647,781.00
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0125（1 列）
- 見出し：Non-Payroll staff (contingent labour/consultancy - CCL) cost
- 例1 値：Total cost of contingent labour: agency… | 309,363.97 | 110,243.00 | 10,584.00 | 38,324.07
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs…, Grand Total paybill…, Comments and notes

## g0126（1 列）
- 見出し：Grand Total paybill/staffing (payroll and non-payroll) costs
- 例1 値：331,579.00 | 266,659.36 | 3,524,200.00 | 1,335,973.70 | 5,444,703.91
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs…, Non-Payroll staff (…, Comments and notes

## g0127（1 列）
- 見出し：Comments and notes
- 例1 値：The Director of Fair Access is on the p… | No returns for consultancy fees for Oct… | Allowances are included within Salary C…
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs…, Non-Payroll staff (…, Grand Total paybill…

## g0128（1 列）
- 見出し：reporting_month
- 例1 値：2025-12-01 | 2026-07-01 | 2025-06-01 | 2026-04-01 | 2025-12-01
  - 同じ表の列：service, portfolio, users, sessions, cumulative_users

## g0129（1 列）
- 見出し：service
- 例1 値：Investment Support Directory | Trade Remedies Service (TRS) | AI Chatbot | Expand Your Business (EYB) | DBT Assist
  - 同じ表の列：reporting_month, portfolio, users, sessions, cumulative_users

## g0130（1 列）
- 見出し：portfolio
- 例1 値：Trade & Regulatory Services | Business Growth | Business Growth | Trade & Regulatory Services | Business Growth
  - 同じ表の列：reporting_month, service, users, sessions, cumulative_users

## g0131（1 列）
- 見出し：users
- 例1 値：1589 | 613 | 384 | 336 | 1555
  - 同じ表の列：reporting_month, service, portfolio, sessions, cumulative_users

## g0132（1 列）
- 見出し：sessions
- 例1 値：2260 | 1279 | 1582 | 1234 | 960
  - 同じ表の列：reporting_month, service, portfolio, users, cumulative_users

## g0133（1 列）
- 見出し：cumulative_users
- 例1 値：127 | 11896 | 13046 | 27890 | 2868
  - 同じ表の列：reporting_month, service, portfolio, users, sessions

## g0134（1 列）
- 見出し：new_lead_dept
- 例1 値：DWP (HSE) | DEFRA | DESNZ | DESNZ | DEFRA
  - 同じ表の列：type_of_reul, primary_secondary, sector, policy_area, territorial_applica…, international_oblig…, reul_status, amendedrepealreplac…

## g0135（1 列）
- 見出し：type_of_reul
- 例1 値：EU direct legislation incorporated by s… | EU direct legislation incorporated by s… | EU-derived domestic legislation preserv… | EU direct legislation incorporated by s… | EU direct legislation incorporated by s…
  - 同じ表の列：new_lead_dept, primary_secondary, sector, policy_area, territorial_applica…, international_oblig…, reul_status, amendedrepealreplac…

## g0136（1 列）
- 見出し：primary_secondary
- 例1 値：#NA | #NA | #NA | #NA | Secondary
  - 同じ表の列：new_lead_dept, type_of_reul, sector, policy_area, territorial_applica…, international_oblig…, reul_status, amendedrepealreplac…

## g0137（1 列）
- 見出し：sector
- 例1 値：Section C | Section C | Multiple Sectors | Section K | Section O
  - 同じ表の列：new_lead_dept, type_of_reul, primary_secondary, policy_area, territorial_applica…, international_oblig…, reul_status, amendedrepealreplac…

## g0138（1 列）
- 見出し：policy_area
- 例1 値：Fisheries, Aquaculture and Marine | Construction products regulation | Fisheries, Aquaculture and Marine | Environment (Waste) | Construction products regulation
  - 同じ表の列：new_lead_dept, type_of_reul, primary_secondary, sector, territorial_applica…, international_oblig…, reul_status, amendedrepealreplac…

## g0139（1 列）
- 見出し：territorial_application_of_reul
- 例1 値：#NA | GB only (England & Wales & Scotland) | UK wide | GB only (England & Wales & Scotland) | UK wide
  - 同じ表の列：new_lead_dept, type_of_reul, primary_secondary, sector, policy_area, international_oblig…, reul_status, amendedrepealreplac…

## g0140（1 列）
- 見出し：international_obligations
- 例1 値：Yes | No | No | No | No
  - 同じ表の列：new_lead_dept, type_of_reul, primary_secondary, sector, policy_area, territorial_applica…, reul_status, amendedrepealreplac…

## g0141（1 列）
- 見出し：reul_status
- 例1 値：Amended | Unchanged | Unchanged | Expired | Unchanged
  - 同じ表の列：new_lead_dept, type_of_reul, primary_secondary, sector, policy_area, territorial_applica…, international_oblig…, amendedrepealreplac…

## g0142（1 列）
- 見出し：amendedrepealreplaced
- 例1 値：#NA | 01/01/2024 | 31/12/2023 | 31/12/2023 | 29/08/2023
  - 同じ表の列：new_lead_dept, type_of_reul, primary_secondary, sector, policy_area, territorial_applica…, international_oblig…, reul_status

## g0143（1 列）
- 見出し：changes_to_reul_details
- 例1 値：#NA | Revoked via the Retained EU Law (Revoca… | Revoked by The Waste (Miscellaneous Ame… | #NA | #NA
  - 同じ表の列：new_lead_dept, type_of_reul, primary_secondary, sector, policy_area, territorial_applica…, international_oblig…, reul_status

## g0144（1 列）
- 見出し：Post Unique Reference
- 例1 値：GO017 | GO066 | GO057 | 0 | GO022
  - 同じ表の列：Grade, Job Title, Job/Team Function, Parent Department, Organisation, Unit, Reports to Senior P…, Salary Cost of Repo…

## g0145（1 列）
- 見出し：Grade
- 例1 値：SCS2 | SCS1 | SCS1 | SCS1 | SCS1
  - 同じ表の列：Post Unique Referen…, Job Title, Job/Team Function, Parent Department, Organisation, Unit, Reports to Senior P…, Salary Cost of Repo…

## g0146（1 列）
- 見出し：Job Title
- 例1 値：Not in post | Deputy Director, Transport & Environmen… | Deputy Director, Safer and Stronger Com… | Not in post | Deputy Director, Europe
  - 同じ表の列：Post Unique Referen…, Grade, Job/Team Function, Parent Department, Organisation, Unit, Reports to Senior P…, Salary Cost of Repo…

## g0147（1 列）
- 見出し：Job/Team Function
- 例1 値：Post eliminated | N/A | N/A | Post eliminated | Post eliminated
  - 同じ表の列：Post Unique Referen…, Grade, Job Title, Parent Department, Organisation, Unit, Reports to Senior P…, Salary Cost of Repo…

## g0148（1 列）
- 見出し：Parent Department
- 例1 値：Department for Communities and Local Go… | Department for Communities and Local Go… | Department for Communities and Local Go… | Department for Communities and Local Go… | Department for Communities and Local Go…
  - 同じ表の列：Post Unique Referen…, Grade, Job Title, Job/Team Function, Organisation, Unit, Reports to Senior P…, Salary Cost of Repo…

## g0149（4 列）
- 見出し：Organisation
- 例1 値：Government Office Network | Government Office Network | Government Office Network | Government Office Network | Government Office Network
  - 同じ表の列：Post Unique Referen…, Grade, Job Title, Job/Team Function, Parent Department, Unit, Reports to Senior P…, Salary Cost of Repo…
- 例2 値：Department for Education | Department for Education | Department for Education | Department for Education | Department for Education
  - 同じ表の列：Parent Department, Unit, Reporting Senior Po…, Grade, Payscale Minimum (」), Payscale Maximum (」), Generic Job Title, Number of Posts in …

## g0150（1 列）
- 見出し：Unit
- 例1 値：N/A | GO London | N/A | GO North West | GO Yorkshire and Humber
  - 同じ表の列：Post Unique Referen…, Grade, Job Title, Job/Team Function, Parent Department, Organisation, Reports to Senior P…, Salary Cost of Repo…

## g0151（1 列）
- 見出し：Reports to Senior Post
- 例1 値：XX | XX | XX | XX | XX
  - 同じ表の列：Post Unique Referen…, Grade, Job Title, Job/Team Function, Parent Department, Organisation, Unit, Salary Cost of Repo…

## g0152（1 列）
- 見出し：Salary Cost of Reports (」)
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Post Unique Referen…, Grade, Job Title, Job/Team Function, Parent Department, Organisation, Unit, Reports to Senior P…

## g0153（1 列）
- 見出し：FTE
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Post Unique Referen…, Grade, Job Title, Job/Team Function, Parent Department, Organisation, Unit, Reports to Senior P…

## g0154（1 列）
- 見出し：LSOA CODE
- 例1 値：E01000087 | E01000667 | E01000084 | E01000221 | E01000816
  - 同じ表の列：PRE 2009 LA CODE, POST 2009 LA CODE, GOR CODE, IMD SCORE, RANK OF IMD SCORE (…, INCOME SCORE, RANK OF INCOME SCOR…, EMPLOYMENT SCORE

## g0155（1 列）
- 見出し：PRE 2009 LA CODE
- 例1 値：00AC | 00AG | 00AF | 00AE | 00AC
  - 同じ表の列：LSOA CODE, POST 2009 LA CODE, GOR CODE, IMD SCORE, RANK OF IMD SCORE (…, INCOME SCORE, RANK OF INCOME SCOR…, EMPLOYMENT SCORE

## g0156（1 列）
- 見出し：POST 2009 LA CODE
- 例1 値：00AF | 00AC | 00AC | 00AF | 00AD
  - 同じ表の列：LSOA CODE, PRE 2009 LA CODE, GOR CODE, IMD SCORE, RANK OF IMD SCORE (…, INCOME SCORE, RANK OF INCOME SCOR…, EMPLOYMENT SCORE

## g0157（1 列）
- 見出し：GOR CODE
- 例1 値：H | H | H | H | H
  - 同じ表の列：LSOA CODE, PRE 2009 LA CODE, POST 2009 LA CODE, IMD SCORE, RANK OF IMD SCORE (…, INCOME SCORE, RANK OF INCOME SCOR…, EMPLOYMENT SCORE

## g0158（1 列）
- 見出し：IMD SCORE
- 例1 値：27.63 | 29.3 | 14.68 | 15.9 | 11.96
  - 同じ表の列：LSOA CODE, PRE 2009 LA CODE, POST 2009 LA CODE, GOR CODE, RANK OF IMD SCORE (…, INCOME SCORE, RANK OF INCOME SCOR…, EMPLOYMENT SCORE

## g0159（1 列）
- 見出し：RANK OF IMD SCORE (where 1 is most deprived)
- 例1 値：8284 | 26899 | 6376 | 9570 | 14500
  - 同じ表の列：LSOA CODE, PRE 2009 LA CODE, POST 2009 LA CODE, GOR CODE, IMD SCORE, INCOME SCORE, RANK OF INCOME SCOR…, EMPLOYMENT SCORE

## g0160（1 列）
- 見出し：INCOME SCORE
- 例1 値：0.19 | 0.08 | 0.04 | 0.06 | 0.35
  - 同じ表の列：LSOA CODE, PRE 2009 LA CODE, POST 2009 LA CODE, GOR CODE, IMD SCORE, RANK OF IMD SCORE (…, RANK OF INCOME SCOR…, EMPLOYMENT SCORE

## g0161（1 列）
- 見出し：RANK OF INCOME SCORE (where 1 is most deprived)
- 例1 値：24485 | 15662 | 13509 | 19850 | 15514
  - 同じ表の列：LSOA CODE, PRE 2009 LA CODE, POST 2009 LA CODE, GOR CODE, IMD SCORE, RANK OF IMD SCORE (…, INCOME SCORE, EMPLOYMENT SCORE

## g0162（1 列）
- 見出し：EMPLOYMENT SCORE
- 例1 値：0.08 | 0.1 | 0.09 | 0.04 | 0.15
  - 同じ表の列：LSOA CODE, PRE 2009 LA CODE, POST 2009 LA CODE, GOR CODE, IMD SCORE, RANK OF IMD SCORE (…, INCOME SCORE, RANK OF INCOME SCOR…

## g0163（1 列）
- 見出し：RANK OF EMPLOYMENT SCORE (where 1 is most deprived)
- 例1 値：28567 | 26837 | 24560 | 14265 | 10371
  - 同じ表の列：LSOA CODE, PRE 2009 LA CODE, POST 2009 LA CODE, GOR CODE, IMD SCORE, RANK OF IMD SCORE (…, INCOME SCORE, RANK OF INCOME SCOR…

## g0164（4 列）
- 見出し：Organisation Type
- 例1 値：Executive Non-Departmental Public Body | Executive Agency | Executive Non-Departmental Public Body | Executive Non-Departmental Public Body | Executive Non-Departmental Public Body
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…
- 例2 値：Executive Non-Departmental Public Body | Executive Non-Departmental Public Body | Ministerial Department | Executive Agency | Executive Agency
  - 同じ表の列：Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0165（1 列）
- 見出し：Main, parent or sponsoring department
- 例1 値：Department for Communities & Local Gove… | Department for Communities & Local Gove… | Department for Communities & Local Gove… | Department for Communities & Local Gove… | Department for Communities & Local Gove…
  - 同じ表の列：Organisation Type, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0166（4 列）
- 見出し：Payroll staff AO/AA Headcount
- 例1 値：16 | 9 | 60 | 3 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…
- 例2 値：4635 | 37 | 2 | 0 | 385
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0167（4 列）
- 見出し：Payroll staff EO Headcount
- 例1 値：128 | 0 | 7 | 26 | 36
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…
- 例2 値：3 | 846 | 22 | 935 | 1
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0168（4 列）
- 見出し：Payroll staff SEO/HEO Headcount
- 例1 値：15 | 75 | 42 | 0 | 795
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…
- 例2 値：4 | 68 | 0 | 9 | 660
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0169（4 列）
- 見出し：Payroll staff Grade 6/7 Headcount
- 例1 値：16 | 0 | 0 | 0 | 5
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…
- 例2 値：0 | 52 | 25 | 293 | 122
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0170（4 列）
- 見出し：Payroll staff SCS Headcount
- 例1 値：6 | 4 | 2 | 17 | 13
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff Other…, Payroll staff Total…
- 例2 値：2 | 8 | 4 | 126 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff Other…, Payroll staff Total…

## g0171（4 列）
- 見出し：Payroll staff Other, unknown or unspecified Headcount
- 例1 値：49 | 4 | 0 | 0 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Total…
- 例2 値：0 | 0 | 0 | 70 | 5
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Total…

## g0172（4 列）
- 見出し：Payroll staff Total Employees Headcount
- 例1 値：44 | 684 | 212 | 49 | 60
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…
- 例2 値：5 | 1142 | 147 | 2607 | 316
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

## g0173（4 列）
- 見出し：Non-payroll Staff Agency staff (clerical/admin) Headcount
- 例1 値：0 | 1 | 1 | 0 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…
- 例2 値：47 | 0 | 0 | 0 | 3
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

## g0174（1 列）
- 見出し：Post Date
- 例1 値：21/11/2011 | 18/11/2011 | 29/11/2011 | 31/01/2011 | 23/11/2011
  - 同じ表の列：Amount, Reference Number, Code, MCC

## g0175（3 列）
- 見出し：Amount
- 例1 値：」762.00 | 」5,224.24 | 」1,215.54 | 」570.00 | 」506.70
  - 同じ表の列：Post Date, Reference Number, Code, MCC
- 例2 値：」581.88 | 」1,088.02 | 」510.00 | 」600.00 | 」600.00
  - 同じ表の列：Date, Supplier, Comments

## g0176（1 列）
- 見出し：Reference Number
- 例1 値：7.46786E+22 | 7.48305E+22 | 7.46786E+22 | 7.47451E+22 | 7.48305E+22
  - 同じ表の列：Post Date, Amount, Code, MCC

## g0177（1 列）
- 見出し：Code
- 例1 値：GB | GB | GB | GB | GB
  - 同じ表の列：Post Date, Amount, Reference Number, MCC

## g0178（2 列）
- 見出し：MCC
- 例1 値：4722 | 5970 | 9399 | 7392 | 9399
  - 同じ表の列：Post Date, Amount, Reference Number, Code
- 例2 値：7342 | 5732 | 5942 | 1520 | 5942
  - 同じ表の列：Department, date, Net Amount

## g0179（1 列）
- 見出し：Apr-10
- 例1 値：Oct-10 | Feb-11 | Sep-10 | make payment within 30 days and which c… | Jan-11
  - 同じ表の列：665, 4287730, 450, 67.67, 2174267, 652, 98.05, 3950347

## g0180（1 列）
- 見出し：665
- 例1 値：382 | 433 | 454 | 418 | 297
  - 同じ表の列：Apr-10, 4287730, 450, 67.67, 2174267, 652, 98.05, 3950347

## g0181（1 列）
- 見出し：4287730
- 例1 値：4452432 | 6163233 | 1412954 | 2342148 | 3217981
  - 同じ表の列：Apr-10, 665, 450, 67.67, 2174267, 652, 98.05, 3950347

## g0182（1 列）
- 見出し：450
- 例1 値：297 | 323 | 183 | 277 | 239
  - 同じ表の列：Apr-10, 665, 4287730, 67.67, 2174267, 652, 98.05, 3950347

## g0183（1 列）
- 見出し：67.67
- 例1 値：61.62 | 74.59 | 79.25 | 75.07 | 65.42
  - 同じ表の列：Apr-10, 665, 4287730, 450, 2174267, 652, 98.05, 3950347

## g0184（1 列）
- 見出し：2174267
- 例1 値：855821 | 4917945 | 1732174.77 | 2785755 | 5239489
  - 同じ表の列：Apr-10, 665, 4287730, 450, 67.67, 652, 98.05, 3950347

## g0185（1 列）
- 見出し：652
- 例1 値：357 | 271 | 407 | 310 | 348
  - 同じ表の列：Apr-10, 665, 4287730, 450, 67.67, 2174267, 98.05, 3950347

## g0186（1 列）
- 見出し：98.05
- 例1 値：96.6 | 95.81 | 95.08 | 96.75 | 95.54
  - 同じ表の列：Apr-10, 665, 4287730, 450, 67.67, 2174267, 652, 3950347

## g0187（1 列）
- 見出し：3950347
- 例1 値：4917945 | 6066153 | 3880392.1 | 1406161 | 3861665
  - 同じ表の列：Apr-10, 665, 4287730, 450, 67.67, 2174267, 652, 98.05

## g0188（1 列）
- 見出し：660
- 例1 値：433 | 317 | 365 | 450 | 297
  - 同じ表の列：Apr-10, 665, 4287730, 450, 67.67, 2174267, 652, 98.05

## g0189（1 列）
- 見出し：Main, parent or sponsoring department:
- 例1 値：Department for Education | Department for Education | Department for Education | Department for Education | Department for Education
  - 同じ表の列：Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0190（1 列）
- 見出し：Payroll staff
- 例1 値：190 | 1 | 36 | Headcount | 30
  - 同じ表の列：Organisation type, Main, parent or spo…, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0191（1 列）
- 見出し：Number of non-payroll staff (contingent labour and consultan
- 例1 値：5 | 20 | Agency staff (clerical/admin) | 55 | 197
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0192（1 列）
- 見出し：Payroll staff costs
- 例1 値：」98,564.44 | 」649,642.00 | Salary | 」4,350,681.23 | 」1,333,608.91
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0193（1 列）
- 見出し：Non-Payroll staff (contingent labour/consultancy - CCL) cost
- 例1 値：」36,257.31 | -」294,700.42 | 」88,065.00 | 」806,570.00 | Total cost of contingent labour: agency…
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Grand Total paybill…, Comments and notes

## g0194（1 列）
- 見出し：Grand Total paybill/staffing (payroll and non-payroll) costs
- 例1 値：」449,899.67 | 」921,458.00 | 」2,552,336.74 | 」11,317,964.78 | 」162,168.00
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Comments and notes

## g0195（1 列）
- 見出し：Comments and notes
- 例1 値：Please note "Specialist Contractors" da… | Agency staff include Practitioners as w…
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0196（1 列）
- 見出し：Parent Department
- 例1 値：Department for Education | Department for Education | Department for Education | Department for Education | Department for Education
  - 同じ表の列：Organisation, Unit, Reporting Senior Po…, Grade, Payscale Minimum (」), Payscale Maximum (」), Generic Job Title, Number of Posts in …

## g0197（1 列）
- 見出し：Unit
- 例1 値：Early Years, Extended Schools and Speci… | Safeguarding Group | Private Office | School Standards Group | Academies Delivery Group
  - 同じ表の列：Parent Department, Organisation, Reporting Senior Po…, Grade, Payscale Minimum (」), Payscale Maximum (」), Generic Job Title, Number of Posts in …

## g0198（1 列）
- 見出し：Reporting Senior Post
- 例1 値：DfE-4074 | DfE-5024 | DfE-5031 | DfE-4044 | DfE-5044
  - 同じ表の列：Parent Department, Organisation, Unit, Grade, Payscale Minimum (」), Payscale Maximum (」), Generic Job Title, Number of Posts in …

## g0199（1 列）
- 見出し：Grade
- 例1 値：Grade 7 | EA/AO | Grade 7 | EO | SEO
  - 同じ表の列：Parent Department, Organisation, Unit, Reporting Senior Po…, Payscale Minimum (」), Payscale Maximum (」), Generic Job Title, Number of Posts in …

## g0200（1 列）
- 見出し：Payscale Minimum (」)
- 例1 値：21916 | 55431 | 33200 | 33200 | 33200
  - 同じ表の列：Parent Department, Organisation, Unit, Reporting Senior Po…, Grade, Payscale Maximum (」), Generic Job Title, Number of Posts in …

## g0201（1 列）
- 見出し：Payscale Maximum (」)
- 例1 値：57222 | 57222 | 40828 | 32232 | 32232
  - 同じ表の列：Parent Department, Organisation, Unit, Reporting Senior Po…, Grade, Payscale Minimum (」), Generic Job Title, Number of Posts in …

## g0202（1 列）
- 見出し：Generic Job Title
- 例1 値：Policy Adviser | Business Manager | Senior Policy Adviser | VFM Economic Appraisal Team Leader | Senior Policy Adviser
  - 同じ表の列：Parent Department, Organisation, Unit, Reporting Senior Po…, Grade, Payscale Minimum (」), Payscale Maximum (」), Number of Posts in …

## g0203（1 列）
- 見出し：Number of Posts in FTE
- 例1 値：11.12 | 1 | 8 | 1 | 1
  - 同じ表の列：Parent Department, Organisation, Unit, Reporting Senior Po…, Grade, Payscale Minimum (」), Payscale Maximum (」), Generic Job Title

## g0204（1 列）
- 見出し：Professional/Occupational Group
- 例1 値：Policy | Policy | Policy | Policy | Policy
  - 同じ表の列：Parent Department, Organisation, Unit, Reporting Senior Po…, Grade, Payscale Minimum (」), Payscale Maximum (」), Generic Job Title

## g0205（1 列）
- 見出し：00:00
- 例1 値：98 | 94 | 111 | 0 | 226
  - 同じ表の列：DATE, 00:30, 01:00, 01:30, 02:00, 02:30, 03:00, 03:30

## g0206（1 列）
- 見出し：00:30
- 例1 値：0 | 0 | 84 | 0 | 83
  - 同じ表の列：DATE, 00:00, 01:00, 01:30, 02:00, 02:30, 03:00, 03:30

## g0207（1 列）
- 見出し：01:00
- 例1 値：0 | 87 | 93 | 0 | 101
  - 同じ表の列：DATE, 00:00, 00:30, 01:30, 02:00, 02:30, 03:00, 03:30

## g0208（1 列）
- 見出し：01:30
- 例1 値：0 | 98 | 93 | 0 | 81
  - 同じ表の列：DATE, 00:00, 00:30, 01:00, 02:00, 02:30, 03:00, 03:30

## g0209（1 列）
- 見出し：02:00
- 例1 値：96 | 98 | 222 | 79 | 86
  - 同じ表の列：DATE, 00:00, 00:30, 01:00, 01:30, 02:30, 03:00, 03:30

## g0210（1 列）
- 見出し：02:30
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：DATE, 00:00, 00:30, 01:00, 01:30, 02:00, 03:00, 03:30

## g0211（1 列）
- 見出し：03:00
- 例1 値：84 | 0 | 0 | 94 | 86
  - 同じ表の列：DATE, 00:00, 00:30, 01:00, 01:30, 02:00, 02:30, 03:30

## g0212（1 列）
- 見出し：03:30
- 例1 値：98 | 96 | 190 | 0 | 0
  - 同じ表の列：DATE, 00:00, 00:30, 01:00, 01:30, 02:00, 02:30, 03:00

## g0213（1 列）
- 見出し：04:00
- 例1 値：94 | 109 | 0 | 100.8 | 96
  - 同じ表の列：DATE, 00:00, 00:30, 01:00, 01:30, 02:00, 02:30, 03:00

## g0214（1 列）
- 見出し：Expense Type
- 例1 値：Utilisation of Provisions - Purchase of… | Research and Development Expenditure | Capital Grants To Local Government | R & D Research and Development Expendit… | Other Technical Professional Services
  - 同じ表の列：Date of Payment, Expense Area, Supplier, Transaction Number, Amount, Supplier Type

## g0215（1 列）
- 見出し：Expense Area
- 例1 値：Net Zero, Nuclear & International - Sci… | Net Zero Buildings and Industry (NZBI) … | Net Zero, Nuclear & International - NDA | Net Zero, Nuclear & International - Nuc… | Net Zero Buildings and Industry (NZBI) …
  - 同じ表の列：Date of Payment, Expense Type, Supplier, Transaction Number, Amount, Supplier Type

## g0216（6 列）
- 見出し：Amount
- 例1 値：90291 | 28800 | 97246.38 | 31374.85 | 29146.66
  - 同じ表の列：Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Supplier Type
- 例2 値：47280 | 61092 | 155875.62 | 166666.67 | 37254229
  - 同じ表の列：Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Supplier Post Code, Supplier Type

## g0217（2 列）
- 見出し：Supplier Type
- 例1 値：VENDOR | WGA ONLY | WGA ONLY | WGA ONLY | VENDOR
  - 同じ表の列：Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount
- 例2 値：Vendor | Vendor | Wga Only | Vendor | Vendor
  - 同じ表の列：Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount, Supplier Post Code

## g0218（1 列）
- 見出し：Merchant
- 例1 値：Connex Travel Limited | Northstar Safety Group | Northstar Safety Group | Amazon Marketplace | The Cinnamon Club
  - 同じ表の列：Transaction Referen…, Transaction Date, Total

## g0219（1 列）
- 見出し：Total
- 例1 値：」529.20 | 」531.36 | 」999.00 | 」717.70 | 」527.68
  - 同じ表の列：Transaction Referen…, Transaction Date, Merchant

## g0220（3 列）
- 見出し：Minister
- 例1 値：Amanda Solloway | Graham Stuart | Martin Callanan | Grant Shapps | Andrew Bowie
  - 同じ表の列：Date, Gift, Given or received, Who gift was given …, Value (」), Outcome (received g…
- 例2 値：Chris Grayling | Baroness Sugg | Jesse Norman | Jo Johnson | Nusrat Ghani
  - 同じ表の列：Date, Gift, Given or received, Who gift was given …, Value (」), Outcome (received g…

## g0221（3 列）
- 見出し：Date
- 例1 値：NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN
  - 同じ表の列：Minister, Gift, Given or received, Who gift was given …, Value (」), Outcome (received g…
- 例2 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Gift, Given or received, Who gift was given …, Value (」), Outcome (received g…

## g0222（2 列）
- 見出し：Gift
- 例1 値：NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN
  - 同じ表の列：Minister, Date, Given or received, Who gift was given …, Value (」), Outcome (received g…
- 例2 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Date, Given or received, Who gift was given …, Value (」), Outcome (received g…

## g0223（2 列）
- 見出し：Given or received
- 例1 値：NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN
  - 同じ表の列：Minister, Date, Gift, Who gift was given …, Value (」), Outcome (received g…
- 例2 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Date, Gift, Who gift was given …, Value (」), Outcome (received g…

## g0224（2 列）
- 見出し：Who gift was given to or received from
- 例1 値：NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN
  - 同じ表の列：Minister, Date, Gift, Given or received, Value (」), Outcome (received g…
- 例2 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Date, Gift, Given or received, Value (」), Outcome (received g…

## g0225（2 列）
- 見出し：Value (」)
- 例1 値：NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN
  - 同じ表の列：Minister, Date, Gift, Given or received, Who gift was given …, Outcome (received g…
- 例2 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Date, Gift, Given or received, Who gift was given …, Outcome (received g…

## g0226（2 列）
- 見出し：Outcome (received gifts only)
- 例1 値：NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN | NIL RETURN
  - 同じ表の列：Minister, Date, Gift, Given or received, Who gift was given …, Value (」)
- 例2 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Date, Gift, Given or received, Who gift was given …, Value (」)

## g0227（1 列）
- 見出し：Minister
- 例1 値：Rt Hon David Davis MP | Rt Hon David Jones MP | Robin Walker MP | Lord Bridges of Headley | Robin Walker MP
  - 同じ表の列：Date, Type of hospitality…

## g0228（2 列）
- 見出し：Type of hospitality received
- 例1 値：Dinner | Dinner | Dinner | Dinner | Dinner
  - 同じ表の列：Minister, Date
- 例2 値：Lunch | Lunch | Lunch | Lunch | Lunch
  - 同じ表の列：Date of hospitality

## g0229（3 列）
- 見出し：Department Family
- 例1 値：DFID | DFID | DFID | DFID | DFID
  - 同じ表の列：Entity, Transaction Date, Expense Type, Expense Area, Transaction Number, Amount
- 例2 値：OFWAT | OFWAT | OFWAT | OFWAT | OFWAT
  - 同じ表の列：Entity, Date, Expense type, Expense area, Supplier, Transaction number, Amount

## g0230（1 列）
- 見出し：Expense Type
- 例1 値：Staff Business Travel and Subsistence | Aid to civil society organisations / NG… | Technical & Advisory services | Aid to civil society organisations / NG… | Printing, Stationary & Postage
  - 同じ表の列：Department Family, Entity, Transaction Date, Expense Area, Transaction Number, Amount

## g0231（1 列）
- 見出し：Expense Area
- 例1 値：International Relations Division | West and Southern Africa | East and Central Africa | Security & Humanitarian, Middle East, C… | West and Southern Africa
  - 同じ表の列：Department Family, Entity, Transaction Date, Expense Type, Transaction Number, Amount

## g0232（5 列）
- 見出し：Amount
- 例1 値：253.61 | 1524.22 | 51818.91 | 850.1 | 5282.8
  - 同じ表の列：Department Family, Entity, Transaction Date, Expense Type, Expense Area, Transaction Number
- 例2 値：352.50 | 197447.37 | 407.00 | 189773.62 | 1200.00
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number

## g0233（1 列）
- 見出し：Post_Date
- 例1 値：26/05/2011 | 05/05/2011 | 19/04/2011 | 16/05/2011 | 05/05/2011
  - 同じ表の列：Amount 」

## g0234（1 列）
- 見出し：Amount 」
- 例1 値：2012.78 | 564.66 | 1042.72 | 927.60 | 1084.00
  - 同じ表の列：Post_Date

## g0235（1 列）
- 見出し：Permanent secretary
- 例1 値：Angela McLean | Angela McLean | Angela McLean | Angela McLean | Angela McLean
  - 同じ表の列：Date, Purpose of meeting

## g0236（1 列）
- 見出し：Date
- 例1 値：2023-09-20 | 2023-07-03 | 2023-09-15 | 2023-07-26 | 2023-07-26
  - 同じ表の列：Permanent secretary, Purpose of meeting

## g0237（1 列）
- 見出し：Purpose of meeting
- 例1 値：Introductory meeting | Introductory meeting | Introductory meeting | AI in the workplace discussion | Attending the Google Curiosity Gardens …
  - 同じ表の列：Permanent secretary, Date

## g0238（2 列）
- 見出し：Transaction Date
- 例1 値：31-Aug-23 | 31-Aug-23 | 31-Aug-23 | 31-Aug-23 | 31-Aug-23
  - 同じ表の列：Transaction Referen…, Merchant, Total
- 例2 値：20-May-11 | 23-Dec-11 | 01-Dec-11 | 01-Dec-11 | 03-May-11
  - 同じ表の列：」 Gross

## g0239（1 列）
- 見出し：Merchant
- 例1 値：House of Commons | Appreciate Group Plc | Appreciate Group Plc | Appreciate Group Plc | Appreciate Group Plc
  - 同じ表の列：Transaction Referen…, Transaction Date, Total

## g0240（1 列）
- 見出し：Total
- 例1 値：」965.00 | 」7,502.88 | 」1,276.18 | 」2,002.38 | 」500.00
  - 同じ表の列：Transaction Referen…, Transaction Date, Merchant

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
g0151	
g0152	
g0153	
g0154	
g0155	
g0156	
g0157	
g0158	
g0159	
g0160	
g0161	
g0162	
g0163	
g0164	
g0165	
g0166	
g0167	
g0168	
g0169	
g0170	
g0171	
g0172	
g0173	
g0174	
g0175	
g0176	
g0177	
g0178	
g0179	
g0180	
g0181	
g0182	
g0183	
g0184	
g0185	
g0186	
g0187	
g0188	
g0189	
g0190	
g0191	
g0192	
g0193	
g0194	
g0195	
g0196	
g0197	
g0198	
g0199	
g0200	
g0201	
g0202	
g0203	
g0204	
g0205	
g0206	
g0207	
g0208	
g0209	
g0210	
g0211	
g0212	
g0213	
g0214	
g0215	
g0216	
g0217	
g0218	
g0219	
g0220	
g0221	
g0222	
g0223	
g0224	
g0225	
g0226	
g0227	
g0228	
g0229	
g0230	
g0231	
g0232	
g0233	
g0234	
g0235	
g0236	
g0237	
g0238	
g0239	
g0240	
```
