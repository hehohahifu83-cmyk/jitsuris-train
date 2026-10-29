# ラベル用シート 001 / 003

- LABEL_GUIDE v2.1 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（5 列）
- 見出し：OrganisationURI
- 例1 値：http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr…
  - 同じ表の列：OrganisationLabel, SiteReference, PreviouslyPartOf, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares
- 例2 値：http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr…
  - 同じ表の列：ExtractDate, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, CoordinateReference…, GeoX, GeoY, GeoPointLicensingURL

## g0002（2 列）
- 見出し：OrganisationLabel
- 例1 値：Bassetlaw District Council | Bassetlaw District Council | Bassetlaw District Council | Bassetlaw District Council | Bassetlaw District Council
  - 同じ表の列：OrganisationURI, SiteReference, PreviouslyPartOf, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares
- 例2 値：Tendring District Council | Tendring District Council | Tendring District Council | Tendring District Council | Tendring District Council
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0003（1 列）
- 見出し：SiteReference
- 例1 値：LAA472 | LAA147 | BFR53 | BFR46 | BFR43
  - 同じ表の列：OrganisationURI, OrganisationLabel, PreviouslyPartOf, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares

## g0004（1 列）
- 見出し：PreviouslyPartOf
- 例1 値：BFR22 | BFR37 | BFR20 | BFR32 | BFR10
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares

## g0005（2 列）
- 見出し：SiteplanURL
- 例1 値：https://arcgisportal.bassetlaw.gov.uk/a… | https://arcgisportal.bassetlaw.gov.uk/a… | https://arcgisportal.bassetlaw.gov.uk/a… | https://arcgisportal.bassetlaw.gov.uk/a… | https://arcgisportal.bassetlaw.gov.uk/a…
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, PreviouslyPartOf, CoordinateReference…, GeoX, GeoY, Hectares
- 例2 値：https://idox.tendringdc.gov.uk/online-a… | https://idox.tendringdc.gov.uk/online-a… | https://idox.tendringdc.gov.uk/online-a… | https://idox.tendringdc.gov.uk/online-a… | https://www.tendringdc.gov.uk/sites/def…
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0006（3 列）
- 見出し：CoordinateReferenceSystem
- 例1 値：OSGB036 | OSGB036 | OSGB036 | OSGB036 | OSGB036
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, PreviouslyPartOf, SiteplanURL, GeoX, GeoY, Hectares
- 例2 値：OSGB36 | OSGB36 | OSGB36 | OSGB36 | OSGB36
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, GeoX, GeoY, GeoPointLicensingURL

## g0007（2 列）
- 見出し：GeoX
- 例1 値：470748 | 465685 | 458414 | 458825 | 458704
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, PreviouslyPartOf, SiteplanURL, CoordinateReference…, GeoY, Hectares
- 例2 値：346959 | 361237 | 340367 | 340124 | 341003
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, CoordinateReference…, GeoY, GeoPointLicensingURL

## g0008（2 列）
- 見出し：GeoY
- 例1 値：380409 | 373085 | 394650 | 379452 | 381119
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, PreviouslyPartOf, SiteplanURL, CoordinateReference…, GeoX, Hectares
- 例2 値：498561 | 504143 | 492166 | 478921 | 470992
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, CoordinateReference…, GeoX, GeoPointLicensingURL

## g0009（3 列）
- 見出し：Hectares
- 例1 値：0.93 | 0.08 | 0.16 | 1.38 | 0.1
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, PreviouslyPartOf, SiteplanURL, CoordinateReference…, GeoX, GeoY
- 例2 値：0.2100000 | 0.7900000 | 0.1700000 | 0.3200000 | 0.6800000
  - 同じ表の列：OID_, SITEREF, SITEPLANUR, GEOX, GEOY, DELIVERABL, PLANNINGST, PERMISSION

## g0010（2 列）
- 見出し：Deliverable
- 例1 値：yes | yes | yes | Yes | yes
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, PreviouslyPartOf, SiteplanURL, CoordinateReference…, GeoX, GeoY
- 例2 値：yes | yes | yes | yes | yes
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares

## g0011（1 列）
- 見出し：Pollutant
- 例1 値：O3 | NO2 | NO2 | NO2 | NO2
  - 同じ表の列：Location Type, station ID (assigne…, Easting, Northing

## g0012（1 列）
- 見出し：Location Type
- 例1 値：Background | Roadside | Roadside | Roadside | Background
  - 同じ表の列：Pollutant, station ID (assigne…, Easting, Northing

## g0013（1 列）
- 見出し：station ID (assigned by COW)
- 例1 値：4 | 5 | 9 | 3 | 1
  - 同じ表の列：Pollutant, Location Type, Easting, Northing

## g0014（1 列）
- 見出し：Easting
- 例1 値：356838 | 358667 | 359644 | 360382 | 360903
  - 同じ表の列：Pollutant, Location Type, station ID (assigne…, Northing

## g0015（1 列）
- 見出し：Northing
- 例1 値：170593 | 172209 | 173108 | 173352 | 170024
  - 同じ表の列：Pollutant, Location Type, station ID (assigne…, Easting

## g0016（1 列）
- 見出し：OID_
- 例1 値：105 | 53 | 287 | 298 | 8
  - 同じ表の列：SITEREF, SITEPLANUR, GEOX, GEOY, HECTARES, DELIVERABL, PLANNINGST, PERMISSION

## g0017（1 列）
- 見出し：SITEREF
- 例1 値：22/01005/APP | SB0339 | 22/02133/PAPCR | 23/03194/APP | 20/05684/FUL
  - 同じ表の列：OID_, SITEPLANUR, GEOX, GEOY, HECTARES, DELIVERABL, PLANNINGST, PERMISSION

## g0018（1 列）
- 見出し：SITEPLANUR
- 例1 値：https://www.buckinghamshire.gov.uk/plan… | https://www.buckinghamshire.gov.uk/plan… | https://www.buckinghamshire.gov.uk/plan… | https://www.buckinghamshire.gov.uk/plan… | https://www.buckinghamshire.gov.uk/plan…
  - 同じ表の列：OID_, SITEREF, GEOX, GEOY, HECTARES, DELIVERABL, PLANNINGST, PERMISSION

## g0019（1 列）
- 見出し：GEOX
- 例1 値：-0.632895800000000 | -0.541601320000000 | -0.822460760000000 | -0.812383240000000 | -0.658673800118000
  - 同じ表の列：OID_, SITEREF, SITEPLANUR, GEOY, HECTARES, DELIVERABL, PLANNINGST, PERMISSION

## g0020（2 列）
- 見出し：GEOY
- 例1 値：51.573900330100003 | 51.601662230000002 | 51.631700000000002 | 51.640778840000003 | 51.610342830000000
  - 同じ表の列：OID_, SITEREF, SITEPLANUR, GEOX, HECTARES, DELIVERABL, PLANNINGST, PERMISSION
- 例2 値：51.9462 | 51.77336 | 51.802337 | 51.848772 | 51.943993
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, Hectares, Deliverable

## g0021（1 列）
- 見出し：DELIVERABL
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：OID_, SITEREF, SITEPLANUR, GEOX, GEOY, HECTARES, PLANNINGST, PERMISSION

## g0022（1 列）
- 見出し：PLANNINGST
- 例1 値：Not Permissioned | Not Permissioned | Not Permissioned | Permissioned | Permissioned
  - 同じ表の列：OID_, SITEREF, SITEPLANUR, GEOX, GEOY, HECTARES, DELIVERABL, PERMISSION

## g0023（1 列）
- 見出し：PERMISSION
- 例1 値：Full planning permission | Outline planning permission | Full planning permission | Full planning permission | Full planning permission
  - 同じ表の列：OID_, SITEREF, SITEPLANUR, GEOX, GEOY, HECTARES, DELIVERABL, PLANNINGST

## g0024（1 列）
- 見出し：PERMISSI0
- 例1 値：07/09/2017 | 07/01/2022 | 03/08/2023 | 30/09/2021 | 20/08/2013
  - 同じ表の列：OID_, SITEREF, SITEPLANUR, GEOX, GEOY, HECTARES, DELIVERABL, PLANNINGST

## g0025（1 列）
- 見出し：Minister
- 例1 値：Does not normally include meetings with… | Prime Minister, The Rt Hon David Camero… | Note
  - 同じ表の列：Date, Purpose of meeting

## g0026（3 列）
- 見出し：Date
- 例1 値：July, 2010 | July, 2010 | June, 2010 | July, 2010 | July, 2010
  - 同じ表の列：Minister, Purpose of meeting
- 例2 値：Jul, 2010 | May, 2010 | Jun, 2010 | Jul, 2010 | Jun, 2010
  - 同じ表の列：Minister, Purpose of meeting

## g0027（1 列）
- 見出し：Purpose of meeting
- 例1 値：To discuss business issues | To discuss business issues | To discuss business issues | To discuss business issues | To discuss sporting and World Cup issues
  - 同じ表の列：Minister, Date

## g0028（1 列）
- 見出し：Date of Meeting
- 例1 値：Feb-13 | Feb-13 | Feb-13 | Feb-13 | Feb-13
  - 同じ表の列：Purpose of Meeting

## g0029（1 列）
- 見出し：Purpose of Meeting
- 例1 値：Keynote speech at President’s Dinner & … | Discussion on Royal Mail | Introductory | Working lunch to discuss the economic, … | UK macroeconomic outlook
  - 同じ表の列：Date of Meeting

## g0030（1 列）
- 見出し：Appointing Minister
- 例1 値：Deputy Prime Minister
  - 同じ表の列：Date of Hospitality, Type of hospitality…

## g0031（2 列）
- 見出し：Date of Hospitality
- 例1 値：03-Nov-2010 | 23-Nov-2010 | 19-Oct-2010 | 10-Nov-2010 | 28-Oct-2010
  - 同じ表の列：Appointing Minister, Type of hospitality…
- 例2 値：15-Jul-2016 | 07-Sep-2016 | 19-Sep-2016 | 07-Sep-2016 | 13-Sep-2016
  - 同じ表の列：Minister, Type of hospitality…

## g0032（1 列）
- 見出し：Type of hospitality received
- 例1 値：Dinner | Lunch | Lunch | Lunch | Drinks
  - 同じ表の列：Appointing Minister, Date of Hospitality

## g0033（1 列）
- 見出し：Department Family
- 例1 値：Cabinet Office | Cabinet Office | Cabinet Office | Cabinet Office | Cabinet Office
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount, Client

## g0034（1 列）
- 見出し：Entity
- 例1 値：Central Office of Information | Central Office of Information | Central Office of Information | Central Office of Information | Central Office of Information
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount, Client

## g0035（3 列）
- 見出し：Date
- 例1 値：17/01/12 | 17/01/12 | 17/01/12 | 03/01/12 | 10/01/12
  - 同じ表の列：Department Family, Entity, Expense Type, Expense Area, Supplier, Transaction Number, Amount, Client
- 例2 値：11/04/2014 | 29/04/2014 | 24/04/2014 | 31/03/2014 | 12/04/2014
  - 同じ表の列：TRANSACTION ID, MCC, AMOUNT, MERCHANT DETAILS

## g0036（1 列）
- 見出し：Expense Type
- 例1 値：Campaigns | Campaigns | Campaign Production | Campaigns | Campaigns
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Transaction Number, Amount, Client

## g0037（1 列）
- 見出し：Expense Area
- 例1 値：Central Office of Information | Central Office of Information | Central Office of Information | Central Office of Information | Central Office of Information
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Transaction Number, Amount, Client

## g0038（1 列）
- 見出し：Supplier
- 例1 値：M4C | The Listening Company Ltd | Fuel Data Strategies | Royal Mail | Miles Calcraft Briginshaw Duffy
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount, Client

## g0039（3 列）
- 見出し：Transaction Number
- 例1 値：10169403 | 10169476 | 10167762 | 10169485 | 10169273
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Amount, Client
- 例2 値：185454 | 186770 | 187313 | 185446 | 187319
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Amount, Supplier Type

## g0040（1 列）
- 見出し：Amount
- 例1 値：100,000.00 | 29,335.50 | 148,418.50 | 171,702.00 | 22,867.50
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Client

## g0041（1 列）
- 見出し：Client
- 例1 値：Department for Business, Innovation and… | The Money Advice Service | Department of Health | Training and Development Agency for Sch… | Department of Health
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0042（1 列）
- 見出し：Campaign
- 例1 値：Worth Talking About' 11/12 | Digital Media Sept - Dec | National Apprenticeship Service 2011/12 | Drink Drugs Sexual Health Line April - … | Customer Relationship Management 11/12
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0043（1 列）
- 見出し：Data status
- 例1 値：Received | Received | Received | Not received | Received
  - 同じ表の列：Department, Organisation, Got everything I wa…, Got most of what I …, Got some of what I …, Got none of what I …, Very Satisfied, Satisfied

## g0044（2 列）
- 見出し：Department
- 例1 値：FCO | DCMS | UKTI | DEFRA | DFT
  - 同じ表の列：Data status, Organisation, Got everything I wa…, Got most of what I …, Got some of what I …, Got none of what I …, Very Satisfied, Satisfied
- 例2 値：FCO | FCO | FCO | FCO | FCO
  - 同じ表の列：Entity, Posted Date, Internal Voucher Nu…, Invoice Line Amount…

## g0045（1 列）
- 見出し：Organisation
- 例1 値：Next Steps | Simply beef and lamb | Teaching and Development Agency | Army | UK Energy Excellence
  - 同じ表の列：Data status, Department, Got everything I wa…, Got most of what I …, Got some of what I …, Got none of what I …, Very Satisfied, Satisfied

## g0046（1 列）
- 見出し：Got everything I wanted
- 例1 値：24.5 | 57.1 | 24 | 41.3 | 30
  - 同じ表の列：Data status, Department, Organisation, Got most of what I …, Got some of what I …, Got none of what I …, Very Satisfied, Satisfied

## g0047（1 列）
- 見出し：Got most of what I wanted
- 例1 値：30 | 15.8 | 17.6 | 13 | 34
  - 同じ表の列：Data status, Department, Organisation, Got everything I wa…, Got some of what I …, Got none of what I …, Very Satisfied, Satisfied

## g0048（1 列）
- 見出し：Got some of what I wanted
- 例1 値：14.3 | 24.4 | 18 | 32.5 | 15.7
  - 同じ表の列：Data status, Department, Organisation, Got everything I wa…, Got most of what I …, Got none of what I …, Very Satisfied, Satisfied

## g0049（1 列）
- 見出し：Got none of what I wanted
- 例1 値：33.5 | 14 | 9 | 22.2 | 4.1
  - 同じ表の列：Data status, Department, Organisation, Got everything I wa…, Got most of what I …, Got some of what I …, Very Satisfied, Satisfied

## g0050（1 列）
- 見出し：Very Satisfied
- 例1 値：16 | 17.9 | 33.03 | 35.6 | 23.8
  - 同じ表の列：Data status, Department, Organisation, Got everything I wa…, Got most of what I …, Got some of what I …, Got none of what I …, Satisfied

## g0051（1 列）
- 見出し：Satisfied
- 例1 値：36 | 30.9 | 34 | 42.7 | 50
  - 同じ表の列：Data status, Department, Organisation, Got everything I wa…, Got most of what I …, Got some of what I …, Got none of what I …, Very Satisfied

## g0052（1 列）
- 見出し：Neither satisfied nor dissatisfied
- 例1 値：12.9 | 24 | 15 | 23.1 | 13
  - 同じ表の列：Data status, Department, Organisation, Got everything I wa…, Got most of what I …, Got some of what I …, Got none of what I …, Very Satisfied

## g0053（1 列）
- 見出し：Permanent secretary
- 例1 値：Jon Thompson -PUS | Commander JFC - General Richard Barons | 1st Sea Lord - Admiral Sir George Zambe… | CAS - Air Chief Marshall Sir Andrew Pul… | CDS- General Sir Nicholas Houghton
  - 同じ表の列：Date, Purpose of meeting

## g0054（1 列）
- 見出し：Date
- 例1 値：Feb-16 | Jan | Feb-16 | 2/2/16 | Feb
  - 同じ表の列：Permanent secretary, Purpose of meeting

## g0055（1 列）
- 見出し：Purpose of meeting
- 例1 値：Teleconference | Official visit Warton site | Update in defence portfolio | CIVILIAN ENGAGMENT WITH EMPLOYERS | Telephone conference
  - 同じ表の列：Permanent secretary, Date

## g0056（1 列）
- 見出し：TRANSACTION ID
- 例1 値：306607902 | 304664753 | 306275985 | 303947084 | 307387354
  - 同じ表の列：MCC, DATE, AMOUNT, MERCHANT DETAILS

## g0057（1 列）
- 見出し：MCC
- 例1 値：8244 | 7372 | 4722 | 7011 | 7372
  - 同じ表の列：TRANSACTION ID, DATE, AMOUNT, MERCHANT DETAILS

## g0058（1 列）
- 見出し：AMOUNT
- 例1 値：857.63 | 781.45 | 5970 | 726.65 | 785.7
  - 同じ表の列：TRANSACTION ID, MCC, DATE, MERCHANT DETAILS

## g0059（1 列）
- 見出し：MERCHANT DETAILS
- 例1 値：COMPUTER PROGRAM/SYS DESIGN | HOTELS/MOTELS/RESORTS | COMPUTER PROGRAM/SYS DESIGN | BUSINESS/SECRETARIAL SCHOOL | TRAVEL AGENCIES
  - 同じ表の列：TRANSACTION ID, MCC, DATE, AMOUNT

## g0060（1 列）
- 見出し：Departmental Family
- 例1 値：Charity Commission | Charity Commission | Charity Commission | Charity Commission | Charity Commission
  - 同じ表の列：Entity, Input Date, Expense Type, Expense Area, Supplier, Transaction No, Amount, Supplier Type

## g0061（2 列）
- 見出し：Entity
- 例1 値：Charity Commission | Charity Commission | Charity Commission | Charity Commission | Charity Commission
  - 同じ表の列：Departmental Family, Input Date, Expense Type, Expense Area, Supplier, Transaction No, Amount, Supplier Type
- 例2 値：Housing Benefits | Employment Programmes | Employment Programmes | Employment Programmes | Jobcentre Plus
  - 同じ表の列：Departmental Family, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0062（1 列）
- 見出し：Input Date
- 例1 値：26/02/2014 | 11/02/2014 | 07/02/2014 | 26/02/2014 | 07/02/2014
  - 同じ表の列：Departmental Family, Entity, Expense Type, Expense Area, Supplier, Transaction No, Amount, Supplier Type

## g0063（1 列）
- 見出し：Expense Type
- 例1 値：Contract computer services | Contract computer services | Hotels/Trains/Flights | Contract computer services | Contract computer services
  - 同じ表の列：Departmental Family, Entity, Input Date, Expense Area, Supplier, Transaction No, Amount, Supplier Type

## g0064（1 列）
- 見出し：Expense Area
- 例1 値：Business Services | General Expenditure | Business Services | Business Services | Business Services
  - 同じ表の列：Departmental Family, Entity, Input Date, Expense Type, Supplier, Transaction No, Amount, Supplier Type

## g0065（1 列）
- 見出し：Supplier
- 例1 値：Level 3 Communications | Level 3 Communications | Level 3 Communications | Level 3 Communications | Attenda Limited
  - 同じ表の列：Departmental Family, Entity, Input Date, Expense Type, Expense Area, Transaction No, Amount, Supplier Type

## g0066（1 列）
- 見出し：Transaction No
- 例1 値：181539 | 10278080 | CR005228 | IN006530 | 73265
  - 同じ表の列：Departmental Family, Entity, Input Date, Expense Type, Expense Area, Supplier, Amount, Supplier Type

## g0067（1 列）
- 見出し：Amount
- 例1 値：137,073.15 | 32,025.00 | 39,991.61 | -39,644.77 | -30,451.00
  - 同じ表の列：Departmental Family, Entity, Input Date, Expense Type, Expense Area, Supplier, Transaction No, Supplier Type

## g0068（1 列）
- 見出し：Supplier Type
- 例1 値：SME | Large | Large | Large | Large
  - 同じ表の列：Departmental Family, Entity, Input Date, Expense Type, Expense Area, Supplier, Transaction No, Amount

## g0069（1 列）
- 見出し：Contract Number
- 例1 値：SC00001487
  - 同じ表の列：Departmental Family, Entity, Input Date, Expense Type, Expense Area, Supplier, Transaction No, Amount

## g0070（1 列）
- 見出し：Valuation Band Range
- 例1 値：」100,000 - 」299,999 | <」50,000 - 」99,999 | <」50,000 - 」99,999 | 」100,000 - 」299,999 | 」100,000 - 」299,999
  - 同じ表の列：Intervening bands, Dwellings value, Tenure Status

## g0071（1 列）
- 見出し：Intervening bands
- 例1 値：<」50,000 | 」260,000 - 」279,999 | 」200,000 - 」239,999 | 」180,000 - 」199,999 | 」220,000 - 」239,999
  - 同じ表の列：Valuation Band Range, Dwellings value, Tenure Status

## g0072（1 列）
- 見出し：Dwellings value
- 例1 値：nil | nil | 298 | 158 | 87
  - 同じ表の列：Valuation Band Range, Intervening bands, Tenure Status

## g0073（1 列）
- 見出し：Tenure Status
- 例1 値：88.89% | 100% | 100% | n/a | n/a
  - 同じ表の列：Valuation Band Range, Intervening bands, Dwellings value

## g0074（1 列）
- 見出し：Ref.
- 例1 値：16.021 | 7.008 | 22.019 | 22.026 | 12.004
  - 同じ表の列：18/19, 19/20, VAT Code

## g0075（1 列）
- 見出し：18/19
- 例1 値：50.00 | 866.00 | 801.00 | 64,000.00 | 5.50
  - 同じ表の列：Ref., 19/20, VAT Code

## g0076（1 列）
- 見出し：19/20
- 例1 値：11.00 | 1,600.00 | N/A | 640.00 | 10.50
  - 同じ表の列：Ref., 18/19, VAT Code

## g0077（1 列）
- 見出し：VAT Code
- 例1 値：NB | EX | EX | NB | NB
  - 同じ表の列：Ref., 18/19, 19/20

## g0078（1 列）
- 見出し：application_source
- 例1 値：On-line application | On-line application | On-line application | On-line application | On-line application
  - 同じ表の列：rep_status, stage_resolved, final_decision, scheme, gender, age, main_injury, rejection_or_reduct…

## g0079（1 列）
- 見出し：rep_status
- 例1 値：Not represented | Not represented | Not represented | Not represented | Not represented
  - 同じ表の列：application_source, stage_resolved, final_decision, scheme, gender, age, main_injury, rejection_or_reduct…

## g0080（1 列）
- 見出し：stage_resolved
- 例1 値：Initial application | Initial application | Initial application | Initial application | Initial application
  - 同じ表の列：application_source, rep_status, final_decision, scheme, gender, age, main_injury, rejection_or_reduct…

## g0081（1 列）
- 見出し：final_decision
- 例1 値：Nil award | Full award | Nil award | Nil award | Nil award
  - 同じ表の列：application_source, rep_status, stage_resolved, scheme, gender, age, main_injury, rejection_or_reduct…

## g0082（1 列）
- 見出し：scheme
- 例1 値：2012 Scheme | 2012 Scheme | 2012 Scheme | 2008 Scheme | 2008 Scheme
  - 同じ表の列：application_source, rep_status, stage_resolved, final_decision, gender, age, main_injury, rejection_or_reduct…

## g0083（1 列）
- 見出し：gender
- 例1 値：Male | Male | Female | Female | Male
  - 同じ表の列：application_source, rep_status, stage_resolved, final_decision, scheme, age, main_injury, rejection_or_reduct…

## g0084（1 列）
- 見出し：age
- 例1 値：18 to 40 | 18 to 40 | 18 to 40 | 0 to 17 | 41 to 64
  - 同じ表の列：application_source, rep_status, stage_resolved, final_decision, scheme, gender, main_injury, rejection_or_reduct…

## g0085（1 列）
- 見出し：main_injury
- 例1 値：NO DATA OR DATA REDACTED AS RARE | NO DATA OR DATA REDACTED AS RARE | NO DATA OR DATA REDACTED AS RARE | NO DATA OR DATA REDACTED AS RARE | NO DATA OR DATA REDACTED AS RARE
  - 同じ表の列：application_source, rep_status, stage_resolved, final_decision, scheme, gender, age, rejection_or_reduct…

## g0086（1 列）
- 見出し：rejection_or_reduction_reasons
- 例1 値：Injury does not qualify for compensation | Multiple | Multiple | Injury does not qualify for compensation | Applicants criminal record/character
  - 同じ表の列：application_source, rep_status, stage_resolved, final_decision, scheme, gender, age, main_injury

## g0087（1 列）
- 見出し：review_decision
- 例1 値：Nil award | Nil award | Nil award | Nil award | Reduced award
  - 同じ表の列：application_source, rep_status, stage_resolved, final_decision, scheme, gender, age, main_injury

## g0088（2 列）
- 見出し：Country
- 例1 値：England | England | Wales | England | England
  - 同じ表の列：GRADE, County
- 例2 値：England | England | England | England | England
  - 同じ表の列：Country Code, Region, Region Code, Second Tier Authori…, Local Authority, Local Authority Code, Calendar Year, LA CO2 Sector

## g0089（1 列）
- 見出し：GRADE
- 例1 値：Grade II* | Grade II | Grade II | Grade II* | Grade II
  - 同じ表の列：Country, County

## g0090（1 列）
- 見出し：County
- 例1 値：North Yorkshire | Wiltshire | Cambridgeshire | Hampshire | Hampshire
  - 同じ表の列：Country, GRADE

## g0091（1 列）
- 見出し：Minister
- 例1 値：Minister of State for Energy and Intell… | Minister of State for Energy and Intell… | Minister of State for Energy and Intell… | Minister of State for Energy and Intell… | Minister of State for Energy and Intell…
  - 同じ表の列：Date of Hospitality, Type of hospitality…

## g0092（1 列）
- 見出し：Type of hospitality received
- 例1 値：Dinner Reception | Dinner Reception | Dinner Reception | Dinner Reception | Dinner Reception
  - 同じ表の列：Minister, Date of Hospitality

## g0093（1 列）
- 見出し：Responsible BEIS Directorate
- 例1 値：Clean Growth | Nuclear Directorate | Communications | Nuclear Directorate | Infrastructure and Materials
  - 同じ表の列：Published?

## g0094（1 列）
- 見出し：Published?
- 例1 値：No | No | No | No | Yes
  - 同じ表の列：Responsible BEIS Di…

## g0095（1 列）
- 見出し：Department
- 例1 値：Department for Business, Energy & Indus… | Department for Business, Energy & Indus… | Department for Business, Energy & Indus… | Department for Business, Energy & Indus… | Department for Business, Energy & Indus…
  - 同じ表の列：Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount, Supplier Type

## g0096（1 列）
- 見出し：Entity
- 例1 値：Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and…
  - 同じ表の列：Department, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount, Supplier Type

## g0097（2 列）
- 見出し：Date of Payment
- 例1 値：01/03/2017 | 23/03/2017 | 06/03/2017 | 06/03/2017 | 06/03/2017
  - 同じ表の列：Department, Entity, Expense Type, Expense Area, Supplier, Transaction Number, Amount, Supplier Type
- 例2 値：05/06/2018 | 13/06/2018 | 08/06/2018 | 05/06/2018 | 05/06/2018
  - 同じ表の列：Department family, Entity, Directorate, Transaction referen…, Amount paid, Contract Number, Expenditure Type

## g0098（1 列）
- 見出し：Expense Type
- 例1 値：Other Travel | Consultancy Expenditure | Hire Of Interim Managers | Other It Consultancy | Learning And Dev - Cs Skills
  - 同じ表の列：Department, Entity, Date of Payment, Expense Area, Supplier, Transaction Number, Amount, Supplier Type

## g0099（1 列）
- 見出し：Expense Area
- 例1 値：FCS - Finance & Corporate Services - Di… | FCS - Finance & Corporate Services - Le… | FCS - Finance & Corporate Services - Co… | FCS - Finance & Corporate Services - Di… | Business and Science - Science and Rese…
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Supplier, Transaction Number, Amount, Supplier Type

## g0100（1 列）
- 見出し：Supplier
- 例1 値：FOREIGN AND COMMONWEALTH OFFICE (FCO) | Personal Expense, Name Withheld | Personal Expense, Name Withheld | Personal Expense, Name Withheld | FOREIGN AND COMMONWEALTH OFFICE (FCO)
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Transaction Number, Amount, Supplier Type

## g0101（1 列）
- 見出し：Amount
- 例1 値：33.56 | 563888.83 | 10.78 | 2895.43 | -95000.00
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Supplier Type

## g0102（1 列）
- 見出し：Supplier Type
- 例1 値：VENDOR | VENDOR | VENDOR | WGA ONLY | EMPLOYEE
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0103（1 列）
- 見出し：Minister
- 例1 値：Minister for Sport & the Olympics | Minister for Culture, Communications & … | Minister for Sport & the Olympics | Minister for Sport & the Olympics | Minister for Tourism and Heritage
  - 同じ表の列：Date, Purpose of meeting

## g0104（1 列）
- 見出し：Purpose of meeting
- 例1 値：Introductory meeting | To discuss audio description for blind … | To discuss 2012 sporting legacy | General discussion | To discuss Cultural Olympiad
  - 同じ表の列：Minister, Date

## g0105（1 列）
- 見出し：Minister
- 例1 値：Secretary of State | Minister for Culture, Communications an… | Minister for Sport and the Olympics | Minister for Tourism & Heritage
  - 同じ表の列：Date, Purpose of meeting

## g0106（1 列）
- 見出し：Purpose of meeting
- 例1 値：To discuss future strategies | Catch up | Introductory meeting | Catch up | Introductory meeting
  - 同じ表の列：Minister, Date

## g0107（2 列）
- 見出し：Main department
- 例1 値：Department for Education | Department for Education | Department for Education
  - 同じ表の列：Organisation, Delegated grades on…, SCS on standard con…, Information for SCS…, Comments
- 例2 値：Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence
  - 同じ表の列：Organisation, Delegated grades, SCS on standard con…, Information for SCS…, Comments

## g0108（1 列）
- 見出し：Organisation
- 例1 値：Office of Qualifications & Examinations… | Department for Education | Office for Standards in Education, Chil…
  - 同じ表の列：Main department, Delegated grades on…, SCS on standard con…, Information for SCS…, Comments

## g0109（1 列）
- 見出し：Delegated grades only
- 例1 値：」64,892,207 | Annual Paybill (delegated grades for fi… | 」182,600,000 | 」7,532,430
  - 同じ表の列：Main department, Organisation, SCS on standard con…, Information for SCS…, Comments

## g0110（1 列）
- 見出し：SCS on standard contracts (end of year NCPRP)
- 例1 値：」19,240,000 | 」902,820 | 」3,331,114 | Annual SCS Paybill for those SCS on sta…
  - 同じ表の列：Main department, Organisation, Delegated grades on…, Information for SCS…, Comments

## g0111（1 列）
- 見出し：Information for SCS on non-standard contracts
- 例1 値：0 | 0 | 0 | Number of SCS on non-standard contracts…
  - 同じ表の列：Main department, Organisation, Delegated grades on…, SCS on standard con…, Comments

## g0112（1 列）
- 見出し：Comments
- 例1 値：This information may vary from the mont… | We have a sizeable number of staff chan…
  - 同じ表の列：Main department, Organisation, Delegated grades on…, SCS on standard con…, Information for SCS…

## g0113（1 列）
- 見出し：Country Code
- 例1 値：E92000001 | E92000001 | E92000001 | E92000001 | E92000001
  - 同じ表の列：Country, Region, Region Code, Second Tier Authori…, Local Authority, Local Authority Code, Calendar Year, LA CO2 Sector

## g0114（1 列）
- 見出し：Region
- 例1 値：North East | North East | North East | North East | North East
  - 同じ表の列：Country, Country Code, Region Code, Second Tier Authori…, Local Authority, Local Authority Code, Calendar Year, LA CO2 Sector

## g0115（1 列）
- 見出し：Region Code
- 例1 値：E12000001 | E12000001 | E12000001 | E12000001 | E12000001
  - 同じ表の列：Country, Country Code, Region, Second Tier Authori…, Local Authority, Local Authority Code, Calendar Year, LA CO2 Sector

## g0116（1 列）
- 見出し：Second Tier Authority
- 例1 値：Redcar and Cleveland | Middlesbrough | Middlesbrough | Middlesbrough | Redcar and Cleveland
  - 同じ表の列：Country, Country Code, Region, Region Code, Local Authority, Local Authority Code, Calendar Year, LA CO2 Sector

## g0117（1 列）
- 見出し：Local Authority
- 例1 値：Middlesbrough | Redcar and Cleveland | Middlesbrough | Hartlepool | Middlesbrough
  - 同じ表の列：Country, Country Code, Region, Region Code, Second Tier Authori…, Local Authority Code, Calendar Year, LA CO2 Sector

## g0118（1 列）
- 見出し：Local Authority Code
- 例1 値：E06000002 | E06000003 | E06000003 | E06000002 | E06000001
  - 同じ表の列：Country, Country Code, Region, Region Code, Second Tier Authori…, Local Authority, Calendar Year, LA CO2 Sector

## g0119（1 列）
- 見出し：Calendar Year
- 例1 値：2011 | 2010 | 2018 | 2019 | 2007
  - 同じ表の列：Country, Country Code, Region, Region Code, Second Tier Authori…, Local Authority, Local Authority Code, LA CO2 Sector

## g0120（1 列）
- 見出し：LA CO2 Sector
- 例1 値：LULUCF | Industry | Domestic | Public Sector | LULUCF
  - 同じ表の列：Country, Country Code, Region, Region Code, Second Tier Authori…, Local Authority, Local Authority Code, Calendar Year

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
