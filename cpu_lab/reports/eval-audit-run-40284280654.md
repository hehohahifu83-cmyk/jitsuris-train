# run 40284280654 交差検証段B：固定5集合の全件誤り監査

作成: 2026-10-26 ChatGPT。対象は許可された dev220 / general / business / business2 / japan_procurement の FT 出力だけ。blind_set*、セット3・5・7は未使用。

## 集計（rawファイルから再計算）

| job | seed | 除外陣 | 集合 | 列数 | 正解率 | 誤り | unknown | 重大 | 学習秒 | peak GPU GiB |
|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | b003,b014,b015,b016,b017 | dev220 | 220 | 97.3% | 6 | 0 | 1 | 1420.3 | 5.46 |
| 1 | 1 | b003,b014,b015,b016,b017 | general | 383 | 91.9% | 18 | 13 | 0 | 1420.3 | 5.46 |
| 1 | 1 | b003,b014,b015,b016,b017 | business | 490 | 96.5% | 11 | 6 | 0 | 1420.3 | 5.46 |
| 1 | 1 | b003,b014,b015,b016,b017 | business2 | 976 | 96.5% | 19 | 15 | 3 | 1420.3 | 5.46 |
| 1 | 1 | b003,b014,b015,b016,b017 | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1420.3 | 5.46 |
| 2 | 1 | b004,b010,b015,b016,b017 | dev220 | 220 | 97.3% | 5 | 1 | 1 | 1504.2 | 5.46 |
| 2 | 1 | b004,b010,b015,b016,b017 | general | 383 | 92.2% | 19 | 11 | 1 | 1504.2 | 5.46 |
| 2 | 1 | b004,b010,b015,b016,b017 | business | 490 | 96.3% | 11 | 7 | 2 | 1504.2 | 5.46 |
| 2 | 1 | b004,b010,b015,b016,b017 | business2 | 976 | 96.7% | 17 | 15 | 4 | 1504.2 | 5.46 |
| 2 | 1 | b004,b010,b015,b016,b017 | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1504.2 | 5.46 |
| 3 | 1 | b005,b007,b015,b016,b017 | dev220 | 220 | 95.9% | 6 | 3 | 1 | 1428.7 | 5.46 |
| 3 | 1 | b005,b007,b015,b016,b017 | general | 383 | 91.6% | 18 | 14 | 0 | 1428.7 | 5.46 |
| 3 | 1 | b005,b007,b015,b016,b017 | business | 490 | 96.5% | 13 | 4 | 0 | 1428.7 | 5.46 |
| 3 | 1 | b005,b007,b015,b016,b017 | business2 | 976 | 96.8% | 19 | 12 | 2 | 1428.7 | 5.46 |
| 3 | 1 | b005,b007,b015,b016,b017 | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1428.7 | 5.46 |
| 4 | 1 | b006,b011,b013,b015,b016,b017 | dev220 | 220 | 95.5% | 9 | 1 | 2 | 1459.1 | 5.55 |
| 4 | 1 | b006,b011,b013,b015,b016,b017 | general | 383 | 92.7% | 15 | 13 | 1 | 1459.1 | 5.55 |
| 4 | 1 | b006,b011,b013,b015,b016,b017 | business | 490 | 95.5% | 13 | 9 | 0 | 1459.1 | 5.55 |
| 4 | 1 | b006,b011,b013,b015,b016,b017 | business2 | 976 | 95.9% | 25 | 15 | 4 | 1459.1 | 5.55 |
| 4 | 1 | b006,b011,b013,b015,b016,b017 | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1459.1 | 5.55 |
| 5 | 1 | b001,b002,b008,b009,b012,b015,b016,b017 | dev220 | 220 | 96.8% | 6 | 1 | 1 | 1394.6 | 5.46 |
| 5 | 1 | b001,b002,b008,b009,b012,b015,b016,b017 | general | 383 | 93.0% | 14 | 13 | 1 | 1394.6 | 5.46 |
| 5 | 1 | b001,b002,b008,b009,b012,b015,b016,b017 | business | 490 | 95.7% | 17 | 4 | 0 | 1394.6 | 5.46 |
| 5 | 1 | b001,b002,b008,b009,b012,b015,b016,b017 | business2 | 976 | 96.9% | 16 | 14 | 3 | 1394.6 | 5.46 |
| 5 | 1 | b001,b002,b008,b009,b012,b015,b016,b017 | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1394.6 | 5.46 |
| 6 | 1 | b015,b016,b017 | dev220 | 220 | 96.8% | 5 | 2 | 1 | 1675.1 | 5.48 |
| 6 | 1 | b015,b016,b017 | general | 383 | 93.5% | 16 | 9 | 1 | 1675.1 | 5.48 |
| 6 | 1 | b015,b016,b017 | business | 490 | 95.7% | 15 | 6 | 0 | 1675.1 | 5.48 |
| 6 | 1 | b015,b016,b017 | business2 | 976 | 96.6% | 21 | 12 | 3 | 1675.1 | 5.48 |
| 6 | 1 | b015,b016,b017 | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1675.1 | 5.48 |

