from egzP1atesty import runtests
"""
dynamik n*m i on działa, czas rozwiązania: 45 min

"""

def titanic( W, M, D ):
    #print(D)
    for r in D:
        print(M[r])
    #print(W)
    S = ""
    for l in W:
        for l2, m in M:
            if l==l2: S += m
    #print(S)
    n = len(S)
    m = len(D)
    F = [[float('inf') for _ in range(n+1)] for _ in range(m)]
    for i in range(0, m):
        F[i][0] = 0
    min_kol = [float('inf') for _ in range(n+1)]
    min_kol[0] = 0
    for i in range(1, n+1):
        for j in range(0, m):
            litera = M[D[j]][1]
            poz_wier = i + len(M[D[j]][1]) - 1
            #print(poz_wier)
            if litera == S[(i-1):(poz_wier)]:
                F[j][poz_wier] = min(F[j][poz_wier], min_kol[i-1]+1)
                min_kol[poz_wier] = min(min_kol[poz_wier], F[j][poz_wier])
    #for r in F:
    #    print(r)
    return min_kol[n]

runtests ( titanic, recursion=False )
