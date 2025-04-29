#!/usr/bin/env python
"""
sync.py
変更を自動でコミットしてプッシュするスクリプト
"""

import subprocess
from datetime import datetime
from pathlib import Path

def run_command(command):
    """コマンドを実行して結果を返す"""
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"エラーが発生しました: {e.stderr}")
        return None

def main():
    # 現在のディレクトリを取得
    current_dir = Path(__file__).resolve().parent.parent
    
    # Gitコマンドを実行
    commands = [
        "git add .",
        f'git commit -m "auto commit: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"',
        "git push"
    ]
    
    print("🔄 変更を同期中...")
    for cmd in commands:
        print(f"実行: {cmd}")
        result = run_command(cmd)
        if result:
            print(result)
    
    print("✅ 同期完了")

if __name__ == "__main__":
    main()
