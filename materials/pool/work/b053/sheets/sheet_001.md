# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：Sample Plan Number // Numero du plan d'echantillonnage
- 例1 値：2021_SB3092 | 2021_SB3092 | 2021_SB3092 | 2021_SB3092 | 2020_SB3092
  - 同じ表の列：Inspection Sample N…, Date Sampled YYYY/M…, Product Type // Typ…, Production Practice…, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…, Method Number // Nu…
- 例2 値：2024_SB3134 | 2024_SB3134 | 2024_SB3134 | 2024_SB3134 | 2024_SB3134
  - 同じ表の列：System ID // ID sys…, Job Laboratory Numb…, Date Sampled YYYY/M…, Product Type // Typ…, Product Subtype // …, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…

## g0002（1 列）
- 見出し：Inspection Sample Number // # d'inspection de l'echantillon
- 例1 値：B2021VCCG00087 | B2021TCCG00178D | B2020VCCG03038 | B2021MCSH00059 | B2021CCCG00194
  - 同じ表の列：Sample Plan Number …, Date Sampled YYYY/M…, Product Type // Typ…, Production Practice…, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…, Method Number // Nu…

## g0003（3 列）
- 見出し：Date Sampled YYYY/MM/DD // Date d'echantillonnage AAAA/MM/JJ
- 例1 値：2021-06-27 | 2021-09-14 | 2021-09-07 | 2021-05-31 | 2021-08-09
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Product Type // Typ…, Production Practice…, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…, Method Number // Nu…
- 例2 値：2020-09-27 | 2020-11-15 | 2020-09-13 | 2021-09-26 | 2021-08-16
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Season // Saison, Product Type // Typ…, Product Subtype // …, Packaging Type // T…, Production Practice…, Country of Origin /…

## g0004（1 列）
- 見出し：Product Type // Type de produit
- 例1 値：Red or green leaf lettuce // Laitue rou… | Red or green leaf lettuce // Laitue rou… | Swiss chard // Bette à carde | Watercress // Cresson | Red or green leaf lettuce // Laitue rou…
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Production Practice…, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…, Method Number // Nu…

## g0005（2 列）
- 見出し：Production Practice // Methode de production
- 例1 値：Conventional // Conventionnelle | Conventional // Conventionnelle | Conventional // Conventionnelle | Conventional // Conventionnelle | Conventional // Conventionnelle
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Product Type // Typ…, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…, Method Number // Nu…
- 例2 値：Conventional // Conventionnelle | Conventional // Conventionnelle | Conventional // Conventionnelle | Conventional // Conventionnelle | Conventional // Conventionnelle
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Season // Saison, Product Type // Typ…, Product Subtype // …, Packaging Type // T…, Country of Origin /…

## g0006（1 列）
- 見出し：Country of Origin // Pays d'origine
- 例1 値：CANADA | CANADA | CANADA | CANADA | CANADA
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Product Type // Typ…, Production Practice…, Domestic and/or Imp…, Analysis Type // Ty…, Method Number // Nu…

## g0007（1 列）
- 見出し：Domestic and/or Import // Canadienne et/ou Importation
- 例1 値：DOMESTIC | DOMESTIC | DOMESTIC | DOMESTIC | DOMESTIC
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Product Type // Typ…, Production Practice…, Country of Origin /…, Analysis Type // Ty…, Method Number // Nu…

## g0008（1 列）
- 見出し：Analysis Type // Type d'analyse
- 例1 値：Generic E. coli // E. coli générique | Salmonella | E. coli O157 | Generic E. coli // E. coli générique | Generic E. coli // E. coli générique
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Product Type // Typ…, Production Practice…, Country of Origin /…, Domestic and/or Imp…, Method Number // Nu…

