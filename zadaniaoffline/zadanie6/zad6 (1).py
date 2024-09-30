from zad6testy import runtests
from queue import PriorityQueue
"""
Konrad Szymański 421297
Algorytm zamienia danie z macierzy na listę sąsiedzctwa dodając krawędzie butowe, a następnie wywołuje zmodyfikowaną dijkstre
aby znaleźć najkrótszą odległość z s do w (Poprawność zmodyfikowanej dijktrsy skomentuje w dijkstrze)
Złożoność czasowa:
Zamiana danych: O(V^3)
Zmodyfikowana Dijkstra: krawędzi bucich jest co najwyżej v^2
Zatem dijkstra ma złożoność O(V^2logV)
"""

def dijkstra(E, a):
    P = PriorityQueue()
    dist = [float('inf') for _ in range(len(E))]
    dist[a] = 0
    P.put((0, a))
    while not P.empty():
        cost, u = P.get()
        for v, w in E[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                P.put((dist[v], v))
    return dist

def dijkstra2(E, a):
    P = PriorityQueue()
    n = len(E)
    dist = [[float('inf'), float('inf')] for _ in range(n)]  #lista minimalnych dystansy wejscia do wierzcholka z nieuzyciem/uzyciem butow
    dist[a][0] = 0
    P.put((0, a, False))  # dystans, wierzchołek, czy wszedłem do wierzchołka używając butów

    while not P.empty():
        cost, u, entry = P.get()
        for v, w, s, pos in E[u]:
            if dist[v][0] > dist[u][0] + w and s == 1:  # wchodzimy do v bez butow wiec dist[v][0] tutaj rozważamy tylko dist[u][0]
                dist[v][0] = dist[u][0] + w
                P.put((dist[v][0], v, False))

            if dist[v][1] > dist[u][0] + w and s == 2 and not entry:  # wchodzimy do v butami wiec dist[v][1] i musielismy wejsc do u bez butow wiec dist[u][0]
                dist[v][1] = dist[u][0] + w
                P.put((dist[v][1], v, True))
                P.put((dist[u][0] + pos, v, False))  # przejście dwóch krawędzi bez butów, pos to odległość u do v bez użycia butów
                for v1, w1, s1, pos1 in E[v]:
                    if dist[v1][0] > dist[v][1] + w1 and s1 == 1:  # wyżej rozważamy wejście po dist[u][0] więc tutaj po dist[u][1] i to ładnie się spina
                        dist[v1][0] = dist[v][1] + w1
                        P.put((dist[v1][0], v1, False))
            # dlaczego to działa?
            # po pierwsze zauważam, że warto by trzymać najkrótsze dystanse po wejściach do wierzchołka, albo bez butów, albo z butami
            # gdyż jeżeli tego nie zrobimy program nie zadziała, ze względu na warunek użycia butów najkrótsza droga do danego wierzchołka
            # nie jest koniecznie najkrótszą drogą do kolejnego wierzchołka przykładowo może opłacać się pójść 3 razy z rzędu bez butów
            # co nie zostałoby rozważone bo droga składająca się z pierwszej krawędzi i dłuższej z dwóch kolejnych byłaby oczywiście krótsza
            # przez co mogłoby umknąć rozważenie najkrótszej ścieżki, da się pewnie zrobić bez rozdziałki dystansów, ale to trzeba by jakoś
            # sensownie kolejność rozważania zakodować, żeby te teoretycznie większe wartości się rozważyły
            # ten kod rozważa przypadki takie jak pójście dwa lub trzy razy z rzędu bez butów, dla 4 razy zawsze opłaca się użyć butów dla 2 i 3 krawędzi
            # więc nie trzeba tego rozważać.

    return dist


def jumper( G, s, w ):
    E = []
    n = len(G)
    for i in range(0, n):
        for j in range(i+1, n):
            if G[i][j] != 0:
                E.append((i, j, G[i][j]))
    # przerobienie macierzy na listę krawędzi
    # przerobienie listy krawędzi na listę sąsiedzctwa
    neighbours = [[] for _ in range(n)]
    for u, v, p in E:
        neighbours[u].append((v, p))
        neighbours[v].append((u, p))
    # wywołanie zwykłej djikstry w celu optymalizacji
    ans = dijkstra(neighbours, s)  # lista najkrótszych odległości do wierzchołków bez użycia butów
    ogr = ans[w]  # ogr i nie chodzi tu o shreka tylko o ograniczenie wartości, zauważam, że jeżeli jakaś krawędź jest
    # dłuższa niż ogr to można ją usunąć podobnie jeżeli dystans do jakiegoś punktu przekracza 2*ogr nie trzeba go roważać

    nn = [[] for _ in range(n)]  # nowi neighborzy jeszcze bez podwójnych krawędzi
    for i in range(0, n):
        for e in neighbours[i]:
            if e[1] <= ogr and ans[e[0]] <= 2 * ogr:
                nn[i].append((e[0], e[1], 1, None))

    for i in range(0, n):  # dodanie podwójnych krawędzi do nowych neighborów
        nnl = []  # nie mogę appendować nowych krawędzi do nn[i], bo to na biężaco wydłużałoby listę krawędzi do rozważenia w pętli
        for u, p1, s1, pos1 in nn[i]:  #(sąsiad, dlugość krawędzi, typ_krawędz(1 - bez butów, 2 - buty), suma p1+p2 jeżeli krawędź podwójna, jak nie jest to jest ona Nonem jak wyżej.
            for v, p2, s2, pos2 in nn[u]:
                if max(p1, p2) < ogr and s1 == s2 and s1 != 2 and v != i and max(ans[u], ans[v]) <= 2*ogr:  # warunki z ograniczeniami wartości czysto optymalizacyjne
                    nnl.append((v, max(p1, p2), 2, p1+p2))
        nn[i] = nn[i] + nnl  # dopisanie nnl do nn[i]

    dist = dijkstra2(nn, s)[w]
    return min(dist)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )
