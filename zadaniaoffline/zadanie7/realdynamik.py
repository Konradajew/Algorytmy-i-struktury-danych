from zad7testy import runtests

def maze( L ):
    n = len(L)
    F = [[0 for _ in range(n)] for _ in range(n)]

    F[0][0] = 1

    return 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )