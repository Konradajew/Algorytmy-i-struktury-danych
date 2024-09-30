from zad5testy import runtests
from queue import PriorityQueue


def is_reachable(G, s, b):
    n = len(G)
    visited = [False] * n
    queue = []
    queue.append(s)

    while queue:
        v = queue.pop(0)
        for e in G[v]:
            if not visited[e[0]]:
                visited[e[0]] = True
                queue.append(e[0])

    return visited[b]

def dijkstra(G, s, b):
    out = [False] * len(G)
    d = [float('inf')] * len(G)
    d[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))

    if not is_reachable(G, s, b):
        return None

    while not Q.empty():
        v = Q.get()[1]
        #print(G[v])
        if not out[v]:
            #print("nnn")
            for n in G[v]:
                if d[n[0]] > d[v] + n[1]:
                    d[n[0]] = d[v] + n[1]
                    Q.put((d[n[0]], n[0]))
        out[v] = True
        if out[b]:
            return d[b]

    return None

def spacetravel( n, E, S, a, b ):
    for i in range(0, len(S)):
        for j in range(i + 1, len(S)):
            E.append((S[i], S[j], 0))
    neighbours = [[] for _ in range(n)]

    for u, v, p in E:
        neighbours[u].append((v, p))
        neighbours[v].append((u, p))

    #optimize(neighbours,a,b)
    return dijkstra(neighbours, a, b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )