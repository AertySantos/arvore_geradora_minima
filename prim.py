# Importando as bibliotecas necessárias
import networkx as nx  # Para manipulação de grafos
import matplotlib.pyplot as plt  # Para visualização de gráficos

# Definindo constantes e a matriz de adjacência original
INF = 9999999  # Um valor infinito para comparação
V = 6  # Número de vértices no grafo
# Matriz de adjacência representando as arestas entre os vértices
G_matrix = [
    [0, 4, 4, 0, 0, 0],  # Arestas partindo do vértice 0
    [4, 0, 2, 0, 0, 0],  # Arestas partindo do vértice 1
    [4, 2, 0, 3, 4, 2],  # Arestas partindo do vértice 2
    [0, 0, 3, 0, 3, 0],  # Arestas partindo do vértice 3
    [0, 0, 4, 3, 0, 3],  # Arestas partindo do vértice 4
    [0, 0, 2, 0, 3, 0]   # Arestas partindo do vértice 5
]



# Criando o grafo original a partir da matriz de adjacência
G = nx.Graph()  # Inicializando um objeto de grafo
for i in range(V):
    for j in range(i + 1, V):  # Evita duplicar arestas em um grafo não direcionado
        if G_matrix[i][j] != 0:  # Se há uma aresta entre os vértices
            G.add_edge(i, j, weight=G_matrix[i][j])  # Adiciona a aresta ao grafo com seu peso

# Visualização do grafo original
pos = nx.spring_layout(G)  # Calcula a posição dos nós usando um layout de mola
plt.figure(figsize=(8, 6))  # Define o tamanho da figura
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700)  # Desenha o grafo
labels = nx.get_edge_attributes(G, 'weight')  # Obtém os rótulos das arestas
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Desenha os rótulos das arestas
plt.title("Grafo Original")  # Título do gráfico
plt.show()  # Exibe o gráfico



# Array para controlar os vértices selecionados na MST
selected = [False] * V  # Inicializa uma lista de seleção para os vértices
selected[0] = True  # Começando do vértice 0 como selecionado

arestas = 0  # Número de arestas na Árvore Geradora Mínima (MST)
mst_edges = []  # Lista para armazenar as arestas da MST

print("Edge : Weight\n")  # Cabeçalho para a exibição das arestas da MST

while arestas < V - 1:  # Enquanto o número de arestas for menor que V-1
    minimum = INF  # Inicializa o mínimo como infinito
    x = 0  # Vértice do qual a aresta mínima é selecionada
    y = 0  # Vértice para o qual a aresta mínima é selecionada
    # Procurar a aresta mínima entre os vértices selecionados e não selecionados
    for i in range(V):
        if selected[i]:  # Se o vértice i já foi selecionado
            for j in range(V):
                if not selected[j] and G_matrix[i][j]:  # Se j não foi selecionado e se forma uma aresta
                    # Atualiza a aresta mínima se uma aresta menor for encontrada
                    if minimum > G_matrix[i][j]:
                        minimum = G_matrix[i][j]  # Atualiza o peso mínimo
                        x = i  # Atualiza o vértice de origem
                        y = j  # Atualiza o vértice de destino
    mst_edges.append((x, y, minimum))  # Adiciona a aresta mínima à lista de arestas da MST
    print(f"{x} - {y}: {minimum}")  # Exibe a aresta e seu peso
    selected[y] = True  # Marca o vértice de destino como selecionado
    arestas += 1  # Incrementa o número de arestas na MST

# Criando o grafo da MST
mst_graph = nx.Graph()  # Inicializa um novo grafo para a MST
mst_graph.add_weighted_edges_from(mst_edges)  # Adiciona as arestas da MST ao grafo

# Visualização da MST
plt.figure(figsize=(8, 6))  # Define o tamanho da figura
nx.draw(mst_graph, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=700)  # Desenha a MST
mst_labels = nx.get_edge_attributes(mst_graph, 'weight')  # Obtém os rótulos das arestas da MST
nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=mst_labels)  # Desenha os rótulos das arestas da MST
plt.title("Árvore Geradora Mínima (MST)")  # Título do gráfico da MST
plt.show()  # Exibe o gráfico da MST
