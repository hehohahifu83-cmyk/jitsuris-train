"""微調整した e5 系モデルを、ブラウザ（Transformers.js ＋ onnxruntime-web）で動かす形に書き出して試験する（2026-10-18）。GitHub Actions で動かす（torch・onnx が要る）。

書き出すもの（out/ の中。Transformers.js が読む形）：
  config.json（縮めた語彙の大きさ・id2label）／tokenizer.json（縮めた語彙の Unigram）／tokenizer_config.json／special_tokens_map.json
  onnx/model.onnx（fp32）／onnx/model_emb8.onnx（埋め込み表だけ行ごとの INT8）／onnx/model_quantized.onnx（さらに全結合層を動的 INT8）
入力は input_ids・attention_mask（バッチ・長さは可変）、出力は logits。トークナイズは Transformers.js に任せるので、ブラウザ側に自作の部品は要らない。
試験：onnxruntime（CPU）で試験を流し、PyTorch の fp32 と比べた一致率・正解率・重大、ファイルの大きさ、1 列あたりの時間を REPORT.md に出す。
未見セット（blind）は扱わない。学習はしない。数字はブラウザの実機の結果ではない。

使い方：python export_onnx.py --model intfloat/multilingual-e5-small --out browser_model [--top-k 0] [--limit 0] [--per-channel] [--labels labels.json]
"""
from __future__ import annotations

import argparse
import json
import os
import time

import numpy as np

import compress_eval as C


def embedding_to_int8(src, dst, vocab, hidden):
    """fp32 の ONNX の『単語の埋め込み表の Gather』を『INT8 の表＋行ごとの倍率』に書き換える。書き換えた Gather の名前を返す。"""
    import onnx
    from onnx import TensorProto, helper, numpy_helper
    m = onnx.load(src)
    g = m.graph
    inits = {i.name: i for i in g.initializer}
    target = None
    for n in g.node:
        if n.op_type == "Gather" and n.input[0] in inits and list(inits[n.input[0]].dims) == [vocab, hidden]:
            target = n
            break
    if target is None:
        raise RuntimeError(f"単語の埋め込み表（{vocab}×{hidden}）の Gather が見つからない")
    wname = target.input[0]
    q, scale = C.quantize_rows_int8(numpy_helper.to_array(inits[wname]))
    g.initializer.remove(inits[wname])
    g.initializer.extend([numpy_helper.from_array(q, wname + "_q8"), numpy_helper.from_array(scale, wname + "_scale")])
    ids, out, base = target.input[1], target.output[0], (target.name or "emb")
    new_nodes = [
        helper.make_node("Gather", [wname + "_q8", ids], [out + "_q8"], axis=0, name=base + "_q8"),
        helper.make_node("Cast", [out + "_q8"], [out + "_f32"], to=TensorProto.FLOAT, name=base + "_cast"),
        helper.make_node("Gather", [wname + "_scale", ids], [out + "_scale"], axis=0, name=base + "_scale"),
        helper.make_node("Mul", [out + "_f32", out + "_scale"], [out], name=base + "_mul"),
    ]
    idx = list(g.node).index(target)
    del g.node[idx]
    for k, node in enumerate(new_nodes):
        g.node.insert(idx + k, node)
    onnx.save(m, dst)
    return base


def export_fp32(model, path, opset=17):
    """PyTorch → ONNX（fp32）。入力 input_ids・attention_mask、出力 logits。バッチと長さは可変。"""
    import torch

    class Wrap(torch.nn.Module):
        def __init__(self, m):
            super().__init__()
            self.m = m

        def forward(self, input_ids, attention_mask):
            return self.m(input_ids=input_ids, attention_mask=attention_mask).logits

    model = model.eval().cpu()
    ids = torch.tensor([[0, 10, 11, 12, 2], [0, 10, 2, 1, 1]], dtype=torch.long)
    mask = torch.tensor([[1, 1, 1, 1, 1], [1, 1, 1, 0, 0]], dtype=torch.long)
    kw = dict(input_names=["input_ids", "attention_mask"], output_names=["logits"], opset_version=opset,
              dynamic_axes={"input_ids": {0: "batch", 1: "seq"}, "attention_mask": {0: "batch", 1: "seq"}, "logits": {0: "batch"}})
    try:
        torch.onnx.export(Wrap(model), (ids, mask), path, dynamo=False, **kw)
    except Exception as exc:  # noqa: BLE001  古い方式が無い版では既定の方式（onnxscript が要る）に切り替える
        print("legacy exporter failed:", type(exc).__name__, str(exc)[:200], flush=True)
        torch.onnx.export(Wrap(model), (ids, mask), path, **kw)


