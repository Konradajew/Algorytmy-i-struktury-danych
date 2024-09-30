"""
ZLOZONOSC MLOGM
Konrad Szymański 421297

UZYWAM ALGORYTMU dijkstry rozmanazac wierzcholki (a w zasadzie odleglosci na zasadzie wjazd wyjazd tym samym lub innymi)
muszę rozmnożyć wierzchołki gdyż może się tak zdarzyć ze mimo wiekszej waga jest lepsza możliwość wyjazdu
Jako, że liczba stacji jest rzędu liczby linii kolejowych to złożoność to O(mlogm)

(Liczę za to na jakieś 5 punktów)
"""


from egz2btesty import runtests
from queue import PriorityQueue

def dijkstra2(G, s, t):
    n = len(G)
    d = [[float('inf') for _ in range(3)] for _ in range(n)]  #(P I, I I , P P)
    Q = PriorityQueue()
    d[s][0] = 0
    d[s][1] = 0
    d[s][2] = 0
    Q.put((s, 0, 'S')) #null type jako stacja poczatkowa

    while not Q.empty():
        v, w, type = Q.get()
        for u, w2, type2 in G[v]:
            if type == 'S':  #specjalny przypadek startowy nic nie dodajemy
                if type2 == 'I':
                    if d[u][0] > w + w2:
                        d[u][0] = w + w2
                        Q.put((u, d[u][0], type2))
                    if d[u][1] > w + w2:
                        d[u][1] = w + w2
                        Q.put((u, d[u][1], type2))
                if type2 == 'P':
                    if d[u][0] > w + w2:
                        d[u][0] = w + w2
                        Q.put((u, d[u][0], type2))
                    if d[u][2] >= w + w2:
                        d[u][2] = w + w2
                        Q.put((u, d[u][2], type2))
            elif type != type2:
                if type == 'I':
                    if d[u][0] > w + w2 + 20:
                        d[u][0] = w + w2 + 20
                        Q.put((u, d[u][0], type2))
                if type == 'P':
                    if d[u][0] > w + w2 + 20:
                        d[u][0] = w + w2 + 20
                        Q.put((u, d[u][0], type2))
            elif type == type2 == 'I':
                if d[u][1] > w + w2 + 5:
                    d[u][1] = w + w2 + 5
                    Q.put((u, d[u][1], type2))
            elif type == type2 == 'P':
                if d[u][2] > w + w2 + 10:
                    d[u][2] = w + w2 + 10
                    Q.put((u, d[u][2], type2))

    return d

def tory_amos( E, A, B ):
    n = len(E)
    nlist = [[] for _ in range(n)]

    for x, y, d, t in E:
        nlist[x].append((y, d, t))
        nlist[y].append((x, d, t))


    d2= dijkstra2(nlist, A, B)

    return min(d2[B])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
