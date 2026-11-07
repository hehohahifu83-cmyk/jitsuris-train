# W2 run 42323220255：許可5集合の全問題出力監査

作成：2026-11-07 Codex。禁止対象（blind_set*、sealed2/3、b018、セット3・5・7）は読んでいない。対象は repository に保存された `eval_reports/latest/job1〜6_probs_val_{pool,general,business,business2,japan_procurement}_{ft,blend70}.json` の60ファイルだけ。

## 実行と成果物（観測事実）

- GitHub Actions run 42323220255 は success（2026-11-07 10:17〜11:39 JST、head `113dcab2`）。
- 評価artifact `13557246189`（5,089,968 bytes、digest `sha256:3625f3…8467`、期限2026-12-07）とモデルartifact `13557211258`（879,625,432 bytes、digest `sha256:aae74a…57ba6`、期限2026-12-07）を別々に確認した。
- W2はe5-base、seed 1/2、教材庫割合1.0/0.5/0.25の6仕事。採否規則は事前固定され、全検証4,551列のmacro-F1差 1.0−0.5 が +0.81pp <1.0 のため「頭打ち」。

## 全60ファイルの再集計

- 総出力 65,280、OK 60,568（correct 58,038、other_ok 2,530）、問題出力 4,712（wrong 2,653、unknown 1,721、other見落し 338）、critical 234。
- 固有問題行 619（pool 533、general 34、business 16、business2 32、japan_procurement 4）。criticalを1回以上含む固有行 48。
- 再発：12/12出力で問題 233行。発生回数分布：1回=61、2回=72、3回=28、4回=44、5回=30、6回=24、7回=21、8回=29、9回=19、10回=31、11回=27、12回=233。

### guard／rawの即時機構

|機構|出力数|観測の意味|
|---|---:|---|
|raw正解→guard unknown|1184|guardが正解候補を保留へ変更|
|raw正解→guard別誤答|0|guardが正解を別ラベルへ変更|
|raw誤答→guard unknown|537|誤答を安全側へ退避|
|raw誤答をwrongとして受理|2653|モデルまたは後処理後も誤答|
|other見落し|338|truth=otherを別ラベルで受理|
|低信頼閾値によるunknown|465|probability_below_threshold|

## 仕事別・集合別（全件）

|job|割合|seed|集合|条件|n|accuracy|wrong|unknown|other見落し|critical|
|---:|---:|---:|---|---|---:|---:|---:|---:|---:|---:|
|1|1.0|1|pool|ft|4551|93.58%|185|96|11|14|
|1|1.0|1|pool|blend70|4551|93.45%|176|111|11|13|
|1|1.0|1|general|ft|204|87.25%|15|2|9|1|
|1|1.0|1|general|blend70|204|88.73%|9|6|8|0|
|1|1.0|1|business|ft|204|95.59%|6|3|0|1|
|1|1.0|1|business|blend70|204|95.59%|6|3|0|0|
|1|1.0|1|business2|ft|415|93.98%|3|9|13|0|
|1|1.0|1|business2|blend70|415|94.22%|2|10|12|0|
|1|1.0|1|japan_procurement|ft|66|96.97%|2|0|0|0|
|1|1.0|1|japan_procurement|blend70|66|96.97%|2|0|0|0|
|2|1.0|2|pool|ft|4551|93.19%|192|108|10|15|
|2|1.0|2|pool|blend70|4551|93.08%|179|127|9|15|
|2|1.0|2|general|ft|204|91.67%|9|3|5|0|
|2|1.0|2|general|blend70|204|91.67%|8|4|5|0|
|2|1.0|2|business|ft|204|96.08%|6|2|0|0|
|2|1.0|2|business|blend70|204|95.59%|6|3|0|0|
|2|1.0|2|business2|ft|415|94.22%|3|9|12|0|
|2|1.0|2|business2|blend70|415|94.22%|3|9|12|0|
|2|1.0|2|japan_procurement|ft|66|96.97%|2|0|0|0|
|2|1.0|2|japan_procurement|blend70|66|98.48%|0|1|0|0|
|3|0.5|1|pool|ft|4551|92.81%|202|115|10|21|
|3|0.5|1|pool|blend70|4551|92.49%|191|142|9|22|
|3|0.5|1|general|ft|204|89.22%|14|2|6|0|
|3|0.5|1|general|blend70|204|90.69%|12|2|5|0|
|3|0.5|1|business|ft|204|96.08%|5|3|0|0|
|3|0.5|1|business|blend70|204|95.59%|5|4|0|0|
|3|0.5|1|business2|ft|415|93.25%|5|9|14|0|
|3|0.5|1|business2|blend70|415|93.98%|4|8|13|0|
|3|0.5|1|japan_procurement|ft|66|96.97%|2|0|0|0|
|3|0.5|1|japan_procurement|blend70|66|98.48%|1|0|0|0|
|4|0.5|2|pool|ft|4551|92.70%|205|118|9|19|
|4|0.5|2|pool|blend70|4551|92.38%|191|149|7|16|
|4|0.5|2|general|ft|204|89.22%|12|5|5|0|
|4|0.5|2|general|blend70|204|90.69%|9|6|4|0|
|4|0.5|2|business|ft|204|96.08%|6|2|0|2|
|4|0.5|2|business|blend70|204|95.10%|5|5|0|0|
|4|0.5|2|business2|ft|415|93.98%|4|8|13|0|
|4|0.5|2|business2|blend70|415|93.98%|4|9|12|0|
|4|0.5|2|japan_procurement|ft|66|98.48%|1|0|0|0|
|4|0.5|2|japan_procurement|blend70|66|98.48%|1|0|0|0|
|5|0.25|1|pool|ft|4551|92.27%|221|119|12|23|
|5|0.25|1|pool|blend70|4551|91.78%|207|157|10|17|
|5|0.25|1|general|ft|204|88.24%|14|5|5|0|
|5|0.25|1|general|blend70|204|89.71%|11|5|5|0|
|5|0.25|1|business|ft|204|93.63%|10|3|0|3|
|5|0.25|1|business|blend70|204|94.12%|6|6|0|2|
|5|0.25|1|business2|ft|415|93.98%|4|8|13|0|
|5|0.25|1|business2|blend70|415|93.98%|4|8|13|0|
|5|0.25|1|japan_procurement|ft|66|95.45%|2|1|0|0|
|5|0.25|1|japan_procurement|blend70|66|98.48%|1|0|0|0|
|6|0.25|2|pool|ft|4551|92.05%|221|129|12|25|
|6|0.25|2|pool|blend70|4551|91.83%|208|153|11|22|
|6|0.25|2|general|ft|204|88.73%|15|5|3|1|
|6|0.25|2|general|blend70|204|90.20%|12|4|4|0|
|6|0.25|2|business|ft|204|95.10%|6|4|0|1|
|6|0.25|2|business|blend70|204|95.59%|5|4|0|1|
|6|0.25|2|business2|ft|415|93.73%|5|8|13|0|
|6|0.25|2|business2|blend70|415|93.49%|5|9|13|0|
|6|0.25|2|japan_procurement|ft|66|96.97%|2|0|0|0|
|6|0.25|2|japan_procurement|blend70|66|98.48%|1|0|0|0|

## 学習時間・GPU・切詰め

|job|割合|seed|学習行|loop秒|total秒|評価秒|peak GPU GiB|train切詰め|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1|1.0|1|139579|1688.4|1717.8|62.3|5.48|867 (0.62%)|
|2|1.0|2|139579|1537.2|1566.7|58.2|5.55|867 (0.62%)|
|3|0.5|1|94978|1049.8|1069.8|53.5|5.46|737 (0.78%)|
|4|0.5|2|94978|1158.5|1175.3|61.6|5.46|737 (0.78%)|
|5|0.25|1|72643|801.5|814.6|54.2|5.45|664 (0.91%)|
|6|0.25|2|72643|884.6|898.1|63.1|5.46|664 (0.91%)|

同一評価入力のtoken切詰め：教材庫143/4551（3.14%）、general 2/204（0.98%）、business 0/204、business2 10/415（2.41%）、japan_procurement 11/66（16.67%）。切詰めと個別誤りの直接因果はartifactだけでは未確定。

## 原因の確定範囲

### 観測事実（高確度）

- W2で1.0割合・ft・両seedとも誤った未知見出し136行は別途全件診断済み。主分類はラベル/規定境界34、入力の手がかり不足仮説15、教材不足を主因として確定0、正しいrawをguardが拒否37、モデル意味誤り等50。
- date 28行は両seedともraw=dateから `date_value_evidence_low` でunknown。Claude独立30行との主分類一致は24/30。guardへ見出しを渡す直しGの再適用では31出力がunknown→correct、新規誤り0。ただしv10再現不一致11/13行の原因は未確認。
- 12/12出力で問題の固有行は233。割合・seed・ft/blend70を変えても残るため、系統的な失敗である。

### 仮説（未確定）

- 12/12再発行はラベル定義、入力表現、guard規則、学習全体の共通偏りの候補。ただしartifactには元値、UNIT、兄弟列、出典、token化後の実入力が全行分そろわず、根本原因の断定はできない。
- japan_procurementはtoken切詰め率16.67%で他集合より高いが、誤り原因との対応は未検証。
- 教材量は全体macro-F1で+0.81ppに留まる一方、同一の未知見出し1,121列では正しい率83.36→83.99→85.33%。「改善は既知見出しだけ」は棄却されたが、量だけで目標へ届くとは言えない。

## 次の一要因

|優先|検証|期待効果|副作用・停止条件|
|---|---|---|---|
|P0|残る6種の日付形を教材学習側でdate/非dateの列数・表数だけ集計|guard拡張候補を安全に限定|amount/quantity/id/category混同が多ければ規則追加しない|
|P0|v10再現不一致11/13行の入力選択差を特定|直しG効果の再現性確保|原因不明のままguard採用しない|
|P1|ラベル境界34行を先生2人が独立確認し根拠裁定|誤ラベルと真のモデル誤りを分離|裁定前に教材ラベル変更しない|
|P1|12/12再発行を表文脈付きで層別|系統的失敗を分解|固定評価例を教材へ転用しない|
|P2|token切詰めと誤りの対応を保存入力で比較|文脈欠落の因果切分け|max_length変更と他要因を同時変更しない|

## 全問題行（固有619行）

各行は60ファイルのうち問題になった回数を集約。variantは `raw→final(reason)×回数`。値は保存しない。

