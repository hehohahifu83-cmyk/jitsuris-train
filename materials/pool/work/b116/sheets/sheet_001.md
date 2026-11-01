# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Year 1
- 例1 値：21 | 12 | 18 | 6 | 18
  - 同じ表の列：Year 2, Year 3, Year 4, Year 5, Total all years

## g0002（1 列）
- 見出し：Year 2
- 例1 値：12 | 20 | 4 | 1 | 17
  - 同じ表の列：Year 1, Year 3, Year 4, Year 5, Total all years

## g0003（1 列）
- 見出し：Year 3
- 例1 値：15 | 1 | 13 | 111 | 17
  - 同じ表の列：Year 1, Year 2, Year 4, Year 5, Total all years

## g0004（1 列）
- 見出し：Year 4
- 例1 値：14 | 12 | 102 | 10 | 10
  - 同じ表の列：Year 1, Year 2, Year 3, Year 5, Total all years

## g0005（1 列）
- 見出し：Year 5
- 例1 値：19 | 14 | 5 | 14 | 11
  - 同じ表の列：Year 1, Year 2, Year 3, Year 4, Total all years

## g0006（1 列）
- 見出し：Total all years
- 例1 値：397 | 4 | 39 | 19 | 84
  - 同じ表の列：Year 1, Year 2, Year 3, Year 4, Year 5

## g0007（1 列）
- 見出し：Ongoing employees
- 例1 値：5 | 8835 | 8936 | 8936 | Employees
  - 同じ表の列：Fixed term and casu…

## g0008（1 列）
- 見出し：Fixed term and casual employees
- 例1 値：FTE | FTE | 78 | 2557 | 274
  - 同じ表の列：Ongoing employees

## g0009（1 列）
- 見出し：Human Services
- 例1 値：Central business district | Property portfolio water use | In 2013–14, the total waste generated a… | Compost | Landfill
  - 同じ表の列：Government owned bu…, Leased buildings, Total

## g0010（1 列）
- 見出し：Government owned buildings
- 例1 値：106438 | 31 | 8573 | Tonnes CO2-e | 470221
  - 同じ表の列：Human Services, Leased buildings, Total

## g0011（1 列）
- 見出し：Leased buildings
- 例1 値：16004914 | 2013–14 | kilograms/year | 104107 | 2013–14 estimated
  - 同じ表の列：Human Services, Government owned bu…, Total

## g0012（1 列）
- 見出し：Total
- 例1 値：131823 | 478423007 | 41916956 | 16417306 | 5603
  - 同じ表の列：Human Services, Government owned bu…, Leased buildings

## g0013（1 列）
- 見出し：id
- 例1 値：CHH_00628 | GTH_PS0820 | LFH_00474 | HBFH_14151 | HBFH_09019
  - 同じ表の列：Object, Titles, Institution, image, Format, Creator(s), Date, Subjects

## g0014（1 列）
- 見出し：Object
- 例1 値：gravestones | war memorials | gravestones | gravestones | gravestones
  - 同じ表の列：id, Titles, Institution, image, Format, Creator(s), Date, Subjects

## g0015（1 列）
- 見出し：Titles
- 例1 値：Gravestone of Ivy May WALKER | Diaries of Malcolm Laing Smith | Headstone of Vera Mary STOKES | Headstone of Lily May Mulibah KEMBLING | Headstone of Sarah FERGUSON
  - 同じ表の列：id, Object, Institution, image, Format, Creator(s), Date, Subjects

## g0016（1 列）
- 見出し：Institution
- 例1 値：Tasmanian Family History Society Inc. H… | Tasmanian Family History Society Inc. D… | Tasmanian Family History Society Inc. D… | Tasmanian Family History Society Inc. D… | Tasmanian Family History Society Inc. L…
  - 同じ表の列：id, Object, Titles, image, Format, Creator(s), Date, Subjects

## g0017（1 列）
- 見出し：image
- 例1 値：https://stors.tas.gov.au/LFH_08581_w | https://stors.tas.gov.au/LFH_Ellesmere%… | https://stors.tas.gov.au/LFH_19300_w | https://stors.tas.gov.au/LFH_28471_w | https://stors.tas.gov.au/DFH_04861_1_w
  - 同じ表の列：id, Object, Titles, Institution, Format, Creator(s), Date, Subjects

## g0018（1 列）
- 見出し：Format
- 例1 値：Monuments and Historical sites | Monuments and Historical sites | Monuments and Historical sites | Pictorial and artistic works | Monuments and Historical sites
  - 同じ表の列：id, Object, Titles, Institution, image, Creator(s), Date, Subjects

## g0019（1 列）
- 見出し：Creator(s)
- 例1 値：unknown | Hart, Miss Margaret | Glamorgan-Spring Bay Historical Society | TAFT | New Norfolk Camera Club
  - 同じ表の列：id, Object, Titles, Institution, image, Format, Date, Subjects

## g0020（1 列）
- 見出し：Date
- 例1 値：tools | 1865 - | 1900 - | 1800 - | 1800 -
  - 同じ表の列：id, Object, Titles, Institution, image, Format, Creator(s), Subjects

## g0021（1 列）
- 見出し：Subjects
- 例1 値：portraits; clothing; women; children | hop-pickers | creeks | processions; coronations; cadets; float… | tableware; eating & drinking apparatus;…
  - 同じ表の列：id, Object, Titles, Institution, image, Format, Creator(s), Date

## g0022（1 列）
- 見出し：Places
- 例1 値：Wynyard, Tasmania | North East Tasmania | Circular Head, Tasmania | Smithton, Tasmania | Wynyard, Tasmania
  - 同じ表の列：id, Object, Titles, Institution, image, Format, Creator(s), Date

## g0023（1 列）
- 見出し：class_code
- 例1 値：-999 | 999 | 8 | 5 | 6
  - 同じ表の列：class_desc, _id, WKT_Geometry

## g0024（1 列）
- 見出し：class_desc
- 例1 値：permanently not suitable | 60% suitability | 70% suitability | temporarily not suitable | 50% suitability
  - 同じ表の列：class_code, _id, WKT_Geometry

## g0025（1 列）
- 見出し：_id
- 例1 値：3 | 6 | 5 | 2 | 4
  - 同じ表の列：class_code, class_desc, WKT_Geometry

## g0026（1 列）
- 見出し：WKT_Geometry
- 例1 値：MULTIPOLYGON (((142.1034339670484 -37.1… | MULTIPOLYGON (((142.53475144388412 -37.… | GEOMETRYCOLLECTION (POLYGON ((141.85716… | GEOMETRYCOLLECTION (POLYGON ((141.64069… | MULTIPOLYGON (((142.5141317528574 -37.6…
  - 同じ表の列：class_code, class_desc, _id

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
```