## g0009（2 列）
- 見出し：Method Number // Numero de methode
- 例1 値：MFLP-52 | CFIAFMWG-001 | MFLP-52 | MFLP-30 | MFLP-29
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Product Type // Typ…, Production Practice…, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…
- 例2 値：MFHPB-21 | MFLP-49 | MFLP-49 | MFLP-49 | MFHPB-18
  - 同じ表の列：Sample Plan Number …, System ID // ID sys…, Job Laboratory Numb…, Date Sampled YYYY/M…, Product Type // Typ…, Product Subtype // …, Country of Origin /…, Domestic and/or Imp…

## g0010（1 列）
- 見出し：Result // Resultat
- 例1 値：Not Detected / 25 grams // Non Détecté … | Not Detected / 25 grams // Non détecté … | Not Detected / 25 grams///Non Détecté /… | Not Detected / 25 grams///Non Détecté /… | Not Detected / 25 grams // Non Détecté …
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Product Type // Typ…, Production Practice…, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…

## g0011（1 列）
- 見出し：Sample Plan Number // Numero du plan d'echantillonnage
- 例1 値：2021_SB3221 | 2020_F263R | 2021_SB3221 | 2021_SB3221 | 2021_SB3222
  - 同じ表の列：Inspection Sample N…, Date Sampled YYYY/M…, Season // Saison, Product Type // Typ…, Product Subtype // …, Packaging Type // T…, Production Practice…, Country of Origin /…

## g0012（1 列）
- 見出し：Inspection Sample Number // # d'inspection de l'echantillon
- 例1 値：S2020NCSK01066 | S2021MCSK01057 | S2020TCSK00930 | S2021OCSK00807 | S2020CCSK01188
  - 同じ表の列：Sample Plan Number …, Date Sampled YYYY/M…, Season // Saison, Product Type // Typ…, Product Subtype // …, Packaging Type // T…, Production Practice…, Country of Origin /…

## g0013（1 列）
- 見出し：Season // Saison
- 例1 値：Summer // Été | Winter // Hiver | Spring // Printemps | Summer // Été | Spring // Printemps
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Product Type // Typ…, Product Subtype // …, Packaging Type // T…, Production Practice…, Country of Origin /…

## g0014（1 列）
- 見出し：Product Type // Type de produit
- 例1 値：Fresh-cut // Fraîchement coupé | Trimmed // Paré | Fresh-cut // Fraîchement coupé | Fresh-cut // Fraîchement coupé | Trimmed // Paré
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Season // Saison, Product Subtype // …, Packaging Type // T…, Production Practice…, Country of Origin /…

## g0015（1 列）
- 見出し：Product Subtype // Sous-type de produit
- 例1 値：Romaine lettuce // Laitue romaine | Mixed vegetables // Légumes mélangés | Chard // Bette à carde | Mixed vegetables // Légumes mélangés | Baby arugula // Jeunes pousses de roque…
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Season // Saison, Product Type // Typ…, Packaging Type // T…, Production Practice…, Country of Origin /…

## g0016（1 列）
- 見出し：Packaging Type // Type d'emballage
- 例1 値：Pre-packaged // Préemballé | Pre-packaged // Préemballé | Pre-packaged // Préemballé | Pre-packaged // Préemballé | Pre-packaged // Préemballé
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Season // Saison, Product Type // Typ…, Product Subtype // …, Production Practice…, Country of Origin /…

## g0017（1 列）
- 見出し：Country of Origin // Pays d'origine
- 例1 値：United States // États-Unis | United States // États-Unis | United States // États-Unis | United States // États-Unis | United States // États-Unis
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Season // Saison, Product Type // Typ…, Product Subtype // …, Packaging Type // T…, Production Practice…

## g0018（2 列）
- 見出し：Domestic and/or Import // Canadienne et/ou Importation
- 例1 値：Import // Importation | Import // Importation | Import // Importation | Import // Importation | Import // Importation
  - 同じ表の列：Sample Plan Number …, Inspection Sample N…, Date Sampled YYYY/M…, Season // Saison, Product Type // Typ…, Product Subtype // …, Packaging Type // T…, Production Practice…
