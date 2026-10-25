"""封印セット #2 を作る（2026-10-25 Claude。specs/SEALED_EVAL_PROTOCOL.md 第 3・4 章 段 0）。

決まった規則だけで選ぶ（目で選ばない）。**値は開かない**：このスクリプトは値を表示しない。数えるのは見出し・表・公開元・言語だけ。

  adopt   eval2 の候補（materials/pool_discover.py --pool eval2 の出力）→ materials/pool/work/sealed2/adopted.json
          （取り出しは s11-fetch-rows.yml。教材庫と同じ道具・同じ個人情報の検査）
  freeze  取り出した corpus.jsonl → independent_eval/results/sealed2/sealed2.json（schema_version 1）と provenance.json。
          1 表 10 列まで・同じ見出しの組は 2 表まで・1 公開元は全体の 12% まで・見出しが学習にもある列は 20% 以下。
          並べる順は列の ID のハッシュだけで決める。凍結したら取り出しの corpus は消す（値の置き場を 1 つにする）

使い方：python independent_eval/sealed2.py adopt --candidates materials/pool/candidates_eval2_*.json
        python independent_eval/sealed2.py freeze
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "materials"))
sys.path.insert(0, str(ROOT))
from pipeline import ALLOWED_LICENSES, TITLE_DENY, known_resources, license_id, platform_of  # noqa: E402

SET_ID = "sealed2-20261025-v1"
WORK = ROOT / "materials" / "pool" / "work" / "sealed2"
OUT = ROOT / "independent_eval" / "results" / "sealed2"
SALT = "jitsuris-sealed2-v1"
TABLES_PER_PUBLISHER = 8      # 取り出し前の上限（取り出せない表があるので多めに採る。凍結で 12% に絞る）
COLS_PER_TABLE = 10
SAME_HEADERS_TABLES = 2
PUBLISHER_SHARE = 0.12
KNOWN_HEADER_SHARE = 0.20
MIN_COLUMNS = 600


def h(s):
    return hashlib.sha256(f"{SALT}|{s}".encode("utf-8")).hexdigest()


def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(s)).strip()).casefold()


def pools():
    pubs = json.load(open(ROOT / "independent_eval" / "allocation.json", encoding="utf-8"))["publishers"]
    return {p["publisher_id"]: p["pool"] for p in pubs}


def adopt(cands, pool_of, known_urls, known_rids, pool="eval2", per_publisher=None):
    """候補 → (採用, 落とした理由)。公開元ごとにハッシュの順で TABLES_PER_PUBLISHER 表まで（封印セット #3 は pool="eval3"、sealed3.py）。"""
    per_publisher = per_publisher or TABLES_PER_PUBLISHER
    why, per_pub, seen, out = Counter(), Counter(), set(), []
    for c in sorted(cands, key=lambda c: h(c.get("resource_id") or c.get("resource_url", ""))):
        url = c.get("resource_url") or ""
        rid = c.get("resource_id")
        pub = str(c.get("publisher_id", ""))
        reason = None
        if pool_of.get(pub) != pool or c.get("pool") != pool:
            reason = f"公開元が {pool} でない"
        elif license_id(c) not in ALLOWED_LICENSES:
            reason = "ライセンスが許可の一覧にない"
        elif TITLE_DENY.search(f"{c.get('title', '')} {c.get('resource_name', '')}"):
            reason = "題名が個人の記録になりやすい表"
        elif not c.get("datastore_available") and c.get("access") != "csv":
            reason = "datastore も CSV も無い"
        elif platform_of(c)[0] is None or not rid:
            reason = "取り出せる場でない"
        elif url in known_urls or rid in known_rids or rid in seen:
            reason = "学習側で使った表（URL・リソースの一致）"
        elif per_pub[pub] >= per_publisher:
            reason = f"1 公開元 {per_publisher} 表まで"
        if reason:
            why[reason] += 1
            continue
        seen.add(rid)
        per_pub[pub] += 1
        plat, host = platform_of(c)
        out.append({"n": len(out) + 1, "publisher_id": pub, "resource_url": url, "title": c.get("title", ""), "platform": plat,
                    "host": host, "resource_id": rid, "access": c.get("access") or ("datastore" if plat != "socrata" else "soda"),
                    "license": license_id(c)})
    return out, why


