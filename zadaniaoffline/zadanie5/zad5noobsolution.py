from zad5testy import runtests
from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    d = [float('inf') for _ in range(n)]
    d[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        v = Q.get()[1]
        for u in G[v]:
            relax(v, u, d, Q)
    return d

def relax(v, u, d, Q):
    if d[u[0]] > d[v] + u[1]:
        d[u[0]] = d[v] + u[1]
        Q.put((d[u[0]], u[0]))

def spacetravel( n, E, S, a, b ):
    for i in range(0, len(S)):
        for j in range(i + 1, len(S)):
            E.append((S[i], S[j], 0))
    neighbours = [[] for _ in range(n)]

    for u, v, p in E:
        neighbours[u].append((v, p))
        neighbours[v].append((u, p))

    distances = dijkstra(neighbours, a)
    if distances[b] == float('inf'):
        return None
    return distances[b]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )

Q = PriorityQueue()
Q.put((0, "ADAS"))
Q.put((-1, "zoisia"))
print(Q)
a = Q.get()
print(a)