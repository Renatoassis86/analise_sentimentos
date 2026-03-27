"""
Módulo de Sentimentos e Estudo de Ablação - ARKOS MI
Este módulo integra classificação estatística (spaCy TextCat) com
Deep Learning (Transformers) para análise de reputação.

Autor: Renato Assis | ARKOS Intelligence
"""

import spacy
from spacy.training import Example
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, classification_report
import random

# --- PARTE A: TextCategorizer spaCy (Baseline) ---

def criar_modelo_textcat(labels=["POSITIVO", "NEGATIVO", "NEUTRO"]):
    """
    Inicializa um modelo spaCy em branco com componente textcat.
    """
    nlp_blank = spacy.blank("pt")
    config = {
        "threshold": 0.5,
        "model": {
            "@architectures": "spacy.TextCatEnsemble.v2",
            "linear_model": {"@architectures": "spacy.TextCatBOW.v2", "exclusive_classes": True, "ngram_size": 1, "no_output_layer": False},
            "tok2vec": {"@architectures": "spacy.Tok2Vec.v2", "embed": {"@architectures": "spacy.MultiHashEmbed.v2", "width": 64, "rows": [2000, 2000, 1000, 1000], "attrs": ["ORTH", "LOWER", "PREFIX", "SUFFIX"], "include_static_vectors": False}, "encode": {"@architectures": "spacy.MaxoutWindowEncoder.v2", "width": 64, "window_size": 1, "maxout_pieces": 3, "depth": 2}}
        }
    }
    textcat = nlp_blank.add_pipe("textcat", config=config)
    for label in labels:
        textcat.add_label(label)
    return nlp_blank

def treinar_textcat(modelo, dados_treino, n_epocas=20):
    """
    Loop de treinamento estatístico para o baseline.
    """
    textcat = modelo.get_pipe("textcat")
    optimizer = modelo.begin_training()
    historico_loss = []

    print(f"Treinando TextCat por {n_epocas} épocas...")
    for i in range(n_epocas):
        losses = {}
        random.shuffle(dados_treino)
        batches = spacy.util.minibatch(dados_treino, size=2)
        for batch in batches:
            examples = []
            for text, annot in batch:
                examples.append(Example.from_dict(modelo.make_doc(text), annot))
            modelo.update(examples, sgd=optimizer, losses=losses)
        historico_loss.append(losses['textcat'])
        if i % 5 == 0:
            print(f"Época {i} - Loss: {losses['textcat']:.4f}")
            
    return historico_loss

def avaliar_textcat(modelo, dados_teste):
    """
    Avalia a performance do modelo spaCy.
    """
    y_true = []
    y_pred = []
    for text, annot in dados_teste:
        doc = modelo(text)
        # Pega a label com maior score
        pred = max(doc.cats, key=doc.cats.get)
        y_pred.append(pred)
        # Pega a label verdadeira
        true = [label for label, val in annot['cats'].items() if val == 1.0][0]
        y_true.append(true)
    
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "report": classification_report(y_true, y_pred, output_dict=True)
    }

