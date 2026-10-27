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


# ---------------------------------------------------------------- 列の候補に変える（convert）
# 1 行＝1 列：{corpus, split, table, col, header, values（5 つまで・60 字まで）, context（同じ表の見出し）, source_label, source_kind}
# 元のラベルはそのまま残す（16 種への読み替えは別に決める）。値は公開の表の一部だけ。個人情報は落とす。

N_VALUES = 5
SHARD_ROWS = 100_000
# 人の名前・連絡先・番地の種類は列ごと使わない（教材庫の決まり：公開データの人の名前は入れない。2026-10-24）
SOTAB_DROP = {"Person/name", "Person", "email", "telephone", "faxNumber", "streetAddress", "PostalAddress", "GenderType"}


def _pii():
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    import fetch_rows as F   # noqa: E402 — 取り出しと同じ個人情報の決まりを使う
    return F.blocked_header, F.sensitive_value


def pick_values(vals, key):
    import hashlib
    seen, out = set(), []
    clean = []
    for v in vals:
        s = str(v if v is not None else "").strip()
        if s and s.lower() not in ("nan", "none", "null") and s not in seen:
            seen.add(s)
            clean.append(s)
    clean.sort(key=lambda s: hashlib.sha256(f"{key}|{s}".encode()).hexdigest())
    for s in clean[:N_VALUES]:
        out.append(s[:60])
    return out, len(clean)


class Writer:
    def __init__(self, out_dir):
        import gzip
        self.gzip = gzip
        self.dir = Path(out_dir)
        self.dir.mkdir(parents=True, exist_ok=True)
        for old in self.dir.glob("part-*.jsonl.gz"):
            old.unlink()
        self.n, self.part, self.f = 0, 0, None

    def write(self, rec):
        if self.f is None or self.n % SHARD_ROWS == 0:
            if self.f:
                self.f.close()
            self.f = self.gzip.open(self.dir / f"part-{self.part:03d}.jsonl.gz", "wt", encoding="utf-8")
            self.part += 1
        self.f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        self.n += 1

    def close(self):
        if self.f:
            self.f.close()


def read_json_table(data):
    import gzip
    text = gzip.decompress(data).decode("utf-8", errors="replace")
    try:
        obj = json.loads(text)
        rows = obj if isinstance(obj, list) else obj.get("data") or list(obj.values())
    except json.JSONDecodeError:
        rows = [json.loads(line) for line in text.splitlines() if line.strip()]
    return rows


def convert_sotab(path, writer, stats):
    import csv
    blocked_header, sensitive_value = _pii()
    tmp = WORK / "sotab_inner"
    tmp.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        stats["outer_files"] = names
        for gt_name in [n for n in names if "CTA" in n and "DatasetsAndGroundTruth" in n]:
            rnd = Path(gt_name).name.split("-")[0]   # Round1・Round2 など
            cands = [n for n in names if Path(n).name.startswith(rnd + "-") and "CTA" in Path(n).name and "Tables" in Path(n).name]
            tables_name = next((n for n in cands if "SCH" in Path(n).name), cands[0] if cands else None)
            if not tables_name:
                stats.setdefault("missing_tables_zip", []).append(gt_name)
                continue
            gt_zip = zipfile.ZipFile(io.BytesIO(z.read(gt_name)))
            labels = {}
            for split in ("train", "validation"):   # test は使わない（ベンチマークの試験用）
                csv_name = next((n for n in gt_zip.namelist() if f"cta_{split}_" in n and n.endswith(".csv") and "target" not in n), None)
                if not csv_name:
                    continue
                for row in csv.DictReader(io.TextIOWrapper(gt_zip.open(csv_name), encoding="utf-8")):
                    labels.setdefault(row["table_name"], []).append((int(row["column_index"]), row["label"], split))
            inner = tmp / Path(tables_name).name
            with z.open(tables_name) as src, open(inner, "wb") as dst:
                while True:
                    chunk = src.read(1 << 22)
                    if not chunk:
                        break
                    dst.write(chunk)
            with zipfile.ZipFile(inner) as tz:
                by_base = {Path(n).name: n for n in tz.namelist() if n.endswith(".json.gz")}
                for table, cols in labels.items():
                    member = by_base.get(table)
                    if not member:
                        stats["table_missing"] = stats.get("table_missing", 0) + 1
                        continue
                    try:
                        rows = read_json_table(tz.read(member))
                    except Exception:  # noqa: BLE001
                        stats["table_unreadable"] = stats.get("table_unreadable", 0) + 1
                        continue
                    for ci, lab, split in cols:
                        if lab in SOTAB_DROP:
                            stats["dropped_person_contact"] = stats.get("dropped_person_contact", 0) + 1
                            continue
                        vals = [r.get(str(ci), r.get(ci)) if isinstance(r, dict) else (r[ci] if ci < len(r) else None) for r in rows]
                        vals = [v for v in vals if not isinstance(v, (dict, list))]
                        if any(sensitive_value(v) for v in vals):
                            stats["dropped_sensitive_values"] = stats.get("dropped_sensitive_values", 0) + 1
                            continue
                        values, distinct = pick_values(vals, f"{table}|{ci}")
                        if not values:
                            stats["empty"] = stats.get("empty", 0) + 1
                            continue
                        writer.write({"corpus": "sotab_v2", "round": rnd, "split": split, "table": table, "col": ci, "header": "",
                                      "values": values, "distinct": distinct, "rows": len(rows), "context": [],
                                      "source_label": lab, "source_kind": "schema.org (SOTAB V2 CTA)"})
                        stats["labels"][lab] = stats["labels"].get(lab, 0) + 1
            inner.unlink()


