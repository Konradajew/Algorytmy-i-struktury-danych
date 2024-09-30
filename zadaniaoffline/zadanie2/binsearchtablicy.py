"""
Konrad Szymański
Algorytm sortuje rosnąca pierwsze p elementów, dodaje k-ty największy do sumy, następnie dodaje (w posortowany sposób)
do tablicy z posortowanymi elementami kolejny element tablicy T, i usuwa pierwszy element tablicy T z posortowanej tablicy
(w kolejnych iteracjach drugi itd), proces ten powtarza się aż do ostatniego indeksu tablicy T. Po pętli zwraca wynik
"""


from zad2testy import runtests

def ksum(T, k, p):
    def mergesort(T):
        if len(T) > 1:
            left = T[:len(T) // 2]
            right = T[len(T) // 2:]

            mergesort(left)
            mergesort(right)

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    T[k] = left[i]
                    i += 1
                else:
                    T[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                T[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                T[k] = right[j]
                j += 1
                k += 1

    def bin_insert(T, el):  # wstawia element w posortowany sposób do tablicy
        left = 0
        right = p - 1  # długośc tablicy danej do funkcji zawsze ma długość p czyli ostatni indeks to p-1

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
                T.insert(left+1, el)
                return T

        T.insert(right, el)
        return T

    def bin_delete(T, el):  # usuwa element z tablicy
        left = 0
        right = p  # długośc tablicy danej do funkcji zawsze ma długość p+1(bo najpierw insertuje w forze) czyli ostatni indeks to p
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
    b = T[:p]
    mergesort(b)
    suma = 0
    in_to_del = 0
    in_to_add = p

    for i in range(0, n - p + 1):
        suma += b[p - k]
        if i < n-p:
            b = bin_insert(b, T[in_to_add])
            b = bin_delete(b, T[in_to_del])

        in_to_del += 1
        in_to_add += 1

    return suma

runtests( ksum, all_tests=True )
"""
Komentarz do złożoności czasowej i zużytej pamięci:
Złożoność czasowa:
sortowania na początku ma złożość plogp, następnie n-p razy przechodzimy pętle, w której wywołujemy fukcje bin_insert
oraz bin_delete, wyszukiwanie binarne ma złożoność O(logp) natomiast insert i pop mają złożonośc O(p), są one jednak
od siebie niezależne więc nienależy ich przemnażać, zatem złożoność czasowa całego algorytmu ma finalnie postać O(np)
Złożoność pamięciowa:
Tablica T - O(n) (jako jej długość)
Tablica b - O(p) (jako jej długość)
mergesort - O(logp)
bin_insert - O(logp) (wyszukiwanie) + O(p) (insert)
bin_delete - O(logp) (wyszukiwanie) + O(p) (pop)
zatem złożoność pamięciowa ma postać O(n+3p+3logp)
"""