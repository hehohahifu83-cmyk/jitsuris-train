// ブラウザ（headless Chromium・WASM）で、書き出したモデルを Transformers.js で動かす試験。外への通信はすべて止める。
// 使い方：node browser_test/run.mjs <書き出したモデルの場所> <reference.json> <結果を書く場所> [node_modules の場所]
// 見るもの：①トークナイザの番号が Python（HF tokenizers）と一致するか ②logits が onnxruntime（CPU）の INT8 と近いか ③1 列ずつ流したときの時間
// 数字は GitHub Actions のサーバーの CPU 上の Chromium の結果で、スマホの実機の速さではない。
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { chromium } from 'playwright';

const [modelDir, refPath, outPath, nodeModules = 'node_modules'] = process.argv.slice(2);
const LIB_DIRS = [`${nodeModules}/@huggingface/transformers/dist`, `${nodeModules}/onnxruntime-web/dist`];
const TYPES = { '.js': 'text/javascript', '.mjs': 'text/javascript', '.wasm': 'application/wasm', '.json': 'application/json', '.html': 'text/html' };
const HEADERS = { 'Cross-Origin-Opener-Policy': 'same-origin', 'Cross-Origin-Embedder-Policy': 'require-corp', 'Cross-Origin-Resource-Policy': 'same-origin' };
const WEB_BUILDS = ['transformers.web.min.js', 'transformers.web.js', 'transformers.min.js', 'transformers.js'].filter((f) => fs.existsSync(path.join(LIB_DIRS[0], f)));
if (!WEB_BUILDS.length) throw new Error('Transformers.js のブラウザ用の build が見つからない: ' + fs.readdirSync(LIB_DIRS[0]).join(','));
const IMPORT_MAP = {};   // 裸の import（onnxruntime-web など）があれば、同じ場所の ort.*.mjs に向ける
for (const [spec, file] of [['onnxruntime-web', 'ort.bundle.min.mjs'], ['onnxruntime-web/webgpu', 'ort.webgpu.bundle.min.mjs'], ['onnxruntime-web/wasm', 'ort.wasm.bundle.min.mjs'], ['onnxruntime-common', 'ort.min.mjs']]) {
  if (LIB_DIRS.some((d) => fs.existsSync(path.join(d, file)))) IMPORT_MAP[spec] = '/lib/' + file;
}
let webBuild = WEB_BUILDS[0];

const pageHtml = () => `<!doctype html><meta charset="utf-8"><title>browser model test</title>
<script type="importmap">${JSON.stringify({ imports: IMPORT_MAP })}</script>
<script type="module">
import { env, AutoTokenizer, AutoModelForSequenceClassification, Tensor } from '/lib/${webBuild}';
env.allowRemoteModels = false; env.allowLocalModels = true; env.localModelPath = '/model_root/'; env.useBrowserCache = false;
env.backends.onnx.wasm.wasmPaths = '/lib/';
let tokenizerPromise = null;
const getTokenizer = () => (tokenizerPromise ??= AutoTokenizer.from_pretrained('model'));
// Python 側（HF tokenizers の truncation=True, max_length=128）と同じ切り方：長いときは先頭 127 個＋最後の </s>。
// Transformers.js の truncation は単に切るだけで </s> が落ちるので、切らずに取って自分で切る。
const capIds = (ids) => (ids.length <= 128 ? ids : ids.slice(0, 127).concat([ids[ids.length - 1]]));
const encodeIds = (tokenizer, text) => capIds(Array.from(tokenizer(text, { truncation: false }).input_ids.data, Number));
const toInputs = (ids) => ({ input_ids: new Tensor('int64', BigInt64Array.from(ids, BigInt), [1, ids.length]), attention_mask: new Tensor('int64', new BigInt64Array(ids.length).fill(1n), [1, ids.length]) });
window.__tokenize = async (texts) => {
  const tokenizer = await getTokenizer();
  const t0 = performance.now();
  const ids = texts.map((t) => encodeIds(tokenizer, t));
  return { ids, ms: performance.now() - t0 };
};
window.__run = async ({ texts, threads, warmup }) => {
  env.backends.onnx.wasm.numThreads = threads;
  const t0 = performance.now();
  const tokenizer = await getTokenizer();
  const tTok = performance.now() - t0;
  const model = await AutoModelForSequenceClassification.from_pretrained('model', { dtype: 'q8', device: 'wasm' });
  const loadMs = performance.now() - t0;
  const ids = [], logits = [], times = [], tokMs = [];
  for (const t of texts) {
    const s0 = performance.now();
    ids.push(encodeIds(tokenizer, t));
    tokMs.push(performance.now() - s0);
  }
  for (let i = 0; i < texts.length; i++) {
    const inputs = toInputs(ids[i]);
    const s = performance.now();
    const out = await model(inputs);
    times.push(performance.now() - s);
    logits.push(Array.from(out.logits.data));
  }
  return { tokenizerMs: tTok, loadMs, ids, logits, tokMs, times: times.slice(warmup), isolated: self.crossOriginIsolated === true, threads: env.backends.onnx.wasm.numThreads };
};
window.__ready = true;
</script>`;

