"""
Konrad Sz
Rozwiazanie sprowadza sie zasadniczo to przerobienia grafu w graf acykliczny wtedy istnieje dokladnie jedna sciezka
pomiedzy jakimis tam dwoma punktami, a nastpenie dodaniu krawedzi o najwiekszej wartosci sposrod usunietych.
Czyli zasadniczo do utworzenia maxymalnego drzewa rozpinajacego


"""

from egzP3btesty import runtests
from queue import PriorityQueue

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal_maximum_spanning_tree(vertices, edges):
    # Sortowanie krawędzi według wag malejąco
    edges.sort(key=lambda edge: edge[2], reverse=True)

    # Inicjalizacja struktury zbiorów rozłącznych (Disjoint Set)
    disjoint_set = DisjointSet(vertices)

    # Lista krawędzi, które będą w maksymalnym drzewie rozpinającym
    max_spanning_tree = []
    edges_to_remove = []

    # Przechodzimy przez posortowane krawędzie
    for edge in edges:
        u, v, weight = edge

        # Sprawdzamy, czy dodanie krawędzi u-v tworzy cykl
        if disjoint_set.find(u) != disjoint_set.find(v):
            max_spanning_tree.append(edge)
            disjoint_set.union(u, v)
        else:
            edges_to_remove.append(weight)

    # Zwracamy listę krawędzi, które tworzą maksymalne drzewo rozpinające
    return [max_spanning_tree, edges_to_remove]

def lufthansa ( G ):
    #print(G)
    krawedzie = set()
    wierzcholki = []
    for i in range(0, len(G)):
        wierzcholki.append(i)
        for e in G[i]:
            krawedzie.add((min(i, e[0]), max(i, e[0]), e[1]))
    krawedzie = list(krawedzie)

    max_spanning_tree, weights_removed = kruskal_maximum_spanning_tree(wierzcholki, krawedzie)
    #print(max_spanning_tree, weights_removed)
    return sum(weights_removed) - max(weights_removed)

runtests ( lufthansa, all_tests=True )