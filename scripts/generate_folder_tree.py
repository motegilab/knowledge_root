#!/usr/bin/env python
"""
generate_folder_tree.py
knowledge_root 配下のフォルダ階層（深さ3まで）と.mdファイルを
docs/folder_tree.md に UTF-8(BOMなし) で書き出す
"""

import os
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]          # /knowledge_root
DOCS = ROOT / "docs"
OUT  = DOCS / "folder_tree.md"
LOG  = DOCS / "folder_tree.log"
MAX_DEPTH = 3

exclude = {'.git', '.venv', 'chroma'}               # 不要な巨大 or 内部フォルダ

base_depth = ROOT.parts.__len__()

# docsディレクトリが存在しない場合は作成
DOCS.mkdir(exist_ok=True)

# ログファイルに実行時刻を記録
with LOG.open('a', encoding='utf-8') as log:
    log.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] フォルダツリー更新開始\n")

with OUT.open('w', encoding='utf-8') as f:
    f.write(f"# フォルダ構成（depth≤3）とMarkdownファイル\n\n")
    f.write(f"最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    for root, dirs, files in os.walk(ROOT):
        path = Path(root)
        rel_depth = path.parts.__len__() - base_depth
        
        # 除外フォルダのスキップ
        if any(part in exclude for part in path.parts):
            continue
            
        # フォルダの深さチェック
        if rel_depth < MAX_DEPTH:
            indent = '    ' * rel_depth
            # フォルダ名を出力
            f.write(f"{indent}- 📂 {path.name}/\n")
            
            # .mdファイルを出力（同じインデントレベル+2spaces）
            md_files = [f for f in files if f.endswith('.md')]
            if md_files:
                for md_file in sorted(md_files):
                    f.write(f"{indent}  - 📄 {md_file}\n")

# ログファイルに完了を記録
with LOG.open('a', encoding='utf-8') as log:
    log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] フォルダツリー更新完了\n")

print("✅ docs/folder_tree.md 更新完了")
