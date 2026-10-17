"""Kaggle（無料の GPU）で動く入口。データセット jitsuris-data の中身（研究用のコードと公開データのラベル。未見セットは入れない）を
作業場所に広げて、args.txt の引数で学習・試験を行う。結果（集計の md とモデル）は /kaggle/working に残し、GitHub 側が取りに来る。"""
import glob, os, shutil, subprocess, sys, tarfile
W = "/kaggle/working/src"
EXPECT = ""  # GitHub 側が今回のモデルの置き場所を書き込む
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
args = open("kaggle/args.txt").read().split()
MODE = args.pop(0) if args and args[0] == "embed" else ""
if args[0].startswith("hfmodel/") and not os.path.exists(os.path.join(args[0], "config.json")):
    c = [p for p in glob.glob("/kaggle/input/**/config.json", recursive=True) if os.path.basename(args[0]) in p]
    diag.write("model not at " + args[0] + "; found " + str(c) + "\n")
    if c: args[0] = os.path.dirname(c[0])
if EXPECT and args[0] != EXPECT:
    diag.write("古い版のデータセット：" + args[0] + " ≠ " + EXPECT + "\n"); diag.close(); sys.exit(3)
diag.write("model: " + args[0] + " exists=" + str(os.path.exists(os.path.join(args[0], "config.json"))) + "\n")
try:
    import torch; diag.write("cuda: " + str(torch.cuda.is_available()) + " " + (torch.cuda.get_device_name(0) if torch.cuda.is_available() else "") + "\n")
except Exception as e: diag.write("torch error " + repr(e) + "\n")
diag.flush()
os.environ["HF_HUB_OFFLINE"] = "1"
env = dict(os.environ)
for a in list(args):
    if a.startswith("FT_LR="): env["FT_LR"] = a[6:]; args.remove(a)
script = "llm_embed_exp.py" if MODE == "embed" else "finetune_exp.py"
r = subprocess.run([sys.executable, script, *args], env=env)
os.makedirs("/kaggle/working/out", exist_ok=True)
for f in ("FINETUNE_RESULTS.md",):
    if os.path.exists(f): shutil.copy(f, "/kaggle/working/out/" + f)
if os.path.isdir("ft_out"): shutil.move("ft_out", "/kaggle/working/out/ft_out")
shutil.rmtree(W, ignore_errors=True)
sys.exit(r.returncode)
