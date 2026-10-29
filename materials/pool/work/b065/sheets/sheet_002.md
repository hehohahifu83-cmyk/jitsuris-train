# ラベル用シート 002 / 003

- LABEL_GUIDE v2.1 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：LA CO2 Sub-sector
- 例1 値：LULUCF Net Emissions: Forest land | Agriculture | Diesel Railways | Public Sector Electricity | Domestic Gas
  - 同じ表の列：Country, Country Code, Region, Region Code, Second Tier Authori…, Local Authority, Local Authority Code, Calendar Year

## g0122（1 列）
- 見出し：HH_ID
- 例1 値：838 | 614 | 15 | 856 | 903
  - 同じ表の列：REGION, IMD_ENG, IMD_WALES, Gcons2005, Gcons2005Valid, Gcons2006, Gcons2006Valid, Gcons2007

## g0123（1 列）
- 見出し：REGION
- 例1 値：E12000008 | E12000004 | E12000004 | W99999999 | E12000002
  - 同じ表の列：HH_ID, IMD_ENG, IMD_WALES, Gcons2005, Gcons2005Valid, Gcons2006, Gcons2006Valid, Gcons2007

## g0124（1 列）
- 見出し：IMD_ENG
- 例1 値：5 | 4 | 2 | 3 | 3
  - 同じ表の列：HH_ID, REGION, IMD_WALES, Gcons2005, Gcons2005Valid, Gcons2006, Gcons2006Valid, Gcons2007

## g0125（1 列）
- 見出し：IMD_WALES
- 例1 値：2 | 4 | 3 | 2 | 1
  - 同じ表の列：HH_ID, REGION, IMD_ENG, Gcons2005, Gcons2005Valid, Gcons2006, Gcons2006Valid, Gcons2007

## g0126（1 列）
- 見出し：Gcons2005
- 例1 値：23500 | 14300 | 8000 | 32000 | 3000
  - 同じ表の列：HH_ID, REGION, IMD_ENG, IMD_WALES, Gcons2005Valid, Gcons2006, Gcons2006Valid, Gcons2007

## g0127（1 列）
- 見出し：Gcons2005Valid
- 例1 値：V | V | V | V | O
  - 同じ表の列：HH_ID, REGION, IMD_ENG, IMD_WALES, Gcons2005, Gcons2006, Gcons2006Valid, Gcons2007

## g0128（1 列）
- 見出し：Gcons2006
- 例1 値：4000 | 18500 | 18000 | 16000 | 6500
  - 同じ表の列：HH_ID, REGION, IMD_ENG, IMD_WALES, Gcons2005, Gcons2005Valid, Gcons2006Valid, Gcons2007

## g0129（1 列）
- 見出し：Gcons2006Valid
- 例1 値：O | O | V | V | V
  - 同じ表の列：HH_ID, REGION, IMD_ENG, IMD_WALES, Gcons2005, Gcons2005Valid, Gcons2006, Gcons2007

## g0130（1 列）
- 見出し：Gcons2007
- 例1 値：11800 | 1000 | 45000 | 16000 | 24000
  - 同じ表の列：HH_ID, REGION, IMD_ENG, IMD_WALES, Gcons2005, Gcons2005Valid, Gcons2006, Gcons2006Valid

## g0131（1 列）
- 見出し：Gcons2007Valid
- 例1 値：V | V | V | M | V
  - 同じ表の列：HH_ID, REGION, IMD_ENG, IMD_WALES, Gcons2005, Gcons2005Valid, Gcons2006, Gcons2006Valid

## g0132（1 列）
- 見出し：Department
- 例1 値：DFID | Period 1st April 2012 to 30 June 2012 i… | Period 1st July 2012 to 30 September 20… | Department | Period 1st January 2012 to 31st March 2…
  - 同じ表の列：Basis for Exception, Value requested, Value Approved, Approval month

## g0133（1 列）
- 見出し：Basis for Exception
- 例1 値：IT element for HQ relocation requiremen… | Projected efficiencies of 」6m between 2… | Projected savings of 」1.6m p.a. versus … | Basis for Exception | Basis for Exception
  - 同じ表の列：Department, Value requested, Value Approved, Approval month

