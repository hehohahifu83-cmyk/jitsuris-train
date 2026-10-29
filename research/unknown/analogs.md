# 本体が誤った 73 列（M11）：学習の教材でいちばん似た列（`research/unknown/analogs.py`）

- 教材 b001〜b014 の確定した列 26652。列名が近い 10 列・値の形が近い 10 列の多数の種類を、本体の答え・正解と比べた

| 分け | 列 |
|---|---:|
| E 似た列の種類は本体の答えとも正解とも違う（本体の答えは似た列からは説明できない） | 39 |
| A 値の形は教材の別の種類の列と同じで、本体は列名より値の形に従った | 19 |
| C 列名が教材の別の種類の列に似ている | 13 |
| D 列名の似た列が教材にない（いちばん近くても似ていない） | 2 |

| id | 見出し | 正解 | 本体 | 列名の近い 10 列の多数 | 値の形の近い 10 列の多数 | 分け | いちばん列名が近い教材の列 |
|---|---|---|---|---|---|---|---|
| b015-0082 | Emp_Wkf_POPD_15+yrs_2021 | quantity | amount | quantity 7/10 | amount 6/10 | A | 2021（quantity・0.53） |
| b015-0083 | Emp_Wkf_POPD_15+yrs_2022 | quantity | amount | quantity 7/10 | amount 6/10 | A | 2022（quantity・0.54） |
| b015-0084 | Emp_Wkf_POPD_15+yrs_2023 | quantity | amount | quantity 4/10 | amount 6/10 | A | unsafe_2023（quantity・0.35） |
| b015-0085 | Emp_Wkf_POPD_15+yrs_2024 | quantity | amount | quantity 5/10 | amount 6/10 | A | DCA 2024（category・0.34） |
| b015-0086 | Emp_Wkf_POPD_15+yrs_2025 | quantity | amount | quantity 4/10 | amount 6/10 | A | DCA 2025（category・0.39） |
| b015-0087 | Emp_Wkf_POPD_15+yrs_2026 | quantity | amount | quantity 5/10 | amount 6/10 | A | 2026（quantity・0.55） |
| b015-0088 | Emp_Wkf_POPD_15+yrs_2027 | quantity | amount | quantity 5/10 | amount 6/10 | A | 2026-27（amount・0.32） |
| b015-0089 | Emp_Wkf_POPD_15+yrs_2028 | quantity | amount | quantity 5/10 | amount 6/10 | A | WKT（other・0.31） |
| b015-0090 | Emp_Wkf_POPD_15+yrs_2029 | quantity | amount | quantity 5/10 | amount 6/10 | A | WKT（other・0.31） |
| b017-0271 | replicate | id | quantity | id 5/10 | quantity 10/10 | A | ReplicateCount（quantity・0.83） |
| b060-0393 | Body | id | other | org 4/10 | other 10/10 | A | Type of Body（category・0.79） |
| b060-0860 | organisati | id | other | org 7/10 | other 10/10 | A | Organisation（org・0.89） |
| b062-0358 | plan | text | category | id 5/10 | category 5/10 | A | MyPlan_GZT（category・0.8） |
| b063-0207 | AGE | category | id | quantity 5/10 | id 5/10 | A | Age（quantity・1.0） |
| b063-0213 | AGE | category | id | quantity 5/10 | id 6/10 | A | Age（quantity・1.0） |
| b063-0275 | Nachgefragt | amount | quantity | category 2/10 | quantity 8/10 | A | nace_v2_code（id・0.25） |
| b064-0160 | funk | id | quantity | category 3/10 | quantity 9/10 | A | Trunk（category・0.49） |
| b064-0174 | crime | category | quantity | date 8/10 | quantity 8/10 | A | crime_guns_recovered（quantity・0.49） |
| b065-0202 | Type of Aid | category | id | category 10/10 | id 8/10 | A | TYPE（category・0.6） |
| b015-0068 | Metal ores | quantity | other | other 4/10 | id 8/10 | C | Scores（other・0.39） |
| b016-0032 | 前5日間平均気温の品質情報 | category | other | other 3/10 | quantity 7/10 | C | 7日間平均陽性者数（other・0.44） |
| b016-0058 | 9 | category | quantity | quantity 8/10 | id 5/10 | C | 9月（quantity・0.6） |
| b017-0296 | Service_FR | category | account | account 5/10 | category 7/10 | C | Service（category・0.87） |
| b017-0346 | Amount per Container | quantity | amount | amount 10/10 | category 6/10 | C | Amount（amount・0.56） |
| b063-0199 | Age | category | quantity | quantity 5/10 | id 8/10 | C | Age（quantity・1.0） |
| b063-0276 | Beschluss | amount | id | id 5/10 | quantity 8/10 | C | BESE（id・0.25） |
| b063-0714 | digital_platform | category | other | other 4/10 | category 5/10 | C | PLATFORM_FUNCTION（category・0.56） |
| b064-0139 | Age | category | quantity | quantity 5/10 | category 3/10 | C | Age（quantity・1.0） |
| b064-0142 | Lim_min | quantity | other | other 6/10 | quantity 10/10 | C | min（other・0.68） |
| b064-0184 | plz | address | id | id 4/10 | quantity 8/10 | C | Plat（id・0.35） |
| b064-0370 | Datierung_Bemerkung | text | date | date 6/10 | address 6/10 | C | Tier（category・0.34） |
| b064-0372 | Widmung | text | other | other 7/10 | text 4/10 | C | width_m（other・0.41） |
| b065-0049 | Got some of what I wanted | rate | other | text 3/10 | rate 7/10 | D | What kinds of data would you l（text・0.29） |
| b065-0050 | Got none of what I wanted | rate | other | quantity 3/10 | quantity 6/10 | D | one_way（category・0.29） |
| b015-0007 | Tree | id | other | id 5/10 | quantity 5/10 | E | Tree_ID（id・0.91） |
| b015-0063 | Sexual violence ('000) | quantity | rate | amount 5/10 | quantity 6/10 | E | Value ('000s)（amount・0.37） |
| b015-0066 | Biomass | quantity | other | category 8/10 | id 6/10 | E | isBiomassCalculated（category・0.6） |
| b015-0067 | Fossil fuels | quantity | amount | category 5/10 | id 8/10 | E | FUEL CO.（org・0.5） |
| b015-0069 | Non-metallic minerals | quantity | other | category 4/10 | id 8/10 | E | Metro Non-metro（category・0.33） |
| b015-0070 | Total (All categories) | quantity | amount | quantity 10/10 | id 7/10 | E | total（quantity・0.5） |
| b016-0054 | 5 | category | other | quantity 5/10 | quantity 10/10 | E | 5（quantity・1.0） |
| b017-0019 | TOTAL_SHEEP_MOUNTAIN | quantity | other | quantity 8/10 | quantity 5/10 | E | Total Sheep（quantity・0.79） |
| b017-0136 | Structure | category | text | category 10/10 | category 4/10 | E | Structure（category・1.0） |
| b017-0168 | Prov/Terr | address | other | address 10/10 | quantity 5/10 | E | prov_terr（address・0.69） |
| b017-0171 | Total - All Returns /Total - T | quantity | amount | quantity 10/10 | quantity 8/10 | E | Total（quantity・0.53） |
| b017-0178 | Tax gap component | category | account | category 3/10 | category 3/10 | E | Component of Indigenous exp（category・0.51） |
| b017-0255 | Family_Famille | category | other | category 4/10 | address 6/10 | E | job_family（category・0.71） |
| b017-0269 | bathPosition | id | other | category 7/10 | id 10/10 | E | Position（category・0.77） |
| b017-0347 | Rank | category | other | category 9/10 | id 7/10 | E | Rank（category・1.0） |
| b060-0177 | service | product | text | account 5/10 | category 5/10 | E | Service（category・1.0） |
| b060-0260 | 01:30 | quantity | rate | date 3/10 | quantity 9/10 | E | 08:30:00（date・0.35） |
| b060-0263 | 03:00 | quantity | rate | date 10/10 | quantity 10/10 | E | 13:32:00（date・0.58） |
| b060-0265 | 04:00 | quantity | rate | date 10/10 | quantity 9/10 | E | 09:14:00（date・0.66） |
| b060-0737 | SiteReference | id | other | id 6/10 | quantity 9/10 | E | Reference（id・0.86） |
| b062-0035 | EW_Total_Company_NSA | quantity | amount | category 4/10 | quantity 10/10 | E | company（org・0.68） |
| b062-0109 | Supplier | org | account | org 3/10 | text 7/10 | E | SUPPLIER（org・1.0） |
| b062-0256 | Control Budget Code | category | id | amount 5/10 | category 7/10 | E | Budget（amount・0.66） |
| b063-0117 | Versicherer | id | quantity | id 4/10 | id 9/10 | E | University（org・0.33） |
| b063-0125 | SMR 2019-2023 | rate | other | quantity 8/10 | rate 7/10 | E | 2019-20（quantity・0.7） |
| b063-0129 | SMR 2024 | rate | other | quantity 6/10 | rate 5/10 | E | DCA 2024（category・0.54） |
| b063-0135 | AnzStand | quantity | other | category 6/10 | quantity 10/10 | E | ApplStandard（category・0.38） |
| b063-0202 | LowerB | quantity | other | category 7/10 | quantity 8/10 | E | POWER_SUPP（category・0.42） |
| b063-0217 | monitoring_program | category | id | account 9/10 | category 6/10 | E | Program（account・0.63） |
| b063-0322 | kumsum | quantity | amount | quantity 9/10 | quantity 9/10 | E | Pika.sum（quantity・0.42） |
| b063-0323 | vj_abs_n | quantity | other | quantity 9/10 | quantity 8/10 | E | n（quantity・0.43） |
| b063-0324 | vj_rel_n | rate | other | quantity 6/10 | rate 7/10 | E | n（quantity・0.49） |
| b063-0325 | vj_abs_kumsum | quantity | other | quantity 8/10 | quantity 8/10 | E | Abstract_Resume_FR（text・0.32） |
| b063-0326 | vj_rel_kumsum | rate | other | quantity 9/10 | rate 7/10 | E | Sum of Volume（quantity・0.33） |
| b063-0495 | designation | category | address | category 3/10 | category 6/10 | E | Designation（category・1.0） |
| b064-0155 | NO_COMPLEMENTAIRE | id | quantity | category 8/10 | category 8/10 | E | Title complement（category・0.62） |
| b064-0177 | energy | category | other | category 4/10 | quantity 8/10 | E | BLD_ENERGY（category・0.83） |
| b064-0178 | finances | category | amount | date 9/10 | quantity 8/10 | E | Finance_ID（id・0.76） |
| b065-0074 | Dwellings value | quantity | other | amount 4/10 | quantity 10/10 | E | DwellingType（category・0.69） |
