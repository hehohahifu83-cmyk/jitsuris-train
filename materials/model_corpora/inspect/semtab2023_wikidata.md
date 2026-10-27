# semtab2023_wikidata の点検（ファイルの形だけ）

- 出典：SemTab 2023 WikidataTables Round 1, DOI 10.5281/zenodo.8393535
- ライセンス表示：CC-BY-4.0
- URL：https://zenodo.org/records/8393535/files/WikidataTables2023R1.zip?download=1
- ダウンロード：9431371 bytes
- zip の中身：10446 件、展開後 73.7 MB
- 拡張子：{'.csv': 10429, '(なし)': 10, '.json': 4, '.py': 3}
- フォルダ（最初の 40）：['.', 'WikidataTables2023R1', 'WikidataTables2023R1/DataSets', 'WikidataTables2023R1/DataSets/Test', 'WikidataTables2023R1/DataSets/Test/gt', 'WikidataTables2023R1/DataSets/Test/tables', 'WikidataTables2023R1/DataSets/Test/targets', 'WikidataTables2023R1/DataSets/Valid', 'WikidataTables2023R1/DataSets/Valid/gt', 'WikidataTables2023R1/DataSets/Valid/tables', 'WikidataTables2023R1/DataSets/Valid/targets']

### WikidataTables2023R1/CTA_WD_Evaluator.py（4980 bytes）
```
import pandas as pd
import json
import os


class CTA_Evaluator:
  def __init__(self, answer_file_path, round=1):
    """
    `round` : Holds the round for which the evaluation is being done. 
    can be 1, 2...upto the number of rounds the challenge has.
    Different rounds will mostly have different ground truth files.
    """
    self.answer_file_path = answer_file_path
    self.round = round

  def _evaluate(self, client_payload, _context={}):
    """
    `client_payload` will be a dict with (atleast) the following keys :
      - submission_file_path : local file path of the submitted file
      - aicrowd_submission_id : A unique id representing the submission
      - aicrowd_participant_id : A unique id for participant/team submitting (if enabled)
    """
    submission_file_path = client_payload["submission_file_path"]

    gt_ancestor = json.load(open("./DataSets/HardTablesR2/Valid/gt/cta_gt_ancestor.json"))
    gt_descendent = json.load(open("./DataSets/HardTablesR2/Valid/gt/cta_gt_descendent.json"))

    cols, col_type = set(), dict()
    gt = pd.read_csv(self.answer_file_path, delimiter=',', names=['tab_id', 'col_id', 'type'],
                     dtype={'tab_id': str, 'col_id': str, 'type': str}, keep_default_na=False)
    for index, row in gt.iterrows():
        col = '%s %s' % (row['tab_id'], row['col_id'])
        gt_type = row['type']
        col_type[col] = gt_type
        cols.add(col)

    annotated_cols = set()
    total_score = 0
    sub = pd.read_csv(sub
```

### WikidataTables2023R1/CPA_WD_Evaluator.py（3956 bytes）
```
import pandas as pd
import os

class CPA_Evaluator:
  def __init__(self, answer_file_path, round=1):
    """
    `round` : Holds the round for which the evaluation is being done. 
    can be 1, 2...upto the number of rounds the challenge has.
    Different rounds will mostly have different ground truth files.
    """
    self.answer_file_path = answer_file_path
    self.round = round

  def _evaluate(self, client_payload, _context={}):
    """
    `client_payload` will be a dict with (atleast) the following keys :
      - submission_file_path : local file path of the submitted file
      - aicrowd_submission_id : A unique id representing the submission
      - aicrowd_participant_id : A unique id for participant/team submitting (if enabled)
    """
    submission_file_path = client_payload["submission_file_path"]

    gt_cols_pro = dict()
    gt = pd.read_csv(self.answer_file_path, delimiter=',', names=['tab_id', 'sub_col_id', 'obj_col_id', 'property'],
                     dtype={'tab_id': str, 'sub_col_id': str, 'obj_col_id': str, 'property': str}, keep_default_na=False)
    for index, row in gt.iterrows():
        cols = '%s %s %s' % (row['tab_id'], row['sub_col_id'], row['obj_col_id'])
        gt_cols_pro[cols] = row['property']

    annotated_cols, correct_cols = set(), set()
    sub = pd.read_csv(submission_file_path, delimiter=',', names=['tab_id', 'sub_col_id', 'obj_col_id', 'property'],
                      dtype={'tab_id': str, 'sub_col_id': str, 'obj_row_id': str,
```

