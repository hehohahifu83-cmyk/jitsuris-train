"""教材庫（materials/pool/）に、陣ごとに教材を貯める道具（2026-10-22 Claude。オーナー指示「少しずつ教材を貯めて一気に学習させたい」）。

流れ（1 陣＝1 つの batch ID。作業の置き場は materials/pool/work/<ID>/）：
  1. adopt     ChatGPT の候補一覧（JSON の selected）から、決まった規則で採用する → work/<ID>/adopted.json
  2. （Actions）fetch_rows.py で値を取り出す → work/<ID>/corpus.jsonl
  3. （Actions）corpus_to_set.py ＋ 今のモデルで予測 → work/<ID>/set.json・pred_e5base_seed1.json
  4. （ChatGPT）全列にラベル → work/<ID>/labels_chatgpt.jsonl（corpus と同じ順、{table, header, label, teacher}）
  5. reconcile 先生とモデルを突き合わせる。一致は自動で採用。食い違いは優先度の高い順に最大 500 列を Claude の裁定へ、残りは捨てる。
               一致の 5%（最少 10 列）を Claude の抜き取りへ → work/<ID>/review.jsonl
  6. （Claude）work/<ID>/decisions.jsonl に {"i": 行番号, "label": …, "reason": …} を書く（review の to_review と audit の全部）
  7. finalize  抜き取りの誤り率が 5% を超えたら止める。通れば pool/batch_<ID>.jsonl（unknown・S を除く）と台帳 pool/manifest.json
  status       教材庫の合計と目標までの残り
学習（encoder_exp の FT_POOL=1）は教材庫の batch_*.jsonl をまとめて読む。値は公開データだけ。ラベルの根拠は LABEL_GUIDE.md だけ。

使い方：python materials/pipeline.py adopt --batch <ID> --candidates <一覧.json> [<一覧.json> …]
        python materials/pipeline.py reconcile --batch <ID>
        python materials/pipeline.py finalize --batch <ID>
        python materials/pipeline.py status [--out bench/pool_status.md]
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import random
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POOL = ROOT / "materials" / "pool"
LABELS = ("account", "address", "amount", "category", "date", "email", "id", "org", "other", "person", "phone",
          "product", "quantity", "rate", "tax_class", "text")
NOT_USED = ("unknown", "S")
ALLOWED_LICENSES = {"cc-by-4.0", "cc-by-40-intl", "cc-by", "cc-zero", "cc0", "cc0-1.0", "odc-by", "ogl-uk-3.0"}
PER_PUBLISHER_BATCH = 3      # 1 陣で 1 公開元あたりの表
PER_PUBLISHER_POOL = 15      # 教材庫全体で 1 公開元あたりの表（系統の偏りを抑える）
SAME_HEADERS_PER_PUBLISHER = 3   # 同じ公開元で見出しの組が同じ表（DATA_COLLECTION_PROTOCOL 第 2 章）
REVIEW_LIMIT = 500           # Claude の裁定は 1 陣 500 列まで（同 第 6 章の 4）
AUDIT_RATE, AUDIT_MIN = 0.05, 10
AUDIT_MAX_ERROR = 0.05
TARGET_COLUMNS = 22000       # 第 1 目標：教材庫の学習に使える列（既存の本物 約 11,000 列と合わせて約 3 倍）。オーナーが変えてよい
CRITICAL = {"date", "amount", "quantity", "rate", "id"}
RARE = {"person", "product", "tax_class", "phone", "email", "account", "org", "text"}


def work(batch):
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{1,30}", batch):
        raise SystemExit("batch ID は英小文字・数字・_・- だけ（例 b003）")
    return POOL / "work" / batch


def read_jsonl(path):
    return [json.loads(line) for line in open(path, encoding="utf-8") if line.strip()]


def write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def manifest():
    p = POOL / "manifest.json"
    return json.load(open(p, encoding="utf-8")) if p.exists() else {"schema_version": 1, "target_columns": TARGET_COLUMNS, "batches": []}


def save_manifest(m):
    POOL.mkdir(parents=True, exist_ok=True)
    (POOL / "manifest.json").write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- 1. 採用

def known_resources():
    """もう使った表：学習の教材・教材庫・主セット・前の陣の採用。URL と resource ID の両方で見る。"""
    urls, rids = set(), set()
    for f in glob.glob(str(ROOT / "materials" / "real_*.jsonl")) + glob.glob(str(POOL / "batch_*.jsonl")):
        for r in read_jsonl(f):
            urls.update({r.get("table", ""), r.get("resource_page", "")})
    prov = ROOT / "independent_eval" / "results" / "main" / "provenance.json"
    if prov.exists():
        for t in json.load(open(prov, encoding="utf-8")).get("tables", []):
            urls.update({t.get("resource_url", ""), t.get("request_url", "")})
    for f in glob.glob(str(POOL / "work" / "*" / "adopted.json")) + glob.glob(str(ROOT / "materials" / "s11_*_adopted_*.json")):
        for a in json.load(open(f, encoding="utf-8")).get("adopted", []):
            urls.add(a.get("resource_url", ""))
    for u in list(urls):
        m = re.search(r"/resource/([0-9a-f-]{36})", u or "")
        if m:
            rids.add(m.group(1))
    urls.discard("")
    return urls, rids


def pool_publisher_tables():
    c = Counter()
    for f in glob.glob(str(POOL / "batch_*.jsonl")):
        c.update(Counter(r["publisher"] for r in {r["table"]: r for r in read_jsonl(f)}.values()))
    return c


def pool_header_sets():
    sets = Counter()
    for f in glob.glob(str(POOL / "batch_*.jsonl")):
        by = {}
        for r in read_jsonl(f):
            by.setdefault((r["publisher"], r["table"]), []).append(r["header"])
        for (pub, _), hs in by.items():
            sets[(pub, frozenset(hs))] += 1
    return sets


def license_id(c):
    lic = c.get("license")
    return str((lic.get("id") if isinstance(lic, dict) else lic) or c.get("license_id") or "").strip().lower()


def adopt(candidates, pools, known_urls, known_rids, pool_pub, pool_hsets):
    """候補（dict のリスト）→ (採用, 落とした理由の Counter)。決まった規則だけで決める（目で選ばない）。"""
    adopted, why = [], Counter()
    per_pub = Counter()
    hsets = Counter(pool_hsets)
    seen = set()
    for c in candidates:
        url = c.get("resource_url", "")
        m = re.search(r"/resource/([0-9a-f-]{36})", url)
        rid = c.get("resource_id") or (m.group(1) if m else None)
        pub = str(c.get("publisher_id", ""))
        heads = frozenset(h for h in (c.get("safe_headers") or c.get("headers") or []) if h != "_id")
        reason = None
        if pools.get(pub) != "train":
            reason = "公開元が train でない"
        elif license_id(c) not in ALLOWED_LICENSES:
            reason = "ライセンスが許可の一覧にない"
        elif not c.get("datastore_available"):
            reason = "datastore が無い（今の取り出しの道具は datastore だけ）"
        elif not rid or not url.startswith("https://data.bodik.jp/"):
            reason = "BODIK の resource でない（今の取り出しの道具は BODIK だけ）"
        elif url in known_urls or rid in known_rids or rid in seen:
            reason = "もう使った表"
        elif per_pub[pub] >= PER_PUBLISHER_BATCH:
            reason = "この陣で 1 公開元 3 表まで"
        elif pool_pub[pub] + per_pub[pub] >= PER_PUBLISHER_POOL:
            reason = "教材庫で 1 公開元 15 表まで"
        elif heads and hsets[(pub, heads)] >= SAME_HEADERS_PER_PUBLISHER:
            reason = "同じ公開元で見出しの組が同じ表が 3 つ以上"
        if reason:
            why[reason] += 1
            continue
        seen.add(rid)
        per_pub[pub] += 1
        if heads:
            hsets[(pub, heads)] += 1
        adopted.append({"n": len(adopted) + 1, "publisher_id": pub, "resource_url": url, "title": c.get("title", "")})
    return adopted, why


def cmd_adopt(a):
    w = work(a.batch)
    if (w / "adopted.json").exists():
        raise SystemExit(f"{w}/adopted.json がもうある（陣の採用は 1 回だけ）")
    pools = {p["publisher_id"]: p["pool"] for p in json.load(open(ROOT / "independent_eval" / "allocation.json", encoding="utf-8"))["publishers"]}
    cands = []
    for f in a.candidates:
        d = json.load(open(f, encoding="utf-8"))
        cands += d.get("selected", d) if isinstance(d, dict) else d
    urls, rids = known_resources()
    adopted, why = adopt(cands, pools, urls, rids, pool_publisher_tables(), pool_header_sets())
    w.mkdir(parents=True, exist_ok=True)
    out = {"schema_version": 1, "batch": a.batch, "decided_by": "pipeline.py adopt（Claude の規則）",
           "decided_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "candidates": [str(Path(f).as_posix()) for f in a.candidates], "candidate_count": len(cands),
           "dropped": dict(why), "adopted": adopted}
    (w / "adopted.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"adopted {len(adopted)}/{len(cands)} tables; dropped {dict(why)}")


# ---------------------------------------------------------------- 5. 突き合わせ

def priority(teacher, model, header):
    """Claude が裁定する順。重大 5 種類・金額↔数量・稀少な種類・日本語を先に。"""
    s = 0
    pair = {teacher, model}
    if pair == {"amount", "quantity"}:
        s += 8
    if pair & CRITICAL:
        s += 4
    if pair & RARE:
        s += 3
    if re.search(r"[぀-ヿ一-鿿]", header or ""):
        s += 1
    if teacher in NOT_USED and model == "unknown":
        s -= 5   # どちらも決めていない列は後回し
    return s


def reconcile(corpus, labels, preds, seed):
    if len(corpus) != len(labels) or len(corpus) != len(preds):
        raise ValueError("corpus・ラベル・予測の行数が違う")
    for i, (c, l) in enumerate(zip(corpus, labels)):
        if c["table"] != l.get("table") or c["header"] != l.get("header"):
            raise ValueError(f"{i} 行目の table／header が corpus と違う")
        if l.get("label") not in LABELS + NOT_USED:
            raise ValueError(f"{i} 行目のラベルが知らない値：{l.get('label')}")
    agree, dis = [], []
    for i, (l, p) in enumerate(zip(labels, preds)):
        (agree if l["label"] == p["guarded_prediction"] else dis).append(i)
    dis.sort(key=lambda i: (-priority(labels[i]["label"], preds[i]["guarded_prediction"], corpus[i]["header"]), i))
    to_review, dropped = dis[:REVIEW_LIMIT], dis[REVIEW_LIMIT:]
    rng = random.Random(seed)
    usable_agree = [i for i in agree if labels[i]["label"] not in NOT_USED]
    audit = sorted(rng.sample(usable_agree, min(len(usable_agree), max(AUDIT_MIN, round(len(usable_agree) * AUDIT_RATE)))))
    rows = []
    for kind, ids in (("to_review", to_review), ("audit", audit), ("dropped", dropped)):
        for i in ids:
            rows.append({"i": i, "kind": kind, "teacher": labels[i]["label"], "model": preds[i]["guarded_prediction"],
                         "priority": priority(labels[i]["label"], preds[i]["guarded_prediction"], corpus[i]["header"]),
                         "header": corpus[i]["header"], "values": corpus[i]["values"][:5], "context": corpus[i].get("context", [])[:8]})
    return {"agree": agree, "disagree": dis, "to_review": to_review, "audit": audit, "dropped": dropped}, rows


def cmd_reconcile(a):
    w = work(a.batch)
    corpus = read_jsonl(w / "corpus.jsonl")
    labels = read_jsonl(w / "labels_chatgpt.jsonl")
    preds = json.load(open(w / "pred_e5base_seed1.json", encoding="utf-8"))["rows"]
    split, rows = reconcile(corpus, labels, preds, seed=f"jitsuris-pool-audit|{a.batch}")
    write_jsonl(w / "review.jsonl", rows)
    print(f"agree {len(split['agree'])} disagree {len(split['disagree'])} → review {len(split['to_review'])}, "
          f"audit {len(split['audit'])}, dropped {len(split['dropped'])}")


# ---------------------------------------------------------------- 7. 確定

def finalize(corpus, labels, preds, review, decisions, batch, teacher_name):
    dec = {d["i"]: d for d in decisions}
    need = [r["i"] for r in review if r["kind"] in ("to_review", "audit")]
    missing = [i for i in need if i not in dec]
    if missing:
        raise ValueError(f"裁定が無い行：{missing[:10]}（{len(missing)} 件）")
    for d in decisions:
        if d.get("label") not in LABELS + NOT_USED:
            raise ValueError(f"裁定のラベルが知らない値：{d}")
    audit = [r["i"] for r in review if r["kind"] == "audit"]
    errors = [i for i in audit if dec[i]["label"] != labels[i]["label"]]
    rate = len(errors) / len(audit) if audit else 0.0
    if rate > AUDIT_MAX_ERROR:
        raise ValueError(f"抜き取りの誤り率 {rate:.1%}（{len(errors)}/{len(audit)}）が 5% を超える。一致の列も全件見直す（DATA_COLLECTION_PROTOCOL 第 6 章の 3）")
    kind = {r["i"]: r["kind"] for r in review}
    out, record, stat = [], [], Counter()
    for i, c in enumerate(corpus):
        k = kind.get(i, "agree")
        if k == "dropped":
            stat["dropped"] += 1
            continue
        if i in dec:
            lab, who = dec[i]["label"], f"claude-{batch}"
        else:
            lab, who = labels[i]["label"], f"{teacher_name}+e5base-agree"
        stat[k] += 1
        rec = {**c, "label": lab, "teacher": who, "batch": batch}
        if i in dec:
            record.append({"i": i, "kind": k, "teacher": labels[i]["label"], "model": preds[i]["guarded_prediction"],
                           "label": lab, "reason": dec[i].get("reason", "")})
        if lab not in NOT_USED:
            out.append(rec)
        else:
            stat["not_used"] += 1
    return out, record, stat, {"audit": len(audit), "audit_errors": len(errors), "audit_error_rate": round(rate, 4)}


def cmd_finalize(a):
    w = work(a.batch)
    final = POOL / f"batch_{a.batch}.jsonl"
    if final.exists():
        raise SystemExit(f"{final} がもうある")
    corpus = read_jsonl(w / "corpus.jsonl")
    labels = read_jsonl(w / "labels_chatgpt.jsonl")
    preds = json.load(open(w / "pred_e5base_seed1.json", encoding="utf-8"))["rows"]
    review = read_jsonl(w / "review.jsonl")
    decisions = read_jsonl(w / "decisions.jsonl")
    teacher = (labels[0].get("teacher") if labels else "chatgpt") or "chatgpt"
    out, record, stat, audit = finalize(corpus, labels, preds, review, decisions, a.batch, teacher)
    write_jsonl(final, out)
    write_jsonl(POOL / f"adjudication_{a.batch}.jsonl", record)
    m = manifest()
    m["batches"].append({"batch": a.batch, "finalized_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                         "columns": len(out), "tables": len({r["table"] for r in out}),
                         "publishers": len({r["publisher"] for r in out}), "labels": dict(Counter(r["label"] for r in out)),
                         "stats": dict(stat), **audit, "sha256": sha256(final),
                         "inputs": {n: sha256(w / n) for n in ("adopted.json", "corpus.jsonl", "labels_chatgpt.jsonl",
                                                                "pred_e5base_seed1.json", "review.jsonl", "decisions.jsonl")}})
    save_manifest(m)
    print(f"batch {a.batch}: {len(out)} columns into the pool; {dict(stat)}; audit {audit}")


# ---------------------------------------------------------------- 教材庫の状態

def cmd_status(a):
    m = manifest()
    rows = [r for f in sorted(glob.glob(str(POOL / "batch_*.jsonl"))) for r in read_jsonl(f)]
    target = m.get("target_columns", TARGET_COLUMNS)
    lines = [f"# 教材庫の状態（{datetime.now(timezone.utc).isoformat(timespec='minutes')}・pipeline.py status で自動生成）", "",
             f"- 学習に使える列：**{len(rows):,}** ／ 第 1 目標 {target:,}（残り {max(0, target - len(rows)):,}）",
             f"- 表 {len({r['table'] for r in rows}):,}・公開元 {len({r['publisher'] for r in rows}):,}・陣 {len(m['batches'])}", "",
             "| 陣 | 列 | 表 | 公開元 | 抜き取りの誤り | 確定 |", "|---|---:|---:|---:|---:|---|"]
    for b in m["batches"]:
        lines.append(f"| {b['batch']} | {b['columns']} | {b['tables']} | {b['publishers']} | {b.get('audit_errors', 0)}/{b.get('audit', 0)} | {b['finalized_utc'][:10]} |")
    lines += ["", "| 種類 | 列 |", "|---|---:|"] + [f"| {k} | {v} |" for k, v in Counter(r["label"] for r in rows).most_common()]
    text = "\n".join(lines) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    print(text)


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("adopt"); p.add_argument("--batch", required=True); p.add_argument("--candidates", nargs="+", required=True)
    p = sub.add_parser("reconcile"); p.add_argument("--batch", required=True)
    p = sub.add_parser("finalize"); p.add_argument("--batch", required=True)
    p = sub.add_parser("status"); p.add_argument("--out")
    a = ap.parse_args(argv)
    {"adopt": cmd_adopt, "reconcile": cmd_reconcile, "finalize": cmd_finalize, "status": cmd_status}[a.cmd](a)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
