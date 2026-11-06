"""教材 第 6 回 b182〜b185（Shirasagi 4 サイト、第 2 回の残りの表）の裁定（2026-11-06 Claude）。先生＝Codex（LABEL_GUIDE v2.4）、2 人目の票＝L 種子 1（r182 でまとめて予測）。

  python research/collection_v2/adjudicate_r182.py   → 各陣の work/<陣>/decisions.jsonl

決め方は adjudicate_r124.py の K1〜K5（rule）と同じ。残り 8 行は MANUAL で決めた。抜き取り 38 行は全部見て誤り 0。
先例の抜き取り：20 グループ中 2 件が先生と違った（b182 g0012・b184 g0016、どちらも POIコード で先例 category・Codex id）。
POIコード は自治体標準オープンデータセットの施設の種類のコードで、確定済み 45 列もすべて category。先例が正しく、Codex の答えの誤り。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from adjudicate_r124 import rule  # noqa: E402

BATCHES = ["b182", "b183", "b184", "b185"]
EN = "施設の名前の英字表記（公共施設の一覧、B10-3。R4：元の名前の列に合わせる）"
POI = "POIコード＝自治体標準オープンデータセットの施設の種類のコード（同じ値が繰り返す。確定済み 45 列も category）"
MANUAL = {
    "b182#13": ("category", POI), "b184#16": ("category", POI),
    "b182#39": ("address", "観光・交流施設の名前（利用可能曜日・開始時間の付く施設の一覧、B10-3）"),
    "b182#40": ("address", "観光・交流施設の名前の読み（R4）"),
    "b184#14": ("address", EN), "b184#24": ("address", EN),
    "b183#14": ("category", "ゴミの種類の決まった語（可燃・プラ容器など）を ; でつないだもの。文ではない"),
    "b185#2": ("category", "疾病の分類のコード（ICD-10 の範囲、B3 の種類のコード。b180#7 と同じ）"),
}
EXTRA = {}


def main():
    tot = {}
    for b in (sys.argv[1:] or BATCHES):
        w = ROOT / "materials" / "pool" / "work" / b
        out = []
        for line in open(w / "review.jsonl", encoding="utf-8"):
            r = json.loads(line)
            key = f"{b}#{r['i']}"
            if r["kind"] == "audit":
                lab, why = r["teacher"], "抜き取り：先生とモデルの一致を確かめた"
            elif key in MANUAL:
                lab, why = MANUAL[key]
            else:
                got = rule(r)
                if not got:
                    raise SystemExit(f"未裁定 {key} {r['teacher']} {r['model']} {r['header']!r}")
                lab, why = got
            out.append({"i": r["i"], "label": lab, "reason": why, "by": "claude-20261106"})
        seen = {d["i"] for d in out}
        for key, (lab, why) in EXTRA.items():
            bb, i = key.split("#")
            if bb == b and int(i) not in seen:
                out.append({"i": int(i), "label": lab, "reason": why, "by": "claude-20261106"})
        with open(w / "decisions.jsonl", "w", encoding="utf-8") as fh:
            for d in out:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
        tot[b] = len(out)
    print(tot, sum(tot.values()))


if __name__ == "__main__":
    main()
