# Circular Single Linked List - Josephus problem - step size = 1 2 3 4 = 1 3 4 = 1 3 = 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove_node(self, node):
        if self.head == node:
            # we are going to move forwared with cur.next in list till we reach head of list
            cur == self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next  # this is when it comes to B
            self.head = self.head.next  # now B is our head of list
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        cur = self.head
        while len(self) > 1:  # while length of list of more than one
            count = 1
            while count != step:  # while count is not equal to step size
                cur = cur.next
                count += 1
            print("Removed: " + str(cur.data)) # this will give us the sequence of removed data i.e. 2 4 3
            self.remove_node(cur)  # removed 2 in first loop
            cur = cur.next  # so now again started from the 3 as this is next to 2


cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

cllist.remove_node(cllist.head)
cllist.josephus_circle(2)
cllist.print_list()
