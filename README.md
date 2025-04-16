#  Simulated Annealing: Encontrando o Ponto Mais Alto em um Terreno

Este projeto implementa o algoritmo de **Simulated Annealing** em Python para resolver um problema de otimização: **encontrar o ponto mais alto de uma montanha fictícia** representada por uma função matemática.

---

## Descrição do Problema

Imagine que você é um **drone explorador** tentando encontrar o pico mais alto de uma cadeia de montanhas. Essas montanhas são descritas por uma função matemática com vários picos e vales:

\[
f(x) = \sin(5x) \cdot (1 - \tanh(x^2))
\]

- **Domínio:** \( x \in [-2, 2] \)
- A função tem **muitos máximos locais**, dificultando encontrar o **máximo global**.

---

## Algoritmo Usado: Simulated Annealing

### Intuição:
- No início, o drone aceita andar mesmo que o caminho **piora**.
- Com o tempo (à medida que a temperatura diminui), ele se torna mais **seletivo** e aceita apenas melhorias.
- Isso ajuda a evitar ficar preso em picos menores.

### Parâmetros definidos:

| Parâmetro              | Valor         |
|------------------------|---------------|
| Temperatura inicial    | `T = 1.0`     |
| Taxa de resfriamento   | `alpha = 0.95`|
| Iterações por temperatura | `100`     |
| Vizinhança (epsilon)   | `[-0.1, 0.1]` |

---
