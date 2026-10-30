# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：ID
- 例1 値：12 | 4 | 14 | 8 | 7
  - 同じ表の列：Province/Territory, Program Stream, Jan-Mar2025, Apr-Jun2025, Jul-Sep2025, Oct-Dec2025, Jan-Mar2026, Apr-Jun2026

## g0002（1 列）
- 見出し：Province/Territory
- 例1 値：PE | QC | AB | NL | NT
  - 同じ表の列：ID, Program Stream, Jan-Mar2025, Apr-Jun2025, Jul-Sep2025, Oct-Dec2025, Jan-Mar2026, Apr-Jun2026

## g0003（1 列）
- 見出し：Program Stream
- 例1 値：Low Wage | Low Wage | Low Wage | Low Wage | Global Talent Stream
  - 同じ表の列：ID, Province/Territory, Jan-Mar2025, Apr-Jun2025, Jul-Sep2025, Oct-Dec2025, Jan-Mar2026, Apr-Jun2026

## g0004（1 列）
- 見出し：Jan-Mar2025
- 例1 値：2 | 69 | 3 | 1 | 40
  - 同じ表の列：ID, Province/Territory, Program Stream, Apr-Jun2025, Jul-Sep2025, Oct-Dec2025, Jan-Mar2026, Apr-Jun2026

## g0005（1 列）
- 見出し：Apr-Jun2025
- 例1 値：0 | 5 | 2,639 | 0 | 24
  - 同じ表の列：ID, Province/Territory, Program Stream, Jan-Mar2025, Jul-Sep2025, Oct-Dec2025, Jan-Mar2026, Apr-Jun2026

## g0006（1 列）
- 見出し：Jul-Sep2025
- 例1 値：93 | 0 | 3 | 0 | 0
  - 同じ表の列：ID, Province/Territory, Program Stream, Jan-Mar2025, Apr-Jun2025, Oct-Dec2025, Jan-Mar2026, Apr-Jun2026

## g0007（1 列）
- 見出し：Oct-Dec2025
- 例1 値：222 | 1,404 | 0 | 0 | 10
  - 同じ表の列：ID, Province/Territory, Program Stream, Jan-Mar2025, Apr-Jun2025, Jul-Sep2025, Jan-Mar2026, Apr-Jun2026

## g0008（1 列）
- 見出し：Jan-Mar2026
- 例1 値：650 | 10 | 1,073 | 5 | 0
  - 同じ表の列：ID, Province/Territory, Program Stream, Jan-Mar2025, Apr-Jun2025, Jul-Sep2025, Oct-Dec2025, Apr-Jun2026

## g0009（1 列）
- 見出し：Apr-Jun2026
- 例1 値：709 | 1,265 | 501 | 29 | 0
  - 同じ表の列：ID, Province/Territory, Program Stream, Jan-Mar2025, Apr-Jun2025, Jul-Sep2025, Oct-Dec2025, Jan-Mar2026

## g0010（1 列）
- 見出し：Station
- 例1 値：CY3 | LE7 | CN1 | ML3 | IK1
  - 同じ表の列：Location/Emplacement, Sampler type/ Type …, Start Date/ Date de…, Stop Date/ Date de …, Volume collected/ V…, Alpha Activity/ Act…, Alpha Unc/ Inc Alph…, Alpha MDC/ CMD Alph…

## g0011（1 列）
- 見出し：Location/Emplacement
- 例1 値：Edmonton | Edmundston | Greenwood | London | Halifax
  - 同じ表の列：Station, Sampler type/ Type …, Start Date/ Date de…, Stop Date/ Date de …, Volume collected/ V…, Alpha Activity/ Act…, Alpha Unc/ Inc Alph…, Alpha MDC/ CMD Alph…

## g0012（1 列）
- 見出し：Sampler type/ Type d'echantilloneur
- 例1 値：Funnel/Entonnoir | Cylinder/Cylindre | Cylinder/Cylindre | Cylinder/Cylindre | Cylinder/Cylindre
  - 同じ表の列：Station, Location/Emplacement, Start Date/ Date de…, Stop Date/ Date de …, Volume collected/ V…, Alpha Activity/ Act…, Alpha Unc/ Inc Alph…, Alpha MDC/ CMD Alph…

## g0013（1 列）
- 見出し：Start Date/ Date de debut
- 例1 値：2025-04-01 | 2024-10-04 | 2024-07-31 | 2024-11-28 | 2021-05-01
  - 同じ表の列：Station, Location/Emplacement, Sampler type/ Type …, Stop Date/ Date de …, Volume collected/ V…, Alpha Activity/ Act…, Alpha Unc/ Inc Alph…, Alpha MDC/ CMD Alph…

## g0014（1 列）
- 見出し：Stop Date/ Date de fin
- 例1 値：2022-08-31 | 2025-05-01 | 2022-11-10 | 2024-05-01 | 2023-06-27
  - 同じ表の列：Station, Location/Emplacement, Sampler type/ Type …, Start Date/ Date de…, Volume collected/ V…, Alpha Activity/ Act…, Alpha Unc/ Inc Alph…, Alpha MDC/ CMD Alph…

## g0015（1 列）
- 見出し：Volume collected/ Volume collectionne (mL)
- 例1 値：3193.07 | 343.2 | 364.53 | 988.06 | 1158.9
  - 同じ表の列：Station, Location/Emplacement, Sampler type/ Type …, Start Date/ Date de…, Stop Date/ Date de …, Alpha Activity/ Act…, Alpha Unc/ Inc Alph…, Alpha MDC/ CMD Alph…

## g0016（1 列）
- 見出し：Alpha Activity/ Activite Alpha (Bq/L)
- 例1 値：0.084 | Below MDC/Inférieur à la CMD | 0.077 | Below MDC/Inférieur à la CMD | Below MDC/Inférieur à la CMD
  - 同じ表の列：Station, Location/Emplacement, Sampler type/ Type …, Start Date/ Date de…, Stop Date/ Date de …, Volume collected/ V…, Alpha Unc/ Inc Alph…, Alpha MDC/ CMD Alph…

## g0017（1 列）
- 見出し：Alpha Unc/ Inc Alpha (Bq/L)
- 例1 値：NA | NA | NA | 0.024 | NA
  - 同じ表の列：Station, Location/Emplacement, Sampler type/ Type …, Start Date/ Date de…, Stop Date/ Date de …, Volume collected/ V…, Alpha Activity/ Act…, Alpha MDC/ CMD Alph…

## g0018（1 列）
- 見出し：Alpha MDC/ CMD Alpha (Bq/L)
- 例1 値：0.04 | 0.04 | 0.04 | 0.04 | 0.04
  - 同じ表の列：Station, Location/Emplacement, Sampler type/ Type …, Start Date/ Date de…, Stop Date/ Date de …, Volume collected/ V…, Alpha Activity/ Act…, Alpha Unc/ Inc Alph…

## g0019（1 列）
- 見出し：Alpha Activity/ Activite Alpha (Bq/m2)
- 例1 値：Below MDC/Inférieur à la CMD | Below MDC/Inférieur à la CMD | Below MDC/Inférieur à la CMD | Below MDC/Inférieur à la CMD | 6.7
  - 同じ表の列：Station, Location/Emplacement, Sampler type/ Type …, Start Date/ Date de…, Stop Date/ Date de …, Volume collected/ V…, Alpha Activity/ Act…, Alpha Unc/ Inc Alph…

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
```
