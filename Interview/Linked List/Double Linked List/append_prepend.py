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


dllist = DoubleLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.print_list()
