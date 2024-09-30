from egz1btesty import runtests

def planets( D, C, T, E ):
    n = len(D)
    F = [[float('inf') for _ in range(n)] for _ in range(E+1)]

    F[0][0]=0
    for i in range(0, n-1):
        for j in range(1, E+1): #zakladamy, ze zawsze mamyw w baku tyle litrow paliwa
            F[j][i] = min(F[j][i], F[j-1][i]+C[i])
            if j >= D[i]-D[i-1]:
                F[j][i] = min(F[j][i], F[j][i - 1] + (D[i]-D[i-1]) * C[i])
        if T[i][0] != i:
            F[0][T[i][0]] = min(F[0][T[i][0]], F[0][i]+T[i][1])
        dist = D[i + 1] - D[i]
        for k in range(dist, E + 1):
            F[k-dist][i + 1] = min(F[k - dist][i + 1], F[k][i])

    for r in F:
        print(r)

    return False


runtests( planets, all_tests = False )
