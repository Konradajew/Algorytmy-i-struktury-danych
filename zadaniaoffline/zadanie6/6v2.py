from zad6testy import runtests
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
        for v, w in E[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                P.put((dist[v], v))
    return dist

def backtrack(L, visited, x, y, ogr, d, c_u_s):
    visited[x] = True
    visited2 = [False] * len(visited)
    #print(len(L))
    for i in range(0, len(visited)):
        visited2[i] = visited[i]

    if d > ogr:
        visited[x] = False
        return 999
    if x == y:
        #print(d)
        return d
    a, b, c, Min = 999, 999, 999, 999
    #print(x)
    #print(L[x])
    for u1, v1, p1 in L:
        if (u1 == x or v1 == x) and not visited[u1 if v1 == x else v1]:
            if x == u1:
                nz = v1
            if x == v1:
                nz = u1
            #visited[nz] = True
            b, c = backtrack(L, visited2, nz, y, ogr, d + p1, False), backtrack(L, visited2, nz, y, ogr, d + p1, True)
            Min = min(b, c, Min)
            if c_u_s:
                for u2, v2, p2 in L:
                    if (u2 == nz or v2 == nz) and not visited[u2 if v2 == nz else v2]:
                        a = backtrack(L, visited2, u2 if v2 == nz else v2, y, ogr, d+max(p1, p2), False)
                        if a < Min:
                            Min = a
            #Min = min(a, b, c, Min)
            #visited[nz] = False

    visited[x] = False
    return Min

def jumper( G, s, w ):
    E = []
    for i in range(0, len(G)):
        for j in range(i+1, len(G)):
            if G[i][j] != 0:
                E.append((i, j, G[i][j]))

    neighbours = [[] for _ in range(len(G))]
    for u, v, p in E:
        neighbours[u].append((v, p))
        neighbours[v].append((u, p))

    visited = [False]*len(G)
    dist = dijkstra(neighbours, s)  #liczymy najkrotsza sciezke normalna bez butow przyda sie to w optymalizacji bruta
    ogr = dist[w]
    for i in range(0, len(G)):
        if dist[i] >= 2*ogr:
            visited[i] = True
    ans = backtrack(E, visited, s, w, ogr, 0, True)

    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )