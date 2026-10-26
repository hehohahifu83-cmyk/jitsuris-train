# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：indicator
- 例1 値：16 | 12b | 8c | 6 | 2a
  - 同じ表の列：type, topic, response, year, respondent_group, sample_size, result, format

## g0002（1 列）
- 見出し：type
- 例1 値：Other | Other | Other | Other | Other
  - 同じ表の列：indicator, topic, response, year, respondent_group, sample_size, result, format

## g0003（1 列）
- 見出し：topic
- 例1 値：Perceptions of safety | Food security | Health | Physical activity | Physical activity
  - 同じ表の列：indicator, type, response, year, respondent_group, sample_size, result, format

## g0004（1 列）
- 見出し：response
- 例1 値：Yes, in the last 12 months | Average satisfaction score (from 0-100) | Yes, in the last 12 months | Yes, in the last 12 months | Reported as feeling very safe or safe
  - 同じ表の列：indicator, type, topic, year, respondent_group, sample_size, result, format

## g0005（4 列）
- 見出し：year
- 例1 値：2022 | 2022 | 2022 | 2022 | 2022
  - 同じ表の列：indicator, type, topic, response, respondent_group, sample_size, result, format
- 例2 値：2013 | 2011 | 2014 | 2010 | 2012
  - 同じ表の列：total_patents_grant…, patents_granted_per…

## g0006（1 列）
- 見出し：respondent_group
- 例1 値：65+ years | 65+ years | Female | Kensington / Flemington 3031 | Docklands 3008
  - 同じ表の列：indicator, type, topic, response, year, sample_size, result, format

## g0007（1 列）
- 見出し：sample_size
- 例1 値：1508 | 1508 | 133 | 242 | 411
  - 同じ表の列：indicator, type, topic, response, year, respondent_group, result, format

## g0008（1 列）
- 見出し：result
- 例1 値：76.0 | 86.2 | 14.7 | 67.7 | 10.7
  - 同じ表の列：indicator, type, topic, response, year, respondent_group, sample_size, format

## g0009（1 列）
- 見出し：format
- 例1 値：Average | Per cent | Per cent | Per cent | Per cent
  - 同じ表の列：indicator, type, topic, response, year, respondent_group, sample_size, result

## g0010（1 列）
- 見出し：profile
- 例1 値：Southbank (high rise residents) | Carlton (high rise residents) | Parkville (high rise residents) | Melbourne (CBD) (high rise residents) | Carlton (high rise residents)
  - 同じ表の列：census_year, category, sub_category, sub_order, value

## g0011（1 列）
- 見出し：census_year
- 例1 値：2016 | 2016 | 2016 | 2016 | 2016
  - 同じ表の列：profile, category, sub_category, sub_order, value

## g0012（1 列）
- 見出し：category
- 例1 値：Housing tenure | Level of education | Providing child care | Educational institution attendance | Labour force status - overview
  - 同じ表の列：profile, census_year, sub_category, sub_order, value

## g0013（1 列）
- 見出し：sub_category
- 例1 値：Malaysia | $800 - $999 | Secular Beliefs and Other Spiritual Bel… | Malay | $1,600 - $1,799
  - 同じ表の列：profile, census_year, category, sub_order, value

## g0014（1 列）
- 見出し：sub_order
- 例1 値：22 | 3 | 1 | 10 | 6
  - 同じ表の列：profile, census_year, category, sub_category, value

## g0015（1 列）
- 見出し：value
- 例1 値：705 | 22176 | 705 | 13 | 1599
  - 同じ表の列：profile, census_year, category, sub_category, sub_order

## g0016（1 列）
- 見出し：total_patents_granted
- 例1 値：120 | 150 | 88 | 133 | 103
  - 同じ表の列：year, patents_granted_per…

## g0017（1 列）
- 見出し：patents_granted_per_100_000_residents
- 例1 値：132.68 | 142.29 | 84.28 | 103.05 | 90.14
  - 同じ表の列：year, total_patents_grant…

## g0018（1 列）
- 見出し：genus
- 例1 値：Platanus | Laurus | Acer | Lagerstroemia | Acer
  - 同じ表の列：species, dbh, height, common, ref, maturity, updated, ule_min, ule_max

## g0019（1 列）
- 見出し：species
- 例1 値：A. x freemanii 'Autumn Blaze' | A. x freemanii 'Autumn Blaze' | A. littoralis | L. nobilis | A. x freemanii 'Autumn Blaze'
  - 同じ表の列：genus, dbh, height, common, ref, maturity, updated, ule_min, ule_max

