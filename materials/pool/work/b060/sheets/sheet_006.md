# ラベル用シート 006 / 006

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_006.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0601（1 列）
- 見出し：Question
- 例1 値：Q1 | Q10 | Q10 | Q1 | Q10
  - 同じ表の列：UKPRN, UPIN, Age_Band, Survey_Type, Score, OrgLowest, OrgMiddle, OrgHighest

## g0602（1 列）
- 見出し：Score
- 例1 値：70.5 | 79.2 | 9.4 | - | 74.6
  - 同じ表の列：UKPRN, UPIN, Age_Band, Survey_Type, Question, OrgLowest, OrgMiddle, OrgHighest

## g0603（1 列）
- 見出し：OrgLowest
- 例1 値：41.8 | - | 31.5 | - | 64.6
  - 同じ表の列：UKPRN, UPIN, Age_Band, Survey_Type, Question, Score, OrgMiddle, OrgHighest

## g0604（1 列）
- 見出し：OrgMiddle
- 例1 値：- | 88.3 | 88.3 | 92.1 | 78.3
  - 同じ表の列：UKPRN, UPIN, Age_Band, Survey_Type, Question, Score, OrgLowest, OrgHighest

## g0605（1 列）
- 見出し：OrgHighest
- 例1 値：93.2 | - | - | 93.2 | 93.2
  - 同じ表の列：UKPRN, UPIN, Age_Band, Survey_Type, Question, Score, OrgLowest, OrgMiddle

## g0606（1 列）
- 見出し：AllLowest
- 例1 値：- | 0.0 | - | 51.3 | 0.0
  - 同じ表の列：UKPRN, UPIN, Age_Band, Survey_Type, Question, Score, OrgLowest, OrgMiddle

## g0607（1 列）
- 見出し：PaymentDate
- 例1 値：09/12/2014 | 17/09/2014 | 13/10/2014 | 12/10/2014 | 22/08/2014
  - 同じ表の列：OrganisationURI, EffectiveDate, Directorate/Service…, ServiceCategoryLabel, ServiceCategoryURI, Supplier, NetAmount, IrrecoverableVAT

## g0608（1 列）
- 見出し：Directorate/ServiceWhereExpenditureIncurred
- 例1 値：Customer Services | Coronation Hall | Town View Field Hostel | Customer Services | Homelessness
  - 同じ表の列：OrganisationURI, EffectiveDate, PaymentDate, ServiceCategoryLabel, ServiceCategoryURI, Supplier, NetAmount, IrrecoverableVAT

## g0609（1 列）
- 見出し：ServiceCategoryLabel
- 例1 値：Central Services | Central Services | Central Services | Cultural Environmental Regulatory & Pla… | Central Services
  - 同じ表の列：OrganisationURI, EffectiveDate, PaymentDate, Directorate/Service…, ServiceCategoryURI, Supplier, NetAmount, IrrecoverableVAT

## g0610（1 列）
- 見出し：ServiceCategoryURI
- 例1 値：http://opendatacommunities.org/def/conc… | http://opendatacommunities.org/def/conc… | http://opendatacommunities.org/def/conc… | http://opendatacommunities.org/def/conc… | http://opendatacommunities.org/def/conc…
  - 同じ表の列：OrganisationURI, EffectiveDate, PaymentDate, Directorate/Service…, ServiceCategoryLabel, Supplier, NetAmount, IrrecoverableVAT

## g0611（1 列）
- 見出し：Supplier
- 例1 値：The World Centre | Middletons | Virgin Trains | RICS | Virgin
  - 同じ表の列：OrganisationURI, EffectiveDate, PaymentDate, Directorate/Service…, ServiceCategoryLabel, ServiceCategoryURI, NetAmount, IrrecoverableVAT

## g0612（1 列）
- 見出し：NetAmount
- 例1 値：15.18 | 33.00 | 43.55 | -50.00 | 5.00
  - 同じ表の列：OrganisationURI, EffectiveDate, PaymentDate, Directorate/Service…, ServiceCategoryLabel, ServiceCategoryURI, Supplier, IrrecoverableVAT

