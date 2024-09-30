from zad2testy import runtests
from testy import *

def ksum(T, k, p):
    # tu prosze wpisac wlasna implementacje
    def mergeSort(A):
        n = len(A)
        if n > 1:

            mid = n // 2
            L = A[:mid]
            R = A[mid:]
            mergeSort(L)
            mergeSort(R)

            i = j = k = 0

            # scalanie
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1

            # kopiowanie pozostalych elemntow z L
            while i < len(L):
                A[k] = L[i]
                i += 1
                k += 1

            # kopiowanie pozostalych elemntow z R
            while j < len(R):
                A[k] = R[j]
                j += 1
                k += 1
        return A

    def binary_insert(A, val):

        start = 0
        end = len(A) - 1

        while start <= end:

            middle = (start + end) // 2

            if val == A[middle]:
                A.insert(middle, val)
                return A
                # A = A[:middle] + [val] + A[middle:]
            elif val < A[middle]:
                end = middle - 1
            else:
                start = middle + 1

        A.insert(start, val)
        return A

    def binary_remove(A, val):

        start = 0
        end = len(A) - 1

        while start <= end:

            middle = (start + end) // 2

            if val == A[middle]:
                # A = A[:middle] + A[middle+1:]
                A.pop(middle)
                return A
            elif val < A[middle]:
                end = middle - 1
            elif val > A[middle]:
                start = middle + 1

        return A

    n = len(T)
    suma = 0

    A = T[0:p]
    A = mergeSort(A)
    suma += A[p - k]
    i = p
    x = 0

    while (i < n):
        binary_insert(A, T[i])
        binary_remove(A, T[x])
        suma += A[p - k]

        i += 1
        x += 1

    return suma


runtests(ksum, all_tests=True)