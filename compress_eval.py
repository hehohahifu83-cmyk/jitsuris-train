"""微調整したモデルを「ブラウザに載る大きさ」に縮めたとき、判定の質がどれだけ変わるかを測る（2026-10-18）。

背景：e5-small は 1.18 億個のパラメータのうち 0.96 億個が単語の埋め込み表（25 万語 × 384）で、変換器の本体は 0.21 億個しかない。
利用者の表に出る単語片はごく一部なので、表を小さくできる。縮め方は次の 4 つ（組み合わせも測る）。
  語彙削減：残す単語片（トークン）だけの表にする。残すのは「学習用の文に出た片」「日本語・英語の 1 文字の片」「特別な記号」「上位 K 個」。
            試験の文で初めて出る片は残さない（新しい表で起きることと同じ）。残さない片は
              unk ＝ <unk> に置き換える（悲観的な見積り）／ chars ＝ 1 文字の片に分けて残す（ブラウザの実装もこちらにする想定）。
  INT8   ：全結合層の重みを 8 ビット整数にする（torch の動的量子化。ONNX Runtime の動的量子化に近い）。埋め込み表は行ごとの対称 INT8 に丸めた値で試す。
  fp16   ：重みを 16 ビット小数に丸めた値で試す。
測るのは判定の質（正解率・重大）と、圧縮なしとの top-1 一致率・確率の最大差。大きさは個数×1 個あたりのバイト数の見積り。
未見セット（blind）は扱わない。学習はしない（微調整が終わったモデルを縮めて試験に流すだけ）。

使い方：finetune_exp.py の FT_COMPRESS=1（FT_COMPRESS_TOPK=上位 K 個、既定 0。FT_COMPRESS_LIMIT=試験ごとの列数の上限、検査用）。
"""
from __future__ import annotations

import copy
import time

import numpy as np

UNDERBAR = "▁"   # SentencePiece の単語頭の印
TEMPLATE_PHRASES = ["列「", "」の値は ", "。同じ表には ", " がある。", "（同じ表: ", "）", "列名: ", " | 値: ", " | 同じ表の列: "]  # 水増しの書き方で使う決まり文句

# 1 文字の片を残す範囲（日本語・英語の表に出る文字）。範囲は閉区間
KEEP_RANGES = [(0x20, 0x7E), (0xA0, 0x24F), (0x2000, 0x206F), (0x20A0, 0x20CF), (0x2100, 0x218F), (0x2190, 0x21FF), (0x2200, 0x22FF), (0x2460, 0x24FF),
               (0x25A0, 0x25FF), (0x3000, 0x303F), (0x3040, 0x309F), (0x30A0, 0x30FF), (0x3200, 0x33FF), (0x4E00, 0x9FFF), (0xFF00, 0xFFEF)]


def is_keep_char(ch):
    o = ord(ch)
    return any(a <= o <= b for a, b in KEEP_RANGES)


def single_char_ids(vocab):
    """vocab：{片: 番号}。『▁』だけ、または『▁』を除いて 1 文字で、その文字が残す範囲にある片の番号。"""
    out = []
    for piece, i in vocab.items():
        s = piece.replace(UNDERBAR, "")
        if piece == UNDERBAR or (len(s) == 1 and is_keep_char(s)):
            out.append(int(i))
    return sorted(out)


def choose_kept_ids(train_ids, vocab_size, special_ids, single_ids, top_k):
    """残す単語片の番号（小さい順）。"""
    kept = {int(i) for i in special_ids}
    kept.update(range(min(int(top_k), vocab_size)))
    kept.update(int(i) for i in single_ids)
    for ids in train_ids:
        kept.update(int(i) for i in ids)
    return sorted(i for i in kept if 0 <= i < vocab_size)


def build_remap(kept, vocab_size, unk_id):
    """元の番号 → 新しい番号。残さない片は unk の新しい番号。unk が残る片に入っていなければ例外。"""
    kept_arr = np.asarray(kept, dtype=np.int64)
    pos = np.searchsorted(kept_arr, unk_id)
    if pos >= len(kept_arr) or kept_arr[pos] != unk_id:
        raise ValueError("unk must be kept")
    remap = np.full(vocab_size, int(pos), dtype=np.int64)
    remap[kept_arr] = np.arange(len(kept_arr))
    return remap


