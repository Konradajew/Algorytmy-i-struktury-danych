from zad4testy import runtests

def DFS(L, x, y, t, visited, min_p, max_p, inp):
    visited[x] = True

    if x == y and max_p-min_p <= 2*t:
        return True

    for i in range(inp, len(L)):
        u, v, p = L[i][0], L[i][1], L[i][2]
        if x == 0:
            min_p = p
            max_p = p
        if (u == x or v == x) and not visited[u if v == x else v] and abs(min_p - p) <= 2*t:
            new_min_p = min(min_p, p)
            new_max_p = max(max_p, p)
            if DFS(L, u if v == x else v, y, t, visited, new_min_p, new_max_p, i):

                return True

    visited[x] = False
    return False

def Flight(L, x, y, t):
    n = len(L)
    visited = [False] * n
    return DFS(L, x, y, t, visited, 0, 0, 0)

runtests(Flight, all_tests = True)