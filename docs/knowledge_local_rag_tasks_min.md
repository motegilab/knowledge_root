knowledge_local_rag_tasks_min

このファイルは「GPT／Cursor が読みやすく、人間もコピー＆ペーストで崩れない」形式で書かれたタスクボード（ミニマル版）です。

---
## md 配置ガイド
`/knowledge_root/docs/` 内に配置

- knowledge_progress_memo_min.md
- knowledge_local_rag_tasks_min.md  ← このファイル

---
## task_category: environment  （Python と必要ライブラリの導入）
- env_1: install python 3.11                        | ⏳
- env_2: pip install --upgrade pip                 | ⏳
- env_3: python -m venv knowledge-env              | ⏳
- env_4: pip install langchain chromadb watchdog python-dotenv openai | ⏳
- env_5: create .env and set OPENAI_API_KEY=xxxx   | ⏳

## task_category: directory_and_assets  （フォルダツリー作成）
- dir_1: create /knowledge_root                    | 🟢
- dir_2: create subfolders raw/, curated/, scripts/, etc | 🟢

## task_category: scripts  （基幹スクリプト配置）
- scr_1: copy ingest.py etc. to scripts/           | ⏳
- scr_2: check path inside each script             | ⏳
- scr_3: run python ingest.py once                 | ⏳

## task_category: automation  （watcher 常駐 & 夜間サマリ）
- auto_1: run watcher.py                           | ⏳
- auto_2: add nightly_summary.py to scheduler (03:00) | ⏳

## task_category: validation  （動作確認）
- val_1: chroma.sqlite is generated                | ⏳
- val_2: watcher reacts to new .md in raw/         | ⏳
- val_3: GPT response includes that new info       | ⏳

## task_category: cloud_setup  （クラウド整備）
- cloud_1: create /knowledge_root on Dropbox       | 🟢
- cloud_2: create subfolders raw/, scripts/, etc   | 🟢
- cloud_3: create /Company/OCR_scans/ on OneDrive  | 🟢
- cloud_4: PowerAutomate OCR→raw flow              | 🟢
- cloud_5: create .env.template in scripts/        | 🟢
- cloud_6: init GitHub knowledge-scripts repo      | ⏳
- cloud_7: push scripts/ and requirements.txt      | ⏳
- cloud_8: GitHub Actions (lint & venv check)      | ⏳
- cloud_9: share folder links if needed            | ⏳

---
### Canvas 生成ルール（エリー用）
- **コピー＆ペーストで崩れない** シンプル MD で書くこと。
- 表や複雑レイアウトを多用しない。
- ステータス記号（🟢 ⏳など）は行末に置き、タブや縦線は避ける。

---
*正式タスクボード（人間向け詳細版）は `knowledge_local_rag_tasks.md` を参照してください。*

