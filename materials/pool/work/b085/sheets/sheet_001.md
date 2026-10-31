# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Departmental Family
- 例1 値：Cabinet Office | Cabinet Office | Cabinet Office | Cabinet Office | Cabinet Office
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount 」

## g0002（1 列）
- 見出し：Entity
- 例1 値：Capacity Builders | Capacity Builders | Capacity Builders | CABINET OFFICE | Capacity Builders
  - 同じ表の列：Departmental Family, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount 」

## g0003（1 列）
- 見出し：Date
- 例1 値：22/04/2010 | 30/04/2010 | 14/04/2010 | 01/04/2010 | 12/04/2010
  - 同じ表の列：Departmental Family, Entity, Expense Type, Expense Area, Supplier, Transaction Number, Amount 」

## g0004（1 列）
- 見出し：Expense Type
- 例1 値：Consultancy | Travel, Subsistence and Hospitality | Grant | Consultancy | Other Staff Related Costs
  - 同じ表の列：Departmental Family, Entity, Date, Expense Area, Supplier, Transaction Number, Amount 」

## g0005（1 列）
- 見出し：Expense Area
- 例1 値：ESTATE MANAGEMENT | CIVIL SERVICE PENSIONS | ESTATE MANAGEMENT | OFFICE FOR CIVIL SOCIETY | ESTATE MANAGEMENT
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Supplier, Transaction Number, Amount 」

## g0006（1 列）
- 見出し：Supplier
- 例1 値：CENTRAL OFFICE OF INFORMATION | LEXISNEXIS | CENTRAL OFFICE OF INFORMATION | DWP NORCROSS | MENTER
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount 」

## g0007（1 列）
- 見出し：Transaction Number
- 例1 値：3000009786 | 2475 | 2018 | 3000009392 | 3000009789
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Expense Area, Supplier, Amount 」

## g0008（1 列）
- 見出し：Amount 」
- 例1 値：29,334.50 | 34,212.50 | 31,695.04 | 32,820.00 | 41,433.61
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number

## g0009（1 列）
- 見出し：Transaction Reference Number
- 例1 値：1449885592 | 1510996104 | 1485953683 | 1482553708 | 1474192970
  - 同じ表の列：Posting Date, Final Transaction A…

## g0010（1 列）
- 見出し：Posting Date
- 例1 値：06/04/2011 | 12/05/2011 | 06/06/2011 | 09/06/2011 | 04/04/2011
  - 同じ表の列：Transaction Referen…, Final Transaction A…

## g0011（1 列）
- 見出し：Final Transaction Amount
- 例1 値：900.84 | 1,421.76 | 832.08 | 1,895.07 | 1,284.00
  - 同じ表の列：Transaction Referen…, Posting Date

