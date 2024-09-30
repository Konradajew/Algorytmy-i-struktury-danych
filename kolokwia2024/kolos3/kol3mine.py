"""
Konrad Szymański 421297
Korzystając ze słówników obliczam wszystkie możliwe sumy, w czasie O(n^2), sprawdzam czy któras jest rowne potrzebnej reszcie
lub reszcie i wielokrotsci m, nie zlicza to drzew, ale jezeli sumy byłyby postaci suma: liczba drzew w slowniku to by działało
"""
from kol3testy import runtests

def lista_sum(dictlist,listaSum, i, T, n):
    if i == n:
        return dictlist
    listaSum = list(listaSum)
    k = len(listaSum)
    nl = [0 for _ in range(k)]
    for j in range(0, k):
        nl[j] = listaSum[j]+T[i]
        dictlist.add((nl[j],i+1))
    if n < 10:
        print(listaSum, nl, T[i])
    listaSum += nl
    listaSum = set(listaSum)
    return lista_sum(dictlist, listaSum, i+1, T, n)

def orchard(T, m):
    n = len(T)
    R = [None for _ in range(n)]
    s = 0
    for i in range(0, n):
        R[i] = T[i]%m
        s += T[i]

    Rc = s % m
    sL = [Rc + i*m for i in range(0, n)]
    s=[R[0]]
    ss = set()
    ss.add((R[0],1))
    sumy = lista_sum(ss, s,1, R, n)
    k=0
    for i in range(0, n):
        for m in range(0, n):
            if (sL[i],m) in sumy:
                print(sL[i], m)
                k = max(k, m)
    if n < 10:
        print(sumy)
    return n-k

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=False)
