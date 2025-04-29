#!/usr/bin/env python
"""
generate_folder_tree.py
knowledge_root 配下のフォルダ階層（深さ3まで）を
knowlage_grail/docs/folder_tree.md に UTF-8(BOMなし) で書き出す
"""

import os
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]          # /knowledge_root
DOCS = ROOT / "knowlage_grail" / "docs"
OUT  = DOCS / "folder_tree.md"
LOG  = DOCS / "folder_tree.log"
MAX_DEPTH = 3

exclude = {'.git', '.venv', 'chroma'}               # 不要な巨大 or 内部フォルダ

base_depth = ROOT.parts.__len__()

# ログファイルに実行時刻を記録
with LOG.open('a', encoding='utf-8') as log:
    log.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] フォルダツリー更新開始\n")

with OUT.open('w', encoding='utf-8') as f:
    f.write(f"# フォルダ構成（depth≤3）\n\n")
    f.write(f"最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    for root, dirs, _ in os.walk(ROOT):
        rel_depth = Path(root).parts.__len__() - base_depth
        if rel_depth < MAX_DEPTH:
            if any(part in exclude for part in Path(root).parts):
                continue
            indent = '    ' * rel_depth
            f.write(f"{indent}- {Path(root).name}/\n")

# ログファイルに完了を記録
with LOG.open('a', encoding='utf-8') as log:
    log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] フォルダツリー更新完了\n")

print("✅ docs/folder_tree.md 更新完了")
