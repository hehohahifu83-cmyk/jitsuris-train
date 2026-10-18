"""FINETUNE_RESULTS.md の 2 つの節（2 回の実行）を並べ、固定試験ごとの差（ポイント）を機械的に出す。

目的：「速い設定にしたら、結果は今までと同じか」を、目で数字を読まずに判定する（読み違い・計算違いを防ぐ）。
決まり：同じ設定の実行どうしでも結果は ±1.5 ポイントほどぶれる。差が 1.5 ポイント未満なら「差なし」と書く。
使い方：python compare_runs.py FINETUNE_RESULTS.md --a "2026-10-17 23:31" --b "仕事1（"
        --a / --b は節の見出しに含まれる文字。1 つに決まらなければ候補を出して止まる（黙って選ばない）。
未見セット（blind_set*）の結果は扱わない（見出し・試験名に blind を含む節は拒否）。
"""
from __future__ import annotations

import argparse
import re
import sys

NOISE = 1.5  # ポイント。これ未満の差は「差なし」

CELL = re.compile(r"^(?P<name>.+?) 正(?P<acc>[\d.]+)% 誤(?P<wrong>\d+) 不明(?P<unk>\d+) 重大(?P<crit>\d+)(?: その他見送り(?P<oc>\d+)/(?P<ot>\d+))?$")
SECONDS = re.compile(r"学習 (?P<train>\d+)秒(?:・評価 (?P<eval>\d+)秒)?")


def parse_sections(text: str):
    """見出し（### …）ごとの {heading, rows}。row = {cond, tests{試験名: セル}, train, eval}。"""
    sections = []
    cur = None
    for line in text.splitlines():
        if line.startswith("### "):
            cur = {"heading": line[4:].strip(), "rows": []}
            sections.append(cur)
            continue
        if cur is None or not line.startswith("|") or "% 誤" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        label = cells[0]
        m = re.search(r"周(?:・水増し)?・(?P<cond>.+)$", label)
        cond = m.group("cond") if m else label
        aug = "・水増し・" in label
        tests = {}
        train = ev = None
        for c in cells[1:]:
            mc = CELL.match(c)
            if mc:
                tests[mc.group("name")] = {k: (float(v) if k == "acc" else int(v) if v is not None else None) for k, v in mc.groupdict().items() if k != "name"}
                continue
            ms = SECONDS.search(c)
            if ms:
                train = int(ms.group("train"))
                ev = int(ms.group("eval")) if ms.group("eval") else None
        cur["rows"].append({"cond": cond, "aug": aug, "tests": tests, "train": train, "eval": ev})
    return sections


def pick(sections, key):
    hits = [s for s in sections if key in s["heading"]]
    if len(hits) != 1:
        names = "\n".join("  - " + s["heading"][:120] for s in hits) or "  （該当なし）"
        raise SystemExit(f"節の指定 {key!r} が 1 つに決まらない（{len(hits)} 件）：\n{names}")
    s = hits[0]
    if "blind" in s["heading"].lower() or any("blind" in t.lower() for r in s["rows"] for t in r["tests"]):
        raise SystemExit("未見セット（blind）の結果は比べない")
    return s


def verdict(diff: float) -> str:
    if abs(diff) < NOISE:
        return "差なし"
    return "上がった" if diff > 0 else "下がった"


def compare(a, b):
    """節 a（基準）と節 b（新しい実行）。条件ごと・試験ごとの差の表と、まとめの文。"""
    lines = []
    out_of_noise = []
    a_rows = {r["cond"]: r for r in a["rows"]}
    for rb in b["rows"]:
        ra = a_rows.get(rb["cond"])
        if ra is None:
            lines.append(f"（条件「{rb['cond']}」は基準に無いので比べない）")
            continue
        lines += ["", f"### 条件：{rb['cond']}", "", "| 試験 | 基準 正解率 | 新 正解率 | 差(pt) | 判定 | 基準 重大 | 新 重大 | 基準 誤 | 新 誤 | 基準 不明 | 新 不明 |", "|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|"]
        for name, tb in rb["tests"].items():
            ta = ra["tests"].get(name)
            if ta is None:
                continue
            d = round(tb["acc"] - ta["acc"], 1)
            v = verdict(d)
            if v != "差なし":
                out_of_noise.append((rb["cond"], name, d, v))
            lines.append(f"| {name} | {ta['acc']:.1f}% | {tb['acc']:.1f}% | {d:+.1f} | {v} | {ta['crit']} | {tb['crit']} | {ta['wrong']} | {tb['wrong']} | {ta['unk']} | {tb['unk']} |")
    secs = [(r["cond"], a_rows[r["cond"]]["train"], r["train"]) for r in b["rows"] if r["cond"] in a_rows and r["train"] and a_rows[r["cond"]]["train"]]
    summary = []
    if secs:
        c, sa, sb = secs[0]
        summary.append(f"学習時間：基準 {sa} 秒 → 新 {sb} 秒（{sa / sb:.2f} 倍速い）" if sb else "")
    if out_of_noise:
        summary.append(f"{NOISE} ポイント以上の差があった（{len(out_of_noise)} 件）：" + "；".join(f"{c}／{n}／{d:+.1f}（{v}）" for c, n, d, v in out_of_noise))
    else:
        summary.append(f"すべての条件・試験で差は {NOISE} ポイント未満（差なし）。")
    return "\n".join(lines), "\n".join(s for s in summary if s), out_of_noise


def noise_table(sections):
    """同じ設定で種だけ違う節（2 つ以上）→ 条件×試験ごとの 平均・最小・最大・幅（ポイント）と、重大の各回。
    『この設定のばらつき』を測るための表。幅が 1.5 ポイントを超える所は、1 回の差を信じない目安になる。"""
    if len(sections) < 2:
        raise SystemExit("ばらつきは 2 つ以上の節がないと出せない")
    lines = [f"種だけ違う {len(sections)} 回のばらつき", "", "| 条件 | 試験 | 平均 | 最小 | 最大 | 幅(pt) | 重大（各回） | 誤（各回） | 不明（各回） |", "|---|---|---|---|---|---|---|---|---|"]
    maxrange = 0.0
    for r0 in sections[0]["rows"]:
        cond = r0["cond"]
        rows = []
        for sec in sections:
            hit = [r for r in sec["rows"] if r["cond"] == cond]
            if not hit:
                rows = None
                break
            rows.append(hit[0])
        if rows is None:
            lines.append(f"（条件「{cond}」はすべての節にはないので出さない）")
            continue
        for name in r0["tests"]:
            cells = [r["tests"].get(name) for r in rows]
            if any(c is None for c in cells):
                continue
            accs = [c["acc"] for c in cells]
            rng = round(max(accs) - min(accs), 1)
            maxrange = max(maxrange, rng)
            lines.append(f"| {cond} | {name} | {sum(accs) / len(accs):.1f}% | {min(accs):.1f}% | {max(accs):.1f}% | {rng:.1f} | {'・'.join(str(c['crit']) for c in cells)} | {'・'.join(str(c['wrong']) for c in cells)} | {'・'.join(str(c['unk']) for c in cells)} |")
    lines += ["", f"最も大きい幅：{maxrange:.1f} ポイント（これを超える差は『種のばらつき』では説明しにくい）"]
    return "\n".join(lines), maxrange


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--a", help="基準の節の見出しに含まれる文字")
    ap.add_argument("--b", help="新しい節の見出しに含まれる文字")
    ap.add_argument("--noise", nargs="+", help="同じ設定で種だけ違う節の見出しに含まれる文字（2 つ以上）。ばらつきの表を出す")
    args = ap.parse_args(argv)
    with open(args.file, encoding="utf-8") as fh:
        sections = parse_sections(fh.read())
    if args.noise:
        table, _ = noise_table([pick(sections, k) for k in args.noise])
        print(table)
        return
    if not (args.a and args.b):
        ap.error("--a と --b（または --noise）が要る")
    a, b = pick(sections, args.a), pick(sections, args.b)
    table, summary, _ = compare(a, b)
    print(f"基準：{a['heading'][:100]}\n新　：{b['heading'][:100]}\n{table}\n\n{summary}")


if __name__ == "__main__":
    main()
