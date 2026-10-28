# ラベル用シート 001 / 004

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Long/ Short Stay
- 例1 値：Long Stay | Long Stay | Long Stay | Long Stay | Long Stay
  - 同じ表の列：Ticket Machine Numb…, No. of ordinary bays, No. of Disabled bays, Motorcycle Bays, Restrictions, No. of ticket machi…, Recycle Point

## g0002（1 列）
- 見出し：Ticket Machine Number
- 例1 値：15W/16W | 13W/14W | 06W | 04R/05R | NO MACHINE FREE PARKING
  - 同じ表の列：Long/ Short Stay, No. of ordinary bays, No. of Disabled bays, Motorcycle Bays, Restrictions, No. of ticket machi…, Recycle Point

## g0003（1 列）
- 見出し：No. of ordinary bays
- 例1 値：16 | 84 | 168 | 37 | 69
  - 同じ表の列：Long/ Short Stay, Ticket Machine Numb…, No. of Disabled bays, Motorcycle Bays, Restrictions, No. of ticket machi…, Recycle Point

## g0004（1 列）
- 見出し：No. of Disabled bays
- 例1 値：18 | 4 | 18 | 7 | 3
  - 同じ表の列：Long/ Short Stay, Ticket Machine Numb…, No. of ordinary bays, Motorcycle Bays, Restrictions, No. of ticket machi…, Recycle Point

## g0005（1 列）
- 見出し：Motorcycle Bays
- 例1 値：0 | 0 | 0 | 0 | 1
  - 同じ表の列：Long/ Short Stay, Ticket Machine Numb…, No. of ordinary bays, No. of Disabled bays, Restrictions, No. of ticket machi…, Recycle Point

## g0006（1 列）
- 見出し：Restrictions
- 例1 値：Suitable for high Sided Vehicles & Coac… | Suitable for high Sided Vehicles & Moto… | Height Barrier | Height Barrier | Height Barrier
  - 同じ表の列：Long/ Short Stay, Ticket Machine Numb…, No. of ordinary bays, No. of Disabled bays, Motorcycle Bays, No. of ticket machi…, Recycle Point

## g0007（1 列）
- 見出し：No. of ticket machines in car park
- 例1 値：16 | 1 | 1 | 2 | 0
  - 同じ表の列：Long/ Short Stay, Ticket Machine Numb…, No. of ordinary bays, No. of Disabled bays, Motorcycle Bays, Restrictions, Recycle Point

## g0008（1 列）
- 見出し：Recycle Point
- 例1 値：No | No | Yes | No | No
  - 同じ表の列：Long/ Short Stay, Ticket Machine Numb…, No. of ordinary bays, No. of Disabled bays, Motorcycle Bays, Restrictions, No. of ticket machi…

## g0009（1 列）
- 見出し：Originating Authority
- 例1 値：Bassetlaw District Council | Bassetlaw District Council | Bassetlaw District Council | Bassetlaw District Council | Bassetlaw District Council
  - 同じ表の列：2014/15

## g0010（1 列）
- 見出し：2014/15
- 例1 値：42 | 416779.83 | 252 | 0 | 3.5
  - 同じ表の列：Originating Authori…

## g0011（1 列）
- 見出し：PORTFOLIO
- 例1 値：Finance, Efficiency & Assets | Other | N'Hood & Env. Health Services | Planning, Econ. Dev. & Housing | Corp Serv, Perform. & Leisure
  - 同じ表の列：COST CENTRE, EXPENDITURE CLASS, POST. DATE, AMOUNT, REF.

## g0012（1 列）
- 見出し：COST CENTRE
- 例1 値：Building Control Services | Housing Strategy & Enabl. Role | C.Tax Billing, Coll & Recovery | General Fund Balance Sheet | General Fund Balance Sheet
  - 同じ表の列：PORTFOLIO, EXPENDITURE CLASS, POST. DATE, AMOUNT, REF.

## g0013（1 列）
- 見出し：EXPENDITURE CLASS
- 例1 値：Seminars & Short Training | Deductions - Avc | Gas | Seminars & Short Training | Electricity
  - 同じ表の列：PORTFOLIO, COST CENTRE, POST. DATE, AMOUNT, REF.

## g0014（1 列）
- 見出し：POST. DATE
- 例1 値：08/01/2013 | 15/01/2013 | 15/01/2013 | 28/01/2013 | 03/01/2013
  - 同じ表の列：PORTFOLIO, COST CENTRE, EXPENDITURE CLASS, AMOUNT, REF.

## g0015（2 列）
- 見出し：AMOUNT
- 例1 値：11,250.00 | 250.00 | 1,340.10 | 1,746.18 | 480.00
  - 同じ表の列：PORTFOLIO, COST CENTRE, EXPENDITURE CLASS, POST. DATE, REF.
- 例2 値：314.57 | 792.29 | 177.09 | 1,379.39 | 60.68
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, SME, Transaction Number

## g0016（1 列）
- 見出し：REF.
- 例1 値：89516 | 89576 | 89497 | 88197 | 89485
  - 同じ表の列：PORTFOLIO, COST CENTRE, EXPENDITURE CLASS, POST. DATE, AMOUNT

## g0017（1 列）
- 見出し：Staff
- 例1 値：Pay & Display | Administration Fees | Parking Permits | Total Income | Support Services
  - 同じ表の列：131,953

## g0018（1 列）
- 見出し：131,953
- 例1 値：798,907 | 184,700 | 74,585 | 3,849,683 | Net Cost 2013-14
  - 同じ表の列：Staff

## g0019（1 列）
- 見出し：Grant recipient
- 例1 値：University of Gloucestershire Students’… | Charlton Kings Parish Council | Cheltenham Polish Tenants and Residents… | Albemarle Orchard Garden Group | Youth and Community Services
  - 同じ表の列：Registration number, amount allocated, Date of award, Time period

## g0020（1 列）
- 見出し：Registration number
- 例1 値：Constituted Voluntary organisation | charity number 1146790 | Company number 4035270 | Charity number 1133186 | Constituted organisation with an adviso…
  - 同じ表の列：Grant recipient, amount allocated, Date of award, Time period

## g0021（1 列）
- 見出し：amount allocated
- 例1 値：275 | 300 | 2970 | 300 | 1,300
  - 同じ表の列：Grant recipient, Registration number, Date of award, Time period

## g0022（1 列）
- 見出し：Date of award
- 例1 値：15-Jul-14 | 15-Jul-14 | 15-Jul-14 | 15-Jul-14 | 15-Jul-14
  - 同じ表の列：Grant recipient, Registration number, amount allocated, Time period

## g0023（1 列）
- 見出し：Time period
- 例1 値：12 months from award | 12 months from award | 12 months from award | 12 months from award | 12 months from award
  - 同じ表の列：Grant recipient, Registration number, amount allocated, Date of award

## g0024（1 列）
- 見出し：Number of employees who were relevant union officials
- 例1 値：Percentage of pay bill spent on facilit… | Total cost of facility time | 51-99% | 1-50% | Percentage of time spent on facility ti…
  - 同じ表の列：62

## g0025（1 列）
- 見出し：62
- 例1 値：0 | 0 | 0 | 0.09 | Number of employees
  - 同じ表の列：Number of employees…

## g0026（1 列）
- 見出し：Period
- 例1 値：1997Q3 | 2009Q3 | 1989Q2 | 2013Q4 | 1992Q2
  - 同じ表の列：Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA

## g0027（2 列）
- 見出し：Year
- 例1 値：2014 | 1991 | 1990 | 2001 | 1997
  - 同じ表の列：Period, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA
- 例2 値：1997 | 1991 | 2014 | 2002 | 2000
  - 同じ表の列：GHG, GHG Grouped, IPCC Code, National Communicat…, National Communicat…, National Communicat…, Source, National Communicat…

## g0028（1 列）
- 見出し：Quarter
- 例1 値：Q1 | Q3 | Q4 | Q3 | Q1
  - 同じ表の列：Period, Year, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA

## g0029（1 列）
- 見出し：EW_Total_Company_SA
- 例1 値：4205 | [x] | 3520 | 4382 | 4627
  - 同じ表の列：Period, Year, Quarter, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA

## g0030（1 列）
- 見出し：EW_Compulsory_SA
- 例1 値：1384 | 1679 | 1210 | 940 | 1234
  - 同じ表の列：Period, Year, Quarter, EW_Total_Company_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA

## g0031（1 列）
- 見出し：EW_CVL_SA
- 例1 値：2476 | 2382 | 1812 | 2029 | [x]
  - 同じ表の列：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA

## g0032（1 列）
- 見出し：EW_Admin_SA
- 例1 値：172 | 322 | [x] | [x] | [x]
  - 同じ表の列：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_CVA_SA, EW_Receiver_SA

## g0033（1 列）
- 見出し：EW_CVA_SA
- 例1 値：127 | 125 | 25 | [x] | 77
  - 同じ表の列：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_Receiver_SA

## g0034（1 列）
- 見出し：EW_Receiver_SA
- 例1 値：[x] | [x] | [x] | 249 | [x]
  - 同じ表の列：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA

## g0035（1 列）
- 見出し：EW_Total_Company_NSA
- 例1 値：4997 | 4323 | 6216 | 4279 | 4075
  - 同じ表の列：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA

## g0036（2 列）
- 見出し：Organisation type
- 例1 値：Executive agency | Executive non-departmental public body | Executive agency | Executive non-departmental public body | Executive non-departmental public body
  - 同じ表の列：Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…
- 例2 値：Executive Agency | Executive Agency | Executive Non-Departmental Public Body | Executive Non-Departmental Public Body | Ministerial Department
  - 同じ表の列：Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0037（1 列）
- 見出し：Main, parent or sponsoring department:
- 例1 値：Department for Business, Energy & Indus… | Department for Business, Energy & Indus… | Department for Business, Energy & Indus… | Department for Business, Energy & Indus… | Department for Business, Energy & Indus…
  - 同じ表の列：Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…

## g0038（1 列）
- 見出し：Payroll staff
- 例1 値：230 | 62 | Headcount | 449 | 17
  - 同じ表の列：Organisation type, Main, parent or spo…, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…

## g0039（1 列）
- 見出し：Number of non-payroll staff (contingent labour and consultan
- 例1 値：3 | 4 | 0 | 3 | 4
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…

## g0040（1 列）
- 見出し：Grand Total (workforce numbers)
- 例1 値：2,181 | 227 | 271 | 1,531 | 319
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…

## g0041（1 列）
- 見出し：Payroll staff costs
- 例1 値：」5,532,179.00 | 」371,433.32 | 」3,012,912.00 | 」1,844,964.10 | 65481.62
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…

## g0042（1 列）
- 見出し：Non-Payroll staff (contingent labour/consultancy) costs
- 例1 値：」63,344.00 | 428193.41 | 」2,256.66 | 」1,254,948.94 | 」5,405.40
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Grand Total paybill…, Comments (NB: These…

## g0043（1 列）
- 見出し：Grand Total paybill/staffing (payroll and non-payroll) costs
- 例1 値：」14,305,612.24 | 」561,980.17 | 」190,606.57 | 」4,168,819.00 | 」2,880,799.82
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Comments (NB: These…

## g0044（1 列）
- 見出し：Comments (NB: These will be published alongside your row of
- 例1 値：Year end accounts are still being compl… | Allowances included within Salary costs. | Met Office do not use Grades. | Data is correct
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0045（1 列）
- 見出し：Which one of the following sources provided most of your inf
- 例1 値：PDG members' websites | PDG members' websites | PDG members' websites | Other - please specify (free text box b… | Other - please specify (free text box b…
  - 同じ表の列：Which one of the fo…, Before reading this…, To what extent are …, How easy did you fi…, How easy did you fi…, How easy did you fi…, How easy did you fi…, Do you consider any…

## g0046（1 列）
- 見出し：Which one of the following sources provided most of your inf
- 例1 値：Owen Boswarva twitter; OpenStreetMap ma… | Local Authority Data under EIR | Local Authority data under EIR | Local Authority Data (under EIR) | Local Authority data under EIR
  - 同じ表の列：Which one of the fo…, Before reading this…, To what extent are …, How easy did you fi…, How easy did you fi…, How easy did you fi…, How easy did you fi…, Do you consider any…

## g0047（1 列）
- 見出し：Before reading this survey, to what extent were you aware th
- 例1 値：Somewhat aware | Somewhat aware | Fully aware | Somewhat aware | Fully aware
  - 同じ表の列：Which one of the fo…, Which one of the fo…, To what extent are …, How easy did you fi…, How easy did you fi…, How easy did you fi…, How easy did you fi…, Do you consider any…

## g0048（1 列）
- 見出し：To what extent are you aware that PDG members make large amo
- 例1 値：Fully aware | Somewhat aware | Fully aware | Somewhat aware | Somewhat aware
  - 同じ表の列：Which one of the fo…, Which one of the fo…, Before reading this…, How easy did you fi…, How easy did you fi…, How easy did you fi…, How easy did you fi…, Do you consider any…

## g0049（1 列）
- 見出し：How easy did you find it to identify and use the free data s
- 例1 値：Somewhat easy | Somewhat easy | Somewhat hard | Somewhat easy | Somewhat hard
  - 同じ表の列：Which one of the fo…, Which one of the fo…, Before reading this…, To what extent are …, How easy did you fi…, How easy did you fi…, How easy did you fi…, Do you consider any…

## g0050（1 列）
- 見出し：How easy did you find it to identify and use the free data s
- 例1 値：Great publication of asset lists is req… | GREAT PUBLICATION OF ASSET LISTS IS REQ… | Need asset list published and commercia… | Licence terms are often so opaque that … | publication of asset list is required
  - 同じ表の列：Which one of the fo…, Which one of the fo…, Before reading this…, To what extent are …, How easy did you fi…, How easy did you fi…, How easy did you fi…, Do you consider any…

## g0051（1 列）
- 見出し：How easy did you find it to identify and use those data sets
- 例1 値：Very hard | Somewhat hard | Very hard | Somewhat hard | Not applicable (have never used paid fo…
  - 同じ表の列：Which one of the fo…, Which one of the fo…, Before reading this…, To what extent are …, How easy did you fi…, How easy did you fi…, How easy did you fi…, Do you consider any…

## g0052（1 列）
- 見出し：How easy did you find it to identify and use those data sets
- 例1 値：I had to buy become a sublicensee an Or… | greater publication of asset lists is r… | greater publication of asset lists is r… | great publication of asset lists is req… | Great publication of asset lists is req…
  - 同じ表の列：Which one of the fo…, Which one of the fo…, Before reading this…, To what extent are …, How easy did you fi…, How easy did you fi…, How easy did you fi…, Do you consider any…

## g0053（1 列）
- 見出し：Do you consider any of the following factors a requirement/p
- 例1 値：APIs | APIs, Linked Data, Supporting tools | APIs, Linked Data, A contact point to s… | A contact point to seek advice | A contact point to seek advice
  - 同じ表の列：Which one of the fo…, Which one of the fo…, Before reading this…, To what extent are …, How easy did you fi…, How easy did you fi…, How easy did you fi…, How easy did you fi…

## g0054（1 列）
- 見出し：Do you consider any of the following factors a requirement/p
- 例1 値：No large financial commitment (OS wante… | All helpful.BUT all less needed if the … | Knowing the data is available in the fi… | Simple, plain English, standardised lic… | Tools for non-technical experts to expl…
  - 同じ表の列：Which one of the fo…, Which one of the fo…, Before reading this…, To what extent are …, How easy did you fi…, How easy did you fi…, How easy did you fi…, How easy did you fi…

## g0055（1 列）
- 見出し：Main Department
- 例1 値：Department for Business, Innovation & S… | Department for Business, Innovation & S… | Department for Business, Innovation & S… | Department for Business, Innovation & S… | Department for Business, Innovation & S…
  - 同じ表の列：Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, In-Year - Number of…, In-Year - Median NC…, End of Year - Cost …

## g0056（1 列）
- 見出し：Organisation
- 例1 値：Business, Innovation & Skills | Meteorological Office | Insolvency Service | UK Intellectual Property Office | Advisory Conciliation & Arbitration Ser…
  - 同じ表の列：Main Department, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, In-Year - Number of…, In-Year - Median NC…, End of Year - Cost …

## g0057（1 列）
- 見出し：Annual Paybill (delegated grades for financial year 2012/13)
- 例1 値：」65,040,000 | 」30,871,691 | 」152,259,751 | 」46,946,741 | 」69,299,856
  - 同じ表の列：Main Department, Organisation, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, In-Year - Number of…, In-Year - Median NC…, End of Year - Cost …

## g0058（1 列）
- 見出し：Headcount (delegated grades as at 31 March 2013)
- 例1 値：781.8 | 1941 | 4492 | 980 | 2007
  - 同じ表の列：Main Department, Organisation, Annual Paybill (del…, Cost of in-year NCP…, Number of staff in …, In-Year - Number of…, In-Year - Median NC…, End of Year - Cost …

## g0059（1 列）
- 見出し：Cost of in-year NCPRP for delegated grades (」)
- 例1 値：」332,080 | 」2,450 | 」142,371 | 」0 | 」0
  - 同じ表の列：Main Department, Organisation, Annual Paybill (del…, Headcount (delegate…, Number of staff in …, In-Year - Number of…, In-Year - Median NC…, End of Year - Cost …

## g0060（2 列）
- 見出し：Number of staff in delegated grades receiving an in-year NCP
- 例1 値：591 | 1180 | 5 | 91 | 47
  - 同じ表の列：Main Department, Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, In-Year - Number of…, In-Year - Median NC…, End of Year - Cost …
- 例2 値：5 | 1131 | 1 | 857 | 0
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, Median NCPRP for th…, Cost of end of year…

## g0061（1 列）
- 見出し：In-Year - Number of staff in delegated grades receiving an i
- 例1 値：0.00% | 8.10% | 60.30% | 0.00% | 0.50%
  - 同じ表の列：Main Department, Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, In-Year - Median NC…, End of Year - Cost …

## g0062（1 列）
- 見出し：In-Year - Median NCPRP for those receiving an in-year NCPRP
- 例1 値：」250 | 」0 | 」100 | 」250 | 」500
  - 同じ表の列：Main Department, Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, In-Year - Number of…, End of Year - Cost …

## g0063（1 列）
- 見出し：End of Year - Cost of end of year NCPRP for delegated grades
- 例1 値：」393,454 | 」1,339,335 | 」0 | 」0 | 」0
  - 同じ表の列：Main Department, Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, In-Year - Number of…, In-Year - Median NC…

## g0064（1 列）
- 見出し：End of Year - Number of staff in delegated grades receiving
- 例1 値：1029 | 0 | 0 | 1913 | 2653
  - 同じ表の列：Main Department, Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, In-Year - Number of…, In-Year - Median NC…

## g0065（1 列）
- 見出し：title
- 例1 値：Lifted ban on UK beef exports to Japan … | UK defence exporters limited by the Can… | New legal framework for carbon markets … | Prohibitive regulations governing certi… | Reduced backlog of pending approval pro…
  - 同じ表の列：is_resolved, status_date, country_or_territor…, caused_by_trading_b…, trading_bloc, location, reported_on

## g0066（1 列）
- 見出し：is_resolved
- 例1 値：False | True | True | True | False
  - 同じ表の列：title, status_date, country_or_territor…, caused_by_trading_b…, trading_bloc, location, reported_on

## g0067（1 列）
- 見出し：status_date
- 例1 値：2021-08-31 | 2019-03-01 | 2024-10-15 | 2020-09-01 | 2022-04-01
  - 同じ表の列：title, is_resolved, country_or_territor…, caused_by_trading_b…, trading_bloc, location, reported_on

## g0068（1 列）
- 見出し：country_or_territory__trading_bloc
- 例1 値：TB00003 | TB00003 | TB00026 | TB00003 | #NA
  - 同じ表の列：title, is_resolved, status_date, caused_by_trading_b…, trading_bloc, location, reported_on

## g0069（1 列）
- 見出し：caused_by_trading_bloc
- 例1 値：#NA | Association of Southeast Asian Nations … | #NA | #NA | European Union (EU)
  - 同じ表の列：title, is_resolved, status_date, country_or_territor…, trading_bloc, location, reported_on

## g0070（1 列）
- 見出し：trading_bloc
- 例1 値：#NA | the ASEAN | the EU | the Mercosur | #NA
  - 同じ表の列：title, is_resolved, status_date, country_or_territor…, caused_by_trading_b…, location, reported_on

## g0071（1 列）
- 見出し：location
- 例1 値：Zimbabwe | #NA | Colombia | Costa Rica | Kenya
  - 同じ表の列：title, is_resolved, status_date, country_or_territor…, caused_by_trading_b…, trading_bloc, reported_on

## g0072（1 列）
- 見出し：reported_on
- 例1 値：2020-08-18T11:38:48.004824Z | 2020-10-20T01:42:16.075366Z | Indonesia | 2023-09-22T13:33:03.106738Z | Brazil
  - 同じ表の列：title, is_resolved, status_date, country_or_territor…, caused_by_trading_b…, trading_bloc, location

## g0073（1 列）
- 見出し：Department Family
- 例1 値：Communities & Local Government | Communities & Local Government | Communities & Local Government | Communities & Local Government | Communities & Local Government
  - 同じ表の列：Entity, Date of Payment, Expense Type, Expense Area, Supplier, Voluntary & Communi…, SME Class, D-U-N-S Number

## g0074（4 列）
- 見出し：Entity
- 例1 値：DCLG | DCLG | DCLG | DCLG | DCLG
  - 同じ表の列：Department Family, Date of Payment, Expense Type, Expense Area, Supplier, Voluntary & Communi…, SME Class, D-U-N-S Number
- 例2 値：HA | GCDA | HA | HA | MCA
  - 同じ表の列：Date Posted, Billing Amount

## g0075（1 列）
- 見出し：Date of Payment
- 例1 値：05/04/2017 | 03/04/2017 | 03/04/2017 | 21/04/2017 | 10/04/2017
  - 同じ表の列：Department Family, Entity, Expense Type, Expense Area, Supplier, Voluntary & Communi…, SME Class, D-U-N-S Number

## g0076（1 列）
- 見出し：Expense Type
- 例1 値：Current (non AEF) Grants to Local Autho… | Revenue Support grant payable | Rail, Underground and Eurostar | ERDF Work in Progress – Resource | Revenue Support grant payable
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Area, Supplier, Voluntary & Communi…, SME Class, D-U-N-S Number

## g0077（1 列）
- 見出し：Expense Area
- 例1 値：Local Government & Public Services | Local Government & Public Services | Decentralisation and Local Growth | Housing & Planning | Corporate Services
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Type, Supplier, Voluntary & Communi…, SME Class, D-U-N-S Number

## g0078（2 列）
- 見出し：Supplier
- 例1 値：GUILDFORD BC | CHARNWOOD BC | CAMBRIDGESHIRE COUNTY COUNCIL | NOTTINGHAM CITY COUNCIL | SHEPWAY DC
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Type, Expense Area, Voluntary & Communi…, SME Class, D-U-N-S Number
- 例2 値：Security Services Group | Scottish Government | Carlson Wagonlit | Carlson Wagonlit | Ministry of Justice
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Reason, Expense Area, Transaction Number, Amount

## g0079（1 列）
- 見出し：Voluntary & Community Sector
- 例1 値：Yes | Yes | Yes | Yes
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Type, Expense Area, Supplier, SME Class, D-U-N-S Number

## g0080（1 列）
- 見出し：SME Class
- 例1 値：Public Bodies | Large | Large | Public Bodies | Large
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Voluntary & Communi…, D-U-N-S Number

## g0081（1 列）
- 見出し：D-U-N-S Number
- 例1 値：293750923 | 293750923 | 213089972 | 506884659 | 213089972
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Voluntary & Communi…, SME Class

## g0082（7 列）
- 見出し：Transaction number
- 例1 値：5000366896 | 5106227596 | 2100272992 | 5106227617 | 5106227906
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Voluntary & Communi…, SME Class
- 例2 値：1002564 | 1002550 | 1002558 | 1002551 | 1002546
  - 同じ表の列：Departmental Family, Entity, Date, Expense type, Expense area, Supplier, Amount

## g0083（1 列）
- 見出し：ALB
- 例1 値：Department for Communities and Local Go… | Department for Communities and Local Go… | Department for Communities and Local Go… | Department for Communities and Local Go… | Department for Communities and Local Go…
  - 同じ表の列：Supplier, Net Amount 」

## g0084（1 列）
- 見出し：Supplier
- 例1 値：ASTAR MANAGEMENT CONSULTANTS LTD | E K BASSA LIMITED | TRUSTMARQUE SOLUTIONS LTD | H S B C INSURANCE BROKERS LTD | M A NOMINEES LTD
  - 同じ表の列：ALB, Net Amount 」

## g0085（1 列）
- 見出し：Net Amount 」
- 例1 値：83,822.95 | 5,117.36 | 16,758,803.82 | 3,645.75 | 11,750.00
  - 同じ表の列：ALB, Supplier

## g0086（2 列）
- 見出し：Organisation type
- 例1 値：Ministerial Department | Executive Agency
  - 同じ表の列：Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…
- 例2 値：Executive Agency | Ministerial Department | Executive Agency | Executive Agency
  - 同じ表の列：Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…

## g0087（1 列）
- 見出し：Main, parent or sponsoring department:
- 例1 値：Department for Culture, Media and Sport | Department for Culture, Media & Sport
  - 同じ表の列：Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…

## g0088（3 列）
- 見出し：Payroll staff
- 例1 値：Headcount | 25 | 19 | AO/AA
  - 同じ表の列：Organisation type, Main, parent or spo…, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…
- 例2 値：AO/AA | 1 | 128 | Headcount
  - 同じ表の列：Organisation type, Main, parent or spo…, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…

## g0089（2 列）
- 見出し：Number of non-payroll staff (contingent labour and consultan
- 例1 値：Headcount | 28 | Agency staff (clerical/admin) | 8
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…
- 例2 値：1 | Headcount | Agency staff (clerical/admin)
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…

## g0090（2 列）
- 見出し：Grand Total (workforce numbers)
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…
- 例2 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…

## g0091（1 列）
- 見出し：Payroll staff costs
- 例1 値：Salary | 」854,623.72 | 」309,102.63
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…

## g0092（2 列）
- 見出し：Non-Payroll staff (contingent labour/consultancy) costs
- 例1 値：」125,512.95 | Total monthly cost of contingent labour… | 」44,014.00
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Grand Total paybill…, Notes for Cabinet O…
- 例2 値：Total monthly cost of contingent labour… | 」30,893.00 | 」19,699.04 | 」35,625.00
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Grand Total paybill…, Notes for Cabinet O…

## g0093（2 列）
- 見出し：Grand Total paybill/staffing (payroll and non-payroll) costs
- 例1 値：」0.00 | 」0.00 | 」0.00 | 」0.00 | 」0.00
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Notes for Cabinet O…
- 例2 値：」0.00 | 」0.00 | 」0.00 | 」0.00 | 」0.00
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Notes for Cabinet O…

## g0094（1 列）
- 見出し：Notes for Cabinet Office (Not for publication)
- 例1 値：ALBs to be included with June figures
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0095（1 列）
- 見出し：Department family
- 例1 値：Department for Culture Media and Sport | Department for Culture Media and Sport | Department for Culture Media and Sport | Department for Culture Media and Sport | Department for Culture Media and Sport
  - 同じ表の列：Entity, Date, Expense Type, Expense area, Supplier, Amount

## g0096（1 列）
- 見出し：Entity
- 例1 値：Department for Culture Media and Sport | Department for Culture Media and Sport | Department for Culture Media and Sport | Department for Culture Media and Sport | Department for Culture Media and Sport
  - 同じ表の列：Department family, Date, Expense Type, Expense area, Supplier, Amount

## g0097（13 列）
- 見出し：Date
- 例1 値：23/09/2011 | 04/04/2011 | 19/08/2011 | 15/04/2011 | 01/09/2011
  - 同じ表の列：Department family, Entity, Expense Type, Expense area, Supplier, Amount
- 例2 値：20/04/2015 | 28/04/2015 | 29/04/2015 | 30/04/2015 | 20/04/2015
  - 同じ表の列：Departmental Family, Entity, Expense type, Expense area, Supplier, Transaction Number, Amount

## g0098（1 列）
- 見出し：Expense Type
- 例1 値：Ceremonials - Other Costs | Capital Grant Private Sector | Grant-in-Aid (DCMS NDPBs) | Grant-in-Aid (DCMS NDPBs) | TSOL Advice Billed Hours
  - 同じ表の列：Department family, Entity, Date, Expense area, Supplier, Amount

## g0099（1 列）
- 見出し：Expense area
- 例1 値：EAU Policy Research + Eval | GIA Museums & Galleries | Leveson Inquiry Admin Costs | GIA Sports bodies | Estates & Property Services
  - 同じ表の列：Department family, Entity, Date, Expense Type, Supplier, Amount

## g0100（1 列）
- 見出し：Supplier
- 例1 値：Olympic Delivery Authority (Citi Tfr) | Brophy Grounds Maintenance Ltd | LOCOG Grants | Tate Gallery | The Royal Parks
  - 同じ表の列：Department family, Entity, Date, Expense Type, Expense area, Amount

## g0101（1 列）
- 見出し：Amount
- 例1 値：877,671.96 | 7,842,000.00 | 118,857.12 | 97,824.00 | 616,500.00
  - 同じ表の列：Department family, Entity, Date, Expense Type, Expense area, Supplier

## g0102（1 列）
- 見出し：Date of Hospitality
- 例1 値：24-Jan | 08-Feb | 18-Mar | 13-Jan | 28-Jan
  - 同じ表の列：Type of hospitality…

## g0103（3 列）
- 見出し：Type of hospitality received
- 例1 値：Lunch | Dinner | Lunch | Lunch | Lunch
  - 同じ表の列：Date of Hospitality
- 例2 値：Lunch | Breakfast | Dinner | Dinner | Dinner
  - 同じ表の列：Minister, Date

## g0104（3 列）
- 見出し：Departmental Family
- 例1 値：Department for Education | Department for Education | Department for Education | Department for Education | Department for Education
  - 同じ表の列：Entity, Date, Expense type, Expense area, Supplier, Transaction Number, Amount
- 例2 値：DEPARTMENT FOR EDUCATION | DEPARTMENT FOR EDUCATION | DEPARTMENT FOR EDUCATION | DEPARTMENT FOR EDUCATION | DEPARTMENT FOR EDUCATION
  - 同じ表の列：Entity, Date, Expense Type Lookup, Expense Area Lookup, Supplier, Transaction Number, Amount

## g0105（3 列）
- 見出し：Entity
- 例1 値：TEACHERS PENSION SCHEME | TEACHERS PENSION SCHEME | TEACHERS PENSION SCHEME | TEACHERS PENSION SCHEME | TEACHERS PENSION SCHEME
  - 同じ表の列：Departmental Family, Date, Expense type, Expense area, Supplier, Transaction Number, Amount
- 例2 値：DEPARTMENT FOR EDUCATION | DEPARTMENT FOR EDUCATION | DEPARTMENT FOR EDUCATION | DEPARTMENT FOR EDUCATION | DEPARTMENT FOR EDUCATION
  - 同じ表の列：Departmental Family, Date, Expense Type Lookup, Expense Area Lookup, Supplier, Transaction Number, Amount

## g0106（1 列）
- 見出し：Expense type
- 例1 値：Funding to pay Teachers' Pensions | Funding to pay Teachers' Pensions | Funding to pay Teachers' Pensions | Funding to pay Teachers' Pensions | Funding to pay Teachers' Pensions
  - 同じ表の列：Departmental Family, Entity, Date, Expense area, Supplier, Transaction Number, Amount

## g0107（1 列）
- 見出し：Expense area
- 例1 値：Finance and Commercial Group | Finance and Commercial Group | Finance and Commercial Group | Finance and Commercial Group | Finance and Commercial Group
  - 同じ表の列：Departmental Family, Entity, Date, Expense type, Supplier, Transaction Number, Amount

## g0108（1 列）
- 見出し：Supplier
- 例1 値：TPS – Funding Account 1 | TPS – Funding Account 1 | TPS – Funding Account 2 | TPS – Funding Account 1 | TPS – Funding Account 2
  - 同じ表の列：Departmental Family, Entity, Date, Expense type, Expense area, Transaction Number, Amount

## g0109（2 列）
- 見出し：Amount
- 例1 値：35773433.73 | 83934.14 | 25985353.00 | 20094659.03 | 20289094.99
  - 同じ表の列：Departmental Family, Entity, Date, Expense type, Expense area, Supplier, Transaction Number
- 例2 値：71968.75 | 25267.37 | 108702.93 | 31293.26 | 49505.42
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Supplier, Transaction number

## g0110（1 列）
- 見出し：Posting Date
- 例1 値：06/04/2011 | 08/04/2011 | 19/04/2011 | 22/06/2011 | 25/04/2011
  - 同じ表の列：Final Transaction A…, Purpose

## g0111（1 列）
- 見出し：Final Transaction Amount
- 例1 値：」524.16 | 」771.60 | 」576.00 | 」863.45 | 」580.68
  - 同じ表の列：Posting Date, Purpose

## g0112（1 列）
- 見出し：Purpose
- 例1 値：ISBNs for Departmental publications | Video Editing KIT | CIIA Membership renewal fee | Subscription services for the DfE legal… | Video Editing KIT
  - 同じ表の列：Posting Date, Final Transaction A…

## g0113（1 列）
- 見出し：Expense Type Lookup
- 例1 値：CONTRACT PROGRAMME EXPENDITURE | GENERAL OFFICE EXPENSES | CURRENT GRANTS | COMMUNICATIONS & PUBLICITY | TEMPORARY (TEMP) STAFF COSTS
  - 同じ表の列：Departmental Family, Entity, Date, Expense Area Lookup, Supplier, Transaction Number, Amount

## g0114（1 列）
- 見出し：Expense Area Lookup
- 例1 値：Chief Information Officer Group EFM | Chief Information Officer Group | School Standards Group | Young People Workforce Group | School Resources Group
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type Lookup, Supplier, Transaction Number, Amount

## g0115（1 列）
- 見出し：Supplier
- 例1 値：BLACKBURN WITH DARWEN BOROUGH COUNCIL | CARLSON WAGONLIT TRAVEL | STAFFORDSHIRE COUNCIL | NEWCASTLE CITY COUNCIL | DTZ
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type Lookup, Expense Area Lookup, Transaction Number, Amount

## g0116（2 列）
- 見出し：Amount
- 例1 値：188.96 | 11668320 | 7528080 | 15088880 | 30512.42
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type Lookup, Expense Area Lookup, Supplier, Transaction Number
- 例2 値：6000 | 13041.31 | 10986.04 | 1000 | 347.99
  - 同じ表の列：Date, Transaction No., Expense Area, Expense Type, Expense Code, Service Area

## g0117（1 列）
- 見出し：Permanent secretary
- 例1 値：Jeremy Pocklington | Jeremy Pocklington | Jeremy Pocklington | Clive Maxwell | Jeremy Pocklington
  - 同じ表の列：Date, Purpose of meeting

## g0118（1 列）
- 見出し：Purpose of meeting
- 例1 値：To discuss Octopus Heat Pump Centre | Strategic network planning | Introductory Meeting | Strategic network planning | To discuss the Nuclear Sector
  - 同じ表の列：Permanent secretary, Date

## g0119（1 列）
- 見出し：GHG
- 例1 値：C2F6 | CH4 | CH4 | CF4 | CH4
  - 同じ表の列：GHG Grouped, IPCC Code, Year, National Communicat…, National Communicat…, National Communicat…, Source, National Communicat…

## g0120（1 列）
- 見出し：GHG Grouped
- 例1 値：CH4 | CH4 | CH4 | CH4 | PFCs
  - 同じ表の列：GHG, IPCC Code, Year, National Communicat…, National Communicat…, National Communicat…, Source, National Communicat…

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
g0119	
g0120	
```
