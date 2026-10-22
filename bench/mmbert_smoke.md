# mmBERT-small の試運転（CPU・GitHub Actions）

run: 39770861031　commit: b1f706d269e8316dc921d8997771fc7e5eafb198

## モデルの取得
```
jhu-clsp/mmBERT-small revision abc32620dd4f6ab06f5fbe905dc25f310618e09f license mit tags ['license:mit']
repo files: ['.gitattributes', 'README.md', 'config.json', 'pytorch_model.bin', 'special_tokens_map.json', 'tokenizer.json', 'tokenizer_config.json']
allow_patterns: ['*.json', '*.safetensors', '*.model', '*.txt', 'sentencepiece*', 'tokenizer*', 'pytorch_model*.bin']
Fetching 5 files:   0%|          | 0/5 [00:00<?, ?it/s]Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Fetching 5 files:  20%|██        | 1/5 [00:00<00:00,  7.01it/s]Fetching 5 files:  60%|██████    | 3/5 [00:00<00:00, 10.83it/s]Fetching 5 files: 100%|██████████| 5/5 [00:06<00:00,  1.56s/it]Fetching 5 files: 100%|██████████| 5/5 [00:06<00:00,  1.24s/it]
fetched: ['config.json', 'pytorch_model.bin', 'special_tokens_map.json', 'tokenizer.json', 'tokenizer_config.json']
intfloat/multilingual-e5-base revision d128750597153bb5987e10b1c3493a34e5a4502a license mit tags ['license:mit']
repo files: ['.eval_results/ArguAna.yaml', '.gitattributes', '1_Pooling/config.json', 'README.md', 'config.json', 'model.safetensors', 'modules.json', 'onnx/config.json', 'onnx/model.onnx', 'onnx/model_O4.onnx', 'onnx/model_qint8_avx512_vnni.onnx', 'onnx/sentencepiece.bpe.model', 'onnx/special_tokens_map.json', 'onnx/tokenizer.json', 'onnx/tokenizer_config.json', 'openvino/openvino_model.```
## 部品の単体試験
```
test_keeps_only_unseen_headers_and_marks_outcome (tests.test_error_overlap.UnseenRowsTests.test_keeps_only_unseen_headers_and_marks_outcome) ... ok
test_other_job_is_ignored (tests.test_error_overlap.UnseenRowsTests.test_other_job_is_ignored) ... ok
test_info_reads_settings_from_manifest (tests.test_evaluate_independent.CheckpointTests.test_info_reads_settings_from_manifest) ... ok
test_tampered_weights_or_unfinished_run_are_refused (tests.test_evaluate_independent.CheckpointTests.test_tampered_weights_or_unfinished_run_are_refused) ... ok
test_texts_follow_training_format (tests.test_evaluate_independent.CheckpointTests.test_texts_follow_training_format) ... ok
test_predict_writes_label_free_predictions_and_ledger (tests.test_evaluate_independent.PredictAndScoreTests.test_predict_writes_label_free_predictions_and_ledger) ... ok
test_same_pair_is_refused_twice_unless_reason_given (tests.test_evaluate_independent.PredictAndScoreTests.test_same_pair_is_refused_twice_unless_reason_given) ... ok
test_saved_prediction_scores_v91_and_v10_without_inference (tests.test_evaluate_independent.PredictAndScoreTests.test_saved_prediction_scores_v91_and_v10_without_inference) ... ok
test_score_counts_assertions_on_unknown_labeled_columns (tests.test_evaluate_independent.PredictAndScoreTests.test_score_counts_assertions_on_unknown_labeled_columns) ... ok
test_score_leaves_out_unknown_and_S_columns_and_says_so (tests.test_evaluate_independent.PredictAndScoreTests.test_score_leaves_out_unknown_and_S_columns_and_says_so) ... ok
test_score_refuses_mismatched_or_unknown_labels (tests.test_evaluate_independent.PredictAndScoreTests.test_score_refuses_mismatched_or_unknown_labels) ... ok
test_score_refuses_when_nothing_is_left_to_evaluate (tests.test_evaluate_independent.PredictAndScoreTests.test_score_refuses_when_nothing_is_left_to_evaluate) ... ok
test_score_writes_records_readable_by_slice_eval (tests.test_evaluate_independent.PredictAndScoreTests.test_score_writes_records_readable_by_slice_eval) ... ok
test_load_set_ok_and_rows_have_empty_label (tests.test_evaluate_independent.SetTests.test_load_set_ok_and_rows_have_empty_label) ... ok
test_load_set_rejects_bad_shapes (tests.test_evaluate_independent.SetTests.test_load_set_rejects_bad_shapes) ... ok
test_missing_timing_or_stats_stops (tests.test_resource_table.NumbersTests.test_missing_timing_or_stats_stops) ... ok
test_per_row_milliseconds_and_truncation (tests.test_resource_table.NumbersTests.test_per_row_milliseconds_and_truncation) ... ok
test_parse_group (tests.test_resource_table.ParseTests.test_parse_group) ... ok
test_different_set_order_between_groups_is_refused (tests.test_resource_table.RenderTests.test_different_set_order_between_groups_is_refused) ... ok
test_render_and_main (tests.test_resource_table.RenderTests.test_render_and_main) ... ok

----------------------------------------------------------------------
Ran 105 tests in 4.980s

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
| ☆6 | 推論 32 列（平均長に詰めた束） | OK | 2.81 秒（88 ms/列・4 スレッド・fp32・この CPU のみの参考値）shape=(32, 128) |
| ☆7 | ONNX opset 18・legacy | OK | onnxruntime と PyTorch の最大差 1.62e-05／別の長さ 1.81e-05／563MB（fp32・語彙を削る前） |

必須（★）で NG：0 件

※ CPU の試運転であり、GPU（fp16）での学習・精度・端末での速さは確かめていない。

# 独立評価の経路の試運転（CPU）

| 項目 | 状態 | 内容 |
|---|---|---|
| ★1 重みの検査と設定の読み取り | OK | model=jhu-clsp/mmBERT-small type=modernbert prefix='' max_length=192 ctx_unit=True 重み 284e6025b77c… |
| ★2 predict（本物の torch） | OK | 24 列・2.675 秒（111.452 ms/列、CPU） |
| ★3 学習時の評価と一致 | OK | 最上位ラベル 24/24、守りを通した判断 24/24、見出し 24/24、確率の最大差 0.00e+00 |
| ★4 score と slice_eval の読み込み | OK | 件数 {'unknown': 16, 'other_ok': 8} |
| ★5 同じ組の 2 回目を断る | OK | この（主セット, 重み）はすでに予測済み（2026-10-22T11:34:27Z）。やり直すなら --repeat-reason に理由を書く |

必須項目の NG：0 件
## finetune_exp.py の通し（末尾）
```
FT_REAL_FRAC=1: selected 986/986 tables and 8106/8106 source rows; expanded real rows 39837; synthetic rows unchanged
FT_VAL=1: 検証モード（固定の試験は評価しない）。検証の行数 検証（一般） 204, 検証（業務） 204, 検証（業務2） 415, 検証（日本の調達） 66
Loading weights:   0%|          | 0/136 [00:00<?, ?it/s]Loading weights: 100%|██████████| 136/136 [00:00<00:00, 26842.28it/s]
[transformers] [1mModernBertForSequenceClassification LOAD REPORT[0m from: hfmodel/jhu-clsp__mmBERT-small
Key               | Status     | 
------------------+------------+-
decoder.bias      | UNEXPECTED | 
decoder.weight    | UNEXPECTED | 
classifier.bias   | MISSING    | 
classifier.weight | MISSING    | 

Notes:
- UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:	those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
device cpu; CPU threads=2/4
model_type=modernbert params=140,647,696 attn=sdpa pooling=mean config_changes={'attention_dropout': 0.1, 'mlp_dropout': 0.1, 'embedding_dropout': 0.1, 'classifier_dropout': 0.1, 'num_labels': 16}
training rows=256 seed=1
token lengths (max_length=192): train mean=52.5 p95=114 p99=149 max=156 truncated=0.00%
CPU token cache: 256 rows tokenized once
train batch=16, accumulation=1, effective=16, checkpointing=False, sort=True, pad_multiple=8, fused=False, freeze_embeddings=False
mixed precision: mode=fp16 active=False fallback_to_fp32=True
focal-loss experiment: gamma=1.5
| hfmodel/jhu-clsp__mmBERT-small 微調整 1.0周・微調整だけ | 検証（一般） 正2.0% 誤0 不明145 重大0 その他見送り55/56 | 検証（業務） 正2.0% 誤0 不明192 重大0 その他見送り8/8 | 検証（業務2） 正1.6% 誤0 不明376 重大0 その他見送り33/33 | 検証（日本の調達） 正0.0% 誤0 不明65 重大0 その他見送り1/1 | 学習 79秒・評価
| hfmodel/jhu-clsp__mmBERT-small 微調整 1.0周・今の仕組みだけ | 検証（一般） 正85.8% 誤12 不明9 重大0 その他見送り52/56 | 検証（業務） 正93.9% 誤10 不明2 重大2 その他見送り8/8 | 検証（業務2） 正94.2% 誤9 不明13 重大3 その他見送り22/33 | 検証（日本の調達） 正98.5% 誤0 不明1 重大0 その他見送り1/1 | 学習 79秒・
| hfmodel/jhu-clsp__mmBERT-small 微調整 1.0周・微調整＋今の仕組み（半々） | 検証（一般） 正72.3% 誤2 不明39 重大0 その他見送り54/56 | 検証（業務） 正85.2% 誤2 不明27 重大2 その他見送り8/8 | 検証（業務2） 正84.3% 誤2 不明58 重大1 その他見送り25/33 | 検証（日本の調達） 正93.8% 誤0 不明4 重大0 その他見送り1/1
| hfmodel/jhu-clsp__mmBERT-small 微調整 1.0周・微調整6割＋今の仕組み4割 | 検証（一般） 正14.2% 誤0 不明127 重大0 その他見送り56/56 | 検証（業務） 正29.6% 誤1 不明137 重大1 その他見送り8/8 | 検証（業務2） 正26.2% 誤0 不明282 重大0 その他見送り33/33 | 検証（日本の調達） 正16.9% 誤0 不明54 重大0 その他見送り1/1
| hfmodel/jhu-clsp__mmBERT-small 微調整 1.0周・微調整7割＋今の仕組み3割 | 検証（一般） 正4.7% 誤0 不明141 重大0 その他見送り56/56 | 検証（業務） 正19.9% 誤0 不明157 重大0 その他見送り8/8 | 検証（業務2） 正12.0% 誤0 不明336 重大0 その他見送り33/33 | 検証（日本の調達） 正7.7% 誤0 不明60 重大0 その他見送り1/1 |
Writing model shards:   0%|          | 0/1 [00:00<?, ?it/s]Writing model shards: 100%|██████████| 1/1 [00:00<00:00,  6.89it/s]Writing model shards: 100%|██████████| 1/1 [00:00<00:00,  6.88it/s]
manifest.json written; weights sha256 284e6025b77ce2708fc45208ad31e5892606bfb3d48afe172c98499762d03211
```
## 検査・集計・記録
```
  }
 },
 "timing": {
  "eval_seconds": 76.0,
  "inference_rows": {
   "検証（一般）": 204,
   "検証（日本の調達）": 66,
   "検証（業務2）": 415,
   "検証（業務）": 204
  },
  "inference_seconds": {
   "検証（一般）": 16.75,
   "検証（日本の調達）": 7.39,
   "検証（業務2）": 34.85,
   "検証（業務）": 15.09
  },
  "peak_gpu_gib": null,
  "train_loop_seconds": 78.6,
  "train_total_seconds": 79.1
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
   "attention_dropout": 0.1,
   "classifier_dropout": 0.1,
   "embedding_dropout": 0.1,
   "mlp_dropout": 0.1,
   "num_labels": 16
  },
  "device": "cpu",
  "dropout_override": 0.1,
  "eval_mode": "validation",
  "gpu": null,
  "max_length": 192,
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
   "config.json": "1cedd649cf99f764d13e4dc811a84c53bacf461d71ebbb9f2de1befda658e6e7",
   "labels.json": "fc7e758c07c6b2107cc587a5d50981c7107c1f9a04ab4dc7753c063167ffa3bf",
   "tokenizer.json": "bdb39e9aaa92647d5ce6d16328282a1a6ae9d864bb1000a204862746949df881",
   "tokenizer_config.json": "a610934a0c3e4f0287078cfaf77b6931fd13598445d27f860cc436b8bf2c4454"
  },
  "weights": {
   "model.safetensors": {
    "bytes": 562604960,
    "sha256": "284e6025b77ce2708fc45208ad31e5892606bfb3d48afe172c98499762d03211"
   }
  }
 },
 "outputs_count": 41
}
```
