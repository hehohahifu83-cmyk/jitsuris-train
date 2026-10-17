"""学習済みの多言語の文の埋め込みモデル（Hugging Face）を土台にした判定の試験。GitHub Actions で実行（モデルの取得が要るため）。
入力の文：「列名: … | 値: … | 同じ表: …」。頭（判定部）はロジスティック回帰。今の疎な特徴とつなげた版も比べる。
出すのは集計だけ（ENCODER_RESULTS.md）。未見セットは使わない。"""
import json, sys, time
import numpy as np
from scipy.sparse import csr_matrix, hstack
from sklearn.linear_model import LogisticRegression
import gen
from exp7 import load_real, split, real_train_rows
from llm_baseline import score_real
from train3 import build_train, mat, split_curriculum, decide
from dev_eval import rows_of

gen.HARD_NUMERIC = 0.0
import os
gtr, gte = split(load_real(("materials/real_labels.jsonl",))); btr, bte = split(load_real(("materials/real_labels_biz.jsonl",)))
b2tr, b2te = split(load_real(("materials/real_labels_biz2.jsonl", "materials/real_labels_direct.jsonl"))) if os.path.exists("materials/real_labels_biz2.jsonl") else ([], [])
jtr, jte = split(load_real(("materials/real_labels_jp.jsonl",))) if os.path.exists("materials/real_labels_jp.jsonl") else ([], [])
syn = build_train({"syn": 400, "muni": 2, "cur": 4}, split_curriculum()[0])
rows = syn + real_train_rows(gtr, 3, 5, True) + real_train_rows(btr, 6, 6, True, per_table=60) + real_train_rows(b2tr, 6, 7, True, per_table=60) + real_train_rows(jtr, 6, 8, True, per_table=60)
y = np.array([r[2] for r in rows])
tests = {"開発用220": rows_of(), "本物（一般）": [(h, v, l, c) for h, v, l, c, _ in gte], "本物（業務）": [(h, v, l, c) for h, v, l, c, _ in bte]}
if b2te:
    tests["本物（業務2）"] = [(h, v, l, c) for h, v, l, c, _ in b2te]
if jte:
    tests["本物（日本の調達）"] = [(h, v, l, c) for h, v, l, c, _ in jte]


def text(r, prefix):
    h, v = r[0], r[1]; ctx = r[3] if len(r) > 3 and r[3] else []
    return f"{prefix}列名: {h} | 値: {', '.join(str(x)[:30] for x in v[:5])} | 同じ表の列: {', '.join(str(x)[:20] for x in ctx[:12])}"


def run(model_name, prefix, out):
    from sentence_transformers import SentenceTransformer
    t0 = time.time(); m = SentenceTransformer(model_name, device="cpu")
    emb = lambda rs: m.encode([text(r, prefix) for r in rs], batch_size=128, normalize_embeddings=True, show_progress_bar=False)
    E = emb(rows); print(model_name, "埋め込み", E.shape, f"{time.time() - t0:.0f}s", flush=True)
    ET = {tn: emb(te) for tn, te in tests.items()}
    Xs = mat(rows)
    for tag, X in (("埋め込みだけ", csr_matrix(E)), ("埋め込み＋今の特徴", hstack([csr_matrix(E * 2.0), Xs]).tocsr())):
        for C in (8,):
            lr = LogisticRegression(C=C, max_iter=2000).fit(X, y); print(tag, "学習", f"{time.time() - t0:.0f}s", flush=True)
            res = []
            for tn, te in tests.items():
                Et = ET[tn]; Xt = csr_matrix(Et) if tag == "埋め込みだけ" else hstack([csr_matrix(Et * 2.0), mat(te)]).tocsr()
                pred = ["unknown" if p == "other" else p for p in decide(list(lr.classes_), lr.predict_proba(Xt), te)]
                s = score_real(pred, [r[2] for r in te])
                res.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}" + (f" その他見送り{s['other_ok']}/{s['other_ok'] + s['other_ng']}" if s['other_ok'] + s['other_ng'] else ""))
            line = f"| {model_name} | {tag} | C={C} | " + " | ".join(res) + " |"
            print(line, flush=True); out.append(line)
            open("ENCODER_RESULTS.md", "w").write("\n".join(out) + "\n")


if __name__ == "__main__":
    out = ["# 学習済みの埋め込みモデルを土台にした試験（集計）", "", f"学習 {len(rows)} 行（合成を減らし、本物の表の学習側を入れた）。試験は Claude 側の試験（表ごとに分けた試験側・開発用）。", "",
           "| モデル | 入力 | 正則化 | 開発用220 | 本物（一般） | 本物（業務） |", "|---|---|---|---|---|---|"]
    # 比べ先：今の仕組み（同じ学習データ）
    lr = LogisticRegression(C=8, max_iter=4000).fit(mat(rows), y); res = []
    for tn, te in tests.items():
        s = score_real(["unknown" if p == "other" else p for p in decide(list(lr.classes_), lr.predict_proba(mat(te)), te)], [r[2] for r in te])
        res.append(f"{tn} 正{s['acc_all']:.1%} 誤{s['wrong']} 不明{s['unknown']} 重大{s['critical']}")
    out.append("| 今の仕組み（v7と同じ作り） | 今の特徴 | C=8 | " + " | ".join(res) + " |")
    for name, prefix in [("intfloat/multilingual-e5-small", "query: "), ("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", ""), ("intfloat/multilingual-e5-base", "query: ")][: int(sys.argv[1]) if len(sys.argv) > 1 else 3]:
        try:
            run(name, prefix, out)
        except Exception as e:  # noqa: BLE001
            out.append(f"| {name} | 失敗 | {type(e).__name__}: {str(e)[:100]} | | | |")
    open("ENCODER_RESULTS.md", "w").write("\n".join(out) + "\n"); print("\n".join(out))
