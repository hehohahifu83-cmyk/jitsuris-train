# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Type
- 例1 値：ER - Compliance notice | ER - Compliance notice | ER - Compliance notice | ER - Revocation of registration | ER - Revocation of registration
  - 同じ表の列：Date effective from, Date no longer in f…, ABN, City, State, Other relevant info, Registration Groups

## g0002（1 列）
- 見出し：Date effective from
- 例1 値：2026-05-12T07:00:00 | 2026-09-29T07:00:00 | 2026-05-06T07:00:00 | 2026-07-13T07:00:00 | 2026-06-02T07:00:00
  - 同じ表の列：Type, Date no longer in f…, ABN, City, State, Other relevant info, Registration Groups

## g0003（1 列）
- 見出し：Date no longer in force
- 例1 値：2028-07-21T07:00:00 | 2026-09-04T07:00:00 | 2026-09-04T07:00:00 | 2026-09-04T07:00:00 | 2026-09-04T07:00:00
  - 同じ表の列：Type, Date effective from, ABN, City, State, Other relevant info, Registration Groups

## g0004（1 列）
- 見出し：ABN
- 例1 値：35678091088 | 17663066242 | 95673504295 | 96678153716 | 67085903407
  - 同じ表の列：Type, Date effective from, Date no longer in f…, City, State, Other relevant info, Registration Groups

## g0005（1 列）
- 見出し：City
- 例1 値：Cheltenham | ACACIA RIDGE | Greenwith | YAGOONA | WANGARATTA
  - 同じ表の列：Type, Date effective from, Date no longer in f…, ABN, State, Other relevant info, Registration Groups

## g0006（1 列）
- 見出し：State
- 例1 値：QLD | NT | NSW | NSW | QLD
  - 同じ表の列：Type, Date effective from, Date no longer in f…, ABN, City, Other relevant info, Registration Groups

## g0007（1 列）
- 見出し：Other relevant info
- 例1 値：and ABN 23458011874
  - 同じ表の列：Type, Date effective from, Date no longer in f…, ABN, City, State, Registration Groups

## g0008（1 列）
- 見出し：Registration Groups
- 例1 値：101 accommodation/tenancy assistance; 1… | 104 high intensity daily personal activ… | 102 assistance to access and maintain e… | 111 home modifications; 131 specialist … | 106 assistance in coordinating or manag…
  - 同じ表の列：Type, Date effective from, Date no longer in f…, ABN, City, State, Other relevant info

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
```
