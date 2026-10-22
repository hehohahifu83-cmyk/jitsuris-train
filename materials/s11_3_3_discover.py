#!/usr/bin/env python3
"""S11 3.3: discover Japanese statistical-table candidates from BODIK metadata.

This stage reads only CKAN package/resource metadata and datastore field schema.
It never downloads a resource file or requests datastore rows (limit=0 only).
Only already-registered BODIK publishers assigned to the train pool are queried.
"""
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
from urllib.parse import quote, urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from independent_eval.discover import HEADER_DENY, TITLE_DENY, normalize_header  # noqa: E402

API = "https://data.bodik.jp/api/3/action"
ALLOWED_HOST = "data.bodik.jp"
ACCEPTED_LICENSES = {"cc-by", "cc-by-40-intl", "cc-by-4.0", "cc-by-30", "cc-by-21-jp"}
SEARCH_QUERY = (
    "統計 OR 人口 OR 世帯 OR 年齢 OR 産業 OR 事業所 OR 観光 OR 農業 OR 農林 OR "
    "漁業 OR 水産 OR 医療 OR 保健 OR 福祉 OR 教育 OR 学校 OR 指数 OR 就業 OR 生産"
)
TITLE_STATS = re.compile(
    r"統計|人口|世帯|年齢|就業|産業|事業所|観光|農業|農林|林業|漁業|水産|医療|保健|"
    r"福祉|教育|学校|指数|家計|生産|商業|工業|労働|国勢|出生|婚姻|地価|作物|収穫|"
    r"港湾|交通|市勢|診療科|推移|構成比|分布|統計書|統計年鑑|統計表",
    re.I,
)
YEAR_ONLY = re.compile(r"^(?:19|20)[0-9０-９]{2}(?:年度|年)?$")
AGE_BAND = re.compile(r"[0-9０-９]+\s*(?:歳|才)\s*(?:[〜～~\-－–]|以上|以下|未満)")
CODE_WORD = re.compile(r"(?:コード|code|分類番号|地域番号)", re.I)
NAME_WORD = re.compile(r"(?:名称|名称.*|項目名|分類名|区分名|label|title)", re.I)
HIERARCHY = re.compile(r"(?:大分類|中分類|小分類|細分類|階級|区分|分類)")
INDEX_WORD = re.compile(r"(?:指数|率|割合|構成比|指標|増減率|伸び率)")
ANSWER_CODE = re.compile(r"(?:回答.*コード|選択肢.*コード|回答番号|設問番号)")
WIDE_CATEGORY = re.compile(r"(?:男性|女性|男女|総数|年齢|産業|診療|分類|階級|区分|部門|品目)")
MAX_SELECTED = 100
MAX_COLUMNS_PER_TABLE = 10
MIN_SAFE_HEADERS = 7
MAX_PER_PUBLISHER = 3
MAX_NON_DATASTORE = 200


class MetadataOnlyError(RuntimeError):
    pass


def _json_request(url: str, *, retries: int = 4) -> dict:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != ALLOWED_HOST:
        raise ValueError("request host is outside the BODIK metadata allowlist")
    for attempt in range(retries):
        req = Request(url, headers={"User-Agent": "jitsuris-s11-metadata-discovery/1.0", "Accept": "application/json"})
        try:
            with urlopen(req, timeout=30) as response:
                return json.loads(response.read(10_000_001).decode("utf-8-sig"))
        except HTTPError as exc:
            if exc.code not in {403, 408, 425, 429, 500, 502, 503, 504} or attempt + 1 == retries:
                raise
            time.sleep(1.0 + 2.0 * attempt)
        except (TimeoutError, URLError, OSError):
            if attempt + 1 == retries:
                raise
            time.sleep(1.0 + 2.0 * attempt)
    raise RuntimeError("metadata request retries exhausted")


def _action(url: str, action: str) -> dict:
    payload = _json_request(url)
    if not payload.get("success"):
        raise RuntimeError(f"CKAN action failed: {action}")
    result = payload.get("result")
    if not isinstance(result, dict):
        raise RuntimeError(f"CKAN action returned no result: {action}")
    return result


