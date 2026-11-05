"""教材 第 3・4 回 b152〜b175 の裁定（2026-11-05 Claude）。先生＝Codex（LABEL_GUIDE v2.4）、2 人目の票＝L 種子 1（r152 でまとめて予測）。

  python research/collection_v2/adjudicate_r152.py   → 各陣の work/<陣>/decisions.jsonl

決め方は adjudicate_r124.py の K1〜K5 と同じ（rule を使う）。残りは MANUAL で 1 行ずつ決めた。
抜き取り（audit、先生とモデルが一致）は 186 行を全部見て、誤り 0。

b163 の先例の抜き取り（5 グループ中 3 件が先生と違う）：先例が誤り。会計・項の番号だけの列は id（LABEL_GUIDE「Fund の番号だけなら id」）、
g0094 は崩れた表で S。隠した 10 グループ 13 列は Claude が全部見て、g0017（世帯数の見出しで値が「総人口・女・男」＝崩れた表）→ S、
g0065（款の番号だけ）→ id に直した。残り 8 グループは先例どおり。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from adjudicate_r124 import rule  # noqa: E402

BATCHES = ["b152", "b153", "b156", "b157", "b158", "b159", "b160", "b161", "b162", "b163", "b164", "b165",
           "b166", "b167", "b168", "b169", "b170", "b171", "b173", "b174", "b175"]
MONTH_DAYS = "収集の日（その月の何日。祝日の印つき）＝日付"
MANUAL = {
    "b152#109": ("date", "閉所の時刻（Excel の時刻の数 0.79＝19:00、B8）"),
    "b152#120": ("date", "月（date）"), "b152#121": ("date", "月（合計の行が混ざるが月の列）"),
    "b152#143": ("quantity", "前回との人数の差"), "b152#145": ("quantity", "前回との世帯数の差（△は減）"),
    "b152#161": ("text", "分類のキーワードの羅列（b141#66 と同じ）"),
    "b152#173": ("category", "公園の種別"),
    "b153#7": ("date", "終了日（Excel の日付番号）"),
    "b156#21": ("S", "値が空（null だけ）"), "b156#22": ("S", "値が空（null だけ）"),
    "b156#25": ("S", "値が空（null だけ）"), "b156#26": ("S", "値が空（null だけ）"),
    "b156#23": ("text", "特定の日の説明"), "b156#24": ("text", "休みの日の説明（K5 と同じ）"),
    "b156#44": ("account", "発行元が役所の中の部署（〇〇事務局）"),
    "b156#109": ("address", "投票所の名前（学校・児童館などいろいろな施設、B10-3）"),
    "b158#100": ("amount", "農業産出額の内訳（計・耕種・畜産と並ぶ金額）"),
    "b158#102": ("other", "農地のかい廃の面積（B1：面積は other）"),
    **{f"b158#{i}": ("date", MONTH_DAYS) for i in range(162, 170)},
    "b158#1": ("category", "座標系の区分（EPSG）"), "b158#7": ("category", "座標系の区分（EPSG）"),
    "b158#202": ("category", "福祉避難所の印（1）"),
    "b158#10": ("account", "農林事務所の課の読み（R4）"),
    "b158#87": ("category", "開局の曜日（利用可能曜日と同じ、K5）"),
    "b158#95": ("category", "契約の種類（物品・役務）。お金を分ける科目ではない（B7）"),
    "b158#161": ("category", "ごみの分別（B7）"),
    "b158#2": ("address", "庁舎の名前（見出しがずれた表、b144#8 と同じ）"),
    "b158#8": ("address", "庁舎の名前（見出しがずれた表）"),
    "b175#2": ("address", "庁舎の名前（見出しがずれた表）"), "b175#8": ("address", "庁舎の名前（見出しがずれた表）"),
    "b159#7": ("id", "地区の番号"), "b160#4": ("id", "地区の番号"),
    "b163#50": ("amount", "粗大ごみの手数料（〇〇円。条件の書き添えあり）"),
    "b163#66": ("id", "款の番号だけ（名前は別の列。Fund の番号だけなら id）"),
    "b163#16": ("S", "崩れた表（世帯数の見出しで値が総人口・女・男）"),
    "b163#43": ("other", "1 日平均（統計値、v1.4）"),
    "b163#54": ("category", "出し方の区分のコード"),
    "b163#115": ("other", "大気の測定値（毎時）"), "b163#116": ("other", "大気の測定値（毎時）"),
    "b163#117": ("other", "大気の測定値（毎時）"),
    "b163#49": ("product", "品目の名前（ごみの出し方の質問）"),
    "b163#51": ("text", "品目の読みと言い換えの羅列"),
    "b163#57": ("text", "夜間収集の説明"),
    "b163#134": ("category", "会議の種類（本会議・委員会）"),
    "b163#83": ("address", "区（場所）"), "b163#139": ("address", "区（場所）"),
    "b163#109": ("address", "大気の測定局の名前（場所）"),
    "b164#23": ("category", "会議の種類（合計の行が混ざる）"),
    "b171#2": ("org", "団地の運営の団体（都市再生機構・公社）"),
    "b175#28": ("date", "年度（平成の年の数）"),
}
# 先生とモデルが一致して review に出ていない行でも、先例の誤りは直す（finalize は decisions の行を全部使う）
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
            out.append({"i": r["i"], "label": lab, "reason": why, "by": "claude-20261105"})
        seen = {d["i"] for d in out}
        for key, (lab, why) in EXTRA.items():
            bb, i = key.split("#")
            if bb == b and int(i) not in seen:
                out.append({"i": int(i), "label": lab, "reason": why, "by": "claude-20261105"})
        with open(w / "decisions.jsonl", "w", encoding="utf-8") as fh:
            for d in out:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
        tot[b] = len(out)
    print(tot, sum(tot.values()))


if __name__ == "__main__":
    main()
