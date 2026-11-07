"""W2 snapshot 113dcab の検証136列だけを診断する。教材・規則・依頼は変更しない。"""
from pathlib import Path
import collections,difflib,hashlib,json,re,subprocess,sys,unicodedata
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from encoder_context import apply_label_fix,unit_context_map,TITLE_SEP
from pool_families import split_val_by_family,cap_tables_per_family
from guard import guard_with_reason,date_shares,num_loose_share
BASE='113dcab'
OUT=ROOT/'research/w2_unknown'

def git_bytes(path):return subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT)
def norm(h):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',str(h))).strip().casefold()
def pattern(v):
    s=unicodedata.normalize('NFKC',str(v)).strip()
    if s.casefold() in ('','-','na','nan','n/a','n/a / n/d','x','?','[x]','[z]'):return 'missing'
    if re.fullmatch(r'[+-]?\d+',s):return 'integer_digits_'+str(min(len(s.lstrip('+-')),6))
    if re.fullmatch(r'[+-]?[\d,]+\.\d+|[+-]?\d{1,3}(,\d{3})+',s):return 'decimal_or_grouped_number'
    return re.sub('[一-龥ぁ-ヿ]+','J',re.sub('[A-Za-zÀ-ÿ]+','A',re.sub(r'\d+','9',s)))[:70]
