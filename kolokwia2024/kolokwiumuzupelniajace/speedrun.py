from kolutesty import runtests

def topological_sort(list, size):
    visited = [False for _ in range(size)]
    stack = []

    def dfs(v):
        visited[v] = True
        for neighbor in list[v]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(v)

    for i in range(size):
        if not visited[i]:
            dfs(i)

    return stack[::-1]

def longest_path(list ,t_sort, size):
    dist = [-float('inf') for _ in range(size)]
    for u in t_sort:
        if dist[u] == -float('inf'):
            dist[u] = 0
        for neighbor in list[u]:
            if dist[neighbor] < dist[u] + 1:
                dist[neighbor] = dist[u] + 1

    max_distance = max(dist)
    return max_distance

def projects(n, L):
    graf = [[] for _ in range(n)]
    print(len(L))
    for e in L:
        graf[e[0]].append(e[1])

    new_l = topological_sort(graf, n)
    dist = longest_path(graf, new_l, n)

    return dist+1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
