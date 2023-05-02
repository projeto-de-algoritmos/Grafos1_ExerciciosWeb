from collections import deque


def ordenacao_topologica(grafo):
    # calcular grau de entrada para cada vértice
    grau_entrada = {v: 0 for v in grafo}
    for v in grafo:
        for u in grafo[v]:
            grau_entrada[u] += 1
    # colocar vértices sem arestas de entrada na fila
    fila = deque(v for v in grafo if grau_entrada[v] == 0)
    # ordenação topológica
    resultado = []
    while fila:
        v = fila.popleft()
        resultado.append(v)
     # busca menor grau
        for u in grafo[v]:
            grau_entrada[u] -= 1
            if grau_entrada[u] == 0:
                fila.append(u)
    
    # verificar se todos os vértices foram visitados
    if len(resultado) != len(grafo):
        raise ValueError("Grafo possui ciclo")
    
    return resultado

if __name__ == '__main__':

    grafo = {
        'v1': ['v5', 'v7'],
        'v2': ['v3', 'v5', 'v6'],
        'v3': ['v4','v5'],
        'v4': ['v5'],
        'v5': ['v6','v7'],
        'v6': ['v7'],
        'v7': []
    }
    print(ordenacao_topologica(grafo))