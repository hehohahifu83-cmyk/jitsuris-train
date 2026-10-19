# 保存済みcheckpointの誤り・unknown理由監査

対象はrun 39241962638のjob1 / seed 1。固定開発試験5種のみを使用し、列値は記録していない。各条件2,161行、合計4,322行（5試験×2条件）を集計した。

## 集計

| 条件 | wrong | unknown | critical numeric confusions |
|---|---:|---:|---:|
| ft | 64 | 44 | 6 |
| blend70 | 57 | 54 | 5 |

blend70はこの固定試験上でwrongが7件、重大誤りが1件少ない一方、unknownが10件多い。採用判断にはせず候補差として記録する。

## unknownの理由

| 理由 | ft | blend70 |
|---|---:|---:|
| other_class | 18 | 17 |
| date_value_evidence_low | 14 | 14 |
| probability_below_threshold | 7 | 16 |
| numeric_values_not_parseable | 5 | 5 |
| numeric_top2_too_close | 0 | 2 |

## blend70で残った重大誤り

| 試験 | 列名 | 正解 | 予測 | top-1確率 |
|---|---|---|---|---:|
| dev220 | purchase order by customer | id | quantity | 0.938361 |
| general | itemfield14 | date | id | 0.684574 |
| business2 | fine | amount | quantity | 0.728080 |
| business2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.849885 |
| business2 | miscellaneous_divers | amount | quantity | 0.992080 |

## 主な誤分類のまとまり

blend70ではcategory→idが7件、org→accountが5件、category→textが5件、quantity→categoryが5件、category→quantityが5件だった。amount→quantityは4件で、そのうち3件が重大誤りとして残った。

business / business2にはquestionnaire由来に見える短いコード列名や一般語の列名が含まれるが、今回の行別記録には出典・兄弟列・列値がない。したがって文脈不足、教材の分布差、ラベル疑義のいずれかを原因と断定できない。高確率の誤りも確認され、確信度だけで誤りを防げていない。

## 次の一手

重大誤り5件のラベルをLABEL_GUIDEと公開元の文脈に照らして点検する。ラベル疑義が残れば、二人の独立した教師役が確認して根拠を裁定するまで修正しない。今回は列値をartifactに含めていないため、この監査だけでラベルの正誤は確定しない。

出力: probs_*.json / errors_*.json（schema v3、decision_reason付き）。unknownは理由を記録。blind setとセット3・5・7は閲覧・評価に使っていない。
