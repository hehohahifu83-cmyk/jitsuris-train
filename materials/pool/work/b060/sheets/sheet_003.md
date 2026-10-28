# ラベル用シート 003 / 006

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：Expense Type
- 例1 値：Grant-in-aid To Arms Length Bodies | R & D External Legal Advice And Services | R & D Strategy Consultancy | Other Professional Services | R & D Current Grants To Private Sector …
  - 同じ表の列：Date of Payment, Expense Area, Supplier, Transaction Number, Amount, Supplier Post Code, Supplier Type

## g0242（1 列）
- 見出し：Expense Area
- 例1 値：Dsit - Science, Innovation And Growth -… | Dsit - Corporate Services - Dsit - Matr… | Dsit - Digital And Technology Group - D… | Dsit - Corporate Services - Dsit - Comm… | Dsit - Science, Innovation And Growth -…
  - 同じ表の列：Date of Payment, Expense Type, Supplier, Transaction Number, Amount, Supplier Post Code, Supplier Type

## g0243（1 列）
- 見出し：Supplier
- 例1 値：Advanced Research And Invention Agency … | Silicon Catalyst Uk Ltd | Npl Management Ltd | Cabinet Office | Yorkshire Services Ltd T/A Yorkshire Wa…
  - 同じ表の列：Date of Payment, Expense Type, Expense Area, Transaction Number, Amount, Supplier Post Code, Supplier Type

## g0244（1 列）
- 見出し：Supplier Post Code
- 例1 値：Tw11 0lw | Tw11 0ly | W1b 1qh | Sn2 1eu | Mk43 0al
  - 同じ表の列：Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount, Supplier Type

## g0245（3 列）
- 見出し：Main, parent or sponsoring department
- 例1 値：Department for Transport | Department for Transport | Department for Transport | Department for Transport | Department for Transport
  - 同じ表の列：Organisation Type, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…
- 例2 値：Department of Health | Department of Health | Department of Health | Department of Health | Department of Health
  - 同じ表の列：Organisation Type, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0246（1 列）
- 見出し：Date
- 例1 値：05/03/2018 | 05/02/2018 | 24/01/2018 | Nil Return | 19/02/2018
  - 同じ表の列：Minister, Type of hospitality…

## g0247（1 列）
- 見出し：Type of hospitality received
- 例1 値：Dinner | Breakfast | Dinner | Lunch | Nil Return
  - 同じ表の列：Minister, Date

## g0248（1 列）
- 見出し：Main, parent or sponsoring department
- 例1 値：Department for Work & Pensions | Department for Work & Pensions | Department for Work & Pensions | Department for Work & Pensions | Department for Work & Pensions
  - 同じ表の列：Organisation Type, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0249（1 列）
- 見出し：Payroll staff AO/AA Headcount
- 例1 値：102 | 5,607 | . | 564 | .
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0250（1 列）
- 見出し：Payroll staff EO Headcount
- 例1 値：. | 3,309 | . | 33,193 | 4,708
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0251（1 列）
- 見出し：Payroll staff SEO/HEO Headcount
- 例1 値：. | 19 | 3,806 | 5,855 | .
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0252（1 列）
- 見出し：Payroll staff Grade 6/7 Headcount
- 例1 値：171 | 683 | . | . | 143
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0253（1 列）
- 見出し：Payroll staff SCS Headcount
- 例1 値：23 | 195 | 1 | 19 | .
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff Other…, Payroll staff Total…

## g0254（1 列）
- 見出し：Payroll staff Other, unknown or unspecified Headcount
- 例1 値：287 | 5,020 | 184 | 3 | 18
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Total…

## g0255（1 列）
- 見出し：Payroll staff Total Employees Headcount
- 例1 値：164 | 287 | 81,073 | 3,589 | 37
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

## g0256（1 列）
- 見出し：Comments
- 例1 値：Payment of ethnic translation print ser… | Payment of interpreter services | Payment of ethnic translation print ser… | Payment of customer training | Payment of equipment for fraud investig…
  - 同じ表の列：Date, Supplier, Amount

## g0257（1 列）
- 見出し：Department
- 例1 値：DECC | DECC | DECC | DECC | DECC
  - 同じ表の列：Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0258（1 列）
- 見出し：Entity
- 例1 値：Department of Energy and Climate Change | Department of Energy and Climate Change | Department of Energy and Climate Change | Department of Energy and Climate Change | Department of Energy and Climate Change
  - 同じ表の列：Department, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0259（1 列）
