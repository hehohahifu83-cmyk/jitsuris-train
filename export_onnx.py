"""微調整した e5 系モデルを、ブラウザ（Transformers.js ＋ onnxruntime-web）で動かす形に書き出して試験する（2026-10-18）。GitHub Actions で動かす（torch・onnx が要る）。

書き出すもの（out/ の中。Transformers.js が読む形）：
  config.json（縮めた語彙の大きさ・id2label）／tokenizer.json（縮めた語彙の Unigram。Precompiled の正規化は外してある）／charsmap.bin（外した正規化の表）／tokenizer_config.json／special_tokens_map.json
  onnx/model.onnx（fp32）／onnx/model_emb8.onnx（埋め込み表だけ行ごとの INT8）／onnx/model_quantized.onnx（さらに全結合層の重みも出力チャネルごとの INT8。重みだけで計算は fp32。ブラウザで使う）／
  onnx/model_dyn8.onnx（比較用：全結合層を動的 INT8＝活性化も 8 ビット。速いが正解率が 3〜5 ポイント落ちた）
入力は input_ids・attention_mask（バッチ・長さは可変）、出力は logits。トークナイズは Transformers.js に任せるが、**正規化だけは自前**（browser_test/charsmap.mjs）：
  Transformers.js は sentencepiece の正規化表（Precompiled）を NFKC で近似しているだけで、半角カナの濁点（ｿﾞ）を合成してしまい、学習時の HF tokenizers と別の片になる。
  そこで書き出す tokenizer.json からは Precompiled を外し、表そのもの（charsmap.bin）を一緒に書き出して、ブラウザで charsmap.mjs が学習時と同じ動きで引く。
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


def linear_weights_to_int8(src, dst, min_params=4096):
    """fp32 の ONNX の全結合層（MatMul の定数の右辺＝重み）を『INT8 の表＋出力チャネルごとの倍率＋DequantizeLinear』に書き換える（重みだけの INT8）。
    計算は fp32 のまま（活性化は 8 ビットにしない）。Kaggle の保存済みモデルでの試験（2026-10-18、e5-small 仕事1）では、動的量子化（活性化も INT8）は
    正解率が 3〜5 ポイント落ちた（top-1 一致 94.8%）が、重みだけを出力チャネルごとの INT8 に丸めた疑似では −0.4 ポイント以内（一致 98.7%）だった。
    その丸め方（出力チャネルごとの対称 INT8、倍率 = 最大絶対値/127）と同じ。onnxruntime が読み込み時に DequantizeLinear を定数畳み込みして fp32 の重みに戻すので、
    配るファイルは INT8（小さい）で、実行時の計算は fp32。小さい行列（min_params 個未満。分類の頭など）は fp32 のまま。
    戻り値：(書き換えた重みの数, その個数)。"""
    import onnx
    from onnx import TensorProto, helper, numpy_helper
    m = onnx.load(src)
    g = m.graph
    opset = max((o.version for o in m.opset_import if o.domain in ("", "ai.onnx")), default=0)
    if opset < 13:
        raise RuntimeError(f"opset {opset} では DequantizeLinear の axis が使えない（13 以上が要る）")
    inits = {i.name: i for i in g.initializer}
    uses = {}
    for node in g.node:
        for k, name in enumerate(node.input):
            uses.setdefault(name, []).append((node, k))
    dq_nodes, n_done, n_params = [], 0, 0
    for name, users in uses.items():
        init = inits.get(name)
        if init is None or init.data_type != TensorProto.FLOAT or len(init.dims) != 2 or int(init.dims[0]) * int(init.dims[1]) < min_params:
            continue
        if not all(node.op_type == "MatMul" and k == 1 for node, k in users):   # MatMul の右辺（重み）だけで使われているもの
            continue
        w = numpy_helper.to_array(init)                                         # [入力, 出力]
        scale = np.abs(w).max(axis=0, keepdims=True) / 127.0                    # 出力チャネル（列）ごと
        scale[scale == 0] = 1.0
        q = np.clip(np.round(w / scale), -127, 127).astype(np.int8)
        g.initializer.remove(init)
        g.initializer.extend([numpy_helper.from_array(q, name + "_q8"), numpy_helper.from_array(scale.reshape(-1).astype(np.float32), name + "_scale")])
        dq_nodes.append(helper.make_node("DequantizeLinear", [name + "_q8", name + "_scale"], [name + "_dq"], axis=1, name=name + "_dequant"))
        for node, k in users:
            node.input[k] = name + "_dq"
        n_done += 1
        n_params += int(q.size)
    for k, node in enumerate(dq_nodes):   # 入力が初期値だけなので、グラフの先頭に置けば使う前に定義される
        g.node.insert(k, node)
    onnx.save(m, dst)
    return n_done, n_params


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


def probs_ort(sess, id_lists, pad_id, batch=32, logits_out=False):
    """onnxruntime で確率（logits_out なら softmax 前の値）を出す。長さ順に束ねて元の順に戻す。"""
    from batching import pad_batch
    out = [None] * len(id_lists)
    order = C.order_by_length(id_lists)
    for s in range(0, len(order), batch):
        idx = order[s:s + batch]
        pids, pmask = pad_batch([id_lists[i] for i in idx], pad_id, 1)
        logits = sess.run(["logits"], {"input_ids": np.asarray(pids, dtype=np.int64), "attention_mask": np.asarray(pmask, dtype=np.int64)})[0].astype(np.float64)
        if logits_out:
            p = logits
        else:
            z = logits - logits.max(axis=1, keepdims=True)
            p = np.exp(z)
            p /= p.sum(axis=1, keepdims=True)
        for k, i in enumerate(idx):
            out[i] = p[k]
    return np.vstack(out)


# トークナイザの一致試験に足す変わった文字列は edge_texts.py（tokenizer_fixtures.py と共通）
from edge_texts import EDGE_TEXTS  # noqa: E402


def write_reference(path, texts, id_lists, sess_q, sess_f, labels, tok_texts=None, tok_ids=None):
    """ブラウザの試験の正解データ：文・縮めたトークナイザの番号・onnxruntime（CPU）の logits（INT8 と fp32）。1 列ずつ（バッチ 1）流す。
    tok_texts / tok_ids は、トークナイザの番号だけを全部の試験文＋変わった文字列で比べるためのもの（モデルは流さない）。"""
    def one(sess, ids):
        return sess.run(["logits"], {"input_ids": np.asarray([ids], dtype=np.int64), "attention_mask": np.ones((1, len(ids)), dtype=np.int64)})[0][0].astype(float).tolist()
    ref = {"texts": texts, "ids": id_lists, "logits_q": [one(sess_q, i) for i in id_lists], "logits_f": [one(sess_f, i) for i in id_lists], "labels": labels}
    if tok_texts is not None:
        ref["tok_texts"], ref["tok_ids"], ref["edge_from"] = tok_texts, tok_ids, len(tok_texts) - len(EDGE_TEXTS)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(ref, f, ensure_ascii=False, separators=(",", ":"))


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
    charsmap = C.pop_precompiled(tj)   # Transformers.js の NFKC による近似は使わない。表は charsmap.bin に出し、ブラウザの charsmap.mjs で引く
    if charsmap is not None:
        with open(os.path.join(out_dir, "charsmap.bin"), "wb") as f:
            f.write(charsmap)
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
    ap.add_argument("--reference", type=int, default=0, help="ブラウザの試験の正解データに使う文の数（試験ごとの先頭から均等に）。0 なら作らない")
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

    fp32, emb8, quant, dyn8 = (os.path.join(out, "onnx", n) for n in ("model.onnx", "model_emb8.onnx", "model_quantized.onnx", "model_dyn8.onnx"))
    export_fp32(trimmed, fp32)
    embedding_to_int8(fp32, emb8, len(kept), hidden)
    n_w8, p_w8 = linear_weights_to_int8(emb8, quant)   # 重みだけ INT8（ブラウザで使う。Transformers.js の dtype 'q8' は model_quantized.onnx を読む）
    quantize_matmul(emb8, dyn8, args.per_channel)       # 比較用：動的量子化（活性化も INT8。正解率が落ちる）

    mb = lambda p: os.path.getsize(p) / 1e6
    tok_mb = os.path.getsize(os.path.join(out, "tokenizer.json")) / 1e6
    report = [f"# ブラウザ用に書き出したモデルの試験（{args.model}）", "",
              f"- 残す単語片 {len(kept):,} 個／全体 {vocab_size:,} 個（上位 K={args.top_k}）。per_channel={args.per_channel}",
              f"- ファイルの大きさ：fp32 {mb(fp32):.1f}MB／埋め込み表だけ INT8 {mb(emb8):.1f}MB／さらに全結合層の重みも INT8＝重みだけ（model_quantized.onnx。{n_w8} 個・{p_w8 / 1e6:.1f}M 個の重み。計算は fp32）{mb(quant):.1f}MB／比較用の動的量子化（model_dyn8.onnx）{mb(dyn8):.1f}MB／tokenizer.json {tok_mb:.1f}MB", ""]

    test_rows = {tn: (te[:args.limit] if args.limit else te) for tn, te in tests.items()}
    ids = {tn: C.cap_ids([e.ids for e in new_tok.encode_batch([text(r, prefix) for r in te])], 128, 2) for tn, te in test_rows.items()}
    lr = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), np.array([r[2] for r in rows]))
    lr_probs = {tn: lr.predict_proba(mat(te)) for tn, te in test_rows.items()}
    ref = {tn: C.probs_dev(trimmed, ids[tn], pad_id) for tn in test_rows}   # PyTorch fp32（縮めたモデル・縮めたトークナイザ）
    n_cols = sum(len(v) for v in ids.values())
    conditions = (("微調整だけ", 1.0), ("微調整7割＋今の仕組み3割", 0.7))
    lines = []
    for vname, path in (("PyTorch fp32", None), ("ONNX fp32", fp32), ("ONNX 埋め込みINT8", emb8), ("ONNX 埋め込みINT8＋全結合層INT8（重みだけ）", quant), ("ONNX 埋め込みINT8＋全結合層INT8（動的量子化）", dyn8)):
        if path is None:
            pr, sec = ref, 0.0
        else:
            sess = ort_session(path)
            t0 = time.time()
            pr = {tn: probs_ort(sess, ids[tn], pad_id) for tn in test_rows}
            sec = time.time() - t0
        agree = float(np.mean(np.concatenate([pr[tn].argmax(1) == ref[tn].argmax(1) for tn in pr])))
        maxdiff = float(max(np.abs(pr[tn] - ref[tn]).max() for tn in pr))
        if path is None:
            lg_ref = {tn: C.probs_dev(trimmed, ids[tn], pad_id, logits_out=True) for tn in test_rows}
            lg_diff = 0.0
            lg_std = float(np.mean([lg_ref[tn].std(axis=1).mean() for tn in lg_ref]))   # 1 列ぶんの logits の広がり（差の大きさを比べる物差し）
        else:
            lg = {tn: probs_ort(sess, ids[tn], pad_id, logits_out=True) for tn in test_rows}
            lg_diff = float(max(np.abs(lg[tn] - lg_ref[tn]).max() for tn in lg))
        for tag, w in conditions:
            res = []
            for tn, te in test_rows.items():
                P = w * pr[tn] + (1 - w) * lr_probs[tn]
                pred = ["unknown" if p == "other" else p for p in decide(labels, P, te)]
                s = score_real(pred, [r[2] for r in te])
                res.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}")
            lines.append(f"| {vname}・{tag} | " + " | ".join(res) + f" | PyTorch fp32 との top-1 一致 {100 * agree:.2f}%・確率の最大差 {maxdiff:.3f}・logits の最大差 {lg_diff:.3f}（logits の広がり {lg_std:.3f}） |")
            print(lines[-1], flush=True)
    report += ["| 版・組み合わせ | " + " | ".join(test_rows) + " | 比較 |", "|---|" + "---|" * (len(test_rows) + 1)] + lines + [""]

    all_ids = [x for tn in test_rows for x in ids[tn]]
    for label, path in (("ONNX fp32", fp32), ("ONNX INT8 重みだけ（model_quantized.onnx）", quant), ("ONNX INT8 動的量子化（model_dyn8.onnx）", dyn8)):
        for threads in (1, 2):
            mean_ms, med_ms = time_single(ort_session(path, threads), all_ids, pad_id)
            report.append(f"- 1 列ずつ流した時間（onnxruntime・CPU・{threads}スレッド・{label}）：平均 {mean_ms:.0f}ms・中央値 {med_ms:.0f}ms／列（全 {n_cols} 列の文の平均 {np.mean([len(x) for x in all_ids]):.0f} トークン）")
    if args.reference:
        per = max(1, args.reference // max(1, len(test_rows)))
        pick = [(tn, i) for tn in test_rows for i in range(min(per, len(ids[tn])))]
        texts = [text(test_rows[tn][i], prefix) for tn, i in pick]
        tok_texts = [text(r, prefix) for tn in test_rows for r in test_rows[tn]] + [prefix + t for t in EDGE_TEXTS]
        tok_ids = C.cap_ids([e.ids for e in new_tok.encode_batch(tok_texts)], 128, 2)
        write_reference(os.path.join(out, "reference.json"), texts, [ids[tn][i] for tn, i in pick], ort_session(quant), ort_session(fp32), labels, tok_texts, tok_ids)
        report.append(f"- ブラウザの試験の正解データ（reference.json）：モデルを流す文 {len(texts)} 文／トークナイザの番号だけを比べる文 {len(tok_texts)} 文（試験の全列＋変わった文字列 {len(EDGE_TEXTS)} 個）")
    report += ["", "数字は GitHub Actions の CPU の結果で、ブラウザ（WASM）の実機の速さではない。精度は保存したモデルを書き出して試験に流した結果。"]
    open(os.path.join(out, "REPORT.md"), "w", encoding="utf-8").write("\n".join(report) + "\n")
    print("\n".join(report))


if __name__ == "__main__":
    main()
