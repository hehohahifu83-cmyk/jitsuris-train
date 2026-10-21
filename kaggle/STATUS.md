# 最新の学習・結果回収状況

- GitHub Actions run: [39579634852](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39579634852)
- 確認更新時刻 (UTC): 2026-10-21T09:47:24+00:00
- 依頼ファイル: `train hfmodel/intfloat__multilingual-e5-base 2 FT_LR=3e-5 FT_SEED=1 FT_VAL=1 FT_REAL_FRAC=0.25 ++ FT_REAL_FRAC=0.5 ++ FT_REAL_FRAC=1.0 ++ FT_SEED=2 FT_REAL_FRAC=0.25 ++ FT_REAL_FRAC=0.5 ++ FT_REAL_FRAC=1.0`
- Kaggle学習状態: 未確認（Kaggle の状態を取得できていない）
- Kaggle状態の最終観測時刻 (UTC): 2026-10-21T09:47:23Z
- Kaggle状態の根拠ログ: `今回の依頼はKaggleへのpush記録がないため、以前のKaggle状態を結び付けず未確認`
- 学習依頼ID: `unsubmitted-39579634852`
- Kaggleでの開始を観測した時刻 (UTC): 未観測
- Kaggleでの完了を観測した時刻 (UTC): 未観測
- 実学習の実行確認: 未確認
- 評価結果回収: 今回の更新なし（過去結果とは区別）
- 評価レポートartifact: 回収 artifact ID 12334849299（1ファイル）
- 学習済みモデル回収: artifact 未確認／未作成
- 判定手順: [STATUS_GUIDE.md](STATUS_GUIDE.md)

学習の開始はKaggleのRUNNING、学習完了はCOMPLETEで確認する。評価結果とモデルは別々に回収確認する。`kaggle.request=done`だけではモデルcheckpointが保存されたことを意味しない。