def plotar_loss(historico):
    """
    Gera o gráfico de convergência do treinamento.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(historico, color='#C8F542', linewidth=2, marker='o')
    plt.title("Curva de Aprendizado (Loss) - ARKOS MI TextCat")
    plt.xlabel("Época")
    plt.ylabel("Loss")
    plt.grid(True, alpha=0.3)
    plt.show()

# --- PARTE B: Transformers (HuggingFace) ---

def carregar_transformer(model_name="cardiffnlp/twitter-roberta-base-sentiment-latest"):
    """
    Carrega pipeline de sentimento baseada em BERT/RoBERTa.
    """
    print(f"Carregando {model_name}...")
    return pipeline("sentiment-analysis", model=model_name, tokenizer=model_name)

def analisar_sentimento_bert(textos, classificador):
    """
    Aplica o estado da arte para análise de sentimentos.
    """
    resultados = classificador(textos)
    df = pd.DataFrame(resultados)
    df['texto'] = textos
    # Mapeamento de labels do Twitter-RoBERTa
    mapping = {
        "positive": "POSITIVO",
        "neutral": "NEUTRO",
        "negative": "NEGATIVO",
        "LABEL_0": "NEGATIVO", # Fallback para modelos comuns
        "LABEL_1": "NEUTRO",
        "LABEL_2": "POSITIVO"
    }
    df['sentimento'] = df['label'].map(lambda x: mapping.get(x.lower(), x.upper()))
    return df[['texto', 'sentimento', 'score']]

# --- PARTE C: Embeddings Semânticos ---

def gerar_embeddings(textos, model_name="all-MiniLM-L6-v2"):
    """
    Transforma texto em vetores densos de alta dimensão.
    """
    print(f"Gerando embeddings com {model_name}...")
    model = SentenceTransformer(model_name)
    return model.encode(textos)

def visualizar_embeddings_pca(embeddings, sentimentos):
    """
    Visualização 2D interativa dos clusters de significado.
    """
    pca = PCA(n_components=2)
    components = pca.fit_transform(embeddings)
    
    df_plot = pd.DataFrame(data=components, columns=['PCA 1', 'PCA 2'])
    df_plot['Sentimento'] = sentimentos
    
    fig = px.scatter(df_plot, x='PCA 1', y='PCA 2', color='Sentimento',
                     title="Aglomerados Semânticos (PCA) - ARKOS MI",
                     color_discrete_map={"POSITIVO": "#C8F542", "NEGATIVO": "#FF4B4B", "NEUTRO": "#8A8F99"})
    fig.show()

# --- PARTE D: Ablation Study ---

def ablation_study(dados_teste, modelo_spacy, classificador_bert):
    """
    Compara o Baseline (Estatístico/BOW) com o Estado da Arte (Transformers).
    Referência: Qiu et al. (2025).
    """
    textos_teste = [d[0] for d in dados_teste]
    y_true = [next(k for k, v in d[1]['cats'].items() if v == 1.0) for d in dados_teste]
    
    # Eval spaCy
    res_spacy = avaliar_textcat(modelo_spacy, dados_teste)
    acc_spacy = res_spacy['accuracy']
    
    # Eval BERT
    res_bert = analisar_sentimento_bert(textos_teste, classificador_bert)
    acc_bert = accuracy_score(y_true, res_bert['sentimento'])
    
    df_ablation = pd.DataFrame({
        "Modelo": ["spaCy TextCat (BOW)", "HuggingFace (Transformer)"],
        "Acurácia": [acc_spacy, acc_bert]
    })
    
    # Gráfico Comparativo
    plt.figure(figsize=(8, 6))
    plt.bar(df_ablation['Modelo'], df_ablation['Acurácia'], color=['#8A8F99', '#C8F542'])
    plt.title("Estudo de Ablação: Baseline vs. Deep Learning")
    plt.ylabel("Acurácia")
    plt.ylim(0, 1.1)
    for i, v in enumerate(df_ablation['Acurácia']):
        plt.text(i, v + 0.05, f"{v:.2f}", ha='center', fontweight='bold')
    plt.show()
    
    return df_ablation

# --- PARTE E: Startup Health Index ---

def calcular_health_index(corpus_textos, classificador_bert, nlp):
    """
    Métrica híbrida proprietária da ARKOS MI.
    """
    if classificador_bert:
        res_sent = analisar_sentimento_bert(corpus_textos, classificador_bert)
        pct_positivo = (res_sent['sentimento'] == 'POSITIVO').mean()
    else:
        # Fallback se o transformer não carregar (vibe check simplificado para demo)
        txt_total = " ".join(corpus_textos).lower()
        pos_words = ['bom', 'ótimo', 'excelente', 'incrível', 'sucesso', 'parabéns', 'resolvido', 'rápido', 'estável', 'impecável']
        neg_words = ['erro', 'falha', 'bug', 'travando', 'horrível', 'péssimo', 'inexistente', 'ruim', 'crise', 'ninguém responde']
        
        pos_count = sum(1 for w in pos_words if w in txt_total)
        neg_count = sum(1 for w in neg_words if w in txt_total)
        pct_positivo = pos_count / (pos_count + neg_count + 1)
    
    # Riqueza Narrativa (Noun Chunks e NER)
    texto_total = " ".join(corpus_textos)
    doc = nlp(texto_total)
    
    n_chunks = len(list(doc.noun_chunks))
    n_ents = len(doc.ents)
    
    # Normalização Heurística (0-1)
    riqueza_chunks = min(n_chunks / 10, 1.0)
    riqueza_ner = min(n_ents / 5, 1.0)
    
    # Score Composto
    score = (pct_positivo * 50) + (riqueza_chunks * 30) + (riqueza_ner * 20)
    
    nivel = "BOA" if score > 70 else "MODERADA" if score > 40 else "CRÍTICA"
    
    recomendas = []
    if pct_positivo < 0.5: recomendas.append("Investir em canais de suporte para reverter sentimentos negativos.")
    if riqueza_chunks < 0.3: recomendas.append("Refinar a clareza da proposta de valor narrativa.")
    if riqueza_ner < 0.3: recomendas.append("Aumentar a presença multicanal para gerar mais indicadores estruturais.")
    
    return {
        "score": round(score, 2),
        "nivel": nivel,
        "recomendas": recomendas
    }

if __name__ == "__main__":
    # Dataset de Treino Embutido (Mock de Issues de Startups)
    train_data = [
        ("A API do iFood está muito estável e rápida hoje.", {"cats": {"POSITIVO": 1, "NEGATIVO": 0, "NEUTRO": 0}}),
        ("Adorei a facilidade de abrir conta no Nubank.", {"cats": {"POSITIVO": 1, "NEGATIVO": 0, "NEUTRO": 0}}),
        ("Creditas liberou meu crédito em tempo recorde!", {"cats": {"POSITIVO": 1, "NEGATIVO": 0, "NEUTRO": 0}}),
        ("Stone é o melhor parceiro para meu pequeno negócio.", {"cats": {"POSITIVO": 1, "NEGATIVO": 0, "NEUTRO": 0}}),
        ("Issue resolvida rapidamente, excelente suporte.", {"cats": {"POSITIVO": 1, "NEGATIVO": 0, "NEUTRO": 0}}),
        ("Interface do QuintoAndar é muito intuitiva.", {"cats": {"POSITIVO": 1, "NEGATIVO": 0, "NEUTRO": 0}}),
        ("Documentação clara ajuda muito no deploy.", {"cats": {"POSITIVO": 1, "NEGATIVO": 0, "NEUTRO": 0}}),
        ("Sistema fora do ar, impossível pagar boletos.", {"cats": {"POSITIVO": 0, "NEGATIVO": 1, "NEUTRO": 0}}),
        ("App trava o tempo todo na tela de login.", {"cats": {"POSITIVO": 0, "NEGATIVO": 1, "NEUTRO": 0}}),
        ("Péssimo atendimento, ninguém resolve meu erro.", {"cats": {"POSITIVO": 0, "NEGATIVO": 1, "NEUTRO": 0}}),
        ("Taxas da Stone estão aumentando sem aviso.", {"cats": {"POSITIVO": 0, "NEGATIVO": 1, "NEUTRO": 0}}),
        ("Bug crítico no checkout do iFood.", {"cats": {"POSITIVO": 0, "NEGATIVO": 1, "NEUTRO": 0}}),
        ("O Nubank lançou um novo layout hoje.", {"cats": {"POSITIVO": 0, "NEGATIVO": 0, "NEUTRO": 1}}),
        ("Atualização de versão 1.2.3 pendente.", {"cats": {"POSITIVO": 0, "NEGATIVO": 0, "NEUTRO": 1}}),
        ("O mercado de fintechs está crescendo no Brasil.", {"cats": {"POSITIVO": 0, "NEGATIVO": 0, "NEUTRO": 1}}),
        ("Reunião de roadmap agendada para sexta.", {"cats": {"POSITIVO": 0, "NEGATIVO": 0, "NEUTRO": 1}}),
        ("Verificando logs do servidor.", {"cats": {"POSITIVO": 0, "NEGATIVO": 0, "NEUTRO": 1}}),
        ("Startup captou 50 milhões em rodada Série B.", {"cats": {"POSITIVO": 1, "NEGATIVO": 0, "NEUTRO": 0}}),
        ("Lançamento oficial da plataforma em SP.", {"cats": {"POSITIVO": 1, "NEGATIVO": 0, "NEUTRO": 0}}),
        ("Erro de conexão persistente na API.", {"cats": {"POSITIVO": 0, "NEGATIVO": 1, "NEUTRO": 0}}),
    ]
    
    # 1. Pipeline spaCy
    nlp_spacy = criar_modelo_textcat()
    historico = treinar_textcat(nlp_spacy, train_data, n_epocas=20)
    # plotar_loss(historico)
    
    # 2. Pipeline Transformers
    # try:
    #     clf_bert = carregar_transformer()
    #     texts = [d[0] for d in train_data[:5]]
    #     results = analisar_sentimento_bert(texts, clf_bert)
    #     print(results)
    # except Exception as e:
    #     print(f"Transformers fail (normal for local dry runs): {e}")
    
    print("\n--- ARKOS MI SENTIMENT ENGINE INITIALIZED ---")
    print("Módulo pronto para processamento híbrido e cálculo do Health Index.")
