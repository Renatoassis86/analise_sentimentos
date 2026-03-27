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
    try:
        resp = requests.get(url_repo, headers=headers)
        if resp.status_code != 200:
            print(f"❌ Erro ao buscar {repo_full_name}: {resp.status_code}")
            return None
        resp_repo = resp.json()
    except Exception as e:
        print(f"❌ Falha de conexão: {e}")
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
    score = min(98, max(45, (stars / 100) + (num_commits * 0.8) - (num_issues * 0.2) + 65))
    
    entity_density = {
        "Cloud": int(stars % 15) + 5,
        "Python": int(num_commits % 20) + 10,
        "Security": int(num_issues % 10) + 12,
        "Scalability": stars // 100 + 5
    }

    return {
        "id": repo_full_name.split("/")[-1].lower(),
        "name": repo_full_name.split("/")[0].upper() + " / " + resp_repo.get("name"),
        "health_score": round(score, 1),
        "interpretation": f"A presença digital da empresa {repo_full_name.split('/')[0]} é robusta. O repositório possui {stars} estrelas e atividade constante.",
        "prescription": f"Manter a governança sobre as {num_issues} issues abertas. O radar Marketing Intelligence sugere blindagem estratégica.",
        "insight": "Referência de Engenharia Brasileira.",
        "recommendations": [
            "Monitorar novas forks ativos",
            "Otimizar tempo de fechamento de bugs",
            "Manter pipelines de CI/CD verdes"
        ],
        "entity_density": entity_density
    }

def sync_all():
    # Repositórios Verificados (Unicórnios Brasileiros)
    repos = [
        "nubank/fklearn",
        "nubank/mockfn",
        "stone-payments/pos-mamba-sdk",
        "pagseguro/pagseguro-sdk-php",
        "quintoandar/validations-engine",
        "creditas/p-queue"
    ]
    
    results = []
    
    # Adicionar o Mock de Crise obrigatório
    results.append({
        "id": "fintech_x_(crise)",
        "name": "FINTECH X (Modo Crise)",
        "health_score": 38.2,
        "interpretation": "Anomalia detectada em canais não estruturados. Queda de 60% na confiança digital.",
        "prescription": "Paralisar novos lançamentos. Estabelecer sala de guerra PR e Jurídico.",
        "insight": "Sinal de Alerta Crítico.",
        "recommendations": ["Auditoria Forense de Dados", "Plano de Resposta a Incidentes"],
        "entity_density": {"Crise": 45, "Justiça": 30, "PROCON": 25}
    })

    for repo in repos:
        data = fetch_github_data(repo)
        if data:
            results.append(data)

    final_json = {"startups": results}
    save_path = "analise_sentimentos/frontend/data.json"
    
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Sincronização finalizada: {len(results)} empresas mapeadas.")

if __name__ == "__main__":
    sync_all()
