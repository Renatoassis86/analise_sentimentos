# 📖 Como Executar o Projeto Neural Marketing Intelligence

Siga estas instruções para rodar o pipeline de **Startup Signal Intelligence** no seu ambiente local ou no Google Colab.

---

### 1. 🚀 Como Abrir no Google Colab
Para rodar online sem instalar nada:
1. Acesse o repositório no GitHub.
2. No notebook desejado, substitua `github.com` por `colab.research.google.com/github` na URL.
   - [Notebook 01 - Regex & spaCy](https://colab.research.google.com/github/Renatoassis86/analise_sentimentos/blob/main/notebooks/01_etapa1_regex_spacy.ipynb)
   - [Notebook 02 - APIs & Scraping](https://colab.research.google.com/github/Renatoassis86/analise_sentimentos/blob/main/notebooks/02_etapa2_coleta_apis.ipynb)
   - [Notebook 03 - PLN & Sentimentos](https://colab.research.google.com/github/Renatoassis86/analise_sentimentos/blob/main/notebooks/03_etapa3_pln_sentimentos.ipynb)

### 2. 🚦 Ordem de Execução
Para garantir que as variáveis e o corpus sejam consistentes:
1. **01_etapa1_regex_spacy.ipynb**: Base de limpeza e normalização.
2. **02_etapa2_coleta_apis.ipynb**: Adquire os dados e constrói o corpus.
3. **03_etapa3_pln_sentimentos.ipynb**: Motor de inteligência final e métricas.

### 🌐 3. Conexão com Internet
As seguintes células exigem conexão ativa:
- Downloads do modelo `pt_core_news_sm`.
- Requisições à `GitHub API`, `BrasilAPI` e `Quotes-to-Scrape`.
- Download do modelo Transformer (`cardiffnlp/twitter-roberta-base-sentiment-latest`).

### ⚙️ 4. Fallback (Contingência)
Caso a API do GitHub ou BrasilAPI apresente erro de *Rate Limit* ou esteja fora do ar:
- O sistema detecta a falha automaticamente.
- **Solução:** O script utilizará o **Corpus Local** pré-embutido nos arquivos `src/limpeza.py` e `src/pln_pipeline.py` para garantir que a demonstração continue funcionando perfeitamente.

### ⏳ 5. Tempo Estimado de Execução
- **Etapa 1:** ~3 minutos (Instalação + Limpeza).
- **Etapa 2:** ~5 minutos (Requests + Scraping + Plots Plotly).
- **Etapa 3:** ~8 minutos (Download do BERT + Treinamento Baseline + Health Index).

---
**Dica:** Siga o Diário de Bordo em `docs/diario_de_bordo.md` para entender as escolhas técnicas feitas durante o desenvolvimento.
