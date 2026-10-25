"""融合（重みの平均・合成）の候補探し：C1 と同じ元モデル intfloat/multilingual-e5-base から微調整した公開モデルの一覧を Hugging Face から集める（メタデータだけ。重みは落とさない）。2026-10-25

重みを混ぜられるのは同じ元から微調整した兄弟だけ（系列が違うと中の数字が対応しない）。
出力：research/merge/candidates.json（全件）と candidates.md（ダウンロード順）。
"""
import json
import sys
import time
import urllib.parse
import urllib.request

API = "https://huggingface.co/api/models"
BASES = ["intfloat/multilingual-e5-base"]


def get(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "jitsuris-train"}), timeout=60) as r:
                return json.load(r), r.headers.get("Link", "")
        except Exception as e:  # 一時的な失敗だけ待って試し直す
            print(f"retry {i}: {e}", file=sys.stderr)
            time.sleep(2 ** (i + 1))
    raise SystemExit(f"取得できない：{url}")


def list_finetunes(base, limit=2000):
    url = f"{API}?filter={urllib.parse.quote('base_model:finetune:' + base)}&sort=downloads&direction=-1&limit=100&full=true"
    out = []
    while url and len(out) < limit:
        page, link = get(url)
        out += page
        url = link.split(";")[0].strip("<> ") if 'rel="next"' in link else None
    return out


def detail(mid):
    d, _ = get(f"{API}/{urllib.parse.quote(mid, safe='/')}?expand[]=cardData&expand[]=downloadsAllTime&expand[]=safetensors&expand[]=config")
    card = d.get("cardData") or {}
    return {
        "datasets": card.get("datasets"), "language": card.get("language"), "license": card.get("license"),
        "params": (d.get("safetensors") or {}).get("total"), "architectures": (d.get("config") or {}).get("architectures"),
        "downloadsAllTime": d.get("downloadsAllTime"),
    }


def main():
    rows = []
    for base in BASES:
        for m in list_finetunes(base):
            rows.append({"base": base, "id": m["id"], "downloads": m.get("downloads", 0), "likes": m.get("likes", 0),
                         "pipeline_tag": m.get("pipeline_tag"), "tags": m.get("tags", []), "lastModified": m.get("lastModified")})
    print(f"fine-tunes: {len(rows)}", flush=True)
    for r in rows[:400]:   # 細目はダウンロード上位 400 だけ
        try:
            r.update(detail(r["id"]))
        except SystemExit as e:
            r["detail_error"] = str(e)
    json.dump(rows, open("research/merge/candidates.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    with open("research/merge/candidates.md", "w", encoding="utf-8") as f:
        f.write(f"# multilingual-e5-base の微調整モデル（Hugging Face、{len(rows)} 件、ダウンロード順）\n\n")
        f.write("| 名前 | DL | 種類 | 言語 | データ | 作り | 大きさ |\n|---|---:|---|---|---|---|---:|\n")
        for r in rows:
            ds = ", ".join(r.get("datasets") or [])[:80] if isinstance(r.get("datasets"), list) else str(r.get("datasets") or "")[:80]
            lang = r.get("language"); lang = ",".join(lang[:5]) if isinstance(lang, list) else (lang or "")
            arch = ",".join(r.get("architectures") or [])
            f.write(f"| {r['id']} | {r['downloads']} | {r.get('pipeline_tag') or ''} | {lang} | {ds} | {arch} | {r.get('params') or ''} |\n")


def cards(ids):
    """候補の説明（README）だけを research/merge/cards/ に保存する。"""
    import os
    os.makedirs("research/merge/cards", exist_ok=True)
    for mid in ids:
        try:
            with urllib.request.urlopen(f"https://huggingface.co/{mid}/raw/main/README.md", timeout=60) as r:
                txt = r.read().decode("utf-8", "replace")
        except Exception as e:
            txt = f"取得できない：{e}"
        open(f"research/merge/cards/{mid.replace('/', '__')}.md", "w", encoding="utf-8").write(txt[:20000])


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "cards":
        cards(sys.argv[2:])
    else:
        main()