## g0020（1 列）
- 見出し：dbh
- 例1 値：13 | 11 | 10 | 7 | 18
  - 同じ表の列：genus, species, height, common, ref, maturity, updated, ule_min, ule_max

## g0021（1 列）
- 見出し：height
- 例1 値：5 | 8 | 4 | 6 | 4
  - 同じ表の列：genus, species, dbh, common, ref, maturity, updated, ule_min, ule_max

## g0022（1 列）
- 見出し：common
- 例1 値：Blackwood | Bloodgood London Plane | Box Elder | Black Locust | Bloodgood London Plane
  - 同じ表の列：genus, species, dbh, height, ref, maturity, updated, ule_min, ule_max

## g0023（1 列）
- 見出し：ref
- 例1 値：10541 | 13432 | 19824 | 4944 | 5054
  - 同じ表の列：genus, species, dbh, height, common, maturity, updated, ule_min, ule_max

## g0024（1 列）
- 見出し：maturity
- 例1 値：Young | Mature | Semi-mature | Semi-mature | Mature
  - 同じ表の列：genus, species, dbh, height, common, ref, updated, ule_min, ule_max

## g0025（1 列）
- 見出し：updated
- 例1 値：8/11/2016 | 15/09/2016 | 23/11/2016 | 15/11/2016 | 21/06/2016
  - 同じ表の列：genus, species, dbh, height, common, ref, maturity, ule_min, ule_max

## g0026（1 列）
- 見出し：ule_min, ule_max
- 例1 値：11, 20 | 1, 5 | 20 | 20 | 20
  - 同じ表の列：genus, species, dbh, height, common, ref, maturity, updated

## g0027（1 列）
- 見出し：1ST TERM CENSUS - FTE - 2020 - TOTAL
- 例1 値：557.4 | 34.2 | 200.4 | 163.4 | 111.8
  - 同じ表の列：1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - H…

## g0028（1 列）
- 見出し：1ST TERM CENSUS - FTE - 2020 - YEAR 11
- 例1 値：1 | 17.7 | 45.3 | 630.8 | 24.2
  - 同じ表の列：1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - H…

## g0029（1 列）
- 見出し：1ST TERM CENSUS - FTE - 2020 - YEAR 12
- 例1 値：2.7 | 322.4 | 0.4 | 23.1 | 1
  - 同じ表の列：1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - H…

## g0030（1 列）
- 見出し：1ST TERM CENSUS - FTE - 2020 - YEAR 13
- 例1 値：2.3 | 1 | 0.8 | 2 | 5.6
  - 同じ表の列：1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - H…

## g0031（1 列）
- 見出し：1ST TERM CENSUS - FTE - 2021 - TOTAL
- 例1 値：488.2 | 131 | 404.6 | 54.2 | 345.5
  - 同じ表の列：1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - H…

## g0032（1 列）
- 見出し：1ST TERM CENSUS - FTE - 2021 - YEAR 11
- 例1 値：50.3 | 375.1 | 18.7 | 0.8 | 41.2
  - 同じ表の列：1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - H…

## g0033（1 列）
- 見出し：1ST TERM CENSUS - FTE - 2021 - YEAR 12
- 例1 値：0.8 | 0.2 | 8.5 | 2.8 | 6.4
  - 同じ表の列：1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - H…

## g0034（1 列）
- 見出し：1ST TERM CENSUS - FTE - 2021 - YEAR 13
- 例1 値：0.6 | 3 | 5.1 | 13.9 | 0.5
  - 同じ表の列：1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - H…

## g0035（1 列）
- 見出し：1ST TERM CENSUS - HEADCOUNT - 2020 - TOTAL
- 例1 値：326 | 364 | 95 | 63 | 96
  - 同じ表の列：1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…

## g0036（1 列）
- 見出し：1ST TERM CENSUS - HEADCOUNT - 2020 - YEAR 11
- 例1 値：1 | 13 | 24 | 26 | 3
  - 同じ表の列：1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…, 1ST TERM CENSUS - F…

## g0037（1 列）
- 見出し：Reason for enforcement activity
- 例1 値：FSP not audited at the frequency determ… | FSP not revised so as to comply with th… | Total | FSP not prepared, implemented, maintain… | FSP audit report not retained by busine…
  - 同じ表の列：Written warnings, Improvement notices, Prohibition orders, Expiations, Prosecutions

## g0038（1 列）
- 見出し：Written warnings
- 例1 値：1 | 0 | 0 | 0 | 1
  - 同じ表の列：Reason for enforcem…, Improvement notices, Prohibition orders, Expiations, Prosecutions

