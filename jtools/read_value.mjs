// 道具 1：値の読み取り（read_value.py の JS 版。2026-11-01 Claude）。ここを変えたら read_value.py も同じに直し、
// `python jtools/make_fixtures.py` で fixtures.json を作り直して `node --test jtools/` を通す。

const ERAS = { 明治: 1867, 大正: 1911, 昭和: 1925, 平成: 1988, 令和: 2018, M: 1867, T: 1911, S: 1925, H: 1988, R: 2018 };
const ERA_NAME = { M: "明治", T: "大正", S: "昭和", H: "平成", R: "令和" };

const CUR_PREFIX = [["US$", "USD"], ["C$", "CAD"], ["A$", "AUD"], ["NZ$", "NZD"], ["HK$", "HKD"], ["CHF", "CHF"], ["EUR", "EUR"], ["USD", "USD"],
  ["GBP", "GBP"], ["JPY", "JPY"], ["CAD", "CAD"], ["AUD", "AUD"], ["$", "USD"], ["€", "EUR"], ["£", "GBP"], ["¥", "JPY"], ["₩", "KRW"],
  ["Fr.", "CHF"], ["R$", "BRL"]];
const CUR_SUFFIX = [["百万円", "JPY", 1000000], ["千万円", "JPY", 10000000], ["億円", "JPY", 100000000], ["万円", "JPY", 10000], ["千円", "JPY", 1000],
  ["円", "JPY", 1], ["ドル", "USD", 1], ["ユーロ", "EUR", 1], ["ポンド", "GBP", 1], ["EUR", "EUR", 1], ["USD", "USD", 1], ["CHF", "CHF", 1],
  ["GBP", "GBP", 1], ["JPY", "JPY", 1], ["CAD", "CAD", 1], ["€", "EUR", 1], ["Fr.", "CHF", 1], ["€", "EUR", 1]];
const UNIT_SUFFIX = [["%", 1], ["‰", 1], ["pt", 1], ["ポイント", 1], ["百万", 1000000], ["千", 1000], ["万", 10000], ["億", 100000000],
  ["km2", 1], ["km²", 1], ["m2", 1], ["m²", 1], ["m3", 1], ["m³", 1], ["km", 1], ["kg", 1], ["mg", 1], ["ha", 1], ["kWh", 1], ["MWh", 1],
  ["cm", 1], ["mm", 1], ["ml", 1], ["t", 1], ["g", 1], ["m", 1], ["l", 1],
  ["人", 1], ["件", 1], ["個", 1], ["台", 1], ["回", 1], ["戸", 1], ["世帯", 1], ["箇所", 1], ["か所", 1], ["本", 1], ["枚", 1], ["歳", 1],
  ["才", 1], ["日", 1], ["時間", 1], ["分", 1], ["年", 1], ["か月", 1], ["ヶ月", 1]];

const KANJI_DIGIT = { "〇": 0, 零: 0, 一: 1, 壱: 1, 二: 2, 弐: 2, 三: 3, 参: 3, 四: 4, 五: 5, 六: 6, 七: 7, 八: 8, 九: 9 };
const KANJI_SMALL = { 十: 10, 拾: 10, 百: 100, 千: 1000 };
const KANJI_BIG = { 万: 10000, 億: 100000000, 兆: 1000000000000 };
const DIGITS = "0123456789";

const NUM = /^(?:[0-9]+(\.[0-9]+)?|\.[0-9]+)$/;
const EMPTY = new Set(["", "-", "−", "—", "–", "na", "n/a", "nan", "null", "none", "…", "x", "*", "..", "."]);

export function clean(s) {
  let t = String(s ?? "").normalize("NFKC");
  t = t.replaceAll("​", "").replaceAll("﻿", "").replaceAll("−", "-").replaceAll("–", "-").replaceAll("—", "-");
  return t.replace(/\s+/g, " ").trim();
}

