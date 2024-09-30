from zad1testy import Node, runtests

"""super wersja na tablicach maksymalnie optymalna, ale niestety falisz dal takie ograniczenia
czasowe, ze wersja na tablicach nie przejdzie jak widac tworzenie tablicy w pamieci troche zajmuje"""

def SortH(p,k):
    def mergesort(ar):
        if len(ar) > 1:
            left_array = ar[:len(ar) // 2]
            right_array = ar[len(ar) // 2:]

            # print(left_array, right_array)
            mergesort(left_array)
            mergesort(right_array)

            i = 0
            j = 0
            l = 0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    ar[l] = left_array[i]
                    i += 1
                else:
                    ar[l] = right_array[j]
                    j += 1
                l += 1

            while i < len(left_array):
                ar[l] = left_array[i]
                i += 1
                l += 1

            while j < len(right_array):
                ar[l] = right_array[j]
                j += 1
                l += 1

    if k == 0:
        return p
    else:
        array = []
        while p is not None:
            array.append(p.val)
            p = p.next

    if k == 1:
        for i in range(0, len(array)-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1],array[i]
    else:
        for i in range(0, len(array), k+1):
            new_array = array[i:i + 2*k+1]
            mergesort(new_array)
            array[i:i + 2*k+1] = new_array
        #mergesort(array)

    head = Node()
    new_node = Node()
    head.next = new_node
    for i in range(0, len(array)):
        new_node.val = array[i]
        if i != len(array) - 1:
            newer_node = Node()
            new_node.next = newer_node
            new_node = new_node.next

    return head.next



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
