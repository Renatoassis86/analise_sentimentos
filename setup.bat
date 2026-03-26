@echo off
echo 🚀 ARKOS MI — Setup do ambiente (Windows)
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
echo ✅ Ambiente configurado!
pause