## g0012（1 列）
- 見出し：GMPP ID Number
- 例1 値：Departmental narrative on schedule, inc… | Financial Year Baseline (£m) (including… | Financial Year Variance (%) | Project Name | Annual Report Category
  - 同じ表の列：BEIS_0004_1920-Q2, DECC_0005_1112-Q1, BEIS_0001_1617-Q2, BIS_0015_1516-Q1, DECC_0013_1213-Q1, BIS_0014_1415-Q3, DECC_0010_1112-Q1, BEIS_0003_1819-Q2

## g0013（1 列）
- 見出し：BEIS_0004_1920-Q2
- 例1 値：01/11/2018 | £32.24 | Budget variance less than 5% | Amber | The baseline Whole Life Cost at Q2 1920…
  - 同じ表の列：GMPP ID Number, DECC_0005_1112-Q1, BEIS_0001_1617-Q2, BIS_0015_1516-Q1, DECC_0013_1213-Q1, BIS_0014_1415-Q3, DECC_0010_1112-Q1, BEIS_0003_1819-Q2

## g0014（1 列）
- 見出し：DECC_0005_1112-Q1
- 例1 値：The scheduled baseline project end date… | 30/06/2008 | BEIS | 31/12/2040 | Geological Disposal Facility Programme …
  - 同じ表の列：GMPP ID Number, BEIS_0004_1920-Q2, BEIS_0001_1617-Q2, BIS_0015_1516-Q1, DECC_0013_1213-Q1, BIS_0014_1415-Q3, DECC_0010_1112-Q1, BEIS_0003_1819-Q2

## g0015（1 列）
- 見出し：BEIS_0001_1617-Q2
- 例1 値：-23% | BEIS | 25/11/2015 | £86.60 | Amber
  - 同じ表の列：GMPP ID Number, BEIS_0004_1920-Q2, DECC_0005_1112-Q1, BIS_0015_1516-Q1, DECC_0013_1213-Q1, BIS_0014_1415-Q3, DECC_0010_1112-Q1, BEIS_0003_1819-Q2

## g0016（1 列）
- 見出し：BIS_0015_1516-Q1
- 例1 値：BEIS | The Programme will deliver a single Loc… | The baseline Whole Life Cost at Q2 1920… | £7.00 | The scheduled baseline project end date…
  - 同じ表の列：GMPP ID Number, BEIS_0004_1920-Q2, DECC_0005_1112-Q1, BEIS_0001_1617-Q2, DECC_0013_1213-Q1, BIS_0014_1415-Q3, DECC_0010_1112-Q1, BEIS_0003_1819-Q2

## g0017（1 列）
- 見出し：DECC_0013_1213-Q1
- 例1 値：£192.00 | -3% | BEIS | 31/08/2019 | Amber
  - 同じ表の列：GMPP ID Number, BEIS_0004_1920-Q2, DECC_0005_1112-Q1, BEIS_0001_1617-Q2, BIS_0015_1516-Q1, BIS_0014_1415-Q3, DECC_0010_1112-Q1, BEIS_0003_1819-Q2

## g0018（1 列）
- 見出し：BIS_0014_1415-Q3
- 例1 値：£64.50 | BEIS | The 19/20 in-year baseline / forecast v… | £68.00 | The scheduled baseline project end date…
  - 同じ表の列：GMPP ID Number, BEIS_0004_1920-Q2, DECC_0005_1112-Q1, BEIS_0001_1617-Q2, BIS_0015_1516-Q1, DECC_0013_1213-Q1, DECC_0010_1112-Q1, BEIS_0003_1819-Q2

## g0019（1 列）
- 見出し：DECC_0010_1112-Q1
- 例1 値：The IPA Delivery Confidence Assessment … | 0% | Smart Metering Implementation Programme | The scheduled baseline project end date… | 31/12/2024
  - 同じ表の列：GMPP ID Number, BEIS_0004_1920-Q2, DECC_0005_1112-Q1, BEIS_0001_1617-Q2, BIS_0015_1516-Q1, DECC_0013_1213-Q1, BIS_0014_1415-Q3, BEIS_0003_1819-Q2

## g0020（1 列）
- 見出し：BEIS_0003_1819-Q2
- 例1 値：The IPA Delivery Confidence Assessment … | 01/09/2019 | Government Transformation and Service D… | The baseline Whole Life Cost at Q2 1920… | £3.00
  - 同じ表の列：GMPP ID Number, BEIS_0004_1920-Q2, DECC_0005_1112-Q1, BEIS_0001_1617-Q2, BIS_0015_1516-Q1, DECC_0013_1213-Q1, BIS_0014_1415-Q3, DECC_0010_1112-Q1

## g0021（1 列）
- 見出し：TRANSACTION TYPE
- 例1 値：Lodged GPC | Lodged GPC | Individual GPC | Lodged GPC | Lodged GPC
  - 同じ表の列：TRANSACTION DATE, TRANSACTION REFEREN…, MERCHANT, TOTAL

## g0022（1 列）
- 見出し：TRANSACTION DATE
- 例1 値：05/12/2012 | 12/12/2012 | 27/12/2012 | 28/12/2012 | 13/12/2012
  - 同じ表の列：TRANSACTION TYPE, TRANSACTION REFEREN…, MERCHANT, TOTAL

## g0023（1 列）
- 見出し：TRANSACTION REFERENCE
- 例1 値：PCCL1649911 | PCCL1648781 | Statement 5 Jan 2013 | 396134702 | 400101727
  - 同じ表の列：TRANSACTION TYPE, TRANSACTION DATE, MERCHANT, TOTAL

## g0024（1 列）
- 見出し：MERCHANT
- 例1 値：Hogg Robinson Group Ltd | ONLINE ERGONOMICS | Hogg Robinson Group Ltd | ONLINE ERGONOMICS | EC GROUP
  - 同じ表の列：TRANSACTION TYPE, TRANSACTION DATE, TRANSACTION REFEREN…, TOTAL

## g0025（1 列）
- 見出し：TOTAL
- 例1 値：515.35 | 2681.19 | -1646.19 | -1929.09 | 2312.10
  - 同じ表の列：TRANSACTION TYPE, TRANSACTION DATE, TRANSACTION REFEREN…, MERCHANT

## g0026（2 列）
- 見出し：Mode of Travel
- 例1 値：AIR | HOTEL | HOTEL | AIR | HOTEL
  - 同じ表の列：Date of Departure, Duration of Stay, Destination, City of Accommodati…, Class of Travel, Base Sales includin…
- 例2 値：Air | Rail | Air | Hotel | Air
  - 同じ表の列：Date of Departure, Duration of stay, Destination, City of accommodati…, Class of travel, Base Sales includin…, Comments

## g0027（2 列）
- 見出し：Date of Departure
- 例1 値：12/4/2013 | 11/13/2013 | 12/4/2013 | 10/27/2013 | 12/12/2013
  - 同じ表の列：Mode of Travel, Duration of Stay, Destination, City of Accommodati…, Class of Travel, Base Sales includin…
- 例2 値：15/05/2013 | 10/04/2013 | 21/05/2013 | 13/05/2013 | 15/04/2013
  - 同じ表の列：Mode of travel, Duration of stay, Destination, City of accommodati…, Class of travel, Base Sales includin…, Comments

## g0028（2 列）
- 見出し：Duration of Stay
- 例1 値：2 | 2 | 2 | 3 | 2
  - 同じ表の列：Mode of Travel, Date of Departure, Destination, City of Accommodati…, Class of Travel, Base Sales includin…
- 例2 値：11 | 6 | 3 | 1 | 6
  - 同じ表の列：Mode of travel, Date of Departure, Destination, City of accommodati…, Class of travel, Base Sales includin…, Comments

## g0029（1 列）
- 見出し：Destination
- 例1 値：Dallas Love | Austin Tx | Berlin Germa | Athens | Baltimore Md
  - 同じ表の列：Mode of Travel, Date of Departure, Duration of Stay, City of Accommodati…, Class of Travel, Base Sales includin…

## g0030（1 列）
- 見出し：City of Accommodation (if different to destination)
- 例1 値：BRUSSELS | BRUSSELS | BRUSSELS | Athens | BRUSSELS
  - 同じ表の列：Mode of Travel, Date of Departure, Duration of Stay, Destination, Class of Travel, Base Sales includin…

## g0031（1 列）
- 見出し：Class of Travel
- 例1 値：DISCOUNT BUSINESS | DISCOUNT BUSINESS | SECOND CLASS RAIL | DISCOUNT ECONOMY | ECONOMY
  - 同じ表の列：Mode of Travel, Date of Departure, Duration of Stay, Destination, City of Accommodati…, Base Sales includin…

## g0032（1 列）
- 見出し：Base Sales including Tax
- 例1 値：390 | 144 | 12 | 88 | 158
  - 同じ表の列：Mode of Travel, Date of Departure, Duration of Stay, Destination, City of Accommodati…, Class of Travel

## g0033（1 列）
- 見出し：RfR1: Eliminating poverty in poorer countries
- 例1 値：C: Bilateral Aid to the Rest of the Wor… | No Specific Pillar | RfR2: Conflict Prevention | Spending in Departmental Expenditure Li… | Resources (excluding capital grants)
  - 同じ表の列：3,815,040, 4,312,049, 5,003,799, 5,318,663

## g0034（1 列）
- 見出し：3,815,040
- 例1 値：- | 2007-08 | 9,558 | - | Outturn
  - 同じ表の列：RfR1: Eliminating p…, 4,312,049, 5,003,799, 5,318,663

## g0035（1 列）
- 見出し：4,312,049
- 例1 値：822,327 | - | 2008-09 | 876,174 | 239,346
  - 同じ表の列：RfR1: Eliminating p…, 3,815,040, 5,003,799, 5,318,663

## g0036（1 列）
- 見出し：5,003,799
- 例1 値：2013-14 | - | 13,631 | 4,624,050 | -
  - 同じ表の列：RfR1: Eliminating p…, 3,815,040, 4,312,049, 5,318,663

## g0037（1 列）
- 見出し：5,318,663
- 例1 値：74,315 | - | 867,205 | 191,114 | -
  - 同じ表の列：RfR1: Eliminating p…, 3,815,040, 4,312,049, 5,003,799

## g0038（1 列）
- 見出し：2008/09
- 例1 値：3 283 996 | 2 277 358 | 310 659 | 249 000 | 4 333 951
  - 同じ表の列：2009/10, 2010/11, 2011/12, 2012/13 1

## g0039（1 列）
- 見出し：2009/10
- 例1 値：486 273 | 6 628 999 | 1 424 089 | 234 398 | 3 958 263
  - 同じ表の列：2008/09, 2010/11, 2011/12, 2012/13 1

## g0040（1 列）
- 見出し：2010/11
- 例1 値：3 221 673 | 1 431 849 | 926 713 | 233 208 | 4 248 018
  - 同じ表の列：2008/09, 2009/10, 2011/12, 2012/13 1

## g0041（1 列）
- 見出し：2011/12
- 例1 値：220 352 | 8 949 587 | 3 461 684 | 434 462 | 7 682 191
  - 同じ表の列：2008/09, 2009/10, 2010/11, 2012/13 1

## g0042（1 列）
- 見出し：2012/13 1
- 例1 値：1 025 431 | 4 169 389 | 220 220 | 424 145 | 3 498 040
  - 同じ表の列：2008/09, 2009/10, 2010/11, 2011/12

## g0043（1 列）
- 見出し：Olympics Transport Programme
- 例1 値：24.862 | 24.607 | DfT | Green | 31/12/2012
  - 同じ表の列：Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Search & Rescue Hel…, Thameslink, Rail Refranchising …, M25 DBFO (Design, B…

## g0044（1 列）
- 見出し：Rail Refranchising Management Programme - East Coast
- 例1 値：Amber | 31/05/2013 | The Secretary of State is required to d… | 20/07/2009 | The franchise programme was paused in O…
  - 同じ表の列：Olympics Transport …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Search & Rescue Hel…, Thameslink, Rail Refranchising …, M25 DBFO (Design, B…

## g0045（1 列）
- 見出し：Rail Refranchising Management Programme - GA Long
- 例1 値：The Secretary of State is required to d… | 31/01/2015 | The franchise programme was paused in O… | Amber/Green | DfT
  - 同じ表の列：Olympics Transport …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Search & Rescue Hel…, Thameslink, Rail Refranchising …, M25 DBFO (Design, B…

## g0046（1 列）
- 見出し：Rail Refranchising Management Programme - Greater Anglia Sho
- 例1 値：Completed on schedule. | 01/06/2010 | The bases of the Budget and the Forecas… | -396.7769231 | DfT
  - 同じ表の列：Olympics Transport …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Search & Rescue Hel…, Thameslink, Rail Refranchising …, M25 DBFO (Design, B…

## g0047（1 列）
- 見出し：Rail Refranchising Management Programme - West Coast
- 例1 値：08/04/2014 | Red | The Secretary of State is required to d… | The franchise programme was paused in O… | DfT
  - 同じ表の列：Olympics Transport …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Search & Rescue Hel…, Thameslink, Rail Refranchising …, M25 DBFO (Design, B…

## g0048（1 列）
- 見出し：Search & Rescue Helicopters (SARH)
- 例1 値：Cross-departmental virtual team (DfT / … | Scheme is on target to deliver against … | To procure a contract for the provision… | 37 | 3286
  - 同じ表の列：Olympics Transport …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Thameslink, Rail Refranchising …, M25 DBFO (Design, B…

## g0049（1 列）
- 見出し：Thameslink
- 例1 値：01/12/2018 | In December 2012 the Department reached… | DfT | The Thameslink programme will dramatica… | 01/07/2005
  - 同じ表の列：Olympics Transport …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Search & Rescue Hel…, Rail Refranchising …, M25 DBFO (Design, B…

## g0050（1 列）
- 見出し：Rail Refranchising Management Programme- Thameslink, Souther
- 例1 値：The franchise programme was paused in O… | 30/10/2011 | The franchise programme was paused in O… | DfT | Amber/Red
  - 同じ表の列：Olympics Transport …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Search & Rescue Hel…, Thameslink, M25 DBFO (Design, B…

## g0051（1 列）
- 見出し：M25 DBFO (Design, Build, Finance and Operate)
- 例1 値：Green | 31/07/2013 | The key delivery milestones - the openi… | The whole life cost represents the Capi… | This project comprises two road widenin…
  - 同じ表の列：Olympics Transport …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Search & Rescue Hel…, Thameslink, Rail Refranchising …

## g0052（1 列）
- 見出し：Managed Motorways
- 例1 値：Amber/Green | The schemes are on track to deliver on … | Budgets up to 2014/15 reflect the SR10 … | 219.1875919 | 31/10/2011
  - 同じ表の列：Olympics Transport …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Rail Refranchising …, Search & Rescue Hel…, Thameslink, Rail Refranchising …

## g0053（1 列）
- 見出し：BENEFIT
- 例1 値：Assumed income | Severe Disability Premium | Assessed level of disability, Aged 18 a… | Couple (where both people qualify) | Single person
  - 同じ表の列：RATE, FREQUENCY, NOTES

## g0054（1 列）
- 見出し：RATE
- 例1 値：£65.62 | £136.78 or 90% of the individual's gros… | £112.55 | £108.30 | £56.65
  - 同じ表の列：BENEFIT, FREQUENCY, NOTES

## g0055（1 列）
- 見出し：FREQUENCY
- 例1 値：Weekly | Weekly | Weekly | Lump sum | Weekly
  - 同じ表の列：BENEFIT, RATE, NOTES

## g0056（1 列）
- 見出し：NOTES
- 例1 値：A higher rate may be paid where either … | The Winter Fuel Payment is an annual lu… | 70 per cent of the amount paid as charg… | For each £500, or part of £500, of capi… | A higher rate may be paid where either …
  - 同じ表の列：BENEFIT, RATE, FREQUENCY

## g0057（1 列）
- 見出し：Number of travellers
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Spend less tax, Ticket departure da…, Bileteral city pairs

## g0058（1 列）
- 見出し：Spend less tax
- 例1 値：」178.00 | 」509.82 | 」40.00 | 」170.00 | 」28.00
  - 同じ表の列：Number of travellers, Ticket departure da…, Bileteral city pairs

## g0059（1 列）
- 見出し：Ticket departure date
- 例1 値：05/05/2011 | 16/05/2011 | 06/06/2011 | 27/05/2011 | 31/05/2011
  - 同じ表の列：Number of travellers, Spend less tax, Bileteral city pairs

## g0060（1 列）
- 見出し：Bileteral city pairs
- 例1 値：GLASGOW/LONDON | MANCHESTER/NORWICH | EDINBURGH/LONDON | BELFAST/LONDON | BELFAST/LONDON
  - 同じ表の列：Number of travellers, Spend less tax, Ticket departure da…

## g0061（1 列）
- 見出し：Date
- 例1 値：31/03/2013 | 6 Feb 2013 | 01/02/13 | 24-26 Mar | 11-14 Mar 13
  - 同じ表の列：Destination, Purpose, Travel Air, Travel Rail, Taxi/Car, Accommodation/Meals, Other (Including Ho…, Total Cost (」)

## g0062（2 列）
- 見出し：Destination
- 例1 値：Tokyo | Cheltenham | London | Crawley | Oxford
  - 同じ表の列：Date, Purpose, Travel Air, Travel Rail, Taxi/Car, Accommodation/Meals, Other (Including Ho…, Total Cost (」)
- 例2 値：Lagos | Boston | Algiers | Poland | Cairo
  - 同じ表の列：Mode of travel, Date of Departure, Duration of stay, City of accommodati…, Class of travel, Base Sales includin…, Comments

## g0063（1 列）
- 見出し：Purpose
- 例1 値：Trilateral Meeting | Official visit to offices in Hanslope P… | Official Visit | Committee of Legal Advisers on Public I… | Official visit to British Embassies to …
  - 同じ表の列：Date, Destination, Travel Air, Travel Rail, Taxi/Car, Accommodation/Meals, Other (Including Ho…, Total Cost (」)

## g0064（1 列）
- 見出し：Travel Air
- 例1 値：」531.75 | 」7,942.20 | 」1,473.89 | 」623.15 | 」165.13
  - 同じ表の列：Date, Destination, Purpose, Travel Rail, Taxi/Car, Accommodation/Meals, Other (Including Ho…, Total Cost (」)

## g0065（1 列）
- 見出し：Travel Rail
- 例1 値：」23.50 | 」25.70 | 」26.50 | 」29.00 | 23.00
  - 同じ表の列：Date, Destination, Purpose, Travel Air, Taxi/Car, Accommodation/Meals, Other (Including Ho…, Total Cost (」)

## g0066（1 列）
- 見出し：Taxi/Car
- 例1 値：」271.20 | 」154.00 | 」21.00 | 」16.00 | 」55.18
  - 同じ表の列：Date, Destination, Purpose, Travel Air, Travel Rail, Accommodation/Meals, Other (Including Ho…, Total Cost (」)

## g0067（1 列）
- 見出し：Accommodation/Meals
- 例1 値：」406.03 | 」940.38 | 」220.00 | 」477.25 | 」985.75
  - 同じ表の列：Date, Destination, Purpose, Travel Air, Travel Rail, Taxi/Car, Other (Including Ho…, Total Cost (」)

## g0068（1 列）
- 見出し：Other (Including Hospitality Given)
- 例1 値：」225.66 | 」60.17 | 」147.77 | 」209.52
  - 同じ表の列：Date, Destination, Purpose, Travel Air, Travel Rail, Taxi/Car, Accommodation/Meals, Total Cost (」)

## g0069（1 列）
- 見出し：Total Cost (」)
- 例1 値：」23.16 | 」4,365.09 | 」271.00 | 」2,369.99 | 」3,751.56
  - 同じ表の列：Date, Destination, Purpose, Travel Air, Travel Rail, Taxi/Car, Accommodation/Meals, Other (Including Ho…

## g0070（1 列）
- 見出し：JAKARTA: New Embassy
- 例1 値：01/09/2014 | 11.06 | FCO | This project is for the construction of… | 11.06
  - 同じ表の列：TEL AVIV: Embassy U…, UKERP, Echo, Prism and Firecrest…, ABUJA: New Office a…

## g0071（1 列）
- 見出し：TEL AVIV: Embassy Upgrade
- 例1 値：FCO | 28/10/2009 | This project is to upgrade the structur… | 22 | Occupation of the Embassy from the deca…
  - 同じ表の列：JAKARTA: New Embassy, UKERP, Echo, Prism and Firecrest…, ABUJA: New Office a…

## g0072（1 列）
- 見出し：UKERP
- 例1 値：01/08/2016 | The FCO intends to maximise the efficie… | Amber | FCO | 1.44
  - 同じ表の列：JAKARTA: New Embassy, TEL AVIV: Embassy U…, Echo, Prism and Firecrest…, ABUJA: New Office a…

## g0073（1 列）
- 見出し：Echo
- 例1 値：29.96 | 32.07 | 179 | 31/12/2012 | Amber/Green
  - 同じ表の列：JAKARTA: New Embassy, TEL AVIV: Embassy U…, UKERP, Prism and Firecrest…, ABUJA: New Office a…

## g0074（1 列）
- 見出し：Prism and Firecrest Re-procurement Programme
- 例1 値：Amber | On schedule | FCO | 01/01/2011 | To renew the contracts for the followin…
  - 同じ表の列：JAKARTA: New Embassy, TEL AVIV: Embassy U…, UKERP, Echo, ABUJA: New Office a…

## g0075（1 列）
- 見出し：ABUJA: New Office and Residence
- 例1 値：Amber | To provide fit for purpose and secure o… | On schedule | 0.95 | 01/12/2010
  - 同じ表の列：JAKARTA: New Embassy, TEL AVIV: Embassy U…, UKERP, Echo, Prism and Firecrest…

## g0076（1 列）
- 見出し：Flights
- 例1 値：1 | 2 | 2 | 2 | 2
  - 同じ表の列：Fare Paid, Departure Date, Origin City, Destination Airport…, Destination City, Origin Country, Destination Country, Class

## g0077（1 列）
- 見出し：Fare Paid
- 例1 値：-214.28 | 258.17 | 102.7 | 145.03 | 108
  - 同じ表の列：Flights, Departure Date, Origin City, Destination Airport…, Destination City, Origin Country, Destination Country, Class

## g0078（1 列）
- 見出し：Departure Date
- 例1 値：08-Jun-11 | 13-Apr-11 | 12-Apr-11 | 28-Apr-11 | 17-May-11
  - 同じ表の列：Flights, Fare Paid, Origin City, Destination Airport…, Destination City, Origin Country, Destination Country, Class

## g0079（1 列）
- 見出し：Origin City
- 例1 値：LONDON | LONDON | GLASGOW | BELFAST | NEWCASTLE
  - 同じ表の列：Flights, Fare Paid, Departure Date, Destination Airport…, Destination City, Origin Country, Destination Country, Class

## g0080（1 列）
- 見出し：Destination Airport Code
- 例1 値：LCY | NQY | BFS | BHD | BHD
  - 同じ表の列：Flights, Fare Paid, Departure Date, Origin City, Destination City, Origin Country, Destination Country, Class

## g0081（1 列）
- 見出し：Destination City
- 例1 値：EAST MIDLANDS | OTTAWA | KUALA LUMPUR | LONDON | LONDON
  - 同じ表の列：Flights, Fare Paid, Departure Date, Origin City, Destination Airport…, Origin Country, Destination Country, Class

## g0082（1 列）
- 見出し：Origin Country
- 例1 値：UNITED KINGDOM | UNITED KINGDOM | UNITED KINGDOM | UNITED KINGDOM | UNITED KINGDOM
  - 同じ表の列：Flights, Fare Paid, Departure Date, Origin City, Destination Airport…, Destination City, Destination Country, Class

## g0083（1 列）
- 見出し：Destination Country
- 例1 値：UNITED KINGDOM | UNITED KINGDOM | UNITED KINGDOM | UNITED KINGDOM | UNITED KINGDOM
  - 同じ表の列：Flights, Fare Paid, Departure Date, Origin City, Destination Airport…, Destination City, Origin Country, Class

## g0084（1 列）
- 見出し：Class
- 例1 値：Economy | Economy | Economy | Economy | Economy
  - 同じ表の列：Flights, Fare Paid, Departure Date, Origin City, Destination Airport…, Destination City, Origin Country, Destination Country

## g0085（1 列）
- 見出し：Trip Type
- 例1 値：Domestic | Domestic | Domestic | Domestic | Domestic
  - 同じ表の列：Flights, Fare Paid, Departure Date, Origin City, Destination Airport…, Destination City, Origin Country, Destination Country

## g0086（1 列）
- 見出し：Main department
- 例1 値：Home Office | Home Office | Home Office
  - 同じ表の列：Organisation, Delegated grades on…, SCS on standard con…, Information for SCS…, Comments

## g0087（1 列）
- 見出し：Organisation
- 例1 値：Identity & Passport Service | Criminal Records Bureau | Home Office and UKBA
  - 同じ表の列：Main department, Delegated grades on…, SCS on standard con…, Information for SCS…, Comments

## g0088（2 列）
- 見出し：Delegated grades only
- 例1 値：」18,447,589 | 」1,140,849,332 | 」106,401,743 | Annual Paybill (delegated grades for fi… | 」1,016,000,000
  - 同じ表の列：Main department, Organisation, SCS on standard con…, Information for SCS…, Comments
- 例2 値：Annual Paybill (delegated grades for fi… | 」90,350,000 | 」1,092,306,465 | 」185,300,000 | 」15,241,226
  - 同じ表の列：Main department, Organisation, SCS on standard con…, Information for SCS…, Comments

## g0089（2 列）
- 見出し：SCS on standard contracts (end of year NCPRP)
- 例1 値：」22,680,794 | Annual SCS Paybill for those SCS on sta…
  - 同じ表の列：Main department, Organisation, Delegated grades on…, Information for SCS…, Comments
- 例2 値：」14,349,834 | Annual SCS Paybill for those SCS on sta…
  - 同じ表の列：Main department, Organisation, Delegated grades on…, Information for SCS…, Comments

## g0090（2 列）
- 見出し：Information for SCS on non-standard contracts
- 例1 値：Number of SCS on non-standard contracts… | 3
  - 同じ表の列：Main department, Organisation, Delegated grades on…, SCS on standard con…, Comments
- 例2 値：1 | Number of SCS on non-standard contracts…
  - 同じ表の列：Main department, Organisation, Delegated grades on…, SCS on standard con…, Comments

## g0091（1 列）
- 見出し：Comments
- 例1 値：Although the number of SCS on a standar…
  - 同じ表の列：Main department, Organisation, Delegated grades on…, SCS on standard con…, Information for SCS…

## g0092（1 列）
- 見出し：City of accommodation (if different to destination)
- 例1 値：New Zealand | United States | Poland
  - 同じ表の列：Mode of travel, Date of Departure, Duration of stay, Destination, Class of travel, Base Sales includin…, Comments

## g0093（1 列）
- 見出し：Class of travel
- 例1 値：Economy | Economy | Economy | Business | Business
  - 同じ表の列：Mode of travel, Date of Departure, Duration of stay, Destination, City of accommodati…, Base Sales includin…, Comments

## g0094（1 列）
- 見出し：Base Sales including tax
- 例1 値：」119.00 | 」1,809 | 」490.00 | 」643 | 」506
  - 同じ表の列：Mode of travel, Date of Departure, Duration of stay, Destination, City of accommodati…, Class of travel, Comments

## g0095（1 列）
- 見出し：Comments
- 例1 値：Cancelled | Cancelled | Credit note - full refund | Credit note - partial refund
  - 同じ表の列：Mode of travel, Date of Departure, Duration of stay, Destination, City of accommodati…, Class of travel, Base Sales includin…

## g0096（1 列）
- 見出し：Year
- 例1 値：2021
  - 同じ表の列：Month, Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…

## g0097（1 列）
- 見出し：Month
- 例1 値：October
  - 同じ表の列：Year, Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…

## g0098（1 列）
- 見出し：Organisation type
- 例1 値：Ministerial Department
  - 同じ表の列：Year, Month, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…

## g0099（1 列）
- 見出し：Main, parent or sponsoring department:
- 例1 値：Northern Ireland Office
  - 同じ表の列：Year, Month, Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…

## g0100（1 列）
- 見出し：Payroll staff
- 例1 値：Headcount | AO/AA | 10.00
  - 同じ表の列：Year, Month, Organisation type, Main, parent or spo…, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…

## g0101（1 列）
- 見出し：Number of non-payroll staff (contingent labour and consultan
- 例1 値：Agency staff | Headcount
  - 同じ表の列：Year, Month, Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…

## g0102（1 列）
- 見出し：Grand Total (workforce numbers)
- 例1 値：0 | 0 | 181 | 0 | 0
  - 同じ表の列：Year, Month, Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs, Non-Payroll staff (…

## g0103（1 列）
- 見出し：Payroll staff costs
- 例1 値：£563,141.22 | Salary
  - 同じ表の列：Year, Month, Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…

## g0104（1 列）
- 見出し：Non-Payroll staff (contingent labour/consultancy) costs
- 例1 値：Total monthly cost of contingent labour…
  - 同じ表の列：Year, Month, Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs

## g0105（1 列）
- 見出し：Grand Total paybill/staffing (payroll and non-payroll) costs
- 例1 値：£0.00 | £0.00 | £0.00 | £0.00 | £0.00
  - 同じ表の列：Year, Month, Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs

## g0106（1 列）
- 見出し：Organisation Type
- 例1 値：Executive Agency | Executive Agency | Executive Non-Departmental Public Body | Ministerial Department | Executive Non-Departmental Public Body
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0107（1 列）
- 見出し：Main, parent or sponsoring department
- 例1 値：Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence
  - 同じ表の列：Organisation Type, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0108（1 列）
- 見出し：Payroll staff AO/AA Headcount
- 例1 値：12,016 | 0 | 11 | 185 | 1,567
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0109（1 列）
- 見出し：Payroll staff EO Headcount
- 例1 値：375 | 0 | 549 | 7,141 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0110（1 列）
- 見出し：Payroll staff SEO/HEO Headcount
- 例1 値：3 | 3 | 12,707 | 270 | 442
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0111（1 列）
- 見出し：Payroll staff Grade 6/7 Headcount
- 例1 値：51 | 2,306 | 79 | 1 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0112（1 列）
- 見出し：Payroll staff SCS Headcount
- 例1 値：1 | 35 | 1 | 231 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff Other…, Payroll staff Total…

## g0113（1 列）
- 見出し：Payroll staff Other, unknown or unspecified Headcount
- 例1 値：51 | 14,494 | 0 | 0 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Total…

## g0114（1 列）
- 見出し：Payroll staff Total Employees Headcount
- 例1 値：1,085 | 16 | 2,441 | 48,895 | 3,849
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

## g0115（1 列）
- 見出し：Non-payroll Staff Agency staff (clerical/admin) Headcount
- 例1 値：0 | 2 | 1,769 | 27 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

## g0116（1 列）
- 見出し：Main department
- 例1 値：Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence
  - 同じ表の列：Organisation, Delegated grades on…, SCS on standard con…, Information for SCS…, Comments

## g0117（1 列）
- 見出し：Organisation
- 例1 値：Ministry of Defence | Defence Science and Technology Laborato… | Royal Fleet Auxilary | UK Hydrographic Office | Defence Electronic and Components Agency
  - 同じ表の列：Main department, Delegated grades on…, SCS on standard con…, Information for SCS…, Comments

## g0118（1 列）
- 見出し：Comments
- 例1 値：Dstl introduced a pilot in-year reward … | As reported last year that following th… | The year-end awards, although linked to… | DECA was launched on 1st April 13 follo… | SCS numbers reported in this line inclu…
  - 同じ表の列：Main department, Organisation, Delegated grades on…, SCS on standard con…, Information for SCS…

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
```
