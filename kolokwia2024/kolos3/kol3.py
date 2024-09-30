from kol3testy import runtests

def orchard(T, m):
    n = len(T)
    F = [[float('inf') for _ in range(m)] for _ in range(n)]
    for i in range(0, n):
        T[i] = T[i]%m
    F[0][0] = 1
    F[0][T[0] % m] = 0

    for i in range(1, n):
        for j in range(m):
            F[i][j] = min(F[i-1][(j-T[i]) % m], F[i-1][j] + 1)

    return F[n-1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
