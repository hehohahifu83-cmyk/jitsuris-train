"""G4（方法 T1 を測る未使用の海外の陣）を作る（2026-11-18 Claude。independent_eval/g3.py を元に書き直した）。
事前記録：bench/g4_prereg_20261118.md（凍結版）。**値は開かない**：このスクリプトは値を表示しない。

  adopt    候補（materials/pool_discover.py --national --pool hold --only-national open.alberta.ca --only-national ckan.govdata.de、語で絞らない）
           → materials/pool/work/g4/adopted.json（採用・控え・落とした理由）
  reserve  1 回目の取り出し（g4/corpus.jsonl・corpus_log.json）で行が取れなかった表だけ、同じ公開元の控えの 1 番目で置き換える
           → materials/pool/work/g4x/adopted.json（1 回だけ。控えも取れなければそこで打ち切り）
  freeze   corpus（g4 と g4x）→ independent_eval/results/g4/g4.json・provenance.json（row_context・row_context_none つき）
  verify   凍結したセットを corpus から作り直し、row_context と除外の決まりが合うかを確かめる（値は表示しない）

採用の決まり（順に、機械的に一意。先生のラベルや金額の多さでは選ばない）：
  1. 候補を落とす：公開元が hold でない／カタログが Alberta・GovData.de でない／G1〜G3 で表を採った公開元（USED_PROVENANCE の publisher）／
     ライセンスが許可の一覧にない／題名が個人の記録になりやすい（pipeline.TITLE_DENY）／datastore も同じ場の CSV も無い／取り出せる場でない／
     使い済みの資源（used_resources：pipeline.known_resources と同じ範囲から封印の陣を除いたもの）／使い済みのデータセット（(ホスト, dataset の名前) の組）
  2. 残りを h(resource_id) の小さい順に並べる。同じ値なら resource_url の文字の順（resource_id の無い候補は 1. で「取り出せる場でない」として落とす）
  3. 同じデータセット（(ホスト, dataset の名前)）は最初の 1 表だけ
  4. 公開元ごとに先頭 TABLES_PER_PUBLISHER 表を採用、次の RESERVES_PER_PUBLISHER 表を控え
  5. 採用が MAX_TABLES を超えたら、h(resource_url) の小さい順に MAX_TABLES 表だけ残す（外れた表は控えにしない）
凍結の決まり：1 表 COLS_PER_TABLE 列まで（h(表|列名|corpus の番号) の順）、同じ列名の組（norm の集合）の表は SAME_HEADERS_TABLES まで（h(表) の順）。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

# 2026-11-19 Codex の点検 P0-1：封印セットの道具（sealed2・sealed3）を import しない・その adopted を開かない。
# 封印セットの表は eval2・eval3 のプールの公開元だけから採っている（allocation.json の pool）。G4 は hold の公開元だけを使うので、
# 公開元のプールの分け方で重ならない（資源の照合はしない。限界として事前記録に書く）。
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "materials"))
sys.path.insert(0, str(ROOT))
import encoder_context as EC  # noqa: E402
from pipeline import ACCESS_ERRORS, ALLOWED_LICENSES, TITLE_DENY, license_id, platform_of  # noqa: E402

SET_ID = "g4-20261118-v1"
POOL = "hold"
WORK = ROOT / "materials" / "pool" / "work" / "g4"
WORK_X = ROOT / "materials" / "pool" / "work" / "g4x"
OUT = ROOT / "independent_eval" / "results" / "g4"
SALT = "jitsuris-g4-v1"
CATALOGS = ("alberta_cat", "govdata_cat")
TABLES_PER_PUBLISHER = 3
RESERVES_PER_PUBLISHER = 2
MAX_TABLES = 300
COLS_PER_TABLE = 10
SAME_HEADERS_TABLES = 2
USED_PROVENANCE = ("independent_eval/results/g1/provenance.json", "independent_eval/results/g2/provenance.json",
                   "independent_eval/results/g3/provenance.json")
USED_WORKS = ("f1", "g1", "g1x", "g2", "g2x", "g3", "g3x")   # 開いてよい（凍結・採点の済んだ）陣の adopted だけ
NONE_REASONS = {"列が無い", "同じ列名が 2 つ以上", "row_index が空の列がある", "列ごとに row_index が違う", "同じ行番号の重複",
                "row_values と row_index の長さが違う"}


def h(s):
    return hashlib.sha256(f"{SALT}|{s}".encode("utf-8")).hexdigest()


def norm(s):
    """列名の正規化（封印セットの道具の norm と同じ式。封印の道具を import しないために写した）。"""
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(s)).strip()).casefold()


def pools():
    pubs = json.load(open(ROOT / "independent_eval" / "allocation.json", encoding="utf-8"))["publishers"]
    return {p["publisher_id"]: p["pool"] for p in pubs}


def sha_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def norm_pub(p):
    sys.path.insert(0, str(ROOT / "independent_eval"))
    import allocation as A
    return A.normalize_publisher_id(str(p))


def dataset_key(url):
    """(ホスト, dataset の名前)。CKAN の資源の URL（…/dataset/<名前>/resource/…）から。取れなければ None。"""
    u = urlparse(str(url or ""))
    m = re.search(r"/dataset/([^/]+)", u.path)
    return (u.hostname or "", m.group(1)) if m else None


def used_publishers():
    pubs = set()
    for f in USED_PROVENANCE:
        pubs |= {norm_pub(t["publisher"]) for t in json.load(open(ROOT / f, encoding="utf-8"))["tables"]}
    return pubs


SEALED_WORKS = ("sealed2", "sealed3", "b018")   # 封印の陣：開かない（名前が blind で始まる作業ディレクトリも開かない）


def _read_jsonl(path):
    return [json.loads(line) for line in open(path, encoding="utf-8") if line.strip()]


def used_resources():
    """使い済みの資源（URL・resource_id）とデータセットの組。pipeline.known_resources と同じ範囲から、封印の陣だけを除いて読む
    （学習の教材・教材庫・主セットの provenance・封印でない作業ディレクトリの adopted.json・S11 の adopted）。
    取り出しで届かなかった表（corpus_log の ACCESS_ERRORS）は使っていないので数えない（pipeline と同じ）。"""
    urls, rids = set(), set()
    for f in sorted((ROOT / "materials").glob("real_*.jsonl")) + sorted((ROOT / "materials" / "pool").glob("batch_*.jsonl")):
        for r in _read_jsonl(f):
            urls.update({r.get("table", ""), r.get("resource_page", "")})
    prov = ROOT / "independent_eval" / "results" / "main" / "provenance.json"
    if prov.exists():
        for t in json.load(open(prov, encoding="utf-8")).get("tables", []):
            urls.update({t.get("resource_url", ""), t.get("request_url", "")})
    works = [d for d in sorted((ROOT / "materials" / "pool" / "work").iterdir())
             if d.is_dir() and d.name not in SEALED_WORKS and not d.name.startswith("blind") and d.name not in ("g4", "g4x")]
    for f in [d / "adopted.json" for d in works] + sorted((ROOT / "materials").glob("s11_*_adopted_*.json")):
        if not f.exists():
            continue
        log = f.with_name("corpus_log.json")
        failed = set()
        if log.exists():
            failed = {t.get("resource_url") for t in json.load(open(log, encoding="utf-8")).get("tables", [])
                      if t.get("status") == "error" and re.search(ACCESS_ERRORS, t.get("error", ""))}
        for x in json.load(open(f, encoding="utf-8")).get("adopted", []):
            if x.get("resource_url") not in failed:
                urls.add(x.get("resource_url", ""))
                rids.add(x.get("resource_id"))
    urls.discard("")
    rids.discard(None)
    datasets = {k for k in (dataset_key(u) for u in urls) if k}
    return urls, rids, datasets


def adopt_rule(cands, pool_of, used_pubs, known_urls, known_rids, known_datasets):
    """候補 → (採用, 控え（公開元 → 並び）, 落とした理由の数)。上の決まり 1〜5 の順。"""
    why, ok = Counter(), []
    for c in cands:
        url, rid, pub = c.get("resource_url") or "", c.get("resource_id"), norm_pub(c.get("publisher_id", ""))
        reason = None
        if pool_of.get(c.get("publisher_id")) != POOL or c.get("pool") != POOL:
            reason = "公開元が hold でない"
        elif pub.split(":")[0] not in CATALOGS:
            reason = "カタログが Alberta・GovData.de でない"
        elif pub in used_pubs:
            reason = "G1〜G3 で表を採った公開元"
        elif license_id(c) not in ALLOWED_LICENSES:
            reason = "ライセンスが許可の一覧にない"
        elif TITLE_DENY.search(f"{c.get('title', '')} {c.get('resource_name', '')}"):
            reason = "題名が個人の記録になりやすい表"
        elif not c.get("datastore_available") and c.get("access") != "csv":
            reason = "datastore も CSV も無い"
        elif platform_of(c)[0] is None or not rid:
            reason = "取り出せる場でない"
        elif url in known_urls or rid in known_rids:
            reason = "使い済みの資源"
        elif dataset_key(url) in known_datasets:
            reason = "使い済みのデータセット"
        if reason:
            why[reason] += 1
        else:
            ok.append(c)
    ok.sort(key=lambda c: (h(c["resource_id"]), c.get("resource_url", "")))
    seen_ds, per_pub, adopted, reserves = set(), Counter(), [], defaultdict(list)
    for c in ok:
        ds = dataset_key(c.get("resource_url")) or ("", c.get("resource_url"))
        if ds in seen_ds:
            why["同じデータセットの 2 つ目より後"] += 1
            continue
        seen_ds.add(ds)
        pub = norm_pub(c["publisher_id"])
        plat, host = platform_of(c)
        rec = {"publisher_id": c["publisher_id"], "resource_url": c["resource_url"], "title": c.get("title", ""), "platform": plat, "host": host,
               "resource_id": c["resource_id"], "access": c.get("access") or "datastore", "license": license_id(c)}
        if per_pub[pub] < TABLES_PER_PUBLISHER:
            per_pub[pub] += 1
            adopted.append(rec)
        elif len(reserves[pub]) < RESERVES_PER_PUBLISHER:
            reserves[pub].append(rec)
        else:
            why[f"1 公開元 {TABLES_PER_PUBLISHER} 表＋控え {RESERVES_PER_PUBLISHER} 表まで"] += 1
    if len(adopted) > MAX_TABLES:
        keep = {x["resource_url"] for x in sorted(adopted, key=lambda x: (h(x["resource_url"]), x["resource_url"]))[:MAX_TABLES]}
        why[f"全体で {MAX_TABLES} 表まで"] += len(adopted) - MAX_TABLES
        adopted = [x for x in adopted if x["resource_url"] in keep]
    adopted = [dict(x, n=str(k + 1)) for k, x in enumerate(adopted)]
    pubs_in = {norm_pub(x["publisher_id"]) for x in adopted}
    reserves = {p: r for p, r in reserves.items() if p in pubs_in}
    return adopted, reserves, why


def cmd_adopt(a):
    out = WORK / "adopted.json"
    if out.exists():
        raise SystemExit("adopted.json がもうある（採用は 1 回だけ）")
    cands = []
    for f in a.candidates:
        cands += json.load(open(f, encoding="utf-8")).get("selected") or []
    urls, rids, datasets = used_resources()
    adopted, reserves, why = adopt_rule(cands, pools(), used_publishers(), urls, rids, datasets)
    WORK.mkdir(parents=True, exist_ok=True)
    doc = {"schema_version": 1, "batch": "g4", "pool": POOL, "set_id": SET_ID, "decided_by": "independent_eval/g4.py adopt（規則だけ）",
           "decided_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "candidates": [str(Path(f).as_posix()) for f in a.candidates],
           "candidates_sha256": {str(Path(f).as_posix()): sha_file(f) for f in a.candidates},
           "used_provenance_sha256": {f: sha_file(ROOT / f) for f in USED_PROVENANCE}, "used_publishers": len(used_publishers()),
           "candidate_count": len(cands), "dropped": dict(why), "adopted": adopted, "reserves": reserves, "values_viewed": False}
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"adopted {len(adopted)}/{len(cands)} tables from {len({x['publisher_id'] for x in adopted})} publishers; dropped {dict(why)}")


def fetched_pages(work):
    """取り出せた表の resource_page（corpus.jsonl に行がある資源。採用の resource_url と同じもの）。"""
    p = work / "corpus.jsonl"
    return {r.get("resource_page") or r["table"] for r in _read_jsonl(p)} if p.exists() else set()


def expected_reserves(first, got_pages):
    """控えの置き換えの決まり（reserve と照合で同じ関数）：1 回目の採用の順に、取れなかった表ごとに、同じ公開元の控えを先頭から 1 つずつ。
    控えが尽きた公開元はそこで打ち切り。返すのは g4x の採用の記録の並び（控えの記録そのもの＋n＋replaces）と取れなかった表の数。"""
    failed = [x for x in first["adopted"] if x["resource_url"] not in got_pages]
    used, new = Counter(), []
    for x in failed:
        pub = norm_pub(x["publisher_id"])
        res = first["reserves"].get(pub) or []
        if used[pub] < len(res):
            new.append(dict(res[used[pub]], n=str(len(first["adopted"]) + len(new) + 1), replaces=x["resource_url"]))
            used[pub] += 1
    return new, len(failed)


def cmd_reserve(a):
    """1 回目に取れなかった表だけを、同じ公開元の控えで置き換える（1 回だけ。控えも取れなければ打ち切り）。"""
    out = WORK_X / "adopted.json"
    if out.exists():
        raise SystemExit("g4x/adopted.json がもうある（1 回だけ）")
    first = json.load(open(WORK / "adopted.json", encoding="utf-8"))
    new, failed = expected_reserves(first, fetched_pages(WORK))
    doc = {"schema_version": 1, "batch": "g4", "pool": POOL, "set_id": SET_ID, "decided_by": "independent_eval/g4.py reserve（規則だけ）",
           "decided_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "failed": failed, "adopted": new, "values_viewed": False}
    WORK_X.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"failed {failed}; reserves {len(new)}")


def select(rows):
    """corpus の行 → 選んだ行の番号（表の順・表の中は corpus の順）と数えた記録。値は見ない。"""
    by_table = defaultdict(list)
    for i, r in enumerate(rows):
        by_table[r["table"]].append(i)
    stats = Counter()
    picked = {t: sorted(ix, key=lambda i: h(f"{t}|{rows[i]['header']}|{i}"))[:COLS_PER_TABLE] for t, ix in by_table.items()}
    stats["drop_over_10_columns"] = sum(len(ix) - len(picked[t]) for t, ix in by_table.items())
    keep, hset = [], Counter()
    for t in sorted(picked, key=lambda t: (h(t), t)):
        key = frozenset(norm(rows[i]["header"]) for i in by_table[t])
        if hset[key] >= SAME_HEADERS_TABLES:
            stats["drop_same_headers"] += 1
            continue
        hset[key] += 1
        keep.append(t)
    order = {t: k for k, t in enumerate(keep)}
    cols = sorted((i for t in keep for i in picked[t]), key=lambda i: (order[rows[i]["table"]], i))
    return cols, stats


def adopted_entries(first=None, x_doc=None, g4_pages=None):
    """g4 と g4x の採用（resource_url → 記録）。2026-11-19 Codex の再点検 1：g4x の採用は、1 回目の採用・控え・1 回目に取れた表から
    `expected_reserves` が一通りに作るものと、記録の全部（resource_url・resource_id・publisher_id・platform・host・access・license・題名・n・replaces）が
    同じでなければ止まる（同じ元の 2 回の置き換え・控えの記録の書き換え・取れていた表の置き換えを拒否する）。
    corpus の行は resource_id を持たないので、資源の同一性は「corpus の resource_page ＝ この照合を通った採用の resource_url」でたどる。"""
    first = first if first is not None else json.load(open(WORK / "adopted.json", encoding="utf-8"))
    ent = {x["resource_url"]: dict(x, batch="g4") for x in first["adopted"]}
    if len(ent) != len(first["adopted"]):
        raise SystemExit("g4 の採用に同じ資源が 2 つある")
    if x_doc is None and (WORK_X / "adopted.json").exists():
        x_doc = json.load(open(WORK_X / "adopted.json", encoding="utf-8"))
    if x_doc is not None:
        got = g4_pages if g4_pages is not None else fetched_pages(WORK)
        want, failed = expected_reserves(first, got)
        if x_doc.get("adopted") != want or x_doc.get("failed") != failed:
            raise SystemExit("g4x の採用が、控えの決まりで作り直したものと違う")
        for x in want:
            if x["resource_url"] in ent:
                raise SystemExit("g4x の表が g4 の採用と重なる")
            ent[x["resource_url"]] = dict(x, batch="g4x")
    return ent


def check_corpus(rows, ent):
    """corpus の表を採用に全部結びつける（2026-11-19 Codex の点検 P0-3）。余分・重複・公開元の違い・取り出しの違い・
    置き換えたのに元も入っている、を拒否。採用したのに取れなかった表の数を返す。"""
    by_page = defaultdict(set)
    for r in rows:
        by_page[r.get("resource_page") or r["table"]].add((r["table"], r["publisher"], r.get("batch_src")))
    for page, items in by_page.items():
        if page not in ent:
            raise SystemExit("corpus に採用していない表がある")
        if len({t for t, _, _ in items}) != 1:
            raise SystemExit("同じ採用の資源が corpus に 2 つの表として入っている")
        if any(norm_pub(p) != norm_pub(ent[page]["publisher_id"]) for _, p, _ in items):
            raise SystemExit("corpus の表の公開元が採用と違う")
        if any(b != ent[page]["batch"] for _, _, b in items):
            raise SystemExit("corpus の表が採用と別の取り出しから来ている")
    tables = [next(iter(v))[0] for v in by_page.values()]
    if len(tables) != len(set(tables)):
        raise SystemExit("別の採用の資源が同じ表になっている")
    for page, e in ent.items():
        if e["batch"] == "g4x" and e["replaces"] in by_page:
            raise SystemExit("置き換えた元の表も corpus に入っている")
    return sum(1 for p in ent if p not in by_page)


def load_rows():
    rows = [dict(r, batch_src="g4") for r in _read_jsonl(WORK / "corpus.jsonl")]
    extra = WORK_X / "corpus.jsonl"
    if extra.exists():
        rows += [dict(r, batch_src="g4x") for r in _read_jsonl(extra)]
    for r in rows:
        r["header"] = str(r["header"]).lstrip("\ufeff")
    return rows


def build_set(rows):
    """corpus の行 → (セット, provenance の中身)。row_context はセットのその表の列（セットの順）だけで作る（許可された列の集合＝セットの列）。
    単位の欄もセットの列だけから作る（落とした列の値を戻さない）。"""
    cols, stats = select(rows)
    first = {}
    for k, i in enumerate(cols):
        first.setdefault(rows[i]["table"], k)
    tables = sorted(first, key=first.get)
    tid = {t: f"t{k + 1:03d}" for k, t in enumerate(tables)}
    sel = [rows[i] for i in cols]
    units = EC.unit_context_map([(r["header"], r["values"], "", r.get("context") or [], r["table"]) for r in sel])
    out_cols = []
    for k, r in enumerate(sel, 1):
        out_cols.append({"id": f"g4-{k:04d}", "table": tid[r["table"]], "source": r["publisher"], "language": r.get("language", ""),
                         "header": r["header"], "values": r["values"][:5] or [""], "siblings": r.get("context") or [],
                         "unit": units.get(r["table"], "")})
    by_t = defaultdict(list)
    for r in sel:
        by_t[r["table"]].append(r)
    row_context, row_context_none, row_index_sha = {}, {}, {}
    for t in tables:
        ctx, why = EC.table_row_context(t, by_t[t])
        if ctx is None:
            row_context_none[tid[t]] = why
        else:
            row_context[tid[t]] = ctx
        row_index_sha[tid[t]] = hashlib.sha256(json.dumps([r.get("row_index") for r in by_t[t]]).encode("utf-8")).hexdigest()
    doc = {"schema_version": 1, "set_id": SET_ID, "columns": out_cols, "row_context": row_context, "row_context_none": row_context_none}
    meta = {"stats": dict(stats), "tables": tables, "tid": tid, "row_index_sha256": row_index_sha,
            "row_context_version": EC.ROWCTX_VERSION, "row_context_none_reasons": dict(Counter(row_context_none.values())),
            "row_context_sha256": hashlib.sha256(json.dumps(row_context, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()}
    return doc, meta, sel


def check_context_values(doc, sel):
    """文脈の値が、セットのその表のその列の corpus の行の値の中にあるか（別の表の同じ名前の列を混ぜない。Codex の点検）。
    sel：セットの列と同じ順の corpus の行。"""
    if len(sel) != len(doc["columns"]):
        raise SystemExit("セットの列と corpus の行の数が違う")
    vals = defaultdict(set)
    for c, r in zip(doc["columns"], sel):
        vals[(c["table"], c["header"])].update(str(v) for v in r.get("row_values") or [])
    for t, ctx in doc["row_context"].items():
        for row in ctx["rows"]:
            for hd, v in zip(ctx["headers"], row):
                if v not in vals[(t, hd)]:
                    raise SystemExit("row_context にセットのその表のその列の行に無い値がある")


def check_set(doc, rows):
    """凍結したセットを corpus から作り直して照合する（値は表示しない）。違えば SystemExit。"""
    again, _, sel = build_set(rows)
    if again != doc:
        raise SystemExit("セットを corpus から作り直したものと凍結したものが違う")
    tables = {c["table"] for c in doc["columns"]}
    if set(doc["row_context"]) & set(doc["row_context_none"]) or set(doc["row_context"]) | set(doc["row_context_none"]) != tables:
        raise SystemExit("どの表も row_context か row_context_none のどちらか 1 つだけ、になっていない")
    bad = {v for v in doc["row_context_none"].values() if v not in NONE_REASONS}
    if bad:
        raise SystemExit(f"row_context_none の理由が決まった一覧にない：{len(bad)} 種")
    heads = defaultdict(list)
    for c in doc["columns"]:
        heads[c["table"]].append(c["header"])
    for t, ctx in doc["row_context"].items():
        if ctx["headers"] != heads[t]:
            raise SystemExit(f"{t}：文脈の列がセットの列と違う")
        for h_ in ctx["headers"]:
            EC.check_row_context(ctx, h_)
    # セットの列にない値が row_context に入っていない（文脈の値は、そのセットの列の corpus の row_values の中の値だけ）
    check_context_values(doc, sel)
    return True


TIME_FIELDS = ("frozen_utc",)   # provenance の中で、作り直して一致を求めない項目（時刻だけ）


def build_artifacts(rows, ent):
    """凍結の 3 つの中身（セット・provenance（時刻を除く）・題名）を、corpus の行と照合済みの採用から一通りに作る。"""
    pool_of = pools()
    used = used_publishers()
    bad = [r for r in rows if pool_of.get(r.get("publisher")) != POOL or norm_pub(r.get("publisher")) in used
           or norm_pub(r.get("publisher")).split(":")[0] not in CATALOGS]
    if bad:
        raise SystemExit(f"G4 の公開元でない行がある：{len(bad)}")
    missing = check_corpus(rows, ent)
    doc, meta, sel = build_set(rows)
    body = json.dumps(doc, ensure_ascii=False, indent=0) + "\n"
    page = {r["table"]: r.get("resource_page") or r["table"] for r in sel}
    corpus, extra = WORK / "corpus.jsonl", WORK_X / "corpus.jsonl"
    prov = {"schema_version": 1, "set_id": SET_ID,
            "set_path": "independent_eval/results/g4/g4.json", "set_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
            "column_count": len(doc["columns"]), "table_count": len(meta["tables"]), "publisher_count": len({r["publisher"] for r in sel}),
            "adopted_tables": len(ent), "adopted_not_fetched": missing,
            "columns_per_catalog": dict(Counter(norm_pub(r["publisher"]).split(":")[0] for r in sel)),
            "tables_per_catalog": dict(Counter(norm_pub(next(r["publisher"] for r in sel if r["table"] == t)).split(":")[0] for t in meta["tables"])),
            "selection": meta["stats"], "corpus_sha256": sha_file(corpus) if corpus.exists() else None,
            "corpus_extra_sha256": sha_file(extra) if extra.exists() else None,
            "row_context_version": meta["row_context_version"], "row_context_sha256": meta["row_context_sha256"],
            "row_context_tables": len(doc["row_context"]), "row_context_none_reasons": meta["row_context_none_reasons"],
            "row_index_sha256": meta["row_index_sha256"],
            "labels_written": False, "values_viewed": False, "predictions_made": False,
            "tables": [{"table_id": meta["tid"][t], "publisher": next(r["publisher"] for r in sel if r["table"] == t), "resource_url": t,
                        "resource_page": page[t], "title": (ent.get(page[t]) or {}).get("title", ""),
                        "license": next(r.get("license", "") for r in sel if r["table"] == t)} for t in meta["tables"]]}
    titles = {x["table_id"]: x["title"] for x in prov["tables"] if x["title"]}
    return doc, body, prov, titles


def check_artifacts(out_dir, rows, ent):
    """凍結の 3 つのファイル（g4.json・provenance.json・titles.json）を全部、作り直したものと照合する（Codex の再点検 2）。
    provenance は時刻（TIME_FIELDS）だけを除いて一致、時刻は空でない文字列。g4.json はバイトの SHA も provenance と一致。"""
    doc, body, prov, titles = build_artifacts(rows, ent)
    raw = (out_dir / "g4.json").read_bytes()
    if raw.decode("utf-8") != body or hashlib.sha256(raw).hexdigest() != prov["set_sha256"]:
        raise SystemExit("g4.json が作り直したものと違う")
    got_prov = json.loads((out_dir / "provenance.json").read_text(encoding="utf-8"))
    if not isinstance(got_prov, dict) or any(not isinstance(got_prov.get(k), str) or not got_prov.get(k) for k in TIME_FIELDS):
        raise SystemExit("provenance.json の時刻が無い")
    if {k: v for k, v in got_prov.items() if k not in TIME_FIELDS} != prov:
        raise SystemExit("provenance.json が作り直したものと違う")
    if json.loads((out_dir / "titles.json").read_text(encoding="utf-8")) != titles:
        raise SystemExit("titles.json が作り直したものと違う")
    check_set(json.loads(raw), rows)
    return prov


def freeze_to(out_dir, rows, ent):
    """凍結の 3 つのファイルを out_dir に作る（out_dir はまだ無い場所）。作ったあと、3 つ全部を作り直したものと照合する。"""
    doc, body, prov, titles = build_artifacts(rows, ent)
    out_dir.mkdir(parents=True)
    (out_dir / "g4.json").write_text(body, encoding="utf-8")
    full = {"schema_version": prov["schema_version"], "set_id": prov["set_id"], "frozen_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            **{k: v for k, v in prov.items() if k not in ("schema_version", "set_id")}}
    (out_dir / "provenance.json").write_text(json.dumps(full, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out_dir / "titles.json").write_text(json.dumps(titles, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    check_artifacts(out_dir, rows, ent)
    return full


def atomic_freeze(out, rows, ent):
    """2026-11-19 Codex の点検 P0-2：出力の場所があれば止める（上書きしない）。同じ場所の一時ディレクトリに作り、全部の照合が通ったあとで
    rename する（同じファイルシステムの中なので一度に入れ替わる）。失敗したら一時ディレクトリを消し、出力の場所には何も残さない。"""
    if out.exists():
        raise SystemExit(f"凍結の出力がもうある：{out}（上書きしない）")
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix=".g4_freeze_", dir=out.parent))
    try:
        prov = freeze_to(tmp / "set", rows, ent)
        os.rename(tmp / "set", out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return prov


def cmd_freeze(a):
    prov = atomic_freeze(OUT, load_rows(), adopted_entries())
    print(json.dumps({k: v for k, v in prov.items() if k not in ("tables", "row_index_sha256")}, ensure_ascii=False))


def cmd_verify(a):
    check_artifacts(OUT, load_rows(), adopted_entries())
    print("ok")


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("adopt")
    p.add_argument("--candidates", nargs="+", required=True)
    sub.add_parser("reserve")
    sub.add_parser("freeze")
    sub.add_parser("verify")
    a = ap.parse_args(argv)
    {"adopt": cmd_adopt, "reserve": cmd_reserve, "freeze": cmd_freeze, "verify": cmd_verify}[a.cmd](a)


if __name__ == "__main__":
    main()
