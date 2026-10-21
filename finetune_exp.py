"""学習済みの多言語モデル（multilingual-e5-small、MIT）を、列の種類の判定に合わせて微調整する（PyTorch・CPU、GitHub Actions）。
入力の文は encoder_exp.py と同じ。試験は Claude 側の試験（表ごとに分けた試験側・開発用）。集計だけを FINETUNE_RESULTS.md に出す。
学習したモデルは ft_out に保存する（ONNX への書き出しは未実装）。FT_COMPRESS=1 なら、学習のあと縮めた版（語彙削減・INT8・fp16）の質も測って同じ表に足す（compress_eval.py）。"""
import json, math, os, random, re, sys, time, unicodedata
from cpu_speed import configure_cpu_threads

CPU_AVAILABLE, CPU_THREADS = configure_cpu_threads()

import numpy as np
import torch
torch.set_num_threads(CPU_THREADS)
try:
    torch.set_num_interop_threads(1)
except RuntimeError as exc:
    print(f"could not set torch inter-op threads; continuing: {exc}", flush=True)
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification, get_linear_schedule_with_warmup
import gen, features
import provenance   # 学習の記録（manifest.json）。どの重み・データ・設定で作ったかを後から確かめるため
from batching import plan_micro_batches, pad_batch
features.USE_NUM2 = True  # 今の仕組み側は v8 と同じ（数字の値特徴あり）
# Experiment A: add explicit interactions between header semantics and value-shape evidence.
FT_CROSS = os.environ.get("FT_CROSS") == "1"
if FT_CROSS:
    features.set_dims(cross=True)
    print("feature interaction experiment: header × value-profile crosses enabled", flush=True)
from encoder_exp import rows, tests, text
from llm_baseline import score_real
from evaluation_records import assert_metrics_match, build_record, is_issue
from train3 import decide, decide_with_details

seed_text = os.environ.get("FT_SEED")
if seed_text is None:
    torch.manual_seed(0); random.seed(0)
else:
    seed = int(seed_text)
    torch.manual_seed(seed); random.seed(seed); np.random.seed(seed)
    if torch.cuda.is_available(): torch.cuda.manual_seed_all(seed)
NAME = sys.argv[1] if len(sys.argv) > 1 else "intfloat/multilingual-e5-small"
EPOCHS = float(sys.argv[2]) if len(sys.argv) > 2 else 2
PREFIX = "query: " if "e5" in NAME else ""
labels = sorted(set(r[2] for r in rows)); L = {c: i for i, c in enumerate(labels)}
base_train_rows = list(rows)  # Keep the sparse baseline free of machine pseudo-labels
replay_rows = []
replay_path = os.environ.get("FT_CPU_LAB_REPLAY")
pseudo_path = os.environ.get("FT_CPU_LAB_PSEUDO")
if replay_path and pseudo_path:
    raise ValueError("choose either human-verified replay or machine pseudo replay, not both")
if replay_path:
    from cpu_lab.self_learning import load_approved_replay
    replay_rows = load_approved_replay(replay_path, set(labels))
    rows = rows + replay_rows
    print(f"CPU lab replay: {len(replay_rows)} audited rows from {replay_path}", flush=True)
if pseudo_path:
    from cpu_lab.self_learning import load_pseudo_replay
    base_rows = len(base_train_rows)
    pseudo_rows = load_pseudo_replay(pseudo_path, set(labels), base_rows=base_rows)
    rows = rows + pseudo_rows
    print(f"CPU lab pseudo replay: {len(pseudo_rows)} unverified rows (capped at 1% of {base_rows}) from {pseudo_path}", flush=True)
tok = AutoTokenizer.from_pretrained(NAME)
# --- モデルの種類ごとの違い（2026-10-20：mmBERT-small＝ModernBERT 系を通すため。E5（XLM-R 系）の計算は変えない。違いは model_setup.py に集めた）---
from transformers import AutoConfig
import model_setup
MODEL_TYPE = getattr(AutoConfig.from_pretrained(os.environ.get("FT_INIT_MODEL_PATH") or NAME), "model_type", "")
NO_DROPOUT = os.environ.get("FT_NO_DROPOUT") == "1"
DROPOUT = model_setup.parse_dropout(os.environ.get("FT_DROPOUT"))   # 空なら各モデルの既定のまま（E5 は 0.1、ModernBERT 系は 0）。数を入れると dropout をその値にする（2026-10-21）
if NO_DROPOUT and DROPOUT is not None:
    raise ValueError("FT_NO_DROPOUT and FT_DROPOUT cannot be used together")
