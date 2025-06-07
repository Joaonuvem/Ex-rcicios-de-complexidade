import numpy as np
import matplotlib.pyplot as plt

# Configurações do gráfico
plt.style.use('seaborn')
plt.figure(figsize=(10, 6))

# Valores de n
n_values = np.arange(4, 26, 2)

# Tempos simulados (i5 11ª geração)
original_times = [0.00001 * (1.8 ** n) for n in n_values]
opt1_times = [0.00002 * n for n in n_values]

# Plotando
plt.plot(n_values, original_times, 'b-o', linewidth=2, markersize=8, label='Algoritmo Original')
plt.plot(n_values, opt1_times, 'r-s', linewidth=2, markersize=8, label='Com Memoização')

# Configurações do gráfico
plt.title('Comparação: Algoritmo Original vs Versão com Memoização', pad=20)
plt.xlabel('Tamanho do Problema (n)', labelpad=10)
plt.ylabel('Tempo Médio (segundos)', labelpad=10)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(n_values)

# Salvar como PNG
plt.savefig('original_vs_memoizacao.png', dpi=300, bbox_inches='tight')
plt.show()
