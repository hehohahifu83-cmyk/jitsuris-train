# Jitsuris CPU Lab

ジツリスの教材整理と、CPUで行う独立した候補学習のための隔離領域です。Kaggle GPUの順番待ち中に準備を進める目的ですが、GPU側の実験と同じ学習を重複させたり、CPU学習を遅らせたりしないことを優先します。

## いまの段階

この場所と運用ルールを作成しました。研究教材マップは追加しましたが、公開データセットや実際の訓練教材、CPU候補学習ジョブはこれからです。教材ファイルを置くだけではモデルの重みは変わりません。教材を訓練例に変換し、CPU上の別候補として学習・評価する工程を接続して初めて学習になります。

## 領域

- `materials/`: 出典・ライセンス・取得日・対象列タイプを記録した公開教材と合成例。顧客データ、個人情報、未見試験データは保存しません。
- `experiments/`: CPU学習の仮説、設定、使用した訓練データ版、seed、所要時間、メモリ、候補モデルの識別情報。
- `reports/`: 固定された許可済み5試験の結果、誤り分析、採否と未解決点。
- 大きな学習済みモデルはGitへ追加せず、GitHub Actionsの期限付きartifactに保存します。

## 隔離・非干渉ルール

1. ラボは `kaggle/kaggle.request`、通常の訓練データ、既定モデル、製品コードを書き換えません。採用には別途比較と記録が必要です。
2. Kaggleで同一モデル・同一条件のジョブがQUEUED/RUNNINGなら、同じ実験をCPUラボで重複開始しません。ログ上のqueue-timeoutだけではKaggle側が終了したと決めつけず、最新状態を確認します。
3. 既存の `.github/workflows/cpu-e5base-training.yml` とラボのCPU学習を同時に走らせません。ラボ用ワークフローを追加するとき、両方に共通の排他グループを設定し、1実行だけにします。実行は初期段階では手動確認式にし、自動スケジュールは実測後に判断します。
4. 誤答を使った自己学習やAI生成ラベルは、出典・生成方法・確認状況を分け、未監査のまま正解ラベルへ混ぜません。
5. 許可済み固定5試験だけで採否を評価します。blind_set*、セット3・5・7は開かず、教材化・学習・調整に使いません。
6. 各試験の前後でCPU学習の時間・CPU使用率・メモリを記録し、既存CPU学習への影響が出たらラボ側を止めます。

## 自己学習の補助プログラム

`cpu_lab/self_learning.py` は既存の分類器でラベルなしの公開/合成列を採点し、情報量が高く重複の少ない候補を人手確認キューへ出します。確率上位・不確実度は確認の優先順位であり、正解ラベルとしては扱いません。

1. 許可された訓練候補だけをJSONLへ用意する。各行に `id, header, values, source, license, split, privacy_checked` が必要。splitは `unlabeled` または `train`。個人情報を含めず、利用条件を確認する。
2. `python cpu_lab/self_learning.py select --model ft_out --pool cpu_lab/materials/pool.jsonl --out cpu_lab/materials/review_queue.jsonl --budget 100`
3. 人が根拠を確認した行だけ、`review.status=approved`, `review.label`, `review.reviewer`, `review.verified=true` を設定する。未確認・AI擬似ラベルは出力できない。
4. `python cpu_lab/self_learning.py approve --reviewed cpu_lab/materials/review_queue.jsonl --out cpu_lab/materials/verified_replay/approved.jsonl`
5. 承認済みJSONLをリポジトリに保存してから、Actions の `CPU lab verified active-learning replay` を `confirm_cpu=yes` で手動起動する。固定済み5試験は結果測定専用で訓練追加行にしない。2 seedを逐次実行し、結果・誤り・ログ・教材版を7日間のartifactへ保存する。

学習への追加は `FT_CPU_LAB_REPLAY` を明示したときだけ有効。人手確認・出典・ライセンス・プライバシー・既存ラベル集合を再検査し、不正な行は学習前に停止します。通常Kaggle依頼や既定モデルには触れず、既定モデルへの昇格も行いません。CPUラボworkflowと既存CPU e5-base workflowは共通の `jitsuris-cpu-training` 排他グループで直列化します。

この仕組みは完全自律の自己改変ではなく、人が確認した教材だけで候補を更新する能動学習ループです。評価データ混入と未確認の誤ラベルを防ぎながら、全件を一律学習する代わりに次に確認すべき例を優先します。

## 次の作業

- まず小さい公開または合成プールを作り、選択・人手確認・承認・再読込を練習する。
- 学習実行前にKaggleとGitHubの学習状態を確認し、同一/近似実験が走っていないことを確認する。
- Claudeが復帰したら教材のライセンス/重複/ラベル監査とキュー設計の独立レビューを依頼する。連絡箱の自動整理workflowが失敗中のため、メッセージがINBOXへ反映されたことは別途確認する。
- 初回学習と比較が終わるまで、候補は採用しない。