MAX_LEN = int(os.environ.get("FT_MAX_LEN", "128"))   # 入力の最大トークン数（既定 128。mmBERT は日本語が長く分かれ、実表で切れる割合が E5 の約 2 倍なので、192 などを試せるようにした。2026-10-21）
config_changes = {}
if MODEL_TYPE == "modernbert":
    tok.model_input_names = ["input_ids", "attention_mask"]   # ModernBERT は token_type_ids を受け取らない
    _mcfg = AutoConfig.from_pretrained(os.environ.get("FT_INIT_MODEL_PATH") or NAME)
    config_changes = model_setup.apply_modernbert_overrides(_mcfg, num_labels=len(labels), pooling=os.environ.get("FT_POOLING", ""), no_dropout=NO_DROPOUT, dropout=DROPOUT)
    # config を渡して読む（引数で渡すと transformers の版によって落ちる）。T4 では flash-attn は使えないので sdpa
    model_args = {"config": _mcfg, "attn_implementation": os.environ.get("FT_ATTN", "sdpa")}
    fresh_extra = {}
else:
    model_args = model_setup.no_dropout_args(MODEL_TYPE) if NO_DROPOUT else model_setup.dropout_args(MODEL_TYPE, DROPOUT)   # 何も指定しなければ、各モデルの既定のまま（E5 は dropout 0.1）
    fresh_extra = {"num_labels": len(labels)}
init_model_path = os.environ.get("FT_INIT_MODEL_PATH")
if init_model_path:
    init_labels_path = os.path.join(init_model_path, "labels.json")
    if not os.path.isfile(init_labels_path) or json.load(open(init_labels_path, encoding="utf-8")) != labels:
        raise ValueError("FT_INIT_MODEL_PATH label map does not exactly match current training labels")
    model = AutoModelForSequenceClassification.from_pretrained(init_model_path, **model_args)
    if model.config.num_labels != len(labels):
        raise ValueError("FT_INIT_MODEL_PATH classifier dimension does not match current labels")
    print(f"initialized from audited source checkpoint: {init_model_path}", flush=True)
else:
    model = AutoModelForSequenceClassification.from_pretrained(NAME, **fresh_extra, **model_args)
DEV = "cuda" if torch.cuda.is_available() else "cpu"; model.to(DEV)  # Kaggle では GPU
print(f"device {DEV}; CPU threads={CPU_THREADS}/{CPU_AVAILABLE}", flush=True)
print(f"model_type={MODEL_TYPE} params={sum(p.numel() for p in model.parameters()):,} attn={getattr(model.config, '_attn_implementation', None)} "
      f"pooling={getattr(model.config, 'classifier_pooling', None)} config_changes={config_changes}", flush=True)
AUG = os.environ.get("FT_AUG") == "1"  # 入れ方の水増し（教育方針の改訂の3）：毎回、値の選び方・並べ方・文脈の列・書き方を変える。試験は固定の text() のまま
if AUG and os.environ.get("FT_VALPROF") == "1":
    raise SystemExit("FT_AUG=1 と FT_VALPROF=1 は同時に使えない（text_aug は値の形を入れない）")
def text_aug(r, prefix):
    h, v = r[0], [str(x) for x in r[1]]; ctx = list(r[3]) if len(r) > 3 and r[3] else []
    pick = random.random()
    if pick < 1 / 3: vs = v[:5]
    elif pick < 2 / 3: vs = random.sample(v, min(5, len(v)))
    else:
        seen, vs = set(), []
        for x in v:
            if x not in seen: seen.add(x); vs.append(x)
        vs = vs[:5]
    random.shuffle(ctx); ctx = ctx[:random.randint(4, 12)]
    vals = ", ".join(x[:30] for x in vs); cs = ", ".join(str(x)[:20] for x in ctx)
    form = random.randrange(3)
    if form == 0: return f"{prefix}列名: {h} | 値: {vals} | 同じ表の列: {cs}"
    if form == 1: return f"{prefix}{h}: {vals} （同じ表: {cs}）"
    return f"{prefix}列「{h}」の値は {vals}。同じ表には {cs} がある。"
