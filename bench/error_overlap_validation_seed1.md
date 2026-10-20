# 未知の見出しで外した行の重なり：mmBERT-small(1e-4) と E5-base(3e-5)

検証モード（学習側の表の 1/8 を外した検証。固定試験・blind は使っていない）。外れ＝`slice_eval.OK_OUTCOMES` に入らない行。

| | 行数 |
|---|---:|
| 未知の見出しの行 | 255 |
| mmBERT-small(1e-4) が外した | 51 |
| E5-base(3e-5) が外した | 52 |
| **両方が外した** | **39** |
| mmBERT-small(1e-4) だけが外した | 12 |
| E5-base(3e-5) だけが外した | 13 |
| 両方が外した行のうち、予測も同じ | 24 |

## 両方が外した行の取り違え（正解 → mmBERT-small(1e-4) の予測／E5-base(3e-5) の予測）

| 正解 | 予測A | 予測B | 行数 |
|---|---|---|---:|
| quantity | category | category | 14 |
| other | category | rate | 9 |
| date | id | unknown | 2 |
| date | unknown | unknown | 2 |
| category | account | unknown | 1 |
| account | unknown | text | 1 |
| amount | id | id | 1 |
| org | address | address | 1 |

## mmBERT-small(1e-4) だけが外した（正解 → 予測）

| 正解 | 予測 | 行数 |
|---|---|---:|
| rate | category | 3 |
| quantity | category | 2 |
| quantity | unknown | 2 |
| category | account | 1 |
| rate | unknown | 1 |
| org | unknown | 1 |
| org | text | 1 |
| category | unknown | 1 |

## E5-base(3e-5) だけが外した（正解 → 予測）

| 正解 | 予測 | 行数 |
|---|---|---:|
| quantity | category | 2 |
| other | rate | 2 |
| other | category | 2 |
| other | amount | 2 |
| account | org | 1 |
| date | unknown | 1 |
| rate | quantity | 1 |
| org | address | 1 |

## 両方が外した行の見出し（重複を除く）

`quarterno`（正解 date）、`unfounded_non-fonde`（正解 quantity）、`no-action_aucune-action`（正解 quantity）、`document_budget_des_dépenses`（正解 category）、`poste_législatif`（正解 account）、`autorisations`（正解 amount）、`year 2016/2017`（正解 date）、`car_park_name`（正解 org）、`health deprivation and disability 2007`（正解 other）、`health deprivation and disability 2010`（正解 other）、`education skills and training deprivation 2007`（正解 other）、`education skills and training deprivation 2010`（正解 other）、`barriers to housing and services deprivation 2007`（正解 other）、`crime and disorder deprivation 2007`（正解 other）、`crime and disorder deprivation 2010`（正解 other）、`living environment deprivation 2007`（正解 other）、`living environment deprivation 2010`（正解 other）、`有効終了年月日`（正解 date）、`令和8年1月1日時点で静岡市を含む政令指定都市に住所があった人(税率8%)※`（正解 category）、`genus`（正解 other）、`iso_3166_1_alpha_3`（正解 address）、`リウマチ科`（正解 quantity）、`産婦人科`（正解 quantity）、`ngram`（正解 text）、`count_altmetric`（正解 quantity）、`消化器科`（正解 quantity）、`呼吸器外科`（正解 quantity）、`心療内科`（正解 quantity）、`relative flows`（正解 other）、`サービス形態別_その他`（正解 quantity）、`detail of applicant`（正解 person）、`呼吸器科`（正解 quantity）、`気管食道科`（正解 quantity）、`泌尿器科`（正解 quantity）、`耳鼻いんこう科`（正解 quantity）、`麻酔科`（正解 quantity）、`こう門科`（正解 quantity）、`請負業者名`（正解 org）

注意：検証の記録に表の ID は無いため、同じ表の列かどうかは数えていない（見出しからの推測にとどまる）。同じ表の列は似た誤りをまとめて出しやすいので、行数は独立な件数ではない。
