# ラベル用シート 002 / 004

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：IPCC Code
- 例1 値：1A1ai | 1A1ai | 2G2e | 2G2e | 1A1aiii
  - 同じ表の列：GHG, GHG Grouped, Year, National Communicat…, National Communicat…, National Communicat…, Source, National Communicat…

## g0122（1 列）
- 見出し：National Communication Sector
- 例1 値：Energy Supply | Business | Energy Supply | Energy Supply | Energy Supply
  - 同じ表の列：GHG, GHG Grouped, IPCC Code, Year, National Communicat…, National Communicat…, Source, National Communicat…

## g0123（1 列）
- 見出し：National Communication Sub-sector
- 例1 値：(blank) | (blank) | (blank) | (blank) | (blank)
  - 同じ表の列：GHG, GHG Grouped, IPCC Code, Year, National Communicat…, National Communicat…, Source, National Communicat…

## g0124（1 列）
- 見出し：National Communication Category
- 例1 値：Power Stations | Power Stations | Halocarbon production | Power Stations | Power Stations
  - 同じ表の列：GHG, GHG Grouped, IPCC Code, Year, National Communicat…, National Communicat…, Source, National Communicat…

## g0125（1 列）
- 見出し：Source
- 例1 値：Power stations | Refineries - combustion | Refineries - combustion | Refineries - combustion | Power stations
  - 同じ表の列：GHG, GHG Grouped, IPCC Code, Year, National Communicat…, National Communicat…, National Communicat…, National Communicat…

## g0126（1 列）
- 見出し：National Communication Fuel Group
- 例1 値：Petroleum | Gaseous fuels | Other emissions | Petroleum | Other solid fuels
  - 同じ表の列：GHG, GHG Grouped, IPCC Code, Year, National Communicat…, National Communicat…, National Communicat…, Source

## g0127（1 列）
- 見出し：National Communication Fuel
- 例1 値：Other gases | Other emissions | Other emissions | Other emissions | Other gases
  - 同じ表の列：GHG, GHG Grouped, IPCC Code, Year, National Communicat…, National Communicat…, National Communicat…, Source

## g0128（1 列）
- 見出し：Minister
- 例1 値：Lord Bridges of Headley MBE Until 13th … | Rt Hon David Davis MP | Baroness Anelay of St Johns From 12th J… | Rt Hon David Jones MP Until 12th June | Rt Hon David Jones MP Until 12th June
  - 同じ表の列：Date, Type of hospitality…

## g0129（1 列）
- 見出し：Date
- 例1 値：3 May 2017 | 10 April 2017 | 11 April 2017 | 25 April 2017 | 3 May 2017
  - 同じ表の列：Minister, Type of hospitality…

## g0130（1 列）
- 見出し：GNI (」m)
- 例1 値：1,593,448 | 1,622,166 | 28,718 | 1,700,170 | 32,409
  - 同じ表の列：ODA (」m), ODA:GNI ratios (%)

## g0131（1 列）
- 見出し：ODA (」m)
- 例1 値：11,437 1 | 11,462 | 11,462 | 11,462
  - 同じ表の列：GNI (」m), ODA:GNI ratios (%)

## g0132（1 列）
- 見出し：ODA:GNI ratios (%)
- 例1 値：0.71 | 0.72 | 0.69 | 0.67
  - 同じ表の列：GNI (」m), ODA (」m)

## g0133（1 列）
- 見出し：Date(s) of trip
- 例1 値：Dec-10 | Nov-10 | 7th – 11th November | 23rd – 27th November | Date of Meeting
  - 同じ表の列：Destination, Purpose of trip, Type of travel, Total cost includin…

## g0134（1 列）
- 見出し：Destination
- 例1 値：Lord Mayor of ??r | Washington DC, USA | Delhi, India | WomanKind | Human Rights Watch
  - 同じ表の列：Date(s) of trip, Purpose of trip, Type of travel, Total cost includin…

