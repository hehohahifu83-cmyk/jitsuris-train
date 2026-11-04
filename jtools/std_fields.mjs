import DATA from './std_fields_data.mjs';
export const key = value => String(value ?? '').normalize('NFKC').replace(/^[ \t\r\n\u00a0\ufeff]+|[ \t\r\n\u00a0\ufeff]+$/g, '').toLowerCase();
const INDEX = new Map();
for (const [dataset, name, name_en, format] of DATA.fields) {
  const item = {dataset, name, name_en, format};
  for (const alias of new Set([key(name), key(name_en)])) {
    if (!alias) continue;
    if (!INDEX.has(alias)) INDEX.set(alias, []);
    INDEX.get(alias).push(item);
  }
}
export const lookup = header => (INDEX.get(key(header)) || []).map(item => ({...item}));
