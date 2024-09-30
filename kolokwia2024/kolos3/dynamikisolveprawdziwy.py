from kol3testy import runtests


def orchard(T, m):
    n = len(T)
    F = [[float('inf') for _ in range(m)] for _ in range(n)]
    F[0][0] = 1
    F[0][T[0] % m] = 0
    for i in range(1, n):  # i - dane drzewo
        for j in range(0, m):  # j - dana reszta, którą chcemy uzyskać
            F[i][j] = min(F[i-1][j] + 1, F[i-1][(j-T[i]) % m])
            #(j-T[i])%m = reszcie, którą musimy dodać, aby się dało uzyskać daną resztę, wystarczy zatem
            # sprawdzić ile trzeba wyciąć drzew aby reszte takową otrzymać, o ile się da
            # przechodzenie po drzewach po kolei gwarantuje, że możemy to zrobić ładnie i zgrabnie
            #dlaczego j-T[i], a nie na odwrót, bo dopełniam do j, a nie m

    return F[n-1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
