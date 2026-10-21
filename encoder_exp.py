"""学習済みの多言語の文の埋め込みモデル（Hugging Face）を土台にした判定の試験。GitHub Actions で実行（モデルの取得が要るため）。
入力の文：「列名: … | 値: … | 同じ表: …」。頭（判定部）はロジスティック回帰。今の疎な特徴とつなげた版も比べる。
出すのは集計だけ（ENCODER_RESULTS.md）。未見セットは使わない。"""
import json, sys, time
import numpy as np
from scipy.sparse import csr_matrix, hstack
from sklearn.linear_model import LogisticRegression
import gen
from exp7 import load_real, split, perturb
from encoder_context import attach_unit_context, format_encoder_text, real_train_rows_with_units, unit_context_map
from real_fraction import parse_real_fraction, select_real_fraction
from llm_baseline import score_real
from train3 import build_train, mat, split_curriculum, decide
from dev_eval import rows_of

gen.HARD_NUMERIC = 0.0
import os
g_all = load_real(("materials/real_labels.jsonl",))
b_all = load_real(("materials/real_labels_biz.jsonl",))
b2_all = load_real(("materials/real_labels_biz2.jsonl", "materials/real_labels_direct.jsonl")) if os.path.exists("materials/real_labels_biz2.jsonl") else []
j_all = load_real(tuple(f for f in ("materials/real_labels_jp.jsonl", "materials/real_labels_jp2.jsonl") if os.path.exists(f))) if os.path.exists("materials/real_labels_jp.jsonl") else []
gtr, gte = split(g_all); btr, bte = split(b_all); b2tr, b2te = split(b2_all); jtr, jte = split(j_all)
# FT_VAL=1：学習率などを選ぶための検証モード（2026-10-20）。学習側の本物の表のうち 1/8 を検証に回し、固定の試験側には触れない（val_split.py）。
VAL_MODE = os.environ.get("FT_VAL") == "1"
gval = bval = b2val = jval = []
if VAL_MODE:
    from val_split import split_val
    gtr, gval = split_val(gtr); btr, bval = split_val(btr); b2tr, b2val = split_val(b2tr); jtr, jval = split_val(jtr)
unit_by_table = unit_context_map(g_all + b_all + b2_all + j_all)
syn = build_train({"syn": 400, "muni": 2, "cur": 4}, split_curriculum()[0])
real_rows = real_train_rows_with_units(gtr, 3, 5, True, unit_by_table, perturb) + real_train_rows_with_units(btr, 6, 6, True, unit_by_table, perturb, per_table=60) + real_train_rows_with_units(b2tr, 6, 7, True, unit_by_table, perturb, per_table=60) + real_train_rows_with_units(jtr, 6, 8, True, unit_by_table, perturb, per_table=60)
REAL_FRAC = parse_real_fraction(os.environ.get("FT_REAL_FRAC"))
selected_real_rows = select_real_fraction(real_rows, REAL_FRAC)
real_tables = {str(r[4]) for r in real_rows}
selected_tables = {str(r[4]) for r in selected_real_rows}
print(f"FT_REAL_FRAC={REAL_FRAC:g}: selected {len(selected_tables)}/{len(real_tables)} tables and {len(selected_real_rows)}/{len(real_rows)} rows; synthetic rows unchanged", flush=True)
rows = syn + selected_real_rows
y = np.array([r[2] for r in rows])
tests = {"開発用220": rows_of(), "本物（一般）": attach_unit_context(gte, unit_by_table), "本物（業務）": attach_unit_context(bte, unit_by_table)}
if b2te:
    tests["本物（業務2）"] = attach_unit_context(b2te, unit_by_table)
if jte:
    tests["本物（日本の調達）"] = attach_unit_context(jte, unit_by_table)
if VAL_MODE:   # 検証モードでは固定の試験を評価しない（検証だけ）。名前は試験側と同じ並び
    tests = {}
    for _name, _vr in (("検証（一般）", gval), ("検証（業務）", bval), ("検証（業務2）", b2val), ("検証（日本の調達）", jval)):
        if _vr:
            tests[_name] = attach_unit_context(_vr, unit_by_table)
    print("FT_VAL=1: 検証モード（固定の試験は評価しない）。検証の行数 " + ", ".join(f"{k} {len(v)}" for k, v in tests.items()), flush=True)


CTX_UNIT = os.environ.get("FT_CTX_UNIT") == "1"  # 同じ表の UNIT / Unit / 単位の値を文脈に足す ablation（既定オフ）

def text(r, prefix):
    return format_encoder_text(r, prefix, ctx_unit=CTX_UNIT)


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
