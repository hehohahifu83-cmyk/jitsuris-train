# ラベル用シート 002 / 003

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Type of test
- 例1 値：UNDECLARED Multi Allergen | UNDECLARED Multi Allergen | UNDECLARED Multi Allergen | UNDECLARED Multi Allergen | UNDECLARED Multi Allergen
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Produit

## g0122（2 列）
- 見出し：Sample No. - No. d'echantillon
- 例1 値：2011MYC0049 | 2011MYC0237 | 2011MYC0508 | 2011MYC0411 | 2011MYC0043
  - 同じ表の列：Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…, Type of Test
- 例2 値：2011MYC0369 | 2011MYC0464 | 2011MYC0842 | 2011MYC0115 | 2011MYC0972
  - 同じ表の列：Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…, Type of Test

## g0123（1 列）
- 見出し：Origine
- 例1 値：ÉTATS-UNIS | BOLIVIE, ÉTAT PLURINATIONAL DE | CANADA | ÉTATS-UNIS | CANADA
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Product, Produit, Date Sampled - Date…, Type of Test

## g0124（1 列）
- 見出し：Product
- 例1 値：Cereal - Other | Baked Goods | Cereal - Other | Corn Products | Millet
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Produit, Date Sampled - Date…, Type of Test

## g0125（1 列）
- 見出し：Produit
- 例1 値：Céréales - autre | Farine - Autre | Grain - Quinoa | Produits de blé | Céréales - autre
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Date Sampled - Date…, Type of Test

## g0126（2 列）
- 見出し：Type of Test
- 例1 値：VOMITOXIN | VOMITOXIN | VOMITOXIN | VOMITOXIN | VOMITOXIN
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…
- 例2 値：OCHRATOXIN | OCHRATOXIN | OCHRATOXIN | OCHRATOXIN | OCHRATOXIN
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g0127（2 列）
- 見出し：Type d'analyse
- 例1 値：VOMITOXINE | VOMITOXINE | VOMITOXINE | VOMITOXINE | VOMITOXINE
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…
- 例2 値：OCHRATOXINE | OCHRATOXINE | OCHRATOXINE | OCHRATOXINE | OCHRATOXINE
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g0128（1 列）
- 見出し：Product
- 例1 値：Bakery Product - Bread - Other | Infant Formula - Dairy | Bran - Wheat | Cereal - Children | Infant Food - Cereal
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Produit, Date Sampled - Date…, Type of Test

## g0129（1 列）
- 見出し：Produit
- 例1 値：Pain | Pain - Tortilla/Wrap/Pita | Pain | Préparation pour nourrissons - Laitier | farine de maïs
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Date Sampled - Date…, Type of Test

## g0130（1 列）
- 見出し：Prov/Terr
- 例1 値：59 | 35 | 59 | 35 | 24
  - 同じ表の列：CMA-CA/RMR-AR, Classification, Total - All Returns…, Total Income / Reve…, Under $5,000 / Moin…, $5,000 to $9,999 / …, $10,000 to $14,999 …, $15,000 to $19,999 …

## g0131（1 列）
- 見出し：CMA-CA/RMR-AR
- 例1 値：860 | 943 | 456 | 595 | 915
  - 同じ表の列：Prov/Terr, Classification, Total - All Returns…, Total Income / Reve…, Under $5,000 / Moin…, $5,000 to $9,999 / …, $10,000 to $14,999 …, $15,000 to $19,999 …

## g0132（1 列）
- 見出し：Classification
- 例1 値：TOTAL | TOTAL | CMA/RMR | TOTAL | TOTAL
  - 同じ表の列：Prov/Terr, CMA-CA/RMR-AR, Total - All Returns…, Total Income / Reve…, Under $5,000 / Moin…, $5,000 to $9,999 / …, $10,000 to $14,999 …, $15,000 to $19,999 …

## g0133（1 列）
- 見出し：Total - All Returns /Total - Toutes les declarations
- 例1 値：692110 | 135260 | 32270 | 17190 | 34580
  - 同じ表の列：Prov/Terr, CMA-CA/RMR-AR, Classification, Total Income / Reve…, Under $5,000 / Moin…, $5,000 to $9,999 / …, $10,000 to $14,999 …, $15,000 to $19,999 …

## g0134（1 列）
- 見出し：Total Income / Revenu total
- 例1 値：55475000 | 962588000 | 1017531000 | 19640566000 | 1301673000
  - 同じ表の列：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns…, Under $5,000 / Moin…, $5,000 to $9,999 / …, $10,000 to $14,999 …, $15,000 to $19,999 …

## g0135（1 列）
- 見出し：Under $5,000 / Moins de 5 000 $
- 例1 値：5660 | 4270 | 6110 | 1410 | 2660
  - 同じ表の列：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns…, Total Income / Reve…, $5,000 to $9,999 / …, $10,000 to $14,999 …, $15,000 to $19,999 …

## g0136（1 列）
- 見出し：$5,000 to $9,999 / 5 000 $ a 9 999 $
- 例1 値：8190 | 2280 | 450 | 920 | 2590
  - 同じ表の列：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns…, Total Income / Reve…, Under $5,000 / Moin…, $10,000 to $14,999 …, $15,000 to $19,999 …

## g0137（1 列）
- 見出し：$10,000 to $14,999 / 10 000 $ a 14 999 $
- 例1 値：490 | 760 | 1620 | 2230 | 270060
  - 同じ表の列：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns…, Total Income / Reve…, Under $5,000 / Moin…, $5,000 to $9,999 / …, $15,000 to $19,999 …

## g0138（1 列）
- 見出し：$15,000 to $19,999 / 15 000 $ a 19 999 $
- 例1 値：1150 | 840 | 4180 | 760 | 8560
  - 同じ表の列：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns…, Total Income / Reve…, Under $5,000 / Moin…, $5,000 to $9,999 / …, $10,000 to $14,999 …

## g0139（1 列）
- 見出し：$20,000 to $24,999 / 20 000 $ a 24 999 $
- 例1 値：1530 | 9170 | 7750 | 1280 | 1280
  - 同じ表の列：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns…, Total Income / Reve…, Under $5,000 / Moin…, $5,000 to $9,999 / …, $10,000 to $14,999 …

