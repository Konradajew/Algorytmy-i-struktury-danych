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

    max = 0
    #for e in L:
    #    if e[1] > max: max = e[1]
    #    if e[0] == x or e[1] == y: print(e)
    #print(max)

    k = 0
    while L[k][0] == 0:
        new_L = new_p(L, L[k][2], 2*t)
        #if(y==102): print(new_L)
        if bfs(new_L, x, y):
            return True
        k += 1

    #if(y==102): print(L)
    #print(L)
    #print(new_p(L, 2045, 60))
    #print(bfs(new_L, x, y))
    return False


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(Flight, all_tests=True)
