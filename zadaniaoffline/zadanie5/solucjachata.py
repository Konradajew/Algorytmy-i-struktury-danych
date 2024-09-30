import heapq

def dijkstra(graph, start):
    n = len(graph)  # Liczba wierzchołków w grafie
    distances = [float('infinity')] * n  # Inicjalizacja odległości jako nieskończoność
    distances[start] = 0  # Odległość do startowego wierzchołka wynosi 0
    visited = [False] * n  # Tablica odwiedzonych wierzchołków
    queue = [(0, start)]  # Kolejka priorytetowa

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Pomijamy wierzchołek, jeśli odległość do niego jest większa niż obecna
        if current_distance > distances[current_vertex]:
            continue

        # Oznaczamy bieżący wierzchołek jako odwiedzony
        visited[current_vertex] = True

        # Iterujemy przez sąsiadów bieżącego wierzchołka
        for neighbor, weight in graph[current_vertex]:
            if not visited[neighbor]:
                distance = current_distance + weight

                # Jeśli znaleziono krótszą ścieżkę do sąsiada, aktualizujemy odległość
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

    return distances

# Przykładowa lista sąsiedztwa, gdzie indeksy odpowiadają numerom wierzchołków
# a wartości to listy par (sąsiad, waga)
graph = [
    [(1, 5), (2, 3)],  # Wierzchołek 0
    [(0, 5), (2, 1), (3, 3)],  # Wierzchołek 1
    [(0, 3), (1, 1), (3, 2)],  # Wierzchołek 2
    [(1, 3), (2, 2)]  # Wierzchołek 3
]

start_vertex = 0  # Indeks wierzchołka startowego
distances = dijkstra(graph, start_vertex)
print("Najkrótsze odległości od wierzchołka", start_vertex, "do pozostałych wierzchołków:")
print(distances)