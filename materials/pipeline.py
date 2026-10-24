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
import unicodedata
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POOL = ROOT / "materials" / "pool"
LABELS = ("account", "address", "amount", "category", "date", "email", "id", "org", "other", "person", "phone",
          "product", "quantity", "rate", "tax_class", "text")
NOT_USED = ("unknown", "S")
# 再配布できる条件だけ（DATA_COLLECTION_PROTOCOL 第 2 章：CC0・CC BY・政府標準利用規約 2.0・PDL 1.0・OGL）。NC・SA・不明は入れない。
# 政府標準利用規約の CKAN の ID は、カタログでの表記を確かめてから足す（2026-10-22 時点で未確認）。
ALLOWED_LICENSES = {"cc-by-4.0", "cc-by-40-intl", "cc-by", "cc-by-21", "cc-by-21-jp", "cc-by-30", "cc-zero", "cc0", "cc0-1.0", "odc-by",
                    "ogl-uk-3.0", "ogl-canada-2.0", "pdl1.0", "public-domain"}   # pdl1.0・cc-by-21 は 2026-10-22 に内訳を見て追加。public-domain は CC0 と同じ扱い
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


def normalize_license(raw):
    """カタログごとの書き方の違いをそろえる（Socrata の PUBLIC_DOMAIN・CC0_10・「name-public-domain-…」など）。"""
    v = str(raw or "").strip().lower().replace("_", "-")
    words = re.split(r"[^a-z0-9]+", v)
    if "nc" in words or "sa" in words or "nd" in words or "noncommercial" in words or "sharealike" in words or "noderivatives" in words:
        return v   # 非営利・継承・改変禁止は一覧に無いので、そのまま返して落とす
    # 書き方の違い（2026-10-24 の候補集めで落ちていた）：URL（creativecommons.org/licenses/by/4.0）、版・国つきの CC BY
    # （cc-by-2.5・cc-by-3.0-au・「Creative Commons Attribution 3.0 Australia」）は表示だけのライセンスなので cc-by にまとめる
    if re.search(r"creativecommons\.org/publicdomain/zero", v):
        return "cc0"
    if re.search(r"creativecommons\.org/licenses/by/", v) or re.fullmatch(r"cc-by-[0-9.]+(-(au|intl|int|nz))?", v) \
            or re.fullmatch(r"creative commons (cc-by|attribution)( [0-9.]+)?( (australia|international|au|intl))?", v):
        return v if v in ("cc-by-4.0", "cc-by-30", "cc-by-21") else "cc-by"
    if v in ("ca-ogl-lgo", "qc-cc-by"):   # カナダ連邦の Open Government Licence、ケベック州の CC BY（open.canada.ca の ID）
        return "ogl-canada-2.0" if v == "ca-ogl-lgo" else "cc-by"
    # カナダの州・準州の Open Government Licence（OGL-UK を元にした出典表示だけのライセンス）とサスカチュワンの
    # Standard Unrestricted Use Data Licence（出典表示だけ）。連邦の OGL-Canada と同じ扱い（2026-10-24 Claude の判断）
    if v in ("ab-ogla", "bc-oglbc", "on-oglo", "ns-oglns", "nb-oglnb", "nl-oglnl", "pei-oglpei", "yk-oglyk", "mb-omb", "nwt-tno", "sk-suudl"):
        return "ogl-canada-2.0"
    if "public-domain" in v or v == "public domain" or v in ("odc-pddl", "pddl"):   # PDDL は公有の宣言（CC0 と同じ扱い）
        return "public-domain"
    if "cczero" in v or v.startswith("cc0") or "cc0-10" in v:
        return "cc0"
    if v in ("ogl-canada-2.0", "ogl-canada", "open-government-licence-canada"):   # 出典表示だけの政府ライセンス（OGL-UK と同じ扱い。2026-10-24）
        return "ogl-canada-2.0"
    if v in ("cc-30-by", "cc-by-3.0"):
        return "cc-by-30"
    if v in ("cc-40-by", "cc-by-40"):
        return "cc-by-4.0"
    return v


def license_from_pkg(pkg):
    """CKAN のデータセットのライセンス。license_id が空なら license_title を読む（e-Gov は名前だけを書く。2026-10-24）。
    政府標準利用規約（第2.0版）は CC BY 4.0 と互換と規約に明記されているので cc-by-4.0 と同じ扱い。"""
    lid = normalize_license(pkg.get("license_id"))
    if lid and lid not in ("notspecified", "none"):
        return lid
    title = unicodedata.normalize("NFKC", str(pkg.get("license_title") or "")).strip()
    if not title:
        title = license_text_elsewhere(pkg)
    if re.search(r"政府標準利用規約.*(2\.0|第2)", title) or re.search(r"(CC|クリエイティブ・?コモンズ)\s*(BY|表示)\s*4\.0", title, re.I):
        return "cc-by-4.0"
    if re.search(r"(CC|クリエイティブ・?コモンズ)\s*(BY|表示)(?![-\s]*(NC|SA|非営利|継承))", title, re.I):
        return "cc-by"
    return normalize_license(title) if title else lid


def license_text_elsewhere(pkg):
    """license_id・license_title が両方空のとき、extras（key に license・ライセンス・利用規約）とリソースの license・rights を読む
    （e-Gov は 10/24 の候補集めで 12,908 件すべて両方が空だった。2026-10-24）。見つからなければ空。"""
    for e in pkg.get("extras") or []:
        if isinstance(e, dict) and re.search(r"licen[cs]e|ライセンス|利用規約|rights", str(e.get("key") or ""), re.I) and str(e.get("value") or "").strip():
            return unicodedata.normalize("NFKC", str(e["value"])).strip()
    for r in pkg.get("resources") or []:
        for k in ("license", "license_title", "rights"):
            if str(r.get(k) or "").strip():
                return unicodedata.normalize("NFKC", str(r[k])).strip()
    return ""


def csv_domains(catalog_host):
    """カタログのホストごとに、CSV を取ってよい組織のドメイン（allowed_hosts.json の csv_domains）。カタログのホストは常に含む。"""
    p = POOL / "allowed_hosts.json"
    extra = json.load(open(p, encoding="utf-8")).get("csv_domains", {}).get(catalog_host, []) if p.exists() else []
    return [catalog_host] + list(extra)


def host_in(host, domains):
    host = (host or "").lower()
    return any(host == d or host.endswith("." + d) for d in domains)


def license_id(c):
    lic = c.get("license")
    return normalize_license((lic.get("id") if isinstance(lic, dict) else lic) or c.get("license_id"))


# 題名で落とす（個人の記録が入りやすい表。列の検査だけに頼らない）
TITLE_DENY = re.compile(r"(crime|arrest|police|incident|complaint|311|service request|campaign|contribut|donor|election|"
                        r"permit|licens|inspection|violation|calls for service|admission|enrol+ment|allegation|internal affairs|student|patient|victim|offender|inmate|payroll|employee|salar|"
                        r"犯罪|逮捕|通報|苦情|選挙|寄付者|申請者|利用者|患者|児童|生徒|職員|在籍者|入学者|"
                        r"crime|ocorr[eê]ncia|den[uú]ncia|reclama[cç]|elei[cç]|servidor|sal[aá]rio|remunera[cç]|folha de pagamento|"
                        r"aluno|estudante|profissionais|concurso|inscri[cç]|matr[ií]cula|paciente|v[ií]tima|pres[oa]s|detent|alvar[aá]|multa|benefici[aá]rio)", re.I)


def platform_of(c):
    """候補の取り出し方：bodik・ckan（許可のホスト）・socrata（公開元の ID とホストが一致するもの）。どれでもなければ None。"""
    from urllib.parse import urlparse
    url = c.get("resource_url") or c.get("catalog_url") or ""
    host = (urlparse(url).hostname or "").lower()
    if (c.get("platform") or "").lower() == "socrata":
        pid = str(c.get("publisher_id", ""))
        if pid.startswith("world_socrata_") and pid[len("world_socrata_"):] == re.sub(r"[.-]", "_", host) and re.fullmatch(r"[a-z0-9]{4}-[a-z0-9]{4}", str(c.get("resource_id", ""))):
            return "socrata", host
        return None, host
    if host == "data.bodik.jp":
        return "bodik", host
    if host in allowed_ckan_hosts():
        return "ckan", host
    return None, host


def allowed_ckan_hosts():
    p = POOL / "allowed_hosts.json"
    return set(json.load(open(p, encoding="utf-8")).get("ckan", [])) if p.exists() else set()


def adopt(candidates, pools, known_urls, known_rids, pool_pub, pool_hsets):
    """候補（dict のリスト）→ (採用, 落とした理由の Counter)。決まった規則だけで決める（目で選ばない）。"""
    adopted, why = [], Counter()
    per_pub = Counter()
    hsets = Counter(pool_hsets)
    seen = set()
    for c in candidates:
        url = c.get("resource_url") or c.get("catalog_url") or ""
        m = re.search(r"/resource/([0-9a-f-]{36})", url)
        rid = c.get("resource_id") or (m.group(1) if m else None)
        pub = str(c.get("publisher_id", ""))
        heads = frozenset(h for h in (c.get("safe_headers") or c.get("headers") or []) if h != "_id")
        reason = None
        if pools.get(pub) != "train":
            reason = "公開元が train でない"
        elif license_id(c) not in ALLOWED_LICENSES:
            reason = "ライセンスが許可の一覧にない"
        elif TITLE_DENY.search(f"{c.get('title', '')} {c.get('resource_name', '')}"):
            reason = "題名が個人の記録になりやすい表"
        elif not c.get("datastore_available") and c.get("access") != "csv":
            reason = "datastore も CSV も無い（取り出しの道具は datastore・SODA・同じホストの CSV）"
        elif platform_of(c)[0] is None or not rid:
            reason = "取り出せる場でない（BODIK・許可の CKAN・公開元と一致する Socrata だけ）"
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
        plat, host = platform_of(c)
        adopted.append({"n": len(adopted) + 1, "publisher_id": pub, "resource_url": url, "title": c.get("title", ""),
                        "platform": plat, "host": host, "resource_id": rid, "access": c.get("access") or ("datastore" if plat != "socrata" else "soda")})
    return adopted, why


def cmd_adopt(a):
    w = work(a.batch)
    if (w / "adopted.json").exists():
        raise SystemExit(f"{w}/adopted.json がもうある（陣の採用は 1 回だけ）")
    pools = {p["publisher_id"]: p["pool"] for p in json.load(open(ROOT / "independent_eval" / "allocation.json", encoding="utf-8"))["publishers"]}
    cands = []
    for f in a.candidates:
        d = json.load(open(f, encoding="utf-8"))
        lst = (d.get("selected") or d.get("candidates")) if isinstance(d, dict) else d
        if not isinstance(lst, list):
            raise SystemExit(f"{f}：候補の一覧（selected か candidates）が無い")
        cands += lst
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


def align_preds(set_columns, pred_rows):
    """予測を set.json の id の順に並べる。予測の後に列を消した（個人情報の除去など）ときも、
    予測を作り直さずに残った列だけを使える。set にあって予測に無い列があれば止める。"""
    by_id = {r["id"]: r for r in pred_rows}
    missing = [c["id"] for c in set_columns if c["id"] not in by_id]
    if missing:
        raise ValueError(f"予測に無い列：{missing[:5]}（{len(missing)} 件）。予測を依頼し直す")
    return [by_id[c["id"]] for c in set_columns]


def load_preds(w):
    preds = json.load(open(w / "pred_e5base_seed1.json", encoding="utf-8"))["rows"]
    cols = json.load(open(w / "set.json", encoding="utf-8"))["columns"]
    return align_preds(cols, preds)


def cmd_reconcile(a):
    w = work(a.batch)
    corpus = read_jsonl(w / "corpus.jsonl")
    labels = read_jsonl(w / "labels_chatgpt.jsonl")
    preds = load_preds(w)
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
        if lab == "person":
            # 公開データの表の人の名前は教材庫に入れない（個人情報。2026-10-24）。person の教材は仕様由来の偽の名前で作る
            stat["not_used_person"] += 1
            continue
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
    preds = load_preds(w)
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
