# run 40202377192 C2：固定5集合の全件誤り監査

作成: 2026-10-26 ChatGPT。対象は許可された dev220 / general / business / business2 / japan_procurement の FT 出力だけ。blind_set*、セット3・5・7は未使用。

## 集計（rawファイルから再計算）

| job | seed | 除外陣 | 集合 | 列数 | 正解率 | 誤り | unknown | 重大 | 学習秒 | peak GPU GiB |
|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | - | dev220 | 220 | 96.8% | 5 | 2 | 1 | 1563.4 | 5.46 |
| 1 | 1 | - | general | 383 | 94.0% | 14 | 9 | 1 | 1563.4 | 5.46 |
| 1 | 1 | - | business | 490 | 96.5% | 11 | 6 | 0 | 1563.4 | 5.46 |
| 1 | 1 | - | business2 | 976 | 96.5% | 21 | 13 | 4 | 1563.4 | 5.46 |
| 1 | 1 | - | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1563.4 | 5.46 |
| 2 | 2 | - | dev220 | 220 | 96.4% | 6 | 2 | 3 | 1553.3 | 5.54 |
| 2 | 2 | - | general | 383 | 92.4% | 20 | 9 | 1 | 1553.3 | 5.54 |
| 2 | 2 | - | business | 490 | 95.5% | 16 | 6 | 1 | 1553.3 | 5.54 |
| 2 | 2 | - | business2 | 976 | 96.4% | 19 | 16 | 3 | 1553.3 | 5.54 |
| 2 | 2 | - | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1553.3 | 5.54 |
| 3 | 3 | - | dev220 | 220 | 97.3% | 5 | 1 | 1 | 1556.0 | 5.55 |
| 3 | 3 | - | general | 383 | 91.4% | 19 | 14 | 1 | 1556.0 | 5.55 |
| 3 | 3 | - | business | 490 | 95.5% | 14 | 8 | 0 | 1556.0 | 5.55 |
| 3 | 3 | - | business2 | 976 | 96.4% | 19 | 16 | 3 | 1556.0 | 5.55 |
| 3 | 3 | - | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1556.0 | 5.55 |

| 集合 | 平均正解率 | 平均誤り | 平均unknown | 平均重大 |
|---|---:|---:|---:|---:|
| dev220 | 96.8% | 5.3 | 1.7 | 1.7 |
| general | 92.6% | 17.7 | 10.7 | 1.0 |
| business | 95.9% | 13.7 | 6.7 | 0.3 |
| business2 | 96.4% | 19.7 | 15.0 | 3.3 |
| japan_procurement | 100.0% | 0.0 | 0.0 | 0.0 |

問題出力 271 件、固有ケース 125 件。2 job以上で再発 89 件、全3 jobで再発 57 件。

## 観測事実と原因仮説
- 観測: raw誤り＋見送り 58件。
- 観測: rawモデル誤分類 169件。
- 観測: guardが正解rawを変更 44件。
- 高確度: rawが正解でguard後だけ不正解のケースは後段規則が直接原因。
- 中確度仮説: 正解がtop2/top3に残るraw誤分類は、ラベル境界・確信度較正・文脈不足の影響が候補。
- 低〜中確度仮説: 正解がtop3外のケースは教材分布差、定義未学習、入力切り詰め、出典差が候補。個別根因は元表・UNIT・兄弟列・行別token情報との照合前なので断定しない。
- ラベルは変更していない。疑義は先生2人の独立確認と根拠裁定が必要。

## 優先対策
1. raw正解を変更したguardケースを理由別に再検証する。正解回復が期待できるが、重大誤り再流入の副作用がある。
2. 全jobで再発する重大・誤りを元表タイトル、UNIT、兄弟列、token切り詰めと照合する。根因特定が期待できるが監査工数が増える。
3. 評価行を流用せず、教材側の類似失敗だけをhard negative候補にする。変更は一要因ずつ再試験する。

## 全問題一覧

