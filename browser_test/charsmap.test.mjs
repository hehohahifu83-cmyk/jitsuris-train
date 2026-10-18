// JS の正規化（charsmap.mjs）が、Hugging Face tokenizers（Rust）の正規化と同じ答えを出すか調べる。
// 使い方：node browser_test/charsmap.test.mjs [正解データの場所。省略なら browser_test/fixtures]
// 正解データは tokenizer_fixtures.py が作る（GitHub Actions の「トークナイザの正規化の一致試験」）：
//   charsmap.b64      … tokenizer.json の Precompiled の表（base64）
//   norm_single.json  … 1 文字だけの文字列（全 Unicode スカラー値）の正規化のうち、元と変わるものだけ（残りは元のまま）
//   norm_cases.json   … [元, 正規化後] の組（基底の文字＋結合文字・ランダムな文・試験の文・変わった文字列など）
// 1 件でも違えば終了コード 1。最初の数件は、元・JS の答え・正解をコードポイントで出す。
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { makeNormalizer, base64ToBytes, parseCharsmap } from './charsmap.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const dir = process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : path.join(here, 'fixtures');
const read = (name) => fs.readFileSync(path.join(dir, name), 'utf-8');

const cps = (s) => Array.from(s, (c) => 'U+' + c.codePointAt(0).toString(16).toUpperCase().padStart(4, '0')).join(' ');
const shown = (s) => (s.length <= 40 ? JSON.stringify(s) : JSON.stringify(s.slice(0, 40)) + '…');

const charsmap = parseCharsmap(base64ToBytes(read('charsmap.b64').trim()));
const normalize = makeNormalizer(charsmap);
const normalizeApprox = makeNormalizer(charsmap, { segmenter: null });   // Intl.Segmenter がない環境の代用（参考）

let total = 0, bad = 0;
const lines = [];
const detail = [];
const report = (group, raw, got, want) => {
  if (detail.length < 25) detail.push(`  不一致[${group}] 元 ${shown(raw)} (${cps(raw).slice(0, 120)})\n    JS   ${shown(got)} (${cps(got).slice(0, 160)})\n    正解 ${shown(want)} (${cps(want).slice(0, 160)})`);
};

// 1. 1 文字だけの文字列：全スカラー値
{
  const single = JSON.parse(read('norm_single.json'));
  const diff = new Map(Object.entries(single.diff).map(([k, v]) => [Number(k), v]));
  let n = 0, b = 0;
  for (let cp = 0; cp <= 0x10ffff; cp++) {
    if (cp >= 0xd800 && cp <= 0xdfff) continue;
    const raw = String.fromCodePoint(cp);
    const want = diff.has(cp) ? diff.get(cp) : raw;
    const got = normalize(raw);
    n++;
    if (got !== want) { b++; report('1文字', raw, got, want); }
  }
  total += n; bad += b;
  lines.push(`1 文字（全スカラー値）: ${n} 件中 不一致 ${b}（表で変わる文字 ${diff.size} 個）`);
}

// 2. 組み合わせ・ランダム文・試験の文・変わった文字列
{
  const cases = JSON.parse(read('norm_cases.json'));
  for (const [group, list] of Object.entries(cases.groups)) {
    let n = 0, b = 0, bApprox = 0;
    for (const [raw, want] of list) {
      const got = normalize(raw);
      n++;
      if (got !== want) { b++; report(group, raw, got, want); }
      if (normalizeApprox(raw) !== want) bApprox++;
    }
    total += n; bad += b;
    lines.push(`${group}: ${n} 件中 不一致 ${b}（参考：Intl.Segmenter なしの近似の分け方だと ${bApprox}）`);
  }
}

// 3. 見本（ログで目で見るため）
const demo = ['ｱｲｳｴｵ ﾊﾟﾋﾟﾌﾟ ｶﾞｷﾞ', 'ﾔﾏｸﾞﾁ ｹﾝ', 'が が', 'ＡＢＣ１２３ ㈱ ①', 'a  b\r\nc'];
const demoLines = demo.map((t) => `見本 ${shown(t)} → ${shown(normalize(t))} (${cps(normalize(t)).slice(0, 100)})`);

console.log(detail.join('\n'));
console.log('=== 要点（この下が注に出る）===');
console.log(`正規化の一致試験（Node ${process.version}・Intl.Segmenter ${typeof Intl !== 'undefined' && Intl.Segmenter ? 'あり' : 'なし'}）: 全 ${total} 件中 不一致 ${bad}`);
for (const l of lines) console.log(l);
for (const l of demoLines) console.log(l);
process.exit(bad === 0 ? 0 : 1);
