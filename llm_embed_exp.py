"""生成モデル（Qwen3・LLM-jp-3・sarashina2.2 など、MIT/Apache）を学習させずに使い、列の文の埋め込み（最後の層の平均）を作って、
判定部（ロジスティック回帰・近傍）だけを学ぶ試験。研究の「凍結した LLM の列の埋め込み」の考え方（教育方針の改訂 2026-10-17 の 2）。
試験は encoder_exp と同じ。集計だけを FINETUNE_RESULTS.md に追記する。"""
import os, sys, time
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from scipy.sparse import csr_matrix, hstack
import gen, features
features.USE_NUM2 = True
from encoder_exp import rows, tests, text
from llm_baseline import score_real
from train3 import decide, mat

NAME = sys.argv[1]
DEV = "cuda" if torch.cuda.is_available() else "cpu"
t0 = time.time()
tok = AutoTokenizer.from_pretrained(NAME)
if tok.pad_token is None: tok.pad_token = tok.eos_token
tok.padding_side = "right"
model = AutoModel.from_pretrained(NAME, torch_dtype=torch.float16 if DEV == "cuda" else torch.float32).to(DEV).eval()
print("device", DEV, NAME, flush=True)


def embed(texts, bs=32):
    out = []
    with torch.no_grad():
        for i in range(0, len(texts), bs):
            enc = tok(texts[i:i + bs], truncation=True, max_length=256, padding=True, return_tensors="pt").to(DEV)
            h = model(**enc).last_hidden_state.float()
            m = enc["attention_mask"].unsqueeze(-1).float()
            out.append(((h * m).sum(1) / m.sum(1)).cpu().numpy())
    return np.vstack(out)


def embed_rows(rs):
    ts = [text(r, "") for r in rs]; uniq = sorted(set(ts)); idx = {t: i for i, t in enumerate(uniq)}
    E = embed(uniq); return E[[idx[t] for t in ts]]


E = embed_rows(rows); y = np.array([r[2] for r in rows])
print("埋め込み", E.shape, f"{time.time() - t0:.0f}s", flush=True)
ET = {tn: embed_rows(te) for tn, te in tests.items()}
sc = StandardScaler().fit(E)
lr_e = LogisticRegression(C=1.0, max_iter=3000).fit(sc.transform(E), y)
Xs = mat(rows)
lr_c = LogisticRegression(C=1.0, max_iter=3000).fit(hstack([csr_matrix(sc.transform(E)), Xs]).tocsr(), y)
labels = list(lr_e.classes_)
# 近傍：ラベル付きの列の埋め込みから近いもの10件の多数決（端末の中の検索の考え方）
En = E / np.linalg.norm(E, axis=1, keepdims=True); Y = np.array([labels.index(l) for l in y])
def knn_probs(T, k=10):
    Tn = T / np.linalg.norm(T, axis=1, keepdims=True); P = np.zeros((len(T), len(labels)))
    for i in range(0, len(Tn), 512):
        S = Tn[i:i + 512] @ En.T; top = np.argpartition(-S, k, axis=1)[:, :k]
        for j, row in enumerate(top):
            for t in row: P[i + j, Y[t]] += 1
    return P / k
lines = []
for tag, fn in (("埋め込み＋LR", lambda tn, te: lr_e.predict_proba(sc.transform(ET[tn]))),
                ("埋め込み＋今の特徴＋LR", lambda tn, te: lr_c.predict_proba(hstack([csr_matrix(sc.transform(ET[tn])), mat(te)]).tocsr())),
                ("埋め込み＋LR と近傍の半々", lambda tn, te: 0.5 * lr_e.predict_proba(sc.transform(ET[tn])) + 0.5 * knn_probs(ET[tn]))):
    res = []
    for tn, te in tests.items():
        P = fn(tn, te)
        pred = ["unknown" if p == "other" else p for p in decide(labels, P, te)]
        s = score_real(pred, [r[2] for r in te])
        res.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}")
    lines.append(f"| {NAME} 凍結埋め込み・{tag} | " + " | ".join(res) + f" | {time.time() - t0:.0f}秒 |"); print(lines[-1], flush=True)
prev = (open("FINETUNE_RESULTS.md").read() if os.path.exists("FINETUNE_RESULTS.md") else "# 集計\n") + f"\n### {time.strftime('%Y-%m-%d %H:%M')} 凍結埋め込み（試験：{', '.join(tests)}）\n"
open("FINETUNE_RESULTS.md", "w").write(prev + "\n".join(lines) + "\n")
