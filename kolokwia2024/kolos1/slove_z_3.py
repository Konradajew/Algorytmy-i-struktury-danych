from kol1testy import runtests

def maxrank(T):

    def quicksort(arr, low, high):
        if low < high:
            q = partition(arr, low, high)
            quicksort(arr, low, q-1)
            quicksort(arr, q, high)

    def partition(arr, low, high):
        x = arr[high][0]
        i = low - 1
        #print(arr[0][0])
        for j in range(low, high):
            if arr[j][0] <= x:
                i += 1
                arr[i][0], arr[j][0] = arr[j][0], arr[i][0]
                arr[i][1], arr[j][1] = arr[j][1], arr[i][1]
        arr[i+1][0], arr[high][0] = arr[high][0], arr[i+1][0]
        arr[i + 1][1], arr[high][1] = arr[high][1], arr[i + 1][1]
        return i+1

    n = len(T)
    new_ind = [[T[i], i, i] for i in range(0, n)]
    # po quicksorcie liczby w tablicy maja postac [liczba, stary_indeks, nowy_indeks]
    # dzieki temu można zrobic ctrl c ctlr v z 3 i dziala ez
    quicksort(new_ind, 0, n-1)

    # jeszcze dla tych samych wartosci trzeba ujednolicic indeksy, wiadomo zeby sie nie okazalo, ze 5 dominuje 5
    for i in range(1, n):
        if new_ind[i][0] == new_ind[i-1][0]:
            new_ind[i][2] = new_ind[i-1][2]

    P = []
    for e in new_ind:
        P.append((e[1]+1, e[2]+1))

    maks_sila = 0
    # troche trzeba pozmieniac zakresy, bo idziemy az do wartosci maxymalnej n wlacznie, bo nie od zera tylko od 1
    # bo dla wspolrzednych z zerem sie kod pierdoli, a jak obie zwiekszam o jeden to ez
    licznik_x = [0] * (n + 2)
    licznik_y = [0] * (n + 2)

    for point in P:
        x = point[0]
        y = point[1]
        licznik_x[x] += 1
        licznik_y[y] += 1

    prefix_sum_x = [0] * (n + 2)
    prefix_sum_y = [0] * (n + 2)

    for i in range(1, n + 2):
        prefix_sum_x[i] = prefix_sum_x[i - 1] + licznik_x[i]
        prefix_sum_y[i] = prefix_sum_y[i - 1] + licznik_y[i]

    for point in P:
        x = point[0]
        y = point[1]

        pom = prefix_sum_x[x - 1] + prefix_sum_y[y - 1] - n + 1
        maks_sila = max(maks_sila, pom)

    return maks_sila

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
