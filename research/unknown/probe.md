# 本体に直接聞く：入力を 1 か所変えると答えはどう変わるか（`research/unknown/probe.py`）

同じ C2 種子 1・題名なし。本体が誤った 73 列（M11）。v0 そのまま／h 列名を「x」に／s 同じ表の列名を外す／c 値を整える

| 分け | 列 |
|---|---:|
| 1 か所変えると答えは変わるが、正しくはならない | 37 |
| どこを 1 か所変えても答えが変わらない | 28 |
| 同じ表の列名を外すと正しくなる＝同じ表の列名に引っ張られた | 4 |
| 列名を消すと正しくなる＝列名に引っ張られた | 2 |
| 値を整えると正しくなる＝値の形に引っ張られた | 2 |

| 分け | id | 見出し | 正解 | v0 | h | s | c |
|---|---|---|---|---|---|---|---|
| 1 か所変えると答えは変 | b015-0063 | Sexual violence ('000) | quantity | rate 0.72 | other 0.96 | rate 0.86 | rate 0.72 |
| 1 か所変えると答えは変 | b015-0067 | Fossil fuels | quantity | amount 0.74 | other 0.98 | amount 0.88 | amount 0.74 |
| 1 か所変えると答えは変 | b015-0070 | Total (All categories) | quantity | amount 0.93 | other 0.99 | amount 0.89 | amount 0.93 |
| 1 か所変えると答えは変 | b015-0082 | Emp_Wkf_POPD_15+yrs_2021 | quantity | amount 0.98 | other 0.98 | amount 0.99 | amount 0.98 |
| 1 か所変えると答えは変 | b015-0083 | Emp_Wkf_POPD_15+yrs_2022 | quantity | amount 0.99 | other 0.98 | amount 0.99 | amount 0.99 |
| 1 か所変えると答えは変 | b015-0084 | Emp_Wkf_POPD_15+yrs_2023 | quantity | amount 0.97 | other 0.98 | amount 0.98 | amount 0.98 |
| 1 か所変えると答えは変 | b015-0085 | Emp_Wkf_POPD_15+yrs_2024 | quantity | amount 0.99 | other 0.98 | amount 0.99 | amount 0.99 |
| 1 か所変えると答えは変 | b015-0086 | Emp_Wkf_POPD_15+yrs_2025 | quantity | amount 0.98 | other 0.98 | amount 0.98 | amount 0.99 |
| 1 か所変えると答えは変 | b015-0087 | Emp_Wkf_POPD_15+yrs_2026 | quantity | amount 0.98 | other 0.98 | amount 0.99 | amount 0.98 |
| 1 か所変えると答えは変 | b015-0088 | Emp_Wkf_POPD_15+yrs_2027 | quantity | amount 0.97 | other 0.98 | amount 0.98 | amount 0.98 |
| 1 か所変えると答えは変 | b015-0089 | Emp_Wkf_POPD_15+yrs_2028 | quantity | amount 0.98 | other 0.98 | amount 0.98 | amount 0.98 |
| 1 か所変えると答えは変 | b015-0090 | Emp_Wkf_POPD_15+yrs_2029 | quantity | amount 0.98 | other 0.98 | amount 0.99 | amount 0.98 |
| 1 か所変えると答えは変 | b016-0058 | 9 | category | quantity 0.65 | other 0.92 | quantity 0.87 | quantity 0.65 |
| 1 か所変えると答えは変 | b017-0136 | Structure | category | text 0.40 | address 0.50 | address 0.44 | text 0.40 |
| 1 か所変えると答えは変 | b017-0271 | replicate | id | quantity 0.93 | other 0.98 | quantity 0.93 | quantity 0.93 |
| 1 か所変えると答えは変 | b017-0346 | Amount per Container | quantity | amount 0.55 | other 0.87 | amount 0.61 | amount 0.55 |
| 1 か所変えると答えは変 | b060-0177 | service | product | text 0.45 | org 0.66 | text 0.58 | text 0.45 |
| 1 か所変えると答えは変 | b060-0260 | 01:30 | quantity | rate 0.39 | other 0.97 | rate 0.63 | rate 0.39 |
| 1 か所変えると答えは変 | b060-0263 | 03:00 | quantity | rate 0.40 | other 0.97 | rate 0.80 | rate 0.40 |
| 1 か所変えると答えは変 | b060-0265 | 04:00 | quantity | rate 0.75 | other 0.97 | rate 0.92 | rate 0.75 |
| 1 か所変えると答えは変 | b062-0035 | EW_Total_Company_NSA | quantity | amount 0.61 | other 0.98 | amount 0.56 | amount 0.61 |
| 1 か所変えると答えは変 | b062-0109 | Supplier | org | account 0.42 | category 0.94 | category 0.44 | account 0.42 |
| 1 か所変えると答えは変 | b062-0256 | Control Budget Code | category | id 0.62 | other 0.91 | account 0.79 | id 0.62 |
| 1 か所変えると答えは変 | b062-0358 | plan | text | category 0.46 | other 0.71 | category 0.49 | category 0.46 |
| 1 か所変えると答えは変 | b063-0199 | Age | category | quantity 0.89 | other 0.91 | quantity 0.95 | quantity 0.89 |
| 1 か所変えると答えは変 | b063-0207 | AGE | category | id 0.52 | other 0.85 | id 0.68 | id 0.52 |
| 1 か所変えると答えは変 | b063-0213 | AGE | category | id 0.37 | other 0.96 | id 0.49 | id 0.37 |
| 1 か所変えると答えは変 | b063-0217 | monitoring_program | category | id 0.62 | other 0.98 | id 0.87 | id 0.62 |
| 1 か所変えると答えは変 | b063-0275 | Nachgefragt | amount | quantity 0.88 | other 0.98 | quantity 0.95 | quantity 0.88 |
| 1 か所変えると答えは変 | b063-0322 | kumsum | quantity | amount 0.42 | other 0.98 | other 0.50 | amount 0.42 |
| 1 か所変えると答えは変 | b064-0139 | Age | category | quantity 0.86 | other 0.55 | quantity 0.92 | quantity 0.86 |
| 1 か所変えると答えは変 | b064-0155 | NO_COMPLEMENTAIRE | id | quantity 0.86 | other 0.89 | quantity 0.88 | quantity 0.86 |
| 1 か所変えると答えは変 | b064-0160 | funk | id | quantity 0.66 | other 0.97 | quantity 0.57 | quantity 0.66 |
| 1 か所変えると答えは変 | b064-0174 | crime | category | quantity 0.68 | other 0.98 | quantity 0.82 | quantity 0.68 |
| 1 か所変えると答えは変 | b064-0178 | finances | category | amount 0.76 | other 0.98 | amount 0.85 | amount 0.76 |
| 1 か所変えると答えは変 | b064-0184 | plz | address | id 0.86 | other 0.98 | id 0.98 | id 0.86 |
| 1 か所変えると答えは変 | b064-0372 | Widmung | text | other 0.47 | other 0.83 | category 0.45 | other 0.47 |
| どこを 1 か所変えても | b015-0007 | Tree | id | other 0.68 | other 0.98 | other 0.68 | other 0.68 |
| どこを 1 か所変えても | b015-0066 | Biomass | quantity | other 0.78 | other 0.98 | other 0.81 | other 0.78 |
| どこを 1 か所変えても | b015-0068 | Metal ores | quantity | other 0.81 | other 0.99 | other 0.77 | other 0.81 |
| どこを 1 か所変えても | b015-0069 | Non-metallic minerals | quantity | other 0.86 | other 0.98 | other 0.92 | other 0.86 |
| どこを 1 か所変えても | b016-0032 | 前5日間平均気温の品質情報 | category | other 0.94 | other 0.98 | other 0.65 | other 0.94 |
| どこを 1 か所変えても | b016-0054 | 5 | category | other 0.58 | other 0.84 | other 0.65 | other 0.58 |
| どこを 1 か所変えても | b017-0019 | TOTAL_SHEEP_MOUNTAIN | quantity | other 0.95 | other 0.98 | other 0.96 | other 0.95 |
| どこを 1 か所変えても | b017-0168 | Prov/Terr | address | other 0.47 | other 0.96 | other 0.77 | other 0.47 |
| どこを 1 か所変えても | b017-0255 | Family_Famille | category | other 0.83 | other 0.97 | other 0.84 | other 0.83 |
| どこを 1 か所変えても | b017-0269 | bathPosition | id | other 0.63 | other 0.98 | other 0.57 | other 0.63 |
| どこを 1 か所変えても | b017-0347 | Rank | category | other 0.52 | other 0.98 | other 0.52 | other 0.52 |
| どこを 1 か所変えても | b060-0393 | Body | id | other 0.99 | other 0.99 | other 0.99 | other 0.99 |
| どこを 1 か所変えても | b060-0860 | organisati | id | other 0.99 | other 0.99 | other 0.99 | other 0.99 |
| どこを 1 か所変えても | b063-0129 | SMR 2024 | rate | other 0.88 | other 0.91 | other 0.95 | other 0.44 |
| どこを 1 か所変えても | b063-0135 | AnzStand | quantity | other 0.96 | other 0.98 | other 0.91 | other 0.96 |
| どこを 1 か所変えても | b063-0202 | LowerB | quantity | other 0.69 | other 0.98 | other 0.97 | other 0.69 |
| どこを 1 か所変えても | b063-0323 | vj_abs_n | quantity | other 0.48 | other 0.97 | other 0.90 | other 0.48 |
| どこを 1 か所変えても | b063-0324 | vj_rel_n | rate | other 0.95 | other 0.97 | other 0.98 | other 0.95 |
| どこを 1 か所変えても | b063-0325 | vj_abs_kumsum | quantity | other 0.55 | other 0.98 | other 0.94 | other 0.55 |
| どこを 1 か所変えても | b063-0326 | vj_rel_kumsum | rate | other 0.70 | other 0.97 | other 0.97 | other 0.70 |
| どこを 1 か所変えても | b063-0495 | designation | category | address 0.41 | address 0.44 | address 0.62 | address 0.41 |
| どこを 1 か所変えても | b063-0714 | digital_platform | category | other 0.89 | other 0.99 | other 0.81 | other 0.89 |
| どこを 1 か所変えても | b064-0142 | Lim_min | quantity | other 0.88 | other 0.98 | other 0.98 | other 0.88 |
| どこを 1 か所変えても | b064-0177 | energy | category | other 0.64 | other 0.98 | other 0.87 | other 0.64 |
| どこを 1 か所変えても | b064-0370 | Datierung_Bemerkung | text | date 0.67 | date 0.86 | date 0.82 | date 0.67 |
| どこを 1 か所変えても | b065-0049 | Got some of what I wanted | rate | other 0.68 | other 0.97 | other 0.88 | other 0.68 |
| どこを 1 か所変えても | b065-0050 | Got none of what I wanted | rate | other 0.58 | other 0.98 | other 0.84 | other 0.58 |
| どこを 1 か所変えても | b065-0202 | Type of Aid | category | id 0.72 | id 0.90 | id 0.61 | id 0.72 |
| 値を整えると正しくなる＝ | b063-0125 | SMR 2019-2023 | rate | other 0.86 | other 0.95 | other 0.88 | rate 0.85 |
| 値を整えると正しくなる＝ | b065-0074 | Dwellings value | quantity | other 0.59 | other 0.98 | quantity 0.62 | quantity 0.47 |
| 列名を消すと正しくなる＝ | b017-0178 | Tax gap component | category | account 0.47 | category 0.73 | account 0.49 | account 0.47 |
| 列名を消すと正しくなる＝ | b017-0296 | Service_FR | category | account 0.47 | category 0.48 | text 0.49 | account 0.47 |
| 同じ表の列名を外すと正し | b017-0171 | Total - All Returns /Total - | quantity | amount 0.52 | other 0.98 | quantity 0.73 | amount 0.52 |
| 同じ表の列名を外すと正し | b060-0737 | SiteReference | id | other 0.79 | other 0.99 | id 0.54 | other 0.79 |
| 同じ表の列名を外すと正し | b063-0117 | Versicherer | id | quantity 0.97 | other 0.97 | id 0.91 | quantity 0.97 |
| 同じ表の列名を外すと正し | b063-0276 | Beschluss | amount | id 0.49 | other 0.98 | amount 0.46 | id 0.49 |
