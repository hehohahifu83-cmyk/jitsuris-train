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
# FT_JP3=1：S11 第 1 陣（日本の財務・調達、行をそろえて取り出し、先生＋モデル＋Claude の裁定。materials/real_labels_jp3.jsonl）を学習側だけに足す（2026-10-22）。
# 試験・検証には入れない（検証の列は基準線と同じ）。既定はオフ＝従来どおり。
JP3 = os.environ.get("FT_JP3") == "1"
# FT_JPVAL=1（FT_VAL=1 のときだけ）：jp3 の表の 1/4 を検証「検証（jp3）」に回し、学習には使わない（2026-10-22）。
# 日本の財務の表を足した効果を検証で見るため。比べる両方の群（FT_JP3 あり・なし）に付けて、同じ列で比べる。
JPVAL = os.environ.get("FT_JPVAL") == "1" and os.environ.get("FT_VAL") == "1"
if (JP3 or JPVAL) and not os.path.exists("materials/real_labels_jp3.jsonl"):
    raise SystemExit("FT_JP3／FT_JPVAL なのに materials/real_labels_jp3.jsonl が無い（Kaggle の束に入っているか確かめる）")
j3_all = load_real(("materials/real_labels_jp3.jsonl",)) if (JP3 or JPVAL) else []
if (JP3 or JPVAL) and not j3_all:
    raise SystemExit("FT_JP3／FT_JPVAL なのに jp3 の行が 0")
j3tr, j3val = j3_all, []
if JPVAL:
    from val_split import split_val
    j3tr, j3val = split_val(j3_all, salt="jitsuris-jpval-v1", mod=4)
# FT_POOL=1：教材庫（materials/pool/batch_*.jsonl、pipeline.py で陣ごとに確定した教材）をまとめて学習に足す（2026-10-22。オーナー指示「少しずつ教材を貯めて一気に学習させたい」）。
# FT_VAL=1 のときは教材庫の表の 1/8 を「検証（教材庫）」に回す。水増しの倍率は FT_POOL_COPIES（既定 3）、表あたり 60 列まで。jp3 は教材庫の陣 jp3 として入っているので FT_JP3 と一緒に使わない。
POOL = os.environ.get("FT_POOL") == "1"
POOL_COPIES = int(os.environ.get("FT_POOL_COPIES", "3") or 3)
if POOL and (JP3 or JPVAL):
    raise SystemExit("FT_POOL と FT_JP3／FT_JPVAL は同時に使えない（jp3 が二重に入る）")
pool_all = []
if POOL:
    import glob as _glob
    _pool_files = sorted(_glob.glob("materials/pool/batch_*.jsonl"))
    if not _pool_files:
        raise SystemExit("FT_POOL=1 なのに materials/pool/batch_*.jsonl が無い（Kaggle の束に入っているか確かめる）")
    pool_all = load_real(tuple(_pool_files))
    if not pool_all:
        raise SystemExit("FT_POOL=1 なのに教材庫の行が 0")
pooltr, poolval = pool_all, []
if POOL and os.environ.get("FT_VAL") == "1":
    from val_split import split_val
    pooltr, poolval = split_val(pool_all, salt="jitsuris-poolval-v1", mod=8)
# FT_VAL=1：学習率などを選ぶための検証モード（2026-10-20）。学習側の本物の表のうち 1/8 を検証に回し、固定の試験側には触れない（val_split.py）。
VAL_MODE = os.environ.get("FT_VAL") == "1"
gval = bval = b2val = jval = []
if VAL_MODE:
    from val_split import split_val
    gtr, gval = split_val(gtr); btr, bval = split_val(btr); b2tr, b2val = split_val(b2tr); jtr, jval = split_val(jtr)
REAL_FRAC = parse_real_fraction(os.environ.get("FT_REAL_FRAC"))
# Select on the original rows, whose fifth field is the table ID. After expansion,
# encoder_context stores unit examples in that field, so sampling expanded rows is invalid.
source_splits = (gtr, btr, b2tr, jtr)
all_source_rows = [row for source_rows in source_splits for row in source_rows]
real_tables = {str(row[4]) for row in all_source_rows}
selected_splits = tuple(select_real_fraction(source_rows, REAL_FRAC) for source_rows in source_splits)
gtr, btr, b2tr, jtr = selected_splits
selected_source_rows = [row for source_rows in selected_splits for row in source_rows]
selected_tables = {str(row[4]) for row in selected_source_rows}
unit_by_table = unit_context_map(g_all + b_all + b2_all + j_all + j3_all + pool_all)
syn = build_train({"syn": 400, "muni": 2, "cur": 4}, split_curriculum()[0])
real_rows = real_train_rows_with_units(gtr, 3, 5, True, unit_by_table, perturb) + real_train_rows_with_units(btr, 6, 6, True, unit_by_table, perturb, per_table=60) + real_train_rows_with_units(b2tr, 6, 7, True, unit_by_table, perturb, per_table=60) + real_train_rows_with_units(jtr, 6, 8, True, unit_by_table, perturb, per_table=60)
if JP3:   # 日本の調達（jtr）と同じ倍率・表あたりの上限。種は別
    real_rows += real_train_rows_with_units(j3tr, 6, 9, True, unit_by_table, perturb, per_table=60)
    print(f"FT_JP3=1: +{len(j3tr)} jp3 source rows ({len({r[4] for r in j3tr})} tables)", flush=True)
if POOL:
    real_rows += real_train_rows_with_units(pooltr, POOL_COPIES, 10, True, unit_by_table, perturb, per_table=60)
    print(f"FT_POOL=1: +{len(pooltr)} pool source rows ({len({r[4] for r in pooltr})} tables) x{POOL_COPIES}; validation {len(poolval)}", flush=True)
print(f"FT_REAL_FRAC={REAL_FRAC:g}: selected {len(selected_tables)}/{len(real_tables)} tables and {len(selected_source_rows)}/{len(all_source_rows)} source rows; expanded real rows {len(real_rows)}; synthetic rows unchanged", flush=True)
rows = syn + real_rows
y = np.array([r[2] for r in rows])
tests = {"開発用220": rows_of(), "本物（一般）": attach_unit_context(gte, unit_by_table), "本物（業務）": attach_unit_context(bte, unit_by_table)}
if b2te:
    tests["本物（業務2）"] = attach_unit_context(b2te, unit_by_table)
if jte:
    tests["本物（日本の調達）"] = attach_unit_context(jte, unit_by_table)
if VAL_MODE:   # 検証モードでは固定の試験を評価しない（検証だけ）。名前は試験側と同じ並び
    tests = {}
    for _name, _vr in (("検証（一般）", gval), ("検証（業務）", bval), ("検証（業務2）", b2val), ("検証（日本の調達）", jval), ("検証（jp3）", j3val), ("検証（教材庫）", poolval)):
        if _vr:
            tests[_name] = attach_unit_context(_vr, unit_by_table)
    print("FT_VAL=1: 検証モード（固定の試験は評価しない）。検証の行数 " + ", ".join(f"{k} {len(v)}" for k, v in tests.items()), flush=True)


CTX_UNIT = os.environ.get("FT_CTX_UNIT") == "1"  # 同じ表の UNIT / Unit / 単位の値を文脈に足す ablation（既定オフ）
VAL_PROF = os.environ.get("FT_VALPROF") == "1"  # W3a：値の形（value_profile.py）を値の直後に足す（既定オフ。オフなら入力の文は従来と同じ）

def text(r, prefix):
    return format_encoder_text(r, prefix, ctx_unit=CTX_UNIT, val_profile=VAL_PROF)


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