function kanjiNumber(s) {
  if (!s || !/^[0-9〇零一壱二弐三参四五六七八九十拾百千万億兆]+$/.test(s) || /^[0-9]+$/.test(s)) return null;
  if (s === "〇" || s === "零") return null;
  let total = 0, section = 0, digits = "";
  for (const ch of s) {
    if (DIGITS.includes(ch) || ch in KANJI_DIGIT) {
      digits += DIGITS.includes(ch) ? ch : String(KANJI_DIGIT[ch]);
    } else if (ch in KANJI_SMALL) {
      section += (digits ? parseInt(digits, 10) : 1) * KANJI_SMALL[ch];
      digits = "";
    } else if (ch in KANJI_BIG) {
      section += digits ? parseInt(digits, 10) : 0;
      if (section === 0) return null;
      total += section * KANJI_BIG[ch];
      section = 0; digits = "";
    }
  }
  section += digits ? parseInt(digits, 10) : 0;
  return total + section;
}

const int = (x) => (x ? parseInt(x, 10) : 0);

function mk(y, m, d, era, fiscal) {
  if (!(y >= 1800 && y <= 2200) || !(m >= 0 && m <= 12) || !(d >= 0 && d <= 31) || (d && !m)) return null;
  return { kind: "date", y, m, d, era, fiscal };
}

function readDate(t) {
  let m = t.match(/^(明治|大正|昭和|平成|令和)\s?([0-9]{1,2}|元)\s?年(度)?(?:\s?([0-9]{1,2})\s?月(?:\s?([0-9]{1,2})\s?日)?)?$/);
  if (m) {
    const y = m[2] === "元" ? 1 : parseInt(m[2], 10);
    return mk(ERAS[m[1]] + y, int(m[4]), int(m[5]), m[1], Boolean(m[3]));
  }
  m = t.match(/^([MTSHR])\s?([0-9]{1,2})\s?[.\-/]\s?([0-9]{1,2})\s?[.\-/]\s?([0-9]{1,2})$/i);
  if (m) {
    const e = m[1].toUpperCase();
    return mk(ERAS[e] + parseInt(m[2], 10), parseInt(m[3], 10), parseInt(m[4], 10), ERA_NAME[e], false);
  }
  m = t.match(/^([0-9]{4})\s?年\s?(度)?(?:\s?([0-9]{1,2})\s?月(?:\s?([0-9]{1,2})\s?日)?)?$/);
  if (m) return mk(parseInt(m[1], 10), int(m[3]), int(m[4]), "", Boolean(m[2]));
  m = t.match(/^([0-9]{4})([\-/.])([0-9]{1,2})(?:\2([0-9]{1,2}))?(?:[ T]([0-9]{1,2}):([0-9]{2})(?::([0-9]{2})(?:\.[0-9]+)?)?(?:Z|[+\-][0-9]{2}:?[0-9]{2})?)?$/);
  if (m) return mk(parseInt(m[1], 10), parseInt(m[3], 10), int(m[4]), "", false);
  m = t.match(/^([0-9]{1,2})\.([0-9]{1,2})\.([0-9]{4})$/);
  if (m) return mk(parseInt(m[3], 10), parseInt(m[2], 10), parseInt(m[1], 10), "", false);
  m = t.match(/^([0-9]{1,2})\/([0-9]{1,2})\/([0-9]{4})(?: [0-9]{1,2}:[0-9]{2}(?::[0-9]{2})?(?: ?[AP]M)?)?$/i);
  if (m) {
    const a = parseInt(m[1], 10), b = parseInt(m[2], 10);
    const [mo, d] = a > 12 ? [b, a] : [a, b];
    return mk(parseInt(m[3], 10), mo, d, "", false);
  }
  return null;
}

export function readValue(raw) {
  const t = clean(raw);
  if (EMPTY.has(t.toLowerCase())) return { kind: "empty" };
  const d = readDate(t);
  if (d) return d;
  const m = t.match(/^([0-9]{1,2}):([0-9]{2})(?::([0-9]{2}))?$/);
  if (m && parseInt(m[1], 10) <= 24 && parseInt(m[2], 10) < 60 && int(m[3]) < 60) {
    return { kind: "time", h: parseInt(m[1], 10), mi: parseInt(m[2], 10), s: int(m[3]) };
  }
  return readNumber(t) || { kind: "text" };
}

function readNumber(t) {
  let s = t.replaceAll(" ", "");
  let neg = false;
  if (s.startsWith("(") && s.endsWith(")")) { neg = true; s = s.slice(1, -1); }
  if (["-", "△", "▲"].includes(s.slice(0, 1))) { neg = true; s = s.slice(1); }
  else if (s.slice(0, 1) === "+") s = s.slice(1);
  let currency = "", unit = "", scale = 1;
  for (const [sym, code] of CUR_PREFIX) {
    if (s.startsWith(sym) && s.length > sym.length) { currency = code; s = s.slice(sym.length); break; }
  }
  if (["-", "△", "▲"].includes(s.slice(0, 1)) && !neg) { neg = true; s = s.slice(1); }
  for (const [suf, code, sc] of CUR_SUFFIX) {
    if (s.endsWith(suf) && s.length > suf.length) {
      if (currency && currency !== code) return null;
      currency = code; s = s.slice(0, -suf.length); scale = sc;
      unit = sc !== 1 ? suf : "";
      break;
    }
  }
  const kanji = (k) => ({ kind: "number", value: neg ? -k : k, neg, sep: false, decimals: 0, currency, unit, scale, kanji: true });
  let k = kanjiNumber(s);
  if (k !== null) return kanji(k);
  if (!unit) {
    for (const [suf, sc] of UNIT_SUFFIX) {
      if (s.endsWith(suf) && s.length > suf.length) {
        const head = s.slice(0, -suf.length);
        if (!/[0-9〇零一壱二弐三参四五六七八九十拾百千万億兆]$/.test(head)) continue;
        unit = suf; s = head; scale = sc;
        break;
      }
    }
  }
  if (s.endsWith("-")) { neg = true; s = s.slice(0, -1); }
  k = kanjiNumber(s);
  if (k !== null) return kanji(k);
  let sep = false;
  if (/^[0-9]{1,3}(,[0-9]{3})+(\.[0-9]+)?$/.test(s)) { sep = true; s = s.replaceAll(",", ""); }
  else if (/^[0-9]{1,3}(\.[0-9]{3})+,[0-9]+$/.test(s)) { sep = true; s = s.replaceAll(".", "").replaceAll(",", "."); }
  else if (/^[0-9]{1,3}('[0-9]{3})+(\.[0-9]+)?$/.test(s)) { sep = true; s = s.replaceAll("'", ""); }
  else if (/^[0-9]+,[0-9]{1,2}$/.test(s)) s = s.replaceAll(",", ".");
  if (!NUM.test(s)) return null;
  const dot = s.indexOf(".");
  const dec = dot < 0 ? 0 : s.length - dot - 1;
  const v = parseFloat(s);
  return { kind: "number", value: neg ? -v : v, neg, sep, decimals: dec, currency, unit, scale, kanji: false };
}

const byCode = (a, b) => (a < b ? -1 : a > b ? 1 : 0);

export function columnSummary(values) {
  const rs = values.map(readValue);
  const ne = rs.filter((r) => r.kind !== "empty");
  const nums = ne.filter((r) => r.kind === "number");
  const curs = [...new Set(nums.filter((r) => r.currency).map((r) => r.currency))].sort(byCode);
  const units = [...new Set(nums.filter((r) => r.unit).map((r) => r.unit))].sort(byCode);
  const count = (arr, f) => arr.filter(f).length;
  return {
    n: ne.length,
    number: nums.length,
    date: count(ne, (r) => r.kind === "date"),
    time: count(ne, (r) => r.kind === "time"),
    text: count(ne, (r) => r.kind === "text"),
    currency: curs.length === 1 ? curs[0] : curs.length ? "mixed" : "",
    unit: units.length === 1 ? units[0] : units.length ? "mixed" : "",
    era: count(ne, (r) => r.kind === "date" && Boolean(r.era)),
    kanji: count(nums, (r) => r.kanji),
    neg: count(nums, (r) => r.neg),
  };
}
