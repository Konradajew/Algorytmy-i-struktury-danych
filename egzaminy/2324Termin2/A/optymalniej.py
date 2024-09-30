from egz2atesty import runtests
import itertools

"""
To jest troche szybsze ale nadal tragiczne
"""

def is_correct(perm, n):
    for i in range(0, n//2):
        x, y = min(perm[i]), max(perm[i])
        for j in range(i, n//2):
            x1, y1 = min(perm[j]), max(perm[j])
            if x < x1 < y < y1 or x1 < x < y1 < y:
                return False
    return True

def calc_val(perm, n, T):
    val = 0
    for i in range(0, n//2):
        val += abs(T[perm[i][0]] - T[perm[i][1]])
    val += n//2
    return val

def unique_pairs(numbers):
    # Tworzymy wszystkie możliwe kombinacje liczb w parach
    all_combinations = list(itertools.combinations(numbers, 2))

    # Tworzymy wszystkie możliwe podziały na zestawy par
    unique_splits = []
    for pairs in itertools.combinations(all_combinations, len(numbers) // 2):
        used_numbers = set(itertools.chain.from_iterable(pairs))
        if len(used_numbers) == len(numbers):
            unique_splits.append(pairs)

    return unique_splits

def wired( T ):
    n = len(T)
    Min = float('inf')
    indexes = [i for i in range(0, n)]

    if n < 15:
        permutations = unique_pairs(indexes)
        Min = float('inf')

        print(len(permutations))

        for perm in permutations:
            if is_correct(perm, n):
                val = calc_val(perm, n, T)
                Min = min(val, Min)


    return Min

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = False )
