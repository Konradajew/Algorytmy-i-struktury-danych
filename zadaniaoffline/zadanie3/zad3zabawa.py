from zad3testy import runtests


def dominance(P):
    # super nowa solucja bez nie heurystyczna
    sort_x = []
    for i in range(0, len(P)):
        sort_x.append(P[i][0])
    sort_y = []
    for i in range(0, len(P)):
        sort_y.append(P[i][1])
    sort_x.sort()
    sort_y.sort()
    print(sort_x, sort_y)

    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