def train_bodik_organizations(allocation: dict, sources: dict) -> list[str]:
    pools = {str(x.get("publisher_id")): x.get("pool") for x in allocation.get("publishers", [])}
    bodik = next((x for x in sources.get("sources", []) if x.get("portal_id") == "bodik"), None)
    if not bodik or bodik.get("portal_url") != API:
        raise ValueError("allocation source map is missing the expected BODIK portal")
    return sorted({
        str(org) for org in bodik.get("organization_names", [])
        if str(org) in pools and pools[str(org)] == "train"
    })


def is_statistical_title(title: str, resource_name: str = "") -> bool:
    combined = f"{title} {resource_name}"
    return bool(TITLE_STATS.search(combined) and not TITLE_DENY.search(combined))


def safe_headers(fields: list[dict]) -> list[str]:
    kept = []
    for item in fields:
        name = str(item.get("id") or "").strip().lstrip("\ufeff")
        if name and not HEADER_DENY.search(normalize_header(name)):
            kept.append(name[:100])
    return kept


def schema_signals(headers: list[str]) -> dict:
    age = sum(bool(AGE_BAND.search(x)) for x in headers)
    code = any(CODE_WORD.search(x) for x in headers)
    label = any(NAME_WORD.search(x) for x in headers)
    hierarchy = sum(bool(HIERARCHY.search(x)) for x in headers)
    index = sum(bool(INDEX_WORD.search(x)) for x in headers)
    answer = any(ANSWER_CODE.search(x) for x in headers)
    wide_category = sum(bool(WIDE_CATEGORY.search(x)) for x in headers)
    years_only = sum(bool(YEAR_ONLY.fullmatch(normalize_header(x))) for x in headers)
    code_name_pair = code and label
    wide_hint = age >= 2 or (wide_category >= 3 and len(headers) >= 10) or len(headers) >= 15
    hints = []
    if age >= 2:
        hints.append("年齢階級見出しが複数")
    if wide_category >= 3 and len(headers) >= 10:
        hints.append("分類・階層見出しが複数")
    if len(headers) >= 15:
        hints.append("安全な列見出しが15以上（横持ちかは未確認）")
    if code_name_pair:
        hints.append("コード列と名称列の対候補")
    if hierarchy:
        hints.append("分類・階層語を含む見出し")
    if index:
        hints.append("指数・率・割合の見出し")
    if answer:
        hints.append("回答コード関連の見出し")
    if years_only and years_only >= max(2, len(headers) * 0.6) and not (age or code_name_pair or hierarchy or index):
        hints.append("年だけの見出しが多く要確認")
    score = (5 if wide_hint else 0) + (4 if age >= 2 else 0) + (3 if code_name_pair else 0)
    score += min(hierarchy, 3) + min(index, 3) + (2 if answer else 0)
    score += min(3, len(headers) // 5)
    return {
        "wide_hint": wide_hint,
        "age_band_header_count": age,
        "wide_category_header_count": wide_category,
        "code_name_pair_hint": code_name_pair,
        "hierarchy_header_count": hierarchy,
        "index_rate_header_count": index,
        "answer_code_hint": answer,
        "year_only_header_count": years_only,
        "priority_score": score,
        "hints": hints,
    }


def _package_page(package_name: str) -> str:
    return f"https://data.bodik.jp/dataset/{quote(package_name, safe='') }"


def _resource_page(package_name: str, resource_id: str) -> str:
    return f"{_package_page(package_name)}/resource/{quote(resource_id, safe='')}"


def _search_packages(org: str, *, rows: int = 100) -> list[dict]:
    params = {
        "q": SEARCH_QUERY,
        "fq": f"organization:{org}",
        "rows": rows,
        "start": 0,
        "sort": "metadata_modified desc",
    }
    result = _action(f"{API}/package_search?{urlencode(params)}", "package_search")
    packages = result.get("results", [])
    return packages if isinstance(packages, list) else []


def _schema(resource_id: str) -> tuple[list[dict], int]:
    params = {"resource_id": resource_id, "limit": 0}
    result = _action(f"{API}/datastore_search?{urlencode(params)}", "datastore_search")
    records = result.get("records") or []
    if records:
        # Do not inspect, print, or persist any returned cell values.
        raise MetadataOnlyError("datastore limit=0 unexpectedly returned rows")
    fields = result.get("fields") or []
    total = result.get("total")
    try:
        total = int(total)
    except (TypeError, ValueError):
        total = None
    return fields if isinstance(fields, list) else [], total


def _license(package: dict) -> dict:
    license_id = str(package.get("license_id") or "").strip().lower()
    return {
        "id": license_id,
        "title": str(package.get("license_title") or "")[:160],
        "url": str(package.get("license_url") or "")[:400],
        "accepted_identifier_for_candidate_screen": license_id in ACCEPTED_LICENSES,
        "terms_review": "個別CKANメタデータの識別子のみ。原文規約の確認は採用前に必要",
    }


def _stat_candidate(org: str, package: dict, resource: dict, fields: list[dict], total: int) -> dict | None:
    title = str(package.get("title") or package.get("name") or "").strip()
    resource_name = str(resource.get("name") or "").strip()
    headers = safe_headers(fields)
    if len(headers) < MIN_SAFE_HEADERS:
        return None
    signals = schema_signals(headers)
    # Mostly year-only schema with no useful category/code/context is excluded
    # from the 3.3 target to avoid columns likely to be unknown under the guide.
    if "年だけの見出しが多く要確認" in signals["hints"] and not signals["wide_hint"]:
        return None
    pkg_name = str(package.get("name") or "").strip()
    resource_id = str(resource.get("id") or "").strip()
    resource_url = str(resource.get("url") or "").strip()
    catalog_url = _package_page(pkg_name) if pkg_name else ""
    return {
        "publisher_id": org,
        "pool": "train",
        "title": title[:300],
        "resource_name": resource_name[:200],
        "catalog_url": catalog_url,
        "resource_url": _resource_page(pkg_name, resource_id) if pkg_name and resource_id else "",
        "download_url_metadata": resource_url[:500],
        "resource_id": resource_id,
        "format": str(resource.get("format") or "").strip()[:40],
        "datastore_available": True,
        "datastore_total_rows": total,
        "safe_header_count": len(headers),
        "candidate_columns_capped_at_10": min(len(headers), MAX_COLUMNS_PER_TABLE),
        "safe_headers": headers[:MAX_COLUMNS_PER_TABLE],
        "license": _license(package),
        "metadata_updated": str(resource.get("last_modified") or package.get("metadata_modified") or "")[:50],
        "sample_rows_requested": 0,
        "resource_file_downloaded": False,
        "cell_values_saved": False,
        "manual_review_required": True,
        "structure_orientation": "列見出しからの候補ヒントのみ。横持ちかは値を見ずに確定していない",
        **signals,
    }


def _non_datastore(org: str, package: dict, resource: dict) -> dict:
    pkg_name = str(package.get("name") or "").strip()
    resource_id = str(resource.get("id") or "").strip()
    return {
        "publisher_id": org,
        "pool": "train",
        "title": str(package.get("title") or pkg_name)[:300],
        "resource_name": str(resource.get("name") or "")[:200],
        "catalog_url": _package_page(pkg_name) if pkg_name else "",
        "resource_url": _resource_page(pkg_name, resource_id) if pkg_name and resource_id else "",
        "download_url_metadata": str(resource.get("url") or "")[:500],
        "resource_id": resource_id,
        "format": str(resource.get("format") or "").strip()[:40],
        "datastore_available": False,
        "safe_header_count": None,
        "candidate_columns_capped_at_10": None,
        "license": _license(package),
        "schema_status": "未確認（datastoreなし。ファイル未取得）",
        "resource_file_downloaded": False,
        "cell_values_saved": False,
        "manual_review_required": True,
    }


def choose_candidates(candidates: list[dict], target: int = MAX_SELECTED) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in candidates:
        grouped[item["publisher_id"]].append(item)
    for publisher, items in grouped.items():
        items.sort(key=lambda x: (-x["priority_score"], -(x.get("candidate_columns_capped_at_10") or 0), x["title"], x["resource_url"]))
        seen_signatures = set()
        unique = []
        for item in items:
            signature = tuple(sorted(normalize_header(x) for x in item["safe_headers"]))
            if signature in seen_signatures:
                continue
            seen_signatures.add(signature)
            unique.append(item)
        grouped[publisher] = unique
    publishers = sorted(grouped, key=lambda p: (-grouped[p][0]["priority_score"], p))
    chosen: list[dict] = []
    for round_index in range(MAX_PER_PUBLISHER):
        for publisher in publishers:
            items = grouped[publisher]
            if round_index < len(items) and len(chosen) < target:
                chosen.append(items[round_index])
        if len(chosen) >= target:
            break
    return chosen


def run_self_test() -> None:
    allocation = {"publishers": [
        {"publisher_id": "100001", "pool": "train"},
        {"publisher_id": "100002", "pool": "eval3"},
    ]}
    sources = {"sources": [{"portal_id": "bodik", "portal_url": API,
                             "organization_names": ["100001", "100002", "999999"]}]}
    assert train_bodik_organizations(allocation, sources) == ["100001"]
    assert not is_statistical_title("人口統計", "患者名簿")
    headers = safe_headers([{"id": "コード"}, {"id": "名称"}, {"id": "20歳～29歳"},
                            {"id": "30歳～39歳"}, {"id": "氏名"}, {"id": "住所"},
                            {"id": "男性"}, {"id": "女性"}, {"id": "総数"},
                            {"id": "年齢"}, {"id": "産業"}, {"id": "分類"}])
    assert "氏名" not in headers and "住所" not in headers
    signals = schema_signals(headers)
    assert signals["code_name_pair_hint"] and signals["age_band_header_count"] == 2
    assert signals["wide_hint"]
    sample = {"publisher_id": "100001", "priority_score": 8,
              "candidate_columns_capped_at_10": 7, "title": "統計", "resource_url": "u",
              "safe_headers": ["コード", "名称", "A", "B", "C", "D", "E"]}
    chosen = choose_candidates([sample, dict(sample)], target=10)
    assert chosen == [sample]
    distinct = [dict(sample, resource_url=str(i), safe_headers=sample["safe_headers"] + [f"列{i}"])
                for i in range(4)]
    assert len(choose_candidates(distinct)) == MAX_PER_PUBLISHER
    print("S11 3.3 metadata discovery self-test passed")


def discover(allocation: dict, source_map: dict, *, max_organizations: int | None = None) -> dict:
    organizations = train_bodik_organizations(allocation, source_map)
    if max_organizations is not None:
        organizations = organizations[:max_organizations]
    candidates: list[dict] = []
    no_datastore: list[dict] = []
    errors: dict[str, int] = defaultdict(int)
    searched = 0
    packages_seen = 0
    schema_calls = 0
    for org in organizations:
        searched += 1
        try:
            packages = _search_packages(org)
        except Exception:
            errors["package_search_failed"] += 1
            time.sleep(0.08)
            continue
        packages_seen += len(packages)
        for package in packages:
            if str(package.get("state") or "active") != "active":
                errors["inactive"] += 1
                continue
            license_info = _license(package)
            if not license_info["accepted_identifier_for_candidate_screen"]:
                errors["license_not_in_candidate_allowlist"] += 1
                continue
            title = str(package.get("title") or package.get("name") or "")
            if TITLE_DENY.search(title):
                errors["title_privacy_screen"] += 1
                continue
            for resource in package.get("resources", []) or []:
                resource_name = str(resource.get("name") or "")
                if not is_statistical_title(title, resource_name):
                    continue
                url = str(resource.get("url") or "")
                if not url or urlparse(url).scheme != "https" or urlparse(url).hostname not in {ALLOWED_HOST}:
                    errors["resource_host_not_allowed"] += 1
                    continue
                resource_id = str(resource.get("id") or "").strip()
                if not bool(resource.get("datastore_active")):
                    if len(no_datastore) < MAX_NON_DATASTORE:
                        no_datastore.append(_non_datastore(org, package, resource))
                    errors["no_datastore"] += 1
                    continue
                if not resource_id:
                    errors["missing_resource_id"] += 1
                    continue
                schema_calls += 1
                try:
                    fields, total = _schema(resource_id)
                except MetadataOnlyError:
                    errors["limit_zero_returned_rows_discarded"] += 1
                    continue
                except Exception:
                    errors["schema_request_failed"] += 1
                    continue
                item = _stat_candidate(org, package, resource, fields, total)
                if item:
                    candidates.append(item)
                else:
                    errors["schema_not_suitable_for_3_3_target"] += 1
                time.sleep(0.04)
        time.sleep(0.04)
    chosen = choose_candidates(candidates)
    selected_columns = sum(x["candidate_columns_capped_at_10"] for x in chosen)
    return {
        "schema_version": 1,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "stage": "metadata_candidates_only",
        "source_policy": {
            "catalog": "BODIK CKAN only",
            "only_preassigned_train_publishers": True,
            "new_publisher_assignments_created": False,
            "dataset_license_ids_screened": sorted(ACCEPTED_LICENSES),
            "individual_license_text_reviewed": False,
            "e_stat_queried": False,
            "resource_files_downloaded": False,
            "datastore_rows_requested": 0,
            "datastore_cells_saved": False,
            "sample_values_saved": False,
            "privacy_values_screened": False,
            "safe_header_denylist": "independent_eval/discover.py HEADER_DENY",
            "title_denylist": "independent_eval/discover.py TITLE_DENY",
        },
        "metrics": {
            "train_bodik_publishers_searched": searched,
            "packages_seen_from_scoped_queries": packages_seen,
            "datastore_schema_requests": schema_calls,
            "datastore_ready_candidates": len(candidates),
            "selected_tables": len(chosen),
            "selected_publishers": len({x["publisher_id"] for x in chosen}),
            "selected_columns_capped_at_10": selected_columns,
            "wide_header_hint_tables": sum(bool(x["wide_hint"]) for x in chosen),
            "code_name_pair_hint_tables": sum(bool(x["code_name_pair_hint"]) for x in chosen),
            "non_datastore_metadata_candidates_recorded": len(no_datastore),
            "target_tables_100_met": len(chosen) >= 100,
            "target_columns_700_met": selected_columns >= 700,
        },
        "exclusion_and_error_counts": dict(sorted(errors.items())),
        "selected": chosen,
        "non_datastore": no_datastore,
    }


def render_markdown(report: dict) -> str:
    m = report["metrics"]
    lines = [
        "# S11 3.3 統計表候補（メタデータのみ）",
        "",
        f"作成日時 UTC: {report['created_at_utc']}",
        "",
        "## 調査方法と制約",
        "",
        "- allocation.json で事前に train と割り当て済みの BODIK 公開元だけを検索。新しい割当は作成していません。",
        "- CKAN package/resource metadata と datastore_search の `limit=0` による列スキーマ・総行数だけを取得しました。配布ファイル、行、セル値は取得・保存していません。",
        "- ライセンスは個別 CKAN metadata の ID を候補スクリーニングに使用。原文規約は未精査で、採用前の確認が必要です。",
        "- 横持ち・コード対等は列見出しからの候補ヒントで、表の値を確認していないため形式は未確定です。年だけの列が中心と推定される表は候補から外しました。",
        "- e-Stat はこの調査では照会していません。非datastore候補は下段に分け、列数目標の計算に入れていません。",
        "",
        "## 集計",
        "",
        f"- 検索した train 公開元: {m['train_bodik_publishers_searched']}",
        f"- datastore 対応候補: {m['datastore_ready_candidates']} 件（表スキーマを取得できたもの）",
        f"- 選定候補: {m['selected_tables']} 表 / {m['selected_publishers']} 公開元 / 上限適用後 {m['selected_columns_capped_at_10']} 列",
        f"- 横持ち構造の見出しヒントあり: {m['wide_header_hint_tables']} 表。コード＋名称の対ヒントあり: {m['code_name_pair_hint_tables']} 表。",
        f"- 目安達成: 100表={'達成' if m['target_tables_100_met'] else '未達'}, 700列={'達成' if m['target_columns_700_met'] else '未達'}",
        f"- 非datastore候補（ファイル未取得・見出し未確認）: {m['non_datastore_metadata_candidates_recorded']} 件",
        "",
        "## datastore 対応候補",
        "",
        "| # | 公開元 ID | データセット / resource | 列数（採用上限10） | datastore 行数 | license ID | 列構造ヒント |",
        "|---:|---|---|---:|---:|---|---|",
    ]
    for i, x in enumerate(report["selected"], 1):
        title = (x["title"] + (" / " + x["resource_name"] if x["resource_name"] else "")).replace("|", "／")
        title = title.replace("[", "（").replace("]", "）")
        link = f"[{title}]({x['resource_url']})" if x["resource_url"] else title
        row_count = str(x["datastore_total_rows"]) if x["datastore_total_rows"] is not None else "未取得"
        hints = "、".join(x["hints"]) or "広いスキーマ候補（方向は未確認）"
        lines.append(f"| {i} | {x['publisher_id']} (train) | {link} | {x['candidate_columns_capped_at_10']} / {x['safe_header_count']} | {row_count} | `{x['license']['id']}` | {hints} |")
        lines.append("|  |  | 安全な列見出し: " + "、".join(x["safe_headers"]).replace("|", "／") + " |  |  | 原文未精査 | 値未確認 |")
    lines.extend([
        "",
        "## 非datastore候補（見出し未確認・列目標に算入せず）",
        "",
        "以下はCKAN metadata上のタイトル・形式・個別license IDだけを記録しています。XLSX等の配布ファイルは開いていません。",
        "",
        "| 公開元 ID | データセット / resource | 形式 | license ID | datastore |",
        "|---|---|---|---|---|",
    ])
    for x in report["non_datastore"]:
        title = (x["title"] + (" / " + x["resource_name"] if x["resource_name"] else "")).replace("|", "／")
        title = title.replace("[", "（").replace("]", "）")
        link = f"[{title}]({x['resource_url']})" if x["resource_url"] else title
        lines.append(f"| {x['publisher_id']} (train) | {link} | {x['format'] or '未記載'} | `{x['license']['id']}` | なし |")
    lines.extend(["", "## 除外・取得エラー数", ""])
    if report["exclusion_and_error_counts"]:
        for reason, count in report["exclusion_and_error_counts"].items():
            lines.append(f"- `{reason}`: {count}")
    else:
        lines.append("- なし")
    lines.extend(["", "## 次の手順", "", "Claude が採用する候補を決め、個別ライセンス原文とデータ内容のプライバシー条件を別段で確認してください。これは候補一覧であり、採用・抽出・学習用ラベル付けは行っていません。", ""])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--allocation", type=Path, default=ROOT / "independent_eval/allocation.json")
    parser.add_argument("--sources", type=Path, default=ROOT / "independent_eval/allocation_sources_20261021.json")
    parser.add_argument("--out-json", type=Path)
    parser.add_argument("--out-md", type=Path)
    parser.add_argument("--max-organizations", type=int)
    args = parser.parse_args(argv)
    if args.self_test:
        run_self_test()
        return 0
    if not args.out_json or not args.out_md:
        parser.error("--out-json と --out-md は候補調査の実行に必要です")
    allocation = json.loads(args.allocation.read_text(encoding="utf-8"))
    source_map = json.loads(args.sources.read_text(encoding="utf-8"))
    report = discover(allocation, source_map, max_organizations=args.max_organizations)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text(render_markdown(report), encoding="utf-8")
    m = report["metrics"]
    print("S11 3.3 metadata-only discovery complete")
    print(f"publishers={m['train_bodik_publishers_searched']} datastore_candidates={m['datastore_ready_candidates']} selected={m['selected_tables']} columns={m['selected_columns_capped_at_10']}")
    print(f"target_tables_100={m['target_tables_100_met']} target_columns_700={m['target_columns_700_met']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