### WikidataTables2023R1/DataSets/Valid/tables/Y3OHOKFF.csv（100 bytes）
```
col0,col1,col2
Three Little Pigs,4:3,The Three Little Pigs
Space Jam: A New Legacy,4:3,Space Jam

```

### WikidataTables2023R1/DataSets/Valid/tables/Y4OS3SBS.csv（126 bytes）
```
col0,col1
Roman Bridge,
Pont del Diable,
Ponte Vecchio,
Ponte Vecchio,
Pont de Pierre,1
Ponte Milvio,6
Pont du Gard,6

```

### WikidataTables2023R1/DataSets/Valid/tables/RQT6VSWL.csv（160 bytes）
```
col0,col1
zirconium-85m,10.9
zirconium-102,2.9
zirconium-109,63
zirconium-96,23500000000000000000
zirconium-98,30.7
zirconium-81,5.5
zirconium-103,1.32

```

### WikidataTables2023R1/DataSets/Valid/gt/cta_gt_descendent.json（1314167 bytes）
```
{"http://www.wikidata.org/entity/Q14947481": {}, "http://www.wikidata.org/entity/Q52721923": {}, "http://www.wikidata.org/entity/Q17272482": {}, "http://www.wikidata.org/entity/Q269949": {"http://www.wikidata.org/entity/Q5712736": "3", "http://www.wikidata.org/entity/Q47012": "2", "http://www.wikidata.org/entity/Q313301": "2", "http://www.wikidata.org/entity/Q320008": "2", "http://www.wikidata.org/entity/Q339800": "2", "http://www.wikidata.org/entity/Q693906": "2", "http://www.wikidata.org/entity/Q789026": "2", "http://www.wikidata.org/entity/Q1133841": "2", "http://www.wikidata.org/entity/Q1367934": "2", "http://www.wikidata.org/entity/Q2154027": "2", "http://www.wikidata.org/entity/Q3357704": "2", "http://www.wikidata.org/entity/Q3456602": "2", "http://www.wikidata.org/entity/Q4826921": "2", "http://www.wikidata.org/entity/Q5395107": "2", "http://www.wikidata.org/entity/Q7603361": "2", "http://www.wikidata.org/entity/Q10915476": "2", "http://www.wikidata.org/entity/Q11837631": "2", "http://www.wikidata.org/entity/Q25325210": "2", "http://www.wikidata.org/entity/Q26792858": "2", "http://www.wikidata.org/entity/Q57447621": "2", "http://www.wikidata.org/entity/Q57448432": "2", "http://www.wikidata.org/entity/Q106451534": "2", "http://www.wikidata.org/entity/Q112650017": "2", "http://www.wikidata.org/entity/Q115806173": "2", "http://www.wikidata.org/entity/Q115856942": "2", "http://www.wikidata.org/entity/Q115915688": "2", "http://www.wikidata.org/entity/Q115916067": "2", "http
```

### WikidataTables2023R1/DataSets/Valid/gt/cta_gt_ancestor.json（312146 bytes）
```
{"http://www.wikidata.org/entity/Q1852859": {"http://www.wikidata.org/entity/Q618123": "6", "http://www.wikidata.org/entity/Q112966864": "6", "http://www.wikidata.org/entity/Q2221906": "7", "http://www.wikidata.org/entity/Q23956024": "7", "http://www.wikidata.org/entity/Q58416391": "10", "http://www.wikidata.org/entity/Q874405": "4", "http://www.wikidata.org/entity/Q58778": "5", "http://www.wikidata.org/entity/Q16334295": "5", "http://www.wikidata.org/entity/Q99527517": "14", "http://www.wikidata.org/entity/Q82794": "5", "http://www.wikidata.org/entity/Q177634": "3", "http://www.wikidata.org/entity/Q27096235": "4", "http://www.wikidata.org/entity/Q16686448": "5", "http://www.wikidata.org/entity/Q27096213": "9", "http://www.wikidata.org/entity/Q17334923": "8", "http://www.wikidata.org/entity/Q16334298": "6", "http://www.wikidata.org/entity/Q4632675": "1", "http://www.wikidata.org/entity/Q4835091": "3", "http://www.wikidata.org/entity/Q486972": "2", "http://www.wikidata.org/entity/Q15642541": "2", "http://www.wikidata.org/entity/Q115095765": "9", "http://www.wikidata.org/entity/Q61961344": "7", "http://www.wikidata.org/entity/Q71468208": "8", "http://www.wikidata.org/entity/Q98119401": "8", "http://www.wikidata.org/entity/Q28813620": "10", "http://www.wikidata.org/entity/Q58415929": "12", "http://www.wikidata.org/entity/Q16889133": "9", "http://www.wikidata.org/entity/Q16887380": "9"}, "http://www.wikidata.org/entity/Q756102": {"http://www.wikidata.org/entity/Q618123": "10", "h
```