## g0613（1 列）
- 見出し：IrrecoverableVAT
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：OrganisationURI, EffectiveDate, PaymentDate, Directorate/Service…, ServiceCategoryLabel, ServiceCategoryURI, Supplier, NetAmount

## g0614（1 列）
- 見出し：ProcurementClassification:ProclassLabel
- 例1 値：Public Transport | Environmental Services | Clothing | Environmental Services | Catering
  - 同じ表の列：OrganisationURI, EffectiveDate, PaymentDate, Directorate/Service…, ServiceCategoryLabel, ServiceCategoryURI, Supplier, NetAmount

## g0615（1 列）
- 見出し：ExtractDate
- 例1 値：20/04/2015 | 20/04/2015 | 20/04/2015 | 20/04/2015 | 20/04/2015
  - 同じ表の列：OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, CarParkLocationText, CoordinateReference…, GeoX, GeoY

## g0616（1 列）
- 見出し：ServiceTypeURI
- 例1 値：http://id.esd.org.uk/service/478 | http://id.esd.org.uk/service/478 | http://id.esd.org.uk/service/478 | http://id.esd.org.uk/service/478 | http://id.esd.org.uk/service/478
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeLabel, CarParkLocationText, CoordinateReference…, GeoX, GeoY

## g0617（1 列）
- 見出し：ServiceTypeLabel
- 例1 値：Council Car Parks | Council Car Parks | Council Car Parks | Council Car Parks | Council Car Parks
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, CarParkLocationText, CoordinateReference…, GeoX, GeoY

## g0618（1 列）
- 見出し：CarParkLocationText
- 例1 値：Sedbergh | Kendal | Kendal | Kendal | Milnthorpe
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, CoordinateReference…, GeoX, GeoY

## g0619（1 列）
- 見出し：GeoPointLicensingURL
- 例1 値：http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/…
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, CarParkLocationText, CoordinateReference…, GeoX

## g0620（1 列）
- 見出し：ExpenditureType
- 例1 値：Traffic Penalties Tribunal | Total | Equipment Maintenance and Renewal | Contractors | In-house Staff
  - 同じ表の列：OrganisationLabel, OrganisationURI, EffectiveDate, ExpenditureAmount, SurplusAmount, ParkingSpacesNumber, FreeParkingSpacesNu…, Charged-forParkingS…

## g0621（1 列）
- 見出し：ExpenditureAmount
- 例1 値：601888.66 | 67591.32 | 2080 | 746225.39 | 997557.21
  - 同じ表の列：OrganisationLabel, OrganisationURI, EffectiveDate, ExpenditureType, SurplusAmount, ParkingSpacesNumber, FreeParkingSpacesNu…, Charged-forParkingS…

## g0622（1 列）
- 見出し：SurplusAmount
- 例1 値：1654808.65
  - 同じ表の列：OrganisationLabel, OrganisationURI, EffectiveDate, ExpenditureType, ExpenditureAmount, ParkingSpacesNumber, FreeParkingSpacesNu…, Charged-forParkingS…

## g0623（1 列）
- 見出し：ParkingSpacesNumber
- 例1 値：4104
  - 同じ表の列：OrganisationLabel, OrganisationURI, EffectiveDate, ExpenditureType, ExpenditureAmount, SurplusAmount, FreeParkingSpacesNu…, Charged-forParkingS…

## g0624（1 列）
- 見出し：FreeParkingSpacesNumber
- 例1 値：204
  - 同じ表の列：OrganisationLabel, OrganisationURI, EffectiveDate, ExpenditureType, ExpenditureAmount, SurplusAmount, ParkingSpacesNumber, Charged-forParkingS…

## g0625（1 列）
- 見出し：Charged-forParkingSpacesNumber
- 例1 値：3900
  - 同じ表の列：OrganisationLabel, OrganisationURI, EffectiveDate, ExpenditureType, ExpenditureAmount, SurplusAmount, ParkingSpacesNumber, FreeParkingSpacesNu…

## g0626（1 列）
- 見出し：District
- 例1 値：South Norfolk | South Norfolk | South Norfolk | South Norfolk | South Norfolk
  - 同じ表の列：Parish, PropUse, Alt_Ref, PlanningSt, Brownfield, Easting, Northing, Weblink

