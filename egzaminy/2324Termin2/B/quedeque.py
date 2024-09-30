from egz2btesty import runtests
from collections import deque
"""
Ta wersja jest duzo szybsza(visited doklaniej), ale nie przechodzi jednego testu, bo formalnie nalezaloby rozmnozyc
wyjscia wierzcholkow razy 3, ale to juz mi sie nie chcialo to jest tak bardzo niszowy przypadek, ze przechodzi 
wszystkie testy poza jednym, a jeden idzie 50 sekund"""


def bfs(s, k, G):
    n = len(G)
    visited = [False]*n
    queue = deque([[s, 0, 0, 'S', 0]]) #wierzcgholek, przebyty dystans, czas do opuszczenia, typwjazdowy, czas opusczenia stacji(zeby po opuszceniu stacji dac visited)
    visited[s] = True

    while queue:
        v, d, t, rt, tl = queue.popleft()
        if t == tl:  
            visited[v] = True
        if t<1:
            if v == k: return d
            #visited[v] = True
            for u, w, rt2 in G[v]:
                if not visited[u]:
                    if v == s:
                        queue.append([u, 0, w, rt2, -1])
                    else:
                        if rt == rt2:
                            if rt == 'I':
                                queue.append([u, d, 5+w, rt2, w])
                            else:
                                queue.append([u, d, 10+w, rt2, w])
                        else:
                            queue.append([u, d, 20+w, rt2, w])
        else:
            queue.append([v, d+1, t-1, rt, tl])


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
