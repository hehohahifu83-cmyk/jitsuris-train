"""1 回だけの予測の門（2026-11-26 Claude、Codex の点検 1。g4b-predict.yml が使う）。
  check <依頼ファイル> <依頼の文> <予測のディレクトリ>   → 「proceed」か「skip」を出す（止めるべきときは終了コード 1）
  start <依頼ファイル> <依頼の文> <予測のディレクトリ>   → 依頼ファイルを「started <依頼の文の名前>」に、STARTED の印を書く（予測の前に main へ push する）
決まり：
  - 依頼の文が「run <名前> once」でなければ skip（何もしない）。
  - 予測のディレクトリに予測（pred_*.json）か STARTED の印があれば止める（開始済み・失敗済みの依頼は自動で再実行しない）。
  - 依頼ファイルが「started …」のまま（前の実行が途中で失敗した）なら skip（依頼の文と違うので）。やり直すときは、人が artifact を回収し、理由を事前記録に書いてから印を外す。
"""
import sys
from datetime import datetime, timezone
from pathlib import Path


def check(req, want, pred_dir):
    first = Path(req).read_text(encoding="utf-8").splitlines()[:1]
    if first != [want]:
        return "skip"
    d = Path(pred_dir)
    if (d / "STARTED").exists() or any(d.glob("pred_*.json")):
        raise SystemExit("予測がもうある・開始済み（1 回だけ）。artifact を回収し、理由を書いてから印を外す")
    return "proceed"


def start(req, want, pred_dir):
    if check(req, want, pred_dir) != "proceed":
        raise SystemExit("始められない")
    d = Path(pred_dir)
    d.mkdir(parents=True, exist_ok=True)
    (d / "STARTED").write_text(f"{want}\nstarted_utc {datetime.now(timezone.utc).isoformat(timespec='seconds')}\n", encoding="utf-8")
    Path(req).write_text("started " + want.split()[1] + "\n", encoding="utf-8")


if __name__ == "__main__":
    cmd, req, want, pred = sys.argv[1:5]
    if cmd == "check":
        print(check(req, want, pred))
    elif cmd == "start":
        start(req, want, pred)
        print("started")
    else:
        raise SystemExit("check か start")
