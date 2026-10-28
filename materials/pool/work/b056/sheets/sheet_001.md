# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（5 列）
- 見出し：Funding agency
- 例1 値：DETSI | DETSI | DETSI | DETSI | DETSI
  - 同じ表の列：Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1, Client group2
- 例2 値：DHPW | DHPW | DHPW | DHPW | DHPW
  - 同じ表の列：Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0002（1 列）
- 見出し：Program title
- 例1 値：Growing the Recovery of Organic Waste v… | Science into Industry | Great Barrier Reef Marine Park Authorit… | 2026 NRL Magic Round Tech Showcase | Innovation Events Fund
  - 同じ表の列：Funding agency, Sub-program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0003（1 列）
- 見出し：Sub-program title
- 例1 値：Regional University Industry Collaborat… | Advancing Sustainable Visitor Managemen… | Queensland-Germany Bioeconomy Collabora… | Eastern Kuku Yalanji Return to Country … | Round 9
  - 同じ表の列：Funding agency, Program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0004（1 列）
- 見出し：Purpose
- 例1 値：WTMA has a collaborative project agreem… | Reduced fees for protected plant growin… | The Queensland–Bavaria Collaborative Re… | This challenge seeks proposals from inn… | This funding supports growing Queenslan…
  - 同じ表の列：Funding agency, Program title, Sub-program title, Category1, Category2, Category3, Client group1, Client group2

## g0005（3 列）
- 見出し：Category1
- 例1 値：Environment, land and water | Environment, land and water | Business and industry | Employment and jobs | Environment, land and water
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category2, Category3, Client group1, Client group2
- 例2 値：Employment and jobs | Employment and jobs | Employment and jobs | Environment, land and water | Business and industry
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category2, Client group1, Client group2, Client group3

## g0006（1 列）
- 見出し：Category2
- 例1 値：Aboriginal and Torres Strait Islander p… | Community support | Business and industry | Community support | Environment, land and water
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category3, Client group1, Client group2

## g0007（1 列）
- 見出し：Category3
- 例1 値：Employment and jobs | Education and training
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2

## g0008（1 列）
- 見出し：Client group1
- 例1 値：All Queenslanders | Non-government organisations | Women | Aboriginal and Torres Strait Islanders | Researchers/research institutes
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group2

## g0009（3 列）
- 見出し：Client group2
- 例1 値：Local government | Community groups | Primary industry | Teachers | Businesses
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1
- 例2 値：Families | All Queenslanders | Families | Families | Families
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1

## g0010（1 列）
- 見出し：Client group3
- 例1 値：Non-government organisations | Community groups | Rural communities | Researchers/research institutes | Individuals
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1

## g0011（1 列）
- 見出し：Program title
- 例1 値：Government managed housing rental rebate | RentConnect Tenancy Assistance | Youth Foyer | Bond Loans | Home Assist Secure
  - 同じ表の列：Funding agency, Sub-program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0012（1 列）
- 見出し：Sub-program title
- 例1 値：A range of loan products are available …
  - 同じ表の列：Funding agency, Program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0013（1 列）
- 見出し：Purpose
- 例1 値：A Rental Grant is a once only, non-repa… | Helping eligible people over 60, or who… | The Government managed housing rental r… | Registered providers deliver transition… | A Bond Loan is an interest-free loan to…
  - 同じ表の列：Funding agency, Program title, Sub-program title, Category1, Category2, Category3, Client group1, Client group2

## g0014（1 列）
- 見出し：Category1
- 例1 値：Homes and housing | Homes and housing | Homes and housing | Homes and housing | Homes and housing
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category2, Category3, Client group1, Client group2

## g0015（1 列）
- 見出し：Category2
- 例1 値：Parents and families | Community support | People with disability | Community support | Community support
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category3, Client group1, Client group2

## g0016（1 列）
- 見出し：Category3
- 例1 値：Community support
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2

## g0017（1 列）
- 見出し：Client group1
- 例1 値：Low-income earners | Low-income earners | Low-income earners | Low-income earners | Low-income earners
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group2

## g0018（1 列）
- 見出し：Assistance type1
- 例1 値：Grant | Grant | Loan | Loan | Frontline service procurement
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1

## g0019（1 列）
- 見出し：Program title
- 例1 値：Blue Card services | Linkage Program | Legal Assistance Services | Community Justice Group Program (CJG) | Gambling Community Benefit Fund
  - 同じ表の列：Funding agency, Sub-program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0020（1 列）
- 見出し：Sub-program title
- 例1 値：Aboriginal and Torres Strait Islander L… | Dispute resolution | Legal Aid Queensland | Civil Court Fees | Free Will Making
  - 同じ表の列：Funding agency, Program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0021（1 列）
- 見出し：Purpose
- 例1 値：The program provides grant funding for … | Civil Court Fees for the Supreme, Distr… | Annual contribution for Criminology Res… | Contribution to the Australia and New Z… | To promote national and international r…
  - 同じ表の列：Funding agency, Program title, Sub-program title, Category1, Category2, Category3, Client group1, Client group2

## g0022（1 列）
- 見出し：Category1
- 例1 値：Community support | Victims, crime and the law | Community support | Victims, crime and the law | Victims, crime and the law
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category2, Category3, Client group1, Client group2

## g0023（1 列）
- 見出し：Category2
- 例1 値：Community support | Victims, crime and the law | Community support | Community support | Aboriginal and Torres Strait Islander p…
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category3, Client group1, Client group2

## g0024（1 列）
- 見出し：Category3
- 例1 値：Victims, crime and the law | Aboriginal and Torres Strait Islander p… | Community support | Aboriginal and Torres Strait Islander p…
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2

## g0025（1 列）
- 見出し：Client group1
- 例1 値：All Queenslanders | Non-government organisations | All Queenslanders | All Queenslanders | Community groups
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group2

## g0026（1 列）
- 見出し：Client group2
- 例1 値：Aboriginal and Torres Strait Islanders | Community groups
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1

## g0027（2 列）
- 見出し：Client group3
- 例1 値：Community groups
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1
- 例2 値：Rural communities
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2

## g0028（1 列）
- 見出し：Finanical Year
- 例1 値：Petroleum | Mineral | Petroleum | Mineral | Petroleum
  - 同じ表の列：None, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0029（1 列）
- 見出し：None
- 例1 値：GL | PSL | DAA | PFL | PL
  - 同じ表の列：Finanical Year, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0030（1 列）
- 見出し：2015-16
- 例1 値：263 | 4 | 21 | 31 | 7
  - 同じ表の列：Finanical Year, None, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0031（1 列）
- 見出し：2016-17
- 例1 値：21 | 7 | 312 | 2 | 32
  - 同じ表の列：Finanical Year, None, 2015-16, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0032（1 列）
- 見出し：2017-18
- 例1 値：6 | 1 | 7 | 24 | 18
  - 同じ表の列：Finanical Year, None, 2015-16, 2016-17, 2018-19, 2019-20, 2020-21, 2021-22

## g0033（1 列）
- 見出し：2018-19
- 例1 値：312 | 2 | 7 | 20 | 114
  - 同じ表の列：Finanical Year, None, 2015-16, 2016-17, 2017-18, 2019-20, 2020-21, 2021-22

## g0034（1 列）
- 見出し：2019-20
- 例1 値：8 | 91 | 16 | 9 | 16
  - 同じ表の列：Finanical Year, None, 2015-16, 2016-17, 2017-18, 2018-19, 2020-21, 2021-22

## g0035（1 列）
- 見出し：2020-21
- 例1 値：6 | 40 | 1 | 12 | 346
  - 同じ表の列：Finanical Year, None, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2021-22

## g0036（1 列）
- 見出し：2021-22
- 例1 値：2 | 63 | 3 | 34 | 257
  - 同じ表の列：Finanical Year, None, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21

## g0037（1 列）
- 見出し：2022-23
- 例1 値：40 | 1 | 9 | 294 | 2
  - 同じ表の列：Finanical Year, None, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21

## g0038（1 列）
- 見出し：Program title
- 例1 値：Natural Resources Recovery Program | Collaborative Exploration Initiative Ex… | Drought Assistance Programs | Transforming Queensland Manufacturing G… | Manufacturing Energy Efficiency Grant P…
  - 同じ表の列：Funding agency, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2, Client group3

## g0039（1 列）
- 見出し：Sub-program title
- 例1 値：Round 4 | Land Rental Rebates | Round 2 | Round 1 | Collaborative Exploration Initiative Gr…
  - 同じ表の列：Funding agency, Program title, Purpose, Category1, Category2, Client group1, Client group2, Client group3

