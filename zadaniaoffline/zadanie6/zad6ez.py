from zad6testy import runtests
from queue import PriorityQueue

def dijkstra(E, a, b):
    P = PriorityQueue()
    dist = [float('inf') for _ in range(len(E))]
    dist[a] = 0
    P.put((0, a))

    while not P.empty():
        cost, u = P.get()
        if u == b:
            return dist[u]
        for v, w in E[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                P.put((dist[v], v))
    return None

def backtrack(L, visited, x, y, ogr, d, c_u_s):
    visited[x] = True
    if d > ogr:
        visited[x] = False
        return 999
    if x == y:
        print(d)
        return d
    a, b, c = 999, 999, 999
    #print(x)
    #print(L[x])
    for e1 in L[x]:
        u1, p1 = e1
        #print(u1)
        if c_u_s:
            for e2 in L[u1]:
                u2, p2 = e2
                if not visited[u2] and d+max(p1, p2) < ogr:
                    visited[u1] = True
                    d += max(p1, p2)
                    print(d)
                    a = backtrack(L, visited, u2, y, ogr, d, False)
                    visited[u1] = False
        if not visited[u1] and d+p1 < ogr:
            b = backtrack(L, visited, u1, y, ogr, d+p1, False)
            c = backtrack(L, visited, u1, y, ogr, d+p1, True)

    #visited[x] = False
    return min(a, b, c)

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

    print(G)
    print(neighbours)

    visited = [False]*len(G)
    ogr = dijkstra(neighbours, s, w)
    print("lol")
    ans = backtrack(neighbours, visited, s, w, ogr, 0, True)
    print(ans)
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )