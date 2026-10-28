# ラベル用シート 004 / 006

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_004.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0361（1 列）
- 見出し：Expense Type
- 例1 値：Legal Costs | Legal Costs | Legal Costs | Legal Costs | Legal Costs
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Transaction Number, Spend

## g0362（1 列）
- 見出し：Transaction Number
- 例1 値：H36 | H102 | H53 | H100 | H32
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Spend

## g0363（1 列）
- 見出し：Spend
- 例1 値：12,702.45 | 9,981.99 | 7,887.10 | 1,477,672.16 | 401,523.36
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number

## g0364（2 列）
- 見出し：SiteplanURL
- 例1 値：http://www.hinckley-bosworth.gov.uk/bro… | http://www.hinckley-bosworth.gov.uk/bro… | http://www.hinckley-bosworth.gov.uk/bro… | http://www.hinckley-bosworth.gov.uk/bro… | http://www.hinckley-bosworth.gov.uk/bro…
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable
- 例2 値：https://mapping.north-norfolk.gov.uk/wm… | https://mapping.north-norfolk.gov.uk/wm… | https://mapping.north-norfolk.gov.uk/wm… | https://mapping.north-norfolk.gov.uk/wm… | https://mapping.north-norfolk.gov.uk/wm…
  - 同じ表の列：OrganisationURI, SiteReference, GeoY, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0365（1 列）
- 見出し：PlanningStatus
- 例1 値：not permissioned | not permissioned | not permissioned | not permissioned | not permissioned
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares

## g0366（1 列）
- 見出し：Department family
- 例1 値：HM Revenue & Customs | HM Revenue & Customs | HM Revenue & Customs | HM Revenue & Customs | HM Revenue & Customs
  - 同じ表の列：Entity, Date, Supplier, Amount

## g0367（1 列）
- 見出し：Entity
- 例1 値：HM Revenue & Customs | HM Revenue & Customs | HM Revenue & Customs | HM Revenue & Customs | HM Revenue & Customs
  - 同じ表の列：Department family, Date, Supplier, Amount

## g0368（1 列）
- 見出し：Supplier
- 例1 値：AMERICAN AIRLINES | AMERICAN AIRLINES | AMERICAN AIRLINES | AMERICAN AIRLINES | AMERICAN AIRLINES
  - 同じ表の列：Department family, Entity, Date, Amount

## g0369（1 列）
- 見出し：Amount
- 例1 値：2,632.63 | 2,632.63 | 884 | 884 | 2,632.63
  - 同じ表の列：Department family, Entity, Date, Supplier

## g0370（1 列）
- 見出し：Date of meeting with HMRC
- 例1 値：25/05/2012 | 27/04/2012 | 25/05/2012 | 25/05/2012 | 25/05/2012
  - 同じ表の列：Organisation, Issues discussed

## g0371（1 列）
- 見出し：Organisation
- 例1 値：Imperial Tobacco | Philip Morris International | Japan Tobacco International | British American Tobacco | Tobacco Manufacturers’ Association
  - 同じ表の列：Date of meeting wit…, Issues discussed

## g0372（1 列）
- 見出し：Issues discussed
- 例1 値：Anti-Illicit Joint Working Group | Anti-Illicit Joint Working Group | Anti-Illicit Joint Working Group | Anti-Illicit Joint Working Group | Composition of the Illicit market
  - 同じ表の列：Date of meeting wit…, Organisation

## g0373（1 列）
- 見出し：Transaction date
- 例1 値：19/04/2011 00:00 | 05/04/2011 00:00 | 27/04/2011 00:00 | 21/04/2011 00:00 | 05/04/2011 00:00
  - 同じ表の列：Transaction amount, Entity, Details

## g0374（1 列）
- 見出し：Transaction amount
- 例1 値：1,000.00 | 1,089.90 | 1,380.00 | 600 | 760.33
  - 同じ表の列：Transaction date, Entity, Details

## g0375（2 列）
- 見出し：Entity
- 例1 値：HM Treasury | HM Treasury | DMO | HM Treasury | DMO
  - 同じ表の列：Transaction date, Transaction amount, Details
- 例2 値：HM Treasury | HM Treasury | HM Treasury | HM Treasury | DMO
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0376（1 列）
- 見出し：Details
- 例1 値：Air Travel | Training Course Fees | Air Travel | Training Course Fees | Corporate subs and other Info services
  - 同じ表の列：Transaction date, Transaction amount, Entity

