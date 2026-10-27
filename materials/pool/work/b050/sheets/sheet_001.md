# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Suburb
- 例1 値：BIGGERA WATERS | BIGGERA WATERS | BENOWA | BIGGERA WATERS | BROADBEACH
  - 同じ表の列：Device Status, Installation Date, Decommission Date, Protection Type, Manufacturer Code, Model, Device Size

## g0002（1 列）
- 見出し：Device Status
- 例1 値：REGISTERED | HISTORIC | REGISTERED | HISTORIC | HISTORIC
  - 同じ表の列：Suburb, Installation Date, Decommission Date, Protection Type, Manufacturer Code, Model, Device Size

## g0003（1 列）
- 見出し：Installation Date
- 例1 値：17/03/2007 | 6/09/2002 | 6/06/2005 | 29/07/2002 | 2/03/2011
  - 同じ表の列：Suburb, Device Status, Decommission Date, Protection Type, Manufacturer Code, Model, Device Size

## g0004（1 列）
- 見出し：Decommission Date
- 例1 値：3/04/2007 | 24/09/2009 | 28/04/2014 | 21/05/2008 | 23/09/2009
  - 同じ表の列：Suburb, Device Status, Installation Date, Protection Type, Manufacturer Code, Model, Device Size

## g0005（1 列）
- 見出し：Protection Type
- 例1 値：INDIVIDUAL | INDIVIDUAL | CONTAINMENT | CONTAINMENT | ZONED
  - 同じ表の列：Suburb, Device Status, Installation Date, Decommission Date, Manufacturer Code, Model, Device Size

## g0006（1 列）
- 見出し：Manufacturer Code
- 例1 値：WATTS | VALVETEC | CONBRACO | VALVETEC | FEBCO
  - 同じ表の列：Suburb, Device Status, Installation Date, Decommission Date, Protection Type, Model, Device Size

## g0007（1 列）
- 見出し：Model
- 例1 値：765 | PJ9483 | RP1097 | 009 | 860
  - 同じ表の列：Suburb, Device Status, Installation Date, Decommission Date, Protection Type, Manufacturer Code, Device Size

## g0008（1 列）
- 見出し：Device Size
- 例1 値：20 | 20 | 20 | 20 | 20
  - 同じ表の列：Suburb, Device Status, Installation Date, Decommission Date, Protection Type, Manufacturer Code, Model

## g0009（1 列）
- 見出し：MAKE_DESC
- 例1 値：AIR RIDE | ALDOM | ALFA ROMEO | ALDOM | ALFA ROMEO
  - 同じ表の列：BODY_TYPE_DESC, YEAR_OF_MANUFACTURE, COLOUR_DESC, TOTAL

## g0010（1 列）
- 見出し：BODY_TYPE_DESC
- 例1 値：TANKER TRAILER | TRAILER | LAND IMPLEMENT VEHICLE | SEDAN | TRAILER
  - 同じ表の列：MAKE_DESC, YEAR_OF_MANUFACTURE, COLOUR_DESC, TOTAL

## g0011（1 列）
- 見出し：YEAR_OF_MANUFACTURE
- 例1 値：2002 | 2017 | 2008 | 2001 | 2018
  - 同じ表の列：MAKE_DESC, BODY_TYPE_DESC, COLOUR_DESC, TOTAL

## g0012（1 列）
- 見出し：COLOUR_DESC
- 例1 値：SILVER | BLUE | BLACK | SILVER | RED
  - 同じ表の列：MAKE_DESC, BODY_TYPE_DESC, YEAR_OF_MANUFACTURE, TOTAL

## g0013（1 列）
- 見出し：TOTAL
- 例1 値：2 | 1 | 1 | 4 | 1
  - 同じ表の列：MAKE_DESC, BODY_TYPE_DESC, YEAR_OF_MANUFACTURE, COLOUR_DESC

## g0014（1 列）
- 見出し：Publisher Title
- 例1 値：City of Salisbury Council | SA Country Fire Service | Environment Protection Authority (EPA) | State Library of South Australia | ABS (SA Data)
  - 同じ表の列：Views, Visits

## g0015（1 列）
- 見出し：Views
- 例1 値：11091 | 1958 | 3648 | 440 | 1622
  - 同じ表の列：Publisher Title, Visits

## g0016（1 列）
- 見出し：Visits
- 例1 値：2749 | 18 | 36 | 58 | 11
  - 同じ表の列：Publisher Title, Views

## g0017（1 列）
- 見出し：PROPERTY_INDEX
- 例1 値：Hutchins School | Hutchins School | Hutchins School | Hutchins School | Hutchins School
  - 同じ表の列：FATHER, AGE, ADMISS_DATE, YEAR, PROPERTY, MOTHER

## g0018（1 列）
- 見出し：FATHER
- 例1 値：Goldie, A. | Evans, G.F | Clerke, Alexander | Jones, A.B. | Kenny, Luke
  - 同じ表の列：PROPERTY_INDEX, AGE, ADMISS_DATE, YEAR, PROPERTY, MOTHER

## g0019（1 列）
- 見出し：AGE
- 例1 値：12 | 11 | 14 | 9 | 14
  - 同じ表の列：PROPERTY_INDEX, FATHER, ADMISS_DATE, YEAR, PROPERTY, MOTHER

## g0020（1 列）
- 見出し：ADMISS_DATE
- 例1 値：22 Jul 1850 | 5 Feb 1877 | 07 Oct 1852 | 17 Jul 1886 | 30 Jan 1877
  - 同じ表の列：PROPERTY_INDEX, FATHER, AGE, YEAR, PROPERTY, MOTHER

