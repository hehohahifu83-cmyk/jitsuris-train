# ブラウザ版の取り込み量を減らす調査（2026-10-18）

## 現時点の基準

- 既存の headless Chromium 試験（run 39098438676、学習していない e5-small）では、配信対象は合計 60.1 MB。
- その内訳は量子化 ONNX 31.3 MB、ONNX Runtime の wasm 26.9 MB、tokenizer 1.0 MB、Transformers.js 0.45 MB、その他の JS/glue/config。
- これは GitHub Actions 上の試験であり、スマホ実機の通信量・速度ではない。
- d1c9f28 で tokenizer の切り詰め修正と追加文字列の ID 比較が入った。現在の browser_model_summary.md は修正前の run 39098438676 の記録のままなので、修正後の T5 判定はまだ出せない。

## 調べた方式と実装上の条件

ONNX Runtime Web は onnxruntime-web から直接 import し、InferenceSession と Tensor でモデルを実行できる。Transformers.js を外す試作は可能だが、ONNX Runtime 自体は残るため、26.9 MB の wasm が残る可能性が高い。専用の ort.wasm.min.mjs を使うだけでどれだけ削れるかは、同じ入力・同じ model.onnx で測定して確認する必要がある。

tokenizer.json の Unigram 語彙と score だけでは、Python と同じ token ID を保証できない。tokenizer の処理は少なくとも normalizer、pre-tokenizer、Unigram model、post-processor の順で構成される。自作 tokenizer はこの全処理と特殊 token の挿入を再現し、参照の全テスト文・追加文字列で token ID が完全一致した場合だけ候補にする。NFKC と空白処理だけの近似で進めると、今回見つかった末尾切り詰めとは別の不一致を隠すおそれがある。

## 次に行う比較

1. d1c9f28 の CI 結果が更新された後、まず T5 の ID 不一致数を確認する。
2. tokenizer.json の normalizer / pre-tokenizer / post-processor と特殊 token を列挙し、手書き Unigram で再現できる範囲を決める。
3. browser_test/run.mjs は残し、別ファイル browser_test/run_light.mjs で直接 ONNX Runtime Web を使う小さな試作を作る。
4. 同じモデル・同じ reference で全 ID、logits 差、外部通信、配信ファイル合計を比較する。ID が 1 件でも違う試作は採用候補にしない。
5. 測定結果が出るまで「軽量化した」とは扱わない。WASM を含む量と、圧縮転送時の量を分けて記録する。

## 公式資料

- ONNX Runtime Web の直接 import・ブラウザ対応: https://onnxruntime.ai/docs/get-started/with-javascript/web.html
- InferenceSession の input feeds / run() API: https://onnxruntime.ai/docs/api/js/interfaces/InferenceSession.html
- Hugging Face Tokenizers の normalizer、pre-tokenizer、モデル、post-processor の処理順: https://huggingface.co/docs/tokenizers/python/latest/pipeline.html
- Hugging Face Tokenizers の Unigram は候補の最良スコアを選ぶ分割方式: https://huggingface.co/docs/tokenizers/python/latest/components.html
