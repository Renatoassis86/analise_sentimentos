"""
Pipeline de Processamento de Linguagem Natural (PLN) - Neural Marketing Intelligence
Este módulo implementa os componentes fundamentais do spaCy para análise profunda
de narrativas de startups brasileiras.

Autor: Renato Assis | Neural Platform Intelligence
"""

import spacy
import pandas as pd
import matplotlib.pyplot as plt
from spacy import displacy
from collections import Counter
import os

# Inicialização automática do modelo spaCy
try:
    nlp = spacy.load("pt_core_news_sm")
except OSError:
    # Caso o modelo não esteja baixado, avisar ou baixar (aqui apenas avisamos para evitar bloqueios)
    print("Aviso: Modelo 'pt_core_news_sm' não encontrado. Execute 'python -m spacy download pt_core_news_sm'")
    nlp = None

def tokenizar(texto, nlp_obj):
    """
    Componente 1: Tokenização e propriedades básicas.
    Retorna um DataFrame com metadados de cada token.
    """
    doc = nlp_obj(texto)
    dados = []
    for token in doc:
        dados.append({
            "Token": token.text,
            "Índice": token.i,
            "É pontuação?": token.is_punct,
            "É número?": token.is_digit,
            "É stopword?": token.is_stop
        })
    return pd.DataFrame(dados)

def normalizar_e_lematizar(texto, nlp_obj):
    """
    Componente 2: Normalização e Lematização.
    Retorna dicionário com versões processadas do texto.
    """
    doc = nlp_obj(texto)
    # Lematização removendo pontuação e stopwords para o 'texto_lematizado'
    tokens_lematizados = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
    
    return {
        "texto_original": texto,
        "texto_limpo": " ".join([token.text.lower() for token in doc if not token.is_punct]),
        "tokens_lematizados": tokens_lematizados,
        "texto_lematizado": " ".join(tokens_lematizados)
    }

def pos_tagging(texto, nlp_obj):
    """
    Componente 3: Part-of-Speech Tagging.
    Retorna DataFrame de tags e gera gráfico de distribuição.
    """
    doc = nlp_obj(texto)
    dados = []
    for token in doc:
        dados.append({
            "Token": token.text,
            "Lema": token.lemma_,
            "POS": token.pos_,
            "Explicação": spacy.explain(token.pos_),
            "É stopword?": token.is_stop
        })
    df = pd.DataFrame(dados)
    
    # Gráfico de barras de distribuição de POS
    if not df.empty:
        plt.figure(figsize=(10, 5))
        df['POS'].value_counts().plot(kind='bar', color='#C8F542', edgecolor='#0A0C0F')
        plt.title("Distribuição de Part-of-Speech (POS) - Neural Marketing Intelligence")
        plt.xlabel("Categoria Gramatical")
        plt.ylabel("Frequência")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
        
    return df

def extrair_noun_chunks(corpus_textos, nlp_obj):
    """
    Componente 4: Extração de Sintagmas Nominais (Noun Chunks).
    Analisa os núcleos sintáticos da narrativa.
    """
    dados = []
    textos_completos = " ".join(corpus_textos)
    doc = nlp_obj(textos_completos)
    
    for chunk in doc.noun_chunks:
        dados.append({
            "Sintagma": chunk.text,
            "Núcleo": chunk.root.text,
            "Dependência": chunk.root.dep_,
            "Cabeça sintática": chunk.root.head.text
        })
    df = pd.DataFrame(dados)
    
    # Counter com top 15 chunks mais frequentes
    chunks_count = Counter([d['Sintagma'].lower() for d in dados])
    top_15 = chunks_count.most_common(15)
    
    return df, top_15

def reconhecer_entidades(corpus_textos, nlp_obj):
    """
    Componente 5: Reconhecimento de Entidades Nomeadas (NER).
    Extrai Organizações, Pessoas, Locais e Valores.
    """
    dados = []
    textos_completos = " ".join(corpus_textos)
    doc = nlp_obj(textos_completos)
    
    for ent in doc.ents:
        dados.append({
            "Entidade": ent.text,
            "Tipo": ent.label_,
            "Explicação": spacy.explain(ent.label_)
        })
    df = pd.DataFrame(dados)
    
    # Gráfico de barras de frequência por tipo de entidade
    if not df.empty:
        plt.figure(figsize=(10, 5))
        df['Tipo'].value_counts().plot(kind='bar', color='#C8F542', edgecolor='#0A0C0F')
        plt.title("Distribuição de Entidades (NER) - Neural Marketing Intelligence")
        plt.show()
        
    return df, doc

def segmentar_sentencas(texto, nlp_obj):
    """
    Componente 6: Segmentação de Sentenças e Dependências.
    Analisa a estrutura das frases.
    """
    doc = nlp_obj(texto)
    sentencas = [sent.text.strip() for sent in doc.sents]
    
    return sentencas, doc

def rodar_pipeline_completa(corpus_textos, nlp_obj=None):
    """
    Função Mestre: Executa todos os componentes da pipeline em sequência.
    """
    if nlp_obj is None:
        global nlp
        nlp_obj = nlp
    
    if nlp_obj is None:
        return {"erro": "Modelo spaCy não carregado."}

    texto_unico = " ".join(corpus_textos)
    
    print("Iniciando Pipeline Neural Marketing Intelligence...")
    
    res = {}
    res["tokens"] = tokenizar(texto_unico, nlp_obj)
    res["normalizacao"] = normalizar_e_lematizar(texto_unico, nlp_obj)
    res["pos"] = pos_tagging(texto_unico, nlp_obj)
    res["chunks"], res["top_chunks"] = extrair_noun_chunks(corpus_textos, nlp_obj)
    res["entidades"], doc_ent = reconhecer_entidades(corpus_textos, nlp_obj)
    res["sentencas"], doc_sent = segmentar_sentencas(texto_unico, nlp_obj)
    
    print("Pipeline finalizada com sucesso.")
    return res

# --- CORPUS DE EXEMPLO (STARTUP MATURITY) ---
corpus_startups = [
    "O iFood é a empresa líder de delivery na América Latina, investindo pesado em IA para logística.",
    "O Nubank revolucionou o setor bancário no Brasil com seu cartão roxo e atendimento digital.",
    "QuintoAndar simplifica o aluguel e venda de imóveis usando dados para prever preços de mercado.",
    "Stone oferece soluções de pagamento para empreendedores brasileiros com foco em transparência.",
    "Creditas é a principal plataforma digital de crédito com garantia na América Latina."
]

if __name__ == "__main__":
    if nlp:
        resultados = rodar_pipeline_completa(corpus_startups, nlp)
        
        print("\n--- TOP 10 NOUN CHUNKS ---")
        print(resultados["top_chunks"][:10])
        
        print("\n--- ENTIDADES DETECTADAS (NER) ---")
        print(resultados["entidades"].head(10))
        
        print("\n--- EXEMPLO DE LEMATIZAÇÃO ---")
        print(resultados["normalizacao"]["texto_lematizado"][:200] + "...")
    else:
        print("Erro: nlp não inicializado.")
