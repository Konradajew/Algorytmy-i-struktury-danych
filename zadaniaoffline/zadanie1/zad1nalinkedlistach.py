"""
Konrad Szymański  nr indeksu: 421297
Zauważamy, że sortując 2k+1 pierwszych elementów linked listy, k+1 pierwszych elementów zostanie dokładnie posortowana
(elementy będą stały na właściwych miejscach) dzieje się tak, ponieważ dany element jest maksymalnie odległy o k od
swojej pozycji czyli element minimalny będzię maksymalnie odległy od swojej pozycji o maksymalnie k miejsc, oznacza to, że sortując k+1
pierwszych elementów element 1 napewno będzie dokładnie posortowany, rozciągając to myślenie do maksimum otrzymamy, że sortując 2k+1
pierwszych elementów, k+1 z nich znajdzie się dokładnie na swoich pozycjach, następnie powtarzamy ten proces przesuwając
się za każdym razem o k+1 elementów, gdy nie jesteśmy w stanie tego zrobić zwyczajnie sortujemy reszte elementów.
Do sortowania używam merge sorta.
Podsumowując program ma posortować 2k+1 pierwszych elementów, z czego k+1 zostanie posortowancyh dokładnie, następnie
od k+2 elemntu powtarzac do skutku ten proces.
"""

from zad1testy import Node, runtests

def SortH(p,k):
    def merge_part(head, c, n):  # c - liczba juz posortowanych dokładnie elementów ll, n - długość ll
        if 2*k+1 + c >= n:  # sprawdzanie czy da się wybrać 2k+1 kolejnych elementów ll, jeżeli nie to reszta jest merge sortowana
            return (merge_sort(head), None)

        first = head
        for i in range(0, 2*k):
            head = head.next
        new = head.next  # pierwszy element ll który nie jest w tym momencie sortowany jest to potem przydatne
        head.next = None
        head = merge_sort(first)

        return (head, new)

    def merge_sort(head):
        if not head or not head.next:
            return head

        mid = find_middle(head)
        new = mid.next
        mid.next = None

        sort_left = merge_sort(head)
        sort_right = merge_sort(new)

        return merge(sort_left, sort_right)

    def merge(left, right):
        if not left:
            return right
        if not right:
            return left

        if left.val < right.val:
            r = left
            r.next = merge(left.next, right)
        else:
            r = right
            r.next = merge(left, right.next)

        return r

    def find_middle(head):
        if not head:
            return None
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def find_last(head):
        while head:
            if not head.next:
                return head
            head = head.next

    if k == 0:
        return p
    else:
        if k == 1:  # dla k=1 zauważam, że wystarczy porównywać i co najwyżej poprzepinać sąsiadujące wartości jest to szybsze niz merge sort
            g = Node()
            g.next = p
            prev = g
            while p.next:
                if p.val > p.next.val:
                    temp = p.next.next
                    prev.next = p.next
                    p.next.next = p
                    p.next = temp
                prev = p
                p = p.next
                if not p:
                    break

            return g.next
        else:
            first = p
            n = 0  # określenie długości ll
            while p:
                n += 1
                p = p.next

            if k > n:  # tak na wszelki wypadek
                head = merge_sort(p)
                return head

            mid = first
            new_ll = Node()
            c = 0  # liczba posortowanych dokładnie elementów
            head = (1, 1)  # head 1 stanie się None gdy nie bedzie juz elementow do sortowania
            result = new_ll
            while head[1]:
                head = merge_part(mid, c, n)
                mid = find_middle(head[0])
                # funkcja find middle w istocie zwróci środkowy czyli k+1 element, ale on jest juz dobrze posortowany
                # zatem przechodze do kolejnego elementu
                mid = mid.next

                # poprzeninianie otrzymywanych resultatów w 1 spójny wynik
                new_ll.next = head[0]
                for j in range(0, k+1):
                    new_ll = new_ll.next

                # przepięcie ostatniego elementu mida na pierwszy element nie posortowanej listy
                mid_last = find_last(mid)
                mid_last.next = head[1]
                c += k+1

    return result.next

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )

"""
Komentarz do złożoności czasowej:
Dla k=0 zlożoność Θ(1)
Dla k=1 złożoność Θ(n)
Dla k>1:
Merge sortujemy n/(k+1) zaokrąglone w góre przedziałów z których każdy(dokładniej każdy poza ostatnim choć czasem ten też,
ale nie zmienia to wyniku więc nie ma to specjalnego znaczenia) jest wielkośći 2k+1 zatem złożonośc ma postać
(n/(k+1))*(2k+1)log(2k+1) < (n/(k+1))*(2k+2)log(2k+1) = (2n+2)log(2k+1) co oznacza, że w notacji theta ma ona
postać Θ(nlogk) 
"""
