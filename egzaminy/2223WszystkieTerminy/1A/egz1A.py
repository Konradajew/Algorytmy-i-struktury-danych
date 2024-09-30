"""
na logike 2 dajkstry z dwóch stron i zadziała

"""
from egz1Atesty import runtests
from queue import PriorityQueue

def dijkstra(s, G, r, add_r):
    distances = [float('inf') for _ in range(len(G))]
    distances[s] = 0

    Q = PriorityQueue()
    Q.put((s, 0))

    while not Q.empty():
        p, w1 = Q.get()
        for v, w2 in G[p]:
            if add_r:
                if w1 + w2*2 + r < distances[v]:
                    distances[v] = distances[p] + w2*2 + r
                    Q.put((v, distances[v]))
            else:
                if w1 + w2 < distances[v]:
                    distances[v] = distances[p] + w2
                    Q.put((v, distances[v]))

    return distances

def gold(G,V,s,t,r):
    dist1 = dijkstra(s, G, r, False)
    dist2 = dijkstra(t, G, r, True)

    min = float('inf')
    for i in range(0, len(G)):
        if dist1[i] + dist2[i] - V[i] < min:
            min = dist1[i] + dist2[i] - V[i]

    return min

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