## g0039（1 列）
- 見出し：Improvement notices
- 例1 値：1 | 0 | 2 | 1 | 0
  - 同じ表の列：Reason for enforcem…, Written warnings, Prohibition orders, Expiations, Prosecutions

## g0040（1 列）
- 見出し：Prohibition orders
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Reason for enforcem…, Written warnings, Improvement notices, Expiations, Prosecutions

## g0041（1 列）
- 見出し：Expiations
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Reason for enforcem…, Written warnings, Improvement notices, Prohibition orders, Prosecutions

## g0042（1 列）
- 見出し：Prosecutions
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Reason for enforcem…, Written warnings, Improvement notices, Prohibition orders, Expiations

## g0043（1 列）
- 見出し：X Values
- 例1 値：2019 | 2013 | 2015 | 2014 | 2010
  - 同じ表の列：Melbourne, Sydney, Brisbane, Perth, NEPM standard

## g0044（2 列）
- 見出し：Melbourne
- 例1 値：0.041 | 0.039 | 0.035666666666667 | 0.039 | 0.036
  - 同じ表の列：X Values, Sydney, Brisbane, Perth, NEPM standard
- 例2 値：18.05962449 | 20.874289 | 2.978230963 | 49.4114709 | 8.676384645
  - 同じ表の列：Public transport ac…, Adelaide, Brisbane, Canberra, Darwin, Hobart, Perth, Sydney

## g0045（2 列）
- 見出し：Sydney
- 例1 値：0.035125 | 0.039857142857143 | 0.040285714285714 | 0.036428571428572 | 0.042428571428572
  - 同じ表の列：X Values, Melbourne, Brisbane, Perth, NEPM standard
- 例2 値：0.738789994 | 14.29654739 | 47.45623296 | 4.017444115 | 33.49098554
  - 同じ表の列：Public transport ac…, Adelaide, Brisbane, Canberra, Darwin, Hobart, Melbourne, Perth

## g0046（2 列）
- 見出し：Brisbane
- 例1 値：0.03375 | 0.033 | 0.036 | 0.03775 | 0.0335
  - 同じ表の列：X Values, Melbourne, Sydney, Perth, NEPM standard
- 例2 値：42.52713515 | 7.802304988 | 15.59138437 | 23.86575801 | 10.21341748
  - 同じ表の列：Public transport ac…, Adelaide, Canberra, Darwin, Hobart, Melbourne, Perth, Sydney

## g0047（2 列）
- 見出し：Perth
- 例1 値：0.034 | 0.04 | 0.030333333333333 | 0.032333333333333 | 0.031333333333333
  - 同じ表の列：X Values, Melbourne, Sydney, Brisbane, NEPM standard
- 例2 値：51.36595635 | 26.75668169 | 8.868853688 | 1.81705562 | 11.19145265
  - 同じ表の列：Public transport ac…, Adelaide, Brisbane, Canberra, Darwin, Hobart, Melbourne, Sydney

## g0048（1 列）
- 見出し：NEPM standard
- 例1 値：0.12 | 0.12 | 0.12 | 0.12 | 0.12
  - 同じ表の列：X Values, Melbourne, Sydney, Brisbane, Perth

## g0049（1 列）
- 見出し：NumberofSpeciesBreeding
- 例1 値：1 | 10 | 25 | 7 | 16
  - 同じ表の列：Year, Mean

## g0050（1 列）
- 見出し：Mean
- 例1 値：12.9 | 12.9 | 12.9 | 12.9 | 12.9
  - 同じ表の列：Year, NumberofSpeciesBree…

## g0051（1 列）
- 見出し：Public transport accessibility
- 例1 値：Very High Accessibility | Limited Accessibility | Moderate Accessibility | Low Accessibility | High Accessibility
  - 同じ表の列：Adelaide, Brisbane, Canberra, Darwin, Hobart, Melbourne, Perth, Sydney

## g0052（1 列）
- 見出し：Adelaide
- 例1 値：0.682122432 | 21.91043192 | 61.94896264 | 10.6901474 | 4.768335607
  - 同じ表の列：Public transport ac…, Brisbane, Canberra, Darwin, Hobart, Melbourne, Perth, Sydney

## g0053（1 列）
- 見出し：Canberra
- 例1 値：8.850400873 | 29.12651381 | 56.74596035 | 4.644893232 | 0.63223173
  - 同じ表の列：Public transport ac…, Adelaide, Brisbane, Darwin, Hobart, Melbourne, Perth, Sydney

