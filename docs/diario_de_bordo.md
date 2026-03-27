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

## 🟢 27/03/2026 — Sessão 02: Coleta, NLP e Dashboard de Negócio

### 🎯 Objetivos de Hoje:
1. Integrar APIs (GitHub, BrasilAPI) e Scraping.
2. Implementar Pipeline NLP (spaCy) e Estudo de Ablação (Baseline vs Transformers).
3. Desenvolver Front-end interativo para apresentação passo-a-passo do projeto.

### 🚀 O que fizemos:
- **Pipeline:** Integramos `sentimentos.py` com o dashboard final.
- **Dashboard:** Criamos uma plataforma interativa em 5 etapas (Apresentação, Coleta, NLP, Sentimento, Dashboard).
- **Inovação:** Implementamos a lógica de **Interpretação e Prescrição** para transformar dados em ação.
- **Visual:** Overhaul visual seguindo o sistema 'Arkos Neural Grid' (Acid Green, Raw Borders 1px, 90/10 Asymmetry).
- **Agentes:** Otimizamos o projeto seguindo as regras de todos os agentes (Frontend Specialist, Backend Architect, Security Auditor).

### ⚠️ Erros e Correções de Rumo:
1. **Deploy Interface:** O deploy inicial via Vercel falhou por tentar rodar scripts de build inexistentes.
   - *Correção:* Adicionamos `vercel.json` para forçar o modo estático `version: 2`.
2. **Design Standards:** O design inicial usava glassmorphism excessivo (clichê de IA).
   - *Correção:* Seguindo o `frontend-specialist`, mudamos para superfícies brutas (1px borders) e tipografia de alto impacto.
3. **Segurança:** Identificamos o risco de exposição de tokens de API.
   - *Correção:* Criamos `.gitignore` e `.env.example` para documentar a segurança do projeto.

---

## ⏭️ Próximos Passos (Próxima Sessão):
- Expandir o corpus de treinamento para 50 startups.
- Refinar as métricas do Health Index com pesos dinâmicos por setor.
