from typing import List

def shortestPathLength(graph: List[List[int]]) -> int:
    n = len(graph)
    target = (1 << n) - 1  # target state where all nodes have been visited

    # start BFS from all nodes simultaneously
    q = [(i, 1 << i, 0) for i in range(n)]  # (node, state, distance)
    visited = set((i, 1 << i) for i in range(n))  # avoid revisiting the same node with the same state

    while q:
        node, state, dist = q.pop(0)
        if state == target:
            return dist  # if all nodes have been visited, return the shortest distance
        for neighbor in graph[node]:
            new_state = state | (1 << neighbor)  # mark the neighbor as visited
            if (neighbor, new_state) not in visited:
                visited.add((neighbor, new_state))
                q.append((neighbor, new_state, dist+1))
    
    return -1  # if there is no path that visits every node, return -1

# Exemplo de uso:
graph = [[1,2,3],[0],[0],[0]]
print(shortestPathLength(graph))  # Saída: 4