from zad4testy import runtests

def Flight(L,x,y,t):
    def new_p(T, p, t):
        new_T = [] * len(T)
        for e in T:
            if abs(e[2] - p) <= t:
                new_T.append((e[0], e[1], abs(e[2] - p)))
        return new_T

    def bfs(L, x, y):  # ale uposledzony bo w sumie wiele nie potrzeba zeby to dzialalo
        n = len(L)
        visited = [False for _ in range(y + 1)]
        visited[0] = True
        for i in range(0, n):
            if visited[L[i][0]] or visited[L[i][1]]:
                visited[L[i][1]] = True
                visited[L[i][0]] = True
                if L[i][1] == y:
                    return True

        return False

    i = 0
    while L[i][0] == 0:
        u, v, p = L[i][0], L[i][1], L[i][2]
        for j in range(p-t, p+t+1):
            new_L = new_p(L, j, t)
            if bfs(new_L, x, y):
                return True
        i += 1

    return False


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
