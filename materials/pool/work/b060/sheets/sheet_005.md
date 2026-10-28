# ラベル用シート 005 / 006

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_005.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0481（3 列）
- 見出し：Expense Type
- 例1 値：Travel | Contracted Inspection Costs | Contracted Inspection Costs | Travel | Corporate Contracts
  - 同じ表の列：Department, Entity, Date, Expense Area, Supplier, Transaction No, Amount, Expenditure Type
- 例2 値：Disabled Facilities Grant | Amenity Variations | Temporary Staff | Electricity | Payment to Artistes
  - 同じ表の列：Organisation, Service Area, Cost Centre, Payment Date, Transaction No., Amount, Capital Revenue, Supplier ID

## g0482（1 列）
- 見出し：Expense Area
- 例1 値：Information Services | Inspection Costs | Inspection Costs | Inspection Data & Insight | Inspection Costs
  - 同じ表の列：Department, Entity, Date, Expense Type, Supplier, Transaction No, Amount, Expenditure Type

## g0483（1 列）
- 見出し：Supplier
- 例1 値：Cfbt | CGI IT UK Ltd | Serco Limited | Tribal Education Ltd | Redfern Travel Ltd
  - 同じ表の列：Department, Entity, Date, Expense Type, Expense Area, Transaction No, Amount, Expenditure Type

## g0484（1 列）
- 見出し：Transaction No
- 例1 値：812352 | 812425 | 812464 | 159745 | 812581
  - 同じ表の列：Department, Entity, Date, Expense Type, Expense Area, Supplier, Amount, Expenditure Type

## g0485（1 列）
- 見出し：Amount
- 例1 値：-」2,589,596.98 | 」39,192.94 | 」383,177.80 | 」32,390.30 | 」474,247.59
  - 同じ表の列：Department, Entity, Date, Expense Type, Expense Area, Supplier, Transaction No, Expenditure Type

## g0486（1 列）
- 見出し：Expenditure Type
- 例1 値：Programme Class | Programme Class | Programme Class | Programme Class | Programme Class
  - 同じ表の列：Department, Entity, Date, Expense Type, Expense Area, Supplier, Transaction No, Amount

## g0487（1 列）
- 見出し：Report
- 例1 値：Report | Report | Report | Report | Report
  - 同じ表の列：URN, Inspection or regul…, Provider type, Provision type, Region, Local authority, No. of times on OP …, 1st time

## g0488（1 列）
- 見出し：URN
- 例1 値：139332 | 103587 | 101144 | 119894 | 58182
  - 同じ表の列：Report, Inspection or regul…, Provider type, Provision type, Region, Local authority, No. of times on OP …, 1st time

## g0489（1 列）
- 見出し：Inspection or regulatory remit
- 例1 値：Maintained schools and academies | Early years and childcare | Maintained schools and academies | Early years and childcare | Early years and childcare
  - 同じ表の列：Report, URN, Provider type, Provision type, Region, Local authority, No. of times on OP …, 1st time

## g0490（1 列）
- 見出し：Provider type
- 例1 値：Voluntary Aided School | Academy Sponsor Led | LA Nursery School | Voluntary Controlled School | Childminder
  - 同じ表の列：Report, URN, Inspection or regul…, Provision type, Region, Local authority, No. of times on OP …, 1st time

## g0491（1 列）
- 見出し：Provision type
- 例1 値：Secondary | Primary | Secondary | Primary | Primary
  - 同じ表の列：Report, URN, Inspection or regul…, Provider type, Region, Local authority, No. of times on OP …, 1st time

## g0492（1 列）
- 見出し：Region
- 例1 値：East of England | East of England | London | London | East of England
  - 同じ表の列：Report, URN, Inspection or regul…, Provider type, Provision type, Local authority, No. of times on OP …, 1st time

## g0493（1 列）
- 見出し：Local authority
- 例1 値：Hackney | Slough | Hertfordshire | Liverpool | Northamptonshire
  - 同じ表の列：Report, URN, Inspection or regul…, Provider type, Provision type, Region, No. of times on OP …, 1st time

## g0494（1 列）
- 見出し：No. of times on OP list
- 例1 値：1 | 1 | 1 | 1 | 2
  - 同じ表の列：Report, URN, Inspection or regul…, Provider type, Provision type, Region, Local authority, 1st time

