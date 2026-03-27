"""
ARKOS MI — Exportador de Resultados para Frontend
Gera o arquivo de dados JSON que alimenta o Dashboard Interativo.
"""

import sys
import os
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg') # Evitar que o matplotlib tente abrir janelas (GUI) no background

# Caminhos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, 'src')
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

sys.path.append(SRC_DIR)

from pln_pipeline import *
from sentimentos import *
from limpeza import *

def processar_startup(nome, corpus, score_base=None):
    nlp = spacy.load("pt_core_news_sm")
    # Pipeline
    res = rodar_pipeline_completa(corpus, nlp)
    # Health Index
    health = calcular_health_index(corpus, None, nlp)
    if score_base:
        health['score'] = score_base # Forçar score para simulação de crise se necessário
    
    # Entidades para gráfico
    ents_count = res['entidades']['Tipo'].value_counts().to_dict()
    
    return {
        "id": nome.lower().replace(" ", "_"),
        "name": nome,
        "health_score": health['score'],
        "health_status": health['nivel'],
        "recommendations": health['recomendas'],
        "sentiment": "Positivo" if health['score'] > 60 else "Negativo",
        "top_chunks": [c[0] for c in res['top_chunks'][:3]],
        "entity_density": ents_count,
        "corpus_sample": corpus[0][:150] + "..."
    }

def main():
    print("🚀 Arkos MI: Processando dados para o Frontend...")
    
    # Case I: iFood
    corpus_ifood = [
        "A logística do iFood está impecável após a nova atualização de IA.",
        "O pedido chegou em 15 minutos, experiência incrível.",
        "Suporte do iFood resolveu meu problema com o cupom rapidamente.",
        "Parceria do iFood com novos restaurantes sustenta o crescimento do setor."
    ]
    
    # Case II: Fintech X (Crise)
    corpus_fintech_x = [
        "O app da Fintech X trava no login há 2 dias, ninguém responde.",
        "Tentei transferir meu saldo e deu erro de conexão persistente.",
        "O atendimento da Fintech X é inexistente, me sentindo abandonado.",
        "Mudaram o layout mas esqueceram de arrumar os bugs básicos."
    ]

    results = {
        "startups": [
            processar_startup("iFood (Líder)", corpus_ifood),
            processar_startup("Fintech X (Crise)", corpus_fintech_x, score_base=32.5)
        ],
        "system_status": {
            "version": "1.0.2-stable",
            "last_run": "2026-03-27T00:30:00Z",
            "active_nodes": 4
        }
    }

    output_path = os.path.join(FRONTEND_DIR, 'data.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Resultados exportados para: {output_path}")

if __name__ == "__main__":
    main()
