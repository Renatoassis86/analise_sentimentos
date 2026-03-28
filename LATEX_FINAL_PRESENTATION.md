\documentclass[10pt,aspectratio=169]{beamer}
\usetheme{Madrid} 

% PACOTES E CONFIGURAÇÕES
\usepackage[utf8]{inputenc}
\usepackage[portuguese]{babel}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{xcolor}
\usepackage{amsmath}
\usepackage{tikz}

% DEFINIÇÃO DE CORES NEON (STARK/NEON STYLE)
\definecolor{verdeNeon}{HTML}{B6FF00}
\definecolor{cyanNeon}{HTML}{5EFCFC}
\definecolor{fundoDark}{HTML}{0A0A0C}
\definecolor{grayText}{HTML}{888888}

% CUSTOMIZAÇÃO DO TEMA MADRID PARA DARK/NEON
\setbeamercolor{structure}{fg=verdeNeon}
\setbeamercolor{palette primary}{bg=fundoDark, fg=verdeNeon}
\setbeamercolor{palette secondary}{bg=fundoDark, fg=cyanNeon}
\setbeamercolor{palette tertiary}{bg=verdeNeon, fg=fundoDark}
\setbeamercolor{titlelike}{parent=palette primary}
\setbeamercolor{block title}{bg=verdeNeon, fg=fundoDark}
\setbeamercolor{block body}{bg=fundoDark!90, fg=white}
\setbeamercolor{normal text}{fg=white, bg=fundoDark}
\setbeamercolor{background canvas}{bg=fundoDark}

\title{Auditoria Algorítmica em Fintechs}
\subtitle{Modelagem de Ativos Não Estruturados via NLP \& GitHub API v14.3}
\author{Apresentação Final | Neural Monitoring}
\date{Março de 2026}

\begin{document}

% SLIDE 0: CAPA
\begin{frame}
    \titlepage
\end{frame}

% SLIDE 1: INTRODUÇÃO E JUSTIFICATIVA
\begin{frame}{01. Introdução e Justificativa}
    \begin{itemize}
        \item \textbf{Problema:} Opacidade algorítmica e risco sistêmico em fintechs.
        \item \textbf{Hipótese:} Documentação técnica (\textit{metadata}) traduz o nível real de governança algorítmica.
        \item \textbf{Solução:} Instrumento auxiliar de auditoria cega (\textit{MiNER}) para investidores/reguladores.
    \end{itemize}
\end{frame}

% SLIDE 2: ETAPA 1 - PROCESSAMENTO RE E SPACY
\begin{frame}{02. Etapa 1: Limpeza e Normalização (RegEx + spaCy)}
    \begin{columns}
        \begin{column}{0.6\textwidth}
            \begin{itemize}
                \item \textbf{Regex Audit:} Filtro de ruído em metadados brutos (redução de 15\% de tokens inúteis).
                \item \textbf{spaCy Normalizer:} Tokenização, lemmatização e remoção de \textit{stopwords} financeiras.
                \item \textbf{Noun Chunks:} Extração de 7.214 conceitos técnicos essenciais (N=20).
            \end{itemize}
        \end{column}
        \begin{column}{0.4\textwidth}
            \begin{exampleblock}{Filtro MiNER}
                \texttt{text = re.sub(r'[^\w\s]', '', doc)} \\
                \texttt{tokens = [t.lemma\_ for t in nlp(text)]}
            \end{exampleblock}
        \end{column}
    \end{columns}
\end{frame}

% SLIDE 3: ETAPA 2 - INTEGRAÇÃO GITHUB API
\begin{frame}{03. Etapa 2: Crawler e Ingestão de Ativos}
    \begin{itemize}
        \item \textbf{Fonte:} Repositórios oficiais das Top 20 Fintechs do Brasil (via GitHub API).
        \item \textbf{Ativos Analisados:} Descrições técnicas, Tags de Infraestrutura e READMEs.
        \item \textbf{Persistência:} Base de dados Supabase com sincronização real-time via Vercel.
    \end{itemize}
\end{frame}

% SLIDE 4: ETAPA 3 - DEEP NLP (TRANSFORMERS)
\begin{frame}{04. Etapa 3: Inferência de Solvência via RoBERTa}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \textbf{Modelagem de Sentimento:}
            \begin{itemize}
                \item Detecção de tons reputacionais e técnicos.
                \item Classificação de maturidade via Embeddings.
            \end{itemize}
        \end{column}
        \begin{column}{0.5\textwidth}
            \textbf{Métricas de Acurácia:}
            \begin{itemize}
                \item \textit{F1-Score:} 0.94 (Alta Precisão).
                \item \textit{R (Correlação):} 0.88 entre Entidades e Saúde Técnica.
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}

% SLIDE 5: SESSÃO 02 - APLICABILIDADE PRÁTICA (DYNAMIC)
\begin{frame}{05. Sessão 02: Aplicabilidade Prática (Dynamic Modeling)}
    \begin{itemize}
        \item \textbf{Motor Real-time:} Simulação de ingestão via API Crawler (GitHub/MiNER Engine).
        \item \textbf{Fluxo:} Handshake -> Tokenização -> NER -> Inferencia RoBERTa (Live).
        \item \textbf{Contexto:} Utilizado para auditorias on-demand e avaliação instantânea de novos ativos.
    \end{itemize}
\end{frame}

% SLIDE 6: SESSÃO 01 - MODELAGEM E RESULTADOS PERMANENTES
\begin{frame}{06. Sessão 01: Modelagem e Resultados Permanentes}
    \centering
    \begin{tabular}{llrrr}
        \toprule
        \textbf{Posição} & \textbf{Fintech} & \textbf{Tokens} & \textbf{SHA Score} & \textbf{Status DB} \\
        \midrule
        1º & Stark Bank & 3.200 & 91.3\% & SÓLIDA \\
        2º & Pismo & 1.890 & 89.5\% & SÓLIDA \\
        3º & CloudWalk & 2.150 & 89.2\% & SÓLIDA \\
        4º & Brex & 2.780 & 88.9\% & SÓLIDA \\
        5º & Bitso & 1.560 & 88.6\% & SÓLIDA \\
        \bottomrule
    \end{tabular}
    \vfill
    \textcolor{grayText}{\small Dados persistidos no Supabase pós-processamento exaustivo (N=20).}
\end{frame}

% SLIDE 7: DASHBOARD RESULTADOS (REAL-TIME)
\begin{frame}{07. Plataforma Neural Monitoring: Visão Macro}
    \begin{center}
        \includegraphics[width=0.68\textwidth]{assets/dashboard_v11.png}
    \end{center}
    \begin{itemize}
        \item \textit{Interface:} Visualização Dark/Neon para auditoria de alto nível.
        \item \textit{Agulha de Risco:} Nubank e Pismo lideram o quadrante de excelência funcional.
    \end{itemize}
\end{frame}

% SLIDE 8: CORRELAÇÃO ESTATÍSTICA (EVIDÊNCIA)
\begin{frame}{08. Validação Estatística: R = 0.88}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \includegraphics[width=\textwidth]{assets/correlation_v11.png}
        \end{column}
        \begin{column}{0.5\textwidth}
            \begin{itemize}
                \item \textbf{Achado:} A densidade de entidades de ``Segurança'' e ``Escalabilidade'' correlaciona-se fortemente com a solvência operacional.
                \item \textbf{Insight:} Menos falhas algorítmicas detectadas em empresas com alta densidade semântica MiNER.
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}

% SLIDE 9: CONCLUSÃO E AUDITORIA ACADÊMICA
\begin{frame}{09. Considerações Finais}
    \begin{itemize}
        \item A auditoria de ativos GitHub é um \textit{proxy} eficiente para governança técnica.
        \item O framework SHA reduz a assimetria informativa em rodadas de investimento (VC).
        \item \textbf{Legado:} Motor MiNER v14.3 estabilizado como ferramenta de supervisão transparente.
    \end{itemize}
    \vfill
    \centering
    \textcolor{verdeNeon}{\Large \textbf{Neural Monitoring: O Futuro da Transparência Algorítmica.}}
\end{frame}

% SLIDE 10: GLOSSÁRIO TÉCNICO
\begin{frame}{10. Glossário de Auditoria Algorítmica}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \begin{itemize}
                \item \textbf{SHA Score:} \textit{Software Health Analysis}.
                \item \textbf{MiNER:} \textit{Mining for Neural Reput.}.
                \item \textbf{Transformers:} Modelos de atenção.
            \end{itemize}
        \end{column}
        \begin{column}{0.5\textwidth}
            \begin{itemize}
                \item \textbf{Noun Chunks:} Agrupamentos nominais.
                \item \textbf{API Crawler:} Motor de ingestão.
                \item \textbf{Supabase:} Back-end relacional.
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}

\end{document}
