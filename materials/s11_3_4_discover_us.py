#!/usr/bin/env python3
"""S11 3.4 world catalogue registry and metadata-only table discovery."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from independent_eval.allocation import load_allocation, normalize_publisher_id, pool, validate_allocation  # noqa: E402
from independent_eval.discover import HEADER_DENY, TITLE_DENY, normalize_header  # noqa: E402

DATE = "2026-10-22"
TARGET_TABLES = 67
MAX_PER_PUBLISHER = 2
MIN_SAFE_HEADERS = 8
MAX_HEADERS = 10
MAX_BYTES = 20_000_000
DATAPORTALS_CSV = "https://raw.githubusercontent.com/okfn/dataportals.org/3665762ef571ff0027b80842e8f62641c3a2292d/data/portals.csv"
SOCRATA_SERVICE = "https://raw.githubusercontent.com/cyanheads/socrata-mcp-server/020153743c1d528a44b3d517f7e8bd59fa975db3/src/services/socrata/socrata-service.ts"
RAW_HOST = "raw.githubusercontent.com"
SOCRATA_US_API = "https://api.us.socrata.com/api/catalog/v1"
SOCRATA_EU_API = "https://api.eu.socrata.com/api/catalog/v1"
SOCRATA_US_HOST = "api.us.socrata.com"
SOCRATA_EU_HOST = "api.eu.socrata.com"
EXCLUDED_COUNTRIES = {
    "uk", "gb", "united kingdom", "great britain", "england", "ireland", "ie",
    "canada", "ca", "australia", "au", "japan", "jp", "new zealand", "nz", "jersey", "je",
}
COUNTRY_TO_CODE = {
    "united states": "US", "usa": "US", "united states of america": "US",
    "switzerland": "CH", "germany": "DE", "italy": "IT", "spain": "ES",
    "brazil": "BR", "nepal": "NP", "palestine": "PS", "south africa": "ZA",
    "european union": "EU", "europe": "EU", "jersey": "JE",
}
NYC_DOMAIN = re.compile(r"(?:^|[.-])(?:nyc|new-york-city|cityofnewyork)(?:[.-]|$)", re.I)
JAPANESE_SCRIPT = re.compile(r"[ぁ-んァ-ヶ一-龯々〆〤]")
CODE_HEADER = re.compile(r"(?:code|_id$|^id$|identifier|number$)", re.I)
NAME_HEADER = re.compile(r"(?:name|title|description|label)", re.I)
USEFUL_HEADER = re.compile(
    r"(?:amount|total|quantity|qty|unit|price|rate|tax|account|category|class|code|id|date|"
    r"name|description|order|invoice|product|department|value|count|number|status|type|"
    r"measure|index|ratio|percent|revenue|expenditure|budget|population|employment|"
    r"statistic|spend|payment|income|expense|cost|salary|wage|trade)", re.I
)
LICENSE_IDS = {
    "cc-by-2.1-jp", "cc-by-2.1", "cc-by-21", "cc-by-3.0", "cc-by-30",
    "cc-by-30-us", "cc-by-30-intl", "cc-by-4.0", "cc-by-40", "cc-by-40-intl",
    "cc0", "cc-zero", "cc0-1.0", "pdl-1.0", "us-pd", "us-public-domain",
    "us-gov-public-domain", "us-government-work", "government-standard-terms-1.0",
    "government-standard-terms-2.0", "gov-standard-terms-1.0", "gov-standard-terms-2.0",
    "ogl-3.0", "open-government-licence-canada", "open-government-license-canada",
    "singapore-open-data-licence", "singapore-open-data-licence-1.0",
    "singapore-open-data-license", "singapore-open-data-license-1.0",
}
QUERY_TERMS = {
    "en": ["statistics", "budget", "finance", "population", "employment", "trade", "education", "price", "tax"],
    "pt": ["estatística", "orçamento", "despesa", "receita", "população", "emprego", "comércio", "educação"],
    "es": ["estadística", "presupuesto", "gasto", "ingreso", "población", "empleo", "comercio", "educación"],
    "de": ["statistik", "haushalt", "ausgaben", "einnahmen", "bevölkerung", "beschäftigung", "handel"],
    "fr": ["statistique", "budget", "dépense", "recette", "population", "emploi", "commerce", "éducation"],
    "it": ["statistica", "bilancio", "spesa", "entrate", "popolazione", "occupazione", "commercio"],
}


def _host(url: str) -> str:
    return (urlparse(url).hostname or "").lower()


def _safe_url(url: str, allowed_host: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or (parsed.hostname or "").lower() != allowed_host.lower():
        raise ValueError("request host is outside the registered metadata allowlist")


def _get_bytes(url: str, allowed_host: str, retries: int = 3) -> bytes:
    _safe_url(url, allowed_host)
    for attempt in range(retries):
        req = Request(url, headers={
            "User-Agent": "jitsuris-s11-metadata-discovery/1.0",
            "Accept": "application/json,text/csv,text/plain",
        })
        try:
            with urlopen(req, timeout=40) as response:
                final_host = _host(response.geturl())
                if final_host != allowed_host.lower():
                    raise ValueError("metadata response redirected outside the registered host")
                data = response.read(MAX_BYTES + 1)
                if len(data) > MAX_BYTES:
                    raise RuntimeError("metadata response exceeded safety cap")
                return data
        except HTTPError as exc:
            if exc.code not in {408, 425, 429, 500, 502, 503, 504} or attempt + 1 == retries:
                raise
            time.sleep(1.0 + 2.0 * attempt)
        except (TimeoutError, URLError, OSError):
            if attempt + 1 == retries:
                raise
            time.sleep(1.0 + 2.0 * attempt)
    raise RuntimeError("metadata request retries exhausted")


def _json(url: str, allowed_host: str) -> dict:
    return json.loads(_get_bytes(url, allowed_host).decode("utf-8-sig"))


def _country_code(country: str) -> str:
    value = str(country or "").strip()
    if value.upper() in {"US", "GB", "UK", "IE", "CA", "AU", "NZ", "JP", "BR", "DE", "ES", "IT", "CH", "PS", "ZA", "JE", "EU", "NP"}:
        return value.upper()
    return COUNTRY_TO_CODE.get(value.casefold(), value.upper()[:2])


def _excluded_country(country: str, domain: str = "") -> bool:
    value = str(country or "").strip().casefold()
    if value in EXCLUDED_COUNTRIES:
        return True
    host = str(domain or "").strip().lower()
    if host.endswith((".gov.uk", ".ac.uk", ".ie", ".gov.ie", ".ca", ".gov.ca", ".gc.ca",
                      ".gov.au", ".edu.au", ".nz", ".govt.nz", ".jp")):
        return True
    return False


def _publisher_id(platform: str, domain: str, organization: str = "") -> str:
    raw = f"world_{platform}_{domain}_{organization}".strip("_").lower()
    raw = re.sub(r"[^a-z0-9]+", "_", raw).strip("_")
    if not raw:
        raise ValueError("publisher identity is empty")
    return raw


def _socrata_domains(ts_text: str) -> list[dict]:
    results = []
    for line in ts_text.splitlines():
        match = re.search(r"\{ domain: '([^']+)', organization: '([^']+)' \}", line)
        if match:
            domain, org = match.groups()
            results.append({"domain": domain.lower(), "title": org, "country": "US",
                            "platform": "socrata", "registry_id": "cyanheads-known-portals"})
    return results


def registry_sources() -> list[dict]:
    csv_host = RAW_HOST
    csv_bytes = _get_bytes(DATAPORTALS_CSV, csv_host)
    rows = csv.DictReader(io.StringIO(csv_bytes.decode("utf-8-sig")))
    sources: dict[str, dict] = {}
    for row in rows:
        if str(row.get("status") or "").strip().lower() != "active":
            continue
        api_type = str(row.get("api_type") or "").strip()
        platform = "ckan" if "ckan" in api_type.lower() else "socrata" if "socrata" in api_type.lower() else ""
        if not platform:
            continue
        homepage = str(row.get("url") or "").strip()
        api_root = str(row.get("api_endpoint") or "").strip().rstrip("/")
        country = str(row.get("country") or "").strip()
        domain = _host(homepage)
        if not domain or _excluded_country(country, domain):
            continue
        if platform == "ckan":
            if not api_root or urlparse(api_root).scheme != "https":
                continue
            if not _host(api_root):
                continue
        else:
            if domain.endswith(".opendata.arcgis.com"):
                continue
        entry = {
            "domain": domain, "portal_url": homepage, "api_root": api_root,
            "platform": platform, "country": _country_code(country), "language": str(row.get("language") or ""),
            "directory_id": str(row.get("name") or ""), "directory_title": str(row.get("title") or ""),
            "registry_id": "okfn-dataportals",
        }
        sources[domain] = entry

    socrata_bytes = _get_bytes(SOCRATA_SERVICE, RAW_HOST)
    for entry in _socrata_domains(socrata_bytes.decode("utf-8")):
        domain = entry["domain"]
        if _excluded_country(entry["country"], domain):
            continue
        prior = sources.get(domain, {})
        entry.update({
            "portal_url": f"https://{domain}/",
            "api_root": SOCRATA_EU_API if entry["country"] in {"IT", "ES", "DE", "CH", "EU"} else SOCRATA_US_API,
            "language": prior.get("language", "en"),
            "directory_id": prior.get("directory_id", ""),
        })
        sources[domain] = {**prior, **entry}

    cleaned = []
    for domain, source in sorted(sources.items()):
        source["publisher_ids"] = []
        source["registry_status"] = "listed"
        source["catalog_access"] = "not checked"
        if NYC_DOMAIN.search(domain):
            source["protected_alias"] = True
        cleaned.append(source)
    if not cleaned:
        raise RuntimeError("pinned world portal registries returned no eligible catalogues")
    return cleaned


def _ckan_action_url(api_root: str, action: str, params: dict) -> list[str]:
    root = api_root.rstrip("/")
    bases = [root] if root.endswith("/action") else [root + "/action", root]
    query = urlencode(params)
    return [f"{base}/{action}?{query}" for base in dict.fromkeys(bases)]


def _ckan_result(api_root: str, action: str, params: dict) -> object:
    last_error: Exception | None = None
    for url in _ckan_action_url(api_root, action, params):
        host = _host(url)
        try:
            payload = _json(url, host)
            if payload.get("success"):
                return payload.get("result")
            last_error = RuntimeError("CKAN action returned success=false")
        except Exception as exc:
            last_error = exc
    if last_error:
        raise last_error
    raise RuntimeError(f"CKAN action failed: {action}")


def register_publishers(allocation_path: Path, sources_path: Path, report_path: Path) -> dict:
    allocation = load_allocation(allocation_path)
    sources = registry_sources()
    ckan_catalogues = 0
    ckan_orgs = 0
    socrata_sources = 0
    source_records = []
    existing_pools = {
        normalize_publisher_id(x["publisher_id"]): x["pool"]
        for x in allocation["publishers"]
    }
    alias_names = {normalize_publisher_id(x) for x in allocation.get("aliases", {})}
    pending_records: dict[str, dict] = {}

    def reserve_publisher(publisher_id: str) -> str:
        canonical = normalize_publisher_id(publisher_id)
        if canonical in alias_names:
            raise ValueError(f"world publisher collides with a registered alias: {canonical}")
        if canonical in existing_pools:
            return existing_pools[canonical]
        if canonical in pending_records:
            return pending_records[canonical]["pool"]
        if not canonical.startswith("world_") or ":" in canonical:
            raise ValueError("batch registration only accepts generated world publisher IDs")
        assigned_pool = pool(canonical)
        pending_records[canonical] = {
            "publisher_id": canonical, "pool": assigned_pool, "date": DATE
        }
        return assigned_pool

    for source in sources:
        domain = source["domain"]
        platform = source["platform"]
        assigned = []
        if source.get("protected_alias"):
            pid = _publisher_id("socrata", domain)
            allocation.setdefault("aliases", {})[pid] = "nyc"
            assigned.append({"publisher_id": pid, "canonical_publisher_id": "nyc", "pool": "main"})
            source["registry_status"] = "excluded_main_alias"
            source["catalog_access"] = "not queried"
        elif platform == "ckan":
            ckan_catalogues += 1
            try:
                orgs = _ckan_result(source["api_root"], "organization_list", {"all_fields": "false"})
                if not isinstance(orgs, list) or any(not isinstance(x, str) for x in orgs):
                    raise RuntimeError("organization_list was not a string-id list")
                for org_id in sorted({x.strip() for x in orgs if x.strip()}):
                    pid = _publisher_id("ckan", domain, org_id)
                    assigned_pool = reserve_publisher(pid)
                    assigned.append({"organization_id": org_id, "publisher_id": pid, "pool": assigned_pool})
                ckan_orgs += len(assigned)
                source["catalog_access"] = "organization IDs retrieved; no dataset metadata queried"
                source["registry_status"] = "registered"
            except Exception as exc:
                source["registry_status"] = "organization_list_failed"
                source["catalog_access"] = f"not searchable; {type(exc).__name__}"
        else:
            socrata_sources += 1
            pid = _publisher_id("socrata", domain)
            assigned_pool = reserve_publisher(pid)
            assigned.append({"publisher_id": pid, "pool": assigned_pool})
            source["catalog_access"] = "portal registered; no dataset metadata queried"
            source["registry_status"] = "registered"
        source["publisher_ids"] = assigned
        source_records.append(source)
    allocation["publishers"].extend(pending_records.values())
    allocation["publishers"].sort(key=lambda item: item["publisher_id"])
    validate_allocation(allocation)
    allocation_path.write_text(json.dumps(allocation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pools = Counter(x["pool"] for source in source_records for x in source["publisher_ids"])
    source_doc = {
        "schema_version": 1,
        "collected_date": DATE,
        "purpose": "S11 3.4 non-Japanese table candidates; register catalog publishers before dataset metadata",
        "method": "Pinned DataPortals.org active CKAN catalog registry plus pinned Socrata known-portal registry; CKAN organization_list(all_fields=false) only; no package_search or table metadata queried.",
        "registry_sources": [
            {"url": DATAPORTALS_CSV, "source_commit": "3665762ef571ff0027b80842e8f62641c3a2292d", "license": "DataPortals.org public-domain portal registry"},
            {"url": SOCRATA_SERVICE, "source_commit": "020153743c1d528a44b3d517f7e8bd59fa975db3", "license": "Socrata MCP server's curated portal membership list"},
        ],
        "excluded_countries": ["United Kingdom", "Ireland", "Canada", "Australia", "Japan"],
        "dataset_metadata_queried": False,
        "catalogues": source_records,
    }
    sources_path.write_text(json.dumps(source_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "catalogues_in_registry": len(sources),
        "ckan_catalogues_attempted": ckan_catalogues,
        "ckan_organizations_registered": ckan_orgs,
        "socrata_portals_registered": socrata_sources,
        "publisher_ids_registered": sum(len(x["publisher_ids"]) for x in source_records),
        "train_publishers": pools.get("train", 0),
        "eval2_publishers": pools.get("eval2", 0),
        "eval3_publishers": pools.get("eval3", 0),
        "main_aliases_excluded": pools.get("main", 0),
        "dataset_metadata_queried": False,
        "catalogues_by_status": dict(Counter(x["registry_status"] for x in source_records)),
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def safe_headers(fields: list[dict]) -> list[str]:
    headers = []
    for item in fields:
        if not isinstance(item, dict):
            continue
        name = str(item.get("id") or item.get("fieldName") or item.get("name") or "").strip().lstrip("\ufeff")
        if not name or JAPANESE_SCRIPT.search(name) or HEADER_DENY.search(normalize_header(name)):
            continue
        headers.append(name[:100])
    return list(dict.fromkeys(headers))


def _license_allowlist_match(values: list[object]) -> bool:
    parts = [str(x).strip() for x in values if x is not None and str(x).strip()]
    joined = " ".join(parts).lower()
    # Reject restrictive Creative Commons variants even if a broader CC-BY token is present.
    if re.search(r"non[ -]?commercial|share[ -]?alike|no[ -]?derivatives|\bby[- /]?(?:nc|sa|nd)\b|\bcc[- ]?by[- ]?(?:nc|sa|nd)\b", joined):
        return False
    for part in parts:
        normalized = re.sub(r"[^a-z0-9.-]+", "-", part.lower()).strip("-").replace("_", "-")
        if normalized in LICENSE_IDS:
            return True
        compact = re.sub(r"[^a-z0-9]", "", part.lower())
        if re.fullmatch(r"(?:ccby)(?:21jp|30|30us|30intl|40|40intl)", compact):
            return True
        if re.fullmatch(r"creativecommonsattribution(?:21jp|30|40|40international)", compact):
            return True
        if compact in {"cc0", "cczero", "cczero10", "publicdomain", "uspublicdomain", "usgovernmentwork"}:
            return True
        if compact in {"pdl10", "governmentstandardterms10", "governmentstandardterms20",
                       "govstandardterms10", "govstandardterms20", "ogl30",
                       "opengovernmentlicencecanada", "opengovernmentlicensecanada",
                       "singaporeopendatalicence", "singaporeopendatalicence10",
                       "singaporeopendatalicense", "singaporeopendatalicense10"}:
            return True
        if re.search(r"creativecommons\.org/licenses/by/(?:2\.1(?:/jp)?|3\.0|4\.0)(?:/|$)", part.lower()):
            return True
        if re.search(r"creativecommons\.org/publicdomain/zero/1\.0(?:/|$)", part.lower()):
            return True
    return False


def license_info(package: dict) -> dict:
    license_id = str(package.get("license_id") or package.get("licenseId") or "").strip().lower()
    title = str(package.get("license_title") or package.get("licenseTitle") or "").strip()[:160]
    url = str(package.get("license_url") or package.get("licenseUrl") or "").strip()[:500]
    allowed = _license_allowlist_match([license_id, title, url])
    return {
        "id": license_id,
        "title": title,
        "url": url,
        "candidate_allowlist_match": allowed,
        "individual_terms_reviewed": False,
    }


def signals(headers: list[str]) -> dict:
    code_name = any(CODE_HEADER.search(x) for x in headers) and any(NAME_HEADER.search(x) for x in headers)
    useful = sum(bool(USEFUL_HEADER.search(x)) for x in headers)
    return {
        "code_name_pair_hint": code_name,
        "useful_header_count": useful,
        "priority_score": (4 if code_name else 0) + min(useful, 6) + min(len(headers), 10) // 2,
        "hints": (["code/name pair candidate"] if code_name else []) + (["multiple task-oriented headers"] if useful >= 3 else []),
    }


def _language_terms(language: str) -> list[str]:
    value = str(language or "").lower().replace("_", "-")
    for code in ("pt", "es", "de", "fr", "it"):
        if code in value:
            return QUERY_TERMS[code]
    return QUERY_TERMS["en"]


def _ckan_train_orgs(sources: dict, allocation: dict) -> list[tuple[dict, dict]]:
    pools = {x["publisher_id"]: x["pool"] for x in allocation.get("publishers", [])}
    result = []
    for source in sources.get("catalogues", []):
        if source.get("platform") != "ckan" or source.get("registry_status") != "registered":
            continue
        for org in source.get("publisher_ids", []):
            if pools.get(org.get("publisher_id")) == "train":
                result.append((source, org))
    return result


def _socrata_train_sources(sources: dict, allocation: dict) -> list[dict]:
    pools = {x["publisher_id"]: x["pool"] for x in allocation.get("publishers", [])}
    result = []
    for source in sources.get("catalogues", []):
        if source.get("platform") != "socrata" or source.get("registry_status") != "registered":
            continue
        pid = source.get("publisher_ids", [{}])[0].get("publisher_id")
        if pools.get(pid) == "train":
            result.append(source)
    return result


def _candidate_base(publisher_id: str, publisher_name: str, country: str, language: str,
                    title: str, catalog_url: str, platform: str, license_meta: dict) -> dict:
    return {
        "publisher_id": publisher_id,
        "publisher_name": publisher_name[:160],
        "pool": "train",
        "country": country,
        "language": language or "non-Japanese (verified by script screen; exact language unverified)",
        "title": title[:300],
        "catalog_url": catalog_url[:700],
        "platform": platform,
        "license": license_meta,
        "sample_rows_requested": 0,
        "resource_file_downloaded": False,
        "cell_values_saved": False,
        "manual_review_required": True,
    }


def _add_schema_candidate(candidates: list[dict], publisher_id: str, publisher_name: str,
                          country: str, language: str, title: str, catalog_url: str,
                          platform: str, resource_id: str, headers: list[str],
                          license_meta: dict, format_name: str, total_rows: int | None = None) -> bool:
    if len(headers) < MIN_SAFE_HEADERS or not license_meta.get("candidate_allowlist_match"):
        return False
    candidate = _candidate_base(publisher_id, publisher_name, country, language, title, catalog_url, platform, license_meta)
    candidate.update({
        "resource_id": resource_id,
        "format": format_name[:40],
        "datastore_available": True,
        "datastore_total_rows": total_rows,
        "safe_header_count": len(headers),
        "candidate_columns_capped_at_10": min(len(headers), MAX_HEADERS),
        "safe_headers": headers[:MAX_HEADERS],
        "structure_orientation": "header-only candidate hint; no values read",
        "license_status": "allowlist match; individual terms need adoption-stage review",
        **signals(headers),
    })
    candidates.append(candidate)
    return True


def _record_non_datastore(non_datastore: list[dict], publisher_id: str, publisher_name: str,
                          country: str, language: str, title: str, catalog_url: str,
                          platform: str, resource_id: str, format_name: str, license_meta: dict) -> None:
    if not license_meta.get("candidate_allowlist_match") or JAPANESE_SCRIPT.search(title):
        return
    item = _candidate_base(publisher_id, publisher_name, country, language, title, catalog_url, platform, license_meta)
    item.update({
        "resource_id": resource_id,
        "format": format_name[:40],
        "datastore_available": False,
        "schema_status": "not available from metadata API; file not downloaded",
        "safe_headers": [],
        "license_status": "allowlist match; individual terms need adoption-stage review",
    })
    non_datastore.append(item)


def _ckan_discover(source: dict, org: dict, candidates: list[dict],
                   non_datastore: list[dict], seen: set[tuple[str, str]]) -> None:
    api_root = source["api_root"]
    org_id = org["organization_id"]
    pid = org["publisher_id"]
    publisher_name = f"{source.get('directory_title') or source['domain']} / {org_id}"
    terms = _language_terms(source.get("language"))
    accepted_for_publisher = 0
    for term in terms:
        if accepted_for_publisher >= MAX_PER_PUBLISHER or len(candidates) >= TARGET_TABLES:
            break
        try:
            result = _ckan_result(api_root, "package_search", {
                "q": term, "fq": f"organization:{org_id}", "rows": 50, "start": 0,
                "sort": "metadata_modified desc",
            })
        except Exception:
            continue
        if not isinstance(result, dict):
            continue
        packages = result.get("results") if isinstance(result.get("results"), list) else []
        for package in packages:
            if accepted_for_publisher >= MAX_PER_PUBLISHER or len(candidates) >= TARGET_TABLES:
                break
            if not isinstance(package, dict):
                continue
            title = str(package.get("title") or package.get("name") or "")
            if not title or TITLE_DENY.search(title) or JAPANESE_SCRIPT.search(title):
                continue
            lic = license_info(package)
            name = str(package.get("name") or "")
            page = str(package.get("url") or "")
            if not page and name:
                page = f"{source.get('portal_url','').rstrip('/')}/dataset/{name}"
            resources = package.get("resources") if isinstance(package.get("resources"), list) else []
            for resource in resources:
                if accepted_for_publisher >= MAX_PER_PUBLISHER or len(candidates) >= TARGET_TABLES:
                    break
                if not isinstance(resource, dict):
                    continue
                rid = str(resource.get("id") or "")
                if not rid or (pid, rid) in seen:
                    continue
                seen.add((pid, rid))
                fmt = str(resource.get("format") or "")
                if not resource.get("datastore_active"):
                    _record_non_datastore(non_datastore, pid, publisher_name, source.get("country",""),
                                          source.get("language",""), title, page, "ckan", rid, fmt, lic)
                    continue
                try:
                    schema = _ckan_result(api_root, "datastore_search", {"resource_id": rid, "limit": 0})
                    if not isinstance(schema, dict):
                        continue
                    # A compliant limit=0 response contains no rows. If it does, test only emptiness and discard.
                    records = schema.get("records") or []
                    if records:
                        continue
                    fields = schema.get("fields") if isinstance(schema.get("fields"), list) else []
                    headers = safe_headers(fields)
                    total = schema.get("total")
                    try:
                        total = int(total) if total is not None else None
                    except (TypeError, ValueError):
                        total = None
                except Exception:
                    continue
                if _add_schema_candidate(candidates, pid, publisher_name, source.get("country",""),
                                         source.get("language",""), title, page, "ckan", rid, headers,
                                         lic, fmt, total):
                    accepted_for_publisher += 1


def _socrata_schema(domain: str, resource_id: str) -> dict:
    url = f"https://{domain}/api/views/{resource_id}.json"
    return _json(url, domain)


def _socrata_license(view: dict) -> dict:
    fields = [view.get("license"), view.get("licenseId"), view.get("license_url")]
    metadata = view.get("metadata") if isinstance(view.get("metadata"), dict) else {}
    custom_fields = metadata.get("custom_fields")
    if not isinstance(custom_fields, dict):
        custom_fields = {}
    for key, value in custom_fields.items():
        if "license" in str(key).lower():
            fields.extend(value if isinstance(value, list) else [value])
    text = " ".join(str(x) for x in fields if x).strip()
    norm = re.sub(r"[^a-z0-9.-]+", "-", text.lower()).strip("-")
    matched = _license_allowlist_match(fields)
    return {
        "id": norm[:120],
        "title": text[:160],
        "url": next((str(x) for x in fields if isinstance(x, str) and x.startswith("http")), "")[:500],
        "candidate_allowlist_match": matched,
        "individual_terms_reviewed": False,
    }


def _socrata_discover(source: dict, candidates: list[dict],
                      non_datastore: list[dict], seen: set[tuple[str, str]]) -> None:
    domain = source["domain"]
    api = source["api_root"]
    api_host = _host(api)
    pid = source["publisher_ids"][0]["publisher_id"]
    publisher_name = source.get("directory_title") or domain
    accepted_for_publisher = 0
    for term in _language_terms(source.get("language")):
        if accepted_for_publisher >= MAX_PER_PUBLISHER or len(candidates) >= TARGET_TABLES:
            break
        params = {
            "domains": domain, "search_context": domain, "only": "dataset",
            "q": term, "limit": 100,
        }
        url = f"{api}?{urlencode(params)}"
        try:
            payload = _json(url, api_host)
        except Exception:
            continue
        results = payload.get("results") if isinstance(payload.get("results"), list) else []
        for item in results:
            if accepted_for_publisher >= MAX_PER_PUBLISHER or len(candidates) >= TARGET_TABLES:
                break
            if not isinstance(item, dict):
                continue
            resource = item.get("resource") if isinstance(item.get("resource"), dict) else {}
            rid = str(resource.get("id") or "")
            if not re.fullmatch(r"[a-z0-9]{4}-[a-z0-9]{4}", rid) or (pid, rid) in seen:
                continue
            seen.add((pid, rid))
            title = str(item.get("name") or item.get("title") or resource.get("name") or "")
            if not title or TITLE_DENY.search(title) or JAPANESE_SCRIPT.search(title):
                continue
            page = str(item.get("link") or f"https://{domain}/d/{rid}")
            try:
                view = _socrata_schema(domain, rid)
            except Exception:
                continue
            columns = view.get("columns") if isinstance(view.get("columns"), list) else []
            headers = safe_headers(columns)
            lic = _socrata_license(view)
            if _add_schema_candidate(candidates, pid, publisher_name, source.get("country",""),
                                     source.get("language",""), title, page, "socrata", rid,
                                     headers, lic, "SODA datastore"):
                accepted_for_publisher += 1


def discover(allocation_path: Path, sources_path: Path, json_path: Path, md_path: Path) -> dict:
    allocation = load_allocation(allocation_path)
    sources = json.loads(sources_path.read_text(encoding="utf-8"))
    train_ckan = _ckan_train_orgs(sources, allocation)
    train_socrata = _socrata_train_sources(sources, allocation)
    # Stable order avoids favoring registries with many early rows.
    train_ckan.sort(key=lambda x: hashlib.sha256(x[1]["publisher_id"].encode()).hexdigest())
    train_socrata.sort(key=lambda x: hashlib.sha256(x["publisher_ids"][0]["publisher_id"].encode()).hexdigest())
    candidates: list[dict] = []
    non_datastore: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for source, org in train_ckan:
        if len(candidates) >= TARGET_TABLES:
            break
        _ckan_discover(source, org, candidates, non_datastore, seen)
        time.sleep(0.06)
    for source in train_socrata:
        if len(candidates) >= TARGET_TABLES:
            break
        _socrata_discover(source, candidates, non_datastore, seen)
        time.sleep(0.06)

    candidates.sort(key=lambda x: (-x["priority_score"], x["publisher_id"], x["title"].casefold()))
    # Enforce the protocol's 3% publisher cap using the final candidate-list size.
    cap = max(1, math.floor(len(candidates) * 0.03))
    selected = []
    counts = Counter()
    for candidate in candidates:
        if counts[candidate["publisher_id"]] >= cap:
            continue
        selected.append(candidate)
        counts[candidate["publisher_id"]] += 1
        if len(selected) >= TARGET_TABLES:
            break
    selected_count = len(selected)
    final_cap = max(1, math.floor(selected_count * 0.03))
    if selected_count and max(Counter(x["publisher_id"] for x in selected).values()) > final_cap:
        # One last denominator check after selection. Drop excess and report the actual safe count.
        kept, final_counts = [], Counter()
        for candidate in selected:
            if final_counts[candidate["publisher_id"]] < final_cap:
                kept.append(candidate)
                final_counts[candidate["publisher_id"]] += 1
        selected = kept
    headers_total = sum(x["candidate_columns_capped_at_10"] for x in selected)
    report = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "S11 3.4 world metadata discovery",
        "publisher_rule": "only train CKAN organizations and train Socrata portals were searched",
        "target": {"tables": 60, "safe_columns": 450, "publishers": 20},
        "protocol_cap": {"max_fraction_per_publisher": 0.03, "enforced_table_cap": max(1, math.floor(len(selected) * 0.03))},
        "candidate_tables": len(selected),
        "safe_candidate_columns": headers_total,
        "distinct_train_publishers": len({x["publisher_id"] for x in selected}),
        "datastore_tables": sum(bool(x.get("datastore_available")) for x in selected),
        "non_datastore_leads": len(non_datastore),
        "candidate_targets_met": {
            "tables_60": len(selected) >= 60,
            "columns_450": headers_total >= 450,
            "publishers_20": len({x["publisher_id"] for x in selected}) >= 20,
        },
        "cell_values_saved": False,
        "rows_requested": 0,
        "candidates": selected,
        "non_datastore_candidates": non_datastore[:200],
        "limitations": [
            "No data rows or files were downloaded.",
            "CKAN schemas were requested with datastore_search limit=0; unexpected records were discarded without inspecting fields.",
            "Socrata schema fields came from /api/views/{id}.json metadata only.",
            "License identifiers were screened against the allowlist; individual license text has not been reviewed.",
        ],
    }
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# S11 3.4 非日本語公開表候補（メタデータのみ）", "",
        f"- 候補: {len(selected)} 表 / 安全見出し {headers_total} 列 / 公開元 {report['distinct_train_publishers']} 件",
        f"- datastore/API schemaあり: {report['datastore_tables']} 表; datastoreなしの別枠候補: {len(non_datastore)} 件",
        "- 値の行・ファイルは取得していません。ライセンスの個別規約は採用段階で原文確認が必要です。",
        "- 公開元割当後の train 組織/ポータルだけを検索しました。", "",
        "| # | 国 | 公開元 | 表題 | datastore | 安全な列見出し（最大10） | 優先ヒント | License ID |",
        "|---:|---|---|---|:---:|---|---|---|",
    ]
    for i, x in enumerate(selected, 1):
        headers = "<br>".join(x.get("safe_headers", []))
        hints = ", ".join(x.get("hints", []))
        lines.append(f"| {i} | {x.get('country','')} | {x['publisher_name']} | [{x['title']}]({x['catalog_url']}) | ○ | {headers} | {hints} | {x.get('license',{}).get('id','')} |")
    lines += ["", "## Datastoreなしの候補", "",
              "以下はカタログ上に表ファイルはありますが、列スキーマを取得できませんでした。ファイルは開いていません。", "",
              "| 公開元 | 表題 | 形式 | License ID | catalog |",
              "|---|---|---|---|---|"]
    for x in non_datastore[:200]:
        lines.append(f"| {x['publisher_name']} | {x['title']} | {x['format']} | {x.get('license',{}).get('id','')} | {x['catalog_url']} |")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {k: report[k] for k in ("candidate_tables", "safe_candidate_columns", "distinct_train_publishers",
                                    "datastore_tables", "non_datastore_leads", "candidate_targets_met")}


def self_test() -> None:
    assert _publisher_id("ckan", "data.example.gov", "public-works") == "world_ckan_data_example_gov_public_works"
    assert _excluded_country("Canada", "data.example.gov")
    assert _excluded_country("US", "data.example.ca")
    assert not _excluded_country("US", "data.ca.gov")
    assert NYC_DOMAIN.search("data.cityofnewyork.us")
    assert JAPANESE_SCRIPT.search("人口")
    assert not JAPANESE_SCRIPT.search("population")
    assert "cc-by-40-intl" in LICENSE_IDS
    assert _license_allowlist_match(["cc-by-40-intl"])
    assert _license_allowlist_match(["Creative Commons Attribution 4.0 International"])
    assert not _license_allowlist_match(["CC BY-NC 4.0", "https://creativecommons.org/licenses/by-nc/4.0/"])
    assert not _license_allowlist_match(["cc-by-sa-4.0"])
    assert _license_allowlist_match(["Public Domain"])
    assert license_info({"license_id": "cc-by-40-intl"})["candidate_allowlist_match"]
    assert not _socrata_license({"license": "CC BY-NC 4.0"})["candidate_allowlist_match"]
    assert safe_headers([{"id": "amount"}, {"id": "email"}, {"id": "population"}, {"id": "人口"}]) == ["amount", "population"]
    print("S11 3.4 world publisher/discovery self-test passed")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--mode", choices={"register", "discover"})
    args = parser.parse_args(argv)
    if args.self_test:
        self_test()
        return 0
    if args.mode == "register":
        report = register_publishers(
            ROOT / "independent_eval/allocation.json",
            ROOT / "independent_eval/allocation_sources_world_20261022.json",
            ROOT / "materials/s11_3_4_world_registration_20261022.json",
        )
        print(
            f"world portals={report['catalogues_in_registry']} CKAN orgs={report['ckan_organizations_registered']} "
            f"Socrata portals={report['socrata_portals_registered']} train={report['train_publishers']}; dataset metadata not queried"
        )
        return 0
    if args.mode == "discover":
        report = discover(
            ROOT / "independent_eval/allocation.json",
            ROOT / "independent_eval/allocation_sources_world_20261022.json",
            ROOT / "materials/s11_3_4_candidates_20261022.json",
            ROOT / "materials/s11_3_4_candidates_20261022.md",
        )
        print(json.dumps(report, ensure_ascii=False))
        return 0
    parser.error("--mode register, --mode discover, or --self-test is required")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