| job | 集合#index | 列名 | 正解 | raw→最終 | outcome | 重大 | 正解rank | top1確率 | reason | 観測 | 仮説 |
|---:|---|---|---|---|---|---:|---:|---:|---|---|---|
| 1 | dev220#75 | 支払を受ける者の個人番号 | id | other→unknown | unknown | no | 2 | 0.608 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | dev220#128 | 担当課 | org | account→account | wrong | no | 2 | 0.711 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.755 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | dev220#170 | tax id | id | other→unknown | unknown | no | 2 | 0.725 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | dev220#171 | customer rank | quantity | category→category | wrong | no | >3 | 0.954 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | dev220#172 | supplier rank | quantity | category→category | wrong | no | >3 | 0.977 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 3 | 0.973 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.801 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 2 | 0.734 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | >3 | 0.885 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | general#71 | property | category | other→unknown | unknown | no | 3 | 0.604 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.949 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#83 | place | org | address→address | wrong | no | 2 | 0.811 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.960 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#121 | dag-stage | other | category→category | other_ng | no | 2 | 0.510 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#134 | dbpedia_score | other | rate→rate | other_ng | no | 2 | 0.886 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#207 | year_step_size | quantity | category→category | wrong | no | 2 | 0.817 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.983 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | general#282 | 読み方 | address | org→org | wrong | no | 2 | 0.583 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#286 | value | other | rate→rate | other_ng | no | 2 | 0.961 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#291 | cleaned | text | account→account | wrong | no | 2 | 0.827 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.975 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.596 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#309 | goal | id | quantity→quantity | wrong | yes | >3 | 0.701 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 3 | 0.988 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.982 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | general#370 | source_value | category | text→unknown | unknown | no | 3 | 0.433 | probability_below_threshold | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.618 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.945 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#382 | source | category | text→text | wrong | no | 2 | 0.774 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.983 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business#77 | publisher label | org | address→address | wrong | no | 2 | 0.619 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#84 | department | org | account→account | wrong | no | 2 | 0.976 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#92 | department | org | account→account | wrong | no | 2 | 0.823 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#101 | entitiy | org | category→category | wrong | no | 3 | 0.567 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business#148 | merchant details | text | category→category | wrong | no | 3 | 0.968 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business#199 | department | org | account→account | wrong | no | 2 | 0.983 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#215 | account_name | account | org→org | wrong | no | 2 | 0.675 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.979 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.928 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.945 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business#303 | d1 | category | quantity→quantity | wrong | no | 2 | 0.695 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#347 | regrp_sommaire | account | category→category | wrong | no | 2 | 0.685 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#401 | ligne | category | id→id | wrong | no | 2 | 0.984 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#404 | type de matériel | category | category→unknown | unknown | no | 1 | 0.453 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.981 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business#451 | title | category | account→unknown | unknown | no | 3 | 0.326 | probability_below_threshold | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business2#45 | type | account | category→category | wrong | no | 2 | 0.973 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#75 | monitor | id | category→category | wrong | no | 2 | 0.798 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#149 | projection | category | id→id | wrong | no | 2 | 0.675 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#163 | projection | category | id→id | wrong | no | 2 | 0.735 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#177 | fine | amount | rate→rate | wrong | yes | >3 | 0.634 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | business2#230 | warddesc | address | category→category | wrong | no | 2 | 0.567 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#238 | terrace | quantity | other→unknown | unknown | no | 3 | 0.930 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business2#288 | construction_age_band | category | date→date | wrong | no | 2 | 0.736 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#291 | epc_score_known | category | other→unknown | unknown | no | 2 | 0.639 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business2#295 | potential_epc_score_known | category | category→unknown | unknown | no | 1 | 0.447 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#298 | number_habitable_rooms | quantity | category→category | wrong | no | 2 | 0.887 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.862 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#301 | total_floor_area_known | category | other→unknown | unknown | no | 3 | 0.672 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business2#317 | energy_consumption | other | quantity→quantity | other_ng | no | 2 | 0.823 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#325 | loac_group | category | address→address | wrong | no | 2 | 0.923 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#326 | fuel_poverty | rate | other→unknown | unknown | no | 2 | 0.870 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business2#356 | want to live in this parish only | quantity | category→category | wrong | no | 2 | 0.690 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#370 | average bids per property | other | amount→amount | other_ng | no | 3 | 0.666 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business2#379 | terrace | quantity | other→unknown | unknown | no | 3 | 0.913 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business2#381 | total_verified_sales | quantity | amount→amount | wrong | yes | 2 | 0.912 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#440 | situtation | address | text→text | wrong | no | 3 | 0.850 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.989 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.974 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#548 | health service executive area | address | org→org | wrong | no | 2 | 0.537 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#563 | bike_stands | quantity | category→category | wrong | no | 2 | 0.655 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.984 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.983 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.983 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.983 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.984 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.859 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#962 | service | account | org→org | wrong | no | >3 | 0.647 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | business2#973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity→quantity | wrong | yes | 2 | 0.839 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.992 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#17 | 商品計 | amount | quantity→quantity | wrong | yes | 2 | 0.662 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#49 | 税率 | rate | tax_class→tax_class | wrong | no | 2 | 0.717 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#75 | 支払を受ける者の個人番号 | id | id→unknown | unknown | no | 1 | 0.478 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | dev220#116 | 履行場所 | address | address→unknown | unknown | no | 1 | 0.499 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | dev220#171 | customer rank | quantity | category→category | wrong | no | 3 | 0.935 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | dev220#172 | supplier rank | quantity | category→category | wrong | no | 3 | 0.978 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 2 | 0.947 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#196 | credit limit | amount | quantity→quantity | wrong | yes | 2 | 0.786 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#1 | author | person | org→org | wrong | no | 2 | 0.875 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.940 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 2 | 0.973 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#35 | denominatorunweighted | quantity | id→id | wrong | yes | 3 | 0.740 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | general#47 | mood | other | category→category | other_ng | no | 2 | 0.818 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#48 | source | category | org→org | wrong | no | 2 | 0.841 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#70 | lda | text | category→category | wrong | no | 2 | 0.536 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#71 | property | category | other→unknown | unknown | no | 3 | 0.895 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.962 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#83 | place | org | address→address | wrong | no | 2 | 0.787 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.814 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#134 | dbpedia_score | other | rate→rate | other_ng | no | 2 | 0.884 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#148 | mechanism | category | id→id | wrong | no | 2 | 0.611 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#152 | 東第5 | quantity | quantity→unknown | unknown | no | 1 | 0.493 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | general#207 | year_step_size | quantity | category→category | wrong | no | 2 | 0.755 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | general#234 | 発生県 | id | address→address | wrong | no | 2 | 0.623 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#283 | 城南第2 | quantity | date→unknown | unknown | no | 2 | 0.634 | date_value_evidence_low | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#286 | value | other | rate→rate | other_ng | no | 2 | 0.970 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.963 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#302 | episode | other | quantity→quantity | other_ng | no | >3 | 0.657 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.853 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#309 | goal | id | category→category | wrong | no | >3 | 0.670 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 2 | 0.989 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | general#343 | mt2 | other | category→category | other_ng | no | >3 | 0.657 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.925 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.937 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#382 | source | category | text→text | wrong | no | 2 | 0.887 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#41 | total invoices paid | quantity | amount→amount | wrong | yes | 2 | 0.661 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.981 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business#84 | department | org | account→account | wrong | no | 2 | 0.871 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#92 | department | org | account→account | wrong | no | 2 | 0.508 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#101 | entitiy | org | account→account | wrong | no | 3 | 0.773 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business#136 | capital revenue | category | account→account | wrong | no | 2 | 0.505 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#148 | merchant details | text | category→category | wrong | no | 3 | 0.977 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business#199 | department | org | account→account | wrong | no | 3 | 0.967 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business#225 | description | account | text→text | wrong | no | 2 | 0.803 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.881 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#238 | procurementclassification:proclasslabel | account | category→category | wrong | no | 2 | 0.918 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.964 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.944 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#320 | dispute-status_statut-de-différend-fra | category | text→text | wrong | no | 2 | 0.815 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#342 | commodity-title_en | product | category→unknown | unknown | no | 2 | 0.460 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#344 | portefeuille_nom_et_code | org | account→account | wrong | no | 2 | 0.760 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#347 | regrp_sommaire | account | category→unknown | unknown | no | 2 | 0.418 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#401 | ligne | category | id→id | wrong | no | 2 | 0.797 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#403 | tournée | id | category→category | wrong | no | 2 | 0.527 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.984 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business#408 | km budgété | other | quantity→quantity | other_ng | no | 2 | 0.509 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#451 | title | category | text→text | wrong | no | 3 | 0.569 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#13 | cost centre description | account | org→org | wrong | no | 2 | 0.513 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#45 | type | account | category→category | wrong | no | 2 | 0.969 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#75 | monitor | id | category→category | wrong | no | 2 | 0.928 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#90 | total invoices paid | quantity | amount→unknown | unknown | no | 2 | 0.610 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business2#149 | projection | category | id→id | wrong | no | 2 | 0.953 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#151 | habitatdescription | text | other→unknown | unknown | no | 2 | 0.563 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business2#163 | projection | category | id→id | wrong | no | 2 | 0.953 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#176 | contravention | category | text→text | wrong | no | 2 | 0.675 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#177 | fine | amount | rate→rate | wrong | yes | >3 | 0.861 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | business2#238 | terrace | quantity | other→unknown | unknown | no | 3 | 0.450 | probability_below_threshold | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | business2#288 | construction_age_band | category | date→date | wrong | no | 2 | 0.667 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#298 | number_habitable_rooms | quantity | quantity→unknown | unknown | no | 1 | 0.941 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.956 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#301 | total_floor_area_known | category | other→unknown | unknown | no | 3 | 0.680 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | business2#317 | energy_consumption | other | quantity→quantity | other_ng | no | 2 | 0.817 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#321 | avg_tilt | other | rate→rate | other_ng | no | 2 | 0.546 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#325 | loac_group | category | address→address | wrong | no | 2 | 0.946 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#326 | fuel_poverty | rate | category→category | wrong | no | >3 | 0.832 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | business2#379 | terrace | quantity | other→unknown | unknown | no | 3 | 0.532 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | business2#381 | total_verified_sales | quantity | amount→amount | wrong | yes | 2 | 0.934 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#440 | situtation | address | text→text | wrong | no | 3 | 0.919 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.989 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.978 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.981 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.980 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.975 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.985 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#946 | service_responsable | account | category→category | wrong | no | 2 | 0.630 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.774 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#958 | volume (mcf) | quantity | other→unknown | unknown | no | 2 | 0.521 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business2#962 | service | account | org→org | wrong | no | >3 | 0.875 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | business2#972 | sales-goods-svcs_ventes-biens-srvs | amount | amount→unknown | unknown | no | 1 | 0.518 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity→unknown | unknown | no | 2 | 0.500 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.989 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#128 | 担当課 | org | account→account | wrong | no | 2 | 0.840 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.626 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#151 | taxable | category | category→unknown | unknown | no | 1 | 0.480 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | dev220#171 | customer rank | quantity | category→category | wrong | no | >3 | 0.742 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | dev220#172 | supplier rank | quantity | category→category | wrong | no | >3 | 0.967 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | >3 | 0.625 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#1 | author | person | org→org | wrong | no | 2 | 0.793 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.861 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 2 | 0.936 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | >3 | 0.959 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#47 | mood | other | category→category | other_ng | no | 2 | 0.808 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#71 | property | category | other→unknown | unknown | no | 3 | 0.835 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 3 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.960 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#83 | place | org | address→address | wrong | no | 2 | 0.870 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.957 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#112 | 住家全壊 | quantity | other→unknown | unknown | no | 2 | 0.561 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#121 | dag-stage | other | category→category | other_ng | no | 2 | 0.501 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#134 | dbpedia_score | other | rate→rate | other_ng | no | 2 | 0.826 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#148 | mechanism | category | id→id | wrong | no | 2 | 0.757 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#174 | domain | category | id→unknown | unknown | no | 3 | 0.328 | probability_below_threshold | raw誤り＋見送り | 上位3候補内の境界 |
| 3 | general#197 | age_q3 | quantity | quantity→unknown | unknown | no | 1 | 0.463 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | general#207 | year_step_size | quantity | category→category | wrong | no | 3 | 0.875 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | general#213 | age_q3_nd | quantity | quantity→unknown | unknown | no | 1 | 0.494 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | general#224 | study | text | person→person | wrong | no | 2 | 0.509 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | general#234 | 発生県 | id | address→unknown | unknown | no | 2 | 0.334 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#282 | 読み方 | address | org→org | wrong | no | 2 | 0.640 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#286 | value | other | rate→rate | other_ng | no | 2 | 0.919 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#291 | cleaned | text | account→account | wrong | no | 2 | 0.610 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.971 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.724 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#309 | goal | id | quantity→quantity | wrong | yes | >3 | 0.620 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | >3 | 0.984 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | general#343 | mt2 | other | category→category | other_ng | no | >3 | 0.593 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#370 | source_value | category | other→unknown | unknown | no | >3 | 0.478 | probability_below_threshold | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.947 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.954 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#382 | source | category | text→text | wrong | no | 2 | 0.835 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#41 | total invoices paid | quantity | quantity→unknown | unknown | no | 1 | 0.511 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.984 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business#77 | publisher label | org | address→address | wrong | no | 2 | 0.559 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#84 | department | org | account→account | wrong | no | 2 | 0.824 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#101 | entitiy | org | account→account | wrong | no | 2 | 0.682 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#148 | merchant details | text | category→category | wrong | no | 2 | 0.579 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#199 | department | org | account→account | wrong | no | 2 | 0.958 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#215 | account_name | account | org→org | wrong | no | 2 | 0.572 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#225 | description | account | text→text | wrong | no | 2 | 0.569 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.689 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#238 | procurementclassification:proclasslabel | account | category→category | wrong | no | 2 | 0.731 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.970 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.954 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business#312 | agebann | category | id→unknown | unknown | no | 2 | 0.434 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business#320 | dispute-status_statut-de-différend-fra | category | text→text | wrong | no | 2 | 0.725 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#332 | segment | id | category→category | wrong | no | 2 | 0.614 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#342 | commodity-title_en | product | category→category | wrong | no | 2 | 0.514 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#344 | portefeuille_nom_et_code | org | account→account | wrong | no | 2 | 0.574 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#347 | regrp_sommaire | account | category→category | wrong | no | 2 | 0.827 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#401 | ligne | category | id→unknown | unknown | no | 2 | 0.487 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.977 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business#451 | title | category | account→unknown | unknown | no | 2 | 0.442 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#5 | account name | account | org→org | wrong | no | 2 | 0.504 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#13 | cost centre description | account | org→org | wrong | no | 2 | 0.728 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#45 | type | account | category→category | wrong | no | 2 | 0.966 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#75 | monitor | id | category→category | wrong | no | 2 | 0.957 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#90 | total invoices paid | quantity | amount→unknown | unknown | no | 2 | 0.536 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#163 | projection | category | id→id | wrong | no | 2 | 0.522 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#177 | fine | amount | rate→rate | wrong | yes | >3 | 0.611 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#230 | warddesc | address | category→category | wrong | no | 2 | 0.688 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#238 | terrace | quantity | other→unknown | unknown | no | 3 | 0.920 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 3 | business2#291 | epc_score_known | category | other→unknown | unknown | no | 2 | 0.516 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#295 | potential_epc_score_known | category | other→unknown | unknown | no | 2 | 0.484 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#298 | number_habitable_rooms | quantity | category→category | wrong | no | 2 | 0.672 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.877 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#301 | total_floor_area_known | category | other→unknown | unknown | no | >3 | 0.938 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#323 | imd19_income_decile | category | amount→amount | wrong | no | 2 | 0.644 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#325 | loac_group | category | address→address | wrong | no | 2 | 0.937 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#326 | fuel_poverty | rate | other→unknown | unknown | no | 2 | 0.619 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#330 | conservation_area_site_id | category | id→id | wrong | no | 2 | 0.748 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#370 | average bids per property | other | amount→amount | other_ng | no | >3 | 0.944 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#379 | terrace | quantity | other→unknown | unknown | no | 3 | 0.918 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 3 | business2#381 | total_verified_sales | quantity | amount→amount | wrong | yes | 2 | 0.940 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#440 | situtation | address | text→text | wrong | no | 3 | 0.702 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.990 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.979 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#548 | health service executive area | address | org→org | wrong | no | 2 | 0.715 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.985 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.978 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.978 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.979 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.982 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#944 | numéro_de_lot | id | address→unknown | unknown | no | 2 | 0.498 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.669 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#962 | service | account | org→org | wrong | no | 3 | 0.805 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business2#963 | numéro entente-cadre | id | quantity→unknown | unknown | no | 2 | 0.524 | numeric_values_not_parseable | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.981 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
