"""
Módulo de Coleta e Web Scraping - ARKOS MI
Este módulo integra APIs públicas e técnicas de scraping com BeautifulSoup 
para alimentar o Startup Signal Intelligence.

Autor: Renato Assis | ARKOS Intelligence
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px

def coletar_github_repos(org_name):
    """
    Simulação de coleta de repositórios via GitHub API pública.
    """
    url = f"https://api.github.com/orgs/{org_name}/repos"
    print(f"Buscando repositórios da organização: {org_name}...")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            repos = response.json()
            return pd.DataFrame([{
                "Nome": r["name"],
                "Descrição": r["description"],
                "Estrelas": r["stargazers_count"],
                "Linguagem": r["language"],
                "Data Criacao": r["created_at"]
            } for r in repos])
        else:
            print(f"Erro {response.status_code}: {response.text}")
            return pd.DataFrame()
    except Exception as e:
        print(f"Erro na coleta GitHub: {e}")
        return pd.DataFrame()

def coletar_brasilapi_corretoras():
    """
    Coleta dados de corretoras via BrasilAPI para análise de mercado financeiro.
    """
    url = "https://brasilapi.com.br/api/cvm/corretora/v1"
    print("Coletando dados de corretoras na BrasilAPI (CVM)...")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            dados = response.json()
            # Pegando as 50 primeiras para exemplo
            df = pd.DataFrame(dados[:50])
            return df
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro na BrasilAPI: {e}")
        return pd.DataFrame()

def scraping_quotes_demo():
    """
    Exemplo de web scraping com BeautifulSoup no site Quotes to Scrape.
    """
    url = "http://quotes.toscrape.com/"
    print(f"Iniciando scraping em {url}...")
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        quotes = []
        for item in soup.find_all('div', class_='quote'):
            text = item.find('span', class_='text').text
            author = item.find('small', class_='author').text
            tags = [tag.text for tag in item.find_all('a', class_='tag')]
            quotes.append({"Texto": text, "Autor": author, "Tags": ", ".join(tags)})
            
        return pd.DataFrame(quotes)
    except Exception as e:
        print(f"Erro no scraping: {e}")
        return pd.DataFrame()

def gerar_grafico_bolhas_corretoras(df):
    """
    Gera um gráfico Plotly de bolhas para as corretoras brasileiras.
    """
    if df.empty:
        return None
        
    # Agrupando por UF (simplificação do gráfico)
    df_count = df.groupby('uf').size().reset_index(name='Quantidade')
    
    fig = px.scatter(df_count, x='uf', y='Quantidade', size='Quantidade',
                     color='uf', title="Distribuição de Corretoras por Estado (BrasilAPI)",
                     labels={'uf': 'Estado'}, template='plotly_dark')
    return fig

if __name__ == "__main__":
    print("--- ARKOS MI coleta.py Demo ---")
    df_gh = coletar_github_repos("arkos-intelligence") # Exemplo
    print(df_gh.head() if not df_gh.empty else "Nenhum dado GitHub.")
    
    df_quotes = scraping_quotes_demo()
    print(df_quotes.head())
