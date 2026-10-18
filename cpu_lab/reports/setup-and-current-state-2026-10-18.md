# CPUラボ初期セットアップ記録（2026-10-18）

## 作成した領域
- `cpu_lab/README.md`: 目的、用途分離、KaggleとCPUワークフローとの重複・競合防止、採用前評価のルール。
- `cpu_lab/materials/README.md`: 出典・利用条件・個人情報・未見試験の持込み制限。
- `cpu_lab/materials/column-type-research-map.md`: Sherlock、Sato、TURL、Permutation Invariant Strategy、DODUOを参考文献として整理。研究要点とCPU向け優先順位を記録。データセット・モデル重みは取り込んでいない。
- `cpu_lab/experiments/README.md` と `cpu_lab/reports/README.md`: 独立実験記録と結果・エラー原因の記録項目。

## 非干渉の設計
現在のCPUワークフロー `.github/workflows/cpu-e5base-training.yml` はe5-base seed 1/2を使う。Kaggle側でも同じか近い条件がQUEUEDの可能性があるため、重複する学習はしない。今後ラボ用workflowを作る段階で、既存CPU workflowと共通の排他グループ、単一実行、手動開始、期限付きartifact、CPU時間/壁時計時間/ピークメモリ計測を実装する。

これらの排他機能はまだ実装されていない。教材の配置と記録スペースを作った段階であり、CPU学習も自動学習も起動していない。次はまず教材の利用条件を確認し、別候補の訓練例を作る。GPU実験と同一の設定・モデルを重ねない。

## Claudeへの依頼状態
ai-bridgeにClaude宛て依頼ファイル `messages/20261018-1949_chatgpt-to-claude_cpu-lab-materials.md` を作成した。ファイル名・必須見出し・本文のsecret patternはローカル検査上合格（secret hit 0）。しかし ai-bridge workflow run 39120861818（再試行含む）が失敗し、GitHubから実行ログを取得できなかった。さらに README/STATE更新を契機としたruns 39121062324・39121064227も失敗した。個別メッセージに限らない自動整理workflow全体の問題が疑われるが、原因はログ不足で未確定。INBOX.mdは更新されておらず、Claude宛て未読一覧への反映および受領は未確認。よってClaudeが受け取ったとは扱わない。次の連絡ではユーザーにも未達を伝える。

## 未完了
1. ai-bridgeのworkflow失敗理由を特定する（既存形式不備かテスト・環境かは未確定）。
2. 正常にINBOXへ反映されたことを確認後、ユーザーへClaudeに「連絡箱」と送るタイミングを伝える。
3. Claude提案を受領したら、出典・ライセンス・重複・PIIを確認して教材化。
4. CPU用workflowを作成し、既存CPU e5-base workflowとの排他とCPU使用計測を動作確認。
