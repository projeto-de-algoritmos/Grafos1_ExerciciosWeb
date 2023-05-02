from typing import List

def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = set()  # conjunto para armazenar os nós já visitados
    count = 0  # contador de províncias

    def dfs(node: int) -> None:
        visited.add(node)  # marca o nó atual como visitado
        for neighbor in range(n):
            if isConnected[node][neighbor] and neighbor not in visited:
                dfs(neighbor)  # visita o vizinho

    for i in range(n):
        if i not in visited:
            dfs(i)  # inicia a busca em profundidade a partir do nó não visitado
            count += 1  # se encontrar uma nova província, incrementa o contador

    return count

isConnected_1 = [[1,1,0],[1,1,0],[0,0,1]]
print("Dada a seguinte matriz de conexão: "+ str(isConnected_1) +" a saida é: ")
print(findCircleNum(isConnected_1))  

isConnected_2 = [[1,0,0],[0,1,0],[0,0,1]]
print("Dada a seguinte matriz de conexão: " +str(isConnected_2) +" a saida é: ")
print(findCircleNum(isConnected_2))  
