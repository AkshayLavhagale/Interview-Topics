# Double linked list - pairs with sum e.g. 2 + 3 = 5 and 4 + 1 = 5
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    # intially equals to None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def pairs_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next  # else statement
            p = p.next  # once we are outside of q we go on with next p

        return pairs


# (1, 2), (1, 3), (1, 4), (1, 5)
# (2, 3), (2, 4), (2, 5)
# (3, 4), (3, 5)
# (4, 5)

dllist = DoubleLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)

print(dllist.pairs_with_sum(5))
# print(dllist.pairs_with_sum(0))
