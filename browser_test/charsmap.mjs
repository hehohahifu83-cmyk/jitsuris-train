// sentencepiece の正規化表（precompiled_charsmap）を JavaScript で引く（ブラウザでも Node でも動く。外部ライブラリなし）。
//
// なぜ要るか：学習に使った Hugging Face tokenizers（Rust）は、sentencepiece の表を書記素ごとに引いて文を正規化する。
// Transformers.js はこの表を引かず、NFKC で近似している。NFKC は文字を合成するので、半角カナの濁点（ｿﾞ）が「ゾ」になり、
// 学習時の「ソ」＋「゙」（2 片）と別の片になる。業務データの半角カナ（銀行の振込データなど）で実際に起きる。
// そこで、書き出した tokenizer.json からは Precompiled を外し、表そのもの（charsmap.bin）をこの関数で引く。
//
// 動きは Rust 側（huggingface/spm_precompiled の lib.rs と、huggingface/tokenizers の normalizers/precompiled.rs）を読んで写した：
//   1. 文を書記素（拡張書記素クラスタ）に分ける。
//   2. 書記素の UTF-8 の長さが 6 バイト未満なら、その書記素を丸ごと 1 回表引きする。規則が見つかれば、書記素ぜんぶを置き換えにする。
//      表引きは「先頭から 1 バイトずつ進めて、最初に見つかった規則」を使う（いちばん短い一致。長い一致は使わない）。
//   3. 見つからないか 6 バイト以上なら、1 文字ずつ表引きする。見つからない文字はそのまま。
//   表の形式：[u32 表のバイト数][u32 の配列＝ダブル配列のトライ（darts-clone）][置き換えの文字列（NUL 終わりの UTF-8）]。
// 検査：tokenizer_fixtures.py が作る Python（Rust 実装）の正規化結果と、全文字・組み合わせ・ランダム文で突き合わせる（charsmap.test.mjs）。
// この関数の後に、tokenizer.json に残した Replace（空白の連続を 1 つに）が Transformers.js で適用される。

const DEC = new TextDecoder('utf-8');
const ENC = new TextEncoder();

/** 表のバイト列 → { trie: Uint32Array, strings: Uint8Array } */
export function parseCharsmap(bytes) {
  const u8 = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
  if (u8.byteLength < 4) throw new Error('charsmap が短すぎる');
  const dv = new DataView(u8.buffer, u8.byteOffset, u8.byteLength);
  const trieBytes = dv.getUint32(0, true);
  if (4 + trieBytes > u8.byteLength) throw new Error('charsmap の表の大きさがファイルより大きい');
  const n = trieBytes >>> 2;
  const trie = new Uint32Array(n);
  for (let i = 0; i < n; i++) trie[i] = dv.getUint32(4 + 4 * i, true);   // 小さい順（little-endian）に読む（実行する機械の並びに依らない）
  return { trie, strings: u8.subarray(4 + trieBytes) };
}

/** base64 の文字列 → バイト列（Node とブラウザの両方） */
export function base64ToBytes(b64) {
  if (typeof Buffer !== 'undefined') return new Uint8Array(Buffer.from(b64, 'base64'));
  const bin = atob(b64);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

// darts-clone のダブル配列の 1 つぶん（u32）の読み方
const hasLeaf = (u) => ((u >>> 8) & 1) === 1;
const labelOf = (u) => (u & 0x800000ff) >>> 0;
const offsetOf = (u) => (u >>> 10) << ((u & 0x200) >>> 6);

function utf8Length(s) {
  let n = 0;
  for (let i = 0; i < s.length; i++) {
    const c = s.charCodeAt(i);
    if (c < 0x80) n += 1;
    else if (c < 0x800) n += 2;
    else if (c >= 0xd800 && c <= 0xdbff) { n += 4; i++; }   // サロゲートペア＝1 文字 4 バイト
    else n += 3;
  }
  return n;
}

/** 書記素に分ける関数を作る。Intl.Segmenter（UAX #29。Rust の unicode-segmentation と同じ規則）がなければ近似（結合文字をくっつける）で代用する */
function makeGraphemes(segmenter) {
  if (segmenter) {
    return function* (s) { for (const x of segmenter.segment(s)) yield x.segment; };
  }
  const re = /\r\n|[\s\S][\p{M}ﾞﾟ‍︀-️]*/gu;
  return function* (s) { for (const m of s.matchAll(re)) yield m[0]; };
}

export function defaultSegmenter() {
  return typeof Intl !== 'undefined' && Intl.Segmenter ? new Intl.Segmenter('en', { granularity: 'grapheme' }) : null;
}

/**
 * 正規化の関数 normalize(text) を作る。
 * charsmap：表のバイト列（charsmap.bin の中身）か parseCharsmap の結果。
 * opts.segmenter：書記素の分け方（省略なら Intl.Segmenter。null を渡すと近似の分け方）。
 */
export function makeNormalizer(charsmap, opts = {}) {
  const isParsed = charsmap && charsmap.trie instanceof Uint32Array;
  const { trie, strings } = isParsed ? charsmap : parseCharsmap(charsmap);
  const graphemes = makeGraphemes('segmenter' in opts ? opts.segmenter : defaultSegmenter());
  const buf = new Uint8Array(16);   // 表引きするのは 6 バイト未満の書記素か 1 文字（最大 4 バイト）だけ
  const cache = new Map();          // 置き換えの文字列の位置 → 文字列
  const nTrie = trie.length;

  function replacementAt(index) {
    let s = cache.get(index);
    if (s === undefined) {
      let end = index;
      while (end < strings.length && strings[end] !== 0) end++;
      s = DEC.decode(strings.subarray(index, end));
      cache.set(index, s);
    }
    return s;
  }

  // 規則が見つかれば置き換えの文字列（空文字列のこともある＝その文字を消す）、なければ null
  function transform(str) {
    const written = ENC.encodeInto(str, buf).written;
    let pos = 0;
    pos ^= offsetOf(trie[0]);
    for (let i = 0; i < written; i++) {
      const c = buf[i];
      if (c === 0) break;                       // NUL で打ち切り（Rust と同じ）
      pos ^= c;
      if (pos >= nTrie) return null;
      const unit = trie[pos];
      if (labelOf(unit) !== c) return null;
      pos ^= offsetOf(unit);
      if (hasLeaf(unit)) {                      // ここまでが規則の左辺。最初に見つかった規則を使う
        if (pos >= nTrie) return null;
        return replacementAt(trie[pos] & 0x7fffffff);
      }
    }
    return null;
  }

  return function normalize(text) {
    let s = String(text);
    if (typeof s.isWellFormed === 'function' && !s.isWellFormed()) s = s.toWellFormed();   // 壊れたサロゲートは U+FFFD にする（Rust の文字列は壊れていない）
    let out = '';
    for (const g of graphemes(s)) {
      const oneCodePoint = g.length === 1 || (g.length === 2 && g.codePointAt(0) > 0xffff);
      if (oneCodePoint || utf8Length(g) < 6) {
        const r = transform(g);
        if (r !== null) { out += r; continue; }
        if (oneCodePoint) { out += g; continue; }
      }
      for (const ch of g) {
        const r = transform(ch);
        out += r === null ? ch : r;
      }
    }
    return out;
  };
}
