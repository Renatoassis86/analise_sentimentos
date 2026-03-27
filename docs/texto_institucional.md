# 🏢 Neural Platform Intelligence — Motor de Marketing Intelligence (MI)

## O que estamos fazendo? (A Ciência por trás do Neural Marketing Intelligence)

A plataforma **Neural Platform** é uma infraestrutura de inteligência de dados que resolve o gargalo da tomada de decisão em organizações que ainda operam com "achismos". O módulo **MI** foca especificamente em converter a **Narrativa Pública** de startups e empresas em **Vantagem Competitiva**.

### As 3 Etapas do Processo:

#### 1. Estruturação Narrativa (Regex + spaCy)
Nesta etapa inicial, utilizamos **Expressões Regulares (Regex)** para garimpar o texto bruto em busca de "Trust Markers" (Marcadores de Confiança).
- **Por que?** Porque uma startup que mantém um e-mail de suporte ativo (`regex e-mails`), versões de software constantes (`regex versões`) e uma documentação estruturada (`regex qualidade readme`) demonstra maior maturidade e menor risco.
- **Objetivo:** Converter texto não estruturado em um "Narrative Identity Card".

#### 2. Capital Social Digital (Scraping + NLTK)
Aqui, o foco muda para a rede. Coletamos dados de APIs e Web Scraping para quantificar a tração e a legitimidade.
- **Por que?** Segundo Cheng (2024), a presença multicanal de uma startup correlaciona-se fortemente com sua capacidade de atrair investimento ($R^2$ de 0.78).
- **Objetivo:** Quantificar o alcance e a regularidade da comunicação da marca.

#### 3. Inteligência Semântica (Transformers + Classificação)
A etapa final e mais avançada utiliza **Deep Learning (HuggingFace)** para ler "entre as linhas".
- **Por que?** Apenas saber "se falaram bem ou mal" não basta. Analisamos se a startup comunica uma "Solução Societal" (resolver um problema do mundo) ou é puramente "Product-Centric".
- **Objetivo:** Predizer o sucesso e o estágio de maturidade através de sinais narrativos profundos.

---
**Status do Projeto:** 🟢 Stage 1 (Infraestrutura e Regex) Completo.
**Autor:** Renato Assis | Neural Platform Intelligence
