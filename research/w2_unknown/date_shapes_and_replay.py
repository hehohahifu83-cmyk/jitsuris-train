"""W2学習側の6形の集計とv10再現差の診断。guard/教材/ラベルは変更しない。"""
from pathlib import Path
import collections,hashlib,json,re,sys,unicodedata
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(Path(__file__).resolve().parent))
import codex_causes as C
import guard
from encoder_context import apply_label_fix,pick_values,MISSING
from pool_families import split_val_by_family,cap_tables_per_family
OUT=Path(__file__).resolve().parent

# 集計用の操作的定義であり、予測規則ではない。形同士は重なり得る。
DEFINITIONS={
 'hhmm4':'4桁の文字列、00<=HH<=23かつ00<=MM<=59。先頭0を保存。年やコードも該当し得る。',
 'day_number':'1〜2桁の整数文字列で1〜31。月/日以外の小さい件数やコードも該当。',
 'excel_serial':'5桁の整数文字列20000〜60000（末尾.0の型変換表記も含む）。日付かどうかの意味は使わない。',
 'mmyyyy6':'6桁MMYYYY、MM=01〜12、YYYY=1000〜2099。桁と月年範囲だけの判定。',
 'century18_year':'整数文字列1701〜1800（暦上の18世紀）。金額/数量も形が合えば含む。',
 'clock_dot00':'HH:MM:SS.00、HH=00〜23、MM/SS=00〜59。秒の後ろがちょうど.00。'
}

