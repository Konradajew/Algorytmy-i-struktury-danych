from zad4testy import runtests


def get_adjacency_list(L):
    V = max(L, key = lambda x: x[1])[1] + 1
    G = [[] for _ in range(V)]
    for edge in L:
        u, v, p = edge
        G[u].append((v, p))
        G[v].append((u, p))
    return G

def Flight(L, x, y, t):
    G = get_adjacency_list(L)
    visited = [False] * (y+1)
    visited[x] = True
    def DFS(u, START, END):
        if START <= END:
            if u == y:
                return True
            for (v, p) in G[u]:
                if not visited[v]:
                    visited[v] = True
                    if DFS(v, max(START, p-t), min(END, p+t)):
                        return True
                    visited[v] = False
            return False
    return DFS(x,float('-inf'),float('inf'))

runtests(Flight, all_tests = True)
