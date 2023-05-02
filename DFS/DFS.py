class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
def DFS(graph, v, discovered):
 
    discovered[v] = True            # marca o nó atual como descoberto
    print(v, end=' ')               # imprime o nó atual
 
    # faz para cada aresta (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:       
            DFS(graph, u, discovered)
 
 
if __name__ == '__main__':
 
    edges = [
        # Observe que o nó 0 está desconectado
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
    n = 13

    # constrói um gráfico a partir das arestas dadas
    graph = Graph(edges, n)

    # para acompanhar se um vértice é descoberto ou não
    discovered = [False] * n

    # Executa a travessia DFS de todos os nós não descobertos para
    # cobre todos os componentes conectados de um gráfico
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)