def normalize(v):return unicodedata.normalize('NFKC',str(v)).strip()
def missing(v):return normalize(v).casefold() in MISSING|{'?','n/a / n/d','n/a\xa0/ n/d','ー','－'}
def matches(key,v):
 s=normalize(v)
 if key=='hhmm4':return bool(re.fullmatch(r'(?:[01]\d|2[0-3])[0-5]\d',s))
 if key=='day_number':return bool(re.fullmatch(r'\d{1,2}',s)) and 1<=int(s)<=31
 if key=='excel_serial':return bool(re.fullmatch(r'\d{5}(?:\.0+)?',s)) and 20000<=float(s)<=60000
 if key=='mmyyyy6':return bool(re.fullmatch(r'(?:0[1-9]|1[0-2])(?:1\d{3}|20\d{2})',s))
 if key=='century18_year':return bool(re.fullmatch(r'\d{4}',s)) and 1701<=int(s)<=1800
 if key=='clock_dot00':return bool(re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\.00',s))
 raise ValueError(key)

def load_snapshot():
 import subprocess
 for fn in ('guard.py','train3.py','encoder_context.py','pool_families.py'):
  assert (ROOT/fn).read_bytes()==C.git_bytes(fn)
 paths=subprocess.check_output(['git','ls-tree','-r','--name-only',C.BASE,'materials/pool'],cwd=ROOT,text=True).splitlines()
 files=[p for p in paths if re.fullmatch(r'materials/pool/batch_[^/]+\.jsonl',p)]
 assert not any('b018' in p for p in files)
 docs=[]
 for fn in files:
  b=C.git_bytes(fn);assert (ROOT/fn).read_bytes()==b
  docs.extend(json.loads(l) for l in b.decode().splitlines())
 junk={'nan','None','','NaN','null','NULL'}
 rows=[(d['header'].lstrip('\ufeff'),[v for v in d['values'] if v.strip() not in junk],d['label'],d['context'],d['table']) for d in docs]
 fix='materials/pool/labelfix_v24.jsonl';assert (ROOT/fix).read_bytes()==C.git_bytes(fix)
 rows,nfix=apply_label_fix(rows,[str(ROOT/fix)])
 before,val=split_val_by_family(rows,salt='jitsuris-poolval-v2',mod=8)
 train,ncap=cap_tables_per_family(before,4)
 assert (len(rows),len(before),len(train),len(val),nfix,ncap)==(38654,34103,29696,4551,153,576)
 # tuple照合済みの値から、row_valuesを使う別経路だけを比較する。
 raw_by_key=collections.defaultdict(list)
 for d in docs:raw_by_key[d['table'],d['header'].lstrip('\ufeff')].append(d)
 return before,train,val,raw_by_key

def summarize(rows,key,threshold):
 chosen=[]
 for h,v,lab,ctx,t in rows:
  usable=[x for x in v if not missing(x)]
  hits=sum(matches(key,x) for x in usable)
  if usable and hits/len(usable)>=threshold:
   chosen.append({'header':h,'truth':lab,'table':t,'usable_values':len(usable),'matching_values':hits,
    'four_digit_year_collision_values':sum(bool(re.fullmatch(r'(?:19|20)\d{2}',normalize(z))) for z in usable) if key=='hhmm4' else None,
    'year_header_hint':bool(re.search(r'year|jahr|年度|年次|西暦|^年$|tlist\(a',C.norm(h))),
    'clock_header_hint':bool(re.search(r'time|hour|時|heure|uhr',C.norm(h))),
    'temporal_header_hint':bool(guard._H1_HEADER.search(C.norm(h)) or guard._G4_HEADER.search(C.norm(h)) or guard._F3_HEADER.search(C.norm(h)))})
 by={lab:{'columns':sum(r['truth']==lab for r in chosen),'tables':len({r['table'] for r in chosen if r['truth']==lab})} for lab in sorted({r['truth'] for r in chosen})}
 return {'columns':len(chosen),'tables':len({r['table'] for r in chosen}),'by_truth':by,
         'date_columns':sum(r['truth']=='date' for r in chosen),'non_date_columns':sum(r['truth']!='date' for r in chosen),
         'date_with_year_header_columns':sum(r['truth']=='date' and r['year_header_hint'] for r in chosen),
         'date_with_clock_header_columns':sum(r['truth']=='date' and r['clock_header_hint'] for r in chosen),
         'temporal_header_hint_columns':sum(r['temporal_header_hint'] for r in chosen),
         'temporal_header_hint_by_truth':dict(collections.Counter(r['truth'] for r in chosen if r['temporal_header_hint'])),
         'rows':chosen}

def decide(p,values,header=None,threshold=True):
 order=[(x['label'],x['probability']) for x in p['top3']]
 if threshold and order[0][1]<0.5:return ('unknown','probability_below_threshold')
 return guard.guard_with_reason(order[0][0],order,values,header=header)

def replay(val,raw_by_key):
 out=[]
 for job in (1,2):
  ps=json.loads((ROOT/f'eval_reports/latest/job{job}_probs_val_pool_ft.json').read_text())['rows']
  assert len(ps)==len(val)==4551
  exact=[];omitted=[];vsel=[];unfiltered=[];changes=[]
  for i,(p,r) in enumerate(zip(ps,val)):
   h,v,lab,ctx,t=r;assert (C.norm(h),lab)==(p['column'],p['truth'])
   expected=(p['guarded_prediction'],p['decision_reason'])
   actual=decide(p,v)
   if actual!=expected:exact.append(i)
   no=decide(p,v,threshold=False)
   if no[0]!=expected[0]:
    omitted.append({'index':i,'header':h,'truth':lab,'table':t,'stored_prediction':expected[0],
      'stored_reason':expected[1],'without_threshold_prediction':no[0],'top1_probability':p['top3'][0]['probability']})
   candidates=raw_by_key[t,h];junk={'nan','None','','NaN','null','NULL'}
   d=next(x for x in candidates if [s for s in x['values'] if s.strip() not in junk]==v)
   vv=[s for s in pick_values(d['values'],d.get('row_values')) if s.strip() not in junk]
   if decide(p,vv)[0]!=expected[0]:vsel.append(i)
   if decide(p,d['values'])[0]!=expected[0]:unfiltered.append(i)
   g=decide(p,v,header=h)
   if g[0]!=expected[0]:changes.append({'index':i,'header':h,'truth':lab,'from':expected[0],'to':g[0]})
  assert not exact,exact
  assert len(omitted)=={1:11,2:13}[job]
  assert all(x['stored_reason']=='probability_below_threshold' and x['top1_probability']<.5 for x in omitted)
  assert len(changes)==31 and all(x['to']==x['truth'] and x['from']=='unknown' for x in changes)
  out.append({'job':job,'v10_exact_match':4551,'v10_exact_reason_match':4551,
    'without_probability_threshold_mismatches':omitted,
    'FT_VALSEL_only_mismatch_indices':vsel,'unfiltered_values_only_mismatch_indices':unfiltered,
    'header_G_changes_with_threshold':changes})
 return out

def compact_counts(part):
 return ', '.join(f'{k}:{v["columns"]}列/{v["tables"]}表' for k,v in part['by_truth'].items()) or 'なし'

def main():
 before,tr,val,raw=load_snapshot();groups={}
 for key in DEFINITIONS:
  groups[key]={'definition':DEFINITIONS[key],
    'actual_training_after_cap_80pct':summarize(tr,key,.8),
    'actual_training_after_cap_all_usable':summarize(tr,key,1.0),
    'training_before_cap_80pct':summarize(before,key,.8)}
 rp=replay(val,raw)
 result={'base_commit':'113dcab','scope':'W2のpool学習側だけ。検証の様式を除外、label-fix適用後。主集計はcap4適用後の29696列。値は保存しない。',
    'pool_rows':38654,'before_cap_training_rows':34103,'after_cap_training_rows':29696,'validation_rows':4551,
    'selection':'NFKC・既知の欠け記号を除いた標本の80%以上が形に一致、非欠け>=1。すべて一致の感度集計も併記。予測規則の提案ではない。',
    'limits':'同じ形は意味の同一性ではない。5標本の集計で元表全行ではない。形は非排他、表数はラベル間重複あり。既存正解の誤りも未裁定。',
    'input_hashes':{f'eval_reports/latest/job{j}_probs_val_pool_ft.json':hashlib.sha256((ROOT/f'eval_reports/latest/job{j}_probs_val_pool_ft.json').read_bytes()).hexdigest() for j in (1,2)},
    'shapes':groups,'replay':rp}
 C.dump(OUT/'date_shapes_and_replay.json',result)
 md=['# W2：日付候補6形の分布とv10再現差','',
  '- W2の113dcabを基準に、教材38654列→label-fix153→family検証4551列を除外→cap4で学習29696列（cap前34103列）を再現。教材/規則/ラベル/依頼を変更していない。',
  '- 各形の定義はJSONを参照。主集計は欠けを除く標本の80%以上一致、最低1値。全値一致とcap前の感度集計もJSONに併記。形は非排他で、行数/表数を形間・ラベル間で単純加算しない。','',
  '| 値の形（主集計：cap後・80%） | 全列/表 | date列/表 | 非date列 | amount/quantity/id/category（列/表） |','|---|---:|---:|---:|---|']
 for key,g in groups.items():
  x=g['actual_training_after_cap_80pct'];dt=x['by_truth'].get('date',{'columns':0,'tables':0})
  others='; '.join(f'{lab} {x["by_truth"].get(lab,{"columns":0})["columns"]}/{x["by_truth"].get(lab,{"tables":0})["tables"]}' for lab in ('amount','quantity','id','category'))
  md.append(f'| {key} | {x["columns"]}/{x["tables"]} | {dt["columns"]}/{dt["tables"]} | {x["non_date_columns"]} | {others} |')
 md+=['','## 解釈','',
  '- 月日番号・4桁時刻・Excelシリアル風の数は、日付以外の数量/金額/識別コードと同じ形になり得る。集計は意味でdateを選んだものではない。入力に同じ形があっても一律dateにする根拠にはならない。',
  '- 年月6桁は主集計でid1列/date0、全値一致では0列。18世紀年とHH:MM:SS.00はcap前後とも0列。date比率が高いという学習根拠は今回の6形にはなく、ゼロ件の形は安全でなく未評価とする。',
  '- JSONには全ラベルの列数/表数、該当した列の見出し・表・保存正解、既存の日付語を見出しに持つ場合の内訳を保存。生値は保存しない。見出し語の有無は診断用の層別で、新しいguard規則ではない。',
  f'- hhmm4のdate502列のうち、年を示す見出しの列は{groups["hhmm4"]["actual_training_after_cap_80pct"]["date_with_year_header_columns"]}列、時刻を示す見出しの列は{groups["hhmm4"]["actual_training_after_cap_80pct"]["date_with_clock_header_columns"]}列。年2000等もHHMM形に合うため、dateの総数を時刻の教材の数と解釈しない。',
  '- dateの割合が高く見える少数の形でも、独立した表数・全値一致の感度・ラベル境界を確認してからClaudeが次の検証案を決める。今回、候補の採用や事前の線の変更はしていない。','',
  '## v10不一致11/13列の理由','',
  '- `train3.decide_with_details` は最大確率<0.5を先にunknownとし、その後でguardを呼ぶ。`guard_with_reason`単独呼出しにはこの閾値がない。',
  '- 閾値を省略した再現はjob1で4540/4551、job2で4538/4551となり、報告の不一致数11/13を正確に再現。24出力すべての保存reasonはprobability_below_thresholdで、top1<0.5。該当index/見出し/確率はJSONに保存。Claudeの未保存スクリプト自体は未確認だが、閾値省略だけでこの数が再現する。',
  '- W2当時の値と0.5閾値を含めれば、両jobとも4551/4551の予測とdecision_reasonが一致。FT_VALSELだけを変えた場合の差分はJSON参照。少なくとも11/13の主説明をFT_VALSELとする根拠は無い。',
  '- 閾値を維持した直しG（見出しを渡す）も当て直し、両job31列がunknown→保存正解、新しい誤り0を再確認。この検証集合内の結果で、未見データでの安全性を証明したとは扱わない。','',
  '## 再現・検証','',
  '`python research/w2_unknown/date_shapes_and_replay.py`。snapshotコード/教材一致・分割/上限/ラベル件数・全4551列×2jobのv10予測と理由・閾値省略11/13・G31/31をassert。学習/推論/外部取得なし。既存の禁止セット・固定評価は開かず、対象はW2教材庫だけ。','']
 (OUT/'date_shapes_and_replay.md').write_text('\n'.join(md))
 for k,g in groups.items():
  x=g['actual_training_after_cap_80pct'];print(k,compact_counts(x))
 print('replay exact',[(r['job'],r['v10_exact_match'],len(r['without_probability_threshold_mismatches']),r['FT_VALSEL_only_mismatch_indices']) for r in rp])
if __name__=='__main__':main()
