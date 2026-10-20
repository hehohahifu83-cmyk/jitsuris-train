"""Hugging Face のモデルを、学習に要るファイルだけ取る（kaggle.sh と mmbert-smoke.yml から使う）。2026-10-20。

使い方：python kaggle/hf_fetch.py <repo> <保存先> [--tokenizer-only]

- 基本の取り方は今までと同じ（*.json *.safetensors *.model *.txt sentencepiece* tokenizer*）。
- 先頭の階層に *.safetensors が無く、pytorch_model*.bin がある（mmBERT-small など）ときだけ、その bin も取る
  （E5 のように safetensors がある repo では bin は取らない＝束が重くならない）。
- どの版（commit）・ライセンスの表示のモデルを取ったかを <保存先>/hf_revision.json に残す（学習の記録 manifest.json に入る）。
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import sys

BASE_PATTERNS = ["*.json", "*.safetensors", "*.model", "*.txt", "sentencepiece*", "tokenizer*"]


def choose_patterns(files, tokenizer_only=False):
    """repo のファイル一覧 → allow_patterns。"""
    if tokenizer_only:
        return [p for p in BASE_PATTERNS if p != "*.safetensors"]
    pats = list(BASE_PATTERNS)
    top = [f for f in files if "/" not in f]
    has_safetensors = any(fnmatch.fnmatch(f, "*.safetensors") for f in top)
    if not has_safetensors and any(fnmatch.fnmatch(f, "pytorch_model*.bin") for f in top):
        pats.append("pytorch_model*.bin")
    return pats


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("dest")
    ap.add_argument("--tokenizer-only", action="store_true")
    a = ap.parse_args(argv)
    from huggingface_hub import HfApi, snapshot_download
    info = HfApi().model_info(a.repo)
    files = [s.rfilename for s in (info.siblings or [])]
    pats = choose_patterns(files, a.tokenizer_only)
    lic = None
    try:
        lic = info.card_data.license if info.card_data is not None else None
    except Exception:  # noqa: BLE001
        lic = None
    print(f"{a.repo} revision {info.sha} license {lic} tags {[t for t in (info.tags or []) if t.startswith('license')]}", flush=True)
    print("repo files:", sorted(files), flush=True)
    print("allow_patterns:", pats, flush=True)
    snapshot_download(a.repo, local_dir=a.dest, allow_patterns=pats)
    got = sorted(f for f in os.listdir(a.dest) if os.path.isfile(os.path.join(a.dest, f)))
    meta = {"repo": a.repo, "revision": info.sha, "license": lic, "patterns": pats, "top_level_files": got}
    with open(os.path.join(a.dest, "hf_revision.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    print("fetched:", got, flush=True)
    if not a.tokenizer_only and not any(f.endswith((".safetensors", ".bin")) for f in got):
        print("ERROR: 重みのファイルが取れていない", file=sys.stderr, flush=True)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
