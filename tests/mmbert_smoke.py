"""mmBERT-small（jhu-clsp/mmBERT-small、MIT）を、今の学習の道筋に通せるかの試運転（CPU・GitHub Actions）。2026-10-20。

使い方：python tests/mmbert_smoke.py <mmBERT の置き場> [--e5 <E5 の置き場（トークナイザだけで可）>] [--out 結果.md] [--onnx]

確かめること（必須は★、参考は☆）：
 ★1 読み込み：config・トークナイザ・重み。型・層・隠れ・語彙・パラメータ数・classifier_pooling・注意の実装。
 ★2 トークナイザ：日本語の入力文の分割、特殊トークン、token_type_ids の有無、128 での切り捨ての割合（学習データと試験データの実際の文で、E5 と並べる）。
 ★3 分類の頭：AutoModelForSequenceClassification(num_labels=15) に通る。pooling が cls / mean の両方で動く。
 ★4 学習の 1 ステップ：順伝播・逆伝播・AdamW・勾配と損失が有限。
 ★5 保存と読み込み：save_pretrained → from_pretrained → 同じ入力で logits が一致。
 ☆6 速度の目安（この CPU での値。端末での速さではない）。
 ☆7 ONNX への書き出し（--onnx）：通れば onnxruntime の logits が PyTorch と一致するか。
列の値そのものは結果に出さない（件数と長さの統計だけ）。未見セット（blind_set*）は読まない。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import time
import traceback

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

results = []   # (記号, 名前, 状態, 説明)


def record(kind, name, ok, detail=""):
    results.append((kind, name, "OK" if ok else "NG", str(detail)))
    print(f"[{'OK' if ok else 'NG'}] {kind} {name}: {detail}", flush=True)


def guard(kind, name):
    def deco(fn):
        def run(*a, **k):
            try:
                return fn(*a, **k)
            except Exception as e:  # noqa: BLE001
                tb = traceback.format_exc()[-1500:]
                record(kind, name, False, f"{type(e).__name__}: {str(e)[:300]}")
                print(tb, flush=True)
                return None
        return run
    return deco


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model_dir")
    ap.add_argument("--e5", default=None)
    ap.add_argument("--out", default="mmbert_smoke.md")
    ap.add_argument("--onnx", action="store_true")
    a = ap.parse_args()
    sys.argv = sys.argv[:1]   # encoder_exp などの読み込みが argv を見ないように空にする

    import numpy as np
    import torch
    import transformers
    from transformers import AutoConfig, AutoModelForSequenceClassification, AutoTokenizer
    import provenance

    info = {"transformers": transformers.__version__, "torch": torch.__version__, "python": sys.version.split()[0]}
    print(json.dumps(info), flush=True)
    import model_setup

    def load_cls(path, pooling=None, num_labels=15):
        """finetune_exp.py と同じ作り方（model_setup）で分類モデルを読む。"""
        cfg = AutoConfig.from_pretrained(path)
        ch = model_setup.apply_modernbert_overrides(cfg, num_labels=num_labels, pooling=pooling or "")
        m = AutoModelForSequenceClassification.from_pretrained(path, config=cfg, attn_implementation="sdpa")
        return m, ch

    # ---- ★1 読み込み ----
    @guard("★1", "読み込み（config・トークナイザ・重み）")
    def load():
        cfg = AutoConfig.from_pretrained(a.model_dir)
        tok = AutoTokenizer.from_pretrained(a.model_dir)
        keys = ("model_type", "architectures", "hidden_size", "num_hidden_layers", "num_attention_heads", "intermediate_size", "vocab_size",
                "max_position_embeddings", "classifier_pooling", "classifier_activation", "classifier_bias", "classifier_dropout",
                "global_attn_every_n_layers", "local_attention", "pad_token_id", "bos_token_id", "eos_token_id", "cls_token_id", "sep_token_id",
                "reference_compile", "tie_word_embeddings")
        shown = {k: getattr(cfg, k, None) for k in keys}
        record("★1", "config", cfg.model_type == "modernbert", json.dumps(shown, ensure_ascii=False))
        record("★1", "トークナイザ", True, f"{type(tok).__name__} vocab={len(tok)} pad={tok.pad_token!r}/{tok.pad_token_id} bos={tok.bos_token!r}/{tok.bos_token_id} "
                                         f"eos={tok.eos_token!r}/{tok.eos_token_id} cls={tok.cls_token!r} sep={tok.sep_token!r} unk={tok.unk_token!r} model_max_length={tok.model_max_length} "
                                         f"model_input_names={tok.model_input_names}")
        return cfg, tok
    loaded = load()
    if not loaded:
        return finish(a, info)
    cfg, tok = loaded
    tok.model_input_names = ["input_ids", "attention_mask"]   # finetune_exp.py と同じ

    # ---- ★2 トークナイザ（実際の学習・試験の文で）----
    @guard("★2", "トークナイザ（日本語の入力文・切り捨て）")
    def tokenization():
        samples = ["列名: 金額 | 値: 1,200, 3,400, 560 | 同じ表の列: 日付, 取引先, 摘要", "列名: 取引先名 | 値: 株式会社山田商事, 有限会社佐藤工業 | 同じ表の列: 金額, 日付",
                   "query: 列名: 税率 | 値: 0.10, 0.08 | 同じ表の列: 適用区分, 税額", "列名: Ｖａｌｕｅ　１ | 値: ABC-001, ABC-002 | 同じ表の列: ID, name"]
        for s in samples:
            enc = tok(s, truncation=True, max_length=128)
            pieces = tok.convert_ids_to_tokens(enc["input_ids"])
            record("★2", "分割の例", True, f"{len(enc['input_ids'])} トークン／keys={sorted(enc.keys())}／先頭 {pieces[:6]} … 末尾 {pieces[-3:]}")
        enc = tok(samples[:2], padding=True, return_tensors="pt")
        has_tt = "token_type_ids" in tok(samples[0]).keys()
        record("★2", "パディング", "attention_mask" in enc and not has_tt,
               f"padding_side={tok.padding_side} shape={tuple(enc['input_ids'].shape)} mask={enc['attention_mask'].tolist()} token_type_ids を返す={has_tt}")
        import encoder_exp as E
        pref = ""
        def lens(t, prefix, rs):
            ids = t([E.text(r, prefix) for r in rs], truncation=False, padding=False)["input_ids"]
            return provenance.length_stats([len(x) for x in ids], 128)
        report = {}
        for label, t, prefix in [("mmBERT", tok, pref)] + ([("E5", AutoTokenizer.from_pretrained(a.e5), "query: ")] if a.e5 else []):
            report[label] = {"train": lens(t, prefix, E.rows)}
            for tn, te in E.tests.items():
                report[label][tn] = lens(t, prefix, te)
        for label, d in report.items():
            for name, st in d.items():
                record("★2", f"長さ {label} / {name}", True, f"n={st['n']} 平均={st['mean']:.1f} p50={st['p50']} p95={st['p95']} p99={st['p99']} 最大={st['max']} 128超で切捨={st['truncated']}件({st['truncated_rate']:.2%})")
        return report
    tokenization()

    # ---- ★3 分類の頭 ----
    @guard("★3", "分類の頭（cls / mean）")
    def heads():
        torch.manual_seed(0)
        enc = tok(["列名: 金額 | 値: 100, 200 | 同じ表の列: 日付", "列名: 取引先 | 値: 山田商事 | 同じ表の列: 金額"], padding=True, return_tensors="pt")
        outs = {}
        for pooling in ("cls", "mean", None):
            m, ch = load_cls(a.model_dir, pooling)
            m = m.eval()
            with torch.no_grad():
                lg = m(**enc).logits
            outs[str(pooling)] = lg
            ok = tuple(lg.shape) == (2, 15) and bool(torch.isfinite(lg).all())
            record("★3", f"pooling={pooling or '（config のまま：' + str(getattr(m.config, 'classifier_pooling', None)) + '）'}", ok,
                   f"logits shape={tuple(lg.shape)} attn={m.config._attn_implementation} head={[n for n, _ in m.named_children()]} config変更={ch}")
        return outs
    heads()

    # ---- ★4 学習の 1 ステップ ----
    @guard("★4", "学習の1ステップ")
    def one_step():
        import encoder_exp as E
        torch.manual_seed(0)
        m, _ = load_cls(a.model_dir)
        m.train()
        labels = sorted(set(r[2] for r in E.rows))
        L = {c: i for i, c in enumerate(labels)}
        sample = E.rows[:: max(1, len(E.rows) // 16)][:16]
        enc = tok([E.text(r, "") for r in sample], truncation=True, max_length=128, padding=True, return_tensors="pt")
        y = torch.tensor([L[r[2]] % 15 for r in sample])
        opt = torch.optim.AdamW(m.parameters(), lr=1e-4, weight_decay=0.01)
        losses = []
        for _ in range(3):
            loss = torch.nn.functional.cross_entropy(m(**enc).logits.float(), y)
            loss.backward()
            gn = torch.nn.utils.clip_grad_norm_(m.parameters(), 1.0)
            opt.step(); opt.zero_grad()
            losses.append(float(loss))
        finite = all(np.isfinite(losses)) and bool(torch.isfinite(gn))
        record("★4", "3 ステップ", finite, f"損失 {[round(x, 4) for x in losses]} 勾配ノルム {float(gn):.3f}（同じ 16 文を使い回すので下がるのが普通。下がった={losses[-1] < losses[0]}）")
        return m
    one_step()

    # ---- ★5 保存と読み込み ----
    @guard("★5", "保存と読み込み")
    def save_load():
        torch.manual_seed(0)
        m, _ = load_cls(a.model_dir)
        m = m.eval()
        enc = tok(["列名: 金額 | 値: 100, 200 | 同じ表の列: 日付", "列名: 取引先 | 値: 山田商事 | 同じ表の列: 金額"], padding=True, return_tensors="pt")
        with torch.no_grad():
            before = m(**enc).logits
        with tempfile.TemporaryDirectory() as d:
            m.save_pretrained(d); tok.save_pretrained(d)
            json.dump([f"c{i}" for i in range(15)], open(os.path.join(d, "labels.json"), "w"))
            files = sorted(os.listdir(d))
            m2 = AutoModelForSequenceClassification.from_pretrained(d, attn_implementation="sdpa").eval()
            tok2 = AutoTokenizer.from_pretrained(d)
            enc2 = tok2(["列名: 金額 | 値: 100, 200 | 同じ表の列: 日付", "列名: 取引先 | 値: 山田商事 | 同じ表の列: 金額"], padding=True, return_tensors="pt")
            with torch.no_grad():
                after = m2(**{k: v for k, v in enc2.items() if k in ("input_ids", "attention_mask")}).logits
            wd = provenance.weights_digests(d)
        same_ids = bool((enc["input_ids"] == enc2["input_ids"]).all())
        diff = float((before - after).abs().max())
        wd_text = ", ".join("%s: %.0fMB" % (k, v["bytes"] / 1e6) for k, v in wd.items())
        record("★5", "保存→読み込みで logits 一致・トークナイザの ID 一致", diff < 1e-5 and same_ids,
               f"最大差 {diff:.2e}／ID一致 {same_ids}／保存したファイル {files}／重み {wd_text}")
    save_load()

    # ---- ☆6 速度の目安 ----
    @guard("☆6", "速度の目安（CPU）")
    def speed():
        import encoder_exp as E
        torch.set_num_threads(max(1, os.cpu_count() or 1))
        m, _ = load_cls(a.model_dir)
        m = m.eval()
        rs = E.tests["開発用220"][:32]
        enc = tok([E.text(r, "") for r in rs], truncation=True, max_length=128, padding=True, return_tensors="pt")
        with torch.no_grad():
            m(**enc)
            t = time.time()
            for _ in range(3):
                m(**enc)
            dt = (time.time() - t) / 3
        record("☆6", "推論 32 列（平均長に詰めた束）", True, f"{dt:.2f} 秒（{dt / 32 * 1000:.0f} ms/列・{os.cpu_count()} スレッド・fp32・この CPU のみの参考値）shape={tuple(enc['input_ids'].shape)}")
    speed()

    # ---- ☆7 ONNX ----
    if a.onnx:
        @guard("☆7", "ONNX への書き出し")
        def onnx_export():
            import onnxruntime as ort
            m, _ = load_cls(a.model_dir)
            m = m.eval()
            enc = tok(["列名: 金額 | 値: 100, 200 | 同じ表の列: 日付", "列名: 取引先 | 値: 山田商事 | 同じ表の列: 金額"], padding=True, return_tensors="pt")
            with tempfile.TemporaryDirectory() as d:
                p = os.path.join(d, "m.onnx")

                class Wrap(torch.nn.Module):
                    def __init__(self, inner):
                        super().__init__()
                        self.inner = inner

                    def forward(self, ids, mask):
                        return self.inner(input_ids=ids, attention_mask=mask).logits
                last = None
                kw = dict(input_names=["input_ids", "attention_mask"], output_names=["logits"],
                          dynamic_axes={"input_ids": {0: "b", 1: "s"}, "attention_mask": {0: "b", 1: "s"}, "logits": {0: "b"}})
                for opset in (18, 17):
                    for dyn in (False, True):   # export_onnx.py と同じ順：古い方式、だめなら既定の方式（onnxscript が要る）
                        try:
                            if dyn:
                                torch.onnx.export(Wrap(m), (enc["input_ids"], enc["attention_mask"]), p, opset_version=opset, **kw)
                            else:
                                torch.onnx.export(Wrap(m), (enc["input_ids"], enc["attention_mask"]), p, opset_version=opset, dynamo=False, **kw)
                            last = f"{opset}・{'dynamo' if dyn else 'legacy'}"
                            break
                        except Exception as e:  # noqa: BLE001
                            record("☆7", f"ONNX opset {opset} {'dynamo' if dyn else 'legacy'}", False, f"{type(e).__name__}: {str(e)[:300]}")
                    if last:
                        break
                if last is None:
                    return
                sess = ort.InferenceSession(p, providers=["CPUExecutionProvider"])
                with torch.no_grad():
                    ref = m(**enc).logits.numpy()
                out = sess.run(None, {"input_ids": enc["input_ids"].numpy(), "attention_mask": enc["attention_mask"].numpy()})[0]
                # 別の長さでも動くか（動的な軸）
                enc2 = tok(["列名: 日付 | 値: 2026-01-01 | 同じ表の列: 金額, 取引先, 摘要, 備考, 区分, 数量"], padding=True, return_tensors="pt")
                out2 = sess.run(None, {"input_ids": enc2["input_ids"].numpy(), "attention_mask": enc2["attention_mask"].numpy()})[0]
                with torch.no_grad():
                    ref2 = m(**enc2).logits.numpy()
                record("☆7", f"ONNX opset {last}", float(np.abs(ref - out).max()) < 1e-3 and float(np.abs(ref2 - out2).max()) < 1e-3,
                       f"onnxruntime と PyTorch の最大差 {float(np.abs(ref - out).max()):.2e}／別の長さ {float(np.abs(ref2 - out2).max()):.2e}／{os.path.getsize(p) / 1e6:.0f}MB（fp32・語彙を削る前）")
        onnx_export()

    return finish(a, info)


def finish(a, info):
    required_failed = [r for r in results if r[0].startswith("★") and r[2] == "NG"]
    lines = ["# mmBERT-small の試運転（CPU・GitHub Actions）", "", f"環境：{json.dumps(info)}", "", "| 区分 | 項目 | 結果 | 説明 |", "|---|---|---|---|"]
    for kind, name, state, detail in results:
        lines.append(f"| {kind} | {name} | {state} | {detail.replace('|', '／').replace(chr(10), ' ')[:900]} |")
    lines += ["", f"必須（★）で NG：{len(required_failed)} 件", "",
              "※ CPU の試運転であり、GPU（fp16）での学習・精度・端末での速さは確かめていない。"]
    text = "\n".join(lines) + "\n"
    open(a.out, "w", encoding="utf-8").write(text)
    print("\n=== 要点（この下が注に出る）===\n" + "\n".join(f"{r[2]} {r[0]} {r[1]}" for r in results), flush=True)
    return 1 if required_failed else 0


if __name__ == "__main__":
    sys.exit(main())
