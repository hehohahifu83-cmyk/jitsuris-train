import {columnSummary} from './read_value.mjs';
import {isName} from './facility_kind.mjs';
const READING = /(カナ|かな|ｶﾅ|フリガナ|ふりがな|よみ|読み|英字|英語|ローマ字|通称|_en$|_kana$|_english$|Kana$|English$|En$)/i;
const UNIT = /^(単位|単位名|unit|units|uom|einheit|unit[_ ]of[_ ]measure|unit_meas|measurement[_ ]unit)$/i;
const ID = /(^id$|(^|[_ ])(id|code)($|[_ ])|コード|番号|識別子|code$|identifier$)/i;
const OPERATOR = /^(運営|管理|設置)(者|主体|団体|法人|機関|組織)(名|名称)?$|^(operator|owner|managed_by|operated_by)$/i;
const norm = h => String(h ?? '').replaceAll('\n', ' ').replace(/^[ \t\r\n\u00a0\ufeff]+|[ \t\r\n\u00a0\ufeff]+$/g, '');
export function baseHeader(header) {
  const h = norm(header);
  let b = h.replace(/[_＿（(]?(カナ|かな|ｶﾅ|フリガナ|ふりがな|よみ|読み|英字|英語|ローマ字|通称)[）)]?.*$/, '');
  if (b === h) {
    b = h.replace(/_(en|kana|english)$/i, '');
    if (b === h) b = h.replace(/(Kana|English|En)$/, '');
  }
  b = b.replace(/[\s_＿]+$/, '');
  return b || h;
}
const nonEmpty = a => Array.isArray(a) && a.length ? a : null;
export function findLinks(columns) {
  const headers = columns.map(c => norm(c.header));
  const units = headers.flatMap((h, i) => UNIT.test(h) ? [i] : []);
  const names = headers.flatMap((h, i) => isName(h) && !READING.test(h) ? [i] : []);
  const numeric = columns.flatMap((c, i) => {
    const s = columnSummary(nonEmpty(c.rows) || nonEmpty(c.values) || []);
    return s.n && s.number * 5 >= s.n * 4 && !units.includes(i) && !ID.test(headers[i]) ? [i] : [];
  });
  const out = [];
  headers.forEach((h, i) => {
    const base = baseHeader(h);
    const targets = headers.flatMap((v, j) => j !== i && v.toLowerCase() === base.toLowerCase() ? [j] : []);
    if (READING.test(h) && base !== h) for (const j of targets) out.push({kind: 'reading', source: i, target: j, ambiguous: targets.length > 1});
  });
  for (const i of units) for (const j of numeric) out.push({kind: 'unit', source: i, target: j, ambiguous: units.length > 1});
  headers.forEach((h, i) => {
    if (OPERATOR.test(h)) for (const j of names) if (j !== i) out.push({kind: 'operator', source: i, target: j, ambiguous: names.length > 1});
  });
  return out;
}
