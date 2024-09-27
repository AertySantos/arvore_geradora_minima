import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, vertices):
        # Inicializa o grafo com o número de vértices
        self.V = vertices
        self.grafo = []  # Lista para armazenar as arestas do grafo
        self.mst = []    # Lista para armazenar a Árvore Geradora Mínima

    def add_aresta(self, u, v, w):
        # Método para adicionar uma aresta ao grafo com seu peso
        self.grafo.append([u, v, w])

    # Função de busca
    def encontrar(self, parent, i):
        # Função de busca para o algoritmo de União-Busca para encontrar o representante de um conjunto
        if parent[i] == i:
            return i
        return self.encontrar(parent, parent[i])

    def aplicar_uniao(self, parent, rank, x, y):
        # Função de união para mesclar dois conjuntos com base na classificação
        xroot = self.encontrar(parent, x)
        yroot = self.encontrar(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Aplicando o algoritmo de Kruskal
    def kruskal_algo(self):
        # Método para encontrar a Árvore Geradora Mínima usando o Algoritmo de Kruskal
        i, e = 0, 0  # Inicializa variáveis para aresta e índice
        self.grafo = sorted(self.grafo, key=lambda item: item[2])  # Ordena as arestas por peso
        parent = []  # Lista para armazenar o pai de cada vértice
        rank = []    # Lista para armazenar a classificação de cada vértice
        for node in range(self.V):
            parent.append(node)  # Inicializa cada vértice como seu próprio pai
            rank.append(0)       # Inicializa a classificação de cada vértice como 0
        while e < self.V - 1:#arestas da arvore m=n-1
            # Loop até que todos os vértices estejam incluídos na AGM
            u, v, w = self.grafo[i]  # Obtém a aresta com o peso mínimo
            i += 1  # Move para a próxima aresta
            x = self.encontrar(parent, u)  # Encontra o representante do conjunto de u
            y = self.encontrar(parent, v)  # Encontra o representante do conjunto de v
            if x != y:
                # Se adicionar a aresta não formar um ciclo
                e += 1  # Incrementa a contagem de arestas
                self.mst.append([u, v, w])  # Armazena a aresta na lista de MST
                self.aplicar_uniao(parent, rank, x, y)  # Mescla os conjuntos de u e v
        print(i)
        print(e)
        print(self.V - 1)
        for u, v, peso in self.mst:
            # Imprime as arestas da AGM
            print("%d - %d: %d" % (u, v, peso))

    # Função para desenhar o grafo e a árvore geradora mínima
    def desenhar_mst(self):
        # Criar um grafo usando NetworkX
        G = nx.Graph()

        # Adicionar todas as arestas do grafo original
        for u, v, w in self.grafo:
            G.add_edge(u, v, weight=w)

        # Definir o layout do grafo
        pos = nx.spring_layout(G)

        # Desenhar o grafo original com todas as arestas
        plt.figure(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.title("Grafo Original")
        plt.show()

        # Desenhar apenas a árvore geradora mínima (MST)
        mst = nx.Graph()
        for u, v, w in self.mst:
            mst.add_edge(u, v, weight=w)

        plt.figure(figsize=(10, 7))
        nx.draw(mst, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=10)
        mst_labels = nx.get_edge_attributes(mst, 'weight')
        nx.draw_networkx_edge_labels(mst, pos, edge_labels=mst_labels)

        plt.title("Árvore Geradora Mínima (Kruskal)")
        plt.show()

# Exemplo de uso
g = Grafo(6)  # Cria um grafo com 6 vértices
#g = Grafo(4)  # Cria um grafo com 6 vértices
# Adiciona arestas com seus pesos ao grafo

g.add_aresta(0, 1, 4)
g.add_aresta(0, 2, 4)
g.add_aresta(1, 2, 2)
g.add_aresta(1, 0, 4)
g.add_aresta(2, 0, 4)
g.add_aresta(2, 1, 2)
g.add_aresta(2, 3, 3)
g.add_aresta(2, 5, 2)
g.add_aresta(2, 4, 4)
g.add_aresta(3, 2, 3)
g.add_aresta(3, 4, 3)
g.add_aresta(4, 2, 4)
g.add_aresta(4, 3, 3)
g.add_aresta(5, 2, 2)
g.add_aresta(5, 4, 3)

"""
g.add_aresta(0, 1, 1)
g.add_aresta(1, 3, 1)
g.add_aresta(0, 3, 3)
g.add_aresta(1, 2, 2)
g.add_aresta(2, 3, 4)
"""
g.kruskal_algo()  # Encontra e imprime a Árvore Geradora Mínima
g.desenhar_mst()  # Desenha o grafo original e a MST
