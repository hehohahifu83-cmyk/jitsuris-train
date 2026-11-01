// Python 版と JS 版の道具が同じ結果を出すか（2026-11-01 Claude）。正解は `python jtools/make_fixtures.py` が作る fixtures.json。
//   node --test jtools/
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { readValue, columnSummary as readSummary } from "./read_value.mjs";
import { check, columnSummary as idSummary } from "./check_digits.mjs";
import { relations } from "./table_arith.mjs";
import { runTable } from "./run_tools.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = join(HERE, "..");
const FX = JSON.parse(readFileSync(join(HERE, "fixtures.json"), "utf-8"));

// キーの順と -0 を気にせずに比べる（Python の 1234.0 と JS の 1234 は JSON で同じ数）
const canon = (x) => JSON.stringify(x, (k, v) => (v && typeof v === "object" && !Array.isArray(v)
  ? Object.fromEntries(Object.keys(v).sort().map((key) => [key, v[key]])) : v));
const same = (a, b, msg) => assert.equal(canon(a), canon(b), msg);

test("値の読み取り・番号の検査が Python と同じ", () => {
  for (const f of FX.values) {
    same(readValue(f.in), f.read, `read ${JSON.stringify(f.in)}`);
    same(check(f.in), f.check, `check ${JSON.stringify(f.in)}`);
  }
});

test("列のまとめが Python と同じ", () => {
  for (const f of FX.summaries) {
    same(readSummary(f.in), f.read, `read summary ${JSON.stringify(f.in).slice(0, 60)}`);
    same(idSummary(f.in), f.ids, `id summary ${JSON.stringify(f.in).slice(0, 60)}`);
  }
});

test("本物の表で、道具の結果と計算の関係が Python と同じ", () => {
  const cache = new Map();
  for (const f of FX.tables) {
    if (!cache.has(f.corpus)) {
      const rows = readFileSync(join(ROOT, f.corpus), "utf-8").split("\n").filter((l) => l.trim()).map((l) => JSON.parse(l));
      cache.set(f.corpus, rows);
    }
    const cols = cache.get(f.corpus).filter((r) => r.table === f.table && r.row_values && r.row_values.length);
    same(runTable(cols.map((c) => ({ header: c.header, values: c.values, rows: c.row_values }))), f.result, `table ${f.table}`);
    const aligned = cols.length >= 2 && new Set(cols.map((c) => c.row_values.length)).size === 1;
    same(aligned ? relations(cols.map((c) => ({ header: c.header, rows: c.row_values }))) : [], f.relations, `relations ${f.table}`);
  }
});