def quantize_matmul(src, dst, per_channel=False):
    from onnxruntime.quantization import QuantType, quantize_dynamic
    quantize_dynamic(src, dst, weight_type=QuantType.QInt8, per_channel=per_channel, op_types_to_quantize=["MatMul"], extra_options={"MatMulConstBOnly": True})


def ort_session(path, threads=0):
    import onnxruntime as ort
    so = ort.SessionOptions()
    if threads:
        so.intra_op_num_threads = threads
    return ort.InferenceSession(path, so, providers=["CPUExecutionProvider"])


def probs_ort(sess, id_lists, pad_id, batch=32):
    from batching import pad_batch
    out = [None] * len(id_lists)
    order = C.order_by_length(id_lists)
    for s in range(0, len(order), batch):
        idx = order[s:s + batch]
        pids, pmask = pad_batch([id_lists[i] for i in idx], pad_id, 1)
        logits = sess.run(["logits"], {"input_ids": np.asarray(pids, dtype=np.int64), "attention_mask": np.asarray(pmask, dtype=np.int64)})[0].astype(np.float64)
        logits -= logits.max(axis=1, keepdims=True)
        p = np.exp(logits)
        p /= p.sum(axis=1, keepdims=True)
        for k, i in enumerate(idx):
            out[i] = p[k]
    return np.vstack(out)


def time_single(sess, id_lists, pad_id, n=60):
    """1 列ずつ（バッチ 1）流したときの 1 列あたりの平均 ms と中央値 ms。"""
    ts = []
    for ids in id_lists[:n]:
        feed = {"input_ids": np.asarray([ids], dtype=np.int64), "attention_mask": np.ones((1, len(ids)), dtype=np.int64)}
        t0 = time.perf_counter()
        sess.run(["logits"], feed)
        ts.append(1000.0 * (time.perf_counter() - t0))
    ts = ts[2:] if len(ts) > 4 else ts   # 最初の数回は準備で遅い
    return float(np.mean(ts)), float(np.median(ts))


def write_tokenizer_files(tok, kept, out_dir):
    """縮めた tokenizer.json と、Transformers.js が読む tokenizer_config.json・special_tokens_map.json を書く。"""
    tok.save_pretrained(out_dir)
    tj = C.edit_tokenizer_json(json.loads(tok.backend_tokenizer.to_str()), kept)
    with open(os.path.join(out_dir, "tokenizer.json"), "w", encoding="utf-8") as f:
        json.dump(tj, f, ensure_ascii=False, separators=(",", ":"))
    cfg_path = os.path.join(out_dir, "tokenizer_config.json")
    if os.path.exists(cfg_path):
        cfg = json.load(open(cfg_path, encoding="utf-8"))
        index = {int(old): new for new, old in enumerate(kept)}
        dec = cfg.get("added_tokens_decoder")
        if isinstance(dec, dict):
            cfg["added_tokens_decoder"] = {str(index[int(k)]): v for k, v in dec.items() if int(k) in index}
        json.dump(cfg, open(cfg_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for stale in ("sentencepiece.bpe.model", "spiece.model"):   # 縮める前の語彙。ブラウザには要らない
        p = os.path.join(out_dir, stale)
        if os.path.exists(p):
            os.remove(p)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--out", default="browser_model")
    ap.add_argument("--top-k", type=int, default=0)
    ap.add_argument("--limit", type=int, default=0, help="試験ごとの列数の上限（検査用。0 なら全部）")
    ap.add_argument("--per-channel", action="store_true")
    ap.add_argument("--labels", default="")
    args = ap.parse_args(argv)

    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    from sklearn.linear_model import LogisticRegression
    import features
    features.USE_NUM2 = True
    from encoder_exp import rows, tests, text
    from llm_baseline import score_real
    from train3 import decide, mat
    if any("blind" in k.lower() for k in tests):
        raise RuntimeError("blind test sets must not be evaluated or saved")

    labels = json.load(open(args.labels, encoding="utf-8")) if args.labels else sorted(set(r[2] for r in rows))
    prefix = "query: " if "e5" in args.model.lower() else ""
    tok = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForSequenceClassification.from_pretrained(args.model, num_labels=len(labels)).eval()
    base = C.cpu_copy(model)
    vocab_size, hidden = base.get_input_embeddings().weight.shape
    pad_id, unk_id = tok.pad_token_id, tok.unk_token_id
    train_ids = tok([text(r, prefix) for r in rows] + [prefix + p for p in C.TEMPLATE_PHRASES], truncation=True, max_length=128, padding=False)["input_ids"]
    kept = C.choose_kept_ids(train_ids, vocab_size, sorted(set(tok.all_special_ids)), C.single_char_ids(tok.get_vocab()), args.top_k)
    C.check_special_positions(kept, C.build_remap(kept, vocab_size, unk_id), [pad_id, unk_id, getattr(tok, "cls_token_id", None), tok.sep_token_id])
    trimmed = C.trimmed_copy(base, kept)
    trimmed.config.vocab_size = len(kept)
    trimmed.config.id2label = {i: l for i, l in enumerate(labels)}
    trimmed.config.label2id = {l: i for i, l in enumerate(labels)}

    out = args.out
    os.makedirs(os.path.join(out, "onnx"), exist_ok=True)
    trimmed.config.save_pretrained(out)
    write_tokenizer_files(tok, kept, out)
    new_tok = C.trimmed_tokenizer(tok, kept)

    fp32, emb8, quant = (os.path.join(out, "onnx", n) for n in ("model.onnx", "model_emb8.onnx", "model_quantized.onnx"))
    export_fp32(trimmed, fp32)
    embedding_to_int8(fp32, emb8, len(kept), hidden)
    quantize_matmul(emb8, quant, args.per_channel)

    mb = lambda p: os.path.getsize(p) / 1e6
    tok_mb = os.path.getsize(os.path.join(out, "tokenizer.json")) / 1e6
    report = [f"# ブラウザ用に書き出したモデルの試験（{args.model}）", "",
              f"- 残す単語片 {len(kept):,} 個／全体 {vocab_size:,} 個（上位 K={args.top_k}）。per_channel={args.per_channel}",
              f"- ファイルの大きさ：fp32 {mb(fp32):.1f}MB／埋め込み表だけ INT8 {mb(emb8):.1f}MB／さらに全結合層も INT8（model_quantized.onnx）{mb(quant):.1f}MB／tokenizer.json {tok_mb:.1f}MB", ""]

    test_rows = {tn: (te[:args.limit] if args.limit else te) for tn, te in tests.items()}
    ids = {tn: C.cap_ids([e.ids for e in new_tok.encode_batch([text(r, prefix) for r in te])], 128, 2) for tn, te in test_rows.items()}
    lr = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), np.array([r[2] for r in rows]))
    lr_probs = {tn: lr.predict_proba(mat(te)) for tn, te in test_rows.items()}
    ref = {tn: C.probs_dev(trimmed, ids[tn], pad_id) for tn in test_rows}   # PyTorch fp32（縮めたモデル・縮めたトークナイザ）
    n_cols = sum(len(v) for v in ids.values())
    conditions = (("微調整だけ", 1.0), ("微調整7割＋今の仕組み3割", 0.7))
    lines = []
    for vname, path in (("PyTorch fp32", None), ("ONNX fp32", fp32), ("ONNX 埋め込みINT8", emb8), ("ONNX 埋め込みINT8＋全結合層INT8", quant)):
        if path is None:
            pr, sec = ref, 0.0
        else:
            sess = ort_session(path)
            t0 = time.time()
            pr = {tn: probs_ort(sess, ids[tn], pad_id) for tn in test_rows}
            sec = time.time() - t0
        agree = float(np.mean(np.concatenate([pr[tn].argmax(1) == ref[tn].argmax(1) for tn in pr])))
        maxdiff = float(max(np.abs(pr[tn] - ref[tn]).max() for tn in pr))
        for tag, w in conditions:
            res = []
            for tn, te in test_rows.items():
                P = w * pr[tn] + (1 - w) * lr_probs[tn]
                pred = ["unknown" if p == "other" else p for p in decide(labels, P, te)]
                s = score_real(pred, [r[2] for r in te])
                res.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}")
            lines.append(f"| {vname}・{tag} | " + " | ".join(res) + f" | PyTorch fp32 との top-1 一致 {100 * agree:.2f}%・確率の最大差 {maxdiff:.3f} |")
            print(lines[-1], flush=True)
    report += ["| 版・組み合わせ | " + " | ".join(test_rows) + " | 比較 |", "|---|" + "---|" * (len(test_rows) + 1)] + lines + [""]

    all_ids = [x for tn in test_rows for x in ids[tn]]
    for label, path in (("ONNX fp32", fp32), ("ONNX INT8（model_quantized.onnx）", quant)):
        for threads in (1, 2):
            mean_ms, med_ms = time_single(ort_session(path, threads), all_ids, pad_id)
            report.append(f"- 1 列ずつ流した時間（onnxruntime・CPU・{threads}スレッド・{label}）：平均 {mean_ms:.0f}ms・中央値 {med_ms:.0f}ms／列（全 {n_cols} 列の文の平均 {np.mean([len(x) for x in all_ids]):.0f} トークン）")
    report += ["", "数字は GitHub Actions の CPU の結果で、ブラウザ（WASM）の実機の速さではない。精度は保存したモデルを書き出して試験に流した結果。"]
    open(os.path.join(out, "REPORT.md"), "w", encoding="utf-8").write("\n".join(report) + "\n")
    print("\n".join(report))


if __name__ == "__main__":
    main()
