# Kaggle 学習状態の確認手順

## まず見る場所

- [STATUS.md](STATUS.md)：直近の確認結果。状態・観測時刻・根拠になったKaggleログ・結果回収・モデル回収を分けて記録する。
- [GitHub Actions の実行履歴](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/workflows/kaggle.yml)：処理中のログ、失敗した工程、成果物のダウンロード先。
- [Kaggle notebook](https://www.kaggle.com/code/jitsurio/jitsuris-train)：Kaggle側の現在状態と実行画面。
- [KAGGLE_LOG.md](KAGGLE_LOG.md)：時刻付きの状態履歴。
- [PROGRESS.md](PROGRESS.md)：実行中に定期更新する途中経過。

## 状態の判定

| 表示 | 意味 | 判定根拠 |
|---|---|---|
| 未依頼 | 学習依頼が出ていない | `kaggle.request` が `done` で、実行中の依頼なし |
| 待機中 | KaggleがGPU割当待ち | 最新状態ログが `KernelWorkerStatus.QUEUED` |
| 実行中 | Kaggleでカーネルが動作中 | 最新状態ログが `KernelWorkerStatus.RUNNING` |
| 学習完了 | Kaggleカーネルが正常終了 | 最新状態ログが `KernelWorkerStatus.COMPLETE` |
| 失敗 | Kaggleカーネルが異常終了 | 最新状態ログが `KernelWorkerStatus.ERROR` |
| キャンセル | Kaggleが実行をキャンセル | 最新状態ログが `CANCELED` または `CANCELLED` |
| 未確認 | Kaggleの新しい状態を取得できていない | `done` などの依頼ファイルだけでは完了とみなさない |

「依頼を受け付けた」「GitHub Actionsが動いている」「KaggleがRUNNINGになった」は別の段階です。Kaggleの `RUNNING` が記録されて初めて「学習開始」、`COMPLETE` が記録されて初めて「学習完了」とします。

## 結果の回収も別に確認

学習完了後、次の項目を別々に見ます。

1. **学習状態**：Kaggleが `COMPLETE` を返したか。
2. **評価結果**：今回の実行で `FINETUNE_RESULTS.md` が更新されたか。過去結果の存在を今回の回収と取り違えない。
3. **評価レポート**：Actions実行の `jitsuris-evaluation-reports` artifact が作られたか。
4. **モデルcheckpoint**：Actions実行の `jitsuris-model` artifact IDが記録され、artifactを開けるか。

`kaggle.request=done` は依頼処理が終わったことを示すだけで、モデルや評価結果の回収保証ではありません。モデルartifactが空、またはIDなしなら「モデル回収済み」と扱いません。

## 待機が長いとき

GitHub ActionsはKaggleの待ち時間を無制限に占有しません。待機上限でActionsが止まってもKaggle側が `QUEUED` のまま残る場合があります。その場合は「学習中」ではなく「Kaggle GPU割当待ち」とし、次回の定期チェックで状態確認・結果回収を続けます。Actionsの成否だけでKaggle学習の成否を決めません。

## 報告に必ず含める項目

- Kaggleの判定状態と、その根拠となる生の `KernelWorkerStatus`
- その状態を確認したUTC時刻
- GitHub Actions runへのリンクと成否
- `kaggle.request` の値
- 今回の評価結果更新の有無
- 評価レポートartifact IDとモデルartifact ID（なければ未回収と明記）

この確認では `blind_set*`、sets 3、5、7を読まない。
