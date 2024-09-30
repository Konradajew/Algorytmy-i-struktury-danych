print("fiut")
"""
Konrad Szymański 421297
zwykły brute force sprawdza ile elementow o mniejszym indeksie jest mniejszych od niego
złożoność czasowa O(n^2), pamięciowa O(n) tylko na tablicy działa
Po tablicy przechodzę od tyłu bo dla losowych danych jest to optymalniejsze
"""

from kol1testy import runtests

def maxrank(T):
    n = len(T)
    max_dom = 0
    cur = 0
    for i in range(n-1, -1, -1):  #przechodzenie od tyłu to dobra optymalizacja, ale niestesty to nadal brute forca
        for j in range(0, i):
            if T[i] > T[j]:
                cur += 1
        if cur > max_dom:
            max_dom = cur
        if max_dom > i:
            return max_dom
        cur = 0
    return max_dom

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
