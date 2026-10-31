# ラベル用シート 002 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：GEOGRAPHY_TYPE
- 例1 値：local authorities: county / unitary (pr… | local authorities: district / unitary (… | local authorities: district / unitary (… | local authorities: district / unitary (… | local authorities: district / unitary (…
  - 同じ表の列：DATE, DATE_CODE, DATE_TYPE, DATE_TYPECODE, DATE_SORTORDER, GEOGRAPHY, GEOGRAPHY_CODE, GEOGRAPHY_TYPECODE

## g0122（1 列）
- 見出し：GEOGRAPHY_TYPECODE
- 例1 値：463 | 464 | 464 | 464 | 464
  - 同じ表の列：DATE, DATE_CODE, DATE_TYPE, DATE_TYPECODE, DATE_SORTORDER, GEOGRAPHY, GEOGRAPHY_CODE, GEOGRAPHY_TYPE

## g0123（1 列）
- 見出し：GEOGRAPHY_SORTORDER
- 例1 値：5 | 5 | 2 | 1 | 7
  - 同じ表の列：DATE, DATE_CODE, DATE_TYPE, DATE_TYPECODE, DATE_SORTORDER, GEOGRAPHY, GEOGRAPHY_CODE, GEOGRAPHY_TYPE

## g0124（1 列）
- 見出し：Supplier Type
- 例1 値：Other Supplier | Other Supplier | Foundation Trust | Other Supplier | Other Supplier
  - 同じ表の列：Department Family, Supplier, Supplier Number, Payment Document, Payment Method, Payment Date, Payment Number, Payment Currency

## g0125（1 列）
- 見出し：Supplier
- 例1 値：Hm Revenue And Customs | Tameside And Glossop Integrated Care NH… | Cheadle Royal Hospital Priory | NHS Property Services Ltd | Cheadle Royal Hospital Priory
  - 同じ表の列：Department Family, Supplier Type, Supplier Number, Payment Document, Payment Method, Payment Date, Payment Number, Payment Currency

## g0126（1 列）
- 見出し：Supplier Number
- 例1 値：17507 | 192108 | 215154 | 40003 | 203270
  - 同じ表の列：Department Family, Supplier Type, Supplier, Payment Document, Payment Method, Payment Date, Payment Number, Payment Currency

## g0127（1 列）
- 見出し：Payment Document
- 例1 値：RT2N BACS | RT2N BACS | RT2N BACS | RT2N BACS | RT2N BACS
  - 同じ表の列：Department Family, Supplier Type, Supplier, Supplier Number, Payment Method, Payment Date, Payment Number, Payment Currency

## g0128（1 列）
- 見出し：Payment Method
- 例1 値：EFT | EFT | EFT | EFT | EFT
  - 同じ表の列：Department Family, Supplier Type, Supplier, Supplier Number, Payment Document, Payment Date, Payment Number, Payment Currency

## g0129（1 列）
- 見出し：Payment Number
- 例1 値：5137677 | 5137619 | 5137727 | 900002088 | 5137232
  - 同じ表の列：Department Family, Supplier Type, Supplier, Supplier Number, Payment Document, Payment Method, Payment Date, Payment Currency

## g0130（1 列）
- 見出し：Payment Currency
- 例1 値：GBP | GBP | GBP | GBP | GBP
  - 同じ表の列：Department Family, Supplier Type, Supplier, Supplier Number, Payment Document, Payment Method, Payment Date, Payment Number

## g0131（1 列）
- 見出し：Invoice Number
- 例1 値：2900021035 | T0009591 | 14974 | M4 APPRENTESHIP LEVY | T0009716
  - 同じ表の列：Department Family, Supplier Type, Supplier, Supplier Number, Payment Document, Payment Method, Payment Date, Payment Number

## g0132（1 列）
- 見出し：ATCOCode
- 例1 値：1180PLA11147 | 1180PLB11766 | 1180PLB12000 | 1180PLG40009 | 1180PLB11894
  - 同じ表の列：NaptanCode, Bearing, Easting, Northing, StopType, BusStopType, Status

## g0133（1 列）
- 見出し：NaptanCode
- 例1 値：plympaw | plymwtp | plypaga | plygdwm | plyatwd
  - 同じ表の列：ATCOCode, Bearing, Easting, Northing, StopType, BusStopType, Status

## g0134（1 列）
- 見出し：Bearing
- 例1 値：SW | E | SW | E | E
  - 同じ表の列：ATCOCode, NaptanCode, Easting, Northing, StopType, BusStopType, Status

## g0135（1 列）
- 見出し：Easting
- 例1 値：248069 | 253908 | 248884 | 245668 | 246724
  - 同じ表の列：ATCOCode, NaptanCode, Bearing, Northing, StopType, BusStopType, Status

## g0136（1 列）
- 見出し：Northing
- 例1 値：60802 | 54421 | 58987 | 58639 | 54488
  - 同じ表の列：ATCOCode, NaptanCode, Bearing, Easting, StopType, BusStopType, Status

## g0137（1 列）
- 見出し：StopType
- 例1 値：BCT | BCT | BCT | BCT | BCT
  - 同じ表の列：ATCOCode, NaptanCode, Bearing, Easting, Northing, BusStopType, Status

## g0138（1 列）
- 見出し：BusStopType
- 例1 値：MKD | MKD | MKD | MKD | MKD
  - 同じ表の列：ATCOCode, NaptanCode, Bearing, Easting, Northing, StopType, Status

## g0139（1 列）
- 見出し：Status
- 例1 値：active | active | active | active | active
  - 同じ表の列：ATCOCode, NaptanCode, Bearing, Easting, Northing, StopType, BusStopType

## g0140（1 列）
- 見出し：Ref No
- 例1 値：47 | 154 | 293 | 136 | 62
  - 同じ表の列：RP, Scheme, Tenure, Type, Bed, Residents, DHC, Transfer

## g0141（1 列）
- 見出し：RP
- 例1 値：Westward | DCH | Affinity Sutton | DCH | Affinity Sutton
  - 同じ表の列：Ref No, Scheme, Tenure, Type, Bed, Residents, DHC, Transfer

## g0142（1 列）
- 見出し：Scheme
- 例1 値：Plymstock Quarry | NP 2.1a | Plym View | PLUSS Site | Hooe Lake
  - 同じ表の列：Ref No, RP, Tenure, Type, Bed, Residents, DHC, Transfer

## g0143（1 列）
- 見出し：Tenure
- 例1 値：Shared Ownership | Rented | Rented | Shared Ownership | Shared Ownership
  - 同じ表の列：Ref No, RP, Scheme, Type, Bed, Residents, DHC, Transfer

## g0144（1 列）
- 見出し：Type
- 例1 値：Flat | Flat | House | House | Flat
  - 同じ表の列：Ref No, RP, Scheme, Tenure, Bed, Residents, DHC, Transfer

## g0145（1 列）
- 見出し：Bed
- 例1 値：2 | 2 | 3 | 1 | 2
  - 同じ表の列：Ref No, RP, Scheme, Tenure, Type, Residents, DHC, Transfer

## g0146（1 列）
- 見出し：Residents
- 例1 値：No answer | 2 | No answer | No answer | 4
  - 同じ表の列：Ref No, RP, Scheme, Tenure, Type, Bed, DHC, Transfer

## g0147（1 列）
- 見出し：DHC
- 例1 値：Very Good | OK | Good | Good | Very Good
  - 同じ表の列：Ref No, RP, Scheme, Tenure, Type, Bed, Residents, Transfer

## g0148（1 列）
- 見出し：Transfer
- 例1 値：Very Good | Very Good | Very Good | Very Good | Good
  - 同じ表の列：Ref No, RP, Scheme, Tenure, Type, Bed, Residents, DHC

## g0149（1 列）
- 見出し：H2BSW
- 例1 値：Good | Good | Very Good | Good | Very Good
  - 同じ表の列：Ref No, RP, Scheme, Tenure, Type, Bed, Residents, DHC

## g0150（1 列）
- 見出し：Expense Area
- 例1 値：Balance Sheet | Balance Sheet | Balance Sheet | Balance Sheet | IT Technical Services
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Transaction Number, AP Amount, VAT Registration Nu…

## g0151（2 列）
- 見出し：Supplier
- 例1 値：INSPIRING HOPE LTD | PENTAX UK LTD | DIVERSITY AND ABILITY LTD | LIFECYCLE MANAGEMENT GROUP LTD | PULSE HEALTHCARE LTD
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, AP Amount, VAT Registration Nu…
- 例2 値：LLOYDS RETAIL CHEMISTS LTD | LIVANOVA UK LTD | LLOYDS RETAIL CHEMISTS LTD | NHS BLOOD AND TRANSPLANT | ZIMMER BIOMET UK LIMITED
  - 同じ表の列：Dept Family, Entity, Date, Expense Type, Expense Area, Amount

## g0152（1 列）
- 見出し：VAT Registration Number
- 例1 値：771715813 | GB491848503 | GB386334767 | GB491848503 | 207929448
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, AP Amount

## g0153（1 列）
- 見出し：SUPPLIER
- 例1 値：ION AMBULANCE CARE LTD | CHURCHILL CONTRACT SERVICES LTD | ORTIVUS UK LTD | CHURCHILL CONTRACT SERVICES LTD | NHS SHARED BUSINESS SERVICES LTD
  - 同じ表の列：DEPARTMENT FAMILY, ENTITY, DATE, EXPENSE TYPE, EXPENSE AREA, TRANSACTION NUMBER, AMOUNT

## g0154（1 列）
- 見出し：EXPENSE AREA
- 例1 値：OPERATIONS | NON EMERGENCY SERVICES | ICT | FINANCE, ESTATES AND PROCUREMENT | CLINICAL SERVICES
  - 同じ表の列：DEPARTMENT FAMILY, ENTITY, DATE, EXPENSE TYPE, SUPPLIER, TRANSACTION NUMBER, AMOUNT

## g0155（1 列）
- 見出し：SUPPLIER
- 例1 値：SOUTH CENTRAL FLEET SERVICES LTD | SOUTH CENTRAL FLEET SERVICES LTD | NHS PROPERTY SERVICES LTD | SEE SERVICES | CHURCHILL CONTRACT SERVICES LTD
  - 同じ表の列：DEPARTMENT FAMILY, ENTITY, DATE, EXPENSE TYPE, EXPENSE AREA, TRANSACTION NUMBER, AMOUNT

## g0156（1 列）
- 見出し：Date of Payment
- 例1 値：12/04/2010 | 26/04/2010 | 29/04/2010 | 22/04/2010 | 06/04/2010
  - 同じ表の列：Department Family, Entity, Expense Type, Expense Area, Expense Area_2, Supplier, Amount in Sterling

## g0157（1 列）
- 見出し：Expense Type
- 例1 値：FP10 Prescriptions | M & S Equipment | Computer Hardware & Software | M & S Equipment | Computer Hardware & Software
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Area, Expense Area_2, Supplier, Amount in Sterling

## g0158（1 列）
- 見出し：Expense Area
- 例1 値：Women & Children | Capital | Diagnostics & Clinical Support | Capital | Capital
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Type, Expense Area_2, Supplier, Amount in Sterling

## g0159（1 列）
- 見出し：Expense Area_2
- 例1 値：Paed - Medical - Bury | Network Strategy Phase One | PC Replacements | Pharmacy (North) | Pharmacy (North)
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Amount in Sterling

## g0160（1 列）
- 見出し：Supplier
- 例1 値：PINACL SOLUTIONS LTD | NHS SUPPLY CHAIN | PHILIPS HEALTHCARE | NHS SUPPLY CHAIN | CARE QUALITY COMMISION
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Type, Expense Area, Expense Area_2, Amount in Sterling

## g0161（1 列）
- 見出し：Amount in Sterling
- 例1 値：954180.22 | 18623.77 | 26210.87 | 4997.25 | 25693.55
  - 同じ表の列：Department Family, Entity, Date of Payment, Expense Type, Expense Area, Expense Area_2, Supplier

## g0162（1 列）
- 見出し：Entity
- 例1 値：The Royal Wolverhampton NHS Trust RL4 | The Royal Wolverhampton NHS Trust RL4 | The Royal Wolverhampton NHS Trust RL4 | The Royal Wolverhampton NHS Trust RL4 | The Royal Wolverhampton NHS Trust RL4
  - 同じ表の列：Department Family, Date Paid, Expense Type, Expense Area, Supplier, Transaction Number, Amount in Sterling

## g0163（2 列）
- 見出し：Date Paid
- 例1 値：15/04/2025 | 23/04/2025 | 23/04/2025 | 02/04/2025 | 23/04/2025
  - 同じ表の列：Department Family, Entity, Expense Type, Expense Area, Supplier, Transaction Number, Amount in Sterling
- 例2 値：23/09/2025 | 16/09/2025 | 16/09/2025 | 24/09/2025 | 16/09/2025
  - 同じ表の列：Department Of Health, Entity, Analysed Gross, Month

## g0164（1 列）
- 見出し：Expense Type
- 例1 値：Bedding And Linen | Capital Project | Gp Registrar Second In | Business Rates - New Cross | Course Fees
  - 同じ表の列：Department Family, Entity, Date Paid, Expense Area, Supplier, Transaction Number, Amount in Sterling

## g0165（1 列）
- 見出し：Supplier
- 例1 値：Sciensus Pharma Services Ltd | Total Gas And Power Ltd | Bayer Plc | Nhs Supply Chain Coordination Ltd (Main… | Bayer Plc
  - 同じ表の列：Department Family, Entity, Date Paid, Expense Type, Expense Area, Transaction Number, Amount in Sterling

## g0166（1 列）
- 見出し：Amount in Sterling
- 例1 値：204,008.78 | 2,165,997.70 | 91,212.00 | 28,800.00 | 109,137.60
  - 同じ表の列：Department Family, Entity, Date Paid, Expense Type, Expense Area, Supplier, Transaction Number

## g0167（3 列）
- 見出し：Department Of Health
- 例1 値：Department Of Health | Department Of Health | Department Of Health | Department Of Health | Department Of Health
  - 同じ表の列：Entity, Date of Payment, Expense Type, Expense Area, Supplier, Amount, Month
- 例2 値：Department Of Health | Department Of Health | Department Of Health | Department Of Health | Department Of Health
  - 同じ表の列：Entity, Date Paid, Analysed Gross, Month

## g0168（1 列）
- 見出し：Date of Payment
- 例1 値：2017-09-07 00:00:00.0 | 2017-09-14 00:00:00.0 | 2017-09-28 00:00:00.0 | 2017-09-28 00:00:00.0 | 2017-09-28 00:00:00.0
  - 同じ表の列：Department Of Health, Entity, Expense Type, Expense Area, Supplier, Amount, Month

## g0169（1 列）
- 見出し：Expense Type
- 例1 値：EXTERNAL CONTRACTS | COST OF FP 10 PRESCRIPTIONS | CLINICAL SERVICE CONTRACT | CLINICAL SERVICE CONTRACT | FUEL - STEAM
  - 同じ表の列：Department Of Health, Entity, Date of Payment, Expense Area, Supplier, Amount, Month

## g0170（1 列）
- 見出し：Expense Area
- 例1 値：COMMISSIONING & PERFORMANCE | THEATRES LINCOLN | DIAGNOSTICS | PAN TRUST | PAN TRUST
  - 同じ表の列：Department Of Health, Entity, Date of Payment, Expense Type, Supplier, Amount, Month

## g0171（1 列）
- 見出し：Supplier
- 例1 値：NHS LITIGATION AUTHORITY | ORCA BUILDING PRODUCTS LTD | MEDICA GROUP | NHS SUPPLY CHAIN (PRODUCT SALES) | NHS LITIGATION AUTHORITY
  - 同じ表の列：Department Of Health, Entity, Date of Payment, Expense Type, Expense Area, Amount, Month

## g0172（3 列）
- 見出し：Month
- 例1 値：Sep-17 | Sep-17 | Sep-17 | Sep-17 | Sep-17
  - 同じ表の列：Department Of Health, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Amount
- 例2 値：Sep-25 | Sep-25 | Sep-25 | Sep-25 | Sep-25
  - 同じ表の列：Department Of Health, Entity, Date Paid, Analysed Gross

## g0173（1 列）
- 見出し：Analysed Gross
- 例1 値：54497.27 | 32506.2 | 55929.54 | 85120 | 26601.97
  - 同じ表の列：Department Of Health, Entity, Date Paid, Month

## g0174（1 列）
- 見出し：Date of Payment
- 例1 値：2018-07-05 | 2018-07-16 | 2018-07-27 | 2018-07-12 | 2018-07-19
  - 同じ表の列：Department Of Health, Entity, Expense Type, Expense Area, Supplier, Amount, Month

## g0175（1 列）
- 見出し：Expense Type
- 例1 値：FUEL - STEAM | CPAP MACHINES | SERVICES FROM NON-NHS BODIES | PHARMACY | SERVICES FROM NON-NHS BODIES
  - 同じ表の列：Department Of Health, Entity, Date of Payment, Expense Area, Supplier, Amount, Month

## g0176（1 列）
- 見出し：Expense Area
- 例1 値：W&C SERVICES BOSTON | OPERATIONAL MGMT SUPPORT | PAN TRUST | W&C SERVICES BOSTON | PAN TRUST
  - 同じ表の列：Department Of Health, Entity, Date of Payment, Expense Type, Supplier, Amount, Month

## g0177（1 列）
- 見出し：Supplier
- 例1 値：JANSSEN-CILAG LTD | KPMG LLP | PORTAKABIN LIMITED | GEO HOULTON & SONS LTD | NHS LITIGATION AUTHORITY
  - 同じ表の列：Department Of Health, Entity, Date of Payment, Expense Type, Expense Area, Amount, Month

## g0178（1 列）
- 見出し：Amount
- 例1 値：228,164.80 | 52,380.00 | 49,517.96 | 31,464.00 | 104,601.72
  - 同じ表の列：Department Of Health, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Month

## g0179（2 列）
- 見出し：Dept Family
- 例1 値：NHS | NHS | NHS | NHS | NHS
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Amount
- 例2 値：NHS | NHS | NHS | NHS | NHS
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Amount

## g0180（2 列）
- 見出し：Entity
- 例1 値：UHCW NHS TRUST | UHCW NHS TRUST | UHCW NHS TRUST | UHCW NHS TRUST | UHCW NHS TRUST
  - 同じ表の列：Dept Family, Date, Expense Type, Expense Area, Supplier, Amount
- 例2 値：UHCW NHS TRUST | UHCW NHS TRUST | UHCW NHS TRUST | UHCW NHS TRUST | UHCW NHS TRUST
  - 同じ表の列：Dept Family, Date, Expense Type, Expense Area, Supplier, Amount

## g0181（1 列）
- 見出し：Expense Type
- 例1 値：APPLIANCES & IMPLANTS | SERVICES REC FROM THIRD PARTY | DRUGS | FURNITURE OFFICE & COMP EQUIP | MEDICAL & SURGICAL EQUIP PURCH
  - 同じ表の列：Dept Family, Entity, Date, Expense Area, Supplier, Amount

## g0182（1 列）
- 見出し：Expense Area
- 例1 値：BLOOD SCIENCES | ESTATES | MICROBIOLOGY | INFORMATION AND COMMS TECH | ORTHOPAEDICS
  - 同じ表の列：Dept Family, Entity, Date, Expense Type, Supplier, Amount

## g0183（2 列）
- 見出し：Amount
- 例1 値：1822.54 | 1066.64 | 344.09 | 101649.92 | -58683.91
  - 同じ表の列：Dept Family, Entity, Date, Expense Type, Expense Area, Supplier
- 例2 値：27322.67 | 14142.37 | 155000.00 | -21117.27 | 9860.00
  - 同じ表の列：Dept Family, Entity, Date, Expense Type, Expense Area, Supplier

## g0184（1 列）
- 見出し：Expense Type
- 例1 値：OTHER ESTABLISHMENT COSTS | LABORATORY EQUIP - PURCHASES | CAPITAL EXPENDITURE IN YEAR | FURNITURE OFFICE & COMP EQUIP | OTHER ESTABLISHMENT COSTS
  - 同じ表の列：Dept Family, Entity, Date, Expense Area, Supplier, Amount

## g0185（1 列）
- 見出し：Supplier
- 例1 値：COVENTRY & RUGBY HOSPITAL COMPANY PLC | ROCHE PRODUCTS LTD | NHS SUPPLY CHAIN (10004157) | SOFTWARE BOX LTD | SOFTWARE BOX LTD
  - 同じ表の列：Dept Family, Entity, Date, Expense Type, Expense Area, Amount

## g0186（1 列）
- 見出し：class="no-js"
- 例1 値：<meta name="description" content="We ar… | <div class="gm-dropdown-menu-wrapper"><… | <div class="gm-dropdown-menu-wrapper"><… | <div class="gm-dropdown-menu-wrapper"><… | <li id="menu-item-mobile-8311" class="m…
  - 同じ表の列：lang="en-US">

## g0187（1 列）
- 見出し：lang="en-US">
- 例1 値：<li id="menu-item-mobile-8459" class="m… | <li id="menu-item-13069" class="menu-it… | </div> | <li id="menu-item-mobile-2666" class="m… | <li id="menu-item-8214" class="menu-ite…
  - 同じ表の列：class="no-js"

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
```
