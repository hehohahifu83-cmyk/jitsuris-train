# ブラウザ用の書き出しの検査（GitHub Actions・CPU）

run: 39098438676　commit: 9b6e0918af1d6deb259a11ff13a2bdc406461b5c　学習済みモデル:  

# ブラウザ用に書き出したモデルの試験（intfloat/multilingual-e5-small）

- 残す単語片 21,772 個／全体 250,037 個（上位 K=0）。per_channel=False
- ファイルの大きさ：fp32 120.3MB／埋め込み表だけ INT8 95.3MB／さらに全結合層も INT8（model_quantized.onnx）31.3MB／tokenizer.json 1.0MB

| 版・組み合わせ | 開発用220 | 本物（一般） | 本物（業務） | 本物（業務2） | 本物（日本の調達） | 比較 |
|---|---|---|---|---|---|---|
| PyTorch fp32・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.000・logits の最大差 0.000（logits の広がり 0.025） |
| PyTorch fp32・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.000・logits の最大差 0.000（logits の広がり 0.025） |
| ONNX fp32・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 67.28%・確率の最大差 0.003・logits の最大差 0.045（logits の広がり 0.025） |
| ONNX fp32・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 67.28%・確率の最大差 0.003・logits の最大差 0.045（logits の広がり 0.025） |
| ONNX 埋め込みINT8・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 67.28%・確率の最大差 0.003・logits の最大差 0.045（logits の広がり 0.025） |
| ONNX 埋め込みINT8・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 67.28%・確率の最大差 0.003・logits の最大差 0.045（logits の広がり 0.025） |
| ONNX 埋め込みINT8＋全結合層INT8・微調整だけ | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 68.90%・確率の最大差 0.003・logits の最大差 0.044（logits の広がり 0.025） |
| ONNX 埋め込みINT8＋全結合層INT8・微調整7割＋今の仕組み3割 | 開発用220 正0.0% 誤0 不明100 重大0 | 本物（一般） 正0.0% 誤0 不明80 重大0 | 本物（業務） 正0.0% 誤0 不明98 重大0 | 本物（業務2） 正0.0% 誤0 不明94 重大0 | 本物（日本の調達） 正0.0% 誤0 不明92 重大0 | PyTorch fp32 との top-1 一致 68.90%・確率の最大差 0.003・logits の最大差 0.044（logits の広がり 0.025） |

- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX fp32）：平均 62ms・中央値 62ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX fp32）：平均 34ms・中央値 33ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX INT8（model_quantized.onnx））：平均 40ms・中央値 39ms／列（全 492 列の文の平均 96 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX INT8（model_quantized.onnx））：平均 23ms・中央値 22ms／列（全 492 列の文の平均 96 トークン）
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
   "tokenizerLoadMs": 55,
   "loadMs": 1452,
   "tokMsMean": 1.77,
   "idMismatch": 3,
   "maxLogitDiffVsOrtInt8": 0.0059,
   "maxLogitDiffVsOrtFp32": 0.0113,
   "argmaxAgreeVsOrtInt8": "38/40",
   "msPerColumnMean": 109.2,
   "msPerColumnMedian": 103.4,
   "msPerColumnP90": 140.5,
   "wallSeconds": 6.348
  },
  {
   "threads": 2,
   "isolated": true,
   "effectiveThreads": 2,
   "tokenizerLoadMs": 52,
   "loadMs": 1432,
   "tokMsMean": 1.16,
   "idMismatch": 3,
   "maxLogitDiffVsOrtInt8": 0.0059,
   "maxLogitDiffVsOrtFp32": 0.0113,
   "argmaxAgreeVsOrtInt8": "38/40",
   "msPerColumnMean": 114.8,
   "msPerColumnMedian": 97.3,
   "msPerColumnP90": 127.5,
   "wallSeconds": 7.788
  },
  {
   "threads": 4,
   "isolated": true,
   "effectiveThreads": 4,
   "tokenizerLoadMs": 56,
   "loadMs": 1665,
   "tokMsMean": 2.1,
   "idMismatch": 3,
   "maxLogitDiffVsOrtInt8": 0.0059,
   "maxLogitDiffVsOrtFp32": 0.0113,
   "argmaxAgreeVsOrtInt8": "38/40",
   "msPerColumnMean": 105.7,
   "msPerColumnMedian": 75.1,
   "msPerColumnP90": 196.1,
   "wallSeconds": 7.219
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
 "mismatches": [
  {
   "i": 13,
   "firstDiff": 127,
   "lenGot": 128,
   "lenWant": 128,
   "got": [
    "外",
    "からの",
    "転"
   ],
   "want": [
    "外",
    "からの",
    "</s>"
   ],
   "gotIds": [
    977,
    5972,
    8105
   ],
   "wantIds": [
    977,
    5972,
    2
   ],
   "codepoints": [
    "U+5217",
    "U+540D",
    "U+793E",
    "U+4F1A",
    "U+52D5",
    "U+614B",
    "U+4ED6",
    "U+533A",
    "U+304B",
    "U+3089",
    "U+306E",
    "U+8EE2"
   ]
  },
  {
   "i": 34,
   "firstDiff": 127,
   "lenGot": 128,
   "lenWant": 128,
   "got": [
    "▁",
    "契約",
    "番号"
   ],
   "want": [
    "▁",
    "契約",
    "</s>"
   ],
   "gotIds": [
    6,
    7265,
    12971
   ],
   "wantIds": [
    6,
    7265,
    2
   ],
   "codepoints": [
    "U+5217",
    "U+540D",
    "U+5DE5",
    "U+4E8B",
    "U+FF08",
    "U+59D4",
    "U+8A17",
    "U+FF09",
    "U+5024",
    "U+4EE4",
    "U+548C",
    "U+FF17"
   ]
  },
  {
   "i": 38,
   "firstDiff": 127,
   "lenGot": 128,
   "lenWant": 128,
   "got": [
    "名",
    ",",
    "▁"
   ],
   "want": [
    "名",
    ",",
    "</s>"
   ],
   "gotIds": [
    902,
    4,
    6
   ],
   "wantIds": [
    902,
    4,
    2
   ],
   "codepoints": [
    "U+5217",
    "U+540D",
    "U+8ACB",
    "U+8CA0",
    "U+696D",
    "U+8005",
    "U+5024",
    "U+9AD8",
    "U+6A4B",
    "U+5DE5",
    "U+682A",
    "U+5F0F"
   ]
  }
 ],
 "served": {
  "model_quantized.onnx": 31284394,
  "ort-wasm-simd-threaded.asyncify.wasm": 26861777,
  "tokenizer.json": 957555,
  "transformers.web.min.js": 454425,
  "ort.min.mjs": 368019,
  "ort.webgpu.bundle.min.mjs": 117929,
  "ort-wasm-simd-threaded.asyncify.mjs": 53057,
  "config.json": 1371,
  "tokenizer_config.json": 392
 },
 "servedTotalMB": 60.1,
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