def parse_wikidbs_cell(v):
    s = str(v or "").strip()
    if s.startswith("['") and s.endswith("']") and "', 'Q" in s:   # 項目は ['名前', 'Q123'] の形
        return s[2:s.rindex("', 'Q")]
    return s


def convert_wikidbs(path, writer, stats):
    import csv
    csv.field_size_limit(10_000_000)
    blocked_header, sensitive_value = _pii()
    with zipfile.ZipFile(path) as z:
        infos = [n for n in z.namelist() if n.endswith("info_full.json")]
        for info_name in infos:
            db_dir = info_name.rsplit("/", 1)[0]
            info = json.loads(z.read(info_name))
            for tname, t in info.get("TABLES", {}).items():
                member = f"{db_dir}/tables/{t['FILEPATH']}"
                if member not in z.NameToInfo:
                    stats["table_missing"] = stats.get("table_missing", 0) + 1
                    continue
                reader = csv.reader(io.TextIOWrapper(z.open(member), encoding="utf-8", errors="replace"))
                try:
                    header = next(reader)
                except StopIteration:
                    continue
                rows = [r for _, r in zip(range(2000), reader)]
                # 人物の表（instance of が human＝Q5、生年月日・性別の列がある）は丸ごと使わない（人の名前を教材に入れない）
                low = [h.lower() for h in header]
                inst = low.index("instance of") if "instance of" in low else None
                if any(h in low for h in ("date of birth", "sex or gender", "date of death", "given name", "family name")) or (
                        inst is not None and sum("'Q5'" in (r[inst] if inst < len(r) else "") for r in rows) > len(rows) / 4):
                    stats["dropped_person_table"] = stats.get("dropped_person_table", 0) + 1
                    continue
                types = t.get("COLUMN_DATATYPES") or []
                cols = t.get("COLUMNS") or header
                for ci, h in enumerate(header):
                    dtype = types[ci] if ci < len(types) and len(cols) == len(header) else ""
                    if blocked_header(h):
                        stats["dropped_header"] = stats.get("dropped_header", 0) + 1
                        continue
                    vals = [parse_wikidbs_cell(r[ci]) for r in rows if ci < len(r)]
                    if any(sensitive_value(v) for v in vals):
                        stats["dropped_sensitive_values"] = stats.get("dropped_sensitive_values", 0) + 1
                        continue
                    values, distinct = pick_values(vals, f"{member}|{ci}")
                    if not values:
                        stats["empty"] = stats.get("empty", 0) + 1
                        continue
                    lab = f"{dtype}|{h}"
                    writer.write({"corpus": "wikidbs10k", "split": "train", "table": f"{info['INFO']['db_folder_name']}/{t['FILEPATH']}",
                                  "table_title": tname, "col": ci, "header": h[:60], "values": values, "distinct": distinct,
                                  "rows": len(rows), "context": [x[:40] for x in header if x != h][:20],
                                  "source_label": dtype, "source_kind": "Wikidata datatype (WikiDBs)"})
                    stats["labels"][dtype] = stats["labels"].get(dtype, 0) + 1


def cmd_convert(name, out_dir):
    import hashlib
    c = CORPORA[name]
    p = download(c["url"], WORK / name / "archive.zip")
    writer = Writer(out_dir)
    stats = {"labels": {}}
    {"sotab_v2": convert_sotab, "wikidbs10k": convert_wikidbs}[name](p, writer, stats)
    writer.close()
    out = Path(out_dir)
    manifest = {"corpus": name, "source_url": c["url"], "license": c["license"], "attribution": c["attribution"],
                "archive_bytes": p.stat().st_size, "columns": writer.n,
                "labels": dict(sorted(stats.pop("labels").items(), key=lambda x: -x[1])), "stats": stats,
                "files": {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(out.glob("part-*.jsonl.gz"))},
                "rules": ["元のアーカイブは commit しない", "値は 1 列 5 つまで・60 字まで", "test の分割は使わない",
                          "人の名前・メール・電話・番地の種類と、個人情報に見える値のある列は落とした（fetch_rows.py の決まり）",
                          "source_label は元のラベル。16 種への読み替えは別に決める（弱いラベル）。教材庫には先生 2 人の確認なしに入れない"]}
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / "ATTRIBUTION.md").write_text(f"# 出典\n\n- {c['attribution']}\n- ライセンス：{c['license']}（https://creativecommons.org/licenses/by/4.0/）\n"
                                        f"- 変更：元の表から列ごとに値を 5 つまで抜き出し、個人情報に見える列を除いた。\n", encoding="utf-8")
    print(name, writer.n, "columns")


def main(argv=None):
    argv = argv or sys.argv[1:]
    if argv[0] == "inspect":
        cmd_inspect(argv[1], argv[2])
    elif argv[0] == "convert":
        cmd_convert(argv[1], argv[2])
    else:
        raise SystemExit(f"知らない命令：{argv[0]}")


if __name__ == "__main__":
    main()
