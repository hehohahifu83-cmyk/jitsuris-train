# Jitsuris CPU Lab

ジツリスの教材整理と、CPUで行う独立した候補学習のための隔離領域です。Kaggle GPUの順番待ち中に準備を進める目的ですが、GPU側の実験と同じ学習を重複させたり、CPU学習を遅らせたりしないことを優先します。

## いまの段階

この場所と運用ルール、研究教材マップ、Jitsuris専用の優先教材パック、未ラベル合成pool 36件を追加し、人手確認なしで仮ラベル候補を絞るコードを実装してCPU safety testsで検証済みです。モデルcheckpointが未取得のためautolabelとCPU候補学習はまだ未開始です。仮ラベルは正解と見なさず、固定5試験で別候補として評価します。

## 領域

- `materials/`: [優先教材パック](materials/learning-materials-priority-pack-2026-10-18.md)、`pool.jsonl`（内部生成・未ラベル合成例36件）、出典・利用条件・確認日・対象列タイプの記録。外部raw corpusや正解ラベル付きの新規訓練例はありません。
- `experiments/`: CPU学習の仮説、設定、使用した訓練データ版、seed、所要時間、メモリ、候補モデルの識別情報。
- `reports/`: 固定された許可済み5試験の結果、誤り分析、採否と未解決点。
- 大きな学習済みモデルはGitへ追加せず、GitHub Actionsの期限付きartifactに保存します。

## 隔離・非干渉ルール

1. ラボは `kaggle/kaggle.request`、通常の訓練データ、既定モデル、製品コードを書き換えません。採用には別途比較と記録が必要です。
2. Kaggleで同一モデル・同一条件のジョブがQUEUED/RUNNINGなら、同じ実験をCPUラボで重複開始しません。ログ上のqueue-timeoutだけではKaggle側が終了したと決めつけず、最新状態を確認します。
3. 既存の `.github/workflows/cpu-e5base-training.yml` とラボのCPU学習を同時に走らせません。ラボ用workflowは既存CPU e5-baseと共通の排他グループで直列化し、1実行だけにします。実行は初期段階では手動確認式にし、自動スケジュールは実測後に判断します。
4. 機械仮ラベルは正解データと区別し、出典・方式・信頼度を保持した候補としてのみ使います。
5. 許可済み固定5試験だけで採否を評価します。blind_set*、セット3・5・7は開かず、教材化・学習・調整に使いません。
6. 各試験の前後でCPU学習の時間・CPU使用率・メモリを記録し、既存CPU学習への影響が出たらラボ側を止めます。

## 自己学習の補助プログラム

`cpu_lab/self_learning.py` には、人手レビュー経路と、人手確認なしの仮ラベル経路があります。後者は同じ分類器で値の並びだけを変えた3入力を採点し、全て同じクラスを確率0.995以上、1位と2位の差0.50以上で予測した例だけを出力します。これは正解の証明ではありません。各例を `verified=false` の機械仮ラベルとして区別します。

1. 利用条件・個人情報を確認した未ラベルpoolを用意する。各行に `id, header, values, source, license, split, privacy_checked` が必要。splitは `unlabeled` のみ。
2. 保存済みのJitsuris分類器checkpointとpoolから候補を作る:
   `python cpu_lab/self_learning.py autolabel --model <checkpoint> --pool cpu_lab/materials/pool.jsonl --out cpu_lab/materials/pseudo_replay/candidate.jsonl`
3. `CPU lab material learning` workflowを手動起動し、完了済みKaggle e5-base run IDとcheckpoint directoryを指定する。人手のラベル確認は不要。run IDのcheckpointから自動で仮ラベルを作り、仮ラベルは元訓練行の最大1%までに制限し、2 seedを逐次実行する。候補が0件なら学習を自動スキップする。
4. 各教材IDについて、未選択/仮ラベル候補/学習投入確認のreceiptを作る。開始前・学習後に合成の進捗probeも測り、性能変化の根拠を残す。これは学習工程へ入ったこととprobe上の変化の確認であり、モデル内部での意味的習得を証明するものではない。許可済み固定5試験の正解率・誤り・重大誤り・unknown・時間・ピークメモリが最終判断。差1.5ポイント未満は差なし。候補は自動採用しない。

`select/approve` による人手確認経路も残しています。機械仮ラベル経路では、出所・ライセンス・プライバシー・既存クラス・3入力一致・確信度・重複・1%上限を学習前に検査します。学習追加は `FT_CPU_LAB_PSEUDO` を明示したときだけ有効で、通常のKaggle依頼・既定モデル・製品コードは変更しません。CPUラボworkflowと既存CPU e5-base workflowは共通の `jitsuris-cpu-training` 排他グループで直列化します。

この方式は無人で候補を作れますが、仮ラベルの誤りをゼロにはできません。固定試験で測る独立候補としてのみ扱い、未見セットをプール・学習・調整に使いません。

## 教材の処理・習得状況の確認

- `cpu_lab/material_receipt.py` は各pool IDについて「仮ラベル門を通ったか」「学習ログ上で学習投入が確認できたか」をSHA256と一緒に記録する。
- `cpu_lab/progress_probe.py` は学習前後で同じ合成probeを採点し、正解数・誤り・変化したケースを記録する。probeは合成の診断用で、訓練には使わない。これはモデル内部の習得を直接観察するものではなく、学習投入の証拠と行動上の変化を分けて示す。
- `CPU lab material learning` workflowは二seedを直列実行し、準備/学習receipt、仮ラベル教材、前後probe、固定5試験の結果/誤り記録をartifactに保存する。開始には完了済みKaggle e5-base checkpointを含むGitHub Actions run IDが必要。現在はそのcheckpoint artifactが見つかっていないため、学習は未開始。

## 次の作業

- 完了済みKaggle e5-base runが`jitsuris-model` artifactを生成したら、そのrun IDとcheckpoint directoryを指定してCPU lab workflowを起動する。
- 学習実行前にKaggleとGitHubの学習状態を確認し、同一/近似実験が走っていないことを確認する。
- Claudeが復帰したら教材のライセンス/重複/ラベル監査とキュー設計の独立レビューを依頼する。連絡箱の自動整理workflowが失敗中のため、メッセージがINBOXへ反映されたことは別途確認する。
- 初回学習と比較が終わるまで、候補は採用しない。
