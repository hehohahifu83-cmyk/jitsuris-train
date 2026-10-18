# Jitsuris CPU Lab

ジツリスの教材整理と、CPUで行う独立した候補学習のための隔離領域です。Kaggle GPUの順番待ち中に準備を進める目的ですが、GPU側の実験と同じ学習を重複させたり、CPU学習を遅らせたりしないことを優先します。

## いまの段階

この場所と運用ルール、研究教材マップ、Jitsuris専用の優先教材パックを追加し、人手確認なしで仮ラベル候補を絞るコードを実装し、CPU safety testsで検証済みです。公開データセットや未ラベルpoolは未登録で、CPU候補学習はまだ未開始です。仮ラベルは正解と見なさず、固定5試験で別候補として評価します。

## 領域

- `materials/`: [優先教材パック](materials/learning-materials-priority-pack-2026-10-18.md)、出典・利用条件・確認日・対象列タイプを記録する公開教材/合成例。現在は調査資料と未確認の合成草案のみで、raw corpusや検証済みの新規訓練例はありません。
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
3. Actions の `CPU lab candidate replay` を `confirm_cpu=yes` で手動起動し、`automatic_pseudo` と候補JSONLを指定する。人手レビューは不要。仮ラベルは元の訓練行の最大1%までに制限し、2 seedを逐次実行する。
4. 許可済み固定5試験の正解率・誤り・重大誤り・unknown・時間・ピークメモリを比較する。差1.5ポイント未満は差なし。候補の自動採用はせず、悪化・重大誤り増加があれば棄却する。

`select/approve` による人手確認経路も残しています。機械仮ラベル経路では、出所・ライセンス・プライバシー・既存クラス・3入力一致・確信度・重複・1%上限を学習前に検査します。学習追加は `FT_CPU_LAB_PSEUDO` を明示したときだけ有効で、通常のKaggle依頼・既定モデル・製品コードは変更しません。CPUラボworkflowと既存CPU e5-base workflowは共通の `jitsuris-cpu-training` 排他グループで直列化します。

この方式は無人で候補を作れますが、仮ラベルの誤りをゼロにはできません。固定試験で測る独立候補としてのみ扱い、未見セットをプール・学習・調整に使いません。

## 次の作業

- 保存済み分類器checkpointの所在を確認し、許可条件が明確な小規模未ラベルpoolを用意して、自動仮ラベルの選択率と重複を試す。人手確認がない前提で、候補の棄却ゲートを先に検証する。
- 学習実行前にKaggleとGitHubの学習状態を確認し、同一/近似実験が走っていないことを確認する。
- Claudeが復帰したら教材のライセンス/重複/ラベル監査とキュー設計の独立レビューを依頼する。連絡箱の自動整理workflowが失敗中のため、メッセージがINBOXへ反映されたことは別途確認する。
- 初回学習と比較が終わるまで、候補は採用しない。
