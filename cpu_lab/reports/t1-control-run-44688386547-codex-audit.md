# T1-256 対 control-256 全6本補助監査（run 44688386547・採否判定外）

作成: 2026-11-20（日本時間）

## 範囲と制約
- 対象: `dev220 / general / business / business2 / japan_procurement` のみ。
- 条件: control-256 と T1-256（各 seed 1〜3）、比較に使う `ft` と `blend70`。
- `blind_set*`、セット3・5・7、sealed2/3、b018は読んでいない。
- 評価JSONの列名・正解・予測・上位確率・判定理由だけを確認し、列の値は読んでいない。従って値文脈や元表の意味による原因確定はしていない。
- **訂正（2026-11-21）**：この固定試験には同行値が無く、controlとT1の評価token統計は5集合すべて完全一致した。T1は文脈ありで学習したが、この試験では文脈なしで評価されている。事前記録どおり、T1の採否は同行値を持つG4系の主比較で決める。本書は文脈欠落時の頑健性を読む補助監査である。
- 既存の自動分析 `error-analysis-run-44688386547.md` は40入力で止まり、全6 jobを覆っていなかった。本書は比較対象60ファイルを全件再集計した。

## 実行と成果物の確認
- GitHub Actions run: `44688386547`、head `20dca1286798e4cd2f198ae8a8d47dc77d8e4abb`。
- Kaggleは2026-11-20 18:14 JSTにCOMPLETE。`kaggle.request=done`。
- 評価artifact `jitsuris-evaluation-reports`: id `14615884982`、SHA-256 digest `bd605612789a12f963cb98f1c12dad29a27dd2758065b427b677d7b553e7b16f`。
- モデルartifact `jitsuris-model`: id `14616951272`、5,289,826,149 bytes、SHA-256 digest `8d035bf88710919f2d68179cdd4b9c7d5c0cb854f2146194291974185839cced`。
- control/T1は同じcommit・モデルrevision・教材・設定で、T1だけ `FT_ROWCTX=1`。manifestのcontrolはrow_contextなし、T1は`rowctx-v1`。

## 結果（3 seed合算）
| 条件 | 方式 | セット | 正答率 | 誤り | 重大 | unknown | other見落とし |
|---|---|---|---:|---:|---:|---:|---:|
| ft | control | dev220 | 96.52% | 19 | 3 | 4 | 0 |
| ft | control | general | 93.11% | 28 | 1 | 33 | 26 |
| ft | control | business | 96.83% | 25 | 4 | 21 | 1 |
| ft | control | business2 | 96.43% | 49 | 8 | 49 | 1 |
| ft | control | japan_procurement | 100.00% | 0 | 0 | 0 | 0 |
| blend70 | control | dev220 | 96.82% | 16 | 3 | 5 | 0 |
| blend70 | control | general | 93.45% | 24 | 0 | 34 | 23 |
| blend70 | control | business | 96.56% | 21 | 3 | 29 | 0 |
| blend70 | control | business2 | 96.58% | 42 | 6 | 52 | 2 |
| blend70 | control | japan_procurement | 100.00% | 0 | 0 | 0 | 0 |
| ft | T1 | dev220 | 96.21% | 24 | 4 | 1 | 0 |
| ft | T1 | general | 92.43% | 35 | 3 | 32 | 16 |
| ft | T1 | business | 96.90% | 25 | 6 | 20 | 0 |
| ft | T1 | business2 | 96.43% | 50 | 12 | 48 | 0 |
| ft | T1 | japan_procurement | 100.00% | 0 | 0 | 0 | 0 |
| blend70 | T1 | dev220 | 96.82% | 19 | 4 | 2 | 0 |
| blend70 | T1 | general | 91.75% | 30 | 0 | 43 | 13 |
| blend70 | T1 | business | 96.76% | 19 | 6 | 28 | 0 |
| blend70 | T1 | business2 | 96.25% | 47 | 12 | 56 | 3 |
| blend70 | T1 | japan_procurement | 100.00% | 0 | 0 | 0 | 0 |

## T1-control差（観測事実）
| 条件 | セット | 精度差pp | 誤り差 | 重大差 | unknown差 | 判定 |
|---|---|---:|---:|---:|---:|---|
| ft | dev220 | -0.31 | +5 | +1 | -3 | 差なし |
| ft | general | -0.68 | +7 | +2 | -1 | 差なし |
| ft | business | +0.07 | +0 | +2 | -1 | 差なし |
| ft | business2 | +0.00 | +1 | +4 | -1 | 差なし |
| ft | japan_procurement | +0.00 | +0 | +0 | +0 | 差なし |
| blend70 | dev220 | +0.00 | +3 | +1 | -3 | 差なし |
| blend70 | general | -1.70 | +6 | +0 | +9 | 悪化 |
| blend70 | business | +0.20 | -2 | +3 | -1 | 差なし |
| blend70 | business2 | -0.33 | +5 | +6 | +4 | 差なし |
| blend70 | japan_procurement | +0.00 | +0 | +0 | +0 | 差なし |

- `blend70/general`だけが閾値1.5ppを越えて **-1.70ppの悪化**。他は差なし。ただし全評価入力に同行値が無いため、これはT1本来の入力効果の採否判定ではない。
- 重大誤り合計はftでcontrol 16→T1 25、blend70でcontrol 12→T1 22。同行値が無い表への頑健性は悪化したが、この固定試験だけではT1の採否を決めない。
- 学習時間平均はcontrol 1,888秒、T1 3,249秒（約72%増）。peak GPU memoryはcontrol 6.4GiB、T1平均7.27GiB（約0.87GiB増）。
- T1学習入力は157,123件中33,662件（21.42%）が256 tokenで切詰め。controlは0件。

## 原因分析
### 確認できた事実
- 比較対象の誤り・unknown・other見落としは延べ1015件、固定列として145件。
- 誤り473件のうちtop-1確率0.8以上は180件。単なる低確率判定だけでは説明できない。
- 多い取り違えは `org→address` 53、`quantity→category` 42、`amount→quantity` 38、`text→category` 33、`account→category` 32。
- unknown理由は `probability_below_threshold` 156、`other_class` 125、`date_value_evidence_low` 112、`numeric_top2_too_close` 35、`numeric_values_not_parseable` 29。
- controlとT1の両方・複数seedで同じ誤りが反復する列があり、行文脈追加だけで解消しない失敗がある。

### 原因仮説
| 仮説 | 根拠 | 確度 | 追加確認 |
|---|---|---|---|
| 学習時は同行値あり、固定試験時は同行値なしという入力分布差が悪化の一因 | T1学習入力にはrowctx、5固定試験のcontrol/T1 token統計は完全一致、重大増 | 高（分布差の存在）・中（因果） | 同行値を持つG4系で主比較し、row_context_noneを分離 |
| 境界ラベルの教材不足または定義の曖昧さが再発を生む | org/address、amount/quantity、category/text等が複数seedで反復 | 中 | 元表とLABEL_GUIDEを教師2人が独立確認。裁定前はラベル変更禁止 |
| guardが正しいraw予測をunknownへ変えるケースが残る | date_value_evidence_low等が高top-1確率でも反復 | 中 | raw/guarded差を列別に再集計し、値を見ずに確定できる範囲を分離 |
| seed依存があり、T1の効果が安定していない | 同一セットでもseedごとの改善・悪化方向が一致しない | 高 | 3 seedのpaired bootstrapまたは表単位区間を出す |
| 実装差・artifact欠落が主因 | 6 manifestは同commit・同revisionで、60ファイルを回収 | 低 | artifact digestとmanifest SHAを保存し再現確認 |

## 優先する一要因
1. T1の採否は未決とし、事前登録どおり同行値を持つG4系の主比較で決める。それまでは製品と土台をL24/controlのまま維持する。
2. 高確信かつ全seed再発の境界ケースを、教師2人の独立確認へ回す。ラベルは裁定まで変更しない。
3. G4系では文脈あり列とrow_context_noneを分離し、同行値の効果と文脈欠落時の弱さを混ぜない。
4. guard由来unknownはraw正解/誤りを分け、guardだけの一要因として再検証する。