## g0054（1 列）
- 見出し：Darwin
- 例1 値：6.253272061 | 59.59998449 | 4.861070715 | 4.005002618 | 25.28067012
  - 同じ表の列：Public transport ac…, Adelaide, Brisbane, Canberra, Hobart, Melbourne, Perth, Sydney

## g0055（1 列）
- 見出し：Hobart
- 例1 値：39.28771897 | 1.336623243 | 11.72147251 | 42.66260495 | 4.991580326
  - 同じ表の列：Public transport ac…, Adelaide, Brisbane, Canberra, Darwin, Melbourne, Perth, Sydney

## g0056（1 列）
- 見出し：Proportion Unsentenced
- 例1 値：27.4 | 23.1 | 24.3 | 24 | 23.4
  - 同じ表の列：Year

## g0057（1 列）
- 見出し：Six_Cities22
- 例1 値：Rest of NSW | Central River City | Total NSW | Remainder GMA** | Central Coast City
  - 同じ表の列：ERP_2021, ERP_2022, ERP_2023, ERP_2024, ERP_2025, ERP_2026, ERP_2027, ERP_2028

## g0058（1 列）
- 見出し：ERP_2021
- 例1 値：6390350.99999965 | 348493.00000170 | 1615746.10375162 | 422439.99999711 | 8097062.00000743
  - 同じ表の列：Six_Cities22, ERP_2022, ERP_2023, ERP_2024, ERP_2025, ERP_2026, ERP_2027, ERP_2028

## g0059（1 列）
- 見出し：ERP_2022
- 例1 値：427759.12304483 | 8158192.69863783 | 1708315.25758026 | 2144662.04460373 | 92930.15521530
  - 同じ表の列：Six_Cities22, ERP_2021, ERP_2023, ERP_2024, ERP_2025, ERP_2026, ERP_2027, ERP_2028

## g0060（1 列）
- 見出し：ERP_2023
- 例1 値：93984.91838010 | 1720685.17759220 | 1690397.36540201 | 353050.87062065 | 626630.48587769
  - 同じ表の列：Six_Cities22, ERP_2021, ERP_2022, ERP_2024, ERP_2025, ERP_2026, ERP_2027, ERP_2028

## g0061（1 列）
- 見出し：ERP_2024
- 例1 値：356339.41978466 | 1733092.36149729 | 1733470.12092960 | 635929.34847588 | 2227748.82328070
  - 同じ表の列：Six_Cities22, ERP_2021, ERP_2022, ERP_2023, ERP_2025, ERP_2026, ERP_2027, ERP_2028

## g0062（1 列）
- 見出し：ERP_2025
- 例1 値：95795.08148450 | 1264410.71068318 | 5276251.70603443 | 1765016.59671279 | 1744178.67679451
  - 同じ表の列：Six_Cities22, ERP_2021, ERP_2022, ERP_2023, ERP_2024, ERP_2026, ERP_2027, ERP_2028

## g0063（1 列）
- 見出し：ERP_2026
- 例1 値：654003.15210872 | 362744.09097641 | 1283830.50755040 | 1797495.22953011 | 461307.20142599
  - 同じ表の列：Six_Cities22, ERP_2021, ERP_2022, ERP_2023, ERP_2024, ERP_2025, ERP_2027, ERP_2028

## g0064（1 列）
- 見出し：ERP_2027
- 例1 値：8778641.58543764 | 1303117.22462067 | 97540.11747310 | 1826834.87073614 | 2285987.38220145
  - 同じ表の列：Six_Cities22, ERP_2021, ERP_2022, ERP_2023, ERP_2024, ERP_2025, ERP_2026, ERP_2028

## g0065（1 列）
- 見出し：ERP_2028
- 例1 値：1778051.31941770 | 5481783.17620756 | 7097858.96850064 | 1854754.02353446 | 476698.24832214
  - 同じ表の列：Six_Cities22, ERP_2021, ERP_2022, ERP_2023, ERP_2024, ERP_2025, ERP_2026, ERP_2027

## g0066（1 列）
- 見出し：ERP_2029
- 例1 値：2330490.63682389 | 484354.05327437 | 1788529.83592372 | 5546903.19145126 | 99261.59524080
  - 同じ表の列：Six_Cities22, ERP_2021, ERP_2022, ERP_2023, ERP_2024, ERP_2025, ERP_2026, ERP_2027

