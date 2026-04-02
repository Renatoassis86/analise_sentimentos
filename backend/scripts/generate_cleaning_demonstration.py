"""
GENERATE CLEANING DEMONSTRATION v1.0
Este script gera os metadados detalhados da pipeline de limpeza e PLN
para visualização no dashboard (Sessão: Behind the Scenes).
"""

import json
import re
import spacy
from collections import Counter

# Tente carregar o modelo spaCy
try:
    nlp = spacy.load("pt_core_news_sm")
except:
    nlp = None

def get_demo_metrics():
    # 1. TEXTO BRUTO (RUIDOSO)
    raw_text = """
    # PROJETO: Neural PlatformPay (v2.5.1) 🚀
    
    [![Build Status](https://img.shields.io/travis/pay.svg)](url)
    
    Este é o sistema disruptivo de **pagamentos** da @NeuralPlatform.
    Contato em: sac@neuralpay.com.br ou https://neuralpay.com.br/docs/api
    
    ## Instalação
    ```bash
    pip install neuralpay
    ```
    
    ### Erros comuns (#404, #500):
    - Falha de conexão
    - Timeout de API
    """

    # 2. TRACKING REGEX
    original_tokens = len(raw_text.split())
    
    # Simulação de passos de limpeza
    steps = []
    
    # Passo 1: Markdown
    step1_text = re.sub(r'```[\s\S]*?```', '', raw_text) # Blocos de código
    step1_text = re.sub(r'!\[.*?\]\(.*?\)', '', step1_text) # Imagens
    step1_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', step1_text) # Links
    step1_text = re.sub(r'#{1,6}\s', '', step1_text) # Headers
    markdown_removed = original_tokens - len(step1_text.split())
    steps.append({"name": "Markdown Removal", "removed": markdown_removed, "type": "Regex"})

    # Passo 2: Padrões Específicos
    step2_text = re.sub(r'[a-zA-Z0-9._%+-]+Resource@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', step1_text) # Emails
    step2_text = re.sub(r'https?://\S+', '', step2_text) # URLs
    step2_text = re.sub(r'@[\w-]+', '', step2_text) # Mentions
    entities_removed = len(step1_text.split()) - len(step2_text.split())
    steps.append({"name": "Technical Entities", "removed": entities_removed, "type": "Regex"})

    # Passo 3: Normalização
    step3_text = re.sub(r'[^\w\s]', '', step2_text) # Símbolos
    step3_text = re.sub(r'\s+', ' ', step3_text).strip().lower()
    norm_removed = len(step2_text.split()) - len(step3_text.split())
    steps.append({"name": "Normalization", "removed": norm_removed, "type": "Regex"})

    cleaned_text_regex = step3_text
    tokens_after_regex = len(cleaned_text_regex.split())

    # 3. SPACY PROCESSING
    spacy_data = {}
    if nlp:
        doc = nlp(cleaned_text_regex)
        spacy_data = {
            "pos": dict(Counter([token.pos_ for token in doc])),
            "lemmas": [token.lemma_ for token in doc if not token.is_stop],
            "entities": [{"text": ent.text, "label": ent.label_} for ent in doc.ents],
            "removed_stopwords": len([token for token in doc if token.is_stop])
        }
        steps.append({"name": "Stopwords Removal", "removed": spacy_data["removed_stopwords"], "type": "spaCy"})
    else:
        # Mock data se não tiver spaCy
        spacy_data = {
            "pos": {"NOUN": 15, "ADJ": 8, "VERB": 5, "ADV": 2},
            "lemmas": ["sistema", "disruptivo", "pagamento", "neuralplatform"],
            "entities": [{"text": "NeuralPlatform", "label": "ORG"}],
            "removed_stopwords": 12
        }
        steps.append({"name": "Stopwords Removal", "removed": 12, "type": "spaCy"})

    # 4. FINAL JSON
    demo_data = {
        "raw_sample": raw_text.strip(),
        "cleaned_sample": cleaned_text_regex,
        "token_audit": {
            "initial": original_tokens,
            "after_regex": tokens_after_regex,
            "final_pln": len(spacy_data["lemmas"]),
            "reduction_pct": round((1 - (len(spacy_data["lemmas"]) / original_tokens)) * 100, 2)
        },
        "cleaning_steps": steps,
        "spacy_audit": spacy_data
    }

    return demo_data

if __name__ == "__main__":
    data = get_demo_metrics()
    with open('d:/repositorio_geral/modalagem_n_esturturado/analise_sentimentos/frontend/cleaning_demo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Dashboard Demonstration Data Generated: /frontend/cleaning_demo.json")
