"""1 回の学習が『何で・何を・どの設定で』作ったかを manifest.json に残す（2026-10-20、P0：成果物の追跡）。

背景：10/20 の Kaggle 学習（版31）では、持ち帰られたモデルが baseline の仕事1だけで、リプレイの仕事3・4の重みは残らなかった。
ブラウザの試験の依頼も、古い実行の番号を指したままだった。『どの重みを、どのデータ・設定で作り、どれを評価したか』を後から確かめられないと、
結果を比べても次の学習・製品に繋げられない。ここでは、重みの SHA-256・学習データの要約ハッシュ・設定・コードの版・ライブラリの版を 1 つの JSON にまとめる。

方針：
- 列の値そのもの（お客さまのデータではなく公開データ・合成データだが）は書かない。ハッシュと件数だけ。
- 重い依存（torch など）に頼らない純粋な関数だけ。tests/test_provenance.py で試験する。
- 未見セット（blind_set*）は読まない。
"""
from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
import time

SCHEMA_VERSION = 1
# コードの版として記録するファイル（学習の計算に関わるもの）
CODE_FILES = ("finetune_exp.py", "encoder_exp.py", "encoder_context.py", "train3.py", "features.py", "gen.py",
              "jobs.py", "batching.py", "evaluation_records.py", "llm_baseline.py", "exp7.py", "provenance.py")


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def _canon(row):
    """学習の 1 行 → 順序の決まった文字列（値は文字列にそろえる）。"""
    header, values, label = row[0], row[1], row[2]
    ctx = row[3] if len(row) > 3 and row[3] else []
    unit = row[4] if len(row) > 4 else ""
    return json.dumps([str(header), [str(v) for v in values], str(label), [str(c) for c in ctx], str(unit or "")], ensure_ascii=False, separators=(",", ":"))


def rows_digest(rows):
    """学習の行の並びの SHA-256（並びも込み。同じ行でも順番が違えば別のハッシュ）と、並びを問わないハッシュを返す。"""
    ordered = hashlib.sha256()
    lines = []
    for r in rows:
        s = _canon(r)
        ordered.update(s.encode("utf-8")); ordered.update(b"\n")
        lines.append(hashlib.sha256(s.encode("utf-8")).hexdigest())
    unordered = hashlib.sha256("\n".join(sorted(lines)).encode("ascii")).hexdigest()
    return {"count": len(lines), "sha256_ordered": ordered.hexdigest(), "sha256_unordered": unordered}


def labels_digest(labels):
    return {"count": len(labels), "sha256": sha256_bytes(json.dumps(list(labels), ensure_ascii=False, separators=(",", ":")).encode("utf-8"))}


def ft_env(environ=None):
    """FT_ で始まる環境変数（学習の設定）をそのまま。値が空のものは外す。"""
    environ = os.environ if environ is None else environ
    return {k: v for k, v in sorted(environ.items()) if k.startswith("FT_") and v != ""}


def code_digests(root=".", names=CODE_FILES):
    out = {}
    for n in names:
        p = os.path.join(root, n)
        if os.path.isfile(p):
            out[n] = sha256_file(p)
    return out


def weights_digests(dir_):
    """保存したモデルの置き場にある重みのファイル（*.safetensors / *.bin）の SHA-256 とバイト数。"""
    out = {}
    if not os.path.isdir(dir_):
        return out
    for n in sorted(os.listdir(dir_)):
        if n.endswith((".safetensors", ".bin")):
            p = os.path.join(dir_, n)
            out[n] = {"sha256": sha256_file(p), "bytes": os.path.getsize(p)}
    return out


def small_files_digests(dir_, names=("config.json", "tokenizer.json", "tokenizer_config.json", "labels.json", "special_tokens_map.json", "tokenizer.model")):
    out = {}
    for n in names:
        p = os.path.join(dir_, n)
        if os.path.isfile(p):
            out[n] = sha256_file(p)
    return out


