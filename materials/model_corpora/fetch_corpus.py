"""上位モデルの学習データ（権利の表示がはっきりしたものだけ）を取り、形を調べる・列の候補に変える（2026-10-27 Claude）。

オーナー指示（2026-10-27）「ジツリスの上位互換モデルを検索しその学習データを入手してくれ、教材もあるだけ」。
取ってよいもの（`CORPORA`）は、配布元がライセンスを明示しているものだけ（Zenodo・Hugging Face の記録で確認、
`probe/probe_20261027.json`）。ダウンロードは Actions（model-corpora-fetch.yml）の作業場所だけで行い、元のアーカイブは commit しない。

  python -I materials/model_corpora/fetch_corpus.py inspect <名前> <出力.md>   # ファイルの一覧と最初の数行だけ
"""
import io
import json
import os
import sys
import urllib.request
import zipfile
from pathlib import Path

UA = "jitsuris-train model-corpora fetch"

CORPORA = {
    "wikidbs10k": {"url": "https://zenodo.org/records/8227452/files/wikidbs_10k.zip?download=1", "license": "CC-BY-4.0",
                   "attribution": "WikiDBs (10k), Vogel, Bodensohn, Binnig, DOI 10.5281/zenodo.8227452; built from Wikidata (CC0)"},
    "semtab2023_wikidata": {"url": "https://zenodo.org/records/8393535/files/WikidataTables2023R1.zip?download=1", "license": "CC-BY-4.0",
                            "attribution": "SemTab 2023 WikidataTables Round 1, DOI 10.5281/zenodo.8393535"},
    "gittables_cta": {"url": "https://zenodo.org/api/records/5706316", "license": "CC-BY-4.0", "zenodo_files": True,
                      "attribution": "GitTables benchmark - column type detection, DOI 10.5281/zenodo.5706316"},
    "sotab_v2": {"url": "https://zenodo.org/records/8422037/files/SOTAB%20V2%20for%20SemTab%202023.zip?download=1", "license": "CC-BY-4.0",
                 "attribution": "SOTAB V2 for SemTab 2023, Korini, Peeters, Bizer, DOI 10.5281/zenodo.8422037"},
    "tableinstruct": {"url": "https://huggingface.co/api/datasets/osunlp/TableInstruct/tree/main?recursive=true", "license": "CC-BY-4.0", "hf_tree": True,
                      "attribution": "TableInstruct, Zhang et al. (TableLlama), osunlp/TableInstruct on Hugging Face"},
}

WORK = Path(os.environ.get("CORPUS_WORK", "/tmp/corpora"))


def download(url, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return dest
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=600) as r, open(dest, "wb") as f:
        while True:
            chunk = r.read(1 << 22)
            if not chunk:
                break
            f.write(chunk)
    return dest


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def head_bytes(data, n=1500):
    text = data[:n].decode("utf-8", errors="replace")
    return text.replace("```", "'''")


def inspect_zip(path, lines):
    with zipfile.ZipFile(path) as z:
        infos = z.infolist()
        lines.append(f"- zip の中身：{len(infos)} 件、展開後 {sum(i.file_size for i in infos) / 2**20:.1f} MB")
        exts = {}
        for i in infos:
            ext = Path(i.filename).suffix.lower() or "(なし)"
            exts[ext] = exts.get(ext, 0) + 1
        lines.append(f"- 拡張子：{dict(sorted(exts.items(), key=lambda x: -x[1]))}")
        dirs = sorted({str(Path(i.filename).parent) for i in infos})
        lines.append(f"- フォルダ（最初の 40）：{dirs[:40]}")
        shown, per_ext = 0, {}
        for i in infos:
            if i.is_dir():
                continue
            ext = Path(i.filename).suffix.lower()
            if per_ext.get(ext, 0) >= 3 or shown >= 14:
                continue
            per_ext[ext] = per_ext.get(ext, 0) + 1
            shown += 1
            with z.open(i) as f:
                data = f.read(4000)
            if ext in (".zip", ".gz", ".parquet", ".bz2", ".db", ".sqlite"):
                lines.append(f"\n### {i.filename}（{i.file_size} bytes、中を開かない形式）")
                if ext == ".zip":
                    try:
                        with z.open(i) as f2:
                            inner = zipfile.ZipFile(io.BytesIO(f2.read()))
                        names = inner.namelist()
                        lines.append(f"- 中の zip：{len(names)} 件。最初：{names[:10]}")
                        for nm in names[:3]:
                            if not nm.endswith("/"):
                                lines.append(f"\n#### {nm}\n```\n{head_bytes(inner.read(nm))}\n```")
                    except Exception as e:  # noqa: BLE001
                        lines.append(f"- 中の zip を開けない：{e}")
                continue
            lines.append(f"\n### {i.filename}（{i.file_size} bytes）\n```\n{head_bytes(data)}\n```")


def cmd_inspect(name, out):
    c = CORPORA[name]
    lines = [f"# {name} の点検（ファイルの形だけ）", "", f"- 出典：{c['attribution']}", f"- ライセンス表示：{c['license']}", f"- URL：{c['url']}"]
    if c.get("zenodo_files"):
        rec = get_json(c["url"])
        for f in rec.get("files", []):
            p = download(f["links"]["self"], WORK / name / f["key"])
            lines.append(f"\n## {f['key']}（{f['size']} bytes）")
            if p.suffix == ".zip":
                inspect_zip(p, lines)
            else:
                lines.append(f"```\n{head_bytes(p.read_bytes())}\n```")
    elif c.get("hf_tree"):
        tree = get_json(c["url"])
        lines.append(f"\n## ファイル一覧（{len(tree)} 件）")
        for t in tree:
            lines.append(f"- {t.get('path')}（{t.get('size')} bytes）")
        targets = [t["path"] for t in tree if t.get("type") == "file" and ("col_type" in t["path"] or "column_type" in t["path"] or "cta" in t["path"].lower())]
        for path in targets[:4]:
            url = f"https://huggingface.co/datasets/osunlp/TableInstruct/resolve/main/{path}"
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Range": "bytes=0-3999"})
            with urllib.request.urlopen(req, timeout=120) as r:
                lines.append(f"\n### {path}（先頭 4KB）\n```\n{head_bytes(r.read(), 3500)}\n```")
    else:
        p = download(c["url"], WORK / name / "archive.zip")
        lines.append(f"- ダウンロード：{p.stat().st_size} bytes")
        inspect_zip(p, lines)
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote", out)


def main(argv=None):
    argv = argv or sys.argv[1:]
    if argv[0] == "inspect":
        cmd_inspect(argv[1], argv[2])
    else:
        raise SystemExit(f"知らない命令：{argv[0]}")


if __name__ == "__main__":
    main()