## g0135（1 列）
- 見出し：Purpose of trip
- 例1 値：World Bank Annual Meetings | To discuss a range of development issue… | To present their campaign on “Speaking … | To update DFID on their activities and … | Visit to country office. Meetings with …
  - 同じ表の列：Date(s) of trip, Destination, Type of travel, Total cost includin…

## g0136（1 列）
- 見出し：Type of travel
- 例1 値：Scheduled | Scheduled | Scheduled | Scheduled | Scheduled
  - 同じ表の列：Date(s) of trip, Destination, Purpose of trip, Total cost includin…

## g0137（1 列）
- 見出し：Total cost including travel, and accommodation of Minister o
- 例1 値：£4,019.00 | £2,838.00 | £2,703 | £3,607.00 | £2,793
  - 同じ表の列：Date(s) of trip, Destination, Purpose of trip, Type of travel

## g0138（3 列）
- 見出し：Minister
- 例1 値：Paul Scully | George Freeman | Jonathan Berry | Chloe Smith | Michelle Donelan
  - 同じ表の列：Date, Gift, Given or received, Who gift was given …, Value (£), Outcome (received g…
- 例2 値：Nusrat Ghani | Jesse Norman | Jesse Norman | Chris Grayling | Chris Grayling
  - 同じ表の列：Date, Purpose of meeting

## g0139（4 列）
- 見出し：Date
- 例1 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Gift, Given or received, Who gift was given …, Value (£), Outcome (received g…
- 例2 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Minister, Gift, Given or received, Who gift was given …, Value (」), Outcome (received g…

## g0140（2 列）
- 見出し：Gift
- 例1 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Date, Given or received, Who gift was given …, Value (£), Outcome (received g…
- 例2 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Special Adviser, Date, Given or received, Who gift was given …, Value (œ), Outcome (received g…

## g0141（2 列）
- 見出し：Given or received
- 例1 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Date, Gift, Who gift was given …, Value (£), Outcome (received g…
- 例2 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Special Adviser, Date, Gift, Who gift was given …, Value (œ), Outcome (received g…

## g0142（2 列）
- 見出し：Who gift was given to or received from
- 例1 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Date, Gift, Given or received, Value (£), Outcome (received g…
- 例2 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Special Adviser, Date, Gift, Given or received, Value (œ), Outcome (received g…

## g0143（1 列）
- 見出し：Value (£)
- 例1 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Date, Gift, Given or received, Who gift was given …, Outcome (received g…

## g0144（2 列）
- 見出し：Outcome (received gifts only)
- 例1 値：Nil Return | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Minister, Date, Gift, Given or received, Who gift was given …, Value (£)
- 例2 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Special Adviser, Date, Gift, Given or received, Who gift was given …, Value (œ)

## g0145（1 列）
- 見出し：Purpose of meeting
- 例1 値：Informal discussion | Range of local transport issues | To discuss electric vehicles | To discuss London’s future as a centre … | To discuss resilience partnership
  - 同じ表の列：Minister, Date

## g0146（1 列）
- 見出し：Date Posted
- 例1 値：25/02/2013 | 19/02/2013 | 22/02/2013 | 18/02/2013 | 07/02/2013
  - 同じ表の列：Entity, Billing Amount

## g0147（1 列）
- 見出し：Billing Amount
- 例1 値：」913.26 | 」1,889.04 | 」2,484.97 | 」600.00 | 」1,969.57
  - 同じ表の列：Entity, Date Posted

## g0148（1 列）
- 見出し：Date
- 例1 値：06.09.2012 | 26.09.2012 | 10.09.2012 | 13.09.2012 | 17.09.2012
  - 同じ表の列：Departmental Family, Entity, Expense Type, Expense Area, Supplier, Transaction No, Sum of Amount

## g0149（1 列）
- 見出し：Expense Type
- 例1 値：Cap Grt Loc Auth | Property Maintenance | BUS FDR Wales | Subsidies Private Se | Property Maintenance
  - 同じ表の列：Departmental Family, Entity, Date, Expense Area, Supplier, Transaction No, Sum of Amount

## g0150（1 列）
- 見出し：Expense Area
- 例1 値：Aviation Security | Aviation Security | Local | Roads | Local
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Supplier, Transaction No, Sum of Amount

## g0151（1 列）
- 見出し：Supplier
- 例1 値：ELLESMERE PORT & NESTON COM TRANS | MICHAEL PAGE INTERNATIONAL | MSRS FREIGHT GRANT | AGE CONCERN BATH | DISPLAY MATRIX LTD
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Expense Area, Transaction No, Sum of Amount

## g0152（1 列）
- 見出し：Transaction No
- 例1 値：2000011432 | 2000012807 | 2000012092 | 2000012478 | 2000011661
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Expense Area, Supplier, Sum of Amount

## g0153（1 列）
- 見出し：Sum of Amount
- 例1 値：730.66 | 11.68 | 2025.97 | 2040 | 7681
  - 同じ表の列：Departmental Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction No

## g0154（1 列）
- 見出し：Title
- 例1 値：Director General, Corporate IT and Chie… | Director General, Employment Group | Chief Executive, Jobcentre Plus | Permanent Secretary | Director General, Welfare and Wellbeing
  - 同じ表の列：Date, Type of Hospitality…

## g0155（1 列）
- 見出し：Date
- 例1 値：15-Feb | Nil Return | Nil Return | Nil Return | Nil Return
  - 同じ表の列：Title, Type of Hospitality…

## g0156（1 列）
- 見出し：Minister
- 例1 値：Minister of State (Minister for Employm… | Minister of State (Minister for Pension… | Parliamentary Under-Secretary of State … | Parliamentary Under-Secretary of State … | Parliamentary Under-Secretary of State …
  - 同じ表の列：Date of Meeting, Purpose of Meeting

## g0157（1 列）
- 見出し：Date of Meeting
- 例1 値：Jun-10 | Jul-10 | Jul-10 | Jul-10 | Jul-10
  - 同じ表の列：Minister, Purpose of Meeting

## g0158（1 列）
- 見出し：Purpose of Meeting
- 例1 値：Work Programme | Work Programme | Work Programme | Work Programme | Work Programme
  - 同じ表の列：Minister, Date of Meeting

## g0159（2 列）
- 見出し：DESTINATION
- 例1 値：Manchester | Leeds | Birmingham | London | London
  - 同じ表の列：DATE, PURPOSE, OTHER, TOTAL COST
- 例2 値：UAE | MILAN | LONDON | PARIS | SHEFFIELD
  - 同じ表の列：Senior official (SC…, Start date of trip, Duration of Visit, Purpose of trip, Mode of transport, Class of travel, Accommodation/Meals, Other (including ho…

## g0160（1 列）
- 見出し：PURPOSE
- 例1 値：Attending an official meeting | Attending an official meeting | Type of hospitality received | Attending an internal meeting | Attending an official meeting
  - 同じ表の列：DATE, DESTINATION, OTHER, TOTAL COST

## g0161（1 列）
- 見出し：OTHER
- 例1 値：OTHER | OTHER | OTHER | 8,090.11 | 」17.82
  - 同じ表の列：DATE, DESTINATION, PURPOSE, TOTAL COST

## g0162（1 列）
- 見出し：TOTAL COST
- 例1 値：」139.50 | 」3.80 | 」426.00 | 」45.80 | 」77.50
  - 同じ表の列：DATE, DESTINATION, PURPOSE, OTHER

## g0163（1 列）
- 見出し：FIN.POSTING DATE
- 例1 値：02/07/2018 | 26/07/2018 | 19/07/2018 | 03/07/2018 | 05/07/2018
  - 同じ表の列：FIN.TRANSACTION AMO…

## g0164（1 列）
- 見出し：FIN.TRANSACTION AMOUNT
- 例1 値：522 | 708 | 756 | 969.67 | 560
  - 同じ表の列：FIN.POSTING DATE

## g0165（2 列）
- 見出し：Main department
- 例1 値：Department of Health | Department of Health | Department of Health
  - 同じ表の列：Organisation, Delegated grades on…, SCS on standard con…, Information for SCS…
- 例2 値：Ministry of Justice | Ministry of Justice | Ministry of Justice | Ministry of Justice | Ministry of Justice
  - 同じ表の列：Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, Number of staff in …, Median NCPRP for th…, Cost of end of year…

## g0166（1 列）
- 見出し：Organisation
- 例1 値：Medicines and Healthcare Products Regul… | Public Health England | Department of Health (excl agencies)
  - 同じ表の列：Main department, Delegated grades on…, SCS on standard con…, Information for SCS…

## g0167（1 列）
- 見出し：Delegated grades only
- 例1 値：」40,929,943 | Annual Paybill (delegated grades for fi… | 」60,231,276 | 」91,579,510
  - 同じ表の列：Main department, Organisation, SCS on standard con…, Information for SCS…

## g0168（1 列）
- 見出し：SCS on standard contracts (end of year NCPRP)
- 例1 値：」18,362,093 | Annual SCS Paybill for those SCS on sta… | 」4,262,403 | 」9,873,764
  - 同じ表の列：Main department, Organisation, Delegated grades on…, Information for SCS…

## g0169（1 列）
- 見出し：Information for SCS on non-standard contracts
- 例1 値：0 | 0 | Number of SCS on non-standard contracts… | 0
  - 同じ表の列：Main department, Organisation, Delegated grades on…, SCS on standard con…

## g0170（1 列）
- 見出し：Extending Agency
- 例1 値：3 | 3 | 3 | 3 | 3
  - 同じ表の列：Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow, Type of Finance

## g0171（1 列）
- 見出し：Donor Project Number
- 例1 値：A/02463 | A/02264 | A/02393 | A/02913 | A/02463
  - 同じ表の列：Extending Agency, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow, Type of Finance

## g0172（1 列）
- 見出し：Project Title
- 例1 値：Creative and Cultural Economy | Global Engaging Teaching | SSA LCR ENG Skills For Teachers Engage | INTERNATIONAL HIGHER EDUCATION (GLO) | Global English Interface
  - 同じ表の列：Extending Agency, Donor Project Number, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow, Type of Finance

## g0173（1 列）
- 見出し：Nature of Submission
- 例1 値：3 | 3 | 1 | 3 | 3
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow, Type of Finance

## g0174（1 列）
- 見出し：Benefitting Country Code
- 例1 値：SY | LB | KE | MU | CN
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Input Sector code, Channel of Delivery…, Type of Flow, Type of Finance

## g0175（1 列）
- 見出し：Input Sector code
- 例1 値：11230 | 11430 | 11130 | 11130 | 11110
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Channel of Delivery…, Type of Flow, Type of Finance

## g0176（1 列）
- 見出し：Channel of Delivery Code
- 例1 値：20000 | 52000 | 12000 | 20000 | 51000
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Type of Flow, Type of Finance

## g0177（1 列）
- 見出し：Type of Flow
- 例1 値：10 | 10 | 10 | 10 | 10
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Finance

## g0178（1 列）
- 見出し：Type of Finance
- 例1 値：100 | 100 | 100 | 100 | 100
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow

## g0179（1 列）
- 見出し：Type of Aid
- 例1 値：CO1 | CO1 | CO1 | CO1 | CO1
  - 同じ表の列：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country…, Input Sector code, Channel of Delivery…, Type of Flow

## g0180（1 列）
- 見出し：Region
- 例1 値：Europe | Europe | Africa | Africa | Multilateral
  - 同じ表の列：Country/Territory, Location (City), Type of Post

## g0181（1 列）
- 見出し：Country/Territory
- 例1 値：Italy | Vietnam | United States | Falkland Islands | Russia
  - 同じ表の列：Region, Location (City), Type of Post

## g0182（1 列）
- 見出し：Location (City)
- 例1 値：Dusseldorf | Tehran | Johannesburg | Astana | Bangkok
  - 同じ表の列：Region, Country/Territory, Type of Post

## g0183（1 列）
- 見出し：Type of Post
- 例1 値：British Embassy | British Embassy | British Consulate General | Governor | British Trade Office
  - 同じ表の列：Region, Country/Territory, Location (City)

## g0184（1 列）
- 見出し：Gift
- 例1 値：Nil return | Nil return | Rug | Leather briefcase | Nil return
  - 同じ表の列：Minister, Date, Given or received, Who gift was given …, Value (」), Outcome (received g…

## g0185（1 列）
- 見出し：Given or received
- 例1 値：Nil return | Received | Nil return | Nil return | Nil return
  - 同じ表の列：Minister, Date, Gift, Who gift was given …, Value (」), Outcome (received g…

## g0186（1 列）
- 見出し：Who gift was given to or received from
- 例1 値：Nil return | Dr Gargash, Deputy Foreign Minister, UAE | Nil return | Nil return | Nil return
  - 同じ表の列：Minister, Date, Gift, Given or received, Value (」), Outcome (received g…

## g0187（1 列）
- 見出し：Value (」)
- 例1 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Minister, Date, Gift, Given or received, Who gift was given …, Outcome (received g…

## g0188（1 列）
- 見出し：Outcome (received gifts only)
- 例1 値：Nil return | Nil return | Held by department | Held by department | Nil return
  - 同じ表の列：Minister, Date, Gift, Given or received, Who gift was given …, Value (」)

## g0189（1 列）
- 見出し：Special Adviser
- 例1 値：Beth Armstrong | Simon Finkelstein | Robert Oxley | Sally Rushton | William Sweet
  - 同じ表の列：Date, Gift, Given or received, Who gift was given …, Value (œ), Outcome (received g…

## g0190（1 列）
- 見出し：Value (œ)
- 例1 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Special Adviser, Date, Gift, Given or received, Who gift was given …, Outcome (received g…

## g0191（1 列）
- 見出し：Start date of trip
- 例1 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…, Total cost, includi…

## g0192（1 列）
- 見出し：Duration of Visit (in days)
- 例1 値：1 | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Start date of trip, Destination, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…, Total cost, includi…

## g0193（1 列）
- 見出し：Destination
- 例1 値：Nil return | Glasgow, UK | Nil return | Nil return | Nil return
  - 同じ表の列：Start date of trip, Duration of Visit (…, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…, Total cost, includi…

## g0194（1 列）
- 見出し：Purpose of trip
- 例1 値：Visiting Finance Operations teams after… | UK-Jordan Strategic Dialogue | Trilateral Political Directors meeting | Nil return | Nil return
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…, Total cost, includi…

## g0195（1 列）
- 見出し：Mode of transport
- 例1 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Purpose of trip, Class of travel, Accomodation/Meals, Other (including ho…, Total cost, includi…

## g0196（1 列）
- 見出し：Class of travel
- 例1 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Accomodation/Meals, Other (including ho…, Total cost, includi…

## g0197（1 列）
- 見出し：Accomodation/Meals
- 例1 値：Nil return | Nil return | 」0 | Nil return | Nil return
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Class of travel, Other (including ho…, Total cost, includi…

## g0198（1 列）
- 見出し：Other (including hospitality given)
- 例1 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Total cost, includi…

## g0199（1 列）
- 見出し：Total cost, including all visas, accommodation, travel, meal
- 例1 値：Nil return | Nil return | Nil return | Nil return | 」210
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…

## g0200（1 列）
- 見出し：Total Cost of Use of Official Secure Car
- 例1 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…

## g0201（2 列）
- 見出し：Department family
- 例1 値：HMRC | HMRC | HMRC | HMRC | HMRC
  - 同じ表の列：Entity, Date, Expense type, Expense area, Supplier, Transaction number, Amount
- 例2 値：BIS | BIS | BIS | BIS | BIS
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0202（1 列）
- 見出し：Expense type
- 例1 値：Business Rates | White boards LT | Maj AW non-struc VAT | OGD costs | Non PFI serv VAT
  - 同じ表の列：Department family, Entity, Date, Expense area, Supplier, Transaction number, Amount

## g0203（1 列）
- 見出し：Expense area
- 例1 値：Commercial Directorate | Communications & Marketing | Customer Operations PSA & NICEO | Estates & Support Services | Finance & Internal Audit
  - 同じ表の列：Department family, Entity, Date, Expense type, Supplier, Transaction number, Amount

## g0204（1 列）
- 見出し：Supplier
- 例1 値：Fujitsu Services Ltd (Pacesetter) | Mapeley Steps Limited | RYGOR Commercial Ltd | G3 Worldwide (UK) Ltd | Lovells
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Transaction number, Amount

## g0205（1 列）
- 見出し：Start date of expense
- 例1 値：18/01/2024 | 18/03/2024 | 13/02/2024 | 18/01/2024 | 01/02/2024
  - 同じ表の列：End date of expense, Purpose of expense, Destination, Mode(s) of transport, Class of transport, Sub- total of all t…, Sub - total costs o…, Sub- total cost of …

## g0206（1 列）
- 見出し：End date of expense
- 例1 値：14/03/2024 | 04/01/2024 | 20/02/2024 | 07/03/2024 | 01/02/2024
  - 同じ表の列：Start date of expen…, Purpose of expense, Destination, Mode(s) of transport, Class of transport, Sub- total of all t…, Sub - total costs o…, Sub- total cost of …

## g0207（1 列）
- 見出し：Purpose of expense
- 例1 値：Chartered Institute of Taxation (CIOT) | HMRC Audit and Risk Committee meeting | Management & leadership meeting | Enterprise Leadership Group meeting | Making Tax Digital Strategic meetings
  - 同じ表の列：Start date of expen…, End date of expense, Destination, Mode(s) of transport, Class of transport, Sub- total of all t…, Sub - total costs o…, Sub- total cost of …

## g0208（1 列）
- 見出し：Destination
- 例1 値：Liverpool, UK | London, UK | London | Birmingham, UK | Birmingham, UK
  - 同じ表の列：Start date of expen…, End date of expense, Purpose of expense, Mode(s) of transport, Class of transport, Sub- total of all t…, Sub - total costs o…, Sub- total cost of …

## g0209（1 列）
- 見出し：Mode(s) of transport
- 例1 値：Private car | Train, Taxi | Private car | Train | Train
  - 同じ表の列：Start date of expen…, End date of expense, Purpose of expense, Destination, Class of transport, Sub- total of all t…, Sub - total costs o…, Sub- total cost of …

## g0210（1 列）
- 見出し：Class of transport
- 例1 値：N/A | Economy/Standard | Economy/Standard | Economy/Standard | Economy/Standard
  - 同じ表の列：Start date of expen…, End date of expense, Purpose of expense, Destination, Mode(s) of transport, Sub- total of all t…, Sub - total costs o…, Sub- total cost of …

## g0211（1 列）
- 見出し：Sub- total of all transport used (£)
- 例1 値：Nil return | 68.70 | 268.00 | 148.00 | N/A
  - 同じ表の列：Start date of expen…, End date of expense, Purpose of expense, Destination, Mode(s) of transport, Class of transport, Sub - total costs o…, Sub- total cost of …

## g0212（1 列）
- 見出し：Sub - total costs of all accommodation and meals (£)
- 例1 値：158.20 | 109.00 | 354.92 | N/A | 109.40
  - 同じ表の列：Start date of expen…, End date of expense, Purpose of expense, Destination, Mode(s) of transport, Class of transport, Sub- total of all t…, Sub- total cost of …

## g0213（1 列）
- 見出し：Sub- total cost of all other expenses, including hospitality
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：Start date of expen…, End date of expense, Purpose of expense, Destination, Mode(s) of transport, Class of transport, Sub- total of all t…, Sub - total costs o…

## g0214（1 列）
- 見出し：Total cost of expenses claimed (£)
- 例1 値：188.00 | 226.00 | 445.99 | 690.53 | 315.80
  - 同じ表の列：Start date of expen…, End date of expense, Purpose of expense, Destination, Mode(s) of transport, Class of transport, Sub- total of all t…, Sub - total costs o…

## g0215（2 列）
- 見出し：Senior Official (SCS2 and above)
- 例1 値：Karen Wheeler | Hannah Watson | Simon Claydon | Peter Grant | Tom Smith
  - 同じ表の列：Date, Type of hospitality…
- 例2 値：Stephen Phipson | Michael Boyd | Michael Boyd | Dominic Jermey | Stephen Phipson
  - 同じ表の列：Date, Type of hospitality…

## g0216（1 列）
- 見出し：Type of hospitality received
- 例1 値：Dinner | Nil return | Nil return | Nil return | Dinner
  - 同じ表の列：Senior Official (SC…, Date

## g0217（1 列）
- 見出し：Main, parent or sponsoring department:
- 例1 値：HM Treasury | HM Treasury | HM Treasury | HM Treasury
  - 同じ表の列：Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…

## g0218（1 列）
- 見出し：Payroll staff costs
- 例1 値：」408,953.24 | Salary | 」374,844.54 | 」3,893,300.78 | 41,221.80
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…, Notes for Cabinet O…

## g0219（1 列）
- 見出し：Notes for Cabinet Office (Not for publication)
- 例1 値：DMO do not have a civil service grading… | This is the Asset Protection Agency. Co… | AO includes students. Does not include …
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0220（1 列）
- 見出し：Organisation Code
- 例1 値：ACL048 | BIS084 | BIS084 | BIS084 | BIS084
  - 同じ表の列：Organisation, Control Budget Code, Sub Segment Code, Economic Category C…, Economic Budget Code, PESA Economic Group…, Version, Year

## g0221（1 列）
- 見出し：Organisation
- 例1 値：DEPARTMENT FOR BUSINESS INNOVATION AND … | DEPARTMENT FOR BUSINESS INNOVATION AND … | AGRICULTURE & HORTICULTURE DEVELOPMENT … | DEPARTMENT FOR BUSINESS INNOVATION AND … | Air Travel Trust
  - 同じ表の列：Organisation Code, Control Budget Code, Sub Segment Code, Economic Category C…, Economic Budget Code, PESA Economic Group…, Version, Year

## g0222（1 列）
- 見出し：Control Budget Code
- 例1 値：AME | DEL | DEL | AME | DEL
  - 同じ表の列：Organisation Code, Organisation, Sub Segment Code, Economic Category C…, Economic Budget Code, PESA Economic Group…, Version, Year

## g0223（1 列）
- 見出し：Sub Segment Code
- 例1 値：X048A051 | X084A235 | X902A004 | X084A127 | X084A034
  - 同じ表の列：Organisation Code, Organisation, Control Budget Code, Economic Category C…, Economic Budget Code, PESA Economic Group…, Version, Year

## g0224（1 列）
- 見出し：Economic Category Code
- 例1 値：B101 | B101 | D111 | D111 | G101
  - 同じ表の列：Organisation Code, Organisation, Control Budget Code, Sub Segment Code, Economic Budget Code, PESA Economic Group…, Version, Year

## g0225（1 列）
- 見出し：Economic Budget Code
- 例1 値：RESOURCE | RESOURCE | RESOURCE | RESOURCE | RESOURCE
  - 同じ表の列：Organisation Code, Organisation, Control Budget Code, Sub Segment Code, Economic Category C…, PESA Economic Group…, Version, Year

## g0226（1 列）
- 見出し：PESA Economic Group Code
- 例1 値：NET PUBLIC SERVICE PENSIONS | OTHER RESOURCE | OTHER RESOURCE | NET PUBLIC SERVICE PENSIONS | PURCHASE OF GOODS AND SERVICES
  - 同じ表の列：Organisation Code, Organisation, Control Budget Code, Sub Segment Code, Economic Category C…, Economic Budget Code, Version, Year

## g0227（1 列）
- 見出し：Version
- 例1 値：RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG
  - 同じ表の列：Organisation Code, Organisation, Control Budget Code, Sub Segment Code, Economic Category C…, Economic Budget Code, PESA Economic Group…, Year

## g0228（1 列）
- 見出し：Year
- 例1 値：2013-14 | 2013-14 | 2013-14 | 2013-14 | 2013-14
  - 同じ表の列：Organisation Code, Organisation, Control Budget Code, Sub Segment Code, Economic Category C…, Economic Budget Code, PESA Economic Group…, Version

## g0229（1 列）
- 見出し：Quarter
- 例1 値：Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14
  - 同じ表の列：Organisation Code, Organisation, Control Budget Code, Sub Segment Code, Economic Category C…, Economic Budget Code, PESA Economic Group…, Version

## g0230（1 列）
- 見出し：Property
- 例1 値：Home Office - UKBA | Home Office - UKBA | Home Office - GEO | Please note other terms, especially ren… | Home Office - UKBA
  - 同じ表の列：exceptions for peri…

## g0231（1 列）
- 見出し：exceptions for period 01 November 2010 - 30 September 2011
- 例1 値：Property lease | Property lease | Property lease | Property lease | Property lease
  - 同じ表の列：Property

## g0232（1 列）
- 見出し：Recruitment
- 例1 値：Home office HQ | SIA | CRB | IPCC | HMIC
  - 同じ表の列：Exceptions for peri…

## g0233（1 列）
- 見出し：Exceptions for period 01 November 2010 - 30 September 2011
- 例1 値：0 | 0 | 0 | 0 | AA
  - 同じ表の列：Recruitment

## g0234（3 列）
- 見出し：Department Family
- 例1 値：Land Registry | Land Registry | Land Registry | Land Registry | Land Registry
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, SME, Transaction Number, Amount
- 例2 値：Scotland Office | Scotland Office | Scotland Office | Scotland Office | Scotland Office
  - 同じ表の列：Entity, Date, Expense Type, Expense Reason, Expense Area, Supplier, Transaction Number, Amount

## g0235（1 列）
- 見出し：Entity
- 例1 値：Land Registry | Land Registry | Land Registry | Land Registry | Land Registry
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Supplier, SME, Transaction Number, Amount

## g0236（1 列）
- 見出し：Expense Type
- 例1 値：FM Ext Helpdesk | Waste Disposal | Property Maintenance | Security Expenses | Property Maintenance
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, SME, Transaction Number, Amount

## g0237（1 列）
- 見出し：Expense Area
- 例1 値：Coventry Office | Governance & Policy | Durham Office | Fylde Office | Leicester Office
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, SME, Transaction Number, Amount

## g0238（1 列）
- 見出し：Supplier
- 例1 値：Carillion Services Ltd | Redfern Travel Ltd | Redfern Travel Ltd | Carillion Services Ltd | Carillion Services Ltd
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, SME, Transaction Number, Amount

## g0239（1 列）
- 見出し：SME
- 例1 値：SME | SME | SME | Large | SME
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0240（1 列）
- 見出し：Expenditure Type
- 例1 値：Administration | Administration | Administration | Administration | Administration
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, SME, Transaction Number

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
