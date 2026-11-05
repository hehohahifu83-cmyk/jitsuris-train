"""Shirasagi の提供元の登録（2026-11-05 Claude）。Codex の下書き（shirasagi_owner_crosswalk_draft_20261105.json）の確認順 255 件から、
メタデータだけで持ち主が分かるものを選び、allocation に自治体を登録し（ハッシュの pool。eval2・eval3 になった自治体は教材に使わない）、
allowed_hosts.json の shirasagi に train の自治体だけを書く。

  python research/catalogs/shirasagi_register.py [--write]
    → 確認の結果 research/catalogs/shirasagi_register_20261105.json（--write で allocation・allowed_hosts も書く）

採る条件（どれも満たすもの）：
  A1 フィールドが author か user.name（user.id は投稿者のアカウントで、県が市町の代わりに投稿していることがあるので、ページを見るまで採らない）
  A2 値そのものが持ち主を名乗る：値が自治体の名前で始まる（「青森県　総務部…」「松茂町 総務課」「むつ市」）、
     または愛媛県のカタログで、値の「部」と「課・室」が愛媛県の公式の組織のページ（shirasagi_official_organizations_20261105.json）にある
  A3 全 926 組で、同じフィールドの同じ値が別の自治体・不明・除外に使われていない
  A4 6 桁のコードの検査数字が正しい・仙台市 041009 でない・allocation で train 以外（hold・main・eval）に登録済みでない
  A5 ハッシュの pool が train（新しく登録する自治体）
静岡は全件を取れていない（2 件取得できない）ので、下書きにも単独の案が無く、登録しない。
"""
import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "independent_eval"))
sys.path.insert(0, str(ROOT / "materials"))
from allocation import add_assignment, assignment_for, load_allocation  # noqa: E402

DRAFT = ROOT / "research/catalogs/shirasagi_owner_crosswalk_draft_20261105.json"
ORGS = ROOT / "research/catalogs/shirasagi_official_organizations_20261105.json"
ALLOC = ROOT / "independent_eval/allocation.json"
HOSTS = ROOT / "materials/pool/allowed_hosts.json"
OUT = ROOT / "research/catalogs/shirasagi_register_20261105.json"
TODAY = "2026-11-05"
EXCLUDED = {"041009"}
MAX_DATASETS = {"https://opendata.pref.aomori.lg.jp": 1100, "https://opendata.pref.tokushima.lg.jp": 2000,
                "https://opendata.pref.kagawa.lg.jp": 700, "https://odp-pref-tottori.tori-info.co.jp": 300,
                "https://www.pref.ehime.jp/opendata-catalog": 1000}
EHIME = "https://www.pref.ehime.jp/opendata-catalog"


def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(s))).strip()


def valid_code(code):
    return bool(re.fullmatch(r"\d{6}", code or "")) and int(code[-1]) == ((11 - sum(int(a) * b for a, b in zip(code[:5], (6, 5, 4, 3, 2))) % 11) % 10)


def ehime_names():
    for r in json.load(open(ORGS, encoding="utf-8"))["results"]:
        if r["pref"] == "愛媛県":
            return {norm(l["name"]) for l in r["organization_links"]}
    return set()


def ehime_department(value, names):
    """「企画振興部企画統計課」→ 部（企画振興部）と課（企画統計課）が公式のページにあるか。部の無い「教育委員会事務局…」「人事委員会事務局…」も見る。"""
    v = norm(value).replace(" ", "")
    if v in names:
        return True
    m = re.match(r"^(.+?(?:部|事務局|委員会事務局))(.+)$", v)
    if not m:
        return False
    head, tail = m.groups()
    heads = {n.split(" ")[0] for n in names}
    return (head in heads or any(n.startswith(head) for n in names)) and (tail in names or v in names or f"{head}{tail}" in names
                                                                      or any(n.endswith(tail) for n in names))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)
    d = json.load(open(DRAFT, encoding="utf-8"))
    combos = d["combinations"]
    owners = {}
    for c in combos:
        for f, key in (("author", "author"), ("user.name", "user_name"), ("user.id", "user_id")):
            v = c.get(key)
            if v in (None, ""):
                continue
            owners.setdefault((c["site"], f, str(v)), set()).add(c["municipality_code"] if not c.get("excluded") else "除外/不明")
    names = ehime_names()
    alloc = load_allocation(ALLOC)
    results = []
    for x in d["reduced_review_queue"]:
        why = []
        v, m = norm(x["value"]), x["municipality"]
        if x["field"] == "user.id":
            why.append("A1 user.id（投稿者のアカウント）はページを見るまで採らない")
        elif not (v.startswith(m) or (x["site"] == EHIME and m == "愛媛県" and ehime_department(x["value"], names))):
            why.append("A2 値が持ち主を名乗らない（部署の名前だけ）")
        other = owners.get((x["site"], x["field"], str(x["value"])), set()) - {x["municipality_code"]}
        if other:
            why.append(f"A3 同じ値が別の持ち主にも使われる {sorted(other)}")
        code = x["municipality_code"]
        if not valid_code(code) or code in EXCLUDED:
            why.append("A4 コードが正しくない・仙台市")
        pool = assignment_for(code, alloc)["pool"] if valid_code(code) else "?"
        if not why and pool != "train":
            why.append(f"A5 自治体の pool が {pool}（教材に使わない）")
        results.append({**{k: x[k] for k in ("site", "field", "value", "municipality", "municipality_code", "datasets", "evidence_url")},
                        "pool": pool, "accepted": not why, "reasons": why})
    accepted = [r for r in results if r["accepted"]]
    # 採らなかった自治体も、名乗りが確かめられたもの（A5 だけで落ちたもの）は登録して eval の側に固定する
    register = sorted({r["municipality_code"] for r in results if r["accepted"] or r["reasons"] and all(w.startswith("A5") for w in r["reasons"])})
    summary = {"queue": len(results), "accepted": len(accepted), "accepted_datasets": sum(r["datasets"] for r in accepted),
               "registered_codes": register,
               "pools": {c: assignment_for(c, alloc)["pool"] for c in register}}
    OUT.write_text(json.dumps({"created": TODAY, "draft_sha256_source": str(DRAFT.name), "summary": summary, "results": results},
                              ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    if not a.write:
        return
    for c in register:
        alloc = add_assignment(alloc, c, TODAY)
    ALLOC.write_text(json.dumps(alloc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    hosts = json.load(open(HOSTS, encoding="utf-8"))
    sites = []
    for site, mx in MAX_DATASETS.items():
        pubs = [{"field": r["field"], "value": r["value"], "municipality_code": r["municipality_code"], "evidence_url": r["evidence_url"]}
                for r in accepted if r["site"] == site]
        if pubs:
            sites.append({"site": site, "max_datasets": mx, "publishers": pubs})
    hosts["shirasagi"] = sites
    HOSTS.write_text(json.dumps(hosts, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"allocation に {len(register)} 自治体、shirasagi に {len(sites)} サイト {len(accepted)} 組")


if __name__ == "__main__":
    main()
