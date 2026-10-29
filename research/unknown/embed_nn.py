"""本体の中で「どの教材の列がいちばん似ているか」を調べる（2026-10-30 Claude。原因の確かめの最後の段）。
本体 C2 種子 1 が答えを出す直前の表現（分類の最後の層への入力）で、本体が誤った列（root_cause の M11、73 列）に近い学習の教材の列を 10 列ずつ探す。
本体がどの教材から「この列はこの種類」と覚えたかを直接見る。製品・評価には使わない。

学習の教材：encoder_exp.py と同じ出どころ（合成 build_train・real_labels・biz・biz2/direct・jp・教材庫 b001〜b014）。
教材の文は学習と同じ format_encoder_text（前置き・単位の欄・題名＝materials/pool/titles.json）。ただし学習で足していた「同じ表の単位列の例」は空にした（近さの比べには小さい差）。
誤った列の文は予測と同じ（各陣の set.json、題名なし）。
  python research/unknown/embed_nn.py --checkpoint /tmp/e5-model/ft_out_job1 --out research/unknown/embed_nn.json   （Actions の research-embed.yml）
"""
import argparse
import glob
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
K = 10


def training_rows():
    from exp7 import load_real
    from train3 import build_train, split_curriculum
    rows = [("syn", r) for r in build_train({"syn": 400, "muni": 2, "cur": 4}, split_curriculum()[0])]
    for name, files in (("g", ("materials/real_labels.jsonl",)), ("b", ("materials/real_labels_biz.jsonl",)),
                        ("b2", ("materials/real_labels_biz2.jsonl", "materials/real_labels_direct.jsonl")),
                        ("j", ("materials/real_labels_jp.jsonl", "materials/real_labels_jp2.jsonl"))):
        rows += [(name, r) for r in load_real(tuple(f for f in files if os.path.exists(os.path.join(ROOT, f))))]
    pool = sorted(f for f in glob.glob(os.path.join(ROOT, "materials/pool/batch_b*.jsonl")) if int(re.search(r"batch_b(\d+)", f).group(1)) <= 14)
    rows += [(os.path.basename(f)[6:10], r) for f in pool for r in load_real((f,))]
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=0, help="試し用：教材の行をこの数に絞る")
    a = ap.parse_args()
    import numpy as np
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    import evaluate_independent as EI
    from encoder_context import TITLE_SEP, format_encoder_text
    info = EI.checkpoint_info(a.checkpoint)
    titles = json.load(open(os.path.join(ROOT, "materials/pool/titles.json"), encoding="utf-8"))
    tr = training_rows()
    if a.limit:
        tr = tr[:a.limit]
    def unit_of(r):   # 合成の行は (列名, 値, 種類, 同じ表の列名) の 4 つで表の名前がない
        t = r[4] if len(r) > 4 else ""
        return TITLE_SEP + titles[t] if t in titles else ""
    tr_text = [format_encoder_text((r[0], r[1], r[2], r[3], unit_of(r)), info["prefix"], ctx_unit=info["ctx_unit"], title=True) for _, r in tr]
    rc = [json.loads(l) for l in open(os.path.join(HERE, "root_cause.jsonl"), encoding="utf-8")]
    ids = [r["id"] for r in rc if r["mechanism"].startswith("M11")]
    sets = {}
    for b in sorted({i[:4] for i in ids}):
        sd = json.load(open(os.path.join(ROOT, "materials/pool/work", b, "set.json"), encoding="utf-8"))
        for c, row in zip(sd["columns"], EI.rows_of(sd)):
            sets[c["id"]] = row
    q_text = EI.texts_of([sets[i] for i in ids], info)

    tok = AutoTokenizer.from_pretrained(a.checkpoint, local_files_only=True)
    model = AutoModelForSequenceClassification.from_pretrained(a.checkpoint, local_files_only=True).eval()
    feats = []
    model.classifier.out_proj.register_forward_pre_hook(lambda m, inp: feats.append(inp[0].detach().float().cpu().numpy()))
    labels = info["labels"]

    def embed(texts, bs=64):
        feats.clear()
        preds = []
        with torch.no_grad():
            for i in range(0, len(texts), bs):
                enc = tok(texts[i:i + bs], truncation=True, max_length=info["max_length"], padding=True, return_tensors="pt")
                preds += [labels[j] for j in model(**enc).logits.argmax(-1).tolist()]
        e = np.vstack(feats)
        return e / (np.linalg.norm(e, axis=1, keepdims=True) + 1e-9), preds

    t0 = time.time()
    Eq, pq = embed(q_text)
    Et, pt = embed(tr_text)
    sims = Eq @ Et.T
    out = {"note": "本体 C2 種子 1 の分類の最後の層への入力で近い教材の列（余弦）。teacher＝教材の種類、model＝本体がその教材の列に付ける答え",
           "checkpoint": {k: info[k] for k in ("weights_sha256", "prefix", "max_length", "ctx_unit")}, "train_rows": len(tr),
           "seconds": round(time.time() - t0, 1), "targets": []}
    for k, i in enumerate(ids):
        nn = np.argsort(-sims[k])[:K]
        out["targets"].append({"id": i, "model": pq[k], "neighbors": [
            {"src": tr[j][0], "header": str(tr[j][1][0])[:60], "values": [str(v)[:20] for v in tr[j][1][1][:4]], "teacher": tr[j][1][2],
             "model": pt[j], "sim": round(float(sims[k, j]), 3), "table": str(tr[j][1][4])[:80] if len(tr[j][1]) > 4 else ""} for j in nn]})
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    json.dump(out, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"targets {len(ids)} train {len(tr)} seconds {out['seconds']}")


if __name__ == "__main__":
    main()
