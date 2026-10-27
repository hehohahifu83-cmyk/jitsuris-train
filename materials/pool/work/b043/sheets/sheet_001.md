# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：id
- 例1 値：http://schema.org/3DModel | http://schema.org/AdvertiserContentArti… | http://schema.org/AnalysisNewsArticle | http://schema.org/ArchiveComponent | http://schema.org/ArchiveOrganization
  - 同じ表の列：label, comment, subTypeOf, enumerationtype, properties, subTypes, isPartOf

## g0002（1 列）
- 見出し：label
- 例1 値：3DModel | AdvertiserContentArticle | AnalysisNewsArticle | ArchiveComponent | ArchiveOrganization
  - 同じ表の列：id, comment, subTypeOf, enumerationtype, properties, subTypes, isPartOf

## g0003（1 列）
- 見出し：comment
- 例1 値：A 3D model represents some kind of 3D c… | An <a class="localLink" href="http://sc… | An AnalysisNewsArticle is a <a class="l… | An intangible type to be applied to any… | An organization with archival holdings.…
  - 同じ表の列：id, label, subTypeOf, enumerationtype, properties, subTypes, isPartOf

## g0004（1 列）
- 見出し：subTypeOf
- 例1 値：http://schema.org/CreativeWork | http://schema.org/Article | http://schema.org/NewsArticle | http://schema.org/CreativeWork | http://schema.org/LocalBusiness
  - 同じ表の列：id, label, comment, enumerationtype, properties, subTypes, isPartOf

## g0005（1 列）
- 見出し：enumerationtype
- 例1 値：http://schema.org/LegalValueLevel | http://schema.org/LegalValueLevel | http://schema.org/RefundTypeEnumeration | http://schema.org/RefundTypeEnumeration | http://schema.org/LegalForceStatus
  - 同じ表の列：id, label, comment, subTypeOf, properties, subTypes, isPartOf

## g0006（1 列）
- 見出し：properties
- 例1 値：http://schema.org/conditionsOfAccess, h… | http://schema.org/backstory | http://schema.org/conditionsOfAccess, h… | http://schema.org/archiveHeld | http://schema.org/codeValue, http://sch…
  - 同じ表の列：id, label, comment, subTypeOf, enumerationtype, subTypes, isPartOf

## g0007（1 列）
- 見出し：subTypes
- 例1 値：http://schema.org/ReviewNewsArticle | http://schema.org/CategoryCode | http://schema.org/CategoryCodeSet | http://schema.org/MonetaryGrant | http://schema.org/LegislationObject
  - 同じ表の列：id, label, comment, subTypeOf, enumerationtype, properties, isPartOf

## g0008（1 列）
- 見出し：isPartOf
- 例1 値：http://pending.schema.org | http://pending.schema.org | http://pending.schema.org | http://pending.schema.org | http://pending.schema.org
  - 同じ表の列：id, label, comment, subTypeOf, enumerationtype, properties, subTypes

## g0009（1 列）
- 見出し：Unnamed: 0
- 例1 値：0 | 1 | 2 | 3 | 4
  - 同じ表の列：assoc

## g0010（1 列）
- 見出し：assoc
- 例1 値：they buy | they buy | they buy | they sell | they buy
  - 同じ表の列：Unnamed: 0

## g0011（1 列）
- 見出し：id
- 例1 値：1 | 2 | 3 | 4 | 5
  - 同じ表の列：msg_id, parent_id, link_id, Count_read, Forum, Rank, Activity, Merit

## g0012（1 列）
- 見出し：msg_id
- 例1 値：msg31594372 | msg31606291 | msg31611001 | msg31655106 | msg31655299
  - 同じ表の列：id, parent_id, link_id, Count_read, Forum, Rank, Activity, Merit

## g0013（1 列）
- 見出し：parent_id
- 例1 値：https://bitcointalk.org/index.php?topic… | https://bitcointalk.org/index.php?topic… | https://bitcointalk.org/index.php?topic… | https://bitcointalk.org/index.php?topic… | https://bitcointalk.org/index.php?topic…
  - 同じ表の列：id, msg_id, link_id, Count_read, Forum, Rank, Activity, Merit

## g0014（1 列）
- 見出し：link_id
- 例1 値：msg31655299
  - 同じ表の列：id, msg_id, parent_id, Count_read, Forum, Rank, Activity, Merit

## g0015（1 列）
- 見出し：Count_read
- 例1 値：395 | 395 | 395 | 395 | 395
  - 同じ表の列：id, msg_id, parent_id, link_id, Forum, Rank, Activity, Merit

## g0016（1 列）
- 見出し：Forum
- 例1 値：Announcements (Altcoins) | Announcements (Altcoins) | Announcements (Altcoins) | Announcements (Altcoins) | Announcements (Altcoins)
  - 同じ表の列：id, msg_id, parent_id, link_id, Count_read, Rank, Activity, Merit

## g0017（1 列）
- 見出し：Rank
- 例1 値：Copper Member | Newbie | Copper Member | Newbie | Member
  - 同じ表の列：id, msg_id, parent_id, link_id, Count_read, Forum, Activity, Merit

## g0018（1 列）
- 見出し：Activity
- 例1 値：9 | 6 | 9 | 6 | 224
  - 同じ表の列：id, msg_id, parent_id, link_id, Count_read, Forum, Rank, Merit

## g0019（1 列）
- 見出し：Merit
- 例1 値：0 | 0 | 0 | 0 | 10
  - 同じ表の列：id, msg_id, parent_id, link_id, Count_read, Forum, Rank, Activity

## g0020（1 列）
- 見出し：Title
- 例1 値：[ANN][ICO] MVI Coin - Value Invest, all… | [ANN][ICO] MVI Coin - Value Invest, all… | [ANN][ICO] MVI Coin - Value Invest, all… | [ANN][ICO] MVI Coin - Value Invest, all… | [ANN][ICO] MVI Coin - Value Invest, all…
  - 同じ表の列：id, msg_id, parent_id, link_id, Count_read, Forum, Rank, Activity

## g0021（1 列）
- 見出し：ScamHeader
- 例1 値：False | False | False | False | False
  - 同じ表の列：id, msg_id, parent_id, link_id, Count_read, Forum, Rank, Activity

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
g0008	
g0009	
g0010	
g0011	
g0012	
g0013	
g0014	
g0015	
g0016	
g0017	
g0018	
g0019	
g0020	
g0021	
```
