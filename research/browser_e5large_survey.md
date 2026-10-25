# multilingual-e5-large をブラウザで使う場合の公開測定例

調査日：2026-10-25  
対象：語彙刈り込み + INT8 の multilingual-e5-large を ONNX Runtime Web の WASM / WebGPU で使う場合のモデルサイズと 1 列あたりの時間。公開資料の調査のみで、ジツリスのモデルを実測したものではない。

## 結論

今回見つかった公開資料には、**multilingual-e5-large を語彙刈り込み + INT8 にし、ONNX Runtime Web の WASM と WebGPU の両方で列分類時間を測った同条件の結果はない**。従って「約 300 MB」「約 3 倍遅い」は、このモデル・このタスク・ブラウザに対する測定値としては裏付けられない。

公開されている関連例は、(1) 小型の MiniLM Q8 を実ブラウザで測った比較、(2) e5-large を Web Worker + WASM で動かす実装例、(3) 別の大規模モデルを WebGPU で測った公式デモ。いずれも目安にはなるが、multilingual-e5-large の 1 列レイテンシへ直接換算できない。

## 直接確認できたモデルの大きさ

Hugging Face の公式 `intfloat/multilingual-e5-large` モデルカードは 24 層・隠れ次元 1,024 を記載し、`model.safetensors` は 2.24 GB。比較対象の `multilingual-e5-base` は 12 層・768 次元で重みが 1.11 GB。大きい方は層数が 2 倍、隠れ次元が 4/3 倍である。

**単純な容量換算（推算）**：全ての重みを FP32 から 8-bit に置き換え、他の条件が同じなら、2.24 GB の重みは概算約 0.56 GB。実際の ONNX ファイルは、量子化対象外の重み、scale/zero-point、グラフ構造、外部データ、語彙刈り込みの有無で変わる。300 MB はこの単純換算からさらに約 46% 小さいため、語彙表をどれほど削れるかと多言語品質を別途測る必要がある。サイズ換算は実測ではない。

語彙刈り込みは埋め込み表の容量を減らせても、Transformer の各層の計算を同じ割合で減らすとは限らない。日本語・英語・ポルトガル語のトークン被覆と、分類精度への影響を確認する必要がある。また、公式モデルは feature-extraction の埋め込みモデル。ジツリスで使う候補が分類 head 付きなら、その ONNX グラフと同じトークナイズで測る。

## 公開されているブラウザ測定

