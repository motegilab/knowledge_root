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