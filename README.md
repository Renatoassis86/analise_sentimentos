# <p align="center">🛡️ ArKOS Marketing Intelligence: Auditoria Algorítmica em Fintechs</p>

<p align="center">
  <img src="assets/arkos_logo.png" alt="ArKOS MI Logo" width="220"/>
</p>

<p align="center">
  <strong>Motor de Inteligência MiNER (Marketing Intelligence Engine for Reputation)</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Academic-UFPB-red?style=for-the-badge" alt="UFPB"/>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/spaCy-v3.x-05BDAD?style=for-the-badge&logo=spacy" alt="spaCy"/>
  <img src="https://img.shields.io/badge/Transformers-RoBERTa-FFD21E?style=for-the-badge&logo=huggingface" alt="Transformers"/>
</p>

---

## 🚀 Visão Geral
O **ArKOS MI** é uma plataforma de auditoria algorítmica projetada para avaliar a saúde tecnológica e reputacional de Fintechs brasileiras. Através da modelagem de dados não estruturados (READMEs de repositórios, documentação de APIs e manifestos de segurança), o sistema gera o **SHA 4D Score** — um indicador quantitativo de Segurança, Saúde, Atividade e Popularidade.

## 🏗️ Metodologia Acadêmica (3 Etapas)
O pipeline de auditoria é estruturado em três camadas de análise profunda:

1.  **Etapa 01: Limpeza e Normalização (Regex + spaCy)**
    *   Remoção de ruídos técnicos via Expressões Regulares.
    *   Lematização semântica e filtragem de ruído linguístico.
2.  **Etapa 02: Ingestão e Governança (Web APIs)**
    *   Extração automatizada de documentação técnica via GitHub Raw API.
    *   Mapeamento de infraestrutura e transparência de código.
3.  **Etapa 03: Auditoria Semântica Profunda (POS, NER & Transformers)**
    *   **POS Tagging:** Auditoria da Gramática de Design (Densidade de Ativos vs. Marketing).
    *   **NER:** Reconhecimento de Entidades de Governança e Compliance (ISO, BCB, etc).
    *   **RoBERTa:** Inferência contextual de saúde algorítmica e sentimentos técnicos.

## 🧪 Estrutura do Repositório
*   `notebooks/`: Dossiês de execução para defesa acadêmica.
    *   `03_etapa3_pln_sentimentos.ipynb`: O coração do motor de inteligência.
    *   `DEMONSTRACAO_GERAL_PROJETO.ipynb`: Visão consolidada para a banca examinadora.
*   `src/`: Código fonte modularizado para produção.
*   `frontend/`: Dashboard em Next.js para visualização executiva (Vercel).

## 🛠️ Configuração do Ambiente
```bash
# Instalação facilitada
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
```

---

**Pesquisador:** Renato Assis  
**Disciplina:** Modelagem de Dados Não Estruturados | UFPB  
**Status:** 100% Operacional para Defesa Acadêmica.