## g0377（1 列）
- 見出し：Expense Type
- 例1 値：AME Mint Stock Metal Costs | Service Charges | Software Licences | Consultants - Financial - Advisory only | Facilities Mgt. Service Charges(Contrac…
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Transaction Number, Amount

## g0378（1 列）
- 見出し：Supplier
- 例1 値：PARTNERSHIPS UK PLC | GOVERNMENT ACTUARY'S DEPT | DEUTSCHE BANK AG LONDON | DTZ | EXCHEQUER PARTNERSHIP PLC
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount

## g0379（1 列）
- 見出し：Date of hospitality
- 例1 値：June, 2010 | July, 2010 | July, 2010 | [2] Hospitality does not normally inclu… | June, 2010
  - 同じ表の列：Type of hospitality…

## g0380（1 列）
- 見出し：FOOTBALL BANNING ORDERS BY CLUB SUPPORTED
- 例1 値：Aston Villa | Everton | Manchester City | Birmingham City | Blackpool
  - 同じ表の列：TABLE 1

## g0381（1 列）
- 見出し：TABLE 1
- 例1 値：Bangor City | Wrexham | Mansfield Town | Luton Town | York City
  - 同じ表の列：FOOTBALL BANNING OR…

## g0382（1 列）
- 見出し：SPENDING
- 例1 値：Upto top 5 contributory elements | Working Capital Forecast [% variance of… | Total Annually Managed Expenditure (AME) | Accuracy of Cash Forecasting ( +/-, %) | Purchase of goods and services within R…
  - 同じ表の列：PEOPLE

## g0383（1 列）
- 見出し：PEOPLE
- 例1 値：Workforce Diversity [Senior Civil Serva… | Theme scores (%) | Average Staff Costs (」) (current = at 3… | Payroll Staff [Total full-time equivale… | Contingent Labour [Total full-time equi…
  - 同じ表の列：SPENDING

## g0384（1 列）
- 見出し：Department family
- 例1 値：Department for Business Energy and Indu… | Department for Business Energy and Indu… | Department for Business Energy and Indu… | Department for Business Energy and Indu… | Department for Business Energy and Indu…
  - 同じ表の列：Entity, Date, Expense type, Expense area, Supplier, Amount, VAT registration nu…

## g0385（1 列）
- 見出し：Expense type
- 例1 値：Travel & Subsistence | Steering Board | Supporting UK Business | Pay Costs | Marketing & Publicity
  - 同じ表の列：Department family, Entity, Date, Expense area, Supplier, Amount, VAT registration nu…

## g0386（1 列）
- 見出し：Expense area
- 例1 値：People Places & Serv Directorate | People Places & Serv Directorate | People Places & Serv Directorate | People Places & Serv Directorate | IT Directorate
  - 同じ表の列：Department family, Entity, Date, Expense type, Supplier, Amount, VAT registration nu…

## g0387（2 列）
- 見出し：Supplier
- 例1 値：Viking | Alexander Mann Solutions Limited | The Intellectual Property | Alexander Mann Solutions Limited | Senator International Ltd
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Amount, VAT registration nu…
- 例2 値：Civil Aviation Authority | Civil Aviation Authority | CREDO | BYTES TECHNOLOGY GROUP | CAPITA SECURE INFORMATION SYSTEMS
  - 同じ表の列：Department family, Entity, Date of payment, Expense Code, Expense type, Cost Centre, Expense area, Transaction Number

## g0388（1 列）
- 見出し：VAT registration number
- 例1 値：Not Applicable | Not Applicable | Not Applicable | Not Applicable | Not Applicable
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Supplier, Amount

## g0389（1 列）
- 見出し：Running
- 例1 値：」 000 | 」494 | Expenses | 」1,828 | (2)
  - 同じ表の列：Total, Sales, Fees, Other, Total_2, Net Current

## g0390（1 列）
- 見出し：Total
- 例1 値：Expenditure | (3) = (1) + (2) | 」 000 | 」2,552 | 」630
  - 同じ表の列：Running, Sales, Fees, Other, Total_2, Net Current

## g0391（1 列）
- 見出し：Sales, Fees
- 例1 値：302 | 」43 | 」361 | 」361 | 」 000
  - 同じ表の列：Running, Total, Other, Total_2, Net Current

## g0392（1 列）
- 見出し：Other
- 例1 値：Income | 」1,169 | 」 000 | (5)
  - 同じ表の列：Running, Total, Sales, Fees, Total_2, Net Current

## g0393（1 列）
- 見出し：Total_2
- 例1 値：Income | (6) = (4) + (5) | 」361 | 」 000 | 」2,271
  - 同じ表の列：Running, Total, Sales, Fees, Other, Net Current

## g0394（1 列）
- 見出し：Net Current
- 例1 値：」281 | 」 000 | 」269 | Expenditure | (7) = (3) - (6)
  - 同じ表の列：Running, Total, Sales, Fees, Other, Total_2

## g0395（1 列）
- 見出し：Dataset_Title
- 例1 値：HMLR: Legal Charges | HMLR: Exempt Information Documents | HMLR: INSPIRE Index Polygons spatial da… | HMLR: Mines and Minerals | HMLR: Rentcharges
  - 同じ表の列：Organisation, Abstract, Inspire_Theme, Inspire_Feature_Type, Other_Related_Themes, Constraints, Metadata_published_…, Data_Published

## g0396（1 列）
- 見出し：Abstract
- 例1 値：HM Land Registry’s Index Map data conta… | HM Land Registry’s Price Paid Register … | HM Land Registry’s Restrictions data co… | HM Land Registry’s Equitable Charges da… | HM Land Registry’s UK Companies data co…
  - 同じ表の列：Organisation, Dataset_Title, Inspire_Theme, Inspire_Feature_Type, Other_Related_Themes, Constraints, Metadata_published_…, Data_Published

## g0397（1 列）
- 見出し：Inspire_Theme
- 例1 値：Cadastral Parcel | Cadastral Parcel | Cadastral Parcel | Cadastral Parcel | Cadastral Parcel
  - 同じ表の列：Organisation, Dataset_Title, Abstract, Inspire_Feature_Type, Other_Related_Themes, Constraints, Metadata_published_…, Data_Published

## g0398（1 列）
- 見出し：Inspire_Feature_Type
- 例1 値：Cadastral Parcel | Cadastral Parcel | Cadastral Parcel | Cadastral Parcel | Cadastral Parcel
  - 同じ表の列：Organisation, Dataset_Title, Abstract, Inspire_Theme, Other_Related_Themes, Constraints, Metadata_published_…, Data_Published

## g0399（1 列）
- 見出し：Other_Related_Themes
- 例1 値：Title Register;Protecting interest in l… | Administrative area;County;Metropolitan… | Survey metadata;Electronic land or prop… | Survey metadata;Survey features | Title Register;Leasehold;Date of lease;…
  - 同じ表の列：Organisation, Dataset_Title, Abstract, Inspire_Theme, Inspire_Feature_Type, Constraints, Metadata_published_…, Data_Published

## g0400（1 列）
- 見出し：Constraints
- 例1 値：Currently only available in copy regist… | Available on a per title basis | Currently only available in copy regist… | Available under licence; Third party In… | Only available in copy registers on a p…
  - 同じ表の列：Organisation, Dataset_Title, Abstract, Inspire_Theme, Inspire_Feature_Type, Other_Related_Themes, Metadata_published_…, Data_Published

## g0401（2 列）
- 見出し：Metadata_published_on_datagovuk
- 例1 値：Unpublished | Unpublished | Unpublished | Unpublished | Published
  - 同じ表の列：Organisation, Dataset_Title, Abstract, Inspire_Theme, Inspire_Feature_Type, Other_Related_Themes, Constraints, Data_Published
- 例2 値：Unpublished | Unpublished | Unpublished | Unpublished | Unpublished
  - 同じ表の列：Organisation, Dataset_Title, Abstract, INSPIRE_Theme, INSPIRE_Feature_Type, Other_Related_Themes, Constraints, Where_To_Find_More_…

## g0402（1 列）
- 見出し：Data_Published
- 例1 値：Published | Unpublished – This dataset is under con… | Unpublished – This dataset is under con… | Published | Unpublished – This dataset is under con…
  - 同じ表の列：Organisation, Dataset_Title, Abstract, Inspire_Theme, Inspire_Feature_Type, Other_Related_Themes, Constraints, Metadata_published_…

## g0403（1 列）
- 見出し：Where_To_Find_More_Information
- 例1 値：https://www.gov.uk/government/publicati… | https://use-land-property-data.service.… | https://www.gov.uk/make-a-freedom-of-in… | https://use-land-property-data.service.… | https://use-land-property-data.service.…
  - 同じ表の列：Organisation, Dataset_Title, Abstract, Inspire_Theme, Inspire_Feature_Type, Other_Related_Themes, Constraints, Metadata_published_…

## g0404（1 列）
- 見出し：Site Code
- 例1 値：CD1 | BL0 | IM1 | BL0 | CD1
  - 同じ表の列：Site Type, Bulletin Date, Bulletin Date Forma…, NO2 Air Quality Band, NO2 Air Quality Ind…, Latest Capture, Latest Week, Ward Code

## g0405（1 列）
- 見出し：Site Type
- 例1 値：Kerbside | Kerbside | Kerbside | Kerbside | Urban Background
  - 同じ表の列：Site Code, Bulletin Date, Bulletin Date Forma…, NO2 Air Quality Band, NO2 Air Quality Ind…, Latest Capture, Latest Week, Ward Code

## g0406（1 列）
- 見出し：Bulletin Date
- 例1 値：19/12/2021 12:00:00 AM | 10/05/2022 06:00:00 AM | 24/04/2022 08:00:00 PM | 26/06/2022 03:00:00 PM | 23/04/2022 10:00:00 AM
  - 同じ表の列：Site Code, Site Type, Bulletin Date Forma…, NO2 Air Quality Band, NO2 Air Quality Ind…, Latest Capture, Latest Week, Ward Code

## g0407（1 列）
- 見出し：Bulletin Date Formatted
- 例1 値：Day 252 10:00 | Day 065 15:00 | Day 114 21:00 | Day 064 02:00 | Day 352 07:00
  - 同じ表の列：Site Code, Site Type, Bulletin Date, NO2 Air Quality Band, NO2 Air Quality Ind…, Latest Capture, Latest Week, Ward Code

## g0408（1 列）
- 見出し：NO2 Air Quality Band
- 例1 値：Low | Low | Low | No data | No data
  - 同じ表の列：Site Code, Site Type, Bulletin Date, Bulletin Date Forma…, NO2 Air Quality Ind…, Latest Capture, Latest Week, Ward Code

## g0409（1 列）
- 見出し：NO2 Air Quality Index
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Site Code, Site Type, Bulletin Date, Bulletin Date Forma…, NO2 Air Quality Band, Latest Capture, Latest Week, Ward Code

## g0410（1 列）
- 見出し：Latest Capture
- 例1 値：No | No | No | No | No
  - 同じ表の列：Site Code, Site Type, Bulletin Date, Bulletin Date Forma…, NO2 Air Quality Band, NO2 Air Quality Ind…, Latest Week, Ward Code

## g0411（1 列）
- 見出し：Latest Week
- 例1 値：No | No | No | No | No
  - 同じ表の列：Site Code, Site Type, Bulletin Date, Bulletin Date Forma…, NO2 Air Quality Band, NO2 Air Quality Ind…, Latest Capture, Ward Code

## g0412（2 列）
- 見出し：Ward Code
- 例1 値：E05000129 | E05013653 | E05000133 | E05000129 | E05000133
  - 同じ表の列：Site Code, Site Type, Bulletin Date, Bulletin Date Forma…, NO2 Air Quality Band, NO2 Air Quality Ind…, Latest Capture, Latest Week
- 例2 値：E05013669 | E05013658 | E05013662 | E05013653 | E05013662
  - 同じ表の列：Building Number, Unit Count, Responsible Authori…, Easting, Northing, Spatial Accuracy, Location, Organisation URI

## g0413（1 列）
- 見出し：Building Number
- 例1 値：250 | 43-45 | 32 | 96 | 236
  - 同じ表の列：Unit Count, Responsible Authori…, Ward Code, Easting, Northing, Spatial Accuracy, Location, Organisation URI

## g0414（1 列）
- 見出し：Unit Count
- 例1 値：8 | 2 | 1 | 1 | 2
  - 同じ表の列：Building Number, Responsible Authori…, Ward Code, Easting, Northing, Spatial Accuracy, Location, Organisation URI

## g0415（1 列）
- 見出し：Responsible Authority
- 例1 値：HSE Enforced Premises | Local Authority Enforced Premises | Local Authority Enforced Premises | Local Authority Enforced Premises | Local Authority Enforced Premises
  - 同じ表の列：Building Number, Unit Count, Ward Code, Easting, Northing, Spatial Accuracy, Location, Organisation URI

## g0416（1 列）
- 見出し：Spatial Accuracy
- 例1 値：Property Level | Property Level | Unknown | Property Level | Property Level
  - 同じ表の列：Building Number, Unit Count, Responsible Authori…, Ward Code, Easting, Northing, Location, Organisation URI

## g0417（1 列）
- 見出し：Location
- 例1 値：POINT (-0.117291 51.518654) | POINT (-0.165298 51.553227) | POINT (-0.114978 51.524067) | POINT (-0.137369 51.525737) | POINT (-0.127685 51.539)
  - 同じ表の列：Building Number, Unit Count, Responsible Authori…, Ward Code, Easting, Northing, Spatial Accuracy, Organisation URI

## g0418（1 列）
- 見出し：Organisation URI
- 例1 値：http://opendatacommunities.org/id/londo… | http://opendatacommunities.org/id/londo… | http://opendatacommunities.org/id/londo… | http://opendatacommunities.org/id/londo… | http://opendatacommunities.org/id/londo…
  - 同じ表の列：Building Number, Unit Count, Responsible Authori…, Ward Code, Easting, Northing, Spatial Accuracy, Location

## g0419（1 列）
- 見出し：SiteReference
- 例1 値：SOU6f | SOU6c | 164869FUL | EAL11 | EAL15
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0420（1 列）
- 見出し：{'gtm.start': new Date().getTime()
- 例1 値：Sundry debts | <a href="/myservices/benefits/housing-b… | Parking reports and policies | </a> | </div>
  - 同じ表の列：event:'gtm.js'}

## g0421（1 列）
- 見出し：event:'gtm.js'}
- 例1 値：dl=l!='dataLayer'?'&l='+l:'';j.async=tr… | document | refunds and appeals | people with a disability and people wit… | registration.scope);
  - 同じ表の列：{'gtm.start': new D…

## g0422（1 列）
- 見出し：{'gtm.start': new Date().getTime()
- 例1 値：<a href="/myservices/environment/commer… | Housing | <a href="/myservices/planning/unauthori… | What is council tax and who has to pay? | <a href="/myservices/housing/council-te…
  - 同じ表の列：event:'gtm.js'}

## g0423（1 列）
- 見出し：event:'gtm.js'}
- 例1 値：f); | deaths | deaths | people with a disability and people wit… | which lists previously developed sites …
  - 同じ表の列：{'gtm.start': new D…

## g0424（1 列）
- 見出し：{'gtm.start': new Date().getTime()
- 例1 値：<a href="/myservices/education" class="… | </a> | <a href="/myservices/socialcare/adult" … | </a> | <!-- start item-->
  - 同じ表の列：event:'gtm.js'}

## g0425（1 列）
- 見出し：event:'gtm.js'}
- 例1 値：f); | hygiene and standards | training and advice | fines and regulations | allotments and community gardening
  - 同じ表の列：{'gtm.start': new D…

## g0426（1 列）
- 見出し：WKT
- 例1 値：MULTIPOLYGON (((538133.168003774 194174… | MULTIPOLYGON (((537181.33256196 192747.… | MULTIPOLYGON (((537495.929193035 187486… | MULTIPOLYGON (((539214.276045614 186274… | MULTIPOLYGON (((536027.792868696 189760…
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, PlanningStatus, PermissionType

## g0427（1 列）
- 見出し：SiteReference
- 例1 値：SA13 | BLR_046 | BLR_156 | 230208 | 212178
  - 同じ表の列：WKT, OrganisationURI, SiteplanURL, GeoY, GeoX, Hectares, PlanningStatus, PermissionType

## g0428（1 列）
- 見出し：GeoX
- 例1 値：538957 | 539524 | 537706.7841 | 538936 | 539379
  - 同じ表の列：WKT, OrganisationURI, SiteReference, SiteplanURL, GeoY, Hectares, PlanningStatus, PermissionType

## g0429（1 列）
- 見出し：Expense type
- 例1 値：Solicitors | Passport/Visa | Computing Operation Costs | Solicitors | Overseas Hotel/Accommodation
  - 同じ表の列：Department family, Entity, Date, Expense area, Supplier, Transaction number, Amount, VAT registration nu…

## g0430（1 列）
- 見出し：Expense area
- 例1 値：Inspection, Enforcement & Standards | Licensing | Vigilance and Risk Management of Medici… | Vigilance and Risk Management of Medici… | Facilities & Estates
  - 同じ表の列：Department family, Entity, Date, Expense type, Supplier, Transaction number, Amount, VAT registration nu…

## g0431（1 列）
- 見出し：VAT registration number
- 例1 値：862247715 | 413640679 | 788629066 | 107831677 | 862247715
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Supplier, Transaction number, Amount

## g0432（1 列）
- 見出し：Amount
- 例1 値：£851.17 | £855.00 | £860.00 | £849.98 | £2,480.00
  - 同じ表の列：Date, Type

## g0433（1 列）
- 見出し：Type
- 例1 値：Equipment | Equipment | Equipment | Travel and subsistence | Print and publishing
  - 同じ表の列：Date, Amount

## g0434（1 列）
- 見出し：OrganisationURL
- 例1 値：http://opendatacommunities.org/id/unita… | http://opendatacommunities.org/id/unita… | http://opendatacommunities.org/id/unita… | http://opendatacommunities.org/id/unita… | http://opendatacommunities.org/id/unita…
  - 同じ表の列：SiteReference, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0435（1 列）
- 見出し：PlanningHistory
- 例1 値：https://tvcaplanning.co.uk/online-appli… | https://tvcaplanning.co.uk/online-appli… | https://planning.agileapplications.co.u… | https://planning.agileapplications.co.u… | https://planning.agileapplications.co.u…
  - 同じ表の列：OrganisationURL, SiteReference, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus, PermissionType

## g0436（1 列）
- 見出し：Organisation
- 例1 値：Coal Authority | Coal Authority | Coal Authority | Coal Authority | Coal Authority
  - 同じ表の列：Dataset_Title, Abstract, INSPIRE_Theme, INSPIRE_Feature_Type, Other_Related_Themes, Constraints, Metadata_published_…, Where_To_Find_More_…

## g0437（1 列）
- 見出し：Dataset_Title
- 例1 値：Coal Authority Legal Notices | Shallow Coal Mine Workings | Coal Mining Surface Hazards Area | Coal Extraction Licence Table | Coal Mine Gas Site
  - 同じ表の列：Organisation, Abstract, INSPIRE_Theme, INSPIRE_Feature_Type, Other_Related_Themes, Constraints, Metadata_published_…, Where_To_Find_More_…

## g0438（1 列）
- 見出し：Abstract
- 例1 値：Locations of the entrance points to ove… | The Development Low Risk Area is the pa… | Locations where environmental data is c… | Copies of many of the documents created… | Sites that have either been subject to …
  - 同じ表の列：Organisation, Dataset_Title, INSPIRE_Theme, INSPIRE_Feature_Type, Other_Related_Themes, Constraints, Metadata_published_…, Where_To_Find_More_…

## g0439（1 列）
- 見出し：INSPIRE_Theme
- 例1 値：Geology | Energy Resources | Energy Resources | No Applicable Theme | Energy Resources
  - 同じ表の列：Organisation, Dataset_Title, Abstract, INSPIRE_Feature_Type, Other_Related_Themes, Constraints, Metadata_published_…, Where_To_Find_More_…

## g0440（1 列）
- 見出し：INSPIRE_Feature_Type
- 例1 値：No Applicable Theme | No Applicable Theme | VectorEnergyResource | Geologic Feature | EnvironmentalMonitoringActivity
  - 同じ表の列：Organisation, Dataset_Title, Abstract, INSPIRE_Theme, Other_Related_Themes, Constraints, Metadata_published_…, Where_To_Find_More_…

## g0441（1 列）
- 見出し：Other_Related_Themes
- 例1 値：Operational metadata | Operational metadata | Operational metadata | Coal mining infrastructure | Operational metadata
  - 同じ表の列：Organisation, Dataset_Title, Abstract, INSPIRE_Theme, INSPIRE_Feature_Type, Constraints, Metadata_published_…, Where_To_Find_More_…

## g0442（1 列）
- 見出し：Constraints
- 例1 値：Available under Open Government Licence… | Available to view under Environmental I… | Available to view under Environmental I… | Available under Open Government Licence… | This dataset is held in relation to the…
  - 同じ表の列：Organisation, Dataset_Title, Abstract, INSPIRE_Theme, INSPIRE_Feature_Type, Other_Related_Themes, Metadata_published_…, Where_To_Find_More_…

## g0443（1 列）
- 見出し：Where_To_Find_More_Information
- 例1 値：This dataset has not been formally appr… | This dataset has been formally approved… | This dataset is available to view under… | This dataset has been formally approved… | This dataset has been formally approved…
  - 同じ表の列：Organisation, Dataset_Title, Abstract, INSPIRE_Theme, INSPIRE_Feature_Type, Other_Related_Themes, Constraints, Metadata_published_…

## g0444（1 列）
- 見出し：3D Evolution Ltd
- 例1 値：Ansell Jones Marine Services Ltd | Enersys Ltd | Clydeport Operations Ltd | Covrad Heat Transfer Ltd | ESL Defence Ltd
  - 同じ表の列：Fly BN Ltd, Phoenix Strategic L…

## g0445（1 列）
- 見出し：Fly BN Ltd
- 例1 値：Kent Engineering Services Ltd | Hellermanntyton Ltd | Meridian Aviation UK Ltd | Nyk Logistics (Deutschland) Gmbh | Glenair UK Ltd
  - 同じ表の列：3D Evolution Ltd, Phoenix Strategic L…

## g0446（1 列）
- 見出し：Phoenix Strategic Ltd
- 例1 値：Sensor Technology Systems Inc | WPDS Software Ltd | Red Orange LLC | Tiflex Ltd | Quo Imus Ltd
  - 同じ表の列：3D Evolution Ltd, Fly BN Ltd

## g0447（1 列）
- 見出し：Organisation Type
- 例1 値：Ministerial Department | OTHER | Ministerial Department | Executive Agency | Executive Agency
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0448（1 列）
- 見出し：Non-payroll Staff Agency staff (clerical/admin) Headcount
- 例1 値：1 | 56.72522661 | 0 | 4 | 40
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

## g0449（1 列）
- 見出し：Type of Hospitality received
- 例1 値：NIL Return | NIL Return | NIL Return | NIL Return | NIL Return
  - 同じ表の列：Date

## g0450（1 列）
- 見出し：DATE
- 例1 値：21-May-10 | 24-May-10 | 12-May-10 | 24-May-10 | 12-May-10
  - 同じ表の列：DEPARTMENT FAMILY, ENTITY, EXPENSE_AREA, EXPENSE_TYPE, TRANSACTION_NUMBER, AMOUNT

## g0451（1 列）
- 見出し：EXPENSE_AREA
- 例1 値：BZ999-London Region | BZ999-London Region | BZ999-London Region | ZZ900-MoJ HQ | BZ999-London Region
  - 同じ表の列：DEPARTMENT FAMILY, ENTITY, DATE, EXPENSE_TYPE, TRANSACTION_NUMBER, AMOUNT

## g0452（1 列）
- 見出し：EXPENSE_TYPE
- 例1 値：610400-Debtors <1 year - Prepayments & … | 610400-Debtors <1 year - Prepayments & … | 222002-Other Property Costs | 265000-IT & Telecommunications | 532000-Tangible GBV - Additions
  - 同じ表の列：DEPARTMENT FAMILY, ENTITY, DATE, EXPENSE_AREA, TRANSACTION_NUMBER, AMOUNT

## g0453（1 列）
- 見出し：TRANSACTION_NUMBER
- 例1 値：1020686 | 1227915 | 1020331 | 1220909 | 1218570
  - 同じ表の列：DEPARTMENT FAMILY, ENTITY, DATE, EXPENSE_AREA, EXPENSE_TYPE, AMOUNT

## g0454（1 列）
- 見出し：AMOUNT
- 例1 値：」41,125.00 | 」30,687.01 | 」173,048.19 | 」92,934.33 | 」143,665.00
  - 同じ表の列：DEPARTMENT FAMILY, ENTITY, DATE, EXPENSE_AREA, EXPENSE_TYPE, TRANSACTION_NUMBER

## g0455（1 列）
- 見出し：Week commencing
- 例1 値：2026-09-14 | 2026-01-05 | 2025-12-08 | 2025-12-15 | 2026-07-06
  - 同じ表の列：Transactions – onli…, Completion rate, User satisfaction, Very dissatisfied, Dissatisfied, Neither satisfied o…, Satisfied, Very satisfied

## g0456（1 列）
- 見出し：Transactions – online
- 例1 値：39888 | 41208 | 38618 | 40755 | 42612
  - 同じ表の列：Week commencing, Completion rate, User satisfaction, Very dissatisfied, Dissatisfied, Neither satisfied o…, Satisfied, Very satisfied

## g0457（1 列）
- 見出し：Completion rate
- 例1 値：84% | 87% | 87% | 87% | 88%
  - 同じ表の列：Week commencing, Transactions – onli…, User satisfaction, Very dissatisfied, Dissatisfied, Neither satisfied o…, Satisfied, Very satisfied

## g0458（1 列）
- 見出し：User satisfaction
- 例1 値：98% | 98% | 98% | 96% | 97%
  - 同じ表の列：Week commencing, Transactions – onli…, Completion rate, Very dissatisfied, Dissatisfied, Neither satisfied o…, Satisfied, Very satisfied

## g0459（1 列）
- 見出し：Very dissatisfied
- 例1 値：5 | 5 | 2 | 4 | 6
  - 同じ表の列：Week commencing, Transactions – onli…, Completion rate, User satisfaction, Dissatisfied, Neither satisfied o…, Satisfied, Very satisfied

## g0460（1 列）
- 見出し：Dissatisfied
- 例1 値：3 | 2 | 2 | 6 | 1
  - 同じ表の列：Week commencing, Transactions – onli…, Completion rate, User satisfaction, Very dissatisfied, Neither satisfied o…, Satisfied, Very satisfied

## g0461（1 列）
- 見出し：Neither satisfied or dissatisfied
- 例1 値：3 | 8 | 3 | 8 | 9
  - 同じ表の列：Week commencing, Transactions – onli…, Completion rate, User satisfaction, Very dissatisfied, Dissatisfied, Satisfied, Very satisfied

## g0462（1 列）
- 見出し：Satisfied
- 例1 値：49 | 49 | 49 | 45 | 33
  - 同じ表の列：Week commencing, Transactions – onli…, Completion rate, User satisfaction, Very dissatisfied, Dissatisfied, Neither satisfied o…, Very satisfied

## g0463（1 列）
- 見出し：Very satisfied
- 例1 値：326 | 455 | 365 | 360 | 405
  - 同じ表の列：Week commencing, Transactions – onli…, Completion rate, User satisfaction, Very dissatisfied, Dissatisfied, Neither satisfied o…, Satisfied

## g0464（1 列）
- 見出し：Serious Fraud Office
- 例1 値：Serious Fraud Office | Serious Fraud Office | Serious Fraud Office | Serious Fraud Office | Serious Fraud Office
  - 同じ表の列：National Fraud Auth…, 27/05/2010, Professional Fees, Engagement, Broadcasting Suppor…, 884, 45,541.41, 38,758.65

## g0465（1 列）
- 見出し：National Fraud Authority
- 例1 値：National Fraud Authority | National Fraud Authority | National Fraud Authority | National Fraud Authority | National Fraud Authority
  - 同じ表の列：Serious Fraud Office, 27/05/2010, Professional Fees, Engagement, Broadcasting Suppor…, 884, 45,541.41, 38,758.65

## g0466（1 列）
- 見出し：27/05/2010
- 例1 値：10/06/2010 | 30/03/2011 | 30/09/2010 | 17/08/2010 | 30/09/2010
  - 同じ表の列：Serious Fraud Office, National Fraud Auth…, Professional Fees, Engagement, Broadcasting Suppor…, 884, 45,541.41, 38,758.65

## g0467（1 列）
- 見出し：Professional Fees
- 例1 値：Professional Fees | Professional Fees | Professional Fees | Professional Fees | Professional Fees
  - 同じ表の列：Serious Fraud Office, National Fraud Auth…, 27/05/2010, Engagement, Broadcasting Suppor…, 884, 45,541.41, 38,758.65

## g0468（1 列）
- 見出し：Engagement
- 例1 値：Engagement | Engagement | Engagement | Programme Delivery | Human Resources
  - 同じ表の列：Serious Fraud Office, National Fraud Auth…, 27/05/2010, Professional Fees, Broadcasting Suppor…, 884, 45,541.41, 38,758.65

## g0469（1 列）
- 見出し：Broadcasting Support Services
- 例1 値：Broadcasting Support Services | Broadcasting Support Services | Broadcasting Support Services | Cabinet Office | Broadcasting Support Services
  - 同じ表の列：Serious Fraud Office, National Fraud Auth…, 27/05/2010, Professional Fees, Engagement, 884, 45,541.41, 38,758.65

## g0470（1 列）
- 見出し：884
- 例1 値：1277 | 1130 | 1214 | 940 | 1046
  - 同じ表の列：Serious Fraud Office, National Fraud Auth…, 27/05/2010, Professional Fees, Engagement, Broadcasting Suppor…, 45,541.41, 38,758.65

## g0471（1 列）
- 見出し：45,541.41
- 例1 値：45,710.32 | 31,537.00 | 64,248.00 | 27,522.19 | 45,916.30
  - 同じ表の列：Serious Fraud Office, National Fraud Auth…, 27/05/2010, Professional Fees, Engagement, Broadcasting Suppor…, 884, 38,758.65

## g0472（1 列）
- 見出し：38,758.65
- 例1 値：36,040.02 | 26,429.16 | 64,248.00 | 27,522.19 | Nil
  - 同じ表の列：Serious Fraud Office, National Fraud Auth…, 27/05/2010, Professional Fees, Engagement, Broadcasting Suppor…, 884, 45,541.41

## g0473（1 列）
- 見出し：Entity
- 例1 値：Wiltshire Probation | Lancashire Probation Trust | Norfolk & Suffolk Probation Trust | Surrey and Sussex Probation Trust | London Probation Trust
  - 同じ表の列：Department family, Date, Expense type, Expense area, Supplier, Transaction number, Amount

## g0474（1 列）
- 見出し：Expense type
- 例1 値：YOT - Cash Contribution (2010/11) | Employee/Employer Contributions | Youth Offending Team | Agency - Double waking cover | TELEPHONE CHARGES
  - 同じ表の列：Department family, Entity, Date, Expense area, Supplier, Transaction number, Amount

## g0475（1 列）
- 見出し：Expense area
- 例1 値：All Staff | Achieve - ESF Project | Achieve - ESF Project | North Wales Area | Approved Premises
  - 同じ表の列：Department family, Entity, Date, Expense type, Supplier, Transaction number, Amount

## g0476（1 列）
- 見出し：Supplier
- 例1 値：Lancashire County Council | Worcestershire County Council | East Sussex County Council | East Sussex County Council | O2 UK Ltd
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Transaction number, Amount

## g0477（1 列）
- 見出し：PlanningHistory
- 例1 値：https://idoxpa.north-norfolk.gov.uk/onl… | https://idoxpa.north-norfolk.gov.uk/onl… | https://idoxpa.north-norfolk.gov.uk/onl… | https://idoxpa.north-norfolk.gov.uk/onl… | https://idoxpa.north-norfolk.gov.uk/onl…
  - 同じ表の列：OrganisationURI, SiteReference, GeoY, GeoX, SiteplanURL, Hectares, PlanningStatus, PermissionType

## g0478（1 列）
- 見出し：SiteReference
- 例1 値：9096 | 6992 | 9729 | 3500x | 2187
  - 同じ表の列：OrganisationURI, SiteplanURL, GeoX, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0479（1 列）
- 見出し：SiteplanURL
- 例1 値：https://experience.arcgis.com/experienc… | https://experience.arcgis.com/experienc… | https://experience.arcgis.com/experienc… | https://experience.arcgis.com/experienc… | https://experience.arcgis.com/experienc…
  - 同じ表の列：OrganisationURI, SiteReference, GeoX, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0480（1 列）
- 見出し：Department
- 例1 値：Department of Education | Department of Education | Department of Education | Department of Education | Department of Education
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Transaction No, Amount, Expenditure Type

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