train_setup_start = time.time()
train_rows = rows
per_label_limit = os.environ.get("FT_LIMIT_PER_LABEL")
limit_text = os.environ.get("FT_LIMIT")
if per_label_limit and limit_text:
    raise ValueError("choose either FT_LIMIT or FT_LIMIT_PER_LABEL")
if per_label_limit:
    cap = int(per_label_limit)
    if cap < 1: raise ValueError("FT_LIMIT_PER_LABEL must be a positive integer")
    sample_rng = random.Random(int(os.environ.get("FT_SAMPLE_SEED", "0")))
    buckets = {}
    for row in base_train_rows:
        buckets.setdefault(row[2], []).append(row)
    sampled = []
    for label in sorted(buckets):
        bucket = list(buckets[label])
        sample_rng.shuffle(bucket)
        sampled.extend(bucket[:cap])
    # Always retain every independently audited CPU-lab row.
    train_rows = sampled + replay_rows
    print(f"stratified base sample: cap={cap}/label; fixed sample seed={os.environ.get('FT_SAMPLE_SEED', '0')}; replay={len(replay_rows)}", flush=True)
elif limit_text:
    limit = int(limit_text)
    if limit < 1: raise ValueError("FT_LIMIT must be a positive integer")
    train_rows = rows[:limit]

# Optional synthetic, train-excluded probe for the CPU lab. The same newly
# initialized classifier is scored immediately before and after fitting, so
# this measures within-run learning without touching the fixed test sets.
PROGRESS_PROBE = os.environ.get("FT_PROGRESS_PROBE", "").strip()
progress_rows = []
if PROGRESS_PROBE:
    from cpu_lab.self_learning import _read_jsonl
    progress_rows = _read_jsonl(__import__("pathlib").Path(PROGRESS_PROBE))
    if not progress_rows or any(r.get("split") != "progress_probe" or "target" not in r for r in progress_rows):
        raise ValueError("FT_PROGRESS_PROBE must point to labeled progress_probe rows")
    missing_probe_labels = sorted({r["target"] for r in progress_rows} - set(labels))
    if missing_probe_labels:
        raise ValueError(f"probe labels missing from training taxonomy: {missing_probe_labels}")
    train_signatures = {(str(r[0]), tuple(map(str, r[1])), str(r[2])) for r in train_rows}
    probe_signatures = {(str(r["header"]), tuple(map(str, r["values"])), str(r["target"])) for r in progress_rows}
    if train_signatures & probe_signatures:
        raise ValueError("progress probe overlaps the selected training rows")
    print(f"separate progress probe: {len(progress_rows)} synthetic rows; excluded from training", flush=True)

def score_progress_probe(stage):
    if not progress_rows:
        return
    model.eval()
    predictions = []
    with torch.inference_mode():
        for start in range(0, len(progress_rows), 32):
            batch = progress_rows[start:start + 32]
            enc = tok([text((r["header"], r["values"], r["target"], r.get("context", []), r.get("unit_context", "")), PREFIX)
                      for r in batch], truncation=True, max_length=MAX_LEN, padding=True, return_tensors="pt")
            enc = {k: v.to(DEV) for k, v in enc.items()}
            probs = torch.softmax(model(**enc).logits.float(), dim=-1).cpu().tolist()
            for row, p in zip(batch, probs):
                pred = labels[max(range(len(p)), key=lambda i: p[i])]
                predictions.append({"id": row["id"], "target": row["target"], "prediction": pred,
                                    "correct": pred == row["target"]})
    correct = sum(int(x["correct"]) for x in predictions)
    result = {"stage": stage, "seed": seed_text or "default", "model_name": NAME,
              "probe_count": len(progress_rows), "correct": correct,
              "errors": len(progress_rows) - correct, "accuracy": correct / len(progress_rows),
              "predictions": predictions, "split": "progress_probe",
              "training_overlap": 0, "fixed_test_sets_used": False}
    os.makedirs("progress_probe_results", exist_ok=True)
    with open(f"progress_probe_results/{stage}.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"progress probe {stage}: {correct}/{len(progress_rows)} ({result['accuracy']:.1%})", flush=True)

if progress_rows:
    score_progress_probe("before")
HMASK = float(os.environ.get("FT_HMASK", "0") or 0)   # W4：学習の行の見出しを決まった割合で「（なし）」に替える（既定 0＝替えない。評価の文は変えない）
if HMASK:
    if AUG:
        raise SystemExit("FT_HMASK と FT_AUG は同時に使えない")
    from encoder_context import mask_headers, HEADER_MASK_TOKEN
    _text_rows = mask_headers(train_rows, HMASK)
    print(f"FT_HMASK={HMASK:g}: masked {sum(r[0] == HEADER_MASK_TOKEN for r in _text_rows)}/{len(_text_rows)} training headers", flush=True)
else:
    _text_rows = train_rows
data = [(r, L[r[2]]) for r in train_rows] if AUG else [(text(r, PREFIX), L[r[2]]) for r in _text_rows]
print(f"training rows={len(train_rows)} seed={seed_text or 'default'}", flush=True)
# --- 学習の記録（manifest.json）と、入力の長さ・切り捨ての割合（2026-10-20）---
# MAX_LEN は上（FT_MAX_LEN）で定義済み
token_stats = {}
if os.environ.get("FT_TOKEN_STATS", "1") == "1":
    def _len_stats(rs):
        ids = tok([text(r, PREFIX) for r in rs], truncation=False, padding=False)["input_ids"]
        return provenance.length_stats([len(x) for x in ids], MAX_LEN)
    token_stats["train"] = _len_stats(train_rows)
    for _tn, _te in tests.items():
        token_stats[_tn] = _len_stats(_te)
    _t = token_stats["train"]
    print(f"token lengths (max_length={MAX_LEN}): train mean={_t['mean']:.1f} p95={_t['p95']} p99={_t['p99']} max={_t['max']} truncated={_t['truncated_rate']:.2%}", flush=True)
try:
    _args_txt = open("kaggle/args.txt", encoding="utf-8").read().strip() if os.path.isfile("kaggle/args.txt") else None
except OSError:
    _args_txt = None
manifest = provenance.build_manifest(
    model_name=NAME, hf_repo_id=provenance.hf_repo_id_from_path(NAME), epochs=EPOCHS, seed=seed_text or "default", labels=labels,
    train_rows=train_rows, replay_rows=replay_rows, tests={tn: provenance.rows_digest(te) for tn, te in tests.items()},
    source_model_dir=(init_model_path or (NAME if os.path.isdir(NAME) else None)),
    extra={"model_type": MODEL_TYPE, "config_changes": config_changes, "no_dropout": NO_DROPOUT, "dropout_override": DROPOUT, "prefix": PREFIX, "max_length": MAX_LEN,
           "token_stats": token_stats, "request_args": _args_txt, "device": DEV,
           "gpu": (torch.cuda.get_device_name(0) if DEV == "cuda" else None), "eval_mode": "validation" if os.environ.get("FT_VAL") == "1" else "fixed_tests"})
manifest["status"] = "started"
provenance.write_manifest("manifest.json", manifest)
random.shuffle(data)
CPU_TOKEN_CACHE = DEV == "cpu" and not AUG and os.environ.get("FT_CPU_CACHE", "1") == "1"
if CPU_TOKEN_CACHE:
    token_texts = [x for x, _ in data]
    token_rows = tok(token_texts, truncation=True, max_length=MAX_LEN, padding=False)
    data = [({k: token_rows[k][i] for k in token_rows.keys()}, y) for i, (_, y) in enumerate(data)]
    print(f"CPU token cache: {len(data)} rows tokenized once", flush=True)

def collate(b):
    if CPU_TOKEN_CACHE:
        enc = tok.pad([x for x, _ in b], padding=True, return_tensors="pt")
    else:
        enc = tok([text_aug(x, PREFIX) if AUG else x for x, _ in b], truncation=True, max_length=MAX_LEN, padding=True, return_tensors="pt")
    enc["labels"] = torch.tensor([y for _, y in b]); return enc
IS_LARGE = "large" in NAME.lower()
DEFAULT_BS = 2 if DEV == "cuda" and IS_LARGE else (64 if DEV == "cuda" else 32)
DEFAULT_ACC = 32 if DEV == "cuda" and IS_LARGE else 1
BS = int(os.environ.get("FT_BS", str(DEFAULT_BS)))
ACC = int(os.environ.get("FT_ACC", str(DEFAULT_ACC)))  # 大型モデルは実効バッチ64を小さい束に分ける
USE_CKPT = os.environ.get("FT_CKPT", "1" if DEV == "cuda" and IS_LARGE else "0") == "1"
# --- 速くする設定（どれも学習の計算結果は変えない。既定は今までどおり＝オフ）---
SORT = os.environ.get("FT_SORT", "0") == "1"          # 実効バッチ（BS×ACC 文）の中を長さ順に並べて小さな束に分け、詰め物の無駄を減らす
PAD_MULT = 8 if os.environ.get("FT_PAD8", "0") == "1" else 1  # 幅を8の倍数にする（fp16 の計算が速い形）
FUSED = os.environ.get("FT_FUSED", "0") == "1" and DEV == "cuda"  # AdamW を GPU 上でまとめて計算する
# --- 計算結果が変わりうる設定（A/B で確かめるまで使わない）---
FREEZE_EMB = os.environ.get("FT_FREEZE_EMB", "0") == "1"  # 単語の埋め込み表（約2.6億個）を固定する
if USE_CKPT: model.gradient_checkpointing_enable()
if FREEZE_EMB:
    model.get_input_embeddings().weight.requires_grad_(False)
print(f"train batch={BS}, accumulation={ACC}, effective={BS * ACC}, checkpointing={USE_CKPT}, sort={SORT}, pad_multiple={PAD_MULT}, fused={FUSED}, freeze_embeddings={FREEZE_EMB}", flush=True)

def collate_eff(b):
    """実効バッチ全体を一度にトークン化 → 長さ順に小さな束へ分ける。損失の重みのため全体の文数も返す。"""
    if CPU_TOKEN_CACHE: ids = [x["input_ids"] for x, _ in b]
    else:
        texts = [text_aug(x, PREFIX) if AUG else x for x, _ in b]
        ids = tok(texts, truncation=True, max_length=MAX_LEN, padding=False)["input_ids"]
    ys = [y for _, y in b]; micros = []
    for idx in plan_micro_batches([len(s) for s in ids], BS):
        pids, pmask = pad_batch([ids[i] for i in idx], tok.pad_token_id, PAD_MULT)
        micros.append({"input_ids": torch.tensor(pids), "attention_mask": torch.tensor(pmask), "labels": torch.tensor([ys[i] for i in idx])})
    return micros, len(b)

if SORT:
    dl = DataLoader(data, batch_size=BS * ACC, shuffle=True, collate_fn=collate_eff)
    steps = int(len(dl) * EPOCHS)
else:
    dl = DataLoader(data, batch_size=BS, shuffle=True, collate_fn=collate)
    steps = int(len(dl) * EPOCHS / ACC)
opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=float(os.environ.get("FT_LR", "5e-5")), weight_decay=0.01, **({"fused": True} if FUSED else {}))
sch = get_linear_schedule_with_warmup(opt, int(steps * 0.06), steps)
# --- 混合精度（既定は今までどおり fp16）。FT_AMP=off で fp32。ModernBERT 系は、fp16 で損失が有限にならない状態が続いたら fp32 に切り替えて続ける（切り替えた step を記録に残す）---
AMP_MODE = os.environ.get("FT_AMP", "fp16")
if AMP_MODE not in ("fp16", "off"):
    raise ValueError(f"FT_AMP must be fp16 or off: {AMP_MODE}")
AMP_ON = [DEV == "cuda" and AMP_MODE == "fp16"]
AMP_FALLBACK = os.environ.get("FT_AMP_FALLBACK", "1" if MODEL_TYPE == "modernbert" else "0") == "1"
amp_fallback_step = [None]
scaler = torch.amp.GradScaler(enabled=AMP_ON[0])
print(f"mixed precision: mode={AMP_MODE} active={AMP_ON[0]} fallback_to_fp32={AMP_FALLBACK}", flush=True)
FOCAL_GAMMA_TEXT = os.environ.get("FT_FOCAL_GAMMA", "").strip()
FOCAL_GAMMA = float(FOCAL_GAMMA_TEXT) if FOCAL_GAMMA_TEXT else None
if FOCAL_GAMMA is not None and FOCAL_GAMMA <= 0:
    raise ValueError("FT_FOCAL_GAMMA must be positive")
def training_loss(logits, targets):
    # Experiment B: focal loss gives more gradient to difficult, currently misclassified samples.
    ce = torch.nn.functional.cross_entropy(logits.float(), targets, reduction="none")
    if FOCAL_GAMMA is None:
        return ce.mean()
    pt = torch.exp(-ce)
    return (((1.0 - pt) ** FOCAL_GAMMA) * ce).mean()