- 見出し：Expense Type
- 例1 値：PURCHASE OF GOODS/SERVICES - ICT OUTSOU… | Purchase Of Goods/Services - Other Prof… | PURCHASE OF GOODS/SERVICES - OTHER PROF… | PURCHASE OF GOODS/SERV-ICT OUTSOURC&MAI… | PURCHASE OF GOODS/SERV-ICT OUTSOURC&MAI…
  - 同じ表の列：Department, Entity, Date of Payment, Expense Area, Supplier, Transaction Number, Amount

## g0260（1 列）
- 見出し：Expense Area
- 例1 値：Finance & Corporate Services | Energy Transformation | Energy Transformation | Energy Transformation | Energy Transformation
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Supplier, Transaction Number, Amount

## g0261（1 列）
- 見出し：Supplier
- 例1 値：SENERGY (GB) LTD | CLEAN ENERGY PROSPECTOR LTD | BRITISH INSTITUTE OF ENERGY ECONOMICS | DEPT FOR COMMUNITIES & LOCAL GOV | FCO SERVICES
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Transaction Number, Amount

## g0262（1 列）
- 見出し：Transaction Number
- 例1 値：PN10062016 | LT04062016 | JW250616D | PH310516D | JW250616D
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Amount

## g0263（1 列）
- 見出し：Departmental Family
- 例1 値：Department of Health | Department of Health | Department of Health | Department of Health | Department of Health
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Amount

## g0264（1 列）
- 見出し：Expense Type
- 例1 値：CASH FUNDING Rev Inside RAB | Research & development | Research & development | Travel & Subsistence | Service charge
  - 同じ表の列：Departmental Family, Entity, Date, Expense Area, Supplier, Amount

## g0265（1 列）
- 見出し：Expense Area
- 例1 値：NHS FC | SOCIAL CARE | INFORMATICS | NHS FINANCE PERFORMANCE & OPERATIONS | INFORMATICS
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Supplier, Amount

## g0266（1 列）
- 見出し：Supplier
- 例1 値：CENTRAL OFFICE OF INFORMATION (COI) | BT GLOBAL SERVICES LTD | AVON & WILTSHIRE MENTAL HEALTH PARTNERS… | FRONTIER ECONOMICS LTD | TRIBAL CONSULTING LTD
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Expense Area, Amount

## g0267（1 列）
- 見出し：Amount
- 例1 値：25200 | 35229.49 | 105679 | 122616.04 | 39,000,000
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Expense Area, Supplier

## g0268（1 列）
- 見出し：Supplier
- 例1 値：STATIONERY OFFICE BOOK | DAYS INN MANCHESTER CONFE | KINGS FUND | DEPARTMENT OF HEALTH | MANAGEMENT DEVELOP
  - 同じ表の列：Date, Amount

## g0269（1 列）
- 見出し：Organisation Type
- 例1 値：Executive Non-Departmental Public Body | Executive Non-Departmental Public Body | Special Health Authority | Executive Non-Departmental Public Body | Special Health Authority
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0270（3 列）
- 見出し：OrganisationLabel
- 例1 値：Derbyshire Dales District Council | Derbyshire Dales District Council | Derbyshire Dales District Council | Derbyshire Dales District Council | Derbyshire Dales District Council
  - 同じ表の列：OrganisationURI, SiteReference, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus, PermissionType
- 例2 値：Rotherham Metropolitan Borough Council | Rotherham Metropolitan Borough Council | Rotherham Metropolitan Borough Council | Rotherham Metropolitan Borough Council | Rotherham Metropolitan Borough Council
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0271（1 列）
- 見出し：PermissionType
- 例1 値：full planning permission | reserved matters, full planning permiss… | full planning permission | Development completed | full planning permission
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus

## g0272（1 列）
- 見出し：ogc_fid
- 例1 値：87 | 174 | 67 | 194 | 112
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, PlanningStatus, PermissionType

## g0273（1 列）
- 見出し：Body
- 例1 値：http://statistics.data.gov.uk/id/local-… | http://statistics.data.gov.uk/id/local-… | http://statistics.data.gov.uk/id/local-… | http://statistics.data.gov.uk/id/local-… | http://statistics.data.gov.uk/id/local-…
  - 同じ表の列：Date, Transaction Number, Amount, Supplier ID, Expense Area, Expense Type, Expense Code, Service Code

## g0274（1 列）
- 見出し：Supplier ID
- 例1 値：COX001 | TFE001 | CAN001 | CUM022 | INS021
  - 同じ表の列：Body, Date, Transaction Number, Amount, Expense Area, Expense Type, Expense Code, Service Code

