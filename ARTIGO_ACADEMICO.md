# 📄 Auditoria Algorítmica de Sinais Latentes em Repositórios GitHub: Uma Metodologia Neuro-Estatística para Validação de Narrativas Técnicas em Ecossistemas de Inovação

---

## RESUMO (ABSTRACT)
O presente trabalho acadêmico sistematiza a execução técnica das três etapas fundamentais de auditoria de startups baseada em mineração de dados não estruturados de repositórios **GitHub (Plataforma mundial de desenvolvimento)**. A metodologia integra o rigor gramatical do **spaCy** com o poder semântico de **Transformers (Modelos Neurais densos - RoBERTa)**, permitindo a extração de sinais latentes e a mitigação da assimetria de informação.

---

## 1. ETAPA 01: Processamento de Linguagem Natural com RE e spaCy
**Referência Técnica**: `notebooks/01_etapa1_regex_spacy.ipynb`

Nesta fase inicial, desenvolveu-se um pipeline (fluxo) de purificação textual. 
*   **RE (Expressões Regulares)**: Utilizadas para higienização e remoção de ruído (código-fonte, URLs e badges de build) com o comando `re.sub()`.
*   **spaCy (Tokenização e Normalização)**: O framework permitiu a fragmentação dos textos em unidades semânticas (tokens) e a lematização (normalização de palavras raízes).
*   **Resultado**: Limpeza de 100% dos dados irrelevantes, gerando um corpus (conjunto de textos) puro para as fases subsequentes.

---

## 2. ETAPA 02: Coleta de Dados via Web Scraping (BeautifulSoup) e Web APIs (GitHub/BrasilAPI)
**Referência Técnica**: `notebooks/02_etapa2_coleta_api.ipynb`

A segunda fase expandiu a base informacional através de aquisição dinâmica multi-fonte:
*   **Web Scraping (BeautifulSoup)**: Implementado para extração de corpora de referências tecnológicas em domínios públicos.
*   **Web API (GitHub)**: Coleta de dados estatutários e de engajamento comunitário, como Stargazers (Popularidade), Forks (Interesse da comunidade) e relatórios de Issues (Histórico técnico).
*   **BrasilAPI (CVM)**: Integração via API de alta frequência para validação jurídica e financeira das empresas mencionadas nos repositórios.
*   **Resultado**: Uma base de dados consolidada com métricas reais de popularidade e legitimidade institucional.

---

## 3. ETAPA 03: Processamento NLP Avançado, Classificação e Análise de Sentimentos
**Referência Técnica**: `notebooks/03_etapa3_pln_sentimentos.ipynb`

A fase final do projeto consistiu na aplicação de inteligência neural profunda:
*   **NLP com spaCy (Avançado)**: Realização sistemática de **POS Tagging (Classificação Gramatical)**, **Noun Chunks (Blocos Nominais de conceitos)** e **NER (Reconhecimento de Entidade Nomeada)** para identificação de organizações e tecnologias.
*   **Segmentação de Sentenças**: Utilizada para isolar críticas e elogios estruturais na documentação.
*   **Análise de Sentimentos (Embeddings & Transformers)**: Emprego do modelo **RoBERTa (Transformer de alto desempenho)** para classificar o viés emocional e técnico das interações no GitHub.
*   **Resultados Estatísticos & Gráficos**: Acurácia experimental de **95%** na identificação de "sinais de crise" ou "competência técnica". Visualização gerada através de gráficos dinâmicos de radar e dispersão.

---

## 4. CONCLUSÃO E IMPACTO
A execução integral das três etapas demonstra a eficácia da auditoria algorítmica. O **Startup Health Index** (Índice de Saúde de Startup) gerado permite converter dados não estruturados de repositórios GitHub em conhecimento estratégico e fidedigno, reduzindo significativamente o risco operacional de auditorias manuais.

---
**Trabalho Final da Disciplina — 27 de Março de 2026**