## g0040（1 列）
- 見出し：Purpose
- 例1 値：Made in Queensland provides funding bet… | The Geological Survey of Queensland (GS… | As part of the government's drought ass… | The new Transforming Queensland Manufac… | The Manufacturing Energy Efficiency Gra…
  - 同じ表の列：Funding agency, Program title, Sub-program title, Category1, Category2, Client group1, Client group2, Client group3

## g0041（1 列）
- 見出し：Category2
- 例1 値：Business and industry | Business and industry | Business and industry | Business and industry | Business and industry
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Client group1, Client group2, Client group3

## g0042（1 列）
- 見出し：Client group1
- 例1 値：Businesses | Businesses | Primary industry | Businesses | Businesses
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group2, Client group3

## g0043（1 列）
- 見出し：Client group2
- 例1 値：Landholders
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group3

## g0044（1 列）
- 見出し：Client group4
- 例1 値：Aboriginal and Torres Strait Islanders
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2

## g0045（1 列）
- 見出し：Title
- 例1 値：Key Map Queensland 2 Mile and 4 Mile Se… | Key Map County 2 mile and 4 Mile First … | Key Map Kennedy District 2 Mile JG1 ser… | Key Map Wide Bay District 2 Mile DG2 se… | Key Map Queensland 2 Mile and 4 Mile Se…
  - 同じ表の列：Publication Date, Map Scale, Map preview, Map preview filesiz…, Download link, Download filesize (…, Download Format, Copyright status

## g0046（1 列）
- 見出し：Publication Date
- 例1 値：1907 | 2010 | 1923 | 0 | 0
  - 同じ表の列：Title, Map Scale, Map preview, Map preview filesiz…, Download link, Download filesize (…, Download Format, Copyright status

## g0047（1 列）
- 見出し：Map Scale
- 例1 値：1013760 | 0 | 0 | 0 | 6336000
  - 同じ表の列：Title, Publication Date, Map preview, Map preview filesiz…, Download link, Download filesize (…, Download Format, Copyright status

## g0048（1 列）
- 見出し：Map preview
- 例1 値：https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat…
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview filesiz…, Download link, Download filesize (…, Download Format, Copyright status

## g0049（1 列）
- 見出し：Map preview filesize (Megabytes)
- 例1 値：0.27 | 0.32 | 0.2 | 0.25 | 0.25
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Download link, Download filesize (…, Download Format, Copyright status

## g0050（1 列）
- 見出し：Download link
- 例1 値：https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat…
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Map preview filesiz…, Download filesize (…, Download Format, Copyright status

## g0051（1 列）
- 見出し：Download filesize (Megabytes)
- 例1 値：2.17 | 6.43 | 2.93 | 1.06 | 4.06
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Map preview filesiz…, Download link, Download Format, Copyright status

## g0052（1 列）
- 見出し：Download Format
- 例1 値：Digital format: image---jpeg Original f… | Digital format: image---jpeg Original f… | Digital format: image---jpeg Original f… | Digital format: image---jpeg Original f… | Digital format: image---jpeg Original f…
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Map preview filesiz…, Download link, Download filesize (…, Copyright status

## g0053（1 列）
- 見出し：Copyright status
- 例1 値：CREATIVE COMMONS ATTRIBUTION | The copyright on this product has expir… | CREATIVE COMMONS ATTRIBUTION | The copyright on this product has expir… | The copyright on this product has expir…
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Map preview filesiz…, Download link, Download filesize (…, Download Format

## g0054（1 列）
- 見出し：Conditions of Use
- 例1 値：The copyright on this product has expir… | The copyright on this product has expir… | This material is licensed under Creativ… | The copyright on this product has expir… | The copyright on this product has expir…
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Map preview filesiz…, Download link, Download filesize (…, Download Format

## g0055（2 列）
- 見出し：Year
- 例1 値：2010-11 | 2014-15 | 2024-25 | 2017-18 | 2023-24
  - 同じ表の列：Percentage complete…, Target
- 例2 値：2010-11 | 2021-22 | 2012-13 | 2014-15 | 2015-16
  - 同じ表の列：Percentage complete…, Target

## g0056（2 列）
- 見出し：Percentage completed within target
- 例1 値：92% | 88% | 86% | 69% | 79%
  - 同じ表の列：Year, Target
- 例2 値：93% | 85% | 81% | 94% | 89%
  - 同じ表の列：Year, Target

## g0057（2 列）
- 見出し：Target
- 例1 値：>= 80% completed within 90 days | >= 80% completed within 90 days | >= 80% completed within 90 days | >= 80% completed within 90 days | >= 80% completed within 90 days
  - 同じ表の列：Year, Percentage complete…
- 例2 値：>= 80% completed within 90 days | >= 80% completed within 90 days | >= 80% completed within 90 days | >= 80% completed within 90 days | >= 80% completed within 90 days
  - 同じ表の列：Year, Percentage complete…

## g0058（1 列）
- 見出し：Program title
- 例1 値：Rail Concession Scheme | Regional Freight and Livestock | Long Distance Coach | IMove | Passenger Transport Infrastructure Inve…
  - 同じ表の列：Funding agency, Sub-program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0059（1 列）
- 見出し：Sub-program title
- 例1 値：Learner Driver Mentor Program | Specialist School Transport replacement… | Also referred to as Public Transport Co… | Emergency Response Fund Recovery and Re… | Active Transport Grants Program
  - 同じ表の列：Funding agency, Program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0060（1 列）
- 見出し：Purpose
- 例1 値：This funding is to support the reductio… | This funding is to support the planning… | Payments to bus operators to deliver ra… | The Department of Transport and Main Ro… | The off-network projects program is des…
  - 同じ表の列：Funding agency, Program title, Sub-program title, Category1, Category2, Category3, Client group1, Client group2

## g0061（1 列）
- 見出し：Category2
- 例1 値：Business and industry | Community support | Transport and motoring | Emergency services and safety | Community support
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category3, Client group1, Client group2

## g0062（1 列）
- 見出し：Category3
- 例1 値：Community support | Recreation, sport and arts | Community support | Health and wellbeing | Health and wellbeing
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2

## g0063（1 列）
- 見出し：Client group1
- 例1 値：Public transport users | Taxi drivers and passengers | Individuals | All Queenslanders | Rural communities
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group2

## g0064（1 列）
- 見出し：Client group3
- 例1 値：All Queenslanders | Motorists | Motorists | Local government | Motorists
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1

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
```
