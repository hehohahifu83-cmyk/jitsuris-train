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
const WEB_BUILDS = ['transformers.web.min.js', 'transformers.web.js', 'transformers.min.js', 'transformers.js'];
const webBuild = WEB_BUILDS.find((f) => fs.existsSync(path.join(LIB_DIRS[0], f)));
if (!webBuild) throw new Error('Transformers.js のブラウザ用の build が見つからない: ' + fs.readdirSync(LIB_DIRS[0]).join(','));

const PAGE = `<!doctype html><meta charset="utf-8"><title>browser model test</title>
<script type="module">
import { env, AutoTokenizer, AutoModelForSequenceClassification } from '/lib/${webBuild}';
env.allowRemoteModels = false; env.allowLocalModels = true; env.localModelPath = '/model_root/'; env.useBrowserCache = false;
env.backends.onnx.wasm.wasmPaths = '/lib/';
window.__run = async ({ texts, threads, warmup }) => {
  env.backends.onnx.wasm.numThreads = threads;
  const t0 = performance.now();
  const tokenizer = await AutoTokenizer.from_pretrained('model');
  const tTok = performance.now() - t0;
  const model = await AutoModelForSequenceClassification.from_pretrained('model', { dtype: 'q8', device: 'wasm' });
  const loadMs = performance.now() - t0;
  const ids = [], logits = [], times = [];
  for (const t of texts) {
    const enc = tokenizer(t, { truncation: true, max_length: 128 });
    ids.push(Array.from(enc.input_ids.data, Number));
  }
  for (let i = 0; i < texts.length; i++) {
    const enc = tokenizer(texts[i], { truncation: true, max_length: 128 });
    const s = performance.now();
    const out = await model(enc);
    times.push(performance.now() - s);
    logits.push(Array.from(out.logits.data));
  }
  return { tokenizerMs: tTok, loadMs, ids, logits, times: times.slice(warmup), isolated: self.crossOriginIsolated === true, threads: env.backends.onnx.wasm.numThreads };
};
window.__ready = true;
</script>`;

function send(res, file) {
  if (!file || !fs.existsSync(file) || !fs.statSync(file).isFile()) { res.writeHead(404); res.end('not found'); return; }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream', ...HEADERS });
  fs.createReadStream(file).pipe(res);
}

const server = http.createServer((req, res) => {
  const url = decodeURIComponent(req.url.split('?')[0]);
  if (url === '/') { res.writeHead(200, { 'Content-Type': 'text/html', ...HEADERS }); res.end(PAGE); return; }
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
const result = { build: webBuild, n: ref.texts.length, runs: [], blocked: [], console: [] };
const browser = await chromium.launch({ headless: true });
try {
  for (const threads of [1, 2]) {
    const ctx = await browser.newContext({ serviceWorkers: 'block' });
    const page = await ctx.newPage();
    page.on('console', (m) => { if (result.console.length < 40) result.console.push(`[${threads}] ${m.type()}: ${m.text().slice(0, 300)}`); });
    page.on('pageerror', (e) => result.console.push(`[${threads}] pageerror: ${String(e).slice(0, 300)}`));
    await page.route('**/*', (route) => {
      const u = route.request().url();
      if (u.startsWith(base + '/') || u.startsWith('data:') || u.startsWith('blob:')) return route.continue();
      result.blocked.push(u.slice(0, 200)); return route.abort();
    });
    await page.goto(base + '/');
    await page.waitForFunction(() => window.__ready === true, null, { timeout: 60000 });
    const t0 = Date.now();
    let r;
    try {
      r = await page.evaluate((o) => window.__run(o), { texts: ref.texts, threads, warmup: 3 });
    } catch (e) {
      result.runs.push({ threads, error: String(e).slice(0, 500) }); await ctx.close(); continue;
    }
    let idMismatch = 0, firstBad = null;
    r.ids.forEach((ids, i) => { if (JSON.stringify(ids) !== JSON.stringify(ref.ids[i])) { idMismatch++; if (firstBad === null) firstBad = { i, got: ids.slice(0, 40), want: ref.ids[i].slice(0, 40) }; } });
    let maxQ = 0, maxF = 0, agreeQ = 0;
    r.logits.forEach((lg, i) => { lg.forEach((v, k) => { maxQ = Math.max(maxQ, Math.abs(v - ref.logits_q[i][k])); maxF = Math.max(maxF, Math.abs(v - ref.logits_f[i][k])); }); if (argmax(lg) === argmax(ref.logits_q[i])) agreeQ++; });
    const ts = [...r.times].sort((a, b) => a - b);
    result.runs.push({ threads, isolated: r.isolated, effectiveThreads: r.threads, tokenizerMs: Math.round(r.tokenizerMs), loadMs: Math.round(r.loadMs),
      idMismatch, firstBad, maxLogitDiffVsOrtInt8: +maxQ.toFixed(4), maxLogitDiffVsOrtFp32: +maxF.toFixed(4), argmaxAgreeVsOrtInt8: `${agreeQ}/${ref.texts.length}`,
      msPerColumnMean: +(r.times.reduce((a, b) => a + b, 0) / r.times.length).toFixed(1), msPerColumnMedian: +ts[Math.floor(ts.length / 2)].toFixed(1), msPerColumnP90: +ts[Math.floor(ts.length * 0.9)].toFixed(1), wallSeconds: (Date.now() - t0) / 1000 });
    await ctx.close();
  }
} finally {
  await browser.close(); server.close();
}
fs.writeFileSync(outPath, JSON.stringify(result, null, 1));
console.log(JSON.stringify(result, null, 1));
