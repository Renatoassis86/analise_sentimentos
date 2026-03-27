# 🎭 Roteiro de Apresentação — Neural Marketing Intelligence: Startup Signal Intelligence

Este roteiro organiza os 10 slides estratégicos para a banca da UFPB. O objetivo é equilibrar o **rigor técnico da disciplina** com a **visão executiva da Neural Platform**.

---

### 🖼️ SLIDE 1 — Capa
**Visual:** Logo Neural Marketing Intelligence centralizado (Obsidiana + Verde Sinal).
**Texto:** 
- **TítuloPrincipal:** Neural Marketing Intelligence — Startup Signal Intelligence
- **Subtítulo:** Módulo Marketing Intelligence | Análise de Sentimentos com PLN
- **Apresentadores:** Renato Assis & Equipe Neural Platform
- **Data:** Março de 2026
**Fala sugerida (1 min):** *"Bom dia a todos. Hoje apresentamos o Neural Marketing Intelligence, o motor de inteligência por trás do nosso ecossistema corporativo. Nosso objetivo é transformar o mar de dados não estruturados de startups em indicadores de reputação e tração real."*

---

### 🖼️ SLIDE 2 — Contexto e Problema
**Visual:** Gráfico de bolhas (Plotly) ou Iconografia de Redes Sociais.
**Texto:** "Por que monitorar sentimentos de startups?"
- **Qiu et al. (2025):** Sentimento positivo em mídias sociais prediz o financiamento futuro ($F1 = 0.82$).
- **Saura et al. (2019):** Distribuição típica de startups: 57% Positivo, 29% Neutro, 14% Negativo.
- **Slogan:** "Neural Marketing Intelligence: Do dado bruto à decisão executiva."
**Fala sugerida:** *"Startups não falham por falta de tecnologia, mas por falta de legitimidade. A ciência prova que o sentimento digital é um proxy direto para a captação de investimento."*

---

### 🖼️ SLIDE 3 — Arquitetura do Sistema
**Visual:** Fluxograma linear colorido (Roxo #6366F1 e Verde #10B981).
**Diagrama:**
1.  **Etapa 1:** RE + spaCy Baseline (Estruturação)
2.  **Etapa 2:** APIs + Scraping (Coleta Multicanal)
3.  **Etapa 3:** Deep NLP + Transformers (Análise de Saúde)
**Fala sugerida:** *"Nosso pipeline é dividido em três camadas: a infraestrutura de limpeza, o motor de coleta multicanal e a camada de inteligência com Deep Learning."*

---

### 🖼️ SLIDE 4 — Etapa 1: RE + spaCy
**Visual:** Tabela comparativa "Antes vs Depois".
**Conteúdo:**
- **re.findall:** Extração de E-mails, Versões (v2.1.0), Menções (@), Issues (#).
- **re.sub:** Limpeza progressiva de Markdown e Ruído.
- **re.search / re.split:** Qualidade de README e fragmentação de Changelogs.
**Fala sugerida:** *"Aqui usamos Expressões Regulares para minerar 'Trust Markers'. Sem um e-mail de suporte ou versões constantes detetadas via regex, a startup já perde pontos no nosso score de confiança."*

---

### 🖼️ SLIDE 5 — Etapa 2: Coleta de Dados
**Visual:** Logotipos GitHub, BrasilAPI e BeautifulSoup.
**Conteúdo:**
- **GitHub API:** Buscamos registros de 'fintech brazil' e capturamos issues reais.
- **BrasilAPI:** Extraímos dados estruturados de corretoras CVM.
- **BeautifulSoup:** Scraping de sites de notícias para o nosso Corpus Digital.
**Fala sugerida:** *"Nossos dados vêm de fontes diversas. Integramos APIs oficiais e scraping para garantir que nossa inteligência seja alimentada por dados reais e atualizados."*

---

### 🖼️ SLIDE 6 — Etapa 3: Pipeline spaCy Completa
**Visual:** Tabela dos 6 componentes + print do `displacy.render()`.
**Conteúdo:**
- **Componentes:** Tokenização, Lematização, POS Tagging, Noun Chunks, NER, Segmentação.
- **Destaque:** Demonstração visual de como o spaCy identifica "iFood" como Organização e "PIX" como Produto.
**Fala sugerida:** *"Este é o cérebro da Etapa 3. Usamos o spaCy para decompor a gramática e entender quem são os atores e produtos citados nas discussões."*

---

### 🖼️ SLIDE 7 — Classificação de Textos
**Visual:** Gráfico de Loss (Matplotlib) e Pizza de Sentimentos (Plotly).
**Conteúdo:**
- **TextCategorizer (spaCy):** Treinado para o baseline rápido.
- **Transformer (RoBERTa):** Estado da arte para precisão extrema.
- **Ablation Study:** Comprovação da superioridade dos Transformers ($Acc \uparrow$).
**Fala sugerida:** *"Não confiamos apenas em um modelo. Comparamos o baseline estatístico com o Deep Learning para garantir que a análise de reputação seja precisa e sem vieses."*

---

### 🖼️ SLIDE 8 — Startup Health Dashboard (INTERATIVO)
**Visual:** Navegação live pelo Front-end Neural Platform Intelligence.
**Conteúdo:**
- **Etapas:** Demonstração visual de Coleta -> Processamento -> Sentimento -> Veredito.
- **Diferencial:** Inclusão de **Interpretação e Prescrição** automatizada para cada startup.
- **Saúde Real:** Foco no KPI consolidado (Health Index).
**Fala sugerida:** *"O nosso Health Dashboard não é apenas um gráfico estático. Ele é uma plataforma interativa que guia o stakeholder através de cada técnica aplicada, culminando em uma prescrição de negócio clara."*

---

### 🖼️ SLIDE 9 — Diário de Bordo (Obrigatório)
**Visual:** Lista de "Check x Fix".
**Problemas & Soluções:**
- **Linguagem:** Mix de PT/EN $\rightarrow$ Solução: Pipeline híbrida.
- **Desbalanceamento:** Muitas 'positives' $\rightarrow$ Solução: F1-Score Ponderado.
- **API Limits:** Rate Limit GitHub $\rightarrow$ Solução: Cache local de JSONs.
- **Hardware:** BERT pesado $\rightarrow$ Solução: Truncagem de sequências em 256 tokens.
**Fala sugerida:** *"Tivemos desafios reais de produção, desde limites de API até modelos pesados de BERT, mas resolvemos através de engenharia de sistema robusta."*

---

### 🖼️ SLIDE 10 — Resultados e Conclusão
**Visual:** Selo de "✅ Checklist Completo".
**Resumo:**
- Todas as estratégias da UFPB cobertas.
- Suporte científico em 5 artigos de impacto.
- **Slogan Final:** "Neural Marketing Intelligence — Do dado bruto à decisão executiva."
**Fala sugerida:** *"Concluímos que a modelagem de dados não estruturados não é apenas técnica, é estratégica. A Neural Marketing Intelligence está pronta para o mercado. Obrigado."*
