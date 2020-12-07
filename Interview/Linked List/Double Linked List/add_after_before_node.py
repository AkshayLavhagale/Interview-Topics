# Double linked list - NoneABCDNone = NoneABECDNone - After key B adding data E
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    # intially equals to None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:  # if there are no node in list
            new_node = Node(data)  # then we are creating new node
            # we are referring the previous node to None = None<-A as this is Double linked list
            new_node.prev = None
            self.head = new_node  # as the added new node is the only node it is assigned as head
        else:  # if there are already node and we want to append in it
            new_node = Node(data)  # creating the new node
            cur = self.head  # we start with the head node and then traverse through link till we reach last node
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur  # current is last node
            new_node.next = None  # D points to None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur.next:
            # if there is only one node is present in the list and the data in it is the key
            if cur.next is None and cur.data == key:
                self.append(data)  # then we are appending the data directly
                return
            elif cur.data == key:  # here the current data is B
                new_node = Node(data)  # we created the E
                nxt = cur.next
                cur.next = new_node  # then instead of B to C it refer to B to E
                new_node.next = nxt  # now E refers to C
                new_node.prev = cur  # now previous of E refers to B
                nxt.prev = new_node  # now previous of C refers to E
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur.next:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                pre = cur.prev
                cur.prev = new_node
                new_node.next = pre
                new_node.next = cur
                pre.next = new_node
            cur = cur.next


dllist = DoubleLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.add_after_node(1, 11)
dllist.add_before_node(3, 12)

dllist.print_list()
