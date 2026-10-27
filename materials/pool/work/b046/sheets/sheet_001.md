# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Unnamed: 0
- 例1 値：0 | 1 | 2 | 3 | 4
  - 同じ表の列：GoldID, QID, Name, Formula, Identifiers, Properties, Formula unit, Formula sympy

## g0002（1 列）
- 見出し：GoldID
- 例1 値：310 | 311 | 312 | 313 | 314
  - 同じ表の列：Unnamed: 0, QID, Name, Formula, Identifiers, Properties, Formula unit, Formula sympy

## g0003（1 列）
- 見出し：QID
- 例1 値：Q11376 | Q186300 | Q834020 | Q161254 | Q161635
  - 同じ表の列：Unnamed: 0, GoldID, Name, Formula, Identifiers, Properties, Formula unit, Formula sympy

## g0004（1 列）
- 見出し：Name
- 例1 値：acceleration | angular acceleration | angular frequency | angular momentum | angular velocity
  - 同じ表の列：Unnamed: 0, GoldID, QID, Formula, Identifiers, Properties, Formula unit, Formula sympy

## g0005（1 列）
- 見出し：Formula
- 例1 値：a = \frac{d v}{d t} | \boldsymbol{\alpha} = \frac{d \boldsymb… | \omega = 2 \pi f | L = R* p | \boldsymbol{\omega} = \frac{d \varphi}{…
  - 同じ表の列：Unnamed: 0, GoldID, QID, Name, Identifiers, Properties, Formula unit, Formula sympy

## g0006（1 列）
- 見出し：Identifiers
- 例1 値：[('acceleration', 'a', 'm s^-2'), ('vel… | [('angular acceleration', '\\boldsymbol… | [('angular frequency', '\\omega', 's^-1… | [('angular momentum', 'L', 'm^2 kg s^-1… | [('velocity', 'v', 'm s^-1'), ('radius'…
  - 同じ表の列：Unnamed: 0, GoldID, QID, Name, Formula, Properties, Formula unit, Formula sympy

## g0007（1 列）
- 見出し：Properties
- 例1 値：P7235 | P7235 | P7235 | P7235 | P7235
  - 同じ表の列：Unnamed: 0, GoldID, QID, Name, Formula, Identifiers, Formula unit, Formula sympy

## g0008（1 列）
- 見出し：Formula unit
- 例1 値：m s^-2 | s^-2 | s^-1 | m^2 kg s^-1 | s^-1
  - 同じ表の列：Unnamed: 0, GoldID, QID, Name, Formula, Identifiers, Properties, Formula sympy

## g0009（1 列）
- 見出し：Formula sympy
- 例1 値：2*pi*f | R*p | 0 | -m*v**2 | pi*d
  - 同じ表の列：Unnamed: 0, GoldID, QID, Name, Formula, Identifiers, Properties, Formula unit

## g0010（1 列）
- 見出し：Identifiers sympy
- 例1 値：(a, v, t) | (\boldsymbol{\alpha}, \boldsymbol{\omeg… | (\omega, f) | (L, r, p) | (v, r, a_c)
  - 同じ表の列：Unnamed: 0, GoldID, QID, Name, Formula, Identifiers, Properties, Formula unit

## g0011（1 列）
- 見出し：Sympy rhs
- 例1 値：2*pi | 3*R | 0 | -175 | pi*d
  - 同じ表の列：Unnamed: 0, GoldID, QID, Name, Formula, Identifiers, Properties, Formula unit

## g0012（1 列）
- 見出し：Sympy solve
- 例1 値：[(\omega, []), (f, [omega/(2*pi)])] | [(L, [R*p]), (r, []), (p, [L/R])] | [(F, [-m*v**2]), (m, [-F/v**2]), (v, [-… | [(d, [C/pi]), (C, [pi*d]), (r, [])] | [(k, [2*U/(Delta*x**2)]), (\Delta, []),…
  - 同じ表の列：Unnamed: 0, GoldID, QID, Name, Formula, Identifiers, Properties, Formula unit

## g0013（1 列）
- 見出し：list_name
- 例1 値：yk45i75 | yk45i75 | yk45i75 | fz2pa27 | fz2pa27
  - 同じ表の列：name, label

## g0014（1 列）
- 見出し：name
- 例1 値：room_temperatu | elevated_tempe | cryo_temperatu | celsius | kelvin
  - 同じ表の列：list_name, label

## g0015（1 列）
- 見出し：label
- 例1 値：Room Temperature | Elevated Temperature | Cryo Temperature | Celsius | Kelvin
  - 同じ表の列：list_name, name

## g0016（1 列）
- 見出し：plane
- 例1 値：51 pegasi b | 55 cancri d | jupi | gliese 581c | sa
  - 同じ表の列：Unnamed: 1

## g0017（1 列）
- 見出し：Unnamed: 1
- 例1 値：er | urn | auri bb | une | h
  - 同じ表の列：plane

## g0018（1 列）
- 見出し：names
- 例1 値：SMC | LMC | NGC-221 | NGC-224 | NGC-598
  - 同じ表の列：distances, velocities

## g0019（1 列）
- 見出し：distances
- 例1 値：0.032 | 0.034 | 0.275 | 0.275 | 0.263
  - 同じ表の列：names, velocities

## g0020（1 列）
- 見出し：velocities
- 例1 値：170 | 290 | -185 | -220 | -70
  - 同じ表の列：names, distances

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
```
