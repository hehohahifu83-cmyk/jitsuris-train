// Chromium の中で、JS の正規化（charsmap.mjs）が正解データ（Hugging Face tokenizers＝Rust の答え）と同じかを調べる。
// Node の試験（charsmap.test.mjs）と同じ比べ方だが、実際にブラウザで動くのは Chromium の Intl.Segmenter（書記素の分け方）なので、そちらでも確かめる。
// 使い方：node browser_test/charsmap.chromium.test.mjs [正解データの場所。省略なら browser_test/fixtures]
//   playwright（と Chromium）が要る。GitHub Actions では browser-model.yml が入れた /tmp/js で動かす。
//   手元で試すときは PLAYWRIGHT_BROWSERS_PATH などで Chromium の場所を教える。
// 1 件でも違えば終了コード 1。最初の数件は、元・JS の答え・正解をコードポイントで出す。
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const dir = path.resolve(process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : path.join(here, 'fixtures'));
const modPath = fs.existsSync(path.join(here, 'charsmap.mjs')) ? path.join(here, 'charsmap.mjs') : path.resolve('charsmap.mjs');

async function loadPlaywright() {
  try { return await import('playwright'); } catch { /* 次へ */ }
  for (const root of [process.cwd(), '/opt/npm-tools/node_modules/']) {
    try { return createRequire(root.endsWith('/') ? root : root + '/')('playwright'); } catch { /* 次へ */ }
  }
  throw new Error('playwright が見つからない');
}
const pw = await loadPlaywright();
const chromium = pw.chromium || pw.default?.chromium;

const server = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split('?')[0]);
  if (u === '/') { res.writeHead(200, { 'content-type': 'text/html' }); res.end('<!doctype html><meta charset=utf-8><title>charsmap</title>'); return; }
  let file = null, type = 'text/plain; charset=utf-8';
  if (u === '/charsmap.mjs') { file = modPath; type = 'text/javascript'; }
  else if (u.startsWith('/fx/')) { file = path.join(dir, path.basename(u)); type = u.endsWith('.json') ? 'application/json' : 'text/plain'; }
  if (!file || !fs.existsSync(file)) { res.writeHead(404); res.end('no'); return; }
  res.writeHead(200, { 'content-type': type }); res.end(fs.readFileSync(file));
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const port = server.address().port;

const browser = await chromium.launch();
let result;
try {
  const page = await browser.newPage();
  page.on('pageerror', (e) => console.log('pageerror', e.message));
  await page.goto(`http://127.0.0.1:${port}/`);
  result = await page.evaluate(async () => {
    const m = await import('/charsmap.mjs');
    const b64 = (await (await fetch('/fx/charsmap.b64')).text()).trim();
    const normalize = m.makeNormalizer(m.parseCharsmap(m.base64ToBytes(b64)));
    const single = await (await fetch('/fx/norm_single.json')).json();
    const cases = await (await fetch('/fx/norm_cases.json')).json();
    const cps = (s) => Array.from(s, (c) => 'U+' + c.codePointAt(0).toString(16).toUpperCase().padStart(4, '0')).join(' ');
    const out = { segmenter: typeof Intl !== 'undefined' && !!Intl.Segmenter, ua: navigator.userAgent, total: 0, bad: 0, groups: [], details: [] };
    const miss = (group, raw, got, want) => { if (out.details.length < 20) out.details.push(`  不一致[${group}] 元 ${cps(raw).slice(0, 120)}\n    JS   ${cps(got).slice(0, 160)}\n    正解 ${cps(want).slice(0, 160)}`); };
    const diff = new Map(Object.entries(single.diff).map(([k, v]) => [Number(k), v]));
    let n = 0, b = 0;
    for (let cp = 0; cp <= 0x10ffff; cp++) {
      if (cp >= 0xd800 && cp <= 0xdfff) continue;
      const raw = String.fromCodePoint(cp);
      const want = diff.has(cp) ? diff.get(cp) : raw;
      const got = normalize(raw);
      n++;
      if (got !== want) { b++; miss('1文字', raw, got, want); }
    }
    out.total += n; out.bad += b; out.groups.push(`1 文字（全スカラー値）: ${n} 件中 不一致 ${b}`);
    for (const [group, list] of Object.entries(cases.groups)) {
      let n2 = 0, b2 = 0;
      for (const [raw, want] of list) {
        const got = normalize(raw);
        n2++;
        if (got !== want) { b2++; miss(group, raw, got, want); }
      }
      out.total += n2; out.bad += b2; out.groups.push(`${group}: ${n2} 件中 不一致 ${b2}`);
    }
    return out;
  });
} finally {
  await browser.close();
  server.close();
}

console.log(result.details.join('\n'));
console.log('=== 要点（この下が注に出る）===');
console.log(`Chromium の中での正規化の一致試験（${result.ua.replace(/^.*?(HeadlessChrome|Chrome)\//, '$1 ').split(' ').slice(0, 2).join(' ')}・Intl.Segmenter ${result.segmenter ? 'あり' : 'なし'}）: 全 ${result.total} 件中 不一致 ${result.bad}`);
for (const l of result.groups) console.log(l);
process.exit(result.bad === 0 && result.segmenter ? 0 : 1);
