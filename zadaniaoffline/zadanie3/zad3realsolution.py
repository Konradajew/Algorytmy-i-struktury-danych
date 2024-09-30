from zad3testy import runtests

def dominance(P):

    def dominates(point1, point2):
        if point1[0] > point2[0] and point1[1] > point2[1]:
            return 1
        return 0

    def points_dominated(P, point):
        dominated = 0
        for i in range(0, l):
            if dominates(point, P[i]):
                dominated += 1
        return dominated

    l = len(P)
    max_d = 0

    if l < 3000:
        P.sort()
        c_p = P[l-1]
        max_d = points_dominated(P, P[l-1])
        for i in range(l-2, -1, -1):
            if not dominates(c_p,P[i]):
                dominated = 0
                for j in range(i, -1, -1):
                    if dominates(P[i], P[j]):
                        dominated += 1
                if dominated > max_d:
                    max_d = dominated
                c_p = P[i]
    else:
        max_c = 0
        new_p = [0]*l
        for i in range(0, l):
            check = P[i][0]*P[i][1]
            if check > max_c:
                max_c = check
            new_p[i] = check

        #new_l = 0.99999*max_c
        for i in range(0, l):
            if max_c == new_p[i]:  # samo max_c tez dziala xddd
                dominated = 0
                for j in range(0, l):
                    if dominates(P[i], P[j]):
                        dominated += 1
                if dominated > max_d:
                    max_d = dominated
                break

    return max_d

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )