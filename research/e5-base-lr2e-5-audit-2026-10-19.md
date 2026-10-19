## 2026-10-19 UTC：FT_LR=2e-5 matched test 完了・誤り監査

### 実行と成果物（事実）
- GitHub Actions run 39174794327 は success。Kaggle Kernel Version 21 の一致する最新ログは 2026-10-18T23:24:34Z に COMPLETE。kaggle.request は done、他のKaggle学習runは稼働なし。
- FINETUNE_RESULTS.md に2 seed分の結果が反映済み（仕事1 seed=1、仕事2 seed=2）。評価 artifact 12154383249（81ファイル）とモデル artifact 12154602284 は別々に存在・回収確認。状態と回収記録は kaggle/STATUS.md。
- 対象は dev220 / general / business / business2 / japan_procurement の5セットだけ。blind_set、set 3/5/7は参照していない。
- 比較対象は直前の同条件 frozen embedding + UNIT、既定LR、seed 1/2（FINETUNE_RESULTS.md の2026-10-18 21:15節）。評価セットとseedを合わせ、LRだけを変えた比較。

### 精度・誤り比較
| セット | 既定LR seed1/2 精度 | LR=2e-5 seed1/2 精度 | 平均差 | 誤り 合計 | 重大 合計 | unknown 合計 |
|---|---:|---:|---:|---:|---:|---:|
| dev220 | 95.9 / 97.3 | 96.4 / 97.3 | +0.25 pp | 14→11 | 3→2 | 1→3 |
| general | 92.5 / 91.5 | 90.5 / 91.9 | −0.80 pp | 15→21 | 3→4 | 32→31 |
| business | 92.4 / 91.8 | 91.2 / 92.8 | −0.10 pp | 53→56 | 7→8 | 22→20 |
| business2 | 95.3 / 95.5 | 95.7 / 95.3 | +0.10 pp | 52→45 | 7→8 | 32→37 |
| japan_procurement | 98.9 / 98.9 | 98.9 / 98.9 | 0.00 pp | 0→0 | 0→0 | 2→2 |
| 合計 | — | — | 全セット <1.5 pp | 134→133 | 20→22 | 89→93 |

- 判定：精度は指定基準上「差なし」。総誤りは1件だけ減ったが、重大誤りは2件、不明は4件増えた。general の誤りが6件増、business2 は7件減。seedごとの上下もあり、LR=2e-5を改善と結論しない。
- 学習時間：既定LR 467/456秒（平均461.5秒）→ LR=2e-5 494/471秒（平均482.5秒）、約+4.6%。評価は基準16/16秒、今回18/18秒。GPUピークは両条件3.5 GiBで変化なし（Kaggle実行ログ）。
- 2 seedしかなく、僅かな差の統計的有意性は判断できない。丸められた精度表示の平均に基づく。

### ケース監査：観測と原因仮説
ケース一覧は同runの評価artifact ERROR_ANALYSIS.md の ft 行にある。全5セット×2 seedの誤り・重大誤り・unknown一覧を監査した。以下はartifactに記録された観測で、ラベルや値の正しさを独立に再判定したものではない。

- business：category→quantityがseed1/2で繰り返し最多（seed1 23件）。department org→account、abn id→amount、total invoices paid quantity→amountも両seedで再発。重大例にはabn、total invoices paid、seed2のamount/id/quantity取り違え。
- business2：amount→quantity、category→quantity、category↔idなど数量・金額・識別子の境界が反復。重大例 fine amount→quantity、miscellaneous_divers amount→quantity（top confidence 約0.996）、sales-goods-svcs_ventes-biens-srvs amount→quantity、total invoices paid quantity→amount が両seedで再発。
- general：quantity→category、quantity→rateが中心。n_occurences quantity→rateはseed1/2で再発し、高確信（最大約0.918）。seed2ではage_q3 / age_q3_nd quantity→rateも重大扱い。goal id→categoryなど曖昧な短い見出しも再発。
- dev220：誤りが少数でも purchase order by customer id→quantity が両seedで重大。Japan procurementは誤り0、unknown 1/seed。
- unknown例の列名には年度・四半期・期間、分類語、ローカライズ表記等が含まれ、高確信でもunknownとなる例がある。これはラベル・正規化・unknown判定のいずれかが候補だが、これだけで原因は確定できない。
- confidence：誤り一覧には高確率の誤分類が複数あり、単純な低信頼閾値だけでは重大誤りを防げない。確率校正とクラス対ごとの拒否/レビュー方針を検討する価値がある。
- 分布・分割：seedをまたいで同じ列名/同じ誤ラベルが再現することはartifact上で確認。元データの出典、重複レコード、分割漏れ、カテゴリ頻度はartifactにないため、分布シフト・漏洩の有無は未確認。
- 文脈・前処理：誤りは似た意味役割（amount/quantity/rate、org/account、id/category）に集中。列名だけの曖昧さ、UNIT文脈の不足、正規化・トークナイズの影響が仮説。値や隣接列・入力前処理の追跡情報がないため因果は未確定。
- ラベル：goal、VALUE、department、titleなどは文脈依存が強い候補。ラベル誤りとモデル誤りを切り分ける根拠（元表・値・ラベル根拠）は未収録。自動的に教師データへ追加・変更しない。