## g0067（1 列）
- 見出し：Six Cities 2022
- 例1 値：Central River City | Rest of NSW | Total Sydney | Eastern Harbour City | ** Remainder GMA LGAs of Dungog, Single…
  - 同じ表の列：EMP_2021, EMP_2022, EMP_2023, EMP_2024, EMP_2025, EMP_2026, EMP_2027, EMP_2028

## g0068（1 列）
- 見出し：EMP_2021
- 例1 値：644373.88608854 | 3278887.15530813 | 177536.73525568 | 4052532.27817583 | 1554091.99138981
  - 同じ表の列：Six Cities 2022, EMP_2022, EMP_2023, EMP_2024, EMP_2025, EMP_2026, EMP_2027, EMP_2028

## g0069（1 列）
- 見出し：EMP_2022
- 例1 値：1559461.60105995 | 47282.43821971 | 647156.53404799 | 178838.55309527 | 2628025.41681395
  - 同じ表の列：Six Cities 2022, EMP_2021, EMP_2023, EMP_2024, EMP_2025, EMP_2026, EMP_2027, EMP_2028

## g0070（1 列）
- 見出し：EMP_2023
- 例1 値：191791.70342186 | 3504795.51031852 | 1659643.72313947 | 318644.34862850 | 689530.14037237
  - 同じ表の列：Six Cities 2022, EMP_2021, EMP_2022, EMP_2024, EMP_2025, EMP_2026, EMP_2027, EMP_2028

## g0071（1 列）
- 見出し：EMP_2024
- 例1 値：193610.75156725 | 2847250.37903432 | 146102.62922939 | 459896.87470216 | 4379198.04065161
  - 同じ表の列：Six Cities 2022, EMP_2021, EMP_2022, EMP_2023, EMP_2025, EMP_2026, EMP_2027, EMP_2028

## g0072（1 列）
- 見出し：EMP_2025
- 例1 値：194741.06855268 | 3583650.67481337 | 146121.45396387 | 1696404.21682780 | 705719.17394876
  - 同じ表の列：Six Cities 2022, EMP_2021, EMP_2022, EMP_2023, EMP_2024, EMP_2026, EMP_2027, EMP_2028

## g0073（1 列）
- 見出し：EMP_2026
- 例1 値：3624381.55417337 | 475194.51753562 | 329840.91215460 | 196424.85743290 | 821242.68957909
  - 同じ表の列：Six Cities 2022, EMP_2021, EMP_2022, EMP_2023, EMP_2024, EMP_2025, EMP_2027, EMP_2028

## g0074（1 列）
- 見出し：EMP_2027
- 例1 値：825697.50763040 | 333856.73178552 | 3681630.03688716 | 198600.49253352 | 487699.91800925
  - 同じ表の列：Six Cities 2022, EMP_2021, EMP_2022, EMP_2023, EMP_2024, EMP_2025, EMP_2026, EMP_2028

## g0075（1 列）
- 見出し：EMP_2028
- 例1 値：3741822.52814230 | 49841.19302910 | 337491.66449918 | 502566.89265674 | 3003127.77336913
  - 同じ表の列：Six Cities 2022, EMP_2021, EMP_2022, EMP_2023, EMP_2024, EMP_2025, EMP_2026, EMP_2027

## g0076（1 列）
- 見出し：EMP_2029
- 例1 値：151570.80189512 | 837508.38164391 | 4633525.15266826 | 517801.12083042 | 204166.34188893
  - 同じ表の列：Six Cities 2022, EMP_2021, EMP_2022, EMP_2023, EMP_2024, EMP_2025, EMP_2026, EMP_2027

## g0077（1 列）
- 見出し：TSN
- 例1 値：219874 | 215316 | 208110 | 223230 | 216438
  - 同じ表の列：TRANSIT_STOP_TYPE, SUBURB, TZ16_CODE

## g0078（1 列）
- 見出し：TRANSIT_STOP_TYPE
- 例1 値：Bus Stop | Train Station | Bus Stop | Bus Stop | Bus Stop
  - 同じ表の列：TSN, SUBURB, TZ16_CODE

## g0079（1 列）
- 見出し：SUBURB
- 例1 値：ARCADIA | QUIRINDI | PROSPECT | KENDALL | HORSLEY PARK
  - 同じ表の列：TSN, TRANSIT_STOP_TYPE, TZ16_CODE

## g0080（1 列）
- 見出し：TZ16_CODE
- 例1 値：3650 | 4120 | 3833 | 7351 | 5730
  - 同じ表の列：TSN, TRANSIT_STOP_TYPE, SUBURB

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
```
