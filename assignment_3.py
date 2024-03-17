import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4, 'E': 2},
    'C': {'B': 8, 'E': 7},
    'D': {'E': 6, 'F': 3},
    'E': {'F': 1},
    'F': {}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)

print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex, distance in shortest_distances.items():
    print(f"{vertex}: {distance}")
