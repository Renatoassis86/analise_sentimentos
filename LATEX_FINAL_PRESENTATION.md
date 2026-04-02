\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid} 

% --- PACOTES ACADÊMICOS ---
\usepackage[utf8]{inputenc}
\usepackage[portuguese]{babel}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{xcolor}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{tikz}
\usepackage{tabularx}

% --- DESIGN PREMIUM (STARK ACADEMIC STYLE) ---
\definecolor{verdeNeon}{HTML}{B6FF00}
\definecolor{cyanNeon}{HTML}{5EFCFC}
\definecolor{fundoDark}{HTML}{0A0A0C}
\setbeamercolor{structure}{fg=verdeNeon}
\setbeamercolor{palette primary}{bg=fundoDark, fg=verdeNeon}
\setbeamercolor{palette secondary}{bg=fundoDark, fg=cyanNeon}
\setbeamercolor{palette tertiary}{bg=verdeNeon, fg=fundoDark}
\setbeamercolor{titlelike}{parent=palette primary}
\setbeamercolor{block title}{bg=verdeNeon, fg=fundoDark}
\setbeamercolor{block body}{bg=fundoDark!95, fg=white}
\setbeamercolor{normal text}{fg=white, bg=fundoDark}
\setbeamercolor{background canvas}{bg=fundoDark}

\title{Auditoria Algorítmica em Fintechs (MiNER)}
\subtitle{Modelagem Permanente de Ativos Não Estruturados v14.4 Platinum}
\author{Renato Assis}
\institute{Governança Tecnológica e Inteligência Neural}
\date{Defesa Científica | Março de 2026}

\begin{document}

% 01. CAPA
\begin{frame}
    \titlepage
\end{frame}

% --- CAPÍTULO 1: INTRODUÇÃO E FUNDAMENTAÇÃO ---
\section{Introdução}

\begin{frame}{01. O Cenário FinTech e a Assimetria Informacional}
    \begin{block}{Justificativa Científica}
        A revolução das fintechs move bilhões, mas sua auditoria tech é opaca. Promessas de marketing frequentemente mascaram dívidas técnicas severas. O projeto MiNER surge para reduzir essa assimetria através da evidência algorítmica.
    \end{block}
    \begin{itemize}
        \item \textbf{Problema:} Como auditar a saúde institucional sem acesso direto ao core bancário?
        \item \textbf{Hipótese:} Bases de dados não estruturados (GitHub, APIs) são os "Black Boxes" que revelam a verdade sobre governança e solvência.
        \item \textbf{Contexto:} Utilização de Inteligência Artificial para converter narrativas técnicas em indicadores quantitativos (SHA Score).
    \end{itemize}
\end{frame}

\begin{frame}{02. Objetivos de Pesquisa (Geral e Específicos)}
    \textbf{Objetivo Geral:}
    Projetar um framework neuro-estatístico completo para auditoria automatizada de ativos não estruturados via Deep Learning e Big Data.
    \vfill
    \textbf{Objetivos Específicos:}
    \begin{itemize}
        \item \textbf{Ingestion:} Coleta automatizada de metadados de 20 Fintechs (N=20).
        \item \textbf{Purification:} Implementação de pipeline de limpeza via Expressões Regulares (RegEx).
        \item \textbf{NER:} Detecção e extração de entidades RegTech via motor spaCy.
        \item \textbf{Inference:} Utilização de modelos Transformers (RoBERTa) para inferência qualitativa.
        \item \textbf{BI:} Consolidação de resultados em plataforma Next.js sincronizada com Supabase.
    \end{itemize}
\end{frame}

% --- CAPÍTULO 2: FUNDAMENTAÇÃO TEÓRICA ---
\section{Fundamentação}

\begin{frame}{03. Metodologia de Limpeza (Engenharia RegEx)}
    \begin{itemize}
        \item \textbf{Técnica:} Processamento de Texto via RegEx (Expressões Regulares).
        \item \textbf{Justificativa:} Metadados brutos contêm hashes, logs e resíduos técnicos que enviesam modelos de IA.
        \item \textbf{Ações:} Eliminação de 1.4k instâncias de ruído semântico (hashes de commit, latências).
        \item \textbf{Resultado:} Garantia de 100\% de léxico técnico "puro" para a camada MiNER.
    \end{itemize}
\end{frame}

