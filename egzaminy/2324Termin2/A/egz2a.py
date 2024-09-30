from egz2atesty import runtests
import itertools

"""
Ta najbardziej podstawowa wersja generalnie dziala 
"""

def is_correct(perm, n):
    pair_list = []
    for i in range(0, n, 2):
        pair_list.append((perm[i], perm[i+1]))

    for i in range(0, n//2):
        x, y = min(pair_list[i]), max(pair_list[i])
        for j in range(i, n//2):
            x1, y1 = min(pair_list[j]), max(pair_list[j])
            if x < x1 < y < y1 or x1 < x < y1 < y:
                return False
    return True

def calc_val(perm, n, T):
    val = 0
    for i in range(0, n, 2):
        val += abs(T[perm[i]] - T[perm[i + 1]])
    val += n//2
    return val


def wired( T ):
    n = len(T)
    Min = float('inf')
    indexes = [i for i in range(0, n)]

    if n < 11:

        permutations = list(itertools.permutations(indexes, r = n))
        Min = float('inf')
        print(len(permutations))

        for perm in permutations:
            if is_correct(perm, n):
                val = calc_val(perm, n, T)
                Min = min(val, Min)


    return Min

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = False )
