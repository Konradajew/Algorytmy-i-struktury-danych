import random


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def generate_ll(n):
    head = Node()
    new_node = Node()
    head.next = new_node
    for i in range(0, n):
        new_node.val = random.randint(1, 100)
        new_node2 = Node()
        if i != n - 1:
            new_node.next = new_node2
            new_node = new_node.next
    return head.next


#merge sort z chata, ale huj
def findLast(head):
    while head:
        if head.next is None:
            return head
        head = head.next

def mergefrag(head, l, c, n):
    if l + c >= n:
        return [mergeSort(head), None]
    first = head
    for i in range(0, l-1):
        head = head.next
    new = head.next
    head.next = None
    head = mergeSort(first)
    return [head, new]


def mergeSort(head):
    if not head or not head.next:
        return head

    # Podział listy na dwie części
    mid = findMiddle(head)
    mid_next = mid.next
    mid.next = None

    # Rekurencyjne sortowanie obu połówek
    left_sorted = mergeSort(head)
    right_sorted = mergeSort(mid_next)

    # Scalanie posortowanych połówek
    return merge(left_sorted, right_sorted)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.val < right.val:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result


def findMiddle(head):
    if not head:
        return None
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def printList(node):
    c = 0
    while node:
        print(node.val, end=" ")
        node = node.next
        c+=1
    print()
    print(c)


# Przykładowe użycie
k = 7
first = generate_ll(22)
#print("Lista przed sortowaniem:")
#printList(first)

p = first
n = 0
while p is not None:
    n += 1
    p = p.next
print(n)


if k == 1:
    wart = Node()
    wart.next = first
    prev = wart
    printList(first)
    while first.next is not None:
        if first.val > first.next.val:
            temp = first.next.next
            prev.next = first.next
            first.next.next = first
            first.next = temp
        prev = first
        first = first.next
        if first is None:
            break

    printList(wart.next)

else:

    if k > n:
        head = mergeSort(first)
        printList(head)

    #print("fiutini")
    mid = first
    nl = Node()
    c = 0
    st = nl
    head = (1, 1)
    while head[1]:
        head = mergefrag(mid, 2 * k + 1, c, n)

        mid = findMiddle(head[0])
        print("pp", end=" ")
        printList(head[0])

        mid = mid.next

        nl.next = head[0]
        for j in range(0, k+1):
            nl = nl.next
        #printList(st)

        #printList(mid)
        mid_last = findLast(mid)
        mid_last.next = head[1]
        print("po przep", end=" ")
        printList(head[0])

        print("od mida", end=" ")
        printList(mid)
        print()
        c += k+1

    printList(st.next)

if None:
    print("haksiusiak")