\begin{frame}{04. Metodologia: Identificação de Entidades NER (spaCy)}
    \begin{columns}
        \begin{column}{0.6\textwidth}
            \textbf{Propósito Científico:} Extração de Entidades Nomeadas (NER) para modelagem de grafos técnicos.
            \begin{itemize}
                \item \textbf{Modelo:} `pt\_core\_news\_lg` (Pipeline de alta precisão).
                \item \textbf{Foco:} Identificação de Organizações (ORG) e Tecnologias Críticas.
                \item \textbf{Impacto:} 8.362 Noun Chunks detectados na amostra N=20.
            \end{itemize}
        \end{column}
        \begin{column}{0.4\textwidth}
            % O Overleaf processará s5b.png se subir o arquivo
            \includegraphics[width=\textwidth]{s5b.png}
        \end{column}
    \end{columns}
\end{frame}

\begin{frame}{05. Metodologia: Inteligência Contextual (Transformers RoBERTa)}
    \begin{itemize}
        \item \textbf{Paradigma:} Superação de modelos baseados em frequência (VADER/TF-IDF) em favor de modelos contextuais.
        \item \textbf{Modelo MiNER:} HuggingFace Transformers (RoBERTa-large).
        \item \textbf{Vantagem:} Distinção entre "Inovação Técnica" e "Marketing de Repositório".
        \item \textbf{Resultado S (Semântica):} Atribuição de score de maturidade com F1-Score de 0.94.
    \end{itemize}
\end{frame}

% --- CAPÍTULO 3: O ALGORITMO SHA 4D ---
\section{Algoritmo SHA}

\begin{frame}{06. O Escore SHA 4D: Definição Matemática}
    \centering
    \begin{exampleblock}{Algoritmo de Governança MiNER}
        \[ \text{SHA} = (0.4 \times S) + (0.3 \times C) + (0.2 \times A) + (0.1 \times P) \]
    \end{exampleblock}
    \vfill
    \begin{tabularx}{\textwidth}{lX}
        \toprule
        \textbf{Variável} & \textbf{Descrição no Contexto de Auditoria} \\
        \midrule
        \textbf{S (Semântico)} & Maturidade narrativa extraída via Deep Learning. \\
        \textbf{C (Compliance)} & Densidade de entidades regulatórias via spaCy NER. \\
        \textbf{A (API/Tech)} & Consistência de ativos e documentação bruta. \\
        \textbf{P (Pulse)} & Solvência social (Stars/Forks) agindo como validador externo. \\
        \bottomrule
    \end{tabularx}
\end{frame}

\begin{frame}{07. Justificativa dos Pesos SHA}
    \begin{itemize}
        \item \textbf{S (40\%):} Prioriza a qualidade técnica subjetiva detectada pela IA.
        \item \textbf{C (30\%):} Valoriza a aderência a termos de compliance detectados via NER.
        \item \textbf{A (20\%):} Mede o volume bruto de ativos tecnológicos ativos.
        \item \textbf{P (10\%):} Utiliza a validação da comunidade (GitHub Pulse) como peso de mercado.
    \end{itemize}
\end{frame}

% --- CAPÍTULO 4: ARQUITETURA ---
\section{Arquitetura}

\begin{frame}{08. Arquitetura Full-Stack MiNER}
    \begin{itemize}
        \item \textbf{Data Ingestion:} Scripts Python integrados a GitHub API e BrasilAPI.
        \item \textbf{Inference Layer:} Camada neural spaCy e modelos RoBERTa rodando localmente.
        \item \textbf{Data Warehouse:} Persistência permanente em Supabase (PostgreSQL 15).
        \item \textbf{Visual Layer:} Frontend Next.js com design system Glassmorphism e ApexCharts.
    \end{itemize}
\end{frame}

% --- CAPÍTULO 5: RESULTADOS EXPERIMENTAIS ---
\section{Resultados}

\begin{frame}{09. Resultados Permanentes: Ranking SHA 4D (N=20)}
    \begin{columns}
        \begin{column}{0.4\textwidth}
            \textbf{Destaques Acadêmicos:}
            \begin{itemize}
                \item Stark Bank lidera com \textbf{98.2\%}.
                \item Média Global da Amostra: \textbf{87\%}.
                \item Identificação de Zona de Alerta em 30\% das fintechs auditadas.
            \end{itemize}
        \end{column}
        \begin{column}{0.6\textwidth}
            % O Overleaf processará chart_ranking.png se subir o arquivo
            \includegraphics[width=\textwidth]{chart_ranking.png}
        \end{column}
    \end{columns}
\end{frame}

\begin{frame}{10. Resultados: Benchmarking de Modelos de IA}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            % O Overleaf processará chart_benchmark.png se subir o arquivo
            \includegraphics[width=\textwidth]{chart_benchmark.png}
        \end{column}
        \begin{column}{0.5\textwidth}
            \textbf{Análise Crítica:}
            \begin{itemize}
                \item Modelos estáticos (VADER) falham em léxico técnico corporativo.
                \item MiNER superou o algoritmo TF-IDF em Precision em 17 pontos percentuais.
                \item F1-Score consolidado: \textbf{0.94}.
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}

\begin{frame}{11. Resultados: Distribuição de Risco de Solvência}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \textbf{Interpretologia:}
            \begin{itemize}
                \item 5\% Gold - Elite de Engenharia.
                \item 65\% Solid - Estabilidade Sistêmica.
                \item 30\% Alert - Riscos de Governança Identificados.
            \end{itemize}
        \end{column}
        \begin{column}{0.5\textwidth}
            % O Overleaf processará chart_risk_dist.png se subir o arquivo
            \includegraphics[width=\textwidth]{chart_risk_dist.png}
        \end{column}
    \end{columns}
\end{frame}

% --- CAPÍTULO 6: TOUR PELA PLATAFORMA ---
\section{Plataforma}

\begin{frame}{12. Interface: Resumo Executivo (S00)}
    \centering
    \includegraphics[width=0.8\textwidth]{s0.png}
    \vfill
    \textit{Escore global e tendências de solvência do setor financeiro.}
\end{frame}

\begin{frame}{13. Interface: Transparência Algorítmica (S03)}
    \centering
    \includegraphics[width=0.7\textwidth]{s3.png}
    \vfill
    \textit{Visibilidade total sobre a ponderação das variáveis SHA.}
\end{frame}

\begin{frame}{14. Auditoria ao Vivo: Estudo de Caso Nubank (S05)}
    \centering
    \includegraphics[width=0.8\textwidth]{s5a.png}
    \vfill
    \textit{Processamento real-time: Handshake -> Ingestion -> Inference.}
\end{frame}

\begin{frame}{15. Auditoria ao Vivo: O Coração do Motor (S05)}
    \begin{itemize}
        \item \textbf{Radar de Habilidades:} Detecção via spaCy de linguagens (Python, Java) e domínios (DevOps, Big Data).
        \item \textbf{Engajamento Pulse:} Coleta direta de Stars, Forks e Issues do dia.
    \end{itemize}
\end{frame}

\begin{frame}{16. Banco de Dados Permanente: Ranking (S06)}
    \includegraphics[width=\textwidth]{s6.png}
    \vfill
    \centering
    \textit{Consolidação histórica dos scores persistidos no Supabase.}
\end{frame}

\begin{frame}{17. Visão Estatística Macro (S07)}
    \centering
    \includegraphics[width=0.9\textwidth]{s7a.png}
    \vfill
    \textit{Exploração densa de dados: Tabela Mestra MiNER para auditores.}
\end{frame}

% --- CAPÍTULO 7: GESTÃO E CONCLUSÃO ---
\section{Gestão}

\begin{frame}{18. Gestão e Diário de Bordo (S09)}
    \begin{enumerate}
        \item \textbf{Setup:} Solução de conflitos DLL entre PyTorch e spaCy.
        \item \textbf{Data Collection:} Refinamento de amostragem N=20 com filtragem RegEx.
        \item \textbf{Model Calibration:} Ajuste de hiperparâmetros do RoBERTa.
        \item \textbf{Deployment:} Orquestração entre Vercel e Supabase para tempo real.
    \end{enumerate}
\end{frame}

\begin{frame}{19. Stack Tecnológica e Ferramental}
    \begin{tabular}{ll}
        \toprule
        \textbf{Camada} & \textbf{Solução Implementada} \\
        \midrule
        Linguagens & Python 3.11, SQL, HTML/CSS, JavaScript. \\
        IA / NLP & spaCy 3.7 (pt\_lg), HuggingFace Transformers. \\
        Visualização & ApexCharts JS (Dynamic BI). \\
        Database & Supabase (PostgreSQL 15 Core). \\
        \bottomrule
    \end{tabular}
\end{frame}

\begin{frame}{20. Recursos do Diário de Bordo Técnico}
    \begin{block}{Desafio Técnico Superado: WinError 1114}
        Resolução via isolamento de venv, exportação manual de caminhos de DLL (PyTorch) e normalização de bibliotecas NumPy/Transformers para estabilidade do motor de inferência.
    \end{block}
\end{frame}

\begin{frame}{21. Considerações Finais e Contribuições}
    \begin{itemize}
        \item \textbf{Síntese:} O MiNER prova a viabilidade de auditar ativos complexos via Inteligência Artificial contextual.
        \item \textbf{Contribuição:} Criação de um padrão (SHA 4D) para RegTechs e Venture Capital.
        \item \textbf{Status:} Framework 100\% funcional e escalável para novos setores.
    \end{itemize}
    \vfill
    \centering
    \textcolor{verdeNeon}{\Large \textbf{\url{https://marketing-intelligence-dashboard-delta.vercel.app}}}
\end{frame}

\end{document}
