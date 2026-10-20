# mmBERT-small の試運転（CPU・GitHub Actions）

run: 39430761623　commit: 95586730b3ecaf63de316195398d7ba04346df90

## モデルの取得
```
jhu-clsp/mmBERT-small revision abc32620dd4f6ab06f5fbe905dc25f310618e09f license mit ['license:mit']
Fetching 4 files:   0%|          | 0/4 [00:00<?, ?it/s]Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Fetching 4 files:  50%|█████     | 2/4 [00:00<00:00, 11.83it/s]Fetching 4 files: 100%|██████████| 4/4 [00:00<00:00,  3.78it/s]Fetching 4 files: 100%|██████████| 4/4 [00:00<00:00,  4.20it/s]
intfloat/multilingual-e5-base revision d128750597153bb5987e10b1c3493a34e5a4502a license mit ['license:mit']
Fetching 13 files:   0%|          | 0/13 [00:00<?, ?it/s]Fetching 13 files:  23%|██▎       | 3/13 [00:00<00:00, 29.27it/s]Fetching 13 files:  69%|██████▉   | 9/13 [00:00<00:00, 43.38it/s]Fetching 13 files: 100%|██████████| 13/13 [00:00<00:00, 13.30it/s]
hfmodel/intfloat__multilingual-e5-base:
total 21676
drwxr-xr-x 5 runner runner     4096 Oct 20 13:30 .
drwxr-xr-x 4 runner runner     4096 Oct 20 13:30 ..
drwxr-xr-x 3 runner runner     4096 Oct 20 13:30 .cache
drwxr-xr-x 2 runner runner     4096 Oct 20 13:30 1_Pooling
-rw-r--r-- 1 runner runner      694 Oct 20 13:30 config.json
-rw-r--r-- 1 runner runner      387 Oct 20 13:30 modules.json
drwxr-xr-x 2 runner runner     4096 Oct 20 13:30 onnx
-rw-r--r-- 1 runner runner       57 Oct 20 13:30 sentence_bert_config.json
-rw-r--r-- 1 runner runner  5069051```
## 部品の単体試験
```
[仕事2] 終了（終了コード 0）
[仕事4] 開始（GPU 1）仕事1との違い：FT_TAG=d
[仕事3] 終了（終了コード 0）
[仕事4] 終了（終了コード 0）
[仕事5] 開始（GPU 0）仕事1との違い：FT_TAG=e
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
[仕事1] /opt/hostedtoolcache/Python/3.12.15/x64/bin/python: can't open file '/tmp/tmpb3206odd/missing_script.py': [Errno 2] No such file or directory
[仕事2] /opt/hostedtoolcache/Python/3.12.15/x64/bin/python: can't open file '/tmp/tmpb3206odd/missing_script.py': [Errno 2] No such file or directory
[仕事1] 終了（終了コード 2）
[仕事2] 終了（終了コード 2）
ok

----------------------------------------------------------------------
Ran 54 tests in 4.962s

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
| ★3 | 分類の頭（cls / mean） | NG | OSError: Error no file named model.safetensors, or pytorch_model.bin, found in directory hfmodel/jhu-clsp__mmBERT-small. |
| ★4 | 学習の1ステップ | NG | OSError: Error no file named model.safetensors, or pytorch_model.bin, found in directory hfmodel/jhu-clsp__mmBERT-small. |
| ★5 | 保存と読み込み | NG | OSError: Error no file named model.safetensors, or pytorch_model.bin, found in directory hfmodel/jhu-clsp__mmBERT-small. |
| ☆6 | 速度の目安（CPU） | NG | OSError: Error no file named model.safetensors, or pytorch_model.bin, found in directory hfmodel/jhu-clsp__mmBERT-small. |
| ☆7 | ONNX への書き出し | NG | OSError: Error no file named model.safetensors, or pytorch_model.bin, found in directory hfmodel/jhu-clsp__mmBERT-small. |

必須（★）で NG：3 件

※ CPU の試運転であり、GPU（fp16）での学習・精度・端末での速さは確かめていない。
## finetune_exp.py の通し（末尾）
```
FT_VAL=1: 検証モード（固定の試験は評価しない）。検証の行数 検証（一般） 204, 検証（業務） 204, 検証（業務2） 415, 検証（日本の調達） 66
Traceback (most recent call last):
  File "/home/runner/work/jitsuris-train/jitsuris-train/finetune_exp.py", line 87, in <module>
    model = AutoModelForSequenceClassification.from_pretrained(NAME, num_labels=len(labels), **model_args)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/transformers/models/auto/auto_factory.py", line 411, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/transformers/modeling_utils.py", line 4251, in from_pretrained
    checkpoint_files, sharded_metadata = _get_resolved_checkpoint_files(
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/transformers/modeling_utils.py", line 627, in _get_resolved_checkpoint_files
    raise OSError(
OSError: Error no file named model.safetensors, or pytorch_model.bin, found in directory hfmodel/jhu-clsp__mmBERT-small.
```
## 検査・集計・記録
```
Traceback (most recent call last):
  File "/home/runner/work/jitsuris-train/jitsuris-train/cpu_lab/eval_artifact_integrity.py", line 163, in <module>
    main()
  File "/home/runner/work/jitsuris-train/jitsuris-train/cpu_lab/eval_artifact_integrity.py", line 156, in main
    result = validate_report_dir(args.report_dir,
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/cpu_lab/eval_artifact_integrity.py", line 64, in validate_report_dir
    raise ValueError("no probs report found")
ValueError: no probs report found
```