def check_special_positions(kept, remap, special_ids):
    """特別な記号（pad など）が残っていて、縮めたあとも同じ番号か。transformers が pad の番号で位置を数えるので、変わると位置がずれる。"""
    kept_set = set(int(k) for k in kept)
    for s in special_ids:
        if s is None:
            continue
        if int(s) not in kept_set or int(remap[s]) != s:
            raise ValueError(f"special id {s} is dropped or moved")


def apply_vocab(ids_list, kept_set, remap, expand=None, max_len=128, eos_id=2):
    """トークン番号の並びのリスト → 縮めた表の番号の並びのリスト。
    expand(片の番号) が与えられたら、残さない片を 1 文字の片の並びに置き換える（長さが max_len を超えたら末尾を </s> にして切る）。"""
    out = []
    for ids in ids_list:
        seq = ids
        if expand is not None:
            seq = []
            for t in ids:
                if t in kept_set:
                    seq.append(t)
                else:
                    seq.extend(expand(t))
            if len(seq) > max_len:
                seq = seq[:max_len - 1] + [eos_id]
        out.append([int(remap[t]) for t in seq])
    return out


def coverage(ids_list, kept_set):
    """(片の総数, 残さない片の数, 残さない片を含む列の数)。特別な記号は数えない。"""
    total = dropped = cols = 0
    for ids in ids_list:
        n = sum(1 for t in ids if t not in kept_set)
        total += len(ids); dropped += n; cols += n > 0
    return total, dropped, cols


def fake_quant_rows_int8(w):
    """行ごとの対称 INT8 に丸めて戻した値（保存形式が INT8 のときモデルが見る値）。"""
    w = np.asarray(w, dtype=np.float32)
    scale = np.abs(w).max(axis=1, keepdims=True) / 127.0
    scale[scale == 0] = 1.0
    return (np.clip(np.round(w / scale), -127, 127) * scale).astype(np.float32)


def size_report(n_total, n_embed_full, hidden, n_kept):
    """個数と大きさ（MB、1MB=10^6 バイト）の見積り。埋め込み表以外（本体）には位置の表・正規化・全結合層が入る。"""
    body = n_total - n_embed_full
    emb = n_kept * hidden
    mb = lambda params, b: params * b / 1e6
    return {
        "total_params": n_total, "embed_params": n_embed_full, "body_params": body, "kept_embed_params": emb,
        "full_fp32_mb": mb(n_total, 4), "full_int8_mb": mb(n_total, 1),
        "trim_fp32_mb": mb(body + emb, 4), "trim_fp16_mb": mb(body + emb, 2), "trim_int8_mb": mb(body + emb, 1),
    }


def order_by_length(id_lists):
    return sorted(range(len(id_lists)), key=lambda i: (len(id_lists[i]), i))


# ---- ここから torch が要る部分 ----

def cpu_copy(model):
    """元のモデルを動かさずに、CPU の fp32 の複製を作る。"""
    import torch
    state = {k: v.detach().cpu().float().clone() if v.is_floating_point() else v.detach().cpu().clone() for k, v in model.state_dict().items()}
    m = type(model)(model.config)
    m.load_state_dict(state)
    return m.float().eval()


def trimmed_copy(base, kept):
    import torch
    m = copy.deepcopy(base)
    old = m.get_input_embeddings()
    new = torch.nn.Embedding(len(kept), old.embedding_dim, padding_idx=old.padding_idx)
    with torch.no_grad():
        new.weight.copy_(old.weight[torch.as_tensor(kept, dtype=torch.long)])
    m.set_input_embeddings(new)
    return m.eval()


def int8_linear(m):
    import torch
    return torch.ao.quantization.quantize_dynamic(m, {torch.nn.Linear}, dtype=torch.qint8, inplace=False).eval()


def round_embedding_int8(m):
    import torch
    w = m.get_input_embeddings().weight
    with torch.no_grad():
        w.copy_(torch.from_numpy(fake_quant_rows_int8(w.detach().cpu().numpy())))
    return m


