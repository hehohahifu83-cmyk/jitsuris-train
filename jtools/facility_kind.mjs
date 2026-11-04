import DATA from './facility_rules.mjs';
const PAT = Object.fromEntries(Object.entries(DATA).filter(([k]) => !['KINDS', 'FIXED'].includes(k)).map(([k, [p, i]]) => [k, new RegExp(p, i ? 'i' : '')]));
const KINDS = DATA.KINDS.map(([k, p]) => [k, new RegExp(p)]);
const FIXED = DATA.FIXED.map(([p, label, reason]) => [new RegExp(p), label, reason]);
export const isName = header => PAT.HEAD.test(String(header ?? '')) && !PAT.NOT.test(String(header ?? ''));
export function decide(header, values, context) {
  const h = String(header ?? '');
  const result = (label, reason, rule) => ({label, reason, rule});
  if (!isName(h) || PAT.READING.test(h)) return result('unknown', '名称列以外・読みの列は元の名称列で確認', '');
  for (const [pat, label, reason] of FIXED) if (pat.test(h)) return result(label, reason, 'fixed');
  const vals = (values || []).filter(v => v != null && String(v).trim() && !['nan', 'None', '-'].includes(String(v).trim())).map(String);
  const ctx = (context || []).map(String).join(' ');
  const kinds = new Set(vals.flatMap(v => KINDS.filter(([, p]) => p.test(v)).map(([k]) => k)));
  const org = vals.filter(v => PAT.ORG_V.test(v)).length;
  const place = vals.filter(v => PAT.PLACE_V.test(v)).length;
  const inst = vals.filter(v => PAT.INST_V.test(v) && !PAT.PLACE_V.test(v)).length;
  const n = Math.max(vals.length, 1);
  if (PAT.LIC.test(ctx)) return result('org', '営業許可・登録の台帳の店名（B10-2）', 'B10-2');
  if (org * 5 >= 3 * n) return result('org', '値の多くが団体・会社の名前（B10-4）', 'B10-4');
  if (PAT.USE_LOC.test(ctx)) return result('address', '避難所・投票所・設置場所など場所として使う一覧（B10-3）', 'B10-3');
  if (kinds.size >= 3 && !PAT.INST_C.test(ctx)) return result('address', `いろいろな種類の施設が並ぶ一覧（${kinds.size} 種類、B10-3）`, 'B10-3');
  if (place * 2 >= n) return result('address', '値の多くが場所そのものの名前（体育館・校庭・公園など、v1.7、B10-3）', 'B10-3');
  if (inst * 5 >= 3 * n) return result('org', '同じ種類の機関の名簿（B10-1）', 'B10-1');
  if (PAT.LOC_C.test(ctx) && !PAT.INST_C.test(ctx)) return result('address', 'いろいろな施設の一覧で場所の属性が付く（B10-3）', 'B10-3');
  return result('unknown', '規則で決めきれない', '');
}
