import os
import json
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_github_data(repo_full_name):
    """Puxa dados reais do GitHub para uma empresa/repo."""
    print(f"📡 Buscando dados para: {repo_full_name}...")
    
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    
    # 1. Dados Básicos do Repo
    url_repo = f"https://api.github.com/repos/{repo_full_name}"
    resp_repo = requests.get(url_repo, headers=headers).json()
    
    if "name" not in resp_repo:
        print(f"❌ Erro ao buscar {repo_full_name}: {resp_repo.get('message')}")
        return None

    # 2. Issues (Proxy de interação)
    url_issues = f"https://api.github.com/repos/{repo_full_name}/issues?state=open"
    resp_issues = requests.get(url_issues, headers=headers).json()
    num_issues = len(resp_issues) if isinstance(resp_issues, list) else 0

    # 3. Commits (Proxy de atividade)
    url_commits = f"https://api.github.com/repos/{repo_full_name}/commits"
    resp_commits = requests.get(url_commits, headers=headers).json()
    num_commits = len(resp_commits) if isinstance(resp_commits, list) else 0

    stars = resp_repo.get("stargazers_count", 0)
    score = min(98, max(45, (stars / 100) + (num_commits * 0.8) - (num_issues * 0.2)))
    
    entity_density = {
        "Cloud": int(stars % 15) + 5,
        "Python": int(num_commits % 20) + 10,
        "Security": int(num_issues % 10) + 8,
        "Scalability": stars // 100
    }

    return {
        "id": repo_full_name.split("/")[-1].lower(),
        "name": resp_repo.get("name").upper(),
        "health_score": round(score, 1),
        "interpretation": f"A presença digital do repositório {repo_full_name} é alta, com {stars} estrelas. A base de código está em movimento contínuo.",
        "prescription": "Promover maior documentação para issues abertas. O radar Arkos sugere blindagem estratégica da infraestrutura.",
        "insight": "Referência Técnica no Setor.",
        "recommendations": [
            "Manter cobertura CI/CD ativa",
            "Refatorar módulos legados",
            "Expandir testes de integração"
        ],
        "entity_density": entity_density
    }

def sync_all():
    # Repositórios Reais e Existentes:
    repos = [
        "nubank/fk-it",
        "nubank/mockfn",
        "ifood/ifood-engineering-principles"
    ]
    
    results = []
    
    # Adicionar o Mock de Crise para propósitos de demonstração (Obrigatório pela Gestão Arkos)
    results.append({
        "id": "fintech_x_(crise)",
        "name": "FINTECH X (CRISE)",
        "health_score": 38.2,
        "interpretation": "Queda brusca na reputação digital detectada. Mismatch entre narrativa e código.",
        "prescription": "Garantir blindagem de dados e transparência com stakeholders.",
        "insight": "Sinal de Alerta Crítico.",
        "recommendations": ["Auditoria de Segurança", "Plano de Resposta Rápida"],
        "entity_density": {"Crise": 45, "Risco": 30, "Security": 5}
    })

    for repo in repos:
        data = fetch_github_data(repo)
        if data:
            results.append(data)

    final_json = {"startups": results}
    
    # Caminho corrigido para rodar da raiz
    save_path = "analise_sentimentos/frontend/data.json"
    
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Arquivo {save_path} atualizado com sucesso!")

if __name__ == "__main__":
    sync_all()
