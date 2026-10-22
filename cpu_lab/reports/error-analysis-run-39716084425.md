# run 39716084425 失敗分析（S11 jp3 第1バッチ）

更新: 2026-10-22 JST

## 結論

S11 jp3 第1バッチを加えた学習は完了したが、採用基準を満たさなかった。固定255列の平均OK率はベースライン81.4%に対し81.3%（-0.1ポイント、1.5ポイント未満なので差なし）、889列での重大誤り平均は2.7件から4.3件へ増加した。新モデルは採用せず、jp3教材は次の大きな教材束に統合して再評価する。

## 監査範囲と整合性

- 対象: run 39716084425、微調整単体（ft）、seed 1/2/3。
- 読んだ固定検証: val_general、val_business、val_business2、val_japan_procurement のみ。
- blind_set*、set 3・5・7は読んでいない。
- 12個の確率ファイルを行単位で再集計。総2,667判定（889列×3 seed）のうち、誤り・重大誤り・unknown・other_ngに該当する問題インスタンスは186件、列名・正解ラベル単位では75ケース。
- 内訳: wrong 89、other_ng 57、unknown 40。集合別: val_business2 84、val_general 66、val_business 33、val_japan_procurement 3。
- 最終の「固定255列OK率」は別途定義された部分集合指標であり、本監査の186件は889列全体の診断母集団である。両者を混同しない。
- 成果物: evaluation-report artifact 12400042015（507,171 bytes）、model artifact 12399962009（865,260,145 bytes）。3つのmanifestで学習行53,047と保存モデルhash/sizeを確認済み。

## 確認済みの観測事実

- 教材は50,491行から53,047行へ+2,556行（約5%）。jp3由来は426列・67表で、idラベル42列を含む。
- 主要混同行列: quantity->category 44、other->rate 37、date->unknown 19、other->category 11、amount->unknown 9、date->id 6、category->account 6、org->address 6、category->unknown 5、text->category 5、quantity->unknown 5、other->amount 4。
- 判定理由: null 146、date_value_evidence_low 18、probability_below_threshold 11、numeric_values_not_parseable 6、other_class 3、numeric_top2_too_close 2。
- 同一ケースのseed再現性: 3 seedすべて46ケース、2 seed 8ケース、1 seedのみ19ケース。単発の乱数揺れだけでは説明できない誤りが多い。
- date系unknownの多くは raw modelの低確信ではなく date_value_evidence_low によるguard棄却である。数値系にも numeric_values_not_parseable / numeric_top2_too_close がある。モデルとguardを分離して評価する必要がある。
- tlist(q1) は同一seed内で重複出現し、3 seed合計9件のunknownとなる。ファイル内の重複は確認したが、元表・split生成段階の重複原因は未確認。

## 重大誤り（全件をパターン集約）

|集合|列名|正解|発生数|seed|予測|重大|理由|
|---|---|---:|---:|---|---|---:|---|
|val_business|autorisations|amount|3|1,2,3|unknown:2, id:1|1|probability_below_threshold:2, null:1|
|val_business|patents_granted_per_100_000_residents|rate|3|1,2,3|quantity:3|3|null:3|
|val_business|quarterno|date|3|1,2,3|id:3|3|null:3|
|val_business2|quarterno|date|3|1,2,3|id:3|3|null:3|
|val_general|debris cataloged|quantity|4|2,3|id:3, unknown:1|3|null:3, numeric_top2_too_close:1|

重大誤りの確認済みパターンは5つ: quarterno（date→id、business/business2）、patents_granted_per_100_000_residents（rate→quantity）、debris cataloged（quantity→id/unknown）、autorisations（amount→id）。

## 原因評価

|観点|観測事実|原因仮説|確度|追加確認|
|---|---|---|---|---|
|教材量|追加は全体の約5%|効果がseed分散に埋もれた|中|同じ条件でより大きい事前登録済み教材束を追加|
|id偏り|jp3に小整数の「款・項・目コード」等を含むid 42列。date/quantity/amount→id重大誤りが増加|小整数idの追加がid方向へ境界を動かした|中（相関、因果未証明）|id教材を兄弟列・UNIT文脈と対にし、一要因で再試験|
|文脈|医療科名のquantity→category、known_as/car_park_nameのorg→address等が3 seedで反復|見出し単独では定義・表文脈を復元できない|中〜高|安全な表ID、兄弟列、UNIT有無を成果物へ保存し層別評価|
|guard|date_value_evidence_low 18件、numeric parse系8件|raw modelが正しくてもguardがunknown化|高（実装理由を直接確認）|guard前後を別指標化し、独立開発集合でのみ調整|
|ラベル|医療科名quantity、deprivation列other等に意味上の疑義|一部はラベル定義不一致|低〜中|先生2人の独立確認と根拠裁定。完了までラベル変更禁止|
|切り詰め|run全体の切り詰め率5.63%|長い文脈喪失が一部誤りに寄与|低|行別token長・切り詰めフラグを保存して誤りと照合|
|漏洩/分割|確率ファイルに元表ID・split由来がない|漏洩または同一表またぎの有無は判断不能|未確認|source/table hashをmanifestと行に追加し重複監査|

