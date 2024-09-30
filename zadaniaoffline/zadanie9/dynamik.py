"""
Konrad Szymański 421297
Przerabiam na graf nieskierowany acykliczny sortuje topologicznie z użyciem dfs, następnie znajduje najdłuższą ścieżke
żłożoność czasowa O(n*m) choć stała nie najlepsza
"""
from zad9testy import runtests

def trip(M):
    n, m = len(M), len(M[0])
    T = [[0 for _ in range(m)] for _ in range(n)]

    def longest_path(i, j):
        if T[i][j] == 0:
            flag = True
            if i < n - 1:
                if M[i + 1][j] > M[i][j]:  # do dołu
                    if T[i + 1][j] > 0:
                        T[i][j] = max(T[i][j], T[i + 1][j]+1)
                    T[i][j] = max(T[i][j], longest_path(i+1, j)+1)
                    flag = False
            if j < m - 1:
                if M[i][j + 1] > M[i][j]:  # do prawej
                    if M[i][j + 1] > 0:
                        T[i][j] = max(T[i][j], T[i][j + 1]+1)
                    T[i][j] = max(T[i][j], longest_path(i, j + 1)+1)
                    flag = False
            if j > 0:
                if M[i][j - 1] > M[i][j]:  # do lewej
                    if M[i][j - 1] > 0:
                        T[i][j] = max(T[i][j], T[i][j - 1] + 1)
                    T[i][j] = max(T[i][j], longest_path(i, j - 1)+1)
                    flag = False
            if i > 0:
                if M[i - 1][j] > M[i][j]:  # do góry
                    if M[i - 1][j] > 0:
                        T[i][j] = max(T[i][j], T[i - 1][j] + 1)
                    T[i][j] = max(T[i][j], longest_path(i - 1, j)+1)
                    flag = False
            if flag:
                T[i][j] = 1
                return 1
        if T[i][j] > 0:
            return T[i][j]

    Max = 0
    for i in range(0, n):
        for j in range(0, m):
            if T[i][j] == 0:
                if i < n-1:
                    if M[i + 1][j] > M[i][j]:  # do dołu
                        longest_path(i, j)
                if j < m-1:
                    if M[i][j + 1] > M[i][j]:  # do prawej
                        longest_path(i, j)
                if j > 0:
                    if M[i][j - 1] > M[i][j]:  # do lewej
                        longest_path(i, j)
                if i > 0:
                    if M[i - 1][j] > M[i][j]:  # do góry
                        longest_path(i, j)
            if T[i][j] > Max:
                Max = T[i][j]
    return Max

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = False )