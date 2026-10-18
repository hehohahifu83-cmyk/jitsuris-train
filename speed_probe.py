"""学習の速さを設定ごとに測る（Kaggle の GPU で 1 回流す。学習済みモデルは作らない）。

使い方（Kaggle の依頼）：  train probe <モデル>      例：train probe intfloat/multilingual-e5-large
親（この引数なしの実行）は GPU を一切使わず、設定ごとに子の実行を 1 つずつ起動する（設定同士でメモリの状態が残らない）。
  1. 実際の学習データから 640 文を取り、本物のトークン数の分布を出す（詰め物の無駄の見積もりに使う）
  2. 設定ごとの 1 秒あたりの文数・GPU メモリの最大値（実効バッチ 64 文で 4 回流して最初の 1 回は捨てる）
  3. 勾配の一致の検査：小さい束・長さ順・チェックポイント・幅を8の倍数にする設定が、基準と同じ勾配になるか（ドロップアウトを切って比べる）
  4. 一番速い設定を GPU 2 枚で同時に流したときの、1 枚あたりの速さ（GPU 2 枚の同時利用が本当に 2 倍近くになるか）
結果は FINETUNE_RESULTS.md の表（kaggle.sh が回収）と probe_results.json に出す。未見セットは使わない。
"""
import gc, json, os, random, statistics, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
EFF = 64  # 実効バッチ（今の学習と同じ）


def cfg(bs, ckpt=False, sort=False, pad8=False, fused=False, freeze=False):
    return {"bs": bs, "ckpt": ckpt, "sort": sort, "pad8": pad8, "fused": fused, "freeze": freeze}


# 名前 → 設定。large は今の既定（bs2・チェックポイントあり）が基準。base は今の既定（bs64）が基準。
LARGE = {
    "L00_bs2_ckpt_今": cfg(2, ckpt=True),
    "L01_bs8_ckpt": cfg(8, ckpt=True),
    "L02_bs16_ckpt": cfg(16, ckpt=True),
    "L03_bs32_ckpt": cfg(32, ckpt=True),
    "L04_bs8_noc": cfg(8),
    "L05_bs16_noc": cfg(16),
    "L06_bs8_ckpt_sort": cfg(8, ckpt=True, sort=True),
    "L07_bs16_ckpt_sort": cfg(16, ckpt=True, sort=True),
    "L08_bs32_ckpt_sort": cfg(32, ckpt=True, sort=True),
    "L09_bs8_noc_sort": cfg(8, sort=True),
    "L10_bs16_noc_sort": cfg(16, sort=True),
    "L11_bs16_ckpt_sort_pad8_fused": cfg(16, ckpt=True, sort=True, pad8=True, fused=True),
    "L12_bs8_noc_sort_pad8_fused": cfg(8, sort=True, pad8=True, fused=True),
    "L13_bs16_noc_sort_pad8_fused_凍結": cfg(16, sort=True, pad8=True, fused=True, freeze=True),
}
BASE = {
    "B00_bs64_今": cfg(64),
    "B01_bs16_sort": cfg(16, sort=True),
    "B02_bs32_sort": cfg(32, sort=True),
    "B03_bs64_sort": cfg(64, sort=True),
    "B04_bs16_sort_pad8_fused": cfg(16, sort=True, pad8=True, fused=True),
    "B05_bs64_pad8_fused": cfg(64, pad8=True, fused=True),
    "B06_bs32_sort_pad8_fused_凍結": cfg(32, sort=True, pad8=True, fused=True, freeze=True),
}
ALL = {**LARGE, **BASE}
EQUIV_REF = cfg(4)
EQUIV_TESTS = {"bs2_ckpt": cfg(2, ckpt=True), "bs16_ckpt_sort_pad8": cfg(16, ckpt=True, sort=True, pad8=True),
               "bs8_noc_sort": cfg(8, sort=True), "bs32_ckpt_sort": cfg(32, ckpt=True, sort=True)}