## g0627（1 列）
- 見出し：PropUse
- 例1 値：Housing | Housing | Housing | Housing | Housing
  - 同じ表の列：Parish, District, Alt_Ref, PlanningSt, Brownfield, Easting, Northing, Weblink

## g0628（1 列）
- 見出し：Alt_Ref
- 例1 値：2018/1765 | S.DI.1 | 2011/0152 | 2020/0671 | 2017/1000
  - 同じ表の列：Parish, District, PropUse, PlanningSt, Brownfield, Easting, Northing, Weblink

## g0629（1 列）
- 見出し：PlanningSt
- 例1 値：Planning Permission | Planning Permission | Planning Permission | Planning Permission | Planning Permission
  - 同じ表の列：Parish, District, PropUse, Alt_Ref, Brownfield, Easting, Northing, Weblink

## g0630（1 列）
- 見出し：Brownfield
- 例1 値：S/HAR/002 | S/WYM/004 | S/WYM/002 | S/TRO/001 | S/SCO/002
  - 同じ表の列：Parish, District, PropUse, Alt_Ref, PlanningSt, Easting, Northing, Weblink

## g0631（1 列）
- 見出し：Weblink
- 例1 値：https://geo.norwich.gov.uk/portal/apps/… | https://geo.norwich.gov.uk/portal/apps/… | https://geo.norwich.gov.uk/portal/apps/… | https://geo.norwich.gov.uk/portal/apps/… | https://geo.norwich.gov.uk/portal/apps/…
  - 同じ表の列：Parish, District, PropUse, Alt_Ref, PlanningSt, Brownfield, Easting, Northing

## g0632（1 列）
- 見出し：Date Added
- 例1 値：06/12/2021 | 19/11/2024 | 31/12/2017 | 09/02/2025 | 02/09/2025
  - 同じ表の列：Parish, District, PropUse, Alt_Ref, PlanningSt, Brownfield, Easting, Northing

## g0633（1 列）
- 見出し：SiteReference
- 例1 値：2236020OUT | 2134099POR | 1623671FUL | 2235428FUL | 2337120FUL
  - 同じ表の列：OrganisationURI, GeoY, GeoX, SiteplanURL, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0634（1 列）
- 見出し：Hectares
- 例1 値：0.1401 | 0.2 | 0.0737 | N/A | 0.1859
  - 同じ表の列：OrganisationURI, SiteReference, GeoY, GeoX, SiteplanURL, PlanningStatus, PermissionType, PermissionDate

## g0635（1 列）
- 見出し：PlanningStatus
- 例1 値：N/A | N/A | permissioned | permissioned | permissioned
  - 同じ表の列：OrganisationURI, SiteReference, GeoY, GeoX, SiteplanURL, Hectares, PermissionType, PermissionDate

## g0636（1 列）
- 見出し：PermissionType
- 例1 値：N/A | outline planning permission | full planning permission | full planning permission | full planning permission
  - 同じ表の列：OrganisationURI, SiteReference, GeoY, GeoX, SiteplanURL, Hectares, PlanningStatus, PermissionDate

## g0637（1 列）
- 見出し：PermissionDate
- 例1 値：N/A | 14/08/2024 | 10/08/2017 | N/A | N/A
  - 同じ表の列：OrganisationURI, SiteReference, GeoY, GeoX, SiteplanURL, Hectares, PlanningStatus, PermissionType

## g0638（1 列）
- 見出し：PlanningHistory
- 例1 値：http://www.staffordbc.gov.uk/planning-p… | N/A | http://www.staffordbc.gov.uk/planning-p… | N/A | N/A
  - 同じ表の列：OrganisationURI, SiteReference, GeoY, GeoX, SiteplanURL, Hectares, PlanningStatus, PermissionType

## g0639（1 列）
- 見出し：SiteReference
- 例1 値：2015/468 | 2015/1962 | OXT 016 | 2015/1227 | 2014/1378
  - 同じ表の列：OrganisationURI, OrganisationLabel, PreviouslyPartOf, SitePlanURL, CoordinateReference…, GeoX, GeoY, Hectares

