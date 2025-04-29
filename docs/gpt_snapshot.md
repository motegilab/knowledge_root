knowledge\_progress\_memo\_min
このファイルは「GPT／Cursor が読みやすく、人間もコピー＆ペーストで崩れない」ことを最重要視した進行メモ（ミニマル版）です。

***
## md 配置ガイド（Knowledge レイヤー基準）
すべてのドキュメントは以下に集約する： `/knowledge_root/docs/`
* knowledge\_progress\_memo.md # 通常版メモ（人間向け）
* knowledge\_progress\_memo\_min.md # ← このファイル（AI 貼付け用）
* knowledge\_local\_rag\_tasks.md # タスク一覧（人間向け）
* knowledge\_local\_rag\_tasks\_min.md # タスク一覧（AI 貼付け用）
* knowledge\_feature\_requests.md # 拡張アイデア集
* docs\_index.md # 全体目録
> **レイヤー構造**
> `knowledge`（根幹）
> └─ stulive / business / private

***
## memo\_category: progress\_status （現在地）
* progress\_01: クラウド構成整備完了（/knowledge\_root, PowerAutomate, .env.template） | 🟢
* progress\_02: GitHub 構成作成（knowledge\_grail repo, push待ち） | ⏳
* progress\_03: scripts テンプレ準備（ingest.py 等未作成） | ⏳
* progress\_04: デスクトップ PC 到着待ち → ローカル環境構築フェーズ | ⏳
## memo\_category: purpose\_and\_structure （目的と基盤設計）
* すべての知識は `/knowledge_root` に統一 | ✅
* Dropbox = 母艦、OneDrive = OCR 受信専用 | ✅
* md は `docs/` に集約し GPT／Cursor の主データソースに | ✅
* 命名規則 = 小文字 + アンダースコア、内容はコピペ再現性優先 | ✅
## memo\_category: final\_goals （最終目標）
* goal\_knowledge: AI と人が共有する永続ナレッジベースを確立 | ✅
* goal\_stulive: 台本生成・表情制御・演出の自動化 | ✅
* goal\_business: 社員管理・契約更新・在留カード処理の自動化 | ✅
* goal\_private: 思考・哲学ログを AI と共有し第二の脳として活用 | ✅

***
### 📜 Canvas 生成ルール（エリー用）
* **コピペで形が崩れない** プレーン MD を最優先。
* 表・罫線・複雑レイアウトは最小限に（AI／人間が相互編集しやすく）。
* md ファイルは常にこのルールを踏襲する。

***

*このファイルは Knowledge レイヤー以下のすべての md のフォーマット規範となります。*

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



distance\_recommend\_memo\_min
\---
\## 特許取得フェーズ
\- idea整理
\- 特許ドラフト作成
\- 仮出願 → PCT
\## PoC設計フェーズ
\- ファイル構成設計
\- モジュール設計
\- データサンプル設計
\## 実装進捗管理
\- env\_1: install numpy pandas
\- src\_1: create [distance.py](http://distance.py)
\- src\_2: create [stats.py](http://stats.py)
\- src\_3: create [bandit.py](http://bandit.py)
\- src\_4: create [recommend.py](http://recommend.py)
\- src\_5: create [app.py](http://app.py)
\- nb\_1: create sanity\_check.ipynb
\## 売り込みフェーズ
\- ピッチデッキ作成
\- 国内外VC打診
\- アクセラ応募
\---
このファイルもUTF-8厳守・コピペで崩れない形式