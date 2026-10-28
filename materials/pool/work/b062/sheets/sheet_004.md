# ラベル用シート 004 / 004

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_004.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0361（1 列）
- 見出し：Expense Area
- 例1 値：Revenue Account For Year | Car Parks | Caravan Site | Printing Section | Business Support Community Services
  - 同じ表の列：Date, Transaction No., Amount, Expense Type, Expense Code, Service Area

## g0362（1 列）
- 見出し：Expense Type
- 例1 値：Advertising | NPS Planned Maintenance | Contract & Agency staff | Other Local Authorities | Economic Development Fund
  - 同じ表の列：Date, Transaction No., Amount, Expense Area, Expense Code, Service Area

## g0363（1 列）
- 見出し：Expense Code
- 例1 値：VGR2415257 | GHM1214918 | VGR2415257 | XPA5098021 | ERI3214694
  - 同じ表の列：Date, Transaction No., Amount, Expense Area, Expense Type, Service Area

## g0364（1 列）
- 見出し：Service Area
- 例1 値：Central Services | Housing Services | Highways & Transport Services | Parish CT Grant | Internal Trading Accounts
  - 同じ表の列：Date, Transaction No., Amount, Expense Area, Expense Type, Expense Code

## g0365（1 列）
- 見出し：EffectiveDate
- 例1 値：07/04/2017 | 07/04/2017 | 07/04/2017 | 07/04/2017 | 07/04/2017
  - 同じ表の列：OrganisationURI, ServiceCategoryLabel, ServiceCategoryURI, Licence, PropertyRef, Occupied, ExemptionDescription, MandatoryReliefDesc…

## g0366（1 列）
- 見出し：ServiceCategoryLabel
- 例1 値：Business rates account enquiries | Business rates account enquiries | Business rates account enquiries | Business rates account enquiries | Business rates account enquiries
  - 同じ表の列：OrganisationURI, EffectiveDate, ServiceCategoryURI, Licence, PropertyRef, Occupied, ExemptionDescription, MandatoryReliefDesc…

## g0367（1 列）
- 見出し：ServiceCategoryURI
- 例1 値：http://id.esd.org.uk/service/56 | http://id.esd.org.uk/service/56 | http://id.esd.org.uk/service/56 | http://id.esd.org.uk/service/56 | http://id.esd.org.uk/service/56
  - 同じ表の列：OrganisationURI, EffectiveDate, ServiceCategoryLabel, Licence, PropertyRef, Occupied, ExemptionDescription, MandatoryReliefDesc…

## g0368（1 列）
- 見出し：Licence
- 例1 値：http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/…
  - 同じ表の列：OrganisationURI, EffectiveDate, ServiceCategoryLabel, ServiceCategoryURI, PropertyRef, Occupied, ExemptionDescription, MandatoryReliefDesc…

## g0369（1 列）
- 見出し：PropertyRef
- 例1 値：0599181071000A | 0723350717000A | 02556795500005 | 02356100210002 | 00055806002121
  - 同じ表の列：OrganisationURI, EffectiveDate, ServiceCategoryLabel, ServiceCategoryURI, Licence, Occupied, ExemptionDescription, MandatoryReliefDesc…

## g0370（1 列）
- 見出し：Occupied
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：OrganisationURI, EffectiveDate, ServiceCategoryLabel, ServiceCategoryURI, Licence, PropertyRef, ExemptionDescription, MandatoryReliefDesc…

## g0371（1 列）
- 見出し：ExemptionDescription
- 例1 値：minrv | minrv | minrv | 3mths | 3
  - 同じ表の列：OrganisationURI, EffectiveDate, ServiceCategoryLabel, ServiceCategoryURI, Licence, PropertyRef, Occupied, MandatoryReliefDesc…

## g0372（1 列）
- 見出し：MandatoryReliefDescription
- 例1 値：Rural Public House Mandatory 50% | Post office Mandatory 50% | Post office Mandatory 50%
  - 同じ表の列：OrganisationURI, EffectiveDate, ServiceCategoryLabel, ServiceCategoryURI, Licence, PropertyRef, Occupied, ExemptionDescription

## g0373（1 列）
- 見出し：DiscretionaryReliefDescription
- 例1 値：Reoccupation Rate Relief 50% | Rural Relief | Rural Relief | Rural Relief
  - 同じ表の列：OrganisationURI, EffectiveDate, ServiceCategoryLabel, ServiceCategoryURI, Licence, PropertyRef, Occupied, ExemptionDescription

## g0374（1 列）
- 見出し：Expense Type
- 例1 値：Project Funding | Project Funding | Strategic/Core Funding | Project Funding | Research
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Transaction Number, Amount

## g0375（1 列）
- 見出し：Expense Area
- 例1 値：SSC Programme | SSC Programme | UKCES Programme | SSC Programme | SSC Programme
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Transaction Number, Amount

## g0376（1 列）
- 見出し：Supplier
- 例1 値：SKills for Health | Skills for Care & Development | Lifelong Learning UK | Skillset | Lifelong Learning UK
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount

## g0377（1 列）
- 見出し：Transaction Number
- 例1 値：April Retention | SI4 Initial Payment | SI3 Q4 Payment | 316LC2 | April Retention
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Amount

## g0378（1 列）
- 見出し：Amount
- 例1 値：167390 | 130335 | 29756 | 110344 | 72925
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number

## g0379（1 列）
- 見出し：Transaction Date
- 例1 値：8/30/2012 | 9/17/2012 | 9/14/2012 | 8/20/2012 | 8/24/2012
  - 同じ表の列：Transaction Referen…, Merchant, Total

## g0380（1 列）
- 見出し：Transaction Reference
- 例1 値：372158913 | 381748595 | 368963544 | PCCL1608191 | 378452072
  - 同じ表の列：Transaction Date, Merchant, Total

## g0381（1 列）
- 見出し：Merchant
- 例1 値：Hogg Robinson Group Ltd | Hogg Robinson Group Ltd | Hogg Robinson Group Ltd | Hogg Robinson Group Ltd | Hogg Robinson Group Ltd
  - 同じ表の列：Transaction Date, Transaction Referen…, Total

## g0382（1 列）
- 見出し：Total
- 例1 値：3225.69 | 686.89 | 4852.39 | 3235.39 | 2572.49
  - 同じ表の列：Transaction Date, Transaction Referen…, Merchant

## g0383（1 列）
- 見出し：Senior official (SCS2 and above)
- 例1 値：BOLTON/NICOLA MRS | JERMEY/DOMINIC MR | OWEN/JANE MS | ARCHER/NICHOLAS MR | JERMEY/DOMINIC MR
  - 同じ表の列：Start date of trip, Duration of Visit, Destination, Purpose of trip, Mode of transport, Class of travel, Accommodation/Meals, Other (including ho…

## g0384（1 列）
- 見出し：Start date of trip
- 例1 値：16/06/2015 | 14/06/2015 | 17/04/2015 | 15/06/2015 | 02/06/2015
  - 同じ表の列：Senior official (SC…, Duration of Visit, Destination, Purpose of trip, Mode of transport, Class of travel, Accommodation/Meals, Other (including ho…

## g0385（1 列）
- 見出し：Duration of Visit
- 例1 値：2 | 2 | 1 | 1 | 1
  - 同じ表の列：Senior official (SC…, Start date of trip, Destination, Purpose of trip, Mode of transport, Class of travel, Accommodation/Meals, Other (including ho…

## g0386（1 列）
- 見出し：Purpose of trip
- 例1 値：Visit Delhi and Bangalore to meet key c… | Paris Airshow 14-16 June | Introductory visit to the Gulf 18-21 May | Visiting Lockheed Martin - live fire on… | Visiting Lockheed Martin at Ampthill ne…
  - 同じ表の列：Senior official (SC…, Start date of trip, Duration of Visit, Destination, Mode of transport, Class of travel, Accommodation/Meals, Other (including ho…

## g0387（1 列）
- 見出し：Mode of transport
- 例1 値：TAXI/RAIL | RAIL | RAIL | TAXI | AIR/TAXI/PRIVATE CAR
  - 同じ表の列：Senior official (SC…, Start date of trip, Duration of Visit, Destination, Purpose of trip, Class of travel, Accommodation/Meals, Other (including ho…

## g0388（1 列）
- 見出し：Class of travel
- 例1 値：STANDARD | STANDARD | PREMIUM ECONOMY | STANDARD | STANDARD
  - 同じ表の列：Senior official (SC…, Start date of trip, Duration of Visit, Destination, Purpose of trip, Mode of transport, Accommodation/Meals, Other (including ho…

## g0389（1 列）
- 見出し：Accommodation/Meals
- 例1 値：」87.00 | 」97.28 | 」251.05 | 」233.89 | 」512.61
  - 同じ表の列：Senior official (SC…, Start date of trip, Duration of Visit, Destination, Purpose of trip, Mode of transport, Class of travel, Other (including ho…

## g0390（1 列）
- 見出し：Other (including hospitality given)
- 例1 値：」45.00 | 」231.05 | 」49.89 | 」45.34
  - 同じ表の列：Senior official (SC…, Start date of trip, Duration of Visit, Destination, Purpose of trip, Mode of transport, Class of travel, Accommodation/Meals

## g0391（1 列）
- 見出し：Total cost, including all visas, accommodation, travel, meal
- 例1 値：」112.28 | 」1,291.96 | 」207.40 | 」31.40 | 」49.60
  - 同じ表の列：Senior official (SC…, Start date of trip, Duration of Visit, Destination, Purpose of trip, Mode of transport, Class of travel, Accommodation/Meals

## g0392（1 列）
- 見出し：Type of hospitality received
- 例1 値：Lunch | Lunch | Lunch | Dinner | Lunch and Dinner
  - 同じ表の列：Senior Official (SC…, Date

## g0393（1 列）
- 見出し：OrganisationLabel
- 例1 値：Wirral | Wirral | Wirral | Wirral | Wirral
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0394（1 列）
- 見出し：SiteReference
- 例1 値：468 | 1878 | 3047 | 655400 | 2046
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0395（1 列）
- 見出し：GeoX
- 例1 値：331539 | 330693 | 330725 | 331423 | 332645
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoY, Hectares, Deliverable

## g0396（1 列）
- 見出し：GeoY
- 例1 値：387684 | 388726 | 389168 | 394168 | 386815
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, Hectares, Deliverable

## g0397（2 列）
- 見出し：Paid Date
- 例1 値：03/10/2022 | 21/10/2022 | 19/10/2022 | 22/10/2022 | 14/10/2022
  - 同じ表の列：Transaction Number, Paid Amount, Department, Cost Centre, Irrecoverable VAT, Merchant Category
- 例2 値：03/10/2022 | 31/10/2022 | 25/10/2022 | 26/10/2022 | 11/10/2022
  - 同じ表の列：Transaction Number, Paid Amount, Department, Cost Centre, Irrecoverable VAT

## g0398（1 列）
- 見出し：Paid Amount
- 例1 値：25.98 | 40.00 | 4.59 | 19.95 | 99.99
  - 同じ表の列：Transaction Number, Paid Date, Department, Cost Centre, Irrecoverable VAT, Merchant Category

## g0399（1 列）
- 見出し：Department
- 例1 値：Children's Services | Delivery Services | Neighbourhoods | Neighbourhoods | Children's Services
  - 同じ表の列：Transaction Number, Paid Date, Paid Amount, Cost Centre, Irrecoverable VAT, Merchant Category

## g0400（2 列）
- 見出し：Cost Centre
- 例1 値：E9061 | E6300 | L4970 | E9061 | L4973
  - 同じ表の列：Transaction Number, Paid Date, Paid Amount, Department, Irrecoverable VAT, Merchant Category
- 例2 値：S6167 | S5600 | H6080 | S6142 | P4090
  - 同じ表の列：Transaction Number, Paid Date, Paid Amount, Department, Irrecoverable VAT

## g0401（1 列）
- 見出し：Irrecoverable VAT
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Transaction Number, Paid Date, Paid Amount, Department, Cost Centre, Merchant Category

## g0402（1 列）
- 見出し：Merchant Category
- 例1 値：ADVERTISING SERVICES | ARTIST SUPPLY STORES, CRAFT SHOPS | DISCOUNT STORES | SERVICE STATIONS WITH OR WITHOUT ANCILL… | GROCERY STORES, SUPERMARKETS
  - 同じ表の列：Transaction Number, Paid Date, Paid Amount, Department, Cost Centre, Irrecoverable VAT

## g0403（1 列）
- 見出し：Paid Amount
- 例1 値：2,200.00 | 400.00 | 7,327.20 | 2,464.00 | 2,200.00
  - 同じ表の列：Transaction Number, Paid Date, Department, Cost Centre, Irrecoverable VAT

## g0404（1 列）
- 見出し：Department
- 例1 値：Adults Care and Health and Strategic Co… | Children, Families & Education | Children, Families & Education | Children, Families & Education | Adults Care and Health and Strategic Co…
  - 同じ表の列：Transaction Number, Paid Date, Paid Amount, Cost Centre, Irrecoverable VAT

## g0405（1 列）
- 見出し：Irrecoverable VAT
- 例1 値：15.58 | 15.58
  - 同じ表の列：Transaction Number, Paid Date, Paid Amount, Department, Cost Centre

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
```
