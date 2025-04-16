import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Função do terreno (a montanha)
def f(x):
    return math.sin(5 * x) * (1 - math.tanh(x ** 2))

# parametros do Simulated Annealing
T = 1.0             # temperatura inicial
alpha = 0.95        # fator resfriamtno
max_iter = 100      # iterações
x = random.uniform(-2, 2)  # começa em ponto aleatório (dentro do dominio)
best_x = x
best_fx = f(x)

# plot caminho
history = [x]

while T > 1e-4: #(1^-4)
    for _ in range(max_iter):
        # gera vizinho próximo
        epsilon = random.uniform(-0.1, 0.1)
        # posicao aleatoria
        x_new = x + epsilon

        # mantém no intervalo [-2, 2]
        x_new = max(min(x_new, 2), -2)

        fx = f(x)
        fx_new = f(x_new)
        delta = fx_new - fx

        # aceita se for melhor OU com certa probabilidade se for pior
        if delta > 0 or random.random() < math.exp(delta / T):
            x = x_new
            if fx_new > best_fx:
                best_x = x_new
                best_fx = fx_new
            history.append(x)

    T *= alpha  # Resfriamento

# plota a função e o caminho do drone
x_vals = np.linspace(-2, 2, 1000)
y_vals = [f(x) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.plot(history, [f(x) for x in history], 'r.-', label='Caminho do SA')
plt.scatter(best_x, best_fx, color='green', label='Melhor ponto', zorder=5)
plt.title('Simulated Annealing - Ponto mais alto da montanha')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
