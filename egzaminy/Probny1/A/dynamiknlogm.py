from egzP1atesty import runtests
"""
Technicznie O(n), zauważyłem, że w poprzednim w zasadzie wystarczy jechać po samych kolumnach
gdyż tylko minimum kolumnowe ma jakieś znaczenie reszte można zignorować

litery zsetowałem więc czas dostępu O(1), reszta algorytmu O(4*n)
Zakładając, że setowanie jest zakazanie, można binarnie wyszukiwać litery do porównania wtedy mamy
4*n*logm = O(nlogm)

Czas rozwiązania: 30min, jakbys musiał napisać wyszukiwanie binarne to pewnie by jeszcze z 15min zeszło

"""

def titanic( W, M, D ):
    S = ""
    for l in W:
        for l2, m in M:
            if l==l2: S += m
    n = len(S)
    F = [float('inf') for _ in range(n+6)]
    F[0] = 0
    litery = [M[D[i]][1] for i in range(0, len(D))]
    litery = set(litery)
    for i in range(1, n+6):  #n+6, zeby mi sie indeksy nie wypierdały
        for j in range(1, 5):
            if S[(i-1):(i+j-1)] in litery:
                F[i+j-1] = min(F[i+j-1], F[i-1] + 1)

    return F[n]

runtests ( titanic, recursion=False )
