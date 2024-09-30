#zmieniamy krawedzie na logarytmy a w dijksrze + na * i dziala
#oczywiscie problem z liczbami <1 bo wtedy na logarytmie smiesne rzeczy sie dzieja
import heapq


def dijkstra(graph, start):
    # Inicjalizacja odległości dla każdego wierzchołka jako nieskończoność,
    # z wyjątkiem startowego wierzchołka, którego odległość ustawiamy na 0.
    n = len(graph)
    distances = [float('infinity')] * n
    distances[start] = 1

    # Inicjalizacja kolejki priorytetowej.
    priority_queue = [(1, start)]

    while priority_queue:
        # Pobieramy wierzchołek z najmniejszą dotychczasową odległością.
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Sprawdzamy, czy obecna odległość jest mniejsza niż dotychczasowa dla tego wierzchołka.
        if current_distance > distances[current_vertex]:
            continue

        # Przeglądamy sąsiadów obecnego wierzchołka i aktualizujemy ich odległości,
        # jeśli możemy do nich dojść szybciej przez obecny wierzchołek.
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance * weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Dodajemy nową odległość do kolejki priorytetowej.
                heapq.heappush(priority_queue, (distance, neighbor))

    distances[start] = 0
    return distances


# Przykładowy graf w postaci listy sąsiedztwa.
graph = [
    [(1, 1), (2, 4)],  # Wierzchołek A
    [(0, 1), (2, 2), (3, 5)],  # Wierzchołek B
    [(0, 4), (1, 2), (3, 1)],  # Wierzchołek C
    [(1, 5), (2, 1)]  # Wierzchołek D
]

start_vertex = 0  # Indeks wierzchołka startowego
print("Odległości od wierzchołka", start_vertex, "do pozostałych wierzchołków:")
print(dijkstra(graph, start_vertex))