## g0275（1 列）
- 見出し：Expense Area
- 例1 値：Revenue/Benefits Manager | Engineering Manager | Human Resources Manager | Communities Manager | Financial Services Manager
  - 同じ表の列：Body, Date, Transaction Number, Amount, Supplier ID, Expense Type, Expense Code, Service Code

## g0276（1 列）
- 見出し：Expense Type
- 例1 値：Land Management Contract | Legal and court costs | Promotions | Capital grants | Promotions
  - 同じ表の列：Body, Date, Transaction Number, Amount, Supplier ID, Expense Area, Expense Code, Service Code

## g0277（1 列）
- 見出し：Expense Code
- 例1 値：5505 | 2046 | 2229 | 2229 | 2079
  - 同じ表の列：Body, Date, Transaction Number, Amount, Supplier ID, Expense Area, Expense Type, Service Code

## g0278（1 列）
- 見出し：Service Code
- 例1 値：DIREGR | EDEVPR | CEMETE | FOOLIG | INFTEC
  - 同じ表の列：Body, Date, Transaction Number, Amount, Supplier ID, Expense Area, Expense Type, Expense Code

## g0279（1 列）
- 見出し：Service Label
- 例1 値：Crime & Disorder Reduction Partnership | Community Wardens | Holding Accounts | Central Expenses | Information Technology
  - 同じ表の列：Body, Date, Transaction Number, Amount, Supplier ID, Expense Area, Expense Type, Expense Code

## g0280（1 列）
- 見出し：Organisation Code
- 例1 値：http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr…
  - 同じ表の列：Expenditure Type, Expenditure Amount, Surplus Amount

## g0281（1 列）
- 見出し：Expenditure Type
- 例1 値：Other asset related costs | Utility costs | Contract with Eden Parking Services | Ground maintenance and gritting | Maintenance and repair schemes
  - 同じ表の列：Organisation Code, Expenditure Amount, Surplus Amount

## g0282（1 列）
- 見出し：Expenditure Amount
- 例1 値：-1217 | 19343 | 33011 | 27884 | 35000
  - 同じ表の列：Organisation Code, Expenditure Type, Surplus Amount

## g0283（1 列）
- 見出し：Surplus Amount
- 例1 値：103268
  - 同じ表の列：Organisation Code, Expenditure Type, Expenditure Amount

## g0284（1 列）
- 見出し：Net Amount
- 例1 値：89.93 | 3.7 | 552.23 | 24 | 4.36
  - 同じ表の列：Department, MCC, date

## g0285（1 列）
- 見出し：1
- 例1 値：28 | 131 | 11 | 81 | 2
  - 同じ表の列：Land Only, EEBC, SY452248, EEBC/10/00012, FREEHOLD, Public Open Space, 521333.20472898, 165588.29644882

## g0286（1 列）
- 見出し：Land Only
- 例1 値：Land Only | Land Only | Buildings Only | Land Only | Land/Buildings
  - 同じ表の列：1, EEBC, SY452248, EEBC/10/00012, FREEHOLD, Public Open Space, 521333.20472898, 165588.29644882

## g0287（1 列）
- 見出し：EEBC
- 例1 値：EEBC | EEBC | EEBC | EEBC | EEBC
  - 同じ表の列：1, Land Only, SY452248, EEBC/10/00012, FREEHOLD, Public Open Space, 521333.20472898, 165588.29644882

## g0288（1 列）
- 見出し：SY452248
- 例1 値：SY19250 | no landreg | SY221993 | b | SY109485
  - 同じ表の列：1, Land Only, EEBC, EEBC/10/00012, FREEHOLD, Public Open Space, 521333.20472898, 165588.29644882

## g0289（1 列）
- 見出し：EEBC/10/00012
- 例1 値：EEBC/15/00004 | EEBC/05/00006A | EEBC/05/00068 | EEBC/06/00020 | EEBC/15/00044
  - 同じ表の列：1, Land Only, EEBC, SY452248, FREEHOLD, Public Open Space, 521333.20472898, 165588.29644882

## g0290（1 列）
- 見出し：FREEHOLD
- 例1 値：FREEHOLD | FREEHOLD | FREEHOLD | FREEHOLD | FREEHOLD
  - 同じ表の列：1, Land Only, EEBC, SY452248, EEBC/10/00012, Public Open Space, 521333.20472898, 165588.29644882

