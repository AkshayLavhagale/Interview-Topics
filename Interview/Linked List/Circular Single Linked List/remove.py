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

    def remove(self, key):
        if self.head.data == key:
            cur == self.head # we are going to move forwared with cur.next in list till we reach head of list
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next # this is when it comes to B 
            self.head = self.head.next # now B is our head of list
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur =  cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next


cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")

cllist.remove("B")
cllist.print_list() 
