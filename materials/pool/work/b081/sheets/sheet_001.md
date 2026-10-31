# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Appointing Minister
- 例1 値：Does not normally include attendance at… | Note | Minister without Portfolio | Minister for the Cabinet Office, Paymas… | Minister of State, Cabinet Office
  - 同じ表の列：Date of Hospitality, Type of hospitality…

## g0002（1 列）
- 見出し：Date of Hospitality
- 例1 値：nil return | 16/20 July 2010 | 15-Jul-2010
  - 同じ表の列：Appointing Minister, Type of hospitality…

## g0003（1 列）
- 見出し：Type of hospitality received
- 例1 値：Dinner | Flight upgrades
  - 同じ表の列：Appointing Minister, Date of Hospitality

## g0004（1 列）
- 見出し：DATES
- 例1 値：22.11.11 | DEPARTMENT FOR EDUCATION – TOM JEFFERY,… | 19.12.11 | 20.10.11 | 25.10.11
  - 同じ表の列：DESTINATION, PURPOSE, TRAVEL, OTHER (Including Ho…, Total Cost £

## g0005（1 列）
- 見出し：DESTINATION
- 例1 値：Lord Puttnam of Queensgate | London | Sheffield | Excel Centre, London | Frodsham
  - 同じ表の列：DATES, PURPOSE, TRAVEL, OTHER (Including Ho…, Total Cost £

## g0006（1 列）
- 見出し：PURPOSE
- 例1 値：Type of Hospitality Received | Personal Incidental allowance | Board meeting | Travel to London | Personal Incidental allowance
  - 同じ表の列：DATES, DESTINATION, TRAVEL, OTHER (Including Ho…, Total Cost £

## g0007（1 列）
- 見出し：TRAVEL
- 例1 値：Air | TRAVEL | TRAVEL | TRAVEL | Air
  - 同じ表の列：DATES, DESTINATION, PURPOSE, OTHER (Including Ho…, Total Cost £

## g0008（1 列）
- 見出し：OTHER (Including Hospitality Given)
- 例1 値：OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given)
  - 同じ表の列：DATES, DESTINATION, PURPOSE, TRAVEL, Total Cost £

## g0009（1 列）
- 見出し：Total Cost £
- 例1 値：34.83 | 5 | 5 | 75.31 | Total Cost £
  - 同じ表の列：DATES, DESTINATION, PURPOSE, TRAVEL, OTHER (Including Ho…

## g0010（1 列）
- 見出し：Date gift given
- 例1 値：Date(s) of trip | Parliamentary Under-Secretary of State,… | Sep-11 | Sep-11 | Sep-11
  - 同じ表の列：To, Gift, Value

## g0011（1 列）
- 見出し：To
- 例1 値：Organisation for Economic Co-operation … | To | Ibk initiatives | Brook (sexual health) | The National Literacy Trust;
  - 同じ表の列：Date gift given, Gift, Value

## g0012（1 列）
- 見出し：Gift
- 例1 値：To discuss teacher training | General discussion | To discuss young runaways | General discussion | To discuss the English Baccalaureate an…
  - 同じ表の列：Date gift given, To, Value

## g0013（1 列）
- 見出し：Value
- 例1 値：‘No 32 (The Royal) Squadron’ or ‘other … | Value | ‘No 32 (The Royal) Squadron’ or ‘other … | Value | Value
  - 同じ表の列：Date gift given, To, Gift

## g0014（1 列）
- 見出し：Start date of trip
- 例1 値：21/09/2016 | 31/08/2016 | 16/09/2016 | 07/07/2016 | 26/09/2016
  - 同じ表の列：Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Class of travel, Accommodation/ Meals, Total cost, includi…

## g0015（1 列）
- 見出し：Duration of Visit (Days)
- 例1 値：1 | 1 | 1 | 2 | 1
  - 同じ表の列：Start date of trip, Destination, Purpose of trip, Mode of transport, Class of travel, Accommodation/ Meals, Total cost, includi…

## g0016（1 列）
- 見出し：Destination
- 例1 値：Paris/Rome | Amsterdam | Warsaw / Budapest | Brussels | London
  - 同じ表の列：Start date of trip, Duration of Visit (…, Purpose of trip, Mode of transport, Class of travel, Accommodation/ Meals, Total cost, includi…

## g0017（1 列）
- 見出し：Purpose of trip
- 例1 値：Meeting with European Officials | Meeting with European Officials | Meeting with European Officials | Meeting with European Officials | Meeting with European Officials
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Mode of transport, Class of travel, Accommodation/ Meals, Total cost, includi…

## g0018（1 列）
- 見出し：Mode of transport
- 例1 値：AIR | RAIL | RAIL/TAXI | RAIL | AIR/TAXI
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Purpose of trip, Class of travel, Accommodation/ Meals, Total cost, includi…

## g0019（1 列）
- 見出し：Class of travel
- 例1 値：DISCOUNT ECONOMY | BUSINESS PREMIER | BUSINESS PREMIER | DISCOUNT ECONOMY | N/A
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Accommodation/ Meals, Total cost, includi…

## g0020（1 列）
- 見出し：Accommodation/ Meals
- 例1 値：HOTEL
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Class of travel, Total cost, includi…

## g0021（1 列）
- 見出し：Total cost, including all visas, accommodation, travel, meal
- 例1 値：」490.00 | 」490.00 | 」523.00 | 」781.00 | 」391.20
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Class of travel, Accommodation/ Meals

## g0022（1 列）
- 見出し：Mode of travel
- 例1 値：AIR | AIR | AIR | AIR | AIR
  - 同じ表の列：Date of Departure, Duration of stay, Destination, Class of travel, Base Sales Includin…

## g0023（1 列）
- 見出し：Date of Departure
- 例1 値：06/06/2013 | 17/06/2013 | 22/06/2013 | 08/06/2013 | 29/04/2013
  - 同じ表の列：Mode of travel, Duration of stay, Destination, Class of travel, Base Sales Includin…

## g0024（1 列）
- 見出し：Duration of stay
- 例1 値：1 | 2 | 2 | 4 | 6
  - 同じ表の列：Mode of travel, Date of Departure, Destination, Class of travel, Base Sales Includin…

## g0025（1 列）
- 見出し：Destination
- 例1 値：Lon Heathrow | Dulles | Brussels | Moscow Domod | Dubai
  - 同じ表の列：Mode of travel, Date of Departure, Duration of stay, Class of travel, Base Sales Includin…

## g0026（1 列）
- 見出し：Class of travel
- 例1 値：ECONOMY | SECOND CLASS RAIL | SECOND CLASS RAIL | ECONOMY | PREMIUM ECONOMY
  - 同じ表の列：Mode of travel, Date of Departure, Duration of stay, Destination, Base Sales Includin…

## g0027（1 列）
- 見出し：Base Sales Including Tax
- 例1 値：」1,650.00 | 」1,021.00 | 」486.00 | 」531.00 | 」607.00
  - 同じ表の列：Mode of travel, Date of Departure, Duration of stay, Destination, Class of travel

## g0028（1 列）
- 見出し：1 - Aid/effectiveness
- 例1 値：Table 1.3: G8 Multilateral Debt Relief | Table 1.2: G8 bilateral & imputed multi… | Additional table | Figure 6.3: G8 disbursements to educati… | Annex C
  - 同じ表の列：Notes/source

## g0029（1 列）
- 見出し：Notes/source
- 例1 値：Source: WHO/UNICEF Joint Monitoring Pro… | Source: UNDP and WHO. Legros, G., Havet… | see figure 2.1 | see figure 1.2 | see figure 9.2
  - 同じ表の列：1 - Aid/effectivene…

## g0030（1 列）
- 見出し：Percentage paid within 30 working days
- 例1 値：DFTc | HA Agency | DVLA Agency | VCA Agency | GCDA Agency
  - 同じ表の列：Jan-12, Feb-12, Mar-12, Apr-12, May-12, Jun-12, Jul-12, Aug-12

## g0031（1 列）
- 見出し：Jan-12
- 例1 値：99.63% | 98.59% | 100.00% | 99.71% | 99.37%
  - 同じ表の列：Percentage paid wit…, Feb-12, Mar-12, Apr-12, May-12, Jun-12, Jul-12, Aug-12

## g0032（1 列）
- 見出し：Feb-12
- 例1 値：100.00% | 100.00% | 99.78% | 99.75% | 99.30%
  - 同じ表の列：Percentage paid wit…, Jan-12, Mar-12, Apr-12, May-12, Jun-12, Jul-12, Aug-12

## g0033（1 列）
- 見出し：Mar-12
- 例1 値：99.98% | 99.79% | 100.00% | 99.33% | 99.97%
  - 同じ表の列：Percentage paid wit…, Jan-12, Feb-12, Apr-12, May-12, Jun-12, Jul-12, Aug-12

## g0034（1 列）
- 見出し：Apr-12
- 例1 値：99.82% | 100.00% | 100.00% | 99.72% | 99.88%
  - 同じ表の列：Percentage paid wit…, Jan-12, Feb-12, Mar-12, May-12, Jun-12, Jul-12, Aug-12

## g0035（1 列）
- 見出し：May-12
- 例1 値：100.00% | 99.73% | 99.79% | 99.94% | 98.44%
  - 同じ表の列：Percentage paid wit…, Jan-12, Feb-12, Mar-12, Apr-12, Jun-12, Jul-12, Aug-12

## g0036（1 列）
- 見出し：Jun-12
- 例1 値：99.89% | 100.00% | 99.79% | 99.83% | 99.77%
  - 同じ表の列：Percentage paid wit…, Jan-12, Feb-12, Mar-12, Apr-12, May-12, Jul-12, Aug-12

## g0037（1 列）
- 見出し：Jul-12
- 例1 値：99.25% | 100.00% | 99.94% | 99.78% | 100.00%
  - 同じ表の列：Percentage paid wit…, Jan-12, Feb-12, Mar-12, Apr-12, May-12, Jun-12, Aug-12

## g0038（1 列）
- 見出し：Aug-12
- 例1 値：99.79% | 99.76% | 100.00% | 98.79% | 100.00%
  - 同じ表の列：Percentage paid wit…, Jan-12, Feb-12, Mar-12, Apr-12, May-12, Jun-12, Jul-12

## g0039（1 列）
- 見出し：Sep-12
- 例1 値：100.00% | 99.15% | 99.95% | 99.77% | 100.00%
  - 同じ表の列：Percentage paid wit…, Jan-12, Feb-12, Mar-12, Apr-12, May-12, Jun-12, Jul-12

## g0040（1 列）
- 見出し：NptgLocalityCode
- 例1 値：E0035207 | N0061491 | E0035664 | E0035663 | E0035271
  - 同じ表の列：AdministrativeAreaC…, NptgDistrictCode, SourceLocalityType, Easting, Northing, CreationDateTime, ModificationDateTime, RevisionNumber

## g0041（1 列）
- 見出し：AdministrativeAreaCode
- 例1 値：007 | 010 | 001 | 010 | 006
  - 同じ表の列：NptgLocalityCode, NptgDistrictCode, SourceLocalityType, Easting, Northing, CreationDateTime, ModificationDateTime, RevisionNumber

## g0042（1 列）
- 見出し：NptgDistrictCode
- 例1 値：310 | 310 | 310 | 310 | 310
  - 同じ表の列：NptgLocalityCode, AdministrativeAreaC…, SourceLocalityType, Easting, Northing, CreationDateTime, ModificationDateTime, RevisionNumber

## g0043（1 列）
- 見出し：SourceLocalityType
- 例1 値：Lo | Lo | Lo | Add | Add
  - 同じ表の列：NptgLocalityCode, AdministrativeAreaC…, NptgDistrictCode, Easting, Northing, CreationDateTime, ModificationDateTime, RevisionNumber

## g0044（1 列）
- 見出し：Easting
- 例1 値：372632 | 318653 | 315080 | 372198 | 295679
  - 同じ表の列：NptgLocalityCode, AdministrativeAreaC…, NptgDistrictCode, SourceLocalityType, Northing, CreationDateTime, ModificationDateTime, RevisionNumber

## g0045（1 列）
- 見出し：Northing
- 例1 値：167528 | 195270 | 177839 | 422650 | 168981
  - 同じ表の列：NptgLocalityCode, AdministrativeAreaC…, NptgDistrictCode, SourceLocalityType, Easting, CreationDateTime, ModificationDateTime, RevisionNumber

## g0046（1 列）
- 見出し：CreationDateTime
- 例1 値：2005-10-05T10:46:11 | 2005-10-05T10:47:09 | 2005-10-05T10:50:27 | 2005-10-05T10:46:04 | 2005-10-05T10:52:39
  - 同じ表の列：NptgLocalityCode, AdministrativeAreaC…, NptgDistrictCode, SourceLocalityType, Easting, Northing, ModificationDateTime, RevisionNumber

## g0047（1 列）
- 見出し：ModificationDateTime
- 例1 値：2005-10-05T10:49:15 | 2005-10-05T10:52:37 | 2005-10-05T10:53:17 | 2018-06-26T21:48:01.583 | 2014-03-14T10:06:52
  - 同じ表の列：NptgLocalityCode, AdministrativeAreaC…, NptgDistrictCode, SourceLocalityType, Easting, Northing, CreationDateTime, RevisionNumber

## g0048（1 列）
- 見出し：RevisionNumber
- 例1 値：2 | 0 | 1 | 1 | 0
  - 同じ表の列：NptgLocalityCode, AdministrativeAreaC…, NptgDistrictCode, SourceLocalityType, Easting, Northing, CreationDateTime, ModificationDateTime

## g0049（1 列）
- 見出し：Modification
- 例1 値：new | new | revise | revise | new
  - 同じ表の列：NptgLocalityCode, AdministrativeAreaC…, NptgDistrictCode, SourceLocalityType, Easting, Northing, CreationDateTime, ModificationDateTime

## g0050（1 列）
- 見出し：Enabling Retirement Savings Programme
- 例1 値：98.8 | Project on schedule and commenced in Oc… | The whole life costs cover the period f… | 18/05/2007 | The variance in the 2012/13 Programme f…
  - 同じ表の列：Fraud and Error Pro…, Incapacity Benefit …, Personal Independen…, Specialist Disabili…, State Pension Refor…, Universal Credit Pr…, Work Programme, Youth Contract

## g0051（1 列）
- 見出し：Fraud and Error Programme
- 例1 値：01/03/2015 | The last MPA review assessed the Progra… | 770.3 | The Fraud and Error Programme will deli… | The budget whole life costs represented…
  - 同じ表の列：Enabling Retirement…, Incapacity Benefit …, Personal Independen…, Specialist Disabili…, State Pension Refor…, Universal Credit Pr…, Work Programme, Youth Contract

## g0052（1 列）
- 見出し：Incapacity Benefit Reassessment
- 例1 値：Green | Progress against target is monitored mo… | 09/07/2009 | 143.6 | DWP
  - 同じ表の列：Enabling Retirement…, Fraud and Error Pro…, Personal Independen…, Specialist Disabili…, State Pension Refor…, Universal Credit Pr…, Work Programme, Youth Contract

## g0053（1 列）
- 見出し：Personal Independence Payment Implementation
- 例1 値：31/10/2011 | DWP | Personal Independence Payment (PIP) wil… | 126.72 | The MPA review team recognised the huge…
  - 同じ表の列：Enabling Retirement…, Fraud and Error Pro…, Incapacity Benefit …, Specialist Disabili…, State Pension Refor…, Universal Credit Pr…, Work Programme, Youth Contract

## g0054（1 列）
- 見出し：Specialist Disability Employment Programme
- 例1 値：DWP | The Programme is working closely with c… | 35.63 | Amber | Whole life costs assume that £15m savin…
  - 同じ表の列：Enabling Retirement…, Fraud and Error Pro…, Incapacity Benefit …, Personal Independen…, State Pension Refor…, Universal Credit Pr…, Work Programme, Youth Contract

## g0055（1 列）
- 見出し：State Pension Reform - Single Tier
- 例1 値：Amber/Green | 1.12 | DWP | 27/02/2012 | 31/10/2017
  - 同じ表の列：Enabling Retirement…, Fraud and Error Pro…, Incapacity Benefit …, Personal Independen…, Specialist Disabili…, Universal Credit Pr…, Work Programme, Youth Contract

## g0056（1 列）
- 見出し：Universal Credit Programme
- 例1 値：The Universal Credit Pathfinder was suc… | At the time of the review, there was a … | 17/11/2011 | The budgeted whole life costs will be c… | This rating dates back to September 201…
  - 同じ表の列：Enabling Retirement…, Fraud and Error Pro…, Incapacity Benefit …, Personal Independen…, Specialist Disabili…, State Pension Refor…, Work Programme, Youth Contract

## g0057（1 列）
- 見出し：Work Programme
- 例1 値：25/11/2010 | 777 | Work Programme budgets vary automatical… | Work Programme budgets vary automatical… | DWP
  - 同じ表の列：Enabling Retirement…, Fraud and Error Pro…, Incapacity Benefit …, Personal Independen…, Specialist Disabili…, State Pension Refor…, Universal Credit Pr…, Youth Contract

## g0058（1 列）
- 見出し：Youth Contract
- 例1 値：Since project went live, timing and sch… | 182.04 | Following an aggressive timetable the P… | The Youth Contract was a response to un… | 19/01/2012
  - 同じ表の列：Enabling Retirement…, Fraud and Error Pro…, Incapacity Benefit …, Personal Independen…, Specialist Disabili…, State Pension Refor…, Universal Credit Pr…, Work Programme

## g0059（1 列）
- 見出し：Benefit Cap
- 例1 値：The project went live in Bromley, Croyd… | The 12/13 budget was set early in 2012 … | 27 | Project on track | 31/07/2013
  - 同じ表の列：Enabling Retirement…, Fraud and Error Pro…, Incapacity Benefit …, Personal Independen…, Specialist Disabili…, State Pension Refor…, Universal Credit Pr…, Work Programme

## g0060（1 列）
- 見出し：Department Family
- 例1 値：FCO | FCO | FCO | FCO | FCO
  - 同じ表の列：Entity, Payment Date, Expense Type, Expense Area, Transactions Number, Amount (」)

## g0061（1 列）
- 見出し：Entity
- 例1 値：FCO | FCO | FCO | FCO | FCO
  - 同じ表の列：Department Family, Payment Date, Expense Type, Expense Area, Transactions Number, Amount (」)

## g0062（1 列）
- 見出し：Payment Date
- 例1 値：16-Apr-10 | 15-Apr-10 | 06-Apr-10 | 28-Apr-10 | 27-Apr-10
  - 同じ表の列：Department Family, Entity, Expense Type, Expense Area, Transactions Number, Amount (」)

## g0063（1 列）
- 見出し：Expense Type
- 例1 値：IT/IS Consultancy | Office Support Services | Programme Spend (Oracle Projects Contro… | Assets Under Construction (Oracle PA Co… | Cleaning & Waste
  - 同じ表の列：Department Family, Entity, Payment Date, Expense Area, Transactions Number, Amount (」)

## g0064（1 列）
- 見出し：Expense Area
- 例1 値：DG CHANGE & DELIVERY | DG CHANGE & DELIVERY | DG CHANGE & DELIVERY | DG CHANGE & DELIVERY | DG CHANGE & DELIVERY
  - 同じ表の列：Department Family, Entity, Payment Date, Expense Type, Transactions Number, Amount (」)

## g0065（1 列）
- 見出し：Transactions Number
- 例1 値：9232 | 1162640 | 1162828 | 5089 | 1161841
  - 同じ表の列：Department Family, Entity, Payment Date, Expense Type, Expense Area, Amount (」)

## g0066（1 列）
- 見出し：Amount (」)
- 例1 値：6,680.58 | 6,616.35 | 6,737.50 | 7,650.00 | 5,183.18
  - 同じ表の列：Department Family, Entity, Payment Date, Expense Type, Expense Area, Transactions Number

## g0067（1 列）
- 見出し：UID
- 例1 値：1853 | 1083 | 1296 | 1080 | 708
  - 同じ表の列：Estimated Number of…, Date Range

## g0068（1 列）
- 見出し：Estimated Number of Files
- 例1 値：56 | 8 | 11 | 2 | 92
  - 同じ表の列：UID, Date Range

## g0069（1 列）
- 見出し：Date Range
- 例1 値：1988-1988 | 1957-1968 | 1993-1994 | 1958-1967 | 2005-2005
  - 同じ表の列：UID, Estimated Number of…

## g0070（1 列）
- 見出し：Main, parent or sponsoring department
- 例1 値：Foreign, Commonwealth & Development Off… | Foreign, Commonwealth & Development Off… | Foreign, Commonwealth & Development Off… | Foreign, Commonwealth & Development Off… | Foreign, Commonwealth & Development Off…
  - 同じ表の列：Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…, Non-payroll Staff A…

## g0071（2 列）
- 見出し：Payroll staff AO/AA Headcount
- 例1 値：133 | 0 | 487 | 0 | 0
  - 同じ表の列：Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…, Non-payroll Staff A…
- 例2 値：197 | 12 | 604 | 1 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0072（1 列）
- 見出し：Payroll staff EO Headcount
- 例1 値：31 | 0 | 0 | 9 | 1
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…, Non-payroll Staff A…

## g0073（1 列）
- 見出し：Payroll staff SEO/HEO Headcount
- 例1 値：0 | 22 | 5 | 2829 | 435
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…, Non-payroll Staff A…

## g0074（1 列）
- 見出し：Payroll staff Grade 6/7 Headcount
- 例1 値：0 | 19 | 3028 | 218 | 0
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…, Non-payroll Staff A…

## g0075（2 列）
- 見出し：Payroll staff SCS Headcount
- 例1 値：3 | 1 | 550 | 100 | 0
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff Other…, Payroll staff Total…, Non-payroll Staff A…
- 例2 値：1 | 251 | 30 | 0 | 1
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff Other…, Payroll staff Total…

## g0076（1 列）
- 見出し：Payroll staff Other, unknown or unspecified Headcount
- 例1 値：0 | 45 | 0 | 10 | 0
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Total…, Non-payroll Staff A…

## g0077（2 列）
- 見出し：Payroll staff Total Employees Headcount
- 例1 値：1,335 | 53 | 10 | 10 | 0
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Non-payroll Staff A…
- 例2 値：67 | 15 | 174 | 1910 | 2,987
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

## g0078（2 列）
- 見出し：Non-payroll Staff Agency staff (clerical/admin) Headcount
- 例1 値：0 | 2 | 0 | 14 | 0
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…
- 例2 値：0 | 83 | 779 | 1 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

## g0079（1 列）
- 見出し：Non-payroll Staff Intermin Managers Headcount
- 例1 値：0 | 3 | 0 | 21 | 0
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0080（1 列）
- 見出し：Role in HMRC
- 例1 値：Deputy Director, SCS 1 | Director, SCS 2 | Deputy Director, SCS 1 | HR Director, SCS 1 | Deputy Director, SCS 1
  - 同じ表の列：Outside employment

## g0081（1 列）
- 見出し：Outside employment
- 例1 値：Cambridge University Hospitals Trust, N… | Welsh Rugby Union. Referee Educator | NHS Blood and Transplant, Non-Executive… | Ty Tanc Ltd – Director; James Mitton Co… | Dean & Canons of Manchester Cathedral, …
  - 同じ表の列：Role in HMRC

## g0082（1 列）
- 見出し：Electronic Exchange of Social Security Information (EESSI) P
- 例1 値：The Electronic Exchange of Social Secur… | HMRC | 0.12 | Amber/Green | 0.12
  - 同じ表の列：One Click, Open Cases Programme, Organised Crime, Real Time Informati…, Volume Crime, Wider Coverage Proj…, Expanding the use o…, Debt Management & B…

## g0083（1 列）
- 見出し：One Click
- 例1 値：10.01 | Amber/Red | 24/03/2010 | One Click brings many tax services (Cor… | Most of this programme has been deliver…
  - 同じ表の列：Electronic Exchange…, Open Cases Programme, Organised Crime, Real Time Informati…, Volume Crime, Wider Coverage Proj…, Expanding the use o…, Debt Management & B…

## g0084（1 列）
- 見出し：Open Cases Programme
- 例1 値：Green | HMRC | The Programme cleared all legacy open c… | 31/10/2010 | 19.43
  - 同じ表の列：Electronic Exchange…, One Click, Organised Crime, Real Time Informati…, Volume Crime, Wider Coverage Proj…, Expanding the use o…, Debt Management & B…

## g0085（1 列）
- 見出し：Organised Crime
- 例1 値：Amber/Green | 82.73 | The Programme was originally forecast t… | 01/04/2011 | 02/07/2012
  - 同じ表の列：Electronic Exchange…, One Click, Open Cases Programme, Real Time Informati…, Volume Crime, Wider Coverage Proj…, Expanding the use o…, Debt Management & B…

## g0086（1 列）
- 見出し：Real Time Information (RTI)
- 例1 値：Amber | 28.32 | 241.10 | Real Time Information is the next stage… | HMRC
  - 同じ表の列：Electronic Exchange…, One Click, Open Cases Programme, Organised Crime, Volume Crime, Wider Coverage Proj…, Expanding the use o…, Debt Management & B…

## g0087（1 列）
- 見出し：Volume Crime
- 例1 値：HMRC | Amber/Green | 11.20 | 42.04 | 31/03/2013
  - 同じ表の列：Electronic Exchange…, One Click, Open Cases Programme, Organised Crime, Real Time Informati…, Wider Coverage Proj…, Expanding the use o…, Debt Management & B…

## g0088（1 列）
- 見出し：Wider Coverage Project
- 例1 値：104.74 | 552.59 | HMRC | 103.77 | 14/09/2011
  - 同じ表の列：Electronic Exchange…, One Click, Open Cases Programme, Organised Crime, Real Time Informati…, Volume Crime, Expanding the use o…, Debt Management & B…

## g0089（1 列）
- 見出し：Expanding the use of Debt Collection Agencies
- 例1 値：The forecast costs figure of £18.70m fo… | Amber/Green | 70.68 | The investment to extend the use of Deb… | HMRC
  - 同じ表の列：Electronic Exchange…, One Click, Open Cases Programme, Organised Crime, Real Time Informati…, Volume Crime, Wider Coverage Proj…, Debt Management & B…

## g0090（1 列）
- 見出し：Debt Management & Banking (DMB) Staff Reinvestment
- 例1 値：56.41 | Investment in Debt Management & Banking… | HMRC | 11.27 | 11.26
  - 同じ表の列：Electronic Exchange…, One Click, Open Cases Programme, Organised Crime, Real Time Informati…, Volume Crime, Wider Coverage Proj…, Expanding the use o…

## g0091（1 列）
- 見出し：ICT
- 例1 値：6 | 1 | 8 | 9 | Note that figures are given for amounts…
  - 同じ表の列：Exceptions for peri…

## g0092（1 列）
- 見出し：Exceptions for period 01 November 2010 to 30 September 2011
- 例1 値：Department | Home Office | Home Office | Home Office | Home Office
  - 同じ表の列：ICT

## g0093（1 列）
- 見出し：Posting Date
- 例1 値：13/04/2011 | 04/04/2011 | 18/04/2011 | 04/04/2011 | 08/04/2011
  - 同じ表の列：Transaction Amount

## g0094（1 列）
- 見出し：Transaction Amount
- 例1 値：902.4 | 582 | 545.08 | 666 | 837.65
  - 同じ表の列：Posting Date

## g0095（1 列）
- 見出し：Escorting and Travel
- 例1 値：HO | This project oversees the re-tendering … | 283.56 | 74.88 | 01/07/2008
  - 同じ表の列：SOCA Catalyst, Commercial and Oper…, Extend and Blend, Immigration and Asy…, Immigration Case Wo…, IMPACT, New Passport Progra…, Next Generation Out…

## g0096（1 列）
- 見出し：SOCA Catalyst
- 例1 値：01/06/2010 | The SOCA Catalyst Programme closed foll… | 6.74 | The programme costs are tracking profil… | Amber/Green
  - 同じ表の列：Escorting and Travel, Commercial and Oper…, Extend and Blend, Immigration and Asy…, Immigration Case Wo…, IMPACT, New Passport Progra…, Next Generation Out…

## g0097（1 列）
- 見出し：Commercial and Operating Managers Procuring Asylum Support S
- 例1 値：01/07/2009 | The overall aim of COMPASS project is t… | 686.70 | Spend is within budget. | The Whole Life Cost of the project incl…
  - 同じ表の列：Escorting and Travel, SOCA Catalyst, Extend and Blend, Immigration and Asy…, Immigration Case Wo…, IMPACT, New Passport Progra…, Next Generation Out…

## g0098（1 列）
- 見出し：Extend and Blend
- 例1 値：30/04/2012 | HO | The programme was re-phased to take acc… | The new systems have now been rolled ou… | 01/10/2009
  - 同じ表の列：Escorting and Travel, SOCA Catalyst, Commercial and Oper…, Immigration and Asy…, Immigration Case Wo…, IMPACT, New Passport Progra…, Next Generation Out…

## g0099（1 列）
- 見出し：Immigration and Asylum Biometric System (IABS)
- 例1 値：27.70 | The programme end date was revised to 3… | 24.69 | Amber/Green | 367.15
  - 同じ表の列：Escorting and Travel, SOCA Catalyst, Commercial and Oper…, Extend and Blend, Immigration Case Wo…, IMPACT, New Passport Progra…, Next Generation Out…

## g0100（1 列）
- 見出し：Immigration Case Work (ICW)
- 例1 値：The ICW Programme is a business-led cha… | The programme has successfully delivere… | 25/06/2007 | 374.00 | 59.97
  - 同じ表の列：Escorting and Travel, SOCA Catalyst, Commercial and Oper…, Extend and Blend, Immigration and Asy…, IMPACT, New Passport Progra…, Next Generation Out…

## g0101（1 列）
- 見出し：IMPACT
- 例1 値：The return on investment will be consid… | The programme costs are tracking profil… | 5.93 | The programme’s mandate, as set out in … | The programme end date has now been rev…
  - 同じ表の列：Escorting and Travel, SOCA Catalyst, Commercial and Oper…, Extend and Blend, Immigration and Asy…, Immigration Case Wo…, New Passport Progra…, Next Generation Out…

## g0102（1 列）
- 見出し：New Passport Programme
- 例1 値：45.27 | The capability is now operating as Busi… | 01/11/2012 | Programme spend has been tracking profi… | The Whole Life Cost remains on track su…
  - 同じ表の列：Escorting and Travel, SOCA Catalyst, Commercial and Oper…, Extend and Blend, Immigration and Asy…, Immigration Case Wo…, IMPACT, Next Generation Out…

## g0103（1 列）
- 見出し：Next Generation Outsourced Visa Services Contract
- 例1 値：N/A | N/A | 09/12/2011 | 01/07/2014 | Amber/Green
  - 同じ表の列：Escorting and Travel, SOCA Catalyst, Commercial and Oper…, Extend and Blend, Immigration and Asy…, Immigration Case Wo…, IMPACT, New Passport Progra…

## g0104（1 列）
- 見出し：SOCA Information Systems and Operating Technology (ISOT) Pro
- 例1 値：01/04/2008 | 30/09/2013 | Amber/Red | HO | The programme costs are tracking profil…
  - 同じ表の列：Escorting and Travel, SOCA Catalyst, Commercial and Oper…, Extend and Blend, Immigration and Asy…, Immigration Case Wo…, IMPACT, New Passport Progra…

## g0105（1 列）
- 見出し：Organisation Type
- 例1 値：Executive Agency | Executive Non-Departmental Public Body | Executive Non-Departmental Public Body | Executive Non-Departmental Public Body | Ministerial Department
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0106（1 列）
- 見出し：Main, parent or sponsoring department
- 例1 値：Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence
  - 同じ表の列：Organisation Type, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0107（1 列）
- 見出し：Payroll staff EO Headcount
- 例1 値：0 | 284 | 0 | 8,920 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0108（1 列）
- 見出し：Payroll staff SEO/HEO Headcount
- 例1 値：3 | 14,151 | 1912 | 0 | 266
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0109（1 列）
- 見出し：Payroll staff Grade 6/7 Headcount
- 例1 値：4 | 0 | 1242 | 2,318 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0110（1 列）
- 見出し：Payroll staff Other, unknown or unspecified Headcount
- 例1 値：98 | 19,232 | 0 | 57 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Total…

## g0111（1 列）
- 見出し：Minister
- 例1 値：Mrs Ursula Brennan, Permanent Secretary… | Mrs Ursula Brennan, Permanent Secretary… | Sir Bill Jeffrey KCB, Permanent Secreta… | Sir Bill Jeffrey KCB, Permanent Secreta… | Mrs Ursula Brennan, 2nd Permanent Secre…
  - 同じ表の列：Date of Meeting, Purpose of Meeting

## g0112（1 列）
- 見出し：Date of Meeting
- 例1 値：Oct-10 | Dec-10 | Dec-10 | Dec-10 | Dec-10
  - 同じ表の列：Minister, Purpose of Meeting

## g0113（1 列）
- 見出し：Purpose of Meeting
- 例1 値：Catch up meeting | Catch up meeting | General discussion | Introductory meeting | General discussion
  - 同じ表の列：Minister, Date of Meeting

## g0114（1 列）
- 見出し：Department
- 例1 値：Ministry of Defence - DSTL | Ministry of Defence - Centre - SPVA | Ministry of Defence - Centre - SPVA | Ministry of Defence - Centre - SPVA | Ministry of Defence - Met Off
  - 同じ表の列：Net Present Value (…, Basis for Exception, Date

## g0115（1 列）
- 見出し：Net Present Value (?)
- 例1 値：2,286,000 | 37,628,000 | 39,225,000 | 10,570,000 | 69,300,000
  - 同じ表の列：Department, Basis for Exception, Date

## g0116（1 列）
- 見出し：Basis for Exception
- 例1 値：a delay would stop or directly impact d… | a delay would stop or directly impact d… | a delay would stop or directly impact d… | the new spend/contract needs to be appr… | a delay would stop or directly impact d…
  - 同じ表の列：Department, Net Present Value (…, Date

## g0117（1 列）
- 見出し：Date
- 例1 値：Oct | Nov | Oct | Aug | Oct
  - 同じ表の列：Department, Net Present Value (…, Basis for Exception

## g0118（1 列）
- 見出し：Department Family
- 例1 値：Ministry of Justice | Ministry of Justice | Ministry of Justice | Ministry of Justice | Ministry of Justice
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Transaction Number, Amount, Supplier Type, Project Code

## g0119（1 列）
- 見出し：Entity
- 例1 値：HMCTS | MoJ HQ | HMCTS | MoJ HQ | HMCTS
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Transaction Number, Amount, Supplier Type, Project Code

## g0120（1 列）
- 見出し：Date
- 例1 値：27-Jul-12 | 02-Jul-12 | 31-Jul-12 | 09-Jul-12 | 23-Jul-12
  - 同じ表の列：Department Family, Entity, Expense Type, Expense Area, Transaction Number, Amount, Supplier Type, Project Code

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
