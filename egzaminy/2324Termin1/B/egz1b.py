from egz1btesty import runtests

def kstrong( T, k):
    n = len(T)
    F = [[-float('inf') for _ in range(k+1)] for _ in range(n)]

    F[0][0] = T[0]
    for i in range(1, n):
        F[i][0] = max(T[i], F[i-1][0]+T[i])
    for i in range(0, n):
        for j in range(1, k+1):
            if i == j:
                F[i][j] = max(F[i][j-1], T[i])
            elif i > j:
                F[i][j] = max(F[i-1][j] + F[i-1][j-1]-F[i-1][j], F[i][j-1] - F[i-1][j-1]+F[i-1][j])

    #print(T)
    #for r in F:
    #    print(r)
    #print(max(F[n-1]))
    return max(F[i][j] for i in range(n) for j in range(k + 1))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = False )
