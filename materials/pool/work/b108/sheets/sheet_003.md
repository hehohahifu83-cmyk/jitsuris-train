# ラベル用シート 003 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：ratecases_total
- 例1 値：48.27 | 0 | 3632.32 | 381.37 | 533.28
  - 同じ表の列：pruid, date, reporting_week, reporting_year, update, totalcases, numdeaths, ratedeaths

## g0242（1 列）
- 見出し：numdeaths
- 例1 値：277 | 4 | 0 | 157 | 20553
  - 同じ表の列：pruid, date, reporting_week, reporting_year, update, totalcases, ratecases_total, ratedeaths

## g0243（1 列）
- 見出し：ratedeaths
- 例1 値：0.0 | 2.22 | 0.0 | 23.53 | 55.49
  - 同じ表の列：pruid, date, reporting_week, reporting_year, update, totalcases, ratecases_total, numdeaths

## g0244（1 列）
- 見出し：amendmentNumber-numeroModification
- 例1 値：000 | 000 | 000 | 000 | 000
  - 同じ表の列：solicitationNumber-…, numberOfRecords-nom…, publicationDate-dat…, contractAwardDate-d…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…

## g0245（1 列）
- 見出し：solicitationNumber-numeroSollicitation
- 例1 値：WS5008552173 | WS4919381136 | WS5122680510 | WS4811669826 | WS3817208998
  - 同じ表の列：amendmentNumber-num…, numberOfRecords-nom…, publicationDate-dat…, contractAwardDate-d…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…

## g0246（1 列）
- 見出し：numberOfRecords-nombreEnregistrements
- 例1 値：2 | 4 | 1 | 5 | 3
  - 同じ表の列：amendmentNumber-num…, solicitationNumber-…, publicationDate-dat…, contractAwardDate-d…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…

## g0247（1 列）
- 見出し：publicationDate-datePublication
- 例1 値：2025-03-27 | 2023-10-25 | 2026-06-24 | 2024-07-27 | 2025-01-22
  - 同じ表の列：amendmentNumber-num…, solicitationNumber-…, numberOfRecords-nom…, contractAwardDate-d…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…

## g0248（1 列）
- 見出し：contractAwardDate-dateAttributionContrat
- 例1 値：2025-02-28 | 2023-08-21 | 2024-10-03 | 2025-02-11 | 2023-09-22
  - 同じ表の列：amendmentNumber-num…, solicitationNumber-…, numberOfRecords-nom…, publicationDate-dat…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…

## g0249（1 列）
- 見出し：contractStartDate-contratDateDebut
- 例1 値：2026-04-01 | 2023-11-30 | 2024-12-01 | 2023-06-05 | 2024-06-01
  - 同じ表の列：amendmentNumber-num…, solicitationNumber-…, numberOfRecords-nom…, publicationDate-dat…, contractAwardDate-d…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…

## g0250（1 列）
- 見出し：contractEndDate-dateFinContrat
- 例1 値：2028-08-31 | 2027-04-10 | 2024-11-10 | 2024-03-31 | 2024-12-31
  - 同じ表の列：amendmentNumber-num…, solicitationNumber-…, numberOfRecords-nom…, publicationDate-dat…, contractAwardDate-d…, contractStartDate-c…, contractAmount-mont…, totalContractValue-…

## g0251（1 列）
- 見出し：contractAmount-montantContrat
- 例1 値：82782.00 | 97775259.00 | 56500.00 | 14381.51 | 11300.00
  - 同じ表の列：amendmentNumber-num…, solicitationNumber-…, numberOfRecords-nom…, publicationDate-dat…, contractAwardDate-d…, contractStartDate-c…, contractEndDate-dat…, totalContractValue-…

## g0252（1 列）
- 見出し：totalContractValue-valeurTotaleContrat
- 例1 値：187058.00 | 654902379.00 | 730450.32 | 0.00 | 100000.00
  - 同じ表の列：amendmentNumber-num…, solicitationNumber-…, numberOfRecords-nom…, publicationDate-dat…, contractAwardDate-d…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…

## g0253（1 列）
- 見出し：contractCurrency-contratMonnaie
- 例1 値：CAD | CAD | CAD | CAD | CAD
  - 同じ表の列：amendmentNumber-num…, solicitationNumber-…, numberOfRecords-nom…, publicationDate-dat…, contractAwardDate-d…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…

## g0254（1 列）
- 見出し：Aut-type_eng
- 例1 値：Budgetary | Budgetary | Non-budgetary | Budgetary | Budgetary
  - 同じ表の列：Aut-type_fra, Accounting-ops-type…, Accounting-ops-type…, Lvl1-aut-code_Code-…, Lvl2-aut-code_Code-…, Lvl2-aut-desc_Desc-…, Lvl2-aut-desc_Desc-…, Lvl3-aut-code_Code-…

## g0255（1 列）
- 見出し：Aut-type_fra
- 例1 値：Budgétaire | Non budgétaire | Non budgétaire | Budgétaire | Non budgétaire
  - 同じ表の列：Aut-type_eng, Accounting-ops-type…, Accounting-ops-type…, Lvl1-aut-code_Code-…, Lvl2-aut-code_Code-…, Lvl2-aut-desc_Desc-…, Lvl2-aut-desc_Desc-…, Lvl3-aut-code_Code-…

## g0256（1 列）
- 見出し：Accounting-ops-type_Type-ops-comptables_eng
- 例1 値：Other specified purpose accounts | Other specified purpose accounts | Non-appropriated amounts | Other specified purpose accounts | Loan and advance accounts
  - 同じ表の列：Aut-type_eng, Aut-type_fra, Accounting-ops-type…, Lvl1-aut-code_Code-…, Lvl2-aut-code_Code-…, Lvl2-aut-desc_Desc-…, Lvl2-aut-desc_Desc-…, Lvl3-aut-code_Code-…

## g0257（1 列）
- 見出し：Accounting-ops-type_Type-ops-comptables_fra
- 例1 値：Comptes de prêts et d'avances | Autres comptes à fins déterminées | Dépenses | Dépenses | Dépenses
  - 同じ表の列：Aut-type_eng, Aut-type_fra, Accounting-ops-type…, Lvl1-aut-code_Code-…, Lvl2-aut-code_Code-…, Lvl2-aut-desc_Desc-…, Lvl2-aut-desc_Desc-…, Lvl3-aut-code_Code-…

## g0258（1 列）
- 見出し：Lvl1-aut-code_Code-aut-niv1
- 例1 値：G | A | A | G | F
  - 同じ表の列：Aut-type_eng, Aut-type_fra, Accounting-ops-type…, Accounting-ops-type…, Lvl2-aut-code_Code-…, Lvl2-aut-desc_Desc-…, Lvl2-aut-desc_Desc-…, Lvl3-aut-code_Code-…

## g0259（1 列）
- 見出し：Lvl2-aut-code_Code-aut-niv2
- 例1 値：A2 | B1 | A2 | N1 | A2
  - 同じ表の列：Aut-type_eng, Aut-type_fra, Accounting-ops-type…, Accounting-ops-type…, Lvl1-aut-code_Code-…, Lvl2-aut-desc_Desc-…, Lvl2-aut-desc_Desc-…, Lvl3-aut-code_Code-…

## g0260（1 列）
- 見出し：Lvl2-aut-desc_Desc-aut-niv2_eng
- 例1 値：The codes in G1 should be used for any … | The codes in G1 should be used for any … | Details on transfer payments are requir… | Details on transfer payments are requir… | Details on transfer payments are requir…
  - 同じ表の列：Aut-type_eng, Aut-type_fra, Accounting-ops-type…, Accounting-ops-type…, Lvl1-aut-code_Code-…, Lvl2-aut-code_Code-…, Lvl2-aut-desc_Desc-…, Lvl3-aut-code_Code-…

## g0261（1 列）
- 見出し：Lvl2-aut-desc_Desc-aut-niv2_fra
- 例1 値：Les particularités des paiements de tra… | Si un ministère doit rendre compte de d… | Si un ministère doit rendre compte de d… | Les particularités des paiements de tra… | Les particularités des paiements de tra…
  - 同じ表の列：Aut-type_eng, Aut-type_fra, Accounting-ops-type…, Accounting-ops-type…, Lvl1-aut-code_Code-…, Lvl2-aut-code_Code-…, Lvl2-aut-desc_Desc-…, Lvl3-aut-code_Code-…

## g0262（1 列）
- 見出し：Lvl3-aut-code_Code-aut-niv3
- 例1 値：D34 | P75 | A39 | A83 | D34
  - 同じ表の列：Aut-type_eng, Aut-type_fra, Accounting-ops-type…, Accounting-ops-type…, Lvl1-aut-code_Code-…, Lvl2-aut-code_Code-…, Lvl2-aut-desc_Desc-…, Lvl2-aut-desc_Desc-…

## g0263（1 列）
- 見出し：Lvl3-aut-desc_Desc-aut-niv3_eng
- 例1 値：For the description, please refer to D2… | For the description, please refer to D2… | These amounts are included as operating… | The user charges revenue authority code… | The user charges revenue authority code…
  - 同じ表の列：Aut-type_eng, Aut-type_fra, Accounting-ops-type…, Accounting-ops-type…, Lvl1-aut-code_Code-…, Lvl2-aut-code_Code-…, Lvl2-aut-desc_Desc-…, Lvl2-aut-desc_Desc-…

## g0264（1 列）
- 見出し：cadorsnumber
- 例1 値：2000P0656 | 2001Q0682 | 2009P1099 | 1995C0231 | 2008Q0390
  - 同じ表の列：occurrence_category…, occurrence_category…

## g0265（1 列）
- 見出し：occurrence_category_etxt
- 例1 値：System/component failure or malfunction… | System/component failure or malfunction… | Other | ATM/CNS | ATM/CNS
  - 同じ表の列：cadorsnumber, occurrence_category…

## g0266（1 列）
- 見出し：occurrence_category_ftxt
- 例1 値：Panne ou mauvais fonctionnement d'un ci… | Autre | Contact anormal avec la piste | Autre | ATM/CNS
  - 同じ表の列：cadorsnumber, occurrence_category…

## 答えの雛形

```
g0241	
g0242	
g0243	
g0244	
g0245	
g0246	
g0247	
g0248	
g0249	
g0250	
g0251	
g0252	
g0253	
g0254	
g0255	
g0256	
g0257	
g0258	
g0259	
g0260	
g0261	
g0262	
g0263	
g0264	
g0265	
g0266	
```
