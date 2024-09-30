from egz1btesty import runtests
"""
F(T, k) = max(F(T-1, k),    F(T-1, k-1) + T[i])
            wyrzucam T[i]      biorę T[i]

dla danego T[i] funkcja zwracą maksymalną sumę ciągu, z którego usunięto co najwyżej k elementów, kończącego się w i
"""

def kstrong( T, k):
    n = len(T)
    F = [[-float('inf') for _ in range(k+1)] for _ in range(n)]

    F[0][0] = T[0]
    for i in range(1, n):
        F[i][0] = max(T[i], F[i-1][0]+T[i], 0)  #ciąg 0-spójny
    for i in range(1, n):
        for j in range(1, k+1):
            if i == j:
                F[i][j] = max(F[i][j-1], T[i], F[i-1][j-1], 0)
            elif i > j:
                if T[i] < 0 and F[i-1][j-1] > F[i-1][j]+T[i]: 
                    F[i][j] = F[i-1][j-1]
                else:
                    F[i][j] = F[i-1][j] + T[i]
    if n == k:  #nawet dał huj taki zjebany przypadek
        F[n-1][k] = max(F[n-1][k - 1], T[n-1], F[n - 1][k - 1])

    return max(F[i][j] for i in range(n) for j in range(k + 1))
   

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
