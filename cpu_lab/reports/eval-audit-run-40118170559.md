# run 40118170559 固定5集合の全件誤り監査

作成: 2026-10-25 ChatGPT。対象は許可された dev220 / general / business / business2 / japan_procurement の FT 出力のみ。blind_set*、セット3・5・7は未使用。

## 再現性と成果物
- 学習: C1（multilingual-e5-base、FT_POOL=1、FT_KEEP=1、seed 1–3）。
- 評価artifact: 12571866892、モデルartifact: 12571472299。別成果物として存在し、いずれも2026-11-23まで。
- raw出力は `eval_reports/runs/40118170559/job{1,2,3}_probs_*_ft.json`。各manifestのtest件数とraw行数を照合した。`other_ok`は正式評価どおり正解として扱った。

## 集計（rawファイルから再計算）

| seed | 集合 | 列数 | 正解率 | 誤り | unknown | 重大 | 学習秒 | peak GPU GiB |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | dev220 | 220 | 95.9% | 6 | 3 | 1 | 1260.8 | 5.37 |
| 1 | general | 383 | 92.4% | 18 | 11 | 1 | 1260.8 | 5.37 |
| 1 | business | 490 | 95.9% | 13 | 7 | 1 | 1260.8 | 5.37 |
| 1 | business2 | 976 | 96.4% | 18 | 17 | 4 | 1260.8 | 5.37 |
| 1 | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1260.8 | 5.37 |
| 2 | dev220 | 220 | 95.5% | 9 | 1 | 2 | 1208.2 | 5.37 |
| 2 | general | 383 | 91.6% | 21 | 11 | 2 | 1208.2 | 5.37 |
| 2 | business | 490 | 95.7% | 14 | 7 | 3 | 1208.2 | 5.37 |
| 2 | business2 | 976 | 96.6% | 17 | 16 | 3 | 1208.2 | 5.37 |
| 2 | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1208.2 | 5.37 |
| 3 | dev220 | 220 | 95.9% | 8 | 1 | 2 | 1209.6 | 5.37 |
| 3 | general | 383 | 91.9% | 20 | 11 | 2 | 1209.6 | 5.37 |
| 3 | business | 490 | 95.3% | 17 | 6 | 2 | 1209.6 | 5.37 |
| 3 | business2 | 976 | 96.1% | 22 | 16 | 2 | 1209.6 | 5.37 |
| 3 | japan_procurement | 92 | 100.0% | 0 | 0 | 0 | 1209.6 | 5.37 |

| 集合 | 3 seed平均正解率 | 平均誤り | 平均unknown | 平均重大 |
|---|---:|---:|---:|---:|
| dev220 | 95.8% | 7.7 | 1.7 | 1.7 |
| general | 92.0% | 19.7 | 11.0 | 1.7 |
| business | 95.6% | 14.7 | 6.7 | 2.0 |
| business2 | 96.4% | 19.0 | 16.3 | 3.0 |
| japan_procurement | 100.0% | 0.0 | 0.0 | 0.0 |

全問題出力 290 件、固有ケース 131 件。2 seed以上で再発 92 件、3 seed全てで再発 67 件。

## 観測事実と原因仮説
- 観測: raw誤り＋見送り 53件。
- 観測: rawモデル誤分類 183件。
- 観測: guardが正解rawを変更 54件。
- 原因確定（高確度）: rawが正解でguard後だけ不正解のケースは、後段規則が直接の原因。
- 原因仮説（中確度）: 正解がtop2/top3に残るraw誤分類は、ラベル境界・確信度較正・文脈不足の影響が強い。個別の直接原因は値・UNIT・兄弟列・元表を追加照合しない限り未確定。
- 原因仮説（低〜中確度）: 正解がtop3外のケースは教材分布差、定義未学習、入力切り詰め、出典差のいずれか。dataset単位のtoken切り詰め率はmanifestにあるが、行単位の因果は示せない。
- ラベル疑義はこの監査で変更していない。先生2人の独立確認と根拠裁定が必要。

## 優先対策
1. 高: raw正解をunknown/別ラベルへ変えたguardケースを理由別に再検証する。期待効果は正解回復、副作用は重大誤りの再流入。
2. 高: 3 seedで再発する重大・誤りを、元表タイトル、UNIT、兄弟列、token切り詰め有無と照合する。期待効果は再発根因の特定、副作用は監査工数。
3. 中: top2境界を検査役v2と候補付きunknownで扱い、rhoはb013で固定した0.7を維持して封印セット#3で一度だけ検証する。
4. 中: amount/quantity、org/address/account、date/text、id/quantityのhard negativeを、評価行を流用せず教材側から増やす。一度に一要因だけ試す。

