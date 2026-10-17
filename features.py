"""特徴量（ブラウザ版の JavaScript と同じ計算にする。ここを変えたら column-ai.js も同じに直す）。
Sherlock（Hulsebos ほか 2019）の考え方を小さくしたもの：列名の文字のかたまり＋値の文字のかたまり＋値の統計。
"""
import math
import re
import unicodedata

H_DIM = 4096   # 列名の文字のかたまり
V_DIM = 2048   # 値の文字のかたまり
CTX_DIM = 512  # 同じ表のほかの列名（文脈。Sato の考え方）
X_DIM = 1024   # 列名の最後の部分 × 値の形（組み合わせ。OpenAI の指摘：線形では「この名前かつこの値」を表しにくい）
USE_CROSS = False


def fnv1a(s):
    h = 0x811C9DC5
    for b in s.encode("utf-8"):
        h ^= b
        h = (h * 0x01000193) & 0xFFFFFFFF
    return h


def norm_header(h):
    s = unicodedata.normalize("NFKC", str(h or "")).replace("\ufeff", "").lower().strip()
    s = re.sub(r"[\[\]【】「」\*＊]", "", s)
    return s


def header_grams(h):
    s = norm_header(h)
    out = []
    t = "^" + s + "$"
    for n in (1, 2, 3):
        for i in range(len(t) - n + 1):
            out.append("c" + str(n) + ":" + t[i:i + n])
    words = []
    for w in re.split(r"[^0-9a-z]+", s):
        if len(w) >= 2:
            out.append("w:" + w)
            words.append(w)
    # 複合語は最後の部分が種類を決める（日本語も英語も。例：取引先コード→コード、discount_code→code）
    core = re.sub(r"[\(（][^\)）]*[\)）]$", "", s)
    core = re.sub(r"[0-9_\-\s\.:#]+$", "", core)
    cc = list(core)
    for n in (1, 2, 3):
        if len(cc) >= n:
            out.append("e" + str(n) + ":" + "".join(cc[-n:]))
    ew = [w for w in re.split(r"[^a-z]+", core) if len(w) >= 2]
    camel = re.findall(r"[A-Z]?[a-z]+", unicodedata.normalize("NFKC", str(h or "")))
    if camel and len(camel) > 1:
        ew = [camel[-1].lower()]
    if ew:
        out.append("lw:" + ew[-1])
    return out


DATE_RES = [re.compile(p) for p in [
    r"^[0-9]{4}[/\-.][0-9]{1,2}[/\-.][0-9]{1,2}$", r"^[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日$", r"^[0-9]{8}$", r"^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$",
    r"^[rhs][0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}$", r"^令和[0-9]+年"]]
DATETIME_RE = re.compile(r"^[0-9]{4}[/\-][0-9]{1,2}[/\-][0-9]{1,2}[ t][0-9]{1,2}:[0-9]{2}")
TIME_RE = re.compile(r"^[0-9]{1,2}:[0-9]{2}(:[0-9]{2})?$")
NUM_RE = re.compile(r"^[+\-▲△]?[¥\\$]?[0-9][0-9,]*(\.[0-9]+)?(円|%)?$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$")
PHONE_RE = re.compile(r"^(\+81[ \-]?)?0?[0-9]{1,4}[ \-]?[0-9]{1,4}[ \-]?[0-9]{3,4}$")
POSTAL_RE = re.compile(r"^〒?[0-9]{3}-[0-9]{4}$")
PREF_RE = re.compile(r"(都|道|府|県)|(市|区|町|村)\S*[0-9]")
ORG_RE = re.compile(r"株式会社|有限会社|合同会社|\(株\)|\(有\)|銀行|信用金庫|商店|inc\.?$|llc|co\.,?")
STAT_NAMES = ["empty", "date", "datetime", "time", "num", "int", "decimal", "comma", "yen", "pct", "neg", "lead0", "email", "phone",
              "postal", "pref", "org", "kanji", "hira", "kata", "hkata", "latin", "digit", "space", "len_mean", "len_std", "len_fixed",
              "uniq", "log_mean", "log_std", "small_int", "bool"]