if FOCAL_GAMMA is not None:
    print(f"focal-loss experiment: gamma={FOCAL_GAMMA}", flush=True)
trace_n = int(os.environ.get("FT_TRACE_LOSS", "0"))
if DEV == "cuda": torch.cuda.reset_peak_memory_stats()
t0 = time.time(); model.train(); step = 0; micro = 0
_guard = model_setup.NonFiniteGuard(AMP_ON[0], AMP_FALLBACK)   # 100 step ごとの損失が有限でない状態が続いたときの扱い（fp16 → fp32 の切り替え、または停止）
def finish_step(eff_loss):
    global step, scaler
    scaler.unscale_(opt); torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    scaler.step(opt); scaler.update(); sch.step(); opt.zero_grad(); step += 1
    if step <= trace_n: print(f"step_loss {step} {eff_loss.item():.6f}", flush=True)
    if step % 100 == 0:
        _lv = eff_loss.item()
        print(f"step {step}/{steps} loss {_lv:.3f} {time.time() - t0:.0f}s", flush=True)
        # 損失が有限でない状態が続いたら止める（fp16 の桁あふれなどで、何も学ばないまま結果だけ出るのを防ぐ）
        if _guard.observe(_lv, step) == "fallback":
            # fp16 の桁あふれ。GradScaler が更新を飛ばしていたので重みは壊れていない。fp32 に切り替えて続ける
            AMP_ON[0] = False; scaler = torch.amp.GradScaler(enabled=False); amp_fallback_step[0] = step
            print(f"fp16 で損失が有限にならない状態が続いたので、step {step} から fp32 に切り替える", flush=True)
while step < steps:
    if SORT:
        for micros, n in dl:
            eff_loss = torch.zeros((), device=DEV)
            for m in micros:
                m = {k: v.to(DEV) for k, v in m.items()}
                with torch.autocast(DEV, dtype=torch.float16, enabled=AMP_ON[0]):
                    loss = training_loss(model(**m).logits, m["labels"]) * (m["labels"].shape[0] / n)  # 束の文数/実効バッチの文数で重みを付ける＝64文を一度に流したのと同じ勾配
                scaler.scale(loss).backward(); eff_loss += loss.detach()
            finish_step(eff_loss)
            if step >= steps: break
    else:
        eff_loss = torch.zeros((), device=DEV)
        for b in dl:
            b = {k: v.to(DEV) for k, v in b.items()}
            with torch.autocast(DEV, dtype=torch.float16, enabled=AMP_ON[0]):
                loss = training_loss(model(**b).logits, b["labels"]) / ACC
            scaler.scale(loss).backward(); micro += 1; eff_loss += loss.detach()
            if micro % ACC: continue
            finish_step(eff_loss); eff_loss = torch.zeros((), device=DEV)
            if step >= steps: break
peak_gpu_gib = torch.cuda.max_memory_allocated() / 2**30 if DEV == "cuda" else None
if DEV == "cuda": print(f"peak GPU memory {peak_gpu_gib:.1f} GiB; training loop {time.time() - t0:.0f}s", flush=True)
train_loop_seconds = time.time() - t0
train_seconds = time.time() - train_setup_start
model.eval()
if progress_rows:
    score_progress_probe("after")
EVAL_BS = 4 if DEV == "cuda" and IS_LARGE else 32
def probs(rs):
    out = []
    with torch.no_grad():
        for i in range(0, len(rs), EVAL_BS):
            enc = tok([text(r, PREFIX) for r in rs[i:i + EVAL_BS]], truncation=True, max_length=MAX_LEN, padding=True, return_tensors="pt")
            enc = {k: v.to(DEV) for k, v in enc.items()}
            out.append(torch.softmax(model(**enc).logits.float(), -1).cpu().numpy())
    return np.vstack(out)
from sklearn.linear_model import LogisticRegression
from train3 import mat
lr = LogisticRegression(C=8, max_iter=3000).fit(mat(base_train_rows), np.array([r[2] for r in base_train_rows]))
assert list(lr.classes_) == labels
if os.environ.get("FT_EVAL") == "dev220":
    tests = {k: v for k, v in tests.items() if k == "開発用220"}
if any("blind" in k.lower() for k in tests):
    raise RuntimeError("blind test sets must not be evaluated or saved")
eval_start = time.time()
model_probs, infer_seconds = {}, {}
for tn, te in tests.items():
    _ti = time.time(); model_probs[tn] = probs(te); infer_seconds[tn] = round(time.time() - _ti, 2)   # 推論の時間（この GPU / CPU での値。端末での速さではない）
    if not np.isfinite(model_probs[tn]).all():
        raise RuntimeError(f"確率が有限でない（NaN/inf）：{tn}")
lr_probs = {tn: lr.predict_proba(mat(te)) for tn, te in tests.items()}
conditions = (("微調整だけ", 1.0), ("今の仕組みだけ", 0.0), ("微調整＋今の仕組み（半々）", 0.5), ("微調整6割＋今の仕組み4割", 0.6), ("微調整7割＋今の仕組み3割", 0.7))
condition_names = {"微調整だけ": "ft", "今の仕組みだけ": "sparse", "微調整＋今の仕組み（半々）": "blend50", "微調整6割＋今の仕組み4割": "blend60", "微調整7割＋今の仕組み3割": "blend70"}
critical_labels = {"date", "amount", "quantity", "rate", "id"}

def normalized_header(value):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(value)).strip()).casefold()

def safe_test_name(name):
    names = {"開発用220": "dev220", "本物（一般）": "general", "本物（業務）": "business", "本物（業務2）": "business2", "本物（日本の調達）": "japan_procurement",
             "検証（一般）": "val_general", "検証（業務）": "val_business", "検証（業務2）": "val_business2", "検証（日本の調達）": "val_japan_procurement"}   # 検証＝学習から除いた表（FT_VAL=1）
    return names.get(name, "test")

lines = []
eval_seed = seed_text if seed_text is not None else "default"
for tag, w in conditions:
    res = []
    for tn, te in tests.items():
        P = w * model_probs[tn] + (1 - w) * lr_probs[tn]
        details = decide_with_details(labels, P, te)
        pred = [item["guarded_prediction"] for item in details]
        truth_labels = [r[2] for r in te]
        s = score_real(pred, truth_labels)
        res.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}" + (f" その他見送り{s['other_ok']}/{s['other_ok'] + s['other_ng']}" if s['other_ok'] + s['other_ng'] else ""))
        top = np.argsort(P, axis=1)[:, ::-1][:, :3]
        prob_rows = []
        for i, (row, truth, detail) in enumerate(zip(te, truth_labels, details)):
            chosen = detail["guarded_prediction"]
            top3 = [{"label": labels[int(j)], "probability": round(float(P[i, j]), 6)} for j in top[i]]
            prob_rows.append(build_record(
                index=i, dataset=safe_test_name(tn), seed=eval_seed,
                condition=condition_names[tag], column=normalized_header(row[0]),
                truth=truth, guarded_prediction=chosen, top3=top3,
                decision_reason=detail["decision_reason"],
            ))
        # Fail the run before writing artifacts if row-level records cannot reproduce the official score.
        assert_metrics_match(prob_rows, s)
        error_rows = [row for row in prob_rows if is_issue(row)]
        suffix = f"{safe_test_name(tn)}_{condition_names[tag]}"
        metadata = {"schema_version": 3, "test": tn, "dataset": safe_test_name(tn),
                    "seed": eval_seed, "condition": tag, "condition_id": condition_names[tag]}
        with open(f"probs_{suffix}.json", "w", encoding="utf-8") as f:
            json.dump({**metadata, "rows": prob_rows}, f, ensure_ascii=False, separators=(",", ":"))
        with open(f"errors_{suffix}.json", "w", encoding="utf-8") as f:
            json.dump({**metadata, "errors": error_rows}, f, ensure_ascii=False, separators=(",", ":"))
    lines.append(f"| {NAME} 微調整 {EPOCHS}周{'・水増し' if AUG else ''}・{tag} | " + " | ".join(res) + f" | 学習 {train_seconds:.0f}秒・評価 {time.time() - eval_start:.0f}秒 |"); print(lines[-1], flush=True)
notes = []
if os.environ.get("FT_COMPRESS") == "1":   # 縮めた版（語彙削減・INT8・fp16）の質。失敗しても本体の結果は残す
    try:
        import compress_eval
        extra, notes = compress_eval.run(model, tok, tests, rows, labels, lr_probs, text, PREFIX, decide, score_real, f"{NAME} 微調整 {EPOCHS}周",
                                         top_k=int(os.environ.get("FT_COMPRESS_TOPK", "0")), limit=int(os.environ["FT_COMPRESS_LIMIT"]) if os.environ.get("FT_COMPRESS_LIMIT") else None, model_probs=model_probs)
        lines += extra
    except Exception as exc:  # noqa: BLE001
        import traceback; traceback.print_exc()
        notes = [f"- 圧縮の試験は失敗した：{type(exc).__name__}: {str(exc)[:200]}"]
line = "\n".join(lines)
os.makedirs("ft_out", exist_ok=True); model.save_pretrained("ft_out"); tok.save_pretrained("ft_out"); json.dump(labels, open("ft_out/labels.json", "w"))
prev = (open("FINETUNE_RESULTS.md").read() if os.path.exists("FINETUNE_RESULTS.md") else "# 学習済みモデルの微調整（集計）\n") + f"\n### {time.strftime('%Y-%m-%d %H:%M')}（試験：{', '.join(tests)}）\n"
open("FINETUNE_RESULTS.md", "w").write(prev + line + "\n" + ("\n" + "\n".join(notes) + "\n" if notes else ""))
# --- 学習の記録を完成させる（重みの SHA-256・出力ファイルの SHA-256・時間・メモリ）。モデルと一緒に ft_out にも置く ---
manifest["status"] = "completed"
manifest["saved_model"] = {"files": provenance.small_files_digests("ft_out"), "weights": provenance.weights_digests("ft_out")}
manifest["outputs"] = provenance.output_digests(".", ("probs_*.json", "errors_*.json", "progress_probe_results/*.json", "FINETUNE_RESULTS.md"))
manifest["amp"] = {"mode": AMP_MODE, "fallback_enabled": AMP_FALLBACK, "fallback_step": amp_fallback_step[0], "active_at_end": AMP_ON[0]}
manifest["timing"] = {"train_loop_seconds": round(train_loop_seconds, 1), "train_total_seconds": round(train_seconds, 1), "eval_seconds": round(time.time() - eval_start, 1),
                      "inference_seconds": infer_seconds, "inference_rows": {tn: len(te) for tn, te in tests.items()}, "peak_gpu_gib": None if peak_gpu_gib is None else round(peak_gpu_gib, 2)}
manifest["model_config"] = {"model_type": MODEL_TYPE, "parameters": sum(p.numel() for p in model.parameters()), "hidden_size": getattr(model.config, "hidden_size", None),
                            "layers": getattr(model.config, "num_hidden_layers", None), "vocab_size": getattr(model.config, "vocab_size", None),
                            "classifier_pooling": getattr(model.config, "classifier_pooling", None), "attn_implementation": getattr(model.config, "_attn_implementation", None)}
provenance.write_manifest("manifest.json", manifest)
provenance.write_manifest("ft_out/manifest.json", manifest)
print("manifest.json written; weights sha256 " + str(provenance.weights_sha256(manifest)), flush=True)

