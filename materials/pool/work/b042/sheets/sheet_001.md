# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（3 列）
- 見出し：ID
- 例1 値：10101454 | 10101453 | 10101452 | 10101451 | 10101450
  - 同じ表の列：Type, Points, Comments, Author, Title, Content
- 例2 値：9037913 | 9037912 | 9037911 | 9037910 | 9037909
  - 同じ表の列：Type, Story, Parent, Points, Comments, Author, Title

## g0002（3 列）
- 見出し：Type
- 例1 値：comment | comment | comment | story | comment
  - 同じ表の列：ID, Points, Comments, Author, Title, Content
- 例2 値：comment | story | comment | story | comment
  - 同じ表の列：ID, Story, Parent, Points, Comments, Author, Title

## g0003（3 列）
- 見出し：Points
- 例1 値：0 | 0 | 0 | 1 | 0
  - 同じ表の列：ID, Type, Comments, Author, Title, Content
- 例2 値：0 | 3 | 0 | 14 | 0
  - 同じ表の列：ID, Type, Story, Parent, Comments, Author, Title

## g0004（3 列）
- 見出し：Comments
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：ID, Type, Points, Author, Title, Content
- 例2 値：0 | 0 | 0 | 7 | 0
  - 同じ表の列：ID, Type, Story, Parent, Points, Author, Title

## g0005（3 列）
- 見出し：Author
- 例1 値：MyDogHasFleas | jtheory | siegecraft | fspeech | nickpsecurity
  - 同じ表の列：ID, Type, Points, Comments, Title, Content
- 例2 値：infraruby | dottrap | bronz | rahulgolwalkar | Animats
  - 同じ表の列：ID, Type, Story, Parent, Points, Comments, Title

## g0006（1 列）
- 見出し：Title
- 例1 値：Jsonnet is a configuration language tha… | iOS 9 Ad Blocker Benchmarks | Natural and Artificial Intelligence (19… | Ask HN: How much equity does one deserv… | Ports and Power in the Indian Ocean
  - 同じ表の列：ID, Type, Points, Comments, Author, Content

## g0007（1 列）
- 見出し：Content
- 例1 値：The X in Xedit was for Xavier Delambert… | Right; in some cases it& | Is that really that surprising, though?… | Unsurprising given it was built by the … | Usually this is best done by in-house e…
  - 同じ表の列：ID, Type, Points, Comments, Author, Title

## g0008（2 列）
- 見出し：Story
- 例1 値：9035549.0 | 9037788.0 | 9034690.0 | 9037151.0 | 9036407.0
  - 同じ表の列：ID, Type, Parent, Points, Comments, Author, Title
- 例2 値：5919112.0 | 5925525.0 | 5925579.0 | 5925828.0 | 5925910.0
  - 同じ表の列：ID, Type, Parent, Points, Comments, Author, Title, URL

## g0009（2 列）
- 見出し：Parent
- 例1 値：9037886.0 | 9037788.0 | 9037104.0 | 9037525.0 | 9036407.0
  - 同じ表の列：ID, Type, Story, Points, Comments, Author, Title
- 例2 値：5922584.0 | 5925525.0 | 5925579.0 | 5925828.0 | 5925910.0
  - 同じ表の列：ID, Type, Story, Points, Comments, Author, Title, URL

## g0010（1 列）
- 見出し：Title
- 例1 値：Feds can read emails after 180 days wit… | Your Crush wont say NO to your Valentin… | Now Gmail Will Let You Share Attachment… | Vehicle-miles driven declining since 20… | Jeb Bush just published thousands of ci…
  - 同じ表の列：ID, Type, Story, Parent, Points, Comments, Author

## g0011（1 列）
- 見出し：Title
- 例1 値：The Recorded Future | Machined Learnings: ICML 2013: Sparse, … | Senator Bernie Sanders' Restore Our Pri… | Booz Allen, the World's Most Profitable… | Honcho: a python clone of Foreman.
  - 同じ表の列：ID, Type, Story, Parent, Points, Comments, Author, URL

## g0012（1 列）
- 見出し：URL
- 例1 値：http://www.mimisbrunnr.net/~munin/blog/… | http://www.machinedlearnings.com/2013/0… | http://www.sanders.senate.gov/newsroom/… | http://www.businessweek.com/printer/art… | https://github.com/nickstenning/honcho
  - 同じ表の列：ID, Type, Story, Parent, Points, Comments, Author, Title

## g0013（1 列）
- 見出し：Content
- 例1 値：I was commenting on the podcast, which … | Did Dropbox buy Snapjoy or did the team… | People aren& | Two things:<p>1. This is incredibly ane… | Looks great!<p>One thing R really needs…
  - 同じ表の列：ID, Type, Story, Parent, Points, Comments, Author, Title

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
```