def training_headers():
    """学習側の見出し（本物の教材と教材庫。合成は数えない）。"""
    heads = set()
    for f in list((ROOT / "materials").glob("real_labels*.jsonl")) + list((ROOT / "materials" / "pool").glob("batch_*.jsonl")):
        for line in open(f, encoding="utf-8"):
            if line.strip():
                heads.add(norm(json.loads(line).get("header", "")))
    return heads


def is_ja(s):
    return bool(re.search(r"[぀-ヿ一-鿿]", s or ""))


def select(rows, train_heads):
    """corpus の行 → 選んだ行の番号の並び（表の順・表の中は corpus の順）と、数えた記録。値は見ない。"""
    by_table = defaultdict(list)
    for i, r in enumerate(rows):
        by_table[r["table"]].append(i)
    stats = Counter()
    # 1. 1 表 10 列まで（列の ID のハッシュの順）
    picked = {t: sorted(ix, key=lambda i: h(f"{t}|{rows[i]['header']}|{i}"))[:COLS_PER_TABLE] for t, ix in by_table.items()}
    # 2. 同じ見出しの組（表の全部の見出し）は 2 表まで
    tables = sorted(picked, key=h)
    hset_count, keep = Counter(), []
    for t in tables:
        key = frozenset(norm(rows[i]["header"]) for i in by_table[t])
        if hset_count[key] >= SAME_HEADERS_TABLES:
            stats["drop_same_headers"] += 1
            continue
        hset_count[key] += 1
        keep.append(t)
    # 3. 見出しが学習にもある列は 20% 以下：学習にある見出しの列を、全体の 20% を超える分だけハッシュの順で落とす
    cols = [i for t in keep for i in picked[t]]
    known = [i for i in cols if norm(rows[i]["header"]) in train_heads]
    unknown = [i for i in cols if norm(rows[i]["header"]) not in train_heads]
    allow_known = int(KNOWN_HEADER_SHARE * len(unknown) / (1 - KNOWN_HEADER_SHARE))
    known_kept = set(sorted(known, key=lambda i: h(f"k|{i}"))[:allow_known])
    stats["drop_known_header"] = len(known) - len(known_kept)
    cols = [i for i in cols if i in known_kept or norm(rows[i]["header"]) not in train_heads]
    # 4. 1 公開元は全体の 12% まで（大きい公開元から、表の単位で落とす）
    while True:
        n = len(cols)
        per_pub = Counter(rows[i]["publisher"] for i in cols)
        pub, top = per_pub.most_common(1)[0] if per_pub else (None, 0)
        if not n or top <= PUBLISHER_SHARE * n:
            break
        t_of_pub = sorted({rows[i]["table"] for i in cols if rows[i]["publisher"] == pub}, key=h)
        drop = t_of_pub[-1]
        cols = [i for i in cols if rows[i]["table"] != drop]
        stats["drop_publisher_share"] += 1
    order = {t: k for k, t in enumerate(keep)}
    cols.sort(key=lambda i: (order[rows[i]["table"]], i))
    return cols, stats


