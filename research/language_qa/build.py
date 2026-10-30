"""質疑応答の試験を作る（2026-10-30 Claude。計画：research/language-qa-plan-2026-10-30.md）。
確かめる陣（conf1030 の 15 陣）の表を、今の製品の形（C2 種子 1＋見張り＋recheck（F4・F8）＋検査役＋rho＋通貨の手がかり）で判定し、
その答えを「判定の表」として固定する。質疑応答の部分は、この判定の表・LABEL_GUIDE の種類の表・facts.md だけを根拠に答える。
  python research/language_qa/build.py   → contexts.jsonl（判定の表）・questions.jsonl（質問と要点）・sheet_chatgpt.md（ChatGPT に渡す分。要点は入れない）
正解のラベルは判定の表に入れない（試験は「判定を言葉で説明できるか」で、判定が正しいかではない）。
"""
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "research", "fixes"))
import eval_fixes as EF  # noqa: E402

FIXES = ("F4", "F8")   # 製品の決め方に入れた直し（2026-10-30）
N_TABLES = 40
JA = {"date": "日付", "amount": "金額", "quantity": "数量", "rate": "率", "id": "番号・コード", "org": "会社・団体", "person": "人の名前",
      "product": "商品", "account": "勘定科目・部門", "tax_class": "税区分", "text": "文章", "category": "区分", "email": "メール",
      "phone": "電話", "address": "住所", "other": "その他", "unknown": "不明"}


def h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def judge():
    """確かめる陣の全列を製品の形で判定する。id → (答え, 列名, 理由, 値5個, 単位)。"""
    A, V, E = EF.A, EF.V, EF.E
    labels = list(V.LABELS)
    train = [c for b in A.TRAIN for c in E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    per = {}
    EF.run(EF.load(EF.CONFIRM), mv, labels, FIXES, per)
    return per
