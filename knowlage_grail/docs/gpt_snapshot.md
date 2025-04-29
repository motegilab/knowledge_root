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