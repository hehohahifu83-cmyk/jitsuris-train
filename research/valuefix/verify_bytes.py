"""直した値を元のファイルのバイトと照合する（2026-11-01 Claude。ChatGPT「既存114列は元バイトと照合して値を修復し…確かめてから学習対象に」）。
GitHub の手順（valuefix-verify.yml）で走らせる（この環境からは data.gov.uk などに届かない）。
一覧の各表を取り直し、直した値（ASCII でない字を含む値・兄弟の列の名前・列名）を CP1252 にしたバイトが、ファイルのバイトの中にあるかを数える。
  python -I research/valuefix/verify_bytes.py → research/valuefix/verify.json・verify.md
"""
import glob
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
from encoder_context import cp932_to_cp1252  # noqa: E402

MAX = 60 * 1024 * 1024


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "jitsuris-train valuefix check (github actions)"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read(MAX + 1)


def main():
    lst = [json.loads(l) for l in open(os.path.join(ROOT, "materials", "pool", "valuefix_cp1252.jsonl"), encoding="utf-8") if l.strip()]
    want = {o["table"] for o in lst}
    rows = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "materials", "pool", "batch_*.jsonl"))):
        for line in open(f, encoding="utf-8"):
            d = json.loads(line)
            if d.get("table") in want:
                rows.setdefault(d["table"], []).append(d)
    res = []
    for o in lst:
        t = o["table"]
        strs = set()
        for d in rows[t]:
            for s in [d["header"]] + list(d["values"]) + list(d["context"]):
                s = str(s)
                if any(ord(c) > 127 for c in s) and len(s.strip()) >= 2:
                    strs.add(cp932_to_cp1252(s).strip())
        r = {"table": t, "batch": o["batch"], "checked": len(strs)}
        try:
            raw = fetch(t)
        except Exception as e:  # noqa: BLE001
            r.update(fetched=False, error=f"{type(e).__name__}: {str(e)[:120]}")
            res.append(r)
            continue
        r["fetched"] = len(raw) <= MAX
        r["bytes"] = len(raw)
        try:
            raw.decode("utf-8")
            r["file_is_utf8"] = True
        except UnicodeDecodeError:
            r["file_is_utf8"] = False
        ok = [s for s in strs if s.encode("cp1252", "strict") in raw]
        r["matched_cp1252_bytes"] = len(ok)
        r["unmatched_examples"] = sorted(strs - set(ok))[:3]
        res.append(r)
        print(t[:80], r.get("matched_cp1252_bytes"), "/", r["checked"], flush=True)
    json.dump(res, open(os.path.join(HERE := os.path.dirname(os.path.abspath(__file__)), "verify.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    got = [r for r in res if r.get("fetched")]
    L = ["# 直した値と元のファイルのバイトの照合（`research/valuefix/verify_bytes.py`）", "",
         f"- 表 {len(res)}：取れた {len(got)}、取れなかった {len(res) - len(got)}。",
         f"- 取れた表で、照合した文字列 {sum(r['checked'] for r in got)}、CP1252 のバイトが元のファイルにあった {sum(r['matched_cp1252_bytes'] for r in got)}。",
         f"- 取れた表のうち UTF-8 として読めるファイル（化けの前提に合わない）：{sum(r.get('file_is_utf8', False) for r in got)}。", "",
         "| 陣 | 表 | 取れた | 照合 | 一致 | UTF-8 | 合わない例・誤り |", "|---|---|---|---:|---:|---|---|"]
    for r in res:
        ex = r.get("error") or " ／ ".join(x[:30] for x in r.get("unmatched_examples", []))
        L.append(f"| {r['batch']} | {r['table'][-60:]} | {'○' if r.get('fetched') else '×'} | {r['checked']} | {r.get('matched_cp1252_bytes', '')} | {r.get('file_is_utf8', '')} | {ex.replace('|', '/')} |")
    open(os.path.join(HERE, "verify.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
