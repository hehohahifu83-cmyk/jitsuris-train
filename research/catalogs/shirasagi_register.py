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

2026-11-05 追加：A1・A2 で落ちた組（user.id・部署名だけ）は、Codex の一覧（shirasagi_owner_inventory_20261105.json）の
groups（Shirasagi の所属。「鳥取県/鳥取市」「徳島県/美馬市/企画総務部/…」のように持ち主が階層で入る）で確かめる：
  G1 その値を持つ全部の組で、候補の自治体を指す groups の数 ≥ データセットの数
  G2 ほかの groups は、県のカタログ管理の課（…情報政策課）か県の名前だけ
  G3 県が候補のときは、groups に県内の市町村の名前が無い（2 段目が部・局・庁などの県の組織）
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
INVENTORY = ROOT / "research/catalogs/shirasagi_owner_inventory_20261105.json"
MUNI = json.load(open(ROOT / "materials/dict/jp_municipalities.json", encoding="utf-8"))
CITY_NAMES = {r["city"] for r in MUNI if r["city"]}
PREF_NAMES = {r["pref"] for r in MUNI}
OUT = ROOT / "research/catalogs/shirasagi_register_20261105.json"
TODAY = "2026-11-05"
EXCLUDED = {"041009"}
MAX_DATASETS = {"https://opendata.pref.aomori.lg.jp": 1100, "https://opendata.pref.tokushima.lg.jp": 2000,
                "https://opendata.pref.kagawa.lg.jp": 700, "https://odp-pref-tottori.tori-info.co.jp": 300,
                "https://www.pref.ehime.jp/opendata-catalog": 1000, "https://opendata.pref.shizuoka.jp": 4000}
SHIZUOKA = "https://opendata.pref.shizuoka.jp"
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


def group_check(row, inventory):
    """G1〜G3。戻り値：(通るか, 説明)。"""
    combos = [c for c in inventory[row["site"]]["combinations"]
              if (str(c["user_id"]) == row["value"] if row["field"] == "user.id"
                  else c["author" if row["field"] == "author" else "user_name"] == row["value"])]
    ds = sum(c["datasets"] for c in combos)
    if not ds:
        return False, "G0 一覧に組が無い"
    groups = {}
    for c in combos:
        for g, n in c["group_affiliations"].items():
            groups[g] = groups.get(g, 0) + n
    m = row["municipality"]
    is_pref = m in PREF_NAMES
    own = other = 0
    bad = []
    for g, n in groups.items():
        parts = [norm(x) for x in g.split("/")]
        cities = [x for x in parts if x in CITY_NAMES or any(x.startswith(cn + " ") for cn in CITY_NAMES)]
        if is_pref:
            if parts[0] == m and len(parts) >= 2 and not cities:
                own += n
            elif parts == [m]:
                other += n
            else:
                bad.append(g)
        else:
            if any(x == m or x.startswith(m + " ") or x.startswith(m) for x in parts[:3]):
                own += n
            elif parts == [parts[0]] and parts[0] in PREF_NAMES or (parts[0] in PREF_NAMES and parts[-1].endswith("情報政策課")):
                other += n
            else:
                bad.append(g)
    if bad:
        return False, f"G2/G3 ほかの持ち主の groups {bad[:3]}"
    if own < ds:
        return False, f"G1 持ち主の groups {own} < データセット {ds}"
    return True, f"G 持ち主の groups {own} ≥ データセット {ds}（ほか {other} は県のカタログ管理・県名だけ）"


def shizuoka_rows(inventory):
    """静岡（2026-11-06 追加）：Codex の確認順には静岡が無い（一覧 3,800 件のうち 2 件が取れず、単独の案を出さなかった）。
    一覧の静岡の組から、投稿者（user.id）ごとに、groups がただ 1 つの市町（または県の組織）を指すものを候補にする。確かめは group_check（G1〜G3）。
    取れなかった 2 件は、取り出しのときに user.id を照らすだけで、groups は見ない。その 2 件が別の持ち主でも、混ざるのはその 2 件まで。"""
    cities = {r["city"]: r["code"] for r in MUNI if r["pref"] == "静岡県" and r["city"]}
    by_uid = {}
    for c in inventory[SHIZUOKA]["combinations"]:
        if c["user_id"] is None:
            continue
        by_uid.setdefault(str(c["user_id"]), []).append(c)
    out = []
    for uid, cs in sorted(by_uid.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else 0):
        hit = set()
        for c in cs:
            for g in c["group_affiliations"]:
                parts = [norm(x) for x in g.split("/")]
                hit |= {cn for cn in cities for x in parts[:3] if x.startswith(cn)}
        if len(hit) == 1:
            m = next(iter(hit)); code = cities[m]
        elif not hit and any(g.startswith("静岡県/") for c in cs for g in c["group_affiliations"]):
            m, code = "静岡県", "220001"
        else:
            continue
        out.append({"site": SHIZUOKA, "field": "user.id", "value": uid, "municipality": m, "municipality_code": code,
                    "datasets": sum(c["datasets"] for c in cs), "evidence_url": (cs[0].get("evidence_pages") or [""])[0], "_shizuoka": True})
    # 投稿者の無い組（user.id が None。島田市・静岡市など）は、author がちょうど「静岡県/<市町>」か「<市町>」のものだけ
    seen_auth = set()
    for c in inventory[SHIZUOKA]["combinations"]:
        a = norm(c["author"])
        m = a.split("/", 1)[1] if a.startswith("静岡県/") else a
        if m not in cities or c["author"] in seen_auth:
            continue
        seen_auth.add(c["author"])
        ds = sum(x["datasets"] for x in inventory[SHIZUOKA]["combinations"] if x["author"] == c["author"])
        out.append({"site": SHIZUOKA, "field": "author", "value": c["author"], "municipality": m, "municipality_code": cities[m],
                    "datasets": ds, "evidence_url": (c.get("evidence_pages") or [""])[0], "_shizuoka": True})
    return out


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
    inventory = {x["site"]: x for x in json.load(open(INVENTORY, encoding="utf-8"))["results"]}
    alloc = load_allocation(ALLOC)
    results = []
    for x in d["reduced_review_queue"] + shizuoka_rows(inventory):
        why = []
        v, m = norm(x["value"]), x["municipality"]
        named = x["field"] != "user.id" and (v.startswith(m) or (x["site"] == EHIME and m == "愛媛県" and ehime_department(x["value"], names)))
        basis = "A2 値が持ち主を名乗る"
        if not named:
            ok, msg = group_check(x, inventory)
            if ok:
                basis = msg
            else:
                why.append(("A1 user.id" if x["field"] == "user.id" else "A2 部署の名前だけ") + "で、groups でも確かめられない：" + msg)
        other = owners.get((x["site"], x["field"], str(x["value"])), set()) - {x["municipality_code"]}
        if other and not x.get("_shizuoka"):   # 静岡は Codex が多くを「不明」にしたので、持ち主の食い違いは groups（G2/G3）で見る
            why.append(f"A3 同じ値が別の持ち主にも使われる {sorted(other)}")
        code = x["municipality_code"]
        if not valid_code(code) or code in EXCLUDED:
            why.append("A4 コードが正しくない・仙台市")
        pool = assignment_for(code, alloc)["pool"] if valid_code(code) else "?"
        if not why and pool != "train":
            why.append(f"A5 自治体の pool が {pool}（教材に使わない）")
        results.append({**{k: x[k] for k in ("site", "field", "value", "municipality", "municipality_code", "datasets", "evidence_url")},
                        "pool": pool, "accepted": not why, "basis": basis if not why else "", "reasons": why})
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
