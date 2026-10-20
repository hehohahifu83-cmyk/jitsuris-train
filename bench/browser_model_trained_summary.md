# ブラウザ用の書き出しの検査（GitHub Actions・CPU）

run: 39432505584　commit: 6b64d531edc227f43dee8cb055971ecefc3a53e9　学習済みモデル: 39098438731 ft_out_job4

# ブラウザ用に書き出したモデルの試験（trained/ft_out_job4）

- 残す単語片 21,772 個／全体 250,037 個（上位 K=0）。per_channel=False
- ファイルの大きさ：fp32 120.3MB／埋め込み表だけ INT8 95.3MB／さらに全結合層の重みも INT8＝重みだけ（model_quantized.onnx。72 個・21.2M 個の重み。計算は fp32）31.7MB／比較用の動的量子化（model_dyn8.onnx）31.3MB／tokenizer.json 0.6MB

| 版・組み合わせ | 開発用220 | 本物（一般） | 本物（業務） | 本物（業務2） | 本物（日本の調達） | 比較 |
|---|---|---|---|---|---|---|
| PyTorch fp32・微調整だけ | 開発用220 正81.8% 誤9 不明31 重大1 | 本物（一般） 正84.7% 誤12 不明33 重大3 | 本物（業務） 正89.9% 誤39 不明9 重大9 | 本物（業務2） 正92.9% 誤36 不明29 重大16 | 本物（日本の調達） 正96.7% 誤1 不明2 重大1 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.000・logits の最大差 0.000（logits の広がり 1.924） |
| PyTorch fp32・微調整7割＋今の仕組み3割 | 開発用220 正82.7% 誤7 不明31 重大1 | 本物（一般） 正85.1% 誤8 不明36 重大2 | 本物（業務） 正89.9% 誤38 不明10 重大9 | 本物（業務2） 正93.2% 誤36 不明26 重大16 | 本物（日本の調達） 正96.7% 誤0 不明3 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.000・logits の最大差 0.000（logits の広がり 1.924） |
| ONNX fp32・微調整だけ | 開発用220 正82.7% 誤6 不明32 重大1 | 本物（一般） 正84.4% 誤13 不明33 重大4 | 本物（業務） 正90.3% 誤36 不明10 重大9 | 本物（業務2） 正93.3% 誤33 不明28 重大12 | 本物（日本の調達） 正97.8% 誤0 不明2 重大0 | PyTorch fp32 との top-1 一致 97.18%・確率の最大差 0.927・logits の最大差 4.181（logits の広がり 1.924） |
| ONNX fp32・微調整7割＋今の仕組み3割 | 開発用220 正85.5% 誤6 不明26 重大1 | 本物（一般） 正85.8% 誤8 不明34 重大1 | 本物（業務） 正90.1% 誤34 不明13 重大8 | 本物（業務2） 正93.8% 誤30 不明27 重大11 | 本物（日本の調達） 正98.9% 誤0 不明1 重大0 | PyTorch fp32 との top-1 一致 97.18%・確率の最大差 0.927・logits の最大差 4.181（logits の広がり 1.924） |
| ONNX 埋め込みINT8・微調整だけ | 開発用220 正82.7% 誤6 不明32 重大1 | 本物（一般） 正84.4% 誤13 不明33 重大4 | 本物（業務） 正90.3% 誤35 不明11 重大9 | 本物（業務2） 正93.3% 誤34 不明27 重大12 | 本物（日本の調達） 正97.8% 誤0 不明2 重大0 | PyTorch fp32 との top-1 一致 97.27%・確率の最大差 0.929・logits の最大差 4.202（logits の広がり 1.924） |
| ONNX 埋め込みINT8・微調整7割＋今の仕組み3割 | 開発用220 正85.5% 誤6 不明26 重大1 | 本物（一般） 正85.4% 誤8 不明35 重大1 | 本物（業務） 正90.1% 誤34 不明13 重大8 | 本物（業務2） 正93.8% 誤29 不明28 重大11 | 本物（日本の調達） 正98.9% 誤0 不明1 重大0 | PyTorch fp32 との top-1 一致 97.27%・確率の最大差 0.929・logits の最大差 4.202（logits の広がり 1.924） |
| ONNX 埋め込みINT8＋全結合層INT8（重みだけ）・微調整だけ | 開発用220 正82.7% 誤6 不明32 重大1 | 本物（一般） 正84.4% 誤13 不明33 重大4 | 本物（業務） 正90.3% 誤36 不明10 重大9 | 本物（業務2） 正93.5% 誤32 不明27 重大11 | 本物（日本の調達） 正97.8% 誤0 不明2 重大0 | PyTorch fp32 との top-1 一致 97.18%・確率の最大差 0.908・logits の最大差 4.176（logits の広がり 1.924） |
| ONNX 埋め込みINT8＋全結合層INT8（重みだけ）・微調整7割＋今の仕組み3割 | 開発用220 正85.5% 誤6 不明26 重大1 | 本物（一般） 正85.1% 誤7 不明37 重大1 | 本物（業務） 正90.3% 誤34 不明12 重大8 | 本物（業務2） 正93.9% 誤29 不明27 重大10 | 本物（日本の調達） 正98.9% 誤0 不明1 重大0 | PyTorch fp32 との top-1 一致 97.18%・確率の最大差 0.908・logits の最大差 4.176（logits の広がり 1.924） |
| ONNX 埋め込みINT8＋全結合層INT8（動的量子化）・微調整だけ | 開発用220 正81.8% 誤8 不明32 重大1 | 本物（一般） 正81.4% 誤17 不明38 重大4 | 本物（業務） 正90.1% 誤37 不明10 重大6 | 本物（業務2） 正93.1% 誤34 不明29 重大11 | 本物（日本の調達） 正96.7% 誤0 不明3 重大0 | PyTorch fp32 との top-1 一致 96.71%・確率の最大差 0.950・logits の最大差 6.856（logits の広がり 1.924） |
| ONNX 埋め込みINT8＋全結合層INT8（動的量子化）・微調整7割＋今の仕組み3割 | 開発用220 正84.1% 誤8 不明27 重大1 | 本物（一般） 正84.1% 誤16 不明31 重大3 | 本物（業務） 正90.3% 誤33 不明13 重大5 | 本物（業務2） 正93.4% 誤29 不明31 重大10 | 本物（日本の調達） 正96.7% 誤0 不明3 重大0 | PyTorch fp32 との top-1 一致 96.71%・確率の最大差 0.950・logits の最大差 6.856（logits の広がり 1.924） |

- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX fp32）：平均 62ms・中央値 60ms／列（全 2161 列の文の平均 89 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX fp32）：平均 34ms・中央値 33ms／列（全 2161 列の文の平均 89 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX INT8 重みだけ（model_quantized.onnx））：平均 92ms・中央値 91ms／列（全 2161 列の文の平均 89 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX INT8 重みだけ（model_quantized.onnx））：平均 50ms・中央値 49ms／列（全 2161 列の文の平均 89 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX INT8 動的量子化（model_dyn8.onnx））：平均 40ms・中央値 39ms／列（全 2161 列の文の平均 89 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX INT8 動的量子化（model_dyn8.onnx））：平均 22ms・中央値 22ms／列（全 2161 列の文の平均 89 トークン）
- ブラウザの試験の正解データ（reference.json）：モデルを流す文 40 文／トークナイザの番号だけを比べる文 2235 文（試験の全列＋変わった文字列 74 個）

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
   "tokenizerLoadMs": 65,
   "loadMs": 1765,
   "tokMsMean": 2.46,
   "idMismatch": 0,
   "maxLogitDiffVsOrtInt8": 0.042,
   "maxLogitDiffVsOrtFp32": 0.086,
   "argmaxAgreeVsOrtInt8": "40/40",
   "msPerColumnMean": 241.3,
   "msPerColumnMedian": 236.2,
   "msPerColumnP90": 304.4,
   "wallSeconds": 12.754
  },
  {
   "threads": 2,
   "isolated": true,
   "effectiveThreads": 2,
   "tokenizerLoadMs": 75,
   "loadMs": 2026,
   "tokMsMean": 2.37,
   "idMismatch": 0,
   "maxLogitDiffVsOrtInt8": 0.042,
   "maxLogitDiffVsOrtFp32": 0.086,
   "argmaxAgreeVsOrtInt8": "40/40",
   "msPerColumnMean": 144,
   "msPerColumnMedian": 133.2,
   "msPerColumnP90": 201.7,
   "wallSeconds": 8.609
  },
  {
   "threads": 4,
   "isolated": true,
   "effectiveThreads": 4,
   "tokenizerLoadMs": 61,
   "loadMs": 1991,
   "tokMsMean": 1.86,
   "idMismatch": 0,
   "maxLogitDiffVsOrtInt8": 0.042,
   "maxLogitDiffVsOrtFp32": 0.086,
   "argmaxAgreeVsOrtInt8": "40/40",
   "msPerColumnMean": 117.4,
   "msPerColumnMedian": 110.8,
   "msPerColumnP90": 160.7,
   "wallSeconds": 9.873
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
  "total": 2235,
  "edge": 74,
  "mismatches": 0,
  "mismatchesEdge": 0,
  "ms": 696,
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
  "config.json": 1440,
  "tokenizer_config.json": 495
 },
 "servedTotalMB": 60.5,
 "servedBrotliMB": 33.7,
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

## 学習済みモデルの確認（重みの SHA-256・manifest・依頼との照合）
```json
{
 "model_dir": "trained/ft_out_job4",
 "weights": {
  "model.safetensors": {
   "sha256": "a23aaf2c1870e7798dbf6d20811d895b9a15e57c5aa5388da102a67c8f374f82",
   "bytes": 470663224
  }
 },
 "weights_sha256": "a23aaf2c1870e7798dbf6d20811d895b9a15e57c5aa5388da102a67c8f374f82",
 "manifest": null,
 "problems": [],
 "warnings": [
  "manifest.json が無い（学習の記録なし。版 31 以前の回収か、記録の書き出しに失敗）"
 ],
 "ok": true
}
```