## 全件一覧（誤り・重大誤り・unknown・other見落とし）
| 方式 | 条件 | seed | セット | index | 列名 | 正解 | 予測 | 結果 | 重大 | top1確率 | 判定理由 |
|---|---|---:|---|---:|---|---|---|---|---|---:|---|
| control | blend70 | 1 | business | 46 | quarterno | date | unknown | unknown | no | 0.971617 | date_value_evidence_low |
| control | blend70 | 1 | business | 77 | publisher label | org | unknown | unknown | no | 0.445466 | probability_below_threshold |
| control | blend70 | 1 | business | 101 | entitiy | org | category | wrong | no | 0.583875 |  |
| control | blend70 | 1 | business | 148 | merchant details | text | category | wrong | no | 0.771639 |  |
| control | blend70 | 1 | business | 225 | description | account | text | wrong | no | 0.711952 |  |
| control | blend70 | 1 | business | 237 | purposeofexpenditure | text | account | wrong | no | 0.894302 |  |
| control | blend70 | 1 | business | 278 | 目名 | category | unknown | unknown | no | 0.928351 | other_class |
| control | blend70 | 1 | business | 279 | 科名 | category | unknown | unknown | no | 0.952754 | other_class |
| control | blend70 | 1 | business | 342 | commodity-title_en | product | unknown | unknown | no | 0.474441 | probability_below_threshold |
| control | blend70 | 1 | business | 343 | commodity-title_fr | product | unknown | unknown | no | 0.400636 | probability_below_threshold |
| control | blend70 | 1 | business | 344 | portefeuille_nom_et_code | org | unknown | unknown | no | 0.480068 | probability_below_threshold |
| control | blend70 | 1 | business | 347 | regrp_sommaire | account | category | wrong | no | 0.640775 |  |
| control | blend70 | 1 | business | 348 | regrp_nom | account | unknown | unknown | no | 0.441982 | probability_below_threshold |
| control | blend70 | 1 | business | 401 | ligne | category | unknown | unknown | no | 0.483388 | probability_below_threshold |
| control | blend70 | 1 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.766203 | date_value_evidence_low |
| control | blend70 | 1 | business | 451 | title | category | text | wrong | no | 0.523542 |  |
| control | blend70 | 1 | business2 | 45 | type | account | category | wrong | no | 0.628361 |  |
| control | blend70 | 1 | business2 | 75 | monitor | id | category | wrong | no | 0.583186 |  |
| control | blend70 | 1 | business2 | 176 | contravention | category | text | wrong | no | 0.619048 |  |
| control | blend70 | 1 | business2 | 177 | fine | amount | unknown | unknown | no | 0.359893 | probability_below_threshold |
| control | blend70 | 1 | business2 | 230 | warddesc | address | category | wrong | no | 0.573250 |  |
| control | blend70 | 1 | business2 | 238 | terrace | quantity | unknown | unknown | no | 0.454564 | probability_below_threshold |
| control | blend70 | 1 | business2 | 288 | construction_age_band | category | unknown | unknown | no | 0.366520 | probability_below_threshold |
| control | blend70 | 1 | business2 | 291 | epc_score_known | category | unknown | unknown | no | 0.430240 | probability_below_threshold |
| control | blend70 | 1 | business2 | 298 | number_habitable_rooms | quantity | unknown | unknown | no | 0.493229 | probability_below_threshold |
| control | blend70 | 1 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.687985 |  |
| control | blend70 | 1 | business2 | 301 | total_floor_area_known | category | unknown | unknown | no | 0.435977 | probability_below_threshold |
| control | blend70 | 1 | business2 | 325 | loac_group | category | address | wrong | no | 0.557790 |  |
| control | blend70 | 1 | business2 | 326 | fuel_poverty | rate | unknown | unknown | no | 0.616671 | other_class |
| control | blend70 | 1 | business2 | 370 | average bids per property | other | rate | other_ng | no | 0.506464 |  |
| control | blend70 | 1 | business2 | 379 | terrace | quantity | unknown | unknown | no | 0.443159 | probability_below_threshold |
| control | blend70 | 1 | business2 | 381 | total_verified_sales | quantity | amount | wrong | yes | 0.678100 |  |
| control | blend70 | 1 | business2 | 440 | situtation | address | text | wrong | no | 0.571052 |  |
| control | blend70 | 1 | business2 | 492 | value () | amount | unknown | unknown | no | 0.988955 | numeric_values_not_parseable |
| control | blend70 | 1 | business2 | 535 | scheme_description | category | unknown | unknown | no | 0.378056 | probability_below_threshold |
| control | blend70 | 1 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.981306 | numeric_values_not_parseable |
| control | blend70 | 1 | business2 | 562 | name | org | address | wrong | no | 0.841834 |  |
| control | blend70 | 1 | business2 | 581 | type of expenditure | account | category | wrong | no | 0.768340 |  |
| control | blend70 | 1 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.990322 | date_value_evidence_low |
| control | blend70 | 1 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.989518 | date_value_evidence_low |
| control | blend70 | 1 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.989077 | date_value_evidence_low |
| control | blend70 | 1 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.988168 | date_value_evidence_low |
| control | blend70 | 1 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.989000 | date_value_evidence_low |
| control | blend70 | 1 | business2 | 946 | service_responsable | account | category | wrong | no | 0.649505 |  |
| control | blend70 | 1 | business2 | 948 | numéro_uev | id | address | wrong | no | 0.792688 |  |
| control | blend70 | 1 | business2 | 956 | terminal | address | unknown | unknown | no | 0.491587 | probability_below_threshold |
| control | blend70 | 1 | business2 | 962 | service | account | unknown | unknown | no | 0.358777 | probability_below_threshold |
| control | blend70 | 1 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | unknown | no | 0.570253 | numeric_top2_too_close |
| control | blend70 | 1 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | unknown | no | 0.537807 | numeric_top2_too_close |
| control | blend70 | 1 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.978822 |  |
| control | blend70 | 1 | dev220 | 21 | ポイント | amount | unknown | unknown | no | 0.450267 | probability_below_threshold |
| control | blend70 | 1 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.869536 |  |
| control | blend70 | 1 | dev220 | 144 | location | org | address | wrong | no | 0.553982 |  |
| control | blend70 | 1 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.984454 |  |
| control | blend70 | 1 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.956111 |  |
| control | blend70 | 1 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.687397 |  |
| control | blend70 | 1 | dev220 | 201 | city | address | unknown | unknown | no | 0.497961 | probability_below_threshold |
| control | blend70 | 1 | general | 27 | keyword | category | text | wrong | no | 0.953609 |  |
| control | blend70 | 1 | general | 28 | fulltext rank | other | category | other_ng | no | 0.659472 |  |
| control | blend70 | 1 | general | 32 | 五島 | other | quantity | other_ng | no | 0.721038 |  |
| control | blend70 | 1 | general | 35 | denominatorunweighted | quantity | unknown | unknown | no | 0.466007 | probability_below_threshold |
| control | blend70 | 1 | general | 65 | app | category | unknown | unknown | no | 0.583035 | other_class |
| control | blend70 | 1 | general | 71 | property | category | unknown | unknown | no | 0.422045 | probability_below_threshold |
| control | blend70 | 1 | general | 83 | place | org | address | wrong | no | 0.860436 |  |
| control | blend70 | 1 | general | 87 | sens_final | rate | unknown | unknown | no | 0.667000 | other_class |
| control | blend70 | 1 | general | 94 | 名称_カナ | org | address | wrong | no | 0.798403 |  |
| control | blend70 | 1 | general | 121 | dag-stage | other | category | other_ng | no | 0.767946 |  |
| control | blend70 | 1 | general | 207 | year_step_size | quantity | category | wrong | no | 0.690944 |  |
| control | blend70 | 1 | general | 224 | study | text | unknown | unknown | no | 0.362913 | probability_below_threshold |
| control | blend70 | 1 | general | 227 | 発生日 | date | unknown | unknown | no | 0.988142 | date_value_evidence_low |
| control | blend70 | 1 | general | 234 | 発生県 | id | unknown | unknown | no | 0.356044 | probability_below_threshold |
| control | blend70 | 1 | general | 286 | value | other | rate | other_ng | no | 0.722831 |  |
| control | blend70 | 1 | general | 291 | cleaned | text | unknown | unknown | no | 0.494051 | probability_below_threshold |
| control | blend70 | 1 | general | 292 | abstract rank | other | category | other_ng | no | 0.703047 |  |
| control | blend70 | 1 | general | 296 | image_level_adj_acc | rate | unknown | unknown | no | 0.772826 | other_class |
| control | blend70 | 1 | general | 308 | ステーション名 | org | address | wrong | no | 0.778881 |  |
| control | blend70 | 1 | general | 309 | goal | id | category | wrong | no | 0.848203 |  |
| control | blend70 | 1 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.735996 | other_class |
| control | blend70 | 1 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.989308 | date_value_evidence_low |
| control | blend70 | 1 | general | 343 | mt2 | other | category | other_ng | no | 0.617864 |  |
| control | blend70 | 1 | general | 380 | 科名 | category | unknown | unknown | no | 0.929162 | other_class |
| control | blend70 | 1 | general | 382 | source | category | unknown | unknown | no | 0.444179 | probability_below_threshold |
| control | blend70 | 2 | business | 41 | total invoices paid | quantity | unknown | unknown | no | 0.511320 | numeric_top2_too_close |
| control | blend70 | 2 | business | 46 | quarterno | date | unknown | unknown | no | 0.965304 | date_value_evidence_low |
| control | blend70 | 2 | business | 77 | publisher label | org | address | wrong | no | 0.506092 |  |
| control | blend70 | 2 | business | 148 | merchant details | text | category | wrong | no | 0.607568 |  |
| control | blend70 | 2 | business | 237 | purposeofexpenditure | text | account | wrong | no | 0.855512 |  |
| control | blend70 | 2 | business | 278 | 目名 | category | unknown | unknown | no | 0.971665 | other_class |
| control | blend70 | 2 | business | 279 | 科名 | category | unknown | unknown | no | 0.968015 | other_class |
| control | blend70 | 2 | business | 342 | commodity-title_en | product | unknown | unknown | no | 0.386722 | probability_below_threshold |
| control | blend70 | 2 | business | 344 | portefeuille_nom_et_code | org | account | wrong | no | 0.632393 |  |
| control | blend70 | 2 | business | 347 | regrp_sommaire | account | category | wrong | no | 0.544249 |  |
| control | blend70 | 2 | business | 401 | ligne | category | id | wrong | no | 0.665331 |  |
| control | blend70 | 2 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.768356 | date_value_evidence_low |
| control | blend70 | 2 | business | 451 | title | category | account | wrong | no | 0.619331 |  |
| control | blend70 | 2 | business | 459 | australian sourced goods | amount | unknown | unknown | no | 0.496300 | probability_below_threshold |
| control | blend70 | 2 | business | 460 | australian sourced services | amount | unknown | unknown | no | 0.407228 | probability_below_threshold |
| control | blend70 | 2 | business | 461 | overseas sourced goods | amount | unknown | unknown | no | 0.396246 | probability_below_threshold |
| control | blend70 | 2 | business | 462 | overseas sourced services | amount | quantity | wrong | yes | 0.595483 |  |
| control | blend70 | 2 | business2 | 45 | type | account | category | wrong | no | 0.805104 |  |
| control | blend70 | 2 | business2 | 58 | numbers of | date | unknown | unknown | no | 0.470611 | probability_below_threshold |
| control | blend70 | 2 | business2 | 75 | monitor | id | category | wrong | no | 0.642444 |  |
| control | blend70 | 2 | business2 | 90 | total invoices paid | quantity | unknown | unknown | no | 0.542232 | numeric_top2_too_close |
| control | blend70 | 2 | business2 | 149 | projection | category | unknown | unknown | no | 0.494341 | probability_below_threshold |
| control | blend70 | 2 | business2 | 163 | projection | category | unknown | unknown | no | 0.478976 | probability_below_threshold |
| control | blend70 | 2 | business2 | 176 | contravention | category | text | wrong | no | 0.656261 |  |
| control | blend70 | 2 | business2 | 177 | fine | amount | unknown | unknown | no | 0.390555 | probability_below_threshold |
| control | blend70 | 2 | business2 | 230 | warddesc | address | category | wrong | no | 0.823218 |  |
| control | blend70 | 2 | business2 | 238 | terrace | quantity | unknown | unknown | no | 0.338559 | probability_below_threshold |
| control | blend70 | 2 | business2 | 291 | epc_score_known | category | unknown | unknown | no | 0.455530 | probability_below_threshold |
| control | blend70 | 2 | business2 | 298 | number_habitable_rooms | quantity | category | wrong | no | 0.702740 |  |
| control | blend70 | 2 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.602322 |  |
| control | blend70 | 2 | business2 | 301 | total_floor_area_known | category | quantity | wrong | no | 0.725341 |  |
| control | blend70 | 2 | business2 | 370 | average bids per property | other | rate | other_ng | no | 0.800739 |  |
| control | blend70 | 2 | business2 | 379 | terrace | quantity | unknown | unknown | no | 0.678746 | other_class |
| control | blend70 | 2 | business2 | 381 | total_verified_sales | quantity | unknown | unknown | no | 0.507168 | numeric_top2_too_close |
| control | blend70 | 2 | business2 | 440 | situtation | address | category | wrong | no | 0.806362 |  |
| control | blend70 | 2 | business2 | 492 | value () | amount | unknown | unknown | no | 0.988890 | numeric_values_not_parseable |
| control | blend70 | 2 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.984297 | numeric_values_not_parseable |
| control | blend70 | 2 | business2 | 562 | name | org | address | wrong | no | 0.804426 |  |
| control | blend70 | 2 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.990758 | date_value_evidence_low |
| control | blend70 | 2 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.987569 | date_value_evidence_low |
| control | blend70 | 2 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.985651 | date_value_evidence_low |
| control | blend70 | 2 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.985886 | date_value_evidence_low |
| control | blend70 | 2 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.987738 | date_value_evidence_low |
| control | blend70 | 2 | business2 | 945 | état | category | account | wrong | no | 0.648299 |  |
| control | blend70 | 2 | business2 | 946 | service_responsable | account | category | wrong | no | 0.710208 |  |
| control | blend70 | 2 | business2 | 948 | numéro_uev | id | address | wrong | no | 0.789973 |  |
| control | blend70 | 2 | business2 | 956 | terminal | address | unknown | unknown | no | 0.382083 | probability_below_threshold |
| control | blend70 | 2 | business2 | 958 | volume (mcf) | quantity | unknown | unknown | no | 0.558729 | other_class |
| control | blend70 | 2 | business2 | 962 | service | account | org | wrong | no | 0.629074 |  |
| control | blend70 | 2 | business2 | 970 | return-on-investments_revenus-de-placements | amount | unknown | unknown | no | 0.497425 | probability_below_threshold |
| control | blend70 | 2 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | unknown | no | 0.536666 | numeric_top2_too_close |
| control | blend70 | 2 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | wrong | yes | 0.801731 |  |
| control | blend70 | 2 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.954835 |  |
| control | blend70 | 2 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.846709 |  |
| control | blend70 | 2 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.990851 |  |
| control | blend70 | 2 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.968071 |  |
| control | blend70 | 2 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.900046 |  |
| control | blend70 | 2 | general | 1 | author | person | org | wrong | no | 0.918581 |  |
| control | blend70 | 2 | general | 27 | keyword | category | text | wrong | no | 0.957216 |  |
| control | blend70 | 2 | general | 28 | fulltext rank | other | category | other_ng | no | 0.724239 |  |
| control | blend70 | 2 | general | 32 | 五島 | other | quantity | other_ng | no | 0.756512 |  |
| control | blend70 | 2 | general | 35 | denominatorunweighted | quantity | unknown | unknown | no | 0.511656 | other_class |
| control | blend70 | 2 | general | 47 | mood | other | category | other_ng | no | 0.663879 |  |
| control | blend70 | 2 | general | 48 | source | category | org | wrong | no | 0.645115 |  |
| control | blend70 | 2 | general | 71 | property | category | unknown | unknown | no | 0.583294 | other_class |
| control | blend70 | 2 | general | 83 | place | org | address | wrong | no | 0.857876 |  |
| control | blend70 | 2 | general | 87 | sens_final | rate | unknown | unknown | no | 0.678180 | other_class |
| control | blend70 | 2 | general | 94 | 名称_カナ | org | address | wrong | no | 0.823173 |  |
| control | blend70 | 2 | general | 121 | dag-stage | other | quantity | other_ng | no | 0.568347 |  |
| control | blend70 | 2 | general | 207 | year_step_size | quantity | category | wrong | no | 0.646980 |  |
| control | blend70 | 2 | general | 227 | 発生日 | date | unknown | unknown | no | 0.987602 | date_value_evidence_low |
| control | blend70 | 2 | general | 234 | 発生県 | id | unknown | unknown | no | 0.382880 | probability_below_threshold |
| control | blend70 | 2 | general | 282 | 読み方 | address | unknown | unknown | no | 0.416246 | probability_below_threshold |
| control | blend70 | 2 | general | 286 | value | other | rate | other_ng | no | 0.904186 |  |
| control | blend70 | 2 | general | 291 | cleaned | text | category | wrong | no | 0.600822 |  |
| control | blend70 | 2 | general | 292 | abstract rank | other | category | other_ng | no | 0.708047 |  |
| control | blend70 | 2 | general | 296 | image_level_adj_acc | rate | unknown | unknown | no | 0.792333 | other_class |
| control | blend70 | 2 | general | 302 | episode | other | quantity | other_ng | no | 0.533051 |  |
| control | blend70 | 2 | general | 308 | ステーション名 | org | address | wrong | no | 0.704373 |  |
| control | blend70 | 2 | general | 309 | goal | id | category | wrong | no | 0.784548 |  |
| control | blend70 | 2 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.738186 | other_class |
| control | blend70 | 2 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.989678 | date_value_evidence_low |
| control | blend70 | 2 | general | 343 | mt2 | other | quantity | other_ng | no | 0.838464 |  |
| control | blend70 | 2 | general | 351 | operationid | other | id | other_ng | no | 0.701340 |  |
| control | blend70 | 2 | general | 370 | source_value | category | unknown | unknown | no | 0.499993 | probability_below_threshold |
| control | blend70 | 2 | general | 380 | 科名 | category | unknown | unknown | no | 0.979358 | other_class |
| control | blend70 | 3 | business | 41 | total invoices paid | quantity | amount | wrong | yes | 0.646112 |  |
| control | blend70 | 3 | business | 46 | quarterno | date | unknown | unknown | no | 0.967672 | date_value_evidence_low |
| control | blend70 | 3 | business | 148 | merchant details | text | org | wrong | no | 0.611405 |  |
| control | blend70 | 3 | business | 225 | description | account | text | wrong | no | 0.719858 |  |
| control | blend70 | 3 | business | 237 | purposeofexpenditure | text | account | wrong | no | 0.781867 |  |
| control | blend70 | 3 | business | 278 | 目名 | category | unknown | unknown | no | 0.965296 | other_class |
| control | blend70 | 3 | business | 279 | 科名 | category | unknown | unknown | no | 0.945292 | other_class |
| control | blend70 | 3 | business | 344 | portefeuille_nom_et_code | org | unknown | unknown | no | 0.371677 | probability_below_threshold |
| control | blend70 | 3 | business | 347 | regrp_sommaire | account | unknown | unknown | no | 0.444665 | probability_below_threshold |
| control | blend70 | 3 | business | 401 | ligne | category | id | wrong | no | 0.615000 |  |
| control | blend70 | 3 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.736971 | date_value_evidence_low |
| control | blend70 | 3 | business | 450 | sub_category | category | account | wrong | no | 0.568220 |  |
| control | blend70 | 3 | business | 451 | title | category | unknown | unknown | no | 0.469297 | probability_below_threshold |
| control | blend70 | 3 | business | 459 | australian sourced goods | amount | quantity | wrong | yes | 0.567843 |  |
| control | blend70 | 3 | business | 460 | australian sourced services | amount | unknown | unknown | no | 0.425044 | probability_below_threshold |
| control | blend70 | 3 | business | 461 | overseas sourced goods | amount | unknown | unknown | no | 0.499907 | probability_below_threshold |
| control | blend70 | 3 | business | 462 | overseas sourced services | amount | unknown | unknown | no | 0.528168 | numeric_top2_too_close |
| control | blend70 | 3 | business2 | 45 | type | account | category | wrong | no | 0.842524 |  |
| control | blend70 | 3 | business2 | 75 | monitor | id | unknown | unknown | no | 0.452526 | probability_below_threshold |
| control | blend70 | 3 | business2 | 90 | total invoices paid | quantity | unknown | unknown | no | 0.616842 | numeric_top2_too_close |
| control | blend70 | 3 | business2 | 177 | fine | amount | category | wrong | no | 0.752025 |  |
| control | blend70 | 3 | business2 | 230 | warddesc | address | category | wrong | no | 0.721094 |  |
| control | blend70 | 3 | business2 | 238 | terrace | quantity | unknown | unknown | no | 0.399908 | probability_below_threshold |
| control | blend70 | 3 | business2 | 298 | number_habitable_rooms | quantity | category | wrong | no | 0.701386 |  |
| control | blend70 | 3 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.669753 |  |
| control | blend70 | 3 | business2 | 301 | total_floor_area_known | category | quantity | wrong | no | 0.724363 |  |
| control | blend70 | 3 | business2 | 326 | fuel_poverty | rate | category | wrong | no | 0.631524 |  |
| control | blend70 | 3 | business2 | 379 | terrace | quantity | address | wrong | no | 0.507437 |  |
| control | blend70 | 3 | business2 | 381 | total_verified_sales | quantity | amount | wrong | yes | 0.646965 |  |
| control | blend70 | 3 | business2 | 440 | situtation | address | text | wrong | no | 0.592163 |  |
| control | blend70 | 3 | business2 | 492 | value () | amount | unknown | unknown | no | 0.990541 | numeric_values_not_parseable |
| control | blend70 | 3 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.983807 | numeric_values_not_parseable |
| control | blend70 | 3 | business2 | 562 | name | org | address | wrong | no | 0.635580 |  |
| control | blend70 | 3 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.988932 | date_value_evidence_low |
| control | blend70 | 3 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.985921 | date_value_evidence_low |
| control | blend70 | 3 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.984588 | date_value_evidence_low |
| control | blend70 | 3 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.984979 | date_value_evidence_low |
| control | blend70 | 3 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.984937 | date_value_evidence_low |
| control | blend70 | 3 | business2 | 946 | service_responsable | account | category | wrong | no | 0.719069 |  |
| control | blend70 | 3 | business2 | 962 | service | account | org | wrong | no | 0.569606 |  |
| control | blend70 | 3 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | unknown | no | 0.605086 | numeric_top2_too_close |
| control | blend70 | 3 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | unknown | no | 0.605664 | numeric_top2_too_close |
| control | blend70 | 3 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.975104 |  |
| control | blend70 | 3 | dev220 | 116 | 履行場所 | address | unknown | unknown | no | 0.490373 | probability_below_threshold |
| control | blend70 | 3 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.762368 |  |
| control | blend70 | 3 | dev220 | 130 | 随意契約理由 | text | category | wrong | no | 0.562927 |  |
| control | blend70 | 3 | dev220 | 151 | taxable | category | tax_class | wrong | no | 0.543390 |  |
| control | blend70 | 3 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.979934 |  |
| control | blend70 | 3 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.961738 |  |
| control | blend70 | 3 | dev220 | 174 | sales order | id | unknown | unknown | no | 0.638559 | date_value_evidence_low |
| control | blend70 | 3 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.840856 |  |
| control | blend70 | 3 | dev220 | 196 | credit limit | amount | unknown | unknown | no | 0.517024 | numeric_top2_too_close |
| control | blend70 | 3 | dev220 | 201 | city | address | id | wrong | no | 0.532065 |  |
| control | blend70 | 3 | general | 27 | keyword | category | text | wrong | no | 0.956476 |  |
| control | blend70 | 3 | general | 28 | fulltext rank | other | category | other_ng | no | 0.536786 |  |
| control | blend70 | 3 | general | 32 | 五島 | other | quantity | other_ng | no | 0.983170 |  |
| control | blend70 | 3 | general | 35 | denominatorunweighted | quantity | unknown | unknown | no | 0.538637 | other_class |
| control | blend70 | 3 | general | 71 | property | category | unknown | unknown | no | 0.621383 | other_class |
| control | blend70 | 3 | general | 83 | place | org | address | wrong | no | 0.908469 |  |
| control | blend70 | 3 | general | 87 | sens_final | rate | unknown | unknown | no | 0.585586 | other_class |
| control | blend70 | 3 | general | 94 | 名称_カナ | org | address | wrong | no | 0.762495 |  |
| control | blend70 | 3 | general | 112 | 住家全壊 | quantity | unknown | unknown | no | 0.352213 | probability_below_threshold |
| control | blend70 | 3 | general | 121 | dag-stage | other | category | other_ng | no | 0.647354 |  |
| control | blend70 | 3 | general | 134 | dbpedia_score | other | rate | other_ng | no | 0.754454 |  |
| control | blend70 | 3 | general | 207 | year_step_size | quantity | category | wrong | no | 0.671566 |  |
| control | blend70 | 3 | general | 224 | study | text | unknown | unknown | no | 0.468510 | probability_below_threshold |
| control | blend70 | 3 | general | 227 | 発生日 | date | unknown | unknown | no | 0.989137 | date_value_evidence_low |
| control | blend70 | 3 | general | 282 | 読み方 | address | text | wrong | no | 0.535512 |  |
| control | blend70 | 3 | general | 286 | value | other | rate | other_ng | no | 0.771619 |  |
| control | blend70 | 3 | general | 291 | cleaned | text | category | wrong | no | 0.862322 |  |
| control | blend70 | 3 | general | 292 | abstract rank | other | category | other_ng | no | 0.648066 |  |
| control | blend70 | 3 | general | 302 | episode | other | id | other_ng | no | 0.528399 |  |
| control | blend70 | 3 | general | 308 | ステーション名 | org | address | wrong | no | 0.735537 |  |
| control | blend70 | 3 | general | 309 | goal | id | category | wrong | no | 0.520879 |  |
| control | blend70 | 3 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.735332 | other_class |
| control | blend70 | 3 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.991903 | date_value_evidence_low |
| control | blend70 | 3 | general | 343 | mt2 | other | category | other_ng | no | 0.580154 |  |
| control | blend70 | 3 | general | 370 | source_value | category | unknown | unknown | no | 0.498968 | probability_below_threshold |
| control | blend70 | 3 | general | 377 | indicator | text | category | wrong | no | 0.500050 |  |
| control | blend70 | 3 | general | 380 | 科名 | category | unknown | unknown | no | 0.948760 | other_class |
| control | ft | 1 | business | 46 | quarterno | date | unknown | unknown | no | 0.988127 | date_value_evidence_low |
| control | ft | 1 | business | 101 | entitiy | org | category | wrong | no | 0.832372 |  |
| control | ft | 1 | business | 148 | merchant details | text | category | wrong | no | 0.886544 |  |
| control | ft | 1 | business | 225 | description | account | text | wrong | no | 0.954505 |  |
| control | ft | 1 | business | 237 | purposeofexpenditure | text | account | wrong | no | 0.879569 |  |
| control | ft | 1 | business | 278 | 目名 | category | unknown | unknown | no | 0.905612 | other_class |
| control | ft | 1 | business | 279 | 科名 | category | unknown | unknown | no | 0.955659 | other_class |
| control | ft | 1 | business | 342 | commodity-title_en | product | category | wrong | no | 0.660496 |  |
| control | ft | 1 | business | 344 | portefeuille_nom_et_code | org | unknown | unknown | no | 0.409427 | probability_below_threshold |
| control | ft | 1 | business | 347 | regrp_sommaire | account | category | wrong | no | 0.830211 |  |
| control | ft | 1 | business | 348 | regrp_nom | account | unknown | unknown | no | 0.472492 | probability_below_threshold |
| control | ft | 1 | business | 401 | ligne | category | id | wrong | no | 0.634040 |  |
| control | ft | 1 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.980844 | date_value_evidence_low |
| control | ft | 1 | business | 451 | title | category | text | wrong | no | 0.615736 |  |
| control | ft | 1 | business2 | 75 | monitor | id | category | wrong | no | 0.777858 |  |
| control | ft | 1 | business2 | 176 | contravention | category | text | wrong | no | 0.722261 |  |
| control | ft | 1 | business2 | 177 | fine | amount | rate | wrong | yes | 0.512013 |  |
| control | ft | 1 | business2 | 230 | warddesc | address | category | wrong | no | 0.525140 |  |
| control | ft | 1 | business2 | 238 | terrace | quantity | unknown | unknown | no | 0.594020 | other_class |
| control | ft | 1 | business2 | 288 | construction_age_band | category | unknown | unknown | no | 0.455595 | probability_below_threshold |
| control | ft | 1 | business2 | 291 | epc_score_known | category | unknown | unknown | no | 0.589766 | other_class |
| control | ft | 1 | business2 | 295 | potential_epc_score_known | category | unknown | unknown | no | 0.478023 | probability_below_threshold |
| control | ft | 1 | business2 | 298 | number_habitable_rooms | quantity | unknown | unknown | no | 0.700250 | numeric_values_not_parseable |
| control | ft | 1 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.949520 |  |
| control | ft | 1 | business2 | 301 | total_floor_area_known | category | unknown | unknown | no | 0.499501 | probability_below_threshold |
| control | ft | 1 | business2 | 325 | loac_group | category | address | wrong | no | 0.796806 |  |
| control | ft | 1 | business2 | 326 | fuel_poverty | rate | unknown | unknown | no | 0.865907 | other_class |
| control | ft | 1 | business2 | 356 | want to live in this parish only | quantity | unknown | unknown | no | 0.494018 | probability_below_threshold |
| control | ft | 1 | business2 | 379 | terrace | quantity | address | wrong | no | 0.632813 |  |
| control | ft | 1 | business2 | 381 | total_verified_sales | quantity | amount | wrong | yes | 0.967278 |  |
| control | ft | 1 | business2 | 440 | situtation | address | text | wrong | no | 0.785827 |  |
| control | ft | 1 | business2 | 492 | value () | amount | unknown | unknown | no | 0.988892 | numeric_values_not_parseable |
| control | ft | 1 | business2 | 535 | scheme_description | category | unknown | unknown | no | 0.495720 | probability_below_threshold |
| control | ft | 1 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.973796 | numeric_values_not_parseable |
| control | ft | 1 | business2 | 562 | name | org | address | wrong | no | 0.783866 |  |
| control | ft | 1 | business2 | 581 | type of expenditure | account | category | wrong | no | 0.800326 |  |
| control | ft | 1 | business2 | 633 | household disposable income quintiles | category | unknown | unknown | no | 0.439491 | probability_below_threshold |
| control | ft | 1 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.987311 | date_value_evidence_low |
| control | ft | 1 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.985590 | date_value_evidence_low |
| control | ft | 1 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.985008 | date_value_evidence_low |
| control | ft | 1 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.983719 | date_value_evidence_low |
| control | ft | 1 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.987602 | date_value_evidence_low |
| control | ft | 1 | business2 | 946 | service_responsable | account | category | wrong | no | 0.527114 |  |
| control | ft | 1 | business2 | 948 | numéro_uev | id | address | wrong | no | 0.874479 |  |
| control | ft | 1 | business2 | 962 | service | account | org | wrong | no | 0.511036 |  |
| control | ft | 1 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | unknown | no | 0.574522 | numeric_top2_too_close |
| control | ft | 1 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | unknown | no | 0.565553 | numeric_top2_too_close |
| control | ft | 1 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.990196 |  |
| control | ft | 1 | dev220 | 21 | ポイント | amount | unknown | unknown | no | 0.633953 | other_class |
| control | ft | 1 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.928037 |  |
| control | ft | 1 | dev220 | 144 | location | org | address | wrong | no | 0.772556 |  |
| control | ft | 1 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.981688 |  |
| control | ft | 1 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.974423 |  |
| control | ft | 1 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.654575 |  |
| control | ft | 1 | dev220 | 189 | payment terms | category | unknown | unknown | no | 0.498871 | probability_below_threshold |
| control | ft | 1 | dev220 | 201 | city | address | id | wrong | no | 0.689641 |  |
| control | ft | 1 | general | 27 | keyword | category | text | wrong | no | 0.953094 |  |
| control | ft | 1 | general | 28 | fulltext rank | other | category | other_ng | no | 0.869420 |  |
| control | ft | 1 | general | 32 | 五島 | other | quantity | other_ng | no | 0.602880 |  |
| control | ft | 1 | general | 35 | denominatorunweighted | quantity | unknown | unknown | no | 0.629844 | other_class |
| control | ft | 1 | general | 47 | mood | other | category | other_ng | no | 0.666002 |  |
| control | ft | 1 | general | 65 | app | category | unknown | unknown | no | 0.831033 | other_class |
| control | ft | 1 | general | 71 | property | category | unknown | unknown | no | 0.602581 | other_class |
| control | ft | 1 | general | 83 | place | org | address | wrong | no | 0.813384 |  |
| control | ft | 1 | general | 87 | sens_final | rate | unknown | unknown | no | 0.951176 | other_class |
| control | ft | 1 | general | 94 | 名称_カナ | org | address | wrong | no | 0.776355 |  |
| control | ft | 1 | general | 121 | dag-stage | other | category | other_ng | no | 0.977609 |  |
| control | ft | 1 | general | 207 | year_step_size | quantity | category | wrong | no | 0.886030 |  |
| control | ft | 1 | general | 224 | study | text | unknown | unknown | no | 0.491851 | probability_below_threshold |
| control | ft | 1 | general | 227 | 発生日 | date | unknown | unknown | no | 0.988782 | date_value_evidence_low |
| control | ft | 1 | general | 234 | 発生県 | id | address | wrong | no | 0.508241 |  |
| control | ft | 1 | general | 286 | value | other | rate | other_ng | no | 0.642407 |  |
| control | ft | 1 | general | 291 | cleaned | text | unknown | unknown | no | 0.484634 | probability_below_threshold |
| control | ft | 1 | general | 292 | abstract rank | other | category | other_ng | no | 0.975920 |  |
| control | ft | 1 | general | 296 | image_level_adj_acc | rate | unknown | unknown | no | 0.912969 | other_class |
| control | ft | 1 | general | 308 | ステーション名 | org | address | wrong | no | 0.853684 |  |
| control | ft | 1 | general | 309 | goal | id | category | wrong | no | 0.817360 |  |
| control | ft | 1 | general | 315 | standardhours | quantity | unknown | unknown | no | 0.486566 | probability_below_threshold |
| control | ft | 1 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.987169 | other_class |
| control | ft | 1 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.984726 | date_value_evidence_low |
| control | ft | 1 | general | 343 | mt2 | other | category | other_ng | no | 0.879155 |  |
| control | ft | 1 | general | 370 | source_value | category | unknown | unknown | no | 0.434785 | probability_below_threshold |
| control | ft | 1 | general | 380 | 科名 | category | unknown | unknown | no | 0.906307 | other_class |
| control | ft | 1 | general | 382 | source | category | text | wrong | no | 0.581935 |  |
| control | ft | 2 | business | 46 | quarterno | date | unknown | unknown | no | 0.979108 | date_value_evidence_low |
| control | ft | 2 | business | 77 | publisher label | org | address | wrong | no | 0.683478 |  |
| control | ft | 2 | business | 101 | entitiy | org | account | wrong | no | 0.619642 |  |
| control | ft | 2 | business | 148 | merchant details | text | category | wrong | no | 0.652156 |  |
| control | ft | 2 | business | 237 | purposeofexpenditure | text | account | wrong | no | 0.824154 |  |
| control | ft | 2 | business | 278 | 目名 | category | unknown | unknown | no | 0.967489 | other_class |
| control | ft | 2 | business | 279 | 科名 | category | unknown | unknown | no | 0.977461 | other_class |
| control | ft | 2 | business | 344 | portefeuille_nom_et_code | org | account | wrong | no | 0.597357 |  |
| control | ft | 2 | business | 347 | regrp_sommaire | account | category | wrong | no | 0.692317 |  |
| control | ft | 2 | business | 401 | ligne | category | id | wrong | no | 0.933302 |  |
| control | ft | 2 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.983919 | date_value_evidence_low |
| control | ft | 2 | business | 451 | title | category | account | wrong | no | 0.867280 |  |
| control | ft | 2 | business | 459 | australian sourced goods | amount | quantity | wrong | yes | 0.707732 |  |
| control | ft | 2 | business | 460 | australian sourced services | amount | unknown | unknown | no | 0.493850 | probability_below_threshold |
| control | ft | 2 | business | 461 | overseas sourced goods | amount | unknown | unknown | no | 0.565051 | numeric_top2_too_close |
| control | ft | 2 | business | 462 | overseas sourced services | amount | quantity | wrong | yes | 0.618710 |  |
| control | ft | 2 | business2 | 45 | type | account | category | wrong | no | 0.726307 |  |
| control | ft | 2 | business2 | 58 | numbers of | date | unknown | unknown | no | 0.477401 | probability_below_threshold |
| control | ft | 2 | business2 | 75 | monitor | id | category | wrong | no | 0.862511 |  |
| control | ft | 2 | business2 | 176 | contravention | category | text | wrong | no | 0.775422 |  |
| control | ft | 2 | business2 | 177 | fine | amount | unknown | unknown | no | 0.405249 | probability_below_threshold |
| control | ft | 2 | business2 | 230 | warddesc | address | category | wrong | no | 0.882236 |  |
| control | ft | 2 | business2 | 238 | terrace | quantity | unknown | unknown | no | 0.482502 | probability_below_threshold |
| control | ft | 2 | business2 | 291 | epc_score_known | category | quantity | wrong | no | 0.551757 |  |
| control | ft | 2 | business2 | 298 | number_habitable_rooms | quantity | category | wrong | no | 0.581192 |  |
| control | ft | 2 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.827144 |  |
| control | ft | 2 | business2 | 301 | total_floor_area_known | category | quantity | wrong | no | 0.933292 |  |
| control | ft | 2 | business2 | 326 | fuel_poverty | rate | unknown | unknown | no | 0.486851 | probability_below_threshold |
| control | ft | 2 | business2 | 370 | average bids per property | other | rate | other_ng | no | 0.760853 |  |
| control | ft | 2 | business2 | 379 | terrace | quantity | unknown | unknown | no | 0.954319 | other_class |
| control | ft | 2 | business2 | 381 | total_verified_sales | quantity | amount | wrong | yes | 0.723091 |  |
| control | ft | 2 | business2 | 440 | situtation | address | category | wrong | no | 0.799540 |  |
| control | ft | 2 | business2 | 492 | value () | amount | unknown | unknown | no | 0.988800 | numeric_values_not_parseable |
| control | ft | 2 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.978069 | numeric_values_not_parseable |
| control | ft | 2 | business2 | 562 | name | org | address | wrong | no | 0.730426 |  |
| control | ft | 2 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.987934 | date_value_evidence_low |
| control | ft | 2 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.982805 | date_value_evidence_low |
| control | ft | 2 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.980113 | date_value_evidence_low |
| control | ft | 2 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.980459 | date_value_evidence_low |
| control | ft | 2 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.985799 | date_value_evidence_low |
| control | ft | 2 | business2 | 944 | numéro_de_lot | id | unknown | unknown | no | 0.490575 | probability_below_threshold |
| control | ft | 2 | business2 | 945 | état | category | account | wrong | no | 0.924471 |  |
| control | ft | 2 | business2 | 946 | service_responsable | account | category | wrong | no | 0.613833 |  |
| control | ft | 2 | business2 | 948 | numéro_uev | id | address | wrong | no | 0.870601 |  |
| control | ft | 2 | business2 | 956 | terminal | address | org | wrong | no | 0.541988 |  |
| control | ft | 2 | business2 | 957 | volume (10^3 m3) | quantity | unknown | unknown | no | 0.509509 | other_class |
| control | ft | 2 | business2 | 958 | volume (mcf) | quantity | unknown | unknown | no | 0.680214 | other_class |
| control | ft | 2 | business2 | 962 | service | account | org | wrong | no | 0.897174 |  |
| control | ft | 2 | business2 | 963 | numéro entente-cadre | id | unknown | unknown | no | 0.544764 | numeric_top2_too_close |
| control | ft | 2 | business2 | 970 | return-on-investments_revenus-de-placements | amount | unknown | unknown | no | 0.506105 | numeric_top2_too_close |
| control | ft | 2 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | unknown | no | 0.526541 | numeric_top2_too_close |
| control | ft | 2 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | wrong | yes | 0.783980 |  |
| control | ft | 2 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.955928 |  |
| control | ft | 2 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.895427 |  |
| control | ft | 2 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.990826 |  |
| control | ft | 2 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.991508 |  |
| control | ft | 2 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.958360 |  |
| control | ft | 2 | general | 1 | author | person | org | wrong | no | 0.895093 |  |
| control | ft | 2 | general | 27 | keyword | category | text | wrong | no | 0.958247 |  |
| control | ft | 2 | general | 28 | fulltext rank | other | category | other_ng | no | 0.961943 |  |
| control | ft | 2 | general | 32 | 五島 | other | quantity | other_ng | no | 0.653558 |  |
| control | ft | 2 | general | 35 | denominatorunweighted | quantity | unknown | unknown | no | 0.695056 | other_class |
| control | ft | 2 | general | 47 | mood | other | category | other_ng | no | 0.946479 |  |
| control | ft | 2 | general | 48 | source | category | org | wrong | no | 0.900561 |  |
| control | ft | 2 | general | 71 | property | category | unknown | unknown | no | 0.832937 | other_class |
| control | ft | 2 | general | 83 | place | org | address | wrong | no | 0.809726 |  |
| control | ft | 2 | general | 87 | sens_final | rate | unknown | unknown | no | 0.967147 | other_class |
| control | ft | 2 | general | 94 | 名称_カナ | org | address | wrong | no | 0.811742 |  |
| control | ft | 2 | general | 121 | dag-stage | other | quantity | other_ng | no | 0.507517 |  |
| control | ft | 2 | general | 207 | year_step_size | quantity | category | wrong | no | 0.823225 |  |
| control | ft | 2 | general | 227 | 発生日 | date | unknown | unknown | no | 0.988010 | date_value_evidence_low |
| control | ft | 2 | general | 234 | 発生県 | id | unknown | unknown | no | 0.410475 | probability_below_threshold |
| control | ft | 2 | general | 286 | value | other | rate | other_ng | no | 0.901485 |  |
| control | ft | 2 | general | 291 | cleaned | text | account | wrong | no | 0.501729 |  |
| control | ft | 2 | general | 292 | abstract rank | other | category | other_ng | no | 0.983063 |  |
| control | ft | 2 | general | 296 | image_level_adj_acc | rate | unknown | unknown | no | 0.940836 | other_class |
| control | ft | 2 | general | 302 | episode | other | quantity | other_ng | no | 0.761392 |  |
| control | ft | 2 | general | 308 | ステーション名 | org | address | wrong | no | 0.747244 |  |
| control | ft | 2 | general | 309 | goal | id | category | wrong | no | 0.726424 |  |
| control | ft | 2 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.990298 | other_class |
| control | ft | 2 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.985255 | date_value_evidence_low |
| control | ft | 2 | general | 343 | mt2 | other | quantity | other_ng | no | 0.838966 |  |
| control | ft | 2 | general | 351 | operationid | other | id | other_ng | no | 0.912260 |  |
| control | ft | 2 | general | 370 | source_value | category | text | wrong | no | 0.707540 |  |
| control | ft | 2 | general | 380 | 科名 | category | unknown | unknown | no | 0.978016 | other_class |
| control | ft | 3 | business | 41 | total invoices paid | quantity | unknown | unknown | no | 0.495095 | probability_below_threshold |
| control | ft | 3 | business | 46 | quarterno | date | unknown | unknown | no | 0.982492 | date_value_evidence_low |
| control | ft | 3 | business | 148 | merchant details | text | org | wrong | no | 0.783593 |  |
| control | ft | 3 | business | 225 | description | account | text | wrong | no | 0.965800 |  |
| control | ft | 3 | business | 237 | purposeofexpenditure | text | account | wrong | no | 0.718948 |  |
| control | ft | 3 | business | 278 | 目名 | category | unknown | unknown | no | 0.958390 | other_class |
| control | ft | 3 | business | 279 | 科名 | category | unknown | unknown | no | 0.945000 | other_class |
| control | ft | 3 | business | 344 | portefeuille_nom_et_code | org | unknown | unknown | no | 0.439486 | probability_below_threshold |
| control | ft | 3 | business | 401 | ligne | category | id | wrong | no | 0.861400 |  |
| control | ft | 3 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.939083 | date_value_evidence_low |
| control | ft | 3 | business | 408 | km budgété | other | quantity | other_ng | no | 0.624177 |  |
| control | ft | 3 | business | 450 | sub_category | category | account | wrong | no | 0.701529 |  |
| control | ft | 3 | business | 451 | title | category | unknown | unknown | no | 0.457535 | probability_below_threshold |
| control | ft | 3 | business | 459 | australian sourced goods | amount | quantity | wrong | yes | 0.809936 |  |
| control | ft | 3 | business | 460 | australian sourced services | amount | unknown | unknown | no | 0.604542 | numeric_top2_too_close |
| control | ft | 3 | business | 461 | overseas sourced goods | amount | quantity | wrong | yes | 0.713138 |  |
| control | ft | 3 | business | 462 | overseas sourced services | amount | unknown | unknown | no | 0.522547 | numeric_top2_too_close |
| control | ft | 3 | business2 | 45 | type | account | category | wrong | no | 0.779764 |  |
| control | ft | 3 | business2 | 90 | total invoices paid | quantity | unknown | unknown | no | 0.531245 | numeric_top2_too_close |
| control | ft | 3 | business2 | 151 | habitatdescription | text | category | wrong | no | 0.583821 |  |
| control | ft | 3 | business2 | 177 | fine | amount | category | wrong | no | 0.921634 |  |
| control | ft | 3 | business2 | 230 | warddesc | address | category | wrong | no | 0.736345 |  |
| control | ft | 3 | business2 | 238 | terrace | quantity | address | wrong | no | 0.570142 |  |
| control | ft | 3 | business2 | 291 | epc_score_known | category | unknown | unknown | no | 0.447041 | probability_below_threshold |
| control | ft | 3 | business2 | 298 | number_habitable_rooms | quantity | category | wrong | no | 0.579259 |  |
| control | ft | 3 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.923474 |  |
| control | ft | 3 | business2 | 301 | total_floor_area_known | category | quantity | wrong | no | 0.931896 |  |
| control | ft | 3 | business2 | 326 | fuel_poverty | rate | category | wrong | no | 0.895266 |  |
| control | ft | 3 | business2 | 330 | conservation_area_site_id | category | id | wrong | no | 0.524950 |  |
| control | ft | 3 | business2 | 364 | want to live in this parish & band a | quantity | unknown | unknown | no | 0.457952 | probability_below_threshold |
| control | ft | 3 | business2 | 367 | want to live in this parish & band d | quantity | unknown | unknown | no | 0.449683 | probability_below_threshold |
| control | ft | 3 | business2 | 379 | terrace | quantity | address | wrong | no | 0.724640 |  |
| control | ft | 3 | business2 | 381 | total_verified_sales | quantity | amount | wrong | yes | 0.922801 |  |
| control | ft | 3 | business2 | 440 | situtation | address | text | wrong | no | 0.815986 |  |
| control | ft | 3 | business2 | 492 | value () | amount | unknown | unknown | no | 0.991158 | numeric_values_not_parseable |
| control | ft | 3 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.977368 | numeric_values_not_parseable |
| control | ft | 3 | business2 | 548 | health service executive area | address | unknown | unknown | no | 0.487190 | probability_below_threshold |
| control | ft | 3 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.985326 | date_value_evidence_low |
| control | ft | 3 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.980450 | date_value_evidence_low |
| control | ft | 3 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.978594 | date_value_evidence_low |
| control | ft | 3 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.979163 | date_value_evidence_low |
| control | ft | 3 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.981798 | date_value_evidence_low |
| control | ft | 3 | business2 | 946 | service_responsable | account | category | wrong | no | 0.626492 |  |
| control | ft | 3 | business2 | 962 | service | account | org | wrong | no | 0.812219 |  |
| control | ft | 3 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.984883 |  |
| control | ft | 3 | dev220 | 49 | 税率 | rate | tax_class | wrong | no | 0.537856 |  |
| control | ft | 3 | dev220 | 116 | 履行場所 | address | id | wrong | no | 0.670341 |  |
| control | ft | 3 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.774939 |  |
| control | ft | 3 | dev220 | 130 | 随意契約理由 | text | category | wrong | no | 0.797320 |  |
| control | ft | 3 | dev220 | 144 | location | org | address | wrong | no | 0.527971 |  |
| control | ft | 3 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.975230 |  |
| control | ft | 3 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.982461 |  |
| control | ft | 3 | dev220 | 174 | sales order | id | unknown | unknown | no | 0.905395 | date_value_evidence_low |
| control | ft | 3 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.873803 |  |
| control | ft | 3 | dev220 | 196 | credit limit | amount | unknown | unknown | no | 0.561133 | numeric_top2_too_close |
| control | ft | 3 | dev220 | 201 | city | address | id | wrong | no | 0.738360 |  |
| control | ft | 3 | general | 6 | hydrozoa_indet | category | unknown | unknown | no | 0.480829 | probability_below_threshold |
| control | ft | 3 | general | 27 | keyword | category | text | wrong | no | 0.957191 |  |
| control | ft | 3 | general | 28 | fulltext rank | other | category | other_ng | no | 0.694154 |  |
| control | ft | 3 | general | 32 | 五島 | other | quantity | other_ng | no | 0.977354 |  |
| control | ft | 3 | general | 35 | denominatorunweighted | quantity | unknown | unknown | no | 0.733601 | other_class |
| control | ft | 3 | general | 47 | mood | other | category | other_ng | no | 0.645959 |  |
| control | ft | 3 | general | 48 | source | category | unknown | unknown | no | 0.470217 | probability_below_threshold |
| control | ft | 3 | general | 71 | property | category | unknown | unknown | no | 0.887349 | other_class |
| control | ft | 3 | general | 83 | place | org | address | wrong | no | 0.882002 |  |
| control | ft | 3 | general | 87 | sens_final | rate | unknown | unknown | no | 0.834869 | other_class |
| control | ft | 3 | general | 94 | 名称_カナ | org | address | wrong | no | 0.725058 |  |
| control | ft | 3 | general | 104 | term | text | category | wrong | no | 0.560686 |  |
| control | ft | 3 | general | 112 | 住家全壊 | quantity | unknown | unknown | no | 0.464008 | probability_below_threshold |
| control | ft | 3 | general | 121 | dag-stage | other | category | other_ng | no | 0.805334 |  |
| control | ft | 3 | general | 132 | _status_ | other | category | other_ng | no | 0.674684 |  |
| control | ft | 3 | general | 134 | dbpedia_score | other | rate | other_ng | no | 0.780061 |  |
| control | ft | 3 | general | 207 | year_step_size | quantity | category | wrong | no | 0.858347 |  |
| control | ft | 3 | general | 227 | 発生日 | date | unknown | unknown | no | 0.990203 | date_value_evidence_low |
| control | ft | 3 | general | 282 | 読み方 | address | unknown | unknown | no | 0.434104 | probability_below_threshold |
| control | ft | 3 | general | 286 | value | other | rate | other_ng | no | 0.712103 |  |
| control | ft | 3 | general | 291 | cleaned | text | category | wrong | no | 0.813503 |  |
| control | ft | 3 | general | 292 | abstract rank | other | category | other_ng | no | 0.897376 |  |
| control | ft | 3 | general | 302 | episode | other | id | other_ng | no | 0.511876 |  |
| control | ft | 3 | general | 308 | ステーション名 | org | address | wrong | no | 0.791764 |  |
| control | ft | 3 | general | 309 | goal | id | quantity | wrong | yes | 0.598813 |  |
| control | ft | 3 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.986220 | other_class |
| control | ft | 3 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.988433 | date_value_evidence_low |
| control | ft | 3 | general | 343 | mt2 | other | category | other_ng | no | 0.825283 |  |
| control | ft | 3 | general | 370 | source_value | category | text | wrong | no | 0.706075 |  |
| control | ft | 3 | general | 377 | indicator | text | category | wrong | no | 0.692052 |  |
| control | ft | 3 | general | 380 | 科名 | category | unknown | unknown | no | 0.934303 | other_class |
| T1 | blend70 | 1 | business | 41 | total invoices paid | quantity | amount | wrong | yes | 0.810293 |  |
| T1 | blend70 | 1 | business | 46 | quarterno | date | unknown | unknown | no | 0.971503 | date_value_evidence_low |
| T1 | blend70 | 1 | business | 77 | publisher label | org | unknown | unknown | no | 0.442579 | probability_below_threshold |
| T1 | blend70 | 1 | business | 101 | entitiy | org | account | wrong | no | 0.519728 |  |
| T1 | blend70 | 1 | business | 148 | merchant details | text | category | wrong | no | 0.781626 |  |
| T1 | blend70 | 1 | business | 237 | purposeofexpenditure | text | account | wrong | no | 0.847809 |  |
| T1 | blend70 | 1 | business | 278 | 目名 | category | unknown | unknown | no | 0.916291 | other_class |
| T1 | blend70 | 1 | business | 279 | 科名 | category | unknown | unknown | no | 0.881391 | other_class |
| T1 | blend70 | 1 | business | 344 | portefeuille_nom_et_code | org | unknown | unknown | no | 0.318903 | probability_below_threshold |
| T1 | blend70 | 1 | business | 347 | regrp_sommaire | account | unknown | unknown | no | 0.419977 | probability_below_threshold |
| T1 | blend70 | 1 | business | 401 | ligne | category | unknown | unknown | no | 0.411041 | probability_below_threshold |
| T1 | blend70 | 1 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.761533 | date_value_evidence_low |
| T1 | blend70 | 1 | business | 421 | abn | id | amount | wrong | yes | 0.602360 |  |
| T1 | blend70 | 1 | business | 451 | title | category | account | wrong | no | 0.534936 |  |
| T1 | blend70 | 1 | business | 459 | australian sourced goods | amount | quantity | wrong | yes | 0.597095 |  |
| T1 | blend70 | 1 | business | 461 | overseas sourced goods | amount | quantity | wrong | yes | 0.618595 |  |
| T1 | blend70 | 1 | business | 462 | overseas sourced services | amount | unknown | unknown | no | 0.495906 | probability_below_threshold |
| T1 | blend70 | 1 | business2 | 45 | type | account | category | wrong | no | 0.850014 |  |
| T1 | blend70 | 1 | business2 | 75 | monitor | id | category | wrong | no | 0.559636 |  |
| T1 | blend70 | 1 | business2 | 90 | total invoices paid | quantity | amount | wrong | yes | 0.748268 |  |
| T1 | blend70 | 1 | business2 | 149 | projection | category | id | wrong | no | 0.625502 |  |
| T1 | blend70 | 1 | business2 | 154 | surveyname | text | unknown | unknown | no | 0.475128 | probability_below_threshold |
| T1 | blend70 | 1 | business2 | 163 | projection | category | id | wrong | no | 0.593133 |  |
| T1 | blend70 | 1 | business2 | 177 | fine | amount | unknown | unknown | no | 0.334397 | probability_below_threshold |
| T1 | blend70 | 1 | business2 | 230 | warddesc | address | category | wrong | no | 0.663832 |  |
| T1 | blend70 | 1 | business2 | 238 | terrace | quantity | unknown | unknown | no | 0.389884 | probability_below_threshold |
| T1 | blend70 | 1 | business2 | 288 | construction_age_band | category | date | wrong | no | 0.510411 |  |
| T1 | blend70 | 1 | business2 | 298 | number_habitable_rooms | quantity | category | wrong | no | 0.531305 |  |
| T1 | blend70 | 1 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.704515 |  |
| T1 | blend70 | 1 | business2 | 301 | total_floor_area_known | category | quantity | wrong | no | 0.725338 |  |
| T1 | blend70 | 1 | business2 | 325 | loac_group | category | address | wrong | no | 0.646851 |  |
| T1 | blend70 | 1 | business2 | 326 | fuel_poverty | rate | unknown | unknown | no | 0.424465 | probability_below_threshold |
| T1 | blend70 | 1 | business2 | 370 | average bids per property | other | rate | other_ng | no | 0.633361 |  |
| T1 | blend70 | 1 | business2 | 379 | terrace | quantity | unknown | unknown | no | 0.411463 | probability_below_threshold |
| T1 | blend70 | 1 | business2 | 381 | total_verified_sales | quantity | amount | wrong | yes | 0.630932 |  |
| T1 | blend70 | 1 | business2 | 440 | situtation | address | category | wrong | no | 0.556441 |  |
| T1 | blend70 | 1 | business2 | 492 | value () | amount | unknown | unknown | no | 0.989984 | numeric_values_not_parseable |
| T1 | blend70 | 1 | business2 | 535 | scheme_description | category | unknown | unknown | no | 0.396762 | probability_below_threshold |
| T1 | blend70 | 1 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.983513 | numeric_values_not_parseable |
| T1 | blend70 | 1 | business2 | 562 | name | org | address | wrong | no | 0.786749 |  |
| T1 | blend70 | 1 | business2 | 581 | type of expenditure | account | category | wrong | no | 0.795459 |  |
| T1 | blend70 | 1 | business2 | 812 | value of payments € 000s 2008 | amount | unknown | unknown | no | 0.530439 | numeric_top2_too_close |
| T1 | blend70 | 1 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.990368 | date_value_evidence_low |
| T1 | blend70 | 1 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.991990 | date_value_evidence_low |
| T1 | blend70 | 1 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.991872 | date_value_evidence_low |
| T1 | blend70 | 1 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.990536 | date_value_evidence_low |
| T1 | blend70 | 1 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.990358 | date_value_evidence_low |
| T1 | blend70 | 1 | business2 | 946 | service_responsable | account | unknown | unknown | no | 0.492304 | probability_below_threshold |
| T1 | blend70 | 1 | business2 | 948 | numéro_uev | id | address | wrong | no | 0.764920 |  |
| T1 | blend70 | 1 | business2 | 957 | volume (10^3 m3) | quantity | unknown | unknown | no | 0.502896 | other_class |
| T1 | blend70 | 1 | business2 | 962 | service | account | unknown | unknown | no | 0.410859 | probability_below_threshold |
| T1 | blend70 | 1 | business2 | 971 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | unknown | no | 0.558823 | numeric_top2_too_close |
| T1 | blend70 | 1 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | unknown | no | 0.504999 | numeric_top2_too_close |
| T1 | blend70 | 1 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | wrong | yes | 0.675451 |  |
| T1 | blend70 | 1 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.977166 |  |
| T1 | blend70 | 1 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.811652 |  |
| T1 | blend70 | 1 | dev220 | 143 | terms | category | text | wrong | no | 0.838821 |  |
| T1 | blend70 | 1 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.977957 |  |
| T1 | blend70 | 1 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.955088 |  |
| T1 | blend70 | 1 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.909882 |  |
| T1 | blend70 | 1 | dev220 | 189 | payment terms | category | text | wrong | no | 0.618818 |  |
| T1 | blend70 | 1 | general | 27 | keyword | category | text | wrong | no | 0.949234 |  |
| T1 | blend70 | 1 | general | 32 | 五島 | other | quantity | other_ng | no | 0.927148 |  |
| T1 | blend70 | 1 | general | 35 | denominatorunweighted | quantity | unknown | unknown | no | 0.693896 | other_class |
| T1 | blend70 | 1 | general | 71 | property | category | unknown | unknown | no | 0.633826 | other_class |
| T1 | blend70 | 1 | general | 83 | place | org | address | wrong | no | 0.869120 |  |
| T1 | blend70 | 1 | general | 87 | sens_final | rate | unknown | unknown | no | 0.673643 | other_class |
| T1 | blend70 | 1 | general | 94 | 名称_カナ | org | address | wrong | no | 0.851093 |  |
| T1 | blend70 | 1 | general | 104 | term | text | category | wrong | no | 0.599679 |  |
| T1 | blend70 | 1 | general | 121 | dag-stage | other | category | other_ng | no | 0.663907 |  |
| T1 | blend70 | 1 | general | 134 | dbpedia_score | other | rate | other_ng | no | 0.670958 |  |
| T1 | blend70 | 1 | general | 207 | year_step_size | quantity | category | wrong | no | 0.621268 |  |
| T1 | blend70 | 1 | general | 224 | study | text | unknown | unknown | no | 0.291649 | probability_below_threshold |
| T1 | blend70 | 1 | general | 227 | 発生日 | date | unknown | unknown | no | 0.989953 | date_value_evidence_low |
| T1 | blend70 | 1 | general | 234 | 発生県 | id | unknown | unknown | no | 0.391097 | probability_below_threshold |
| T1 | blend70 | 1 | general | 275 | attrition | category | unknown | unknown | no | 0.489055 | probability_below_threshold |
| T1 | blend70 | 1 | general | 282 | 読み方 | address | text | wrong | no | 0.822697 |  |
| T1 | blend70 | 1 | general | 286 | value | other | rate | other_ng | no | 0.687482 |  |
| T1 | blend70 | 1 | general | 291 | cleaned | text | category | wrong | no | 0.765249 |  |
| T1 | blend70 | 1 | general | 296 | image_level_adj_acc | rate | unknown | unknown | no | 0.812006 | other_class |
| T1 | blend70 | 1 | general | 308 | ステーション名 | org | address | wrong | no | 0.695443 |  |
| T1 | blend70 | 1 | general | 309 | goal | id | category | wrong | no | 0.595057 |  |
| T1 | blend70 | 1 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.734522 | other_class |
| T1 | blend70 | 1 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.991173 | date_value_evidence_low |
| T1 | blend70 | 1 | general | 343 | mt2 | other | category | other_ng | no | 0.528974 |  |
| T1 | blend70 | 1 | general | 351 | operationid | other | id | other_ng | no | 0.619076 |  |
| T1 | blend70 | 1 | general | 370 | source_value | category | unknown | unknown | no | 0.497324 | probability_below_threshold |
| T1 | blend70 | 1 | general | 380 | 科名 | category | unknown | unknown | no | 0.896927 | other_class |
| T1 | blend70 | 2 | business | 41 | total invoices paid | quantity | unknown | unknown | no | 0.594298 | numeric_top2_too_close |
| T1 | blend70 | 2 | business | 46 | quarterno | date | unknown | unknown | no | 0.963047 | date_value_evidence_low |
| T1 | blend70 | 2 | business | 77 | publisher label | org | address | wrong | no | 0.538789 |  |
| T1 | blend70 | 2 | business | 148 | merchant details | text | unknown | unknown | no | 0.481765 | probability_below_threshold |
| T1 | blend70 | 2 | business | 278 | 目名 | category | unknown | unknown | no | 0.977555 | other_class |
| T1 | blend70 | 2 | business | 279 | 科名 | category | unknown | unknown | no | 0.962803 | other_class |
| T1 | blend70 | 2 | business | 344 | portefeuille_nom_et_code | org | account | wrong | no | 0.649938 |  |
| T1 | blend70 | 2 | business | 347 | regrp_sommaire | account | category | wrong | no | 0.719812 |  |
| T1 | blend70 | 2 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.768092 | date_value_evidence_low |
| T1 | blend70 | 2 | business | 450 | sub_category | category | account | wrong | no | 0.510778 |  |
| T1 | blend70 | 2 | business | 451 | title | category | account | wrong | no | 0.513956 |  |
| T1 | blend70 | 2 | business | 459 | australian sourced goods | amount | quantity | wrong | yes | 0.550784 |  |
| T1 | blend70 | 2 | business | 461 | overseas sourced goods | amount | unknown | unknown | no | 0.459811 | probability_below_threshold |
| T1 | blend70 | 2 | business | 462 | overseas sourced services | amount | unknown | unknown | no | 0.532120 | numeric_top2_too_close |
| T1 | blend70 | 2 | business2 | 13 | cost centre description | account | unknown | unknown | no | 0.493295 | probability_below_threshold |
| T1 | blend70 | 2 | business2 | 45 | type | account | category | wrong | no | 0.812670 |  |
| T1 | blend70 | 2 | business2 | 58 | numbers of | date | unknown | unknown | no | 0.404163 | probability_below_threshold |
| T1 | blend70 | 2 | business2 | 75 | monitor | id | category | wrong | no | 0.581750 |  |
| T1 | blend70 | 2 | business2 | 90 | total invoices paid | quantity | unknown | unknown | no | 0.593129 | numeric_top2_too_close |
| T1 | blend70 | 2 | business2 | 177 | fine | amount | unknown | unknown | no | 0.302224 | probability_below_threshold |
| T1 | blend70 | 2 | business2 | 230 | warddesc | address | category | wrong | no | 0.740980 |  |
| T1 | blend70 | 2 | business2 | 238 | terrace | quantity | unknown | unknown | no | 0.412039 | probability_below_threshold |
| T1 | blend70 | 2 | business2 | 298 | number_habitable_rooms | quantity | category | wrong | no | 0.594111 |  |
| T1 | blend70 | 2 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.676558 |  |
| T1 | blend70 | 2 | business2 | 301 | total_floor_area_known | category | unknown | unknown | no | 0.600392 | other_class |
| T1 | blend70 | 2 | business2 | 325 | loac_group | category | address | wrong | no | 0.555661 |  |
| T1 | blend70 | 2 | business2 | 326 | fuel_poverty | rate | unknown | unknown | no | 0.556824 | other_class |
| T1 | blend70 | 2 | business2 | 370 | average bids per property | other | rate | other_ng | no | 0.525923 |  |
| T1 | blend70 | 2 | business2 | 379 | terrace | quantity | unknown | unknown | no | 0.573461 | other_class |
| T1 | blend70 | 2 | business2 | 381 | total_verified_sales | quantity | unknown | unknown | no | 0.548899 | numeric_top2_too_close |
| T1 | blend70 | 2 | business2 | 440 | situtation | address | category | wrong | no | 0.608455 |  |
| T1 | blend70 | 2 | business2 | 492 | value () | amount | unknown | unknown | no | 0.989857 | numeric_values_not_parseable |
| T1 | blend70 | 2 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.979791 | numeric_values_not_parseable |
| T1 | blend70 | 2 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.990734 | date_value_evidence_low |
| T1 | blend70 | 2 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.988842 | date_value_evidence_low |
| T1 | blend70 | 2 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.988404 | date_value_evidence_low |
| T1 | blend70 | 2 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.989300 | date_value_evidence_low |
| T1 | blend70 | 2 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.990051 | date_value_evidence_low |
| T1 | blend70 | 2 | business2 | 948 | numéro_uev | id | address | wrong | no | 0.799459 |  |
| T1 | blend70 | 2 | business2 | 956 | terminal | address | unknown | unknown | no | 0.418699 | probability_below_threshold |
| T1 | blend70 | 2 | business2 | 958 | volume (mcf) | quantity | unknown | unknown | no | 0.667374 | other_class |
| T1 | blend70 | 2 | business2 | 962 | service | account | unknown | unknown | no | 0.320121 | probability_below_threshold |
| T1 | blend70 | 2 | business2 | 970 | return-on-investments_revenus-de-placements | amount | unknown | unknown | no | 0.526333 | numeric_top2_too_close |
| T1 | blend70 | 2 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | wrong | yes | 0.691408 |  |
| T1 | blend70 | 2 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | wrong | yes | 0.812484 |  |
| T1 | blend70 | 2 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.977001 |  |
| T1 | blend70 | 2 | dev220 | 21 | ポイント | amount | unknown | unknown | no | 0.463344 | probability_below_threshold |
| T1 | blend70 | 2 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.782702 |  |
| T1 | blend70 | 2 | dev220 | 130 | 随意契約理由 | text | category | wrong | no | 0.578220 |  |
| T1 | blend70 | 2 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.974104 |  |
| T1 | blend70 | 2 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.959930 |  |
| T1 | blend70 | 2 | dev220 | 173 | active | category | unknown | unknown | no | 0.494261 | probability_below_threshold |
| T1 | blend70 | 2 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.887836 |  |
| T1 | blend70 | 2 | general | 1 | author | person | org | wrong | no | 0.521491 |  |
| T1 | blend70 | 2 | general | 27 | keyword | category | text | wrong | no | 0.934123 |  |
| T1 | blend70 | 2 | general | 35 | denominatorunweighted | quantity | unknown | unknown | no | 0.467596 | probability_below_threshold |
| T1 | blend70 | 2 | general | 48 | source | category | org | wrong | no | 0.620281 |  |
| T1 | blend70 | 2 | general | 65 | app | category | unknown | unknown | no | 0.642806 | other_class |
| T1 | blend70 | 2 | general | 70 | lda | text | category | wrong | no | 0.512606 |  |
| T1 | blend70 | 2 | general | 71 | property | category | unknown | unknown | no | 0.369187 | probability_below_threshold |
| T1 | blend70 | 2 | general | 83 | place | org | address | wrong | no | 0.753874 |  |
| T1 | blend70 | 2 | general | 87 | sens_final | rate | unknown | unknown | no | 0.669377 | other_class |
| T1 | blend70 | 2 | general | 94 | 名称_カナ | org | address | wrong | no | 0.663991 |  |
| T1 | blend70 | 2 | general | 121 | dag-stage | other | category | other_ng | no | 0.728156 |  |
| T1 | blend70 | 2 | general | 207 | year_step_size | quantity | category | wrong | no | 0.559445 |  |
| T1 | blend70 | 2 | general | 227 | 発生日 | date | unknown | unknown | no | 0.988022 | date_value_evidence_low |
| T1 | blend70 | 2 | general | 234 | 発生県 | id | unknown | unknown | no | 0.318665 | probability_below_threshold |
| T1 | blend70 | 2 | general | 275 | attrition | category | quantity | wrong | no | 0.565086 |  |
| T1 | blend70 | 2 | general | 282 | 読み方 | address | unknown | unknown | no | 0.355689 | probability_below_threshold |
| T1 | blend70 | 2 | general | 286 | value | other | rate | other_ng | no | 0.934031 |  |
| T1 | blend70 | 2 | general | 291 | cleaned | text | category | wrong | no | 0.657887 |  |
| T1 | blend70 | 2 | general | 296 | image_level_adj_acc | rate | unknown | unknown | no | 0.800706 | other_class |
| T1 | blend70 | 2 | general | 308 | ステーション名 | org | address | wrong | no | 0.521529 |  |
| T1 | blend70 | 2 | general | 309 | goal | id | category | wrong | no | 0.612225 |  |
| T1 | blend70 | 2 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.736700 | other_class |
| T1 | blend70 | 2 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.988005 | date_value_evidence_low |
| T1 | blend70 | 2 | general | 351 | operationid | other | id | other_ng | no | 0.700590 |  |
| T1 | blend70 | 2 | general | 370 | source_value | category | unknown | unknown | no | 0.340557 | probability_below_threshold |
| T1 | blend70 | 2 | general | 377 | indicator | text | unknown | unknown | no | 0.499721 | probability_below_threshold |
| T1 | blend70 | 2 | general | 380 | 科名 | category | unknown | unknown | no | 0.973462 | other_class |
| T1 | blend70 | 2 | general | 382 | source | category | unknown | unknown | no | 0.428570 | probability_below_threshold |
| T1 | blend70 | 3 | business | 41 | total invoices paid | quantity | amount | wrong | yes | 0.911170 |  |
| T1 | blend70 | 3 | business | 46 | quarterno | date | unknown | unknown | no | 0.969769 | date_value_evidence_low |
| T1 | blend70 | 3 | business | 77 | publisher label | org | unknown | unknown | no | 0.415441 | probability_below_threshold |
| T1 | blend70 | 3 | business | 101 | entitiy | org | unknown | unknown | no | 0.379329 | probability_below_threshold |
| T1 | blend70 | 3 | business | 148 | merchant details | text | category | wrong | no | 0.591732 |  |
| T1 | blend70 | 3 | business | 237 | purposeofexpenditure | text | account | wrong | no | 0.829367 |  |
| T1 | blend70 | 3 | business | 278 | 目名 | category | unknown | unknown | no | 0.971203 | other_class |
| T1 | blend70 | 3 | business | 279 | 科名 | category | unknown | unknown | no | 0.943745 | other_class |
| T1 | blend70 | 3 | business | 342 | commodity-title_en | product | unknown | unknown | no | 0.485754 | probability_below_threshold |
| T1 | blend70 | 3 | business | 344 | portefeuille_nom_et_code | org | unknown | unknown | no | 0.353848 | probability_below_threshold |
| T1 | blend70 | 3 | business | 347 | regrp_sommaire | account | unknown | unknown | no | 0.318014 | probability_below_threshold |
| T1 | blend70 | 3 | business | 348 | regrp_nom | account | unknown | unknown | no | 0.483492 | probability_below_threshold |
| T1 | blend70 | 3 | business | 401 | ligne | category | id | wrong | no | 0.646884 |  |
| T1 | blend70 | 3 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.742558 | date_value_evidence_low |
| T1 | blend70 | 3 | business | 444 | grant in dollars | amount | unknown | unknown | no | 0.503590 | date_value_evidence_low |
| T1 | blend70 | 3 | business | 451 | title | category | account | wrong | no | 0.629170 |  |
| T1 | blend70 | 3 | business2 | 13 | cost centre description | account | org | wrong | no | 0.510526 |  |
| T1 | blend70 | 3 | business2 | 45 | type | account | category | wrong | no | 0.875328 |  |
| T1 | blend70 | 3 | business2 | 75 | monitor | id | category | wrong | no | 0.595624 |  |
| T1 | blend70 | 3 | business2 | 90 | total invoices paid | quantity | amount | wrong | yes | 0.911106 |  |
| T1 | blend70 | 3 | business2 | 149 | projection | category | id | wrong | no | 0.824560 |  |
| T1 | blend70 | 3 | business2 | 163 | projection | category | id | wrong | no | 0.835713 |  |
| T1 | blend70 | 3 | business2 | 177 | fine | amount | unknown | unknown | no | 0.451250 | probability_below_threshold |
| T1 | blend70 | 3 | business2 | 229 | post code sector | address | unknown | unknown | no | 0.484578 | probability_below_threshold |
| T1 | blend70 | 3 | business2 | 230 | warddesc | address | unknown | unknown | no | 0.390694 | probability_below_threshold |
| T1 | blend70 | 3 | business2 | 238 | terrace | quantity | unknown | unknown | no | 0.677055 | other_class |
| T1 | blend70 | 3 | business2 | 288 | construction_age_band | category | unknown | unknown | no | 0.473977 | probability_below_threshold |
| T1 | blend70 | 3 | business2 | 298 | number_habitable_rooms | quantity | unknown | unknown | no | 0.527108 | numeric_values_not_parseable |
| T1 | blend70 | 3 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.657370 |  |
| T1 | blend70 | 3 | business2 | 325 | loac_group | category | address | wrong | no | 0.621257 |  |
| T1 | blend70 | 3 | business2 | 326 | fuel_poverty | rate | unknown | unknown | no | 0.487859 | probability_below_threshold |
| T1 | blend70 | 3 | business2 | 370 | average bids per property | other | rate | other_ng | no | 0.560110 |  |
| T1 | blend70 | 3 | business2 | 379 | terrace | quantity | unknown | unknown | no | 0.655487 | other_class |
| T1 | blend70 | 3 | business2 | 381 | total_verified_sales | quantity | amount | wrong | yes | 0.658410 |  |
| T1 | blend70 | 3 | business2 | 440 | situtation | address | text | wrong | no | 0.528478 |  |
| T1 | blend70 | 3 | business2 | 492 | value () | amount | unknown | unknown | no | 0.990607 | numeric_values_not_parseable |
| T1 | blend70 | 3 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.983228 | numeric_values_not_parseable |
| T1 | blend70 | 3 | business2 | 562 | name | org | address | wrong | no | 0.598608 |  |
| T1 | blend70 | 3 | business2 | 581 | type of expenditure | account | category | wrong | no | 0.764110 |  |
| T1 | blend70 | 3 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.991764 | date_value_evidence_low |
| T1 | blend70 | 3 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.989768 | date_value_evidence_low |
| T1 | blend70 | 3 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.988945 | date_value_evidence_low |
| T1 | blend70 | 3 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.989929 | date_value_evidence_low |
| T1 | blend70 | 3 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.989980 | date_value_evidence_low |
| T1 | blend70 | 3 | business2 | 946 | service_responsable | account | category | wrong | no | 0.720130 |  |
| T1 | blend70 | 3 | business2 | 948 | numéro_uev | id | address | wrong | no | 0.726440 |  |
| T1 | blend70 | 3 | business2 | 957 | volume (10^3 m3) | quantity | unknown | unknown | no | 0.652463 | other_class |
| T1 | blend70 | 3 | business2 | 958 | volume (mcf) | quantity | unknown | unknown | no | 0.526563 | other_class |
| T1 | blend70 | 3 | business2 | 962 | service | account | org | wrong | no | 0.614995 |  |
| T1 | blend70 | 3 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | wrong | yes | 0.762804 |  |
| T1 | blend70 | 3 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | wrong | yes | 0.846264 |  |
| T1 | blend70 | 3 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.974943 |  |
| T1 | blend70 | 3 | dev220 | 116 | 履行場所 | address | id | wrong | no | 0.668046 |  |
| T1 | blend70 | 3 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.887777 |  |
| T1 | blend70 | 3 | dev220 | 151 | taxable | category | tax_class | wrong | no | 0.669907 |  |
| T1 | blend70 | 3 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.960718 |  |
| T1 | blend70 | 3 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.957089 |  |
| T1 | blend70 | 3 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.857531 |  |
| T1 | blend70 | 3 | dev220 | 196 | credit limit | amount | quantity | wrong | yes | 0.725401 |  |
| T1 | blend70 | 3 | dev220 | 201 | city | address | id | wrong | no | 0.689714 |  |
| T1 | blend70 | 3 | general | 27 | keyword | category | text | wrong | no | 0.965958 |  |
| T1 | blend70 | 3 | general | 32 | 五島 | other | quantity | other_ng | no | 0.958261 |  |
| T1 | blend70 | 3 | general | 35 | denominatorunweighted | quantity | unknown | unknown | no | 0.403731 | probability_below_threshold |
| T1 | blend70 | 3 | general | 48 | source | category | org | wrong | no | 0.651848 |  |
| T1 | blend70 | 3 | general | 65 | app | category | unknown | unknown | no | 0.625949 | other_class |
| T1 | blend70 | 3 | general | 71 | property | category | unknown | unknown | no | 0.679758 | other_class |
| T1 | blend70 | 3 | general | 83 | place | org | address | wrong | no | 0.806174 |  |
| T1 | blend70 | 3 | general | 87 | sens_final | rate | unknown | unknown | no | 0.675204 | other_class |
| T1 | blend70 | 3 | general | 94 | 名称_カナ | org | address | wrong | no | 0.717666 |  |
| T1 | blend70 | 3 | general | 104 | term | text | category | wrong | no | 0.688547 |  |
| T1 | blend70 | 3 | general | 112 | 住家全壊 | quantity | unknown | unknown | no | 0.579617 | other_class |
| T1 | blend70 | 3 | general | 121 | dag-stage | other | category | other_ng | no | 0.541539 |  |
| T1 | blend70 | 3 | general | 148 | mechanism | category | unknown | unknown | no | 0.479480 | probability_below_threshold |
| T1 | blend70 | 3 | general | 175 | bib | id | unknown | unknown | no | 0.382457 | probability_below_threshold |
| T1 | blend70 | 3 | general | 207 | year_step_size | quantity | category | wrong | no | 0.636038 |  |
| T1 | blend70 | 3 | general | 224 | study | text | person | wrong | no | 0.577814 |  |
| T1 | blend70 | 3 | general | 227 | 発生日 | date | unknown | unknown | no | 0.989314 | date_value_evidence_low |
| T1 | blend70 | 3 | general | 234 | 発生県 | id | unknown | unknown | no | 0.389376 | probability_below_threshold |
| T1 | blend70 | 3 | general | 282 | 読み方 | address | unknown | unknown | no | 0.441791 | probability_below_threshold |
| T1 | blend70 | 3 | general | 286 | value | other | rate | other_ng | no | 0.664761 |  |
| T1 | blend70 | 3 | general | 291 | cleaned | text | account | wrong | no | 0.537853 |  |
| T1 | blend70 | 3 | general | 296 | image_level_adj_acc | rate | unknown | unknown | no | 0.809804 | other_class |
| T1 | blend70 | 3 | general | 308 | ステーション名 | org | address | wrong | no | 0.675490 |  |
| T1 | blend70 | 3 | general | 309 | goal | id | category | wrong | no | 0.544673 |  |
| T1 | blend70 | 3 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.734083 | other_class |
| T1 | blend70 | 3 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.991498 | date_value_evidence_low |
| T1 | blend70 | 3 | general | 351 | operationid | other | id | other_ng | no | 0.677325 |  |
| T1 | blend70 | 3 | general | 360 | element_char | category | unknown | unknown | no | 0.498748 | probability_below_threshold |
| T1 | blend70 | 3 | general | 370 | source_value | category | unknown | unknown | no | 0.396090 | probability_below_threshold |
| T1 | blend70 | 3 | general | 377 | indicator | text | unknown | unknown | no | 0.496322 | probability_below_threshold |
| T1 | blend70 | 3 | general | 380 | 科名 | category | unknown | unknown | no | 0.950277 | other_class |
| T1 | ft | 1 | business | 41 | total invoices paid | quantity | amount | wrong | yes | 0.729639 |  |
| T1 | ft | 1 | business | 46 | quarterno | date | unknown | unknown | no | 0.987965 | date_value_evidence_low |
| T1 | ft | 1 | business | 77 | publisher label | org | address | wrong | no | 0.592744 |  |
| T1 | ft | 1 | business | 101 | entitiy | org | account | wrong | no | 0.742467 |  |
| T1 | ft | 1 | business | 148 | merchant details | text | category | wrong | no | 0.900811 |  |
| T1 | ft | 1 | business | 225 | description | account | text | wrong | no | 0.593077 |  |
| T1 | ft | 1 | business | 237 | purposeofexpenditure | text | account | wrong | no | 0.813150 |  |
| T1 | ft | 1 | business | 278 | 目名 | category | unknown | unknown | no | 0.888383 | other_class |
| T1 | ft | 1 | business | 279 | 科名 | category | unknown | unknown | no | 0.853713 | other_class |
| T1 | ft | 1 | business | 344 | portefeuille_nom_et_code | org | unknown | unknown | no | 0.445838 | probability_below_threshold |
| T1 | ft | 1 | business | 347 | regrp_sommaire | account | category | wrong | no | 0.514785 |  |
| T1 | ft | 1 | business | 401 | ligne | category | id | wrong | no | 0.570030 |  |
| T1 | ft | 1 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.974173 | date_value_evidence_low |
| T1 | ft | 1 | business | 421 | abn | id | unknown | unknown | no | 0.474756 | probability_below_threshold |
| T1 | ft | 1 | business | 451 | title | category | account | wrong | no | 0.746715 |  |
| T1 | ft | 1 | business | 459 | australian sourced goods | amount | quantity | wrong | yes | 0.851725 |  |
| T1 | ft | 1 | business | 461 | overseas sourced goods | amount | quantity | wrong | yes | 0.882692 |  |
| T1 | ft | 1 | business | 462 | overseas sourced services | amount | unknown | unknown | no | 0.584453 | numeric_top2_too_close |
| T1 | ft | 1 | business2 | 45 | type | account | category | wrong | no | 0.790465 |  |
| T1 | ft | 1 | business2 | 75 | monitor | id | category | wrong | no | 0.744215 |  |
| T1 | ft | 1 | business2 | 90 | total invoices paid | quantity | amount | wrong | yes | 0.641033 |  |
| T1 | ft | 1 | business2 | 149 | projection | category | unknown | unknown | no | 0.498231 | probability_below_threshold |
| T1 | ft | 1 | business2 | 151 | habitatdescription | text | unknown | unknown | no | 0.523775 | other_class |
| T1 | ft | 1 | business2 | 163 | projection | category | unknown | unknown | no | 0.487320 | probability_below_threshold |
| T1 | ft | 1 | business2 | 177 | fine | amount | unknown | unknown | no | 0.463758 | probability_below_threshold |
| T1 | ft | 1 | business2 | 230 | warddesc | address | category | wrong | no | 0.654542 |  |
| T1 | ft | 1 | business2 | 238 | terrace | quantity | address | wrong | no | 0.555822 |  |
| T1 | ft | 1 | business2 | 288 | construction_age_band | category | date | wrong | no | 0.718591 |  |
| T1 | ft | 1 | business2 | 298 | number_habitable_rooms | quantity | unknown | unknown | no | 0.648269 | numeric_values_not_parseable |
| T1 | ft | 1 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.973135 |  |
| T1 | ft | 1 | business2 | 301 | total_floor_area_known | category | quantity | wrong | no | 0.933288 |  |
| T1 | ft | 1 | business2 | 325 | loac_group | category | address | wrong | no | 0.924035 |  |
| T1 | ft | 1 | business2 | 326 | fuel_poverty | rate | category | wrong | no | 0.599467 |  |
| T1 | ft | 1 | business2 | 379 | terrace | quantity | address | wrong | no | 0.587534 |  |
| T1 | ft | 1 | business2 | 381 | total_verified_sales | quantity | amount | wrong | yes | 0.899896 |  |
| T1 | ft | 1 | business2 | 440 | situtation | address | text | wrong | no | 0.532207 |  |
| T1 | ft | 1 | business2 | 492 | value () | amount | unknown | unknown | no | 0.990362 | numeric_values_not_parseable |
| T1 | ft | 1 | business2 | 535 | scheme_description | category | account | wrong | no | 0.566325 |  |
| T1 | ft | 1 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.976949 | numeric_values_not_parseable |
| T1 | ft | 1 | business2 | 562 | name | org | address | wrong | no | 0.705174 |  |
| T1 | ft | 1 | business2 | 581 | type of expenditure | account | category | wrong | no | 0.839066 |  |
| T1 | ft | 1 | business2 | 812 | value of payments € 000s 2008 | amount | unknown | unknown | no | 0.601826 | numeric_top2_too_close |
| T1 | ft | 1 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.987376 | date_value_evidence_low |
| T1 | ft | 1 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.989120 | date_value_evidence_low |
| T1 | ft | 1 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.989000 | date_value_evidence_low |
| T1 | ft | 1 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.987102 | date_value_evidence_low |
| T1 | ft | 1 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.989542 | date_value_evidence_low |
| T1 | ft | 1 | business2 | 948 | numéro_uev | id | address | wrong | no | 0.834810 |  |
| T1 | ft | 1 | business2 | 957 | volume (10^3 m3) | quantity | unknown | unknown | no | 0.633332 | other_class |
| T1 | ft | 1 | business2 | 962 | service | account | unknown | unknown | no | 0.440160 | probability_below_threshold |
| T1 | ft | 1 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | unknown | no | 0.503465 | numeric_top2_too_close |
| T1 | ft | 1 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | unknown | no | 0.603580 | numeric_top2_too_close |
| T1 | ft | 1 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.987830 |  |
| T1 | ft | 1 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.845346 |  |
| T1 | ft | 1 | dev220 | 143 | terms | category | text | wrong | no | 0.906257 |  |
| T1 | ft | 1 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.972406 |  |
| T1 | ft | 1 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.972961 |  |
| T1 | ft | 1 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.972411 |  |
| T1 | ft | 1 | dev220 | 189 | payment terms | category | text | wrong | no | 0.825091 |  |
| T1 | ft | 1 | dev220 | 194 | payment terms | category | text | wrong | no | 0.510331 |  |
| T1 | ft | 1 | general | 27 | keyword | category | text | wrong | no | 0.946844 |  |
| T1 | ft | 1 | general | 32 | 五島 | other | quantity | other_ng | no | 0.897323 |  |
| T1 | ft | 1 | general | 35 | denominatorunweighted | quantity | unknown | unknown | no | 0.955399 | other_class |
| T1 | ft | 1 | general | 47 | mood | other | category | other_ng | no | 0.530133 |  |
| T1 | ft | 1 | general | 71 | property | category | unknown | unknown | no | 0.905125 | other_class |
| T1 | ft | 1 | general | 83 | place | org | address | wrong | no | 0.825790 |  |
| T1 | ft | 1 | general | 87 | sens_final | rate | unknown | unknown | no | 0.960665 | other_class |
| T1 | ft | 1 | general | 94 | 名称_カナ | org | address | wrong | no | 0.851627 |  |
| T1 | ft | 1 | general | 104 | term | text | category | wrong | no | 0.851588 |  |
| T1 | ft | 1 | general | 121 | dag-stage | other | category | other_ng | no | 0.828982 |  |
| T1 | ft | 1 | general | 134 | dbpedia_score | other | rate | other_ng | no | 0.660782 |  |
| T1 | ft | 1 | general | 207 | year_step_size | quantity | category | wrong | no | 0.786493 |  |
| T1 | ft | 1 | general | 224 | study | text | unknown | unknown | no | 0.405992 | probability_below_threshold |
| T1 | ft | 1 | general | 227 | 発生日 | date | unknown | unknown | no | 0.991368 | date_value_evidence_low |
| T1 | ft | 1 | general | 282 | 読み方 | address | text | wrong | no | 0.768958 |  |
| T1 | ft | 1 | general | 286 | value | other | rate | other_ng | no | 0.591909 |  |
| T1 | ft | 1 | general | 291 | cleaned | text | category | wrong | no | 0.674827 |  |
| T1 | ft | 1 | general | 296 | image_level_adj_acc | rate | unknown | unknown | no | 0.968939 | other_class |
| T1 | ft | 1 | general | 308 | ステーション名 | org | address | wrong | no | 0.734486 |  |
| T1 | ft | 1 | general | 309 | goal | id | unknown | unknown | no | 0.455722 | probability_below_threshold |
| T1 | ft | 1 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.985063 | other_class |
| T1 | ft | 1 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.987390 | date_value_evidence_low |
| T1 | ft | 1 | general | 343 | mt2 | other | category | other_ng | no | 0.752169 |  |
| T1 | ft | 1 | general | 351 | operationid | other | id | other_ng | no | 0.794740 |  |
| T1 | ft | 1 | general | 370 | source_value | category | text | wrong | no | 0.703726 |  |
| T1 | ft | 1 | general | 380 | 科名 | category | unknown | unknown | no | 0.860257 | other_class |
| T1 | ft | 2 | business | 46 | quarterno | date | unknown | unknown | no | 0.975884 | date_value_evidence_low |
| T1 | ft | 2 | business | 77 | publisher label | org | address | wrong | no | 0.730188 |  |
| T1 | ft | 2 | business | 148 | merchant details | text | unknown | unknown | no | 0.472438 | probability_below_threshold |
| T1 | ft | 2 | business | 278 | 目名 | category | unknown | unknown | no | 0.975903 | other_class |
| T1 | ft | 2 | business | 279 | 科名 | category | unknown | unknown | no | 0.970016 | other_class |
| T1 | ft | 2 | business | 344 | portefeuille_nom_et_code | org | account | wrong | no | 0.622421 |  |
| T1 | ft | 2 | business | 347 | regrp_sommaire | account | category | wrong | no | 0.943121 |  |
| T1 | ft | 2 | business | 401 | ligne | category | unknown | unknown | no | 0.497555 | probability_below_threshold |
| T1 | ft | 2 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.983542 | date_value_evidence_low |
| T1 | ft | 2 | business | 450 | sub_category | category | account | wrong | no | 0.619470 |  |
| T1 | ft | 2 | business | 451 | title | category | account | wrong | no | 0.716744 |  |
| T1 | ft | 2 | business | 459 | australian sourced goods | amount | quantity | wrong | yes | 0.785566 |  |
| T1 | ft | 2 | business | 461 | overseas sourced goods | amount | quantity | wrong | yes | 0.655858 |  |
| T1 | ft | 2 | business2 | 13 | cost centre description | account | org | wrong | no | 0.545104 |  |
| T1 | ft | 2 | business2 | 45 | type | account | category | wrong | no | 0.737115 |  |
| T1 | ft | 2 | business2 | 58 | numbers of | date | unknown | unknown | no | 0.575655 | numeric_top2_too_close |
| T1 | ft | 2 | business2 | 75 | monitor | id | category | wrong | no | 0.775806 |  |
| T1 | ft | 2 | business2 | 177 | fine | amount | unknown | unknown | no | 0.423851 | probability_below_threshold |
| T1 | ft | 2 | business2 | 230 | warddesc | address | category | wrong | no | 0.764754 |  |
| T1 | ft | 2 | business2 | 238 | terrace | quantity | address | wrong | no | 0.587473 |  |
| T1 | ft | 2 | business2 | 298 | number_habitable_rooms | quantity | unknown | unknown | no | 0.549069 | numeric_values_not_parseable |
| T1 | ft | 2 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.933196 |  |
| T1 | ft | 2 | business2 | 301 | total_floor_area_known | category | unknown | unknown | no | 0.734379 | other_class |
| T1 | ft | 2 | business2 | 325 | loac_group | category | address | wrong | no | 0.793764 |  |
| T1 | ft | 2 | business2 | 326 | fuel_poverty | rate | unknown | unknown | no | 0.780412 | other_class |
| T1 | ft | 2 | business2 | 330 | conservation_area_site_id | category | id | wrong | no | 0.545244 |  |
| T1 | ft | 2 | business2 | 379 | terrace | quantity | unknown | unknown | no | 0.803912 | other_class |
| T1 | ft | 2 | business2 | 381 | total_verified_sales | quantity | amount | wrong | yes | 0.626480 |  |
| T1 | ft | 2 | business2 | 440 | situtation | address | category | wrong | no | 0.516815 |  |
| T1 | ft | 2 | business2 | 492 | value () | amount | unknown | unknown | no | 0.990181 | numeric_values_not_parseable |
| T1 | ft | 2 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.971632 | numeric_values_not_parseable |
| T1 | ft | 2 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.987899 | date_value_evidence_low |
| T1 | ft | 2 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.984623 | date_value_evidence_low |
| T1 | ft | 2 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.984046 | date_value_evidence_low |
| T1 | ft | 2 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.985336 | date_value_evidence_low |
| T1 | ft | 2 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.989104 | date_value_evidence_low |
| T1 | ft | 2 | business2 | 948 | numéro_uev | id | address | wrong | no | 0.884152 |  |
| T1 | ft | 2 | business2 | 958 | volume (mcf) | quantity | unknown | unknown | no | 0.835420 | other_class |
| T1 | ft | 2 | business2 | 962 | service | account | unknown | unknown | no | 0.455813 | probability_below_threshold |
| T1 | ft | 2 | business2 | 970 | return-on-investments_revenus-de-placements | amount | unknown | unknown | no | 0.528944 | numeric_top2_too_close |
| T1 | ft | 2 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | wrong | yes | 0.799582 |  |
| T1 | ft | 2 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | wrong | yes | 0.799342 |  |
| T1 | ft | 2 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.987594 |  |
| T1 | ft | 2 | dev220 | 21 | ポイント | amount | unknown | unknown | no | 0.477545 | probability_below_threshold |
| T1 | ft | 2 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.803988 |  |
| T1 | ft | 2 | dev220 | 130 | 随意契約理由 | text | category | wrong | no | 0.819166 |  |
| T1 | ft | 2 | dev220 | 146 | description | text | category | wrong | no | 0.679199 |  |
| T1 | ft | 2 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.966902 |  |
| T1 | ft | 2 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.979878 |  |
| T1 | ft | 2 | dev220 | 173 | active | category | text | wrong | no | 0.687134 |  |
| T1 | ft | 2 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.940918 |  |
| T1 | ft | 2 | general | 27 | keyword | category | text | wrong | no | 0.925257 |  |
| T1 | ft | 2 | general | 35 | denominatorunweighted | quantity | id | wrong | yes | 0.666169 |  |
| T1 | ft | 2 | general | 48 | source | category | org | wrong | no | 0.865085 |  |
| T1 | ft | 2 | general | 65 | app | category | unknown | unknown | no | 0.916420 | other_class |
| T1 | ft | 2 | general | 70 | lda | text | category | wrong | no | 0.540231 |  |
| T1 | ft | 2 | general | 71 | property | category | unknown | unknown | no | 0.527069 | other_class |
| T1 | ft | 2 | general | 83 | place | org | address | wrong | no | 0.661152 |  |
| T1 | ft | 2 | general | 87 | sens_final | rate | unknown | unknown | no | 0.954571 | other_class |
| T1 | ft | 2 | general | 94 | 名称_カナ | org | address | wrong | no | 0.584339 |  |
| T1 | ft | 2 | general | 121 | dag-stage | other | category | other_ng | no | 0.920766 |  |
| T1 | ft | 2 | general | 207 | year_step_size | quantity | category | wrong | no | 0.698174 |  |
| T1 | ft | 2 | general | 227 | 発生日 | date | unknown | unknown | no | 0.988610 | date_value_evidence_low |
| T1 | ft | 2 | general | 234 | 発生県 | id | unknown | unknown | no | 0.454554 | probability_below_threshold |
| T1 | ft | 2 | general | 282 | 読み方 | address | org | wrong | no | 0.501195 |  |
| T1 | ft | 2 | general | 286 | value | other | rate | other_ng | no | 0.944121 |  |
| T1 | ft | 2 | general | 291 | cleaned | text | category | wrong | no | 0.521454 |  |
| T1 | ft | 2 | general | 296 | image_level_adj_acc | rate | unknown | unknown | no | 0.952798 | other_class |
| T1 | ft | 2 | general | 309 | goal | id | unknown | unknown | no | 0.480249 | probability_below_threshold |
| T1 | ft | 2 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.988174 | other_class |
| T1 | ft | 2 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.982864 | date_value_evidence_low |
| T1 | ft | 2 | general | 351 | operationid | other | id | other_ng | no | 0.911189 |  |
| T1 | ft | 2 | general | 370 | source_value | category | unknown | unknown | no | 0.352065 | probability_below_threshold |
| T1 | ft | 2 | general | 377 | indicator | text | category | wrong | no | 0.691583 |  |
| T1 | ft | 2 | general | 380 | 科名 | category | unknown | unknown | no | 0.969592 | other_class |
| T1 | ft | 2 | general | 382 | source | category | text | wrong | no | 0.559637 |  |
| T1 | ft | 3 | business | 41 | total invoices paid | quantity | amount | wrong | yes | 0.873750 |  |
| T1 | ft | 3 | business | 46 | quarterno | date | unknown | unknown | no | 0.985487 | date_value_evidence_low |
| T1 | ft | 3 | business | 77 | publisher label | org | address | wrong | no | 0.553976 |  |
| T1 | ft | 3 | business | 101 | entitiy | org | account | wrong | no | 0.541897 |  |
| T1 | ft | 3 | business | 148 | merchant details | text | category | wrong | no | 0.629533 |  |
| T1 | ft | 3 | business | 237 | purposeofexpenditure | text | account | wrong | no | 0.786804 |  |
| T1 | ft | 3 | business | 278 | 目名 | category | unknown | unknown | no | 0.966828 | other_class |
| T1 | ft | 3 | business | 279 | 科名 | category | unknown | unknown | no | 0.942789 | other_class |
| T1 | ft | 3 | business | 344 | portefeuille_nom_et_code | org | unknown | unknown | no | 0.414016 | probability_below_threshold |
| T1 | ft | 3 | business | 347 | regrp_sommaire | account | unknown | unknown | no | 0.369124 | probability_below_threshold |
| T1 | ft | 3 | business | 401 | ligne | category | id | wrong | no | 0.906949 |  |
| T1 | ft | 3 | business | 406 | mois calendrier | date | unknown | unknown | no | 0.947066 | date_value_evidence_low |
| T1 | ft | 3 | business | 444 | grant in dollars | amount | unknown | unknown | no | 0.709443 | date_value_evidence_low |
| T1 | ft | 3 | business | 451 | title | category | account | wrong | no | 0.881336 |  |
| T1 | ft | 3 | business2 | 13 | cost centre description | account | org | wrong | no | 0.725074 |  |
| T1 | ft | 3 | business2 | 45 | type | account | category | wrong | no | 0.826627 |  |
| T1 | ft | 3 | business2 | 75 | monitor | id | category | wrong | no | 0.795626 |  |
| T1 | ft | 3 | business2 | 90 | total invoices paid | quantity | amount | wrong | yes | 0.873659 |  |
| T1 | ft | 3 | business2 | 149 | projection | category | id | wrong | no | 0.782600 |  |
| T1 | ft | 3 | business2 | 163 | projection | category | id | wrong | no | 0.833864 |  |
| T1 | ft | 3 | business2 | 177 | fine | amount | unknown | unknown | no | 0.491957 | probability_below_threshold |
| T1 | ft | 3 | business2 | 238 | terrace | quantity | unknown | unknown | no | 0.911866 | other_class |
| T1 | ft | 3 | business2 | 298 | number_habitable_rooms | quantity | unknown | unknown | no | 0.749598 | numeric_values_not_parseable |
| T1 | ft | 3 | business2 | 299 | number_habitable_rooms_known | category | quantity | wrong | no | 0.905784 |  |
| T1 | ft | 3 | business2 | 323 | imd19_income_decile | category | unknown | unknown | no | 0.438338 | probability_below_threshold |
| T1 | ft | 3 | business2 | 325 | loac_group | category | address | wrong | no | 0.887472 |  |
| T1 | ft | 3 | business2 | 326 | fuel_poverty | rate | unknown | unknown | no | 0.681889 | other_class |
| T1 | ft | 3 | business2 | 330 | conservation_area_site_id | category | id | wrong | no | 0.531352 |  |
| T1 | ft | 3 | business2 | 379 | terrace | quantity | unknown | unknown | no | 0.921092 | other_class |
| T1 | ft | 3 | business2 | 381 | total_verified_sales | quantity | amount | wrong | yes | 0.939150 |  |
| T1 | ft | 3 | business2 | 440 | situtation | address | text | wrong | no | 0.725007 |  |
| T1 | ft | 3 | business2 | 492 | value () | amount | unknown | unknown | no | 0.991252 | numeric_values_not_parseable |
| T1 | ft | 3 | business2 | 542 | percentage (%) of the total amount paid | rate | unknown | unknown | no | 0.976541 | numeric_values_not_parseable |
| T1 | ft | 3 | business2 | 581 | type of expenditure | account | category | wrong | no | 0.794283 |  |
| T1 | ft | 3 | business2 | 825 | tlist(q1) | date | unknown | unknown | no | 0.989371 | date_value_evidence_low |
| T1 | ft | 3 | business2 | 864 | tlist(q1) | date | unknown | unknown | no | 0.985946 | date_value_evidence_low |
| T1 | ft | 3 | business2 | 874 | tlist(q1) | date | unknown | unknown | no | 0.984818 | date_value_evidence_low |
| T1 | ft | 3 | business2 | 883 | tlist(q1) | date | unknown | unknown | no | 0.986235 | date_value_evidence_low |
| T1 | ft | 3 | business2 | 926 | tlist(q1) | date | unknown | unknown | no | 0.989002 | date_value_evidence_low |
| T1 | ft | 3 | business2 | 946 | service_responsable | account | category | wrong | no | 0.628008 |  |
| T1 | ft | 3 | business2 | 948 | numéro_uev | id | address | wrong | no | 0.779839 |  |
| T1 | ft | 3 | business2 | 957 | volume (10^3 m3) | quantity | unknown | unknown | no | 0.846999 | other_class |
| T1 | ft | 3 | business2 | 958 | volume (mcf) | quantity | unknown | unknown | no | 0.634262 | other_class |
| T1 | ft | 3 | business2 | 962 | service | account | org | wrong | no | 0.877062 |  |
| T1 | ft | 3 | business2 | 972 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | wrong | yes | 0.901576 |  |
| T1 | ft | 3 | business2 | 973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | wrong | yes | 0.847600 |  |
| T1 | ft | 3 | business2 | 974 | miscellaneous_divers | amount | quantity | wrong | yes | 0.984653 |  |
| T1 | ft | 3 | dev220 | 116 | 履行場所 | address | id | wrong | no | 0.946551 |  |
| T1 | ft | 3 | dev220 | 128 | 担当課 | org | account | wrong | no | 0.954095 |  |
| T1 | ft | 3 | dev220 | 130 | 随意契約理由 | text | category | wrong | no | 0.540912 |  |
| T1 | ft | 3 | dev220 | 144 | location | org | address | wrong | no | 0.635134 |  |
| T1 | ft | 3 | dev220 | 151 | taxable | category | tax_class | wrong | no | 0.555688 |  |
| T1 | ft | 3 | dev220 | 171 | customer rank | quantity | category | wrong | no | 0.947780 |  |
| T1 | ft | 3 | dev220 | 172 | supplier rank | quantity | category | wrong | no | 0.975820 |  |
| T1 | ft | 3 | dev220 | 177 | purchase order by customer | id | quantity | wrong | yes | 0.897624 |  |
| T1 | ft | 3 | dev220 | 196 | credit limit | amount | quantity | wrong | yes | 0.812288 |  |
| T1 | ft | 3 | dev220 | 201 | city | address | id | wrong | no | 0.963574 |  |
| T1 | ft | 3 | general | 27 | keyword | category | text | wrong | no | 0.970736 |  |
| T1 | ft | 3 | general | 32 | 五島 | other | quantity | other_ng | no | 0.941770 |  |
| T1 | ft | 3 | general | 35 | denominatorunweighted | quantity | id | wrong | yes | 0.574933 |  |
| T1 | ft | 3 | general | 47 | mood | other | category | other_ng | no | 0.558553 |  |
| T1 | ft | 3 | general | 48 | source | category | org | wrong | no | 0.910180 |  |
| T1 | ft | 3 | general | 65 | app | category | unknown | unknown | no | 0.892338 | other_class |
| T1 | ft | 3 | general | 71 | property | category | unknown | unknown | no | 0.970742 | other_class |
| T1 | ft | 3 | general | 83 | place | org | address | wrong | no | 0.735866 |  |
| T1 | ft | 3 | general | 87 | sens_final | rate | unknown | unknown | no | 0.962894 | other_class |
| T1 | ft | 3 | general | 94 | 名称_カナ | org | address | wrong | no | 0.661017 |  |
| T1 | ft | 3 | general | 104 | term | text | category | wrong | no | 0.978541 |  |
| T1 | ft | 3 | general | 112 | 住家全壊 | quantity | unknown | unknown | no | 0.826835 | other_class |
| T1 | ft | 3 | general | 121 | dag-stage | other | category | other_ng | no | 0.654170 |  |
| T1 | ft | 3 | general | 148 | mechanism | category | id | wrong | no | 0.551404 |  |
| T1 | ft | 3 | general | 175 | bib | id | unknown | unknown | no | 0.357020 | probability_below_threshold |
| T1 | ft | 3 | general | 207 | year_step_size | quantity | category | wrong | no | 0.807593 |  |
| T1 | ft | 3 | general | 224 | study | text | person | wrong | no | 0.821247 |  |
| T1 | ft | 3 | general | 227 | 発生日 | date | unknown | unknown | no | 0.990456 | date_value_evidence_low |
| T1 | ft | 3 | general | 282 | 読み方 | address | category | wrong | no | 0.565547 |  |
| T1 | ft | 3 | general | 286 | value | other | rate | other_ng | no | 0.559449 |  |
| T1 | ft | 3 | general | 291 | cleaned | text | account | wrong | no | 0.767751 |  |
| T1 | ft | 3 | general | 296 | image_level_adj_acc | rate | unknown | unknown | no | 0.965795 | other_class |
| T1 | ft | 3 | general | 308 | ステーション名 | org | address | wrong | no | 0.705982 |  |
| T1 | ft | 3 | general | 309 | goal | id | quantity | wrong | yes | 0.566314 |  |
| T1 | ft | 3 | general | 338 | denominatorweighted | quantity | unknown | unknown | no | 0.984436 | other_class |
| T1 | ft | 3 | general | 340 | 登録年月日 | date | unknown | unknown | no | 0.987854 | date_value_evidence_low |
| T1 | ft | 3 | general | 343 | mt2 | other | category | other_ng | no | 0.681908 |  |
| T1 | ft | 3 | general | 351 | operationid | other | id | other_ng | no | 0.877953 |  |
| T1 | ft | 3 | general | 360 | element_char | category | unknown | unknown | no | 0.461700 | probability_below_threshold |
| T1 | ft | 3 | general | 370 | source_value | category | product | wrong | no | 0.565832 |  |
| T1 | ft | 3 | general | 377 | indicator | text | category | wrong | no | 0.685524 |  |
| T1 | ft | 3 | general | 380 | 科名 | category | unknown | unknown | no | 0.936471 | other_class |