# ラベル用シート 007 / 008

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_007.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0721（1 列）
- 見出し：title_translated_en
- 例1 値：Notice to Importers Eggs and Egg Produc… | Utilization Data - Eggs and Egg Product… | Notice to Importers Broiler Hatching Eg… | CPTPP Import Permits Issuance - Eggs fo… | Notices to Importers Broiler Hatching E…
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0722（1 列）
- 見出し：title_translated_fr
- 例1 値：Liste des détenteurs de contingent des … | Oeufs et ovoproduits : Oeufs a craquer … | Délivrance de Permis d'Importation PTPG… | Avis aux importateurs des œufs d’incuba… | Oeufs d'incubation de poulet et poussin…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0723（1 列）
- 見出し：notes_translated_en
- 例1 値：WTO Egg and Egg Product Quota Holders L… | Utilization Data - Eggs and Egg Product… | Eggs and Egg Products (Item 135 To 139 … | Broiler Hatching Eggs and Chicks for Ch… | CPTPP Eggs Quota Holders List.
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0724（1 列）
- 見出し：notes_translated_fr
- 例1 値：Oeufs et ovoproduits (Articles 135 à 13… | Oeufs d'incubation de poulets de chair … | PTPGP oeufs et ovoproduits liste des dé… | Rapport de prix moyen des oeufs d’incub… | 1.1 Le présent Avis a pour objet: a) d'…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0725（1 列）
- 見出し：title_translated_en
- 例1 値：Notice to Importers: Dairy – CETA Chees… | CUSMA Cheeses of All Types Quota Holder… | Accountant’s letter - CPTPP: Industrial… | WTO Cheeses of All Types Quota Holders … | CUSMA Cheeses of All Types Quota Holder…
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0726（1 列）
- 見出し：title_translated_fr
- 例1 値：OMC : CT pour les fromages de tous type… | Avis aux importateurs : Produits laitie… | Liste des détenteurs de contingent pour… | Sommaire des importations sous continge… | Ouverture de la période de demande pour…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0727（1 列）
- 見出し：notes_translated_en
- 例1 値：CPTPP: Industrial Cheese TRQ | CUSMA cheese permits | CETA Industrial Cheese Tariff Rate Quot… | CUSMA: Industrial Cheeses TRQ | CPTPP cheese permits
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0728（1 列）
- 見出し：notes_translated_fr
- 例1 値：PTPGP: CT pour les fromages de tous typ… | Résumé du contingent tarifaire pour les… | Liste des détenteurs de contingent du f… | Liste des détenteurs de contingent pour… | Liste des détenteurs de contingent tari…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0729（1 列）
- 見出し：subject
- 例1 値：economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published

## g0730（1 列）
- 見出し：Groupe de services
- 例1 値：Téléphone | Traceur réseau | Total | COMPTES, COURRIELS ET MOTS DE PASSE | Téléconférence
  - 同じ表の列：Bagotville, Borden, Cold Lake, Comox, Edmonton, Esquimalt, Gagetown, Greenwood

## g0731（1 列）
- 見出し：Bagotville
- 例1 値：205 | 1288 | 0 | 891 | 259
  - 同じ表の列：Groupe de services, Borden, Cold Lake, Comox, Edmonton, Esquimalt, Gagetown, Greenwood

## g0732（1 列）
- 見出し：Borden
- 例1 値：96 | 277 | 143 | 2352 | 7
  - 同じ表の列：Groupe de services, Bagotville, Cold Lake, Comox, Edmonton, Esquimalt, Gagetown, Greenwood

## g0733（1 列）
- 見出し：Cold Lake
- 例1 値：11 | 8 | 0 | 2295 | 2
  - 同じ表の列：Groupe de services, Bagotville, Borden, Comox, Edmonton, Esquimalt, Gagetown, Greenwood

## g0734（1 列）
- 見出し：Comox
- 例1 値：41 | 7 | 142 | 1 | 0
  - 同じ表の列：Groupe de services, Bagotville, Borden, Cold Lake, Edmonton, Esquimalt, Gagetown, Greenwood

## g0735（1 列）
- 見出し：Edmonton
- 例1 値：75 | 0 | 10582 | 203 | 58
  - 同じ表の列：Groupe de services, Bagotville, Borden, Cold Lake, Comox, Esquimalt, Gagetown, Greenwood

## g0736（1 列）
- 見出し：Esquimalt
- 例1 値：26 | 1111 | 303 | 3614 | 648
  - 同じ表の列：Groupe de services, Bagotville, Borden, Cold Lake, Comox, Edmonton, Gagetown, Greenwood

## g0737（1 列）
- 見出し：Gagetown
- 例1 値：6 | 1126 | 13 | 0 | 171
  - 同じ表の列：Groupe de services, Bagotville, Borden, Cold Lake, Comox, Edmonton, Esquimalt, Greenwood

## g0738（1 列）
- 見出し：Greenwood
- 例1 値：1467 | 187 | 485 | 104 | 0
  - 同じ表の列：Groupe de services, Bagotville, Borden, Cold Lake, Comox, Edmonton, Esquimalt, Gagetown

## g0739（1 列）
- 見出し：Halifax
- 例1 値：88 | 573 | 0 | 7174 | 1
  - 同じ表の列：Groupe de services, Bagotville, Borden, Cold Lake, Comox, Edmonton, Esquimalt, Gagetown

## g0740（1 列）
- 見出し：Month
- 例1 値：Sept. / sept. | - | Dec. / déc. | - | Feb. / fév.
  - 同じ表の列：Year, Retirement Pension, Post Retirement Ben…, Disability Pension, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…

## g0741（1 列）
- 見出し：Retirement Pension
- 例1 値：134.97 | 1,178.77 | 727.08 | 775 | 1,372.86
  - 同じ表の列：Year, Month, Post Retirement Ben…, Disability Pension, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…

## g0742（1 列）
- 見出し：Post Retirement Benefit
- 例1 値：36.26 | 30.87 | - | - | -
  - 同じ表の列：Year, Month, Retirement Pension, Disability Pension, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…

## g0743（1 列）
- 見出し：Disability Pension
- 例1 値：1,390.23 | 1,390.60 | 1,612.09 | 1,466.29 | 1,153.37
  - 同じ表の列：Year, Month, Retirement Pension, Post Retirement Ben…, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…

## g0744（1 列）
- 見出し：Survivor's Pension, Under 65
- 例1 値：675.03 | 626.72 | 770.88 | 604.32 | 99.51
  - 同じ表の列：Year, Month, Retirement Pension, Post Retirement Ben…, Disability Pension, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…

## g0745（1 列）
- 見出し：Survivor's Pension, Under 65 (pension begins in January)
- 例1 値：- | - | - | - | -
  - 同じ表の列：Year, Month, Retirement Pension, Post Retirement Ben…, Disability Pension, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…

## g0746（1 列）
- 見出し：Survivor's Pension, 65 and over
- 例1 値：130.84 | 911.13 | 693.54 | 820.18 | 753.32
  - 同じ表の列：Year, Month, Retirement Pension, Post Retirement Ben…, Disability Pension, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…

## g0747（1 列）
- 見出し：Survivor's Pension, Over 65 (pension begins in January)
- 例1 値：747.37 | - | - | - | -
  - 同じ表の列：Year, Month, Retirement Pension, Post Retirement Ben…, Disability Pension, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…

## g0748（1 列）
- 見出し：Children of Disabled or Deceased Contributor Benefits
- 例1 値：218.5 | 255.03 | 224.62 | 264.53 | 244.64
  - 同じ表の列：Year, Month, Retirement Pension, Post Retirement Ben…, Disability Pension, Survivor's Pension,…, Survivor's Pension,…, Survivor's Pension,…

## g0749（1 列）
- 見出し：Retirement
- 例1 値：2,695,480 | 3,425,009 | 4,025,904 | 2,369,019 | 5,200,832
  - 同じ表の列：Year, Disability, Child's -18, Child's 18-24, Survivor, Orphan's -18, Orphan's 18-24, Total

## g0750（1 列）
- 見出し：Disability
- 例1 値：155,077 | 279,247 | 296,329 | 300,118 | 84,795
  - 同じ表の列：Year, Retirement, Child's -18, Child's 18-24, Survivor, Orphan's -18, Orphan's 18-24, Total

## g0751（1 列）
- 見出し：Child's -18
- 例1 値：69,009 | 34,235 | 67,145 | 28,834 | 67,520
  - 同じ表の列：Year, Retirement, Disability, Child's 18-24, Survivor, Orphan's -18, Orphan's 18-24, Total

## g0752（1 列）
- 見出し：Child's 18-24
- 例1 値：14,344 | 6,999 | 17,497 | 20,408 | 21,927
  - 同じ表の列：Year, Retirement, Disability, Child's -18, Survivor, Orphan's -18, Orphan's 18-24, Total

## g0753（1 列）
- 見出し：Survivor
- 例1 値：356,290 | 1,022,886 | Survivant | 1,183,862 | 890,783
  - 同じ表の列：Year, Retirement, Disability, Child's -18, Child's 18-24, Orphan's -18, Orphan's 18-24, Total

## g0754（1 列）
- 見出し：Orphan's -18
- 例1 値：80,530 | 69,601 | 47,140 | 55,369 | 83,360
  - 同じ表の列：Year, Retirement, Disability, Child's -18, Child's 18-24, Survivor, Orphan's 18-24, Total

## g0755（1 列）
- 見出し：Orphan's 18-24
- 例1 値：23,557 | 11,651 | 16,199 | 25,628 | 26,225
  - 同じ表の列：Year, Retirement, Disability, Child's -18, Child's 18-24, Survivor, Orphan's -18, Total

## g0756（1 列）
- 見出し：Total
- 例1 値：1,471,610 | 6,292,127 | 6,811,708 | 3,928,480 | 6,472,184
  - 同じ表の列：Year, Retirement, Disability, Child's -18, Child's 18-24, Survivor, Orphan's -18, Orphan's 18-24

## g0757（1 列）
- 見出し：Post Retirement
- 例1 値：5,588,148 | ... | ... | Après - retraite | ...
  - 同じ表の列：Year, Retirement, Disability, Child's -18, Child's 18-24, Survivor, Orphan's -18, Orphan's 18-24

## g0758（1 列）
- 見出し：Benefits/Prestations
- 例1 値：Disability Benefit/Prestation d'invalid… | Retirement Pension/Pension de retraite | Disability Benefit/Prestation d'invalid… | Retirement Pension/Pension de retraite | Survivor Benefit/Prestation de survivant
  - 同じ表の列：Gender/Sexe, June/Juin 1981, June/Juin 1982, June/Juin 1983, June/Juin 1984, June/Juin 1985, June/Juin 1986, June/Juin 1987

## g0759（1 列）
- 見出し：Gender/Sexe
- 例1 値：Male/Sexe masculin | Male/Sexe masculin | Female/Sexe féminin | Male/Sexe masculin | Female/Sexe féminin
  - 同じ表の列：Benefits/Prestations, June/Juin 1981, June/Juin 1982, June/Juin 1983, June/Juin 1984, June/Juin 1985, June/Juin 1986, June/Juin 1987

## g0760（1 列）
- 見出し：June/Juin 1981
- 例1 値：62,995 | 245,713 | 27,185 | 576,176 | 17,932
  - 同じ表の列：Benefits/Prestations, Gender/Sexe, June/Juin 1982, June/Juin 1983, June/Juin 1984, June/Juin 1985, June/Juin 1986, June/Juin 1987

## g0761（1 列）
- 見出し：June/Juin 1982
- 例1 値：608,542 | 30,111 | 20,623 | 68,315 | 306,873
  - 同じ表の列：Benefits/Prestations, Gender/Sexe, June/Juin 1981, June/Juin 1983, June/Juin 1984, June/Juin 1985, June/Juin 1986, June/Juin 1987

## g0762（1 列）
- 見出し：June/Juin 1983
- 例1 値：335,905 | 297,491 | 77,008 | 638,391 | 23,562
  - 同じ表の列：Benefits/Prestations, Gender/Sexe, June/Juin 1981, June/Juin 1982, June/Juin 1984, June/Juin 1985, June/Juin 1986, June/Juin 1987

## g0763（1 列）
- 見出し：June/Juin 1984
- 例1 値：667,770 | 85,838 | 25,879 | 366,400 | 323,099
  - 同じ表の列：Benefits/Prestations, Gender/Sexe, June/Juin 1981, June/Juin 1982, June/Juin 1983, June/Juin 1985, June/Juin 1986, June/Juin 1987

## g0764（1 列）
- 見出し：June/Juin 1985
- 例1 値：38,735 | 705,216 | 93,967 | 348,218 | 403,539
  - 同じ表の列：Benefits/Prestations, Gender/Sexe, June/Juin 1981, June/Juin 1982, June/Juin 1983, June/Juin 1984, June/Juin 1986, June/Juin 1987

## g0765（1 列）
- 見出し：June/Juin 1986
- 例1 値：42,488 | 442,182 | 376,656 | 741,769 | 102,582
  - 同じ表の列：Benefits/Prestations, Gender/Sexe, June/Juin 1981, June/Juin 1982, June/Juin 1983, June/Juin 1984, June/Juin 1985, June/Juin 1987

## g0766（1 列）
- 見出し：June/Juin 1987
- 例1 値：44,124 | 422,217 | 545,946 | 106,319 | 38,221
  - 同じ表の列：Benefits/Prestations, Gender/Sexe, June/Juin 1981, June/Juin 1982, June/Juin 1983, June/Juin 1984, June/Juin 1985, June/Juin 1986

## g0767（1 列）
- 見出し：June/Juin 1988
- 例1 値：605,685 | 42,977 | 456,111 | 907,603 | 47,332
  - 同じ表の列：Benefits/Prestations, Gender/Sexe, June/Juin 1981, June/Juin 1982, June/Juin 1983, June/Juin 1984, June/Juin 1985, June/Juin 1986

## g0768（1 列）
- 見出し：System
- 例1 値：Pickering | Point Lepreau | Ottawa Valley | Regional | Gentilly
  - 同じ表の列：Station, Month, Ar41 (nGy/month), Xe133 (nGy/month), Xe135 (nGy/month), Air KERMA (nGy/mont…

## g0769（1 列）
- 見出し：Station
- 例1 値：Petewawa | London | Infocentre | London | Chalk River
  - 同じ表の列：System, Month, Ar41 (nGy/month), Xe133 (nGy/month), Xe135 (nGy/month), Air KERMA (nGy/mont…

## g0770（4 列）
- 見出し：Month
- 例1 値：May | Jun | Feb | Jun | Mar
  - 同じ表の列：System, Station, Ar41 (nGy/month), Xe133 (nGy/month), Xe135 (nGy/month), Air KERMA (nGy/mont…
- 例2 値：November | April | June | December | May
  - 同じ表の列：Fiscal Year, Fiscal Period, Information Date, Branch, Service, Value, Comments, Metric Type

## g0771（1 列）
- 見出し：Ar41 (nGy/month)
- 例1 値：- | - | - | - | x
  - 同じ表の列：System, Station, Month, Xe133 (nGy/month), Xe135 (nGy/month), Air KERMA (nGy/mont…

## g0772（1 列）
- 見出し：Xe133 (nGy/month)
- 例1 値：- | - | - | - | -
  - 同じ表の列：System, Station, Month, Ar41 (nGy/month), Xe135 (nGy/month), Air KERMA (nGy/mont…

## g0773（1 列）
- 見出し：Xe135 (nGy/month)
- 例1 値：- | - | - | - | -
  - 同じ表の列：System, Station, Month, Ar41 (nGy/month), Xe133 (nGy/month), Air KERMA (nGy/mont…

## g0774（1 列）
- 見出し：Air KERMA (nGy/month)
- 例1 値：15627 | 11722 | x | 19047 | 20375
  - 同じ表の列：System, Station, Month, Ar41 (nGy/month), Xe133 (nGy/month), Xe135 (nGy/month)

## g0775（1 列）
- 見出し：EMDatasetID_EMJeuID
- 例1 値：EM145 | EM145 | EM145 | EM145 | EM145
  - 同じ表の列：id, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs, ObsSampleComments_O…

## g0776（1 列）
- 見出し：DatasetID_IDJeu
- 例1 値：259 | 402 | 365 | 36 | 292
  - 同じ表の列：id, EMDatasetID_EMJeuID, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs, ObsSampleComments_O…

## g0777（1 列）
- 見出し：SampleID_IDEchantillon
- 例1 値：ABIBAL_BL117-AF-OL | RHOGRO_BL4040-CB-OL | CHAANG_BL117-CB-OL | CORCAN_BL4040-AF-SL | SPIANN_BL117-AF-OL
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs, ObsSampleComments_O…

## g0778（1 列）
- 見出し：TOPICSpeciesCode_CodeEspTOPIC
- 例1 値：CORCAN | ALNVIR | LINBOR | VIBEDU | ALNCRI
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs, ObsSampleComments_O…

## g0779（1 列）
- 見出し：TraitCode
- 例1 値：SLA | SLA | SLA | LA | LA
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, ObsTraitValue_Valeu…, ObsUnit_UniteObs, ObsSampleComments_O…

## g0780（1 列）
- 見出し：ObsTraitValue_ValeurTraitObs
- 例1 値：121.13 | 0.07557 | 0.00519 | 1.5693 | 2.11481
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsUnit_UniteObs, ObsSampleComments_O…

## g0781（1 列）
- 見出し：ObsUnit_UniteObs
- 例1 値：cm2 | g | cm2 g-1 | cm2 g-1 | cm2 g-1
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsSampleComments_O…

## g0782（1 列）
- 見出し：ObsSampleComments_ObsEchantillonsCommentaires
- 例1 値：Number of leaves used: 20 | Number of leaves used: 17 | Number of leaves used: 15 | Number of leaves used: 20 | Number of leaves used: 10
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs

## g0783（1 列）
- 見出し：EMPlotID_EMIDParcelle
- 例1 値：EM145-3 | EM145-4 | EM145-3 | EM145-1 | EM145-4
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs

## g0784（1 列）
- 見出し：eu_ID
- 例1 値：14 | 5 | 13 | 23 | 20
  - 同じ表の列：su_ID, eu_su_ID, LAT, LONG, ELEV, Insect, Logging, Horizon

## g0785（1 列）
- 見出し：su_ID
- 例1 値：4 | 2 | 1 | 4 | 1
  - 同じ表の列：eu_ID, eu_su_ID, LAT, LONG, ELEV, Insect, Logging, Horizon

## g0786（1 列）
- 見出し：eu_su_ID
- 例1 値：192 | 43 | 221 | 213 | 225
  - 同じ表の列：eu_ID, su_ID, LAT, LONG, ELEV, Insect, Logging, Horizon

## g0787（1 列）
- 見出し：LAT
- 例1 値：47.3017 | 47.27369 | 47.24406 | 47.31847 | 47.3092
  - 同じ表の列：eu_ID, su_ID, eu_su_ID, LONG, ELEV, Insect, Logging, Horizon

## g0788（1 列）
- 見出し：LONG
- 例1 値：-71.20885 | -71.19939 | -71.21749 | -71.13288 | -71.21665
  - 同じ表の列：eu_ID, su_ID, eu_su_ID, LAT, ELEV, Insect, Logging, Horizon

## g0789（1 列）
- 見出し：ELEV
- 例1 値：853 | 630 | 821 | 756 | 763
  - 同じ表の列：eu_ID, su_ID, eu_su_ID, LAT, LONG, Insect, Logging, Horizon

## g0790（1 列）
- 見出し：Insect
- 例1 値：Defoliated | Natural | Defoliated | Natural | Natural
  - 同じ表の列：eu_ID, su_ID, eu_su_ID, LAT, LONG, ELEV, Logging, Horizon

## g0791（1 列）
- 見出し：Logging
- 例1 値：Cut | Cut | Uncut | Uncut | Uncut
  - 同じ表の列：eu_ID, su_ID, eu_su_ID, LAT, LONG, ELEV, Insect, Horizon

## g0792（1 列）
- 見出し：Horizon
- 例1 値：FH | FH | Mineral | FH | Mineral
  - 同じ表の列：eu_ID, su_ID, eu_su_ID, LAT, LONG, ELEV, Insect, Logging

## g0793（1 列）
- 見出し：C total
- 例1 値：5.4921 | 2.6177 | 2.5716 | 39.786 | 7.2851
  - 同じ表の列：eu_ID, su_ID, eu_su_ID, LAT, LONG, ELEV, Insect, Logging

## g0794（1 列）
- 見出し：TOPIC_ID
- 例1 値：11 | 573 | 431 | 836 | 82
  - 同じ表の列：Dataset_Type, NTSC_Seedlot_ID, TOPIC_OfficialSpeci…, TSW_TestDate, TSW_g, Moist_TestDate, Moist_Pct, Germ_TestStart

## g0795（1 列）
- 見出し：Dataset_Type
- 例1 値：P | P | GV | P | P
  - 同じ表の列：TOPIC_ID, NTSC_Seedlot_ID, TOPIC_OfficialSpeci…, TSW_TestDate, TSW_g, Moist_TestDate, Moist_Pct, Germ_TestStart

## g0796（1 列）
- 見出し：NTSC_Seedlot_ID
- 例1 値：9810009 | 8930031 | 20021019 | 8370331 | 8370332
  - 同じ表の列：TOPIC_ID, Dataset_Type, TOPIC_OfficialSpeci…, TSW_TestDate, TSW_g, Moist_TestDate, Moist_Pct, Germ_TestStart

## g0797（1 列）
- 見出し：TOPIC_OfficialSpeciesCode
- 例1 値：ACESAZ | ACESAC | ABIBAL | ACEPEN | ACERUB
  - 同じ表の列：TOPIC_ID, Dataset_Type, NTSC_Seedlot_ID, TSW_TestDate, TSW_g, Moist_TestDate, Moist_Pct, Germ_TestStart

## g0798（1 列）
- 見出し：TSW_TestDate
- 例1 値：2005-08-01 | 1991-11-01 | 1980-01-01 | 2008-11-01 | 2001-07-01
  - 同じ表の列：TOPIC_ID, Dataset_Type, NTSC_Seedlot_ID, TOPIC_OfficialSpeci…, TSW_g, Moist_TestDate, Moist_Pct, Germ_TestStart

## g0799（1 列）
- 見出し：TSW_g
- 例1 値：11.45 | 0.31 | 12.02 | 44.84 | 6.42
  - 同じ表の列：TOPIC_ID, Dataset_Type, NTSC_Seedlot_ID, TOPIC_OfficialSpeci…, TSW_TestDate, Moist_TestDate, Moist_Pct, Germ_TestStart

## g0800（1 列）
- 見出し：Moist_TestDate
- 例1 値：2005-06-01 | 1984-07-01 | 2006-06-01 | 2000-07-01 | 2006-06-01
  - 同じ表の列：TOPIC_ID, Dataset_Type, NTSC_Seedlot_ID, TOPIC_OfficialSpeci…, TSW_TestDate, TSW_g, Moist_Pct, Germ_TestStart

## g0801（1 列）
- 見出し：Moist_Pct
- 例1 値：8.43 | 5.74 | 4.82 | 7.18 | 9.5
  - 同じ表の列：TOPIC_ID, Dataset_Type, NTSC_Seedlot_ID, TOPIC_OfficialSpeci…, TSW_TestDate, TSW_g, Moist_TestDate, Germ_TestStart

## g0802（1 列）
- 見出し：Germ_TestStart
- 例1 値：1984-11-01 | 2001-09-01 | 2003-07-01 | 1986-07-01 | 2008-09-01
  - 同じ表の列：TOPIC_ID, Dataset_Type, NTSC_Seedlot_ID, TOPIC_OfficialSpeci…, TSW_TestDate, TSW_g, Moist_TestDate, Moist_Pct

## g0803（1 列）
- 見出し：DB1_SeedCoat
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：TOPIC_ID, Dataset_Type, NTSC_Seedlot_ID, TOPIC_OfficialSpeci…, TSW_TestDate, TSW_g, Moist_TestDate, Moist_Pct

## g0804（1 列）
- 見出し：Title
- 例1 値：Chief Executive Officer | SVP, Legal and Compliance, Chief Agent | Principal Officer | President and Chief Executive Officer | Chief Executive Officer
  - 同じ表の列：City, Province State, Authorized Insuranc…

## g0805（1 列）
- 見出し：City
- 例1 値：VANCOUVER | TORONTO | MONTREAL | PORTAGE LA PRAIRIE | TORONTO
  - 同じ表の列：Title, Province State, Authorized Insuranc…

## g0806（1 列）
- 見出し：Province State
- 例1 値：Quebec | Ontario | Ontario | Ontario | Saskatchewan
  - 同じ表の列：Title, City, Authorized Insuranc…

## g0807（1 列）
- 見出し：Authorized Insurance Classes
- 例1 値：Liability; Marine; Hail; Boiler and mac… | Credit protection; Life; Accident and s… | Surety; Automobile; Liability; Marine; … | Life. | Life; Accident and sickness.
  - 同じ表の列：Title, City, Province State

## g0808（2 列）
- 見出し：Park
- 例1 値：MRNP | MRNP | MRNP | MRNP | MRNP
  - 同じ表の列：Location, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…, Female adult
- 例2 値：GNP | GNP | GNP | GNP | GNP
  - 同じ表の列：Location, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…, Female adult

## g0809（1 列）
- 見出し：Location
- 例1 値：Ski Chalet | Ski Chalet | Ski Chalet | Ski Chalet | Ski Chalet
  - 同じ表の列：Park, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…, Female adult

## g0810（2 列）
- 見出し：Trail type
- 例1 値：Wildlife | Wildlife | Wildlife | Wildlife | Wildlife
  - 同じ表の列：Park, Location, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…, Female adult
- 例2 値：Wildlife | Wildlife | Wildlife | Wildlife | Wildlife
  - 同じ表の列：Park, Location, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…, Female adult

## g0811（2 列）
- 見出し：Date camera deployed
- 例1 値：2021-05-25 | 2022-01-14 | 2021-05-25 | 2021-05-25 | 2021-05-25
  - 同じ表の列：Park, Location, Trail type, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…, Female adult
- 例2 値：2022-08-26 | 2023-07-18 | 2022-08-26 | 2022-08-26 | 2021-08-10
  - 同じ表の列：Park, Location, Trail type, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…, Female adult

## g0812（2 列）
- 見出し：Date when image taken
- 例1 値：2021-11-05 | 2022-07-29 | 2022-08-18 | 2021-01-16 | 2021-04-01
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Time when image tak…, Species/user types, Total number of spe…, Female adult
- 例2 値：2022-06-10 | 2023-08-02 | 2022-12-29 | 2023-07-08 | 2023-08-04
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Time when image tak…, Species/user types, Total number of spe…, Female adult

## g0813（2 列）
- 見出し：Time when image taken
- 例1 値：12:00:00 | 01:37:28 | 12:00:00 | 10:31:22 | 12:00:00
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Date when image tak…, Species/user types, Total number of spe…, Female adult
- 例2 値：12:00:00 | 12:00:00 | 12:00:00 | 12:00:00 | 12:00:00
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Date when image tak…, Species/user types, Total number of spe…, Female adult

## g0814（1 列）
- 見出し：Species/user types
- 例1 値：Empty | Empty | Empty | Empty | White-tailed Deer
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Total number of spe…, Female adult

## g0815（1 列）
- 見出し：Total number of species/user types
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Female adult

## g0816（1 列）
- 見出し：Female adult
- 例1 値：NA | NA | NA | 1 | NA
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…

## g0817（2 列）
- 見出し：Male adult
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…
- 例2 値：NA | NA | NA | NA | NA
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…

## g0818（1 列）
- 見出し：Point.ID
- 例1 値：5 | 3 | 2 | 2 | 3
  - 同じ表の列：Visit.Number, elevation, aspect, slope, Temperature, Wind, perPikaHabitat, Pika.sum

## g0819（1 列）
- 見出し：Visit.Number
- 例1 値：2 | 2 | 1 | 1 | 1
  - 同じ表の列：Point.ID, elevation, aspect, slope, Temperature, Wind, perPikaHabitat, Pika.sum

## g0820（1 列）
- 見出し：elevation
- 例1 値：1970 | 2076 | 2123 | 2344 | 1953
  - 同じ表の列：Point.ID, Visit.Number, aspect, slope, Temperature, Wind, perPikaHabitat, Pika.sum

## g0821（1 列）
- 見出し：aspect
- 例1 値：107 | 268 | 9 | 267 | 13
  - 同じ表の列：Point.ID, Visit.Number, elevation, slope, Temperature, Wind, perPikaHabitat, Pika.sum

## g0822（1 列）
- 見出し：slope
- 例1 値：47 | 30 | 39 | 71 | 51
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, Temperature, Wind, perPikaHabitat, Pika.sum

## g0823（1 列）
- 見出し：Temperature
- 例1 値：24.3 | 11.1 | 16.4 | 16.6 | 7.2
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, slope, Wind, perPikaHabitat, Pika.sum

## g0824（1 列）
- 見出し：Wind
- 例1 値：1.1 | 7.3 | 4.2 | 3.8 | 3.1
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, slope, Temperature, perPikaHabitat, Pika.sum

## g0825（1 列）
- 見出し：perPikaHabitat
- 例1 値：100 | 75 | 80 | 40 | 90
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, slope, Temperature, Wind, Pika.sum

## g0826（1 列）
- 見出し：Pika.sum
- 例1 値：4 | 4 | 4 | 0 | 3
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, slope, Temperature, Wind, perPikaHabitat

## g0827（5 列）
- 見出し：date
- 例1 値：2024-08-22 | 2024-08-29 | 2023-09-14 | 2023-09-03 | 2024-08-22
  - 同じ表の列：Point.ID, Visit.Number, elevation, aspect, slope, Temperature, Wind, perPikaHabitat
- 例2 値：2022-01-31 | 2017-04-30 | 2018-01-31 | 2022-03-31 | 2020-07-31
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Branch, Service, Value, Metric Type

## g0828（1 列）
- 見出し：Location
- 例1 値：Mountain Creek Headwaters3 | Mountain Creek Headwaters3 | Mountain Creek Headwaters3 | Mountain Creek Headwaters3 | Mountain Creek Headwaters3
  - 同じ表の列：Park, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…, Female adult

## g0829（1 列）
- 見出し：Species/user types
- 例1 値：Red Squirrel | Empty | Empty | Empty | Empty
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Total number of spe…, Female adult

## g0830（1 列）
- 見出し：Total number of species/user types
- 例1 値：NA | NA | NA | 1 | NA
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Female adult

## g0831（1 列）
- 見出し：Female adult
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：Park, Location, Trail type, Date camera deployed, Date when image tak…, Time when image tak…, Species/user types, Total number of spe…

## g0832（1 列）
- 見出し：Program/Component
- 例1 値：Young Canada Works at Building Careers … | Museums Assistance Program / Collection… | Young Canada Works in Heritage Organiza… | Museums Assistance Program / Collection… | Museums Assistance Program / Collection…
  - 同じ表の列：Type of Funding, Province, # of professonal le…, # of participants w…, # of participants w…, # of participants r…, % of participants r…

## g0833（1 列）
- 見出し：Type of Funding
- 例1 値：Contribution | Grant | Contribution | Grant | Contribution
  - 同じ表の列：Program/Component, Province, # of professonal le…, # of participants w…, # of participants w…, # of participants r…, % of participants r…

## g0834（2 列）
- 見出し：Province
- 例1 値：ON | BC | QC | MB | AB
  - 同じ表の列：Program/Component, Type of Funding, # of professonal le…, # of participants w…, # of participants w…, # of participants r…, % of participants r…
- 例2 値：ON | SK | QC | NS | QC
  - 同じ表の列：Program/Component, Type of Funding/Ser…, # of host venues, # of visitors, # of public program…, # of public program…

## g0835（1 列）
- 見出し：# of professonal learning opportunities
- 例1 値：152 | 8 | 173 | 4 | 1,442
  - 同じ表の列：Program/Component, Type of Funding, Province, # of participants w…, # of participants w…, # of participants r…, % of participants r…

## g0836（1 列）
- 見出し：# of participants who attended
- 例1 値：152 | 12 | 37 | 211 | 1,442
  - 同じ表の列：Program/Component, Type of Funding, Province, # of professonal le…, # of participants w…, # of participants r…, % of participants r…

## g0837（1 列）
- 見出し：# of participants who responded to participant survey
- 例1 値：11 | 16 | 116 | 42 | 47
  - 同じ表の列：Program/Component, Type of Funding, Province, # of professonal le…, # of participants w…, # of participants r…, % of participants r…

## g0838（1 列）
- 見出し：# of participants reporting improvement
- 例1 値：112 | 36 | 11 | 41 | 16
  - 同じ表の列：Program/Component, Type of Funding, Province, # of professonal le…, # of participants w…, # of participants w…, % of participants r…

## g0839（1 列）
- 見出し：% of participants reporting improvement
- 例1 値：77% | 96% | 87% | 98% | 100%
  - 同じ表の列：Program/Component, Type of Funding, Province, # of professonal le…, # of participants w…, # of participants w…, # of participants r…

## g0840（1 列）
- 見出し：Program/Component
- 例1 値：Museums Assistance Program / Exhibition… | Museums Assistance Program / Exhibition… | Museums Assistance Program / Exhibition… | Museums Assistance Program / Exhibition… | Museums Assistance Program / Access to …
  - 同じ表の列：Type of Funding/Ser…, Province, # of host venues, # of visitors, # of public program…, # of public program…

## 答えの雛形

```
g0721	
g0722	
g0723	
g0724	
g0725	
g0726	
g0727	
g0728	
g0729	
g0730	
g0731	
g0732	
g0733	
g0734	
g0735	
g0736	
g0737	
g0738	
g0739	
g0740	
g0741	
g0742	
g0743	
g0744	
g0745	
g0746	
g0747	
g0748	
g0749	
g0750	
g0751	
g0752	
g0753	
g0754	
g0755	
g0756	
g0757	
g0758	
g0759	
g0760	
g0761	
g0762	
g0763	
g0764	
g0765	
g0766	
g0767	
g0768	
g0769	
g0770	
g0771	
g0772	
g0773	
g0774	
g0775	
g0776	
g0777	
g0778	
g0779	
g0780	
g0781	
g0782	
g0783	
g0784	
g0785	
g0786	
g0787	
g0788	
g0789	
g0790	
g0791	
g0792	
g0793	
g0794	
g0795	
g0796	
g0797	
g0798	
g0799	
g0800	
g0801	
g0802	
g0803	
g0804	
g0805	
g0806	
g0807	
g0808	
g0809	
g0810	
g0811	
g0812	
g0813	
g0814	
g0815	
g0816	
g0817	
g0818	
g0819	
g0820	
g0821	
g0822	
g0823	
g0824	
g0825	
g0826	
g0827	
g0828	
g0829	
g0830	
g0831	
g0832	
g0833	
g0834	
g0835	
g0836	
g0837	
g0838	
g0839	
g0840	
```
