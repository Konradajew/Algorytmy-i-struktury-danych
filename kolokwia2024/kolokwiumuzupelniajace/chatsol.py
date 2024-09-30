from kolutesty import runtests
from collections import defaultdict, deque
def projects(n, L):
    graph = defaultdict(list)
    indegree = [0] * n

    # Budowanie grafu i obliczanie stopni wejściowych
    for p, q in L:
        graph[q].append(p)
        indegree[p] += 1

    # Kolejka do przetwarzania projektów o zerowym stopniu wejściowym
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    # Tablica dp do przechowywania najwcześniejszego możliwego zakończenia projektu
    dp = [0] * n

    # Przetwarzanie projektów w kolejności topologicznej
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            dp[neighbor] = max(dp[neighbor], dp[current] + 1)
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Wynik to maksymalna wartość w dp + 1 (bo zaczynamy od 0)
    return max(dp) + 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )