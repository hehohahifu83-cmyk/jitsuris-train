# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：ECODISTRIC
- 例1 値：590 | 746 | 591 | 771 | 728
  - 同じ表の列：SL, PROVINCE, YEAR, BARLEY, ODFBNS, BUCWHT, CANARY, CANOLA

## g0002（1 列）
- 見出し：SL
- 例1 値：828017 | 680003 | 688004 | 591024 | 678002
  - 同じ表の列：ECODISTRIC, PROVINCE, YEAR, BARLEY, ODFBNS, BUCWHT, CANARY, CANOLA

## g0003（1 列）
- 見出し：PROVINCE
- 例1 値：AB | AB | AB | AB | AB
  - 同じ表の列：ECODISTRIC, SL, YEAR, BARLEY, ODFBNS, BUCWHT, CANARY, CANOLA

## g0004（5 列）
- 見出し：YEAR
- 例1 値：1985 | 1985 | 1985 | 1985 | 1985
  - 同じ表の列：ECODISTRIC, SL, PROVINCE, BARLEY, ODFBNS, BUCWHT, CANARY, CANOLA
- 例2 値：2016 | 2011 | 2003 | 2009 | 2022
  - 同じ表の列：Month, Type of Production, Well Site, Total

## g0005（1 列）
- 見出し：BARLEY
- 例1 値：2985 | 2553 | 2674 | 1706 | 1187
  - 同じ表の列：ECODISTRIC, SL, PROVINCE, YEAR, ODFBNS, BUCWHT, CANARY, CANOLA

## g0006（1 列）
- 見出し：ODFBNS
- 例1 値：1610 | 1610 | 1000 | 1610 | 1610
  - 同じ表の列：ECODISTRIC, SL, PROVINCE, YEAR, BARLEY, BUCWHT, CANARY, CANOLA

## g0007（1 列）
- 見出し：BUCWHT
- 例1 値：1060 | 1120 | 1120 | 1120 | 1120
  - 同じ表の列：ECODISTRIC, SL, PROVINCE, YEAR, BARLEY, ODFBNS, CANARY, CANOLA

## g0008（1 列）
- 見出し：CANARY
- 例1 値：1105.67 | 1105.67 | 1105.67 | 1410 | 1410
  - 同じ表の列：ECODISTRIC, SL, PROVINCE, YEAR, BARLEY, ODFBNS, BUCWHT, CANOLA

## g0009（1 列）
- 見出し：CANOLA
- 例1 値：577 | 1409 | 1314 | 1838 | 879
  - 同じ表の列：ECODISTRIC, SL, PROVINCE, YEAR, BARLEY, ODFBNS, BUCWHT, CANARY

## g0010（1 列）
- 見出し：CORNGR
- 例1 値：5281 | 4542 | 5109 | 5546 | 5232
  - 同じ表の列：ECODISTRIC, SL, PROVINCE, YEAR, BARLEY, ODFBNS, BUCWHT, CANARY

## g0011（1 列）
- 見出し：TrialYear_AnneeEssai
- 例1 値：2018 | 2014 | 2019 | 2007 | 2016
  - 同じ表の列：DisciplineEn_Discip…, DisciplineFr_Discip…, DFRField_TerrainDFR, DFRLab_LabDFR, EfficacyField_Terra…, ToleranceField_Terr…, ResidueField_Terrai…, ResidueProcessing_T…

## g0012（1 列）
- 見出し：DisciplineEn_DisciplineAn
- 例1 値：Entomology | Entomology | Entomology | Pathology | Entomology
  - 同じ表の列：TrialYear_AnneeEssai, DisciplineFr_Discip…, DFRField_TerrainDFR, DFRLab_LabDFR, EfficacyField_Terra…, ToleranceField_Terr…, ResidueField_Terrai…, ResidueProcessing_T…

## g0013（1 列）
- 見出し：DisciplineFr_DisciplineFr
- 例1 値：Pathologie | Malherbologie | Pathologie | Pathologie | Entomologie
  - 同じ表の列：TrialYear_AnneeEssai, DisciplineEn_Discip…, DFRField_TerrainDFR, DFRLab_LabDFR, EfficacyField_Terra…, ToleranceField_Terr…, ResidueField_Terrai…, ResidueProcessing_T…

## g0014（1 列）
- 見出し：DFRField_TerrainDFR
- 例1 値：1 | 0 | 0 | 0 | 4
  - 同じ表の列：TrialYear_AnneeEssai, DisciplineEn_Discip…, DisciplineFr_Discip…, DFRLab_LabDFR, EfficacyField_Terra…, ToleranceField_Terr…, ResidueField_Terrai…, ResidueProcessing_T…

