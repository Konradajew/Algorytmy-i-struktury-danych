"""
Konrad Szymański 421297
Algorytm przekształca najpierw dane wejściowe w listę sąsiedzctwa oraz zbija wszystkie punkty osobliwości
w jeden punkt zachowując krawędź o najkrótszej długości prowadzącą do danego punktu. Następnie sprawdza czy da się
dostać z a do b bfsem, jeżeli nie zwraca None, następnie za pomocą algorytmu dijkstry znajduje najkrótszą ściężke.
Złożoność czasowa: Przekształcenie w listę sąsiedzctwa - E
zbicie punktów osobliwości w jeden punkt - E
is_reachable(bfs) - V + E
djikstra - (V + Elog(V))      (generalnie w sumie mniej, bo wiele wierzchołków się zbija w jeden, ale to w sumie tyle samo z dokładnością do stałej)
Zatem złożoność czasowa wynosi O(V+ElogV)
Jeżeli uwzględnimy S w obliczaniu złoności to po zbiciu liczba wierzchołków wynosi V-S+1, a krawędzi E-Sk+Su, gdzie Sk
to wszystkie krawędzie z S a Su to najkrótsze Krawędzie z S do unikalnych wierzchołków wtedy złożoność czasowa wynosi:
O(V-S+1 + (E-Sk+Su)log(V-S+1))
"""
from zad5testy import runtests
from queue import PriorityQueue

def is_reachable(G, a, b, n):  #zwykły bfs sprawdzający czy da się dostać z a do b
    visited = [False] * n
    queue = []
    queue.append(a)

    while queue:
        v = queue.pop(0)
        for e in G[v]:
            if not visited[e[0]]:
                visited[e[0]] = True
                queue.append(e[0])

    return visited[b]

def dijkstra(G, a, b, n):  #algorytm oblicza długość najkrótszej ścieżki z a do b o ile się da oczywiście
    out = [False] * n  #czy wszystkie krawędzie z wierzchołka zostały zrelaksowane jak tak to true
    d = [float('inf')] * n
    d[a] = 0
    Q = PriorityQueue()
    Q.put((0, a))

    while not Q.empty():
        v = Q.get()[1]
        if not out[v]:
            for n in G[v]:
                if d[n[0]] > d[v] + n[1]:
                    d[n[0]] = d[v] + n[1]
                    Q.put((d[n[0]], n[0]))
        out[v] = True
        if out[b]:  #jeżeli wszystkie krawędzie z b są zrelaksowane to znamy długość najkrótszej ścieżki z a do b
            return d[b]

def spacetravel( n, E, S, a, b ):
    if a in S:  #jeżeli a jest w osobliwości to a=n, bo wierzchołek a zostanie zbity do wierzchołka n
        a = n
    if b in S:  #jeżeli b jest w osobliwości to b=n, bo wierzchołek b zostanie zbity do wierzchołka n
        b = n
    if a == b:  #jeżeli a i b są w osobliwości to odległość wynosi 0
        return 0

    neighbours = [[] for _ in range(n+1)]  #lista sąsiedzctwa wraz z wierzchołkiem osobliwości o indeksie n
    osob_k = [float('inf')] * n  #lista najkrótszych krawędzi z osobliwości do punktu o danym indeksie, jak nie ma krawędzi to inf

    for u, v, k in E:  #dodanie wszystkich krawędzi do listy sąsiedzctwa, narazie bez wierzchołka osobliwości
        neighbours[u].append((v, k))
        neighbours[v].append((u, k))

    for e in S:  #dodaje długości najkrótszych krawędzi z wierzchołka osobliwości n do innych wierzchołków
        for s, k in neighbours[e]:
            if k < osob_k[s]:
                osob_k[s] = k
            #użycie tu neighbours[s].remove((e, p)) działa praktycznie szybciej niż ten późniejszy for, ale teoretycznie
            #zwiększa złożoność obliczeniową bardziej niż ten kolejny for w najgorszym przypadku, a przynajmniej
            #tak mi się wydaje możliwe, że się myle
        neighbours[e] = []  #wierzchołek e ma zniknąć więc usuwamy wszystkie krawędzie z niego

    for i in range(0, n):  #usunięcię krawędzi do wierzchołków z osobliwości
        n_n = []  #sąsiedzi danego wierzchołka, przepisanie sąsiadów ma lepszą złożoność niż używanie remove
        for k in neighbours[i]:
            if neighbours[k[0]]:  #jeżeli istnieją jacyś sąsiedzi k[0] to znaczy, że nie jest to wierzchołek z osobliwości
                n_n.append(k)  #zatem dopisujemy krawędź do niego do n_n
        neighbours[i] = n_n  #zatem wartość neighbours[i] = n_n

    for i in range(0, n):  #dopisujemy do tablicy sąsiadów, krawędzie do i z wierzchołka osobliwości i odwrotnie
        if osob_k[i] < float('inf'):
            neighbours[i].append((n, osob_k[i]))
            neighbours[n].append((i, osob_k[i]))

    if not is_reachable(neighbours, a, b, n+1):  #sprawdzamy czy da się dostać z a do b, praktycznie bez tego kod przechodzi testy szybciej
        #ale mam nadzięję, że na coś się przyda i uratuje jakiś złośliwy test, złożoności w sumie nie zwiększa
        return None

    return dijkstra(neighbours, a, b, n+1)  #zwraca długość ścieżki z a do b

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )