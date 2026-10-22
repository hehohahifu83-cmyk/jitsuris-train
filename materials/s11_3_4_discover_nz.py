#!/usr/bin/env python3
"""S11 3.4 New Zealand catalogue candidate discovery; metadata/schema only."""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from independent_eval.allocation import add_assignment, assignment_for, load_allocation  # noqa: E402
from independent_eval.discover import HEADER_DENY, TITLE_DENY, normalize_header  # noqa: E402

API = "https://catalogue.data.govt.nz/api/3/action"
LEGACY_API = "https://catalogue.data.govt.nz/api/action"
HOST = "catalogue.data.govt.nz"
PORTAL = "https://catalogue.data.govt.nz"
LICENSE_IDS = {
    "cc-by", "cc-by-40-intl", "cc-by-4.0", "cc-by-30", "cc-by-3.0",
    "cc-by-30-nz", "cc-by-3.0-nz", "cc-by-21", "cc-by-2.1",
    "cc-zero", "cc0", "cc0-1.0", "pddl", "odc-pddl",
}
MIN_HEADERS = 8
MAX_HEADERS = 10
TARGET_TABLES = 60
MAX_PER_PUBLISHER = 1  # 1/60 = 1.67%, within the protocol's 3% cap.
MAX_SCHEMA_PER_PUBLISHER = 3
MAX_SCHEMA_REQUESTS = 1200
MAX_NON_DATASTORE = 300
SENSITIVE_TITLE = TITLE_DENY
USEFUL_HEADER = re.compile(
    r"(?:amount|total|quantity|qty|unit|price|rate|tax|account|category|class|code|id|date|"
    r"name|description|order|invoice|product|department|value|count|number|status|type|"
    r"measure|index|ratio|percent|revenue|expenditure|budget|population|employment)", re.I
)
CODE_HEADER = re.compile(r"(?:code|_id$|^id$|identifier|number$)", re.I)
NAME_HEADER = re.compile(r"(?:name|title|description|label)", re.I)
JAPANESE_SCRIPT = re.compile(r"[ぁ-んァ-ヶ一-龯々〆〤]")


def _json_request(url: str, retries: int = 4, data: bytes | None = None) -> dict:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != HOST:
        raise ValueError("request host is outside the New Zealand catalogue allowlist")
    for attempt in range(retries):
        headers = {"User-Agent": "jitsuris-s11-metadata-discovery/1.0", "Accept": "application/json"}
        if data is not None:
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        req = Request(url, data=data, headers=headers)
        try:
            with urlopen(req, timeout=40) as response:
                return json.loads(response.read(15_000_001).decode("utf-8-sig"))
        except HTTPError as exc:
            if exc.code not in {408, 425, 429, 500, 502, 503, 504} or attempt + 1 == retries:
                raise
            time.sleep(1.0 + 2.0 * attempt)
        except (TimeoutError, URLError, OSError):
            if attempt + 1 == retries:
                raise
            time.sleep(1.0 + 2.0 * attempt)
    raise RuntimeError("metadata request retries exhausted")


def _action(action: str, params: dict | None = None, *, api_root: str = API, method: str = "GET"):
    if method == "POST":
        payload = _json_request(f"{api_root}/{action}", data=urlencode(params or {}).encode("utf-8"))
    else:
        query = f"?{urlencode(params)}" if params else ""
        payload = _json_request(f"{api_root}/{action}{query}")
    if not payload.get("success"):
        raise RuntimeError(f"CKAN action failed: {action}")
    return payload.get("result")


def publisher_id(org_id: str) -> str:
    org_id = str(org_id).strip().lower()
    if not org_id or ":" in org_id:
        raise ValueError(f"invalid catalogue organization id: {org_id!r}")
    return f"nz_{org_id}"


def register_publishers(allocation_path: Path, old_sources_path: Path, out_sources_path: Path) -> dict:
    allocation = load_allocation(allocation_path)
    raw_orgs = _action("organization_list", {"all_fields": "false"}, api_root=LEGACY_API, method="POST")
    if not isinstance(raw_orgs, list):
        raise RuntimeError("organization_list did not return a list")
    orgs = sorted({str(x).strip() for x in raw_orgs if str(x).strip()})
    if not orgs:
        raise RuntimeError("organization_list returned no organization ids")
    for org in orgs:
        allocation = add_assignment(allocation, publisher_id(org), "2026-10-22")
    allocation_path.write_text(json.dumps(allocation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    sources = json.loads(old_sources_path.read_text(encoding="utf-8"))
    sources["collected_date"] = "2026-10-22"
    sources["method"] = sources.get("method", "") + "; New Zealand CKAN organization_list (all_fields=false), publisher assignments registered before package metadata"
    sources["sources"] = [s for s in sources.get("sources", []) if s.get("portal_id") != "nz"]
    sources["sources"].append({
        "portal_id": "nz",
        "portal_url": API,
        "portal_home": PORTAL,
        "publisher_id_prefix": "nz_",
        "organization_names": orgs,
        "country": "New Zealand",
        "list_method": "CKAN organization_list(all_fields=false); publisher ids registered before package_search",
        "license_policy_source": "Dataset-specific licence is in each CKAN package metadata; catalogue API terms require following it",
    })
    sources["sources"].sort(key=lambda item: item["portal_id"])
    out_sources_path.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pools = {str(p["publisher_id"]): p["pool"] for p in allocation["publishers"]}
    train = [o for o in orgs if pools.get(publisher_id(o)) == "train"]
    return {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "catalogue": PORTAL,
        "publisher_ids_registered": len(orgs),
        "train_publishers": len(train),
        "eval2_publishers": sum(pools.get(publisher_id(o)) == "eval2" for o in orgs),
        "eval3_publishers": sum(pools.get(publisher_id(o)) == "eval3" for o in orgs),
        "package_or_dataset_metadata_queried": False,
        "organization_ids": orgs,
        "train_organization_ids": train,
    }


def train_organizations(allocation: dict, sources: dict) -> list[str]:
    source = next((x for x in sources.get("sources", []) if x.get("portal_id") == "nz"), None)
    if not source or source.get("portal_url") != API or source.get("publisher_id_prefix") != "nz_":
        raise ValueError("New Zealand source map is missing the registered catalogue")
    pools = {str(x.get("publisher_id")): x.get("pool") for x in allocation.get("publishers", [])}
    return sorted(
        org for org in map(str, source.get("organization_names", []))
        if pools.get(publisher_id(org)) == "train"
    )


def safe_headers(fields: list[dict]) -> list[str]:
    return [
        name[:100] for item in fields
        if (name := str(item.get("id") or "").strip().lstrip("\ufeff"))
        and not HEADER_DENY.search(normalize_header(name))
    ]


def is_non_japanese(text: str) -> bool:
    return not JAPANESE_SCRIPT.search(text)


def accepted_license(package: dict) -> bool:
    return str(package.get("license_id") or "").strip().lower() in LICENSE_IDS


def signals(headers: list[str]) -> dict:
    code_name = any(CODE_HEADER.search(x) for x in headers) and any(NAME_HEADER.search(x) for x in headers)
    useful = sum(bool(USEFUL_HEADER.search(x)) for x in headers)
    return {
        "code_name_pair_hint": code_name,
        "useful_business_or_statistical_header_count": useful,
        "priority_score": (4 if code_name else 0) + min(useful, 6) + min(len(headers), 10) // 2,
        "hints": (["code/name pair candidate"] if code_name else []) + (["multiple task-oriented headers"] if useful >= 3 else []),
    }


def _package_search(org: str, start: int = 0) -> tuple[list[dict], int]:
    result = _action("package_search", {
        "fq": f"organization:{org}",
        "rows": 100,
        "start": start,
        "sort": "metadata_modified desc",
    })
    if not isinstance(result, dict):
        return [], 0
    packages = result.get("results", [])
    return (packages if isinstance(packages, list) else [], int(result.get("count", 0) or 0))


def _schema(resource_id: str) -> tuple[list[dict], int | None]:
    result = _action("datastore_search", {"resource_id": resource_id, "limit": 0})
    if not isinstance(result, dict):
        return [], None
    # limit=0 is required. If a broken API nevertheless returns rows, discard the result without reading values.
    records = result.get("records") or []
    if records:
        raise RuntimeError("datastore limit=0 unexpectedly returned rows; discarded")
    fields = result.get("fields") or []
    total = result.get("total")
    try:
        total = int(total)
    except (TypeError, ValueError):
        total = None
    return (fields if isinstance(fields, list) else []), total


def _metadata_candidate(org: str, package: dict, resource: dict, headers: list[str], total: int | None) -> dict:
    name = str(package.get("name") or "")
    resource_id = str(resource.get("id") or "")
    organization = package.get("organization") if isinstance(package.get("organization"), dict) else {}
    signals_ = signals(headers)
    return {
        "publisher_id": publisher_id(org),
        "publisher_name": str(organization.get("title") or organization.get("name") or org)[:160],
        "pool": "train",
        "country": "New Zealand",
        "language": "non-Japanese (script screen passed; exact language unverified)",
        "title": str(package.get("title") or name)[:300],
        "resource_name": str(resource.get("name") or "")[:200],
        "catalog_url": f"{PORTAL}/dataset/{name}" if name else "",
        "resource_url": f"{PORTAL}/dataset/{name}/resource/{resource_id}" if name and resource_id else "",
        "resource_id": resource_id,
        "format": str(resource.get("format") or "")[:40],
        "datastore_available": True,
        "datastore_total_rows": total,
        "safe_header_count": len(headers),
        "candidate_columns_capped_at_10": min(len(headers), MAX_HEADERS),
        "safe_headers": headers[:MAX_HEADERS],
        "license": {
            "id": str(package.get("license_id") or "").strip().lower(),
            "title": str(package.get("license_title") or "")[:160],
            "url": str(package.get("license_url") or "")[:500],
            "individual_terms_reviewed": False,
            "candidate_screen": "identifier in permitted CC0/CC-BY/PDL allowlist; original terms require adoption-stage review",
        },
        "metadata_updated": str(resource.get("last_modified") or package.get("metadata_modified") or "")[:50],
        "sample_rows_requested": 0,
        "resource_file_downloaded": False,
        "cell_values_saved": False,
        "manual_review_required": True,
        "structure_orientation": "header-only candidate hint; no values read",
        **signals_,
    }


def _non_datastore(org: str, package: dict, resource: dict) -> dict:
    name = str(package.get("name") or "")
    rid = str(resource.get("id") or "")
    organization = package.get("organization") if isinstance(package.get("organization"), dict) else {}
    return {
        "publisher_id": publisher_id(org),
        "publisher_name": str(organization.get("title") or organization.get("name") or org)[:160],
        "pool": "train",
        "country": "New Zealand",
        "title": str(package.get("title") or name)[:300],
        "resource_name": str(resource.get("name") or "")[:200],
        "catalog_url": f"{PORTAL}/dataset/{name}" if name else "",
        "resource_url": f"{PORTAL}/dataset/{name}/resource/{rid}" if name and rid else "",
        "resource_id": rid,
        "format": str(resource.get("format") or "")[:40],
        "datastore_available": False,
        "license": {
            "id": str(package.get("license_id") or "").strip().lower(),
            "title": str(package.get("license_title") or "")[:160],
            "url": str(package.get("license_url") or "")[:500],
            "individual_terms_reviewed": False,
        },
        "schema_status": "not checked; file not downloaded",
        "resource_file_downloaded": False,
        "cell_values_saved": False,
        "manual_review_required": True,
    }


def choose(candidates: list[dict]) -> list[dict]:
    candidates = sorted(candidates, key=lambda x: (-x["priority_score"], -x["candidate_columns_capped_at_10"], x["publisher_id"], x["title"]))
    selected = []
    publishers = set()
    urls = set()
    for item in candidates:
        if item["publisher_id"] in publishers or item["resource_url"] in urls:
            continue
        publishers.add(item["publisher_id"])
        urls.add(item["resource_url"])
        selected.append(item)
        if len(selected) >= TARGET_TABLES:
            break
    return selected


def discover(allocation: dict, sources: dict) -> dict:
    organizations = train_organizations(allocation, sources)
    candidates: list[dict] = []
    non_datastore: list[dict] = []
    counts: dict[str, int] = defaultdict(int)
    error_types: dict[str, int] = defaultdict(int)
    package_count = schema_count = searched = 0
    for org in organizations:
        searched += 1
        try:
            packages, total = _package_search(org, 0)
            package_count += len(packages)
            if total > len(packages):
                extra, _ = _package_search(org, 100)
                packages.extend(extra)
                package_count += len(extra)
        except Exception as exc:
            counts["package_search_failed"] += 1
            error_types[type(exc).__name__] += 1
            time.sleep(0.35)
            continue
        publisher_schemas = 0
        for package in packages:
            if str(package.get("state") or "active") != "active":
                counts["inactive"] += 1
                continue
            if not accepted_license(package):
                counts["license_not_in_candidate_allowlist"] += 1
                continue
            title = str(package.get("title") or package.get("name") or "")
            if SENSITIVE_TITLE.search(title):
                counts["sensitive_title_excluded"] += 1
                continue
            for resource in package.get("resources", []) or []:
                if schema_count >= MAX_SCHEMA_REQUESTS or publisher_schemas >= MAX_SCHEMA_PER_PUBLISHER:
                    break
                rid = str(resource.get("id") or "").strip()
                if not rid:
                    counts["missing_resource_id"] += 1
                    continue
                if not bool(resource.get("datastore_active")):
                    if not is_non_japanese(title + " " + str(resource.get("name") or "")):
                        counts["japanese_script_excluded"] += 1
                        continue
                    if len(non_datastore) < MAX_NON_DATASTORE:
                        non_datastore.append(_non_datastore(org, package, resource))
                    counts["non_datastore_metadata_only"] += 1
                    continue
                schema_count += 1
                publisher_schemas += 1
                try:
                    fields, total_rows = _schema(rid)
                except Exception as exc:
                    counts["schema_request_failed_or_rows_discarded"] += 1
                    error_types[type(exc).__name__] += 1
                    continue
                headers = safe_headers(fields)
                if len(headers) < MIN_HEADERS:
                    counts["fewer_than_8_safe_headers"] += 1
                    continue
                if not is_non_japanese(title + " " + str(resource.get("name") or "") + " " + " ".join(headers)):
                    counts["japanese_script_excluded"] += 1
                    continue
                candidates.append(_metadata_candidate(org, package, resource, headers, total_rows))
                time.sleep(0.1)
        time.sleep(0.35)

    selected = choose(candidates)
    columns = sum(x["candidate_columns_capped_at_10"] for x in selected)
    return {
        "schema_version": 1,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "stage": "metadata_candidates_only",
        "source_policy": {
            "catalogue": PORTAL,
            "only_preassigned_train_publishers_queried": True,
            "publisher_assignments_committed_before_dataset_metadata": True,
            "license_allowlist": sorted(LICENSE_IDS),
            "license_original_terms_reviewed": False,
            "title_and_header_privacy_screen": "independent_eval/discover.py TITLE_DENY / HEADER_DENY",
            "dataset_files_downloaded": False,
            "datastore_rows_requested": 0,
            "datastore_cells_saved": False,
            "sample_values_saved": False,
        },
        "metrics": {
            "train_publishers_searched": searched,
            "packages_seen": package_count,
            "datastore_schema_requests": schema_count,
            "datastore_ready_candidates": len(candidates),
            "selected_tables": len(selected),
            "selected_publishers": len({x["publisher_id"] for x in selected}),
            "selected_columns_capped_at_10": columns,
            "target_tables_60_met": len(selected) >= TARGET_TABLES,
            "target_columns_450_met": columns >= 450,
            "non_datastore_metadata_candidates_recorded": len(non_datastore),
        },
        "exclusion_and_error_counts": dict(sorted(counts.items())),
        "error_type_counts": dict(sorted(error_types.items())),
        "selected": selected,
        "non_datastore": non_datastore,
    }


def render_markdown(report: dict) -> str:
    m = report["metrics"]
    lines = [
        "# S11 3.4 非日本語の公開表候補 — ニュージーランド（メタデータのみ）", "",
        f"作成日時 UTC: {report['created_at_utc']}", "",
        "## 方法と制約", "",
        "- 公式カタログの organization_list で公開元 ID のみ取得し、全公開元を allocation.py の規則で先に登録。割当コミット後、train 公開元だけを照会しました。",
        "- CKAN package/resource metadata と datastore_search `limit=0` の列スキーマ・行数だけを使用。配布ファイル、データ行、セル値は取得・保存していません。",
        "- 個別 license ID を CC0／CC BY／PDL の候補ふるいに使いました。個別原文規約の確認は Claude の採用後、抽出前に必要です。",
        "- 個人情報・機微情報に関係するタイトルと禁止見出しは除外。見出しは安全判定後の最大10個のみ掲載し、値は未確認です。",
        "- publisher 上限は1表（目標60表の1.67%）に設定。候補であり、採用・抽出・ラベル付けはしていません。", "",
        "## 集計", "",
        f"- train 公開元を検索: {m['train_publishers_searched']}",
        f"- package metadata: {m['packages_seen']} 件 / schema照会: {m['datastore_schema_requests']} 件",
        f"- datastore 候補: {m['datastore_ready_candidates']} 表",
        f"- 選定候補: {m['selected_tables']} 表 / {m['selected_publishers']} 公開元 / 最大10列適用後 {m['selected_columns_capped_at_10']} 列",
        f"- 目標: 60表={'達成' if m['target_tables_60_met'] else '未達'}、450列={'達成' if m['target_columns_450_met'] else '未達'}",
        f"- datastore なし（ファイル未取得、列数目標に不算入）: {m['non_datastore_metadata_candidates_recorded']} 件", "",
        "## datastore 候補", "",
        "| # | 公開元 | 表 / resource | 列（安全見出し） | datastore 行数 | license ID | 列見出しのみの候補ヒント |",
        "|---:|---|---|---:|---:|---|---|",
    ]
    for i, x in enumerate(report["selected"], 1):
        title = (x["title"] + (" / " + x["resource_name"] if x["resource_name"] else "")).replace("|", "／").replace("[", "（").replace("]", "）")
        link = f"[{title}]({x['resource_url']})" if x["resource_url"] else title
        hints = "、".join(x["hints"]) or "見出し構造のみ確認"
        lines.append(f"| {i} | {x['publisher_name']} (`{x['publisher_id']}`, train) | {link} | {x['candidate_columns_capped_at_10']} / {x['safe_header_count']} | {x['datastore_total_rows'] if x['datastore_total_rows'] is not None else '未取得'} | `{x['license']['id']}` ([原文候補]({x['license']['url']})) | {hints} |")
        lines.append("|  |  | 安全な列見出し: " + "、".join(x["safe_headers"]).replace("|", "／") + " |  |  | 原文未精査 | 値未確認 |")
    lines.extend(["", "## datastore なし（メタデータのみ）", "", "| 公開元 | 表 / resource | 形式 | license ID |", "|---|---|---|---|"])
    for x in report["non_datastore"]:
        title = (x["title"] + (" / " + x["resource_name"] if x["resource_name"] else "")).replace("|", "／").replace("[", "（").replace("]", "）")
        link = f"[{title}]({x['resource_url']})" if x["resource_url"] else title
        lines.append(f"| {x['publisher_name']} (`{x['publisher_id']}`) | {link} | {x['format'] or '未記載'} | `{x['license']['id']}` |")
    lines.extend(["", "## 除外・取得エラー", ""])
    if report["exclusion_and_error_counts"]:
        lines.extend(f"- `{k}`: {v}" for k, v in report["exclusion_and_error_counts"].items())
    else:
        lines.append("- なし")
    if report.get("error_type_counts"):
        lines.append("- エラー型: " + "、".join(f"{k} {v}" for k, v in report["error_type_counts"].items()))
    lines.extend(["", "## 次の手順", "", "Claude が候補を採用した後、ライセンス原文・表の対象・日本語以外であることを確認し、承認分だけ抽出・ラベル付けします。", ""])
    return "\n".join(lines)


def self_test() -> None:
    assert publisher_id("ministry-of-health") == "nz_ministry-of-health"
    assert len(safe_headers([{"id": "Amount"}, {"id": "Person Name"}, {"id": "Date"}])) == 2
    assert accepted_license({"license_id": "cc-by-40-intl"})
    assert not accepted_license({"license_id": "cc-by-sa"})
    base = {"publisher_id": "nz_org1", "priority_score": 1, "candidate_columns_capped_at_10": 8,
            "safe_headers": ["a", "b"], "resource_url": "u1", "title": "A"}
    chosen = choose([base, dict(base, publisher_id="nz_org2", resource_url="u2")])
    assert len(chosen) == 2  # separate publishers remain eligible with similar headings
    print("S11 3.4 New Zealand metadata discovery self-test passed")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--mode", choices={"register", "discover"})
    parser.add_argument("--run-date")
    args = parser.parse_args(argv)
    if args.self_test:
        self_test()
        return 0
    if args.mode == "register":
        report = register_publishers(
            ROOT / "independent_eval/allocation.json",
            ROOT / "independent_eval/allocation_sources_20261021.json",
            ROOT / "independent_eval/allocation_sources_20261022.json",
        )
        out = ROOT / f"materials/s11_3_4_nz_registration_{args.run_date}.json"
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"New Zealand publishers registered={report['publisher_ids_registered']} train={report['train_publishers']}; no dataset metadata queried")
        return 0
    if args.mode == "discover":
        allocation = load_allocation(ROOT / "independent_eval/allocation.json")
        sources = json.loads((ROOT / "independent_eval/allocation_sources_20261022.json").read_text(encoding="utf-8"))
        report = discover(allocation, sources)
        (ROOT / f"materials/s11_3_4_candidates_{args.run_date}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (ROOT / f"materials/s11_3_4_candidates_{args.run_date}.md").write_text(render_markdown(report), encoding="utf-8")
        m = report["metrics"]
        print(f"S11 3.4 complete: publishers={m['train_publishers_searched']} candidates={m['datastore_ready_candidates']} selected={m['selected_tables']} columns={m['selected_columns_capped_at_10']}")
        return 0
    parser.error("--mode register/discover または --self-test が必要です")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
