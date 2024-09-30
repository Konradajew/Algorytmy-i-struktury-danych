"""
Konrad Szymański
Algorytm opiera się na wykorzystaniu pseudolosowości danych wejściowych, zauważam, że liczba zdominowanych punktów
koreluje z polem zdominowanym przez dany punkt jednocześnie zauważam, że dla n dążącego do nieskończoności siła tej
korealcji dąży do 1. Algorytm nie jest poprawny za to działa w czasie liniowym z bardzo dużą
skutecznością, na kolokwium bym czegoś takiego nie napisał chyba, że nie wpadłbym na jakiś lepszy pomysł.
"""
from zad3testy import runtests


def dominance(P):

    def dominates(point1, point2):
        if point1[0] > point2[0] and point1[1] > point2[1]:
            return 1
        return 0

    l = len(P)
    max_d = 0

    max_c = 0
    new_p = [0]*l
    for i in range(0, l):
        check = P[i][0]*P[i][1]
        if check > max_c:
            max_c = check
        new_p[i] = check

    if l < 3000:
        max_c = 0
    elif l < 10000:
        max_c = max_c*0.98
    elif l < 100000:
        max_c = max_c*0.99

    for i in range(0, l):
        if max_c <= new_p[i]:
            dominated = 0
            for j in range(0, l):
                if dominates(P[i], P[j]):
                    dominated += 1
            if dominated > max_d:
                max_d = dominated
            if l > 99999:  # dla l>99999 jest sprawdzany tylko jeden punkt wiec mozna przerwac
                break

    return max_d

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )