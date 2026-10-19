"""学習済みの多言語モデル（multilingual-e5-small、MIT）を、列の種類の判定に合わせて微調整する（PyTorch・CPU、GitHub Actions）。
入力の文は encoder_exp.py と同じ。試験は Claude 側の試験（表ごとに分けた試験側・開発用）。集計だけを FINETUNE_RESULTS.md に出す。
学習したモデルは ft_out に保存する（ONNX への書き出しは未実装）。FT_COMPRESS=1 なら、学習のあと縮めた版（語彙削減・INT8・fp16）の質も測って同じ表に足す（compress_eval.py）。"""
import json, os, random, re, sys, time, unicodedata
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
dropout_args = {"hidden_dropout_prob": 0.0, "attention_probs_dropout_prob": 0.0} if os.environ.get("FT_NO_DROPOUT") == "1" else {}
init_model_path = os.environ.get("FT_INIT_MODEL_PATH")
if init_model_path:
    init_labels_path = os.path.join(init_model_path, "labels.json")
    if not os.path.isfile(init_labels_path) or json.load(open(init_labels_path, encoding="utf-8")) != labels:
        raise ValueError("FT_INIT_MODEL_PATH label map does not exactly match current training labels")
    model = AutoModelForSequenceClassification.from_pretrained(init_model_path, **dropout_args)
    if model.config.num_labels != len(labels):
        raise ValueError("FT_INIT_MODEL_PATH classifier dimension does not match current labels")
    print(f"initialized from audited source checkpoint: {init_model_path}", flush=True)
else:
    model = AutoModelForSequenceClassification.from_pretrained(NAME, num_labels=len(labels), **dropout_args)
DEV = "cuda" if torch.cuda.is_available() else "cpu"; model.to(DEV)  # Kaggle では GPU
print(f"device {DEV}; CPU threads={CPU_THREADS}/{CPU_AVAILABLE}", flush=True)
AUG = os.environ.get("FT_AUG") == "1"  # 入れ方の水増し（教育方針の改訂の3）：毎回、値の選び方・並べ方・文脈の列・書き方を変える。試験は固定の text() のまま
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
data = [(r, L[r[2]]) for r in train_rows] if AUG else [(text(r, PREFIX), L[r[2]]) for r in train_rows]
print(f"training rows={len(train_rows)} seed={seed_text or 'default'}", flush=True)
random.shuffle(data)
CPU_TOKEN_CACHE = DEV == "cpu" and not AUG and os.environ.get("FT_CPU_CACHE", "1") == "1"
if CPU_TOKEN_CACHE:
    token_texts = [x for x, _ in data]
    token_rows = tok(token_texts, truncation=True, max_length=128, padding=False)
    data = [({k: token_rows[k][i] for k in token_rows.keys()}, y) for i, (_, y) in enumerate(data)]
    print(f"CPU token cache: {len(data)} rows tokenized once", flush=True)

def collate(b):
    if CPU_TOKEN_CACHE:
        enc = tok.pad([x for x, _ in b], padding=True, return_tensors="pt")
    else:
        enc = tok([text_aug(x, PREFIX) if AUG else x for x, _ in b], truncation=True, max_length=128, padding=True, return_tensors="pt")
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
        ids = tok(texts, truncation=True, max_length=128, padding=False)["input_ids"]
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
scaler = torch.amp.GradScaler(enabled=DEV == "cuda")
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
def finish_step(eff_loss):
    global step
    scaler.unscale_(opt); torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    scaler.step(opt); scaler.update(); sch.step(); opt.zero_grad(); step += 1
    if step <= trace_n: print(f"step_loss {step} {eff_loss.item():.6f}", flush=True)
    if step % 100 == 0: print(f"step {step}/{steps} loss {eff_loss.item():.3f} {time.time() - t0:.0f}s", flush=True)
while step < steps:
    if SORT:
        for micros, n in dl:
            eff_loss = torch.zeros((), device=DEV)
            for m in micros:
                m = {k: v.to(DEV) for k, v in m.items()}
                with torch.autocast(DEV, dtype=torch.float16, enabled=DEV == "cuda"):
                    loss = training_loss(model(**m).logits, m["labels"]) * (m["labels"].shape[0] / n)  # 束の文数/実効バッチの文数で重みを付ける＝64文を一度に流したのと同じ勾配
                scaler.scale(loss).backward(); eff_loss += loss.detach()
            finish_step(eff_loss)
            if step >= steps: break
    else:
        eff_loss = torch.zeros((), device=DEV)
        for b in dl:
            b = {k: v.to(DEV) for k, v in b.items()}
            with torch.autocast(DEV, dtype=torch.float16, enabled=DEV == "cuda"):
                loss = training_loss(model(**b).logits, b["labels"]) / ACC
            scaler.scale(loss).backward(); micro += 1; eff_loss += loss.detach()
            if micro % ACC: continue
            finish_step(eff_loss); eff_loss = torch.zeros((), device=DEV)
            if step >= steps: break
if DEV == "cuda": print(f"peak GPU memory {torch.cuda.max_memory_allocated() / 2**30:.1f} GiB; training loop {time.time() - t0:.0f}s", flush=True)
train_seconds = time.time() - train_setup_start
model.eval()
EVAL_BS = 4 if DEV == "cuda" and IS_LARGE else 32
def probs(rs):
    out = []
    with torch.no_grad():
        for i in range(0, len(rs), EVAL_BS):
            enc = tok([text(r, PREFIX) for r in rs[i:i + EVAL_BS]], truncation=True, max_length=128, padding=True, return_tensors="pt")
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
model_probs = {tn: probs(te) for tn, te in tests.items()}
lr_probs = {tn: lr.predict_proba(mat(te)) for tn, te in tests.items()}
conditions = (("微調整だけ", 1.0), ("今の仕組みだけ", 0.0), ("微調整＋今の仕組み（半々）", 0.5), ("微調整6割＋今の仕組み4割", 0.6), ("微調整7割＋今の仕組み3割", 0.7))
condition_names = {"微調整だけ": "ft", "今の仕組みだけ": "sparse", "微調整＋今の仕組み（半々）": "blend50", "微調整6割＋今の仕組み4割": "blend60", "微調整7割＋今の仕組み3割": "blend70"}
critical_labels = {"date", "amount", "quantity", "rate", "id"}

def normalized_header(value):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(value)).strip()).casefold()

def safe_test_name(name):
    names = {"開発用220": "dev220", "本物（一般）": "general", "本物（業務）": "business", "本物（業務2）": "business2", "本物（日本の調達）": "japan_procurement"}
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

