"""同じ陣・同じ列名で種類が割れている組を出す（2026-10-30 Claude。LABEL_GUIDE v2.2 の C）。
教材庫（materials/pool/batch_*.jsonl、v2.2 の付け直しのあと）で、同じ陣の中に同じ列名が 2 列以上あり、種類が 2 つ以上に分かれる組。
組ごとに「割れてよい（表が違って意味が違う）」か「付け直す」かを先生が見る。
  python research/labels/split_groups.py   → split_groups.jsonl・sheets/split_NNN.md（先生に渡すシート。1 枚 30 組）
"""
import glob
import json
import os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PER_SHEET = 30


def groups():
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "materials", "pool", "batch_*.jsonl"))):
        b = os.path.basename(p)[len("batch_"):-len(".jsonl")]
        by = defaultdict(list)
        for k, line in enumerate(open(p, encoding="utf-8")):
            r = json.loads(line)
            by[r["header"]].append((k, r))
        for h, cs in by.items():
            labs = Counter(r["label"] for _, r in cs)
            if len(cs) >= 2 and len(labs) >= 2:
                out.append({"gid": f"G{len(out) + 1:03d}", "batch": b, "header": h, "labels": dict(labs),
                            "adjudicated_mixed": len({r.get("teacher", "").startswith(("claude", "Claude")) for _, r in cs}) > 1,
                            "columns": [{"line": k, "label": r["label"], "teacher": r.get("teacher", ""), "table": r["table"],
                                         "values": [str(v) for v in (r.get("row_values") or r["values"])[:8]], "context": r.get("context", [])[:8]}
                                        for k, r in cs]})
    return out


def flat(v):
    return " ".join(str(v).split()).replace("|", "｜")[:60]


def main():
    gs = groups()
    with open(os.path.join(HERE, "split_groups.jsonl"), "w", encoding="utf-8") as f:
        for g in gs:
            f.write(json.dumps(g, ensure_ascii=False) + "\n")
    # シートには、組で多いほうの種類の列を例として 3 列、少ないほうの列は全部載せる。判断するのは少ないほうの列（多いほうに合わせるか、そのままか）
    os.makedirs(os.path.join(HERE, "sheets"), exist_ok=True)
    for f in glob.glob(os.path.join(HERE, "sheets", "split_*.md")):
        os.remove(f)
    for s in range(0, len(gs), PER_SHEET):
        L = [f"# 割れている組の見直し {s // PER_SHEET + 1:03d}（LABEL_GUIDE v2.2）", "",
             "同じ陣・同じ列名なのに種類が割れている組。判断するのは「少ないほうの列」（番号つき）。",
             "`answers/split_NNN.tsv` に少ないほうの列 1 列ずつ 1 行：`gid`・`col`（番号）・`label`（付けるべき種類。今のままなら今の種類、決められなければ unknown）・`reason`。",
             "今のラベルは参考。v2.2 の決まりと、その列の表・値・同じ表の列から決める。表が違って意味が違えば、割れたままでよい。", ""]
        for g in gs[s:s + PER_SHEET]:
            major = Counter(c["label"] for c in g["columns"]).most_common(1)[0][0]
            ex = [c for c in g["columns"] if c["label"] == major][:3]
            L += [f"## {g['gid']}　{g['batch']}「{flat(g['header'])}」（{len(g['columns'])} 列：" + "・".join(f"{k} {v}" for k, v in sorted(g["labels"].items(), key=lambda x: -x[1])) + "）", "",
                  f"多いほうの {major} の例：", ""]
            for c in ex:
                L.append(f"- {' / '.join(flat(v) for v in c['values'])}（同じ表：{'・'.join(flat(x) for x in c['context'])}）")
            L += ["", "| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |", "|---:|---|---|---|---|"]
            for n, c in enumerate(g["columns"], 1):
                if c["label"] != major:
                    L.append(f"| {n} | {c['label']} | {' / '.join(flat(v) for v in c['values'])} | {'・'.join(flat(x) for x in c['context'])} | {c['table'][-60:]} |")
            L.append("")
        open(os.path.join(HERE, "sheets", f"split_{s // PER_SHEET + 1:03d}.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    minor = sum(sum(c["label"] != Counter(x["label"] for x in g["columns"]).most_common(1)[0][0] for c in g["columns"]) for g in gs)
    print("判断する少ないほうの列", minor)
    pairs = Counter("↔".join(sorted(g["labels"])[:2]) for g in gs if len(g["labels"]) == 2)
    print(f"組 {len(gs)}・列 {sum(len(g['columns']) for g in gs)}・裁定が混ざる組 {sum(g['adjudicated_mixed'] for g in gs)}・シート {(len(gs) + PER_SHEET - 1) // PER_SHEET}")
    print(pairs.most_common(8))


if __name__ == "__main__":
    main()
