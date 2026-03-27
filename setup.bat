@echo off
echo 🚀 Neural Marketing Intelligence — Setup do ambiente (Windows)
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
echo ✅ Ambiente configurado!
pause
