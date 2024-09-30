#chat
import heapq


def dijkstra(graph, start):
    # Inicjalizacja odległości dla każdego wierzchołka jako nieskończoność,
    # z wyjątkiem startowego wierzchołka, którego odległość ustawiamy na 0.
    n = len(graph)
    distances = [float('infinity')] * n
    distances[start] = 0

    # Inicjalizacja kolejki priorytetowej.
    priority_queue = [(0, start)]

    while priority_queue:
        # Pobieramy wierzchołek z najmniejszą dotychczasową odległością.
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Sprawdzamy, czy obecna odległość jest mniejsza niż dotychczasowa dla tego wierzchołka.
        if current_distance > distances[current_vertex]:
            continue

        # Przeglądamy sąsiadów obecnego wierzchołka i aktualizujemy ich odległości,
        # jeśli możemy do nich dojść szybciej przez obecny wierzchołek.
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Dodajemy nową odległość do kolejki priorytetowej.
                heapq.heappush(priority_queue, (distance, neighbor))

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


#chlop
from queue import PriorityQueue
# graf w postaci listy sąsiedztwa
def dijkstra2(G, s):
    out = [False] * len(G)
    n = len(G)
    d = [float('inf') for _ in range(n)]
    d[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))  # Wstawiamy krotkę (priorytet, wierzchołek) do kolejki

    while not Q.empty():
        v = Q.get()[1]  # Pobieramy wierzchołek o najniższym priorytecie
        if not out[v]:
            for u in G[v]:
                relax(v, u, d, Q)
        out[v] = True
    return d

def relax(v, u, d, Q):
    if d[u[0]] > d[v] + u[1]:
        d[u[0]] = d[v] + u[1]
        Q.put((d[u[0]], u[0]))

graph = [
    [(1, 1), (2, 4)],  # Wierzchołek A
    [(0, 1), (2, 2), (3, 5)],  # Wierzchołek B
    [(0, 4), (1, 2), (3, 1)],  # Wierzchołek C
    [(1, 5), (2, 1)]  # Wierzchołek D
]
start_vertex = 0  # Indeks wierzchołka startowego
print("Odległości od wierzchołka", start_vertex, "do pozostałych wierzchołków:")
print(dijkstra2(graph, start_vertex))