## g0291（1 列）
- 見出し：Public Open Space
- 例1 値：Recreation Ground | Public Car Park | Park | Amenity Land | Public Open Space
  - 同じ表の列：1, Land Only, EEBC, SY452248, EEBC/10/00012, FREEHOLD, 521333.20472898, 165588.29644882

## g0292（1 列）
- 見出し：521333.20472898
- 例1 値：521986.90048661 | 521236.78607146 | 519139.65357864 | 520847.38406479 | 520063.02680174
  - 同じ表の列：1, Land Only, EEBC, SY452248, EEBC/10/00012, FREEHOLD, Public Open Space, 165588.29644882

## g0293（1 列）
- 見出し：165588.29644882
- 例1 値：161207.21354948 | 160795.10825723 | 161721.79872774 | 161128.24387555 | 163564.19637923
  - 同じ表の列：1, Land Only, EEBC, SY452248, EEBC/10/00012, FREEHOLD, Public Open Space, 521333.20472898

## g0294（1 列）
- 見出し：Royal Avenue
- 例1 値：Roy Richmond Way | High Street | Park Avenue West | Salisbury Road | West Hill
  - 同じ表の列：1, Land Only, EEBC, SY452248, EEBC/10/00012, FREEHOLD, Public Open Space, 521333.20472898

## g0295（7 列）
- 見出し：Entity
- 例1 値：Equality and Human Rights Commission | Equality and Human Rights Commission | Equality and Human Rights Commission | Equality and Human Rights Commission | Equality and Human Rights Commission
  - 同じ表の列：Department family, Allocation Date, Expense type, Expense Area, Supplier, Transaction Number, Amount in Sterling
- 例2 値：Office of Rail and Road | Office of Rail and Road | Office of Rail and Road | Office of Rail and Road | Office of Rail and Road
  - 同じ表の列：Department family, Date of payment, Expense Code, Expense type, Cost Centre, Expense area, Supplier, Transaction Number

## g0296（1 列）
- 見出し：Allocation Date
- 例1 値：01/06/2011 | 01/06/2011 | 14/06/2011 | 21/06/2011 | 21/06/2011
  - 同じ表の列：Department family, Entity, Expense type, Expense Area, Supplier, Transaction Number, Amount in Sterling

## g0297（1 列）
- 見出し：Expense type
- 例1 値：Accommodation | Recruitment Advertising | Agency Staff | BT Non Managed Services | Conference Set Up/Equipment Costs Board…
  - 同じ表の列：Department family, Entity, Allocation Date, Expense Area, Supplier, Transaction Number, Amount in Sterling

## g0298（1 列）
- 見出し：Expense Area
- 例1 値：Regulation - Disability Programme | Corporate Management - Grants Unit | Corporate Management - People | Corporate Management - Buildings | Corporate Management - Finance
  - 同じ表の列：Department family, Entity, Allocation Date, Expense type, Supplier, Transaction Number, Amount in Sterling

## g0299（1 列）
- 見出し：Supplier
- 例1 値：DWP | Morgan Hunt UK Ltd | Event Management Training Limited | Department For Communities & Local Gove… | Cheshire Hw Rec
  - 同じ表の列：Department family, Entity, Allocation Date, Expense type, Expense Area, Transaction Number, Amount in Sterling

## g0300（1 列）
- 見出し：Transaction Number
- 例1 値：iPOS Invoice 40658 | iPOS Invoice 40404 | iPOS Invoice 40551 | iPOS Invoice 40254 | iPOS Invoice 40753
  - 同じ表の列：Department family, Entity, Allocation Date, Expense type, Expense Area, Supplier, Amount in Sterling

## g0301（2 列）
- 見出し：Amount in Sterling
- 例1 値：767.35 | 576 | 9,613.13 | 1,324.80 | 8,430.00
  - 同じ表の列：Department family, Entity, Allocation Date, Expense type, Expense Area, Supplier, Transaction Number
- 例2 値：1,350.00 | 842.55 | 9,249.98 | 983.41 | 500
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number

## g0302（1 列）
- 見出し：Department
- 例1 値：Foreign and Commonwealth Office | Foreign and Commonwealth Office | NOTES: | Foreign and Commonwealth Office | Foreign and Commonwealth Office
  - 同じ表の列：Basis for expenditu…, Value (」M), Total Value Request…, Total Value Approve…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…

## g0303（1 列）
- 見出し：Basis for expenditure approval
- 例1 値：Business critical/front line recruitment | Business critical/front line recruitment | Business critical/front line recruitment | Business critical/front line recruitment | Business critical/front line recruitment
  - 同じ表の列：Department, Value (」M), Total Value Request…, Total Value Approve…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…

## g0304（1 列）
- 見出し：Value (」M)
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：Department, Basis for expenditu…, Total Value Request…, Total Value Approve…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…

## g0305（1 列）
- 見出し：Total Value Requested (」M)
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：Department, Basis for expenditu…, Value (」M), Total Value Approve…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…

## g0306（1 列）
- 見出し：Total Value Approved (」M)
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：Department, Basis for expenditu…, Value (」M), Total Value Request…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…

## g0307（1 列）
- 見出し：Civil Service Grade (FTE) AA/AO
- 例1 値：0 | 0 | 3 | 9 | 0
  - 同じ表の列：Department, Basis for expenditu…, Value (」M), Total Value Request…, Total Value Approve…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…

## g0308（1 列）
- 見出し：Civil Service Grade (FTE) EO
- 例1 値：0 | 1 | 9 | 12 | 0
  - 同じ表の列：Department, Basis for expenditu…, Value (」M), Total Value Request…, Total Value Approve…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…

## g0309（1 列）
- 見出し：Civil Service Grade (FTE) HEO
- 例1 値：0 | 2 | 0 | 0 | 10
  - 同じ表の列：Department, Basis for expenditu…, Value (」M), Total Value Request…, Total Value Approve…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…

## g0310（1 列）
- 見出し：Civil Service Grade (FTE) SEO
- 例1 値：2 | 0 | 0 | 0 | 0
  - 同じ表の列：Department, Basis for expenditu…, Value (」M), Total Value Request…, Total Value Approve…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…

## g0311（1 列）
- 見出し：Civil Service Grade (FTE) Grade 6/7
- 例1 値：0 | 0 | 0 | 5.5 | 5
  - 同じ表の列：Department, Basis for expenditu…, Value (」M), Total Value Request…, Total Value Approve…, Civil Service Grade…, Civil Service Grade…, Civil Service Grade…

## g0312（1 列）
- 見出し：Region
- 例1 値：Eastern Europe & Central Asia | Americas | Americas | Africa | Americas
  - 同じ表の列：Country/Territory, Location (City), Type of Post, y, x

## g0313（1 列）
- 見出し：Country/Territory
- 例1 値：Estonia | Greece | Lebanon | India | China
  - 同じ表の列：Region, Location (City), Type of Post, y, x

## g0314（1 列）
- 見出し：Location (City)
- 例1 値：Hamilton | Juba | Guatemala City | Ibiza | Vienna
  - 同じ表の列：Region, Country/Territory, Type of Post, y, x

## g0315（1 列）
- 見出し：Type of Post
- 例1 値：British High Commission | British Embassy Office | British Embassy | British High Commission | British Office
  - 同じ表の列：Region, Country/Territory, Location (City), y, x

## g0316（1 列）
- 見出し：y
- 例1 値：44.94 | 42.44 | 33.97 | -8.7 | 26.33
  - 同じ表の列：Region, Country/Territory, Location (City), Type of Post, x

## g0317（1 列）
- 見出し：x
- 例1 値：25.3 | -64.78 | -62.21 | 71.42 | 4.86
  - 同じ表の列：Region, Country/Territory, Location (City), Type of Post, y

## g0318（1 列）
- 見出し：source_base_path
- 例1 値：/apply-blue-badge | /change-name-address-v5c | /annual-test-for-lorries-buses-and-trai… | /blackouts-and-driving | /apply-for-council-housing
  - 同じ表の列：sink_base_path, link_type

## g0319（1 列）
- 見出し：sink_base_path
- 例1 値：/vehicle-approval | /book-driving-test | /reapply-driving-licence-medical-condit… | /health-conditions-and-driving | /passport-services-disabled
  - 同じ表の列：source_base_path, link_type

## g0320（1 列）
- 見出し：link_type
- 例1 値：related_link | related_link | related_link | related_link | related_link
  - 同じ表の列：source_base_path, sink_base_path

## g0321（1 列）
- 見出し：EmployerId
- 例1 値：16326 | 1812 | 1829 | 1386 | 16327
  - 同じ表の列：CompanyNumber, SicCodes, DiffMeanHourlyPerce…, DiffMedianHourlyPer…, DiffMeanBonusPercent, DiffMedianBonusPerc…, MaleBonusPercent, FemaleBonusPercent

## g0322（1 列）
- 見出し：CompanyNumber
- 例1 値：01518983 | 00278802 | 04788424 | 06655187 | 09942425
  - 同じ表の列：EmployerId, SicCodes, DiffMeanHourlyPerce…, DiffMedianHourlyPer…, DiffMeanBonusPercent, DiffMedianBonusPerc…, MaleBonusPercent, FemaleBonusPercent

## g0323（1 列）
- 見出し：SicCodes
- 例1 値：56290 | 96090 | 1, 85320 | 64191 | 13921, 31090
  - 同じ表の列：EmployerId, CompanyNumber, DiffMeanHourlyPerce…, DiffMedianHourlyPer…, DiffMeanBonusPercent, DiffMedianBonusPerc…, MaleBonusPercent, FemaleBonusPercent

## g0324（1 列）
- 見出し：DiffMeanHourlyPercent
- 例1 値：12.80 | 37.00 | 17.70 | 6.20 | 46.80
  - 同じ表の列：EmployerId, CompanyNumber, SicCodes, DiffMedianHourlyPer…, DiffMeanBonusPercent, DiffMedianBonusPerc…, MaleBonusPercent, FemaleBonusPercent

## g0325（1 列）
- 見出し：DiffMedianHourlyPercent
- 例1 値：37.00 | 46.70 | -9.90 | 3.70 | 30.00
  - 同じ表の列：EmployerId, CompanyNumber, SicCodes, DiffMeanHourlyPerce…, DiffMeanBonusPercent, DiffMedianBonusPerc…, MaleBonusPercent, FemaleBonusPercent

## g0326（1 列）
- 見出し：DiffMeanBonusPercent
- 例1 値：31.00 | 0.00 | 30.20 | 35.60 | 0.00
  - 同じ表の列：EmployerId, CompanyNumber, SicCodes, DiffMeanHourlyPerce…, DiffMedianHourlyPer…, DiffMedianBonusPerc…, MaleBonusPercent, FemaleBonusPercent

## g0327（1 列）
- 見出し：DiffMedianBonusPercent
- 例1 値：3.30 | 0.00 | 74.20 | 28.00 | 0.00
  - 同じ表の列：EmployerId, CompanyNumber, SicCodes, DiffMeanHourlyPerce…, DiffMedianHourlyPer…, DiffMeanBonusPercent, MaleBonusPercent, FemaleBonusPercent

## g0328（1 列）
- 見出し：MaleBonusPercent
- 例1 値：80.70 | 8.30 | 74.00 | 90.30 | 82.00
  - 同じ表の列：EmployerId, CompanyNumber, SicCodes, DiffMeanHourlyPerce…, DiffMedianHourlyPer…, DiffMeanBonusPercent, DiffMedianBonusPerc…, FemaleBonusPercent

## g0329（1 列）
- 見出し：FemaleBonusPercent
- 例1 値：0.00 | 96.40 | 17.70 | 65.50 | 28.10
  - 同じ表の列：EmployerId, CompanyNumber, SicCodes, DiffMeanHourlyPerce…, DiffMedianHourlyPer…, DiffMeanBonusPercent, DiffMedianBonusPerc…, MaleBonusPercent

## g0330（1 列）
- 見出し：MaleLowerQuartile
- 例1 値：71.20 | 23.00 | 53.20 | 1.00 | 20.00
  - 同じ表の列：EmployerId, CompanyNumber, SicCodes, DiffMeanHourlyPerce…, DiffMedianHourlyPer…, DiffMeanBonusPercent, DiffMedianBonusPerc…, MaleBonusPercent

## g0331（1 列）
- 見出し：Transactions: Date
- 例1 値：15/01/2013 | 21/01/2013 | 09/01/2013 | 24/01/2013 | 17/01/2013
  - 同じ表の列：Transactions Amount…, More Details

## g0332（1 列）
- 見出し：Transactions Amount Gross
- 例1 値：540.00 | 606.00 | 933.60 | 640.09 | 689.40
  - 同じ表の列：Transactions: Date, More Details

## g0333（1 列）
- 見出し：More Details
- 例1 値：Disability Training for specific staff | Franking Machine Centormail Labels | Dongles monthly rental | Security Badges | Vodafone Bill Payments
  - 同じ表の列：Transactions: Date, Transactions Amount…

## g0334（1 列）
- 見出し：Department family
- 例1 値：HM Procurator General and Treasury Soli… | HM Procurator General and Treasury Soli… | HM Procurator General and Treasury Soli… | HM Procurator General and Treasury Soli… | HM Procurator General and Treasury Soli…
  - 同じ表の列：Entity, Date, Expense type, Expense area, Supplier, Transaction number, Amount, Supplier Type

## g0335（1 列）
- 見出し：Entity
- 例1 値：The Treasury Solicitor's Department | The Treasury Solicitor's Department | The Treasury Solicitor's Department | Attorney General's Office | The Treasury Solicitor's Department
  - 同じ表の列：Department family, Date, Expense type, Expense area, Supplier, Transaction number, Amount, Supplier Type

## g0336（1 列）
- 見出し：Expense type
- 例1 値：Agency Staff: Legal | Maintenance: Accommodation | Agency Staff: Legal | Advisory Counsel Fees | Expert Report
  - 同じ表の列：Department family, Entity, Date, Expense area, Supplier, Transaction number, Amount, Supplier Type

## g0337（3 列）
- 見出し：Expense area
- 例1 値：Litigation Division | Defra Legal | Litigation Division | Defra Legal | Litigation Division
  - 同じ表の列：Department family, Entity, Date, Expense type, Supplier, Transaction number, Amount, Supplier Type
- 例2 値：Home Office | Home Office | Home Office | Home Office | Home Office
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Transaction Number, Spend

## g0338（1 列）
- 見出し：Supplier
- 例1 値：HM Revenue and Customs | Jones Lang Lasalle | Altodigital | Allen & Overy LLP | Redfern Travel Ltd
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Transaction number, Amount, Supplier Type

## g0339（3 列）
- 見出し：Expenditure Type
- 例1 値：Administration | Administration | Administration | Administration | Administration
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Supplier, Transaction number, Amount
- 例2 値：Administration | Administration | Administration | Administration | Administration
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0340（1 列）
- 見出し：SiteReference
- 例1 値：BLR_031 | BLR_084 | BLR_027 | BLR_037 | BLR_050
  - 同じ表の列：OrganisationURI, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0341（3 列）
- 見出し：OrganisationURI
- 例1 値：http://opendatacommunities.org/id/geogr… | http://opendatacommunities.org/id/geogr… | http://opendatacommunities.org/id/geogr… | http://opendatacommunities.org/id/geogr… | http://opendatacommunities.org/id/geogr…
  - 同じ表の列：SiteReference, SiteplanURL, GeoX, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：http://opendatacommunities.org/id/geogr… | http://opendatacommunities.org/id/geogr… | http://opendatacommunities.org/id/geogr… | http://opendatacommunities.org/id/geogr… | http://opendatacommunities.org/id/geogr…
  - 同じ表の列：SiteReference, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0342（4 列）
- 見出し：GeoX
- 例1 値：579085.751 | 578477.5481 | 579410.8093 | 581619.79 | 580283.5
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：517196.59 | 517408.31 | 516470.03 | 512613.77 | 512709.76
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoY, Hectares, Deliverable

## g0343（1 列）
- 見出し：PermissionDate
- 例1 値：21/01/2020 | 29/03/2018 | 11/11/2009 | 21.11.2023 | 20/02/2020
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoX, GeoY, Hectares, PlanningStatus, PermissionType

## g0344（1 列）
- 見出し：Main department
- 例1 値：Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence
  - 同じ表の列：Organisation, Delegated grades, SCS on standard con…, Information for SCS…, Comments

## g0345（1 列）
- 見出し：Organisation
- 例1 値：Defence Science and Technology Laborato… | Defence Electronic and Components Agency | Royal Fleet Auxilary | Defence Equipment and Support | UK Hydrographic Office
  - 同じ表の列：Main department, Delegated grades, SCS on standard con…, Information for SCS…, Comments

## g0346（1 列）
- 見出し：Delegated grades
- 例1 値：」208,453,917 | Annual Paybill (delegated grades for fi… | 」468,236,981 | 」1,053,041,472 | 」89,399,301
  - 同じ表の列：Main department, Organisation, SCS on standard con…, Information for SCS…, Comments

## g0347（1 列）
- 見出し：SCS on standard contracts
- 例1 値：Annual SCS Paybill for those SCS on sta… | 」16,469,061 | 」18,099,035
  - 同じ表の列：Main department, Organisation, Delegated grades, Information for SCS…, Comments

## g0348（1 列）
- 見出し：Information for SCS on non-standard terms
- 例1 値：Number of SCS on non-standard performan… | 4
  - 同じ表の列：Main department, Organisation, Delegated grades, SCS on standard con…, Comments

## g0349（1 列）
- 見出し：Comments
- 例1 値：MOD ceased paying end of year award in … | Please note the Dstl Performance year /… | UKHO's Team Performance Award is payabl… | SDA separated from DE&S on 1 April 2018… | There were 424 employees who qualified …
  - 同じ表の列：Main department, Organisation, Delegated grades, SCS on standard con…, Information for SCS…

## g0350（1 列）
- 見出し：Financial Year and quarter
- 例1 値：22/23 Q3 | 19/20 Q4 | 21/22 Q4 | 23/24 Q1 | 19/20 Q1
  - 同じ表の列：Percentage of invoi…, Percentage of invoi…

## g0351（1 列）
- 見出し：Percentage of invoices paid within 5 days
- 例1 値：84.56% | 86.09% | 79.27% | 81.99% | 79.96%
  - 同じ表の列：Financial Year and …, Percentage of invoi…

## g0352（1 列）
- 見出し：Percentage of invoices paid within 30 days
- 例1 値：93.76% | 88.00% | 91.11% | 92.00% | 91.24%
  - 同じ表の列：Financial Year and …, Percentage of invoi…

## g0353（1 列）
- 見出し：SiteReference
- 例1 値：GL056 | NM034 | BV002 | HPK/2018/0089 | HPK/2017/0232
  - 同じ表の列：OrganisationURI, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0354（1 列）
- 見出し：Row
- 例1 値：7 | 3 | 8 | 4 | 2
  - 同じ表の列：What is required, Reason For Inclusion, Additional Informat…, Inclusion Status

## g0355（1 列）
- 見出し：What is required
- 例1 値：Total number of trade union representat… | Unique code of identify organisation | Total number (full time equivalent) of … | A basic estimate of spending on unions … | Name of Authority
  - 同じ表の列：Row, Reason For Inclusion, Additional Informat…, Inclusion Status

## g0356（1 列）
- 見出し：Reason For Inclusion
- 例1 値：Requested in the Code | Identifies Public Organisation | Requested in the Code | Requested in the Code | Requested in the Code
  - 同じ表の列：Row, What is required, Additional Informat…, Inclusion Status

## g0357（1 列）
- 見出し：Additional Information
- 例1 値：0 | 0 | 0 | 0 | High Peak Borough Council
  - 同じ表の列：Row, What is required, Reason For Inclusion, Inclusion Status

## g0358（1 列）
- 見出し：Inclusion Status
- 例1 値：Mandated | Mandated | Mandated | Optional | Mandated
  - 同じ表の列：Row, What is required, Reason For Inclusion, Additional Informat…

## g0359（2 列）
- 見出し：Department Family
- 例1 値：Home Office | Home Office | Home Office | Home Office | Home Office
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Transaction Number, Spend
- 例2 値：HM Treasury | HM Treasury | HM Treasury | HM Treasury | HM Treasury
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0360（1 列）
- 見出し：Entity
- 例1 値：Home Office | Home Office | Home Office | Home Office | Home Office
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Transaction Number, Spend

## 答えの雛形

```
g0241	
g0242	
g0243	
g0244	
g0245	
g0246	
g0247	
g0248	
g0249	
g0250	
g0251	
g0252	
g0253	
g0254	
g0255	
g0256	
g0257	
g0258	
g0259	
g0260	
g0261	
g0262	
g0263	
g0264	
g0265	
g0266	
g0267	
g0268	
g0269	
g0270	
g0271	
g0272	
g0273	
g0274	
g0275	
g0276	
g0277	
g0278	
g0279	
g0280	
g0281	
g0282	
g0283	
g0284	
g0285	
g0286	
g0287	
g0288	
g0289	
g0290	
g0291	
g0292	
g0293	
g0294	
g0295	
g0296	
g0297	
g0298	
g0299	
g0300	
g0301	
g0302	
g0303	
g0304	
g0305	
g0306	
g0307	
g0308	
g0309	
g0310	
g0311	
g0312	
g0313	
g0314	
g0315	
g0316	
g0317	
g0318	
g0319	
g0320	
g0321	
g0322	
g0323	
g0324	
g0325	
g0326	
g0327	
g0328	
g0329	
g0330	
g0331	
g0332	
g0333	
g0334	
g0335	
g0336	
g0337	
g0338	
g0339	
g0340	
g0341	
g0342	
g0343	
g0344	
g0345	
g0346	
g0347	
g0348	
g0349	
g0350	
g0351	
g0352	
g0353	
g0354	
g0355	
g0356	
g0357	
g0358	
g0359	
g0360	
```
