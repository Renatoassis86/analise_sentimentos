import os
import pandas as pd
import numpy as np
import logging
import time
import re
from datetime import datetime
import tweepy
import spacy
from tqdm import tqdm

# =============================================================================
# CONFIGURAÇÃO E DIRETÓRIOS
# =============================================================================
OUTPUT_DIR = "outputs"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

LOG_FILE = os.path.join(OUTPUT_DIR, "diario_bordo.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# =============================================================================
# CARREGAR E LIMPAR companies.csv
# =============================================================================
def load_and_preprocess_companies(file_path):
    logging.info("Carregando base de empresas...")
    try:
        # Lendo com tratamento de erro comum em CSVs do Kaggle
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='latin1')
    
    logging.info(f"Total de registros originais: {len(df)}")

    # Normalizar funding para float
    if 'funding_total_usd' in df.columns:
        df['funding_total_usd'] = pd.to_numeric(df['funding_total_usd'], errors='coerce').fillna(0)
    
    # Filtrar apenas as que possuem twitter_username
    df_with_twitter = df[df['twitter_username'].notna() & (df['twitter_username'] != '')].copy()
    
    # Ordenar por funding
    df_with_twitter = df_with_twitter.sort_values(by='funding_total_usd', ascending=False)
    
    output_path = os.path.join(OUTPUT_DIR, "companies_top_funding_with_twitter.csv")
    df_with_twitter.to_csv(output_path, index=False)
    
    logging.info(f"Total com Twitter: {len(df_with_twitter)}")
    return df_with_twitter

# =============================================================================
# COLETA X API (Tweepy v2)
# =============================================================================
def get_twitter_client():
    bearer_token = os.environ.get("X_BEARER_TOKEN")
    if not bearer_token:
        logging.error("ERRO: Variável de ambiente X_BEARER_TOKEN não encontrada.")
        return None
    return tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

def fetch_tweets_for_users(df_top, n_startups=50, tweets_per_startup=100):
    client = get_twitter_client()
    if not client:
        return None

    all_tweets = []
    output_tweets = os.path.join(OUTPUT_DIR, "tweets_raw.csv")

    for idx, row in tqdm(df_top.iloc[:n_startups].iterrows(), total=n_startups, desc="Coletando Tweets"):
        username = row['twitter_username']
        company_name = row['name']
        
        try:
            # Obter User ID
            user = client.get_user(username=username)
            if not user.data:
                logging.warning(f"Usuário {username} não encontrado.")
                continue
            
            user_id = user.data.id
            
            # Coletar tweets (100 por startup)
            paginator = tweepy.Paginator(
                client.get_users_tweets,
                id=user_id,
                max_results=100, # Limite por request
                tweet_fields=["created_at", "public_metrics", "lang"],
                limit=1 # Apenas 1 página para pegar os últimos 100
            )

            count = 0
            for page in paginator:
                if page.data:
                    for tweet in page.data:
                        tweet_data = {
                            "company_name": company_name,
                            "twitter_username": username,
                            "tweet_id": tweet.id,
                            "text": tweet.text,
                            "created_at": tweet.created_at,
                            "lang": tweet.lang,
                            "retweet_count": tweet.public_metrics['retweet_count'],
                            "reply_count": tweet.public_metrics['reply_count'],
                            "like_count": tweet.public_metrics['like_count'],
                            "quote_count": tweet.public_metrics['quote_count']
                        }
                        all_tweets.append(tweet_data)
                        count += 1
                if count >= tweets_per_startup:
                    break
            
            logging.info(f"Coletados {count} tweets para {company_name}")
            
            # Salvamento incremental
            pd.DataFrame(all_tweets).to_csv(output_tweets, index=False)

        except tweepy.TooManyRequests:
            logging.warning("Limite de requisições atingido. Aguardando...")
            time.sleep(60)
        except Exception as e:
            logging.error(f"Erro ao coletar para {username}: {str(e)}")
            continue

    return pd.DataFrame(all_tweets)