## 全問題一覧

`観測`はrawとguardの保存値から確定。`仮説`は追加検査前の候補であり断定ではない。

| seed | 集合#index | 列名 | 正解 | raw→最終 | outcome | 重大 | 正解rank | top1確率 | reason | 観測 | 仮説 |
|---:|---|---|---|---|---|---:|---:|---:|---|---|---|
| 1 | dev220#75 | 支払を受ける者の個人番号 | id | other→unknown | unknown | no | 2 | 0.456 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | dev220#128 | 担当課 | org | account→account | wrong | no | 2 | 0.918 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.906 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | dev220#143 | terms | category | text→text | wrong | no | 2 | 0.630 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | dev220#170 | tax id | id | other→unknown | unknown | no | 2 | 0.824 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | dev220#171 | customer rank | quantity | category→category | wrong | no | 3 | 0.826 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | dev220#172 | supplier rank | quantity | category→category | wrong | no | >3 | 0.968 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 3 | 0.957 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | dev220#196 | credit limit | amount | amount→unknown | unknown | no | 1 | 0.566 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.904 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 2 | 0.742 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | 2 | 0.903 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#62 | nodes | other | category→category | other_ng | no | 2 | 0.586 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#70 | lda | text | text→unknown | unknown | no | 1 | 0.489 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | general#71 | property | category | other→unknown | unknown | no | 3 | 0.436 | probability_below_threshold | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.909 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#83 | place | org | address→address | wrong | no | 2 | 0.871 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.847 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#104 | term | text | category→unknown | unknown | no | 2 | 0.491 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#121 | dag-stage | other | category→category | other_ng | no | >3 | 0.843 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | general#134 | dbpedia_score | other | rate→rate | other_ng | no | 2 | 0.842 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#148 | mechanism | category | category→unknown | unknown | no | 1 | 0.476 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | general#207 | year_step_size | quantity | category→category | wrong | no | 2 | 0.922 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | general#234 | 発生県 | id | address→address | wrong | no | 2 | 0.516 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#282 | 読み方 | address | org→org | wrong | no | 2 | 0.632 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#286 | value | other | rate→rate | other_ng | no | 2 | 0.926 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#291 | cleaned | text | category→category | wrong | no | 2 | 0.621 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.942 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#306 | 和名 | other | address→address | other_ng | no | 2 | 0.570 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.910 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#309 | goal | id | quantity→quantity | wrong | yes | >3 | 0.836 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 2 | 0.987 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | general#343 | mt2 | other | category→category | other_ng | no | >3 | 0.540 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.810 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.934 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | general#382 | source | category | text→text | wrong | no | 2 | 0.507 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business#77 | publisher label | org | address→address | wrong | no | 2 | 0.692 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#84 | department | org | account→account | wrong | no | 2 | 0.968 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#92 | department | org | account→account | wrong | no | 2 | 0.806 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#101 | entitiy | org | account→account | wrong | no | 2 | 0.787 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#148 | merchant details | text | product→unknown | unknown | no | 2 | 0.422 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business#199 | department | org | account→account | wrong | no | 2 | 0.974 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.916 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#238 | procurementclassification:proclasslabel | account | category→category | wrong | no | 2 | 0.503 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.931 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business#279 | 科名 | category | other→unknown | unknown | no | 3 | 0.956 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business#334 | segment-title_fr | category | account→unknown | unknown | no | 2 | 0.482 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business#344 | portefeuille_nom_et_code | org | category→category | wrong | no | >3 | 0.604 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | business#347 | regrp_sommaire | account | category→category | wrong | no | 2 | 0.965 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#401 | ligne | category | id→id | wrong | no | 2 | 0.858 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#404 | type de matériel | category | id→id | wrong | no | 2 | 0.753 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.980 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business#408 | km budgété | other | quantity→quantity | other_ng | no | 2 | 0.615 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#459 | australian sourced goods | amount | quantity→quantity | wrong | yes | 2 | 0.677 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business#462 | overseas sourced services | amount | amount→unknown | unknown | no | 1 | 0.608 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#45 | type | account | category→category | wrong | no | 2 | 0.981 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#75 | monitor | id | category→category | wrong | no | 2 | 0.879 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#149 | projection | category | id→id | wrong | no | 2 | 0.963 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#163 | projection | category | id→id | wrong | no | 2 | 0.965 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#176 | contravention | category | text→text | wrong | no | 2 | 0.661 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#177 | fine | amount | quantity→quantity | wrong | yes | >3 | 0.670 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 1 | business2#230 | warddesc | address | address→unknown | unknown | no | 1 | 0.446 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#238 | terrace | quantity | other→unknown | unknown | no | 3 | 0.835 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business2#288 | construction_age_band | category | date→unknown | unknown | no | 2 | 0.464 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business2#291 | epc_score_known | category | other→unknown | unknown | no | 2 | 0.515 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business2#298 | number_habitable_rooms | quantity | quantity→unknown | unknown | no | 1 | 0.740 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.941 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#301 | total_floor_area_known | category | other→unknown | unknown | no | 3 | 0.658 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business2#318 | energy_consumption_known | category | category→unknown | unknown | no | 1 | 0.472 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#325 | loac_group | category | address→address | wrong | no | 2 | 0.856 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#330 | conservation_area_site_id | category | id→id | wrong | no | 2 | 0.746 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#370 | average bids per property | other | amount→amount | other_ng | no | 3 | 0.658 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business2#379 | terrace | quantity | other→unknown | unknown | no | 3 | 0.583 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 1 | business2#381 | total_verified_sales | quantity | amount→unknown | unknown | no | 2 | 0.615 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 1 | business2#440 | situtation | address | text→text | wrong | no | 3 | 0.516 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.991 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.977 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#548 | health service executive area | address | address→unknown | unknown | no | 1 | 0.499 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#562 | name | org | address→address | wrong | no | 2 | 0.653 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.988 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.986 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.989 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 1 | business2#946 | service_responsable | account | category→category | wrong | no | 2 | 0.888 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.745 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#962 | service | account | org→org | wrong | no | 3 | 0.762 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 1 | business2#972 | sales-goods-svcs_ventes-biens-srvs | amount | quantity→quantity | wrong | yes | 2 | 0.709 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity→quantity | wrong | yes | 2 | 0.873 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 1 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.988 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#45 | 商品オプション | text | text→unknown | unknown | no | 1 | 0.417 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | dev220#116 | 履行場所 | address | id→id | wrong | no | 2 | 0.532 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#128 | 担当課 | org | account→account | wrong | no | 2 | 0.905 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.891 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#154 | shipping address | address | id→id | wrong | no | 2 | 0.813 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#171 | customer rank | quantity | category→category | wrong | no | 2 | 0.899 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#172 | supplier rank | quantity | category→category | wrong | no | 2 | 0.971 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 2 | 0.953 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#196 | credit limit | amount | quantity→quantity | wrong | yes | 2 | 0.720 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | dev220#201 | city | address | id→id | wrong | no | 2 | 0.611 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#1 | author | person | org→org | wrong | no | 3 | 0.643 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.736 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 3 | 0.982 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | 3 | 0.928 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | general#48 | source | category | org→org | wrong | no | 2 | 0.870 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#70 | lda | text | category→category | wrong | no | 2 | 0.831 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#71 | property | category | category→unknown | unknown | no | 1 | 0.434 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.868 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#83 | place | org | address→address | wrong | no | 2 | 0.880 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.948 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#121 | dag-stage | other | quantity→quantity | other_ng | no | >3 | 0.544 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | general#134 | dbpedia_score | other | rate→rate | other_ng | no | 2 | 0.651 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#148 | mechanism | category | category→unknown | unknown | no | 1 | 0.445 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | general#174 | domain | category | id→id | wrong | no | 2 | 0.504 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#207 | year_step_size | quantity | category→category | wrong | no | 2 | 0.720 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#224 | study | text | person→person | wrong | no | 2 | 0.549 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.981 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | general#234 | 発生県 | id | quantity→quantity | wrong | yes | 2 | 0.734 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#237 | ngram | text | other→unknown | unknown | no | 2 | 0.929 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#282 | 読み方 | address | org→org | wrong | no | 2 | 0.579 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#286 | value | other | rate→rate | other_ng | no | 3 | 0.962 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | general#291 | cleaned | text | category→category | wrong | no | 2 | 0.939 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.955 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#302 | episode | other | quantity→quantity | other_ng | no | >3 | 0.698 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.665 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#309 | goal | id | quantity→quantity | wrong | yes | >3 | 0.638 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 2 | 0.988 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.979 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | general#343 | mt2 | other | quantity→quantity | other_ng | no | >3 | 0.610 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | general#370 | source_value | category | text→unknown | unknown | no | 3 | 0.413 | probability_below_threshold | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.651 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.936 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.968 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business#77 | publisher label | org | address→address | wrong | no | 2 | 0.916 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#84 | department | org | account→account | wrong | no | 2 | 0.961 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#92 | department | org | account→account | wrong | no | 2 | 0.855 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#101 | entitiy | org | category→category | wrong | no | 3 | 0.627 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business#136 | capital revenue | category | account→account | wrong | no | 2 | 0.613 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#148 | merchant details | text | org→unknown | unknown | no | >3 | 0.338 | probability_below_threshold | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | business#199 | department | org | account→account | wrong | no | 2 | 0.967 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#225 | description | account | text→text | wrong | no | 2 | 0.923 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#238 | procurementclassification:proclasslabel | account | category→category | wrong | no | 2 | 0.667 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.953 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.955 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#344 | portefeuille_nom_et_code | org | account→account | wrong | no | 3 | 0.851 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business#347 | regrp_sommaire | account | category→category | wrong | no | 2 | 0.796 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#401 | ligne | category | id→id | wrong | no | 2 | 0.924 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.971 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business#451 | title | category | account→unknown | unknown | no | 2 | 0.470 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business#459 | australian sourced goods | amount | quantity→quantity | wrong | yes | 2 | 0.918 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#460 | australian sourced services | amount | amount→unknown | unknown | no | 1 | 0.505 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business#461 | overseas sourced goods | amount | quantity→quantity | wrong | yes | 2 | 0.764 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business#462 | overseas sourced services | amount | quantity→quantity | wrong | yes | 2 | 0.629 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#11 | merchant description | category | category→unknown | unknown | no | 1 | 0.470 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#45 | type | account | category→category | wrong | no | 2 | 0.945 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#75 | monitor | id | category→category | wrong | no | 3 | 0.568 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#163 | projection | category | category→unknown | unknown | no | 1 | 0.382 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#176 | contravention | category | text→text | wrong | no | 2 | 0.649 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#177 | fine | amount | quantity→quantity | wrong | yes | >3 | 0.819 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | business2#230 | warddesc | address | address→unknown | unknown | no | 1 | 0.412 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#238 | terrace | quantity | other→unknown | unknown | no | 2 | 0.601 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business2#291 | epc_score_known | category | quantity→quantity | wrong | no | 2 | 0.556 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#298 | number_habitable_rooms | quantity | quantity→unknown | unknown | no | 1 | 0.716 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.840 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#301 | total_floor_area_known | category | quantity→quantity | wrong | no | 3 | 0.609 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#322 | imd19_national_decile | category | id→id | wrong | no | 2 | 0.541 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#325 | loac_group | category | address→address | wrong | no | 3 | 0.940 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#326 | fuel_poverty | rate | other→unknown | unknown | no | 2 | 0.693 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 2 | business2#330 | conservation_area_site_id | category | id→id | wrong | no | 2 | 0.586 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#370 | average bids per property | other | amount→amount | other_ng | no | >3 | 0.750 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 2 | business2#379 | terrace | quantity | other→unknown | unknown | no | 3 | 0.861 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 2 | business2#381 | total_verified_sales | quantity | amount→amount | wrong | yes | 2 | 0.646 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#440 | situtation | address | text→text | wrong | no | 3 | 0.520 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.987 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.978 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#548 | health service executive area | address | org→org | wrong | no | 2 | 0.651 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.980 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.976 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.974 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.971 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.983 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.690 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#962 | service | account | org→org | wrong | no | 3 | 0.807 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 2 | business2#973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | amount→unknown | unknown | no | 1 | 0.520 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 2 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.987 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 2 | business2#975 | amt-units_mnt-unite | category | category→unknown | unknown | no | 1 | 0.417 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | dev220#49 | 税率 | rate | tax_class→tax_class | wrong | no | 2 | 0.560 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#130 | 随意契約理由 | text | category→category | wrong | no | 2 | 0.925 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#143 | terms | category | text→text | wrong | no | 2 | 0.820 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#171 | customer rank | quantity | category→category | wrong | no | 3 | 0.891 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | dev220#172 | supplier rank | quantity | category→category | wrong | no | >3 | 0.980 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | dev220#174 | sales order | id | date→unknown | unknown | no | 2 | 0.488 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | dev220#177 | purchase order by customer | id | quantity→quantity | wrong | yes | 2 | 0.731 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#189 | payment terms | category | text→text | wrong | no | 2 | 0.733 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | dev220#196 | credit limit | amount | quantity→quantity | wrong | yes | 2 | 0.619 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#1 | author | person | org→unknown | unknown | no | 2 | 0.496 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#27 | keyword | category | text→text | wrong | no | 2 | 0.655 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#32 | 五島 | other | quantity→quantity | other_ng | no | 3 | 0.976 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | general#35 | denominatorunweighted | quantity | other→unknown | unknown | no | 2 | 0.967 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#48 | source | category | org→unknown | unknown | no | 2 | 0.480 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#70 | lda | text | category→category | wrong | no | 2 | 0.589 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#75 | データセット_キーワード | category | text→text | wrong | no | 2 | 0.720 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#83 | place | org | address→address | wrong | no | 2 | 0.934 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#87 | sens_final | rate | other→unknown | unknown | no | 2 | 0.768 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#104 | term | text | category→category | wrong | no | 2 | 0.673 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#121 | dag-stage | other | category→category | other_ng | no | 3 | 0.585 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | general#134 | dbpedia_score | other | rate→rate | other_ng | no | 2 | 0.643 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#207 | year_step_size | quantity | category→category | wrong | no | 2 | 0.840 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#213 | age_q3_nd | quantity | rate→rate | wrong | yes | 2 | 0.533 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#224 | study | text | date→unknown | unknown | no | 2 | 0.242 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#227 | 発生日 | date | date→unknown | unknown | no | 1 | 0.986 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | general#234 | 発生県 | id | address→address | wrong | no | 2 | 0.910 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#275 | attrition | category | quantity→quantity | wrong | no | 2 | 0.817 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#282 | 読み方 | address | org→unknown | unknown | no | 2 | 0.367 | probability_below_threshold | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#286 | value | other | rate→rate | other_ng | no | 3 | 0.913 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | general#291 | cleaned | text | category→category | wrong | no | 2 | 0.893 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#296 | image_level_adj_acc | rate | other→unknown | unknown | no | 2 | 0.961 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#302 | episode | other | id→id | other_ng | no | >3 | 0.853 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#308 | ステーション名 | org | address→address | wrong | no | 2 | 0.669 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#309 | goal | id | quantity→quantity | wrong | yes | >3 | 0.505 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#338 | denominatorweighted | quantity | other→unknown | unknown | no | 3 | 0.987 | other_class | raw誤り＋見送り | 上位3候補内の境界 |
| 3 | general#340 | 登録年月日 | date | date→unknown | unknown | no | 1 | 0.987 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | general#343 | mt2 | other | quantity→quantity | other_ng | no | >3 | 0.504 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | general#377 | indicator | text | category→category | wrong | no | 2 | 0.913 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | general#380 | 科名 | category | other→unknown | unknown | no | 2 | 0.752 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | general#382 | source | category | text→text | wrong | no | 2 | 0.701 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#41 | total invoices paid | quantity | amount→amount | wrong | yes | 2 | 0.866 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#46 | quarterno | date | date→unknown | unknown | no | 1 | 0.979 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business#77 | publisher label | org | address→address | wrong | no | 2 | 0.544 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#84 | department | org | account→account | wrong | no | 2 | 0.944 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#101 | entitiy | org | account→account | wrong | no | 3 | 0.882 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business#112 | expense area | account | address→address | wrong | no | 3 | 0.588 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business#148 | merchant details | text | category→category | wrong | no | 2 | 0.602 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#199 | department | org | account→account | wrong | no | 2 | 0.968 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#215 | account_name | account | org→org | wrong | no | 2 | 0.814 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#225 | description | account | text→text | wrong | no | 2 | 0.517 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#237 | purposeofexpenditure | text | account→account | wrong | no | 2 | 0.835 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#278 | 目名 | category | other→unknown | unknown | no | 2 | 0.903 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business#279 | 科名 | category | other→unknown | unknown | no | 2 | 0.937 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business#334 | segment-title_fr | category | account→account | wrong | no | 2 | 0.601 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#342 | commodity-title_en | product | category→category | wrong | no | 2 | 0.563 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#344 | portefeuille_nom_et_code | org | account→account | wrong | no | 3 | 0.657 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business#347 | regrp_sommaire | account | category→category | wrong | no | 2 | 0.700 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#401 | ligne | category | id→id | wrong | no | 2 | 0.932 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#406 | mois calendrier | date | date→unknown | unknown | no | 1 | 0.944 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business#451 | title | category | account→account | wrong | no | 2 | 0.785 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#459 | australian sourced goods | amount | quantity→quantity | wrong | yes | 2 | 0.761 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business#461 | overseas sourced goods | amount | amount→unknown | unknown | no | 1 | 0.516 | numeric_top2_too_close | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business#462 | overseas sourced services | amount | quantity→unknown | unknown | no | 2 | 0.591 | numeric_top2_too_close | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#45 | type | account | category→category | wrong | no | 2 | 0.970 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#58 | numbers of | date | quantity→unknown | unknown | no | 2 | 0.825 | numeric_values_not_parseable | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#75 | monitor | id | category→category | wrong | no | 3 | 0.667 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business2#90 | total invoices paid | quantity | amount→amount | wrong | yes | 2 | 0.848 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#140 | surveyname | text | address→address | wrong | no | 2 | 0.517 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#149 | projection | category | id→id | wrong | no | 2 | 0.540 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#151 | habitatdescription | text | category→category | wrong | no | 2 | 0.636 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#154 | surveyname | text | address→address | wrong | no | 2 | 0.921 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#163 | projection | category | id→id | wrong | no | 2 | 0.624 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#177 | fine | amount | category→category | wrong | no | >3 | 0.510 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#230 | warddesc | address | category→category | wrong | no | 2 | 0.943 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#231 | propertytype | category | category→unknown | unknown | no | 1 | 0.464 | probability_below_threshold | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#238 | terrace | quantity | other→unknown | unknown | no | 2 | 0.906 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#291 | epc_score_known | category | other→unknown | unknown | no | >3 | 0.653 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#295 | potential_epc_score_known | category | other→unknown | unknown | no | 2 | 0.644 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#297 | potential_epc_rating_known | category | other→unknown | unknown | no | 2 | 0.587 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#298 | number_habitable_rooms | quantity | quantity→unknown | unknown | no | 1 | 0.933 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#299 | number_habitable_rooms_known | category | quantity→quantity | wrong | no | 2 | 0.964 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#301 | total_floor_area_known | category | other→unknown | unknown | no | >3 | 0.613 | other_class | raw誤り＋見送り | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#317 | energy_consumption | other | quantity→quantity | other_ng | no | 2 | 0.654 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#325 | loac_group | category | address→address | wrong | no | 2 | 0.946 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#326 | fuel_poverty | rate | category→category | wrong | no | >3 | 0.697 |  | rawモデル誤分類 | 入力文脈・教材分布・ラベル境界のいずれか |
| 3 | business2#330 | conservation_area_site_id | category | id→id | wrong | no | 2 | 0.848 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#370 | average bids per property | other | amount→amount | other_ng | no | 3 | 0.773 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business2#379 | terrace | quantity | other→unknown | unknown | no | 2 | 0.905 | other_class | raw誤り＋見送り | 上位2候補の境界・確信度 |
| 3 | business2#440 | situtation | address | text→text | wrong | no | 3 | 0.576 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business2#492 | value () | amount | amount→unknown | unknown | no | 1 | 0.988 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#542 | percentage (%) of the total amount paid | rate | rate→unknown | unknown | no | 1 | 0.970 | numeric_values_not_parseable | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#562 | name | org | address→address | wrong | no | 2 | 0.566 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#825 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.977 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#864 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.964 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#874 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.956 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#883 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.947 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#926 | tlist(q1) | date | date→unknown | unknown | no | 1 | 0.980 | date_value_evidence_low | guardが正解rawを変更 | guard/しきい値が過剰 |
| 3 | business2#946 | service_responsable | account | category→category | wrong | no | 2 | 0.884 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#948 | numéro_uev | id | address→address | wrong | no | 2 | 0.609 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
| 3 | business2#962 | service | account | org→org | wrong | no | 3 | 0.810 |  | rawモデル誤分類 | 上位3候補内の境界 |
| 3 | business2#974 | miscellaneous_divers | amount | quantity→quantity | wrong | yes | 2 | 0.979 |  | rawモデル誤分類 | 上位2候補の境界・確信度 |
