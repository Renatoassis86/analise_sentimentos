"""
MASTER PIPELINE v7.9 (Integrated Audit Dashboard)
Lê o banco de dados, executa a auditoria em lote e sincroniza o Dashboard.
Integra Scripts p/ gerar dados reais (JSON).
"""

import json
from audit_engine import AuditEngine
from stats_model import model_benchmarks

def run_all_fintechs():
    """
    Roda a auditoria algorítmica MiNER em cada uma das 20 Fintechs do banco.
    """
    engine = AuditEngine(data_path='frontend/data.json')
    results = []

    print(f"--- INICIANDO LOTE DE AUDITORIA (N=20) ---")
    
    for startup in engine.data['startups']:
        # Simula o pipeline MiNER p/ cada startup
        report = engine.run_miner(startup['name'].split(' (')[0])
        results.append(report)
        print(f"Startup: {startup['name']} -> SHA: {report['sha_score']}%")

    # Exporta o JSON Consolidado de Resultados Integrados
    with open("backend/outputs/integrated_audit_final.json", "w", encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    
    print("\n--- SINCRONIZAÇÃO COMPLETA: backend/outputs/integrated_audit_final.json ---")

if __name__ == "__main__":
    run_all_fintechs()
