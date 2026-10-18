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