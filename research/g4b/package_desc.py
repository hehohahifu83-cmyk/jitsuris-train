"""表の出典のデータセットの説明だけを取る（2026-11-26 Claude。G4b の裁定の根拠用。値・表の中身は取らない）。
  python -I research/g4b/package_desc.py <host> <dataset の名前か id> ... → research/g4b/package_desc.json
"""
import json
import sys
from urllib.request import Request, urlopen

out = []
args = sys.argv[1:]
for host, pkg in zip(args[0::2], args[1::2]):
    url = f"https://{host}/api/3/action/package_show?id={pkg}"
    try:
        req = Request(url, headers={"Accept": "application/json", "User-Agent": "jitsuris-train/1.0 (research; metadata only)"})
        with urlopen(req, timeout=60) as r:
            res = json.loads(r.read().decode("utf-8"))["result"]
        out.append({"url": url, "title": res.get("title"), "notes": res.get("notes"), "license_id": res.get("license_id"),
                    "organization": (res.get("organization") or {}).get("name"),
                    "resources": [{"id": x.get("id"), "name": x.get("name"), "description": x.get("description")} for x in res.get("resources", [])]})
    except Exception as e:
        out.append({"url": url, "error": f"{type(e).__name__}: {e}"[:300]})
json.dump(out, open("research/g4b/package_desc.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1)[:3000])
