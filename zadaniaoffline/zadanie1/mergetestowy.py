array = [1, 3, 0, 5, 2, 4, 6, 9, 7, 8]

class Node:
  def __init__(self):
    self.val = None
    self.next = None

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

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


for i in range(0, 10, 3):
    new_array = array[i:i+5]
    mergesort(new_array)
    print(new_array)
    array[i:i+5] = new_array
    print(array[i:i+5], array)
    print(i)

head = Node()
new_node = Node()
head.next = new_node
for i in range(0, len(array)):
    new_node.val = array[i]
    if i != len(array) - 1:
        newer_node = Node()
        new_node.next = newer_node
        new_node = new_node.next

printList(head.next)
