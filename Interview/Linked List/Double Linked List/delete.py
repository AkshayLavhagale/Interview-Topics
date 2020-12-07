# Double linked list - Delete the node
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

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1 - if there is just one node in list
                if not cur.next:  # if the current node not pointing to Node, that means it is the last node
                    cur = None
                    self.head = None  # we deleted the only node present in the list
                    return
                # Case 2 - we have more than one node, there are two node None A->B None
                else:
                    nxt = cur.next
                    cur.next = None
                    cur.prev = None
                    nxt.prev = None
                    cur = None  # removing the A
                    self.head = nxt  # now B is the head of the list
                    return
                # Case 3 - deleting the node where cur.next is not None. Means deleting the in between nodes
            elif cur.data == key:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt  # here from the ABC we removed the B and remained is AC
                    nxt.prev = prev  # now from C to A we are referrring
                    cur.next = None
                    cur.prev = None  # removing the pointers to B
                    cur = None
                    return
                # Case 4 - removing the node which have cur.next is None i.e. D
                else:
                    prev = cur.prev  # prev is C
                    prev.next = None
                    cur.prev = None  # we are removing the reference from D so the prev is not required
                    cur = None
                    return
            # we are getting out of loop (keeping in while loop) and removing current point of head through the rest of list
            cur = cur.next


dllist = DoubleLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.delete(1)
dllist.print_list()
