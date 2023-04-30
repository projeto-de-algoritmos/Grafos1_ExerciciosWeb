import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    path = []
    node = end
    while node != start:
        path.append(node)
        node = min(distances, key=lambda n: distances[n] if n in graph[node] else float('inf'))
    path.append(start)
    path.reverse()
    return path

# Example usage:
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'D': 3},
    'C': {'A': 1, 'D': 1},
    'D': {'B': 3, 'C': 1, 'E': 5},
    'E': {'D': 5}
}

start = 'A'
end = 'E'
path = dijkstra(graph, start, end)
print(f"Caminho mais perto de  {start} para {end}: {' -> '.join(path)}")
