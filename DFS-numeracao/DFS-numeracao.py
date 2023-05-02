def dfs(graph, node, visited, counter):
    visited[node] = True
    counter += 1
    print("Nó:", node, "Numerado como:", counter)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            counter = dfs(graph, neighbor, visited, counter)
    return counter

# Exemplo de uso:
graph = {
    2: [4, 5],
    3: [6],
    1: [2, 3],
    4: [],
    5: [7],
    6: [],
    7: []
}

visited = {node: False for node in graph}
counter = 0

for node in graph:
    if not visited[node]:
        counter = dfs(graph, node, visited, counter)
