knowledge\_local\_rag\_tasks\_min
このファイルは「GPT／Cursor が読みやすく、人間もコピー＆ペーストで崩れない」形式で書かれたタスクボード（ミニマル版）です。

***
## md 配置ガイド
`/knowledge_root/docs/` 内に配置
* knowledge\_progress\_memo\_min.md
* knowledge\_local\_rag\_tasks\_min.md ← このファイル

***
## task\_category: environment （Python と必要ライブラリの導入）
* env\_1: install python 3.11 | ⏳
* env\_2: pip install --upgrade pip | ⏳
* env\_3: python -m venv knowledge-env | ⏳
* env\_4: pip install langchain chromadb watchdog python-dotenv openai | ⏳
* env\_5: create .env and set OPENAI\_API\_KEY=xxxx | ⏳
## task\_category: directory\_and\_assets （フォルダツリー作成）
* dir\_1: create /knowledge\_root | 🟢
* dir\_2: create subfolders raw/, curated/, scripts/, etc | 🟢
## task\_category: scripts （基幹スクリプト配置）
* scr\_1: copy ingest.py etc. to scripts/ | ⏳
* scr\_2: check path inside each script | ⏳
* scr\_3: run python ingest.py once | ⏳
## task\_category: automation （watcher 常駐 & 夜間サマリ）
* auto\_1: run watcher.py | ⏳
* auto\_2: add nightly\_summary.py to scheduler (03:00) | ⏳
## task\_category: validation （動作確認）
* val\_1: chroma.sqlite is generated | ⏳
* val\_2: watcher reacts to new .md in raw/ | ⏳
* val\_3: GPT response includes that new info | ⏳
## task\_category: cloud\_setup （クラウド整備）
* cloud\_1: create /knowledge\_root on Dropbox | 🟢
* cloud\_2: create subfolders raw/, scripts/, etc | 🟢
* cloud\_3: create /Company/OCR\_scans/ on OneDrive | 🟢
* cloud\_4: PowerAutomate OCR→raw flow | 🟢
* cloud\_5: create .env.template in scripts/ | 🟢
* cloud\_6: init GitHub knowledge-scripts repo | 🟢
* cloud\_7: push scripts/ and requirements.txt | ⏳
* cloud\_8: GitHub Actions (lint & venv check) | ⏳
* cloud\_9: share folder links if needed | ⏳

***
### Canvas 生成ルール（エリー用）
* **コピー＆ペーストで崩れない** シンプル MD で書くこと。
* 表や複雑レイアウトを多用しない。
* ステータス記号（🟢 ⏳など）は行末に置き、タブや縦線は避ける。

***

*正式タスクボード（人間向け詳細版）は* `knowledge_local_rag_tasks.md` *を参照してください。*
