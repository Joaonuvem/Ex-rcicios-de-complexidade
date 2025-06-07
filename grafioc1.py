import numpy as np
import matplotlib.pyplot as plt

n_values = np.arange(5, 36, 3)

# Tempos hipotéticos (segundos)
time_original = 1e-7 * 2**n_values
time_optimized1 = 5e-6 * n_values

plt.figure(figsize=(8,5))
plt.plot(n_values, time_original, 'b-o', label='Algoritmo Original')
plt.plot(n_values, time_optimized1, 'r-s', label='Algoritmo Otimizado 1 (Memoização)')
plt.xlabel('Tamanho do Problema (n)')
plt.ylabel('Tempo Médio (segundos)')
plt.title('Comparação: Algoritmo Original x Otimizado 1')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