const served = new Map();   // 配ったファイルと大きさ（初回に取り込む量の目安）
function send(res, file) {
  if (!file || !fs.existsSync(file) || !fs.statSync(file).isFile()) { res.writeHead(404); res.end('not found'); return; }
  served.set(path.basename(file), { size: fs.statSync(file).size, file });
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream', ...HEADERS });
  fs.createReadStream(file).pipe(res);
}

const server = http.createServer((req, res) => {
  const url = decodeURIComponent(req.url.split('?')[0]);
  if (url === '/') { res.writeHead(200, { 'Content-Type': 'text/html', ...HEADERS }); res.end(pageHtml()); return; }
  if (url.startsWith('/lib/')) { const name = path.basename(url); send(res, LIB_DIRS.map((d) => path.join(d, name)).find((f) => fs.existsSync(f))); return; }
  if (url.startsWith('/model_root/model/')) {
    const rel = path.normalize(url.slice('/model_root/model/'.length));
    if (rel.startsWith('..')) { res.writeHead(403); res.end(); return; }
    send(res, path.join(modelDir, rel)); return;
  }
  res.writeHead(404); res.end('not found');
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const base = `http://127.0.0.1:${server.address().port}`;

const ref = JSON.parse(fs.readFileSync(refPath, 'utf-8'));
const argmax = (a) => a.indexOf(Math.max(...a));
const pieces = (() => { try { return JSON.parse(fs.readFileSync(path.join(modelDir, 'tokenizer.json'), 'utf-8')).model.vocab.map((v) => v[0]); } catch { return null; } })();
const piece = (id) => (pieces && pieces[id] !== undefined ? pieces[id] : String(id));
const result = { builds: WEB_BUILDS, importMap: IMPORT_MAP, n: ref.texts.length, runs: [], blocked: [], console: [], tried: [] };
const browser = await chromium.launch({ headless: true });
async function openPage(threads) {
  const ctx = await browser.newContext({ serviceWorkers: 'block' });
  const page = await ctx.newPage();
  page.on('console', (m) => { if (result.console.length < 60) result.console.push(`[${threads}/${webBuild}] ${m.type()}: ${m.text().slice(0, 300)}`); });
  page.on('pageerror', (e) => result.console.push(`[${threads}/${webBuild}] pageerror: ${String(e).slice(0, 400)}`));
  page.on('requestfailed', (r) => { if (result.console.length < 60) result.console.push(`[${threads}] requestfailed: ${r.url().slice(0, 150)} ${r.failure()?.errorText}`); });
  await page.route('**/*', (route) => {
    const u = route.request().url();
    if (u.startsWith(base + '/') || u.startsWith('data:') || u.startsWith('blob:')) return route.continue();
    result.blocked.push(u.slice(0, 200)); return route.abort();
  });
  await page.goto(base + '/');
  return { ctx, page };
}
try {
  // どのビルドでページが立ち上がるか（裸の import で失敗するものがある）
  let ok = false;
  for (const b of WEB_BUILDS) {
    webBuild = b;
    const { ctx, page } = await openPage(1);
    try { await page.waitForFunction(() => window.__ready === true, null, { timeout: 20000 }); ok = true; result.tried.push({ build: b, ready: true }); await ctx.close(); break; }
    catch (e) { result.tried.push({ build: b, ready: false, error: String(e).slice(0, 200) }); await ctx.close(); }
  }
  if (ok && ref.tok_texts) {
    const { ctx, page } = await openPage(1);
    await page.waitForFunction(() => window.__ready === true, null, { timeout: 60000 });
    const tk = await page.evaluate((t) => window.__tokenize(t), ref.tok_texts);
    const edgeFrom = ref.edge_from ?? ref.tok_texts.length;
    const bad = [];
    tk.ids.forEach((ids, i) => {
      const want = ref.tok_ids[i];
      if (JSON.stringify(ids) === JSON.stringify(want)) return;
      let k = 0; while (k < Math.min(ids.length, want.length) && ids[k] === want[k]) k++;
      const lo = Math.max(0, k - 2);
      bad.push({ i, edge: i >= edgeFrom, firstDiff: k, lenGot: ids.length, lenWant: want.length, got: ids.slice(lo, k + 5).map(piece), want: want.slice(lo, k + 5).map(piece),
        text: i >= edgeFrom ? ref.tok_texts[i].slice(0, 40) : undefined,
        codepoints: [...new Set([...ref.tok_texts[i]].filter((c) => c.codePointAt(0) > 127))].slice(0, 10).map((c) => 'U+' + c.codePointAt(0).toString(16).toUpperCase()) });
    });
    result.tokParity = { total: ref.tok_texts.length, edge: ref.tok_texts.length - edgeFrom, mismatches: bad.length, mismatchesEdge: bad.filter((b) => b.edge).length, ms: Math.round(tk.ms), first: bad.slice(0, 12) };
    await ctx.close();
  }
  if (ok) {
    result.build = webBuild;
    for (const threads of [1, 2, 4]) {
      const { ctx, page } = await openPage(threads);
      await page.waitForFunction(() => window.__ready === true, null, { timeout: 60000 });
      const t0 = Date.now();
      let r;
      try {
        r = await page.evaluate((o) => window.__run(o), { texts: ref.texts, threads, warmup: 3 });
      } catch (e) {
        result.runs.push({ threads, error: String(e).slice(0, 600) }); await ctx.close(); continue;
      }
      let idMismatch = 0;
      const mism = [];
      r.ids.forEach((ids, i) => {
        const want = ref.ids[i];
        if (JSON.stringify(ids) === JSON.stringify(want)) return;
        idMismatch++;
        let k = 0; while (k < Math.min(ids.length, want.length) && ids[k] === want[k]) k++;
        const lo = Math.max(0, k - 2);
        mism.push({ i, firstDiff: k, lenGot: ids.length, lenWant: want.length,
          got: ids.slice(lo, k + 6).map(piece), want: want.slice(lo, k + 6).map(piece),
          gotIds: ids.slice(lo, k + 6), wantIds: want.slice(lo, k + 6),
          codepoints: [...new Set([...ref.texts[i]].filter((c) => c.codePointAt(0) > 127))].slice(0, 12).map((c) => 'U+' + c.codePointAt(0).toString(16).toUpperCase()) });
      });
      if (threads === 1) result.mismatches = mism;
      let maxQ = 0, maxF = 0, agreeQ = 0;
      r.logits.forEach((lg, i) => { lg.forEach((v, k) => { maxQ = Math.max(maxQ, Math.abs(v - ref.logits_q[i][k])); maxF = Math.max(maxF, Math.abs(v - ref.logits_f[i][k])); }); if (argmax(lg) === argmax(ref.logits_q[i])) agreeQ++; });
      const ts = [...r.times].sort((a, b) => a - b);
      result.runs.push({ threads, isolated: r.isolated, effectiveThreads: r.threads, tokenizerLoadMs: Math.round(r.tokenizerMs), loadMs: Math.round(r.loadMs), tokMsMean: +(r.tokMs.reduce((a, b) => a + b, 0) / r.tokMs.length).toFixed(2),
        idMismatch, maxLogitDiffVsOrtInt8: +maxQ.toFixed(4), maxLogitDiffVsOrtFp32: +maxF.toFixed(4), argmaxAgreeVsOrtInt8: `${agreeQ}/${ref.texts.length}`,
        msPerColumnMean: +(r.times.reduce((a, b) => a + b, 0) / r.times.length).toFixed(1), msPerColumnMedian: +ts[Math.floor(ts.length / 2)].toFixed(1), msPerColumnP90: +ts[Math.floor(ts.length * 0.9)].toFixed(1), wallSeconds: (Date.now() - t0) / 1000 });
      await ctx.close();
    }
  }
} catch (e) {
  result.fatal = String(e).slice(0, 600);
} finally {
  await browser.close(); server.close();
}
const sizes = [...served.entries()].map(([k, v]) => [k, v.size, v.file]).sort((a, b) => b[1] - a[1]);
result.served = Object.fromEntries(sizes.map(([k, n]) => [k, n]));
result.servedTotalMB = +(sizes.reduce((a, [, n]) => a + n, 0) / 1e6).toFixed(1);
// 配信のときに brotli で圧縮して送った場合の目安（品質 6。サーバーの設定しだいで、実際の転送量は変わる）
try {
  const zlib = await import('node:zlib');
  let br = 0;
  for (const [, n, f] of sizes) br += n < 50000 ? n : zlib.brotliCompressSync(fs.readFileSync(f), { params: { [zlib.constants.BROTLI_PARAM_QUALITY]: 6 } }).length;
  result.servedBrotliMB = +(br / 1e6).toFixed(1);
} catch (e) { result.servedBrotliMB = null; }
result.wasmFiles = Object.fromEntries(LIB_DIRS.flatMap((d) => (fs.existsSync(d) ? fs.readdirSync(d).filter((f) => f.endsWith('.wasm')).map((f) => [f, +(fs.statSync(path.join(d, f)).size / 1e6).toFixed(1)]) : [])));
result.dist = LIB_DIRS.map((d) => (fs.existsSync(d) ? fs.readdirSync(d).filter((f) => /\.(m?js|wasm|cjs)$/.test(f)) : null));
fs.writeFileSync(outPath, JSON.stringify(result, null, 1));
console.log(JSON.stringify(result));   // 全部（1 行）
const cut = (x, n = 170) => String(x).replace(/\s+/g, ' ').slice(0, n);
console.log('=== 要点（この下が注に出る）===');
console.log('取り込んだファイル（MB）: 合計 ' + result.servedTotalMB + '　' + cut(Object.entries(result.served).map(([k, v]) => k + ' ' + (v / 1e6).toFixed(1)).join(' / '), 150));
console.log('importMap: ' + cut(JSON.stringify(IMPORT_MAP), 190));
for (const t of result.tried) console.log('立ち上げ試し: ' + cut(JSON.stringify(t), 190));
console.log('使えた build: ' + (result.build || 'なし') + '　外への通信を止めた件数: ' + result.blocked.length);
for (const r of result.runs) console.log('結果: ' + (r.error ? `threads=${r.threads} error ${cut(r.error, 150)}` : `threads=${r.threads}(実際${r.effectiveThreads}・隔離${r.isolated}) 読込${r.loadMs}ms トークン化${r.tokMsMean}ms 番号の不一致${r.idMismatch}/${result.n} 差(INT8/fp32)${r.maxLogitDiffVsOrtInt8}/${r.maxLogitDiffVsOrtFp32} 答え一致${r.argmaxAgreeVsOrtInt8} 1列 平均${r.msPerColumnMean}・中央${r.msPerColumnMedian}・p90 ${r.msPerColumnP90}ms`));
if (result.tokParity) {
  const tp = result.tokParity;
  console.log(`トークナイザの番号の一致（全部の試験文＋変わった文字列）: ${tp.total}文中 不一致${tp.mismatches}（うち変わった文字列 ${tp.mismatchesEdge}／${tp.edge}）・${tp.ms}ms`);
  for (const m of tp.first.slice(0, 6)) console.log('  不一致: ' + cut(JSON.stringify({ i: m.i, edge: m.edge, at: m.firstDiff, n: [m.lenGot, m.lenWant], got: m.got, want: m.want, t: m.text, cp: m.edge ? undefined : m.codepoints }), 195));
}
console.log('配信の目安（brotli）: ' + result.servedBrotliMB + 'MB／wasm の大きさ(MB): ' + cut(JSON.stringify(result.wasmFiles), 150));
for (const m of (result.mismatches || []).slice(0, 3)) console.log('番号の不一致: ' + cut(JSON.stringify({ i: m.i, at: m.firstDiff, n: [m.lenGot, m.lenWant], got: m.got, want: m.want, cp: m.codepoints }), 195));
for (const c of result.console.slice(0, 8)) console.log('console: ' + cut(c, 190));
if (result.fatal) console.log('fatal: ' + cut(result.fatal, 190));
