# ラベル用シート 004 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_004.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0361（1 列）
- 見出し：2014
- 例1 値：4651 | 0 | 260 | 3550 | 0
  - 同じ表の列：Type, 2012, 2013, 2015, 2016, 2017, 2018, 2019

## g0362（1 列）
- 見出し：2015
- 例1 値：258 | 5141 | 257 | 0 | 3855
  - 同じ表の列：Type, 2012, 2013, 2014, 2016, 2017, 2018, 2019

## g0363（1 列）
- 見出し：2016
- 例1 値：0 | 0 | 3773 | 236 | 5025
  - 同じ表の列：Type, 2012, 2013, 2014, 2015, 2017, 2018, 2019

## g0364（1 列）
- 見出し：2017
- 例1 値：5295 | 287 | 0 | 294 | 3907
  - 同じ表の列：Type, 2012, 2013, 2014, 2015, 2016, 2018, 2019

## g0365（1 列）
- 見出し：2018
- 例1 値：233 | 0 | 5051 | 0 | 231
  - 同じ表の列：Type, 2012, 2013, 2014, 2015, 2016, 2017, 2019

## g0366（1 列）
- 見出し：2019
- 例1 値：5252 | 0 | 229 | 0 | 227
  - 同じ表の列：Type, 2012, 2013, 2014, 2015, 2016, 2017, 2018

## g0367（2 列）
- 見出し：2020
- 例1 値：0 | 0 | 5003 | 254 | 3870
  - 同じ表の列：Type, 2012, 2013, 2014, 2015, 2016, 2017, 2018
- 例2 値：895 | 1 | 5 | 30 | 50
  - 同じ表の列：MEASURE, GROUP, SUBJECT, CATEGORY, TAX, DETAILS, 2021, 2022

## g0368（1 列）
- 見出し：Vehicle Type
- 例1 値：Vehicle | Vehicle | Vehicle | Vehicle | Vehicle
  - 同じ表の列：No Of Vehicles

## g0369（1 列）
- 見出し：No Of Vehicles
- 例1 値：246,859 | 12 | 228,319 | 35,048 | 297
  - 同じ表の列：Vehicle Type

## g0370（1 列）
- 見出し：UID
- 例1 値：342 | 269 | AYCA-DTKVR | AYCA-E60ZH | 134
  - 同じ表の列：STAGE, DEVELOPMENT_NATURE, DEVELOPMENT_TYPE, ESTIMATED_NUMBER_OF…, STATUS, DEVELOPER_APPLICATI…, CONTRACT_DATE, ESTIMATED_SERVICE_D…

## g0371（1 列）
- 見出し：STAGE
- 例1 値：6 | 3 & 4 | 2A | 3 Precinct 4 | 4
  - 同じ表の列：UID, DEVELOPMENT_NATURE, DEVELOPMENT_TYPE, ESTIMATED_NUMBER_OF…, STATUS, DEVELOPER_APPLICATI…, CONTRACT_DATE, ESTIMATED_SERVICE_D…

## g0372（1 列）
- 見出し：DEVELOPMENT_NATURE
- 例1 値：Residential | Residential | Residential | Residential | Residential
  - 同じ表の列：UID, STAGE, DEVELOPMENT_TYPE, ESTIMATED_NUMBER_OF…, STATUS, DEVELOPER_APPLICATI…, CONTRACT_DATE, ESTIMATED_SERVICE_D…

## g0373（1 列）
- 見出し：DEVELOPMENT_TYPE
- 例1 値：Sub-division | Sub-division | Sub-division | Sub-division | Sub-division
  - 同じ表の列：UID, STAGE, DEVELOPMENT_NATURE, ESTIMATED_NUMBER_OF…, STATUS, DEVELOPER_APPLICATI…, CONTRACT_DATE, ESTIMATED_SERVICE_D…

## g0374（1 列）
- 見出し：ESTIMATED_NUMBER_OF_LOTS_OR_UNITS
- 例1 値：57 | 84 | 51 | 94 | 75
  - 同じ表の列：UID, STAGE, DEVELOPMENT_NATURE, DEVELOPMENT_TYPE, STATUS, DEVELOPER_APPLICATI…, CONTRACT_DATE, ESTIMATED_SERVICE_D…

## g0375（1 列）
- 見出し：STATUS
- 例1 値：Ready for service | Ready for service | Ready for service | Ready for service | Check with carrier
  - 同じ表の列：UID, STAGE, DEVELOPMENT_NATURE, DEVELOPMENT_TYPE, ESTIMATED_NUMBER_OF…, DEVELOPER_APPLICATI…, CONTRACT_DATE, ESTIMATED_SERVICE_D…

## g0376（1 列）
- 見出し：DEVELOPER_APPLICATION_DATE
- 例1 値：20150306 | 20140106 | 20121015 | 20141212 | 20150729
  - 同じ表の列：UID, STAGE, DEVELOPMENT_NATURE, DEVELOPMENT_TYPE, ESTIMATED_NUMBER_OF…, STATUS, CONTRACT_DATE, ESTIMATED_SERVICE_D…

## g0377（1 列）
- 見出し：CONTRACT_DATE
- 例1 値：20140610 | 20140716 | 20121026 | 20160531 | 20140423
  - 同じ表の列：UID, STAGE, DEVELOPMENT_NATURE, DEVELOPMENT_TYPE, ESTIMATED_NUMBER_OF…, STATUS, DEVELOPER_APPLICATI…, ESTIMATED_SERVICE_D…

## g0378（1 列）
- 見出し：ESTIMATED_SERVICE_DATE
- 例1 値：20170613 | 20180201 | 20040101 | 20141215 | 20041111
  - 同じ表の列：UID, STAGE, DEVELOPMENT_NATURE, DEVELOPMENT_TYPE, ESTIMATED_NUMBER_OF…, STATUS, DEVELOPER_APPLICATI…, CONTRACT_DATE

## g0379（1 列）
- 見出し：TECHNOLOGY_TYPE
- 例1 値：FTTP | FTTP | FTTP | FTTP | FTTP
  - 同じ表の列：UID, STAGE, DEVELOPMENT_NATURE, DEVELOPMENT_TYPE, ESTIMATED_NUMBER_OF…, STATUS, DEVELOPER_APPLICATI…, CONTRACT_DATE

## g0380（1 列）
- 見出し：NSW visitor expenditure in $ million
- 例1 値：24,799 | 30,848 | 41,480 | 28,862 | 33,031
  - 同じ表の列：Years

## g0381（1 列）
- 見出し：Licence number
- 例1 値：LIQC300239152 | LIQC300238105 | LIQC300230104 | LIQC300239470 | LIQC300225801
  - 同じ表の列：Licence type, Status, Start date, Trading Status, Suburb, LGA, Precinct, Extended trading

## g0382（1 列）
- 見出し：Licence type
- 例1 値：Liquor - club licence | Liquor - club licence | Liquor - club licence | Liquor - club licence | Liquor - club licence
  - 同じ表の列：Licence number, Status, Start date, Trading Status, Suburb, LGA, Precinct, Extended trading

## g0383（4 列）
- 見出し：Status
- 例1 値：Current | Current | Current | Current | Current
  - 同じ表の列：Licence number, Licence type, Start date, Trading Status, Suburb, LGA, Precinct, Extended trading
- 例2 値：Active | Emerging | Planned | Active | Active
  - 同じ表の列：State, University, Centre/Precinct, Investment & main p…, Focus sectors, Interesting facts

## g0384（1 列）
- 見出し：LGA
- 例1 値：Cootamundra-Gundagai Regional Council | Blacktown City Council | Mid-Coast Council | Dungog Shire Council | Blacktown City Council
  - 同じ表の列：Licence number, Licence type, Status, Start date, Trading Status, Suburb, Precinct, Extended trading

## g0385（1 列）
- 見出し：Precinct
- 例1 値：Sydney CBD Precinct | Sydney CBD Precinct | Sydney CBD Precinct | Sydney CBD Precinct | Sydney CBD Precinct
  - 同じ表の列：Licence number, Licence type, Status, Start date, Trading Status, Suburb, LGA, Extended trading

## g0386（1 列）
- 見出し：Extended trading
- 例1 値：No | No | No | No | No
  - 同じ表の列：Licence number, Licence type, Status, Start date, Trading Status, Suburb, LGA, Precinct

## g0387（1 列）
- 見出し：Reduced trading
- 例1 値：No | No | No | No | No
  - 同じ表の列：Licence number, Licence type, Status, Start date, Trading Status, Suburb, LGA, Precinct

## g0388（1 列）
- 見出し：Quarter
- 例1 値：Mar - 2026 | Jun - 2026 | Dec - 2023 | Dec - 2024 | Sep - 2023
  - 同じ表の列：Claims Received

## g0389（1 列）
- 見出し：Claims Received
- 例1 値：3249 | 3480 | 4933 | 2118 | 3700
  - 同じ表の列：Quarter

