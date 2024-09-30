"""
Przyznaje, ze jezeli juz sie kiedys rozwiazywalo tego typu zadanie robi sie to zaskakujaco proste, ez najebany kodzik
w 30 minut.

Przerabiam najpierw graf na reprezantacje listowna bo jest lepsza ez O(n^2)
Uruchamian na tym zmodyfikowanego dijkstre gdzie rozmnazam wierzcholki (choc w zasadzie bardziej rozmnazam dystanse)
tak ze mamy informacje o najkrotszej sciezce do danego wierzcholka mogac przejechac jeszcze iles godzin
wtedy mamy dwa przypadki albo starczy nam zeby dostac sie do kolejnego wierzcholka wtedy jedziemy albo nie
wtedy odpoczywamy i przenosimy sie do wierzcholka z ktorego mamy dostepnych 16 godzin
na koncu zwracam minumum z dystansy do t
zlozonosc = O(n^2)
ElogV gdzie e rzedu n*17 i V = 17n wszysko sie spina ez pamieciowa n^2, 17n zalezy co wieksze


"""


from egz3atesty import runtests
from queue import PriorityQueue

def dijkstra(G, s, t):
    n = len(G)
    distances = [[float("inf") for _ in range(17)] for _ in range(n)]  #distanse o 0 do 16
    #print(distances[0])
    distances[s][16] = 0
    Q = PriorityQueue()
    Q.put((s, 0, 16))  #s, distance, mozliwe do przejechania godziny
    while not Q.empty():
        u, cost, avaible = Q.get()
        for v, w in G[u]:
            if avaible >= w:
                if distances[u][avaible] + w < distances[v][avaible-w]:
                    distances[v][avaible - w] = distances[u][avaible] + w
                    Q.put((v, distances[v][avaible - w], avaible - w))
            else:
                if distances[u][16] > distances[u][avaible] + 8:
                    distances[u][16] = distances[u][avaible] + 8
                    Q.put((u, distances[u][16], 16))
    return min(distances[t])

def goodknight(G, s, t):
    n = len(G)
    neighbours = [[] for _ in range(n)]
    for i in range(n):  #przerabiam na liste sasiedzctwa bo tak lepiej mi sie operuje
        for j in range(n):
            if G[i][j] != -1:
                neighbours[i].append((j, G[i][j]))
    l = dijkstra(neighbours,s,t)
    #print(l)

    return l

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(goodknight, all_tests=True)

# testy kontrolne, do sprawdzenia poprawności
"""
G=[[-1, 8, -1, -1, -1, 8, -1, -1, -1],
[ 8, -1, 1, -1, -1, -1, -1, -1, -1],
[-1, 1, -1, 8, -1, -1, -1, -1, -1],
[-1, -1, 8, -1, 4, -1, -1, -1, -1],
[-1, -1, -1, 4, -1, -1, -1, -1, 5],
[ 8, -1, -1, -1, -1, -1, 8, -1, -1],
[-1, -1, -1, -1, -1, 8, -1, 8, -1],
[-1, -1, -1, -1, -1, -1, 8, -1, 8],
[-1, -1, -1, -1, 5, -1, -1, 8, -1]]
print(goodknight(G,0,8)) #40

G=[[-1, 8, -1, -1, -1, 8, -1, -1],
[ 8, -1, 1, -1, -1, -1, -1, -1],
[-1, 1, -1, 8, -1, -1, -1, -1],
[-1, -1, 8, -1, 1, -1, -1, -1],
[-1, -1, -1, 1, -1, -1, 5, 8],
[ 8, -1, -1, -1, -1, -1, 8, -1],
[-1, -1, -1, -1, 5, 8, -1, -1],
[-1, -1, -1, -1, 8, -1, -1, -1]]
print(goodknight(G,0,7)) #37
"""
