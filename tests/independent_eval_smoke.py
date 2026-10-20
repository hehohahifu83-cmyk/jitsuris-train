"""独立評価の経路（evaluate_independent.py）が、学習時の評価と同じ前処理・同じ確率を出すかを、本物の torch で確かめる（CPU・GitHub Actions）。2026-10-21。

使い方（finetune_exp.py を FT_VAL=1 で流したあとの作業場所で）：python tests/independent_eval_smoke.py [--checkpoint ft_out] [--rows 24] [--out 結果.md]

やること：
 ★1 学習が書いた ft_out（manifest つき）を、check_trained_model と同じ検査にかけて読み込む。
 ★2 検証（一般）の先頭の行から主セットの形のファイルを作り、predict（本物の torch の推論）を通す。
 ★3 学習時に書かれた probs_val_general_ft.json と比べる：最上位のラベルが同じ、確率の差が小さい、守りを通した判断が同じ。
 ★4 score を通す（ラベルは別ファイル）。出力が slice_eval.py で読める。
 ★5 同じ（主セット, 重み）の 2 回目の predict が台帳に断られる。
検証の行は学習側の表の 1/8（FT_VAL=1）で、固定試験・blind は使わない。値は結果に出さない。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
results = []


def record(name, ok, detail=""):
    results.append((name, "OK" if ok else "NG", str(detail)))
    print(f"[{'OK' if ok else 'NG'}] {name}: {detail}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", default="ft_out")
    ap.add_argument("--rows", type=int, default=24)
    ap.add_argument("--probs", default="probs_val_general_ft.json")
    ap.add_argument("--out", default="independent_eval_smoke.md")
    a = ap.parse_args()
    os.environ["FT_VAL"] = "1"
    sys.argv = sys.argv[:1]
    import encoder_exp as E
    import evaluate_independent as EV
    import slice_eval as S

    rows = E.tests["検証（一般）"][:a.rows]
    with tempfile.TemporaryDirectory() as d:
        set_path, labels_path = os.path.join(d, "set.json"), os.path.join(d, "labels.json")
        columns = [{"id": f"c{i:03d}", "table": "t", "source": "val", "language": "x", "header": r[0], "values": [str(v) for v in r[1]],
                    "siblings": [str(s) for s in (r[3] or [])], "unit": str(r[4]) if len(r) > 4 and r[4] else ""} for i, r in enumerate(rows)]
        with open(set_path, "w", encoding="utf-8") as fh:
            json.dump({"schema_version": 1, "set_id": "smoke-val-general", "columns": columns}, fh, ensure_ascii=False)
        with open(labels_path, "w", encoding="utf-8") as fh:
            json.dump({c["id"]: r[2] for c, r in zip(columns, rows)}, fh, ensure_ascii=False)

        # ★1
        info = None
        try:
            info = EV.checkpoint_info(a.checkpoint)
            record("★1 重みの検査と設定の読み取り", True, f"model={info['model']} type={info['model_type']} prefix={info['prefix']!r} max_length={info['max_length']} ctx_unit={info['ctx_unit']} 重み {info['weights_sha256'][:12]}…")
        except Exception as e:  # noqa: BLE001
            record("★1 重みの検査と設定の読み取り", False, f"{type(e).__name__}: {e}")
            return finish(a.out)

        # ★2
        preds_path, ledger = os.path.join(d, "preds.json"), os.path.join(d, "ledger.jsonl")
        try:
            doc = EV.predict(set_path, a.checkpoint, preds_path, ledger, device="cpu")
            record("★2 predict（本物の torch）", len(doc["rows"]) == len(rows), f"{len(doc['rows'])} 列・{doc['timing']['seconds']} 秒（{doc['timing']['ms_per_column']} ms/列、CPU）")
        except Exception as e:  # noqa: BLE001
            record("★2 predict（本物の torch）", False, f"{type(e).__name__}: {e}")
            return finish(a.out)

        # ★3
        try:
            with open(a.probs, encoding="utf-8") as fh:
                ref = json.load(fh)["rows"][:len(rows)]
            same_top1 = sum(1 for p, q in zip(doc["rows"], ref) if p["top3"][0]["label"] == q["top3"][0]["label"])
            same_final = sum(1 for p, q in zip(doc["rows"], ref) if p["guarded_prediction"] == q["guarded_prediction"])
            same_col = sum(1 for p, q in zip(doc["rows"], ref) if p["column"] == q["column"])
            drift = max(abs(x["probability"] - y["probability"]) for p, q in zip(doc["rows"], ref) for x, y in zip(p["top3"], q["top3"]) if x["label"] == y["label"])
            n = len(ref)
            record("★3 学習時の評価と一致", same_top1 == n and same_final == n and same_col == n and drift < 5e-3,
                   f"最上位ラベル {same_top1}/{n}、守りを通した判断 {same_final}/{n}、見出し {same_col}/{n}、確率の最大差 {drift:.2e}")
        except Exception as e:  # noqa: BLE001
            record("★3 学習時の評価と一致", False, f"{type(e).__name__}: {e}")

        # ★4
        try:
            out_dir = os.path.join(d, "scored")
            link = EV.score(preds_path, labels_path, out_dir, "job1")
            records = S.load_records(out_dir, "ft")[("job1", "independent_main")]
            record("★4 score と slice_eval の読み込み", len(records) == len(rows) and link["n"] == len(rows), f"件数 {link['counts']}")
        except Exception as e:  # noqa: BLE001
            record("★4 score と slice_eval の読み込み", False, f"{type(e).__name__}: {e}")

        # ★5
        try:
            EV.predict(set_path, a.checkpoint, os.path.join(d, "again.json"), ledger, device="cpu")
            record("★5 同じ組の 2 回目を断る", False, "断られなかった")
        except ValueError as e:
            record("★5 同じ組の 2 回目を断る", "すでに予測済み" in str(e), str(e)[:120])
    return finish(a.out)


def finish(out):
    bad = [r for r in results if r[1] != "OK"]
    lines = ["# 独立評価の経路の試運転（CPU）", "", "| 項目 | 状態 | 内容 |", "|---|---|---|"] + [f"| {n} | {s} | {x} |" for n, s, x in results]
    lines += ["", f"必須項目の NG：{len(bad)} 件"]
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