## g0390（1 列）
- 見出し：Id
- 例1 値：B-002647 | B-003967 | B-003966 | B-004546 | B-002188
  - 同じ表の列：Portfolio Dept?, Title, Portfolio, Classification, Type of Body, GFS Sector Classifi…, Materiality, Established By / Un…

## g0391（1 列）
- 見出し：Portfolio Dept?
- 例1 値：YES | YES | YES | YES | YES
  - 同じ表の列：Id, Title, Portfolio, Classification, Type of Body, GFS Sector Classifi…, Materiality, Established By / Un…

## g0392（1 列）
- 見出し：Title
- 例1 値：Cancer Australia Advisory Council | National Investment Advisory Board | Emagy Pty Ltd | Strengthening Medicare Taskforce | Global Infrastructure Partners Transiti…
  - 同じ表の列：Id, Portfolio Dept?, Portfolio, Classification, Type of Body, GFS Sector Classifi…, Materiality, Established By / Un…

## g0393（1 列）
- 見出し：Portfolio
- 例1 値：Climate Change, Energy, the Environment… | Finance | Climate Change, Energy, the Environment… | Industry, Science and Resources | Agriculture, Fisheries and Forestry
  - 同じ表の列：Id, Portfolio Dept?, Title, Classification, Type of Body, GFS Sector Classifi…, Materiality, Established By / Un…

## g0394（1 列）
- 見出し：Classification
- 例1 値：A. Primary body | D. Other governance relationship | D. Other governance relationship | C. Secondary non-statutory structure | D. Other governance relationship
  - 同じ表の列：Id, Portfolio Dept?, Title, Portfolio, Type of Body, GFS Sector Classifi…, Materiality, Established By / Un…

## g0395（1 列）
- 見出し：Type of Body
- 例1 値：F. Non-statutory advisory structure | L. Joint ventures, partnerships and int… | M. Subsidiaries of corporate Commonweal… | A. Non-corporate Commonwealth entity | L. Joint ventures, partnerships and int…
  - 同じ表の列：Id, Portfolio Dept?, Title, Portfolio, Classification, GFS Sector Classifi…, Materiality, Established By / Un…

## g0396（1 列）
- 見出し：GFS Sector Classification
- 例1 値：GGS | GGS | GGS | GGS | GGS
  - 同じ表の列：Id, Portfolio Dept?, Title, Portfolio, Classification, Type of Body, Materiality, Established By / Un…

## g0397（1 列）
- 見出し：Materiality
- 例1 値：Small | Small | Small | Material | Small
  - 同じ表の列：Id, Portfolio Dept?, Title, Portfolio, Classification, Type of Body, GFS Sector Classifi…, Established By / Un…

## g0398（1 列）
- 見出し：Established By / Under
- 例1 値：Act / Regulation | Principal Body / Management Board / Sen… | Principal Body / Management Board / Sen… | Act / Regulation | Act / Regulation
  - 同じ表の列：Id, Portfolio Dept?, Title, Portfolio, Classification, Type of Body, GFS Sector Classifi…, Materiality

