from egz2atesty import runtests
"""
liczymy liczbe punktow o danym x - tX
maksymalnego y dla danego x maksY (bo maksymalny y jest bardziej dominujacy niz jakis inny)
liczbe punktow o yi>=y - tY

zauwazamy, ze dla najbardziej dominujacego zachodzi
ilosc zdominowanych = n - (punkty o >= x) - (punkty o >= y) + 1 (bo odejmujemy nasz punkt dwa razy)
ten wzor dziala bo dla najbardziej dominujacego punktu zbiory >=x i >=y sa rozlaczne poza naszym punktem
dla reszty punktow wyniki sa niepoprawne moga wychodzic nawet ujemne

"""
def dominance(P):

    n = len(P)
    tX = [0 for _ in range(n+1)]
    tY = [0 for _ in range(n+1)]
    maksY = [0 for _ in range(n+1)]
    # liczba punktów o danym x i y
    for i in range(0, n):
        tX[P[i][0]] += 1
        tY[P[i][1]] += 1
        if P[i][1] > maksY[P[i][0]]:
            maksY[P[i][0]] = P[i][1]

    #liczba punktów dla danego yi o y>=yi i xi>=x
    for i in range(n-1, -1, -1):
        tY[i] += tY[i+1]
        tX[i] += tX[i+1]

    dominator = 0
    for i in range(n, 0, -1):
        curr = n - tY[maksY[i]] - tX[i] + 1
        dominator = max(curr, dominator)
    #ciekawostka ten wzor dziala tylko dla najbardziej dominujacego punktu

    return dominator

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True)