def char_class(c):
    o = ord(c)
    if 0x4E00 <= o <= 0x9FFF:
        return "kanji"
    if 0x3040 <= o <= 0x309F:
        return "hira"
    if 0x30A0 <= o <= 0x30FF:
        return "kata"
    if 0xFF66 <= o <= 0xFF9F:
        return "hkata"
    if ("a" <= c <= "z") or ("A" <= c <= "Z"):
        return "latin"
    if "0" <= c <= "9":
        return "digit"
    if c in " \t\n\r\f\v\u3000":
        return "space"
    return "other"


def to_number(v):
    s = v.replace(",", "").replace("¥", "").replace("\\", "").replace("$", "").replace("円", "").replace("%", "")
    neg = s.startswith(("-", "▲", "△"))
    s = s.lstrip("+-▲△")
    if not re.fullmatch(r"[0-9]+(\.[0-9]+)?", s):   # JavaScript と同じ厳しさ（1e5・inf・1_000 は数としない）
        return None
    x = float(s)
    return -x if neg else x


def value_stats(values):
    vals = [unicodedata.normalize("NFKC", str(v or "")).strip() for v in values]
    n_all = max(1, len(vals))
    ne = [v for v in vals if v != ""]
    st = dict.fromkeys(STAT_NAMES, 0.0)
    st["empty"] = 1 - len(ne) / n_all
    if not ne:
        return [st[k] for k in STAT_NAMES]
    n = len(ne)
    low = [v.lower() for v in ne]
    nums = [to_number(v) for v in ne]
    st["date"] = sum(any(r.match(v) for r in DATE_RES) for v in low) / n
    st["datetime"] = sum(bool(DATETIME_RE.match(v)) for v in low) / n
    st["time"] = sum(bool(TIME_RE.match(v)) for v in low) / n
    st["num"] = sum(bool(NUM_RE.match(v)) for v in ne) / n
    st["int"] = sum(x is not None and float(x).is_integer() for x in nums) / n
    st["decimal"] = sum(x is not None and not float(x).is_integer() for x in nums) / n
    st["comma"] = sum("," in v for v in ne) / n
    st["yen"] = sum(("¥" in v or "円" in v or "\\" in v) for v in ne) / n
    st["pct"] = sum("%" in v for v in ne) / n
    st["neg"] = sum(v[:1] in "-▲△" for v in ne) / n
    st["lead0"] = sum(len(v) > 1 and v[0] == "0" and "0" <= v[1] <= "9" for v in ne) / n
    st["email"] = sum(bool(EMAIL_RE.match(v)) for v in low) / n
    st["phone"] = sum(bool(PHONE_RE.match(v)) and len(re.sub(r"[^0-9]", "", v)) >= 10 for v in ne) / n
    st["postal"] = sum(bool(POSTAL_RE.match(v)) for v in ne) / n
    st["pref"] = sum(bool(PREF_RE.search(v)) for v in ne) / n
    st["org"] = sum(bool(ORG_RE.search(v)) for v in low) / n
    chars = "".join(ne)
    tot = max(1, len(chars))
    for c in chars:
        k = char_class(c)
        if k in st:
            st[k] += 1 / tot
    lens = [len(v) for v in ne]
    m = sum(lens) / n
    st["len_mean"] = math.log1p(m) / 4
    st["len_std"] = math.log1p(math.sqrt(sum((x - m) ** 2 for x in lens) / n)) / 3
    st["len_fixed"] = 1.0 if len(set(lens)) == 1 and n > 1 else 0.0
    st["uniq"] = len(set(ne)) / n
    xs = [abs(x) for x in nums if x is not None]
    if xs:
        logs = [math.log10(1 + x) for x in xs]
        lm = sum(logs) / len(logs)
        st["log_mean"] = lm / 8
        st["log_std"] = math.sqrt(sum((x - lm) ** 2 for x in logs) / len(logs)) / 3
        st["small_int"] = sum(x is not None and float(x).is_integer() and 0 <= x <= 1000 for x in nums) / n
    st["bool"] = sum(v in ("true", "false", "yes", "no", "0", "1", "○", "×", "有", "無") for v in low) / n
    return [st[k] for k in STAT_NAMES]


def value_grams(values):
    out = []
    for v in values:
        s = unicodedata.normalize("NFKC", str(v or "")).lower().strip()
        if not s:
            continue
        s = re.sub(r"[0-9]", "0", s)
        t = "^" + s[:24] + "$"
        for n in (2, 3):
            for i in range(len(t) - n + 1):
                out.append(t[i:i + n])
    return out


def context_grams(others):
    """同じ表のほかの列名から、文字のかたまり（2文字）と英単語を集める"""
    out = []
    for h in others or []:
        s = norm_header(h)
        out += [s[i:i + 2] for i in range(len(s) - 1)]
        out += ["w:" + w for w in re.split(r"[^0-9a-z]+", s) if len(w) >= 2]
    return out


def vectorize(header, values, use_header=True, use_values=True, context=None):
    """疎な特徴（添字→値）を返す。並びは [列名 H_DIM][値の文字 V_DIM][統計 len(STAT_NAMES)][定数1]"""
    f = {}
    if use_header:
        g = header_grams(header)
        for x in g:
            k = fnv1a("h" + x) % H_DIM
            f[k] = f.get(k, 0) + 1
        z = math.sqrt(sum(v * v for v in f.values())) or 1
        f = {k: v / z for k, v in f.items()}
    if use_values:
        g = value_grams(values)
        vf = {}
        for x in g:
            k = H_DIM + fnv1a("v" + x) % V_DIM
            vf[k] = vf.get(k, 0) + 1
        z = math.sqrt(sum(v * v for v in vf.values())) or 1
        for k, v in vf.items():
            f[k] = v / z
        for i, s in enumerate(value_stats(values)):
            if s:
                f[H_DIM + V_DIM + i] = s
    f[H_DIM + V_DIM + len(STAT_NAMES)] = 1.0
    if USE_CROSS:
        base_x = H_DIM + V_DIM + len(STAT_NAMES) + 1 + CTX_DIM
        st = dict(zip(STAT_NAMES, value_stats(values))) if values else None
        if st and st["empty"] < 0.999:
            flags = [n for n, ok in (("num", st["num"] > 0.8), ("int", st["int"] > 0.8), ("small", st["small_int"] > 0.8), ("yen", st["yen"] + st["comma"] > 0.3),
                                     ("lead0", st["lead0"] > 0.3), ("date", st["date"] + st["datetime"] > 0.5), ("pct", st["pct"] > 0.5), ("text", st["num"] < 0.2)) if ok]
            heads = [g for g in header_grams(header) if g[:2] in ("e2", "e3", "lw")]
            for g in heads:
                for fl in flags:
                    k = base_x + fnv1a("c" + g + "|" + fl) % X_DIM
                    f[k] = f.get(k, 0) + 0.5
    if USE_NUM2 and values:
        b2 = (DIM_X if USE_CROSS else DIM_CTX)
        for i, x in enumerate(num2_stats(values)):
            if x:
                f[b2 + i] = x
    if context is not None:
        base = H_DIM + V_DIM + len(STAT_NAMES) + 1
        cf = {}
        for x in context_grams(context):
            k = base + fnv1a("x" + x) % CTX_DIM
            cf[k] = cf.get(k, 0) + 1
        z = math.sqrt(sum(v * v for v in cf.values())) or 1
        for k, v in cf.items():
            f[k] = v / z
    return f


DIM = H_DIM + V_DIM + len(STAT_NAMES) + 1
DIM_CTX = DIM + CTX_DIM
DIM_X = DIM_CTX + X_DIM


def set_dims(h=4096, v=2048, ctx=512, x=1024, cross=False):
    """許容量（特徴の枠の大きさ）を変える（v8〜）。モデルの JSON に h_dim・v_dim・ctx_dim・x_dim・cross を書き、ブラウザ版も同じ値で読む"""
    global H_DIM, V_DIM, CTX_DIM, X_DIM, USE_CROSS, DIM, DIM_CTX, DIM_X
    H_DIM, V_DIM, CTX_DIM, X_DIM, USE_CROSS = h, v, ctx, x, cross
    DIM = H_DIM + V_DIM + len(STAT_NAMES) + 1
    DIM_CTX = DIM + CTX_DIM
    DIM_X = DIM_CTX + X_DIM


USE_NUM2 = False   # 数字の列の値の形をさらに細かく（v8 の試験、ChatGPT 提案 20261017-0047 の1）
NUM2_NAMES = ["d1_2", "d3_4", "d5_6", "d7_8", "d9_11", "d12p", "len_same", "q10", "q50", "q90", "spread", "all_neg", "any_neg",
              "seq", "ymd8", "year", "unit01", "plus", "dec1", "dec2", "dec3p", "zero", "round100", "dup"]


def num2_stats(values):
    import re as _re
    vals = [unicodedata.normalize("NFKC", str(v or "")).strip() for v in values]
    ne = [v for v in vals if v]
    out = dict.fromkeys(NUM2_NAMES, 0.0)
    xs = [(v, to_number(v)) for v in ne]
    nums = [(v, x) for v, x in xs if x is not None]
    if not nums:
        return [0.0] * len(NUM2_NAMES)
    n = len(nums)
    digs = [len(_re.sub(r"[^0-9]", "", v.split(".")[0])) for v, _ in nums]
    for d in digs:
        k = "d1_2" if d <= 2 else "d3_4" if d <= 4 else "d5_6" if d <= 6 else "d7_8" if d <= 8 else "d9_11" if d <= 11 else "d12p"
        out[k] += 1 / n
    out["len_same"] = 1.0 if len(set(len(v) for v, _ in nums)) == 1 and n > 1 else 0.0
    ls = sorted(math.log10(1 + abs(x)) for _, x in nums)
    q = lambda p: ls[min(n - 1, int(p * (n - 1) + 0.5))]
    out["q10"], out["q50"], out["q90"] = q(0.1) / 10, q(0.5) / 10, q(0.9) / 10
    out["spread"] = (ls[-1] - ls[0]) / 10
    negs = sum(x < 0 for _, x in nums)
    out["all_neg"] = 1.0 if negs == n else 0.0
    out["any_neg"] = 1.0 if negs else 0.0
    xs_ = [x for _, x in nums]
    out["seq"] = 1.0 if n > 2 and all(b - a == 1 for a, b in zip(sorted(xs_), sorted(xs_)[1:])) else 0.0
    out["ymd8"] = sum(_re.fullmatch(r"(19|20)[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])", v) is not None for v, _ in nums) / n
    out["year"] = sum(float(x).is_integer() and 1900 <= x <= 2100 for _, x in nums) / n
    out["unit01"] = sum(0 <= x <= 1 and not float(x).is_integer() for _, x in nums) / n
    out["plus"] = sum(v.startswith("+") for v, _ in nums) / n
    for v, _ in nums:
        dp = len(v.split(".")[1]) if "." in v else 0
        if dp == 1: out["dec1"] += 1 / n
        elif dp == 2: out["dec2"] += 1 / n
        elif dp >= 3: out["dec3p"] += 1 / n
    out["zero"] = sum(x == 0 for _, x in nums) / n
    out["round100"] = sum(x != 0 and float(x).is_integer() and x % 100 == 0 for _, x in nums) / n
    out["dup"] = 1 - len(set(xs_)) / n
    return [out[k] for k in NUM2_NAMES]


def total_dim():
    return (DIM_X if USE_CROSS else DIM_CTX) + (len(NUM2_NAMES) if USE_NUM2 else 0)
