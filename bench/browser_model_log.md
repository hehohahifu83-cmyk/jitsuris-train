# ブラウザ用の書き出しの検査のログの末尾

run: 39427927910　commit: d3f029245a581fec2259995f435e23d29853fd84

## 部品の検査
```
test_cap_ids (tests.test_compress_eval.PureFunctionsTest.test_cap_ids) ... ok
test_choose_kept_ids_is_sorted_unique_and_in_range (tests.test_compress_eval.PureFunctionsTest.test_choose_kept_ids_is_sorted_unique_and_in_range) ... ok
test_coverage_counts_dropped_tokens_and_columns (tests.test_compress_eval.PureFunctionsTest.test_coverage_counts_dropped_tokens_and_columns) ... ok
test_edit_tokenizer_json_keeps_scores_unk_and_renumbers_special_tokens (tests.test_compress_eval.PureFunctionsTest.test_edit_tokenizer_json_keeps_scores_unk_and_renumbers_special_tokens) ... ok
test_int8_rounding_error_is_below_half_a_step_and_zero_rows_stay_zero (tests.test_compress_eval.PureFunctionsTest.test_int8_rounding_error_is_below_half_a_step_and_zero_rows_stay_zero) ... ok
test_order_by_length_is_a_stable_permutation (tests.test_compress_eval.PureFunctionsTest.test_order_by_length_is_a_stable_permutation) ... ok
test_pop_precompiled_removes_only_the_leading_precompiled_normalizer_and_returns_its_table (tests.test_compress_eval.PureFunctionsTest.test_pop_precompiled_removes_only_the_leading_precompiled_normalizer_and_returns_its_table) ... ok
test_quantize_rows_int8_roundtrip_and_ranges (tests.test_compress_eval.PureFunctionsTest.test_quantize_rows_int8_roundtrip_and_ranges) ... ok
test_remap_sends_dropped_tokens_to_unk_and_keeps_order (tests.test_compress_eval.PureFunctionsTest.test_remap_sends_dropped_tokens_to_unk_and_keeps_order) ... ok
test_single_char_ids_keep_only_japanese_and_english_characters (tests.test_compress_eval.PureFunctionsTest.test_single_char_ids_keep_only_japanese_and_english_characters) ... ok
test_size_report (tests.test_compress_eval.PureFunctionsTest.test_size_report) ... ok
test_special_positions_must_not_move (tests.test_compress_eval.PureFunctionsTest.test_special_positions_must_not_move) ... ok
test_cpu_copy_is_equal_and_independent (tests.test_compress_eval.TorchTest.test_cpu_copy_is_equal_and_independent) ... /home/runner/work/jitsuris-train/jitsuris-train/tests/test_compress_eval.py:165: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /__w/pytorch/pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:820.)
  self.assertGreater(float(self.model.get_input_embeddings().weight.abs().sum()), 0.0)
ok
test_int8_and_fp16_variants_run_and_stay_close (tests.test_compress_eval.TorchTest.test_int8_and_fp16_variants_run_and_stay_close) ... /home/runner/work/jitsuris-train/jitsuris-train/compress_eval.py:220: DeprecationWarning: torch.ao.quantization is deprecated and will be removed in 2.10. 
For migrations of users: 
1. Eager mode quantization (torch.ao.quantization.quantize, torch.ao.quantization.quantize_dynamic), please migrate to use torchao eager mode quantize_ API instead 
2. FX graph mode quantization (torch.ao.quantization.quantize_fx.prepare_fx,torch.ao.quantization.quantize_fx.convert_fx, please migrate to use torchao pt2e quantization API instead (prepare_pt2e, convert_pt2e) 
3. pt2e quantization has been migrated to torchao (https://github.com/pytorch/ao/tree/main/torchao/quantization/pt2e) 
see https://github.com/pytorch/ao/issues/2259 for more details
  return torch.ao.quantization.quantize_dynamic(m, {torch.nn.Linear}, dtype=torch.qint8, inplace=False).eval()
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/torch/ao/quantization/quantize.py:570: DeprecationWarning: torch.ao.quantization is deprecated and will be removed in 2.10. 
For migrations of users: 
1. Eager mode quantization (torch.ao.quantization.quantize, torch.ao.quantization.quantize_dynamic), please migrate to use torchao eager mode quantize_ API instead 
2. FX graph mode quantization (torch.ao.quantization.quantize_fx.prepare_fx,torch.ao.quantization.quantize_fx.convert_fx, please migrate to use torchao pt2e quantization API instead (prepare_pt2e, convert_pt2e) 
3. pt2e quantization has been migrated to torchao (https://github.com/pytorch/ao/tree/main/torchao/quantization/pt2e) 
see https://github.com/pytorch/ao/issues/2259 for more details
  convert(model, mapping, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/torch/ao/nn/quantized/modules/utils.py:72: UserWarning: torch.quantize_per_tensor, torch.quantize_per_channel and other quantized tensor creation functions that produce tensors with dtype torch.quint8, torch.qint8, and torch.qint32 are deprecated and will be removed in a future PyTorch release. Please see https://github.com/pytorch/pytorch/issues/184982 for more information. (Triggered internally at /__w/pytorch/pytorch/aten/src/ATen/quantized/Quantizer.cpp:111.)
  qweight = torch.quantize_per_tensor(
ok
test_probs_cpu_restores_the_original_order_across_batches (tests.test_compress_eval.TorchTest.test_probs_cpu_restores_the_original_order_across_batches) ... ok
test_round_linear_int8_changes_weights_by_less_than_half_a_step (tests.test_compress_eval.TorchTest.test_round_linear_int8_changes_weights_by_less_than_half_a_step) ... ok
test_run_end_to_end_with_a_fake_tokenizer (tests.test_compress_eval.TorchTest.test_run_end_to_end_with_a_fake_tokenizer) ... | fake・圧縮【圧縮なし（fp32）】・微調整だけ | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【圧縮なし（fp32）】・微調整7割＋今の仕組み3割 | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【語彙削減（残さない片は unk）】・微調整だけ | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【語彙削減（残さない片は unk）】・微調整7割＋今の仕組み3割 | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【語彙削減（残さない片は 1 文字に分ける）】・微調整だけ | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【語彙削減（残さない片は 1 文字に分ける）】・微調整7割＋今の仕組み3割 | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【語彙削減（残さない片は 1 文字に分ける）＋INT8の重み（全結合層・埋め込み表を丸める疑似）】・微調整だけ | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【語彙削減（残さない片は 1 文字に分ける）＋INT8の重み（全結合層・埋め込み表を丸める疑似）】・微調整7割＋今の仕組み3割 | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【語彙削減（残さない片は 1 文字に分ける）＋INT8の動的量子化（全結合層）＋埋め込み表INT8】・微調整だけ | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【語彙削減（残さない片は 1 文字に分ける）＋INT8の動的量子化（全結合層）＋埋め込み表INT8】・微調整7割＋今の仕組み3割 | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【語彙削減（残さない片は 1 文字に分ける）＋fp16（重みを丸める）】・微調整だけ | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
| fake・圧縮【語彙削減（残さない片は 1 文字に分ける）＋fp16（重みを丸める）】・微調整7割＋今の仕組み3割 | t1 正33.3% 誤2 不明0 重大0 | 圧縮の評価 0秒（CPU 2スレッド・1列あたり 0ms） |
ok
test_trimmed_model_gives_identical_logits_on_kept_tokens (tests.test_compress_eval.TorchTest.test_trimmed_model_gives_identical_logits_on_kept_tokens) ... ok
test_trimmed_tokenizer_matches_full_tokenizer_when_all_pieces_are_kept (tests.test_compress_eval.TorchTest.test_trimmed_tokenizer_matches_full_tokenizer_when_all_pieces_are_kept) ... ok
test_edge_texts_contain_the_half_width_katakana_cases_that_failed_in_the_browser (tests.test_tokenizer_fixtures.FixtureHelpersTest.test_edge_texts_contain_the_half_width_katakana_cases_that_failed_in_the_browser) ... ok
test_extenders_cover_the_marks_that_change_graphemes (tests.test_tokenizer_fixtures.FixtureHelpersTest.test_extenders_cover_the_marks_that_change_graphemes) ... ok
test_pairs_and_triples_have_a_base_then_marks (tests.test_tokenizer_fixtures.FixtureHelpersTest.test_pairs_and_triples_have_a_base_then_marks) ... ok
test_random_strings_are_reproducible_and_never_contain_surrogates (tests.test_tokenizer_fixtures.FixtureHelpersTest.test_random_strings_are_reproducible_and_never_contain_surrogates) ... ok
test_scalar_values_skip_only_surrogates (tests.test_tokenizer_fixtures.FixtureHelpersTest.test_scalar_values_skip_only_surrogates) ... ok

----------------------------------------------------------------------
Ran 31 tests in 3.200s

OK
```
## 書き出し
```
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights:   0%|          | 0/199 [00:00<?, ?it/s]Loading weights: 100%|██████████| 199/199 [00:00<00:00, 24961.62it/s]
[transformers] [1mBertForSequenceClassification LOAD REPORT[0m from: intfloat/multilingual-e5-small
Key               | Status  | 
------------------+---------+-
classifier.weight | MISSING | 
classifier.bias   | MISSING | 

Notes:
- MISSING:	those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
/home/runner/work/jitsuris-train/jitsuris-train/export_onnx.py:121: DeprecationWarning: You are using the legacy TorchScript-based ONNX export. Starting in PyTorch 2.9, the new torch.export-based ONNX exporter has become the default. Learn more about the new export logic: https://docs.pytorch.org/docs/stable/onnx_export.html. For exporting control flow: https://pytorch.org/tutorials/beginner/onnx/export_control_flow_model_to_onnx_tutorial.html
  torch.onnx.export(Wrap(model), (ids, mask), path, dynamo=False, **kw)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/transformers/masking_utils.py:208: TracerWarning: Converting a tensor to a Python boolean might cause the trace to be incorrect. We can't record the data flow of Python values, so this value will be treated as a constant in the future. This means that the trace might not generalize to other inputs!
  if (padding_length := kv_length + kv_offset - attention_mask.shape[-1]) > 0:
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/transformers/integrations/sdpa_attention.py:136: TracerWarning: Converting a tensor to a Python boolean might cause the trace to be incorrect. We can't record the data flow of Python values, so this value will be treated as a constant in the future. This means that the trace might not generalize to other inputs!
  is_causal = q_length > 1 and attention_mask is None and is_causal
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/torch/onnx/_internal/torchscript_exporter/symbolic_opset11.py:955: UserWarning: Exporting aten::index operator of advanced indexing in opset 17 is achieved by combination of multiple ONNX operators, including Reshape, Transpose, Concat, and Gather. If indices include negative values, the exported graph will produce incorrect results.
  return opset9.index(g, self, index)
[0;93m2026-10-20 13:09:54.699430762 [W:onnxruntime:Default, device_discovery.cc:95 GetPciBusId] Skipping pci_bus_id for PCI path at "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/MSFT1000:00/5620e0c7-8062-4dce-aeb7-520c7ef76171" because filename "5620e0c7-8062-4dce-aeb7-520c7ef76171" did not match expected pattern of [0-9a-f]+:[0-9a-f]+:[0-9a-f]+[.][0-9a-f]+[m
WARNING:root:Please consider to run pre-processing before quantization. Refer to example: https://github.com/microsoft/onnxruntime-inference-examples/blob/main/quantization/image_classification/cpu/ReadMe.md 
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
```
