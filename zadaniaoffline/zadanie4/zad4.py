"""
Konrad Szymański 421297
Algorytm jest to dfs, którego zamysłem jest znalezienie wszystkich sciezek z x do y, oczywiscie gdy roznica wysokosci
jest juz za duza przerywane jest dzialanie, wywolywanie jest rekurencyjne. Zlozonosc czasowa wynosi O(V!) (najgorszy
przypadek to graf pelny gdzie). Zlozonosc pamieciowa wynosi O(len(L)).

"""

from zad4testy import runtests

def DFS(L, x, y, t, visited, min_p, max_p):
    visited[x] = True

    if x == y and max_p-min_p <= 2*t:
        return True

    if max_p-min_p > 2*t:  # dzialanie optymalizacyjne
        visited[x] = False
        return False

    for u, v, p in L:
        if x == 0:
            min_p = p
            max_p = p
        if (u == x or v == x) and not visited[u if v == x else v] and abs(max_p - p) <= 2*t:
            new_min_p = min(min_p, p)
            new_max_p = max(max_p, p)
            if DFS(L, u if v == x else v, y, t, visited, new_min_p, new_max_p):
                return True

    visited[x] = False
    return False

def Flight(L, x, y, t):
    visited = [False] * (y + 1)
    return DFS(L, x, y, t, visited, 0, 0)

runtests(Flight, all_tests = True)
