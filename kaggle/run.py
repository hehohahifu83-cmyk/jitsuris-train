"""Kaggle（無料の GPU）で動く入口。データセット jitsuris-data の中身（研究用のコードと公開データのラベル。未見セットは入れない）を
作業場所に広げて、args.txt の引数で学習・試験を行う。結果（集計の md とモデル）は /kaggle/working に残し、GitHub 側が取りに来る。"""
import glob, os, shutil, subprocess, sys, tarfile
W = "/kaggle/working/src"
EXPECT = ""  # GitHub 側が今回のモデルの置き場所を書き込む
EXPECT_NONCE = ""  # GitHub 側が今回だけの印を書き込む（同じモデルの前回の版を今回の版と取り違えないため）
hit = glob.glob("/kaggle/input/**/finetune_exp.py", recursive=True)
if hit:
    shutil.copytree(os.path.dirname(hit[0]), W, dirs_exist_ok=True)
else:
    tars = glob.glob("/kaggle/input/**/bundle.tar*", recursive=True)
    assert tars, "データセットが見つからない: " + str(glob.glob("/kaggle/input/**", recursive=True)[:50])
    os.makedirs(W, exist_ok=True); tarfile.open(tars[0]).extractall(W)
os.chdir(W)
os.makedirs("/kaggle/working/out", exist_ok=True)
diag = open("/kaggle/working/out/diag.txt", "w")
diag.write("input: " + " ".join(sorted(set(os.path.dirname(p) for p in glob.glob("/kaggle/input/**/*", recursive=True)))[:40]) + "\n")
for c in glob.glob("/kaggle/input/**/config.json", recursive=True): diag.write("config: " + c + "\n")
assert not glob.glob("blind_set*"), "未見セットが入っている"
subprocess.run("nvidia-smi --query-gpu=name,memory.total --format=csv", shell=True)
got_nonce = [os.path.basename(p) for p in glob.glob("kaggle/nonce-*.txt")]
if EXPECT_NONCE and ("nonce-%s.txt" % EXPECT_NONCE) not in got_nonce:
    diag.write("古い版のデータセット（印が違う）：今回 %s／中身 %s\n" % (EXPECT_NONCE, got_nonce)); diag.close(); sys.exit(3)
diag.write("印: %s\n" % got_nonce)
args = open("kaggle/args.txt").read().split()
MODE = args.pop(0) if args and args[0] in ("embed", "probe") else ""
if args[0].startswith("hfmodel/") and not os.path.exists(os.path.join(args[0], "config.json")):
    c = [p for p in glob.glob("/kaggle/input/**/config.json", recursive=True) if os.path.basename(args[0]) in p]
    diag.write("model not at " + args[0] + "; found " + str(c) + "\n")
    if c: args[0] = os.path.dirname(c[0])
if EXPECT and args[0] != EXPECT:
    diag.write("古い版のデータセット：" + args[0] + " ≠ " + EXPECT + "\n"); diag.close(); sys.exit(3)
diag.write("model: " + args[0] + " exists=" + str(os.path.exists(os.path.join(args[0], "config.json"))) + "\n")
n_gpu = 0
try:
    import torch; n_gpu = torch.cuda.device_count()   # 名前の取得（get_device_name）は親の側に GPU の場所を取ってしまうので使わない
    names = subprocess.run("nvidia-smi --query-gpu=name,memory.total --format=csv,noheader", shell=True, capture_output=True, text=True).stdout.strip().replace("\n", " / ")
    diag.write("cuda: " + str(torch.cuda.is_available()) + " devices=" + str(n_gpu) + " " + names + "\n")
except Exception as e: diag.write("torch error " + repr(e) + "\n")
diag.flush()
os.environ["HF_HUB_OFFLINE"] = "1"
sys.path.insert(0, W)
import jobs as J   # 「++」で区切ると GPU 1 枚につき 1 つの仕事を同時に流す。FT_ で始まる語はすべて環境変数として渡す
specs = J.split_jobs(args)
kept = J.keep_cpu_lab_checkpoint(specs)
if kept: diag.write("CPU lab checkpoint export: retained first e5-base job only; training settings unchanged\n")   # J.MAX_JOBS 個まで。同時に流すのは GPU の枚数まで、残りは空いた順に
diag.write("仕事の数: " + str(len(specs)) + " " + str(specs) + "\n"); diag.flush()
script = {"embed": "llm_embed_exp.py", "probe": "speed_probe.py"}.get(MODE, "finetune_exp.py")
codes = J.run_jobs(specs, script, dict(os.environ), W, n_gpu)
OUT = "/kaggle/working/out"
os.makedirs(OUT, exist_ok=True)
def copy_reports(src, dst):
    os.makedirs(dst, exist_ok=True)
    for pat in ("errors_*.json", "probs_*.json", "probe_*.json"):
        for f in glob.glob(os.path.join(src, pat)): shutil.copy(f, dst)
if len(specs) == 1:
    if os.path.exists("FINETUNE_RESULTS.md"): shutil.copy("FINETUNE_RESULTS.md", OUT + "/FINETUNE_RESULTS.md")
    copy_reports(".", OUT + "/report")
    if os.path.isdir("ft_out"): shutil.move("ft_out", OUT + "/ft_out")
else:   # 仕事ごとの出力は jobN の中。集計は 1 つにまとめ、確率と誤りの一覧は jobN ごとに残す（重いモデルの保存は省く）
    agg = "# 学習済みモデルの微調整（集計）\n"
    for i, spec in enumerate(specs, 1):
        wd = os.path.join(W, "job%d" % i)
        f = os.path.join(wd, "FINETUNE_RESULTS.md")
        label = J.describe(specs, i - 1)
        if os.path.exists(f):
            body = open(f, encoding="utf-8").read().split("\n", 1)[1]
            agg += body.replace("### ", "### 仕事%d（%s）" % (i, label), 1)
        else:
            agg += "\n### 仕事%d（%s）\n結果なし（終了コード %s）\n" % (i, label, codes[i - 1])
        copy_reports(wd, OUT + "/job%d" % i)
        if J.keeps_model(spec) and os.path.isdir(os.path.join(wd, "ft_out")):   # FT_KEEP=1 の仕事のモデルだけ持ち帰る（ブラウザ用の書き出しに使う）
            shutil.move(os.path.join(wd, "ft_out"), OUT + "/ft_out_job%d" % i)
    open(OUT + "/FINETUNE_RESULTS.md", "w", encoding="utf-8").write(agg)
shutil.rmtree(W, ignore_errors=True)
sys.exit(max(codes))
