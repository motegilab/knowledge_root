knowledge_progress_memo_min

このファイルは「GPT／Cursor が読みやすく、人間もコピー＆ペーストで崩れない」形式で書かれた進行メモ（ミニマル版）です。

---
## md 配置ガイド（Knowledge レイヤー）
`/knowledge_root/docs/` に集約

- knowledge_progress_memo_min.md   ← 本ファイル
- knowledge_local_rag_tasks_min.md
- knowledge_feature_requests.md
- gpt_snapshot.md（progress + tasks を連結）

> レイヤー構造: knowledge（根幹） → stulive / business / private / distance_recommend

---
## memo_category: progress_status
- progress_01: クラウド構成整備完了（/knowledge_root, PowerAutomate, .env.template） | 🟢
- progress_02: GitHub Holy-Grail repo + Pages 公開完了                        | 🟢
- progress_03: scripts テンプレ準備（ingest.py等未作成）                      | ⏳
- progress_04: デスクトップPC到着待ち → ローカル環境構築フェーズ              | ⏳

## memo_category: purpose_and_structure
- 全知識は `/knowledge_root` に統一                             | ✅
- Dropbox = 母艦、OneDrive = OCR受信専用                       | ✅
- md は `docs/` に集約、GPT／Cursor の主データソース              | ✅
- 命名規則 = 小文字+アンダースコア、コピペ再現性優先              | ✅

## memo_category: final_goals
- goal_knowledge: 永続ナレッジベース確立                          | ✅
- goal_stulive: 台本生成・演出自動化                            | ✅
- goal_business: 社員管理・契約更新自動化                        | ✅
- goal_private: 思考ログを第二の脳へ                             | ✅

---
knowledge_local_rag_tasks_min

このファイルは RAG タスクボード（ミニマル版）です。

## task_category: environment
- env_1: install python 3.11                                       | 🟢
- env_2: pip install --upgrade pip                                | 🟢
- env_3: python -m venv knowledge-env                             | 🟢
- env_4: pip install langchain chromadb watchdog python-dotenv openai | 🟢
- env_5: create .env and set OPENAI_API_KEY                       | 🟢
- env_6: pip install -U langchain-community                        | 🟢
- env_7: pip install chromadb                                      | 🟢

## task_category: directory_and_assets
- dir_1: create /knowledge_root                                  | 🟢
- dir_2: create subfolders raw/, curated/, scripts/, etc          | 🟢
- dir_3: create obsidian_vault/                                   | 🟢

## task_category: scripts
- scr_1: copy ingest.py etc. to scripts/                         | 🟢
- scr_2: check path inside each script (add obsidian_vault path) | 🟢
- scr_3: run python ingest.py once                               | 🟢
- scr_4: write sync.py (auto-split & commit)                     | 🟢
- scr_5: add .cursor-tasks.yaml (run sync on save)               | ⏳
- scr_6: export folder tree to docs/folder_tree.md               | 🟢
- scr_7: add .gitignore to exclude .env and .venv/               | 🟢

## task_category: automation
- auto_1: run watcher.py                                          | ⏳
- auto_2: schedule nightly_summary.py at 03:00                    | ⏳

## task_category: validation
- val_1: chroma.sqlite is generated                               | 🟢
- val_2: watcher reacts to new .md in raw/                        | ⏳
- val_3: GPT response includes that new info                      | ⏳
- val_4: save→sync.py→GitHub push auto flow works                | ⏳

## task_category: cloud_setup
- cloud_1: create /knowledge_root on Dropbox                      | 🟢
- cloud_2: create subfolders raw/, scripts/, etc                  | 🟢
- cloud_3: create /Company/OCR_scans/ on OneDrive                 | 🟢
- cloud_4: PowerAutomate OCR→raw flow                             | 🟢
- cloud_5: create .env.template in scripts/                       | 🟢
- cloud_6: init GitHub knowledge-scripts repo                     | ⏳
- cloud_7: push scripts/ and requirements.txt                     | ⏳
- cloud_8: GitHub Actions (lint & venv check)                     | ⏳
- cloud_9: share folder links if needed                           | ⏳

## task_category: structure_management
- struct_1: regenerate docs/folder_tree.md after major moves      | ⏳
- struct_2: paste latest folder tree into Session Work            | ⏳

---
distance_recommend_memo_min

このファイルは距離感レコメンド特許＋PoC開発メモ（ミニマル版）です。

## 特許取得フェーズ
- idea整理
- 特許ドラフト作成
- 仮出願 → PCT

## PoC設計フェーズ
- ファイル構成設計
- モジュール設計
- データサンプル設計

## 実装進捗管理
- env_1: install numpy pandas
- src_1: create distance.py
- src_2: create stats.py
- src_3: create bandit.py
- src_4: create recommend.py
- src_5: create app.py
- nb_1: create sanity_check.ipynb

## 売り込みフェーズ
- ピッチデッキ作成
- 国内外VC打診
- アクセラ応募
testlltest

---
