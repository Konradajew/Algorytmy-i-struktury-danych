from egz2btesty import runtests
from queue import Queue

"""
Ta wersja bardzo nie optymalnie przypisuje visited, ale generalnie dziala o(n) tylko, ze powoli


"""



def bfs(s, k, G):
    n = len(G)
    visited = [False]*n  # zmiana, I I, P P
    queue = Queue()
    visited[s] = True
    queue.put((s, 0, 0, 'S')) #wierzcgholek, przebyty dystans, czas do opuszczenia, typwjazdowy

    while queue:
        v, d, t, rt = queue.get()
        if t<1:
            if v == k: return d
            visited[v] = True
            for u, w, rt2 in G[v]:
                if not visited[u]:
                    if v == s:
                        if rt2 == 'I':
                            queue.put((u, d, w, rt2))
                        else:
                            queue.put((u, d, w, rt2))
                    else:
                        if rt == rt2:
                            if rt == 'I':
                                queue.put((u, d, 5+w, rt2))
                            else:
                                queue.put((u, d, 10+w, rt2))
                        else:
                            queue.put((u, d, 20+w, rt2))
        else:
            queue.put((v, d+1, t-1, rt))

def tory_amos( E, A, B ):
    n = len(E)
    nlist = [[] for _ in range(n)]

    for x, y, d, t in E:
        nlist[x].append((y, d, t))
        nlist[y].append((x, d, t))

    res = bfs(A, B, nlist)
    #print(res)

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
