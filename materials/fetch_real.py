"""本物の値つきの表を集める（GitHub Actions で実行・研究ブランチだけに保存）。お客さまのデータではなく公開データ。
1. GitTables 1M（Zenodo 6517052、各表は配布可能なライセンス）：小さめの話題の zip をいくつか取り、各表の列名・値の見本5件・同じ表の列名を取り出す
2. e-Gov データポータル（日本の行政のオープンデータ、CKAN API）：CSV をいくつか取り、同じく取り出す
出力：materials/real_corpus.jsonl（1行＝1列：source, table, header, values, context）
未見セット1〜4・開発用セット・Claude の評価用の出典とは別（GitTables は以前の除外一覧に入れてあり、未見セット側で使っていない）"""
import csv, io, json, os, random, re, sys, time, urllib.parse, urllib.request, zipfile

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_corpus.jsonl")
UA = {"User-Agent": "jitsurio-research/1.0 (+github actions)"}
rng = random.Random(20261016)
MAX_PER_SOURCE_COLS = {"gittables": 12000, "egov": 8000}


def get(url, timeout=120, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except Exception:  # noqa: BLE001
            if i == tries - 1:
                raise
            time.sleep(5 * (i + 1))


def emit(f, source, table, headers, rows):
    n = 0
    for j, h in enumerate(headers):
        h = str(h or "").strip()
        if not h or len(h) > 60:
            continue
        vals = [str(r[j]).strip() for r in rows if j < len(r) and str(r[j]).strip()]
        if not vals:
            continue
        sample = rng.sample(vals, min(5, len(vals)))
        f.write(json.dumps({"source": source, "table": table, "header": h, "values": [v[:60] for v in sample],
                            "context": [str(x)[:40] for k, x in enumerate(headers) if k != j][:20]}, ensure_ascii=False) + "\n")
        n += 1
    return n


BIZ = ["invoice", "order", "sale", "customer", "client", "product", "payment", "transaction", "employee", "salary", "payroll", "price",
       "purchase", "supplier", "vendor", "inventory", "stock", "expense", "budget", "shipment", "shipping", "billing", "receipt", "contact",
       "account", "ledger", "tax", "store", "shop", "retail", "item", "contract", "loan", "bank", "revenue", "cost", "member", "user", "email", "phone"]


def gittables(f, biz=False):
    import pyarrow.parquet as pq
    rec = json.loads(get("https://zenodo.org/api/records/6517052"))
    files = [x for x in rec.get("files", []) if x.get("size", 0) < (60_000_000 if biz else 15_000_000) and x["key"].endswith(".zip")]
    if biz:  # 業務らしい話題の zip だけ（GitTables は話題ごとの zip）
        files = [x for x in files if any(k in x["key"].lower() for k in BIZ)]
        print("業務らしい話題:", len(files), [x["key"] for x in files][:80])
    rng.shuffle(files)
    total = 0
    for x in files[:(40 if biz else 25)]:
        try:
            z = zipfile.ZipFile(io.BytesIO(get(x["links"]["self"], 300)))
        except Exception as e:  # noqa: BLE001
            print("skip", x["key"], e); continue
        names = [n for n in z.namelist() if n.endswith(".parquet")]
        rng.shuffle(names)
        for n in names[:60]:
            try:
                t = pq.read_table(io.BytesIO(z.read(n))).to_pandas()
            except Exception:  # noqa: BLE001
                continue
            rows = t.head(200).astype(str).values.tolist()
            total += emit(f, "gittables:" + x["key"], n, list(t.columns), rows)
            if total >= MAX_PER_SOURCE_COLS["gittables"] * (2 if biz else 1):
                return total
    return total


def decode(b):
    for enc in ("utf-8-sig", "cp932", "utf-8"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            continue
    return None


def egov(f):
    total = 0
    base = "https://data.e-gov.go.jp/data/api/3/action/package_search"
    for start in range(0, 2000, 100):
        try:
            res = json.loads(get(f"{base}?q=res_format:CSV&rows=100&start={start}"))
        except Exception as e:  # noqa: BLE001
            print("egov search stop", e); break
        pkgs = (res.get("result") or {}).get("results") or []
        if not pkgs:
            break
        for p in pkgs:
            csvs = [r for r in p.get("resources", []) if str(r.get("format", "")).lower() == "csv" and r.get("url")]
            if not csvs:
                continue
            r = rng.choice(csvs)
            try:
                b = get(r["url"], 60)[:400_000]
            except Exception:  # noqa: BLE001
                continue
            txt = decode(b)
            if not txt:
                continue
            try:
                rows = list(csv.reader(io.StringIO(txt, newline="")))[:200]
            except Exception:  # noqa: BLE001
                continue
            if len(rows) < 3 or len(rows[0]) < 2:
                continue
            total += emit(f, "egov:" + p.get("name", ""), r["url"], rows[0], rows[1:])
            if total >= MAX_PER_SOURCE_COLS["egov"]:
                return total
            time.sleep(0.3)
    return total


PERSONAL = re.compile(r"e-?mail|phone|tel\b|fax|cardholder|first ?name|last ?name|surname|employee ?name|氏名|電話|メール|ＦＡＸ|携帯", re.I)
CKAN = [  # 業務らしい公開の表（支出・契約・調達・予算）。個人の連絡先らしい列は取らない（2回目：出典と検索語を広げる）
    ("datagov_uk2", "https://data.gov.uk/api/action/package_search", ["purchase card transactions", "expenditure exceeding", "grants awarded", "contracts awarded", "invoice payment", "supplier payments", "asset register", "fees and charges", "income and expenditure", "stock", "sales", "orders"]),
    ("ireland", "https://data.gov.ie/api/3/action/package_search", ["purchase orders", "payments", "contracts", "procurement", "expenditure", "invoices", "budget", "grants"]),
    ("nz", "https://catalogue.data.govt.nz/api/3/action/package_search", ["procurement", "contracts", "expenditure", "payments", "budget", "grants", "revenue"]),
    ("egov_biz2", "https://data.e-gov.go.jp/data/api/3/action/package_search", ["売上", "販売", "支払", "請求", "決算", "財務", "使用料", "手数料", "取引", "在庫", "物品調達", "工事"]),
    ("canada2", "https://open.canada.ca/data/api/3/action/package_search", ["purchase orders", "invoices", "sales", "revenue", "payments to suppliers", "standing offers"]),
]

STATS = {}


def ckan_biz(f, name, base, queries, cap=6000, budget=900):
    total = 0; seen = set(); t0 = time.time()
    st = STATS.setdefault(name, {"pkgs": 0, "csv": 0, "dl_fail": 0, "parse_fail": 0, "tables": 0, "search_fail": 0})
    for q in queries:
        if time.time() - t0 > budget:
            break
        try:
            res = json.loads(get(f"{base}?q={urllib.parse.quote(q)}&fq=res_format:CSV&rows=60", 30, 2))
        except Exception as e:  # noqa: BLE001
            st["search_fail"] += 1; print(name, "search fail", q, e); continue
        for p in (res.get("result") or {}).get("results") or []:
            if time.time() - t0 > budget:
                break
            st["pkgs"] += 1
            if p.get("name") in seen:
                continue
            seen.add(p.get("name"))
            csvs = [r for r in p.get("resources", []) if str(r.get("format", "")).lower().strip(". ") == "csv" and r.get("url")]
            if not csvs:
                continue
            st["csv"] += 1
            r = rng.choice(csvs)
            try:
                b = get(r["url"], 20, 1)[:600_000]
            except Exception:  # noqa: BLE001
                st["dl_fail"] += 1; continue
            txt = decode(b)
            if not txt:
                st["parse_fail"] += 1; continue
            try:
                rows = list(csv.reader(io.StringIO(txt, newline="")))[:300]
            except Exception:  # noqa: BLE001
                st["parse_fail"] += 1; continue
            if len(rows) < 4 or len(rows[0]) < 3:
                st["parse_fail"] += 1; continue
            st["tables"] += 1
            head = rows[0]
            keep = [j for j, h in enumerate(head) if not PERSONAL.search(str(h))]
            rows2 = [[row[j] if j < len(row) else "" for j in keep] for row in rows]
            # 値がメール・電話の形の列も落とす
            def personal_vals(j):
                vals = [x[j] for x in rows2[1:30] if j < len(x)]
                return sum(bool(re.search(r"@|\+?\d{2,4}[- ]\d{2,4}[- ]\d{3,4}", v)) for v in vals) > len(vals) * 0.3
            ok = [j for j in range(len(rows2[0])) if not personal_vals(j)]
            rows3 = [[x[j] for j in ok] for x in rows2]
            total += emit(f, f"{name}:{p.get('name', '')}", r["url"], rows3[0], rows3[1:])
            if total >= cap:
                return total
            time.sleep(0.3)
    return total


DIRECT = [  # ChatGPT 提案（20261017-0031）。学習用だけ（未見セット7には使わない）
    ("canada_contracts", "https://open.canada.ca/data/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b/resource/fac950c0-00d5-4ec1-a4d3-9cbebf98a305/download/contracts.csv"),
    ("ireland_etenders", "https://assets.gov.ie/static/documents/4d482e0e/Public_Procurement_Opendata_Dataset.csv"),
]


def direct(f):
    rep = {}
    for name, url in DIRECT:
        try:
            b = get(url, 120, 2)[:3_000_000]
            txt = decode(b)
            rows = list(csv.reader(io.StringIO(txt, newline="")))
            head, body = rows[0], rows[1:]
            rng.shuffle(body); body = body[:400]
            keep = [j for j, h in enumerate(head) if not PERSONAL.search(str(h))]
            rows2 = [[r[j] if j < len(r) else "" for j in keep] for r in [head] + body]
            # 1つの大きな表を、列の組み合わせの違う複数の「表」として見せないよう、そのまま1表として出す
            rep[name] = emit(f, f"direct:{name}", url, rows2[0], rows2[1:])
        except Exception as e:  # noqa: BLE001
            rep[name] = "error " + str(e)[:120]
    return rep


JP_PAGES = [  # ChatGPT 提案（20261017-1325）。日本の調達・契約・補助金の CSV。学習用だけ
    ("cao_keiyaku", "https://www.cao.go.jp/chotatsu/kohyo/kohyo.html"),
    ("yamagata_nyusatsu", "https://www.city.yamagata-yamagata.lg.jp/opendata/category/1007066/1002550.html"),
    ("nerima_chotatsu", "https://www.city.nerima.tokyo.jp/kusei/tokei/opendata/opendatasite/tokei_kusei/tyoutatujouhou.html"),
    ("npa_hojokin", "https://www.npa.go.jp/policies/budget/yosanjouhou/hojokin.html"),
    ("setagaya_zuikei", "https://www.city.setagaya.lg.jp/opendata/index.php?desc=summary&displayedresults=30&p=27_1"),
]


JP_DIRECT = [  # ChatGPT 提案（20261017-1928）。青森市・山口県の契約、摂津市・海南市の固定資産台帳。学習用だけ
    ('契約方式別契約区分表', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-1-keiyakujisseki-keiyakuhousikibetu.csv'),
    ('一者随契根拠別契約区分表', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-2-keiyakujisseki-zuikeibetu.csv'),
    ('工事契約件数・契約金額調', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-3-1-keiyakujisseki-koujikensusirabe.csv'),
    ('工事', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-3-2-keiyakujisseki-kouji.csv'),
    ('設計等委託', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-4-keiyakujisseki-sekkeitouitaku.csv'),
    ('賃貸借', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-5-keiyakujisseki-chintaishaku.csv'),
    ('一般委託・役務', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-6-keiyakujisseki-ippanitakuekimu.csv'),
    ('物品（入札）', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-7-keiyakujisseki-buppin-nyusatu.csv'),
    ('物品（見積）', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-8-keiyakujisseki-buppin-mitumori.csv'),
    ('物品（一者）', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-9-keiyakujisseki-buppin-zuikei.csv'),
    ('単価契約（賃貸借・一般委託・役務）', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-10-keiyakujisseki-tanka-chintaishaku.csv'),
    ('単価契約（物品）', 'https://www.city.aomori.aomori.jp/_res/projects/default_project/_page_/001/006/215/7-11-keiyakujisseki-tanka-buppin.csv'),
    ('令和8年度・競争入札', 'https://yamaguchi-opendata.jp/ckan/dataset/41e0702f-57ef-4450-a207-d5d04aca6992/resource/d3fc7cfd-f2ff-4c76-a9b7-7303b118f5c1/download/20260924_r8__.csv'),
    ('令和8年度・随意契約', 'https://yamaguchi-opendata.jp/ckan/dataset/41e0702f-57ef-4450-a207-d5d04aca6992/resource/d23688f2-9035-4fd2-877e-cf1e6c59f93e/download/20260924_r8__.csv'),
    ('令和7年度・競争入札', 'https://yamaguchi-opendata.jp/ckan/dataset/41e0702f-57ef-4450-a207-d5d04aca6992/resource/c60908aa-9a8a-4dec-9da8-942ebef32702/download/20260924_r7__.csv'),
    ('令和7年度・随意契約', 'https://yamaguchi-opendata.jp/ckan/dataset/41e0702f-57ef-4450-a207-d5d04aca6992/resource/3dab2497-cde6-4b1c-a6c8-5bc6f58a020b/download/20260924_r7__.csv'),
    ('令和8年度・競争入札', 'https://yamaguchi-opendata.jp/ckan/dataset/f9694fa1-e556-4ff5-979a-dfdf9a68b489/resource/7557cc2d-890c-4019-aa57-b3392c93f964/download/20260917___.csv'),
    ('令和8年度・随意契約', 'https://yamaguchi-opendata.jp/ckan/dataset/f9694fa1-e556-4ff5-979a-dfdf9a68b489/resource/99167054-894a-4e81-bb62-9fa180bd7bb3/download/20260917___.csv'),
    ('令和7年度・競争入札', 'https://yamaguchi-opendata.jp/ckan/dataset/f9694fa1-e556-4ff5-979a-dfdf9a68b489/resource/e3b01552-37c7-4453-9111-c742324a17ac/download/20260416___.csv'),
    ('令和7年度・随意契約', 'https://yamaguchi-opendata.jp/ckan/dataset/f9694fa1-e556-4ff5-979a-dfdf9a68b489/resource/8764ed8e-9c6e-42bf-b234-941fdfa428c1/download/r820260518_r7__.csv'),
    ('令和5年度・土地', 'https://www.city.settsu.osaka.jp/material/files/group/75/R5kotei-toti.csv'),
    ('令和5年度・建物', 'https://www.city.settsu.osaka.jp/material/files/group/75/R5kotei-tatemono.csv'),
    ('令和5年度・工作物他', 'https://www.city.settsu.osaka.jp/material/files/group/75/R5kotei-kousakubutsu.csv'),
    ('令和4年度・土地', 'https://www.city.settsu.osaka.jp/material/files/group/75/R4kotei-toti.csv'),
    ('令和4年度・建物', 'https://www.city.settsu.osaka.jp/material/files/group/75/R4kotei-tatemono.csv'),
    ('令和4年度・工作物他', 'https://www.city.settsu.osaka.jp/material/files/group/75/R4kotei-kousakubutsu.csv'),
    ('令和6年3月31日時点', 'https://www.city.kainan.lg.jp/material/files/group/8/R6koteishisandaicho.csv'),
    ('令和5年3月31日時点', 'https://www.city.kainan.lg.jp/material/files/group/8/R050331.csv'),
    ('令和4年3月31日時点', 'https://www.city.kainan.lg.jp/material/files/group/8/koteisisanndaityou.csv'),
    ('令和3年3月31日時点', 'https://www.city.kainan.lg.jp/material/files/group/8/reiwa2nenndokoteishisandaicho.csv'),
    ('令和2年3月31日時点', 'https://www.city.kainan.lg.jp/material/files/group/8/koteishisandaicho.csv'),
]


def read_table(b):
    rows = [r for r in csv.reader(io.StringIO(decode(b[:3_000_000]), newline="")) if any(c.strip() for c in r)]
    hi = max(range(min(10, len(rows))), key=lambda i: sum(bool(c.strip()) for c in rows[i]))
    return rows[hi], rows[hi + 1:]


def jp_direct(f):
    rep = {}
    for name, u in JP_DIRECT:
        try:
            head, body = read_table(get(u, 60, 2))
            if len(body) < 3: rep[name] = "rows<3"; continue
            rng.shuffle(body); body = body[:300]
            keep = [j for j, h in enumerate(head) if h.strip() and not PERSONAL.search(str(h))]
            rows2 = [[r[j] if j < len(r) else "" for j in keep] for r in [head] + body]
            rep[name] = emit(f, "jp2:" + name, u, rows2[0], rows2[1:])
        except Exception as e:  # noqa: BLE001
            rep[name] = "error " + str(e)[:80]
    return rep


def jp_pages(f, per_page=8):
    """ページの中の .csv へのリンクをたどり、1ファイルを1表として出す。個人の連絡先の列は取らない。"""
    from urllib.parse import urljoin
    rep = {}
    for name, page in JP_PAGES:
        got = []
        try:
            html = decode(get(page, 60, 2))
            links = []
            for m in re.finditer(r'href=["\']([^"\']+?\.csv(?:\?[^"\']*)?)["\']', html, re.I):
                u = urljoin(page, m.group(1))
                if u not in links: links.append(u)
            for u in links[:per_page]:
                try:
                    rows = [r for r in csv.reader(io.StringIO(decode(get(u, 60, 2)[:3_000_000]), newline="")) if any(c.strip() for c in r)]
                    # 先頭の数行が題名のことがあるので、空でない欄がいちばん多い行を見出しとみなす（最初の10行から）
                    hi = max(range(min(10, len(rows))), key=lambda i: sum(bool(c.strip()) for c in rows[i]))
                    head, body = rows[hi], rows[hi + 1:]
                    if len(body) < 3: continue
                    rng.shuffle(body); body = body[:300]
                    keep = [j for j, h in enumerate(head) if h.strip() and not PERSONAL.search(str(h))]
                    rows2 = [[r[j] if j < len(r) else "" for j in keep] for r in [head] + body]
                    got.append(emit(f, f"jp:{name}", u, rows2[0], rows2[1:]))
                except Exception as e:  # noqa: BLE001
                    got.append("error " + str(e)[:60])
            rep[name] = f"csv {len(links)} 件中 {len(got)} 件: {got[:4]}"
        except Exception as e:  # noqa: BLE001
            rep[name] = "error " + str(e)[:120]
    return rep


def main():
    rep = {}
    if len(sys.argv) > 1 and sys.argv[1] == "jpdirect":
        with open(OUT.replace("real_corpus", "real_corpus_jp2"), "w", encoding="utf-8") as f:
            rep = jp_direct(f)
        print(json.dumps(rep, ensure_ascii=False)); return
    if len(sys.argv) > 1 and sys.argv[1] == "jp":
        with open(OUT.replace("real_corpus", "real_corpus_jp"), "w", encoding="utf-8") as f:
            rep = jp_pages(f)
        print(json.dumps(rep, ensure_ascii=False)); print(f"::notice title=本物の表（日本の調達）::{rep}")
        return
    if len(sys.argv) > 1 and sys.argv[1] == "direct":
        with open(OUT.replace("real_corpus", "real_corpus_direct"), "w", encoding="utf-8") as f:
            rep = direct(f)
        print(json.dumps(rep, ensure_ascii=False)); print(f"::notice title=本物の表（直接）::{rep}")
        return
    if len(sys.argv) > 1 and sys.argv[1] == "ckanbiz":
        from concurrent.futures import ThreadPoolExecutor
        def one(src):
            name, base, qs = src
            buf = io.StringIO()
            try:
                n = ckan_biz(buf, name, base, qs)
            except Exception as e:  # noqa: BLE001
                n = "error " + str(e)[:150]
            return name, n, buf.getvalue()
        with ThreadPoolExecutor(len(CKAN)) as ex:
            res = list(ex.map(one, CKAN))
        with open(OUT.replace("real_corpus", "real_corpus_biz2"), "w", encoding="utf-8") as f:
            for name, n, text in res:
                rep[name] = n; f.write(text)
        print(json.dumps(rep, ensure_ascii=False)); print(f"::notice title=本物の表（業務・CKAN）::{rep} {STATS}")
        return
    if len(sys.argv) > 1 and sys.argv[1] == "biz":
        with open(OUT.replace("real_corpus", "real_corpus_biz"), "w", encoding="utf-8") as f:
            rep["gittables_biz"] = gittables(f, biz=True)
        print(json.dumps(rep, ensure_ascii=False)); print(f"::notice title=本物の表（業務）::{rep}")
        return
    with open(OUT, "w", encoding="utf-8") as f:
        for name, fn in (("gittables", gittables), ("egov", egov)):
            try:
                rep[name] = fn(f)
            except Exception as e:  # noqa: BLE001
                rep[name] = "error " + str(e)[:150]
    print(json.dumps(rep, ensure_ascii=False))
    for k, v in rep.items():
        print(f"::notice title=本物の表 {k}::{v}")


if __name__ == "__main__":
    main()