def round_weights_fp16(m):
    import torch
    with torch.no_grad():
        for p in m.parameters():
            p.copy_(p.half().float())
    return m


def probs_dev(model, id_lists, pad_id, batch=32, pad_multiple=1, device="cpu"):
    """確率を出す（device は "cpu" か "cuda"。モデルはすでにその装置にある）。長さ順に束ねて詰め物を減らし、元の順に戻して返す。"""
    import torch
    from batching import pad_batch
    out = [None] * len(id_lists)
    order = order_by_length(id_lists)
    with torch.no_grad():
        for s in range(0, len(order), batch):
            idx = order[s:s + batch]
            pids, pmask = pad_batch([id_lists[i] for i in idx], pad_id, pad_multiple)
            logits = model(input_ids=torch.tensor(pids, device=device), attention_mask=torch.tensor(pmask, device=device)).logits.float()
            p = torch.softmax(logits, -1).cpu().numpy()
            for k, i in enumerate(idx):
                out[i] = p[k]
    return np.vstack(out)


probs_cpu = probs_dev   # 古い名前（検査で使っていた）


def run(model, tok, tests, rows, labels, lr_probs, text_fn, prefix, decide, score_real, name, top_k=0, limit=None, max_len=128, model_probs=None, batch=32):
    """縮めた版ごとに試験を流して、(表の行のリスト, 注のリスト) を返す。行の形は finetune_exp.py の表と同じ。"""
    import torch
    if any("blind" in k.lower() for k in tests):
        raise RuntimeError("blind test sets must not be evaluated or saved")
    t_all = time.time()
    base = cpu_copy(model)
    vocab_size, hidden = base.get_input_embeddings().weight.shape
    pad_id, unk_id, eos_id = tok.pad_token_id, tok.unk_token_id, tok.sep_token_id
    special_ids = sorted(set(tok.all_special_ids))
    vocab = tok.get_vocab()
    singles = single_char_ids(vocab)
    train_texts = [text_fn(r, prefix) for r in rows] + [prefix + p for p in TEMPLATE_PHRASES]
    train_ids = tok(train_texts, truncation=True, max_length=max_len, padding=False)["input_ids"]
    kept = choose_kept_ids(train_ids, vocab_size, special_ids, singles, top_k)
    kept_set = set(kept)
    remap = build_remap(kept, vocab_size, unk_id)
    check_special_positions(kept, remap, [pad_id, unk_id, getattr(tok, "cls_token_id", None), eos_id])
    cache = {}

    def expand(t):   # 残さない片 → 残す 1 文字の片の並び（無い文字は unk）
        if t not in cache:
            piece = tok.convert_ids_to_tokens(int(t))
            ids = []
            for ch in piece:
                cid = tok.convert_tokens_to_ids(ch)
                ids.append(cid if (cid != unk_id and cid in kept_set) else unk_id)
            cache[t] = ids or [unk_id]
        return cache[t]

    test_rows = {tn: (te[:limit] if limit else te) for tn, te in tests.items()}
    full_ids = {tn: tok([text_fn(r, prefix) for r in te], truncation=True, max_length=max_len, padding=False)["input_ids"] for tn, te in test_rows.items()}
    lr_use = {tn: (np.asarray(lr_probs[tn])[:limit] if limit else np.asarray(lr_probs[tn])) for tn in tests}
    n_cols = sum(len(v) for v in full_ids.values())
    tot = drop = cols = 0
    for ids in full_ids.values():
        a, b, c = coverage(ids, kept_set); tot += a; drop += b; cols += c
    n_total = sum(p.numel() for p in base.parameters())
    sizes = size_report(n_total, vocab_size * hidden, hidden, len(kept))
    notes = [
        f"- 圧縮の試験（{name}）：残す単語片 {len(kept):,} 個／全体 {vocab_size:,} 個（上位 K={top_k}、学習の文に出た片＋日本語・英語の 1 文字の片＋特別な記号）。試験の文 {n_cols} 列のうち、残さない片を含む列 {cols} 列（片の {100.0 * drop / max(tot, 1):.2f}%）。",
        f"- 大きさの見積り：全体 {sizes['total_params'] / 1e6:.1f}M 個（埋め込み表 {sizes['embed_params'] / 1e6:.1f}M＋本体 {sizes['body_params'] / 1e6:.1f}M）。圧縮なし fp32 {sizes['full_fp32_mb']:.0f}MB／語彙削減後 fp32 {sizes['trim_fp32_mb']:.0f}MB・fp16 {sizes['trim_fp16_mb']:.0f}MB・INT8 {sizes['trim_int8_mb']:.0f}MB（重みだけの見積り。正規化・バイアスは含まない）。",
    ]
    conditions = (("微調整だけ", 1.0), ("微調整7割＋今の仕組み3割", 0.7))
    gpu = "cuda" if torch.cuda.is_available() else "cpu"   # fp32 の計算で済む版は GPU があれば GPU で（INT8 の動的量子化は CPU だけ）
    variants = [
        ("圧縮なし（fp32）", lambda: copy.deepcopy(base), "full", gpu),
        ("語彙削減（残さない片は unk）", lambda: trimmed_copy(base, kept), "unk", gpu),
        ("語彙削減（残さない片は 1 文字に分ける）", lambda: trimmed_copy(base, kept), "chars", gpu),
        ("語彙削減（1 文字）＋INT8（全結合層＋埋め込み表）", lambda: int8_linear(round_embedding_int8(trimmed_copy(base, kept))), "chars", "cpu"),
        ("語彙削減（1 文字）＋fp16（重みを丸める）", lambda: round_weights_fp16(trimmed_copy(base, kept)), "chars", gpu),
    ]
    lines, base_p = [], None
    for vname, make, mode, device in variants:
        m = make().to(device) if device != "cpu" else make()
        if mode == "full":
            ids_by_test = full_ids
        else:
            ids_by_test = {tn: apply_vocab(ids, kept_set, remap, expand if mode == "chars" else None, max_len, eos_id) for tn, ids in full_ids.items()}
        t0 = time.time()
        pr = {tn: probs_dev(m, ids_by_test[tn], pad_id, batch, device=device) for tn in test_rows}
        sec = time.time() - t0
        del m
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        if base_p is None:
            base_p = pr
        agree = float(np.mean(np.concatenate([pr[tn].argmax(1) == base_p[tn].argmax(1) for tn in pr])))
        maxdiff = float(max(np.abs(pr[tn] - base_p[tn]).max() for tn in pr))
        for tag, w in conditions:
            res = []
            for tn, te in test_rows.items():
                P = w * pr[tn] + (1 - w) * lr_use[tn]
                pred = ["unknown" if p == "other" else p for p in decide(labels, P, te)]
                s = score_real(pred, [r[2] for r in te])
                res.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}" + (f" その他見送り{s['other_ok']}/{s['other_ok'] + s['other_ng']}" if s['other_ok'] + s['other_ng'] else ""))
            lines.append(f"| {name}・圧縮【{vname}】・{tag} | " + " | ".join(res) + f" | 圧縮の評価 {sec:.0f}秒（" + (f"CPU {torch.get_num_threads()}スレッド・1列あたり {1000.0 * sec / max(n_cols, 1):.0f}ms" if device == "cpu" else "GPU") + "） |")
            print(lines[-1], flush=True)
        notes.append(f"- {vname}：圧縮なしとの top-1 一致 {100.0 * agree:.2f}%、確率の最大の差 {maxdiff:.3f}")
    if model_probs is not None:   # 本体の評価（GPU の fp16 かもしれない）と、ここの『圧縮なし』の一致
        base_cmp = np.concatenate([base_p[tn].argmax(1) == np.asarray(model_probs[tn])[:len(base_p[tn])].argmax(1) for tn in base_p])
        notes.append(f"- 参考：ここの『圧縮なし（fp32）』と本体の評価（{'GPU の fp16 の混合精度' if torch.cuda.is_available() else 'CPU'}）の top-1 一致 {100.0 * float(np.mean(base_cmp)):.2f}%")
    notes.append(f"- 圧縮の試験の所要 {time.time() - t_all:.0f}秒（数字は保存した微調整済みモデルを縮めて試験に流した結果で、ブラウザの実機の結果ではない）")
    return lines, notes