## g0640（1 列）
- 見出し：PreviouslyPartOf
- 例1 値：n/a | n/a | n/a | n/a | n/a
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SitePlanURL, CoordinateReference…, GeoX, GeoY, Hectares

## g0641（1 列）
- 見出し：Expense type
- 例1 値：Misc (e.g. subscriptions) | Rail | Hotels | Taxi and car mileage | Hotels
  - 同じ表の列：Q1 (April - June 20…, Q2 (July - Septembe…, Q3 (October - Decem…, Q4 (January - March…

## g0642（1 列）
- 見出し：Q1 (April - June 2014)
- 例1 値：0 | 126.33 | 6.84 | 0 | 161.75
  - 同じ表の列：Expense type, Q2 (July - Septembe…, Q3 (October - Decem…, Q4 (January - March…

## g0643（1 列）
- 見出し：Q2 (July - September 2014)
- 例1 値：623.25 | 1.2 | 262.9 | 0 | 6.7
  - 同じ表の列：Expense type, Q1 (April - June 20…, Q3 (October - Decem…, Q4 (January - March…

## g0644（1 列）
- 見出し：Q3 (October - December 2014)
- 例1 値：1281.18 | 101.7 | 7.1 | 35 | 543.96
  - 同じ表の列：Expense type, Q1 (April - June 20…, Q2 (July - Septembe…, Q4 (January - March…

## g0645（1 列）
- 見出し：Q4 (January - March 2015)
- 例1 値：0 | 91.41 | 0 | 97.81 | 45
  - 同じ表の列：Expense type, Q1 (April - June 20…, Q2 (July - Septembe…, Q3 (October - Decem…

## g0646（1 列）
- 見出し：」 Gross
- 例1 値：1276 | 655.2 | 1551 | 1224.35 | 3369
  - 同じ表の列：Transaction Date

## g0647（1 列）
- 見出し：Pay Period
- 例1 値：27-Oct-11 | 12-Oct-11 | 20-Oct-11 | 7-Oct-11 | 7-Oct-11
  - 同じ表の列：Pay Date, Pay Value, Supplier

## g0648（1 列）
- 見出し：Pay Date
- 例1 値：141,090.00 | 20,440.00 | 139,352.00 | 4,408.91 | 3,064.32
  - 同じ表の列：Pay Period, Pay Value, Supplier

## g0649（1 列）
- 見出し：Pay Value
- 例1 値：PAY | PAY | PAY | PAY | PAY
  - 同じ表の列：Pay Period, Pay Date, Supplier

## g0650（1 列）
- 見出し：Supplier
- 例1 値：Core Technology Systems(UK) Ltd | Council for Administration | People 1st | Financial Services Skills Council | Royal Mail Group Property
  - 同じ表の列：Pay Period, Pay Date, Pay Value

## g0651（1 列）
- 見出し：Post unique reference
- 例1 値：BCF001 | BD2001 | GCO001 | HRD001 | BD3001
  - 同じ表の列：Grade, Job Title, Job/Team Function, Parent Department, Organisation, Unit, Reports To, Salary Costs of Rep…

## g0652（1 列）
- 見出し：Grade
- 例1 値：Director | Deputy Director | Deputy Director | Deputy Director (Temporary) | Deputy Director
  - 同じ表の列：Post unique referen…, Job Title, Job/Team Function, Parent Department, Organisation, Unit, Reports To, Salary Costs of Rep…

## g0653（1 列）
- 見出し：Job Title
- 例1 値：Head of Credit Control and Portfolio Ma… | Chief Executive | General Counsel | Head of Business Division 1 | Director of Credit Risk Group
  - 同じ表の列：Post unique referen…, Grade, Job/Team Function, Parent Department, Organisation, Unit, Reports To, Salary Costs of Rep…

## g0654（1 列）
- 見出し：Job/Team Function
- 例1 値：This division is responsible for premiu… | This division is responsible for countr… | The division is responsible for the und… | This division is responsible for ensuri… | The head of the Finance Group which inc…
  - 同じ表の列：Post unique referen…, Grade, Job Title, Parent Department, Organisation, Unit, Reports To, Salary Costs of Rep…

## g0655（1 列）
- 見出し：Parent Department
- 例1 値：Export Credits Guarantee Department | Export Credits Guarantee Department | Export Credits Guarantee Department | Export Credits Guarantee Department | Export Credits Guarantee Department
  - 同じ表の列：Post unique referen…, Grade, Job Title, Job/Team Function, Organisation, Unit, Reports To, Salary Costs of Rep…

## g0656（1 列）
- 見出し：Organisation
- 例1 値：Export Credits Guarantee Department | Export Credits Guarantee Department | Export Credits Guarantee Department | Export Credits Guarantee Department | Export Credits Guarantee Department
  - 同じ表の列：Post unique referen…, Grade, Job Title, Job/Team Function, Parent Department, Unit, Reports To, Salary Costs of Rep…

## g0657（1 列）
- 見出し：Unit
- 例1 値：Finance group | Finance group | Other | Business Group | General Counsel's Office
  - 同じ表の列：Post unique referen…, Grade, Job Title, Job/Team Function, Parent Department, Organisation, Reports To, Salary Costs of Rep…

## g0658（1 列）
- 見出し：Reports To
- 例1 値：CXO001 | CXO001 | CXO001 | DBG001 | DFG001
  - 同じ表の列：Post unique referen…, Grade, Job Title, Job/Team Function, Parent Department, Organisation, Unit, Salary Costs of Rep…

## g0659（1 列）
- 見出し：Salary Costs of Reports
- 例1 値：」2,589,044 | 」567,593 | 」840,634 | 」550,623 | 」783,493
  - 同じ表の列：Post unique referen…, Grade, Job Title, Job/Team Function, Parent Department, Organisation, Unit, Reports To

## g0660（1 列）
- 見出し：Department for Culture, Media & Sport
- 例1 値：Department for Culture, Media & Sport | Department for Culture, Media & Sport | Department for Culture, Media & Sport | Department for Culture, Media & Sport | Department for Culture, Media & Sport
  - 同じ表の列：UK Sport, 02/04/2019, Grant, WC Events Programme, Rugby League World …, 10058, 1000000

## g0661（1 列）
- 見出し：UK Sport
- 例1 値：UK Sport | UK Sport | UK Sport | UK Sport | UK Sport
  - 同じ表の列：Department for Cult…, 02/04/2019, Grant, WC Events Programme, Rugby League World …, 10058, 1000000

## g0662（1 列）
- 見出し：02/04/2019
- 例1 値：09/04/2019 | 09/04/2019 | 09/04/2019 | 09/04/2019 | 09/04/2019
  - 同じ表の列：Department for Cult…, UK Sport, Grant, WC Events Programme, Rugby League World …, 10058, 1000000

## g0663（1 列）
- 見出し：Grant
- 例1 値：Grant | Grant | Grant | Grant | Software Licence
  - 同じ表の列：Department for Cult…, UK Sport, 02/04/2019, WC Events Programme, Rugby League World …, 10058, 1000000

## g0664（1 列）
- 見出し：WC Events Programme
- 例1 値：Computer Equipment | Summer - Olympic | Aspiration - Olympic | EIS- Investment | Finance
  - 同じ表の列：Department for Cult…, UK Sport, 02/04/2019, Grant, Rugby League World …, 10058, 1000000

## g0665（1 列）
- 見出し：Rugby League World Cup 2021 Limited
- 例1 値：English Institute of Sport Company | British Canoeing | British Judo Association | English Institute of Sport Company | British Triathlon Federation
  - 同じ表の列：Department for Cult…, UK Sport, 02/04/2019, Grant, WC Events Programme, 10058, 1000000

## g0666（1 列）
- 見出し：10058
- 例1 値：10059 | 19549245 | 19549253 | 19549266 | 19549237
  - 同じ表の列：Department for Cult…, UK Sport, 02/04/2019, Grant, WC Events Programme, Rugby League World …, 1000000

## g0667（1 列）
- 見出し：1000000
- 例1 値：52790 | 38688 | 507915 | 25428.75 | 69067
  - 同じ表の列：Department for Cult…, UK Sport, 02/04/2019, Grant, WC Events Programme, Rugby League World …, 10058

## g0668（1 列）
- 見出し：Expense Type
- 例1 値：Stationery | Mobile Phones | Hire of Agency Staff (Professional/Mana… | Subsistence Payments | Taxis Overseas
  - 同じ表の列：Department, Entity, Date of Payment, Expense Area, Supplier, Transaction Number, Amount, Supplier Type

## g0669（1 列）
- 見出し：Expense Area
- 例1 値：UK Trade & Investment - Defence and Sec… | UK Trade & Investment - Strategic Trade | UK Trade & Investment - Investment Group | UK Trade & Investment - Chief Operating… | UK Trade & Investment - Defence and Sec…
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Supplier, Transaction Number, Amount, Supplier Type

## g0670（1 列）
- 見出し：Supplier
- 例1 値：Personal Expense, Name Witheld | VODAFONE LTD | CABINET OFFICE | Personal Expense, Name Witheld | Personal Expense, Name Witheld
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Transaction Number, Amount, Supplier Type

## g0671（2 列）
- 見出し：Supplier Type
- 例1 値：EXT | EXT | EXT | EXT | EXT
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount
- 例2 値：VENDOR | VENDOR | VENDOR | VENDOR | EMPLOYEE
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0672（1 列）
- 見出し：Expense Area
- 例1 値：Marketing Directorate - UK Trade and In… | Marketing Directorate - UK Trade and In… | Marketing Directorate - UK Trade and In… | Marketing Directorate - UK Trade and In… | Regional Directorate - UK Trade and Inv…
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Transaction Number, Amount In Sterling

## g0673（1 列）
- 見出し：Supplier
- 例1 値：JAMIE OLIVER | FOREIGN AND COMMONWEALTH OFFICE (FCO) | PS8 LTD | LANCASHIRE EVENING POST LTD | FOREIGN AND COMMONWEALTH OFFICE (FCO)
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount In Sterling

## g0674（1 列）
- 見出し：Department
- 例1 値：UK Trade and Investment Programme | UK Trade and Investment Programme | UK Trade and Investment Programme | UK Trade and Investment Programme | UK Trade and Investment Programme
  - 同じ表の列：Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount, Supplier Type

## g0675（1 列）
- 見出し：Expense Type
- 例1 値：Telecoms - Non-Specific Programme activ… | Travel & Subsistance UK - Default | Subsistence UK - Default | Other Goods/Services - First Time Expor… | Subsistence UK - Default
  - 同じ表の列：Department, Entity, Date of Payment, Expense Area, Supplier, Transaction Number, Amount, Supplier Type

## g0676（1 列）
- 見出し：Expense Area
- 例1 値：Investment Development - Managing Direc… | Trade Group - English Regions | Defence and Security Organisation - Bus… | Defence and Security Organisation - Bus… | Trade Group - English Regions
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Supplier, Transaction Number, Amount, Supplier Type

## g0677（1 列）
- 見出し：Supplier
- 例1 値：ONE LONDON TRADE AND INVESTMENT LTD | CORE TECHNOLOGY SYSTEMS (UK) LTD | GREEN TOMATO CARS LTD | NATURALLY CONCERNED | VODAFONE LTD
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Transaction Number, Amount, Supplier Type

## g0678（1 列）
- 見出し：Wales Office spend over 」500
- 例1 値：Wales Office | Wales Office | Wales Office | Wales Office | Wales Office
  - 同じ表の列：May-10

## g0679（1 列）
- 見出し：May-10
- 例1 値：5/20/2010 | 5/27/2010 | 11/5/2010 | 5/27/2010 | 4/5/2010
  - 同じ表の列：Wales Office spend …

## g0680（1 列）
- 見出し：<script>(function(w,d,s,l,i){w[l]=w[l]||[]
- 例1 値：<div class="site-search__right"> | <li>The site should be achievable in fi… | <li>The site meets the definition of pr… | <div class="sidebar sidebar--primary "> | <a href="https://www.warwickdc.gov.uk/i…
  - 同じ表の列：w[l].push({'gtm.sta…

## g0681（1 列）
- 見出し：w[l].push({'gtm.start':
- 例1 値：var f=d.getElementsByTagName(s)[0], | return false | Privacy</a></li> | </script> | var o=window.document.createElement("li…
  - 同じ表の列：<script>(function(w…

## g0682（1 列）
- 見出し：Expense type
- 例1 値：Minor Items and Stationery | Minor Items and Stationery | Recruitment | Miscellaneous | Learning and Development
  - 同じ表の列：Department family, Entity, Date, Expense area, Supplier, Transaction number, Amount

## g0683（1 列）
- 見出し：Expense area
- 例1 値：Compliance & Assurance | Compliance & Assurance | Compliance & Assurance | Internal/Resource Pool | Compliance & Assurance
  - 同じ表の列：Department family, Entity, Date, Expense type, Supplier, Transaction number, Amount

## g0684（1 列）
- 見出し：Supplier
- 例1 値：Impact Factory | Totaljobs Group | Totaljobs Group | Banner Group | Expedia
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Transaction number, Amount

## g0685（1 列）
- 見出し：Expense type
- 例1 値：Redfern travel costs | Professional Services Other | Professional Services Other | Professional Services Other | Professional Services Other
  - 同じ表の列：Department family, Entity, Date, Expense area, Supplier, Transaction number, Amount

## g0686（1 列）
- 見出し：Expense area
- 例1 値：Outcomes and CE | Non-Household Retail | Water2020 Risk & Reward | Compliance & Assurance | Outcomes and CE
  - 同じ表の列：Department family, Entity, Date, Expense type, Supplier, Transaction number, Amount

## g0687（1 列）
- 見出し：UPRN
- 例1 値：42044161 | 42192593 | 42134233 | 42134222 | 42161366
  - 同じ表の列：OrganisationLabel, OrganisationURI, AssetCode, PostTown, GEOX, GEOY, TenureType, TenureDetail

## g0688（1 列）
- 見出し：AssetCode
- 例1 値：42164213 | 42065963 | 42175849 | 42167013 | 42166926
  - 同じ表の列：OrganisationLabel, OrganisationURI, UPRN, PostTown, GEOX, GEOY, TenureType, TenureDetail

## g0689（1 列）
- 見出し：PostTown
- 例1 値：Higher Bebington | Wirral | Prenton | Moreton | Wallasey
  - 同じ表の列：OrganisationLabel, OrganisationURI, UPRN, AssetCode, GEOX, GEOY, TenureType, TenureDetail

## g0690（1 列）
- 見出し：GEOX
- 例1 値：332564 | 326706 | 324994 | <REDACTED> | 331287
  - 同じ表の列：OrganisationLabel, OrganisationURI, UPRN, AssetCode, PostTown, GEOY, TenureType, TenureDetail

## g0691（1 列）
- 見出し：GEOY
- 例1 値：386670 | <REDACTED> | 391816 | 388702 | 387580
  - 同じ表の列：OrganisationLabel, OrganisationURI, UPRN, AssetCode, PostTown, GEOX, TenureType, TenureDetail

## g0692（1 列）
- 見出し：TenureType
- 例1 値：Freehold | Freehold | Freehold | Freehold | Freehold
  - 同じ表の列：OrganisationLabel, OrganisationURI, UPRN, AssetCode, PostTown, GEOX, GEOY, TenureDetail

## g0693（1 列）
- 見出し：TenureDetail
- 例1 値：Owner occupied | Owner occupied | Leasehold | Owner occupied | Owner occupied
  - 同じ表の列：OrganisationLabel, OrganisationURI, UPRN, AssetCode, PostTown, GEOX, GEOY, TenureType

## g0694（1 列）
- 見出し：HoldingType
- 例1 値：Land Only | Land Only | Land Only | Land Only | Land Only
  - 同じ表の列：OrganisationLabel, OrganisationURI, UPRN, AssetCode, PostTown, GEOX, GEOY, TenureType

## g0695（1 列）
- 見出し：IncomeType
- 例1 値：On-Street Pay and Display | Off-Street Pay and Display | Penalty Charge Notice | Parking Permits | Other - Rents
  - 同じ表の列：OrganisationURI, IncomeAmount, Expenditure Type, Expenditure Amount, Surplus Spend

## g0696（1 列）
- 見出し：IncomeAmount
- 例1 値：1290879 | 666889 | 4500 | 359327 | 3600
  - 同じ表の列：OrganisationURI, IncomeType, Expenditure Type, Expenditure Amount, Surplus Spend

## g0697（1 列）
- 見出し：Expenditure Type
- 例1 値：Supplies and Services | Enforcement Contract | Communications and Computing | Transport Related | Rents and Rates
  - 同じ表の列：OrganisationURI, IncomeType, IncomeAmount, Expenditure Amount, Surplus Spend

## g0698（1 列）
- 見出し：Expenditure Amount
- 例1 値：286957 | 7661 | 21532 | 241876 | 36012
  - 同じ表の列：OrganisationURI, IncomeType, IncomeAmount, Expenditure Type, Surplus Spend

## g0699（1 列）
- 見出し：Surplus Spend
- 例1 値：893116
  - 同じ表の列：OrganisationURI, IncomeType, IncomeAmount, Expenditure Type, Expenditure Amount

## g0700（1 列）
- 見出し：DATE NOTIFICATION OF DEATH
- 例1 値：10/17/2023 | 10/17/2023 | 04/03/2023 | 1/29/2024 | 11/16/2023
  - 同じ表の列：DATE OF BIRTH, DATE OF DEATH, Age at DOD, FUNERAL TYPE, COST TO LA

## g0701（1 列）
- 見出し：DATE OF BIRTH
- 例1 値：6/24/1939 | 7/29/1943 | 02/05/1956 | 3/20/1938 | 9/21/1941
  - 同じ表の列：DATE NOTIFICATION O…, DATE OF DEATH, Age at DOD, FUNERAL TYPE, COST TO LA

## g0702（1 列）
- 見出し：DATE OF DEATH
- 例1 値：11/15/2023 | 12/06/2023 | 07/08/2023 | 1/27/2024 | 1/18/2024
  - 同じ表の列：DATE NOTIFICATION O…, DATE OF BIRTH, Age at DOD, FUNERAL TYPE, COST TO LA

## g0703（1 列）
- 見出し：Age at DOD
- 例1 値：67 | 85 | 82 | 60 | 58
  - 同じ表の列：DATE NOTIFICATION O…, DATE OF BIRTH, DATE OF DEATH, FUNERAL TYPE, COST TO LA

## g0704（1 列）
- 見出し：FUNERAL TYPE
- 例1 値：Cremation | Cremation | Cremation | Cremation | Cremation
  - 同じ表の列：DATE NOTIFICATION O…, DATE OF BIRTH, DATE OF DEATH, Age at DOD, COST TO LA

## g0705（1 列）
- 見出し：COST TO LA
- 例1 値：1,420.00 | 1,175.00 | 1,499.00 | 1,420.00 | 983
  - 同じ表の列：DATE NOTIFICATION O…, DATE OF BIRTH, DATE OF DEATH, Age at DOD, FUNERAL TYPE

## 答えの雛形

```
g0601	
g0602	
g0603	
g0604	
g0605	
g0606	
g0607	
g0608	
g0609	
g0610	
g0611	
g0612	
g0613	
g0614	
g0615	
g0616	
g0617	
g0618	
g0619	
g0620	
g0621	
g0622	
g0623	
g0624	
g0625	
g0626	
g0627	
g0628	
g0629	
g0630	
g0631	
g0632	
g0633	
g0634	
g0635	
g0636	
g0637	
g0638	
g0639	
g0640	
g0641	
g0642	
g0643	
g0644	
g0645	
g0646	
g0647	
g0648	
g0649	
g0650	
g0651	
g0652	
g0653	
g0654	
g0655	
g0656	
g0657	
g0658	
g0659	
g0660	
g0661	
g0662	
g0663	
g0664	
g0665	
g0666	
g0667	
g0668	
g0669	
g0670	
g0671	
g0672	
g0673	
g0674	
g0675	
g0676	
g0677	
g0678	
g0679	
g0680	
g0681	
g0682	
g0683	
g0684	
g0685	
g0686	
g0687	
g0688	
g0689	
g0690	
g0691	
g0692	
g0693	
g0694	
g0695	
g0696	
g0697	
g0698	
g0699	
g0700	
g0701	
g0702	
g0703	
g0704	
g0705	
```