# =============================================================================
# ETAPA 1: REGEX + SPACY
# =============================================================================
def narrative_analysis(df_companies):
    logging.info("Iniciando análise de narrativa (Etapa 1)...")
    
    try:
        nlp = spacy.load("en_core_web_sm")
    except:
        logging.error("Modelo do spaCy não encontrado. Execute: python -m spacy download en_core_web_sm")
        return None

    # Keywords de narrativa
    keywords = {
        'has_problem': r'\b(problem|challenge|issue|pain|gap|difficulty)\b',
        'has_solution': r'\b(solution|solve|platform|tool|service|product|feature)\b',
        'has_mission': r'\b(mission|vision|aim|goal|objective|purpose|dedicate)\b',
        'has_impact': r'\b(impact|change|transform|improve|help|better|future|environment)\b',
        'has_innovation': r'\b(innovation|disrupt|breakthrough|unique|technology|ai|modern)\b'
    }

    def regex_extract(text):
        if not isinstance(text, str): return {k: 0 for k in keywords}
        text = text.lower()
        results = {}
        for key, pattern in keywords.items():
            results[key] = 1 if re.search(pattern, text) else 0
        
        # Valores monetários e datas
        results['has_money'] = 1 if re.search(r'(\$|usd|million|billion)', text) else 0
        results['has_date'] = 1 if re.search(r'\b(19|20)\d{2}\b', text) else 0
        return results

    results_list = []
    
    # Usar colunas description/overview/short_description
    cols_to_use = ['description', 'overview', 'short_description']
    df_companies['full_text'] = df_companies[df_companies.columns.intersection(cols_to_use)].fillna('').agg(' '.join, axis=1)

    for idx, row in tqdm(df_companies.iterrows(), total=len(df_companies), desc="Processando NLP"):
        text = row['full_text']
        
        # Regex
        reg_features = regex_extract(text)
        
        # spaCy
        doc = nlp(text[:1000000]) # Evitar textos absurdamente longos
        entities = [ent.label_ for ent in doc.ents]
        
        n_org = entities.count('ORG')
        n_person = entities.count('PERSON')
        n_gpe = entities.count('GPE')
        
        # Narrative Score
        score = (reg_features['has_problem'] + reg_features['has_solution'] + 
                 reg_features['has_mission'] + reg_features['has_impact']) + (n_org * 0.1)
        
        res = {
            "name": row['name'],
            "funding_total_usd": row['funding_total_usd'],
            "twitter_username": row['twitter_username'],
            **reg_features,
            "n_org": n_org,
            "n_person": n_person,
            "n_gpe": n_gpe,
            "narrative_score": round(score, 2)
        }
        results_list.append(res)

    df_narrative = pd.DataFrame(results_list)
    output_path = os.path.join(OUTPUT_DIR, "etapa1_narrative_features.csv")
    df_narrative.to_csv(output_path, index=False)
    
    return df_narrative

# =============================================================================
# MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    logging.info("INICIANDO PROJETO FINAL")
    
    # 1. Preparar base
    df_companies = load_and_preprocess_companies("companies.csv")
    
    # 2. Coleta de Tweets
    # (Reduzido para 10 startups no exemplo para ser rápido, mude conforme necessário)
    df_tweets = fetch_tweets_for_users(df_companies, n_startups=20, tweets_per_startup=100)
    
    # 3. Análise de Narrativa
    df_narrative = narrative_analysis(df_companies.head(200)) # Analisando top 200 para dar corpo ao dataset
    
    if df_narrative is not None:
        print("\n=== TOP 15 STARTUPS POR NARRATIVE SCORE ===")
        print(df_narrative.sort_values(by='narrative_score', ascending=False).head(15)[['name', 'narrative_score', 'has_mission', 'n_org']])

    logging.info("PROCESSO CONCLUÍDO COM SUCESSO.")
