from zad2testy import runtests

def ksum(T, k, p):
    def bin_insert(T, el):
        left = 0
        right = p - 1

        if T[right] <= el:
            T.append(el)
            return T
        while left != right:
            middle = (left + right) // 2
            if el > T[middle]:
                left = middle
            elif el < T[middle]:
                right = middle
            else:
                T.insert(middle, el)
                return T
            if left + 1 == right and T[left] < el < T[right]:
                T.insert(left + 1, el)
                return T

        T.insert(right, el)
        return T

    def bin_delete(T, el):
        left = 0
        right = p
        if T[right] == el:
            T.pop(right)
            return T
        while left != right:
            middle = (left + right) // 2
            if el > T[middle]:
                left = middle
            elif el < T[middle]:
                right = middle
            else:
                T.pop(middle)
                return T
            if left + 1 == right and T[left] < el < T[right]:
                T.pop(left)
                return T


    n = len(T)
    print(n)
    b = sorted(T[:p])
    suma = 0
    in_to_del = 0
    in_to_add = p

    for i in range(0, n - p + 1):
        suma += b[p - k]
        if i < n-p:
            x, y = T[in_to_add], T[in_to_del]
            b = bin_insert(b, x)
            b = bin_delete(b, y)

        in_to_del += 1
        in_to_add += 1

    return suma

runtests( ksum, all_tests=True )
