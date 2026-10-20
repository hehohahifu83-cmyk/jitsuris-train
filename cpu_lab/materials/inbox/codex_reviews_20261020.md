# ChatGPT 単独監査: 請求件数と請求金額

- 候補: `codex-20261020-001`, `codex-20261020-002`
- LABEL_GUIDE: v1.5
- 監査者: ChatGPT（利用可能な監査者1人）
- 日付: 2026-10-20
- 出典: 内部生成の合成例。実試験行の値は転記していない。

| ID | 判定 | 確信度 | 根拠 | 採否 |
|---|---|---|---|---|
| codex-20261020-001 | quantity | high | Invoice Count、count単位、Fiscal Periodや支払期限別件数との兄弟列が一貫して件数を示す。値は正の整数。LABEL_GUIDE の quantity「個数・件数」と一致。 | 採用 |
| codex-20261020-002 | amount | high | Invoice Amount、GBP単位、通貨付き値。兄弟のInvoice Countや支払期限別件数と意味が分かれる。LABEL_GUIDE の amount「お金」と一致。 | 採用 |

この対照は実際の「Total Invoices Paid」誤りから一般的な件数/金額の区別を教材にするための新規合成例。元試験行を学習へ逆流させていない。モデルの予測はラベル判断の根拠に使っていない。二者監査ではなく、単独監査として記録する。
