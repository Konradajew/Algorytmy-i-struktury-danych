from zad8testy import runtests
"""
Konrad Szymański 421297
Tworzymy tablicę F o rozmiarze n*m. Zauważamy, że jeżeli wypełnilibyśmy tę tablicę odległościami z i-tego biurowca do j-tego parkingu
odpowiedzą byłaby minimalna suma schodów prowadzących w dół macierzy (jak w macierzy schodkowej, mimo, że tu nie ma
macierzy schodkowej, ale to najlepsze porównanie jakie wymyśliłem, bo zawsze w każdym kolejnym wierszu poruszamy się co 
najmniej o jedną kolumnę w prawo, i nigdy dwa lub więcej wierszy naraz w dół). Wypełniamy pierwszy wiersz minimalnymi
odległościami do kolejnych parkingów, a gdy znajdziemy wartość minimalną przepisujemy ją dalej w wierszu, ze względu na warunki
zadania wartości po prawo od wartości minimalnej wiersza nie są istotne, następnie wypełniamy drugi wiersz od 2-tej kolumny (o indeksie 1)
(ze względu na warunki zadania i tak nie można przypisać 2 biurowcowi 1 parkingu itd.) minimum (j-1 kolumny i-tego wiersza,
j-1 kolumny i i-1 wiersza i sumy odległości do parkingu o indeksie j-tym) nie rozważamy wartości z góry, bo mogło by się tak
zdarzyć, że innym biurowcom przypiszemy ten sam parking, powtarzając ten proces dalej otrzymamy 
minimalną sumę odległości w F[n-1][m-1]
Złożoność czasowa: O(n*m)
Pamięciowa: O(n*m) na tablice F
"""
def parking(X,Y):
    F = [[float('inf')]*len(Y) for _ in range(len(X))]
    for i in range(0, len(X)):
        for j in range(i, len(Y)):
            if i == 0:
                F[i][j] = min(abs(X[0]-Y[j]), F[0][j-1])
            else:
                F[i][j] = min(F[i][j-1], F[i-1][j-1] + abs(Y[j]-X[i]))

    return F[len(X)-1][len(Y)-1]

runtests( parking, all_tests = True )