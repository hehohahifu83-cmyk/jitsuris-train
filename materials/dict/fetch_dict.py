"""辞書の公式データを取る（2026-10-26 Claude。GitHub Actions で動かす。方針：materials/dict/README.md）。

取るのは名前・コードだけ（個人の記録はない）。取れたものだけ materials/dict/<名前>.json に書き、出典・取った日・SHA-256 を sources.json に残す。
- jp_municipalities：総務省「全国地方公共団体コード」の Excel（ページから .xlsx／.xls の最新の表を探す）
- br_municipios：IBGE の市の一覧（API）
- us_counties・us_places：米国勢調査局の地名一覧（Gazetteer。新しい年から順に試す）
- countries・currencies：ISO 3166・ISO 4217（pycountry の同梱データ。元は Debian の iso-codes）
使い方：python materials/dict/fetch_dict.py
"""
import datetime
import hashlib
import io
import json
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

OUT = Path(__file__).resolve().parent
UA = {"User-Agent": "jitsuris-train dictionary fetch (public data)"}


def get(url, timeout=300):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read()


def save(name, data, source, note=""):
    body = json.dumps(data, ensure_ascii=False, indent=0, sort_keys=True)
    (OUT / f"{name}.json").write_text(body + "\n", encoding="utf-8")
    src = json.loads((OUT / "sources.json").read_text(encoding="utf-8")) if (OUT / "sources.json").exists() else {}
    src[name] = {"source": source, "fetched_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                 "count": len(data), "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(), "note": note}
    (OUT / "sources.json").write_text(json.dumps(src, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{name}: {len(data)}", flush=True)


def jp():
    page_url = "https://www.soumu.go.jp/denshijiti/code.html"
    page = get(page_url).decode("utf-8", "replace")
    links = re.findall(r'href="([^"]+\.xlsx?)"', page)
    if not links:
        raise RuntimeError("総務省のページに Excel が見つからない")
    import pandas as pd
    url = links[0] if links[0].startswith("http") else "https://www.soumu.go.jp" + links[0]
    sheets = pd.read_excel(io.BytesIO(get(url)), sheet_name=None, dtype=str)
    rows = []
    for df in sheets.values():
        cols = [str(c) for c in df.columns]
        code = next((c for c in cols if "コード" in c), None)
        pref = next((c for c in cols if "都道府県名" in c and "カナ" not in c), None)
        city = next((c for c in cols if "市区町村名" in c and "カナ" not in c), None)
        if not code or not pref:
            continue
        for _, r in df.iterrows():
            c = str(r[code]).strip()
            if re.fullmatch(r"\d{6}", c):
                rows.append({"code": c, "pref": str(r[pref]).strip(), "city": (str(r[city]).strip() if city and str(r[city]) != "nan" else "")})
    save("jp_municipalities", rows, url, "全国地方公共団体コード（6 桁目は検査数字）")


def check_digit_jp(code5):
    """全国地方公共団体コードの検査数字（総務省の決まり：各桁に 6・5・4・3・2 を掛けた和を 11 で割った余り r、11−r の 1 の位。r＝0 なら 1、r＝1 なら 0）。"""
    s = sum(int(d) * w for d, w in zip(code5, (6, 5, 4, 3, 2)))
    return (11 - s % 11) % 10


def br():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
    data = json.loads(get(url))
    rows = []
    for m in data:
        uf = (((m.get("microrregiao") or {}).get("mesorregiao") or {}).get("UF") or {}) or (((m.get("regiao-imediata") or {}).get("regiao-intermediaria") or {}).get("UF") or {})
        rows.append({"code": str(m["id"]), "name": m["nome"], "uf": uf.get("sigla", "")})
    save("br_municipios", rows, url)


def us():
    for year in (2025, 2024, 2023):
        base = f"https://www2.census.gov/geo/docs/maps-data/data/gazetteer/{year}_Gazetteer/"
        try:
            out = {}
            for kind, fn in (("us_counties", f"{year}_Gaz_counties_national.zip"), ("us_places", f"{year}_Gaz_place_national.zip")):
                z = zipfile.ZipFile(io.BytesIO(get(base + fn)))
                txt = z.read(z.namelist()[0]).decode("latin-1")
                lines = [l.split("\t") for l in txt.splitlines() if l.strip()]
                head = [h.strip() for h in lines[0]]
                i_name, i_st = head.index("NAME"), head.index("USPS")
                out[kind] = (base + fn, [{"name": l[i_name].strip(), "state": l[i_st].strip()} for l in lines[1:]])
            for kind, (u, rows) in out.items():
                save(kind, rows, u)
            return
        except Exception as e:  # 年が違えば次の年を試す
            print(f"us {year}: {e}", flush=True)
    raise RuntimeError("米国の地名一覧が取れない")


def iso():
    import pycountry
    save("countries", [{"alpha2": c.alpha_2, "alpha3": c.alpha_3, "name": c.name} for c in pycountry.countries], "pycountry（Debian iso-codes、ISO 3166-1）")
    save("currencies", [{"code": c.alpha_3, "name": c.name} for c in pycountry.currencies], "pycountry（Debian iso-codes、ISO 4217）")


def main():
    failed = []
    for f in (jp, br, us, iso):
        try:
            f()
        except Exception as e:
            print(f"{f.__name__} 失敗: {e}", flush=True)
            failed.append(f.__name__)
    if (OUT / "jp_municipalities.json").exists():
        rows = json.loads((OUT / "jp_municipalities.json").read_text(encoding="utf-8"))
        bad = [r["code"] for r in rows if check_digit_jp(r["code"][:5]) != int(r["code"][5])]
        print(f"検査数字の確かめ：{len(rows) - len(bad)}/{len(rows)} 合う（合わない例 {bad[:5]}）", flush=True)
    if failed:
        print("失敗：", failed, flush=True)
        sys.exit(0 if len(failed) < 4 else 1)


if __name__ == "__main__":
    main()
