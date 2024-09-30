"""
Algorytmu przekształca liste krawędzi w liste sąsiedzctwa(bez punktu L) następnie znajduje najkrótszą scieżkę składającą się z 3
krawędzi (rozmnażam wierzchołki*4 nie obchodzą mnie wartości dla większej niż 3 krawędzi)
Zwracam minimum z odległości z najkrótszej 3 krawędziowej drogi z D do punkty n i krąwędzi z tego punktu do L
Złożoność O(Elog4V) = O(mlogn)

Dodałem jeszcze do dijkstry coś takiego jak sprawdzanie poprzednika wierzchołka, bo może się teoretycznie zdażyć, że
najkrótsza 3 krawedziowa droga ma postać: D -> u -> v -> u -> L, albo  D -> u -> D -> u -> L
w tych testach akurat takich przypadków nie ma, ale teoretycznie mogą być

Czas rozwiązania 20 minut, 30 jak liczyć opis
"""

from egzP1btesty import runtests
from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    distances = [[[float("inf"), None] for _ in range(4)] for _ in range(n)]
    distances[s][0][0] = 0
    distances[s][0][1] = None
    Q = PriorityQueue()
    Q.put((s, 0, 0, None))
    while not Q.empty():
        u, cost, edges, predecessor = Q.get()
        for v, w in G[u]:
            if edges < 3 and predecessor != v:
                if distances[u][edges][0] + w < distances[v][edges+1][0]:
                    distances[v][edges+1][0] = distances[u][edges][0] + w
                    Q.put((v, distances[v][edges+1], edges+1, u))

    return distances

def turysta( G, D, L ):
    n = len(G)
    neighbours = [[] for _ in range(n)]
    L_neighbours = []

    for i in range(n):
        v1, v2, e = G[i]
        if L != v1 and L != v2:
            neighbours[v1].append((v2, e))
            neighbours[v2].append((v1, e))
        else:
            L_neighbours.append((v1 if L == v2 else v2, e))

    distances = dijkstra(neighbours, D)

    Min = float('inf')
    for n in L_neighbours:
        Min = min(Min, distances[n[0]][3][0]+n[1])

    return Min

runtests ( turysta )