## g0134（1 列）
- 見出し：Value requested
- 例1 値：Value requested | Value | 3.50 | Value requested | Value
  - 同じ表の列：Department, Basis for Exception, Value Approved, Approval month

## g0135（1 列）
- 見出し：Value Approved
- 例1 値：3.50 | Value Approved | 2.40 | Value Approved | Value Approved
  - 同じ表の列：Department, Basis for Exception, Value requested, Approval month

## g0136（1 列）
- 見出し：Approval month
- 例1 値：Approval month | Approval month | 04/01/2012 | 10/09/2012 | Approval month
  - 同じ表の列：Department, Basis for Exception, Value requested, Value Approved

## g0137（1 列）
- 見出し：Organisation type
- 例1 値：Executive Non Departmental Public Body | Executive Non Departmental Public Body | Ministerial Department
  - 同じ表の列：Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0138（1 列）
- 見出し：Main, parent or sponsoring department:
- 例1 値：Department for International Development | Department for International Development | Department for International Development
  - 同じ表の列：Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0139（1 列）
- 見出し：Payroll staff
- 例1 値：Admin officers/admin assistants | 0 | 131 | Headcount | 0
  - 同じ表の列：Organisation type, Main, parent or spo…, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0140（1 列）
- 見出し：Number of non-payroll staff (contingent labour and consultan
- 例1 値：Agency staff (clerical/admin) | 0 | 125 | 0 | Headcount
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0141（1 列）
- 見出し：Grand Total (workforce numbers)
- 例1 値：Headcount | 4 | 1,822 | 0
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0142（1 列）
- 見出し：Payroll staff costs
- 例1 値：」72,902,946 | 0 | Salary | 0
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0143（1 列）
- 見出し：Non-Payroll staff (contingent labour/consultancy - CCL) cost
- 例1 値：Total cost of contingent labour: agency… | 0 | 0 | 」1,363,024
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Grand Total paybill…, Comments and notes

## g0144（1 列）
- 見出し：Grand Total paybill/staffing (payroll and non-payroll) costs
- 例1 値：」95,294,855 | 」14,100 | 0
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Comments and notes

## g0145（1 列）
- 見出し：Comments and notes
- 例1 値：Numbers of agency staff and consultants… | ICAI is an Advisory NDPB. These costs a…
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0146（1 列）
- 見出し：Reference Number
- 例1 値：con_2713 | con_3656 | con_2874 | con_3769 | prj_1841
  - 同じ表の列：Business Area, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0147（1 列）
- 見出し：Business Area
- 例1 値：Matrix Senior Responsible Officer | Communications | Digital | Business Growth | Commercial & Operations
  - 同じ表の列：Reference Number, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0148（1 列）
- 見出し：Contract Title
- 例1 値：Venue Hire | Digital Software Implementation Partner | COMMS - DSIT DESNZ Intranet | BEIS Market Research | Digital Outcome Specialists for impleme…
  - 同じ表の列：Reference Number, Business Area, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0149（1 列）
- 見出し：Commercial Strategy
- 例1 値：New requirement | Renewal (different scope) | New requirement | Re-procurement (same scope) | Re-procurement (same scope)
  - 同じ表の列：Reference Number, Business Area, Contract Title, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0150（1 列）
- 見出し：Procurement Start Date
- 例1 値：45016 | 45022 | 45714 | 46023 | 45019
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Contract Commenceme…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0151（1 列）
- 見出し：Contract Commencement Date
- 例1 値：45346 | 45139 | 45264 | 46202 | 45804
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start D…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0152（1 列）
- 見出し：New Contract End Date
- 例1 値：TBC | 48883 | TBC | 45747 | 45747
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, Value of New Contra…, Procurement Sourcin…

## g0153（1 列）
- 見出し：Value of New Contract (Excluding Options)
- 例1 値：5000000 | 2000000 | 2000000 | 4500000 | 4000000
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Procurement Sourcin…

## g0154（1 列）
- 見出し：Procurement Sourcing Route
- 例1 値：Framework - CCS | Dynamic Purchasing Systems | Above Threshold | Framework | Competitive Procedure with Negotiation
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…

## g0155（1 列）
- 見出し：Category
- 例1 値：Travel | IT | Market Research | Professional Services Other | IT
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…

## g0156（1 列）
- 見出し：Personal Data?
- 例1 値：Yes | Yes | Yes | Yes | No, the data is aggregated to local aut…
  - 同じ表の列：Public

## g0157（1 列）
- 見出し：Public
- 例1 値：Yes | No | No | Yes | Yes
  - 同じ表の列：Personal Data?

## g0158（1 列）
- 見出し：Minister
- 例1 値：Baroness Sugg | Jesse Norman | Chris Grayling | Jo Johnson | Nusrat Ghani
  - 同じ表の列：Start Date of Trip, End Date of Trip, Destination, Purpose of Trip, Mode of Transport, Cost of private jet…, Number of officials…, Total cost (for min…

## g0159（1 列）
- 見出し：Start Date of Trip
- 例1 値：Nil Return | 25/01/2018 | Nil Return | 02/01/2018 | 01/03/2018
  - 同じ表の列：Minister, End Date of Trip, Destination, Purpose of Trip, Mode of Transport, Cost of private jet…, Number of officials…, Total cost (for min…

## g0160（1 列）
- 見出し：End Date of Trip
- 例1 値：Nil Return | Nil Return | 26/01/2018 | 03/03/2018 | 04/01/2018
  - 同じ表の列：Minister, Start Date of Trip, Destination, Purpose of Trip, Mode of Transport, Cost of private jet…, Number of officials…, Total cost (for min…

## g0161（1 列）
- 見出し：Destination
- 例1 値：Washington | Seville, Spain | Nil Return | Nil Return | Mexico
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Purpose of Trip, Mode of Transport, Cost of private jet…, Number of officials…, Total cost (for min…

## g0162（1 列）
- 見出し：Purpose of Trip
- 例1 値：Nil Return | To look at cycling infrastructure in Se… | Bilat meetings and business opportuntie… | Nil Return | UK / USA Aviation Security visit
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Destination, Mode of Transport, Cost of private jet…, Number of officials…, Total cost (for min…

## g0163（1 列）
- 見出し：Mode of Transport
- 例1 値：Nil return | Scheduled flight | Scheduled flight | Scheduled flight | Scheduled flight
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Destination, Purpose of Trip, Cost of private jet…, Number of officials…, Total cost (for min…

## g0164（1 列）
- 見出し：Cost of private jet or RAF plane hire, if relevant (」)
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Destination, Purpose of Trip, Mode of Transport, Number of officials…, Total cost (for min…

## g0165（1 列）
- 見出し：Number of officials who accompanied minister if non-shcedule
- 例1 値：None | None | None | None | None
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Destination, Purpose of Trip, Mode of Transport, Cost of private jet…, Total cost (for min…

## g0166（1 列）
- 見出し：Total cost (for minister only) including all visas, accommod
- 例1 値：1250 | Nil Return | Nil Return | 4,856.27 | 」4,313.61
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Destination, Purpose of Trip, Mode of Transport, Cost of private jet…, Number of officials…

## g0167（1 列）
- 見出し：Date
- 例1 値：2018-02-15 | 2018-01-08 | 2018-02-14 | 2018-02-28 | 2018-01-10
  - 同じ表の列：Type of Hospitality…

## g0168（1 列）
- 見出し：Type of Hospitality received
- 例1 値：other | Taxi from Bristol Airport to Bristol Te… | Reception | other | other
  - 同じ表の列：Date

## g0169（1 列）
- 見出し：Departmental Family
- 例1 値：Department for Work and Pensions | Department for Work and Pensions | Department for Work and Pensions | Department for Work and Pensions | Department for Work and Pensions
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0170（1 列）
- 見出し：Expense Type
- 例1 値：JSP ESF DEL P COSTS | APPS DEV | STAFF COSTS | PROFESSIONAL FEES | EMPLOYMENT ZONES
  - 同じ表の列：Departmental Family, Entity, Date, Expense Area, Supplier, Transaction Number, Amount

## g0171（1 列）
- 見出し：Expense Area
- 例1 値：WWG CORE PROGRAMME | WWG CORE PROGRAMME | HOUSING BENEFIT | GROUP FINANCE | HOUSING BENEFIT
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Supplier, Transaction Number, Amount

## g0172（1 列）
- 見出し：Supplier
- 例1 値：COMPUTACENTER UK LTD | NORD ANGLIA EDUCATION PARTNERSHIPS LTD | WORKING LINKS | SUNDERLAND CITY COUNCIL | A4E LTD
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount

## g0173（1 列）
- 見出し：Amount
- 例1 値：」1,613,896.5 | 」56,859.4 | 」319,304.6 | 」123,038.0 | 」144,294.8
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number

## g0174（1 列）
- 見出し：Spend in 」m
- 例1 値：」1,717.57 | 」36.91 | 」988.18 | 」19,774.67 | 」19.98
  - 同じ表の列：Comments

## g0175（1 列）
- 見出し：Comments
- 例1 値：These figures represent the costs of st… | Cost of hosting DWP systems | Remainder of IT costs excluding B2 above | Only includes offices > 500sqm and excl… | Cost of Application Maintenance and Sup…
  - 同じ表の列：Spend in 」m

## g0176（1 列）
- 見出し：Number of boxes
- 例1 値：1 | 329 | 2 | 4 | 0
  - 同じ表の列：Estimated linear me…, Estimated number of…, Format, Date range

## g0177（1 列）
- 見出し：Estimated linear metres
- 例1 値：1.08 | 1.34 | 0.14 | 10.4 | 0.81
  - 同じ表の列：Number of boxes, Estimated number of…, Format, Date range

## g0178（1 列）
- 見出し：Estimated number of items
- 例1 値：40 | 1328 | 26 | 8 | 23
  - 同じ表の列：Number of boxes, Estimated linear me…, Format, Date range

## g0179（1 列）
- 見出し：Format
- 例1 値：ring binders | Files/loose papers | Files | Files | Files
  - 同じ表の列：Number of boxes, Estimated linear me…, Estimated number of…, Date range

## g0180（1 列）
- 見出し：Date range
- 例1 値：1972-1996 | 1919-1943 | 1999 | 1993 | 1980-1998
  - 同じ表の列：Number of boxes, Estimated linear me…, Estimated number of…, Format

## g0181（1 列）
- 見出し：Region
- 例1 値：Middle East and North Africa | Multilateral Agreements | Multilateral Agreements | Africa | Europe
  - 同じ表の列：UK Treaty Actions N…

## g0182（1 列）
- 見出し：UK Treaty Actions November 2015 - February 2016
- 例1 値：Nagoya Protocol on Access to Genetic Re… | Protocol of 2014 to the Forced Labour C… | No treaty actions during this period. | Spain – Agreement concerning the Protec… | Uruguay – Double Taxation Convention si…
  - 同じ表の列：Region

## g0183（1 列）
- 見出し：Extending Agency
- 例1 値：3 | 3 | 3 | 3 | 3
  - 同じ表の列：Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow, Type of Finance

## g0184（1 列）
- 見出し：Donor Project Number
- 例1 値：PAF NIA 110001 - YD | PAP 000112-3 | PHR MUL 310001 | PAM DOS 000023 | PDS CPD SPF 000147
  - 同じ表の列：Extending Agency, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow, Type of Finance

## g0185（1 列）
- 見出し：Project Title
- 例1 値：OAS Report and recommendations on land … | Nigeria Legal Capacity Building | Scholarships | Supporting the implementation of the Br… | AP ALGERIA HANDICAP INT
  - 同じ表の列：Extending Agency, Donor Project Number, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow, Type of Finance

## g0186（1 列）
- 見出し：Nature of Submission
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow, Type of Finance

## g0187（1 列）
- 見出し：Benefitting Country Code
- 例1 値：JM | BO | BU | CE | CN
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Input Sector code, Channel of Delivery…, Type of Flow, Type of Finance

## g0188（1 列）
- 見出し：Input Sector code
- 例1 値：41032 | 92000 | 15220 | 15141 | 24010
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Channel of Delivery…, Type of Flow, Type of Finance

## g0189（1 列）
- 見出し：Channel of Delivery Code
- 例1 値：11000 | 50000 | 21000 | 21000 | 20000
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Type of Flow, Type of Finance

## g0190（1 列）
- 見出し：Type of Flow
- 例1 値：10 | 10 | 10 | 10 | 10
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Finance

## g0191（1 列）
- 見出し：Type of Finance
- 例1 値：100 | 100 | 100 | 100 | 100
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow

## g0192（1 列）
- 見出し：Type of Aid
- 例1 値：C01 | C01 | C01 | C01 | C01
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow

## g0193（1 列）
- 見出し：Entity
- 例1 値：FCO | FCO | FCO | FCO | FCO
  - 同じ表の列：Department, Posted Date, Internal Voucher Nu…, Invoice Line Amount…

## g0194（2 列）
- 見出し：Posted Date
- 例1 値：02/09/2020 | 07/09/2020 | 01/09/2020 | 01/09/2020 | 17/09/2020
  - 同じ表の列：Department, Entity, Internal Voucher Nu…, Invoice Line Amount…
- 例2 値：23/09/2020 | 14/09/2020 | 22/09/2020 | 22/09/2020 | 14/09/2020
  - 同じ表の列：Invoice_Net_Line_Am…

## g0195（1 列）
- 見出し：Internal Voucher Number
- 例1 値：10894628 | 10898899 | 10888256 | 10908080 | 10901895
  - 同じ表の列：Department, Entity, Posted Date, Invoice Line Amount…

## g0196（1 列）
- 見出し：Invoice Line Amount GBP
- 例1 値：200,000.00 | 30,527.75 | 151,910.16 | 44,694.73 | 48,762.62
  - 同じ表の列：Department, Entity, Posted Date, Internal Voucher Nu…

## g0197（1 列）
- 見出し：Invoice_Net_Line_Amount
- 例1 値：」630.00 | 」750.00 | 」915.00 | 」630.00 | 」630.00
  - 同じ表の列：Posted Date

## g0198（1 列）
- 見出し：Sep-20
- 例1 値：Laos | Malta | Turkmenistan | Poland | Saint Vincent and the Grenadines
  - 同じ表の列：Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0199（1 列）
- 見出し：Arrest/Detention > Assault
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Sep-20, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0200（1 列）
- 見出し：Arrest/Detention > Assault with Weapon
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Sep-20, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0201（1 列）
- 見出し：Arrest/Detention > Child Pornography
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Sep-20, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0202（1 列）
- 見出し：Arrest/Detention > Child Sex
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Sep-20, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0203（1 列）
- 見出し：Arrest/Detention > Drugs
- 例1 値：0 | <5 | 0 | 0 | 0
  - 同じ表の列：Sep-20, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0204（1 列）
- 見出し：Arrest/Detention > Fraud
- 例1 値：<5 | <5 | 0 | 0 | 0
  - 同じ表の列：Sep-20, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0205（1 列）
- 見出し：Arrest/Detention > Immigration
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Sep-20, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0206（1 列）
- 見出し：Arrest/Detention > Modern Slavery / Human Trafficking
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Sep-20, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0207（1 列）
- 見出し：Arrest/Detention > Murder / Manslaughter
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Sep-20, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0208（1 列）
- 見出し：Category
- 例1 値：Housing | Housing | Housing | Housing | Housing
  - 同じ表の列：Local Authority, Site Reference, Is the site Brownfi…, Construction Status, Planning Status, Local Planning Stat…, Are the supply figu…, Houses only complet…

## g0209（1 列）
- 見出し：Local Authority
- 例1 値：Manchester | Bolton | Bolton | Manchester | Bolton
  - 同じ表の列：Category, Site Reference, Is the site Brownfi…, Construction Status, Planning Status, Local Planning Stat…, Are the supply figu…, Houses only complet…

## g0210（1 列）
- 見出し：Site Reference
- 例1 値：743-BOL | 132429/FO/2021 | 132214/FO/2021 | HL/2527/01 | 134873/FO/2022
  - 同じ表の列：Category, Local Authority, Is the site Brownfi…, Construction Status, Planning Status, Local Planning Stat…, Are the supply figu…, Houses only complet…

## g0211（1 列）
- 見出し：Is the site Brownfield, Greenfield or a Mix?
- 例1 値：Brownfield | Brownfield | Brownfield | Greenfield | Brownfield
  - 同じ表の列：Category, Local Authority, Site Reference, Construction Status, Planning Status, Local Planning Stat…, Are the supply figu…, Houses only complet…

## g0212（1 列）
- 見出し：Construction Status
- 例1 値：Not started | Under construction | Under construction | Under construction | Not started
  - 同じ表の列：Category, Local Authority, Site Reference, Is the site Brownfi…, Planning Status, Local Planning Stat…, Are the supply figu…, Houses only complet…

## g0213（1 列）
- 見出し：Planning Status
- 例1 値：Permissioned | Permissioned | Permissioned | Not permissioned | Permissioned
  - 同じ表の列：Category, Local Authority, Site Reference, Is the site Brownfi…, Construction Status, Local Planning Stat…, Are the supply figu…, Houses only complet…

## g0214（1 列）
- 見出し：Local Planning Status
- 例1 値：F | F | O | Prior approval | F
  - 同じ表の列：Category, Local Authority, Site Reference, Is the site Brownfi…, Construction Status, Planning Status, Are the supply figu…, Houses only complet…

## g0215（1 列）
- 見出し：Are the supply figures Net or Gross?
- 例1 値：Net | Gross | Net | Gross | Gross
  - 同じ表の列：Category, Local Authority, Site Reference, Is the site Brownfi…, Construction Status, Planning Status, Local Planning Stat…, Houses only complet…

## g0216（1 列）
- 見出し：Houses only completions - All past years
- 例1 値：0 | 0 | 0 | 0 | 43
  - 同じ表の列：Category, Local Authority, Site Reference, Is the site Brownfi…, Construction Status, Planning Status, Local Planning Stat…, Are the supply figu…

## g0217（1 列）
- 見出し：Houses only supply 2025-26 to 2029-30
- 例1 値：0 | 0 | 4 | 0 | 0
  - 同じ表の列：Category, Local Authority, Site Reference, Is the site Brownfi…, Construction Status, Planning Status, Local Planning Stat…, Are the supply figu…

## g0218（1 列）
- 見出し：Senior Official (SCS2 and above)
- 例1 値：Jonathan Athow | Alan Evans | Myrtle Lloyd | Jonathan Athow | Suzanne Newton
  - 同じ表の列：Date, Purpose of meeting

## g0219（1 列）
- 見出し：Date
- 例1 値：nil return | nil return | 16/02/2024 | 23/02/2024 | 24/03/2024
  - 同じ表の列：Senior Official (SC…, Purpose of meeting

## g0220（1 列）
- 見出し：Purpose of meeting
- 例1 値：To discuss HMRC priorities and regulati… | nil return | To gain feedback from HMRCs key stakeho… | Pre-meeting ahead of the Stakeholder Co… | nil return
  - 同じ表の列：Senior Official (SC…, Date

## g0221（1 列）
- 見出し：Agency
- 例1 値：HMT | HMT | HMT | HMT | HMT
  - 同じ表の列：Paid_fare, Trip type, Routing_type, Ticket class, Departure Date, Origin, Destination, Destination Country

## g0222（1 列）
- 見出し：Paid_fare
- 例1 値：2671.6 | 261.6 | 623.47 | 399 | 301.5
  - 同じ表の列：Agency, Trip type, Routing_type, Ticket class, Departure Date, Origin, Destination, Destination Country

## g0223（1 列）
- 見出し：Trip type
- 例1 値：Domestic | Continental | Continental | Domestic | Continental
  - 同じ表の列：Agency, Paid_fare, Routing_type, Ticket class, Departure Date, Origin, Destination, Destination Country

## g0224（1 列）
- 見出し：Routing_type
- 例1 値：ONE-WAY | ONE-WAY | ONE-WAY | ONE-WAY | ONE-WAY
  - 同じ表の列：Agency, Paid_fare, Trip type, Ticket class, Departure Date, Origin, Destination, Destination Country

## g0225（1 列）
- 見出し：Ticket class
- 例1 値：Business Class | Economy | Economy | Economy | Economy
  - 同じ表の列：Agency, Paid_fare, Trip type, Routing_type, Departure Date, Origin, Destination, Destination Country

## g0226（1 列）
- 見出し：Departure Date
- 例1 値：03/02/2011 | 24/02/2011 | 16/01/2011 | 10/03/2011 | 08/04/2011
  - 同じ表の列：Agency, Paid_fare, Trip type, Routing_type, Ticket class, Origin, Destination, Destination Country

## g0227（1 列）
- 見出し：Origin
- 例1 値：LONDON | LONDON | LONDON | LONDON | AUCKLAND
  - 同じ表の列：Agency, Paid_fare, Trip type, Routing_type, Ticket class, Departure Date, Destination, Destination Country

## g0228（1 列）
- 見出し：Destination
- 例1 値：DELHI | BUENOS AIRES | LONDON | ZURICH | BUDAPEST
  - 同じ表の列：Agency, Paid_fare, Trip type, Routing_type, Ticket class, Departure Date, Origin, Destination Country

## g0229（1 列）
- 見出し：Destination Country
- 例1 値：UNITED KINGDOM | UNITED KINGDOM | HUNGARY | LUXEMBOURG | FRANCE
  - 同じ表の列：Agency, Paid_fare, Trip type, Routing_type, Ticket class, Departure Date, Origin, Destination

## g0230（1 列）
- 見出し：Carrier
- 例1 値：MALEV | SWISS | BRITISH AIRWAYS | FLYBE BRITISH EUROPEAN | EASYJET
  - 同じ表の列：Agency, Paid_fare, Trip type, Routing_type, Ticket class, Departure Date, Origin, Destination

## g0231（1 列）
- 見出し：Organisation Type
- 例1 値：Executive Non-Departmental Public Body | Ministerial Department | Executive Non-Departmental Public Body | Executive Agency | Executive Agency
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0232（1 列）
- 見出し：Main, parent or sponsoring department
- 例1 値：Home Office | Home Office | Home Office | Home Office | Home Office
  - 同じ表の列：Organisation Type, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0233（1 列）
- 見出し：Payroll staff AO/AA Headcount
- 例1 値：14 | 38 | 331 | 77 | 7092
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0234（1 列）
- 見出し：Payroll staff EO Headcount
- 例1 値：39 | 21 | 188 | 0 | 7
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0235（1 列）
- 見出し：Payroll staff SEO/HEO Headcount
- 例1 値：1733 | 114 | 167.8 | 0 | 85
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0236（1 列）
- 見出し：Payroll staff Grade 6/7 Headcount
- 例1 値：2 | 731 | 19 | 33 | 721
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0237（1 列）
- 見出し：Payroll staff SCS Headcount
- 例1 値：26 | 65 | 121 | 15 | 6
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff Other…, Payroll staff Total…

## g0238（1 列）
- 見出し：Payroll staff Other, unknown or unspecified Headcount
- 例1 値：11 | 4 | 0 | 6 | 13
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Total…

## g0239（1 列）
- 見出し：Payroll staff Total Employees Headcount
- 例1 値：21752 | 0 | 432 | 668 | 60
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

## g0240（1 列）
- 見出し：Non-payroll Staff Agency staff (clerical/admin) Headcount
- 例1 値：0 | 0 | 10 | 189 | 10
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

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
