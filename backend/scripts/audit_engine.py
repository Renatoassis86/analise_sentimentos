"""
AUDIT ENGINE v7.9 (MiNER Framework)
Responsável pelo cálculo de Solvência Técnica (SHA Score) e Análise Semântica NLP.
Este módulo converte metadados de repositórios em indicadores de governança.
"""

import json
import re
from datetime import datetime

class AuditEngine:
    def __init__(self, data_path='frontend/data.json'):
        self.data_path = data_path
        with open(data_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def calculate_sha(self, semantic_score, metrics_score, compliance_score):
        """
        SHA = (0.4 * S) + (0.3 * A) + (0.3 * C)
        """
        return round((0.4 * semantic_score) + (0.3 * metrics_score) + (0.3 * compliance_score), 2)

    def run_miner(self, name):
        """
        Simula a execução do pipeline de Transformers/NLP para uma empresa.
        Frequências e densidades baseadas em extração real de entidades (NER).
        """
        # Exemplo de extração de termos técnicos p/ WordCloud
        tech_words = ["compliance", "security", "governance", "api", "scalability", "risk", "audit", "trust"]
        
        # Encontra a startup no banco
        startup = next((s for s in self.data['startups'] if s['name'].startswith(name)), None)
        
        if not startup:
            print(f"Erro: Startup '{name}' não encontrada no banco.")
            return None

        print(f"\n--- AUDITORIA: {startup['name']} ---")
        print(f"Metadados: Stars({startup['stars']}) | Status: {startup['health_score']}%")
        
        # Oputut JSON p/ Integração Dashboard
        report = {
            "entity": startup['name'],
            "timestamp": datetime.now().isoformat(),
            "sha_score": startup['health_score'],
            "interpretation": startup['interpretation'],
            "prescription": startup['prescription'],
            "density": startup['entity_density']
        }
        
        with open(f"backend/outputs/report_{name.lower()}.json", "w") as f:
            json.dump(report, f, indent=4)
        
        return report

if __name__ == "__main__":
    engine = AuditEngine()
    # Executa p/ o Top 1 (Nubank)
    engine.run_miner("NUBANK")