## 改善案（優先順）

1. **P0 監査可能性**: raw件数と最終指標の自動assert、source/table hash、UNIT/兄弟列有無、token長・切り詰め、guard前後予測を成果物へ必須保存。期待効果は原因特定の再現性向上。副作用は成果物増加。
2. **P0 idバランス**: 小整数コードのidだけを増やさず、非id小整数・日付番号・数量とのhard negative、兄弟列/UNITを対にする。期待効果はdate/quantity→id抑制。副作用は真のid再現率低下の恐れ。
3. **P1 教材規模**: 3.3統計表、3.4多国籍メタデータ、3.1保留分のうち監査済みのみを、出典分散を保って少なくとも約700実列規模で一要因追加。副作用は収集・裁定時間増。
4. **P1 guard分離試験**: モデル固定でdate/numeric guardだけを独立評価し、同じ固定試験で閾値を最適化しない。期待効果はunknown削減。副作用は誤受理増加の可能性。
5. **P2 ラベル裁定**: 疑義ケースは先生2人が独立確認し、根拠付き裁定後にのみ教材・評価ラベルを変更する。

## 全75ケース（186インスタンスを集約）

|集合|列名|正解|件数|seed|予測内訳|outcome内訳|重大|理由|top1確率範囲|
|---|---|---:|---:|---|---|---|---:|---|---:|
|val_business|2023-2024|amount|1|3|unknown:1|unknown:1|0|probability_below_threshold:1|0.488–0.488|
|val_business|action-required_action-requise|quantity|2|1,3|category:2|wrong:2|0|null:2|0.775–0.947|
|val_business|autorisations|amount|3|1,2,3|unknown:2, id:1|unknown:2, wrong:1|1|probability_below_threshold:2, null:1|0.462–0.507|
|val_business|complaint-refused-exemption_plainte-refus-exception|quantity|2|1,3|category:2|wrong:2|0|null:2|0.923–0.976|
|val_business|document_budget_des_dépenses|category|3|1,2,3|account:2, unknown:1|wrong:2, unknown:1|0|null:2, probability_below_threshold:1|0.485–0.814|
|val_business|expense type|id|1|3|account:1|wrong:1|0|null:1|0.891–0.891|
|val_business|no-action_aucune-action|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.614–0.917|
|val_business|patents_granted_per_100_000_residents|rate|3|1,2,3|quantity:3|wrong:3|3|null:3|0.632–0.913|
|val_business|paymentdate|date|3|1,2,3|unknown:3|unknown:3|0|date_value_evidence_low:3|0.975–0.978|
|val_business|poste_législatif|account|1|1|text:1|wrong:1|0|null:1|0.549–0.549|
|val_business|procurementclassification:proclasslabel|account|1|3|category:1|wrong:1|0|null:1|0.564–0.564|
|val_business|quarterno|date|3|1,2,3|id:3|wrong:3|3|null:3|0.621–0.857|
|val_business|service description (f)|account|1|2|unknown:1|unknown:1|0|probability_below_threshold:1|0.457–0.457|
|val_business|type/narrative of supply (e)|account|1|2|text:1|wrong:1|0|null:1|0.609–0.609|
|val_business|unfounded_non-fonde|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.824–0.965|
|val_business|well-founded_bien-fonde|quantity|2|2,3|category:1, unknown:1|wrong:1, unknown:1|0|null:1, probability_below_threshold:1|0.474–0.797|
|val_business2|barriers to housing and services deprivation 2007|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.915–0.952|
|val_business2|barriers to housing and services deprivation 2010|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.926–0.946|
|val_business2|car_park_name|org|3|1,2,3|address:3|wrong:3|0|null:3|0.962–0.971|
|val_business2|column6|text|2|1,3|category:2|wrong:2|0|null:2|0.548–0.628|
|val_business2|crime and disorder deprivation 2007|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.963–0.967|
|val_business2|crime and disorder deprivation 2010|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.950–0.962|
|val_business2|education skills and training deprivation 2007|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.924–0.943|
|val_business2|education skills and training deprivation 2010|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.935–0.954|
|val_business2|expense type|id|1|3|account:1|wrong:1|0|null:1|0.888–0.888|
|val_business2|fiscal-month-mois-fiscal|date|3|1,2,3|unknown:3|unknown:3|0|date_value_evidence_low:3|0.972–0.978|
|val_business2|group year average interest paid|amount|3|1,2,3|unknown:3|unknown:3|0|numeric_values_not_parseable:3|0.932–0.979|
|val_business2|health deprivation and disability 2007|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.960–0.969|
|val_business2|health deprivation and disability 2010|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.953–0.968|
|val_business2|index of multiple deprivation (imd) 2007|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.637–0.879|
|val_business2|index of multiple deprivation (imd) 2010|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.711–0.909|
|val_business2|itm_east|other|3|1,2,3|amount:2, id:1|other_ng:3|0|null:3|0.601–0.846|
|val_business2|itm_north|other|3|1,2,3|amount:2, id:1|other_ng:3|0|null:3|0.667–0.888|
|val_business2|known_as|org|3|1,2,3|address:3|wrong:3|0|null:3|0.702–0.876|
|val_business2|living environment deprivation 2007|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.929–0.945|
|val_business2|living environment deprivation 2010|other|3|1,2,3|rate:3|other_ng:3|0|null:3|0.934–0.948|
|val_business2|map_x|other|1|2|category:1|other_ng:1|0|null:1|0.874–0.874|
|val_business2|procurement (merchant) category|category|1|1|account:1|wrong:1|0|null:1|0.504–0.504|
|val_business2|quarterno|date|3|1,2,3|id:3|wrong:3|3|null:3|0.618–0.862|
|val_business2|service category label|category|3|1,2,3|account:3|wrong:3|0|null:3|0.956–0.961|
|val_business2|shapearea|other|3|1,2,3|category:3|other_ng:3|0|null:3|0.707–0.946|
|val_business2|tlist(q1)|date|9|1,2,3|unknown:9|unknown:9|0|date_value_evidence_low:9|0.959–0.979|
|val_business2|total interest paid|amount|3|1,2,3|unknown:3|unknown:3|0|numeric_values_not_parseable:3|0.967–0.979|
|val_business2|value|quantity|1|3|unknown:1|unknown:1|0|numeric_top2_too_close:1|0.568–0.568|
|val_business2|年月|date|3|1,2,3|unknown:3|unknown:3|0|date_value_evidence_low:3|0.977–0.978|
|val_general|count_altmetric|quantity|1|2|unknown:1|unknown:1|0|other_class:1|0.968–0.968|
|val_general|debris cataloged|quantity|4|2,3|id:3, unknown:1|wrong:3, unknown:1|3|null:3, numeric_top2_too_close:1|0.550–0.937|
|val_general|detail of applicant|person|3|1,2,3|org:3|wrong:3|0|null:3|0.893–0.954|
|val_general|iso_3166_1_alpha_3|address|3|1,2,3|category:3|wrong:3|0|null:3|0.813–0.955|
|val_general|ja|other|3|1,2,3|category:3|other_ng:3|0|null:3|0.540–0.753|
|val_general|low flows*|category|1|2|quantity:1|wrong:1|0|null:1|0.924–0.924|
|val_general|metabolic rate|other|1|1|rate:1|other_ng:1|0|null:1|0.735–0.735|
|val_general|ngram|text|3|1,2,3|category:3|wrong:3|0|null:3|0.843–0.940|
|val_general|pfos及びpfoa|other|1|1|category:1|other_ng:1|0|null:1|0.629–0.629|
|val_general|relative flows|other|3|1,2,3|quantity:3|other_ng:3|0|null:3|0.647–0.919|
|val_general|sample body site|category|1|2|unknown:1|unknown:1|0|other_class:1|0.587–0.587|
|val_general|こう門科|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.964–0.977|
|val_general|サービス形態別_その他|quantity|2|2,3|category:2|wrong:2|0|null:2|0.575–0.978|
|val_general|リウマチ科|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.959–0.972|
|val_general|令和8年1月1日時点で静岡市を含む政令指定都市に住所があった人(税率8%)※|category|3|1,2,3|unknown:3|unknown:3|0|probability_below_threshold:3|0.247–0.363|
|val_general|呼吸器外科|quantity|2|1,3|category:2|wrong:2|0|null:2|0.867–0.882|
|val_general|呼吸器科|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.748–0.922|
|val_general|大腸菌※|other|3|1,2,3|category:3|other_ng:3|0|null:3|0.713–0.923|
|val_general|心療内科|quantity|2|1,3|category:2|wrong:2|0|null:2|0.556–0.598|
|val_general|整形外科|quantity|1|1|unknown:1|unknown:1|0|probability_below_threshold:1|0.496–0.496|
|val_general|時分|date|1|1|unknown:1|unknown:1|0|other_class:1|0.832–0.832|
|val_general|気管食道科|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.964–0.983|
|val_general|泌尿器科|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.667–0.976|
|val_general|消化器科|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.615–0.827|
|val_general|産婦人科|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.617–0.969|
|val_general|耳鼻いんこう科|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.968–0.977|
|val_general|読み仮名|org|1|1|unknown:1|unknown:1|0|probability_below_threshold:1|0.489–0.489|
|val_general|麻酔科|quantity|3|1,2,3|category:3|wrong:3|0|null:3|0.881–0.984|
|val_japan_procurement|品目|product|1|3|category:1|wrong:1|0|null:1|0.718–0.718|
|val_japan_procurement|請負業者名|org|2|1,2|person:2|wrong:2|0|null:2|0.620–0.770|

## 未確認・未完了

- jp3のid追加が重大誤り増加の直接原因かは未確定。次回は教材以外を固定した一要因試験が必要。
- 生の値、元表ID、兄弟列、UNIT有無、行別切り詰め情報が現成果物にないため、各ケースの文脈原因は断定しない。
- ChatGPT・Claudeとの同一課題比較による同等以上の実証は未完了。Geminiは比較目標から除外。
