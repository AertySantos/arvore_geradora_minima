# Algoritmos de Kruskal e Prim

## Descrição

Este projeto implementa dois algoritmos clássicos para encontrar a **Árvore Geradora Mínima (MST)** de um grafo não direcionado ponderado: **Kruskal** e **Prim**. Ambos os algoritmos buscam uma subárvore que conecta todos os vértices do grafo com o menor peso total possível, mas fazem isso de maneiras diferentes.

### O que é uma Árvore Geradora Mínima?

Em um grafo não direcionado e conectado, uma **Árvore Geradora Mínima (MST)** é uma subárvore que inclui todos os vértices do grafo e a soma dos pesos das arestas é a menor possível. Ou seja, a MST conecta todos os vértices com o mínimo custo.

---

## Algoritmo de Kruskal

O algoritmo de Kruskal funciona adicionando arestas à MST de acordo com o menor peso, sem formar ciclos. Ele utiliza a **Técnica de Conjuntos Disjuntos** (Union-Find) para evitar a criação de ciclos.

### Etapas:

1. **Ordenar** todas as arestas do grafo pelo peso em ordem crescente.
2. Para cada aresta, **adicioná-la** à árvore geradora se ela não formar um ciclo (utilizando Union-Find para checar ciclos).
3. Repetir o processo até que todos os vértices estejam conectados.

### Complexidade:
- **Tempo**: \( O(E \log E) \), onde \( E \) é o número de arestas, devido à ordenação das arestas e à operação de união.
- **Uso**: Kruskal é mais eficiente quando o grafo é esparso (menos arestas).

---

## Algoritmo de Prim

O algoritmo de Prim constrói a MST de maneira progressiva, partindo de um vértice inicial e expandindo a árvore adicionando as arestas de menor peso que conectam um vértice fora da árvore a um vértice dentro dela.

### Etapas:

1. **Escolher** um vértice inicial arbitrário.
2. Para cada vértice, **adicionar** à árvore a aresta de menor peso que o conecta a um vértice já presente na árvore.
3. Repetir até que todos os vértices estejam na árvore.

### Complexidade:
- **Tempo**: \( O(E \log V) \), onde \( V \) é o número de vértices e \( E \) o número de arestas, usando uma fila de prioridade para obter o próximo vértice de menor peso.
- **Uso**: Prim é geralmente mais eficiente em grafos densos (muitas arestas).

---

## Comparação

| Aspecto        | Kruskal                        | Prim                           |
|----------------|--------------------------------|--------------------------------|
| Abordagem      | Seleciona as arestas de menor peso e adiciona à árvore | Expande a partir de um vértice inicial |
| Complexidade   | \( O(E \log E) \)              | \( O(E \log V) \)              |
| Melhor para    | Grafos esparsos                | Grafos densos                  |
| Método         | Conjuntos disjuntos (Union-Find) | Fila de prioridade (Min-Heap)  |

---

## Como Executar

### Pré-requisitos

- Python 3.x
- Bibliotecas: `heapq` para Prim e uma implementação de Union-Find para Kruskal.

### Execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/AertySantos/arvore_geradora_minima.git
   cd arvore_geradora_minima
   ```

2. Execute o script para Kruskal ou Prim:

   ```bash
   python kruskal.py
   python prim.py
   ```

3. O programa solicitará a entrada do grafo, como a lista de vértices e arestas com pesos.

---

## Exemplo de Entrada

Entrada para um grafo com 4 vértices e 5 arestas:

```
4 5
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4
```

### Saída esperada:

**Kruskal** ou **Prim** fornecerão a MST com peso mínimo e as arestas selecionadas.

---

## Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C. (2009). Introduction to
Algorithms. MIT Press.
- Diestel, R. (2000). Graph Theory. Springer.
- Kruskal, J. B. (1956). On the shortest spanning subtree of a graph and the traveling
salesman problem. In Proceedings of the American Mathematical Society
