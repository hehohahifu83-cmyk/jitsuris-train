# ブラウザ用の書き出しの検査（GitHub Actions・CPU）

run: 39097868415　commit: 362ca7df2546da781d3545083193005a04ee23f3

# ブラウザ用に書き出したモデルの試験（intfloat/multilingual-e5-small）

- 残す単語片 21,772 個／全体 250,037 個（上位 K=0）。per_channel=False
- ファイルの大きさ：fp32 120.3MB／埋め込み表だけ INT8 95.3MB／さらに全結合層も INT8（model_quantized.onnx）31.3MB／tokenizer.json 1.0MB

| 版・組み合わせ | 開発用220 | 本物（一般） | 本物（業務） | 本物（業務2） | 本物（日本の調達） | 比較 |
|---|---|---|---|---|---|---|
| PyTorch fp32・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.000・logits の最大差 0.000（logits の広がり 0.034） |
| PyTorch fp32・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.000・logits の最大差 0.000（logits の広がり 0.034） |
| ONNX fp32・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 70.12%・確率の最大差 0.002・logits の最大差 0.040（logits の広がり 0.034） |
| ONNX fp32・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 70.12%・確率の最大差 0.002・logits の最大差 0.040（logits の広がり 0.034） |
| ONNX 埋め込みINT8・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 70.12%・確率の最大差 0.002・logits の最大差 0.040（logits の広がり 0.034） |
| ONNX 埋め込みINT8・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 70.12%・確率の最大差 0.002・logits の最大差 0.040（logits の広がり 0.034） |
| ONNX 埋め込みINT8＋全結合層INT8・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 65.04%・確率の最大差 0.003・logits の最大差 0.043（logits の広がり 0.034） |
| ONNX 埋め込みINT8＋全結合層INT8・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 65.04%・確率の最大差 0.003・logits の最大差 0.043（logits の広がり 0.034） |

- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX fp32）：平均 26ms・中央値 25ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX fp32）：平均 16ms・中央値 15ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX INT8（model_quantized.onnx））：平均 13ms・中央値 12ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX INT8（model_quantized.onnx））：平均 8ms・中央値 8ms／列（全 492 列の文の平均 96 トークン）
- ブラウザの試験の正解データ（reference.json）：40 文

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
   "tokenizerMs": 37,
   "loadMs": 890,
   "idMismatch": 3,
   "firstBad": {
    "i": 13,
    "got": [
     0,
     38,
     705,
     12,
     6,
     3418,
     902,
     12,
     6,
     1712,
     14842,
     311,
     501,
     1478,
     5972,
     8105,
     596,
     6,
     9168,
     6,
     8000,
     12,
     220,
     1592,
     4,
     6,
     16137,
     4,
     147,
     1546,
     4,
     5699,
     4,
     6,
     14380,
     6,
     9168,
     6,
     6567,
     2073
    ],
    "want": [
     0,
     38,
     705,
     12,
     6,
     3418,
     902,
     12,
     6,
     1712,
     14842,
     311,
     501,
     1478,
     5972,
     8105,
     596,
     6,
     9168,
     6,
     8000,
     12,
     220,
     1592,
     4,
     6,
     16137,
     4,
     147,
     1546,
     4,
     5699,
     4,
     6,
     14380,
     6,
     9168,
     6,
     6567,
     2073
    ]
   },
   "maxLogitDiffVsOrtInt8": 0.0067,
   "maxLogitDiffVsOrtFp32": 0.0117,
   "argmaxAgreeVsOrtInt8": "39/40",
   "msPerColumnMean": 73.7,
   "msPerColumnMedian": 64.4,
   "msPerColumnP90": 89.1,
   "wallSeconds": 4.639
  },
  {
   "threads": 2,
   "isolated": true,
   "effectiveThreads": 2,
   "tokenizerMs": 43,
   "loadMs": 945,
   "idMismatch": 3,
   "firstBad": {
    "i": 13,
    "got": [
     0,
     38,
     705,
     12,
     6,
     3418,
     902,
     12,
     6,
     1712,
     14842,
     311,
     501,
     1478,
     5972,
     8105,
     596,
     6,
     9168,
     6,
     8000,
     12,
     220,
     1592,
     4,
     6,
     16137,
     4,
     147,
     1546,
     4,
     5699,
     4,
     6,
     14380,
     6,
     9168,
     6,
     6567,
     2073
    ],
    "want": [
     0,
     38,
     705,
     12,
     6,
     3418,
     902,
     12,
     6,
     1712,
     14842,
     311,
     501,
     1478,
     5972,
     8105,
     596,
     6,
     9168,
     6,
     8000,
     12,
     220,
     1592,
     4,
     6,
     16137,
     4,
     147,
     1546,
     4,
     5699,
     4,
     6,
     14380,
     6,
     9168,
     6,
     6567,
     2073
    ]
   },
   "maxLogitDiffVsOrtInt8": 0.0067,
   "maxLogitDiffVsOrtFp32": 0.0117,
   "argmaxAgreeVsOrtInt8": "39/40",
   "msPerColumnMean": 51.2,
   "msPerColumnMedian": 48.5,
   "msPerColumnP90": 76.7,
   "wallSeconds": 3.571
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
 "build": "transformers.web.min.js",
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
