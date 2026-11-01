// 道具 2：番号の検査数字と形（check_digits.py の JS 版。2026-11-01 Claude）。ここを変えたら check_digits.py も同じに直し、
// `python jtools/make_fixtures.py` で fixtures.json を作り直して `node --test jtools/` を通す。

export const SCHEMES = ["corp_jp", "invoice_jp", "gtin", "isbn", "iban", "luhn16", "lgcode_jp", "postcode_jp", "postcode_uk", "postcode_ca", "postcode_us"];

const c = (v) => String(v ?? "").normalize("NFKC").trim();
const digits = (s) => [...s].map((ch) => parseInt(ch, 10));

export function corpJp(s) {
  if (!/^[0-9]{13}$/.test(s)) return false;
  const body = digits(s.slice(1)).reverse();
  let total = 0;
  body.forEach((d, i) => { total += d * ((i + 1) % 2 === 1 ? 1 : 2); });
  return parseInt(s[0], 10) === 9 - (total % 9);
}

export function invoiceJp(s) {
  const t = s.replaceAll("-", "").replaceAll(" ", "");
  return /^[Tt][0-9]{13}$/.test(t) && corpJp(t.slice(1));
}

function gtinOk(d) {
  const body = digits(d.slice(0, -1)).reverse();
  let total = 0;
  body.forEach((x, i) => { total += x * (i % 2 === 0 ? 3 : 1); });
  return (10 - (total % 10)) % 10 === parseInt(d[d.length - 1], 10);
}

export function gtin(s) {
  const t = s.replaceAll(" ", "");
  if (!/^(?:[0-9]{8}|[0-9]{12,14})$/.test(t) || /^0+$/.test(t)) return false;
  return gtinOk(t);
}

export function isbn(s) {
  const t = s.replace(/^isbn[:\s-]*/i, "").replaceAll("-", "").replaceAll(" ", "");
  if (/^97[89][0-9]{10}$/.test(t)) return gtinOk(t);
  if (/^[0-9]{9}[0-9Xx]$/.test(t)) {
    let total = 0;
    [...t].forEach((ch, i) => { total += (10 - i) * ("Xx".includes(ch) ? 10 : parseInt(ch, 10)); });
    return total % 11 === 0 && !/^0+$/.test(t);
  }
  return false;
}

export function iban(s) {
  const t = s.replaceAll(" ", "").toUpperCase();
  if (!/^[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}$/.test(t)) return false;
  const r = t.slice(4) + t.slice(0, 4);
  const num = [...r].map((ch) => String(parseInt(ch, 36))).join("");
  let rem = 0;
  for (let i = 0; i < num.length; i += 9) rem = parseInt(String(rem) + num.slice(i, i + 9), 10) % 97;
  return rem === 1;
}

export function luhn16(s) {
  const t = s.replaceAll(" ", "").replaceAll("-", "");
  if (!/^[0-9]{16}$/.test(t) || new Set(t).size === 1) return false;
  let total = 0;
  digits(t).reverse().forEach((d0, i) => {
    let d = d0;
    if (i % 2 === 1) { d *= 2; if (d > 9) d -= 9; }
    total += d;
  });
  return total % 10 === 0;
}

export function lgcodeJp(s) {
  if (!/^[0-9]{6}$/.test(s)) return false;
  const pref = parseInt(s.slice(0, 2), 10);
  if (!(pref >= 1 && pref <= 47)) return false;
  const w = [6, 5, 4, 3, 2];
  let total = 0;
  for (let i = 0; i < 5; i++) total += parseInt(s[i], 10) * w[i];
  return (11 - (total % 11)) % 10 === parseInt(s[5], 10);
}

export const postcodeJp = (s) => /^〒?\s?[0-9]{3}-[0-9]{4}$/.test(s);
export const postcodeUk = (s) => /^(?:GIR 0AA|[A-PR-UWYZ][A-HK-Y]?[0-9][0-9A-HJKMNPR-Y]? ?[0-9][ABD-HJLNP-UW-Z]{2})$/.test(s.toUpperCase());
export const postcodeCa = (s) => /^[ABCEGHJ-NPRSTVXY][0-9][ABCEGHJ-NPRSTV-Z] ?[0-9][ABCEGHJ-NPRSTV-Z][0-9]$/.test(s.toUpperCase());
export const postcodeUs = (s) => /^[0-9]{5}-[0-9]{4}$/.test(s);

const FN = { corp_jp: corpJp, invoice_jp: invoiceJp, gtin, isbn, iban, luhn16, lgcode_jp: lgcodeJp,
  postcode_jp: postcodeJp, postcode_uk: postcodeUk, postcode_ca: postcodeCa, postcode_us: postcodeUs };

export function check(value) {
  const s = c(value);
  if (!s) return [];
  return SCHEMES.filter((k) => FN[k](s));
}

export function columnSummary(values) {
  const vals = [...new Set(values.map(c).filter((v) => v))];
  const out = { n: vals.length };
  for (const k of SCHEMES) {
    const hit = vals.filter((v) => FN[k](v)).length;
    if (hit) out[k] = hit;
  }
  return out;
}
