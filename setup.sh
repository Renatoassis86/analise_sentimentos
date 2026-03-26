#!/bin/bash
echo "🚀 ARKOS MI — Setup do ambiente"
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
echo "✅ Ambiente configurado!"
