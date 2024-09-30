a = [7, 9, 1, 5, 8, 6, 2, 12]
n = len(a)
print(n)
k = 4
p = 5
print(a)
suma = 0
start = n-k
for i in range(0, n-p+1):
    b = sorted(a[i:i+p])
    print(a, b)
    suma += b[p-k]

print(suma)

"""v2"""

class Node:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

class listalinkowana:
    def __init__(self):
        self.head = None

    def sort_append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            current = self.head
            prev = None
            Next = None
            while current is not None:
                if current.val is not None:
                    if data > current.val:
                        prev = current
                        Next = current.next
                    current = current.next

            if prev is not None:
                new_node = Node(data, Next)
                prev.next = new_node
            if prev is None:
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node

    def delete(self, key):
        if key == self.head:
            self.head = self.head.next
        else:
            prev = self.head
            nh = prev
            curr = prev.next
            while curr.next is not None:
                if curr.val == key:
                    prev.next = curr.next
                    self.head = nh
                    break
                prev = curr
                curr = curr.next
                if not curr.next and curr.val == key:
                    prev.next = curr.next
                    self.head = nh
                    break


def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next


ll = listalinkowana()
ll.sort_append(-999)

for i in range(0, n-p+2):
    ll.sort_append(a[i])

#printList(ll.head)
#print()

suma = 0
del_next = a[0]
del_in = 0
app_next = a[p]
app_in = p

for i in range(0, n-p+1):
    first = ll.head
    for i in range(p-k+1):
        first = first.next
        if i==p-k:
            suma += first.val
            #print(suma)
    first = ll.head.next

    ll.delete(del_next)
    ll.sort_append(app_next)

    del_in += 1
    app_in += 1
    #printList(ll.head)
    #print()
    del_next = a[del_in]
    if app_in<n:
        app_next = a[app_in]

print(suma)

"""v3
opis rozwo generalnie jak v1, ale nie sortuje ponownie fragmentu a tylko naprawia dopisuje do b element, ale w sumie
nie widze rozwa na to bez uzycia linked list jak teraz mysle
"""
a = [7, 9, 1, 5, 8, 6, 2, 12]
n = len(a)
print(n)
k = 4
p = 5
print(a)
suma = 0
start = n-k
b = sorted(a[:p])
add_in = p
for i in range(0, n-p+1):

    print(a, b)
    b.append(a[p])

print(suma)