# ------------------------------------------------------------------ 子：1 つの設定を測る
def load_data():
    d = json.load(open(os.path.join(HERE, "_probe_data.tmp"), encoding="utf-8"))
    return d["texts"], d["ys"], d["num_labels"]


def build_micros(tok, texts, ys, c, torch):
    """実効バッチの文 → 小さな束のリスト（各要素は GPU に載せる辞書）と、実トークン数。"""
    from batching import plan_micro_batches, pad_batch
    micros, real = [], 0
    if c["sort"]:
        ids = tok(texts, truncation=True, max_length=128, padding=False)["input_ids"]
        for idx in plan_micro_batches([len(s) for s in ids], c["bs"]):
            pids, pmask = pad_batch([ids[i] for i in idx], tok.pad_token_id, 8 if c["pad8"] else 1)
            micros.append({"input_ids": torch.tensor(pids), "attention_mask": torch.tensor(pmask), "labels": torch.tensor([ys[i] for i in idx])})
            real += sum(len(ids[i]) for i in idx)
    else:
        for s in range(0, len(texts), c["bs"]):
            enc = tok(texts[s:s + c["bs"]], truncation=True, max_length=128, padding=True, pad_to_multiple_of=8 if c["pad8"] else None, return_tensors="pt")
            m = dict(enc); m["labels"] = torch.tensor(ys[s:s + c["bs"]]); micros.append(m)
            real += int(enc["attention_mask"].sum())
    return micros, real


def child_run(name, name_model):
    import torch
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    c = ALL[name]; texts, ys, nl = load_data()
    tok = AutoTokenizer.from_pretrained(name_model)
    out = {"name": name, **c, "torch": torch.__version__, "gpu": torch.cuda.get_device_name(0), "visible": os.environ.get("CUDA_VISIBLE_DEVICES", "all")}
    try:
        model = AutoModelForSequenceClassification.from_pretrained(name_model, num_labels=nl).cuda()
        out["attn"] = str(getattr(model.config, "_attn_implementation", "?"))
        if c["ckpt"]: model.gradient_checkpointing_enable()
        if c["freeze"]: model.get_input_embeddings().weight.requires_grad_(False)
        opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=1e-5, weight_decay=0.01, **({"fused": True} if c["fused"] else {}))
        scaler = torch.amp.GradScaler(); model.train()
        rng = random.Random(0); order = list(range(len(texts))); rng.shuffle(order)
        batches = [order[i:i + EFF] for i in range(0, len(order) - EFF + 1, EFF)][:5]   # 1 回捨てて 4 回測る
        torch.cuda.reset_peak_memory_stats(); times, reals = [], []
        for bi in batches:
            torch.cuda.synchronize(); t = time.time()
            micros, real = build_micros(tok, [texts[i] for i in bi], [ys[i] for i in bi], c, torch)
            for m in micros:
                m = {k: v.cuda() for k, v in m.items()}
                with torch.autocast("cuda", dtype=torch.float16):
                    loss = model(**m).loss * (m["labels"].shape[0] / len(bi))
                scaler.scale(loss).backward()
            scaler.unscale_(opt); torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            scaler.step(opt); scaler.update(); opt.zero_grad()
            torch.cuda.synchronize(); times.append(time.time() - t); reals.append(real)
        t_med = statistics.median(times[1:]); r_med = statistics.median(reals[1:])
        out.update(status="ok", sps=round(EFF / t_med, 1), step_s=round(t_med, 2), tokens_per_s=round(r_med / t_med), peak_gib=round(torch.cuda.max_memory_allocated() / 2**30, 1))
    except torch.cuda.OutOfMemoryError:
        out.update(status="OOM", peak_gib=round(torch.cuda.max_memory_allocated() / 2**30, 1))
    except Exception as e:   # 1 つの設定の失敗で全体を止めない
        out.update(status="error: " + repr(e)[:200])
    print("PROBE_RESULT " + json.dumps(out, ensure_ascii=False), flush=True)


