"""
Konrad Szymański 421297
Założenie działania jest bardzo proste dodaje wszystkie wszystkie ściezki z wierzchołka x do y o długości mniejszej niż 17
następnie puszczam na tym zwykłą djikstre z założeniem, że zawsze odpoczywam więc zawsze dodaje 8
(Przepraszam za obrzydliwość tego kodu starałem się napisać lepszą złożoność)
Złożoność czasowa:
V dikstr żeby znależć krawędzie do dodania O(V * (V + ElogV)) więc generalnie V^3
zakładając, że dodam krawędż z każdego wierzchołka do każdego innego nie będzie ich więcej niż V^2 więc nie ostatnia
dijkstra też ma złożoność nie większą niż V^3
"""

from kol2testy import runtests
from queue import PriorityQueue

def dijkstra(E, a):
    P = PriorityQueue()
    dist = [float('inf') for _ in range(len(E))]
    cur_trav = 0
    dist[a] = 0
    to_add = []
    P.put((0, a, cur_trav))
    while not P.empty():

        cost, u, cur_tr = P.get()
        for v, w in E[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if cur_tr + w <= 16:
                    P.put((dist[v], v, cur_tr + w))
                else:
                    if a < u:
                        to_add.append((a, u, cur_tr))
                    else:
                        to_add.append((u, a, cur_tr))
    #print(to_add)
    return to_add

def dijkstra2(E, a, t):
    P = PriorityQueue()
    dist = [float('inf') for _ in range(len(E))]
    dist[a] = 0
    P.put((0, a))
    while not P.empty():
        cost, u = P.get()
        for v, w in E[u]:
            if dist[v] > dist[u] + w + 8:
                dist[v] = dist[u] + w + 8
                P.put((dist[v] + 8, v))

        if u == t:
            return dist
    return dist

def dijkstra3(E, a):
    P = PriorityQueue()
    dist = [float('inf') for _ in range(len(E))]
    cur_trav = 0
    dist[a] = 0
    P.put((0, a, cur_trav))
    while not P.empty():

        cost, u, cur_tr = P.get()
        for v, w in E[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if cur_tr + w <= 16:
                    P.put((dist[v], v, cur_tr + w))

    return dist

def warrior( G, s, t):
    # przerabiam na liste sąsiedzctwa
    ls = [[] for _ in range(len(G))]
    for i in range(0, len(G)):
        u, v, p = G[i]
        ls[u].append((v, p))
        ls[v].append((u, p))
    #print(ls)

    if dijkstra3(ls, s)[t] <= 16:
        return dijkstra3(ls, s)[t]

    all_to_add = []
    for i in range(0, len(G)):
        all_to_add += dijkstra(ls,i)
    all_to_add.sort()

    nl = []
    nl.append(all_to_add[0])
    for i in range(1, len(all_to_add)): #eliminacja dodania kilkukrotnie tych samych krawędzi
        u, v, p = all_to_add[i-1]
        u1, v1, p1 = all_to_add[i]
        if u != u1 or v != v1 or p != p1:
            nl.append((u1, v1, p1))

    #print(all_to_add)
    for r in nl:
        G.append(r)
    ls = [[] for _ in range(len(G))]
    for i in range(0, len(G)):
        u, v, p = G[i]
        ls[u].append((v, p))
        ls[v].append((u, p))
    #print(nl)


    return dijkstra2(ls,s, t)[t] - 8

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
