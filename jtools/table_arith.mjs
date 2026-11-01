// 道具 3：表の計算の整合（table_arith.py の JS 版。2026-11-01 Claude）。ここを変えたら table_arith.py も同じに直し、
// `python jtools/make_fixtures.py` で fixtures.json を作り直して `node --test jtools/` を通す。
import { readValue } from "./read_value.mjs";

export const TAX_RATES = [0.10, 0.08, 0.05, 0.077, 0.081, 0.19, 0.20, 0.07];
const MIN_ROWS = 5;
const MAX_COLS = 40;

const num = (v) => { const r = readValue(v); return r.kind === "number" ? r.value : null; };
const enough = (ok, n) => n >= MIN_ROWS && ok * 5 >= n * 4;

export function close(x, y) {
  const d = Math.abs(x - y);
  if (d <= 0.01 || d <= Math.abs(y) * 0.005) return true;
  return Math.abs(y) >= 100 && d <= 1.0;
}

export function closeRound(x, y) {
  const d = Math.abs(x - y);
  return Math.abs(y) >= 100 ? d <= 1.0 : d <= 0.01 + Math.abs(y) * 0.0005;
}

function numericColumns(columns) {
  const out = [];
  for (let i = 0; i < columns.length; i++) {
    const rows = columns[i].rows;
    const vals = rows.map(num);
    const got = vals.filter((v) => v !== null);
    const nonempty = rows.filter((v) => String(v ?? "").trim() !== "").length;
    if (got.length >= MIN_ROWS && got.length * 5 >= nonempty * 4 && new Set(got).size >= 2) out.push([i, vals]);
    if (out.length >= MAX_COLS) break;
  }
  return out;
}

const zip = (...arrs) => arrs[0].map((_, k) => arrs.map((a) => a[k]));

function count(rows, fn) {
  let ok = 0, n = 0;
  for (const r of rows) {
    if (r.some((v) => v === null) || r[r.length - 1] === 0) continue;
    n += 1;
    if (fn(...r)) ok += 1;
  }
  return [ok, n];
}

function pair(i, a, j, b) {
  let [ok, n] = count(zip(a, b), close);
  if (enough(ok, n)) return { rel: "same", cols: [i, j], ok, rows: n };
  const pairs = zip(a, b).filter(([x, y]) => x !== null && y !== null);
  if (pairs.length >= MIN_ROWS) {
    const one = pairs.filter(([x, y]) => (x === 0) !== (y === 0)).length;
    if (one * 10 >= pairs.length * 9 && pairs.some(([x]) => x !== 0) && pairs.some(([, y]) => y !== 0)) {
      return { rel: "one_side", cols: [i, j], ok: one, rows: pairs.length };
    }
  }
  for (const [p, x, q, y] of [[i, a, j, b], [j, b, i, a]]) {
    for (const r of TAX_RATES) {
      [ok, n] = count(zip(x, y), (u, v) => u !== 0 && Math.abs(v) >= 10 && closeRound(u * (1 + r), v));
      if (enough(ok, n)) return { rel: "tax", cols: [p, q], rate: r, ok, rows: n };
      [ok, n] = count(zip(x, y), (u, v) => u !== 0 && Math.abs(v) >= 10 && closeRound(u * r, v));
      if (enough(ok, n)) return { rel: "share", cols: [p, q], rate: r, ok, rows: n };
    }
  }
  return null;
}

function partLeWhole(x, w) {
  const use = zip(x, w).filter(([u, v]) => u !== null && v !== null && v !== 0);
  return use.length > 0 && use.filter(([u, v]) => Math.abs(u) <= Math.abs(v)).length * 5 >= use.length * 4;
}

function triple(cols3) {
  const ids = [...cols3.keys()].sort((a, b) => a - b);
  const others = (k) => ids.filter((x) => x !== k);
  for (const k of ids) {
    const [p, q] = others(k);
    const [ok, n] = count(zip(cols3.get(p), cols3.get(q), cols3.get(k)), (x, y, z) => x !== 0 && y !== 0 && close(x * y, z));
    if (enough(ok, n)) return { rel: "product", cols: [p, q, k], ok, rows: n };
  }
  for (const k of ids) {
    const [p, q] = others(k);
    const [ok, n] = count(zip(cols3.get(p), cols3.get(q), cols3.get(k)), (x, y, z) => x !== 0 && y !== 0 && close(x + y, z));
    if (enough(ok, n)) return { rel: "sum", cols: [p, q, k], ok, rows: n };
  }
  const found = [];
  for (const k of ids) {
    const [p, q] = others(k);
    for (const [part, whole] of [[p, q], [q, p]]) {
      const [ok, n] = count(zip(cols3.get(part), cols3.get(whole), cols3.get(k)), (u, w, z) => w !== 0 && close(u / w * 100, z));
      if (enough(ok, n)) found.push([{ rel: "ratio", cols: [part, whole, k], ok, rows: n }, partLeWhole(cols3.get(part), cols3.get(whole))]);
    }
  }
  if (!found.length) return null;
  const good = found.find(([, g]) => g);
  return good ? good[0] : found[0][0];
}

export function relations(columns) {
  const cols = numericColumns(columns);
  const out = [], same = new Set();
  for (let x = 0; x < cols.length; x++) {
    for (let y = x + 1; y < cols.length; y++) {
      const [i, a] = cols[x], [j, b] = cols[y];
      const r = pair(i, a, j, b);
      if (r) {
        out.push(r);
        if (r.rel === "same") same.add(j);
      }
    }
  }
  const usable = cols.filter(([i]) => !same.has(i));
  for (let x = 0; x < usable.length; x++) {
    for (let y = x + 1; y < usable.length; y++) {
      for (let z = y + 1; z < usable.length; z++) {
        const r = triple(new Map([usable[x], usable[y], usable[z]]));
        if (r) out.push(r);
      }
    }
  }
  return out;
}

export const ROLE = { product: ["factor", "factor", "product_result"], sum: ["addend", "addend", "sum_result"],
  tax: ["tax_base", "tax_included"], share: ["tax_base", "tax_amount"], ratio: ["ratio_part", "ratio_whole", "ratio_result"],
  same: ["same_as_other", "same_as_other"], one_side: ["one_side_pair", "one_side_pair"] };

export function columnTags(columns) {
  const tags = columns.map(() => new Set());
  for (const r of relations(columns)) r.cols.forEach((idx, k) => tags[idx].add(ROLE[r.rel][k]));
  return tags.map((t) => [...t].sort((a, b) => (a < b ? -1 : a > b ? 1 : 0)));
}
