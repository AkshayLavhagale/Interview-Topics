class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend_list(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head  # as we are prepending the new node is set to head
        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur = cur.next
        self.head = new_node

    def append_list(self, data):
        if not self.head:  # if there is no node in the list
            self.head = Node(data)
            self.head.next = self.head  # in single linked list next point of head point to itself
        else:  # if there is already data in list then
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            # now the last node D is pointed to A(head)
            new_node.next = self.head

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break


cllist = CircularLinkedList()
cllist.append_list("C")
cllist.append_list("D")
cllist.prepend_list("B")
cllist.prepend_list("A")
cllist.print_list()
