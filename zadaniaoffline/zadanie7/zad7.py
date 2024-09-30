"""
Konrad Szymański 421297
Zauważam, że nasz labirynt jest prawie grafem skierowanym acyklicznym, następnie zauważam, że ze względu na warunki zadania
po wejściu do kolumny możemy poruszać się tylko w dół lub w górę zatem rozdzielam każdą kolumnę na dwie kolumny
w jednej można poruszać się tylko w górę w drugiej tylko w dół. Następnie przekształcam to w acykliczny graf skierowany
na którym uruchamiam niepełne sortowanie topologiczne(interesuje mnie tylko posortowanie wierzchołków do których da się dotrzeć
z 0,0) następnie obliczam długość najdłuższej ścieżki do n-1,n-1 o ile ta istnieje.
Złożoność czasowa:
Przekształcenie w graf O(n*n)
sortowanietopologiczne O(V+E)=O(n*n)   (z każdego wierzchołka w grafie wychodzi średnio (2~3) krawędzie, więc nie zwiększa to złożoności)
Więc złożoność czasowa wynosi: O(n*n)
Niestety stała jest dosyć słaba, ale mam nadzieję, że przejdzie testy
Pamięciowa: O(n*n) jako wielkość tablicy sąsiedzctwa, która reprezentuje graf
"""
from zad7testy import runtests

def dfs(s, V, visited, list):
    visited[s] = True
    for v in V[s]:
        if not visited[v]:
            dfs(v, V, visited, list)

    list.append(s)

def longest_path(s, V, list, size):
    dist = [-float('inf') for _ in range(size)]
    dist[s] = 0
    for v in list:
        if dist[v] >= 0:
            for n in V[v]:
                if dist[n] < dist[v] + 1:
                    dist[n] = dist[v] + 1
    return dist

def maze( L ):
    n = len(L)
    neighbours = [[] for _ in range(n*n)]
    neighbours2 = [[] for _ in range(n*n)]

    for i in range(0, n):  #kolejne wiersze
        for j in range(0, n):   #wnetrze wiersza
            if L[i][j] == ".":
                #i*n+j obecny wierzchołek ale w tej kolumnie idziemy tylko do dolu
                #n*n i*n+j obecny wierzchołek ale w tej kolumnie idziemy tylko do gory
                if j < n-1:  #krawedz do prawej zarowno z kolumny gora/dol do kolumn gora/dol
                    if L[i][j+1] == ".":
                        neighbours[i*n+j].append(i*n+j+1)
                        neighbours2[i*n+j].append(i*n+j+1)
                        neighbours[i*n+j].append(n*n + i * n + j + 1)
                        neighbours2[i*n+j].append(n*n + i * n + j + 1)
                if i < n-1:  #krawedz do dolu
                    if L[i+1][j] == ".":
                        neighbours[i*n+j].append(i*n+n+j)
                if i > 0:   #krawedz do gory
                    if L[i-1][j] == ".":
                        neighbours2[i*n+j].append(n*n+i*n-n+j)
                #pierwsza i ostatnia kolumna w których idzie się tylko do góry nie są potrzebne, ale
                #indeksowanie jest łatwiejsze jeżeli się je doda

    neighbours = neighbours + neighbours2
    visited = [False for _ in range(n*n*2)]
    lista = []
    dfs(0, neighbours, visited, lista)
    if not visited[n*n-1]:  #lekka optymalizacja jeżeli nie da się dojść do n-1,n-1
        return -1
    lista = lista[::-1]
    dist = longest_path(0, neighbours, lista, n*n*2)
    return dist[n*n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )