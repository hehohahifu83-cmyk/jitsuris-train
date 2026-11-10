"""G1（海外の確かめの陣）の公開元を決める（2026-11-11 Claude、収集の前。メタデータの組織名だけを見る。データセットの中身は見ない）。

  python research/g1/g1_orgs.py            → research/g1/g1_orgs.json（組織ごとの今の割り当て・G1 に入れるか）
  python research/g1/g1_orgs.py --write    → 入れる組織を allocation.json に hold で登録する

決まり（bench/g1_prereg_20261111.md）：
  カタログごとに割り当てる（組織をハッシュでばらさない）。G1＝Alberta（open.alberta.ca）・Ontario（data.ontario.ca）・Berlin（datenregister.berlin.de）。
  NSW は data.gov.au 経由で教材庫（train）に 229 組織あるので使わない。GovData.de は Berlin を取り込むので、重ならないよう取っておく。
  データセットのある組織だけ。同じ「親:組織」が allocation.json に hold 以外で登録されていれば外す。
"""
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "independent_eval"))
import allocation as A  # noqa: E402

PROBE = ROOT / "materials/pool/probe/orgs_f1_20261104c.json"
ALLOC = ROOT / "independent_eval/allocation.json"
OUT = ROOT / "research/g1/g1_orgs.json"
PARENT = {"alberta": "alberta_cat", "ontario": "ontario_cat", "berlin": "berlin_cat"}


def main(argv=None):
    write = "--write" in (argv if argv is not None else sys.argv[1:])
    probe = json.load(open(PROBE, encoding="utf-8"))
    alloc = A.load_allocation(ALLOC)
    rows = []
    for h in [x for x in probe["hosts"] if x["site"] in PARENT]:
        for o in h.get("orgs") or []:
            if not o.get("package_count"):
                continue
            pid = f"{PARENT[h['site']]}:{o['name']}"
            canon = A.resolve_publisher_id(pid, alloc.get("aliases", {}))
            now = next((p["pool"] for p in alloc["publishers"] if A.normalize_publisher_id(p["publisher_id"]) == canon), None)
            rows.append({"site": h["site"], "base": h["base"], "org": o["name"], "title": o.get("title", ""), "datasets": o["package_count"],
                         "publisher_id": pid, "pool_now": now, "g1": now in (None, "hold"),
                         "reason": "" if now in (None, "hold") else f"もう {now} に登録"})
    if write:
        today = date.today().isoformat()
        have = {A.normalize_publisher_id(p["publisher_id"]) for p in alloc["publishers"]}
        for r in rows:
            if r["g1"] and A.normalize_publisher_id(r["publisher_id"]) not in have:
                alloc["publishers"].append({"publisher_id": r["publisher_id"], "pool": "hold", "date": today})
                have.add(A.normalize_publisher_id(r["publisher_id"]))
        ALLOC.write_text(json.dumps(alloc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    doc = {"schema_version": 1, "probe": str(PROBE.relative_to(ROOT)), "rows": rows,
           "summary": {s: {"orgs": sum(r["site"] == s for r in rows), "g1": sum(r["site"] == s and r["g1"] for r in rows)} for s in PARENT}}
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(doc["summary"], ensure_ascii=False))


if __name__ == "__main__":
    main()
