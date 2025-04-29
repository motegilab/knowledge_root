stulive_local_rag_tasks_min

このファイルは「GPTにそのまま貼っても情報が失われないこと」を目的とした、完全コピー＆ペースト対応バージョンのタスクボードです。

md配置ガイド

すべてのドキュメントは以下に置く： /knowledge_root/docs/

- stulive_progress_memo.md       # 引き継ぎと目的記録
- stulive_local_rag_tasks.md     # 通常版タスクボード（人間用）
- stulive_local_rag_tasks_min.md # ← このファイル（GPT貼付け用）
- stulive_feature_requests.md    # 拡張アイデア集
- docs_index.md                  # 全体目録

task_category: environment  # Python と必要ライブラリの導入

- e_1: install python 3.11                        | ⏳
- e_2: pip install --upgrade pip                 | ⏳
- e_3: python -m venv stulive-env                | ⏳
- e_4: pip install langchain chromadb watchdog python-dotenv openai | ⏳
- e_5: create .env and set OPENAI_API_KEY=xxxx   | ⏳

task_category: directory_and_assets  # /knowledge_root フォルダツリーとテストファイル作成

- d_1: create /knowledge_root                    | 🟢
- d_2: create subfolders raw/, curated/, scripts/, etc | 🟢

task_category: scripts  # ingest / watcher / nightly_summary を配置して実行可能に

- s_1: copy ingest.py etc. to scripts/           | ⏳
- s_2: check path inside each script             | ⏳
- s_3: run python ingest.py once                 | ⏳

task_category: automation  # watcher 常駐 & 夜間サマリを自動化

- a_1: run watcher.py                            | ⏳
- a_2: add nightly_summary.py to scheduler (03:00) | ⏳

task_category: validation  # 一連の動作確認

- v_1: chroma.sqlite is generated                | ⏳
- v_2: watcher reacts to new .md in raw/         | ⏳
- v_3: GPT response includes that new info       | ⏳

task_category: cloud_setup

- cld_1: create /knowledge_root on Dropbox       | 🟢
- cld_2: create subfolders raw/, scripts/, etc   | 🟢
- cld_3: create /Company/OCR_scans/ on OneDrive  | 🟢
- cld_4: PowerAutomate OCR→raw flow              | 🟢
- cld_5: create .env.template in scripts/        | 🟢
- cld_6: init GitHub knowledge-scripts repo      | ⏳
- cld_7: push scripts/ and requirements.txt      | ⏳
- cld_8: GitHub Actions (lint & venv check)      | ⏳
- cld_9: share folder links if needed            | ⏳

これはGPTでの引き継ぎ・再現性を最大限高めるために作られた「コピー＆貼付け前提タスク形式」です。 ステータス付き・MECE構造のまま構成されており、GPTが読み取っても完璧にタスク管理できます。 正式タスクボードは stulive_local_rag_tasks.md を参照してください。

