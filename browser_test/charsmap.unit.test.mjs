// charsmap.mjs の動きを、小さな自作の表（ダブル配列）で確かめる単体試験。本物の表がなくても手元の Node で動く。
// 本物の表と Python（Rust 実装）との突き合わせは charsmap.test.mjs（正解データは tokenizer_fixtures.py が作る）。
// 使い方：node --test browser_test/charsmap.unit.test.mjs
import test from 'node:test';
import assert from 'node:assert/strict';
import { makeNormalizer, parseCharsmap } from './charsmap.mjs';

const ENC = new TextEncoder();

/** 規則（左辺の文字列 → 置き換え）から、sentencepiece と同じ形式（darts-clone のダブル配列）の表のバイト列を作る */
function buildCharsmap(rules) {
  const blob = [];
  const offsetOf = new Map();
  const valueFor = (rep) => {
    if (!offsetOf.has(rep)) { offsetOf.set(rep, blob.length); blob.push(...ENC.encode(rep), 0); }
    return offsetOf.get(rep);
  };
  const root = { children: new Map(), value: undefined };
  for (const [key, rep] of Object.entries(rules)) {
    let node = root;
    for (const b of ENC.encode(key)) {
      if (!node.children.has(b)) node.children.set(b, { children: new Map(), value: undefined });
      node = node.children.get(b);
    }
    node.value = valueFor(rep);
  }
  const units = new Map();
  const used = new Set([0]);
  const place = (node, idx, label) => {
    const labels = [...node.children.keys()];
    const hasLeaf = node.value !== undefined;
    let base = 1;
    for (; ; base++) {
      const pos = labels.map((l) => base ^ l);
      if (hasLeaf) pos.push(base);
      if (pos.every((p) => !used.has(p))) break;
    }
    for (const l of labels) used.add(base ^ l);
    if (hasLeaf) { used.add(base); units.set(base, (node.value | 0x80000000) >>> 0); }
    units.set(idx, ((label & 0xff) | (hasLeaf ? 0x100 : 0) | ((idx ^ base) << 10)) >>> 0);
    for (const l of labels) place(node.children.get(l), base ^ l, l);
  };
  place(root, 0, 0);
  const n = Math.max(...units.keys()) + 1;
  const words = new Uint32Array(n);
  for (const [i, u] of units) words[i] = u;
  const out = new Uint8Array(4 + 4 * n + blob.length);
  const dv = new DataView(out.buffer);
  dv.setUint32(0, 4 * n, true);
  words.forEach((w, i) => dv.setUint32(4 + 4 * i, w, true));
  out.set(blob, 4 + 4 * n);
  return out;
}

const norm = (rules, opts) => makeNormalizer(buildCharsmap(rules), opts);

test('1 文字ずつの規則：半角カナと半角の濁点は合成されず 2 片のまま（NFKC なら「ゾ」になる）', () => {
  const n = norm({ 'ｿ': 'ソ', 'ﾞ': '゙', 'ﾊ': 'ハ', 'ﾟ': '゚' });
  assert.equal(n('ｿﾞ'), 'ゾ');
  assert.equal(n('ﾊﾟ'), 'パ');
  assert.notEqual(n('ｿﾞ'), 'ｿﾞ'.normalize('NFKC'));
  assert.equal(n('ｿﾞ'), 'ゾ');
  assert.equal(n('abc 漢字'), 'abc 漢字');   // 規則にない文字はそのまま
});

test('消す規則（置き換えが空文字列）は文字を消す。規則がないのとは区別する', () => {
  const n = norm({ '​': '', '\t': ' ' });
  assert.equal(n('a​b\tc'), 'ab c');
});

test('6 バイト未満の書記素は丸ごと 1 回引く：最初に見つかった規則（いちばん短い一致）で書記素ぜんぶが置き換わる', () => {
  // "e" の規則だけがあるとき、"e"＋結合アクセント（3 バイトの 1 書記素）は "E" になり、アクセントは落ちる（Rust と同じ癖）
  assert.equal(norm({ e: 'E' })('é'), 'E');
  // "e" と "é"（e＋アクセント）の両方の規則があっても、先に見つかる短い方（"e"）を使う
  assert.equal(norm({ e: 'E', 'é': 'X' })('é'), 'E');
  // 長い方だけがあれば、それを使う
  assert.equal(norm({ 'é': 'X' })('é'), 'X');
});

test('6 バイト以上の書記素は 1 文字ずつ引く', () => {
  // "ｿﾞ" は 3＋3＝6 バイトの 1 書記素。丸ごとの規則は使わず、1 文字ずつ
  const n = norm({ 'ｿﾞ': 'ZZ', 'ｿ': 'ソ', 'ﾞ': '゙' });
  assert.equal(n('ｿﾞ'), 'ゾ');
  // 5 バイト以下なら丸ごとの規則が使える（"e"＋アクセントは 3 バイト）
  assert.equal(norm({ 'é': 'X', e: 'E' })('é'), 'E');
});

test('別々の書記素にまたがる規則は使われない（"ab" の規則は "a" と "b" に分かれた後では引けない）', () => {
  const n = norm({ a: '1', ab: '2', b: '3' });
  assert.equal(n('ab'), '13');
});

test('CRLF は 1 つの書記素：先頭の \\r の規則で丸ごと置き換わり、\\n は落ちる（Rust と同じ癖）', () => {
  assert.equal(norm({ '\r': ' ' })('a\r\nb'), 'a b');
  assert.equal(norm({ '\r': ' ', '\n': ' ' })('a\r\nb'), 'a b');
  // "\r" の規則がなければ、丸ごとの規則は見つからず（先頭の \r が一致しない）、1 文字ずつ引く：\r は残り、\n だけが空白になる
  assert.equal(norm({ '\n': ' ' })('a\r\nb'), 'a\r b');
});

test('NUL（U+0000）は規則を引く途中で打ち切り。そのまま残る', () => {
  assert.equal(norm({ a: 'A' })('a\u0000b'), 'A\u0000b');
});

test('壊れたサロゲートは U+FFFD にしてから引く', () => {
  const n = norm({ '�': '?' });
  assert.equal(n('a\ud800b'), 'a?b');
});

test('Intl.Segmenter がない環境の近似の分け方でも、1 文字ずつの規則なら同じ答え', () => {
  const rules = { 'ｿ': 'ソ', 'ﾞ': '゙', 'ｶ': 'カ' };
  const exact = norm(rules)('ｶﾞｷﾞ ｿﾞ');
  const approx = norm(rules, { segmenter: null })('ｶﾞｷﾞ ｿﾞ');
  assert.equal(approx, exact);
});

test('表が壊れていれば止まる', () => {
  assert.throws(() => parseCharsmap(new Uint8Array([1, 2])), /短すぎる/);
  assert.throws(() => parseCharsmap(new Uint8Array([255, 0, 0, 0, 1, 2, 3, 4])), /大きさ/);
});
