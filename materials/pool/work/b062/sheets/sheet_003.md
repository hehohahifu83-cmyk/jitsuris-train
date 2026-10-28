# ラベル用シート 003 / 004

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：Main, parent or sponsoring department:
- 例1 値：Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence
  - 同じ表の列：Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0242（1 列）
- 見出し：Number of non-payroll staff (contingent labour and consultan
- 例1 値：1 | 0 | Agency staff (clerical/admin) | 10 | 0
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0243（1 列）
- 見出し：Grand Total (workforce numbers)
- 例1 値：40664 | 204 | 848 | 11115 | Headcount
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0244（1 列）
- 見出し：Payroll staff costs
- 例1 値：118708270 | Salary | 968300.42 | 32098353.18 | 232327.03
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…

## g0245（1 列）
- 見出し：Non-Payroll staff (contingent labour/consultancy) costs
- 例1 値：1356204.94 | 35869.05 | 10159260.4 | 181154 | 7861443.5
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Grand Total paybill…

## g0246（1 列）
- 見出し：Grand Total paybill/staffing (payroll and non-payroll) costs
- 例1 値：467221 | 180296534.3 | 20935554.5 | 1432576.87 | 54309203.91
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…

## g0247（1 列）
- 見出し：Minister
- 例1 値：EARL HOWE | TOBIAS ELLWOOD | GAVIN WILLIAMSON | MARK LANCASTER | GAVIN WILLIAMSON
  - 同じ表の列：Start Date of Trip, End Date of Trip, Destination, Purpose of Trip, Mode of Transport, Cost of private jet…, Number of officials…, Total cost (for min…

## g0248（1 列）
- 見出し：Start Date of Trip
- 例1 値：20/02/2019 | 07/02/2019 | 19/02/2019 | 14/02/2019 | Nil Return
  - 同じ表の列：Minister, End Date of Trip, Destination, Purpose of Trip, Mode of Transport, Cost of private jet…, Number of officials…, Total cost (for min…

## g0249（1 列）
- 見出し：End Date of Trip
- 例1 値：17/02/2019 | Nil Return | 20/02/2019 | 16/02/2019 | 19/03/2019
  - 同じ表の列：Minister, Start Date of Trip, Destination, Purpose of Trip, Mode of Transport, Cost of private jet…, Number of officials…, Total cost (for min…

## g0250（1 列）
- 見出し：Destination
- 例1 値：Legas Vegas - USA | Brussels, Belgium | Abu Dhabi, UAE and Kuwait | Munich, Germany | Zagan and Poznan, Poland
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Purpose of Trip, Mode of Transport, Cost of private jet…, Number of officials…, Total cost (for min…

## g0251（1 列）
- 見出し：Purpose of Trip
- 例1 値：Attend the International Defence Exhibi… | Visiting Troops | Foreign Affairs Council-Defence | Visit Nellis Airforce Base and 29 Palms | VIP Day, UK/US Military Exercise
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Destination, Mode of Transport, Cost of private jet…, Number of officials…, Total cost (for min…

## g0252（1 列）
- 見出し：Mode of Transport
- 例1 値：No 32 (The Royal) Squadron | Scheduled flight | No 32 (The Royal) Squadron | Eurostar | Scheduled flight
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Destination, Purpose of Trip, Cost of private jet…, Number of officials…, Total cost (for min…

## g0253（1 列）
- 見出し：Cost of private jet or RAF plane hire, if relevant (」)
- 例1 値：」0.00 | 」0.00 | 」0.00 | 」0.00 | 」0.00
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Destination, Purpose of Trip, Mode of Transport, Number of officials…, Total cost (for min…

## g0254（1 列）
- 見出し：Number of officials who accompanied minister if non-shcedule
- 例1 値：0 | 0 | 2 | 0 | 0
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Destination, Purpose of Trip, Mode of Transport, Cost of private jet…, Total cost (for min…

## g0255（1 列）
- 見出し：Total cost (for minister only) including all visas, accommod
- 例1 値：」18.25 | 0 | 」2,349.12 | 」2,731.00 | 」339.00
  - 同じ表の列：Minister, Start Date of Trip, End Date of Trip, Destination, Purpose of Trip, Mode of Transport, Cost of private jet…, Number of officials…

## g0256（1 列）
- 見出し：Matched pairs (and unmatched 'treated' offenders)
- 例1 値：15 or more | 30-34 | 18-20 | Males | 90
  - 同じ表の列：42,352 (0), 36,391 (5)

## g0257（1 列）
- 見出し：42,352 (0)
- 例1 値：54.70% | reference category | 65.30% | 69.30% | 1.072
  - 同じ表の列：Matched pairs (and …, 36,391 (5)

## g0258（1 列）
- 見出し：36,391 (5)
- 例1 値：Community Order | Frequency of re-offences per offender | 1.66 | Immediate Custody <12 months (1) compar… | 62.50%
  - 同じ表の列：Matched pairs (and …, 42,352 (0)

## g0259（1 列）
- 見出し：Organisation
- 例1 値：Northern Ireland Office | Scotland Office | Ministry of Justice (excl agencies) | Wales Office | National Offender Management Service
  - 同じ表の列：Main department, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, Number of staff in …, Median NCPRP for th…, Cost of end of year…

## g0260（1 列）
- 見出し：Annual Paybill (delegated grades for financial year 2012/13)
- 例1 値：」22,589,670 | 」888,962 | 」12,418,723 | 」4,283,902 | 」510,683,980
  - 同じ表の列：Main department, Organisation, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, Number of staff in …, Median NCPRP for th…, Cost of end of year…

## g0261（1 列）
- 見出し：Headcount (delegated grades as at 31 March 2013)
- 例1 値：580 | 480 | 21 | 42684 | 19366
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Cost of in-year NCP…, Number of staff in …, Number of staff in …, Median NCPRP for th…, Cost of end of year…

## g0262（1 列）
- 見出し：Cost of in-year NCPRP for delegated grades (」s)
- 例1 値：」2,250 | 」0 | 」652,611 | 」570,048 | 」11,300
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, Number of staff in …, Number of staff in …, Median NCPRP for th…, Cost of end of year…

## g0263（1 列）
- 見出し：Number of staff in delegated grades receiving an in-year NCP
- 例1 値：25.90% | 15.00% | 3.10% | 0.00% | 2.00%
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, Median NCPRP for th…, Cost of end of year…

## g0264（1 列）
- 見出し：Median NCPRP for those receiving an in-year NCPRP fopr deleg
- 例1 値：」400 | 」400 | 」250 | 」150 | 」350
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, Number of staff in …, Cost of end of year…

## g0265（1 列）
- 見出し：Cost of end of year NCPRP for delegated grades (」s)
- 例1 値：」7,800 | 」22,000 | 」3,400 | 」862,990 | 」132,963
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, Number of staff in …, Median NCPRP for th…

## g0266（1 列）
- 見出し：Number of staff in delegated grades receiving an end of year
- 例1 値：25 | 5 | 15 | 2 | 3973
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, Cost of in-year NCP…, Number of staff in …, Number of staff in …, Median NCPRP for th…

## g0267（1 列）
- 見出し：Organisation
- 例1 値：Borough of Pendle | Borough of Pendle | Borough of Pendle | Borough of Pendle | Borough of Pendle
  - 同じ表の列：Effective Date, UPRN (LLPG), Unique Asset ID, Locality, Town, Co-Ordinate Ref. sy…, Eastings, Northings

## g0268（1 列）
- 見出し：Effective Date
- 例1 値：31/03/2020 | 31/03/2020 | 31/03/2020 | 31/03/2020 | 31/03/2020
  - 同じ表の列：Organisation, UPRN (LLPG), Unique Asset ID, Locality, Town, Co-Ordinate Ref. sy…, Eastings, Northings

## g0269（1 列）
- 見出し：UPRN (LLPG)
- 例1 値：10090963850 | 10024183969 | 10090963979 | 10090964515 | 10090964297
  - 同じ表の列：Organisation, Effective Date, Unique Asset ID, Locality, Town, Co-Ordinate Ref. sy…, Eastings, Northings

## g0270（1 列）
- 見出し：Unique Asset ID
- 例1 値：06690/9001/2/000 | 04620/9003/2/000 | 05050/9002/2/000 | 09730/9002/2/000 | 06210/9001/2/000
  - 同じ表の列：Organisation, Effective Date, UPRN (LLPG), Locality, Town, Co-Ordinate Ref. sy…, Eastings, Northings

## g0271（1 列）
- 見出し：Locality
- 例1 値：LOMESHAYE | BRIERFIELD | HIGHAM | SALTERFORTH | BRIERFIELD
  - 同じ表の列：Organisation, Effective Date, UPRN (LLPG), Unique Asset ID, Town, Co-Ordinate Ref. sy…, Eastings, Northings

## g0272（1 列）
- 見出し：Town
- 例1 値：NELSON | COLNE | NELSON | COLNE | NELSON
  - 同じ表の列：Organisation, Effective Date, UPRN (LLPG), Unique Asset ID, Locality, Co-Ordinate Ref. sy…, Eastings, Northings

## g0273（1 列）
- 見出し：Co-Ordinate Ref. system
- 例1 値：O.S. | O.S. | O.S. | O.S. | O.S.
  - 同じ表の列：Organisation, Effective Date, UPRN (LLPG), Unique Asset ID, Locality, Town, Eastings, Northings

## g0274（1 列）
- 見出し：Eastings
- 例1 値：388915 | 385606 | 384780 | 389127 | 387400
  - 同じ表の列：Organisation, Effective Date, UPRN (LLPG), Unique Asset ID, Locality, Town, Co-Ordinate Ref. sy…, Northings

## g0275（1 列）
- 見出し：Northings
- 例1 値：437213 | 440350 | 440530 | 437316 | 437505
  - 同じ表の列：Organisation, Effective Date, UPRN (LLPG), Unique Asset ID, Locality, Town, Co-Ordinate Ref. sy…, Eastings

## g0276（1 列）
- 見出し：Tenure
- 例1 値：FREEHOLD | FREEHOLD | FREEHOLD | FREEHOLD | FREEHOLD
  - 同じ表の列：Organisation, Effective Date, UPRN (LLPG), Unique Asset ID, Locality, Town, Co-Ordinate Ref. sy…, Eastings

## g0277（1 列）
- 見出し：Invoice Date
- 例1 値：10/01/2013 | 18/01/2013 | 04/01/2013 | 03/01/2013 | 08/01/2013
  - 同じ表の列：Proclass Category, Service Area, Invoiced

## g0278（1 列）
- 見出し：Proclass Category
- 例1 値：Housing Management | Social Community Care Supplies & Servic… | Social Community Care Supplies & Servic… | REDACTED | Social Community Care Supplies & Servic…
  - 同じ表の列：Invoice Date, Service Area, Invoiced

## g0279（1 列）
- 見出し：Service Area
- 例1 値：CORPORATE SERVICES | REDACTED | SUPPORT FOR LEARNING | CSF TARGETED SUPPORT | CORPORATE SERVICES
  - 同じ表の列：Invoice Date, Proclass Category, Invoiced

## g0280（1 列）
- 見出し：Invoiced
- 例1 値：」639.45 | 」3,150.00 | 」4,975.74 | 」1,700.00 | 」3,650.00
  - 同じ表の列：Invoice Date, Proclass Category, Service Area

## g0281（1 列）
- 見出し：Property Ref
- 例1 値：Ref:15561721513865 | Ref:11378998470826 | Ref:21529900340034 | Ref:15672800306072 | Ref:15275300080097
  - 同じ表の列：Rate Payer, Start of Liability, Rateable Value 2010, Empty, Empty From, Charity, Discretionary relie…, Mandatory Relief %

## g0282（1 列）
- 見出し：Rate Payer
- 例1 値：CO-OPERATIVE GROUP LTD | BOWSER SUPPLY LIMITED | BIZSPACE PLC | APPLICATION TAPE CO LTD | DOWLIS CORPORATE SOLUTIONS LTD
  - 同じ表の列：Property Ref, Start of Liability, Rateable Value 2010, Empty, Empty From, Charity, Discretionary relie…, Mandatory Relief %

## g0283（1 列）
- 見出し：Start of Liability
- 例1 値：01.05.2011 | 27.02.2011 | 01.04.2014 | 10.09.2012 | 01.08.2008
  - 同じ表の列：Property Ref, Rate Payer, Rateable Value 2010, Empty, Empty From, Charity, Discretionary relie…, Mandatory Relief %

## g0284（1 列）
- 見出し：Rateable Value 2010
- 例1 値：6600 | 5200 | 21250 | 19250 | 79500
  - 同じ表の列：Property Ref, Rate Payer, Start of Liability, Empty, Empty From, Charity, Discretionary relie…, Mandatory Relief %

## g0285（1 列）
- 見出し：Empty
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Property Ref, Rate Payer, Start of Liability, Rateable Value 2010, Empty From, Charity, Discretionary relie…, Mandatory Relief %

## g0286（1 列）
- 見出し：Empty From
- 例1 値：01.04.2010 | 01.01.2015 | 28.03.2013 | 11.04.2014 | 01.09.2008
  - 同じ表の列：Property Ref, Rate Payer, Start of Liability, Rateable Value 2010, Empty, Charity, Discretionary relie…, Mandatory Relief %

## g0287（1 列）
- 見出し：Charity
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Property Ref, Rate Payer, Start of Liability, Rateable Value 2010, Empty, Empty From, Discretionary relie…, Mandatory Relief %

## g0288（1 列）
- 見出し：Discretionary relief %
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Property Ref, Rate Payer, Start of Liability, Rateable Value 2010, Empty, Empty From, Charity, Mandatory Relief %

## g0289（1 列）
- 見出し：Mandatory Relief %
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Property Ref, Rate Payer, Start of Liability, Rateable Value 2010, Empty, Empty From, Charity, Discretionary relie…

## g0290（1 列）
- 見出し：Small Business Rate Relief
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Property Ref, Rate Payer, Start of Liability, Rateable Value 2010, Empty, Empty From, Charity, Discretionary relie…

## g0291（1 列）
- 見出し：reference
- 例1 値：A4DA01 | A4DA07 | A4DA02 | A4DA03 | A4DA04
  - 同じ表の列：geometry, uprn, article_4_direction, permitted_developme…, notes, start_date, entry_date

## g0292（1 列）
- 見出し：geometry
- 例1 値：MULTIPOLYGON (((-2.233015 53.694841, -2… | MULTIPOLYGON (((-2.319066 53.665597, -2… | MULTIPOLYGON (((-2.315719 53.678241, -2… | MULTIPOLYGON (((-2.335258 53.722586, -2… | MULTIPOLYGON (((-2.291147 53.708762, -2…
  - 同じ表の列：reference, uprn, article_4_direction, permitted_developme…, notes, start_date, entry_date

## g0293（1 列）
- 見出し：uprn
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：reference, geometry, article_4_direction, permitted_developme…, notes, start_date, entry_date

## g0294（1 列）
- 見出し：article_4_direction
- 例1 値：A4D03 | A4D02 | A4D01 | A4D04 | A4D07
  - 同じ表の列：reference, geometry, uprn, permitted_developme…, notes, start_date, entry_date

## g0295（1 列）
- 見出し：permitted_development_rights
- 例1 値：6A ; 6B | 6A ; 6B | 1D ; 1F ; 6A ; 6B | 1A ; 1D ; 1E ; 1F ; 2A ; 2B ; 2C ; 4B | 1A ; 1B ; 1C ; 1D ; 1E
  - 同じ表の列：reference, geometry, uprn, article_4_direction, notes, start_date, entry_date

## g0296（1 列）
- 見出し：notes
- 例1 値：The directions apply to land comprising… | The directions apply to all land within… | The directions apply to land at Leabroo… | The directions apply to development aff… | The directions apply to all dwellings i…
  - 同じ表の列：reference, geometry, uprn, article_4_direction, permitted_developme…, start_date, entry_date

## g0297（1 列）
- 見出し：start_date
- 例1 値：1991-04-15 | 2025-09-19 | 1992-11-18 | 1991-09-23 | 1988-10-31
  - 同じ表の列：reference, geometry, uprn, article_4_direction, permitted_developme…, notes, entry_date

## g0298（1 列）
- 見出し：entry_date
- 例1 値：2025-09-23 | 1991-04-15 | 1983-10-04 | 1992-10-16 | 1988-10-31
  - 同じ表の列：reference, geometry, uprn, article_4_direction, permitted_developme…, notes, start_date

## g0299（4 列）
- 見出し：OrganisationURI
- 例1 値：http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr…
  - 同じ表の列：SiteReference, SiteplanURL, GeoY, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr…
  - 同じ表の列：OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0300（2 列）
- 見出し：SiteReference
- 例1 値：ROSBS006 | ROSBS037 | ROSBS017 | ROSBS010 | ROSBS055
  - 同じ表の列：OrganisationURI, SiteplanURL, GeoY, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：BLR22 | BLR21 | BLR13 | BLR16 | BLR9
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0301（3 列）
- 見出し：SiteplanURL
- 例1 値：https://www.rossendale.gov.uk/downloads… | https://www.rossendale.gov.uk/downloads… | https://www.rossendale.gov.uk/downloads… | https://www.rossendale.gov.uk/downloads… | https://www.rossendale.gov.uk/downloads…
  - 同じ表の列：OrganisationURI, SiteReference, GeoY, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：https://my.southlakeland.gov.uk/mysouth… | https://my.southlakeland.gov.uk/mysouth… | https://my.southlakeland.gov.uk/mysouth… | https://my.southlakeland.gov.uk/mysouth… | https://my.southlakeland.gov.uk/mysouth…
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0302（2 列）
- 見出し：GeoY
- 例1 値：53.717264 | 53.7176 | 53.7056 | 53.6591 | 53.7072823
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：54.31999 | 54.20233 | 54.20319 | 54.1945 | 54.33103
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, Hectares, Deliverable

## g0303（2 列）
- 見出し：GeoX
- 例1 値：-2.19535 | -2.19935 | -2.328928 | -2.25017 | -2.18283
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：-2.83006 | -3.08743 | -2.742 | -3.06312 | -2.74216
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoY, Hectares, Deliverable

## g0304（3 列）
- 見出し：Hectares
- 例1 値：0.07 | 0.1 | 0.22 | 0.09 | 0.07
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, GeoX, PlanningStatus, PermissionType, PermissionDate
- 例2 値：0.07 | 3.09 | 0.07 | 0.48 | 0.28
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Deliverable

## g0305（3 列）
- 見出し：PlanningStatus
- 例1 値：permissioned | permissioned | not permissioned | permissioned | not permissioned
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, PermissionType, PermissionDate
- 例2 値：permissioned | not permissioned | not permissioned | permissioned | pending decision
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares

## g0306（1 列）
- 見出し：PermissionType
- 例1 値：full planning permission | full planning permission | full planning permission | full planning permission | full planning permission
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, PlanningStatus, PermissionDate

## g0307（1 列）
- 見出し：PermissionDate
- 例1 値：28/08/2024 | 08/09/2021 | 01/03/2018 | 16/10/2015 | 11/05/2022
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, PlanningStatus, PermissionType

## g0308（1 列）
- 見出し：PlanningHistory
- 例1 値：https://publicaccess.rossendale.gov.uk/… | https://publicaccess.rossendale.gov.uk/… | https://publicaccess.rossendale.gov.uk/… | https://publicaccess.rossendale.gov.uk/… | https://publicaccess.rossendale.gov.uk/…
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, PlanningStatus, PermissionType

## g0309（2 列）
- 見出し：FID
- 例1 値：lp_2030_local_green_spaces.26 | lp_2030_local_green_spaces.20 | lp_2030_local_green_spaces.2 | lp_2030_local_green_spaces.48 | lp_2030_local_green_spaces.11
  - 同じ表の列：id, area, greenbelt
- 例2 値：lp_2030_strategic_employment_areas.6 | lp_2030_strategic_employment_areas.3 | lp_2030_strategic_employment_areas.2 | lp_2030_strategic_employment_areas.5 | lp_2030_strategic_employment_areas.1
  - 同じ表の列：id, code, location, plan

## g0310（3 列）
- 見出し：id
- 例1 値：26 | 20 | 51 | 2 | 22
  - 同じ表の列：FID, area, greenbelt
- 例2 値：8 | 2 | 3 | 1 | 4
  - 同じ表の列：FID, code, location, plan

## g0311（1 列）
- 見出し：area
- 例1 値：3625.3595 | 46265.4440296 | 38914.2309977 | 13456.0973753 | 3424.00934382
  - 同じ表の列：FID, id, greenbelt

## g0312（1 列）
- 見出し：greenbelt
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：FID, id, area

## g0313（2 列）
- 見出し：code
- 例1 値：IE2 | IE2 | IE2 | IE2 | IE2
  - 同じ表の列：FID, id, location, plan
- 例2 値：IE6 | IE6 | IE6 | IE6 | IE6
  - 同じ表の列：FID, id, class, plan

## g0314（1 列）
- 見出し：location
- 例1 値：Longcross Park Enterprise Zone | The Causeway and Pinetrees Business Park | Thorpe Industrial Estate | The Causeway and Pinetrees Business Park | Hillswood Business Park
  - 同じ表の列：FID, id, code, plan

## g0315（2 列）
- 見出し：plan
- 例1 値：Runnymede 2030 Local Plan, Adopted 16th… | Runnymede 2030 Local Plan, Adopted 16th… | Runnymede 2030 Local Plan, Adopted 16th… | Runnymede 2030 Local Plan, Adopted 16th… | Runnymede 2030 Local Plan, Adopted 16th…
  - 同じ表の列：FID, id, code, location
- 例2 値：Runnymede 2030 Local Plan, Adopted 16th… | Runnymede 2030 Local Plan, Adopted 16th… | Runnymede 2030 Local Plan, Adopted 16th… | Runnymede 2030 Local Plan, Adopted 16th… | Runnymede 2030 Local Plan, Adopted 16th…
  - 同じ表の列：FID, id, class, code

## g0316（1 列）
- 見出し：FID
- 例1 値：lp_2030_shopping_frontages.20 | lp_2030_shopping_frontages.49 | lp_2030_shopping_frontages.35 | lp_2030_shopping_frontages.6 | lp_2030_shopping_frontages.50
  - 同じ表の列：id, class, plan, code

## g0317（1 列）
- 見出し：class
- 例1 値：Secondary | Secondary | Secondary | Primary | Primary
  - 同じ表の列：FID, id, plan, code

## g0318（1 列）
- 見出し：Registration Number
- 例1 値：PN72 CBF | MC65 WAO | HK74 NFP | MT59 JNJ | HK74 NFR
  - 同じ表の列：Type of body fitted, Make, Model, Date of acquisition, Leased/owned, Fuel type

## g0319（1 列）
- 見出し：Type of body fitted
- 例1 値：Single Cab | Titan Ecopac | Hatchback | Hatchback | Titan Ecopac
  - 同じ表の列：Registration Number, Make, Model, Date of acquisition, Leased/owned, Fuel type

## g0320（1 列）
- 見出し：Make
- 例1 値：MG | Toyota | MG | Mitsubishi | Mitsubishi
  - 同じ表の列：Registration Number, Type of body fitted, Model, Date of acquisition, Leased/owned, Fuel type

## g0321（1 列）
- 見出し：Model
- 例1 値：Fuso | MG4 EV | MG4 EV | Vivaro | MG4 EV
  - 同じ表の列：Registration Number, Type of body fitted, Make, Date of acquisition, Leased/owned, Fuel type

## g0322（1 列）
- 見出し：Date of acquisition
- 例1 値：Oct-22 | Jan-25 | Oct-22 | Jan-20 | Oct-22
  - 同じ表の列：Registration Number, Type of body fitted, Make, Model, Leased/owned, Fuel type

## g0323（1 列）
- 見出し：Leased/owned
- 例1 値：Owned | Owned | Leased | Leased | Owned
  - 同じ表の列：Registration Number, Type of body fitted, Make, Model, Date of acquisition, Fuel type

## g0324（1 列）
- 見出し：Fuel type
- 例1 値：diesel | diesel | diesel | diesel | electric
  - 同じ表の列：Registration Number, Type of body fitted, Make, Model, Date of acquisition, Leased/owned

## g0325（1 列）
- 見出し：2
- 例1 値：274 | 365 | 136 | 323 | 11
  - 同じ表の列：ACE, Royal Mail Group Ltd, Single award contra…, 05/04/2023, 05/04/2026, £28,008.00, 4138203, No

## g0326（1 列）
- 見出し：ACE
- 例1 値：Property & Growth | Property & Growth | Operational Services | Operational Services | ACE
  - 同じ表の列：2, Royal Mail Group Ltd, Single award contra…, 05/04/2023, 05/04/2026, £28,008.00, 4138203, No

## g0327（1 列）
- 見出し：Royal Mail Group Ltd
- 例1 値：Confirm Solutions Ltd | Twilio Ireland Limited | Enterprise Rent-A-Car UK Limited | Ross & Roberts | Hampshire County Council
  - 同じ表の列：2, ACE, Single award contra…, 05/04/2023, 05/04/2026, £28,008.00, 4138203, No

## g0328（1 列）
- 見出し：Single award contract
- 例1 値：Single | single award contract. Must have suppli… | Unknown | Support contract | single award
  - 同じ表の列：2, ACE, Royal Mail Group Ltd, 05/04/2023, 05/04/2026, £28,008.00, 4138203, No

## g0329（1 列）
- 見出し：05/04/2023
- 例1 値：11/09/2023 | 01/11/2025 | 01/05/2022 | 20/10/2025 | 01/04/2021
  - 同じ表の列：2, ACE, Royal Mail Group Ltd, Single award contra…, 05/04/2026, £28,008.00, 4138203, No

## g0330（1 列）
- 見出し：05/04/2026
- 例1 値：01/01/2027 | 31/03/2026 | 31/03/2028 | 31/12/2026 | 30/04/2026
  - 同じ表の列：2, ACE, Royal Mail Group Ltd, Single award contra…, 05/04/2023, £28,008.00, 4138203, No

## g0331（1 列）
- 見出し：£28,008.00
- 例1 値：£164,500.00 | £17,209.23 | £978.00 | £68,785.15 | £14,000.00
  - 同じ表の列：2, ACE, Royal Mail Group Ltd, Single award contra…, 05/04/2023, 05/04/2026, 4138203, No

## g0332（1 列）
- 見出し：4138203
- 例1 値：13868441 | 6695717 | 12745191 | 2512508 | 3295353
  - 同じ表の列：2, ACE, Royal Mail Group Ltd, Single award contra…, 05/04/2023, 05/04/2026, £28,008.00, No

## g0333（1 列）
- 見出し：No
- 例1 値：No | Yes | No | No | Yes
  - 同じ表の列：2, ACE, Royal Mail Group Ltd, Single award contra…, 05/04/2023, 05/04/2026, £28,008.00, 4138203

## g0334（1 列）
- 見出し：Exemption
- 例1 値：Request for Quotes | Other (add details to comments section) | Framework Agreement | Request for Quotes | Request for Quotes
  - 同じ表の列：2, ACE, Royal Mail Group Ltd, Single award contra…, 05/04/2023, 05/04/2026, £28,008.00, 4138203

## g0335（1 列）
- 見出し：Year
- 例1 値：2020/21 | 2021/22 | 2023/24 | 2016/17 | 2022/23
  - 同じ表の列：Number of Occasions…, Total Number of Emp…, Total Number of Pro…, Total Amount Spent …, Total Number of Fra…

## g0336（1 列）
- 見出し：Number of Occasions that Rushmoor Counter Fraud Officers use
- 例1 値：0 | 8 | 0 | 0 | 0
  - 同じ表の列：Year, Total Number of Emp…, Total Number of Pro…, Total Amount Spent …, Total Number of Fra…

## g0337（1 列）
- 見出し：Total Number of Employees Undertaking Investigations and Pro
- 例1 値：0 * | 2 | 2 | 1.6 | 2
  - 同じ表の列：Year, Number of Occasions…, Total Number of Pro…, Total Amount Spent …, Total Number of Fra…

## g0338（1 列）
- 見出し：Total Number of Professionally Accredited Counter Fraud Spec
- 例1 値：2 | 0 | 1.6 | 1.6 | 2
  - 同じ表の列：Year, Number of Occasions…, Total Number of Emp…, Total Amount Spent …, Total Number of Fra…

## g0339（1 列）
- 見出し：Total Amount Spent by the Authority on the Investigation and
- 例1 値：」- | 」91,216.00 | 」96,026.00 | 」81,178.00 | 」96,029.00
  - 同じ表の列：Year, Number of Occasions…, Total Number of Emp…, Total Number of Pro…, Total Number of Fra…

## g0340（1 列）
- 見出し：Total Number of Fraud Cases Investigated
- 例1 値：659 | 84 | 137 | 572 | 812
  - 同じ表の列：Year, Number of Occasions…, Total Number of Emp…, Total Number of Pro…, Total Amount Spent …

## g0341（2 列）
- 見出し：Entity
- 例1 値：SO1 | SO1 | SO1 | SO1 | SO1
  - 同じ表の列：Department Family, Date, Expense Type, Expense Reason, Expense Area, Supplier, Transaction Number, Amount
- 例2 値：SO1 | SO1 | SO1 | SO1 | SO1
  - 同じ表の列：Department Family, Date, Expense Type, Expense Reason, Expense Area, Supplier, Transaction Number, Amount

## g0342（2 列）
- 見出し：Expense Type
- 例1 値：Rates | Rent | Travel | Travel | Repairs & Maintenance - Buildings
  - 同じ表の列：Department Family, Entity, Date, Expense Reason, Expense Area, Supplier, Transaction Number, Amount
- 例2 値：Repairs & Maintenance - Buildings | Travel | Rent | Repairs & Maintenance - Buildings | Repairs & Maintenance - Buildings
  - 同じ表の列：Department Family, Entity, Date, Expense Reason, Expense Area, Supplier, Transaction Number, Amount

## g0343（1 列）
- 見出し：Expense Reason
- 例1 値：Dover House | Dover House | Monthly travel costs | Yearly Payment of Rates | Monthly travel costs
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0344（2 列）
- 見出し：Expense Area
- 例1 値：Corporate & Constitutional - Edinburgh | Corporate & Constitutional - London | Corporate & Constitutional - Edinburgh | Corporate & Constitutional - Edinburgh | Corporate & Constitutional - London
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Reason, Supplier, Transaction Number, Amount
- 例2 値：Corporate & Constitutional - London | Corporate & Constitutional - London | Corporate & Constitutional - London | Corporate & Constitutional - Edinburgh | Corporate & Constitutional - Edinburgh
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Reason, Supplier, Transaction Number, Amount

## g0345（1 列）
- 見出し：Transaction Number
- 例1 値：SIN000503 | R7018612090701 | R7018612090401 | 3179757209 | IND/190/HQ/4201
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Reason, Expense Area, Supplier, Amount

## g0346（2 列）
- 見出し：Amount
- 例1 値：」35,889.28 | 」43,866.28 | 」37,897.54 | 」29,063.75 | 」35,002.55
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Reason, Expense Area, Supplier, Transaction Number
- 例2 値：」43,768.76 | 」43,866.28 | 」32,200.00 | 」35,889.28 | 」56,502.50
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Reason, Expense Area, Supplier, Transaction Number

## g0347（1 列）
- 見出し：VAT Registration No
- 例1 値：649 2064 28 | 984380190 | 649 4235 17 | 888 8180 55 | 888 8425 51
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Reason, Expense Area, Supplier, Transaction Number

## g0348（1 列）
- 見出し：Expense Reason
- 例1 値：Monthly travel costs | Yearly Payment of Rates | Gas & Electricity costs for Dover House | Maintenance System Support Costs | Dover House
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0349（1 列）
- 見出し：Supplier
- 例1 値：M J Ferguson Ltd | Ministry of Justice | Security Services Group | Ministry of Justice | Ministry of Justice
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Reason, Expense Area, Transaction Number, Amount

## g0350（1 列）
- 見出し：Transaction Number
- 例1 値：OP/I091817 | IND/190/HQ/4201 | 3179757209 | IND190HQ/3905 | 21265
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Reason, Expense Area, Supplier, Amount

## g0351（1 列）
- 見出し：VAT Registration No
- 例1 値：888 8180 55 | 649 4235 17 | 649 2064 28 | 649 2064 28 | 888 8425 51
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Reason, Expense Area, Supplier, Transaction Number

## g0352（1 列）
- 見出し：ESF_Co-financing_Plan_region
- 例1 値：London | North West | East Midlands | London | Yorkshire and The Humber
  - 同じ表の列：UPIN, UKPRN, Contract_value, Contract_end_date

## g0353（1 列）
- 見出し：UPIN
- 例1 値：115949 | 105353 | 107632 | 108526 | 106509
  - 同じ表の列：ESF_Co-financing_Pl…, UKPRN, Contract_value, Contract_end_date

## g0354（1 列）
- 見出し：UKPRN
- 例1 値：10004676 | 10021314 | 10019581 | 10001476 | 10013308
  - 同じ表の列：ESF_Co-financing_Pl…, UPIN, Contract_value, Contract_end_date

## g0355（1 列）
- 見出し：Contract_value
- 例1 値：1981030 | 699300 | 701677 | 1051934 | 1240000
  - 同じ表の列：ESF_Co-financing_Pl…, UPIN, UKPRN, Contract_end_date

## g0356（1 列）
- 見出し：Contract_end_date
- 例1 値：31/07/2015 | 31/07/2015 | 31/03/2015 | 31/07/2015 | 31/07/2015
  - 同じ表の列：ESF_Co-financing_Pl…, UPIN, UKPRN, Contract_value

## g0357（1 列）
- 見出し：OrganisationLabel
- 例1 値：South Lakeland District Council | South Lakeland District Council | South Lakeland District Council | South Lakeland District Council | South Lakeland District Council
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0358（2 列）
- 見出し：CoordinateReferenceSystem
- 例1 値：ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, GeoX, GeoY, Hectares, Deliverable
- 例2 値：OSGB36 | OSGB36 | OSGB36 | OSGB36 | OSGB36
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, GeoX, GeoY, Hectares, Deliverable

## g0359（2 列）
- 見出し：Deliverable
- 例1 値：yes | yes | yes | yes | yes
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares
- 例2 値：yes | yes | yes | yes | yes
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares

## g0360（1 列）
- 見出し：Transaction No.
- 例1 値：39942 | 39825 | 39938 | 39865 | 39733
  - 同じ表の列：Date, Amount, Expense Area, Expense Type, Expense Code, Service Area

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
