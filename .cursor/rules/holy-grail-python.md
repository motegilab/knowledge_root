# Cursor Rules – Holy-Grail (Python + Markdown)

- This repository is a **Python 3.11 project** that orchestrates RAG scripts (`ingest.py`, `sync.py`, `watcher.py`).
- Follow **PEP 8** (black-style) and add type hints where reasonable.
- Treat every folder under `obsidian_vault/` as **content-only**; never modify those files from code.
- Ignore heavy or generated directories: `.venv/`, `.git/`, `vectors/chroma/`.
- When adding scripts, put them in `knowlage_grail/scripts/` and update `__init__.py` if needed.
- Use `dotenv` (`.env`) for secrets; **never** hard-code API keys.
- Prefer **Pathlib** over os.path, and `typer`/`argparse` for CLIs.
- Tests (if any) live in `knowlage_grail/tests/` with pytest.
