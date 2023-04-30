from typing import List

def isBipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    colors = [-1] * n  # inicializa todos os nós com a cor -1 (ainda não foram coloridos)

    def dfs(node: int, color: int) -> bool:
        colors[node] = color  # pinta o nó atual
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False  # se o vizinho tem a mesma cor, então não é bipartido
            if colors[neighbor] == -1 and not dfs(neighbor, 1-color):
                return False  # se o vizinho não foi colorido e a sua sub-árvore não é bipartida, então não é bipartido
        return True

    for i in range(n):
        if colors[i] == -1 and not dfs(i, 0):  # começa a DFS pelos nós não coloridos
            return False
    return True


# Exemplo de uso:
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]  # insere o grafo como uma matriz 2D
print(isBipartite(graph))  # Saída: False

graph = [[1,3],[0,2],[1,3],[0,2]]
print(isBipartite(graph))  # Saída: True