## g0495（1 列）
- 見出し：1st time
- 例1 値：2014/15 | 1999/00 | 2014/15 | 2008/09 | 2014/15
  - 同じ表の列：Report, URN, Inspection or regul…, Provider type, Provision type, Region, Local authority, No. of times on OP …

## g0496（1 列）
- 見出し：2nd time
- 例1 値：2014/15 | 2011/12 | 2005/06 | 2014/15 | 2014/15
  - 同じ表の列：Report, URN, Inspection or regul…, Provider type, Provision type, Region, Local authority, No. of times on OP …

## g0497（2 列）
- 見出し：Department family
- 例1 値：Office of Rail and Road | Office of Rail and Road | Office of Rail and Road | Office of Rail and Road | Office of Rail and Road
  - 同じ表の列：Entity, Date of payment, Expense Code, Expense type, Cost Centre, Expense area, Supplier, Transaction Number
- 例2 値：Office of Rail and Road | Office of Rail and Road | Office of Rail and Road | Office of Rail and Road | Office of Rail and Road
  - 同じ表の列：Entity, Date of payment, Expense Code, Expense type, Cost Centre, Expense area, Supplier, Transaction Number

## g0498（2 列）
- 見出し：Expense Code
- 例1 値：N8090 | C5402 | H1020 | C5350 | Z1100
  - 同じ表の列：Department family, Entity, Date of payment, Expense type, Cost Centre, Expense area, Supplier, Transaction Number
- 例2 値：Z1900 | Z1100 | C5402 | Z1100 | C2100
  - 同じ表の列：Department family, Entity, Date of payment, Expense type, Cost Centre, Expense area, Supplier, Transaction Number

## g0499（1 列）
- 見出し：Expense type
- 例1 値：ACCOMMODATION ACCRUAL | CONSULTANCY - ADVISORY | UPLOAD SUSPENSE - TRAVEL/ACCOMMODATION | UK REGULATION NETWORK COSTS | PURCHASED SOFTWARE LICENSES IY
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Cost Centre, Expense area, Supplier, Transaction Number

## g0500（3 列）
- 見出し：Cost Centre
- 例1 値：1510 | 990 | 1302 | 1201 | 2110
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Expense type, Expense area, Supplier, Transaction Number
- 例2 値：1002 | 0000 | 0000 | 1101 | 0000
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Expense type, Expense area, Supplier, Transaction Number

## g0501（2 列）
- 見出し：Expense area
- 例1 値：STRATEGY | BALANCE SHEET | BALANCE SHEET | ACCOMMODATION | HIGHWAYS
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Expense type, Cost Centre, Supplier, Transaction Number
- 例2 値：Interface | Interface | Administration | Interface | ITC Department
  - 同じ表の列：Department family, Entity, Entered On, Expense Type, Voucher, SumOfAmount

## g0502（1 列）
- 見出し：Transaction Number
- 例1 値：4126 | 02767/1 | MIS0111032 | 6060023246 | EST0935
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Expense type, Cost Centre, Expense area, Supplier

## g0503（2 列）
- 見出し：Amount in Sterling
- 例1 値：291000 | 78000 | 81260.08 | 51599.35 | 25977.6
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Expense type, Cost Centre, Expense area, Supplier
- 例2 値：59400 | 29825 | 335751.57 | 27417 | 241008.12
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Expense type, Cost Centre, Expense area, Supplier

## g0504（1 列）
- 見出し：Expense type
- 例1 値：Fixed Assets suspense account | Consultancy - Advisory | Rates - London | Consultancy - Advisory | Upload Suspense - Travel/Accommodation
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Cost Centre, Expense area, Supplier, Transaction Number

## g0505（1 列）
- 見出し：Expense area
- 例1 値：Administration | Accommodation | Economics, Finance and Markets | Administration | Administration
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Expense type, Cost Centre, Supplier, Transaction Number

## g0506（1 列）
- 見出し：Supplier
- 例1 値：London Borough of Tower Hamlets | Europe Economics | Ove Arup and Partners Limited | Nichols Group Limited | Savills Plc
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Expense type, Cost Centre, Expense area, Transaction Number

## g0507（1 列）
- 見出し：Transaction Number
- 例1 値：D628756 | Duplicate: TNG15119 | 4922 | 3537 | 4666
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Expense type, Cost Centre, Expense area, Supplier