def output_digests(root, patterns):
    """出力ファイル（確率・誤りの一覧・集計）の SHA-256。root からの相対の名前で返す。"""
    import glob
    out = {}
    for pat in patterns:
        for p in sorted(glob.glob(os.path.join(root, pat))):
            if os.path.isfile(p):
                out[os.path.relpath(p, root).replace(os.sep, "/")] = sha256_file(p)
    return out


def length_stats(lengths, max_length):
    """トークン数の並び → 平均・分位点・最大・max_length を超えて切り捨てられる割合。"""
    n = len(lengths)
    if not n:
        return {"n": 0, "mean": 0.0, "p50": 0, "p95": 0, "p99": 0, "max": 0, "max_length": max_length, "truncated": 0, "truncated_rate": 0.0}
    s = sorted(lengths)

    def q(p):
        return s[min(n - 1, int(p * n))]
    trunc = sum(1 for x in lengths if x > max_length)
    return {"n": n, "mean": sum(lengths) / n, "p50": q(0.5), "p95": q(0.95), "p99": q(0.99), "max": s[-1],
            "max_length": max_length, "truncated": trunc, "truncated_rate": trunc / n}


def library_versions():
    v = {"python": sys.version.split()[0], "platform": platform.platform()}
    for mod in ("torch", "transformers", "numpy", "scikit-learn", "tokenizers", "safetensors"):
        try:
            name = "sklearn" if mod == "scikit-learn" else mod
            m = __import__(name)
            v[mod] = getattr(m, "__version__", "?")
        except Exception:  # noqa: BLE001
            v[mod] = None
    return v


def read_commit(paths=("kaggle/commit.txt", "commit.txt")):
    """Kaggle の束に GitHub 側が書いた commit（無ければ unknown）。"""
    for p in paths:
        if os.path.isfile(p):
            s = open(p, encoding="utf-8").read().strip()
            if s:
                return s
    return os.environ.get("GITHUB_SHA", "unknown")


def build_manifest(*, model_name, hf_repo_id, epochs, seed, labels, train_rows, replay_rows=(), tests=None,
                   source_model_dir=None, saved_model_dir=None, extra=None, environ=None, code_root="."):
    """manifest の辞書を作る。tests は {試験名: 行数}。source_model_dir は学習の出発点（HF のモデルを置いた場所）、saved_model_dir は学習後の保存先。"""
    m = {
        "schema_version": SCHEMA_VERSION,
        "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "commit": read_commit(),
        "model": {"name_or_path": model_name, "hf_repo_id": hf_repo_id,
                  "source_files": small_files_digests(source_model_dir) if source_model_dir else {}},
        "run": {"seed": seed, "epochs": epochs, "env": ft_env(environ)},
        "labels": labels_digest(labels),
        "train_rows": rows_digest(train_rows),
        "replay_rows": rows_digest(replay_rows) if replay_rows else {"count": 0},
        "tests": dict(tests or {}),
        "code": code_digests(code_root),
        "libraries": library_versions(),
        "saved_model": {"files": small_files_digests(saved_model_dir) if saved_model_dir else {},
                        "weights": weights_digests(saved_model_dir) if saved_model_dir else {}},
    }
    if extra:
        m["extra"] = extra
    return m


def write_manifest(path, manifest):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1, sort_keys=True)
    return path


def hf_repo_id_from_path(name):
    """Kaggle に送るときの置き場 hfmodel/<org>__<name> → <org>/<name>。それ以外はそのまま返す。"""
    base = os.path.basename(str(name).rstrip("/"))
    if "__" in base and str(name).replace("\\", "/").startswith("hfmodel/"):
        org, _, rest = base.partition("__")
        return f"{org}/{rest}"
    return str(name)


def weights_sha256(manifest):
    """manifest から重みの代表ハッシュ（複数ファイルなら連結したハッシュ）を取り出す。"""
    w = (manifest.get("saved_model") or {}).get("weights") or {}
    if not w:
        return None
    if len(w) == 1:
        return next(iter(w.values()))["sha256"]
    return sha256_bytes("\n".join(f"{k}:{w[k]['sha256']}" for k in sorted(w)).encode("ascii"))