def cmd_adopt(a):
    if (WORK / "adopted.json").exists():
        raise SystemExit("adopted.json がもうある（採用は 1 回だけ）")
    cands = []
    for f in a.candidates:
        d = json.load(open(f, encoding="utf-8"))
        cands += d.get("selected") or []
    urls, rids = known_resources()
    adopted, why = adopt(cands, pools(), urls, rids)
    WORK.mkdir(parents=True, exist_ok=True)
    doc = {"schema_version": 1, "batch": "sealed2", "pool": "eval2", "set_id": SET_ID, "decided_by": "independent_eval/sealed2.py adopt（規則だけ）",
           "decided_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "candidates": [str(Path(f).as_posix()) for f in a.candidates],
           "candidate_count": len(cands), "dropped": dict(why), "adopted": adopted, "values_viewed": False}
    (WORK / "adopted.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"adopted {len(adopted)}/{len(cands)} tables from {len({x['publisher_id'] for x in adopted})} publishers; dropped {dict(why)}")


def cmd_freeze(a):
    corpus = WORK / "corpus.jsonl"
    rows = [json.loads(line) for line in open(corpus, encoding="utf-8") if line.strip()]
    adopted = {x["resource_url"]: x for x in json.load(open(WORK / "adopted.json", encoding="utf-8"))["adopted"]}
    pool_of = pools()
    bad = [r for r in rows if pool_of.get(r.get("publisher")) != "eval2"]
    if bad:
        raise SystemExit(f"eval2 でない公開元の行がある：{len(bad)}")
    cols, stats = select(rows, training_headers())
    if len(cols) < MIN_COLUMNS and not a.allow_small:
        raise SystemExit(f"選んだ列が {len(cols)}（{MIN_COLUMNS} 未満）。候補を足して取り出し直す")
    tables = sorted({rows[i]["table"] for i in cols}, key=lambda t: cols.index(next(i for i in cols if rows[i]["table"] == t)))
    tid = {t: f"t{k + 1:03d}" for k, t in enumerate(tables)}
    from encoder_context import unit_context_map  # noqa: E402
    units = unit_context_map([(r["header"], r["values"], "", r.get("context") or [], r["table"]) for r in rows])
    out_cols = []
    for k, i in enumerate(cols, 1):
        r = rows[i]
        out_cols.append({"id": f"s2-{k:04d}", "table": tid[r["table"]], "source": r["publisher"], "language": r.get("language", "ja"),
                         "header": r["header"], "values": r["values"][:5] or [""], "siblings": r.get("context") or [],
                         "unit": units.get(r["table"], "")})
    data = {"schema_version": 1, "set_id": SET_ID, "columns": out_cols}
    OUT.mkdir(parents=True, exist_ok=True)
    set_path = OUT / "sealed2.json"
    set_path.write_text(json.dumps(data, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    sha = hashlib.sha256(set_path.read_bytes()).hexdigest()
    sel = [rows[i] for i in cols]
    ja = sum(is_ja(r["header"]) or r.get("language") == "ja" for r in sel)
    th = training_headers()
    prov = {"schema_version": 1, "set_id": SET_ID, "frozen_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "set_path": "independent_eval/results/sealed2/sealed2.json", "set_sha256": sha,
            "column_count": len(cols), "table_count": len(tables), "publisher_count": len({r["publisher"] for r in sel}),
            "language": dict(Counter(r.get("language", "?") for r in sel)), "japanese_share": round(ja / len(sel), 4) if sel else 0,
            "known_header_share": round(sum(norm(r["header"]) in th for r in sel) / len(sel), 4) if sel else 0,
            "max_publisher_share": round(max(Counter(r["publisher"] for r in sel).values()) / len(sel), 4) if sel else 0,
            "selection": dict(stats), "corpus_sha256": hashlib.sha256(corpus.read_bytes()).hexdigest(),
            "labels_written": False, "values_viewed": False, "blind_sets_read": False, "raw_source_files_written": False,
            "tables": [{"table_id": tid[t], "publisher": next(r["publisher"] for r in sel if r["table"] == t), "resource_url": t,
                        "title": adopted.get(t, {}).get("title", ""), "license": next(r.get("license", "") for r in sel if r["table"] == t)}
                       for t in tables]}
    (OUT / "provenance.json").write_text(json.dumps(prov, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in prov.items() if k != "tables"}, ensure_ascii=False))


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("adopt"); p.add_argument("--candidates", nargs="+", required=True)
    p = sub.add_parser("freeze"); p.add_argument("--allow-small", action="store_true")
    a = ap.parse_args(argv)
    {"adopt": cmd_adopt, "freeze": cmd_freeze}[a.cmd](a)


if __name__ == "__main__":
    main()
