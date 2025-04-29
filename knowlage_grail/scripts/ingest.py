#!/usr/bin/env python
"""
ingest.py – 指定フォルダ内の .md ファイルを読み込み、
            Chroma DB (local sqlite) にベクトル登録する最小版
"""

from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os, glob

# 1. .env 読み込み
load_dotenv()

# 2. 走査対象ディレクトリ
ROOT = Path(__file__).resolve().parents[1]          # knowledge_root/scripts/knowlage_grail/scripts/..
TARGETS = [
    ROOT.parent / "raw",
    ROOT.parent / "curated",
    ROOT.parent / "obsidian_vault",
]

# 3. Markdown ファイル取得
md_files = []
for folder in TARGETS:
    md_files += glob.glob(str(folder / "**" / "*.md"), recursive=True)

print(f"Found {len(md_files)} markdown files.")

# 4. Embeddings & VectorStore
embeddings = OpenAIEmbeddings()   # OPENAI_API_KEY が .env から読まれる
db_path = ROOT.parent / "vectors" / "chroma"
db_path.mkdir(parents=True, exist_ok=True)

vectordb = Chroma(
    collection_name="knowledge",
    embedding_function=embeddings,
    persist_directory=str(db_path)
)

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# 5. 1ファイルずつ取り込み
for fp in md_files:
    text = Path(fp).read_text(encoding="utf-8", errors="ignore")
    docs = splitter.create_documents([text], metadatas=[{"source": fp}])
    vectordb.add_documents(docs)

vectordb.persist()
print("✅ ingest complete!")
