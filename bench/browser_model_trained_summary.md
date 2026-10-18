# ブラウザ用の書き出しの検査（GitHub Actions・CPU）

run: 39100525878　commit: 9c4fc0f756309a178380475e9c6da0ef666ac069　学習済みモデル: 39098438731 ft_out_job1

# ブラウザ用に書き出したモデルの試験（trained/ft_out_job1）

- 残す単語片 21,772 個／全体 250,037 個（上位 K=0）。per_channel=False
- ファイルの大きさ：fp32 120.3MB／埋め込み表だけ INT8 95.3MB／さらに全結合層も INT8（model_quantized.onnx）31.3MB／tokenizer.json 1.0MB

| 版・組み合わせ | 開発用220 | 本物（一般） | 本物（業務） | 本物（業務2） | 本物（日本の調達） | 比較 |
|---|---|---|---|---|---|---|
| PyTorch fp32・微調整だけ | 開発用220 正80.5% 誤10 不明33 重大2 | 本物（一般） 正84.1% 誤10 不明37 重大2 | 本物（業務） 正89.1% 誤39 不明13 重大8 | 本物（業務2） 正93.6% 誤35 不明23 重大17 | 本物（日本の調達） 正96.7% 誤0 不明3 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.000・logits の最大差 0.000（logits の広がり 1.941） |
| PyTorch fp32・微調整7割＋今の仕組み3割 | 開発用220 正82.7% 誤10 不明28 重大2 | 本物（一般） 正84.7% 誤8 不明37 重大2 | 本物（業務） 正89.5% 誤39 不明11 重大9 | 本物（業務2） 正94.0% 誤34 不明21 重大15 | 本物（日本の調達） 正98.9% 誤0 不明1 重大0 | PyTorch fp32 との top-1 一致 100.00%・確率の最大差 0.000・logits の最大差 0.000（logits の広がり 1.941） |
| ONNX fp32・微調整だけ | 開発用220 正81.4% 誤7 不明34 重大1 | 本物（一般） 正84.4% 誤12 不明34 重大1 | 本物（業務） 正90.5% 誤34 不明11 重大7 | 本物（業務2） 正93.9% 誤28 不明28 重大9 | 本物（日本の調達） 正97.8% 誤0 不明2 重大0 | PyTorch fp32 との top-1 一致 96.95%・確率の最大差 0.922・logits の最大差 5.883（logits の広がり 1.941） |
| ONNX fp32・微調整7割＋今の仕組み3割 | 開発用220 正86.8% 誤6 不明23 重大1 | 本物（一般） 正86.4% 誤11 不明29 重大1 | 本物（業務） 正90.5% 誤36 不明9 重大8 | 本物（業務2） 正94.0% 誤27 不明28 重大10 | 本物（日本の調達） 正98.9% 誤0 不明1 重大0 | PyTorch fp32 との top-1 一致 96.95%・確率の最大差 0.922・logits の最大差 5.883（logits の広がり 1.941） |
| ONNX 埋め込みINT8・微調整だけ | 開発用220 正81.4% 誤7 不明34 重大1 | 本物（一般） 正84.4% 誤12 不明34 重大1 | 本物（業務） 正90.3% 誤34 不明12 重大7 | 本物（業務2） 正94.0% 誤28 不明27 重大9 | 本物（日本の調達） 正97.8% 誤0 不明2 重大0 | PyTorch fp32 との top-1 一致 96.99%・確率の最大差 0.919・logits の最大差 5.881（logits の広がり 1.941） |
| ONNX 埋め込みINT8・微調整7割＋今の仕組み3割 | 開発用220 正86.8% 誤6 不明23 重大1 | 本物（一般） 正86.4% 誤11 不明29 重大1 | 本物（業務） 正90.5% 誤36 不明9 重大8 | 本物（業務2） 正94.0% 誤27 不明28 重大10 | 本物（日本の調達） 正98.9% 誤0 不明1 重大0 | PyTorch fp32 との top-1 一致 96.99%・確率の最大差 0.919・logits の最大差 5.881（logits の広がり 1.941） |
| ONNX 埋め込みINT8＋全結合層INT8・微調整だけ | 開発用220 正80.5% 誤11 不明32 重大1 | 本物（一般） 正84.4% 誤12 不明34 重大1 | 本物（業務） 正90.5% 誤35 不明10 重大6 | 本物（業務2） 正93.8% 誤29 不明28 重大12 | 本物（日本の調達） 正95.7% 誤1 不明3 重大1 | PyTorch fp32 との top-1 一致 96.44%・確率の最大差 0.962・logits の最大差 4.910（logits の広がり 1.941） |
| ONNX 埋め込みINT8＋全結合層INT8・微調整7割＋今の仕組み3割 | 開発用220 正85.0% 誤8 不明25 重大1 | 本物（一般） 正86.1% 誤12 不明29 重大1 | 本物（業務） 正90.1% 誤34 不明13 重大6 | 本物（業務2） 正94.3% 誤27 不明25 重大12 | 本物（日本の調達） 正97.8% 誤0 不明2 重大0 | PyTorch fp32 との top-1 一致 96.44%・確率の最大差 0.962・logits の最大差 4.910（logits の広がり 1.941） |

- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX fp32）：平均 59ms・中央値 58ms／列（全 2161 列の文の平均 89 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX fp32）：平均 33ms・中央値 32ms／列（全 2161 列の文の平均 89 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・1スレッド・ONNX INT8（model_quantized.onnx））：平均 38ms・中央値 38ms／列（全 2161 列の文の平均 89 トークン）
- 1 列ずつ流した時間（onnxruntime・CPU・2スレッド・ONNX INT8（model_quantized.onnx））：平均 22ms・中央値 21ms／列（全 2161 列の文の平均 89 トークン）
- ブラウザの試験の正解データ（reference.json）：モデルを流す文 40 文／トークナイザの番号だけを比べる文 2204 文（試験の全列＋変わった文字列 43 個）

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
   "tokenizerLoadMs": 50,
   "loadMs": 1412,
   "tokMsMean": 2.2,
   "idMismatch": 0,
   "maxLogitDiffVsOrtInt8": 1.3582,
   "maxLogitDiffVsOrtFp32": 3.8488,
   "argmaxAgreeVsOrtInt8": "40/40",
   "msPerColumnMean": 108.5,
   "msPerColumnMedian": 97.8,
   "msPerColumnP90": 134.5,
   "wallSeconds": 6.924
  },
  {
   "threads": 2,
   "isolated": true,
   "effectiveThreads": 2,
   "tokenizerLoadMs": 46,
   "loadMs": 1458,
   "tokMsMean": 2.33,
   "idMismatch": 0,
   "maxLogitDiffVsOrtInt8": 1.3582,
   "maxLogitDiffVsOrtFp32": 3.8488,
   "argmaxAgreeVsOrtInt8": "40/40",
   "msPerColumnMean": 124.9,
   "msPerColumnMedian": 93.3,
   "msPerColumnP90": 157.1,
   "wallSeconds": 8.153
  },
  {
   "threads": 4,
   "isolated": true,
   "effectiveThreads": 4,
   "tokenizerLoadMs": 57,
   "loadMs": 1631,
   "tokMsMean": 0.99,
   "idMismatch": 0,
   "maxLogitDiffVsOrtInt8": 1.3582,
   "maxLogitDiffVsOrtFp32": 3.8488,
   "argmaxAgreeVsOrtInt8": "40/40",
   "msPerColumnMean": 97.4,
   "msPerColumnMedian": 96.7,
   "msPerColumnP90": 154.5,
   "wallSeconds": 6.697
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
 "tokParity": {
  "total": 2204,
  "edge": 43,
  "mismatches": 20,
  "mismatchesEdge": 1,
  "ms": 459,
  "first": [
   {
    "i": 27,
    "edge": false,
    "firstDiff": 38,
    "lenGot": 125,
    "lenWant": 126,
    "got": [
     "ヤ",
     "マ",
     "グ",
     "チ",
     "▁",
     "ケ",
     "ン"
    ],
    "want": [
     "ヤ",
     "マ",
     "ク",
     "゙",
     "チ",
     "▁",
     "ケ"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+4F5C",
     "U+696D",
     "U+8005",
     "U+6B04",
     "U+5024",
     "U+9577",
     "U+8C37",
     "U+5DDD"
    ]
   },
   {
    "i": 28,
    "edge": false,
    "firstDiff": 26,
    "lenGot": 125,
    "lenWant": 127,
    "got": [
     "ア",
     "オ",
     "ゾ",
     "ラ",
     ",",
     "▁",
     "再"
    ],
    "want": [
     "ア",
     "オ",
     "ソ",
     "゙",
     "ラ",
     ",",
     "▁"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+5099",
     "U+8003",
     "U+5024",
     "U+6708",
     "U+30B5",
     "U+30FC",
     "U+30D0",
     "U+4EE3"
    ]
   },
   {
    "i": 93,
    "edge": false,
    "firstDiff": 18,
    "lenGot": 128,
    "lenWant": 128,
    "got": [
     "ア",
     "オ",
     "ゾ",
     "ラ",
     ",",
     "▁",
     "領"
    ],
    "want": [
     "ア",
     "オ",
     "ソ",
     "゙",
     "ラ",
     ",",
     "▁"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+6458",
     "U+8981",
     "U+5024",
     "U+632F",
     "U+66FF",
     "U+FF71",
     "U+FF75",
     "U+FF7F"
    ]
   },
   {
    "i": 119,
    "edge": false,
    "firstDiff": 45,
    "lenGot": 109,
    "lenWant": 110,
    "got": [
     "ア",
     "オ",
     "ゾ",
     "ラ",
     "▁",
     "|",
     "▁"
    ],
    "want": [
     "ア",
     "オ",
     "ソ",
     "゙",
     "ラ",
     "▁",
     "|"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+5951",
     "U+7D04",
     "U+4EF6",
     "U+5024",
     "U+8FD4",
     "U+91D1",
     "U+51E6",
     "U+7406"
    ]
   },
   {
    "i": 197,
    "edge": false,
    "firstDiff": 22,
    "lenGot": 95,
    "lenWant": 96,
    "got": [
     "ヤ",
     "マ",
     "グ",
     "チ",
     "▁",
     "ケ",
     "ン"
    ],
    "want": [
     "ヤ",
     "マ",
     "ク",
     "゙",
     "チ",
     "▁",
     "ケ"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+5024",
     "U+5C0F",
     "U+91CE",
     "U+5BFA",
     "U+6075",
     "U+FF94",
     "U+FF8F",
     "U+FF78"
    ]
   },
   {
    "i": 2023,
    "edge": false,
    "firstDiff": 36,
    "lenGot": 63,
    "lenWant": 67,
    "got": [
     "▁",
     "市場",
     "コード",
     ",",
     "▁",
     "品",
     "名"
    ],
    "want": [
     "▁",
     "市場",
     "コー",
     "ト",
     "゙",
     ",",
     "▁"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+8CA9",
     "U+58F2",
     "U+5024",
     "U+540C",
     "U+3058",
     "U+8868",
     "U+306E",
     "U+5E02"
    ]
   },
   {
    "i": 2024,
    "edge": false,
    "firstDiff": 7,
    "lenGot": 61,
    "lenWant": 65,
    "got": [
     "▁",
     "市場",
     "コード",
     "▁",
     "|",
     "▁",
     "値"
    ],
    "want": [
     "▁",
     "市場",
     "コー",
     "ト",
     "゙",
     "▁",
     "|"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+5E02",
     "U+5834",
     "U+FF7A",
     "U+FF70",
     "U+FF84",
     "U+FF9E",
     "U+5024",
     "U+540C"
    ]
   },
   {
    "i": 2025,
    "edge": false,
    "firstDiff": 47,
    "lenGot": 70,
    "lenWant": 74,
    "got": [
     "▁",
     "市場",
     "コード",
     ",",
     "▁",
     "産",
     "地"
    ],
    "want": [
     "▁",
     "市場",
     "コー",
     "ト",
     "゙",
     ",",
     "▁"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+54C1",
     "U+5024",
     "U+5408",
     "U+8A08",
     "U+3060",
     "U+308B",
     "U+307E",
     "U+3068"
    ]
   },
   {
    "i": 2026,
    "edge": false,
    "firstDiff": 8,
    "lenGot": 58,
    "lenWant": 62,
    "got": [
     "産",
     "地",
     "コード",
     "▁",
     "|",
     "▁",
     "値"
    ],
    "want": [
     "産",
     "地",
     "コー",
     "ト",
     "゙",
     "▁",
     "|"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+7523",
     "U+5730",
     "U+FF7A",
     "U+FF70",
     "U+FF84",
     "U+FF9E",
     "U+5024",
     "U+540C"
    ]
   },
   {
    "i": 2027,
    "edge": false,
    "firstDiff": 46,
    "lenGot": 68,
    "lenWant": 72,
    "got": [
     "▁",
     "市場",
     "コード",
     ",",
     "▁",
     "品",
     "名"
    ],
    "want": [
     "▁",
     "市場",
     "コー",
     "ト",
     "゙",
     ",",
     "▁"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+7523",
     "U+5730",
     "U+5024",
     "U+718A",
     "U+672C",
     "U+548C",
     "U+6B4C",
     "U+5C71"
    ]
   },
   {
    "i": 2028,
    "edge": false,
    "firstDiff": 48,
    "lenGot": 70,
    "lenWant": 74,
    "got": [
     "▁",
     "市場",
     "コード",
     ",",
     "▁",
     "品",
     "名"
    ],
    "want": [
     "▁",
     "市場",
     "コー",
     "ト",
     "゙",
     ",",
     "▁"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+6570",
     "U+91CF",
     "U+5024",
     "U+540C",
     "U+3058",
     "U+8868",
     "U+306E",
     "U+8CA9"
    ]
   },
   {
    "i": 2029,
    "edge": false,
    "firstDiff": 47,
    "lenGot": 69,
    "lenWant": 73,
    "got": [
     "▁",
     "市場",
     "コード",
     ",",
     "▁",
     "品",
     "名"
    ],
    "want": [
     "▁",
     "市場",
     "コー",
     "ト",
     "゙",
     ",",
     "▁"
    ],
    "codepoints": [
     "U+5217",
     "U+540D",
     "U+91D1",
     "U+984D",
     "U+5186",
     "U+5024",
     "U+540C",
     "U+3058",
     "U+8868",
     "U+306E"
    ]
   }
  ]
 },
 "build": "transformers.web.min.js",
 "mismatches": [],
 "served": {
  "model_quantized.onnx": 31284394,
  "ort-wasm-simd-threaded.asyncify.wasm": 26861777,
  "tokenizer.json": 957555,
  "transformers.web.min.js": 454425,
  "ort.min.mjs": 368019,
  "ort.webgpu.bundle.min.mjs": 117929,
  "ort-wasm-simd-threaded.asyncify.mjs": 53057,
  "config.json": 1440,
  "tokenizer_config.json": 495
 },
 "servedTotalMB": 60.1,
 "servedBrotliMB": 27.4,
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
