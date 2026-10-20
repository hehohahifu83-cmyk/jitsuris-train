# ブラウザ用の書き出しの検査（GitHub Actions・CPU）

run: 39427927910　commit: d3f029245a581fec2259995f435e23d29853fd84　学習済みモデル:  ft_out_job1

# ブラウザ用に書き出したモデルの試験（intfloat/multilingual-e5-small）

- 残す単語片 21,772 個／全体 250,037 個（上位 K=0）。per_channel=False
- ファイルの大きさ：fp32 120.3MB／埋め込み表だけ INT8 95.3MB／さらに全結合層の重みも INT8＝重みだけ（model_quantized.onnx。72 個・21.2M 個の重み。計算は fp32）31.7MB／比較用の動的量子化（model_dyn8.onnx）31.3MB／tokenizer.json 0.6MB

| 版・組み合わせ | 開発用220 | 本物（一般） | 本物（業務） | 本物（業務2） | 本物（日本の調達） | 比較 |
|---|---|---|---|---|---|---|
| PyTorch fp32・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.000・logits の最大差 0.000（logits の広がり 0.031） |
| PyTorch fp32・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.000・logits の最大差 0.000（logits の広がり 0.031） |
| ONNX fp32・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.002・logits の最大差 0.043（logits の広がり 0.031） |
| ONNX fp32・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.002・logits の最大差 0.043（logits の広がり 0.031） |
| ONNX 埋め込みINT8・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.002・logits の最大差 0.043（logits の広がり 0.031） |
| ONNX 埋め込みINT8・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.002・logits の最大差 0.043（logits の広がり 0.031） |
| ONNX 埋め込みINT8＋全結合層INT8（重みだけ）・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.002・logits の最大差 0.043（logits の広がり 0.031） |
| ONNX 埋め込みINT8＋全結合層INT8（重みだけ）・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.002・logits の最大差 0.043（logits の広がり 0.031） |
| ONNX 埋め込みINT8＋全結合層INT8（動的量子化）・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.003・logits の最大差 0.043（logits の広がり 0.031） |
| ONNX 埋め込みINT8＋全結合層INT8（動的量子化）・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.003・logits の最大差 0.043（logits の広がり 0.031） |

- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX fp32）：平均 25ms・中央値 25ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX fp32）：平均 15ms・中央値 14ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX INT8 重みだけ（model_quantized.onnx））：平均 22ms・中央値 22ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX INT8 重みだけ（model_quantized.onnx））：平均 13ms・中央値 13ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX INT8 動的量子化（model_dyn8.onnx））：平均 13ms・中央値 12ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX INT8 動的量子化（model_dyn8.onnx））：平均 7ms・中央値 7ms／列（全 492 列の文の平均 96 トークン）
- ブラウザの試験の正解データ（reference.json）：モデルを流す文 40 文／トークナイザの番号だけを比べる文 566 文（試験の全列＋変わった文字列 74 個）

数字は GitHub Actions の CPU の結果で、ブラウザ（WASM）の実機の速さではない。精度は保存したモデルを書き出して試験に流した結果。

## ブラウザ（headless Chromium・WASM・Transformers.js）で動かした結果
```json
{
 "builds": [
  "transformers.web.min.js",
  "transformers.web.js",
  "transformers.min.js",
  "transformers.js"
 ],
 "importMap": {
  "onnxruntime-web": "/lib/ort.bundle.min.mjs",
  "onnxruntime-web/webgpu": "/lib/ort.webgpu.bundle.min.mjs",
  "onnxruntime-web/wasm": "/lib/ort.wasm.bundle.min.mjs",
  "onnxruntime-common": "/lib/ort.min.mjs"
 },
 "n": 40,
 "runs": [
  {
   "threads": 1,
   "isolated": true,
   "effectiveThreads": 1,
   "tokenizerLoadMs": 46,
   "loadMs": 978,
   "tokMsMean": 1.07,
   "idMismatch": 0,
   "maxLogitDiffVsOrtInt8": 0.0009,
   "maxLogitDiffVsOrtFp32": 0.0013,
   "argmaxAgreeVsOrtInt8": "40/40",
   "msPerColumnMean": 153.9,
   "msPerColumnMedian": 146.5,
   "msPerColumnP90": 187.2,
   "wallSeconds": 8.078
  },
  {
   "threads": 2,
   "isolated": true,
   "effectiveThreads": 2,
   "tokenizerLoadMs": 42,
   "loadMs": 985,
   "tokMsMean": 1.5,
   "idMismatch": 0,
   "maxLogitDiffVsOrtInt8": 0.0009,
   "maxLogitDiffVsOrtFp32": 0.0013,
   "argmaxAgreeVsOrtInt8": "40/40",
   "msPerColumnMean": 89.8,
   "msPerColumnMedian": 79,
   "msPerColumnP90": 107.7,
   "wallSeconds": 5.799
  },
  {
   "threads": 4,
   "isolated": true,
   "effectiveThreads": 4,
   "tokenizerLoadMs": 40,
   "loadMs": 1177,
   "tokMsMean": 1.3,
   "idMismatch": 0,
   "maxLogitDiffVsOrtInt8": 0.0009,
   "maxLogitDiffVsOrtFp32": 0.0013,
   "argmaxAgreeVsOrtInt8": "40/40",
   "msPerColumnMean": 81,
   "msPerColumnMedian": 65.6,
   "msPerColumnP90": 156.2,
   "wallSeconds": 5.511
  }
 ],
 "blocked": [],
 "console": [],
 "tried": [
  {
   "build": "transformers.web.min.js",
   "ready": true
  }
 ],
 "normalizer": "charsmap.mjs（表 237539 バイト）",
 "tokParity": {
  "total": 566,
  "edge": 74,
  "mismatches": 0,
  "mismatchesEdge": 0,
  "ms": 102,
  "first": []
 },
 "build": "transformers.web.min.js",
 "mismatches": [],
 "served": {
  "model_quantized.onnx": 31736000,
  "ort-wasm-simd-threaded.asyncify.wasm": 26861777,
  "tokenizer.json": 640791,
  "transformers.web.min.js": 454425,
  "ort.min.mjs": 368019,
  "charsmap.bin": 237539,
  "ort.webgpu.bundle.min.mjs": 117929,
  "ort-wasm-simd-threaded.asyncify.mjs": 53057,
  "charsmap.mjs": 6973,
  "config.json": 1371,
  "tokenizer_config.json": 392
 },
 "servedTotalMB": 60.5,
 "servedBrotliMB": 33.1,
 "wasmFiles": {
  "ort-wasm-simd-threaded.asyncify.wasm": 26.9,
  "ort-wasm-simd-threaded.jsep.wasm": 28.4,
  "ort-wasm-simd-threaded.jspi.wasm": 16.8,
  "ort-wasm-simd-threaded.wasm": 14.3
 },
 "dist": [
  [
   "ort-wasm-simd-threaded.jsep.mjs",
   "transformers.js",
   "transformers.min.js",
   "transformers.node.cjs",
   "transformers.node.min.cjs",
   "transformers.node.min.mjs",
   "transformers.node.mjs",
   "transformers.web.js",
   "transformers.web.min.js"
  ],
  [
   "ort-wasm-simd-threaded.asyncify.mjs",
   "ort-wasm-simd-threaded.asyncify.wasm",
   "ort-wasm-simd-threaded.jsep.mjs",
   "ort-wasm-simd-threaded.jsep.wasm",
   "ort-wasm-simd-threaded.jspi.mjs",
   "ort-wasm-simd-threaded.jspi.wasm",
   "ort-wasm-simd-threaded.mjs",
   "ort-wasm-simd-threaded.wasm",
   "ort.all.bundle.min.mjs",
   "ort.all.js",
   "ort.all.min.js",
   "ort.all.min.mjs",
   "ort.all.mjs",
   "ort.bundle.min.mjs",
   "ort.js",
   "ort.jspi.bundle.min.mjs",
   "ort.jspi.js",
   "ort.jspi.min.js",
   "ort.jspi.min.mjs",
   "ort.jspi.mjs",
   "ort.min.js",
   "ort.min.mjs",
   "ort.mjs",
   "ort.node.min.js",
   "ort.node.min.mjs",
   "ort.wasm.bundle.min.mjs",
   "ort.wasm.js",
   "ort.wasm.min.js",
   "ort.wasm.min.mjs",
   "ort.wasm.mjs",
   "ort.webgl.js",
   "ort.webgl.min.js",
   "ort.webgl.min.mjs",
   "ort.webgl.mjs",
   "ort.webgpu.bundle.min.mjs",
   "ort.webgpu.js",
   "ort.webgpu.min.js",
   "ort.webgpu.min.mjs",
   "ort.webgpu.mjs"
  ]
 ]
}```

## 正規化の一致（Chromium の中・軽い正解データ）
```
=== 要点（この下が注に出る）===
Chromium の中での正規化の一致試験（HeadlessChrome 156.0.8078.4・Intl.Segmenter あり）: 全 1123090 件中 不一致 0
1 文字（全スカラー値）: 1112064 件中 不一致 0
pairs: 3782 件中 不一致 0
triples: 1596 件中 不一致 0
random: 5500 件中 不一致 0
edge: 148 件中 不一致 0
```
