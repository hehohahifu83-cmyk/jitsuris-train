# CPU能動学習ループ実装記録（2026-10-18）

## 実装目的
Kaggle GPU待機中もCPU学習に教材選びの準備を進められるよう、モデルが不確かな候補列を優先提示し、人が検証したラベルだけを独立候補の再学習へ流す仕組みを追加した。予測ラベルをそのまま正解扱いする自己学習は誤りを増幅するため採用していない。

## 変更
- `cpu_lab/self_learning.py`
  - 候補モデルでJSONLの未ラベル列を推論。
  - 不確実度、予測クラスのレビュー済み件数、ヘッダー重複を使い、優先候補を出力。
  - 元の列・値・文脈・出典・ライセンス・プライバシー確認状態をキューに保持。
  - 明示的な人手確認（承認状態・ラベル・レビュアー・verified=true）がある行だけ訓練JSONLに書き出す。
  - 訓練用JSONLの出典、ライセンス、プライバシー、既存クラス集合、重複ID、禁止試験由来を再検査する。
- `finetune_exp.py`
  - `FT_CPU_LAB_REPLAY` を明示した場合だけ承認済みJSONLを既存訓練行へ追加する。未設定なら従来動作。
- `.github/workflows/cpu-lab-active-learning.yml`
  - 手動起動・既定no・確認必須。2 seedを逐次実行し、ログ・固定試験の集計/ケース別誤り・replayデータを7日間artifactに保存。
  - replayファイルは `cpu_lab/materials/verified_replay/*.jsonl` 配下を要求。
- `.github/workflows/cpu-e5base-training.yml`
  - CPUラボと共有する排他グループに変更。
- `cpu_lab/README.md`, `cpu_lab/tests/test_self_learning.py`
  - 運用方法と安全性テストを記録。

## 検証
- ローカルのPython 3で unittest 4件成功。
- `self_learning.py` の py_compile 成功。
- GitHub Actions の実行・学習、候補データ作成、性能差の測定は未実施。
- 学習プールと承認済み教材はまだ存在しない。候補生成、確認、承認を行わないままworkflowを起動しても学習を始めない。

## リスク・未完了
1. 固定試験汚染ガードはファイル名/出典識別子/metadataに基づくため、出典を偽る運用上の脅威まで数学的に排除するものではない。プールを作る段階で人が来歴確認する必要がある。
2. 初回候補選び、速度/CPUピークメモリ測定、固定5試験の比較と全誤り・重大誤りの原因分析が残る。差は1.5ポイント未満なら差なし。
3. 既存AI連絡箱ではこれまで自動整理workflowが失敗し、Claude INBOX反映が未確認。Claude宛て最新メッセージを作成したが受領扱いにはしない。
4. 外部公開教材の具体的な取り込みはまだ行っていない。出典・ライセンス・個人情報の確認後に別途追加する。

## Claudeへの依頼
`ai-bridge/messages/20261018-2000_chatgpt-to-claude_active-learning.md` に独立レビュー依頼を作成。Claude復帰後、ユーザーに連絡箱を読んでもらう必要がある。特に人手確認ゲート、試験漏洩/クラス集合検査、候補の偏りと近重複抑制をレビューする。


## 連絡箱の状態（2026-10-18 20:00確認）
ai-bridgeへClaude宛てレビュー依頼を保存した後、自動整理workflow run 39121537658 が失敗。INBOX.md はClaude宛て未読0件のままで、今回メッセージの掲載・Claude受領は未確認。

## CIの最終確認（2026-10-18）
CPU lab safety tests run 39121622107・39121637227 はテストモジュールへのsys.path設定がリテラル\\nのまま入っていたため失敗。テストファイルを修正し、run 39121657962 はsuccess（コンパイルと4テスト）。同じテストが変更ごとに走る `.github/workflows/cpu-lab-tests.yml` も追加済み。

Claude連絡箱: メッセージの更新後にai-bridge workflow run 39121677204 がfailure。ログ取得APIはBlobNotFound、INBOXのClaude宛て未読は依然0件。ファイルには保存されているが、INBOX掲載・Claude受領は未確認。

## 専用教材の調査・整備（2026-10-18）
- `cpu_lab/materials/learning-materials-priority-pack-2026-10-18.md` を追加。Jitsurisの列タイプ分類に必要な教材の優先順位、unknown境界例、unit/context対照、誤りやすい近接クラスの合成演習草案、外部資料の権利確認状況を記録。
- 長いchain-of-thoughtを学習目標にする方針は採らず、見出し・値・単位/表文脈・判断規則・棄却理由を短い監査用タグとして残す設計を推奨。実装特徴の採否は一要因ずつ試験する。
- e-Statは集計表の候補だが、具体表の注記・第三者権利確認とAPI登録/app IDが必要。データ取得はまだ行っていない。SherlockはREADME記載のライセンスを確認したが、個人情報リスク/由来/重複を解決するまで取り込まない。SOTAB/Sato/GitTablesは現状、方法参考のみ。
- 教材READMEとCPU Lab READMEを、調査済みパックと未取得/未検証の訓練データの区別が明確になるよう更新。
- 現在も訓練可能な承認済み教材はなく、能動学習CPU候補ジョブは未開始。合成例は草案であり訓練データではない。
- Kaggleの記録末尾には2026-10-18T10:56:49Z（JST 19:56:49）のRUNNINGが残る。GitHub上のKaggle workflow run 39121167019はsuccessだが、これはKaggle kernelの完了を保証しない。依頼ファイルは`fetch`。今回取得できた現在のKaggle状態APIはなく、RUNNINGの記録以降の完了は未確認。CPU候補学習はKaggleの重複/資源干渉を避けるため開始していない。