## g0015（1 列）
- 見出し：DFRLab_LabDFR
- 例1 値：1 | 0 | 0 | 0 | 1
  - 同じ表の列：TrialYear_AnneeEssai, DisciplineEn_Discip…, DisciplineFr_Discip…, DFRField_TerrainDFR, EfficacyField_Terra…, ToleranceField_Terr…, ResidueField_Terrai…, ResidueProcessing_T…

## g0016（1 列）
- 見出し：EfficacyField_TerrainEfficacite
- 例1 値：6 | 44 | 2 | 26 | 57
  - 同じ表の列：TrialYear_AnneeEssai, DisciplineEn_Discip…, DisciplineFr_Discip…, DFRField_TerrainDFR, DFRLab_LabDFR, ToleranceField_Terr…, ResidueField_Terrai…, ResidueProcessing_T…

## g0017（1 列）
- 見出し：ToleranceField_TerrainTolerance
- 例1 値：2 | 0 | 1 | 0 | 0
  - 同じ表の列：TrialYear_AnneeEssai, DisciplineEn_Discip…, DisciplineFr_Discip…, DFRField_TerrainDFR, DFRLab_LabDFR, EfficacyField_Terra…, ResidueField_Terrai…, ResidueProcessing_T…

## g0018（1 列）
- 見出し：ResidueField_TerrainResidus
- 例1 値：23 | 32 | 19 | 25 | 21
  - 同じ表の列：TrialYear_AnneeEssai, DisciplineEn_Discip…, DisciplineFr_Discip…, DFRField_TerrainDFR, DFRLab_LabDFR, EfficacyField_Terra…, ToleranceField_Terr…, ResidueProcessing_T…

## g0019（1 列）
- 見出し：ResidueProcessing_TransformationResidus
- 例1 値：2 | 1 | 0 | 1 | 0
  - 同じ表の列：TrialYear_AnneeEssai, DisciplineEn_Discip…, DisciplineFr_Discip…, DFRField_TerrainDFR, DFRLab_LabDFR, EfficacyField_Terra…, ToleranceField_Terr…, ResidueField_Terrai…

## g0020（1 列）
- 見出し：ResidueLab_LabResidus
- 例1 値：9 | 3 | 1 | 20 | 2
  - 同じ表の列：TrialYear_AnneeEssai, DisciplineEn_Discip…, DisciplineFr_Discip…, DFRField_TerrainDFR, DFRLab_LabDFR, EfficacyField_Terra…, ToleranceField_Terr…, ResidueField_Terrai…

## g0021（2 列）
- 見出し：Month
- 例1 値：July | August | September | February | May
  - 同じ表の列：Year, Type of Production, Well Site, Total
- 例2 値：May | February | December | April | February
  - 同じ表の列：Period, Year, Product, Volume (10^3 m3), Volume (MBBL)

## g0022（1 列）
- 見出し：Type of Production
- 例1 値：Oil Production (m3) | Condensate Production (m3) | Gas Production (103m3) | Oil Production (m3) | Oil Production (m3)
  - 同じ表の列：Year, Month, Well Site, Total

## g0023（1 列）
- 見出し：Well Site
- 例1 値：Norman Wells | Norman Wells | Norman Wells | Norman Wells | Norman Wells
  - 同じ表の列：Year, Month, Type of Production, Total

## g0024（1 列）
- 見出し：Total
- 例1 値：0 | 129711.6 | 0 | 170667.6 | 0
  - 同じ表の列：Year, Month, Type of Production, Well Site

## g0025（1 列）
- 見出し：PADD
- 例1 値：Total | PADD III | PADD II | PADD IV | PADD IV
  - 同じ表の列：Year, Volume (m3/d), Volume (bbl/d)

## g0026（1 列）
- 見出し：Volume (m3/d)
- 例1 値：41549.8 | 15019.3 | 13772.4 | 258905.0 | 21187.6
  - 同じ表の列：Year, PADD, Volume (bbl/d)

## g0027（1 列）
- 見出し：Volume (bbl/d)
- 例1 値：535606.3 | 236718.9 | 213685.2 | 561784.8 | 25836.9
  - 同じ表の列：Year, PADD, Volume (m3/d)

## g0028（1 列）
- 見出し：Period
- 例1 値：01/01/1992 | 06/01/1993 | 12/01/1996 | 09/01/1989 | 04/01/1987
  - 同じ表の列：Year, Month, Product, Volume (10^3 m3), Volume (MBBL)

## g0029（1 列）
- 見出し：Product
- 例1 値：Middle Distillate | Total | Total | Jet Fuel | Heavy Fuel Oil
  - 同じ表の列：Period, Year, Month, Volume (10^3 m3), Volume (MBBL)

## g0030（1 列）
- 見出し：Volume (10^3 m3)
- 例1 値：164.3 | Confidential | 240.2 | Confidential | 163.9
  - 同じ表の列：Period, Year, Month, Product, Volume (MBBL)