### WikidataTables2023R1/DataSets/Test/gt/cta_gt_descendent.json（64632311 bytes）
```
{"http://www.wikidata.org/entity/Q13414758": {}, "http://www.wikidata.org/entity/Q3558970": {"http://www.wikidata.org/entity/Q9386054": "1", "http://www.wikidata.org/entity/Q77836349": "1"}, "http://www.wikidata.org/entity/Q1959314": {"http://www.wikidata.org/entity/Q666294": "1", "http://www.wikidata.org/entity/Q1969226": "1", "http://www.wikidata.org/entity/Q27608973": "1", "http://www.wikidata.org/entity/Q55670430": "1", "http://www.wikidata.org/entity/Q55670432": "1", "http://www.wikidata.org/entity/Q55670434": "1", "http://www.wikidata.org/entity/Q108537461": "1"}, "http://www.wikidata.org/entity/Q2516330": {}, "http://www.wikidata.org/entity/Q21009059": {"http://www.wikidata.org/entity/Q413719": "1", "http://www.wikidata.org/entity/Q418492": "1"}, "http://www.wikidata.org/entity/Q28060956": {}, "http://www.wikidata.org/entity/Q726870": {"http://www.wikidata.org/entity/Q430289": "2", "http://www.wikidata.org/entity/Q466918": "2", "http://www.wikidata.org/entity/Q653793": "2", "http://www.wikidata.org/entity/Q672170": "2", "http://www.wikidata.org/entity/Q688825": "2", "http://www.wikidata.org/entity/Q750656": "2", "http://www.wikidata.org/entity/Q864801": "2", "http://www.wikidata.org/entity/Q926196": "2", "http://www.wikidata.org/entity/Q940518": "2", "http://www.wikidata.org/entity/Q1108172": "2", "http://www.wikidata.org/entity/Q1653985": "2", "http://www.wikidata.org/entity/Q1768969": "2", "http://www.wikidata.org/entity/Q1879631": "2", "http://www.wikidata.org/entit
```

### WikidataTables2023R1/CEA_WD_Evaluator.py（4026 bytes）
```
import pandas as pd
import os

class CEA_Evaluator:
    def __init__(self, answer_file_path, round=1):
        """
    `round` : Holds the round for which the evaluation is being done. 
    can be 1, 2...upto the number of rounds the challenge has.
    Different rounds will mostly have different ground truth files.
    """
        self.answer_file_path = answer_file_path
        self.round = round

    def _evaluate(self, client_payload, _context={}):
        """
    `client_payload` will be a dict with (atleast) the following keys :
      - submission_file_path : local file path of the submitted file
      - aicrowd_submission_id : A unique id representing the submission
      - aicrowd_participant_id : A unique id for participant/team submitting (if enabled)
    """
        submission_file_path = client_payload["submission_file_path"]

        gt_cell_ent = dict()
        gt = pd.read_csv(self.answer_file_path, delimiter=',', names=['tab_id', 'row_id', 'col_id', 'entity'],
                         dtype={'tab_id': str, 'row_id': str, 'col_id': str, 'entity': str}, keep_default_na=False)
        for index, row in gt.iterrows():
            cell = '%s %s %s' % (row['tab_id'], row['row_id'], row['col_id'])
            gt_cell_ent[cell] = row['entity']

        correct_cells, annotated_cells = set(), set()
        sub = pd.read_csv(submission_file_path, delimiter=',', names=['tab_id', 'row_id', 'col_id', 'entity'],
                          dtype={'tab_id': str, 'row_id': str, 
```