### 重大な監査上の不整合（事実・未解決）
- 同じrunの job1_probs_business_ft.json は490行中 prediction=="unknown" が26行、一方で FINETUNE_RESULTS.md と ERROR_ANALYSIS.md の公式unknown数は12。job1_errors_business_ft.json の errors は85件だが、公式誤りは30件。
- よって評価artifactの確率/エラーJSONは、最終 guard 後の予測または集計指標と同じ母数・定義を示していない可能性がある。原因は出力スキーマ/条件の説明不足が有力だが未確認。公式指標との対応を再現できるまで、ケース別分類は「artifact内記録の監査」であり、指標定義に沿う完全な個票監査とは断定しない。過去のエラー集計スクリプトに定義ミスがないかも再検証が必要。

### 原因調査の更新・次に行う改善（提案。追加学習は依頼していない）
1. 評価出力を一行一予測の共通schemaにする：set、seed、row_id、truth、raw_pred、guard_pred、abstain_reason、critical、top-k、前処理版を含め、全件数がFINETUNE_RESULTSの集計に一致するassertionをCIで追加。
2. 現runの5セット・2 seedをそのschemaで再出力し、誤り/重大/unknownの集合差を解消してから完全な原因監査を確定。
3. 重大取り違えはまず人手二重判定（ChatGPT/Claude。片方のみの場合も監査者を記録）でラベル根拠と例外を確認。特に amount↔quantity↔rate、id↔amount/quantity、org↔account、曖昧短見出しを優先。固定セットを使った規則調整による楽観バイアスを明記し、未見セットは開かない。
4. 次の精度施策はモデル大型化ではなく、再発confusion対のラベル根拠・UNIT兄弟列/値の有効性・前処理を検証すること。改善は別データの固定評価で確認するまで候補扱い。今回LR変更は精度差なし・時間悪化のため既定LRを維持する。

### 参照
- GitHub Actions run 39174794327: https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39174794327
- Kaggle状態/回収記録: kaggle/STATUS.md
- 指標原本: FINETUNE_RESULTS.md（2026-10-18 21:15 と23:23の節）
- ケースartifact: eval artifact 12154383249 / ERROR_ANALYSIS.md（指定5セットのftセクションのみ）
- model artifact 12154602284（評価artifactとは別。sha256 e96de0f73485f9becb87d4a4dbed01594ca2dc5b817814cf0f5761505a270844）


### 2026-10-19追記：個票と公式指標の差の再確認

- `job1_probs_business_ft.json` の `prediction=="unknown"` 26行と公式 `unknown=12` の差は、そのまま集計不整合を意味しない。`truth=="other"` かつ予測が `unknown` の行は、`score_real` では正しい見送り `other_ok` に入り、通常の `unknown` には数えない。この区別が旧ファイルで見えにくかった。
- 一方、旧 `errors_*.json` は `error_rows` が評価セットのループ外で初期化されていたため、前セットの行を後のファイルへ累積していた。例えば business の85行と当該セット単独の公式誤り30件との差は、確かな個票一覧として扱えない。集計JSONを保存するより前にセット単位で作り直す修正を入れた。
- 新しい評価出力は schema 2 とし、`raw_prediction`、`guarded_prediction`、公式スコア上の `outcome` を別記する。書出し前に行記録を `score_real` の公式集計へ照合し、不一致なら停止する。`abstain_eval.py` は schema 1 と予測フィールドの不一致を拒否する。
- 変更後のローカル検証：評価記録 4件、棄却分析 8件、Python compile がすべて通過。CIも変更対象で起動する設定だが、このコネクタから最新のpush run結果は照会できていない。
- この修正で過去の schema 1 artifact は遡及的に直らない。現runの個票による原因監査と閾値採用は保留し、次の学習実行でschema 2 artifactを生成・照合してから再開する。旧unknown件数の差だけを理由に不整合と判定していた記述は上記のとおり訂正する。
