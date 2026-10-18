# 最新の学習・結果回収状況

更新確認日: 2026-10-18 (UTC)

## 直近のKaggle実験

- 対象: e5-base、UNIT context、埋め込み凍結、seed 1/2
- Kaggle状態: COMPLETE。学習ループは499秒/486秒、最大GPUメモリは各3.5 GiB。
- GitHub Actions: [run 39136346612 成功](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39136346612)
- 依頼状態: `kaggle/kaggle.request = done`
- 評価結果: [FINETUNE_RESULTS.md](../FINETUNE_RESULTS.md) に固定5セットの2 seed結果を追記済み。
- 評価レポート: [80ファイル、554,312 bytesのartifact](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39136346612/artifacts/12139184078)。保持期限は2026-11-17 14:32 UTC。
- 学習済みモデル: 未回収。GitHub Actionsログに `/tmp/model` が空と記録され、モデルartifactは作成されなかった。
- CPU lab: [run 39136475753](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39136475753) の確認処理は成功したが、Kaggle kernelが既にCOMPLETEでQUEUEDではなかったため、CPU学習jobはスキップ。CPU Labによる能力改善はまだ実行・確認されていない。

## 能力変化の見方

seed 1/2の精度差は最大1.3ポイントで、事前に定めた1.5ポイント未満は「差なし」の扱い。UNITのみの対応seedとの比較では、埋め込み凍結による一貫した精度向上は確認できていない。一方、学習時間は約9〜11%短縮し、最大GPUメモリは5.5 GiBから3.5 GiBへ低下。したがって、今回確認できた改善は速度・メモリであり、分類能力の向上とは分けて評価する。

## 今後の状態確認欄

次回のKaggle実行後、このファイルはworkflowが更新します。次の項目を別々に読みます。

1. Kaggle kernelがCOMPLETEか（学習終了）
2. FINETUNE_RESULTS.mdが今回更新されたか（評価結果回収）
3. 評価JSON artifact IDがあるか（エラー・確率レポート保存）
4. jitsuris-model artifact IDがありcheckpointが入っているか（モデル保存）
5. CPU Labのworkflow summaryが実際の学習job完了を示すか（補助学習）

`kaggle.request=done`単独では、2〜5を証明しません。現在は新たな学習依頼を出していません。