def signature(vals):return tuple(sorted({pattern(v) for v in vals}))
def coarse(vals):
    tags=set()
    for v in vals:
        p=pattern(v)
        tags.add('missing' if p=='missing' else 'numeric' if p.startswith('integer_') or p=='decimal_or_grouped_number' else 'non_numeric')
    return tuple(sorted(tags))
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def main():
    for source in ('guard.py','train3.py','encoder_context.py','pool_families.py'):
        assert (ROOT/source).read_bytes()==git_bytes(source),f'W2から変更されたコード: {source}'
    paths=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'materials/pool'],cwd=ROOT,text=True).splitlines()
    files=[p for p in paths if re.fullmatch(r'materials/pool/batch_[^/]+\.jsonl',p)]
    assert not any('b018' in p for p in files),'禁止の陣は開かない'
    docs=[];origin={};fingerprints={}
    for p in files:
        raw=git_bytes(p);assert (ROOT/p).read_bytes()==raw,f'snapshotから変更: {p}'
        fingerprints[p]=hashlib.sha256(raw).hexdigest()
        for line in raw.decode('utf-8').splitlines():
            d=json.loads(line);docs.append(d);origin[d['table'],d['header'].lstrip('\ufeff')]=p
    fix='materials/pool/labelfix_v24.jsonl'
    assert (ROOT/fix).read_bytes()==git_bytes(fix)
    junk={'nan','None','','NaN','null','NULL'}
    rows=[(d['header'].lstrip('\ufeff'),[v for v in d['values'] if v.strip() not in junk],d['label'],d['context'],d['table']) for d in docs]
    rows,nfix=apply_label_fix(rows,[str(ROOT/fix)])
    tr,val=split_val_by_family(rows,salt='jitsuris-poolval-v2',mod=8);tr,ncap=cap_tables_per_family(tr,4)
    assert (len(rows),len(tr),len(val),nfix,ncap)==(38654,29696,4551,153,576)
    titles=json.loads(git_bytes('materials/pool/titles.json'));units=unit_context_map(rows)
    errors=json.loads((OUT/'both_seeds_errors.json').read_text())['rows']
    probs=[json.loads((ROOT/f'eval_reports/latest/job{j}_probs_val_pool_ft.json').read_text())['rows'] for j in (1,2)]
    notes=json.loads((OUT/'codex_review_notes.json').read_text())
    assert len(errors)==136 and len({r['index'] for r in errors})==136
    assert set(notes)=={str(e['index']) for e in errors}
    class_count=collections.Counter(r[2] for r in tr)
    pool_shape=collections.Counter((r[2],signature(r[1])) for r in rows)
    train_shape=collections.Counter((r[2],signature(r[1])) for r in tr)
    train_coarse=collections.Counter((r[2],coarse(r[1])) for r in tr)
    same_header=collections.Counter(norm(r[0]) for r in tr)
    by_label=collections.defaultdict(list)
    for r in tr:by_label[r[2]].append(r)
    records=[];replayed=0
    for e in errors:
        idx=e['index'];h,v,truth,ctx,table=val[idx]
        assert (norm(h),truth,table)==(norm(e['column']),e['truth'],e['table'])
        primary,reason,guide=notes[str(idx)]
        guards=[]
        for seed,ps in enumerate(probs,1):
            p=ps[idx];assert (norm(p['column']),p['truth'])==(norm(h),truth)
            assert (p['guarded_prediction'],p['outcome'])==(e[f'pred_seed{seed}'],e[f'outcome_seed{seed}'])
            order=[(x['label'],x['probability']) for x in p['top3']]
            actual=('unknown','probability_below_threshold') if order[0][1]<0.5 else guard_with_reason(order[0][0],order,v)
            assert actual==(p['guarded_prediction'],p['decision_reason']),(idx,seed,actual)
            replayed+=1
            guards.append({'seed':seed,'raw':p['raw_prediction'],'final':p['guarded_prediction'],'decision_reason':p['decision_reason'],
                'raw_correct':p['raw_prediction']==truth,'correct_raw_rejected':p['raw_prediction']==truth and p['guarded_prediction']!=truth,
                'top3':p['top3'],'date_value_shares':list(date_shares(v)) if p['raw_prediction']=='date' else None,
                'parseable_numeric_share':num_loose_share(v) if p['raw_prediction'] in ('amount','quantity','rate') else None})
        sig=signature(v);shaped=[r for r in by_label[truth] if signature(r[1])==sig]
        candidates=shaped if shaped else by_label[truth]
        # 近い見出しの候補は探索の案内。意味の同一性や因果は保証しない。
        scores=sorted(((difflib.SequenceMatcher(None,norm(h),norm(r[0])).ratio(),r) for r in candidates),key=lambda z:(-z[0],z[1][4],z[1][0]))
        nearest=[];seen=set()
        for score,r in scores:
            key=(r[4],r[0])
            if key in seen:continue
            seen.add(key);nearest.append({'header':r[0],'table':r[4],'label':r[2],'header_similarity':round(score,4),'same_value_signature':signature(r[1])==sig})
            if len(nearest)==3:break
        missing=[]
        if not v:missing.append('values')
        if not ctx:missing.append('sibling_headers')
        if not units.get(table):missing.append('explicit_unit_column_values')
        if not titles.get(table):missing.append('table_title')
        secondary=[]
        if primary!='4' and any(g['correct_raw_rejected'] for g in guards):secondary.append('4')
        if train_shape[truth,sig]<5:secondary.append('3_hypothesis_only')
        records.append({'index':idx,'column':e['column'],'original_header':h,'truth_unchanged':truth,'table':table,
            'title':titles.get(table,''),'batch_source':origin[table,h],
            'primary_category':primary,'secondary_categories':secondary,
            'certainty': 'confirmed_decision_stage' if primary=='4' else 'label_boundary_review_required' if primary=='1' else 'input_gap_causal_hypothesis' if primary=='2' else 'model_semantic_failure_root_unresolved',
            'finding':reason,'label_guide_reference':guide,
            'input_evidence':{'value_count':len(v),'value_pattern_signature':list(sig),'sibling_headers_available':ctx,
                'sibling_headers_encoded_before_token_limit':[str(c)[:20] for c in ctx[:12]], 'sibling_headers_dropped_by_12_column_limit':ctx[12:],
                'unit_values_available':bool(units.get(table)),'title_available':bool(titles.get(table)),
                'title_chars':len(str(titles.get(table,''))),'title_char_limit':40,'value_char_limit':30,
                'value_examples_cut_by_char_limit':sum(len(str(z))>30 for z in v[:5]),'missing_components':missing,
                'actual_160_token_visibility':'未計測。文字の組立と文字数制限まで確認、トークナイザ切詰めは未確認'},
            'training_evidence':{'reference':'W2 113dcab、label-fix適用・family split・cap後、augmentation前のpool学習側のみ',
                'class_rows':class_count[truth],'same_class_and_exact_pattern_rows':train_shape[truth,sig],
                'same_class_and_coarse_pattern_rows':train_coarse[truth,coarse(v)],
                'same_class_and_exact_pattern_tables':len({r[4] for r in shaped}),
                'full_pool_same_class_and_exact_pattern_rows':pool_shape[truth,sig],
                'normalized_exact_header_rows':same_header[norm(h)],'nearest_training_candidates':nearest,
                'scarcity_causal_claim':False},'decision_evidence':guards})
    assert replayed==272
    counts=collections.Counter(r['primary_category'] for r in records)
    rejected=[sum(r['decision_evidence'][s]['correct_raw_rejected'] for r in records) for s in (0,1)]
    info={'source_commit':BASE,'scope':'検証(val_pool)の指定136列だけ。禁止セット/固定試験は未閲覧。値を出力に保存しない。',
        'pool_rows':len(rows),'pool_training_rows':len(tr),'pool_validation_rows':len(val),'applied_label_fixes':nfix,'capped_tables':ncap,
        'matched_rows':136,'guard_replays_matched':replayed,'primary_counts':dict(counts),'correct_raw_rejected_seed1_seed2':rejected,
        'methods':{'value_signature':'NFKC後、整数桁数(6以上は6)、小数/桁区切り、文字列は数字/ラテン文字/和文の連続を9/A/Jへ置換し70字まで。5標本のパターン集合が完全一致。',
                   'coarse_signature':'標本がnumeric/non_numeric/missingのどれを含むかの集合一致。',
                   'limitations':'同じ文字形は同じ意味を保証しない。0件を教材不足の原因と断定しない。合成・他の実データ・augmentation後の露出量は未集計。ラベル提案は未適用。'},
        'rows':records}
    dump(OUT/'codex_causes.json',info)
    manifest={'base_commit':subprocess.check_output(['git','rev-parse',BASE],cwd=ROOT,text=True).strip(),'pool_files_sha256':fingerprints,
        'label_fix_sha256':hashlib.sha256(git_bytes(fix)).hexdigest(),'titles_sha256':hashlib.sha256(git_bytes('materials/pool/titles.json')).hexdigest()}
    dump(OUT/'codex_evidence_manifest.json',manifest)
    names={'1':'正解ラベル・決まりの境界を再確認','2':'入力の意味/単位不足が疑われる','3':'教材不足を主因として確認','4':'正しい元予測をguardが拒否','5':'モデルの意味の取り違え等（深い原因未確定）'}
    md=['# W2 未知見出し136列：Codex原因調査','',f'- W2コミット `{manifest["base_commit"]}` の教材38654列を再構成。label-fix153、学習29696、検証4551、family cap576表。依頼136/136列の正規化見出し・ラベル・表を照合。',
        '- 保存top3と当時の値からguardの272/272判定を再現。推論・学習・モデル取得はしていない。ラベル・教材・規則・依頼ファイルは変更なし。','',
        '| 主分類 | 列数 | 確認できたことと限界 |','|---|---:|---|']
    desc={'1':'ガイドの具体項と各列の根拠をJSONに記録。誤ラベル確定ではなくClaudeとの照合待ち。','2':'通貨/FTE/略語の展開や全0の符号定義等が入力にない。原因としての十分性は仮説。','3':'0。形が似た教材の件数は全136列で付記したが、因果を証明する追加学習をしないため主因とは断定しない。','4':'date28列は両種子ともraw=date→date_value_evidence_low。ほか欠け記号・単位付き数量。','5':'手掛かりが存在しても意味の境目を誤る等。encoderの重み/損失/教材分布のどれが深因かは未確定。'}
    md += [f'| {k} {names[k]} | {counts[k]} | {desc[k]} |' for k in ('1','2','3','4','5')]
    md += ['', '## 確定できた段', '',
        '- date→unknown 28列は「dateを学べていない」ではない。両種子とも元予測dateが、値の形だけのguard v10で不明へ変わる。月/日/四半期の単独番号、HHMM、Excel日付番号、英月・和暦・18世紀・期間・小数年等。`guard.py:446`、`train3.py:155`。H1/F3/G4はheaderを渡す経路だがW2既定v10ではheader=None。規則を変更せず観測だけ記録。',
        f'- 保存された正解ラベルに対して、正しい元予測から不明になった出力は種子1で{rejected[0]}、種子2で{rejected[1]}。ここには閾値未満も含むので、全部を値パーサの不具合と呼ばない。rawがother等ですでに違う列のother_classは主原因をguardにしない。',
        '- numeric_values_not_parseableでは欠け記号が多い標本や、Cylinders/時間・分付きの量を確認。`guard.py:463`の数値率0.5の検査。判定を緩めた場合の誤採用は測っていない。',
        '', '## ラベルと入力の留保','',
        '- index2709は公園/住宅等が混在する公共施設一覧で、B10.3のaddressと正解orgの不整合候補。3152の植物科の学名もother規定との照合が必要。道路TYPE/SUFFIX、会計事項、全0のWeb統計、domain/platform、利用時間17列は境界として区別。正解ファイルは書き換えない。',
        '- 入力は値5例×30字、題名40字、兄弟12列×20字、単位例の欄。長い説明/形式リスト/多言語題名では文字制限を確認したが、160 token切詰め後のどの語が失われたかは未計測。値が存在することと、必要な意味・単位が入力されることは別。',
        '- ③の件数は全136列にclass/同形/coarse形/表数/近い見出し候補を保存。full poolにある例でもvalidationやcapで学習から外れるため、学習側の件数を主に使う。似た文字形0件は同義の教材0件と同じではなく、件数だけで不足を原因確定しない。',
        '', '## W2結果の解釈と次の照合','',
        '- 「追加で上がった分は覚えた見出しだけ」との因果的断定には留保が必要。各割合の未知見出し集合は1389/1265/1121列と異なり、85.6/86.3/84.5は同じ列集合の比較ではない。事前の全検証Δ+0.81による頭打ち判定は変更しない。共通の未知見出し集合での対応比較は今回未実施。',
        '- Claudeの独立30列をindexで突き合わせる。まず28列の日付guard経路とラベル境界を照合し、残る意味誤りは候補教材の意味・入力定義まで確認してから一要因の検証を計画する。追加の数集め・学習・規則変更は行っていない。',
        '', '## 再現','', '`python research/w2_unknown/codex_causes.py`。136行対応、snapshot一致、272 guard replay、主分類件数、件数/列数をassertする。値は出力へ保存しない。明細は `codex_causes.json`、手判断は `codex_review_notes.json`、入力SHAは `codex_evidence_manifest.json`。','']
    (OUT/'codex_summary.md').write_text('\n'.join(md),encoding='utf-8')
    print(json.dumps({'matched':136,'replayed':replayed,'counts':dict(counts),'correct_raw_rejected':rejected},ensure_ascii=False))
if __name__=='__main__':main()