## g0021（1 列）
- 見出し：YEAR
- 例1 値：1861 | 1852 | 1850 | 1854 | 1886
  - 同じ表の列：PROPERTY_INDEX, FATHER, AGE, ADMISS_DATE, PROPERTY, MOTHER

## g0022（1 列）
- 見出し：PROPERTY
- 例1 値：Hutchins School | Hutchins School | Hutchins School | Hutchins School | Hutchins School
  - 同じ表の列：PROPERTY_INDEX, FATHER, AGE, ADMISS_DATE, YEAR, MOTHER

## g0023（1 列）
- 見出し：MOTHER
- 例1 値：Clarke, T. B. | Douglas, A.C | Hogg, T.
  - 同じ表の列：PROPERTY_INDEX, FATHER, AGE, ADMISS_DATE, YEAR, PROPERTY

## g0024（1 列）
- 見出し：School ID
- 例1 値：2472 | 3060 | 7444 | 1495 | 8202
  - 同じ表の列：Gazetted significan…, s170 SHI ID #, Suburb, Post code, LGA

## g0025（1 列）
- 見出し：Gazetted significance
- 例1 値：Local | Local | Local | State | Local
  - 同じ表の列：School ID, s170 SHI ID #, Suburb, Post code, LGA

## g0026（1 列）
- 見出し：s170 SHI ID #
- 例1 値：5064512 | 5065747 | 5065634 | 5067905 | 5064435
  - 同じ表の列：School ID, Gazetted significan…, Suburb, Post code, LGA

## g0027（3 列）
- 見出し：Suburb
- 例1 値：Greystanes | Eastwood | Lithgow | Roseville | Narrandera
  - 同じ表の列：School ID, Gazetted significan…, s170 SHI ID #, Post code, LGA
- 例2 値：Lawnton | Urraween | Bundaberg | Bundaberg | Kingaroy
  - 同じ表の列：Title, Website

## g0028（1 列）
- 見出し：Post code
- 例1 値：2096 | 2576 | 2142 | 2581 | 2040
  - 同じ表の列：School ID, Gazetted significan…, s170 SHI ID #, Suburb, LGA

## g0029（1 列）
- 見出し：LGA
- 例1 値：CESSNOCK | SNOWY MONARO REGIONAL | SINGLETON | CENTRAL COAST | BLUE MOUNTAINS
  - 同じ表の列：School ID, Gazetted significan…, s170 SHI ID #, Suburb, Post code

## g0030（1 列）
- 見出し：Agency (Dept or Stat Body)
- 例1 値：GCHHS | GCHHS | GCHHS | GCHHS | GCHHS
  - 同じ表の列：Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract, Number of offers so…

## g0031（1 列）
- 見出し：Award contract date
- 例1 値：25/07/2025 | 9/10/2025 | 28/08/2025 | 28/07/2025 | 18/12/2025
  - 同じ表の列：Agency (Dept or Sta…, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract, Number of offers so…

## g0032（1 列）
- 見出し：Contract value
- 例1 値：$100,001.55 | $423,535.42 | $1,348,307.00 | $148,302.00 | $33,000.00
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract, Number of offers so…

## g0033（1 列）
- 見出し：Variation to contract (Yes/No)
- 例1 値：No | N | Y | No | N
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract, Number of offers so…

## g0034（1 列）
- 見出し：Specific confidentiality provision used
- 例1 値：N | No | No | No | N
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Procurement method, Reason for use of l…, Form of contract, Number of offers so…

## g0035（1 列）
- 見出し：Procurement method
- 例1 値：Open | Limited | Open | Open | Limited
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Reason for use of l…, Form of contract, Number of offers so…

## g0036（1 列）
- 見出し：Reason for use of limited tendering
- 例1 値：b - (i) The requirement is a work of ar… | Specialised vendor these requirement | Variation to current contract | Variation to current contract | SOLE SOURCE AS PER TGA GUIDELINES
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Form of contract, Number of offers so…

## g0037（1 列）
- 見出し：Form of contract
- 例1 値：SERVICE AGREEMENT | Service Contract | SERVICE AGREEMENT | SERVICE AGREEMENT
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Number of offers so…

## g0038（1 列）
- 見出し：Number of offers sought
- 例1 値：16
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract

## g0039（1 列）
- 見出し：Evaluation criteria and weightings
- 例1 値：Company Overview, Differentiating Facto…
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract

## g0040（1 列）
- 見出し：Title
- 例1 値：Queensland Motorcycle School | Top Rider GC | Motorcycle Masters Riding School | Coastal Motorcycle Training | Stay Upright
  - 同じ表の列：Suburb, Website

## g0041（1 列）
- 見出し：Website
- 例1 値：[Sunshine Coast Motorcycle Rider Traini… | [AMT Australian Motorcycle Training web… | [Sunshine Coast Motorcycle Rider Traini… | [Learn 2 Ride website](http://www.learn… | [Southern Downs Rider Training](https:/…
  - 同じ表の列：Title, Suburb

## g0042（1 列）
- 見出し：Transaction Type
- 例1 値：Registration New Business | Registration New Business | Registration New Business | Registration New Business | Registration New Business
  - 同じ表の列：Suburb, Valid Handled Trans…

## g0043（1 列）
- 見出し：Valid Handled Transactions
- 例1 値：1 | 5 | 1 | 4 | 1
  - 同じ表の列：Suburb, Transaction Type

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
```
