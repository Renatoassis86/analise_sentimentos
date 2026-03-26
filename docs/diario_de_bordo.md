# 📓 Diário de Bordo — ARKOS MI (Startup Signal Intelligence)

Este documento registra o desenvolvimento, as falhas e as correções de curso do módulo de Marketing Intelligence (MI).

---

## 🟢 26/03/2026 — Sessão 01: Infraestrutura e Motor Regex

### 🎯 Objetivos de Hoje:
1. Definir a identidade visual e estratégica do projeto (Verde Sinal + Obsidiana).
2. Criar a estrutura escalável de diretórios.
3. Implementar o primeiro pilar técnico: **Expressões Regulares (RE)** para extração de "Trust Markers".

### 🚀 O que fizemos:
- **Arquitetura:** Criamos `src/`, `notebooks/`, `data/`, e `assets/`.
- **Identidade:** Definimos as cores da ARKOS no README e geramos o logo para o módulo MI.
- **Implementação:** Finalizamos `src/limpeza.py` com todas as funções regex (Markdown, E-mails, Versões, Qualidade de README).

### ⚠️ Erros e Correções de Rumo:
1. **Erro de Comando (Terminal):** Tentamos usar `touch` no PowerShell.
   - *Correção:* Substituímos por `New-Item` e `echo`, adaptando para o ambiente Windows.
2. **Ambiente Python:** Tentamos testar o script e encontramos erro de bibliotecas independentes (`platform independent libraries`).
   - *Causa provável:* O Anaconda não está inicializado no shell atual do VS Code.
   - *Correção:* Validamos o código manualmente e garantimos que as dependências estão no `requirements.txt`.
3. **Escopo:** Decidimos unificar o "Sentiment Analysis" com o framework de maturidade da ARKOS (Davenport Stage 1 to 5). Isso elevou o projeto de um simples script para uma ferramenta de consultoria.

---

## ⏭️ Próximos Passos (Próxima Sessão):
- Construir o wrapper de APIs e Scraping em `src/coleta.py`.
- Iniciar o primeiro Notebook para visualização das frequências narrativas.
