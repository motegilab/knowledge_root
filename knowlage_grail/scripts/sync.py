#!/usr/bin/env python
"""
sync.py – Holy-Grail管理用
複数の _memo_min.md を読み込み連結し、
gpt_snapshot.md を生成してGitHubへpushする
"""

from pathlib import Path
import subprocess
import sys

def run_command(command):
    """コマンド実行して出力もリアルタイム表示"""
    print(f"▶️ 実行: {' '.join(command)}")
    sys.stdout.flush()
    result = subprocess.run(command, check=True, text=True)
    return result

def main():
    # 1. パス設定
    ROOT = Path(__file__).resolve().parents[1]  # /knowlage_grail/
    DOCS = ROOT / "docs"

    # 2. 連結対象ファイル
    files_to_concat = [
        DOCS / "knowledge_progress_memo_min.md",
        DOCS / "knowledge_local_rag_tasks_min.md",
        DOCS / "distance_recommend_memo_min.md",  # ←これを絶対忘れない！
    ]

    # 3. ファイル読み込み・連結
    snapshot_text = ""
    for f in files_to_concat:
        if not f.exists():
            sys.exit(f"❌ ファイルが見つかりません: {f}")
        snapshot_text += f.read_text(encoding="utf-8") + "\n\n"

    # 4. snapshotを書き出す
    output_file = DOCS / "gpt_snapshot.md"
    output_file.write_text(snapshot_text.strip(), encoding="utf-8")
    print(f"✅ {output_file.name} を再生成しました")
    sys.stdout.flush()

    # 5. Git add → commit → push
    try:
        run_command(["git", "add", "docs"])
        run_command(["git", "commit", "-m", "update gpt_snapshot"])
    except subprocess.CalledProcessError:
        print("⚠️  コミットする変更がありません（スキップ）")
    
    run_command(["git", "push"])
    print("🚀 GitHubへpush完了！")
    print("🎉 全工程完了！お疲れ様！")

if __name__ == "__main__":
    main()
