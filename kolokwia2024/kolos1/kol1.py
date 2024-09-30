"""
Konrad Szymański 421297
zwykły brute force sprawdza ile elementow o mniejszym indeksie jest mniejszych od niego
złożoność czasowa O(n^2), pamięciowa O(n) tylko na tablicy działa
Po tablicy przechodzę od tyłu bo dla losowych danych jest to optymalniejsze
W zasadzie można nawet wyargumentować, że dla losowych danych złożonośc nie powinna przekroczyć ~nsqrt(n), ale to
i tak bruteforce

Wymyśliłem jakiś tam sposób na nlogn, ale nie dałem rady zakodować pomysł był taki, że w quicksorcie
zwracamy jeszce liste nowych indeksów danej liczby liczby i jeżeli min(stary_ind, nowy_indeks) = stary_ind to
ta liczba dominuje dokładnie tyle liczb dla różnych danych dla tych samych nie ma specjalnego znaczenia w sumie
jeżeli min to nowy_ind jest to liczba maxymalnie zdominowanych liczb, powinno działać
"""

from kol1testy import runtests

def maxrank(T):
    n = len(T)
    max_dom = 0
    cur = 0
    max_w = []
    c_max_w = 0
    for i in range(n-1, -1, -1):
        if T[i] > c_max_w:
            max_w.append(T[i])
            c_max_w = T[i]
    c_max_w = 0
    for i in range(n-1, -1, -1): #przechodzenie od tyłu to dobra optymalizacja, ale niestesty to nadal brute forca
        if T[i] == max_w[c_max_w]:
            for j in range(0, i):
                if T[i] > T[j]:
                    cur += 1
            if cur > max_dom:
                max_dom = cur
            cur = 0
            c_max_w += 1
            if max_dom > i or c_max_w >= len(max_w):
                return max_dom
    return max_dom

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
