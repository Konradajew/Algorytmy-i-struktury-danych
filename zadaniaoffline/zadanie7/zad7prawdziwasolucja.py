from zad7testy import runtests
from queue import PriorityQueue

def dijkstra(E, a):
    P = PriorityQueue()
    dist = [float('inf') for _ in range(len(E))]
    dist[a] = 0
    P.put((0, a))

    while not P.empty():
        #print(list(P.queue))
        cost, u = P.get()
        #print(list(P.queue))
        #print(E[u])

        for v, w in E[u]:
            #if dist[v] > dist[u] + w and visited[v]:
            #    print(dist[u] + w, dist[v])
            if dist[v] > dist[u] + w:
                #print("lolz")
                dist[v] = dist[u] + w
                P.put((dist[v], v))

    return dist

def maze( L ):
    mozliwe_kier = ["P", "G", "D"]
    n = len(L)
    print(len(L))
    if len(L) < 30:
        for r in L:
            print(r)
    neighbours = [[] for _ in range(n*n)]
    neighbours2 = [[] for _ in range(n*n)]
    # Przykład użycia
    for i in range(0, n):  #kolejne wiersze
        for j in range(0, n):   #wnetrze wiersza
            if L[i][j] == ".":
                #i*n+j obecny wierzchołek w tej kolumnie idziemy tylko do dolu
                if j < n-1:  #krawedz do prawej
                    if L[i][j+1] == ".":
                        neighbours[i*n+j].append((i*n+j+1, -1))
                        neighbours2[i*n+j].append((i*n+j+1, -1))
                        neighbours[i*n+j].append((n*n + i * n + j + 1, -1))
                        neighbours2[i*n+j].append((n*n +i * n + j + 1, -1))
                if i < n-1:  #krawedz do dolu
                    if L[i+1][j] == ".":
                        neighbours[i*n+j].append((i*n+n+j, -1))
                if i > 0:   #krawedz do gory
                    if L[i-1][j] == ".":
                        neighbours2[i*n+j].append((n*n+i*n-n+j, -1))

    neighbours = neighbours + neighbours2
    #if n < 10:
    #    for i in range(n*n):
    #        print(i, neighbours[i], neighbours[i+n*n])

    #print(neighbours[0], neighbours[n*n])

    liczba = dijkstra(neighbours, 0)
    Min = min(liczba[n*n-1], liczba[2*n*n-1])
    if Min < 0:
        return -Min
    else:
        return -1

    return

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )