import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Estilo Dark/Neon
plt.style.use('dark_background')
accent_color = '#B6FF00'
cyan_color = '#5EFCFC'

# 1. CHART: RANKING SHA 4D (TOP 10)
fintechs = ['Stark Bank', 'Stone', 'Creditas', 'Pismo', 'Nu', 'PagSeguro', 'C6 Bank', 'PicPay', 'Inter', 'Neon']
scores = [98.2, 92.5, 91.8, 89.4, 86.8, 85.1, 82.4, 79.5, 78.2, 75.0]

plt.figure(figsize=(10, 6))
bars = plt.barh(fintechs[::-1], scores[::-1], color=accent_color)
plt.xlabel('SHA Score (%)', color='white', fontsize=12)
plt.title('Ranking MiNER: Solvência de Ativos (N=20)', color=cyan_color, fontsize=14, pad=20)
plt.grid(axis='x', linestyle='--', alpha=0.3)
plt.xlim(0, 100)
# Add labels
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}%', va='center', color='white', fontweight='bold')

plt.tight_layout()
plt.savefig(r'd:\repositorio_geral\modalagem_n_esturturado\assets\final_prints\chart_ranking.png', dpi=300)
plt.close()

# 2. CHART: BENCHMARKING MODELOS
metrics = ['Precision', 'Recall', 'F1-Score']
vader = [74.1, 71.0, 72.0]
tfidf = [78.4, 75.2, 77.0]
miner = [95.2, 93.8, 94.0]

x = np.arange(len(metrics))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width, vader, width, label='VADER', color='#888888')
ax.bar(x, tfidf, width, label='TF-IDF', color=cyan_color)
ax.bar(x + width, miner, width, label='MiNER (RoBERTa)', color=accent_color)

ax.set_ylabel('Performance (%)', color='white')
ax.set_title('Benchmarking: Modelagem Neuro-Estatística', color=accent_color, fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()
plt.ylim(0, 110)
plt.grid(axis='y', alpha=0.2)
plt.savefig(r'd:\repositorio_geral\modalagem_n_esturturado\assets\final_prints\chart_benchmark.png', dpi=300)
plt.close()

# 3. CHART: DISTRIBUIÇÃO DE RISCO (PIE)
labels = ['GOLD (Sólida)', 'SOLID (Estável)', 'ALERT (Crítica)']
sizes = [5, 65, 30]
colors = [accent_color, cyan_color, '#FF3E3E']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, textprops={'color':"w", 'weight':'bold'})
plt.title('Distribuição de Risco Algorítmico (Amostra)', color='white', fontsize=14)
plt.savefig(r'd:\repositorio_geral\modalagem_n_esturturado\assets\final_prints\chart_risk_dist.png', dpi=300)
plt.close()

print("Imagens acadêmicas geradas com sucesso em assets/final_prints/")
