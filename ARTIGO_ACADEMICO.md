# 📄 Estudo sobre Auditoria de Sinais em Fintechs: Uma Abordagem de Apoio à Decisão via Repositórios GitHub

---

## 00. RESUMO (ABSTRACT)
O presente estudo explora a aplicação de uma arquitetura de análise automatizada para o setor de Fintechs, fundamentada na mineração de dados de repositórios **GitHub**. Através do uso de técnicas de **PLN (Processamento de Linguagem Natural)**, combinando **Regex** para limpeza e modelos **Transformers** para análise semântica, a pesquisa busca oferecer uma camada adicional de evidências para o ecossistema de investimentos. Os resultados sugerem que a transparência técnica pode servir como um indicador útil de maturidade em ativos de base tecnológica.

---

## 01. INTRODUÇÃO E JUSTIFICATIVA
A avaliação de startups de tecnologia enfrenta desafios constantes na validação de ativos durante processos de **Due Diligence**. A complexidade em distinguir narrativas de marketing da infraestrutura técnica real motiva a busca por métodos empíricos complementares. Este estudo justifica-se pela possibilidade de utilizar dados públicos de desenvolvimento para prover uma visão mais técnica e menos subjetiva sobre a saúde de um projeto de software, auxiliando na compreensão da maturidade tecnológica da empresa.

---

## 02. OBJETIVOS
*   **Geral**: Aplicar as metodologias de análise de dados não estruturados propostas na disciplina para avaliar a saúde técnica de repositórios vinculados a Fintechs brasileiras.
*   **Específicos**: 
    1. **Etapa 01**: Implementar filtragem de dados via **Regex** para remoção de ruídos em documentações.
    2. **Etapa 02**: Demonstrar a coleta de dados via **GitHub API** e validação institucional.
    3. **Etapa 03**: Realizar o processamento linguístico (NER, POS Tagging) para identificar o foco tecnológico.
    4. **Etapa 04**: Aplicar modelos de sentimentos (**Transformers**) para compor um índice experimental de maturidade.

---

## 03. METODOLOGIA (ETAPAS 1, 2, 3)
*   **Técnicas**: Foram utilizadas **Expressões Regulares (RE)** para higienização, **spaCy** para extração de entidades técnicas (NER) e categorização gramatical (POS), e a **GitHub API** para aquisição de metadados de engajamento (Stars, Forks). O cruzamento com dados da **CVM** via **BrasilAPI** buscou adicionar contexto institucional à análise.

---

## 04. MODELAGEM (ETAPA 4)
Criou-se o **SHA (Startup Health Algorithm)**, um índice experimental que pondera atividade técnica e clareza da documentação. 
*   **Desempenho**: O uso de modelos baseados em **Transformers (RoBERTa)** demonstrou uma melhor captura de nuances técnicas em relação a abordagens puramente estatísticas, fundamentando a escolha metodológica para este estudo de caso.

---

## 05. RESULTADOS E APLICABILIDADE
A aplicação resultou em um ranking (**Top 20**) que destaca projetos com alta densidade de documentação e engajamento, como o **fklearn (Nubank)**. O sistema permite visualizar, de forma comparativa, como diferentes empresas do setor financeiro estruturam sua presença técnica pública.

---

## 06. CONCLUSÕES
O estudo demonstra que a mineração de dados não estruturados é uma forma viável de complementar o processo de análise de startups. Embora não substitua a auditoria tradicional, a metodologia provê sinais latentes que enriquecem a governança tecnológica. Conclui-se que o uso de inteligência artificial aplicada a metadados técnicos oferece um suporte relevante para a transparência no setor de Fintechs.

---
**Trabalho Final da Disciplina — 27 de Março de 2026**
