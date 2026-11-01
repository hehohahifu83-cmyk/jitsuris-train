// 道具をまとめて決まった順で呼ぶ（run_tools.py の JS 版。2026-11-01 Claude）。ブラウザでもそのまま動く（外と通信しない）。
// 順番：1 値の読み取り → 2 番号の検査数字 → 3 表の計算の整合（行のそろった値があるときだけ）。
import * as RV from "./read_value.mjs";
import * as CD from "./check_digits.mjs";
import * as TA from "./table_arith.mjs";

const TAG_TEXT = { product_result: "他の2列の積", factor: "積の因数", sum_result: "他の2列の和", addend: "和の項",
  tax_included: "税込", tax_base: "税抜", tax_amount: "税額", ratio_result: "比率の結果", ratio_part: "比率の分子",
  ratio_whole: "比率の分母", same_as_other: "他の列と同じ値", one_side_pair: "片側だけの組" };
const CD_TEXT = { corp_jp: "法人番号", invoice_jp: "インボイス番号", gtin: "JAN/EAN", isbn: "ISBN", iban: "IBAN", luhn16: "カード番号の形",
  lgcode_jp: "団体コード", postcode_jp: "郵便番号(日)", postcode_uk: "郵便番号(英)", postcode_ca: "郵便番号(加)", postcode_us: "ZIP" };

const nonEmpty = (a) => (Array.isArray(a) && a.length ? a : null);

export function runTable(columns) {
  const out = columns.map((c) => {
    const vals = nonEmpty(c.rows) || nonEmpty(c.values) || [];
    return { read: RV.columnSummary(vals), ids: CD.columnSummary(vals), arith: [] };
  });
  const withRows = columns.map((c, i) => (nonEmpty(c.rows) ? i : -1)).filter((i) => i >= 0);
  if (withRows.length >= 2 && new Set(withRows.map((i) => columns[i].rows.length)).size === 1) {
    const tags = TA.columnTags(withRows.map((i) => ({ header: columns[i].header ?? "", rows: columns[i].rows })));
    withRows.forEach((i, k) => { out[i].arith = tags[k]; });
  }
  for (const r of out) r.text = toText(r);
  return out;
}

const pct = (c, n) => `${Math.floor((200 * c + n) / (2 * n))}%`;

export function toText(r) {
  const parts = [];
  const rd = r.read;
  const n = rd.n;
  if (n) {
    for (const [k, name] of [["date", "日付"], ["time", "時刻"], ["number", "数"]]) {
      if (rd[k] * 2 >= n) { parts.push(`${name}${pct(rd[k], n)}`); break; }
    }
    if (rd.currency && rd.number * 2 >= n) parts.push(`通貨${rd.currency}`);
    if (rd.unit && rd.number * 2 >= n) parts.push(`単位${rd.unit}`);
    if (rd.era * 2 >= n) parts.push("和暦");
    if (rd.kanji * 2 >= n) parts.push("漢数字");
    if (rd.neg) parts.push(`負${pct(rd.neg, n)}`);
  }
  const m = r.ids.n || 0;
  for (const k of CD.SCHEMES) {
    if (m >= 3 && (r.ids[k] || 0) * 5 >= m * 4) parts.push(CD_TEXT[k]);
  }
  for (const t of r.arith) parts.push(TAG_TEXT[t]);
  return parts.join(" ");
}