## g0508（1 列）
- 見出し：Organisation (A)
- 例1 値：Pendle Borough Council | Pendle Borough Council | Pendle Borough Council | Pendle Borough Council | Pendle Borough Council
  - 同じ表の列：Department (B), Transaction Date (C), Net Amount (F), Irrecoverable VAT (…

## g0509（1 列）
- 見出し：Department (B)
- 例1 値：HOUSING & COMM | DEMOCRATIC & LEGAL | DEMOCRATIC & LEGAL | HOUSING & ECONOMIC REGENERATION | OPERATIONAL SERVICES
  - 同じ表の列：Organisation (A), Transaction Date (C), Net Amount (F), Irrecoverable VAT (…

## g0510（1 列）
- 見出し：Transaction Date (C)
- 例1 値：29/06/2019 | 24/06/2019 | 18/06/2019 | 06/06/2019 | 24/06/2019
  - 同じ表の列：Organisation (A), Department (B), Net Amount (F), Irrecoverable VAT (…

## g0511（1 列）
- 見出し：Net Amount (F)
- 例1 値：30 | 26.75 | 2.25 | -319.17 | 45
  - 同じ表の列：Organisation (A), Department (B), Transaction Date (C), Irrecoverable VAT (…

## g0512（1 列）
- 見出し：Irrecoverable VAT (G)
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：Organisation (A), Department (B), Transaction Date (C), Net Amount (F)

## g0513（1 列）
- 見出し：Reference Number (B)
- 例1 値：PCO017503 | DAL003402 | PCO017533 | EST004436 | EST004437
  - 同じ表の列：Title of Agreement …, Dept (D), Service Label (E ), Start Date (H), End Date (I), Quantity (J), Price (K), Value (L)

## g0514（1 列）
- 見出し：Title of Agreement (C )
- 例1 値：Marsden Old Hall - Carry out external r… | Intranet Installation & CMS Support Ite… | Fit replacement pumps/flow switches etc… | CUTS TO NORTH AND SOUTH AS PER QUOTE NO… | PCO 017533 to cover your invoice 6433 d…
  - 同じ表の列：Reference Number (B), Dept (D), Service Label (E ), Start Date (H), End Date (I), Quantity (J), Price (K), Value (L)

## g0515（1 列）
- 見出し：Dept (D)
- 例1 値：Property Services | Property Services | Parks & Recreation Services | Democratic & Legal Services | Parks & Recreation Services
  - 同じ表の列：Reference Number (B), Title of Agreement …, Service Label (E ), Start Date (H), End Date (I), Quantity (J), Price (K), Value (L)

## g0516（1 列）
- 見出し：Service Label (E )
- 例1 値：2101 | CD14 | 2101 | CD14 | CD14
  - 同じ表の列：Reference Number (B), Title of Agreement …, Dept (D), Start Date (H), End Date (I), Quantity (J), Price (K), Value (L)

## g0517（1 列）
- 見出し：Start Date (H)
- 例1 値：16/07/2019 | 05/07/2019 | 03/07/2019 | 19/07/2019 | 15/07/2019
  - 同じ表の列：Reference Number (B), Title of Agreement …, Dept (D), Service Label (E ), End Date (I), Quantity (J), Price (K), Value (L)

## g0518（1 列）
- 見出し：End Date (I)
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：Reference Number (B), Title of Agreement …, Dept (D), Service Label (E ), Start Date (H), Quantity (J), Price (K), Value (L)

## g0519（1 列）
- 見出し：Quantity (J)
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Reference Number (B), Title of Agreement …, Dept (D), Service Label (E ), Start Date (H), End Date (I), Price (K), Value (L)

## g0520（1 列）
- 見出し：Price (K)
- 例1 値：25497 | 8683 | 14900 | 14900 | 9250
  - 同じ表の列：Reference Number (B), Title of Agreement …, Dept (D), Service Label (E ), Start Date (H), End Date (I), Quantity (J), Value (L)

## g0521（1 列）
- 見出し：Value (L)
- 例1 値：25497 | 9250 | 8683 | 14900 | 14900
  - 同じ表の列：Reference Number (B), Title of Agreement …, Dept (D), Service Label (E ), Start Date (H), End Date (I), Quantity (J), Price (K)

## g0522（1 列）
- 見出し：Tender Process (N)
- 例1 値：Purchase Order | Purchase Order | Purchase Order | Purchase Order | Purchase Order
  - 同じ表の列：Reference Number (B), Title of Agreement …, Dept (D), Service Label (E ), Start Date (H), End Date (I), Quantity (J), Price (K)

## g0523（2 列）
- 見出し：Department family
- 例1 値：Communities And Local Government | Communities And Local Government | Communities And Local Government | Communities And Local Government | Communities And Local Government
  - 同じ表の列：Entity, Entered On, Expense Type, Expense Area, Voucher, SumOfAmount
- 例2 値：UK Trade and Investment | UK Trade and Investment | UK Trade and Investment | UK Trade and Investment | UK Trade and Investment
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount In Sterling

## g0524（1 列）
- 見出し：Entered On
- 例1 値：20/04/2010 | 13/04/2010 | 20/04/2010 | 13/04/2010 | 13/04/2010
  - 同じ表の列：Department family, Entity, Expense Type, Expense Area, Voucher, SumOfAmount

## g0525（1 列）
- 見出し：Expense Type
- 例1 値：Travel | Water | Cost of Sales - Time & Labour | Training | Stationery
  - 同じ表の列：Department family, Entity, Entered On, Expense Area, Voucher, SumOfAmount

## g0526（1 列）
- 見出し：Voucher
- 例1 値：11254 | 11217 | 11242 | 11240 | 11199
  - 同じ表の列：Department family, Entity, Entered On, Expense Type, Expense Area, SumOfAmount

## g0527（1 列）
- 見出し：SumOfAmount
- 例1 値：507.9 | 706.34 | 444.51 | 300.95 | 1406.47
  - 同じ表の列：Department family, Entity, Entered On, Expense Type, Expense Area, Voucher

## g0528（1 列）
- 見出し：Contract Reference Number
- 例1 値：9TGE-DEVFU0 | 9SWQ-H3KAZ4 | 9U4G-24U6M2 | ROCH-9TGL-5B0T42 | ROCH-9VDM-MQYY8A
  - 同じ表の列：Expression of Inter…, Tender Title, Estimated Contract …, Estimated Contract …

## g0529（1 列）
- 見出し：Expression of Interest Start
- 例1 値：06/02/2015 | 20/02/2015 | 08/01/2015 | 05/03/2015 | 13/03/2015
  - 同じ表の列：Contract Reference …, Tender Title, Estimated Contract …, Estimated Contract …

## g0530（1 列）
- 見出し：Tender Title
- 例1 値：Rochdale Town Hall Entrance Doors | An Invitation to attend the Rochdale Bu… | The Provision of Prevention & Independe… | Invitation to tender for the for the Pr… | Servicing, Maintenance & Repair of Lift…
  - 同じ表の列：Contract Reference …, Expression of Inter…, Estimated Contract …, Estimated Contract …

## g0531（1 列）
- 見出し：Estimated Contract Start Date
- 例1 値：23/02/2015 | 04/02/2015 | 20/02/2015 | 01/09/2015 | 01/04/2015
  - 同じ表の列：Contract Reference …, Expression of Inter…, Tender Title, Estimated Contract …

## g0532（1 列）
- 見出し：Estimated Contract End Date
- 例1 値：31/08/2017 | 09/03/2015 | 25/02/2015 | 31/03/2016 | 31/03/2018
  - 同じ表の列：Contract Reference …, Expression of Inter…, Tender Title, Estimated Contract …

## g0533（1 列）
- 見出し：Record UID
- 例1 値：690 | 185 | 125 | 1095 | 747
  - 同じ表の列：Contract Ref No, Directorate/ Servic…, Start Date, End Date (Includes …, Review Date, Estimated Maximum A…

## g0534（1 列）
- 見出し：Contract Ref No
- 例1 値：STRoPr1179 | STSTPe1115 | NWCE-8KDBJA | NWCE-7NXM2Y | STSTPe1113
  - 同じ表の列：Record UID, Directorate/ Servic…, Start Date, End Date (Includes …, Review Date, Estimated Maximum A…

## g0535（1 列）
- 見出し：Directorate/ Service Responsible
- 例1 値：Public Health | Public Health | Economy and Environment | Economy & Environment | Economy & Environment
  - 同じ表の列：Record UID, Contract Ref No, Start Date, End Date (Includes …, Review Date, Estimated Maximum A…

## g0536（1 列）
- 見出し：Start Date
- 例1 値：01/04/2013 | 01/04/2014 | 01/04/2012 | 15/02/2013 | 01/09/2014
  - 同じ表の列：Record UID, Contract Ref No, Directorate/ Servic…, End Date (Includes …, Review Date, Estimated Maximum A…

## g0537（1 列）
- 見出し：End Date (Includes Ext Date)
- 例1 値：31/03/2015 | 31/03/2016 | 31/05/2016 | 31/03/2015 | 15/01/2017
  - 同じ表の列：Record UID, Contract Ref No, Directorate/ Servic…, Start Date, Review Date, Estimated Maximum A…

## g0538（1 列）
- 見出し：Estimated Maximum Annual Value
- 例1 値：」2,000 | 」120,000 | 」7,500 | 」12,000 | 」5,215
  - 同じ表の列：Record UID, Contract Ref No, Directorate/ Servic…, Start Date, End Date (Includes …, Review Date

## g0539（1 列）
- 見出し：2016
- 例1 値：Totals | December | The net cost to RBC of delivering the s… | September | November
  - 同じ表の列：Number of Stray Dog…, Number of stray dog…, Number of dogs reta…, Number of dogs euth…

## g0540（1 列）
- 見出し：Number of Stray Dogs seized
- 例1 値：21 | 36 | 21 | 306 | 19
  - 同じ表の列：2016, Number of stray dog…, Number of dogs reta…, Number of dogs euth…

## g0541（1 列）
- 見出し：Number of stray dogs kennelled
- 例1 値：18 | 238 | 25 | 22 | 16
  - 同じ表の列：2016, Number of Stray Dog…, Number of dogs reta…, Number of dogs euth…

## g0542（1 列）
- 見出し：Number of dogs retained by the finder
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：2016, Number of Stray Dog…, Number of stray dog…, Number of dogs euth…

## g0543（1 列）
- 見出し：Number of dogs euthanised during the 7 day statutory holding
- 例1 値：0 | 1 | 0 | 1 | 1
  - 同じ表の列：2016, Number of Stray Dog…, Number of stray dog…, Number of dogs reta…

## g0544（1 列）
- 見出し：reference
- 例1 値：T2-114 | T2-28 | No.3 2024 | T2-81 | T2-34
  - 同じ表の列：notes, made-date, start-date, confirmed-date, end-date

## g0545（1 列）
- 見出し：notes
- 例1 値：The TPO was made on 21st July 2004 but … | The TPO was never confirmed | The TPO T2-89 was revoked on 12th April… | Permission granted to fell diseased Syc… | The felling of the 3 protected trees ha…
  - 同じ表の列：reference, made-date, start-date, confirmed-date, end-date

## g0546（1 列）
- 見出し：made-date
- 例1 値：14/12/1984 | 25/08/1999 | 05/02/1975 | 05/01/1966 | 12/04/1988
  - 同じ表の列：reference, notes, start-date, confirmed-date, end-date

## g0547（2 列）
- 見出し：start-date
- 例1 値：24/07/1975 | 19/06/1996 | 10/05/2002 | 30/11/2007 | 10/04/1969
  - 同じ表の列：reference, notes, made-date, confirmed-date, end-date
- 例2 値：04/12/1974 | 04/07/2018 | 01/08/1974 | 01/09/1986 | 07/11/2007
  - 同じ表の列：reference, geometry, notes, designation-date, entry-date

## g0548（1 列）
- 見出し：confirmed-date
- 例1 値：27/02/1980 | 21/06/1984 | 27/01/2015 | 28/11/2018 | 16/01/2018
  - 同じ表の列：reference, notes, made-date, start-date, end-date

## g0549（1 列）
- 見出し：end-date
- 例1 値：30/09/2004 | 04/06/2020 | 04/06/2020 | 02/12/2004 | 30/05/2012
  - 同じ表の列：reference, notes, made-date, start-date, confirmed-date

## g0550（1 列）
- 見出し：reference
- 例1 値：1072823 | 1317745 | 1317784 | 1163340a | 1072812
  - 同じ表の列：listed_building, geometry, notes, uprns, entry_date, start_date

## g0551（1 列）
- 見出し：listed_building
- 例1 値：1072816 | 1072810 | 1072805 | 1072764 | 1361942
  - 同じ表の列：reference, geometry, notes, uprns, entry_date, start_date

## g0552（2 列）
- 見出し：geometry
- 例1 値：MULTIPOLYGON (((-2.251145 53.732124,-2.… | MULTIPOLYGON (((-2.25824 53.690144,-2.2… | MULTIPOLYGON (((-2.327079 53.704317,-2.… | MULTIPOLYGON (((-2.286374 53.724442,-2.… | MULTIPOLYGON (((-2.32789 53.719447,-2.3…
  - 同じ表の列：reference, listed_building, notes, uprns, entry_date, start_date
- 例2 値：MULTIPOLYGON (((-2.325528 53.708445, -2… | MULTIPOLYGON (((-2.292383 53.736616, -2… | MULTIPOLYGON (((-2.285463 53.705694, -2… | MULTIPOLYGON (((-2.204356 53.704904, -2… | MULTIPOLYGON (((-2.276714 53.699194, -2…
  - 同じ表の列：reference, notes, start-date, designation-date, entry-date

## g0553（1 列）
- 見出し：notes
- 例1 値：II | II | II | II | II
  - 同じ表の列：reference, listed_building, geometry, uprns, entry_date, start_date

## g0554（1 列）
- 見出し：uprns
- 例1 値：010013836434,010013836433, 010013836425 | 010013835386 | 100012543680, 100012543613 | 010014331017 | 2.00001E+11
  - 同じ表の列：reference, listed_building, geometry, notes, entry_date, start_date

## g0555（1 列）
- 見出し：entry_date
- 例1 値：22/10/2024 | 15/10/2024 | 16/10/2024 | 22/10/2024 | 17/10/2024
  - 同じ表の列：reference, listed_building, geometry, notes, uprns, start_date

## g0556（1 列）
- 見出し：start_date
- 例1 値：30/11/1984 | 19/06/1968 | 30/11/1984 | 09/08/1966 | 19/06/1968
  - 同じ表の列：reference, listed_building, geometry, notes, uprns, entry_date

## g0557（1 列）
- 見出し：reference
- 例1 値：CA07 | CA03 | CA02 | CA10 | CA08
  - 同じ表の列：geometry, notes, start-date, designation-date, entry-date

## g0558（1 列）
- 見出し：notes
- 例1 値：The Bacup Town Centre Conservation Area…
  - 同じ表の列：reference, geometry, start-date, designation-date, entry-date

## g0559（1 列）
- 見出し：designation-date
- 例1 値：04/07/2018 | 07/11/2007 | 01/08/1974 | 07/03/1975 | 01/07/1978
  - 同じ表の列：reference, geometry, notes, start-date, entry-date

## g0560（1 列）
- 見出し：entry-date
- 例1 値：07/11/2007 | 01/12/1990 | 09/03/2016 | 01/08/1974 | 07/03/1975
  - 同じ表の列：reference, geometry, notes, start-date, designation-date

## g0561（1 列）
- 見出し：Reference Number
- 例1 値：PO00058217 | PO00058268 | PO00059527 | PO00059013 | PO00058551
  - 同じ表の列：Value, Purchase Order Date, Local Authority Dep…

## g0562（1 列）
- 見出し：Value
- 例1 値：65,000.00 | 3,184.95 | 6,953.00 | 8,460.00 | 800,296.86
  - 同じ表の列：Reference Number, Purchase Order Date, Local Authority Dep…

## g0563（1 列）
- 見出し：Purchase Order Date
- 例1 値：12/06/2018 | 06/04/2018 | 18/04/2018 | 18/04/2018 | 17/04/2018
  - 同じ表の列：Reference Number, Value, Local Authority Dep…

## g0564（1 列）
- 見出し：Local Authority Department
- 例1 値：Chief Executives | Modernisation | Comm Safety and Environment | Health and Adult Services | Housing Services HRA
  - 同じ表の列：Reference Number, Value, Purchase Order Date

## g0565（1 列）
- 見出し：FID
- 例1 値：brownfield_register_2025_review.50 | brownfield_register_2025_review.38 | brownfield_register_2025_review.11 | brownfield_register_2025_review.24 | brownfield_register_2025_review.6
  - 同じ表の列：id_0, id, organisati, organisa_1, siterefere, site_id_2, siteplanur, geox

## g0566（1 列）
- 見出し：id_0
- 例1 値：13 | 10 | 33 | 18 | 8
  - 同じ表の列：FID, id, organisati, organisa_1, siterefere, site_id_2, siteplanur, geox

## g0567（1 列）
- 見出し：id
- 例1 値：69 | 152 | 56 | 173 | 128
  - 同じ表の列：FID, id_0, organisati, organisa_1, siterefere, site_id_2, siteplanur, geox

## g0568（1 列）
- 見出し：organisati
- 例1 値：http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr…
  - 同じ表の列：FID, id_0, id, organisa_1, siterefere, site_id_2, siteplanur, geox

## g0569（1 列）
- 見出し：organisa_1
- 例1 値：Runnymede Borough Council | Runnymede Borough Council | Runnymede Borough Council | Runnymede Borough Council | Runnymede Borough Council
  - 同じ表の列：FID, id_0, id, organisati, siterefere, site_id_2, siteplanur, geox

## g0570（1 列）
- 見出し：siterefere
- 例1 値：SLAA/517 | SLAA/281 | SLAA/353 | SLAA/451 | SLAA/358
  - 同じ表の列：FID, id_0, id, organisati, organisa_1, site_id_2, siteplanur, geox

## g0571（1 列）
- 見出し：site_id_2
- 例1 値：258 | 512 | 436 | 451 | 141
  - 同じ表の列：FID, id_0, id, organisati, organisa_1, siterefere, siteplanur, geox

## g0572（1 列）
- 見出し：siteplanur
- 例1 値：http://maps.runnymede.gov.uk/website/ma… | http://maps.runnymede.gov.uk/website/ma… | http://maps.runnymede.gov.uk/website/ma… | http://maps.runnymede.gov.uk/website/ma… | http://maps.runnymede.gov.uk/website/ma…
  - 同じ表の列：FID, id_0, id, organisati, organisa_1, siterefere, site_id_2, geox

## g0573（1 列）
- 見出し：Service Area
- 例1 値：Customer Services | Holding Accounts | Democratic Services | Environmental Health and Housing | Customer Services
  - 同じ表の列：Organisation, Cost Centre, Expense Type, Payment Date, Transaction No., Amount, Capital Revenue, Supplier ID

## g0574（1 列）
- 見出し：Transaction No.
- 例1 値：189364 | 189548 | 188273 | 188989 | 188730
  - 同じ表の列：Organisation, Service Area, Cost Centre, Expense Type, Payment Date, Amount, Capital Revenue, Supplier ID

## g0575（1 列）
- 見出し：Capital Revenue
- 例1 値：Revenue | Revenue | Revenue | Control Accounts | Revenue
  - 同じ表の列：Organisation, Service Area, Cost Centre, Expense Type, Payment Date, Transaction No., Amount, Supplier ID

## g0576（1 列）
- 見出し：Supplier ID
- 例1 値：724 | 9422 | 353 | 9062 | 821
  - 同じ表の列：Organisation, Service Area, Cost Centre, Expense Type, Payment Date, Transaction No., Amount, Capital Revenue

## g0577（1 列）
- 見出し：Effective date
- 例1 値：31/03/2024 | 31/03/2024 | 31/03/2024 | 31/03/2024 | 31/03/2024
  - 同じ表の列：Level, Job title, Grade, Service /Department, Permanent/temporary, Salary in 」5k brack…, Salary Ceiling, Responsibilities

## g0578（1 列）
- 見出し：Level
- 例1 値：LEVEL 3 | LEVEL 2 | LEVEL 3 | LEVEL 3 | LEVEL 2
  - 同じ表の列：Effective date, Job title, Grade, Service /Department, Permanent/temporary, Salary in 」5k brack…, Salary Ceiling, Responsibilities

## g0579（1 列）
- 見出し：Job title
- 例1 値：Corporate Manager - Legal Services | Head of Regeneration & Development | Executive Director and Deputy Chief Exe… | Assistant Chief Executive | Corporate Manager - People (HR and OD)
  - 同じ表の列：Effective date, Level, Grade, Service /Department, Permanent/temporary, Salary in 」5k brack…, Salary Ceiling, Responsibilities

## g0580（1 列）
- 見出し：Grade
- 例1 値：G13 - Exec Head | G12 - Head of Service | CM | G14 - Exec Director | G13 - Exec Head
  - 同じ表の列：Effective date, Level, Job title, Service /Department, Permanent/temporary, Salary in 」5k brack…, Salary Ceiling, Responsibilities

## g0581（1 列）
- 見出し：Service /Department
- 例1 値：Operations | Regeneration | Executive Director | Executive Director | Democracy
  - 同じ表の列：Effective date, Level, Job title, Grade, Permanent/temporary, Salary in 」5k brack…, Salary Ceiling, Responsibilities

## g0582（1 列）
- 見出し：Permanent/temporary
- 例1 値：Permanent | Permanent | Permanent | Permanent | Permanent
  - 同じ表の列：Effective date, Level, Job title, Grade, Service /Department, Salary in 」5k brack…, Salary Ceiling, Responsibilities

## g0583（1 列）
- 見出し：Salary in 」5k brackets
- 例1 値：」130,000-」134,999 | 」80,000-」84,999 | 」60,000-」64,999 | 」65,000-」69,999 | 」100,000-」104,999
  - 同じ表の列：Effective date, Level, Job title, Grade, Service /Department, Permanent/temporary, Salary Ceiling, Responsibilities

## g0584（1 列）
- 見出し：Salary Ceiling
- 例1 値：100,912 | 85,387 | 71,886 | 85,387 | 67,162
  - 同じ表の列：Effective date, Level, Job title, Grade, Service /Department, Permanent/temporary, Salary in 」5k brack…, Responsibilities

## g0585（1 列）
- 見出し：Responsibilities
- 例1 値：https://www.rushmoor.gov.uk/your-counci… | https://www.rushmoor.gov.uk/your-counci… | https://www.rushmoor.gov.uk/your-counci… | https://www.rushmoor.gov.uk/your-counci… | https://www.rushmoor.gov.uk/your-counci…
  - 同じ表の列：Effective date, Level, Job title, Grade, Service /Department, Permanent/temporary, Salary in 」5k brack…, Salary Ceiling

## g0586（1 列）
- 見出し：Minister
- 例1 値：Secretary of State For Scotland | Secretary of State for Scotland | Secretary of State For Scotland | Secretary of State For Scotland | Secretary of State For Scotland
  - 同じ表の列：Date of Hospitality, Type of hospitality…

## g0587（1 列）
- 見出し：Date of Hospitality
- 例1 値：04/09/2011 | 28/09/2011 | 12/07/2011 | 07/07/2011 | 21/07/2011
  - 同じ表の列：Minister, Type of hospitality…

## g0588（1 列）
- 見出し：Type of hospitality received
- 例1 値：Ticket to British Grand Prix and Dinner | Dinner | Dinner | Ticket to Royal Military Tattoo and Din… | Dinner
  - 同じ表の列：Minister, Date of Hospitality

## g0589（1 列）
- 見出し：Organisation type
- 例1 値：Ministerial Department
  - 同じ表の列：Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0590（1 列）
- 見出し：Main, parent or sponsoring department:
- 例1 値：Scotland Office
  - 同じ表の列：Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0591（1 列）
- 見出し：Payroll staff
- 例1 値：13 | AO/AA | Headcount
  - 同じ表の列：Organisation type, Main, parent or spo…, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0592（1 列）
- 見出し：Number of non-payroll staff (contingent labour and consultan
- 例1 値：4 | Agency staff (clerical/admin) | Headcount
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0593（1 列）
- 見出し：Grand Total (workforce numbers)
- 例1 値：0 | 0 | 99 | 0 | 0
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0594（1 列）
- 見出し：Payroll staff costs
- 例1 値：」359,334.04 | Salary
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…

## g0595（1 列）
- 見出し：Non-Payroll staff (contingent labour/consultancy) costs
- 例1 値：Total monthly cost of contingent labour… | 」15,769.08
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Grand Total paybill…

## g0596（1 列）
- 見出し：Grand Total paybill/staffing (payroll and non-payroll) costs
- 例1 値：」0.00 | 」0.00 | 」0.00 | 」0.00 | 」0.00
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…

## g0597（1 列）
- 見出し：UKPRN
- 例1 値：10004686 | 10000146 | 10007193 | 10004977 | 10001535
  - 同じ表の列：UPIN, Age_Band, Survey_Type, Question, Score, OrgLowest, OrgMiddle, OrgHighest

## g0598（1 列）
- 見出し：UPIN
- 例1 値：119215 | 107708 | 118584 | 108877 | 118446
  - 同じ表の列：UKPRN, Age_Band, Survey_Type, Question, Score, OrgLowest, OrgMiddle, OrgHighest

## g0599（1 列）
- 見出し：Age_Band
- 例1 値：All | All | All | 16-18 | All
  - 同じ表の列：UKPRN, UPIN, Survey_Type, Question, Score, OrgLowest, OrgMiddle, OrgHighest

## g0600（1 列）
- 見出し：Survey_Type
- 例1 値：L | L | L | L | SA
  - 同じ表の列：UKPRN, UPIN, Age_Band, Question, Score, OrgLowest, OrgMiddle, OrgHighest

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
