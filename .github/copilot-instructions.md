<!-- .github/copilot-instructions.md - guidance for AI coding agents -->
# Copilot instructions — projeto_final (Portuguese)

This repository is a compact data-collection + NLP pipeline centered on `projeto_final.py`. Keep changes minimal and focused: this project is a single-script ETL + analysis flow that writes outputs to `outputs/`.

Key points (big picture)
- **Primary flow:** `companies.csv` -> `load_and_preprocess_companies()` -> filter by `twitter_username` -> `fetch_tweets_for_users()` (uses X/Tweepy) -> `narrative_analysis()` (regex + spaCy) -> CSVs under `outputs/`.
- **Why**: the code prioritizes reproducible, incremental runs and logging; tweets are saved incrementally to `outputs/tweets_raw.csv` and logs go to `outputs/diario_bordo.log` to allow resumable collection and debugging.

Critical files to reference
- `projeto_final.py` — single-entrypoint script; contains configuration, data-loading, tweet collection, and the NLP step.
- `geral.ipynb` — interactive notebook version; good for exploratory edits and verifying results before updating the script.
- `outputs/README_execucao.txt` — project-specific run instructions and dependency list.
- `companies.csv` — input dataset (Kaggle); many functions expect columns like `name`, `twitter_username`, `funding_total_usd`, `description`.

Dev & run workflow (explicit commands)
- Install dependencies (from `outputs/README_execucao.txt`):
```bash
pip install pandas numpy tqdm python-dotenv tweepy spacy nltk
python -m spacy download en_core_web_sm
```
- Set X API bearer token (example PowerShell):
```powershell
setx X_BEARER_TOKEN "<YOUR_TOKEN>"
# Restart terminal/VSCode after setting env var
```
- Run the script:
```bash
python projeto_final.py
```

Important runtime/config conventions
- Environment variable name: `X_BEARER_TOKEN` (used by `get_twitter_client()`); do not change the name unless updating the client code accordingly.
- Outputs directory: `OUTPUT_DIR` constant is `outputs` — all produced CSVs and `diario_bordo.log` live there.
- Incremental saves: `fetch_tweets_for_users()` writes `tweets_raw.csv` incrementally during collection. Preserve this behavior when refactoring to avoid losing partial results.
- spaCy model: code expects `en_core_web_sm`. If you add other models, update `narrative_analysis()` error message and downloads.

Patterns & conventions in this repo
- Language: variables, comments and messages are Portuguese. Keep log messages consistent (Portuguese) when adding new logging statements.
- Data handling: CSV reads attempt `utf-8` and fall back to `latin1`. Use `pd.to_numeric(..., errors='coerce')` pattern when sanitizing numeric funding fields.
- Rate limits: `fetch_tweets_for_users()` catches `tweepy.TooManyRequests` and sleeps for 60s; preserve the try/except structure rather than removing it.
- Progress UI: loops use `tqdm` for status; preserve `total=` and `desc=` parameters when modifying loops.

What to avoid
- Do not hard-code secrets or API keys into repository files. Use `X_BEARER_TOKEN` (env var) as in the current code.
- Avoid removing incremental writes to CSV/logs — they're used for safety during long API collection runs.

Examples of common edits and how to validate
- If you change tweet collection (pagination or fields): run `python projeto_final.py` with `n_startups=2` and `tweets_per_startup=5` to validate quickly.
- If you refactor `narrative_analysis()` test locally by running `geral.ipynb` on a small slice (e.g., `df_companies.head(50)`), then port changes back to the script.

References (paths)
- Script: [projeto_final.py](projeto_final.py)
- Notebook: [geral.ipynb](geral.ipynb)
- Run notes: [outputs/README_execucao.txt](outputs/README_execucao.txt)
- Example outputs: [outputs/diario_bordo.log](outputs/diario_bordo.log) (created at runtime)

If anything in this file is unclear or you want more detail (e.g., expected CSV schemas, sample rows, or specific tests), ask and I will expand the instructions or add small validation scripts.