|集合|index|列|正解|発生/12|critical|outcome内訳|variant|
|---|---:|---|---|---:|---:|---|---|
|pool|58|データセット_タイトル|text|2|0|wrong:2|raw=address→final=address×2|
|pool|65|旧番号|address|10|0|wrong:10|raw=id→final=id×10|
|pool|81|タグ|category|12|0|wrong:12|raw=text→final=text×12|
|pool|88|提供エリア|address|7|0|wrong:7|raw=text→final=text×7|
|pool|98|名称|org|2|0|wrong:2|raw=address→final=address×2|
|pool|116|名称_通称|org|1|0|wrong:1|raw=address→final=address×1|
|pool|177|公営駐車場_名称|org|7|0|wrong:7|raw=address→final=address×7|
|pool|178|公営駐車場_名称(カナ)|org|3|0|wrong:3|raw=address→final=address×3|
|pool|188|名称_カナ|org|12|0|wrong:12|raw=address→final=address×12|
|pool|209|提供エリア|text|12|0|wrong:12|raw=address→final=address×10; raw=category→final=category×2|
|pool|223|名称_カナ|org|5|0|wrong:5|raw=address→final=address×5|
|pool|241|番|address|11|0|unknown:1,wrong:10|raw=id→final=id×10; raw=address→final=unknown(probability_below_threshold)×1|
|pool|242|都市高速|address|3|0|unknown:3|raw=address→final=unknown(probability_below_threshold)×3|
|pool|247|内容|category|11|0|wrong:11|raw=text→final=text×11|
|pool|248|日付|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|274|名称|org|3|0|wrong:3|raw=address→final=address×3|
|pool|276|名称_通称|org|2|0|wrong:2|raw=address→final=address×2|
|pool|282|名称|org|1|0|wrong:1|raw=address→final=address×1|
|pool|316|名称_カナ|org|2|0|wrong:2|raw=address→final=address×2|
|pool|317|名称_英語|org|5|0|wrong:5|raw=address→final=address×5|
|pool|331|施設名|org|1|0|wrong:1|raw=address→final=address×1|
|pool|353|名称|org|1|0|unknown:1|raw=address→final=unknown(probability_below_threshold)×1|
|pool|383|名称|org|1|0|wrong:1|raw=address→final=address×1|
|pool|384|名称_カナ|org|1|0|wrong:1|raw=address→final=address×1|
|pool|393|名称|org|6|0|unknown:1,wrong:5|raw=address→final=address×5; raw=org→final=unknown(probability_below_threshold)×1|
|pool|394|名称_カナ|org|2|0|wrong:2|raw=address→final=address×2|
|pool|403|名称_カナ|address|12|0|unknown:2,wrong:10|raw=org→final=org×10; raw=address→final=unknown(probability_below_threshold)×2|
|pool|404|名称_通称|address|1|0|unknown:1|raw=address→final=unknown(probability_below_threshold)×1|
|pool|421|団体名|org|12|0|wrong:12|raw=address→final=address×12|
|pool|425|調査年月日|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|471|名称|org|4|0|wrong:4|raw=address→final=address×4|
|pool|521|調査年月日|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|550|名称|org|2|0|unknown:1,wrong:1|raw=address→final=address×1; raw=address→final=unknown(probability_below_threshold)×1|
|pool|647|よみがな|org|7|0|unknown:1,wrong:6|raw=address→final=address×6; raw=address→final=unknown(probability_below_threshold)×1|
|pool|661|名称|address|1|0|wrong:1|raw=org→final=org×1|
|pool|662|名称_カナ|org|12|0|wrong:12|raw=address→final=address×12|
|pool|697|line|category|2|0|unknown:2|raw=category→final=unknown(probability_below_threshold)×2|
|pool|704|location suffix|address|1|0|unknown:1|raw=category→final=unknown(probability_below_threshold)×1|
|pool|768|節名称|account|2|0|wrong:2|raw=text→final=text×2|
|pool|776|アクセス方法|text|9|0|unknown:1,wrong:8|raw=address→final=address×8; raw=text→final=unknown(probability_below_threshold)×1|
|pool|779|月|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|780|日|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|784|名称|org|7|0|wrong:7|raw=address→final=address×7|
|pool|785|名称_カナ|org|1|0|wrong:1|raw=address→final=address×1|
|pool|796|名称|org|1|0|wrong:1|raw=address→final=address×1|
|pool|797|名称_カナ|org|9|0|wrong:9|raw=address→final=address×9|
|pool|817|タグ|text|5|0|unknown:1,wrong:4|raw=category→final=category×4; raw=category→final=unknown(probability_below_threshold)×1|
|pool|819|開催パターン|text|4|0|wrong:4|raw=category→final=category×4|
|pool|864|備考|category|4|0|wrong:4|raw=text→final=text×4|
|pool|874|名称_カナ|org|1|0|wrong:1|raw=address→final=address×1|
|pool|877|提供エリア|address|9|0|unknown:3,wrong:6|raw=category→final=category×6; raw=address→final=unknown(probability_below_threshold)×2; raw=category→final=unknown(probability_below_threshold)×1|
|pool|925|sales|amount|12|12|wrong:12|raw=quantity→final=quantity×12|
|pool|954|材料名|product|1|0|unknown:1|raw=product→final=unknown(probability_below_threshold)×1|
|pool|955|分量(g)|quantity|1|0|unknown:1|raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|960|管理|org|12|0|unknown:6,wrong:6|raw=address→final=address×6; raw=account→final=unknown(probability_below_threshold)×2; raw=address→final=unknown(probability_below_threshold)×2; raw=category→final=unknown(probability_below_threshold)×2|
|pool|1009|名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|1010|名称_カナ|address|12|0|wrong:12|raw=org→final=org×12|
|pool|1011|名称_英字|address|12|0|wrong:12|raw=org→final=org×12|
|pool|1055|利用可能曜日|category|1|0|wrong:1|raw=text→final=text×1|
|pool|1059|調査区分コード|category|8|0|wrong:8|raw=id→final=id×8|
|pool|1077|名称|address|7|0|unknown:2,wrong:5|raw=org→final=org×5; raw=address→final=unknown(probability_below_threshold)×2|
|pool|1078|名称_カナ|address|10|0|wrong:10|raw=org→final=org×10|
|pool|1114|名称|org|1|0|unknown:1|raw=org→final=unknown(probability_below_threshold)×1|
|pool|1149|定員|quantity|12|0|unknown:12|raw=quantity→final=unknown(numeric_values_not_parseable)×12|
|pool|1164|名称|id|12|0|wrong:12|raw=org→final=org×8; raw=address→final=address×4|
|pool|1165|名称_カナ|id|12|0|wrong:12|raw=org→final=org×11; raw=address→final=address×1|
|pool|1166|名称_英語|id|12|0|wrong:12|raw=org→final=org×9; raw=address→final=address×3|
|pool|1176|名称_英語|org|10|0|wrong:10|raw=address→final=address×10|
|pool|1177|設置者|org|12|0|wrong:12|raw=address→final=address×12|
|pool|1186|名称|org|2|0|wrong:2|raw=address→final=address×2|
|pool|1189|説明|text|1|0|unknown:1|raw=text→final=unknown(probability_below_threshold)×1|
|pool|1199|department|account|10|0|wrong:10|raw=org→final=org×10|
|pool|1204|fund|account|8|0|unknown:2,wrong:6|raw=category→final=category×6; raw=category→final=unknown(probability_below_threshold)×2|
|pool|1223|ポリオ|quantity|12|1|unknown:8,wrong:4|raw=quantity→final=unknown(numeric_values_not_parseable)×4; raw=category→final=category×3; raw=category→final=unknown(probability_below_threshold)×1; raw=id→final=id×1; raw=id→final=unknown(numeric_top2_too_close)×1; raw=other→final=unknown(other_class)×1; raw=other→final=unknown(probability_below_threshold)×1|
|pool|1225|五種混合|quantity|12|0|unknown:12|raw=quantity→final=unknown(numeric_values_not_parseable)×12|
|pool|1228|mr|quantity|4|0|unknown:4|raw=quantity→final=unknown(numeric_top2_too_close)×2; raw=id→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|1230|bcg|quantity|8|2|unknown:6,wrong:2|raw=quantity→final=unknown(probability_below_threshold)×3; raw=id→final=id×2; raw=id→final=unknown(probability_below_threshold)×2; raw=other→final=unknown(other_class)×1|
|pool|1281|団体名|address|2|0|wrong:2|raw=org→final=org×2|
|pool|1294|名称|org|1|0|wrong:1|raw=address→final=address×1|
|pool|1309|700万円以上800万円未満|quantity|2|1|unknown:1,wrong:1|raw=rate→final=rate×1; raw=rate→final=unknown(probability_below_threshold)×1|
|pool|1314|fixedid|id|4|2|unknown:2,wrong:2|raw=quantity→final=quantity×2; raw=id→final=unknown(numeric_top2_too_close)×1; raw=quantity→final=unknown(numeric_top2_too_close)×1|
|pool|1327|分団名|account|12|0|unknown:10,wrong:2|raw=category→final=unknown(probability_below_threshold)×5; raw=address→final=unknown(probability_below_threshold)×4; raw=address→final=address×1; raw=category→final=category×1; raw=id→final=unknown(probability_below_threshold)×1|
|pool|1336|備考|category|3|0|wrong:3|raw=text→final=text×3|
|pool|1385|方書|address|5|0|wrong:5|raw=org→final=org×5|
|pool|1388|団体名|address|9|0|unknown:1,wrong:8|raw=org→final=org×8; raw=address→final=unknown(probability_below_threshold)×1|
|pool|1390|ward|id|11|0|unknown:2,wrong:9|raw=category→final=category×9; raw=id→final=unknown(probability_below_threshold)×2|
|pool|1391|precinct|id|2|0|unknown:1,wrong:1|raw=address→final=address×1; raw=address→final=unknown(probability_below_threshold)×1|
|pool|1392|metro council|id|12|12|wrong:12|raw=quantity→final=quantity×12|
|pool|1393|us house|id|12|12|wrong:12|raw=quantity→final=quantity×12|
|pool|1394|psc|id|12|5|unknown:1,wrong:11|raw=category→final=category×6; raw=quantity→final=quantity×5; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|1395|bese|id|12|5|unknown:7,wrong:5|raw=amount→final=amount×3; raw=other→final=unknown(other_class)×3; raw=quantity→final=quantity×2; raw=quantity→final=unknown(probability_below_threshold)×2; raw=amount→final=unknown(probability_below_threshold)×1; raw=other→final=unknown(probability_below_threshold)×1|
|pool|1396|la house|id|12|12|wrong:12|raw=quantity→final=quantity×12|
|pool|1397|la senate|id|12|12|wrong:12|raw=quantity→final=quantity×12|
|pool|1407|ticket sales|amount|12|12|wrong:12|raw=quantity→final=quantity×12|
|pool|1409|retailer commissions|amount|12|12|wrong:12|raw=quantity→final=quantity×12|
|pool|1427|qtd_tr_c_foco|quantity|4|1|unknown:3,wrong:1|raw=quantity→final=unknown(probability_below_threshold)×2; raw=rate→final=rate×1; raw=rate→final=unknown(probability_below_threshold)×1|
|pool|1428|qtd_tr_s_foco|quantity|4|0|unknown:4|raw=quantity→final=unknown(probability_below_threshold)×3; raw=other→final=unknown(probability_below_threshold)×1|
|pool|1431|contratado|org|6|0|unknown:2,wrong:4|raw=category→final=category×4; raw=org→final=unknown(probability_below_threshold)×2|
|pool|1432|objeto|text|7|0|unknown:6,wrong:1|raw=text→final=unknown(probability_below_threshold)×5; raw=product→final=product×1; raw=product→final=unknown(probability_below_threshold)×1|
|pool|1439|realizado|amount|4|2|unknown:2,wrong:2|raw=quantity→final=quantity×2; raw=amount→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|1452|numero|address|8|0|wrong:8|raw=id→final=id×8|
|pool|1465|data_referencia|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|1471|case_title|category|11|0|unknown:2,wrong:9|raw=text→final=text×9; raw=category→final=unknown(probability_below_threshold)×1; raw=text→final=unknown(probability_below_threshold)×1|
|pool|1472|subject|org|10|0|unknown:3,wrong:7|raw=account→final=account×7; raw=account→final=unknown(probability_below_threshold)×3|
|pool|1475|queue|account|2|0|unknown:1,wrong:1|raw=category→final=category×1; raw=category→final=unknown(probability_below_threshold)×1|
|pool|1476|department|account|4|0|unknown:1,wrong:3|raw=org→final=org×3; raw=org→final=unknown(probability_below_threshold)×1|
|pool|1480|state|address|2|0|wrong:2|raw=category→final=category×2|
|pool|1484|vehicle_model|product|10|0|unknown:2,wrong:8|raw=id→final=id×8; raw=product→final=unknown(probability_below_threshold)×2|
|pool|1497|reported enclosed parking area (sq ft)|other|5|0|other_ng:5|raw=quantity→final=quantity×5|
|pool|1499|all property types and gfas|text|12|0|wrong:12|raw=category→final=category×12|
|pool|1502|total site energy usage (kbtu)|quantity|5|0|unknown:5|raw=quantity→final=unknown(probability_below_threshold)×5|
|pool|1503|natural gas usage (kbtu)|quantity|5|0|unknown:5|raw=other→final=unknown(other_class)×2; raw=quantity→final=unknown(probability_below_threshold)×2; raw=other→final=unknown(probability_below_threshold)×1|
|pool|1509|census tract|id|8|4|unknown:4,wrong:4|raw=quantity→final=quantity×4; raw=id→final=unknown(numeric_top2_too_close)×2; raw=quantity→final=unknown(numeric_top2_too_close)×2|
|pool|1511|dri_amenities score|rate|7|0|unknown:7|raw=other→final=unknown(other_class)×7|
|pool|1512|区分|category|9|0|unknown:1,wrong:8|raw=address→final=address×8; raw=address→final=unknown(probability_below_threshold)×1|
|pool|1522|区 分|category|1|0|unknown:1|raw=category→final=unknown(probability_below_threshold)×1|
|pool|1528|実施機関名|org|5|0|unknown:4,wrong:1|raw=account→final=unknown(probability_below_threshold)×2; raw=org→final=unknown(probability_below_threshold)×2; raw=account→final=account×1|
|pool|1532|非公開|quantity|2|0|unknown:2|raw=quantity→final=unknown(probability_below_threshold)×2|
|pool|1533|取下げ|quantity|8|4|unknown:4,wrong:4|raw=rate→final=rate×4; raw=rate→final=unknown(probability_below_threshold)×2; raw=quantity→final=unknown(numeric_top2_too_close)×1; raw=rate→final=unknown(numeric_top2_too_close)×1|
|pool|1534|公開請求|quantity|1|0|unknown:1|raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|1535|順位|category|8|0|unknown:5,wrong:3|raw=id→final=id×3; raw=id→final=unknown(probability_below_threshold)×3; raw=quantity→final=unknown(numeric_top2_too_close)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|1537|内apiによるもの|quantity|10|0|unknown:10|raw=other→final=unknown(other_class)×9; raw=other→final=unknown(probability_below_threshold)×1|
|pool|1541|リソース名|other|7|0|other_ng:7|raw=id→final=id×7|
|pool|1547|町内会等 資源回収量 b|quantity|1|0|unknown:1|raw=quantity→final=unknown(numeric_top2_too_close)×1|
|pool|1561|団体名|address|1|0|wrong:1|raw=org→final=org×1|
|pool|1563|事業名|category|2|0|wrong:2|raw=text→final=text×2|
|pool|1575|名称|org|6|0|wrong:6|raw=address→final=address×6|
|pool|1576|名称_カナ|org|8|0|wrong:8|raw=address→final=address×8|
|pool|1577|名称_英語|org|1|0|wrong:1|raw=address→final=address×1|
|pool|1610|名称|address|8|0|wrong:8|raw=org→final=org×8|
|pool|1611|名称_カナ|address|9|0|unknown:1,wrong:8|raw=org→final=org×8; raw=address→final=unknown(probability_below_threshold)×1|
|pool|1661|exp_onda|other|4|0|other_ng:4|raw=amount→final=amount×4|
|pool|1663|vul_inun|other|2|0|other_ng:2|raw=rate→final=rate×2|
|pool|1667|avg. time on page|quantity|12|9|unknown:3,wrong:9|raw=date→final=date×9; raw=quantity→final=unknown(numeric_values_not_parseable)×2; raw=date→final=unknown(probability_below_threshold)×1|
|pool|1672|total_demand_kw|other|12|0|other_ng:12|raw=quantity→final=quantity×12|
|pool|1676|名称_カナ|org|1|0|wrong:1|raw=address→final=address×1|
|pool|1700|性別コード|category|10|0|wrong:10|raw=id→final=id×10|
|pool|1705|65~74歳人口(万人)|quantity|3|0|unknown:3|raw=quantity→final=unknown(numeric_top2_too_close)×2; raw=rate→final=unknown(probability_below_threshold)×1|
|pool|1710|建築物の名称|org|12|0|unknown:2,wrong:10|raw=address→final=address×6; raw=text→final=text×4; raw=address→final=unknown(probability_below_threshold)×2|
|pool|1722|month|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|1723|day|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|1728|年度|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|1803|名称|address|2|0|wrong:2|raw=org→final=org×2|
|pool|1816|名称|address|1|0|unknown:1|raw=address→final=unknown(probability_below_threshold)×1|
|pool|1843|誤|text|10|0|unknown:2,wrong:8|raw=category→final=category×8; raw=category→final=unknown(probability_below_threshold)×1; raw=text→final=unknown(probability_below_threshold)×1|
|pool|1844|正|text|12|0|unknown:2,wrong:10|raw=category→final=category×10; raw=rate→final=unknown(numeric_values_not_parseable)×2|
|pool|1857|利用施設|address|4|0|unknown:1,wrong:3|raw=category→final=category×2; raw=id→final=id×1; raw=id→final=unknown(probability_below_threshold)×1|
|pool|1858|開催時間 開催時間が毎日異なる場合|date|12|0|unknown:8,wrong:4|raw=date→final=unknown(date_value_evidence_low)×8; raw=text→final=text×4|
|pool|1875|名称|address|2|0|wrong:2|raw=org→final=org×2|
|pool|1876|名称_カナ|address|8|0|unknown:1,wrong:7|raw=org→final=org×7; raw=address→final=unknown(probability_below_threshold)×1|
|pool|1877|名称_英字|address|2|0|wrong:2|raw=org→final=org×2|
|pool|1878|名称_通称|address|1|0|unknown:1|raw=org→final=unknown(probability_below_threshold)×1|
|pool|1925|what sectors or industries use, or can use the facility|text|10|0|wrong:10|raw=category→final=category×10|
|pool|1926|case studies of business use or commercial application resul|text|2|0|wrong:2|raw=org→final=org×2|
|pool|1938|a_road_type|address|12|0|wrong:12|raw=category→final=category×12|
|pool|1939|a_road_suffix|address|12|0|wrong:12|raw=category→final=category×12|
|pool|1940|b_road_type|address|12|0|wrong:12|raw=category→final=category×12|
|pool|1941|b_road_suffix|address|12|0|wrong:12|raw=category→final=category×12|
|pool|1944|title|text|5|0|unknown:5|raw=other→final=unknown(other_class)×2; raw=text→final=unknown(probability_below_threshold)×2; raw=other→final=unknown(probability_below_threshold)×1|
|pool|1955|jurisdiction|address|1|0|unknown:1|raw=address→final=unknown(probability_below_threshold)×1|
|pool|1961|publication|date|4|0|unknown:4|raw=date→final=unknown(date_value_evidence_low)×4|
|pool|1962|topical|text|11|0|unknown:2,wrong:9|raw=category→final=category×9; raw=category→final=unknown(probability_below_threshold)×2|
|pool|1986|dublin area codes|address|2|0|unknown:1,wrong:1|raw=id→final=id×1; raw=id→final=unknown(probability_below_threshold)×1|
|pool|1992|mainstream_sna_allocation__26_27|quantity|12|4|unknown:8,wrong:4|raw=amount→final=unknown(probability_below_threshold)×4; raw=amount→final=amount×3; raw=rate→final=unknown(probability_below_threshold)×3; raw=amount→final=unknown(numeric_top2_too_close)×1; raw=rate→final=rate×1|
|pool|1993|special_class_snas__26_27|quantity|12|7|unknown:5,wrong:7|raw=rate→final=rate×7; raw=other→final=unknown(other_class)×2; raw=rate→final=unknown(probability_below_threshold)×2; raw=other→final=unknown(probability_below_threshold)×1|
|pool|1994|total_sna_allocation_26_27|quantity|11|10|unknown:1,wrong:10|raw=amount→final=amount×10; raw=quantity→final=unknown(numeric_top2_too_close)×1|
|pool|2009|分類コード|category|10|0|wrong:10|raw=id→final=id×10|
|pool|2010|用途分類|category|5|0|unknown:1,wrong:4|raw=account→final=account×4; raw=account→final=unknown(probability_below_threshold)×1|
|pool|2013|area_sub_bacia|other|2|0|other_ng:2|raw=rate→final=rate×2|
|pool|2015|densidade_sub_bacia|other|5|0|other_ng:5|raw=rate→final=rate×4; raw=quantity→final=quantity×1|
|pool|2018|ice_sub_bacia|rate|2|0|unknown:2|raw=other→final=unknown(other_class)×1; raw=rate→final=unknown(probability_below_threshold)×1|
|pool|2028|dateid|date|12|1|unknown:11,wrong:1|raw=date→final=unknown(date_value_evidence_low)×11; raw=id→final=id×1|
|pool|2032|greenfieldgrowtharea|address|2|0|wrong:2|raw=category→final=category×2|
|pool|2034|netcompletion|quantity|8|0|wrong:8|raw=category→final=category×8|
|pool|2035|from|address|1|0|unknown:1|raw=person→final=unknown(probability_below_threshold)×1|
|pool|2043|count start|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2044|count end|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2073|waste_to_energy|quantity|10|0|unknown:10|raw=other→final=unknown(other_class)×8; raw=other→final=unknown(probability_below_threshold)×2|
|pool|2074|export_interstate|quantity|11|2|unknown:9,wrong:2|raw=other→final=unknown(other_class)×4; raw=other→final=unknown(probability_below_threshold)×3; raw=rate→final=rate×2; raw=quantity→final=unknown(probability_below_threshold)×1; raw=rate→final=unknown(probability_below_threshold)×1|
|pool|2075|export_international|quantity|8|5|unknown:3,wrong:5|raw=amount→final=amount×5; raw=amount→final=unknown(probability_below_threshold)×3|
|pool|2076|disposal|quantity|8|4|unknown:4,wrong:4|raw=amount→final=amount×4; raw=other→final=unknown(other_class)×2; raw=amount→final=unknown(probability_below_threshold)×1; raw=other→final=unknown(probability_below_threshold)×1|
|pool|2079|lbb reference|id|12|0|unknown:1,wrong:11|raw=address→final=address×6; raw=org→final=org×5; raw=org→final=unknown(probability_below_threshold)×1|
|pool|2110|2025-26 fy attendance|quantity|2|0|unknown:2|raw=amount→final=unknown(numeric_top2_too_close)×1; raw=quantity→final=unknown(numeric_top2_too_close)×1|
|pool|2114|title_en|org|9|0|unknown:1,wrong:8|raw=text→final=text×8; raw=text→final=unknown(probability_below_threshold)×1|
|pool|2116|short_form_en|org|6|0|wrong:6|raw=id→final=id×5; raw=category→final=category×1|
|pool|2117|short_form_fr|org|7|0|unknown:1,wrong:6|raw=category→final=category×6; raw=org→final=unknown(probability_below_threshold)×1|
|pool|2127|事項|category|11|0|wrong:11|raw=text→final=text×11|
|pool|2139|名称|address|1|0|wrong:1|raw=org→final=org×1|
|pool|2157|地物・地点_名称|address|2|0|unknown:1,wrong:1|raw=address→final=unknown(probability_below_threshold)×1; raw=org→final=org×1|
|pool|2167|年度|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2169|路線|category|4|0|unknown:3,wrong:1|raw=address→final=unknown(probability_below_threshold)×1; raw=category→final=unknown(probability_below_threshold)×1; raw=org→final=org×1; raw=org→final=unknown(probability_below_threshold)×1|
|pool|2170|駅名|address|8|0|wrong:8|raw=org→final=org×8|
|pool|2171|取りまとめ駅|org|4|0|wrong:4|raw=address→final=address×4|
|pool|2194|備考|text|6|0|unknown:6|raw=date→final=unknown(date_value_evidence_low)×5; raw=date→final=unknown(probability_below_threshold)×1|
|pool|2220|ssd_supplier_band1__m|amount|12|11|unknown:1,wrong:11|raw=rate→final=rate×10; raw=quantity→final=quantity×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|2221|ssd_supplier_hectolitres_band1|quantity|10|0|unknown:10|raw=other→final=unknown(other_class)×8; raw=other→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|2225|unpackaged_inventory_units|quantity|12|0|unknown:12|raw=quantity→final=unknown(numeric_values_not_parseable)×12|
|pool|2230|sales_non_medical_units|quantity|12|0|unknown:12|raw=quantity→final=unknown(numeric_values_not_parseable)×12|
|pool|2231|unpackaged_production_kg|quantity|12|0|unknown:12|raw=quantity→final=unknown(numeric_values_not_parseable)×12|
|pool|2232|unpackaged_inventory_kg|quantity|12|0|unknown:12|raw=quantity→final=unknown(numeric_values_not_parseable)×12|
|pool|2239|season start|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2240|season end|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×10; raw=quantity→final=unknown(numeric_top2_too_close)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|2253|cras|org|12|0|unknown:5,wrong:7|raw=category→final=category×6; raw=org→final=unknown(probability_below_threshold)×3; raw=address→final=address×1; raw=address→final=unknown(probability_below_threshold)×1; raw=text→final=unknown(probability_below_threshold)×1|
|pool|2255|mes_ano_referencia|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2271|名称|address|2|0|wrong:2|raw=org→final=org×2|
|pool|2295|名称|address|1|0|wrong:1|raw=org→final=org×1|
|pool|2351|purpose of engagement|text|7|0|unknown:4,wrong:3|raw=account→final=account×3; raw=account→final=unknown(probability_below_threshold)×3; raw=text→final=unknown(probability_below_threshold)×1|
|pool|2371|駅名|org|4|0|wrong:4|raw=address→final=address×4|
|pool|2373|一日平均降車人員|quantity|1|0|unknown:1|raw=other→final=unknown(other_class)×1|
|pool|2382|指定月|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2383|指定日|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2423|開催頻度|quantity|12|0|unknown:3,wrong:9|raw=category→final=category×9; raw=quantity→final=unknown(numeric_values_not_parseable)×2; raw=category→final=unknown(probability_below_threshold)×1|
|pool|2443|location|category|2|0|wrong:2|raw=address→final=address×2|
|pool|2465|agtrends_commodity|product|10|0|unknown:3,wrong:7|raw=category→final=category×7; raw=product→final=unknown(probability_below_threshold)×2; raw=category→final=unknown(probability_below_threshold)×1|
|pool|2469|vocs billion kg per year|quantity|12|0|unknown:12|raw=other→final=unknown(other_class)×12|
|pool|2474|originalphysicalmaterial|text|12|0|unknown:1,wrong:11|raw=category→final=category×11; raw=quantity→final=unknown(numeric_values_not_parseable)×1|
|pool|2475|subject:topical|text|9|0|wrong:9|raw=category→final=category×9|
|pool|2485|regional wmg|org|7|0|unknown:1,wrong:6|raw=address→final=address×6; raw=org→final=unknown(probability_below_threshold)×1|
|pool|2492|primary bin|category|7|0|unknown:2,wrong:5|raw=quantity→final=quantity×5; raw=category→final=unknown(probability_below_threshold)×2|
|pool|2505|t1benefitquarter|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×11; raw=date→final=unknown(probability_below_threshold)×1|
|pool|2509|t1gistotal|amount|12|6|unknown:6,wrong:6|raw=rate→final=rate×6; raw=quantity→final=unknown(probability_below_threshold)×2; raw=amount→final=unknown(probability_below_threshold)×1; raw=other→final=unknown(probability_below_threshold)×1; raw=rate→final=unknown(numeric_top2_too_close)×1; raw=rate→final=unknown(probability_below_threshold)×1|
|pool|2513|food_source_code|id|3|0|unknown:1,wrong:2|raw=category→final=category×2; raw=id→final=unknown(probability_below_threshold)×1|
|pool|2515|cnf_food_group_code|category|4|0|wrong:4|raw=id→final=id×4|
|pool|2536|アクセス|address|12|0|wrong:12|raw=text→final=text×12|
|pool|2544|航路route|address|2|0|wrong:2|raw=category→final=category×2|
|pool|2545|サービスひん度(月当り)frequencypermonth|quantity|5|0|unknown:5|raw=other→final=unknown(other_class)×2; raw=other→final=unknown(probability_below_threshold)×2; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|2552|地区名|address|1|0|wrong:1|raw=category→final=category×1|
|pool|2564|local hospital network identifier|id|4|1|unknown:3,wrong:1|raw=id→final=unknown(numeric_top2_too_close)×2; raw=quantity→final=quantity×1; raw=quantity→final=unknown(numeric_top2_too_close)×1|
|pool|2565|local hospital network|org|5|0|wrong:5|raw=address→final=address×5|
|pool|2566|asgc_ra|category|12|0|unknown:2,wrong:10|raw=quantity→final=quantity×10; raw=category→final=unknown(probability_below_threshold)×2|
|pool|2569|2012-13 peer group code|category|6|0|wrong:6|raw=id→final=id×6|
|pool|2578|public transport complaint response times|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2586|dataset formats|category|11|0|unknown:11|raw=other→final=unknown(other_class)×9; raw=category→final=unknown(probability_below_threshold)×1; raw=other→final=unknown(probability_below_threshold)×1|
|pool|2601|sole_parent|quantity|2|2|wrong:2|raw=rate→final=rate×2|
|pool|2610|declividade_minima|rate|7|0|unknown:7|raw=rate→final=unknown(probability_below_threshold)×3; raw=other→final=unknown(other_class)×2; raw=other→final=unknown(probability_below_threshold)×2|
|pool|2611|declividade_maxima|rate|6|0|unknown:6|raw=other→final=unknown(other_class)×5; raw=other→final=unknown(probability_below_threshold)×1|
|pool|2612|年次・月次|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2614|月|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2615|会計分類|account|10|0|wrong:10|raw=category→final=category×10|
|pool|2616|会計|account|7|0|wrong:7|raw=category→final=category×7|
|pool|2619|借入先|category|5|0|unknown:1,wrong:4|raw=org→final=org×4; raw=org→final=unknown(probability_below_threshold)×1|
|pool|2620|銘柄|id|2|0|unknown:1,wrong:1|raw=product→final=product×1; raw=product→final=unknown(probability_below_threshold)×1|
|pool|2622|事業名|account|1|0|wrong:1|raw=text→final=text×1|
|pool|2624|起債許可年度|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2629|月|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2630|戸籍謄抄本|quantity|2|1|unknown:1,wrong:1|raw=id→final=id×1; raw=quantity→final=unknown(numeric_top2_too_close)×1|
|pool|2637|名称|org|12|0|wrong:12|raw=address→final=address×12|
|pool|2638|名称_カナ|org|11|0|wrong:11|raw=address→final=address×11|
|pool|2685|watershed_bassinversant|id|12|3|wrong:12|raw=category→final=category×9; raw=quantity→final=quantity×3|
|pool|2687|month_mois|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2688|day_jour|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2690|numero_groupe_enregistrement|id|1|0|unknown:1|raw=id→final=unknown(probability_below_threshold)×1|
|pool|2691|nom_groupe_enregistrement|org|9|0|unknown:2,wrong:7|raw=address→final=address×7; raw=address→final=unknown(probability_below_threshold)×2|
|pool|2699|area|id|12|1|unknown:5,wrong:7|raw=category→final=category×6; raw=address→final=unknown(probability_below_threshold)×3; raw=category→final=unknown(probability_below_threshold)×2; raw=quantity→final=quantity×1|
|pool|2701|q2|category|2|0|unknown:1,wrong:1|raw=quantity→final=quantity×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|2704|q4m1|category|4|0|unknown:4|raw=category→final=unknown(probability_below_threshold)×3; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|2709|列1|org|12|0|wrong:12|raw=address→final=address×12|
|pool|2717|申請内容|category|4|0|wrong:4|raw=text→final=text×4|
|pool|2731|備考|category|3|0|wrong:3|raw=text→final=text×3|
|pool|2748|地区名|address|1|0|wrong:1|raw=category→final=category×1|
|pool|2766|tree maintenance|quantity|2|0|unknown:2|raw=category→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|2767|road defects|quantity|6|0|wrong:6|raw=category→final=category×6|
|pool|2768|grass cutting|quantity|6|0|unknown:1,wrong:5|raw=category→final=category×5; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|2771|valid to hour|date|12|2|unknown:10,wrong:2|raw=date→final=unknown(date_value_evidence_low)×10; raw=quantity→final=quantity×2|
|pool|2773|issued hour|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2775|gale warning|text|2|0|wrong:2|raw=category→final=category×2|
|pool|2777|time of meteorological situation|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2779|forecast for area 1|text|11|0|unknown:10,wrong:1|raw=category→final=unknown(probability_below_threshold)×5; raw=address→final=unknown(probability_below_threshold)×3; raw=text→final=unknown(probability_below_threshold)×2; raw=address→final=address×1|
|pool|2780|wind__area_1_|text|12|0|unknown:3,wrong:9|raw=category→final=category×9; raw=category→final=unknown(probability_below_threshold)×2; raw=text→final=unknown(probability_below_threshold)×1|
|pool|2800|arena|id|6|0|unknown:2,wrong:4|raw=category→final=category×4; raw=category→final=unknown(probability_below_threshold)×1; raw=id→final=unknown(probability_below_threshold)×1|
|pool|2801|sdt|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2802|edt|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2803|dt|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2808|centreice_etime|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2843|quantity|category|2|0|unknown:2|raw=category→final=unknown(probability_below_threshold)×2|
|pool|2844|2012-13 actual|quantity|4|1|unknown:3,wrong:1|raw=quantity→final=unknown(numeric_top2_too_close)×2; raw=amount→final=amount×1; raw=amount→final=unknown(numeric_top2_too_close)×1|
|pool|2845|2013-14 actual|quantity|5|1|unknown:4,wrong:1|raw=quantity→final=unknown(numeric_top2_too_close)×3; raw=amount→final=amount×1; raw=amount→final=unknown(numeric_top2_too_close)×1|
|pool|2846|2014-15 target|quantity|4|0|unknown:4|raw=amount→final=unknown(numeric_top2_too_close)×2; raw=quantity→final=unknown(numeric_top2_too_close)×2|
|pool|2847|2014-15 actual|quantity|4|0|unknown:4|raw=quantity→final=unknown(numeric_top2_too_close)×3; raw=amount→final=unknown(numeric_top2_too_close)×1|
|pool|2848|2015-16 actual|quantity|2|0|unknown:2|raw=amount→final=unknown(numeric_top2_too_close)×1; raw=quantity→final=unknown(numeric_top2_too_close)×1|
|pool|2849|2016-17 actual|quantity|2|0|unknown:2|raw=quantity→final=unknown(numeric_top2_too_close)×2|
|pool|2850|2017-18 actual|quantity|3|0|unknown:3|raw=quantity→final=unknown(numeric_top2_too_close)×3|
|pool|2851|2018-19 actual|quantity|4|1|unknown:3,wrong:1|raw=quantity→final=unknown(numeric_top2_too_close)×2; raw=amount→final=amount×1; raw=amount→final=unknown(numeric_top2_too_close)×1|
|pool|2870|quarter/trimestre|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2872|tld transit out/transport dehors (ugy)|other|7|0|other_ng:7|raw=quantity→final=quantity×6; raw=rate→final=rate×1|
|pool|2875|osl transit out/transport dehors (ugy)|other|4|0|other_ng:4|raw=quantity→final=quantity×4|
|pool|2878|location|address|6|0|unknown:4,wrong:2|raw=address→final=unknown(probability_below_threshold)×2; raw=category→final=category×2; raw=category→final=unknown(probability_below_threshold)×2|
|pool|2886|ampa_ug_l|other|2|0|other_ng:2|raw=quantity→final=quantity×2|
|pool|2889|algae_total_cells_ml|other|12|0|other_ng:12|raw=quantity→final=quantity×12|
|pool|2895|pax_annual|quantity|8|8|wrong:8|raw=amount→final=amount×8|
|pool|2896|addr1|address|12|0|wrong:12|raw=id→final=id×12|
|pool|2899|area_sq_m|other|3|0|other_ng:3|raw=id→final=id×3|
|pool|2901|rfos_sub_c|category|12|0|wrong:12|raw=address→final=address×12|
|pool|2902|maintained|org|12|0|wrong:12|raw=category→final=category×12|
|pool|2924|processor/manufacturer|category|2|0|wrong:2|raw=org→final=org×2|
|pool|2949|statistic|id|2|0|wrong:2|raw=category→final=category×2|
|pool|2964|centroid_x|other|12|0|other_ng:12|raw=id→final=id×12|
|pool|2965|centroid_y|other|12|0|other_ng:12|raw=id→final=id×12|
|pool|2967|id|category|11|0|unknown:1,wrong:10|raw=id→final=id×10; raw=category→final=unknown(probability_below_threshold)×1|
|pool|2972|trimestre fiscal|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|2975|total les societes de secours mutuels/iffs|org|6|0|unknown:2,wrong:4|raw=category→final=category×4; raw=category→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|2976|industry group|category|2|0|wrong:2|raw=org→final=org×2|
|pool|2978|return/releve|id|4|0|wrong:4|raw=category→final=category×4|
|pool|2982|aircraft|product|5|0|unknown:2,wrong:3|raw=id→final=id×3; raw=id→final=unknown(probability_below_threshold)×1; raw=product→final=unknown(probability_below_threshold)×1|
|pool|2995|lumquintile|category|6|0|unknown:3,wrong:3|raw=quantity→final=quantity×3; raw=quantity→final=unknown(probability_below_threshold)×2; raw=category→final=unknown(probability_below_threshold)×1|
|pool|2996|traindistthresh|category|7|0|unknown:3,wrong:4|raw=quantity→final=quantity×4; raw=category→final=unknown(probability_below_threshold)×1; raw=id→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|2997|trainpres|category|3|0|unknown:1,wrong:2|raw=quantity→final=quantity×2; raw=category→final=unknown(probability_below_threshold)×1|
|pool|2998|busdistthresh|category|10|0|unknown:5,wrong:5|raw=quantity→final=quantity×5; raw=quantity→final=unknown(probability_below_threshold)×3; raw=category→final=unknown(probability_below_threshold)×2|
|pool|2999|buspres|category|4|0|unknown:1,wrong:3|raw=quantity→final=quantity×3; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3000|accutdestpresquintile|category|4|0|unknown:4|raw=category→final=unknown(probability_below_threshold)×1; raw=other→final=unknown(other_class)×1; raw=other→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3002|cd_clr_bdy_veh_p|category|12|0|unknown:4,wrong:8|raw=id→final=id×8; raw=address→final=unknown(probability_below_threshold)×2; raw=id→final=unknown(probability_below_threshold)×2|
|pool|3031|clearance|other|4|0|other_ng:4|raw=quantity→final=quantity×4|
|pool|3036|reasons for accepting gift (what is the benefit to the queen|text|1|0|wrong:1|raw=category→final=category×1|
|pool|3046|call number|id|2|0|unknown:1,wrong:1|raw=phone→final=phone×1; raw=phone→final=unknown(probability_below_threshold)×1|
|pool|3049|collection|category|10|0|unknown:4,wrong:6|raw=org→final=org×4; raw=category→final=unknown(probability_below_threshold)×2; raw=text→final=text×2; raw=org→final=unknown(probability_below_threshold)×1; raw=text→final=unknown(probability_below_threshold)×1|
|pool|3050|statistic|id|12|0|wrong:12|raw=category→final=category×12|
|pool|3054|measure|id|12|0|wrong:12|raw=category→final=category×12|
|pool|3060|statistic|id|12|0|wrong:12|raw=category→final=category×12|
|pool|3064|measure|id|12|0|wrong:12|raw=category→final=category×12|
|pool|3070|statistic|id|10|0|wrong:10|raw=category→final=category×10|
|pool|3074|measure|id|12|0|wrong:12|raw=category→final=category×12|
|pool|3087|moist_pct|rate|8|0|unknown:8|raw=other→final=unknown(other_class)×8|
|pool|3091|fiscal period|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3095|service|category|9|0|wrong:9|raw=account→final=account×9|
|pool|3096|value|rate|12|12|wrong:12|raw=amount→final=amount×12|
|pool|3108|biomass|quantity|10|0|unknown:10|raw=other→final=unknown(other_class)×10|
|pool|3109|fossil fuels|quantity|8|0|unknown:8|raw=other→final=unknown(other_class)×4; raw=amount→final=unknown(probability_below_threshold)×2; raw=other→final=unknown(probability_below_threshold)×2|
|pool|3110|metal ores|quantity|10|0|unknown:10|raw=other→final=unknown(other_class)×9; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3111|non-metallic minerals|quantity|11|0|unknown:11|raw=other→final=unknown(other_class)×10; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3112|total (all categories)|quantity|8|2|unknown:6,wrong:2|raw=other→final=unknown(other_class)×3; raw=amount→final=amount×2; raw=other→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(numeric_top2_too_close)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3113|@caption|org|1|0|unknown:1|raw=org→final=unknown(probability_below_threshold)×1|
|pool|3117|area|other|2|0|other_ng:2|raw=address→final=address×2|
|pool|3124|statistic|id|12|0|wrong:12|raw=category→final=category×12|
|pool|3128|measure|id|11|0|unknown:1,wrong:10|raw=category→final=category×10; raw=id→final=unknown(probability_below_threshold)×1|
|pool|3136|tlist(q1)|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3143|wind_speed_km_h|other|9|0|other_ng:9|raw=category→final=category×9|
|pool|3147|nom du produit de formulation|product|4|0|unknown:4|raw=product→final=unknown(probability_below_threshold)×4|
|pool|3152|family_famille|category|12|0|unknown:12|raw=other→final=unknown(other_class)×12|
|pool|3155|traitvaluedescription_descriptionvaleurtrait|category|1|0|wrong:1|raw=text→final=text×1|
|pool|3172|粗暴犯のうち凶器準備集合|quantity|12|0|unknown:12|raw=quantity→final=unknown(numeric_values_not_parseable)×12|
|pool|3176|talkback-number|phone|6|0|wrong:6|raw=id→final=id×6|
|pool|3179|po-box|address|2|0|unknown:1,wrong:1|raw=id→final=id×1; raw=id→final=unknown(probability_below_threshold)×1|
|pool|3182|vehicle make|org|2|0|unknown:2|raw=org→final=unknown(probability_below_threshold)×2|
|pool|3184|vehicle number of cylinders|quantity|12|0|unknown:12|raw=quantity→final=unknown(numeric_values_not_parseable)×11; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3192|tariff|category|11|0|unknown:5,wrong:6|raw=org→final=org×3; raw=tax_class→final=tax_class×3; raw=category→final=unknown(probability_below_threshold)×2; raw=tax_class→final=unknown(probability_below_threshold)×2; raw=org→final=unknown(probability_below_threshold)×1|
|pool|3199|publication month|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3205|quarter|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3210|vrt_liability__m|amount|12|0|unknown:12|raw=other→final=unknown(other_class)×7; raw=other→final=unknown(probability_below_threshold)×5|
|pool|3215|sub_order|id|5|3|unknown:2,wrong:3|raw=quantity→final=quantity×3; raw=id→final=unknown(numeric_top2_too_close)×1; raw=quantity→final=unknown(numeric_top2_too_close)×1|
|pool|3217|x values|date|8|0|unknown:8|raw=date→final=unknown(date_value_evidence_low)×8|
|pool|3228|dataset title|text|2|0|wrong:2|raw=category→final=category×2|
|pool|3232|dataset formats|category|9|0|unknown:9|raw=other→final=unknown(other_class)×6; raw=other→final=unknown(probability_below_threshold)×2; raw=category→final=unknown(probability_below_threshold)×1|
|pool|3233|dataset title|text|2|0|unknown:1,wrong:1|raw=category→final=category×1; raw=text→final=unknown(probability_below_threshold)×1|
|pool|3238|department|org|12|0|wrong:12|raw=account→final=account×12|
|pool|3242|period|category|7|0|unknown:7|raw=category→final=unknown(probability_below_threshold)×4; raw=date→final=unknown(date_value_evidence_low)×2; raw=date→final=unknown(probability_below_threshold)×1|
|pool|3251|home library service|quantity|4|0|wrong:4|raw=category→final=category×4|
|pool|3253|period|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3262|post retirement benefit|quantity|5|0|unknown:5|raw=quantity→final=unknown(numeric_top2_too_close)×3; raw=amount→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3265|statistic|id|12|0|wrong:12|raw=category→final=category×12|
|pool|3269|measure|id|1|0|wrong:1|raw=category→final=category×1|
|pool|3276|区分レベル1|account|11|0|wrong:11|raw=category→final=category×11|
|pool|3277|区分レベル2|account|12|0|wrong:12|raw=category→final=category×12|
|pool|3278|区分レベル3|account|12|0|wrong:12|raw=category→final=category×12|
|pool|3279|区分レベル4|account|12|0|wrong:12|raw=category→final=category×12|
|pool|3280|区分レベル5|account|12|0|wrong:12|raw=category→final=category×12|
|pool|3287|市場名|org|10|0|wrong:10|raw=address→final=address×10|
|pool|3294|施設名|address|4|0|wrong:4|raw=org→final=org×4|
|pool|3299|指摘財産|quantity|4|0|unknown:4|raw=quantity→final=unknown(probability_below_threshold)×2; raw=amount→final=unknown(numeric_top2_too_close)×1; raw=amount→final=unknown(probability_below_threshold)×1|
|pool|3306|規模|text|10|0|unknown:2,wrong:8|raw=category→final=category×8; raw=category→final=unknown(probability_below_threshold)×2|
|pool|3307|対象|text|10|0|unknown:1,wrong:9|raw=category→final=category×9; raw=text→final=unknown(probability_below_threshold)×1|
|pool|3314|開始日|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3315|終了日|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3341|名称|org|11|0|wrong:11|raw=address→final=address×11|
|pool|3365|名称|org|11|0|wrong:11|raw=address→final=address×11|
|pool|3367|設置位置|address|1|0|unknown:1|raw=address→final=unknown(probability_below_threshold)×1|
|pool|3377|利用可能日時特記事項|category|12|0|unknown:1,wrong:11|raw=text→final=text×11; raw=text→final=unknown(probability_below_threshold)×1|
|pool|3378|organisation label|org|1|0|unknown:1|raw=org→final=unknown(probability_below_threshold)×1|
|pool|3404|gor code|id|3|0|wrong:3|raw=category→final=category×3|
|pool|3405|imd score|other|4|0|other_ng:4|raw=rate→final=rate×4|
|pool|3406|rank of imd score (where 1 is most deprived)|category|12|0|unknown:5,wrong:7|raw=quantity→final=quantity×6; raw=quantity→final=unknown(probability_below_threshold)×4; raw=id→final=id×1; raw=id→final=unknown(numeric_top2_too_close)×1|
|pool|3408|rank of income score (where 1 is most deprived)|category|11|0|unknown:6,wrong:5|raw=quantity→final=quantity×5; raw=quantity→final=unknown(probability_below_threshold)×5; raw=category→final=unknown(probability_below_threshold)×1|
|pool|3409|employment score|rate|1|0|unknown:1|raw=rate→final=unknown(probability_below_threshold)×1|
|pool|3410|rank of employment score (where 1 is most deprived)|category|11|0|unknown:4,wrong:7|raw=quantity→final=quantity×6; raw=other→final=unknown(probability_below_threshold)×2; raw=category→final=unknown(probability_below_threshold)×1; raw=rate→final=rate×1; raw=rate→final=unknown(probability_below_threshold)×1|
|pool|3417|payscale maximum (」)|amount|9|2|unknown:7,wrong:2|raw=quantity→final=unknown(probability_below_threshold)×3; raw=other→final=unknown(probability_below_threshold)×2; raw=quantity→final=quantity×2; raw=amount→final=unknown(probability_below_threshold)×1; raw=other→final=unknown(other_class)×1|
|pool|3455|capital revenue|category|5|0|wrong:5|raw=account→final=account×5|
|pool|3459|control budget code|category|12|0|unknown:5,wrong:7|raw=id→final=id×7; raw=id→final=unknown(probability_below_threshold)×4; raw=category→final=unknown(probability_below_threshold)×1|
|pool|3461|economic category code|id|3|0|unknown:1,wrong:2|raw=category→final=category×2; raw=category→final=unknown(probability_below_threshold)×1|
|pool|3462|economic budget code|category|3|0|unknown:1,wrong:2|raw=account→final=account×2; raw=account→final=unknown(probability_below_threshold)×1|
|pool|3463|pesa economic group code|account|12|0|wrong:12|raw=category→final=category×12|
|pool|3464|version|category|6|0|unknown:2,wrong:4|raw=id→final=id×4; raw=date→final=unknown(date_value_evidence_low)×1; raw=date→final=unknown(probability_below_threshold)×1|
|pool|3466|quarter|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3473|co-ordinate ref. system|category|1|0|wrong:1|raw=id→final=id×1|
|pool|3474|eastings|other|2|0|other_ng:2|raw=quantity→final=quantity×2|
|pool|3481|kt|address|3|0|unknown:2,wrong:1|raw=category→final=category×1; raw=category→final=unknown(probability_below_threshold)×1; raw=org→final=unknown(probability_below_threshold)×1|
|pool|3485|anzstand|quantity|3|1|unknown:2,wrong:1|raw=id→final=id×1; raw=id→final=unknown(probability_below_threshold)×1; raw=other→final=unknown(other_class)×1|
|pool|3486|kt_standort|address|6|0|wrong:6|raw=category→final=category×6|
|pool|3494|sessionssitzung_uhrzeit|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×11; raw=date→final=unknown(probability_below_threshold)×1|
|pool|3495|sessionssitzung_bezeichnung|category|5|0|unknown:4,wrong:1|raw=category→final=unknown(probability_below_threshold)×3; raw=text→final=text×1; raw=text→final=unknown(probability_below_threshold)×1|
|pool|3498|biomasse_kwh|quantity|3|0|unknown:3|raw=other→final=unknown(other_class)×2; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3499|wind_kwh|quantity|10|0|unknown:10|raw=other→final=unknown(other_class)×10|
|pool|3500|abfall_kwh|quantity|2|0|unknown:2|raw=other→final=unknown(other_class)×1; raw=other→final=unknown(probability_below_threshold)×1|
|pool|3501|trinkwasserkraftwerk_kwh|quantity|2|0|unknown:2|raw=other→final=unknown(other_class)×2|
|pool|3502|klein_wasserkraftwerk_kwh|quantity|3|0|unknown:3|raw=other→final=unknown(other_class)×2; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3503|photovoltaik_kwh|quantity|4|0|unknown:4|raw=other→final=unknown(other_class)×3; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3504|wasserkraft_kwh|quantity|5|0|unknown:5|raw=other→final=unknown(other_class)×3; raw=other→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3513|library_call_number|id|12|0|unknown:3,wrong:9|raw=address→final=address×9; raw=address→final=unknown(probability_below_threshold)×3|
|pool|3517|date_of_publication_or_production|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3518|date_of_publication_or_production_standardised|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3519|series|text|3|0|unknown:1,wrong:2|raw=category→final=category×2; raw=category→final=unknown(probability_below_threshold)×1|
|pool|3522|digital_platform|category|12|0|unknown:11,wrong:1|raw=other→final=unknown(other_class)×8; raw=other→final=unknown(probability_below_threshold)×2; raw=id→final=id×1; raw=id→final=unknown(probability_below_threshold)×1|
|pool|3524|temporal|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3541|geo_comm|id|5|0|unknown:5|raw=id→final=unknown(probability_below_threshold)×3; raw=id→final=unknown(numeric_top2_too_close)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3542|geo_cant|id|12|9|unknown:1,wrong:11|raw=quantity→final=quantity×9; raw=category→final=category×2; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3544|administration|category|12|0|unknown:1,wrong:11|raw=quantity→final=quantity×11; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|3545|agriculture|category|8|0|unknown:1,wrong:7|raw=quantity→final=quantity×7; raw=category→final=unknown(probability_below_threshold)×1|
|pool|3546|construction|category|8|0|unknown:1,wrong:7|raw=quantity→final=quantity×7; raw=category→final=unknown(probability_below_threshold)×1|
|pool|3547|crime|category|12|0|wrong:12|raw=quantity→final=quantity×12|
|pool|3548|culture|category|2|0|wrong:2|raw=quantity→final=quantity×2|
|pool|3549|education|category|8|0|wrong:8|raw=quantity→final=quantity×8|
|pool|3550|energy|category|2|0|unknown:2|raw=other→final=unknown(other_class)×2|
|pool|3551|finances|category|12|0|unknown:3,wrong:9|raw=amount→final=amount×6; raw=quantity→final=quantity×3; raw=amount→final=unknown(probability_below_threshold)×2; raw=quantity→final=unknown(numeric_top2_too_close)×1|
|pool|3552|geography|category|2|0|wrong:2|raw=quantity→final=quantity×2|
|pool|3555|betrieb_plz|address|12|0|wrong:12|raw=id→final=id×12|
|pool|3560|tarifstruktur|category|12|0|wrong:12|raw=account→final=account×12|
|pool|3578|coordinatereferencesystem|id|12|0|wrong:12|raw=category→final=category×12|
|pool|3588|transaction date|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3598|domestic energy consumption in plymouth - 2011 updated 201|category|4|0|unknown:4|raw=quantity→final=unknown(numeric_values_not_parseable)×2; raw=quantity→final=unknown(probability_below_threshold)×2|
|pool|3601|institutioncode|id|1|0|unknown:1|raw=id→final=unknown(probability_below_threshold)×1|
|pool|3604|samplingeventstructure|category|1|0|unknown:1|raw=id→final=unknown(probability_below_threshold)×1|
|pool|3618|sampling_month|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3619|sampling_date|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3620|sampling_st|category|9|0|unknown:2,wrong:7|raw=id→final=id×7; raw=category→final=unknown(probability_below_threshold)×2|
|pool|3623|artist's dates|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3624|date of work|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3641|abteilung|account|3|0|unknown:3|raw=account→final=unknown(probability_below_threshold)×3|
|pool|3642|publisher_suffix|id|12|0|wrong:12|raw=org→final=org×12|
|pool|3674|搭載ファイル|quantity|3|0|unknown:3|raw=quantity→final=unknown(probability_below_threshold)×2; raw=id→final=unknown(numeric_top2_too_close)×1|
|pool|3676|分類|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3683|開設年月日|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|3689|見どころ・札所|text|2|0|unknown:1,wrong:1|raw=address→final=address×1; raw=address→final=unknown(probability_below_threshold)×1|
|pool|3703|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3713|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3723|利用可能 時間|text|4|0|wrong:4|raw=category→final=category×4|
|pool|3728|名称|address|2|0|wrong:2|raw=org→final=org×2|
|pool|3737|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3742|名称|address|7|0|wrong:7|raw=org→final=org×7|
|pool|3755|名称|address|4|0|wrong:4|raw=org→final=org×4|
|pool|3757|利用可能曜日|category|2|0|wrong:2|raw=text→final=text×2|
|pool|3760|利用可能日時特記事項|text|3|0|wrong:3|raw=category→final=category×3|
|pool|3775|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3780|名称|address|1|0|wrong:1|raw=org→final=org×1|
|pool|3783|開始時間|date|2|0|wrong:2|raw=text→final=text×2|
|pool|3789|名称|address|9|0|wrong:9|raw=org→final=org×9|
|pool|3803|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3813|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3823|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3856|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3870|設置位置|category|12|0|wrong:12|raw=address→final=address×12|
|pool|3895|名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|3896|名称_カナ|address|11|0|wrong:11|raw=org→final=org×11|
|pool|3908|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3928|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3943|名称|org|2|0|wrong:2|raw=address→final=address×2|
|pool|3944|名称_カナ|org|3|0|unknown:1,wrong:2|raw=address→final=address×2; raw=address→final=unknown(probability_below_threshold)×1|
|pool|3966|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3989|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|3999|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|4017|方書|address|2|0|unknown:1,wrong:1|raw=category→final=category×1; raw=category→final=unknown(probability_below_threshold)×1|
|pool|4053|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|4083|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|4093|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|4156|利用可能 時間|text|12|0|wrong:12|raw=category→final=category×12|
|pool|4163|名称_カナ|org|3|0|wrong:3|raw=address→final=address×3|
|pool|4182|学校名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4183|学校名称_カナ|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4185|ポリゴン_ファイル名|other|4|0|other_ng:4|raw=id→final=id×4|
|pool|4187|フリガナ|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4189|津波|category|3|0|unknown:1,wrong:2|raw=quantity→final=quantity×2; raw=category→final=unknown(probability_below_threshold)×1|
|pool|4194|延べ床|other|6|0|other_ng:6|raw=quantity→final=quantity×6|
|pool|4208|名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4209|名称_カナ|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4210|名称_英語|address|9|0|unknown:1,wrong:8|raw=org→final=org×8; raw=address→final=unknown(probability_below_threshold)×1|
|pool|4212|設置者|account|2|0|unknown:2|raw=account→final=unknown(probability_below_threshold)×2|
|pool|4216|名称メイショウ|text|2|0|unknown:1,wrong:1|raw=address→final=address×1; raw=address→final=unknown(probability_below_threshold)×1|
|pool|4220|特定日トクテイビ|text|4|0|unknown:1,wrong:3|raw=category→final=category×3; raw=text→final=unknown(probability_below_threshold)×1|
|pool|4221|休日キュウジツ|text|5|0|wrong:5|raw=category→final=category×5|
|pool|4227|投票所_名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4237|畑|other|1|0|other_ng:1|raw=amount→final=amount×1|
|pool|4242|名称|address|11|0|wrong:11|raw=org→final=org×11|
|pool|4243|名称_カナ|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4276|利用可能 時間|text|5|0|wrong:5|raw=category→final=category×5|
|pool|4329|確認年月日カクニンネンガッピ|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|4336|質問|product|6|0|unknown:1,wrong:5|raw=text→final=text×5; raw=text→final=unknown(probability_below_threshold)×1|
|pool|4338|ひらがな|text|12|0|unknown:1,wrong:11|raw=org→final=org×11; raw=text→final=unknown(probability_below_threshold)×1|
|pool|4341|出し方コード|category|12|0|wrong:12|raw=id→final=id×12|
|pool|4346|施設名|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4352|会 議 名|category|8|0|unknown:3,wrong:5|raw=text→final=text×3; raw=account→final=account×2; raw=account→final=unknown(probability_below_threshold)×2; raw=text→final=unknown(probability_below_threshold)×1|
|pool|4353|会議期間(日)|quantity|1|0|unknown:1|raw=quantity→final=unknown(numeric_top2_too_close)×1|
|pool|4355|会議時間|quantity|12|0|unknown:12|raw=quantity→final=unknown(numeric_values_not_parseable)×12|
|pool|4357|年[和暦]|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|4358|月|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|4377|月|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|pool|4383|名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4384|名称_カナ|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4385|名称_英字|address|8|0|wrong:8|raw=org→final=org×8|
|pool|4395|名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4396|名称_カナ|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4401|名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4402|名称_カナ|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4406|名称|address|10|0|unknown:1,wrong:9|raw=org→final=org×9; raw=org→final=unknown(probability_below_threshold)×1|
|pool|4407|名称_カナ|address|11|0|wrong:11|raw=org→final=org×11|
|pool|4408|名称_英字|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4415|名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4430|料金種別|text|1|0|wrong:1|raw=category→final=category×1|
|pool|4431|名称|address|11|0|wrong:11|raw=org→final=org×11|
|pool|4433|投票所区分|address|5|0|unknown:1,wrong:4|raw=category→final=category×4; raw=category→final=unknown(probability_below_threshold)×1|
|pool|4462|名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4463|名称_カナ|address|11|0|wrong:11|raw=org→final=org×11|
|pool|4464|名称_英字|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4465|名称_通称|address|11|0|wrong:11|raw=org→final=org×11|
|pool|4473|名称|address|12|0|wrong:12|raw=org→final=org×12|
|pool|4474|名称_カナ|address|6|0|wrong:6|raw=org→final=org×6|
|pool|4479|料金(基本)|text|1|0|unknown:1|raw=amount→final=unknown(probability_below_threshold)×1|
|pool|4483|6月|quantity|2|0|unknown:2|raw=other→final=unknown(other_class)×2|
|pool|4484|7月|quantity|4|0|unknown:4|raw=other→final=unknown(other_class)×3; raw=quantity→final=unknown(probability_below_threshold)×1|
|pool|4485|8月|quantity|8|0|unknown:8|raw=other→final=unknown(other_class)×7; raw=other→final=unknown(probability_below_threshold)×1|
|pool|4490|エリア名|address|2|0|wrong:2|raw=org→final=org×2|
|pool|4512|starttime|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×10; raw=other→final=unknown(other_class)×2|
|pool|4513|endtime|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×9; raw=other→final=unknown(other_class)×2; raw=other→final=unknown(probability_below_threshold)×1|
|pool|4525|人口1人当たり(円)|amount|3|2|unknown:1,wrong:2|raw=quantity→final=quantity×2; raw=amount→final=unknown(numeric_top2_too_close)×1|
|pool|4534|納付期別|category|1|0|unknown:1|raw=date→final=unknown(probability_below_threshold)×1|
|pool|4535|納付場所|text|9|0|unknown:2,wrong:7|raw=account→final=account×6; raw=category→final=category×1; raw=category→final=unknown(probability_below_threshold)×1; raw=text→final=unknown(probability_below_threshold)×1|
|pool|4543|節|id|1|0|unknown:1|raw=id→final=unknown(probability_below_threshold)×1|
|general|0|令和8年1月1日時点で静岡市を含む政令指定都市に住所があった人(税率8%)※|category|12|0|unknown:5,wrong:7|raw=text→final=text×7; raw=amount→final=unknown(probability_below_threshold)×2; raw=text→final=unknown(probability_below_threshold)×2; raw=category→final=unknown(probability_below_threshold)×1|
|general|9|country_code|address|2|0|wrong:2|raw=category→final=category×2|
|general|16|ja|other|12|0|other_ng:12|raw=category→final=category×12|
|general|17|iso_3166_1_alpha_3|address|12|0|wrong:12|raw=category→final=category×12|
|general|25|リウマチ科|quantity|7|0|wrong:7|raw=category→final=category×7|
|general|30|産婦人科|quantity|5|0|unknown:1,wrong:4|raw=category→final=category×4; raw=quantity→final=unknown(probability_below_threshold)×1|
|general|35|project / study name|text|2|0|unknown:2|raw=text→final=unknown(probability_below_threshold)×2|
|general|46|大腸菌※|other|11|0|other_ng:11|raw=category→final=category×11|
|general|55|page|other|10|0|other_ng:10|raw=id→final=id×10|
|general|60|ngram|text|12|0|unknown:7,wrong:5|raw=category→final=category×4; raw=other→final=unknown(probability_below_threshold)×3; raw=other→final=unknown(other_class)×2; raw=account→final=account×1; raw=account→final=unknown(probability_below_threshold)×1; raw=id→final=unknown(probability_below_threshold)×1|
|general|61|count_altmetric|quantity|10|0|unknown:10|raw=other→final=unknown(other_class)×9; raw=other→final=unknown(probability_below_threshold)×1|
|general|64|問合せ先|phone|2|0|unknown:2|raw=id→final=unknown(probability_below_threshold)×1; raw=phone→final=unknown(probability_below_threshold)×1|
|general|68|small stems|quantity|4|0|unknown:3,wrong:1|raw=category→final=category×1; raw=other→final=unknown(other_class)×1; raw=other→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|general|71|消化器科|quantity|6|0|unknown:2,wrong:4|raw=category→final=category×4; raw=quantity→final=unknown(probability_below_threshold)×2|
|general|100|塩化物イオン|other|2|0|other_ng:2|raw=category→final=category×2|
|general|103|relative flows|other|9|0|other_ng:9|raw=quantity→final=quantity×7; raw=category→final=category×2|
|general|107|臭気|other|1|0|other_ng:1|raw=category→final=category×1|
|general|123|サービス形態別_その他|quantity|12|0|wrong:12|raw=category→final=category×12|
|general|124|pos|text|1|0|unknown:1|raw=text→final=unknown(probability_below_threshold)×1|
|general|135|detail of applicant|person|12|0|unknown:3,wrong:9|raw=org→final=org×8; raw=org→final=unknown(probability_below_threshold)×3; raw=text→final=text×1|
|general|140|呼吸器科|quantity|3|0|wrong:3|raw=category→final=category×3|
|general|149|low flows*|category|8|0|wrong:8|raw=quantity→final=quantity×8|
|general|152|気管食道科|quantity|10|0|wrong:10|raw=category→final=category×10|
|general|155|読み仮名|org|12|0|wrong:12|raw=address→final=address×12|
|general|159|泌尿器科|quantity|3|0|wrong:3|raw=category→final=category×3|
|general|161|耳鼻いんこう科|quantity|12|0|wrong:12|raw=category→final=category×12|
|general|164|pfos及びpfoa|other|4|0|other_ng:4|raw=category→final=category×4|
|general|166|debris cataloged|quantity|6|2|unknown:4,wrong:2|raw=id→final=id×2; raw=id→final=unknown(numeric_top2_too_close)×2; raw=quantity→final=unknown(numeric_top2_too_close)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|general|179|麻酔科|quantity|10|0|wrong:10|raw=category→final=category×10|
|general|180|こう門科|quantity|12|0|wrong:12|raw=category→final=category×12|
|general|185|debris cataloged|quantity|2|0|unknown:2|raw=quantity→final=unknown(numeric_top2_too_close)×2|
|general|192|time[s]|other|12|0|other_ng:12|raw=quantity→final=quantity×12|
|general|194|userdefinedcategories|category|12|0|unknown:7,wrong:5|raw=id→final=id×5; raw=id→final=unknown(probability_below_threshold)×4; raw=other→final=unknown(probability_below_threshold)×2; raw=other→final=unknown(other_class)×1|
|general|196|sexualmaturityage|other|3|0|other_ng:3|raw=quantity→final=quantity×3|
|business|14|service description (f)|account|5|0|unknown:1,wrong:4|raw=text→final=text×4; raw=account→final=unknown(probability_below_threshold)×1|
|business|26|type/narrative of supply (e)|account|5|0|unknown:1,wrong:4|raw=text→final=text×4; raw=text→final=unknown(probability_below_threshold)×1|
|business|89|paymentdate|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|business|93|purposeofspend|text|4|0|wrong:4|raw=account→final=account×4|
|business|115|service|account|1|0|wrong:1|raw=category→final=category×1|
|business|129|smesupplier|category|6|0|wrong:6|raw=org→final=org×6|
|business|153|quarterno|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|business|168|well-founded_bien-fonde|quantity|12|2|unknown:2,wrong:10|raw=category→final=category×8; raw=id→final=id×2; raw=id→final=unknown(probability_below_threshold)×2|
|business|169|unfounded_non-fonde|quantity|12|0|wrong:12|raw=category→final=category×12|
|business|171|no-action_aucune-action|quantity|5|0|unknown:3,wrong:2|raw=category→final=category×2; raw=category→final=unknown(probability_below_threshold)×2; raw=quantity→final=unknown(probability_below_threshold)×1|
|business|172|action-required_action-requise|quantity|7|0|unknown:2,wrong:5|raw=category→final=category×5; raw=category→final=unknown(probability_below_threshold)×1; raw=quantity→final=unknown(probability_below_threshold)×1|
|business|178|city|org|7|0|unknown:1,wrong:6|raw=address→final=address×6; raw=address→final=unknown(probability_below_threshold)×1|
|business|189|fy_ef|date|2|0|unknown:2|raw=date→final=unknown(date_value_evidence_low)×2|
|business|191|document_budget_des_dépenses|category|10|0|wrong:10|raw=account→final=account×10|
|business|193|autorisations|amount|6|3|unknown:3,wrong:3|raw=id→final=unknown(probability_below_threshold)×2; raw=quantity→final=quantity×2; raw=id→final=id×1; raw=id→final=unknown(numeric_top2_too_close)×1|
|business|203|patents_granted_per_100_000_residents|rate|8|5|unknown:3,wrong:5|raw=quantity→final=quantity×5; raw=quantity→final=unknown(probability_below_threshold)×2; raw=quantity→final=unknown(numeric_top2_too_close)×1|
|business2|2|service category label|category|12|0|wrong:12|raw=account→final=account×12|
|business2|5|procurement (merchant) category|category|5|0|wrong:5|raw=account→final=account×5|
|business2|46|quarterno|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|business2|56|total interest paid|amount|12|0|unknown:12|raw=amount→final=unknown(numeric_values_not_parseable)×12|
|business2|57|group year average interest paid|amount|12|0|unknown:12|raw=amount→final=unknown(numeric_values_not_parseable)×12|
|business2|78|expense type|id|8|0|wrong:8|raw=account→final=account×8|
|business2|96|address_2|address|1|0|wrong:1|raw=org→final=org×1|
|business2|99|known_as|org|9|0|unknown:2,wrong:7|raw=address→final=address×7; raw=address→final=unknown(probability_below_threshold)×2|
|business2|100|car_park_name|org|12|0|wrong:12|raw=address→final=address×12|
|business2|106|spaces|quantity|4|0|unknown:4|raw=other→final=unknown(other_class)×4|
|business2|130|index of multiple deprivation (imd) 2007|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|131|index of multiple deprivation (imd) 2010|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|132|income deprivation 2007|rate|1|0|unknown:1|raw=rate→final=unknown(numeric_top2_too_close)×1|
|business2|136|health deprivation and disability 2007|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|137|health deprivation and disability 2010|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|138|education skills and training deprivation 2007|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|139|education skills and training deprivation 2010|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|140|barriers to housing and services deprivation 2007|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|141|barriers to housing and services deprivation 2010|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|142|crime and disorder deprivation 2007|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|143|crime and disorder deprivation 2010|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|144|living environment deprivation 2007|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|145|living environment deprivation 2010|other|12|0|other_ng:12|raw=rate→final=rate×12|
|business2|175|treetype|category|1|0|unknown:1|raw=category→final=unknown(probability_below_threshold)×1|
|business2|188|shapearea|other|8|0|other_ng:8|raw=category→final=category×8|
|business2|234|itm_east|other|1|0|other_ng:1|raw=amount→final=amount×1|
|business2|294|desc_|account|1|0|wrong:1|raw=category→final=category×1|
|business2|348|tlist(q1)|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|business2|356|tlist(q1)|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|business2|366|tlist(q1)|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|business2|378|年月|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|business2|401|fiscal-month-mois-fiscal|date|12|0|unknown:12|raw=date→final=unknown(date_value_evidence_low)×12|
|japan_procurement|11|契約内容 【該当するものをプルダウンから選択】|category|1|0|wrong:1|raw=text→final=text×1|
|japan_procurement|28|備考|text|2|0|unknown:1,wrong:1|raw=category→final=category×1; raw=category→final=unknown(probability_below_threshold)×1|
|japan_procurement|40|請負業者名|org|6|0|unknown:1,wrong:5|raw=person→final=person×5; raw=org→final=unknown(probability_below_threshold)×1|
|japan_procurement|65|品目|product|10|0|wrong:10|raw=category→final=category×10|

## 限界

- これは保存済み予測の全件監査で、固定評価の再推論ではない。値・兄弟列・UNIT・出典を伴う直接原因調査はW2未知見出し136行に限る。
- `STATUS.md` はartifact未確認と表示するが、GitHub Actions APIでは評価/model artifactを別々に確認できた。表示更新遅延として扱う。
- b187の207列はW2完了後に確定したため、W2学習には含まれない。
