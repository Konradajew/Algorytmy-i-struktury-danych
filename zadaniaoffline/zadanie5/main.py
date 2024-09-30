from zad5testy import runtests

def end(neighbours, out, b):

    for u, p in neighbours[b]:
        if not out[u]:
            return False
        return True

def backtrack(neighbours, out, a, b, val, values):
    n = []
    for e in neighbours[a]:
        u, p = e
        val[u] = min(val[u], val[a]+p)
        val[a] = min(val[a], val[u]+p)
        if not out[u]:
            n.append(u)

    out[a] = True
    #print(val, out)
    for u in n:
        if u != b:
            backtrack(neighbours, out, u, b, val, values)
        else:
            values.append(val[b])

    return min(values)

def DFS(E, out, a, b, val):
    n = []
    for u, v, p in E:
        if (a == u or a == v) and not out[u] and not out[v] and a != b:
            val[u] = min(val[u], val[v]+p)
            n.append(u if a == v else v)
    out[a] = True
    for u in n:
        if u != b:
            return backtrack(E, out, u, b, val)
        else:
            print(val[u])


def spacetravel(n, E, S, a, b):
    out = [False] * n
    neighbours = [[] for _ in range(999999)]
    val = [99999]*n
    val[a] = 0
    for i in range(0, len(S)):
        for j in range(i+1, len(S)):
            E.append((S[i], S[j], 0))
    #print(E)
    # print(neighbours)
    for u, v, p in E:
        neighbours[u].append((v, p))
        neighbours[v].append((u, p))
    #print(neighbours)
    return backtrack(neighbours, out, a, b, val, [9999])
    #print(DFS(E, out, a, b, val))

runtests(spacetravel, all_tests = False)