## g0031（1 列）
- 見出し：Volume (MBBL)
- 例1 値：1380.7 | 1853.4 | 1009.7 | 1314.6 | 554.3
  - 同じ表の列：Period, Year, Month, Product, Volume (10^3 m3)

## g0032（1 列）
- 見出し：crop_year
- 例1 値：2013-2014 | 2013-2014 | 2013-2014 | 2013-2014 | 2013-2014
  - 同じ表の列：grain_week, week_ending_date, worksheet, metric, period, grain, grade, region

## g0033（1 列）
- 見出し：grain_week
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：crop_year, week_ending_date, worksheet, metric, period, grain, grade, region

## g0034（1 列）
- 見出し：week_ending_date
- 例1 値：11/8/2013 | 11/8/2013 | 11/8/2013 | 11/8/2013 | 11/8/2013
  - 同じ表の列：crop_year, grain_week, worksheet, metric, period, grain, grade, region

## g0035（1 列）
- 見出し：worksheet
- 例1 値：Terminal Exports | Terminal Disposition | Imported Grains | Terminal Exports | Terminal Disposition
  - 同じ表の列：crop_year, grain_week, week_ending_date, metric, period, grain, grade, region

## g0036（1 列）
- 見出し：metric
- 例1 値：Stocks | Stocks | Shipments | Receipts | Exports
  - 同じ表の列：crop_year, grain_week, week_ending_date, worksheet, period, grain, grade, region

## g0037（1 列）
- 見出し：period
- 例1 値：Current Week | Current Week | Crop Year | Current Week | Current Week
  - 同じ表の列：crop_year, grain_week, week_ending_date, worksheet, metric, grain, grade, region

## g0038（1 列）
- 見出し：grain
- 例1 値：Amber Durum | Amber Durum | Barley | Lentils | Wheat
  - 同じ表の列：crop_year, grain_week, week_ending_date, worksheet, metric, period, grade, region

## g0039（1 列）
- 見出し：grade
- 例1 値：CW Feed | Others | No. 2 CWRS | Tough & Damp | Others
  - 同じ表の列：crop_year, grain_week, week_ending_date, worksheet, metric, period, grain, region

## g0040（1 列）
- 見出し：region
- 例1 値：Churchill | Pacific | Pacific | Thunder Bay | Pacific
  - 同じ表の列：crop_year, grain_week, week_ending_date, worksheet, metric, period, grain, grade

## g0041（1 列）
- 見出し：Ktonnes
- 例1 値：0.3 | 0 | 0 | 0 | 0
  - 同じ表の列：crop_year, grain_week, week_ending_date, worksheet, metric, period, grain, grade

## g0042（1 列）
- 見出し：EN_YEAR
- 例1 値：2019 | 2015 | 2025 | 2026 | 2017
  - 同じ表の列：FR_ANNEÉ, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_INVITATION_CATEG…, FR_CATEGORIE_D'INVI…, TOTAL

## g0043（1 列）
- 見出し：FR_ANNEÉ
- 例1 値：2016 | 2015 | 2026 | 2017 | 2025
  - 同じ表の列：EN_YEAR, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_INVITATION_CATEG…, FR_CATEGORIE_D'INVI…, TOTAL

## g0044（1 列）
- 見出し：EN_PROVINCE_TERRITORY
- 例1 値：Alberta | Northwest Territories | Manitoba | Northwest Territories | Alberta
  - 同じ表の列：EN_YEAR, FR_ANNEÉ, FR_PROVINCE_TERRITO…, EN_INVITATION_CATEG…, FR_CATEGORIE_D'INVI…, TOTAL

## g0045（1 列）
- 見出し：FR_PROVINCE_TERRITOIRE
- 例1 値：Saskatchewan | Nouvelle-Écosse | Ontario | Ontario | Terre-Neuve-et-Labrador
  - 同じ表の列：EN_YEAR, FR_ANNEÉ, EN_PROVINCE_TERRITO…, EN_INVITATION_CATEG…, FR_CATEGORIE_D'INVI…, TOTAL

## g0046（1 列）
- 見出し：EN_INVITATION_CATEGORY
- 例1 値：Canadian Experience Class | Federal Skilled Worker | Federal Skilled Worker | Federal Skilled Trades | Federal Skilled Worker
  - 同じ表の列：EN_YEAR, FR_ANNEÉ, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, FR_CATEGORIE_D'INVI…, TOTAL

## g0047（1 列）
- 見出し：FR_CATEGORIE_D'INVITATION
- 例1 値：Travailleurs qualifiés | Travailleurs qualifiés | Candidats des provinces ou des territoi… | Candidats des provinces ou des territoi… | Catégorie de l'expérience canadienne
  - 同じ表の列：EN_YEAR, FR_ANNEÉ, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_INVITATION_CATEG…, TOTAL

## g0048（1 列）
- 見出し：TOTAL
- 例1 値：70 | 305 | 5 | 75 | 25
  - 同じ表の列：EN_YEAR, FR_ANNEÉ, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_INVITATION_CATEG…, FR_CATEGORIE_D'INVI…

## g0049（2 列）
- 見出し：EN_IMMIGRATION_CATEGORY
- 例1 値：Blended Sponsorship Refugee | Government-Assisted Refugee | Government-Assisted Refugee | Blended Sponsorship Refugee | Privately Sponsored Refugee
  - 同じ表の列：FR_CATÉGORIE_D'IMMI…, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER, FR_SEXE, EN_AGE, FR_ÂGE, TOTAL
- 例2 値：Government-Assisted Refugee | Government-Assisted Refugee | Government-Assisted Refugee | Government-Assisted Refugee | Blended Sponsorship Refugee
  - 同じ表の列：FR_CATÉGORIE_D'IMMI…, EN_COUNTRY_OF_CITIZ…, FR_PAYS_DE_CITOYENN…, TOTAL

## g0050（2 列）
- 見出し：FR_CATÉGORIE_D'IMMIGRATION
- 例1 値：Réfugiés parrainés par le secteur privé | Réfugiés parrainés par le secteur privé | Programme de parrainage mixte des réfug… | Réfugiés parrainés par le secteur privé | Réfugiés pris en charge par le gouverne…
  - 同じ表の列：EN_IMMIGRATION_CATE…, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER, FR_SEXE, EN_AGE, FR_ÂGE, TOTAL
- 例2 値：Réfugiés pris en charge par le gouverne… | Programme de parrainage mixte des réfug… | Réfugiés pris en charge par le gouverne… | Réfugiés parrainés par le secteur privé | Réfugiés pris en charge par le gouverne…
  - 同じ表の列：EN_IMMIGRATION_CATE…, EN_COUNTRY_OF_CITIZ…, FR_PAYS_DE_CITOYENN…, TOTAL

## g0051（1 列）
- 見出し：EN_PROVINCE_TERRITORY
- 例1 値：Alberta | British Columbia | Newfoundland and Labrador | Yukon | Alberta
  - 同じ表の列：EN_IMMIGRATION_CATE…, FR_CATÉGORIE_D'IMMI…, FR_PROVINCE_TERRITO…, EN_GENDER, FR_SEXE, EN_AGE, FR_ÂGE, TOTAL

## g0052（1 列）
- 見出し：FR_PROVINCE_TERRITOIRE
- 例1 値：Nouveau-Brunswick | Ontario | Île-du-Prince-Édouard | Manitoba | Yukon
  - 同じ表の列：EN_IMMIGRATION_CATE…, FR_CATÉGORIE_D'IMMI…, EN_PROVINCE_TERRITO…, EN_GENDER, FR_SEXE, EN_AGE, FR_ÂGE, TOTAL

## g0053（1 列）
- 見出し：EN_GENDER
- 例1 値：Female | Female | Male | Female | Male
  - 同じ表の列：EN_IMMIGRATION_CATE…, FR_CATÉGORIE_D'IMMI…, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, FR_SEXE, EN_AGE, FR_ÂGE, TOTAL

## g0054（1 列）
- 見出し：FR_SEXE
- 例1 値：Hommes | Femmes | Hommes | Hommes | Femmes
  - 同じ表の列：EN_IMMIGRATION_CATE…, FR_CATÉGORIE_D'IMMI…, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER, EN_AGE, FR_ÂGE, TOTAL

## g0055（1 列）
- 見出し：EN_AGE
- 例1 値：18 years old and above | 17 years old and under | 18 years old and above | 18 years old and above | 17 years old and under
  - 同じ表の列：EN_IMMIGRATION_CATE…, FR_CATÉGORIE_D'IMMI…, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER, FR_SEXE, FR_ÂGE, TOTAL

## g0056（1 列）
- 見出し：FR_ÂGE
- 例1 値：18 ans et plus | 18 ans et plus | 17 ans et moins | 18 ans et plus | 17 ans et moins
  - 同じ表の列：EN_IMMIGRATION_CATE…, FR_CATÉGORIE_D'IMMI…, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER, FR_SEXE, EN_AGE, TOTAL

## g0057（2 列）
- 見出し：TOTAL
- 例1 値：315 | 25 | 150 | 10 | --
  - 同じ表の列：EN_IMMIGRATION_CATE…, FR_CATÉGORIE_D'IMMI…, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER, FR_SEXE, EN_AGE, FR_ÂGE
- 例2 値：20 | -- | -- | -- | 35
  - 同じ表の列：EN_IMMIGRATION_CATE…, FR_CATÉGORIE_D'IMMI…, EN_COUNTRY_OF_CITIZ…, FR_PAYS_DE_CITOYENN…

## g0058（1 列）
- 見出し：EN_COUNTRY_OF_CITIZENSHIP
- 例1 値：Cape Verde Islands | Indonesia, Republic of | Ethiopia | Burundi | Mongolia, People's Republic of
  - 同じ表の列：EN_IMMIGRATION_CATE…, FR_CATÉGORIE_D'IMMI…, FR_PAYS_DE_CITOYENN…, TOTAL

## g0059（1 列）
- 見出し：FR_PAYS_DE_CITOYENNETÉ
- 例1 値：Trinité-et-Tobago, République de | Chine, République populaire de | Congo, République Démocratique du | Émirats arabes unis | Bolivie
  - 同じ表の列：EN_IMMIGRATION_CATE…, FR_CATÉGORIE_D'IMMI…, EN_COUNTRY_OF_CITIZ…, TOTAL

## g0060（1 列）
- 見出し：Province or territory
- 例1 値：Northwest Territories | Alberta | New Brunswick | Prince Edward Island | Canada
  - 同じ表の列：Grand total (number…, Grand total (thousa…, Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…, Family income betwe…

## g0061（1 列）
- 見出し：Grand total (number of recipients)
- 例1 値：10160 | 11726460 | 272560 | 1225440 | 2610670
  - 同じ表の列：Province or territo…, Grand total (thousa…, Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…, Family income betwe…

## g0062（1 列）
- 見出し：Grand total (thousands of dollars)
- 例1 値：4680 | 217601 | 6094 | 5546 | 730477
  - 同じ表の列：Province or territo…, Grand total (number…, Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…, Family income betwe…

## g0063（1 列）
- 見出し：Family income less than $5,000 (number of recipients)
- 例1 値：1315990 | 19520 | 169580 | 1130 | 4230
  - 同じ表の列：Province or territo…, Grand total (number…, Grand total (thousa…, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…, Family income betwe…

## g0064（1 列）
- 見出し：Family income less than $5,000 (thousands of dollars)
- 例1 値：69608 | 607 | 1390 | 73182 | 553629
  - 同じ表の列：Province or territo…, Grand total (number…, Grand total (thousa…, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…, Family income betwe…

## g0065（1 列）
- 見出し：Family income $5,000 - $9,999 (no. of recipients)
- 例1 値：1170 | 83550 | 550 | 30330 | 814530
  - 同じ表の列：Province or territo…, Grand total (number…, Grand total (thousa…, Family income less …, Family income less …, Family income $5,00…, Family income betwe…, Family income betwe…

## g0066（1 列）
- 見出し：Family income $5,000 - $9,999 (thousands of dollars)
- 例1 値：33845 | 9293 | 1018 | 202 | 12265
  - 同じ表の列：Province or territo…, Grand total (number…, Grand total (thousa…, Family income less …, Family income less …, Family income $5,00…, Family income betwe…, Family income betwe…

## g0067（1 列）
- 見出し：Family income between $10,000 - $14,999 (number of recipient
- 例1 値：210750 | 96970 | 3700 | 39320 | 1940
  - 同じ表の列：Province or territo…, Grand total (number…, Grand total (thousa…, Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…

## g0068（1 列）
- 見出し：Family income between $10,000 - $14,999 (thousands of dollar
- 例1 値：924 | 543 | 89635 | 43989 | 216003
  - 同じ表の列：Province or territo…, Grand total (number…, Grand total (thousa…, Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…

## g0069（1 列）
- 見出し：Family income between $15,000 - $19,999 (number of recipient
- 例1 値：1160 | 169330 | 454130 | 25480 | 36250
  - 同じ表の列：Province or territo…, Grand total (number…, Grand total (thousa…, Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…

## g0070（1 列）
- 見出し：Province
- 例1 値：New Brunswick | Quebec | Canada | British Columbia | Atlantic
  - 同じ表の列：Year, Species Group, Species, Quantity (kgs), Value (CAD)

## g0071（1 列）
- 見出し：Species Group
- 例1 値：Pelagics | Pelagics | Pelagics | Groundfish | Groundfish
  - 同じ表の列：Year, Province, Species, Quantity (kgs), Value (CAD)

## g0072（1 列）
- 見出し：Species
- 例1 値：Herring | Redfish | Shark | Total other | Grand total
  - 同じ表の列：Year, Province, Species Group, Quantity (kgs), Value (CAD)

## g0073（1 列）
- 見出し：Quantity (kgs)
- 例1 値：26 | 15554 | 142,290 | 1,573,427 | 0
  - 同じ表の列：Year, Province, Species Group, Species, Value (CAD)

## g0074（1 列）
- 見出し：Value (CAD)
- 例1 値：30,722,510 | 227,972,651 | 2,678 | 530,205 | 830,302
  - 同じ表の列：Year, Province, Species Group, Species, Quantity (kgs)

## g0075（1 列）
- 見出し：Date de capture
- 例1 値：7/27/2023 | 6/1/2023 | 7/20/2023 | 6/15/2023 | 5/9/2023
  - 同じ表の列：Sous-secteur de pêc…, Nageoire adipeuse c…, Longueur (cm), Classe de taille, Région de stock rés…, Probabilité, Stock ADN 1, Région ADN 1

## g0076（1 列）
- 見出し：Sous-secteur de pêche récréative
- 例1 値：20DB | 18B | 19A | 19A | 19A
  - 同じ表の列：Date de capture, Nageoire adipeuse c…, Longueur (cm), Classe de taille, Région de stock rés…, Probabilité, Stock ADN 1, Région ADN 1

## g0077（1 列）
- 見出し：Nageoire adipeuse coupée
- 例1 値：Non | Oui | Oui | Oui | Oui
  - 同じ表の列：Date de capture, Sous-secteur de pêc…, Longueur (cm), Classe de taille, Région de stock rés…, Probabilité, Stock ADN 1, Région ADN 1

## g0078（1 列）
- 見出し：Longueur (cm)
- 例1 値：44 | 48 | 37 | 41 | 81
  - 同じ表の列：Date de capture, Sous-secteur de pêc…, Nageoire adipeuse c…, Classe de taille, Région de stock rés…, Probabilité, Stock ADN 1, Région ADN 1

## g0079（1 列）
- 見出し：Classe de taille
- 例1 値：Sous-taille | Sous-taille | Sous-taille | Sous-taille | Sous-taille
  - 同じ表の列：Date de capture, Sous-secteur de pêc…, Nageoire adipeuse c…, Longueur (cm), Région de stock rés…, Probabilité, Stock ADN 1, Région ADN 1

## g0080（1 列）
- 見出し：Région de stock résolue
- 例1 値：Puget Sound | NA | NA | Puget Sound | NA
  - 同じ表の列：Date de capture, Sous-secteur de pêc…, Nageoire adipeuse c…, Longueur (cm), Classe de taille, Probabilité, Stock ADN 1, Région ADN 1

## g0081（1 列）
- 見出し：Probabilité
- 例1 値：NA | 0.9999895 | 0.999993 | 1 | NA
  - 同じ表の列：Date de capture, Sous-secteur de pêc…, Nageoire adipeuse c…, Longueur (cm), Classe de taille, Région de stock rés…, Stock ADN 1, Région ADN 1

## g0082（1 列）
- 見出し：Stock ADN 1
- 例1 値：Rivière Green « montaison d'automne » | Rivière Chilliwack « montaison d'automn… | Partie sud de la rivière Thompson | NA | Rivière Snohomish
  - 同じ表の列：Date de capture, Sous-secteur de pêc…, Nageoire adipeuse c…, Longueur (cm), Classe de taille, Région de stock rés…, Probabilité, Région ADN 1

## g0083（1 列）
- 見出し：Région ADN 1
- 例1 値：Puget Sound | Fraser automne | Frai d'automne de la côte est de l'île … | Puget Sound | Frai d'automne de la côte est de l'île …
  - 同じ表の列：Date de capture, Sous-secteur de pêc…, Nageoire adipeuse c…, Longueur (cm), Classe de taille, Région de stock rés…, Probabilité, Stock ADN 1

## g0084（1 列）
- 見出し：Probabilité 1
- 例1 値：0.9964425 | 0.9932534 | 0.8468044 | 0.999974 | 0.5317157
  - 同じ表の列：Date de capture, Sous-secteur de pêc…, Nageoire adipeuse c…, Longueur (cm), Classe de taille, Région de stock rés…, Probabilité, Stock ADN 1

## g0085（1 列）
- 見出し：Field|Champ
- 例1 値：precip_start | ProjectCode | data_type | hexagon_id | survey_longitude
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, NULL_permitted|auto…, Field_length|Longue…, Values_lookup|Reche…

## g0086（1 列）
- 見出し：Table|Tableau
- 例1 値：YT_BorealBirdMonitoringProgram_HumanPC_… | YT_BorealBirdMonitoringProgram_HumanPC_… | YT_BorealBirdMonitoringProgram_HumanPC_… | YT_BorealBirdMonitoringProgram_HumanPC_… | YT_BorealBirdMonitoringProgram_HumanPCs…
  - 同じ表の列：Field|Champ, Data_type_en, Type_de_données_fr, NULL_permitted|auto…, Field_length|Longue…, Values_lookup|Reche…

## g0087（1 列）
- 見出し：Data_type_en
- 例1 値：decimal | short integer | text | text | short integer
  - 同じ表の列：Field|Champ, Table|Tableau, Type_de_données_fr, NULL_permitted|auto…, Field_length|Longue…, Values_lookup|Reche…

## g0088（1 列）
- 見出し：Type_de_données_fr
- 例1 値：texte | texte | entier court | entier court | entier court
  - 同じ表の列：Field|Champ, Table|Tableau, Data_type_en, NULL_permitted|auto…, Field_length|Longue…, Values_lookup|Reche…

## g0089（1 列）
- 見出し：NULL_permitted|autorisé
- 例1 値：Y|O | Y|O | Y|O | N|N | Y|O
  - 同じ表の列：Field|Champ, Table|Tableau, Data_type_en, Type_de_données_fr, Field_length|Longue…, Values_lookup|Reche…

## g0090（1 列）
- 見出し：Field_length|Longueur_du_champ
- 例1 値：1 | 19 | 11 | 3 | 2
  - 同じ表の列：Field|Champ, Table|Tableau, Data_type_en, Type_de_données_fr, NULL_permitted|auto…, Values_lookup|Reche…

## g0091（1 列）
- 見出し：Values_lookup|Recherche_de_valeurs
- 例1 値：data_type | See sheet|Veuillez consulter la fiche '… | noise_code | cloud_code | distance_interval
  - 同じ表の列：Field|Champ, Table|Tableau, Data_type_en, Type_de_données_fr, NULL_permitted|auto…, Field_length|Longue…

## g0092（1 列）
- 見出し：Period
- 例1 値：Sept. / sept. 2014 | Jul. / juil. 2016 | Feb. / fév. 2015 | Oct. / oct. 2012 | Feb. / fév. 2013
  - 同じ表の列：Province, Retirement, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0093（1 列）
- 見出し：Province
- 例1 値：INTERNATIONAL AGREEMENTS /ACCORDS INTER… | MANITOBA | ALBERTA | SASKATCHEWAN | N.S./N.-É.
  - 同じ表の列：Period, Retirement, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0094（1 列）
- 見出し：Retirement
- 例1 値：207,394 | 2 | 821,321 | 1 | 123,410
  - 同じ表の列：Period, Province, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0095（1 列）
- 見出し：Disability
- 例1 値：33,627 | 1,213 | 59,061 | 22,745 | 12,929
  - 同じ表の列：Period, Province, Retirement, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0096（1 列）
- 見出し：Children of Disabled Contributor (-18)
- 例1 値：237 | 33,451 | 1,729 | 4,247 | 1,676
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0097（1 列）
- 見出し：Children of Disabled Contributor (18-24)
- 例1 値：645 | 683 | 1,401 | X | 3,525
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Survivor's, Children of Decease…, Children of Decease…

## g0098（1 列）
- 見出し：Survivor's
- 例1 値：49,553 | 1,032 | 54,281 | X | 171,279
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Children of Disable…, Children of Decease…, Children of Decease…

## g0099（1 列）
- 見出し：Children of Deceased Contributor (-18)
- 例1 値：7,479 | 1,014 | 289 | 1,061 | X
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…

## g0100（1 列）
- 見出し：Children of Deceased Contributor (18-24)
- 例1 値：2,639 | 1,120 | 0 | 21,733 | 514
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…

## g0101（1 列）
- 見出し：Post Retirement Benefit
- 例1 値：21,521 | 757 | 928 | 19,214 | 2,026,191
  - 同じ表の列：Period, Province, Retirement, Disability, Children of Disable…, Children of Disable…, Survivor's, Children of Decease…

## g0102（1 列）
- 見出し：mp_code
- 例1 値：02536536 | 02507560 | 02566273 | 02564009 | 77701155
  - 同じ表の列：mp_status, mp_status_effective…, mp_type, Health_Canada_ident…

## g0103（1 列）
- 見出し：mp_status
- 例1 値：Active | Active | Active | Active | Active
  - 同じ表の列：mp_code, mp_status_effective…, mp_type, Health_Canada_ident…

## g0104（1 列）
- 見出し：mp_status_effective_time
- 例1 値：20140116 | 20260417 | 20260724 | 19731231 | 20220610
  - 同じ表の列：mp_code, mp_status, mp_type, Health_Canada_ident…

## g0105（1 列）
- 見出し：mp_type
- 例1 値：DIN | CCDD | DIN | CCDD | CCDD
  - 同じ表の列：mp_code, mp_status, mp_status_effective…, Health_Canada_ident…

## g0106（1 列）
- 見出し：Health_Canada_identifier
- 例1 値：02543036 | 02126613 | 02565951 | 02497875 | 01976141
  - 同じ表の列：mp_code, mp_status, mp_status_effective…, mp_type

## g0107（1 列）
- 見出し：Chemical-Group-Groupe-de-substances-chimiques
- 例1 値：Metals and trace elements | Chlorophenols | Flame retardants: Polybrominated diphen… | Chlorophenols | Metals and trace elements
  - 同じ表の列：Chemical-Substances…, Matrix-Matrice, Units-Unites, Group-Groupe, Age-years-annees, Cycle, n, LOD-LD

## g0108（1 列）
- 見出し：Chemical-Substances-chimiques
- 例1 値：Antimony | Cesium | 2,4-Dichlorophenol (2,4-DCP) | Copper | Cesium
  - 同じ表の列：Chemical-Group-Grou…, Matrix-Matrice, Units-Unites, Group-Groupe, Age-years-annees, Cycle, n, LOD-LD

## g0109（1 列）
- 見出し：Matrix-Matrice
- 例1 値：Urine | Urine | Urine | Urine | Plasma
  - 同じ表の列：Chemical-Group-Grou…, Chemical-Substances…, Units-Unites, Group-Groupe, Age-years-annees, Cycle, n, LOD-LD

## g0110（1 列）
- 見出し：Units-Unites
- 例1 値：μg/g creatinine | μg/L | μg/L | μg/L | μg/kg lipid*
  - 同じ表の列：Chemical-Group-Grou…, Chemical-Substances…, Matrix-Matrice, Group-Groupe, Age-years-annees, Cycle, n, LOD-LD

## g0111（1 列）
- 見出し：Group-Groupe
- 例1 値：Females | Total | Total | Total | Males
  - 同じ表の列：Chemical-Group-Grou…, Chemical-Substances…, Matrix-Matrice, Units-Unites, Age-years-annees, Cycle, n, LOD-LD

## g0112（1 列）
- 見出し：Age-years-annees
- 例1 値：3–79 | 6–11 | 40–59 | 60–79 | 6–11
  - 同じ表の列：Chemical-Group-Grou…, Chemical-Substances…, Matrix-Matrice, Units-Unites, Group-Groupe, Cycle, n, LOD-LD

## g0113（1 列）
- 見出し：Cycle
- 例1 値：5 (2016–2017) | 4 (2014–2015) | 2 (2009–2011) | 1 (2007–2009) | 2 (2009–2011)
  - 同じ表の列：Chemical-Group-Grou…, Chemical-Substances…, Matrix-Matrice, Units-Unites, Group-Groupe, Age-years-annees, n, LOD-LD

## g0114（1 列）
- 見出し：n
- 例1 値：2663 | 594 | 613 | 542 | 291
  - 同じ表の列：Chemical-Group-Grou…, Chemical-Substances…, Matrix-Matrice, Units-Unites, Group-Groupe, Age-years-annees, Cycle, LOD-LD

## g0115（1 列）
- 見出し：LOD-LD
- 例1 値：0.03 μg/L | 0.04 μg/L | 0.07 μg/L | 11 pmol/g Hb | 0.5 μg/L
  - 同じ表の列：Chemical-Group-Grou…, Chemical-Substances…, Matrix-Matrice, Units-Unites, Group-Groupe, Age-years-annees, Cycle, n

## g0116（1 列）
- 見出し：pct-ess-than-moins-que-LOD-LD
- 例1 値：9.73 | 46.63 | 100 | 0 | 22.11
  - 同じ表の列：Chemical-Group-Grou…, Chemical-Substances…, Matrix-Matrice, Units-Unites, Group-Groupe, Age-years-annees, Cycle, n

## g0117（1 列）
- 見出し：Nova Scotia/Nouvelle-Écosse
- 例1 値：British Columbia/Colombie-Britannique | Northwest Territories/Territoires du No… | Canada/Canada | Manitoba/Manitoba | Yukon/Yukon
  - 同じ表の列：Receiverships/Mises…, 82, 135,927,973, 58, 250,184,326, 56, 28,249,272, 61

## g0118（1 列）
- 見出し：Receiverships/Mises sous séquestre
- 例1 値：Court Appointment/Nomination par le tri… | Court Appointment/Nomination par le tri… | Private Appointment/Nomination privée | Private Appointment/Nomination privée | Private Appointment/Nomination privée
  - 同じ表の列：Nova Scotia/Nouvell…, 82, 135,927,973, 58, 250,184,326, 56, 28,249,272, 61

## g0119（1 列）
- 見出し：82
- 例1 値：205 | 0 | 1 | 43 | 0
  - 同じ表の列：Nova Scotia/Nouvell…, Receiverships/Mises…, 135,927,973, 58, 250,184,326, 56, 28,249,272, 61

## g0120（1 列）
- 見出し：135,927,973
- 例1 値：685,669 | 0 | 0 | 59,744,341 | 0
  - 同じ表の列：Nova Scotia/Nouvell…, Receiverships/Mises…, 82, 58, 250,184,326, 56, 28,249,272, 61

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
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
```
