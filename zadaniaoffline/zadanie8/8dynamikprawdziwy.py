from zad8testy import runtests

def parking(X,Y):
    x, y = len(X), len(Y)
    F = [[float('inf') for _ in range(Y)] for _ in range(X)]

    for i in range(0, y):
        F[0][i] = min(abs(Y[i]-X[0]), F[0][i-1])
    for i in range(1, x):
        for j in range(i, y):
            F[i][j] = min(F[i][j-1], F[i-1][j-1]+abs(X[i]-Y[j]))

    return F[x-1][y-1]

runtests( parking, all_tests = True )