# ------------------------------------------------------------------ 子：勾配の一致の検査
def child_equiv(name_model):
    import torch
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    texts, ys, nl = load_data(); tok = AutoTokenizer.from_pretrained(name_model)
    model = AutoModelForSequenceClassification.from_pretrained(name_model, num_labels=nl, hidden_dropout_prob=0.0, attention_probs_dropout_prob=0.0).cuda()
    model.train(); n_layers = model.config.num_hidden_layers
    keep = ("classifier", ".layer.0.", f".layer.{n_layers - 1}.")
    names = [n for n, p in model.named_parameters() if any(k in n for k in keep)]
    params = dict(model.named_parameters())
    order = list(range(len(texts))); random.Random(1).shuffle(order); bi = order[:EFF]
    S = 1024.0   # 損失を大きくして fp16 の勾配の桁落ちを避ける（あとで割る）

    def grads(c):
        model.zero_grad(set_to_none=True)
        if c["ckpt"]: model.gradient_checkpointing_enable()
        else: model.gradient_checkpointing_disable()
        micros, _ = build_micros(tok, [texts[i] for i in bi], [ys[i] for i in bi], c, torch)
        total = 0.0
        for m in micros:
            m = {k: v.cuda() for k, v in m.items()}
            with torch.autocast("cuda", dtype=torch.float16):
                loss = model(**m).loss * (m["labels"].shape[0] / EFF)
            (loss * S).backward(); total += loss.item()
        vec = torch.cat([params[n].grad.detach().float().flatten() / S for n in names])
        return total, vec

    ref_loss, ref = grads(EQUIV_REF); res = []
    for tname, c in EQUIV_TESTS.items():
        try:
            loss, g = grads(c)
            cos = float(torch.nn.functional.cosine_similarity(g, ref, dim=0)); rel = float((g - ref).norm() / ref.norm())
            res.append({"name": tname, "loss_diff": round(abs(loss - ref_loss), 5), "cos": round(cos, 6), "rel_err": round(rel, 5), "status": "ok"})
        except Exception as e:
            res.append({"name": tname, "status": "error: " + repr(e)[:200]})
    print("EQUIV_RESULT " + json.dumps({"ref": "bs4 そのまま", "ref_loss": round(ref_loss, 5), "tests": res}, ensure_ascii=False), flush=True)


# ------------------------------------------------------------------ 親
def run_child(args, env_extra=None):
    env = dict(os.environ); env.update(env_extra or {})
    return subprocess.Popen([sys.executable, os.path.abspath(__file__), *args], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)


def collect(proc, prefix, label):
    found = None
    for line in proc.stdout:
        if line.startswith(prefix): found = json.loads(line[len(prefix):])
        elif line.strip(): print(f"[{label}] {line.rstrip()[:300]}", flush=True)
    proc.wait()
    return found


def parent(name_model):
    from transformers import AutoTokenizer
    from encoder_exp import rows, text
    tok = AutoTokenizer.from_pretrained(name_model)
    labels = sorted(set(r[2] for r in rows)); L = {c: i for i, c in enumerate(labels)}
    rng = random.Random(0); pick = rng.sample(range(len(rows)), 640)
    prefix = "query: " if "e5" in name_model else ""
    texts = [text(rows[i], prefix) for i in pick]; ys = [L[rows[i][2]] for i in pick]
    json.dump({"texts": texts, "ys": ys, "num_labels": len(labels)}, open(os.path.join(HERE, "_probe_data.tmp"), "w", encoding="utf-8"), ensure_ascii=False)
    lens = sorted(len(x) for x in tok(texts, truncation=True, max_length=128)["input_ids"])
    n = len(lens); stats = {"mean": round(sum(lens) / n, 1), "median": lens[n // 2], "p90": lens[int(n * .9)], "p99": lens[int(n * .99)], "at_128": round(sum(1 for x in lens if x >= 128) / n, 3)}
    print("トークン数の分布（640文）:", stats, flush=True)
    gpus = subprocess.run("nvidia-smi --query-gpu=name,memory.total --format=csv,noheader", shell=True, capture_output=True, text=True).stdout.strip().replace("\n", " / ")
    is_large = "large" in name_model.lower()
    names = list(LARGE if is_large else BASE)
    only = os.environ.get("FT_PROBE_CONFIGS")
    if only: names = [x for x in names if any(x.startswith(o) for o in only.split(","))]
    results = []
    for nm in names:
        t = time.time(); r = collect(run_child(["--run", nm, name_model]), "PROBE_RESULT ", nm) or {"name": nm, "status": "no result"}
        r["wall_s"] = round(time.time() - t); results.append(r)
        print("→", json.dumps(r, ensure_ascii=False), flush=True)
    equiv = collect(run_child(["--equiv", name_model]), "EQUIV_RESULT ", "equiv")
    print("→ EQUIV", json.dumps(equiv, ensure_ascii=False), flush=True)
    # GPU 2 枚の同時利用：一番速い設定を、GPU 0 と GPU 1 で同時に流す
    ok = [r for r in results if r.get("status") == "ok"]; dual = None
    if ok and "/" in gpus and os.environ.get("FT_PROBE_NO_DUAL") != "1":
        best = max(ok, key=lambda r: r["sps"])
        procs = [run_child(["--run", best["name"], name_model], {"CUDA_VISIBLE_DEVICES": str(g)}) for g in (0, 1)]
        outs = [collect(p, "PROBE_RESULT ", f"dual-gpu{g}") for g, p in enumerate(procs)]
        dual = {"config": best["name"], "solo_sps": best["sps"], "both_sps": [o.get("sps") if o else None for o in outs], "status": [o.get("status") if o else "no result" for o in outs]}
        print("→ DUAL", json.dumps(dual, ensure_ascii=False), flush=True)
    # 表を出す
    base = next((r for r in results if r.get("status") == "ok"), None)
    lines = [f"| 設定 | 1秒あたりの文数 | 実トークン/秒 | GPUメモリ最大(GiB) | 基準比 | 状態 |", "|---|---:|---:|---:|---:|---|"]
    for r in results:
        ratio = f"{r['sps'] / base['sps']:.2f}倍" if r.get("status") == "ok" and base else "—"
        lines.append(f"| {r['name']} | {r.get('sps', '—')} | {r.get('tokens_per_s', '—')} | {r.get('peak_gib', '—')} | {ratio} | {r.get('status')} |")
    extra = [f"モデル {name_model}／GPU {gpus}／実効バッチ {EFF}／トークン数の分布 {stats}／attention={next((r.get('attn') for r in results if r.get('attn')), '?')}／torch {next((r.get('torch') for r in results if r.get('torch')), '?')}"]
    if equiv: extra.append("勾配の一致（基準 bs4 そのまま）: " + "；".join(f"{t['name']} 一致度{t.get('cos')}・相対差{t.get('rel_err')}・損失差{t.get('loss_diff')}" if t.get("status") == "ok" else f"{t['name']} {t['status']}" for t in equiv["tests"]))
    if dual: extra.append(f"GPU2枚を同時に使ったとき（{dual['config']}）: 1枚だけ {dual['solo_sps']} → 2枚それぞれ {dual['both_sps']}（状態 {dual['status']}）")
    body = "\n".join(lines) + "\n\n" + "\n\n".join(extra) + "\n"
    prev = open("FINETUNE_RESULTS.md", encoding="utf-8").read() if os.path.exists("FINETUNE_RESULTS.md") else "# 学習済みモデルの微調整（集計）\n"
    open("FINETUNE_RESULTS.md", "w", encoding="utf-8").write(prev + f"\n### {time.strftime('%Y-%m-%d %H:%M')}（速さの測定）\n" + body)
    json.dump({"results": results, "equiv": equiv, "dual": dual, "token_stats": stats}, open("probe_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(body, flush=True)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--run": child_run(a[1], a[2])
    elif a and a[0] == "--equiv": child_equiv(a[1])
    else: parent(a[0] if a else "intfloat/multilingual-e5-small")