- 例2 値：Unknown // Inconnue | Unknown // Inconnue | Unknown // Inconnue | Unknown // Inconnue | Unknown // Inconnue
  - 同じ表の列：Sample Plan Number …, System ID // ID sys…, Job Laboratory Numb…, Date Sampled YYYY/M…, Product Type // Typ…, Product Subtype // …, Country of Origin /…, Analysis Type // Ty…

## g0019（1 列）
- 見出し：System ID // ID systeme
- 例1 値：B2024TSIL04893 | B2024VSIL01533 | B2024OSIL04383 | B2024VSIL06771 | B2024TSIL06310
  - 同じ表の列：Sample Plan Number …, Job Laboratory Numb…, Date Sampled YYYY/M…, Product Type // Typ…, Product Subtype // …, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…

## g0020（1 列）
- 見出し：Job Laboratory Number // Tache - numero de laboratoire
- 例1 値：B2024TSIL00972 | B2024OSIL05295 | B2024MSIL00970 | B2024TSIL05801 | B2024TSIL03834
  - 同じ表の列：Sample Plan Number …, System ID // ID sys…, Date Sampled YYYY/M…, Product Type // Typ…, Product Subtype // …, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…

## g0021（1 列）
- 見出し：Product Type // Type de produit
- 例1 値：Refrigerated raw fish paste // Pâte de … | Refrigerated raw fish paste // Pâte de … | Refrigerated raw fish paste // Pâte de … | Refrigerated raw fish paste // Pâte de … | Refrigerated raw fish paste // Pâte de …
  - 同じ表の列：Sample Plan Number …, System ID // ID sys…, Job Laboratory Numb…, Date Sampled YYYY/M…, Product Subtype // …, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…

## g0022（1 列）
- 見出し：Product Subtype // Sous-type de produit
- 例1 値：Dace // Carpe | Cuttlefish // Seiche | Dace // Carpe | Dace // Carpe | Dace // Carpe
  - 同じ表の列：Sample Plan Number …, System ID // ID sys…, Job Laboratory Numb…, Date Sampled YYYY/M…, Product Type // Typ…, Country of Origin /…, Domestic and/or Imp…, Analysis Type // Ty…

## g0023（1 列）
- 見出し：Country of Origin // Pays d'origine
- 例1 値：Unknown (Prepared in Canada) // Inconnu… | Unknown (Prepared in Canada) // Inconnu… | Unknown (Prepared in Canada) // Inconnu… | Unknown (Prepared in Canada) // Inconnu… | Unknown // Inconnu
  - 同じ表の列：Sample Plan Number …, System ID // ID sys…, Job Laboratory Numb…, Date Sampled YYYY/M…, Product Type // Typ…, Product Subtype // …, Domestic and/or Imp…, Analysis Type // Ty…

## g0024（1 列）
- 見出し：Analysis Type // Type d'analyse
- 例1 値：Salmonella | Salmonella | Aerobic Colony Count // Numération des … | Staphylococcus aureus | Aerobic Colony Count // Numération des …
  - 同じ表の列：Sample Plan Number …, System ID // ID sys…, Job Laboratory Numb…, Date Sampled YYYY/M…, Product Type // Typ…, Product Subtype // …, Country of Origin /…, Domestic and/or Imp…

## g0025（1 列）
- 見出し：Province or territory
- 例1 値：Ontario | Yukon | Prince Edward Island | Alberta | Newfoundland and Labrador
  - 同じ表の列：Population segment, Age group, Tax filing rate (%), Number of linked po…, Number of tax filer…, Number of non-filer…, Canada Child Benefi…, Families with child…

## g0026（1 列）
- 見出し：Population segment
- 例1 値：Youth | Youth | Canadian residents | Housing insecure individuals | Indigenous Peoples
  - 同じ表の列：Province or territo…, Age group, Tax filing rate (%), Number of linked po…, Number of tax filer…, Number of non-filer…, Canada Child Benefi…, Families with child…

## g0027（1 列）
- 見出し：Age group
- 例1 値：18 years and older | 18 years and older | 18 years and older | 18 years and older | 18 years and older
  - 同じ表の列：Province or territo…, Population segment, Tax filing rate (%), Number of linked po…, Number of tax filer…, Number of non-filer…, Canada Child Benefi…, Families with child…

## g0028（1 列）
- 見出し：Tax filing rate (%)
- 例1 値：88.40% | 96.30% | 98.20% | 89.90% | 87.60%
  - 同じ表の列：Province or territo…, Population segment, Age group, Number of linked po…, Number of tax filer…, Number of non-filer…, Canada Child Benefi…, Families with child…

## g0029（1 列）
- 見出し：Number of linked population (#)
- 例1 値：814,200 | 1,975,800 | 366,190 | 55,170 | 4,982,760
  - 同じ表の列：Province or territo…, Population segment, Age group, Tax filing rate (%), Number of tax filer…, Number of non-filer…, Canada Child Benefi…, Families with child…

## g0030（1 列）
- 見出し：Number of tax filers (#)
- 例1 値：23,905 | 199,615 | 132,340 | 316,075 | 194,875
  - 同じ表の列：Province or territo…, Population segment, Age group, Tax filing rate (%), Number of linked po…, Number of non-filer…, Canada Child Benefi…, Families with child…

## g0031（1 列）
- 見出し：Number of non-filers (#)
- 例1 値：4,705 | 3,080 | 70 | 20,375 | 620
  - 同じ表の列：Province or territo…, Population segment, Age group, Tax filing rate (%), Number of linked po…, Number of tax filer…, Canada Child Benefi…, Families with child…

## g0032（1 列）
- 見出し：Canada Child Benefit (CCB) participation rate (%)
- 例1 値：87.70% | 91.30% | 70.00% | 72.10% | 88.90%
  - 同じ表の列：Province or territo…, Population segment, Age group, Tax filing rate (%), Number of linked po…, Number of tax filer…, Number of non-filer…, Families with child…

## g0033（1 列）
- 見出し：Families with child(ren) under 18 receiving CCB (#)
- 例1 値：205 | 1,905 | 57,165 | 9,160 | 100,185
  - 同じ表の列：Province or territo…, Population segment, Age group, Tax filing rate (%), Number of linked po…, Number of tax filer…, Number of non-filer…, Canada Child Benefi…

## g0034（1 列）
- 見出し：Total Canada Child Benefit (CCB) amount received ($)
- 例1 値：$58,400,000 | $2,620,000,000 | $1,360,000 | $5,040,000 | $14,640,000
  - 同じ表の列：Province or territo…, Population segment, Age group, Tax filing rate (%), Number of linked po…, Number of tax filer…, Number of non-filer…, Canada Child Benefi…

## g0035（2 列）
- 見出し：departmental_identification_number
- 例1 値：OI-545 | OI-577 | OI-577 | OI-1146 | OI-560
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published
- 例2 値：OI-1000 | OI-1085 | OI-562 | OI-465 | OI-1147
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0036（1 列）
- 見出し：title_translated_en
- 例1 値：CPTPP: Ice Cream and Mixes TRQ - Serial… | Notice to Importers Ice Cream and Ice C… | Notice to Importers Ice Cream and Ice C… | Ice Cream Quota Holders List - 2016 | Ice Cream and Ice Cream Novelties Quota…
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0037（1 列）
- 見出し：title_translated_fr
- 例1 値：Liste des détenteurs de contingent pour… | Liste des détenteurs de contingent de c… | Liste des détenteurs de contingent pour… | Liste des détenteurs de contingent de c… | ACEUM : CT de crème glacée et mélanges …
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0038（1 列）
- 見出し：notes_translated_en
- 例1 値：Notice to Importers Ice Cream and Ice C… | WTO Ice Cream and Ice Cream Novelties Q… | In Brief Imports of ice cream and ice c… | CPTPP Ice Cream and Mixes Quota Holders… | Utilization Data - Ice Cream.
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0039（1 列）
- 見出し：notes_translated_fr
- 例1 値：Liste des détenteurs de contingent pour… | Liste des détenteurs de contingent pour… | Liste des détenteurs de contingent pour… | Donnée sur l'utilisation - Crème glacée. | PTPGP : CT de crème glacée et mélanges
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0040（2 列）
- 見出し：organization_title_en
- 例1 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published
- 例2 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0041（2 列）
- 見出し：organization_title_fr
- 例1 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published
- 例2 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0042（2 列）
- 見出し：subject
- 例1 値：economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published
- 例2 値：economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published

## g0043（2 列）
- 見出し：date_published
- 例1 値：2013-06-24 | 2020-06-15 | 2019-04-12 | 2015-04-22 | 2022-12-19
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject
- 例2 値：2019-05-02 | 2024-07-31 | 2019-05-01 | 2024-08-23 | 2024-02-12
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0044（2 列）
- 見出し：portal_type
- 例1 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject
- 例2 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0045（1 列）
- 見出し：title_translated_en
- 例1 値：CUSMA Powdered Buttermilk Quota Holders… | CUSMA: Concentrated or Condensed Milk T… | Milk Protein Substances Imports - Perio… | CPTPP Yogurt and Buttermilk Quota Holde… | CPTPP Milk Quota Holders List - 2020-20…
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0046（1 列）
- 見出し：title_translated_fr
- 例1 値：Lettre d’un expert-comptable - PTPGP : … | Liste des détenteurs de contingent tari… | PTPGP – Contingent tarifaire du lait (a… | Liste de détenteurs de contingent pour … | ACEUM : CT pour le lait écrémé en poudr…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0047（1 列）
- 見出し：notes_translated_en
- 例1 値：CUSMA: Yogurt and Buttermilk TRQ | CUSMA Milk Powders Quota Holders List. | CUSMA Yogurt and Buttermilk Quota Holde… | In Brief Imports of milk protein substa… | CPTPP Products Consisting of Natural Mi…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0048（1 列）
- 見出し：notes_translated_fr
- 例1 値：Liste des détenteurs de produits formés… | Liste des détenteurs de produits formés… | Liste des détenteurs de contingent pour… | Données sur l’utilisation - Yogourt et … | Donnée sur l'utilisation - Produits con…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0049（1 列）
- 見出し：Period
- 例1 値：Jan. / jan. 2013 | Dec. / déc. 2016 | Mar. / mar. 2014 | Sept. / sept. 2014 | Nov. / nov. 2012
  - 同じ表の列：Province, Retirement, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0050（1 列）
- 見出し：Province
- 例1 値：YUKON | ALBERTA | TOTAL | YUKON | N.W.T./T.N.-O.
  - 同じ表の列：Period, Retirement, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0051（1 列）
- 見出し：Retirement
- 例1 値：169 | 38 | 38 | 835 | 4,654
  - 同じ表の列：Period, Province, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0052（1 列）
- 見出し：Disability
- 例1 値：507 | X | 109 | 0 | 2,910
  - 同じ表の列：Period, Province, Retirement, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0053（1 列）
- 見出し：Children of Disabled Contributor (-18)
- 例1 値：1,037 | 145 | 21 | X | X
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0054（1 列）
- 見出し：Children of Disabled Contributor (18-24)
- 例1 値：0 | 120 | X | 0 | 55
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0055（1 列）
- 見出し：Survivor's
- 例1 値：0 | 0 | 153 | 239 | X
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Children of Disable…, Children of Decease…, Children of Decease…

## g0056（1 列）
- 見出し：Children of Deceased Contributor (-18)
- 例1 値：268 | 554 | X | X | X
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…

## g0057（1 列）
- 見出し：Children of Deceased Contributor (18-24)
- 例1 値：X | 0 | X | 211 | 130
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…

## g0058（1 列）
- 見出し：Post Retirement Benefit
- 例1 値：0 | 0 | 116 | 450 | X
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…

## g0059（1 列）
- 見出し：Financial Institution
- 例1 値：Canadian Imperial Bank of Commerce | Royal Bank of Canada | Royal Bank of Canada | Royal Bank of Canada | Toronto-Dominion Bank
  - 同じ表の列：Maintenance fee, Minimum daily balan…, Transaction limit, Separate Interac e-…, ATM network access …

## g0060（1 列）
- 見出し：Maintenance fee
- 例1 値：$15.95 | $16.95 | $12.95 | $30.95 | $17.95
  - 同じ表の列：Financial Instituti…, Minimum daily balan…, Transaction limit, Separate Interac e-…, ATM network access …

## g0061（1 列）
- 見出し：Minimum daily balance to waive maintenance fee
- 例1 値：- | - | - | - | $4,000
  - 同じ表の列：Financial Instituti…, Maintenance fee, Transaction limit, Separate Interac e-…, ATM network access …

## g0062（1 列）
- 見出し：Transaction limit
- 例1 値：Unlimited | Unlimited | 18 | 25 | 18
  - 同じ表の列：Financial Instituti…, Maintenance fee, Minimum daily balan…, Separate Interac e-…, ATM network access …

## g0063（1 列）
- 見出し：Separate Interac e-transfer limit (if applicable)
- 例1 値：- | - | - | - | -
  - 同じ表の列：Financial Instituti…, Maintenance fee, Minimum daily balan…, Transaction limit, ATM network access …

## g0064（1 列）
- 見出し：ATM network access fee
- 例1 値：$2.00 | $2.00 | $2.00 | $0.00 | $2.00
  - 同じ表の列：Financial Instituti…, Maintenance fee, Minimum daily balan…, Transaction limit, Separate Interac e-…

## g0065（1 列）
- 見出し：FoodCode
- 例1 値：2920 | 1378 | 1587 | 114 | 2617
  - 同じ表の列：Type, Recipe_Type

## g0066（1 列）
- 見出し：Type
- 例1 値：Food | Food | Food | Food | Food
  - 同じ表の列：FoodCode, Recipe_Type

## g0067（1 列）
- 見出し：Recipe_Type
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：FoodCode, Type

## g0068（1 列）
- 見出し：RESPID
- 例1 値：5592 | 3763 | 1745 | 3828 | 4805
  - 同じ表の列：L, Q26, Q27, Q35A, Q33, Q34_1, Q34_2, Q34_3

## g0069（1 列）
- 見出し：L
- 例1 値：French (Canada) | English | English | English | English
  - 同じ表の列：RESPID, Q26, Q27, Q35A, Q33, Q34_1, Q34_2, Q34_3

## g0070（1 列）
- 見出し：Q26
- 例1 値：Male | Male | Male | Female | Male
  - 同じ表の列：RESPID, L, Q27, Q35A, Q33, Q34_1, Q34_2, Q34_3

## g0071（1 列）
- 見出し：Q27
- 例1 値：30-34 | 65 or older | 45-49 | 45-49 | 55-59
  - 同じ表の列：RESPID, L, Q26, Q35A, Q33, Q34_1, Q34_2, Q34_3

## g0072（1 列）
- 見出し：Q35A
- 例1 値：Ontario | Ontario | Ontario | Ontario | British Columbia
  - 同じ表の列：RESPID, L, Q26, Q27, Q33, Q34_1, Q34_2, Q34_3

## g0073（1 列）
- 見出し：Q33
- 例1 値：2 | 1 | 2 | 2 | 3
  - 同じ表の列：RESPID, L, Q26, Q27, Q35A, Q34_1, Q34_2, Q34_3

## g0074（1 列）
- 見出し：Q34_1
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：RESPID, L, Q26, Q27, Q35A, Q33, Q34_2, Q34_3

## g0075（1 列）
- 見出し：Q34_2
- 例1 値：0 | 0 | 1 | 0 | 0
  - 同じ表の列：RESPID, L, Q26, Q27, Q35A, Q33, Q34_1, Q34_3

## g0076（1 列）
- 見出し：Q34_3
- 例1 値：1 | 0 | 1 | 0 | 1
  - 同じ表の列：RESPID, L, Q26, Q27, Q35A, Q33, Q34_1, Q34_2

## g0077（1 列）
- 見出し：Q34_4
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：RESPID, L, Q26, Q27, Q35A, Q33, Q34_1, Q34_2

## g0078（1 列）
- 見出し：Fiscal Year
- 例1 値：2017-2018 | 2017-2018 | 2017-2018 | 2017-2018 | 2017-2018
  - 同じ表の列：Fiscal Period, Month, Information Date, Branch, Service, SSC Client, Value, Metric Type

## g0079（1 列）
- 見出し：Fiscal Period
- 例1 値：7 | 3 | 3 | 7 | 7
  - 同じ表の列：Fiscal Year, Month, Information Date, Branch, Service, SSC Client, Value, Metric Type

## g0080（1 列）
- 見出し：Month
- 例1 値：July | June | April | October | October
  - 同じ表の列：Fiscal Year, Fiscal Period, Information Date, Branch, Service, SSC Client, Value, Metric Type

## g0081（1 列）
- 見出し：Information Date
- 例1 値：6/30/2017 | 4/30/2017 | 10/31/2017 | 10/31/2017 | 6/30/2017
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Branch, Service, SSC Client, Value, Metric Type

## g0082（1 列）
- 見出し：Branch
- 例1 値：Data Centre Services | Data Centre Services | Data Centre Services | Data Centre Services | Data Centre Services
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Service, SSC Client, Value, Metric Type

## g0083（1 列）
- 見出し：Service
- 例1 値：DC Facilities - Legacy | DC Facilities - Legacy | DC Facilities - Legacy | DC Facilities - Legacy | DC Facilities - Legacy
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, SSC Client, Value, Metric Type

## g0084（1 列）
- 見出し：SSC Client
- 例1 値：Canadian Heritage | Environment and Climate Change Canada | Immigration and Refugee Board of Canada | Health Canada | National Defence
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, Value, Metric Type

## g0085（1 列）
- 見出し：Value
- 例1 値：2 | 1 | 2 | 0 | 2
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, SSC Client, Metric Type

## g0086（1 列）
- 見出し：Metric Type
- 例1 値：Cumulative | As at | As at | As at | Cumulative
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, SSC Client, Value

## g0087（1 列）
- 見出し：RECALL_NUMBER_NUM
- 例1 値：2021368 | 2021256 | 2021368 | 2021563 | 2020282
  - 同じ表の列：YEAR, CATEGORY_ETXT, CATEGORY_FTXT, UNIT_AFFECTED_NBR, SYSTEM_TYPE_ETXT, SYSTEM_TYPE_FTXT, NOTIFICATION_TYPE_E…, NOTIFICATION_TYPE_F…

## g0088（1 列）
- 見出し：YEAR
- 例1 値：2007 | 2020 | 2019 | 2020 | 2014
  - 同じ表の列：RECALL_NUMBER_NUM, CATEGORY_ETXT, CATEGORY_FTXT, UNIT_AFFECTED_NBR, SYSTEM_TYPE_ETXT, SYSTEM_TYPE_FTXT, NOTIFICATION_TYPE_E…, NOTIFICATION_TYPE_F…

## g0089（1 列）
- 見出し：CATEGORY_ETXT
- 例1 値：RV Trailer | RV Trailer | SUV | A.T.V. | Motorcycle
  - 同じ表の列：RECALL_NUMBER_NUM, YEAR, CATEGORY_FTXT, UNIT_AFFECTED_NBR, SYSTEM_TYPE_ETXT, SYSTEM_TYPE_FTXT, NOTIFICATION_TYPE_E…, NOTIFICATION_TYPE_F…

## g0090（1 列）
- 見出し：CATEGORY_FTXT
- 例1 値：Véhicule utilitaire-sport | Camion - usage moyen et usage intensif | Remorque lourde | Véhicule utilitaire-sport | Camionnette et fourgonnette
  - 同じ表の列：RECALL_NUMBER_NUM, YEAR, CATEGORY_ETXT, UNIT_AFFECTED_NBR, SYSTEM_TYPE_ETXT, SYSTEM_TYPE_FTXT, NOTIFICATION_TYPE_E…, NOTIFICATION_TYPE_F…

## g0091（1 列）
- 見出し：UNIT_AFFECTED_NBR
- 例1 値：719.00 | 3,185.00 | 14,368.00 | 43,618.00 | 3,838.00
  - 同じ表の列：RECALL_NUMBER_NUM, YEAR, CATEGORY_ETXT, CATEGORY_FTXT, SYSTEM_TYPE_ETXT, SYSTEM_TYPE_FTXT, NOTIFICATION_TYPE_E…, NOTIFICATION_TYPE_F…

## g0092（1 列）
- 見出し：SYSTEM_TYPE_ETXT
- 例1 値：Accessories | Steering | Powertrain | Brakes | Fuel Supply
  - 同じ表の列：RECALL_NUMBER_NUM, YEAR, CATEGORY_ETXT, CATEGORY_FTXT, UNIT_AFFECTED_NBR, SYSTEM_TYPE_FTXT, NOTIFICATION_TYPE_E…, NOTIFICATION_TYPE_F…

## g0093（1 列）
- 見出し：SYSTEM_TYPE_FTXT
- 例1 値：Freins | Direction | Alimentation en carburant | Accessoires | Structure
  - 同じ表の列：RECALL_NUMBER_NUM, YEAR, CATEGORY_ETXT, CATEGORY_FTXT, UNIT_AFFECTED_NBR, SYSTEM_TYPE_ETXT, NOTIFICATION_TYPE_E…, NOTIFICATION_TYPE_F…

## g0094（1 列）
- 見出し：NOTIFICATION_TYPE_ETXT
- 例1 値：Safety Mfr | Safety Mfr | Safety Mfr | Safety Mfr | Safety Mfr
  - 同じ表の列：RECALL_NUMBER_NUM, YEAR, CATEGORY_ETXT, CATEGORY_FTXT, UNIT_AFFECTED_NBR, SYSTEM_TYPE_ETXT, SYSTEM_TYPE_FTXT, NOTIFICATION_TYPE_F…

## g0095（1 列）
- 見出し：NOTIFICATION_TYPE_FTXT
- 例1 値：Sécurité - fabricant | Campagne d'entretien du fabricant | Conformité - fabricant | Sécurité - fabricant | Conformité - fabricant
  - 同じ表の列：RECALL_NUMBER_NUM, YEAR, CATEGORY_ETXT, CATEGORY_FTXT, UNIT_AFFECTED_NBR, SYSTEM_TYPE_ETXT, SYSTEM_TYPE_FTXT, NOTIFICATION_TYPE_E…

## g0096（1 列）
- 見出し：RECALL_DATE_DTE
- 例1 値：2020-07-16 | 2019-07-04 | 2021-05-27 | 2021-06-10 | 2021-06-10
  - 同じ表の列：RECALL_NUMBER_NUM, YEAR, CATEGORY_ETXT, CATEGORY_FTXT, UNIT_AFFECTED_NBR, SYSTEM_TYPE_ETXT, SYSTEM_TYPE_FTXT, NOTIFICATION_TYPE_E…

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
```
