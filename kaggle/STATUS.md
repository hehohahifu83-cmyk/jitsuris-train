# 最新の学習・結果回収状況

- 確認更新時刻 (UTC): 2026-10-18T23:05:02Z
- 依頼ファイル: `train intfloat/multilingual-e5-base 2 FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_CTX_UNIT=1 FT_FREEZE_EMB=1 FT_LR=2e-5 FT_SEED=1 ++ FT_SEED=2`
- Kaggle学習状態: 実行中（今回の依頼についてKaggleがRUNNINGを返答）
- Kaggle状態の最終観測時刻 (UTC): 2026-10-18T23:04:18Z
- Kaggle状態の根拠ログ: `jitsurio/jitsuris-train has status "KernelWorkerStatus.RUNNING"`
- Kaggle notebook: https://www.kaggle.com/code/jitsurio/jitsuris-train
- GitHub Actions run: [39174794327（in_progress）](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39174794327)
- 確認時点の実行中Kaggle学習: 1件（この実験）
- 今回の評価結果: 未回収（学習後に5固定セットで比較）
- 今回の評価レポートartifact: 未作成
- 今回の学習済みモデルartifact: 未作成
- 判定手順: [STATUS_GUIDE.md](STATUS_GUIDE.md)

今回の実験は e5-base、UNIT文脈、埋め込み固定を維持し、学習率を 2e-5 に変更したseed 1/2の比較。結果は dev220、general、business、business2、japan_procurement のみを集計し、精度・誤り数・重大誤り・不明数・所要時間・GPU最大メモリを比較する。差が1.5ポイント未満なら差なしと扱う。blind_set* と sets 3、5、7は読まない。

学習開始はKaggleのRUNNING、完了はCOMPLETEで判定する。GitHub Actionsの進行中表示や依頼ファイルの値だけでは開始・完了とみなさない。評価結果とモデルartifactは別々に確認する。