## g0140（1 列）
- 見出し：Tax gap component
- 例1 値：CIT: reporting gap (SMEs, upper-bound) | Excise: gross tax gap (% of excise duti… | Total net tax gap (lower-bound) | GST/HST: reporting gap | CIT: reporting gap (large corporations,…
  - 同じ表の列：2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021

## g0141（1 列）
- 見出し：2014
- 例1 値：-59% | 17.20% | $ - ** | -% ** | $10.10
  - 同じ表の列：Tax gap component, 2015, 2016, 2017, 2018, 2019, 2020, 2021

## g0142（1 列）
- 見出し：2015
- 例1 値：-64% | $0.60 | 4.10% | $11.60 | $5.50
  - 同じ表の列：Tax gap component, 2014, 2016, 2017, 2018, 2019, 2020, 2021

## g0143（1 列）
- 見出し：2016
- 例1 値：$ - ** | -%*** | $0.60 | 24.70% | $2.30
  - 同じ表の列：Tax gap component, 2014, 2015, 2017, 2018, 2019, 2020, 2021

## g0144（1 列）
- 見出し：2017
- 例1 値：-48% | $14.10 | $1.40 | $13.20 | 7.00%
  - 同じ表の列：Tax gap component, 2014, 2015, 2016, 2018, 2019, 2020, 2021

## g0145（1 列）
- 見出し：2018
- 例1 値：$0.80 | $12.30 | $0.50 | -% ** | $4.90
  - 同じ表の列：Tax gap component, 2014, 2015, 2016, 2017, 2019, 2020, 2021

## g0146（1 列）
- 見出し：2019
- 例1 値：9.50% | $21.50 | 7.00% | 19.40% | $0.30
  - 同じ表の列：Tax gap component, 2014, 2015, 2016, 2017, 2018, 2020, 2021

## g0147（1 列）
- 見出し：2020
- 例1 値：-51% | 2.60% | 1.90% | $23.20 | $24.00
  - 同じ表の列：Tax gap component, 2014, 2015, 2016, 2017, 2018, 2019, 2021

## g0148（1 列）
- 見出し：2021
- 例1 値：9.30% | $3.00 | 2.10% | 11.50% | $0.10
  - 同じ表の列：Tax gap component, 2014, 2015, 2016, 2017, 2018, 2019, 2020

## g0149（1 列）
- 見出し：2022
- 例1 値：$10.20 | $2.70 | 8.30% | 15.30% | 5.70%
  - 同じ表の列：Tax gap component, 2014, 2015, 2016, 2017, 2018, 2019, 2020

## g0150（1 列）
- 見出し：Province or Territory
- 例1 値：Prince Edward Island | Northwest Territories | Ontario | Yukon | Nova Scotia
  - 同じ表の列：$55,867 or less, $55,867 - $111,733, $111,733 - $173,205, $173,205 - $246,752, $246,752 or more, All Brackets

## g0151（1 列）
- 見出し：$55,867 or less
- 例1 値：4625360 | 568210 | 20176570 | 2190990 | 577970
  - 同じ表の列：Province or Territo…, $55,867 - $111,733, $111,733 - $173,205, $173,205 - $246,752, $246,752 or more, All Brackets

## g0152（1 列）
- 見出し：$55,867 - $111,733
- 例1 値：8373030 | 102280 | 11770 | 267940 | 164470
  - 同じ表の列：Province or Territo…, $55,867 or less, $111,733 - $173,205, $173,205 - $246,752, $246,752 or more, All Brackets

## g0153（1 列）
- 見出し：$111,733 - $173,205
- 例1 値：2910 | 23300 | 58360 | 304770 | 3040
  - 同じ表の列：Province or Territo…, $55,867 or less, $55,867 - $111,733, $173,205 - $246,752, $246,752 or more, All Brackets

## g0154（1 列）
- 見出し：$173,205 - $246,752
- 例1 値：581060 | 910 | 700 | 1260 | 9410
  - 同じ表の列：Province or Territo…, $55,867 or less, $55,867 - $111,733, $111,733 - $173,205, $246,752 or more, All Brackets

## g0155（1 列）
- 見出し：$246,752 or more
- 例1 値：207340 | 3980 | 2210 | 360 | 7400
  - 同じ表の列：Province or Territo…, $55,867 or less, $55,867 - $111,733, $111,733 - $173,205, $173,205 - $246,752, All Brackets

## g0156（1 列）
- 見出し：All Brackets
- 例1 値：135520 | 443620 | 12222620 | 904660 | 4360050
  - 同じ表の列：Province or Territo…, $55,867 or less, $55,867 - $111,733, $111,733 - $173,205, $173,205 - $246,752, $246,752 or more

## g0157（3 列）
- 見出し：departmental_identification_number
- 例1 値：OI-965 | OI-681 | OI-972 | OI-965 | OI-1062
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published
- 例2 値：OI-610 | OI-605 | OI-612 | OI-608 | OI-610
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0158（1 列）
- 見出し：title_translated_en
- 例1 値：CUSMA Chicken Quota Holders List – Dist… | Notice to Importers: Chicken and Chicke… | Chicken Quota Holders List Non-ICL Prod… | Notice to Importers: Chicken and Chicke… | CPTPP Chicken Quota Holders Lists - Foo…
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0159（1 列）
- 見出し：title_translated_fr
- 例1 値：Avis aux importateurs Poulet et produit… | Liste des détenteurs de contingent de p… | Liste des détenteurs de contingent Rése… | Avis aux importateurs : Poulet et produ… | Délivrance de licences d’importation - …
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0160（1 列）
- 見出し：notes_translated_en
- 例1 値：IMPORT PERMITS ISSUANCE - Chicken - wee… | Chicken Quota Holders List Traditional … | CUSMA Chicken Quota Holders List, proce… | Utilization Data - Chicken and chicken … | Chicken And Chicken Products (Items 96 …
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0161（1 列）
- 見出し：notes_translated_fr
- 例1 値：Délivrance de licences d’importation - … | Liste de détenteur de contingent de Pou… | Poulet et produits du poulet (Article 9… | Liste des détenteurs de contingent de p… | Poulet et produits du poulet (Article 9…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0162（3 列）
- 見出し：organization_title_en
- 例1 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published
- 例2 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0163（3 列）
- 見出し：organization_title_fr
- 例1 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published
- 例2 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0164（3 列）
- 見出し：subject
- 例1 値：economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published
- 例2 値：economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published

## g0165（3 列）
- 見出し：date_published
- 例1 値：2013-06-21 | 2024-02-29 | 2023-01-09 | 2015-12-07 | 2015-12-07
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject
- 例2 値：2023-12-22 | 2022-11-03 | 2022-12-20 | 2019-07-11 | 2019-10-04
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0166（3 列）
- 見出し：portal_type
- 例1 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject
- 例2 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0167（1 列）
- 見出し：title_translated_en
- 例1 値：CUSMA Sugar-Containing Products Quota H… | Sugar and Sugar-Containing Products - C… | Sugar-Containing Products by month - CU… | Notices: Sugar-Containing Products for … | WTO - Sugar-Containing Products Quota H…
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0168（1 列）
- 見出し：title_translated_fr
- 例1 値：Sucre, produits contenant du sucre - OM… | Message à l'intention de l'industrie – … | Sucre, produits contenant du sucre - OM… | Conciliation des données États-Unis - C… | Contingent d’exportation des produits c…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0169（1 列）
- 見出し：notes_translated_en
- 例1 値：CUSMA Sugar-Containing Products Quota H… | Sugar-containing Products for Export to… | Sugar and Sugar-Containing Products - W… | Sugar and Sugar-Containing Products - W… | Sugar-Containing Products Export Quota:…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0170（1 列）
- 見出し：notes_translated_fr
- 例1 値：Liste des détenteurs de contingent pour… | Sucre, produits contenant du sucre - OMC | Sucre, produits contenant du sucre - AC… | Le présent avis énonce les politiques e… | Conciliation des données États-Unis - C…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0171（1 列）
- 見出し：title_translated_en
- 例1 値：CUSMA Butter and Cream Powder Quota Hol… | 2019-2021 – Cream, Powdered Whey, Butte… | CPTPP Cream Quota Holders List - 2019-2… | WTO Specialty Creams Quota Holders List… | Specialty Cream Quota Holders List - 20…
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0172（1 列）
- 見出し：title_translated_fr
- 例1 値：Politique sur les pénuries sur le march… | Avis aux importateurs Crèmes de special… | Liste des détenteurs de contingent pour… | Produits laitiers – Accord de Partenari… | Avis aux importateurs Produits laitiers…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0173（1 列）
- 見出し：notes_translated_en
- 例1 値：CUSMA Butter and Cream Powder Quota Hol… | CPTPP Cream Quota Holders List. | Specialty Cream Quota Holders List. | Dairy – CPTPP Milk Powders Tariff Rate … | WTO Specialty Creams Quota Holders List.
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0174（1 列）
- 見出し：notes_translated_fr
- 例1 値：En bref L’importation au Canada de crèm… | Crèmes de spécialité liste de détenteur… | Liste des détenteurs de contingent pour… | Crèmes de spécialité liste de détenteur… | Crèmes de spécialité liste de détenteur…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0175（1 列）
- 見出し：jurisdiction
- 例1 値：New Brunswick | New Brunswick | Quebec | Alberta | Manitoba
  - 同じ表の列：effective_date, wage

## g0176（1 列）
- 見出し：effective_date
- 例1 値：1971-06-01 | 2017-04-01 | 1995-01-01 | 1986-09-15 | 2024-09-01
  - 同じ表の列：jurisdiction, wage

## g0177（1 列）
- 見出し：wage
- 例1 値：$1.75 | $10.15 | $14.00 | $2.70 | $3.00
  - 同じ表の列：jurisdiction, effective_date

## g0178（2 列）
- 見出し：Province
- 例1 値：ON | NB | NB | ON | AB
  - 同じ表の列：Year, FSA, EAP amount ($), PSE withdrawal amou…, Number of beneficia…, Number of beneficia…
- 例2 値：SK | SK | ON | ON | QC
  - 同じ表の列：Rank, TC Number, Railway Company, Region, Access, Jurisdiction, Mile, Subdivision

## g0179（1 列）
- 見出し：FSA
- 例1 値：A2N | A1K | V6Y | V9R | T3C
  - 同じ表の列：Year, Province, EAP amount ($), PSE withdrawal amou…, Number of beneficia…, Number of beneficia…

## g0180（1 列）
- 見出し：EAP amount ($)
- 例1 値：326,592 | 353,100 | 1,850,881 | 807,374 | 903,747
  - 同じ表の列：Year, Province, FSA, PSE withdrawal amou…, Number of beneficia…, Number of beneficia…

## g0181（1 列）
- 見出し：PSE withdrawal amount ($)
- 例1 値：1,155,384 | 9,807,804 | 4,642,835 | 810,406 | 7,237,093
  - 同じ表の列：Year, Province, FSA, EAP amount ($), Number of beneficia…, Number of beneficia…

## g0182（1 列）
- 見出し：Number of beneficiaries in receipt of EAP
- 例1 値：209 | 254 | 1,796 | * | 723
  - 同じ表の列：Year, Province, FSA, EAP amount ($), PSE withdrawal amou…, Number of beneficia…

## g0183（1 列）
- 見出し：Number of beneficiaries with a PSE withdrawal
- 例1 値：56 | * | 61 | 117 | 128
  - 同じ表の列：Year, Province, FSA, EAP amount ($), PSE withdrawal amou…, Number of beneficia…

## g0184（1 列）
- 見出し：2023/09/01
- 例1 値：22710 | 815600 | 0 | 119103 | 835264
  - 同じ表の列：2023/10/01, 2023/11/01, 2023/12/01, 2024/01/01, 2024/02/01, 2024/03/01, 2024/04/01, 2024/05/01

## g0185（1 列）
- 見出し：2023/10/01
- 例1 値：0 | 26780752 | 5841 | Visits | 223811
  - 同じ表の列：2023/09/01, 2023/11/01, 2023/12/01, 2024/01/01, 2024/02/01, 2024/03/01, 2024/04/01, 2024/05/01

## g0186（1 列）
- 見出し：2023/11/01
- 例1 値：0 | 19205 | 877 | 149445 | 9308861
  - 同じ表の列：2023/09/01, 2023/10/01, 2023/12/01, 2024/01/01, 2024/02/01, 2024/03/01, 2024/04/01, 2024/05/01

## g0187（1 列）
- 見出し：2023/12/01
- 例1 値：0 | 4106 | 2591719 | 52019 | 3837800
  - 同じ表の列：2023/09/01, 2023/10/01, 2023/11/01, 2024/01/01, 2024/02/01, 2024/03/01, 2024/04/01, 2024/05/01

## g0188（1 列）
- 見出し：2024/01/01
- 例1 値：834700 | 1518 | 1702213 | 244 | 16
  - 同じ表の列：2023/09/01, 2023/10/01, 2023/11/01, 2023/12/01, 2024/02/01, 2024/03/01, 2024/04/01, 2024/05/01

## g0189（1 列）
- 見出し：2024/02/01
- 例1 値：0 | 0 | 1453556 | 4211 | 368024
  - 同じ表の列：2023/09/01, 2023/10/01, 2023/11/01, 2023/12/01, 2024/01/01, 2024/03/01, 2024/04/01, 2024/05/01

## g0190（1 列）
- 見出し：2024/03/01
- 例1 値：42772 | 29294 | 1611667 | 390607 | 676
  - 同じ表の列：2023/09/01, 2023/10/01, 2023/11/01, 2023/12/01, 2024/01/01, 2024/02/01, 2024/04/01, 2024/05/01

## g0191（1 列）
- 見出し：2024/04/01
- 例1 値：19951 | 882 | 11928 | 16212195 | 0
  - 同じ表の列：2023/09/01, 2023/10/01, 2023/11/01, 2023/12/01, 2024/01/01, 2024/02/01, 2024/03/01, 2024/05/01

## g0192（1 列）
- 見出し：2024/05/01
- 例1 値：6926 | 11679699 | 15082 | 571316715 | 1625
  - 同じ表の列：2023/09/01, 2023/10/01, 2023/11/01, 2023/12/01, 2024/01/01, 2024/02/01, 2024/03/01, 2024/04/01

## g0193（1 列）
- 見出し：2024/06/01
- 例1 値：0 | 9176214 | 15274 | 6816 | 3698975
  - 同じ表の列：2023/09/01, 2023/10/01, 2023/11/01, 2023/12/01, 2024/01/01, 2024/02/01, 2024/03/01, 2024/04/01

## g0194（1 列）
- 見出し：Licence Sub-Class
- 例1 値：Micro | Micro | Standard | Standard | Micro
  - 同じ表の列：Indoor/Outdoor, Province/Territory

## g0195（1 列）
- 見出し：Indoor/Outdoor
- 例1 値：Indoor/Outdoor | Indoor Only | Indoor Only | Indoor Only | Indoor Only
  - 同じ表の列：Licence Sub-Class, Province/Territory

## g0196（1 列）
- 見出し：Province/Territory
- 例1 値：Ontario | British Columbia | Ontario | British Columbia | British Columbia
  - 同じ表の列：Licence Sub-Class, Indoor/Outdoor

## g0197（1 列）
- 見出し：CAS Number_ numero CAS
- 例1 値：0001406-18-4 | 0012225-18-2 | 0027178-87-6 | 0000097-99-4 | 0007758-05-6
  - 同じ表の列：Nom du produit de f…, List Number_ numero…, Allergen_ allergene

## g0198（1 列）
- 見出し：Nom du produit de formulation
- 例1 値：ACIDE HYDROBROMIQUE 47- 49 % | ROUGE ÉCARLATE | ACIDE BORIQUE | HUILE DE SOYA ÉPOXYDÉE | ACIDE DODÉCANOÏQUE
  - 同じ表の列：CAS Number_ numero …, List Number_ numero…, Allergen_ allergene

## g0199（1 列）
- 見出し：List Number_ numero de liste
- 例1 値：4B | 4B | 2 | 4B | 4B
  - 同じ表の列：CAS Number_ numero …, Nom du produit de f…, Allergen_ allergene

## g0200（1 列）
- 見出し：Allergen_ allergene
- 例1 値：N | N | N | N | N
  - 同じ表の列：CAS Number_ numero …, Nom du produit de f…, List Number_ numero…

## g0201（1 列）
- 見出し：SpeciesCode_CodeEspece
- 例1 値：ACESAZ | CARCAZ | BRARAP | MISSIN | MIMRIN
  - 同じ表の列：ID, Synonym_Synonyme, Family_Famille, TraitCode, TraitValue_ValeurTr…, TraitValueDescripti…, TraitValueComments_…, ReferenceID

## g0202（1 列）
- 見出し：Synonym_Synonyme
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：ID, SpeciesCode_CodeEsp…, Family_Famille, TraitCode, TraitValue_ValeurTr…, TraitValueDescripti…, TraitValueComments_…, ReferenceID

## g0203（1 列）
- 見出し：Family_Famille
- 例1 値：Apocynaceae | aspleniaceae | cornaceae | cyperaceae | rubiaceae
  - 同じ表の列：ID, SpeciesCode_CodeEsp…, Synonym_Synonyme, TraitCode, TraitValue_ValeurTr…, TraitValueDescripti…, TraitValueComments_…, ReferenceID

## g0204（1 列）
- 見出し：TraitCode
- 例1 値：VP | VP | VP | VP | VP
  - 同じ表の列：ID, SpeciesCode_CodeEsp…, Synonym_Synonyme, Family_Famille, TraitValue_ValeurTr…, TraitValueDescripti…, TraitValueComments_…, ReferenceID

## g0205（1 列）
- 見出し：TraitValue_ValeurTrait
- 例1 値：a | r | r | stsp | a
  - 同じ表の列：ID, SpeciesCode_CodeEsp…, Synonym_Synonyme, Family_Famille, TraitCode, TraitValueDescripti…, TraitValueComments_…, ReferenceID

## g0206（1 列）
- 見出し：TraitValueDescription_DescriptionValeurTrait
- 例1 値：rhizomes | layering | layering | not applicable | absent
  - 同じ表の列：ID, SpeciesCode_CodeEsp…, Synonym_Synonyme, Family_Famille, TraitCode, TraitValue_ValeurTr…, TraitValueComments_…, ReferenceID

## g0207（1 列）
- 見出し：TraitValueComments_CommentairesValeurTrait
- 例1 値：May also sprout from the roots | Primary mode | will occasionally layer | NA | NA
  - 同じ表の列：ID, SpeciesCode_CodeEsp…, Synonym_Synonyme, Family_Famille, TraitCode, TraitValue_ValeurTr…, TraitValueDescripti…, ReferenceID

## g0208（1 列）
- 見出し：ReferenceID
- 例1 値：1076 | 1076 | 1076 | 5 | 1076
  - 同じ表の列：ID, SpeciesCode_CodeEsp…, Synonym_Synonyme, Family_Famille, TraitCode, TraitValue_ValeurTr…, TraitValueDescripti…, TraitValueComments_…

## g0209（1 列）
- 見出し：ReferenceType
- 例1 値：4 | 4 | 4 | 4 | 3
  - 同じ表の列：ID, SpeciesCode_CodeEsp…, Synonym_Synonyme, Family_Famille, TraitCode, TraitValue_ValeurTr…, TraitValueDescripti…, TraitValueComments_…

## g0210（1 列）
- 見出し：treeLocation
- 例1 値：Quebec_5 | Quebec_1 | Quebec_? | Quebec_? | Quebec_?
  - 同じ表の列：batch, treeSpecies, experimentNumber, treeNumber, boltNumber, corkNumber, bathPosition, vialPosition

## g0211（1 列）
- 見出し：batch
- 例1 値：1 | NA | NA | NA | NA
  - 同じ表の列：treeLocation, treeSpecies, experimentNumber, treeNumber, boltNumber, corkNumber, bathPosition, vialPosition

## g0212（1 列）
- 見出し：treeSpecies
- 例1 値：White_Birch | Yellow_Birch | White_Birch | White_Birch | White_Birch
  - 同じ表の列：treeLocation, batch, experimentNumber, treeNumber, boltNumber, corkNumber, bathPosition, vialPosition

## g0213（1 列）
- 見出し：experimentNumber
- 例1 値：8 | 9 | 3 | 1 | 11
  - 同じ表の列：treeLocation, batch, treeSpecies, treeNumber, boltNumber, corkNumber, bathPosition, vialPosition

## g0214（1 列）
- 見出し：treeNumber
- 例1 値：23 | 23 | 23 | 8 | 8
  - 同じ表の列：treeLocation, batch, treeSpecies, experimentNumber, boltNumber, corkNumber, bathPosition, vialPosition

## g0215（1 列）
- 見出し：boltNumber
- 例1 値：NA | 8 | 1 | 8 | 7
  - 同じ表の列：treeLocation, batch, treeSpecies, experimentNumber, treeNumber, corkNumber, bathPosition, vialPosition

## g0216（1 列）
- 見出し：corkNumber
- 例1 値：41 | 12 | 73 | 1 | 27
  - 同じ表の列：treeLocation, batch, treeSpecies, experimentNumber, treeNumber, boltNumber, bathPosition, vialPosition

## g0217（1 列）
- 見出し：bathPosition
- 例1 値：23 | 17 | 3 | 19 | 20
  - 同じ表の列：treeLocation, batch, treeSpecies, experimentNumber, treeNumber, boltNumber, corkNumber, vialPosition

## g0218（1 列）
- 見出し：vialPosition
- 例1 値：L | NA | S | S | L
  - 同じ表の列：treeLocation, batch, treeSpecies, experimentNumber, treeNumber, boltNumber, corkNumber, bathPosition

## g0219（1 列）
- 見出し：replicate
- 例1 値：14 | 11 | 4 | 2 | 14
  - 同じ表の列：treeLocation, batch, treeSpecies, experimentNumber, treeNumber, boltNumber, corkNumber, bathPosition

## g0220（1 列）
- 見出し：Point.ID
- 例1 値：1 | 3 | 2 | 5 | 3
  - 同じ表の列：Visit.Number, elevation, aspect, slope, Temperature, Wind, perPikaHabitat, Pika.sum

## g0221（1 列）
- 見出し：Visit.Number
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：Point.ID, elevation, aspect, slope, Temperature, Wind, perPikaHabitat, Pika.sum

## g0222（1 列）
- 見出し：elevation
- 例1 値：2118 | 2086 | 2028 | 2076 | 2298
  - 同じ表の列：Point.ID, Visit.Number, aspect, slope, Temperature, Wind, perPikaHabitat, Pika.sum

## g0223（1 列）
- 見出し：aspect
- 例1 値：227 | 257 | 302 | 61 | 27
  - 同じ表の列：Point.ID, Visit.Number, elevation, slope, Temperature, Wind, perPikaHabitat, Pika.sum

## g0224（1 列）
- 見出し：slope
- 例1 値：47 | 50 | 68 | 60 | 9
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, Temperature, Wind, perPikaHabitat, Pika.sum

## g0225（1 列）
- 見出し：Temperature
- 例1 値：14.3 | 2.9 | 12.3 | 14.6 | 7.2
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, slope, Wind, perPikaHabitat, Pika.sum

## g0226（1 列）
- 見出し：Wind
- 例1 値：1.3 | 1.4 | 4.2 | 0 | 1
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, slope, Temperature, perPikaHabitat, Pika.sum

## g0227（1 列）
- 見出し：perPikaHabitat
- 例1 値：100 | 80 | 80 | 80 | 90
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, slope, Temperature, Wind, Pika.sum

## g0228（1 列）
- 見出し：Pika.sum
- 例1 値：3 | 2 | 4 | 3 | 1
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, slope, Temperature, Wind, perPikaHabitat

## g0229（5 列）
- 見出し：date
- 例1 値：2023-09-02 | 2025-08-13 | 2024-09-10 | 2024-09-10 | 2025-08-14
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, slope, Temperature, Wind, perPikaHabitat
- 例2 値：2022-06-02 | 2022-05-29 | 2022-06-06 | 2022-06-11 | 2022-06-08
  - 同じ表の列：Site, Time, TempC

## g0230（2 列）
- 見出し：Site
- 例1 値：Woolsey | Woolsey | Woolsey | Woolsey | Woolsey
  - 同じ表の列：Date, Time, TempC
- 例2 値：Grizzly | Grizzly | Grizzly | Grizzly | Grizzly
  - 同じ表の列：Date, Time, TempC

## g0231（2 列）
- 見出し：TempC
- 例1 値：4.428 | 4.844 | 4.766 | 4.011 | 5.179
  - 同じ表の列：Site, Date, Time
- 例2 値：2.956 | 5.128 | 2.903 | 5.539 | 3.459
  - 同じ表の列：Site, Date, Time

## g0232（1 列）
- 見出し：FISCAL_YEAR
- 例1 値：2022_2023 | 2022_2023 | 2013_2014 | 2017_2018 | 2012_2013
  - 同じ表の列：emp_equity_designat…, emp_equity_designat…

## g0233（1 列）
- 見出し：emp_equity_designated_group_e
- 例1 値：Women | Women | Indigenous peoples | Members of visible minorities | Persons with disabilities
  - 同じ表の列：FISCAL_YEAR, emp_equity_designat…

## g0234（1 列）
- 見出し：emp_equity_designated_group_f
- 例1 値：Personnes en situation de handicap | Membres des minorités visibles | Membres des minorités visibles | Autochtones | Personnes en situation de handicap
  - 同じ表の列：FISCAL_YEAR, emp_equity_designat…

## g0235（1 列）
- 見出し：Department_EN
- 例1 値：Employment and Social Development Canada | Indigenous Services Canada | Public Service Commission of Canada | Parks Canada | Health Canada
  - 同じ表の列：Department_FR, Service_EN, Service_FR, Value, Date_Captured

## g0236（1 列）
- 見出し：Department_FR
- 例1 値：Innovation, Sciences et Développement é… | Agence canadienne de développement écon… | Emploi et Développement social Canada | Service correctionnel Canada | Service correctionnel Canada
  - 同じ表の列：Department_EN, Service_EN, Service_FR, Value, Date_Captured

## g0237（1 列）
- 見出し：Service_EN
- 例1 値：Telephony - Fixed & Mobile | Software Provisioning | Telephony - Fixed & Mobile | Telephony - Fixed & Mobile | Telephony - Fixed & Mobile
  - 同じ表の列：Department_EN, Department_FR, Service_FR, Value, Date_Captured

## g0238（1 列）
- 見出し：Service_FR
- 例1 値：Téléphonie - Fixe et Mobile | Approvisionnement de logiciels | Téléphonie - Fixe et Mobile | Conférence | Conférence
  - 同じ表の列：Department_EN, Department_FR, Service_EN, Value, Date_Captured

## g0239（1 列）
- 見出し：Date_Captured
- 例1 値：01Mar2023 0:00:00 | 31Dec2022 0:00:00 | 31Jan2023 0:00:00 | 31Mar2023 0:00:00 | 31Jan2023 0:00:00
  - 同じ表の列：Department_EN, Department_FR, Service_EN, Service_FR, Value

## g0240（2 列）
- 見出し：Fiscal Year
- 例1 値：2019-2020 | 2019-2020 | 2019-2020 | 2019-2020 | 2019-2020
  - 同じ表の列：Fiscal Period, Month, Information Date, Value, Data Source, Comments, Metric Type
- 例2 値：2020-2021 | 2020-2021 | 2019-2020 | 2020-2021 | 2021-2022
  - 同じ表の列：Fiscal Period, Month, Information Date, Branch, Service, SSC Client, Value, Metric Type

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
g0151	
g0152	
g0153	
g0154	
g0155	
g0156	
g0157	
g0158	
g0159	
g0160	
g0161	
g0162	
g0163	
g0164	
g0165	
g0166	
g0167	
g0168	
g0169	
g0170	
g0171	
g0172	
g0173	
g0174	
g0175	
g0176	
g0177	
g0178	
g0179	
g0180	
g0181	
g0182	
g0183	
g0184	
g0185	
g0186	
g0187	
g0188	
g0189	
g0190	
g0191	
g0192	
g0193	
g0194	
g0195	
g0196	
g0197	
g0198	
g0199	
g0200	
g0201	
g0202	
g0203	
g0204	
g0205	
g0206	
g0207	
g0208	
g0209	
g0210	
g0211	
g0212	
g0213	
g0214	
g0215	
g0216	
g0217	
g0218	
g0219	
g0220	
g0221	
g0222	
g0223	
g0224	
g0225	
g0226	
g0227	
g0228	
g0229	
g0230	
g0231	
g0232	
g0233	
g0234	
g0235	
g0236	
g0237	
g0238	
g0239	
g0240	
```
