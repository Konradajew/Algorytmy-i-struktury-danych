from egz2btesty import runtests
"""
latwy i przyjemny kodzik nie jak poprzednie zadanie, choc jak zauwazay sie dzialajacy wzor dla max dom to wszystko jest git

Tworzymy tablice m na n gdzie n to biurowce a m parkingi, najblizszy parking to ten w prawo lub w lewo
zatem F[i][j] = F lewej_gory + nowy wybrany parking, zeby nie wybrac 2 razy tego samego lub przepisanie wartosci F z lewej
jezeli ta jest mniejsza wynik uzyskujemy w F[n-1][m-1]
"""

def parking(X, Y):
    n = len(X)  #biurowiec
    m = len(Y)   #parking
    F = [[float('inf') for _ in range(m)] for _ in range(n)]
    for i in range(0, m):
        F[0][i] = min(abs(X[0]-Y[i]), F[0][i-1])
    for i in range(1, n):
        for j in range(i, m):
            F[i][j] = min(F[i][j-1], F[i-1][j-1] + abs(X[i]-Y[j]))

    #for r in F:
    #    print(r)
    return F[n-1][m-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)