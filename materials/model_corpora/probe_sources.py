"""列の種類判定の上位モデルと学習データの「メタデータだけ」を集める（2026-10-27 Claude）。

本体のデータは取らない。Zenodo の記録・Hugging Face のデータセット・GitHub のリポジトリのライセンスと大きさ、
公開データのカタログの件数とライセンスの内訳を JSON に書く。Actions（probe-sources.yml）で動かす。
  python -I materials/model_corpora/probe_sources.py materials/model_corpora/probe/probe_YYYYMMDD.json
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

UA = "jitsuris-train probe (metadata only)"

ZENODO = {
    "11559814": "WikiDBs 100k（Wikidata 由来の関係DB）",
    "8227452": "WikiDBs 10k（先行版）",
    "6517052": "GitTables 1M v0.0.6",
    "5706316": "GitTables CTA ベンチマーク",
    "8422037": "SOTAB V2 for SemTab 2023",
    "8393535": "SemTab 2023 WikidataTables",
    "6153449": "SemTab 2021 Wikidata",
}
ZENODO_QUERIES = ["column type annotation", "semantic type detection tables", "table annotation benchmark",
                  "tabular data knowledge graph matching", "web tables corpus"]
HF_DATASETS = ["osunlp/TableInstruct", "aidalab/rwt-rutabert", "approximatelabs/tablib-v1-full",
               "approximatelabs/tablib-v1-sample", "TheFinAI/sotab", "wdc/sotab"]
HF_QUERIES = ["column type annotation", "table annotation", "semantic type", "sotab", "gittables", "wikitables"]
GITHUB = ["megagonlabs/sato", "megagonlabs/doduo", "mitmedialab/sherlock-project", "sunlab-osu/TURL",
          "OSU-NLP-Group/TableLlama", "hoseinzadeehsan/ZTab", "hoseinzadeehsan/TabEmb", "madelonhulsebos/AdaTyper",
          "DataManagementLab/wikidbs-public", "viznetauthors/viznet", "ysunbp/RECA", "Ehsanhoseinzadeh/ZTab",
          "sem-tab-challenge/2023", "sem-tab-challenge/2024", "wbsg-uni-mannheim/TableAnnotation"]
GITHUB_QUERIES = ["column type annotation", "semantic column type detection", "table column semantic type"]
CKAN = {
    "catalog.data.gov": "https://catalog.data.gov/api/3/action/package_search",
    "data.gov.uk": "https://data.gov.uk/api/action/package_search",
    "data.go.jp": "https://www.data.go.jp/data/api/3/action/package_search",
    "opendata.swiss": "https://opendata.swiss/api/3/action/package_search",
    "catalogue.data.govt.nz": "https://catalogue.data.govt.nz/api/3/action/package_search",
    "open.canada.ca": "https://open.canada.ca/data/api/3/action/package_search",
    "data.gov.au": "https://data.gov.au/data/api/3/action/package_search",
    "data.gov.ie": "https://data.gov.ie/api/3/action/package_search",
}


def get(url, token=None, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001 — 失敗は記録に残す
            err = f"{type(e).__name__}: {e}"
            time.sleep(2 * (attempt + 1))
    return {"_error": err}


def zenodo_record(rid):
    d = get(f"https://zenodo.org/api/records/{rid}")
    if "_error" in d:
        return d
    m = d.get("metadata", {})
    files = d.get("files", [])
    return {"title": m.get("title"), "license": m.get("license"), "rights": m.get("rights"),
            "access_right": m.get("access_right"), "publication_date": m.get("publication_date"),
            "doi": d.get("doi"), "files": len(files), "bytes": sum(f.get("size", 0) for f in files),
            "file_names": [f.get("key") for f in files][:30], "description": (m.get("description") or "")[:1500]}


def zenodo_search(q):
    d = get("https://zenodo.org/api/records?" + urllib.parse.urlencode({"q": q, "size": 25, "type": "dataset", "sort": "mostviewed"}))
    if "_error" in d:
        return d
    return [{"id": h.get("id"), "title": h.get("metadata", {}).get("title"), "license": h.get("metadata", {}).get("license"),
             "bytes": sum(f.get("size", 0) for f in h.get("files", [])), "date": h.get("metadata", {}).get("publication_date")}
            for h in d.get("hits", {}).get("hits", [])]


def hf_dataset(name):
    d = get(f"https://huggingface.co/api/datasets/{name}")
    if "_error" in d:
        return d
    card = d.get("cardData") or {}
    return {"license": card.get("license"), "tags": [t for t in d.get("tags", []) if t.startswith(("license:", "size_categories:", "language:", "task_categories:"))],
            "downloads": d.get("downloads"), "gated": d.get("gated"), "last_modified": d.get("lastModified"),
            "siblings": len(d.get("siblings") or [])}


def hf_search(q):
    d = get("https://huggingface.co/api/datasets?" + urllib.parse.urlencode({"search": q, "limit": 30, "full": "true"}))
    if isinstance(d, dict) and "_error" in d:
        return d
    return [{"id": x.get("id"), "license": [t for t in x.get("tags", []) if t.startswith("license:")],
             "size": [t for t in x.get("tags", []) if t.startswith("size_categories:")], "downloads": x.get("downloads")} for x in d]


def gh_repo(name, token):
    d = get(f"https://api.github.com/repos/{name}", token)
    if "_error" in d or "message" in d and "id" not in d:
        return {"_error": d.get("_error") or d.get("message")}
    lic = d.get("license") or {}
    return {"license": lic.get("spdx_id"), "stars": d.get("stargazers_count"), "pushed_at": d.get("pushed_at"),
            "description": d.get("description"), "archived": d.get("archived")}


def gh_search(q, token):
    d = get("https://api.github.com/search/repositories?" + urllib.parse.urlencode({"q": q, "sort": "stars", "per_page": 20}), token)
    if "_error" in d:
        return d
    return [{"repo": x.get("full_name"), "license": (x.get("license") or {}).get("spdx_id"), "stars": x.get("stargazers_count"),
             "pushed_at": x.get("pushed_at"), "description": (x.get("description") or "")[:200]} for x in d.get("items", [])]


def ckan_summary(url):
    q = urllib.parse.urlencode({"rows": 0, "facet.field": json.dumps(["license_id", "res_format"]), "facet.limit": 40})
    d = get(f"{url}?{q}")
    if "_error" in d:
        return d
    r = d.get("result", {})
    facets = r.get("search_facets", {})
    def items(name):
        return {i["name"]: i["count"] for i in facets.get(name, {}).get("items", [])}
    return {"packages": r.get("count"), "licenses": items("license_id"), "formats": items("res_format")}


def main(out):
    token = os.environ.get("GITHUB_TOKEN")
    rep = {"created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "note": "メタデータのみ。データ本体は取得していない",
           "zenodo": {rid: {"label": lab, **zenodo_record(rid)} for rid, lab in ZENODO.items()},
           "zenodo_search": {q: zenodo_search(q) for q in ZENODO_QUERIES},
           "huggingface": {n: hf_dataset(n) for n in HF_DATASETS},
           "huggingface_search": {q: hf_search(q) for q in HF_QUERIES},
           "github": {n: gh_repo(n, token) for n in GITHUB},
           "github_search": {q: gh_search(q, token) for q in GITHUB_QUERIES},
           "ckan": {h: ckan_summary(u) for h, u in CKAN.items()}}
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(rep, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("wrote", out)


if __name__ == "__main__":
    main(sys.argv[1])
