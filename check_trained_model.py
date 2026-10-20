"""Kaggle で学習したモデルの置き場（artifact から取った ft_out*）が、manifest.json と、依頼に書いた SHA-256 と一致するかを確かめる。2026-10-20。

使い方：python check_trained_model.py <モデルの置き場> [--expect-sha256 <16進>] [--require-manifest] [--out 結果.json]

ブラウザ用の書き出し（browser-model.yml）が『どの回収の・どの仕事の・どの重み』を使ったかを取り違えないための確認（ChatGPT の P0 依頼）。
- 取った重みの SHA-256 を計算し、manifest.json の記録と比べる。
- 依頼（browser_test/run.request の model_sha256=）があれば、それとも比べる。
- 設定ファイル・トークナイザ・ラベルの SHA-256 も manifest の記録と比べる。
- manifest が無い（版 31 以前の回収）のは、--require-manifest を付けなければ警告だけ。
食い違いがあれば終了コード 1。
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import provenance as P


def check(model_dir, expect_sha256=None, require_manifest=False):
    problems, warnings = [], []
    weights = P.weights_digests(model_dir)
    if not weights:
        problems.append("重みのファイル（*.safetensors / *.bin）が無い")
    actual = P.weights_sha256({"saved_model": {"weights": weights}})
    res = {"model_dir": model_dir, "weights": weights, "weights_sha256": actual, "manifest": None}
    manifest = P.read_json(os.path.join(model_dir, "manifest.json"))
    if manifest is None:
        (problems if require_manifest else warnings).append("manifest.json が無い（学習の記録なし。版 31 以前の回収か、記録の書き出しに失敗）")
    else:
        recorded = P.weights_sha256(manifest)
        if recorded is None:
            problems.append("manifest.json に重みの SHA-256 の記録が無い")
        elif recorded != actual:
            problems.append(f"manifest の重みの SHA-256（{recorded[:12]}…）と、取ったモデルの SHA-256（{(actual or '')[:12]}…）が違う")
        for name, digest in ((manifest.get("saved_model") or {}).get("files") or {}).items():
            p = os.path.join(model_dir, name)
            if not os.path.isfile(p):
                problems.append(f"manifest に記録された {name} が無い")
            elif P.sha256_file(p) != digest:
                problems.append(f"{name} の SHA-256 が manifest と違う")
        run = manifest.get("run") or {}
        res["manifest"] = {"status": manifest.get("status"), "commit": manifest.get("commit"), "seed": run.get("seed"), "epochs": run.get("epochs"),
                           "env": run.get("env"), "model": (manifest.get("model") or {}).get("hf_repo_id"),
                           "hf_revision": ((manifest.get("model") or {}).get("hf_revision") or {}).get("revision"),
                           "train_rows": (manifest.get("train_rows") or {}).get("count"), "labels": (manifest.get("labels") or {}).get("count"),
                           "eval_mode": (manifest.get("extra") or {}).get("eval_mode"), "created_utc": manifest.get("created_utc")}
        if manifest.get("status") != "completed":
            problems.append(f"manifest の status が completed でない：{manifest.get('status')}")
    if expect_sha256:
        if (actual or "").lower() != expect_sha256.strip().lower():
            problems.append(f"依頼に書いた SHA-256（{expect_sha256[:12]}…）と、取ったモデルの SHA-256（{(actual or '')[:12]}…）が違う")
        res["expected_sha256"] = expect_sha256.strip().lower()
    res["problems"], res["warnings"], res["ok"] = problems, warnings, not problems
    return res


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("model_dir")
    ap.add_argument("--expect-sha256", default=None)
    ap.add_argument("--require-manifest", action="store_true")
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    res = check(a.model_dir, a.expect_sha256, a.require_manifest)
    text = json.dumps(res, ensure_ascii=False, indent=1)
    print(text)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