## g0399（1 列）
- 見出し：Established by/Under More Info
- 例1 値：National Environmental Biosecurity Resp… | Data Availability and Transparency Act … | Public Governance, Performance and Acco… | Aboriginal Land Rights (Northern Territ… | Public Service Act 1999 - Order to Esta…
  - 同じ表の列：Id, Portfolio Dept?, Title, Portfolio, Classification, Type of Body, GFS Sector Classifi…, Materiality

## g0400（1 列）
- 見出し：SA1_MAIN16
- 例1 値：10102100805 | 10104102007 | 10201104204 | 10201104044 | 10106154233
  - 同じ表の列：SA1_7DIG16, State, MMM2019

## g0401（1 列）
- 見出し：SA1_7DIG16
- 例1 値：1102001 | 1101614 | 1102712 | 1104008 | 1154235
  - 同じ表の列：SA1_MAIN16, State, MMM2019

## g0402（1 列）
- 見出し：State
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：SA1_MAIN16, SA1_7DIG16, MMM2019

## g0403（1 列）
- 見出し：MMM2019
- 例1 値：1 | 1 | 1 | 1 | 4
  - 同じ表の列：SA1_MAIN16, SA1_7DIG16, State

## g0404（1 列）
- 見出し：ASBESTOS CEMENT CLADDING (PANEL FRAME)
- 例1 値：34.19 | 32.21 | 29.0 | 30.0 | 32.67
  - 同じ表の列：Suburb, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, FIBRE CEMENT CLADDI…, FIBRE CEMENT CLADDI…, INSULATED CONCRETE …, MASONRY VENEER (PAN…, MASONRY VENEER (STE…

## g0405（1 列）
- 見出し：ASBESTOS CEMENT CLADDING (STEEL FRAME)
- 例1 値：33.0 | 31.37 | 20.0 | 29.5 | 46.0
  - 同じ表の列：Suburb, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, FIBRE CEMENT CLADDI…, FIBRE CEMENT CLADDI…, INSULATED CONCRETE …, MASONRY VENEER (PAN…, MASONRY VENEER (STE…

## g0406（1 列）
- 見出し：ASBESTOS CEMENT CLADDING (TIMBER FRAME)
- 例1 値：56.0 | 43.75 | 38.0 | 43.72 | 51.0
  - 同じ表の列：Suburb, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, FIBRE CEMENT CLADDI…, FIBRE CEMENT CLADDI…, INSULATED CONCRETE …, MASONRY VENEER (PAN…, MASONRY VENEER (STE…

## g0407（1 列）
- 見出し：FIBRE CEMENT CLADDING ON STEEL FRAME
- 例1 値：10.0 | 53.5 | 17.5 | 8.0 | 13.33
  - 同じ表の列：Suburb, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, FIBRE CEMENT CLADDI…, INSULATED CONCRETE …, MASONRY VENEER (PAN…, MASONRY VENEER (STE…

## g0408（1 列）
- 見出し：FIBRE CEMENT CLADDING ON TIMBER FRAME
- 例1 値：38.0 | 48.0 | 53.0 | 58.0 | 38.0
  - 同じ表の列：Suburb, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, FIBRE CEMENT CLADDI…, INSULATED CONCRETE …, MASONRY VENEER (PAN…, MASONRY VENEER (STE…

## g0409（1 列）
- 見出し：INSULATED CONCRETE FORM
- 例1 値：5.5 | 5.0 | 3.85 | 5.0 | 5.0
  - 同じ表の列：Suburb, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, FIBRE CEMENT CLADDI…, FIBRE CEMENT CLADDI…, MASONRY VENEER (PAN…, MASONRY VENEER (STE…

## g0410（1 列）
- 見出し：MASONRY VENEER (PANEL FRAME)
- 例1 値：57.0 | 44.0 | 12.0 | 35.0 | 51.0
  - 同じ表の列：Suburb, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, FIBRE CEMENT CLADDI…, FIBRE CEMENT CLADDI…, INSULATED CONCRETE …, MASONRY VENEER (STE…

## g0411（1 列）
- 見出し：MASONRY VENEER (STEEL FRAME)
- 例1 値：7.0 | 17.34 | 29.01 | 10.75 | 12.6
  - 同じ表の列：Suburb, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, FIBRE CEMENT CLADDI…, FIBRE CEMENT CLADDI…, INSULATED CONCRETE …, MASONRY VENEER (PAN…

## g0412（1 列）
- 見出し：MASONRY VENEER (TIMBER FRAME)
- 例1 値：29.64 | 30.5 | 27.2 | 55.67 | 39.5
  - 同じ表の列：Suburb, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, ASBESTOS CEMENT CLA…, FIBRE CEMENT CLADDI…, FIBRE CEMENT CLADDI…, INSULATED CONCRETE …, MASONRY VENEER (PAN…

## g0413（1 列）
- 見出し：Year of Whistleblower Disclosure
- 例1 値：2014-15 | 2013-14 | 2018-19 | 2017-18 | 2012-13
  - 同じ表の列：Quantity

## g0414（1 列）
- 見出し：Quantity
- 例1 値：0 | 0 | 2 | 1 | 0
  - 同じ表の列：Year of Whistleblow…

## g0415（1 列）
- 見出し：University
- 例1 値：University of South Australia | Edith Cowan University (ECU) | Curtin University | University of New South Wales (UNSW) | James Cook University (JCU)
  - 同じ表の列：State, Centre/Precinct, Investment & main p…, Focus sectors, Interesting facts, Status

## g0416（1 列）
- 見出し：Centre/Precinct
- 例1 値：CenWest Innovate | John de Laeter Centre | The Bays | Monash Technology Precinct | Techport Australia
  - 同じ表の列：State, University, Investment & main p…, Focus sectors, Interesting facts, Status

## g0417（1 列）
- 見出し：Investment & main partners
- 例1 値：WaterCorp is owned by the West Australi… | A taskforce, headed by Jobs for NSW cha… | CSI UWA is part of a national collabora… | As a not-for-profit organisation, the m… | A major initiative within the QEII Grea…
  - 同じ表の列：State, University, Centre/Precinct, Focus sectors, Interesting facts, Status

## g0418（1 列）
- 見出し：Focus sectors
- 例1 値：Defence and aerospace. | Advanced manufacturing, hardware, deep-… | Multidisciplinary centre with scope for… | Ophthalmology. | Health and manufacturing.
  - 同じ表の列：State, University, Centre/Precinct, Investment & main p…, Interesting facts, Status

## g0419（1 列）
- 見出し：Interesting facts
- 例1 値：NACOG is a hub for training and educati… | The Cairns Innovation Centre will foste… | CSI UWA hosts the annual Social Impact … | Flexible, collaborative co-working and … | The centre hosts over $25 million in wo…
  - 同じ表の列：State, University, Centre/Precinct, Investment & main p…, Focus sectors, Status

## g0420（1 列）
- 見出し：Year
- 例1 値：2013/14 | 2014/15 | 2012/13 | 2016/17 | 2015/16
  - 同じ表の列：Category/nature of …, Number of instances

## g0421（1 列）
- 見出し：Category/nature of fraud
- 例1 値：No Fraud | Allegation of fraud involving misapprop… | No Fraud | No Fraud | No Fraud
  - 同じ表の列：Year, Number of instances

## g0422（1 列）
- 見出し：Number of instances
- 例1 値：0 | 1 | 0 | 0 | 0
  - 同じ表の列：Year, Category/nature of …

## g0423（1 列）
- 見出し：Year
- 例1 値：Note: Disclosure of public interest inf… | 2023-2024 | 2020-2021 | 2022-2023 | 2021-2022
  - 同じ表の列：Number

## g0424（1 列）
- 見出し：CD_MAKE_VEH1
- 例1 値：ABARTH | ABARTH | ABARTH | ABARTH | ABARTH
  - 同じ表の列：CD_CLASS_VEH, NB_YEAR_MFC_VEH, CD_CL_FUEL_ENG, TOTAL1

## g0425（1 列）
- 見出し：CD_CLASS_VEH
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：CD_MAKE_VEH1, NB_YEAR_MFC_VEH, CD_CL_FUEL_ENG, TOTAL1

## g0426（1 列）
- 見出し：NB_YEAR_MFC_VEH
- 例1 値：2021 | 2017 | 2020 | 2017 | 2019
  - 同じ表の列：CD_MAKE_VEH1, CD_CLASS_VEH, CD_CL_FUEL_ENG, TOTAL1

## g0427（1 列）
- 見出し：CD_CL_FUEL_ENG
- 例1 値：P | D | D | D | D
  - 同じ表の列：CD_MAKE_VEH1, CD_CLASS_VEH, NB_YEAR_MFC_VEH, TOTAL1

## g0428（1 列）
- 見出し：TOTAL1
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：CD_MAKE_VEH1, CD_CLASS_VEH, NB_YEAR_MFC_VEH, CD_CL_FUEL_ENG

## g0429（1 列）
- 見出し：Trade type
- 例1 値：Total Exports | Total Exports | Total Exports | Total Exports | Total Exports
  - 同じ表の列：Year, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0430（1 列）
- 見出し：State
- 例1 値：NSW | Confidential | SA | WA | Re-exports
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0431（1 列）
- 見出し：TRIEC 1 digit
- 例1 値：3 Other goods | 3 Other goods | 3 Other goods | 3 Other goods | 3 Other goods
  - 同じ表の列：Year, Trade type, State, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0432（1 列）
- 見出し：TRIEC 2 digit
- 例1 値：30 Other goods | 30 Other goods | 30 Other goods | 30 Other goods | 30 Other goods
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0433（1 列）
- 見出し：TRIEC 3 digit
- 例1 値：304 Other goods - Confidential trade | 304 Other goods - Confidential trade | 304 Other goods - Confidential trade | 304 Other goods - Confidential trade | 304 Other goods - Confidential trade
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0434（1 列）
- 見出し：TRIEC 4 digit
- 例1 値：3041 Confidential trade | 3041 Confidential trade | 3019 Miscellaneous merchandise trade nes | 3019 Miscellaneous merchandise trade nes | 3019 Miscellaneous merchandise trade nes
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, Partner Country, Geographic level 1

## g0435（1 列）
- 見出し：Partner Country
- 例1 値：Cook Islands | Unknown | United Kingdom | Philippines | Indonesia
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Geographic level 1

## g0436（1 列）
- 見出し：Geographic level 1
- 例1 値：Asia | Asia | Oceania & Antarctica | Africa | Oceania & Antarctica
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country

## g0437（1 列）
- 見出し：Geographic level 2
- 例1 値：East Asia | Other | Pacific Islands | Northern & Western Europe | Eastern & Southern Europe
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country

## g0438（3 列）
- 見出し：Town
- 例1 値：Lara | Murchison | Beechworth | West Melbourne | Lara
  - 同じ表の列：Operational capacit…, Security, Map Ref, Profile, Link for further in…
- 例2 値：ST ARNAUD | INDENTED HEAD | REDBANK | CONNEWARRE | ANAKIE
  - 同じ表の列：Corporation, Restriction, Date Effective

## g0439（1 列）
- 見出し：Operational capacity*
- 例1 値：845 | 306 | 54 | 390 | 25
  - 同じ表の列：Town, Security, Map Ref, Profile, Link for further in…

## g0440（1 列）
- 見出し：Security
- 例1 値：Medium/Minimum | Maximum | Minimum | Maximum | Maximum
  - 同じ表の列：Town, Operational capacit…, Map Ref, Profile, Link for further in…

## g0441（1 列）
- 見出し：Map Ref
- 例1 値：56, H6 or 227, N7 | Pg.421, K1 | Map 59, E3 or Map 287, U9 | Map 46, E2 | Map 2E, J2
  - 同じ表の列：Town, Operational capacit…, Security, Profile, Link for further in…

## g0442（1 列）
- 見出し：Profile
- 例1 値：HM Dhurringile Prison is a pre-release … | HM Prison Langi Kal Kal houses minimum … | HM Prison Tarrengower is a minimum secu… | Fulham Correctional Centre accommodates… | The facility provides remand, sentenced…
  - 同じ表の列：Town, Operational capacit…, Security, Map Ref, Link for further in…

## g0443（1 列）
- 見出し：Link for further info
- 例1 値：http://www.justice.vic.gov.au/wps/wcm/c… | http://www.justice.vic.gov.au/wps/wcm/c… | http://www.justice.vic.gov.au/wps/wcm/c… | http://www.justice.vic.gov.au/wps/wcm/c… | http://www.justice.vic.gov.au/wps/wcm/c…
  - 同じ表の列：Town, Operational capacit…, Security, Map Ref, Profile

## g0444（1 列）
- 見出し：Business Category
- 例1 値：Canoe/Kayak Club | Canoe/Kayak Club | Canoe/Kayak Club | Surfing Lessons | Canoe/Kayak Club,Recreation Group
  - 同じ表の列：Suburb, State, LGA, Region

## g0445（1 列）
- 見出し：LGA
- 例1 値：Maribyrnong (C) | Surf Coast (S) | Moira | South Gippsland | Greater Geelong
  - 同じ表の列：Suburb, State, Business Category, Region

## g0446（1 列）
- 見出し：Region
- 例1 値：North and West Metropolitan Region | North and West Metropolitan Region | Eastern Metropolitan Region | North and West Metropolitan Region | North and West Metropolitan Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0447（1 列）
- 見出し：Corporation
- 例1 値：Grampians Wimmera Mallee Water | Lower Murray Water | Grampians Wimmera Mallee Water | Barwon Water | Coliban Water
  - 同じ表の列：Town, Restriction, Date Effective

## g0448（1 列）
- 見出し：Restriction
- 例1 値：Stage 2 | Stage 3 | Stage 3 | Stage 1 | Stage 1
  - 同じ表の列：Corporation, Town, Date Effective

## g0449（1 列）
- 見出し：Date Effective
- 例1 値：27/10/2007 | 1/11/2009 | 9/12/2009 | 12/11/2007 | 30/03/2009
  - 同じ表の列：Corporation, Town, Restriction

## g0450（1 列）
- 見出し：id
- 例1 値：Typical_APS_Test_Lead_APS6 | Typical_APS_Test_Manager_EL1 | Typical_APS_User_Research_Recruiter_APS… | Typical_APS_Lead_Content_Designer_EL1 | Typical_APS_Content_Writer_APS4_APS5
  - 同じ表の列：job_family, job_family_function, job_family_role, aps_job_code, profile_link, demand, interests, learning_link

## g0451（1 列）
- 見出し：job_family
- 例1 値：Data and Research | ICT and Digital Solutions | Portfolio, Program and Project Manageme… | Information and Knowledge Management | Intelligence
  - 同じ表の列：id, job_family_function, job_family_role, aps_job_code, profile_link, demand, interests, learning_link

## g0452（1 列）
- 見出し：job_family_function
- 例1 値：Security | Solutions Implementation | Solutions Implementation | Security | Security
  - 同じ表の列：id, job_family, job_family_role, aps_job_code, profile_link, demand, interests, learning_link

## g0453（1 列）
- 見出し：job_family_role
- 例1 値：Cyber Security Tester | Cyber Security Operations Specialist | Service Manager | Cyber Security Tester | IT Architect
  - 同じ表の列：id, job_family, job_family_function, aps_job_code, profile_link, demand, interests, learning_link

## g0454（1 列）
- 見出し：aps_job_code
- 例1 値：260304 | 170510 | 150501 | 170510 | 200414
  - 同じ表の列：id, job_family, job_family_function, job_family_role, profile_link, demand, interests, learning_link

## g0455（1 列）
- 見出し：profile_link
- 例1 値：https://www.apsc.gov.au/sites/default/f… | https://www.apsprofessions.gov.au/day-l… | https://www.apsprofessions.gov.au/day-l… | https://www.apsprofessions.gov.au/day-l… | https://www.apsc.gov.au/sites/default/f…
  - 同じ表の列：id, job_family, job_family_function, job_family_role, aps_job_code, demand, interests, learning_link

## g0456（1 列）
- 見出し：demand
- 例1 値：0.8 | 0.86 | 0.97 | 0.75 | 0.9
  - 同じ表の列：id, job_family, job_family_function, job_family_role, aps_job_code, profile_link, interests, learning_link

## g0457（1 列）
- 見出し：interests
- 例1 値：Data,Management | Pega,Development,Programming | Cyber Security | Testing,Cyber Security | Analysis,Data,Problem solving,Visualisa…
  - 同じ表の列：id, job_family, job_family_function, job_family_role, aps_job_code, profile_link, demand, learning_link

## g0458（1 列）
- 見出し：learning_link
- 例1 値：https://lisahowdin.github.io/Learnings/… | https://lisahowdin.github.io/Learnings/… | https://www.dta.gov.au/help-and-advice/… | https://www.apsprofessions.gov.au/day-l… | https://www.dta.gov.au/help-and-advice/…
  - 同じ表の列：id, job_family, job_family_function, job_family_role, aps_job_code, profile_link, demand, interests

## g0459（1 列）
- 見出し：discipline
- 例1 値：Business Analysis | Visual Communication Design | Robotic Process Automation (RPA) Design | Data Management | Operations Coordination
  - 同じ表の列：id, job_family, job_family_function, job_family_role, aps_job_code, profile_link, demand, interests

## g0460（1 列）
- 見出し：Workplace injury claims
- 例1 値：Work health and safety regulations | Income support payments: gross ($) | **before third party recovery | Significant injuries (where lost time e… | Total gross workers compensation expend…
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0461（1 列）
- 見出し：2024-25
- 例1 値：0 | $0 | 0 | 0 | 0
  - 同じ表の列：Workplace injury cl…, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0462（1 列）
- 見出し：2023-24
- 例1 値：0 | 0 | $0 | 0 | 0
  - 同じ表の列：Workplace injury cl…, 2024-25, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0463（1 列）
- 見出し：2022-23
- 例1 値：$35,215 | $771 | 0 | 1 | 0
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0464（1 列）
- 見出し：2021-22
- 例1 値：0 | $134,599 | 0 | 0 | 1
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2020-21, 2019-20, 2018-19, 2017-18

## g0465（3 列）
- 見出し：2019-20
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2018-19, 2017-18
- 例2 値：268100078 | 114278680 | 1833128037 | 1169380957 | 111664222
  - 同じ表の列：State/Territory, Month, 2015-16, 2016-17, 2017-18, 2018-19, 2020-21, 2021-22

## g0466（3 列）
- 見出し：2018-19
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2017-18
- 例2 値：123675592 | 831340501 | 895917018 | 328129819 | 639976128
  - 同じ表の列：State/Territory, Month, 2015-16, 2016-17, 2017-18, 2019-20, 2020-21, 2021-22

## g0467（3 列）
- 見出し：2017-18
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19
- 例2 値：279225882 | 306354990 | 1347520688 | 474070385 | 95360786
  - 同じ表の列：State/Territory, Month, 2015-16, 2016-17, 2018-19, 2019-20, 2020-21, 2021-22

## g0468（3 列）
- 見出し：2016-17
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Workplace injury cl…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19
- 例2 値：911656905 | 713785165 | 269001065 | 109291802 | 91455878
  - 同じ表の列：State/Territory, Month, 2015-16, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0469（1 列）
- 見出し：Site
- 例1 値：abellpoint | abellpoint | abellpoint | abellpoint | abellpoint
  - 同じ表の列：Seconds, DateTime, Water Level, Prediction, Residual

## g0470（1 列）
- 見出し：DateTime
- 例1 値：2026-10-22T11:20 | 2026-10-18T17:40 | 2026-10-21T23:10 | 2026-10-23T06:20 | 2026-10-23T16:10
  - 同じ表の列：Site, Seconds, Water Level, Prediction, Residual

## g0471（1 列）
- 見出し：Water Level
- 例1 値：1.408 | 2.343 | 1.498 | 1.644 | 2.719
  - 同じ表の列：Site, Seconds, DateTime, Prediction, Residual

## g0472（1 列）
- 見出し：Prediction
- 例1 値：2.122 | 1.975 | 1.675 | 2.054 | 2.957
  - 同じ表の列：Site, Seconds, DateTime, Water Level, Residual

## g0473（1 列）
- 見出し：Residual
- 例1 値：0.152 | 0.096 | 0.133 | 0.159 | 0.156
  - 同じ表の列：Site, Seconds, DateTime, Water Level, Prediction

## g0474（1 列）
- 見出し：Instances
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year

## g0475（1 列）
- 見出し：Complex_Type
- 例1 値：Hall Reserve | Hall Reserve | Hall Reserve | Recreation Reserve | Public Hall
  - 同じ表の列：Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs, Amenities

## g0476（1 列）
- 見出し：Facility_Type
- 例1 値：Hall | Hall | Hall | Hall | Hall
  - 同じ表の列：Complex_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs, Amenities

## g0477（1 列）
- 見出し：Bookable_Item
- 例1 値：Bannockburn Cultural Centre Hall | Berringa Public Hall | Cape Clear Recreation Reserve Hall | Teesdale Recreation Reserve Public Toil… | Barunah Park Public Hall
  - 同じ表の列：Complex_Type, Facility_Type, Assessment_No, Number, Locality, Post_Code, Home_Clubs, Amenities

## g0478（1 列）
- 見出し：Assessment_No
- 例1 値：41400230 | 41400033 | 53181380 | 54005009 | 66249110
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Number, Locality, Post_Code, Home_Clubs, Amenities

## g0479（1 列）
- 見出し：Post_Code
- 例1 値：3329 | 3352 | 3218 | 3333 | 3321
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Home_Clubs, Amenities

## g0480（1 列）
- 見出し：Home_Clubs
- 例1 値：NIL
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Amenities

## 答えの雛形

```
g0361	
g0362	
g0363	
g0364	
g0365	
g0366	
g0367	
g0368	
g0369	
g0370	
g0371	
g0372	
g0373	
g0374	
g0375	
g0376	
g0377	
g0378	
g0379	
g0380	
g0381	
g0382	
g0383	
g0384	
g0385	
g0386	
g0387	
g0388	
g0389	
g0390	
g0391	
g0392	
g0393	
g0394	
g0395	
g0396	
g0397	
g0398	
g0399	
g0400	
g0401	
g0402	
g0403	
g0404	
g0405	
g0406	
g0407	
g0408	
g0409	
g0410	
g0411	
g0412	
g0413	
g0414	
g0415	
g0416	
g0417	
g0418	
g0419	
g0420	
g0421	
g0422	
g0423	
g0424	
g0425	
g0426	
g0427	
g0428	
g0429	
g0430	
g0431	
g0432	
g0433	
g0434	
g0435	
g0436	
g0437	
g0438	
g0439	
g0440	
g0441	
g0442	
g0443	
g0444	
g0445	
g0446	
g0447	
g0448	
g0449	
g0450	
g0451	
g0452	
g0453	
g0454	
g0455	
g0456	
g0457	
g0458	
g0459	
g0460	
g0461	
g0462	
g0463	
g0464	
g0465	
g0466	
g0467	
g0468	
g0469	
g0470	
g0471	
g0472	
g0473	
g0474	
g0475	
g0476	
g0477	
g0478	
g0479	
g0480	
```
