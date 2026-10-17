"""学習済みの多言語モデル（multilingual-e5-small、MIT）を、列の種類の判定に合わせて微調整する（PyTorch・CPU、GitHub Actions）。
入力の文は encoder_exp.py と同じ。試験は Claude 側の試験（表ごとに分けた試験側・開発用）。集計だけを FINETUNE_RESULTS.md に出す。
学習したモデルは ONNX に書き出し、artifacts として保存（ブラウザで Transformers.js から使う準備）。"""
import json, os, random, sys, time
import numpy as np
import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification, get_linear_schedule_with_warmup
import gen, features
features.USE_NUM2 = True  # 今の仕組み側は v8 と同じ（数字の値特徴あり）
from encoder_exp import rows, tests, text
from llm_baseline import score_real
from train3 import decide

torch.manual_seed(0); random.seed(0)
NAME = sys.argv[1] if len(sys.argv) > 1 else "intfloat/multilingual-e5-small"
EPOCHS = float(sys.argv[2]) if len(sys.argv) > 2 else 2
PREFIX = "query: " if "e5" in NAME else ""
labels = sorted(set(r[2] for r in rows)); L = {c: i for i, c in enumerate(labels)}
tok = AutoTokenizer.from_pretrained(NAME)
model = AutoModelForSequenceClassification.from_pretrained(NAME, num_labels=len(labels))
DEV = "cuda" if torch.cuda.is_available() else "cpu"; model.to(DEV)  # Kaggle では GPU
print("device", DEV, flush=True)
torch.set_num_threads(os.cpu_count() or 4)
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
data = [(r, L[r[2]]) for r in rows] if AUG else [(text(r, PREFIX), L[r[2]]) for r in rows]
random.shuffle(data)
def collate(b):
    enc = tok([text_aug(x, PREFIX) if AUG else x for x, _ in b], truncation=True, max_length=128, padding=True, return_tensors="pt")
    enc["labels"] = torch.tensor([y for _, y in b]); return enc
dl = DataLoader(data, batch_size=32 if DEV == "cpu" else 64, shuffle=True, collate_fn=collate)
opt = torch.optim.AdamW(model.parameters(), lr=float(os.environ.get("FT_LR", "5e-5")), weight_decay=0.01)
steps = int(len(dl) * EPOCHS); sch = get_linear_schedule_with_warmup(opt, int(steps * 0.06), steps)
scaler = torch.amp.GradScaler(enabled=DEV == "cuda")
t0 = time.time(); model.train(); step = 0
while step < steps:
    for b in dl:
        b = {k: v.to(DEV) for k, v in b.items()}
        with torch.autocast(DEV, dtype=torch.float16, enabled=DEV == "cuda"):
            loss = model(**b).loss
        scaler.scale(loss).backward(); scaler.unscale_(opt); torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        scaler.step(opt); scaler.update(); sch.step(); opt.zero_grad(); step += 1
        if step % 100 == 0: print(f"step {step}/{steps} loss {loss.item():.3f} {time.time() - t0:.0f}s", flush=True)
        if step >= steps: break
model.eval()
def probs(rs):
    out = []
    with torch.no_grad():
        for i in range(0, len(rs), 64):
            enc = tok([text(r, PREFIX) for r in rs[i:i + 64]], truncation=True, max_length=128, padding=True, return_tensors="pt")
            enc = {k: v.to(DEV) for k, v in enc.items()}
            out.append(torch.softmax(model(**enc).logits.float(), -1).cpu().numpy())
    return np.vstack(out)
from sklearn.linear_model import LogisticRegression
from train3 import mat
lr = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), np.array([r[2] for r in rows]))
assert list(lr.classes_) == labels
lines = []
for tag, w in (("微調整だけ", 1.0), ("今の仕組みだけ", 0.0), ("微調整＋今の仕組み（半々）", 0.5), ("微調整7割＋今の仕組み3割", 0.7)):
    res = []
    for tn, te in tests.items():
        P = w * probs(te) + (1 - w) * lr.predict_proba(mat(te)) if w < 1 else probs(te)
        pred = ["unknown" if p == "other" else p for p in decide(labels, P, te)]
        s = score_real(pred, [r[2] for r in te])
        res.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}" + (f" その他見送り{s['other_ok']}/{s['other_ok'] + s['other_ng']}" if s['other_ok'] + s['other_ng'] else ""))
    lines.append(f"| {NAME} 微調整 {EPOCHS}周{'・水増し' if AUG else ''}・{tag} | " + " | ".join(res) + f" | 学習 {time.time() - t0:.0f}秒 |"); print(lines[-1], flush=True)
line = "\n".join(lines)
os.makedirs("ft_out", exist_ok=True); model.save_pretrained("ft_out"); tok.save_pretrained("ft_out"); json.dump(labels, open("ft_out/labels.json", "w"))
prev = (open("FINETUNE_RESULTS.md").read() if os.path.exists("FINETUNE_RESULTS.md") else "# 学習済みモデルの微調整（集計）\n") + f"\n### {time.strftime('%Y-%m-%d %H:%M')}（試験：{', '.join(tests)}）\n"
open("FINETUNE_RESULTS.md", "w").write(prev + line + "\n")
