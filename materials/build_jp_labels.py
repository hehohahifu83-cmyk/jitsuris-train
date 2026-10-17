"""日本の調達・契約・補助金の表（ChatGPT 提案の出典）のラベル。列名ごとに Claude が先生役で付けた（jp_labels.txt、列名の初出順の番号）。"""
import json, collections, sys
TAG = sys.argv[1] if len(sys.argv) > 1 else "jp"
M = dict(D='date', A='amount', Q='quantity', R='rate', I='id', O='org', P='person', G='product', K='account', T='tax_class', X='text', C='category',
         E='email', H='phone', L='address', Z='other', S=None)
rows = [json.loads(l) for l in open(f"real_corpus_{TAG}.jsonl", encoding="utf-8")]
order = []
for r in rows:
    h = r["header"].strip()
    if h not in order: order.append(h)
import os
if os.path.exists(f"{TAG}_header_labels.json"):  # 列名ごとのラベル（集め直して順番が変わっても崩れない）
    HL = json.load(open(f"{TAG}_header_labels.json", encoding="utf-8"))
    order = [h for h in order if h in HL]
    code = {i: HL[h] for i, h in enumerate(order)}
else:
  code = {}
  for line in open(f"{TAG}_labels.txt"):
    st, *cs = line.split()
    for k, c in enumerate(cs): code[int(st) + k] = c
assert sorted(code) == list(range(len(order))), (len(code), len(order))
lab = {h: M[code[i]] for i, h in enumerate(order)}
out = []
for r in rows:
    l = lab.get(r["header"].strip())
    vals = [v for v in r["values"] if v.strip() and v.strip() not in ("-", "－")]
    if l is None or not vals: continue
    out.append({**{k: r[k] for k in ("source", "table", "header", "values", "context")}, "label": l, "teacher": f"claude-session-2026-10-17-{TAG}"})
open(f"real_labels_{TAG}.jsonl", "w", encoding="utf-8").write("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in out))
print("labelled", len(out), collections.Counter(o["label"] for o in out).most_common())
