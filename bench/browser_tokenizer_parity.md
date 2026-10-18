# T5 tokenizer parity（d1c9f28）

## 結果

GitHub Actions の browser-model.yml Run 9（commit d1c9f28、2026-10-18 13:52 JST）を確認。Run summary は Success、browser test の export job は完了しています。Actions annotation のREPORTとbrowser_js要約では、試験文40件で長文切り詰め後の不一致は0/40でした。一方、全試験文と変化文字列を含む535文の tokenizer parity は **4件不一致**（通常文3件、edge文字列1件）です。変化文字列は43件中1件不一致です。

不一致は半角カナの濁点・半濁点と正規化に集中しています。例:
- 通常文: Pythonは「ク」+結合濁点に対し、JSは合成済みの「グ」を返す。
- 変化文字列「query: ｱｲｳｴｵ ﾊﾟﾋﾟﾌﾟ ｶﾞｷﾞ」: Python は半濁点付き片を分離し、JS は合成済み片を返す。

これはT5の残件です。Claudeが現在browser_test/charsmap.mjs、charsmap.test.mjs、fixture群などを修正中のため、同じファイルは触らず、再CI後にこの報告を更新します。失敗4件を「一致」とは扱いません。

## 他の実行指標（同じRun 9）

- WASM/Chromiumで動作、外部通信0件。
- モデル等の読み込み約1.4〜1.7秒。40文のtoken idは一致、ONNX INT8とのlogits最大差0.0041、top-1一致38/40。
- 1列あたり平均約107〜114ms（headless CI測定。スマートフォン実機の数字ではない）。
- workflowの全体はSuccess表示ですが、annotationに記録pushのrebase conflictもあり、更新結果はartifact/annotationから読んでいます。

## 根拠

GitHub Actions run: https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39098578939
annotationのbrowser_js / REPORT / recordを確認。artifact: browser-model-check（run 39098578939）。
