class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def mergeSort(head, end):
    if head == end:
        return head

    # Podział listy na dwie części
    mid = findMiddle(head, end)
    mid_next = mid.next

    # Rekurencyjne sortowanie obu połówek
    left_sorted = mergeSort(head, mid)
    right_sorted = mergeSort(mid_next, end)

    # Scalanie posortowanych połówek
    return merge(left_sorted, right_sorted)


def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    if left:
        current.next = left
    elif right:
        current.next = right

    return dummy.next


def findMiddle(start, end):
    slow = start
    fast = start
    while fast != end and fast.next != end:
        slow = slow.next
        fast = fast.next.next
    return slow


def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


# Przykładowe użycie
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

print("Lista przed sortowaniem:")
printList(head)

# Definiujemy wskaźniki na początek i koniec fragmentu do posortowania
start = head
end = head.next.next

# Sortujemy fragment listy
sorted_fragment = mergeSort(start, end)

print("Lista po sortowaniu fragmentu:")
printList(sorted_fragment)

# Wyświetlamy całą listę, aby sprawdzić, czy fragment został posortowany
print("Lista po sortowaniu:")
printList(head)