| 集合 | 平均正解率 | 平均誤り | 平均unknown | 平均重大 |
|---|---:|---:|---:|---:|
| dev220 | 96.6% | 6.2 | 1.3 | 1.2 |
| general | 92.5% | 16.7 | 12.2 | 0.7 |
| business | 96.1% | 13.3 | 6.0 | 0.3 |
| business2 | 96.6% | 19.5 | 13.8 | 3.2 |
| japan_procurement | 100.0% | 0.0 | 0.0 | 0.0 |

問題出力 534 件、固有ケース 145 件。2 job以上で再発 104 件、全6 jobで再発 53 件。

## 観測事実と原因仮説
- 観測: rawモデル誤分類 334件。
- 観測: raw誤り＋見送り 112件。
- 観測: guardが正解rawを変更 88件。
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
| 1 | dev220#128 | 担当課 | org | account→account | wrong | no | 2 | 0.944 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.822 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | dev220#154 | shipping address | address | id→id | wrong | no | 2 | 0.681 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | dev220#171 | customer rank | quantity | category→category | wrong | no | 3 | 0.980 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | dev220#172 | supplier rank | quantity | category→category | wrong | no | 3 | 0.976 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 3 | 0.856 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.920 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 3 | 0.942 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | 3 | 0.951 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | general#47 | mood | other | category→category | other_ng | no | 2 | 0.933 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#48 | source | category | org→unknown | unknown | no | 2 | 0.447 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#65 | app | category | other→unknown | unknown | no | 2 | 0.599 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#71 | property | category | other→unknown | unknown | no | 3 | 0.800 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.986 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#83 | place | org | address→address | wrong | no | 2 | 0.688 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.936 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#121 | dag-stage | other | category→category | other_ng | no | >3 | 0.866 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | general#134 | dbpedia_score | other | rate→rate | other_ng | no | 2 | 0.546 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#207 | year_step_size | quantity | category→category | wrong | no | 2 | 0.690 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | general#240 | standardhours | quantity | quantity→unknown | unknown | no | 1 | 0.488 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | general#282 | 読み方 | address | org→org | wrong | no | 2 | 0.687 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#286 | value | other | rate→rate | other_ng | no | 2 | 0.956 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#291 | cleaned | text | account→account | wrong | no | 2 | 0.787 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#292 | abstract rank | other | category→category | other_ng | no | 2 | 0.551 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.975 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#302 | episode | other | id→id | other_ng | no | >3 | 0.588 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.958 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#309 | goal | id | category→category | wrong | no | >3 | 0.676 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | general#315 | standardhours | quantity | other→unknown | unknown | no | 2 | 0.482 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 3 | 0.989 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | general#343 | mt2 | other | category→category | other_ng | no | >3 | 0.706 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | general#370 | source_value | category | other→unknown | unknown | no | 2 | 0.392 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.934 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.974 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#382 | source | category | text→text | wrong | no | 2 | 0.787 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#41 | total invoices paid | quantity | amount→unknown | unknown | no | 2 | 0.528 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business#84 | department | org | account→account | wrong | no | 2 | 0.943 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#92 | department | org | account→account | wrong | no | 2 | 0.860 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#101 | entitiy | org | account→account | wrong | no | 3 | 0.834 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business#148 | merchant details | text | category→category | wrong | no | 2 | 0.942 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#199 | department | org | account→account | wrong | no | 2 | 0.974 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.778 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#238 | procurementclassification:proclasslabel | account | category→category | wrong | no | 2 | 0.578 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.980 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.977 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business#347 | regrp_sommaire | account | category→category | wrong | no | 2 | 0.932 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#401 | ligne | category | id→id | wrong | no | 2 | 0.668 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#404 | type de matériel | category | id→id | wrong | no | 2 | 0.820 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business#408 | km budgété | other | quantity→quantity | other_ng | no | 2 | 0.511 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#451 | title | category | text→unknown | unknown | no | 3 | 0.449 | probability_below_threshold | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business2#45 | type | account | category→category | wrong | no | 2 | 0.959 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#75 | monitor | id | category→category | wrong | no | 2 | 0.900 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#90 | total invoices paid | quantity | quantity→unknown | unknown | no | 1 | 0.569 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#149 | projection | category | id→id | wrong | no | 3 | 0.949 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business2#163 | projection | category | id→id | wrong | no | >3 | 0.950 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | business2#177 | fine | amount | rate→rate | wrong | yes | >3 | 0.622 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | business2#230 | warddesc | address | category→category | wrong | no | 2 | 0.756 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#238 | terrace | quantity | other→unknown | unknown | no | 3 | 0.564 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business2#291 | epc_score_known | category | category→unknown | unknown | no | 1 | 0.471 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#298 | number_habitable_rooms | quantity | category→category | wrong | no | 2 | 0.815 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.944 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#301 | total_floor_area_known | category | other→unknown | unknown | no | 3 | 0.749 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business2#323 | imd19_income_decile | category | category→unknown | unknown | no | 1 | 0.480 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#326 | fuel_poverty | rate | other→unknown | unknown | no | 2 | 0.674 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business2#356 | want to live in this parish only | quantity | category→category | wrong | no | 2 | 0.763 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#364 | want to live in this parish & band a | quantity | category→category | wrong | no | 2 | 0.750 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#370 | average bids per property | other | quantity→quantity | other_ng | no | 3 | 0.709 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business2#379 | terrace | quantity | address→address | wrong | no | 3 | 0.518 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business2#381 | total_verified_sales | quantity | amount→amount | wrong | yes | 2 | 0.872 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#440 | situtation | address | category→category | wrong | no | 3 | 0.630 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.990 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.973 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#548 | health service executive area | address | org→org | wrong | no | 2 | 0.614 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.986 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.985 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.986 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.986 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#945 | état | category | account→account | wrong | no | 2 | 0.625 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.973 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#959 | numéro | id | address→unknown | unknown | no | 2 | 0.497 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business2#962 | service | account | org→org | wrong | no | >3 | 0.707 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | business2#973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity→unknown | unknown | no | 2 | 0.591 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.989 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#128 | 担当課 | org | account→account | wrong | no | 2 | 0.887 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.816 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#143 | terms | category | text→unknown | unknown | no | 2 | 0.495 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | dev220#171 | customer rank | quantity | category→category | wrong | no | >3 | 0.978 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | dev220#172 | supplier rank | quantity | category→category | wrong | no | >3 | 0.978 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 3 | 0.983 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.796 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 2 | 0.890 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | >3 | 0.719 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | general#48 | source | category | org→org | wrong | no | 2 | 0.597 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#71 | property | category | text→unknown | unknown | no | 3 | 0.467 | probability_below_threshold | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.939 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#83 | place | org | address→address | wrong | no | 2 | 0.721 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.970 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#121 | dag-stage | other | quantity→quantity | other_ng | no | 3 | 0.865 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | general#174 | domain | category | id→id | wrong | no | 2 | 0.565 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#175 | bib | id | text→text | wrong | no | >3 | 0.799 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | general#223 | cause_of_invalid_ranking | text | category→unknown | unknown | no | 2 | 0.476 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#224 | study | text | text→unknown | unknown | no | 1 | 0.424 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | general#234 | 発生県 | id | address→address | wrong | no | 2 | 0.901 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#269 | female_frequency | rate | quantity→unknown | unknown | no | 2 | 0.463 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#282 | 読み方 | address | org→org | wrong | no | 2 | 0.803 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#286 | value | other | rate→rate | other_ng | no | 2 | 0.878 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#291 | cleaned | text | account→account | wrong | no | 2 | 0.785 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#292 | abstract rank | other | category→category | other_ng | no | 2 | 0.871 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.985 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#302 | episode | other | quantity→quantity | other_ng | no | >3 | 0.849 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.763 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#309 | goal | id | quantity→quantity | wrong | yes | 3 | 0.520 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 3 | 0.989 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | general#370 | source_value | category | text→text | wrong | no | 2 | 0.721 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.502 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.868 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#382 | source | category | text→text | wrong | no | 2 | 0.846 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#41 | total invoices paid | quantity | amount→amount | wrong | yes | 2 | 0.787 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business#84 | department | org | account→account | wrong | no | 2 | 0.934 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#101 | entitiy | org | account→account | wrong | no | 3 | 0.720 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business#148 | merchant details | text | category→category | wrong | no | 3 | 0.953 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business#199 | department | org | account→account | wrong | no | 3 | 0.967 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.962 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#238 | procurementclassification:proclasslabel | account | category→category | wrong | no | 2 | 0.899 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.914 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.821 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#344 | portefeuille_nom_et_code | org | account→unknown | unknown | no | 2 | 0.475 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#347 | regrp_sommaire | account | category→category | wrong | no | >3 | 0.854 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | business#401 | ligne | category | id→id | wrong | no | 2 | 0.907 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#404 | type de matériel | category | id→id | wrong | no | 2 | 0.517 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.982 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business#459 | australian sourced goods | amount | quantity→unknown | unknown | no | 2 | 0.492 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#461 | overseas sourced goods | amount | quantity→unknown | unknown | no | 2 | 0.499 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#462 | overseas sourced services | amount | quantity→quantity | wrong | yes | 2 | 0.619 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#45 | type | account | category→category | wrong | no | 2 | 0.972 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#75 | monitor | id | category→category | wrong | no | 3 | 0.958 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#90 | total invoices paid | quantity | amount→amount | wrong | yes | 2 | 0.744 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#149 | projection | category | id→id | wrong | no | 3 | 0.792 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#150 | habitatcode | id | category→category | wrong | no | 2 | 0.503 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#163 | projection | category | id→id | wrong | no | 3 | 0.789 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#176 | contravention | category | text→text | wrong | no | 2 | 0.839 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#177 | fine | amount | category→unknown | unknown | no | >3 | 0.381 | probability_below_threshold | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | business2#238 | terrace | quantity | other→unknown | unknown | no | 3 | 0.955 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | business2#291 | epc_score_known | category | category→unknown | unknown | no | 1 | 0.336 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#298 | number_habitable_rooms | quantity | quantity→unknown | unknown | no | 1 | 0.739 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.968 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#301 | total_floor_area_known | category | quantity→quantity | wrong | no | 3 | 0.552 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#370 | average bids per property | other | amount→amount | other_ng | no | 3 | 0.716 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#379 | terrace | quantity | other→unknown | unknown | no | 3 | 0.956 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | business2#440 | situtation | address | category→category | wrong | no | 3 | 0.856 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.989 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#534 | scheme | id | id→unknown | unknown | no | 1 | 0.416 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.975 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#562 | name | org | address→address | wrong | no | 2 | 0.745 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.737 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#958 | volume (mcf) | quantity | other→unknown | unknown | no | 2 | 0.653 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business2#962 | service | account | org→org | wrong | no | >3 | 0.712 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | business2#970 | return-on-investments_revenus-de-placements | amount | amount→unknown | unknown | no | 1 | 0.555 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#972 | sales-goods-svcs_ventes-biens-srvs | amount | quantity→quantity | wrong | yes | 2 | 0.967 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity→quantity | wrong | yes | 2 | 0.982 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.992 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#75 | 支払を受ける者の個人番号 | id | id→unknown | unknown | no | 1 | 0.494 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | dev220#128 | 担当課 | org | account→account | wrong | no | 2 | 0.947 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.658 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#170 | tax id | id | other→unknown | unknown | no | 2 | 0.907 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | dev220#171 | customer rank | quantity | category→category | wrong | no | >3 | 0.882 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | dev220#172 | supplier rank | quantity | category→category | wrong | no | >3 | 0.952 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 3 | 0.968 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | dev220#196 | credit limit | amount | quantity→unknown | unknown | no | 2 | 0.480 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | dev220#201 | city | address | id→id | wrong | no | 2 | 0.609 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.915 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 2 | 0.685 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | >3 | 0.978 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#47 | mood | other | category→category | other_ng | no | 2 | 0.673 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#48 | source | category | org→unknown | unknown | no | 3 | 0.499 | probability_below_threshold | raw誤り＋見送り | 上位3候補内の境界 |
| 3 | general#71 | property | category | other→unknown | unknown | no | 3 | 0.659 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 3 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.953 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#83 | place | org | address→address | wrong | no | 2 | 0.715 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.962 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#104 | term | text | text→unknown | unknown | no | 1 | 0.500 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | general#121 | dag-stage | other | category→category | other_ng | no | 3 | 0.578 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | general#132 | _status_ | other | category→category | other_ng | no | 2 | 0.619 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#134 | dbpedia_score | other | rate→rate | other_ng | no | 2 | 0.837 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#174 | domain | category | address→unknown | unknown | no | 2 | 0.474 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#207 | year_step_size | quantity | category→category | wrong | no | >3 | 0.847 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#213 | age_q3_nd | quantity | quantity→unknown | unknown | no | 1 | 0.573 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | general#234 | 発生県 | id | address→address | wrong | no | 2 | 0.664 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#282 | 読み方 | address | org→org | wrong | no | 2 | 0.853 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#286 | value | other | rate→rate | other_ng | no | 2 | 0.911 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.943 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#302 | episode | other | quantity→quantity | other_ng | no | 3 | 0.585 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.817 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#309 | goal | id | category→unknown | unknown | no | >3 | 0.500 | probability_below_threshold | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 3 | 0.990 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 3 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | general#343 | mt2 | other | category→category | other_ng | no | >3 | 0.949 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#351 | operationid | other | id→id | other_ng | no | 3 | 0.633 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | general#370 | source_value | category | other→unknown | unknown | no | 2 | 0.646 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.811 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.945 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#382 | source | category | text→text | wrong | no | 2 | 0.724 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business#84 | department | org | account→account | wrong | no | 2 | 0.980 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#92 | department | org | account→account | wrong | no | 2 | 0.912 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#101 | entitiy | org | account→account | wrong | no | 3 | 0.691 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business#148 | merchant details | text | category→category | wrong | no | 2 | 0.550 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#199 | department | org | account→account | wrong | no | 3 | 0.982 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business#225 | description | account | text→text | wrong | no | 2 | 0.961 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.766 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#238 | procurementclassification:proclasslabel | account | category→category | wrong | no | 2 | 0.872 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#278 | 目名 | category | other→unknown | unknown | no | 3 | 0.983 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 3 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.948 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business#332 | segment | id | category→category | wrong | no | 2 | 0.660 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#344 | portefeuille_nom_et_code | org | account→account | wrong | no | 2 | 0.856 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#347 | regrp_sommaire | account | category→category | wrong | no | 2 | 0.513 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.984 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business#408 | km budgété | other | quantity→quantity | other_ng | no | 2 | 0.744 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#451 | title | category | account→account | wrong | no | 2 | 0.621 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#45 | type | account | category→category | wrong | no | 2 | 0.852 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#75 | monitor | id | category→category | wrong | no | 2 | 0.874 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#149 | projection | category | id→id | wrong | no | 2 | 0.934 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#163 | projection | category | id→id | wrong | no | 2 | 0.946 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#176 | contravention | category | text→text | wrong | no | 2 | 0.834 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#177 | fine | amount | category→category | wrong | no | >3 | 0.607 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#230 | warddesc | address | category→category | wrong | no | 2 | 0.860 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#238 | terrace | quantity | other→unknown | unknown | no | >3 | 0.948 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#298 | number_habitable_rooms | quantity | category→category | wrong | no | 2 | 0.712 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.956 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#301 | total_floor_area_known | category | other→unknown | unknown | no | 3 | 0.965 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 3 | business2#325 | loac_group | category | address→address | wrong | no | 2 | 0.944 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#326 | fuel_poverty | rate | other→unknown | unknown | no | 2 | 0.903 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#370 | average bids per property | other | amount→amount | other_ng | no | 3 | 0.846 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business2#379 | terrace | quantity | other→unknown | unknown | no | >3 | 0.905 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#381 | total_verified_sales | quantity | amount→amount | wrong | yes | 2 | 0.621 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#440 | situtation | address | category→category | wrong | no | >3 | 0.801 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.990 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.967 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#548 | health service executive area | address | org→org | wrong | no | 2 | 0.687 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#946 | service_responsable | account | category→category | wrong | no | 2 | 0.901 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.796 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#956 | terminal | address | org→org | wrong | no | 2 | 0.507 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#958 | volume (mcf) | quantity | other→unknown | unknown | no | 2 | 0.484 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#962 | service | account | org→org | wrong | no | 3 | 0.877 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.985 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | dev220#98 | 年末調整未済 | category | text→text | wrong | no | 3 | 0.734 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | dev220#128 | 担当課 | org | account→account | wrong | no | 2 | 0.765 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.838 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | dev220#144 | location | org | address→address | wrong | no | 2 | 0.706 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | dev220#171 | customer rank | quantity | category→category | wrong | no | 2 | 0.980 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | dev220#172 | supplier rank | quantity | category→category | wrong | no | >3 | 0.984 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 4 | dev220#174 | sales order | id | date→unknown | unknown | no | 2 | 0.723 | date_value_evidence_low | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 3 | 0.960 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | dev220#196 | credit limit | amount | quantity→quantity | wrong | yes | 2 | 0.814 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | dev220#201 | city | address | id→id | wrong | no | 2 | 0.840 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.879 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 2 | 0.979 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | 2 | 0.974 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | general#48 | source | category | org→unknown | unknown | no | 2 | 0.410 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | general#53 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity→quantity | wrong | no | 2 | 0.772 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | general#71 | property | category | other→unknown | unknown | no | 2 | 0.662 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.959 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | general#83 | place | org | address→address | wrong | no | 2 | 0.878 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.989 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | general#121 | dag-stage | other | quantity→quantity | other_ng | no | 3 | 0.805 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | general#207 | year_step_size | quantity | quantity→unknown | unknown | no | 1 | 0.475 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.990 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | general#240 | standardhours | quantity | other→unknown | unknown | no | 2 | 0.510 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | general#282 | 読み方 | address | org→org | wrong | no | 2 | 0.767 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | general#286 | value | other | rate→rate | other_ng | no | 3 | 0.947 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | general#291 | cleaned | text | category→category | wrong | no | 2 | 0.708 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | general#292 | abstract rank | other | category→category | other_ng | no | 2 | 0.692 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | >3 | 0.985 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 4 | general#302 | episode | other | quantity→quantity | other_ng | no | 3 | 0.509 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.902 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | general#309 | goal | id | quantity→quantity | wrong | yes | >3 | 0.927 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 4 | general#315 | standardhours | quantity | other→unknown | unknown | no | 2 | 0.649 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 2 | 0.992 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.990 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | general#343 | mt2 | other | quantity→quantity | other_ng | no | 3 | 0.926 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | general#370 | source_value | category | other→unknown | unknown | no | 2 | 0.506 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.933 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | general#382 | source | category | text→text | wrong | no | 2 | 0.546 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#41 | total invoices paid | quantity | amount→unknown | unknown | no | 2 | 0.555 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | business#84 | department | org | account→account | wrong | no | 2 | 0.943 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#92 | department | org | account→account | wrong | no | 2 | 0.629 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#101 | entitiy | org | account→account | wrong | no | 3 | 0.598 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | business#148 | merchant details | text | category→category | wrong | no | 2 | 0.932 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#199 | department | org | account→account | wrong | no | 2 | 0.982 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#225 | description | account | text→text | wrong | no | 2 | 0.985 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.801 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#238 | procurementclassification:proclasslabel | account | category→category | wrong | no | 2 | 0.810 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.932 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.941 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | business#303 | d1 | category | quantity→quantity | wrong | no | 2 | 0.542 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#304 | d2 | category | quantity→unknown | unknown | no | 2 | 0.496 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | business#332 | segment | id | category→category | wrong | no | 2 | 0.517 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#344 | portefeuille_nom_et_code | org | account→account | wrong | no | 2 | 0.538 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#347 | regrp_sommaire | account | category→category | wrong | no | 2 | 0.953 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#401 | ligne | category | id→id | wrong | no | 2 | 0.891 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business#404 | type de matériel | category | product→unknown | unknown | no | 2 | 0.461 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.981 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | business#451 | title | category | account→unknown | unknown | no | 3 | 0.436 | probability_below_threshold | raw誤り＋見送り | 上位3候補内の境界 |
| 4 | business#459 | australian sourced goods | amount | quantity→unknown | unknown | no | 2 | 0.535 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | business2#13 | cost centre description | account | org→org | wrong | no | 2 | 0.723 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#45 | type | account | category→category | wrong | no | 2 | 0.979 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#58 | numbers of | date | date→unknown | unknown | no | 1 | 0.559 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | business2#75 | monitor | id | category→category | wrong | no | 2 | 0.927 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#90 | total invoices paid | quantity | amount→unknown | unknown | no | 2 | 0.550 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | business2#149 | projection | category | id→id | wrong | no | 2 | 0.759 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#151 | habitatdescription | text | other→unknown | unknown | no | 2 | 0.479 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | business2#163 | projection | category | id→id | wrong | no | 2 | 0.786 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#176 | contravention | category | text→text | wrong | no | 2 | 0.776 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#177 | fine | amount | rate→unknown | unknown | no | >3 | 0.472 | probability_below_threshold | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 4 | business2#230 | warddesc | address | category→category | wrong | no | 2 | 0.694 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#238 | terrace | quantity | other→unknown | unknown | no | >3 | 0.634 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 4 | business2#288 | construction_age_band | category | date→date | wrong | no | 3 | 0.852 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | business2#291 | epc_score_known | category | quantity→quantity | wrong | no | 3 | 0.627 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | business2#295 | potential_epc_score_known | category | quantity→quantity | wrong | no | 2 | 0.513 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#298 | number_habitable_rooms | quantity | category→category | wrong | no | 2 | 0.556 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.951 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#301 | total_floor_area_known | category | other→unknown | unknown | no | 3 | 0.842 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 4 | business2#317 | energy_consumption | other | quantity→quantity | other_ng | no | 2 | 0.672 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#321 | avg_tilt | other | quantity→quantity | other_ng | no | 2 | 0.526 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#325 | loac_group | category | address→address | wrong | no | >3 | 0.988 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 4 | business2#326 | fuel_poverty | rate | other→unknown | unknown | no | 2 | 0.696 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | business2#356 | want to live in this parish only | quantity | category→category | wrong | no | 2 | 0.704 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#379 | terrace | quantity | address→address | wrong | no | >3 | 0.633 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 4 | business2#381 | total_verified_sales | quantity | amount→amount | wrong | yes | 2 | 0.932 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#440 | situtation | address | text→text | wrong | no | 3 | 0.543 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.988 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | business2#526 | tlist(d1) | date | id→unknown | unknown | no | 2 | 0.591 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 4 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.972 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | business2#548 | health service executive area | address | org→org | wrong | no | 2 | 0.761 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#562 | name | org | address→address | wrong | no | 2 | 0.713 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 4 | business2#962 | service | account | org→org | wrong | no | 3 | 0.771 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 4 | business2#972 | sales-goods-svcs_ventes-biens-srvs | amount | quantity→quantity | wrong | yes | 2 | 0.852 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity→quantity | wrong | yes | 2 | 0.897 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 4 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.991 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | dev220#128 | 担当課 | org | account→account | wrong | no | 2 | 0.979 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.865 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | dev220#170 | tax id | id | id→unknown | unknown | no | 1 | 0.471 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | dev220#171 | customer rank | quantity | category→category | wrong | no | >3 | 0.956 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 5 | dev220#172 | supplier rank | quantity | category→category | wrong | no | >3 | 0.975 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 5 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 3 | 0.935 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 5 | dev220#201 | city | address | id→id | wrong | no | 2 | 0.663 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.838 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 2 | 0.967 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | 3 | 0.858 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 5 | general#47 | mood | other | category→category | other_ng | no | 2 | 0.650 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#71 | property | category | other→unknown | unknown | no | 3 | 0.871 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 5 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.931 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#83 | place | org | address→address | wrong | no | 2 | 0.651 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.913 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 5 | general#104 | term | text | category→category | wrong | no | 2 | 0.967 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#121 | dag-stage | other | category→category | other_ng | no | 3 | 0.926 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 5 | general#152 | 東第5 | quantity | date→unknown | unknown | no | 2 | 0.971 | date_value_evidence_low | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 5 | general#207 | year_step_size | quantity | category→category | wrong | no | 2 | 0.964 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#224 | study | text | text→unknown | unknown | no | 1 | 0.449 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | general#234 | 発生県 | id | address→address | wrong | no | 2 | 0.837 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#283 | 城南第2 | quantity | date→unknown | unknown | no | 2 | 0.570 | date_value_evidence_low | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 5 | general#286 | value | other | rate→rate | other_ng | no | 2 | 0.958 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.752 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 5 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.964 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#309 | goal | id | quantity→quantity | wrong | yes | >3 | 0.870 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 5 | general#315 | standardhours | quantity | quantity→unknown | unknown | no | 1 | 0.484 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 2 | 0.986 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 5 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.986 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | general#343 | mt2 | other | category→category | other_ng | no | >3 | 0.674 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 5 | general#370 | source_value | category | category→unknown | unknown | no | 1 | 0.226 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.666 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.882 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 5 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.990 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business#77 | publisher label | org | address→address | wrong | no | 2 | 0.683 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#84 | department | org | account→account | wrong | no | 2 | 0.984 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#92 | department | org | account→account | wrong | no | 2 | 0.970 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#101 | entitiy | org | account→account | wrong | no | 2 | 0.590 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#148 | merchant details | text | category→category | wrong | no | 3 | 0.979 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 5 | business#199 | department | org | account→account | wrong | no | 3 | 0.985 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 5 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.932 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#238 | procurementclassification:proclasslabel | account | category→category | wrong | no | 2 | 0.938 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.878 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 5 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.939 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 5 | business#303 | d1 | category | quantity→quantity | wrong | no | 2 | 0.670 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#304 | d2 | category | quantity→quantity | wrong | no | 2 | 0.627 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#308 | d6 | category | quantity→quantity | wrong | no | 2 | 0.561 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#312 | agebann | category | quantity→quantity | wrong | no | 2 | 0.802 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#344 | portefeuille_nom_et_code | org | account→account | wrong | no | 2 | 0.916 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#347 | regrp_sommaire | account | category→category | wrong | no | 2 | 0.550 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#404 | type de matériel | category | id→id | wrong | no | 2 | 0.830 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.970 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business#408 | km budgété | other | quantity→quantity | other_ng | no | 2 | 0.749 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business#451 | title | category | account→account | wrong | no | 2 | 0.572 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#45 | type | account | category→category | wrong | no | 2 | 0.940 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#75 | monitor | id | category→category | wrong | no | 2 | 0.789 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#149 | projection | category | id→id | wrong | no | 3 | 0.628 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 5 | business2#163 | projection | category | id→id | wrong | no | 3 | 0.693 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 5 | business2#177 | fine | amount | rate→rate | wrong | yes | >3 | 0.516 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 5 | business2#230 | warddesc | address | category→category | wrong | no | 3 | 0.969 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 5 | business2#238 | terrace | quantity | other→unknown | unknown | no | 3 | 0.556 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 5 | business2#288 | construction_age_band | category | date→date | wrong | no | 2 | 0.949 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#298 | number_habitable_rooms | quantity | category→category | wrong | no | 2 | 0.747 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.985 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#301 | total_floor_area_known | category | category→unknown | unknown | no | 1 | 0.368 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business2#325 | loac_group | category | address→address | wrong | no | 2 | 0.502 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#326 | fuel_poverty | rate | other→unknown | unknown | no | 2 | 0.475 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 5 | business2#356 | want to live in this parish only | quantity | category→category | wrong | no | 2 | 0.596 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#379 | terrace | quantity | other→unknown | unknown | no | 3 | 0.706 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 5 | business2#381 | total_verified_sales | quantity | amount→amount | wrong | yes | 2 | 0.962 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#440 | situtation | address | category→category | wrong | no | 3 | 0.878 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 5 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.989 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.977 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business2#548 | health service executive area | address | address→unknown | unknown | no | 1 | 0.496 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.986 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.984 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.982 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.984 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.985 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 5 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.671 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#958 | volume (mcf) | quantity | other→unknown | unknown | no | 2 | 0.871 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 5 | business2#962 | service | account | org→org | wrong | no | >3 | 0.926 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 5 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.987 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 5 | business2#975 | amt-units_mnt-unite | category | amount→unknown | unknown | no | 2 | 0.458 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | dev220#128 | 担当課 | org | account→account | wrong | no | 2 | 0.761 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.731 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | dev220#170 | tax id | id | other→unknown | unknown | no | 2 | 0.515 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | dev220#171 | customer rank | quantity | category→category | wrong | no | >3 | 0.963 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 6 | dev220#172 | supplier rank | quantity | category→category | wrong | no | >3 | 0.973 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 6 | dev220#174 | sales order | id | date→unknown | unknown | no | 2 | 0.951 | date_value_evidence_low | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 3 | 0.980 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | general#1 | author | person | org→org | wrong | no | 2 | 0.640 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.962 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 2 | 0.667 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | 3 | 0.683 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 6 | general#71 | property | category | other→unknown | unknown | no | 3 | 0.922 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 6 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.974 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#83 | place | org | address→address | wrong | no | 2 | 0.843 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.971 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | general#121 | dag-stage | other | category→category | other_ng | no | 3 | 0.600 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | general#207 | year_step_size | quantity | category→category | wrong | no | 2 | 0.846 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#223 | cause_of_invalid_ranking | text | category→category | wrong | no | 2 | 0.562 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.991 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | general#234 | 発生県 | id | address→address | wrong | no | 2 | 0.899 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#282 | 読み方 | address | org→org | wrong | no | 2 | 0.943 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#286 | value | other | rate→rate | other_ng | no | 2 | 0.951 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.987 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.870 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#309 | goal | id | quantity→quantity | wrong | yes | >3 | 0.741 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 6 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 3 | 0.991 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 6 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.991 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | general#343 | mt2 | other | category→category | other_ng | no | 3 | 0.795 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | general#370 | source_value | category | other→unknown | unknown | no | 2 | 0.741 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.779 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.968 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | general#382 | source | category | text→text | wrong | no | 2 | 0.629 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#41 | total invoices paid | quantity | amount→unknown | unknown | no | 2 | 0.608 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.990 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business#84 | department | org | account→account | wrong | no | 2 | 0.935 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#92 | department | org | account→unknown | unknown | no | 2 | 0.495 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | business#101 | entitiy | org | category→category | wrong | no | >3 | 0.586 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 6 | business#136 | capital revenue | category | account→account | wrong | no | 2 | 0.716 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#148 | merchant details | text | category→category | wrong | no | 3 | 0.972 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | business#199 | department | org | account→account | wrong | no | 2 | 0.985 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#215 | account_name | account | org→org | wrong | no | 2 | 0.542 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#225 | description | account | text→text | wrong | no | 2 | 0.910 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.681 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#238 | procurementclassification:proclasslabel | account | category→category | wrong | no | 2 | 0.566 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.973 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.971 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | business#342 | commodity-title_en | product | category→category | wrong | no | 2 | 0.707 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#344 | portefeuille_nom_et_code | org | account→account | wrong | no | 2 | 0.883 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#347 | regrp_sommaire | account | category→category | wrong | no | 3 | 0.768 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | business#401 | ligne | category | id→id | wrong | no | 2 | 0.979 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#404 | type de matériel | category | id→id | wrong | no | 2 | 0.536 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.990 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business#451 | title | category | text→text | wrong | no | 3 | 0.687 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | business2#45 | type | account | category→category | wrong | no | 2 | 0.869 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#75 | monitor | id | category→category | wrong | no | 3 | 0.835 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | business2#90 | total invoices paid | quantity | amount→amount | wrong | yes | 2 | 0.637 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#149 | projection | category | id→id | wrong | no | 2 | 0.966 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#163 | projection | category | id→id | wrong | no | 2 | 0.969 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#177 | fine | amount | other→unknown | unknown | no | >3 | 0.580 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 6 | business2#230 | warddesc | address | category→category | wrong | no | 2 | 0.683 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#238 | terrace | quantity | other→unknown | unknown | no | 3 | 0.806 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 6 | business2#288 | construction_age_band | category | date→date | wrong | no | 2 | 0.755 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#291 | epc_score_known | category | category→unknown | unknown | no | 1 | 0.420 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business2#298 | number_habitable_rooms | quantity | category→category | wrong | no | 2 | 0.792 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.959 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#301 | total_floor_area_known | category | quantity→quantity | wrong | no | 3 | 0.786 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | business2#318 | energy_consumption_known | category | category→unknown | unknown | no | 1 | 0.397 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business2#322 | imd19_national_decile | category | id→id | wrong | no | 2 | 0.818 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#325 | loac_group | category | address→address | wrong | no | 2 | 0.919 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#326 | fuel_poverty | rate | other→unknown | unknown | no | 2 | 0.695 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 6 | business2#370 | average bids per property | other | amount→amount | other_ng | no | 2 | 0.851 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#379 | terrace | quantity | address→address | wrong | no | 3 | 0.557 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | business2#381 | total_verified_sales | quantity | amount→amount | wrong | yes | 2 | 0.735 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#440 | situtation | address | text→text | wrong | no | 3 | 0.703 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.988 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.979 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business2#548 | health service executive area | address | org→org | wrong | no | 2 | 0.774 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.990 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.990 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.990 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.990 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 6 | business2#946 | service_responsable | account | category→category | wrong | no | 2 | 0.801 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.972 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 6 | business2#962 | service | account | org→org | wrong | no | 3 | 0.850 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 6 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.992 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
