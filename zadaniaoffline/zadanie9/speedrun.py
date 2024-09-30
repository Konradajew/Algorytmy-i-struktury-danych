"""
Konrad Szymański 421297
Przerabiam na graf nieskierowany acykliczny sortuje topologicznie z użyciem dfs, następnie znajduje najdłuższą ścieżke
żłożoność czasowa O(n*m) choć stała nie najlepsza
Nie jest to co prawda dynamik, ale lubie grafy
"""
from zad9testy import runtests

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

def trip(M):
    n, m = len(M), len(M[0])
    neighbours = [[] for _ in range(n*m)]
    for i in range(n):
        for j in range(m):
            if i < n-1:
                if M[i + 1][j] > M[i][j]:  # do dołu
                    neighbours[i * m + j].append(i * m + m + j)
            if j < m-1:
                if M[i][j + 1] > M[i][j]:  # do prawej
                    neighbours[i * m + j].append(i * m + j + 1)
            if j > 0:
                if M[i][j - 1] > M[i][j]:  # do lewej
                    neighbours[i * m + j].append(i * m + j - 1)
            if i > 0:
                if M[i - 1][j] > M[i][j]:  # do góry
                    neighbours[i * m + j].append(i * m - m + j)

    t_sort = topological_sort(neighbours, n*m)
    max_dist = longest_path(neighbours, t_sort, n*m)

    return max_dist + 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )