
from egz3atesty import runtests
from queue import PriorityQueue

#O(n^2)
def goodknight( G, s, t ):

    return
    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )

#testy kontrolne, do sprawdzenia poprawności
"""
G=[[-1, 8, -1, -1, -1, 8, -1, -1, -1],
[ 8, -1, 1, -1, -1, -1, -1, -1, -1],
[-1, 1, -1, 8, -1, -1, -1, -1, -1],
[-1, -1, 8, -1, 4, -1, -1, -1, -1],
[-1, -1, -1, 4, -1, -1, -1, -1, 5],
[ 8, -1, -1, -1, -1, -1, 8, -1, -1],
[-1, -1, -1, -1, -1, 8, -1, 8, -1],
[-1, -1, -1, -1, -1, -1, 8, -1, 8],
[-1, -1, -1, -1, 5, -1, -1, 8, -1]]
print(goodknight(G,0,8)) #40

G=[[-1, 8, -1, -1, -1, 8, -1, -1],
[ 8, -1, 1, -1, -1, -1, -1, -1],
[-1, 1, -1, 8, -1, -1, -1, -1],
[-1, -1, 8, -1, 1, -1, -1, -1],
[-1, -1, -1, 1, -1, -1, 5, 8],
[ 8, -1, -1, -1, -1, -1, 8, -1],
[-1, -1, -1, -1, 5, 8, -1, -1],
[-1, -1, -1, -1, 8, -1, -1, -1]]
print(goodknight(G,0,7)) #37
"""
