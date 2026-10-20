# mmBERT-small の試運転（CPU・GitHub Actions）

run: 39433968539　commit: f7917c96ca2cc70e912fc2cb9d0ae8aa5e256238

## モデルの取得
```
jhu-clsp/mmBERT-small revision abc32620dd4f6ab06f5fbe905dc25f310618e09f license mit tags ['license:mit']
repo files: ['.gitattributes', 'README.md', 'config.json', 'pytorch_model.bin', 'special_tokens_map.json', 'tokenizer.json', 'tokenizer_config.json']
allow_patterns: ['*.json', '*.safetensors', '*.model', '*.txt', 'sentencepiece*', 'tokenizer*', 'pytorch_model*.bin']
Fetching 5 files:   0%|          | 0/5 [00:00<?, ?it/s]Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Fetching 5 files:  80%|████████  | 4/5 [00:00<00:00,  6.40it/s]Fetching 5 files: 100%|██████████| 5/5 [00:02<00:00,  1.91it/s]Fetching 5 files: 100%|██████████| 5/5 [00:02<00:00,  2.30it/s]
fetched: ['config.json', 'pytorch_model.bin', 'special_tokens_map.json', 'tokenizer.json', 'tokenizer_config.json']
intfloat/multilingual-e5-base revision d128750597153bb5987e10b1c3493a34e5a4502a license mit tags ['license:mit']
repo files: ['.eval_results/ArguAna.yaml', '.gitattributes', '1_Pooling/config.json', 'README.md', 'config.json', 'model.safetensors', 'modules.json', 'onnx/config.json', 'onnx/model.onnx', 'onnx/model_O4.onnx', 'onnx/model_qint8_avx512_vnni.onnx', 'onnx/sentencepiece.bpe.model', 'onnx/special_tokens_map.json', 'onnx/tokenizer.json', 'onnx/tokenizer_config.json', 'openvino/openvino_model.bin', 'openvino/openvino_model.xml', 'pytorch_model.bin', 'sente```
## 部品の単体試験
```
[仕事4] 開始（GPU 0）仕事1との違い：FT_TAG=d
[仕事3] 開始（GPU 1）仕事1との違い：FT_TAG=c
[仕事3] 終了（終了コード 0）
[仕事4] 終了（終了コード 0）
[仕事5] 開始（GPU 1）仕事1との違い：FT_TAG=e
[仕事5] 終了（終了コード 0）
ok
test_single_job_runs_in_the_root (tests.test_jobs.RunJobsTest.test_single_job_runs_in_the_root) ... ok
test_two_jobs_run_side_by_side_with_separate_outputs (tests.test_jobs.RunJobsTest.test_two_jobs_run_side_by_side_with_separate_outputs) ... [仕事1] 開始（GPU 0）FT_TAG=a
[仕事2] 開始（GPU 1）仕事1との違い：FT_TAG=b
[仕事1] 終了（終了コード 0）
[仕事2] 終了（終了コード 0）
ok
test_unlaunchable_job_is_reported_as_failure (tests.test_jobs.RunJobsTest.test_unlaunchable_job_is_reported_as_failure) ... [仕事1] 開始（GPU 0）（設定なし）
[仕事2] 開始（GPU 1）仕事1との違い：なし
[仕事1] /opt/hostedtoolcache/Python/3.12.15/x64/bin/python: can't open file '/tmp/tmptdwczvwz/missing_script.py': [Errno 2] No such file or directory
[仕事2] /opt/hostedtoolcache/Python/3.12.15/x64/bin/python: can't open file '/tmp/tmptdwczvwz/missing_script.py': [Errno 2] No such file or directory
[仕事1] 終了（終了コード 2）
[仕事2] 終了（終了コード 2）
ok

----------------------------------------------------------------------
Ran 65 tests in 5.036s

OK
```

# mmBERT-small の試運転（CPU・GitHub Actions）

環境：{"transformers": "5.20.2", "torch": "2.14.1+cpu", "python": "3.12.15"}

| 区分 | 項目 | 結果 | 説明 |
|---|---|---|---|
| ★1 | config | OK | {"model_type": "modernbert", "architectures": ["ModernBertForMaskedLM"], "hidden_size": 384, "num_hidden_layers": 22, "num_attention_heads": 6, "intermediate_size": 1152, "vocab_size": 256000, "max_position_embeddings": 8192, "classifier_pooling": "mean", "classifier_activation": "gelu", "classifier_bias": false, "classifier_dropout": 0.0, "global_attn_every_n_layers": 3, "local_attention": 128, "pad_token_id": 0, "bos_token_id": 2, "eos_token_id": 1, "cls_token_id": 1, "sep_token_id": 1, "reference_compile": null, "tie_word_embeddings": true} |
| ★1 | トークナイザ | OK | TokenizersBackend vocab=256000 pad='<pad>'/0 bos='<bos>'/2 eos='<eos>'/1 cls='<bos>' sep='<eos>' unk='<unk>' model_max_length=8192 model_input_names=['input_ids', 'attention_mask'] |
| ★2 | 分割の例 | OK | 45 トークン／keys=['attention_mask', 'input_ids']／先頭 ['<bos>', '▁列', '名', ':', '▁金', '額'] … 末尾 ['▁', '摘要', '<eos>'] |
| ★2 | 分割の例 | OK | 35 トークン／keys=['attention_mask', 'input_ids']／先頭 ['<bos>', '▁列', '名', ':', '▁取', '引'] … 末尾 ['▁日', '付', '<eos>'] |
| ★2 | 分割の例 | OK | 37 トークン／keys=['attention_mask', 'input_ids']／先頭 ['<bos>', '▁query', ':', '▁列', '名', ':'] … 末尾 ['▁税', '額', '<eos>'] |
| ★2 | 分割の例 | OK | 38 トークン／keys=['attention_mask', 'input_ids']／先頭 ['<bos>', '▁列', '名', ':', '▁', 'Ｖ'] … 末尾 [',', '▁name', '<eos>'] |
| ★2 | パディング | OK | padding_side=right shape=(2, 45) mask=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] token_type_ids を返す=False |
| ★2 | 長さ mmBERT / train | OK | n=55213 平均=67.4 p50=62 p95=130 p99=166 最大=270 128超で切捨=2880件(5.22%) |
| ★2 | 長さ mmBERT / 開発用220 | OK | n=220 平均=103.7 p50=100 p95=162 p99=185 最大=233 128超で切捨=41件(18.64%) |
| ★2 | 長さ mmBERT / 本物（一般） | OK | n=383 平均=93.7 p50=95 p95=155 p99=164 最大=184 128超で切捨=51件(13.32%) |
| ★2 | 長さ mmBERT / 本物（業務） | OK | n=490 平均=90.2 p50=87 p95=139 p99=146 最大=161 128超で切捨=62件(12.65%) |
| ★2 | 長さ mmBERT / 本物（業務2） | OK | n=976 平均=84.8 p50=83 p95=125 p99=157 最大=212 128超で切捨=42件(4.30%) |
| ★2 | 長さ mmBERT / 本物（日本の調達） | OK | n=92 平均=128.2 p50=108 p95=264 p99=276 最大=276 128超で切捨=25件(27.17%) |
| ★2 | 長さ E5 / train | OK | n=55213 平均=70.1 p50=63 p95=131 p99=163 最大=245 128超で切捨=3097件(5.61%) |
| ★2 | 長さ E5 / 開発用220 | OK | n=220 平均=106.9 p50=105 p95=146 p99=167 最大=186 128超で切捨=45件(20.45%) |
| ★2 | 長さ E5 / 本物（一般） | OK | n=383 平均=95.8 p50=99 p95=134 p99=170 最大=191 128超で切捨=28件(7.31%) |
| ★2 | 長さ E5 / 本物（業務） | OK | n=490 平均=92.4 p50=91 p95=138 p99=145 最大=150 128超で切捨=44件(8.98%) |
| ★2 | 長さ E5 / 本物（業務2） | OK | n=976 平均=85.4 p50=83 p95=123 p99=139 最大=159 128超で切捨=24件(2.46%) |
| ★2 | 長さ E5 / 本物（日本の調達） | OK | n=92 平均=109.1 p50=111 p95=158 p99=199 最大=199 128超で切捨=22件(23.91%) |
| ★3 | pooling=cls | OK | logits shape=(2, 15) attn=sdpa head=['model', 'head', 'drop', 'classifier'] config変更={'classifier_pooling': 'cls', 'num_labels': 15} |
| ★3 | pooling=mean | OK | logits shape=(2, 15) attn=sdpa head=['model', 'head', 'drop', 'classifier'] config変更={'classifier_pooling': 'mean', 'num_labels': 15} |
| ★3 | pooling=（config のまま：mean） | OK | logits shape=(2, 15) attn=sdpa head=['model', 'head', 'drop', 'classifier'] config変更={'num_labels': 15} |
| ★4 | 3 ステップ | OK | 損失 [6.5048, 2.0658, 0.8604] 勾配ノルム 44.148（同じ 16 文を使い回すので下がるのが普通。下がった=True） |
| ★5 | 保存→読み込みで logits 一致・トークナイザの ID 一致 | OK | 最大差 0.00e+00／ID一致 True／保存したファイル ['config.json', 'labels.json', 'model.safetensors', 'tokenizer.json', 'tokenizer_config.json']／重み model.safetensors: 563MB |
| ★5 | .bin → safetensors の置き直し（強制）で読み込み結果が一致 | OK | 最大差 0.00e+00／テンソル 138 個・957MB／変換の要否（torch 2.5.1→True、この環境 2.14.1+cpu→False、2.6.0→False） |
| ☆6 | 推論 32 列（平均長に詰めた束） | OK | 2.83 秒（88 ms/列・4 スレッド・fp32・この CPU のみの参考値）shape=(32, 128) |
| ☆7 | ONNX opset 18・legacy | OK | onnxruntime と PyTorch の最大差 1.62e-05／別の長さ 1.81e-05／563MB（fp32・語彙を削る前） |

必須（★）で NG：0 件

※ CPU の試運転であり、GPU（fp16）での学習・精度・端末での速さは確かめていない。
## finetune_exp.py の通し（末尾）
```
FT_VAL=1: 検証モード（固定の試験は評価しない）。検証の行数 検証（一般） 204, 検証（業務） 204, 検証（業務2） 415, 検証（日本の調達） 66
Loading weights:   0%|          | 0/136 [00:00<?, ?it/s]Loading weights: 100%|██████████| 136/136 [00:00<00:00, 14520.92it/s]
[transformers] [1mModernBertForSequenceClassification LOAD REPORT[0m from: hfmodel/jhu-clsp__mmBERT-small
Key               | Status     | 
------------------+------------+-
decoder.weight    | UNEXPECTED | 
decoder.bias      | UNEXPECTED | 
classifier.weight | MISSING    | 
classifier.bias   | MISSING    | 

Notes:
- UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:	those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
device cpu; CPU threads=2/4
model_type=modernbert params=140,647,696 attn=sdpa pooling=mean config_changes={'num_labels': 16}
training rows=256 seed=1
token lengths (max_length=128): train mean=52.5 p95=114 p99=149 max=156 truncated=1.95%
CPU token cache: 256 rows tokenized once
train batch=16, accumulation=1, effective=16, checkpointing=False, sort=True, pad_multiple=8, fused=False, freeze_embeddings=False
mixed precision: mode=fp16 active=False fallback_to_fp32=True
focal-loss experiment: gamma=1.5
| hfmodel/jhu-clsp__mmBERT-small 微調整 1.0周・微調整だけ | 検証（一般） 正8.1% 誤15 不明121 重大2 その他見送り53/56 | 検証（業務） 正20.9% 誤3 不明152 重大3 その他見送り7/8 | 検証（業務2） 正14.4% 誤17 不明310 重大12 その他見送り30/33 | 検証（日本の調達） 正10.8% 誤0 不明58 重大0 その他見送り0/1 | 学習 64秒・
| hfmodel/jhu-clsp__mmBERT-small 微調整 1.0周・今の仕組みだけ | 検証（一般） 正85.8% 誤12 不明9 重大0 その他見送り52/56 | 検証（業務） 正93.9% 誤10 不明2 重大2 その他見送り8/8 | 検証（業務2） 正93.5% 誤9 不明16 重大3 その他見送り22/33 | 検証（日本の調達） 正96.9% 誤0 不明2 重大0 その他見送り1/1 | 学習 64秒・
| hfmodel/jhu-clsp__mmBERT-small 微調整 1.0周・微調整＋今の仕組み（半々） | 検証（一般） 正73.6% 誤2 不明37 重大0 その他見送り54/56 | 検証（業務） 正83.7% 誤2 不明30 重大2 その他見送り8/8 | 検証（業務2） 正81.4% 誤2 不明69 重大1 その他見送り23/33 | 検証（日本の調達） 正90.8% 誤0 不明6 重大0 その他見送り1/1
| hfmodel/jhu-clsp__mmBERT-small 微調整 1.0周・微調整6割＋今の仕組み4割 | 検証（一般） 正23.6% 誤1 不明112 重大0 その他見送り53/56 | 検証（業務） 正42.9% 誤1 不明111 重大1 その他見送り8/8 | 検証（業務2） 正42.1% 誤0 不明221 重大0 その他見送り32/33 | 検証（日本の調達） 正35.4% 誤0 不明42 重大0 その他見送り1/1
| hfmodel/jhu-clsp__mmBERT-small 微調整 1.0周・微調整7割＋今の仕組み3割 | 検証（一般） 正13.5% 誤1 不明127 重大0 その他見送り53/56 | 検証（業務） 正34.2% 誤1 不明128 重大1 その他見送り8/8 | 検証（業務2） 正29.8% 誤0 不明268 重大0 その他見送り32/33 | 検証（日本の調達） 正23.1% 誤0 不明50 重大0 その他見送り1/1
Writing model shards:   0%|          | 0/1 [00:00<?, ?it/s]Writing model shards: 100%|██████████| 1/1 [00:00<00:00,  6.93it/s]Writing model shards: 100%|██████████| 1/1 [00:00<00:00,  6.92it/s]
manifest.json written; weights sha256 4ca77d90814661dd41bc5e9918df81c78f3322c1cc861c1c611bcb2c1ef39024
```
## 検査・集計・記録
```
  },
  "検証（業務）": {
   "count": 204,
   "sha256_ordered": "8fb19dd702923db7108d08724d95cdc8bde796c7a0153e36d3e7aee93f2f658e",
   "sha256_unordered": "dec9299a959c8ba094619bfbbdae986950140feaf43603f4e112283682c03cad"
  }
 },
 "timing": {
  "eval_seconds": 65.6,
  "inference_rows": {
   "検証（一般）": 204,
   "検証（日本の調達）": 66,
   "検証（業務2）": 415,
   "検証（業務）": 204
  },
  "inference_seconds": {
   "検証（一般）": 14.87,
   "検証（日本の調達）": 4.81,
   "検証（業務2）": 29.7,
   "検証（業務）": 14.34
  },
  "peak_gpu_gib": null,
  "train_loop_seconds": 63.0,
  "train_total_seconds": 63.5
 },
 "model_config": {
  "attn_implementation": "sdpa",
  "classifier_pooling": "mean",
  "hidden_size": 384,
  "layers": 22,
  "model_type": "modernbert",
  "parameters": 140647696,
  "vocab_size": 256000
 },
 "libraries": {
  "numpy": "2.5.4",
  "platform": "Linux-7.0.0-1017-azure-x86_64-with-glibc2.39",
  "python": "3.12.15",
  "safetensors": "0.8.0",
  "scikit-learn": "1.9.1",
  "tokenizers": "0.23.3",
  "torch": "2.14.1+cpu",
  "transformers": "5.20.2"
 },
 "extra": {
  "config_changes": {
   "num_labels": 16
  },
  "device": "cpu",
  "eval_mode": "validation",
  "gpu": null,
  "max_length": 128,
  "model_type": "modernbert",
  "no_dropout": false,
  "prefix": "",
  "request_args": null
 },
 "token_stats_keys": [
  "train",
  "検証（一般）",
  "検証（日本の調達）",
  "検証（業務2）",
  "検証（業務）"
 ],
 "saved_model": {
  "files": {
   "config.json": "9fe3839f839e614e8eccebaa77a88b7f0d92f45438ecf82ebbe61c55ed89254a",
   "labels.json": "fc7e758c07c6b2107cc587a5d50981c7107c1f9a04ab4dc7753c063167ffa3bf",
   "tokenizer.json": "f231fae363627485dbad73e8b95f601378deede800416098c14c81a0deafa813",
   "tokenizer_config.json": "a610934a0c3e4f0287078cfaf77b6931fd13598445d27f860cc436b8bf2c4454"
  },
  "weights": {
   "model.safetensors": {
    "bytes": 562604960,
    "sha256": "4ca77d90814661dd41bc5e9918df81c78f3322c1cc861c1c611bcb2c1ef39024"
   }
  }
 },
 "outputs_count": 41
}
```
