# ブラウザ用の書き出しの検査のログの末尾

run: 39432505584　commit: 6b64d531edc227f43dee8cb055971ecefc3a53e9

## 部品の検査
```
{
 "model_dir": "/tmp/tmpohewp3ua/m",
 "weights": {
  "model.safetensors": {
   "sha256": "9a129038d9a00aed0cf6a7ea059ca50a813449061ab87848cf1a13eafdf33b2c",
   "bytes": 7
  }
 },
 "weights_sha256": "9a129038d9a00aed0cf6a7ea059ca50a813449061ab87848cf1a13eafdf33b2c",
 "manifest": {
  "status": "completed",
  "commit": "6b64d531edc227f43dee8cb055971ecefc3a53e9",
  "seed": "1",
  "epochs": 2.0,
  "env": {
   "FT_LR": "1e-4"
  },
  "model": "jhu-clsp/mmBERT-small",
  "hf_revision": null,
  "train_rows": 1,
  "labels": 2,
  "eval_mode": null,
  "created_utc": "2026-10-20T13:41:54Z"
 },
 "expected_sha256": "0000000000000000000000000000000000000000000000000000000000000000",
 "problems": [
  "依頼に書いた SHA-256（000000000000…）と、取ったモデルの SHA-256（9a129038d9a0…）が違う"
 ],
 "warnings": [],
 "ok": false
}
{
 "model_dir": "/tmp/tmp6d9v9ow7/ft_out_job1",
 "weights": {
  "model.safetensors": {
   "sha256": "9a129038d9a00aed0cf6a7ea059ca50a813449061ab87848cf1a13eafdf33b2c",
   "bytes": 7
  }
 },
 "weights_sha256": "9a129038d9a00aed0cf6a7ea059ca50a813449061ab87848cf1a13eafdf33b2c",
 "manifest": {
  "status": "completed",
  "commit": "6b64d531edc227f43dee8cb055971ecefc3a53e9",
  "seed": "1",
  "epochs": 2.0,
  "env": {
   "FT_LR": "1e-4"
  },
  "model": "jhu-clsp/mmBERT-small",
  "hf_revision": null,
  "train_rows": 1,
  "labels": 2,
  "eval_mode": null,
  "created_utc": "2026-10-20T13:41:54Z"
 },
 "expected_sha256": "9a129038d9a00aed0cf6a7ea059ca50a813449061ab87848cf1a13eafdf33b2c",
 "problems": [],
 "warnings": [],
 "ok": true
}
```
## 書き出し
```
Loading weights:   0%|          | 0/201 [00:00<?, ?it/s]Loading weights: 100%|██████████| 201/201 [00:00<00:00, 3810.30it/s]
/home/runner/work/jitsuris-train/jitsuris-train/export_onnx.py:121: DeprecationWarning: You are using the legacy TorchScript-based ONNX export. Starting in PyTorch 2.9, the new torch.export-based ONNX exporter has become the default. Learn more about the new export logic: https://docs.pytorch.org/docs/stable/onnx_export.html. For exporting control flow: https://pytorch.org/tutorials/beginner/onnx/export_control_flow_model_to_onnx_tutorial.html
  torch.onnx.export(Wrap(model), (ids, mask), path, dynamo=False, **kw)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/transformers/masking_utils.py:208: TracerWarning: Converting a tensor to a Python boolean might cause the trace to be incorrect. We can't record the data flow of Python values, so this value will be treated as a constant in the future. This means that the trace might not generalize to other inputs!
  if (padding_length := kv_length + kv_offset - attention_mask.shape[-1]) > 0:
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/transformers/integrations/sdpa_attention.py:136: TracerWarning: Converting a tensor to a Python boolean might cause the trace to be incorrect. We can't record the data flow of Python values, so this value will be treated as a constant in the future. This means that the trace might not generalize to other inputs!
  is_causal = q_length > 1 and attention_mask is None and is_causal
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/torch/onnx/_internal/torchscript_exporter/symbolic_opset11.py:955: UserWarning: Exporting aten::index operator of advanced indexing in opset 17 is achieved by combination of multiple ONNX operators, including Reshape, Transpose, Concat, and Gather. If indices include negative values, the exported graph will produce incorrect results.
  return opset9.index(g, self, index)
[0;93m2026-10-20 13:42:30.654535274 [W:onnxruntime:Default, device_discovery.cc:95 GetPciBusId] Skipping pci_bus_id for PCI path at "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/MSFT1000:00/5620e0c7-8062-4dce-aeb7-520c7ef76171" because filename "5620e0c7-8062-4dce-aeb7-520c7ef76171" did not match expected pattern of [0-9a-f]+:[0-9a-f]+:[0-9a-f]+[.][0-9a-f]+[m
WARNING:root:Please consider to run pre-processing before quantization. Refer to example: https://github.com/microsoft/onnxruntime-inference-examples/blob/main/quantization/image_classification/cpu/ReadMe.md 
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
```