| 出典と条件 | WASM | WebGPU | 何が分かるか |
|---|---:|---:|---|
| [browser-runtimes-bench](https://github.com/delcenjo/browser-runtimes-bench)、`Xenova/all-MiniLM-L6-v2` Q8、Chrome 150 / Ryzen 7 7435HS / RTX 3050 / Ubuntu 24.04（2026-07-12）。生の onnxruntime-web、batch=1、warmup 10 回を除外し 50 回測定。3 ページセッションの中央値 | p50 12.05 ms、p95 15.00 ms、cold session 1,011.5 ms | p50 158.10 ms、p95 167.86 ms、cold session 1,253.8 ms | この機械・この小型モデルでは batch=1 の WebGPU が WASM より遅かった。モデルは約 23 MB の Q8 MiniLM で、e5-large の代用値にはできない。 |
| [Microsoft の公式 ONNX Runtime Web / Segment Anything デモ](https://opensource.microsoft.com/blog/2024/02/29/onnx-runtime-web-unleashes-generative-ai-in-the-browser-using-webgpu/)、RTX 3060 + Core i9 | ― | encoder 19 倍、decoder 3.8 倍の高速化と報告 | 別モデルの大きな画像処理グラフ。GPU の効果がモデル部分で異なることを示す例で、テキスト列分類の比率ではない。 |

最初の測定はモデルをローカルに置き、cold load にネットワークの重みダウンロード時間を含めていない。WebGPU は Chrome の標準設定ではなく、Vulkan を有効にした起動条件で測っている。報告される JS heap は WASM/GPU の全メモリではなく、スマートフォンや iPhone の速度を示すものでもない。

[実ブラウザで e5-large を Web Worker + WASM で動かす手順例](https://cdn-avatars.qwak.ai/blog/stephen-solka/embedding-model-in-the-browser) は、一般の `e5-large` について FP32 約 1.3 GB、FP16 約 670 MB、動的 INT8 約 336 MB と記載し、ページを固めないため Web Worker で推論する方法を示す。しかし per-call latency は載っておらず、対象が `intfloat/multilingual-e5-large` と同一だと確認できない。公式 multilingual 重み 2.24 GB と容量が一致しないため、336 MB を本モデルの実績として扱わない。

## WASM / WebGPU の制約

- ONNX Runtime Web の公式説明では WASM は全 ONNX 演算子、WebGPU/WebGL/WebNN は一部の演算子だけをサポートする。量子化後の実グラフが WebGPU で動くか、未対応演算子がどの backend で処理されるかを確認してから速度を比べる。
- 公式の WebGPU ガイドは、軽いモデルはバイナリサイズの小さい WASM、計算の重いモデルは WebGPU を候補にするよう案内している。どちらが速いかはモデル・端末・入力長・batch に依存する。
- 2 GB を超える ONNX は protobuf 外部データが必要になり、ブラウザ側で外部データの渡し方にも注意が要る。WASM のメモリ上限は 4 GB。INT8 化で 2 GB 未満になっても、初回ダウンロードと展開後メモリは別に測る。
- WASM のマルチスレッドは Cross-Origin Isolation の設定が関係する。比較時には実際のサイト配信条件を使い、1 thread と可能な multi-thread の条件を分けて記録する。

## ジツリスで判断するための測り方

この調査だけでは採用判断を確定できない。実測する場合は、モデル、量子化、語彙表、トークナイザー、分類 head、入力処理を一式として固定する。

1. 同一 checkpoint から「現行 E5-base」と「multilingual-e5-large」の ONNX を用意し、FP32/INT8、語彙刈り込み率を記録。語彙削減の前後で tokenizer の未知分割・日本語/英語/ポルトガル語の品質を確認する。
2. 実際の 1 列分類処理（前処理・tokenizer・encoder・head・見張り）を batch=1 で測る。cold download、session 作成、初回推論、warm p50/p95 を別々に記録し、入力 token 数の帯ごとに集計する。
3. WASM 1 thread、配信条件を満たした場合の WASM multi-thread、WebGPU を同じ端末・同じブラウザーで比較する。WebGPU が使えない端末では自動で WASM に戻ることも確認する。スマートフォンで使うなら実際の iPhone/Android 端末でも確認する。
4. 推論時間だけでなく、圧縮後ファイルサイズ、転送量、ロード時間、ピークメモリ、タブ応答性、分類性能を記録する。精度評価は開発用の許可済みデータで行い、封印セット #3・eval3 の候補/表/予測は使わない。

## 出典

- multilingual-e5-large model card / architecture / file list: https://huggingface.co/intfloat/multilingual-e5-large
- multilingual-e5-base model card / architecture / file list: https://huggingface.co/intfloat/multilingual-e5-base
- ONNX Runtime Web: https://onnxruntime.ai/docs/tutorials/web/
- ONNX Runtime Web WebGPU guide: https://onnxruntime.ai/docs/tutorials/web/ep-webgpu.html
- ONNX Runtime Web large-model constraints: https://onnxruntime.ai/docs/tutorials/web/large-models.html
- WebGPU operator support: https://github.com/microsoft/onnxruntime/blob/main/js/web/docs/webgpu-operators.md
- e5-large browser implementation example: https://cdn-avatars.qwak.ai/blog/stephen-solka/embedding-model-in-the-browser
- MiniLM in-browser measurement table and methodology: https://github.com/delcenjo/browser-runtimes-bench
- Microsoft official WebGPU measurement: https://opensource.microsoft.com/blog/2024/02/29/onnx-runtime-web-unleashes-generative-ai-in-the-browser-using-webgpu/