## 人手レビューなしの候補学習経路（2026-10-18）
- オーナーより、人手ラベル確認は不可能との指示。人手レビューを学習開始の必須条件にしない。
- `cpu_lab/self_learning.py autolabel` を追加。同じ分類器で元の値順・逆順・一つずらした順の3表現を採点し、3つの予測が同じ、全ての確信度が0.995以上、1位と2位のmarginが0.50以上の列だけ機械仮ラベルに出力する。これは同一モデルの入力一貫性確認であり、独立AI合意や正解保証ではない。
- 学習用loaderは `verified=false` と来歴を保持し、クラス集合・出典・利用条件・プライバシー・重複・閾値・3-view合意を再検査。元訓練行の最大1%に制限し、人手確認済み経路とは同時使用不可。
- `finetune_exp.py` は `FT_CPU_LAB_PSEUDO` を明示した時だけ仮ラベルを読み、疎特徴ベースラインには混ぜない。GitHub Actionsワークフローに `automatic_pseudo` モードを追加し、CPU実行は手動確認かつ候補2 seed逐次。候補を自動昇格しない。
- 検証: CPU lab safety tests run 39122773344 success（2026-10-18 11:19:39Z）。追加したゲート・上限テストを含め合格。途中runの失敗はcapテストの期待値が誤っていたため修正し、最終runで解消。
- 未着手: 利用条件と個人情報を確認した未ラベルpool、候補checkpointの取得/所在確認、autolabel実行、CPU候補学習、許可済み固定5試験での比較。よってCPUラボのモデル学習はまだ始まっていない。KaggleのGPU runと重複させない運用状態も継続確認が必要。
- 残る前提: 3入力一致でも誤ラベルはありうる。改善保証ではなく保守的な候補生成だけを行う。重大誤りの増加/品質悪化は許可済み5試験の比較で候補を棄却する。


## 2026-10-18 — 合成未ラベルpool追加
- `cpu_lab/materials/pool.jsonl` に内部生成の合成例36件を追加。全件JSONL parse成功、ID一意、`split=unlabeled`、`privacy_checked=true`、出典/ライセンス記載あり、label/verifiedフィールドなし。禁止セット由来・参照のパターン検査0件。
- GitHub Actions CPU lab safety tests run 39123051454 success（2026-10-18T11:23:37Z）。
- これは人が確認した教材や正解ラベルではない。現時点で候補poolだけが準備済みで、分類器checkpointが見つからずautolabelは未実行、CPU学習も未開始。
- Kaggle `kaggle/kaggle.request` は `fetch`。最新KAGGLE_LOGは2026-10-18T10:56:49ZのRUNNING行で止まり、より新しい完了状態は取れていない。GitHubの最新Kaggle fetch workflow run 39121167019はsuccessだがartifactなし。これはfetch処理の成功であってKaggle学習の完了証拠ではない。したがってCPU実験を開始せず、GPU学習との重複も避けている。


## 2026-10-18 — 学習準備と教材追跡をend-to-end化
- `.github/workflows/cpu-lab-material-learning.yml` を追加。成功済みKaggle runから `jitsuris-model` artifactを取得し、チェックポイントを検証、pool 36件を人手なしで仮ラベル化、0件なら安全に学習をスキップ、1件以上なら2 seedを同一CPU排他グループで逐次学習する。
- `cpu_lab/material_receipt.py`: poolのSHA、source model、全教材IDの候補化状態、pseudo候補数、訓練ログの追加行数を照合し、IDごとに`included_in_training`を記録する。記録は訓練データフローの証明で、意味的に習得した証明ではない。
- `cpu_lab/materials/progress_probe.jsonl`: 個人情報を含まない内部合成の正解付き診断probe 12件。訓練poolとID分離し、Kaggleの通常bundleにも含めず、学習前後の同じprobeで差分を計る。
- `cpu_lab/progress_probe.py`: 予測・正解数・誤り・改善/悪化caseを保存。固定5試験ではなく診断用probeと明記。最終採否は従来どおり許可済み固定5試験の結果で決める。
- `cpu_lab/tests/test_material_tracking.py` を追加。教材IDの整合、学習ログ確認、probeの差分判定、probe/poolの分離を検査。CI compile対象にもreceipt/probe scriptを追加した。
- 起動条件は成功済みKaggle e5-base checkpoint artifactが出てから。現時点で確認可能なmodel artifactがないため、まだ実学習は起動していない。人手によるラベル確認は不要。
